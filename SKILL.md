---
name: ict-2022-study-room
description: 学习、复盘与维护 ICT 2022 Mentorship [No Rant] 交易体系及本地「ICT 2022 学习室」macOS App。当用户询问 ICT 2022 模型（Stop Hunt、MSS/BMS、Displacement、FVG、Order Block、0.5 均衡位折价/溢价区、Power of 3 / AMD、纽约 08:30/13:30 时间窗口）、发送「复制接续请求」点评学习室笔记与复盘手帐、或要求扩充/维护 ICT 2022 学习室 App 时使用。
---

# ICT 2022 学习室 & 交易体系 Skill (Created by Xiao Ang)

本 Skill 同时负责两件事：
1. **ICT 2022 Mentorship 交易框架教学与实盘复盘指导**（严格基于 2022 No-Rant 全 37 讲原片、1080p 关键帧证据与 6 步决策链路，区分 `ICT原话`、`原片图表` 与 `主模型归纳`）。
2. **「ICT 2022 学习室」App 的接续学习点评、后续集数 1080p 图解扩充与工程维护**。

---

## 一、入口与路径约定

| 入口 | 路径 / 身份 |
| :--- | :--- |
| **GitHub 公开仓库** | `https://github.com/Rouen007/ict-2022-study-room` |
| **本地项目根目录** | `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship` |
| **学习室前端与数据源** | `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room` |
| **macOS 桌面原生成品** | `/Users/rouen/Desktop/ICT 2022 学习室.app` (`local.rouen.ict2022study`) |
| **用户学习笔记与复盘手帐** | `study-room/notebook.json`（及 `study-room/history/` 分钟级快照） |
| **前 5 集图文精读手册** | `ICT_2022_Ep01_05_图文精读手册.md`（同步发布于个人网站 `/kol/ict/`） |
| **全 37 集清洗后逐分钟原稿** | `transcripts/01_*.md` – `37_*.md` |

---

## 二、ICT 2022 核心交易体系（6 步链路 × 12 条原则）

### 1. 一笔 ICT 2022 交易的 6 步标准链路 (`S1–S6`)

1. **`S1` 时间与环境门（今天/此刻值不值得做？）**
   - 图表必须锁定 **纽约时间 (`UTC-4 / UTC-5`)**。
   - 两大黄金猎杀窗口：早盘 **`08:30–11:00 NY`**（`08:30` 宏观数据脉冲 + `09:30` 美股现货开盘）与下午盘 **`13:30–16:00 NY`**。
   - **`12:00–13:00 NY Lunch` 为午休禁区**：严禁开新仓；午休高低点往往成为 `13:30` 下午盘的止损猎杀靶子。
   - **季度移仓检查（3/6/9/12 月第二个周五前）**：在 Barchart 检查 **Open Interest（持仓量）**，新季合约持仓量反超老合约当天即切换主力合约。
2. **`S2` 流动性地图（算法下一站去哪？Draw on Liquidity）**
   - 算法驱动价格只有两个目的：① 猎杀旧高/旧低外侧的止损单（**Liquidity：BSL / SSL**）；② 重新平衡价格失衡区（**Imbalance：FVG**）。
   - 自上而下（`1W → 1D → 1H → 15m`）标出未清扫的相对等高点（**Equal Highs = BSL**）与旧低点（**Old Lows = SSL**）。散户眼中的“双顶强阻力”，正是聪明钱眼里最肥美的买方止损池。
3. **`S3` 猎杀与陷阱识别（Stop Hunt / Inducement / Three Drives）**
   - **诱空/诱多陷阱（Sucker Play）**：大级别看空但上方等高点（BSL）尚未清扫前，开盘初先跌破短期小低点往往是诱导散户追空的陷阱。
   - **三推模式（Three Drives Pattern）**：价格冲击高周期流动性池时，常走出三次阶梯式推高（或推低），第三次刚刺穿旧高/旧低即耗尽动能反转。
4. **`S4` 位移与结构扳机（MSS / BMS + Displacement）**
   - 扫损发生后降维到 **`5m / 2m / 1m`** 图表，绝不左侧摸顶抄底，必须强迫市场亮出底牌（*Forcing the market to tip its hand*）。
   - 扳机条件：出现高能量大实体 K 线（**Displacement，大象跳进儿童泳池**）干脆击穿最近的短期波段高低点（**Market Structure Shift / Break in Market Structure**），且三根 K 线间留下不重叠的 **Fair Value Gap (FVG)**。
   - **订单块交付状态转换（Change in the State of Delivery）**：扫低点前最后一根或连续几根阴线为看涨 Order Block（扫高点前最后阳线为看跌 OB）；当位移大 K 线瞬间吞没该 OB 的开盘价（Opening Price）时，交付状态正式翻转。
5. **`S5` 均衡矩阵与挂单执行（Equilibrium 0.5 + FVG + OB）**
   - 从位移波段起点到终点拉斐波那契 `0–1`（仅保留 `0`、`0.5`、`1`）：
     - **做空**：只选 `>0.5` **溢价区 (Premium)** 内的看跌 FVG，在阳线向上回抽触及 FVG 下沿时限价做空，止损设在扫损高点（或位移起点）外侧，止盈必须跨过 `0.5` 进入 `<0.5` **折价区 (Discount)** 内的内部看涨 FVG 与外部 SSL。
     - **做多**：只选 `<0.5` **折价区 (Discount)** 内的看涨 FVG（常与看涨 OB 重叠），在阴线回抽触及 FVG 上沿时限价做多，止盈设在 `>0.5` 溢价区内部看跌 FVG 与外部 BSL。
   - **无 FVG 不开仓**：若刺穿流动性池后的第一波回落 K 线彼此重叠、无任何 FVG，保持 `Wait`，防范二次冲顶。
6. **`S6` Ep.04 四维复盘手帐规范**
   - 每日收盘后截取 `2m/5m` 图表，强制标注四项数据：① **FVG 入场价 (E)**、② **止损位 (S)**、③ **目标点差 (Handles)**、④ **折算合约美元价值**（`MNQ \$2/pt`、`MES \$5/pt`、`NQ \$20/pt`、`ES \$50/pt`）。不幻想“从最高点吃到最低点”，只统计 FVG 到对侧流动性池的确定性区间。

---

## 三、常见任务执行流程

### 1. 当用户发送「复制接续请求」或要求点评笔记时
1. 读取 `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/notebook.json`。
2. 检查用户的：
   - `summaryNote`（核心理解）与 `lessonNotes`（分集随手记）
   - `answers` / `attemptHistory`（`Wait / Armed / Execute / Cancel / Exit` 练习题作答与理由）
   - `journalEntries`（Ep.04 四维复盘手帐记录）
   - `mistakes`（自查易错项）
3. 结合对应集数的原片时间点与 1080p 图表给出针对性反馈，指出哪里符合 ICT 2022 规则、哪里还存在散户追突破或提前摸顶习惯，并给出下一步练习建议。

### 2. 当用户要求继续扩充后续集数（如 Ep.06–Ep.12）的 1080p 图解时
1. 先阅读 `transcripts/{ep}_*.md` 逐分钟原稿，定位该集讲解核心图表与实盘交割单的精确时间戳 `[MM:SS]`。
2. 用 `yt-dlp` 临时下载该集 1080p 视频流，通过 `ffmpeg -ss` 截取高清 PNG 放入 `study-room/lesson-assets/`，用看图工具逐张核验图表清晰度后**立即删除临时 MP4 视频文件**以节省本地空间。
3. 将新增关键帧与三层提炼卡片写入 `build_course_data.py` 与 `build_study_room.py`，运行：
   ```bash
   python3 build_course_data.py
   python3 build_study_room.py
   ./study-room/native/build.sh
   ```
4. 校验通过后同步提交推送到 `Rouen007/ict-2022-study-room` 与个人网站 `Rouen007/rouen-docs-site`。
