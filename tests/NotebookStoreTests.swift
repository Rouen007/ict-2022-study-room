import Foundation

@main
struct NotebookStoreTests {
    static func check(_ value: Bool) { precondition(value) }
    static func main() throws {
        let root = FileManager.default.temporaryDirectory.appendingPathComponent("ict-store-test-\(UUID().uuidString)")
        let store = NotebookStore(directory: root)
        let payload: [String:Any] = ["schema":"ict-2022-study", "version":1,"summaryNote":"one", "lessonNotes":[:],"answers":[:],"mistakes":[:],"checklist":[:],"completedLessons":[],"completedBatches":[],"attemptHistory":[],"journalEntries":[]]
        let data = try JSONSerialization.data(withJSONObject: payload)
        check(try store.load().token == "missing")
        let first = try store.save(payload: data, expectedToken: "missing")
        assert(first.value?["revision"] as? Int == 1)
        let firstBytes = try Data(contentsOf: store.fileURL)
        var changed = payload
        changed["summaryNote"] = "two"
        let second = try store.save(payload: JSONSerialization.data(withJSONObject: changed), expectedToken: first.token)
        assert(second.value?["revision"] as? Int == 2)
        check(try store.load().value?["summaryNote"] as? String == "two")
        do { _ = try store.save(payload: data, expectedToken: first.token); fatalError("stale write accepted") } catch {}
        check(try store.load().value?["summaryNote"] as? String == "two")
        let history = try FileManager.default.contentsOfDirectory(at: root.appendingPathComponent("history"), includingPropertiesForKeys:nil)
        assert(history.count == 3)
        check(try history.contains { try Data(contentsOf: $0) == firstBytes })
        do { _ = try store.save(payload: Data("not json".utf8), expectedToken: second.token); fatalError("invalid payload accepted") } catch {}
        for (field, value) in [("version", true as Any), ("revision", true as Any), ("lessonNotes", ["03": 42] as Any), ("journalEntries", [NSNull()] as Any)] {
            var invalid = payload
            invalid[field] = value
            let bytes = try JSONSerialization.data(withJSONObject: invalid)
            do { _ = try store.save(payload: bytes, expectedToken: second.token); fatalError("invalid nested data accepted: \(field)") } catch {}
            check(try store.load().value?["summaryNote"] as? String == "two")
        }
        let bound = NotebookStore(directory: root, requireExistingDirectory: true)
        check(try bound.load().value?["summaryNote"] as? String == "two")
        let moved = root.appendingPathExtension("moved")
        try FileManager.default.moveItem(at: root, to: moved)
        do { _ = try bound.load(); fatalError("missing bound directory silently accepted") } catch {}
        do { _ = try bound.save(payload:data, expectedToken:second.token); fatalError("missing bound directory recreated") } catch {}
        check(!FileManager.default.fileExists(atPath:root.path))
        try FileManager.default.moveItem(at:moved,to:root)
        check(try bound.load().value?["summaryNote"] as? String == "two")
        let external = Data("{\"broken\": true}".utf8)
        try external.write(to: store.fileURL)
        do { _ = try store.load(); fatalError("invalid notebook accepted") } catch {}
        do { _ = try store.save(payload:data,expectedToken:second.token); fatalError("corrupt file overwritten") } catch {}
        check(try Data(contentsOf:store.fileURL) == external)
        print("NotebookStore checks passed: revisions, stale writes, snapshots, invalid JSON, corrupt file protection. Fixtures retained: \(root.path)")
    }
}
