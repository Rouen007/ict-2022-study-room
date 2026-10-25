import Foundation
import CryptoKit
import CoreFoundation
import Darwin

struct NotebookFailure: LocalizedError {
    let message: String
    var errorDescription: String? { message }
}

struct NotebookSnapshot {
    let value: [String: Any]?
    let token: String
}

// One authoritative file, with content-token compare-and-swap across app instances.
final class NotebookStore {
    let directory: URL
    var fileURL: URL { directory.appendingPathComponent("notebook.json") }
    let maxBytes = 16 * 1024 * 1024
    private let requireExistingDirectory: Bool
    init(directory: URL, requireExistingDirectory: Bool = false) {
        self.directory = directory
        self.requireExistingDirectory = requireExistingDirectory
    }

    private func checkDirectory() throws {
        guard requireExistingDirectory else { return }
        var isDirectory: ObjCBool = false
        guard FileManager.default.fileExists(atPath: directory.path, isDirectory: &isDirectory), isDirectory.boolValue else {
            throw NotebookFailure(message: "正式笔记目录不可用：\(directory.path)。已停止写入，未切换到空白目录；请恢复该目录或迁移笔记后重新配置。")
        }
    }

    private func integer(_ value: Any?) -> Int? {
        guard let number = value as? NSNumber,
              CFGetTypeID(number) != CFBooleanGetTypeID(),
              number.doubleValue.isFinite,
              number.doubleValue.rounded(.towardZero) == number.doubleValue,
              abs(number.doubleValue) <= 9_007_199_254_740_991 else { return nil }
        return number.intValue
    }

    func validate(_ data: Data) throws -> [String: Any] {
        guard data.count <= maxBytes,
              let object = try JSONSerialization.jsonObject(with: data) as? [String: Any],
              object["schema"] as? String == "ict-2022-study",
              let version = integer(object["version"]), version == 1,
              object["summaryNote"] is String else {
            throw NotebookFailure(message: "笔记格式无效或版本不支持；原文件保持不变，请导出当前编辑并检查备份。")
        }
        for key in ["lessonNotes", "answers", "mistakes", "checklist"] {
            guard object[key] is [String: Any] else { throw NotebookFailure(message: "笔记字段无效：\(key)") }
        }
        for key in ["completedLessons", "completedBatches", "attemptHistory", "journalEntries"] {
            guard object[key] is [Any] else { throw NotebookFailure(message: "笔记字段无效：\(key)") }
        }
        if let revision = object["revision"], integer(revision) == nil || (integer(revision) ?? -1) < 0 || (integer(revision) ?? Int.max) >= 9_007_199_254_740_991 {
            throw NotebookFailure(message: "笔记 revision 无效")
        }
        guard (object["lessonNotes"] as? [String: Any] ?? [:]).values.allSatisfy({ $0 is String }),
              object["completedLessons"] is [String], object["completedBatches"] is [String],
              object["journalEntries"] is [[String: Any]], object["attemptHistory"] is [[String: Any]],
              let answers = object["answers"] as? [String: [String: Any]],
              answers.values.allSatisfy({ answer in
                  (answer["reason"] == nil || answer["reason"] is String) &&
                  (answer["action"] == nil || answer["action"] is String)
              }) else { throw NotebookFailure(message: "笔记条目格式异常，已阻止覆盖；请检查备份或导出后修复。") }
        return object
    }

    private func diskData() throws -> Data? {
        if !FileManager.default.fileExists(atPath: fileURL.path) { return nil }
        let size = try fileURL.resourceValues(forKeys: [.fileSizeKey]).fileSize ?? 0
        guard size <= maxBytes else { throw NotebookFailure(message: "笔记文件超过大小上限，已停止自动写入。") }
        return try Data(contentsOf: fileURL)
    }

    private func token(_ data: Data?) -> String {
        guard let data = data else { return "missing" }
        return SHA256.hash(data: data).map { String(format: "%02x", $0) }.joined()
    }

    func load() throws -> NotebookSnapshot {
        try checkDirectory()
        let data = try diskData()
        return NotebookSnapshot(value: try data.map(validate), token: token(data))
    }

    func save(payload: Data, expectedToken: String) throws -> NotebookSnapshot {
        var object = try validate(payload)
        try checkDirectory()
        try FileManager.default.createDirectory(at: directory, withIntermediateDirectories: true)
        let lockURL = directory.appendingPathComponent(".notebook.lock")
        let fd = Darwin.open(lockURL.path, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR)
        guard fd >= 0 else { throw NotebookFailure(message: "无法锁定笔记文件") }
        defer { Darwin.close(fd) }
        guard flock(fd, LOCK_EX | LOCK_NB) == 0 else { throw NotebookFailure(message: "另一实例正在保存，请稍后重试。") }
        defer { flock(fd, LOCK_UN) }
        let oldData = try diskData()
        guard token(oldData) == expectedToken else {
            throw NotebookFailure(message: "笔记已被其他实例或外部编辑更新。已阻止覆盖；请导出当前编辑，重新载入后合并。")
        }
        let oldObject = try oldData.map(validate)
        object["revision"] = (oldObject?["revision"] as? Int ?? 0) + 1
        let data = try JSONSerialization.data(withJSONObject: object, options: [.prettyPrinted, .sortedKeys])
        guard data.count <= maxBytes else { throw NotebookFailure(message: "笔记超过大小上限") }
        // Preserve the previous valid bytes BEFORE replacing the authoritative file.
        let history = directory.appendingPathComponent("history", isDirectory: true)
        try FileManager.default.createDirectory(at: history, withIntermediateDirectories: true)
        let id = UUID().uuidString
        if let previous = oldData {
            try previous.write(to: history.appendingPathComponent("notebook-before-\(id).json"), options: .atomic)
        }
        try data.write(to: history.appendingPathComponent("notebook-saved-\(id).json"), options: .atomic)
        try data.write(to: fileURL, options: .atomic)
        return NotebookSnapshot(value: object, token: token(data))
    }
}
