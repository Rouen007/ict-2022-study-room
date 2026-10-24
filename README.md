# ICT 2022 学习室 (ICT 2022 Mentorship Study Room)

> **Created by Xiao Ang** · 针对 **2022 ICT Mentorship [No Rant]** 全 37 集课程打造的本地双语精读与交互训练系统（支持零依赖浏览器直开 & 原生 macOS 桌面应用 `ICT 2022 学习室.app`）。

## 🚀 快速上手（其他人 Clone 后可直接使用）

```bash
git clone https://github.com/Rouen007/ict-2022-study-room.git
cd ict-2022-study-room
```

### 方式一：直接用浏览器打开（跨平台 · 零编译）
所有课程数据（`distill-data.js`、`library-data.js`、`course.js`）与全 37 讲 62+ 张 1080p 原片关键帧高清截图均已打包在 `study-room/` 内，直接双击或命令行打开即可使用（笔记自动保存在浏览器 `localStorage`，所有时间戳支持点击一键直达 YouTube 原片 / B站中配对应秒数）：

```bash
open study-room/index.html
```

### 方式二：一键编译原生 macOS 桌面应用 (`ICT 2022 学习室.app`)
在 macOS 上运行以下命令，自动通过系统自带 `swiftc` 编译并签名至你的桌面 `~/Desktop/ICT 2022 学习室.app`（支持本地 `notebook.json` + `history/` 按分钟快照防丢落盘）：

```bash
./study-room/native/build.sh
open "$HOME/Desktop/ICT 2022 学习室.app"
```

---

## 📦 核心功能模块 (`study-room/`)

1. **01 指导课堂**：全 37 讲三层提炼卡片（`S1–S6` 交易链路 + `P01–P12` 可迁移原则）+ **全 37 讲 62+ 张 1080p 原片关键帧逐图精读与六大模块完整图文深度讲义** + 全 37 集逐分钟英文原稿与时间戳双向直达（YouTube 原片 / B站中配）。
2. **02 多周期图谱 & 视频直达**：原片 YouTube / B站中配秒级双直达 + `1W → 1D → 1H → 15m → 2m/1m` 多周期剥洋葱交互图谱（支持盲测遮罩模式）。
3. **03 日内时间与流程**：纽约时间轴 4 阶段（`08:30 前盘前定位` → `08:30–11:00 早盘猎杀` → `12:00–13:00 午休禁区` → `13:30–16:00 下午盘与 MOC`）、开仓前 6 步必检清单与 12 词核心术语库。
4. **04 理解练习**：每次 3 题引导式状态判断（`Wait / Armed / Execute / Cancel / Exit`），带 SVG 盘面演化图与版本化答题记录。
5. **05 Ep.04 复盘手帐**：严格遵循第 4 集四维复盘规范，内置 `MNQ / MES / NQ / ES` 点值与盈亏比计算器。
6. **06 我的笔记**：原生 `WKWebView` 双写持久化（`notebook.json` + `history/` 按分钟快照）与一键「复制接续请求」。

---

## 📚 配套深度文档

- [🧭 ICT 2022 终极总结与全体系精要归纳](file:///Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/ICT_2022_终极总结与全体系精要归纳.md)：IPDA 算法逻辑、S1–S6 六阶段标准化实战决策链、12 大核心技术武器库速查与终局晋级阶梯。
- [📘 ICT 2022 全 37 讲图文精读手册](file:///Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/ICT_2022_全37讲_图文精读手册.md)：涵盖全 37 讲 62+ 张关键帧图解、机构订单流逻辑与避坑指南的大全集讲义。
- [知识体系总纲与六阶段链路](file:///Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/references/framework.md)：12 条核心交易原则与 S1–S6 实战决策链路。
- [学习室技术架构与编译指南](file:///Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/references/study-app-architecture.md)：纯原生 Swift + WKWebView 架构与增量补齐流程。
