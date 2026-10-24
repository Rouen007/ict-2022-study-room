# ICT 2022 学习室 App 架构与维护规范

> **Created by Xiao Ang** · 对应 `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room` 与 `/Users/rouen/Desktop/ICT 2022 学习室.app`。

---

## 一、目录与数据流架构

```text
ict-2022-mentorship/
├── SKILL.md                          # Agent Skill 主入口
├── agents/openai.yaml                # Codex / OpenAI Agent 声明
├── references/                       # Skill 按需加载参考文档
├── courseData.json                   # 37 讲元数据、时间轴节点、关键帧与术语源数据
├── build_course_data.py              # 生成 courseData.json 的脚本
├── build_study_room.py               # 生成 study-room 三大 JS 数据包的核心构建器
├── ICT_2022_全37讲_图文精读手册.md   # 全 37 讲深度中文讲义源文档（含 62+ 关键帧图解与全模块拆解）
├── transcripts/                      # 全 37 集清洗后逐分钟英文原稿 (01_*.md - 37_*.md)
└── study-room/                       # 学习室前端与 macOS 原生封装目录
    ├── index.html                    # 6 大学习模块主页面
    ├── style.css / distill.css       # 纸感墨绿主题与三层提炼样式
    ├── app.js / distill.js           # 交互逻辑、双端外链跳帧与本地存储桥接
    ├── distill-data.js               # [自动生成] window.LESSON_DISTILL (6步链路 + 12原则 + 37集提炼卡)
    ├── library-data.js               # [自动生成] window.ANG_LIBRARY (37集完整图文 HTML + 逐分钟原稿)
    ├── course.js                     # [自动生成] window.STUDY_COURSE (每次3题引导练习)
    ├── lesson-assets/                # 1080p 原片关键帧截图 (*.png)
    ├── notebook.json                 # [运行时落盘] 用户笔记、练习记录与 Ep.04 复盘手帐
    ├── history/                      # [运行时落盘] 按分钟防丢快照 (notebook-yyyyMMdd-HHmm.json)
    └── native/
        ├── App.swift                 # Cocoa + WKWebView 原生容器（含 --qa 自动体检与外链系统级拦截）
        ├── Icon.swift                # 深曜石蓝黑 + 香槟金 FVG 专属图标生成器
        ├── Info.plist                # local.rouen.ict2022study
        └── build.sh                  # 一键编译、签名并输出至 ~/Desktop/ICT 2022 学习室.app
```

---

## 二、修改与重建标准流程

1. **修改数据或讲义内容时**：
   - 不要直接手改生成的 `study-room/distill-data.js`、`study-room/library-data.js` 或 `study-room/course.js`，应修改 `build_course_data.py`、`build_study_room.py` 或 `ICT_2022_Ep01_05_图文精读手册.md`，然后运行：
     ```bash
     cd /Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship
     python3 build_course_data.py
     python3 build_study_room.py
     ```
2. **语法与原生 `--qa` 校验**：
   ```bash
   node --check study-room/distill.js && node --check study-room/app.js
   killall ICT2022Study || true
   ./study-room/native/build.sh
   "/Users/rouen/Desktop/ICT 2022 学习室.app/Contents/MacOS/ICT2022Study" --qa
   open "/Users/rouen/Desktop/ICT 2022 学习室.app"
   ```
   - **注意**：macOS 对已运行的应用执行 `open` 只会切到旧进程前台，不会重新加载新二进制文件；因此每次重编译后必须先 `killall ICT2022Study || true` 再 `open`。

---

## 三、增量补齐后续集数（Ep.06–Ep.37）1080p 关键帧流程

为了保持本地与 GitHub 仓库轻量（不留存几百 MB 的 `.mp4` 视频文件），扩充后续集数截图时严格遵循 **「临时拉流 → 截帧核验 → 即刻删流」**：

1. 阅读 `transcripts/{ep}_*.md`，找出 ICT 在图上讲解关键结构（如 Daily Bias、Power of 3 / AMD、London/NY 扫损、SMT 背离、FVG/OB 进场）的精确时间戳。
2. 临时拉取该集 1080p 视频流到 `/tmp/ep{ep}.mp4`：
   ```bash
   yt-dlp -f "bestvideo[height<=1080][ext=mp4]" -o "/tmp/ep{ep}.mp4" "https://www.youtube.com/watch?v={videoId}"
   ```
3. 使用 `ffmpeg -ss {MM:SS} -i /tmp/ep{ep}.mp4 -frames:v 1 -q:v 2 study-room/lesson-assets/ep{ep}_{slug}.png` 截取高清帧，并用看图工具逐张确认文字批注与 K 线清晰无误。
4. **立即删除临时视频**：`rm -f /tmp/ep{ep}.mp4`。
5. 将新截图信息加入 `build_course_data.py` 与 `build_study_room.py` 的提炼卡片中，重新生成并编译 App。
