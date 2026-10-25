import Cocoa
import WebKit

final class AppDelegate: NSObject, NSApplicationDelegate, WKNavigationDelegate, WKScriptMessageHandler {
    private var window: NSWindow!
    private var webView: WKWebView!
    private let qaMode = CommandLine.arguments.contains("--qa")
    private var qaStage = 0
    private var terminating = false
    private var terminationTimeout: DispatchWorkItem?
    private lazy var studyRootURL: URL = {
        if !qaMode, let path = Bundle.main.object(forInfoDictionaryKey: "StudyRootPath") as? String,
           FileManager.default.fileExists(atPath: path + "/index.html") {
            return URL(fileURLWithPath: path, isDirectory: true)
        }
        return Bundle.main.resourceURL!
    }()
    private var configuredDataPath: String? {
        (Bundle.main.object(forInfoDictionaryKey: "StudyDataPath") as? String)
            ?? (Bundle.main.object(forInfoDictionaryKey: "StudyRootPath") as? String)
    }
    private lazy var dataRootURL: URL = {
        if qaMode {
            return FileManager.default.temporaryDirectory.appendingPathComponent("ict-qa-\(UUID().uuidString)", isDirectory: true)
        }
        if let path = configuredDataPath {
            return URL(fileURLWithPath: path, isDirectory: true)
        }
        return FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask).first!
            .appendingPathComponent("ICT2022Study", isDirectory: true)
    }()
    private lazy var store = NotebookStore(directory: dataRootURL, requireExistingDirectory: !qaMode && configuredDataPath != nil)
    private var indexURL: URL { studyRootURL.appendingPathComponent("index.html").resolvingSymlinksInPath() }

    func applicationDidFinishLaunching(_ notification: Notification) {
        let screen = NSScreen.main?.visibleFrame ?? NSRect(x: 0, y: 0, width: 1440, height: 920)
        window = NSWindow(contentRect: NSRect(x: screen.minX + 40, y: screen.minY + 40,
                            width: min(1440, screen.width - 80), height: min(920, screen.height - 80)),
                          styleMask: [.titled, .closable, .miniaturizable, .resizable], backing: .buffered, defer: false)
        window.title = "ICT 2022 学习室 · Created by Xiao Ang"
        window.minSize = NSSize(width: 980, height: 650)
        let controller = WKUserContentController()
        for name in ["saveNotebook", "reloadPage", "copyText", "openExternalURL", "terminationReady", "exportNotebook"] {
            controller.add(self, name: name)
        }
        let config = WKWebViewConfiguration()
        config.userContentController = controller
        if qaMode { config.websiteDataStore = .nonPersistent() }
        webView = WKWebView(frame: window.contentView!.bounds, configuration: config)
        webView.autoresizingMask = [.width, .height]
        webView.navigationDelegate = self
        window.contentView = webView
        loadStudyPage()
        if qaMode {
            DispatchQueue.main.asyncAfter(deadline: .now() + 25) { self.finishQA(false, "页面或保存验证超时") }
        } else {
            window.makeKeyAndOrderFront(nil)
            NSApp.activate(ignoringOtherApps: true)
        }
    }

    private func loadStudyPage() {
        var boot: [String: Any] = ["qa": qaMode, "storageID": dataRootURL.path]
        do {
            let snapshot = try store.load()
            boot["notebook"] = snapshot.value ?? NSNull()
            boot["token"] = snapshot.token
        } catch {
            boot["error"] = error.localizedDescription
            boot["token"] = "invalid"
        }
        let data = try! JSONSerialization.data(withJSONObject: boot, options: [.sortedKeys])
        // JSON travels as base64 UTF-8, never as executable source from notebook bytes.
        let script = "window.nativeBoot = JSON.parse(new TextDecoder().decode(Uint8Array.from(atob('\(data.base64EncodedString())'), c => c.charCodeAt(0))));"
        let controller = webView.configuration.userContentController
        controller.removeAllUserScripts()
        controller.addUserScript(WKUserScript(source: script, injectionTime: .atDocumentStart, forMainFrameOnly: true))
        let readRoot = studyRootURL.resolvingSymlinksInPath().standardizedFileURL
        if qaMode { print("QA_LOAD: index=\(indexURL.path); root=\(readRoot.path); exists=\(FileManager.default.fileExists(atPath:indexURL.path))"); fflush(stdout) }
        webView.loadFileURL(indexURL, allowingReadAccessTo: readRoot)
    }

    private func trusted(_ message: WKScriptMessage) -> Bool {
        guard message.frameInfo.isMainFrame, let url = message.frameInfo.request.url, url.isFileURL else { return false }
        return url.resolvingSymlinksInPath().path == indexURL.path
    }

    private func callback(_ object: [String: Any]) {
        guard let data = try? JSONSerialization.data(withJSONObject: object), let text = String(data: data, encoding: .utf8) else { return }
        webView.evaluateJavaScript("window.onNativeNotebookSaved && window.onNativeNotebookSaved(\(text))", completionHandler: nil)
    }

    private func allowedExternal(_ url: URL) -> Bool {
        guard url.scheme?.lowercased() == "https", let host = url.host?.lowercased() else { return false }
        return ["youtube.com", "www.youtube.com", "youtu.be", "www.bilibili.com", "bilibili.com", "github.com", "www.nyse.com", "nyse.com"].contains(host)
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        guard trusted(message) else { return }
        switch message.name {
        case "saveNotebook":
            guard let body = message.body as? [String: Any], let id = body["requestId"] as? String,
                  id.count <= 100, let token = body["expectedToken"] as? String,
                  let payload = body["payload"] as? String, let data = payload.data(using: .utf8) else { return }
            do {
                let result = try store.save(payload: data, expectedToken: token)
                callback(["ok": true, "requestId": id, "token": result.token, "revision": result.value?["revision"] ?? 0])
            } catch {
                callback(["ok": false, "requestId": id, "error": error.localizedDescription])
            }
        case "reloadPage": loadStudyPage()
        case "exportNotebook":
            if !qaMode, let text = message.body as? String, let data = text.data(using: .utf8), data.count <= store.maxBytes {
                let panel = NSSavePanel()
                panel.nameFieldStringValue = "ict-notebook-export.json"
                panel.beginSheetModal(for: window) { response in
                    guard response == .OK, let url = panel.url else { return }
                    do { try data.write(to: url, options: .atomic) }
                    catch { let alert = NSAlert(error: error); alert.runModal() }
                }
            }
        case "copyText":
            if let text = message.body as? String, text.utf8.count <= store.maxBytes {
                NSPasteboard.general.clearContents()
                NSPasteboard.general.setString(text, forType: .string)
            }
        case "openExternalURL":
            if !qaMode, let text = message.body as? String, let url = URL(string: text), allowedExternal(url) { NSWorkspace.shared.open(url) }
        case "terminationReady":
            guard terminating else { return }
            terminationTimeout?.cancel()
            terminating = false
            let ok = (message.body as? [String: Any])?["ok"] as? Bool ?? false
            if ok { NSApp.reply(toApplicationShouldTerminate: true) }
            else {
                window.makeKeyAndOrderFront(nil)
                let alert = NSAlert()
                alert.messageText = "笔记保存尚未完成"
                alert.informativeText = "建议继续编辑并导出当前笔记。强制退出可能丢失尚未导出的编辑。"
                alert.addButton(withTitle: "继续编辑并导出")
                alert.addButton(withTitle: "仍然退出")
                NSApp.reply(toApplicationShouldTerminate: alert.runModal() == .alertSecondButtonReturn)
            }
        default: break
        }
    }

    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
        guard let url = navigationAction.request.url else { decisionHandler(.cancel); return }
        if url.isFileURL, url.resolvingSymlinksInPath().path == indexURL.path,
           navigationAction.targetFrame?.isMainFrame == true {
            decisionHandler(.allow); return
        }
        if !qaMode, navigationAction.navigationType == .linkActivated, allowedExternal(url) { NSWorkspace.shared.open(url) }
        decisionHandler(.cancel)
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        guard qaMode else { return }
        let stage = qaStage
        let js = """
        (async () => {
          if (window.ANG_LIBRARY?.lessons?.length !== 37 || document.querySelectorAll('.lesson-item').length !== 37 || document.querySelectorAll('.q-card').length !== 3) throw Error('课程或题库数量错误');
          const macroCount = window.LESSON_DISTILL?.framework?.extensions?.macros?.length || 0;
          if (document.querySelectorAll('#frameworkExtensions [data-macro-id]').length !== macroCount) throw Error('扩展观察窗口未显示');
          const sources = [...new Set(window.ANG_LIBRARY.lessons.flatMap(l => (l.keyframes || []).map(f => 'lesson-assets/' + f.file)))];
          if (sources.length !== window.ANG_LIBRARY.imageCount || sources.length < 62) throw Error('关键帧清单数量不完整');
          await Promise.all(sources.map(src => new Promise((resolve, reject) => { const img = new Image(); img.onload = () => img.naturalWidth > 0 ? resolve() : reject(Error(src)); img.onerror = () => reject(Error(src)); img.src = src; })));
          if (\(stage) > 0 && state.summaryNote !== 'qa-note-' + \(stage)) throw Error('重载未恢复最新笔记');
          if (\(stage) < 2) {
            state.summaryNote = 'qa-note-' + (\(stage) + 1);
            if (!await saveState({ immediate: true })) throw Error('原生保存未确认');
          }
          return { lessons: 37, images: sources.length, macroWindows: macroCount, reloadStage: \(stage) };
        })()
        """
        webView.callAsyncJavaScript("return await \(js)", arguments: [:], in: nil, in: .page) { result in
            switch result {
            case .failure(let error): self.finishQA(false, error.localizedDescription)
            case .success(let value):
                if stage < 2 { self.qaStage += 1; self.loadStudyPage() }
                else { self.finishQA(true, "\(value); resources=\(self.studyRootURL.path); isolatedData=\(self.dataRootURL.path)") }
            }
        }
    }

    private func finishQA(_ ok: Bool, _ detail: String) {
        fputs("\(ok ? "QA_OK" : "QA_ERROR"): \(detail)\n", ok ? stdout : stderr)
        fflush(stdout); fflush(stderr)
        exit(ok ? 0 : 1)
    }
    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) { if qaMode { finishQA(false, error.localizedDescription) } }
    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) { if qaMode { finishQA(false, error.localizedDescription) } }
    func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply {
        if qaMode { return .terminateNow }
        if terminating { return .terminateLater }
        terminating = true
        webView.evaluateJavaScript("flushNativeNotebook().then(ok => window.webkit.messageHandlers.terminationReady.postMessage({ok}))") { _, error in
            if error != nil && self.terminating { self.terminating = false; NSApp.reply(toApplicationShouldTerminate: false) }
        }
        let timeout = DispatchWorkItem {
            if self.terminating { self.terminating = false; NSApp.reply(toApplicationShouldTerminate: false) }
        }
        terminationTimeout = timeout
        DispatchQueue.main.asyncAfter(deadline: .now() + 8, execute: timeout)
        return .terminateLater
    }
    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool { true }
}

@main
struct StudyAppMain {
    static func main() {
        let app = NSApplication.shared
        let delegate = AppDelegate()
        app.setActivationPolicy(.regular)
        app.delegate = delegate
        app.run()
    }
}
