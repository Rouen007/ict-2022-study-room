---
name: ict-2022-study-room
description: 学习、复盘与维护 ICT 2022 Mentorship [No Rant]（全 37 讲）交易体系及本地「ICT 2022 学习室」macOS App。当用户询问 ICT 2022 模型（Stop Hunt、MSS/BMS、Displacement、FVG、Order Block、0.5 均衡位折价/溢价区、Power of 3 / AMD、纽约 08:30/13:30 时间窗口）、发送「复制接续请求」点评学习室笔记与复盘手帐、要求继续扩充后续集数 1080p 图解、或维护 ICT 2022 学习室 App 时使用。
---

# ICT 2022 Study Room & Trading Framework (Created by Xiao Ang)

基于 **2022 ICT Mentorship [No Rant]（全 37 讲）** 原片、1080p 关键帧截图与逐分钟字幕稿，提供可追溯的机构订单流教学、实盘复盘点评，以及本地 **「ICT 2022 学习室」(`ICT 2022 学习室.app`)** 的持续维护与扩充。

## 按请求进入

| 用户请求类型 | 行动与按需阅读 |
| :--- | :--- |
| **解释概念 / 拆解某集或某张 K 线图** | 先读 [references/framework.md](references/framework.md) 对应阶段与原则；若涉及具体集数，按需查阅 `transcripts/{ep}_*.md` 原稿与 `study-room/lesson-assets/` 原图，严格区分「ICT原话」「原片图表」「主模型归纳」。 |
| **发送「复制接续请求」/ 点评笔记或练习** | 先读 [references/teaching-and-review.md](references/teaching-and-review.md)，再读取 `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/notebook.json`，结合用户当前的 `summaryNote`、`lessonNotes`、`answers/attemptHistory` 与 `journalEntries` 进行针对性纠偏与下一步训练指导。 |
| **扩充后续集数（如 Ep.06–37）1080p 图解** | 读 [references/study-app-architecture.md](references/study-app-architecture.md) 的「增量补齐 1080p 关键帧流程」：定位时间戳 → `yt-dlp` 临时拉取 → `ffmpeg` 截帧并视觉核验 → **立即清理临时 MP4 释放磁盘** → 重新生成数据并编译验收 App。 |
| **修改 / 优化「ICT 2022 学习室」App** | 读 [references/study-app-architecture.md](references/study-app-architecture.md)，修改共同源 `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room` 后执行 `./study-room/native/build.sh` 与 `--qa` 校验，确保 `notebook.json` 用户数据不丢失。 |
| **同步更新个人网站 ICT 专栏** | 读 [references/teaching-and-review.md](references/teaching-and-review.md) 的「网站专栏同步规范」，更新 `/Users/rouen/Documents/rouen-docs-site/docs/kol/ict/` 并运行 `npm run docs:build` 通过安全守卫检查。 |

---

## 核心入口与路径表

| 入口 | 路径 / 身份 |
| :--- | :--- |
| **GitHub 公开仓库** | `https://github.com/Rouen007/ict-2022-study-room` |
| **本地共同源根目录** | `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship` |
| **学习室工作台源码** | `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room` |
| **桌面原生 App** | `/Users/rouen/Desktop/ICT 2022 学习室.app` (`local.rouen.ict2022study`) |
| **用户正式笔记与手帐** | `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/notebook.json`（及 `history/` 快照） |
| **个人网站专栏目录** | `/Users/rouen/Documents/rouen-docs-site/docs/kol/ict/` |

---

## 分析与决策主线（6 步链路 `S1–S6`）

任何行情推演、图表诊断或复盘点评均按以下 6 步顺序核验，不跳步、不背口诀：

`S1 时间与环境门 → S2 流动性地图 (DOL) → S3 猎杀与陷阱识别 → S4 位移与结构扳机 (MSS) → S5 均衡矩阵与 FVG 挂单 → S6 四维手帐复盘`

1. **`S1` 时间与环境门**：图表锁定 **纽约时间 (`UTC-4 / UTC-5`)**。只做 `08:30–11:00` 早盘与 `13:30–16:00` 下午盘；`12:00–13:00` 纽约午休强制空仓。交割月先在 Barchart 核对 Open Interest 主力合约。
2. **`S2` 流动性地图 (`Draw on Liquidity`)**：自上而下（`1W → 1D → 1H → 15m`）标出高概率磁铁——旧高买方止损（`BSL`，尤其是相对等高点 `Equal Highs`）、旧低卖方止损（`SSL`）与大周期未回补失衡区（`FVG`）。
3. **`S3` 猎杀与陷阱识别（`Stop Hunt / Sucker Play / Three Drives`）**：高周期流动性池未被刺穿前，开盘初顺势小破位常为诱空/诱多陷阱（`Sucker Play`）；冲击流动性池时常走出三推（`Three Drives`）消耗动能。
4. **`S4` 位移与结构扳机（`MSS / BMS + Displacement`）**：扫损后降维到 `5m / 2m / 1m`，必须等大实体位移 K 线干脆击穿最近的短期波段高低点（`BMS / MSS`），或吞没反向订单块开盘价完成交付状态转换（`Change in the State of Delivery`）。
5. **`S5` 均衡矩阵与 FVG 挂单（`0.5 Equilibrium + FVG + OB`）**：拉斐波那契 `0–1` 仅留 `0.5` 中轴——做空只挂 `>0.5` **溢价区 (Premium)** 看跌 FVG；做多只挂 `<0.5` **折价区 (Discount)** 看涨 FVG（常叠看涨 OB）；目标必须跨过 `0.5` 直指对侧内部 FVG 与外部流动性池。**无 FVG 绝不开仓（保持 `Wait`）**。
6. **`S6` Ep.04 四维手帐复盘**：每日只统计确定性波段四项数据：① FVG 入场价 (E)、② 止损位 (S)、③ 目标点差 (Handles)、④ 折算合约金额（`MNQ \$2/pt`、`MES \$5/pt`、`NQ \$20/pt`、`ES \$50/pt`）。

---

## 归因与工程铁律

- **证据归因**：所有教学提炼必须明确区分 `老师 (ICT原话)`、`老师图 (原片图表)` 与 `主模型 (归纳推演)`，附带原片集数与 `[MM:SS]` 时间戳。
- **轻量化原则**：所有视频跳帧统一使用 **YouTube (`&t=Xs`) + B站中配 (`?p=N&t=X`) 双端外链直达**，不在仓库或包内留存大体积 `.mp4` 文件。
- **笔记安全**：任何界面或脚本更新前先确认 `study-room/notebook.json` 不被覆盖。
