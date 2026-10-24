# -*- coding: utf-8 -*-
"""Handbook text for Episodes 12 to 16 (Module 3)."""

CHAPTERS = {}

CHAPTERS[12] = """## Ep. 12：高阶市场结构拆解：中继结构与止损铁律（Advanced Price Action Theory）

### 12.1 三层波段结构的分形层级（LTH / ITH / STH）`[00:01 – 06:00]`
为了避免散户在日内被局部的每一个微小假波动震出局，ICT 在本集公开了机构级别的三层市场结构模型：
1. **短期高/低点（Short Term High / Low, STH / STL）**：由 3 根 K 线组成的最基础分形摆动点（中间 K 线高点高于左右两侧即为 STH）。这是最低维度的微观结构。
2. **中期高/低点（Intermediate Term High / Low, ITH / ITL）**：
   - 当价格回抽测试一个更高周期的公允价值缺口（HTF FVG）或订单块（HTF OB）时所形成的摆动高点/低点。
   - **结构特征**：ITH 的两侧必然各自存在一个更低维度的 STH。
   - **机构意义**：只要当前的 ITH 没有被收盘价实体有效击穿，整个大级别的单边趋势就处于完全健康状态！
3. **长期高/低点（Long Term High / Low, LTH / LTL）**：由多个 ITH 组合而成，代表日线或周线级别的绝对流动性转折点。

### 12.2 保护性止损的梯级推进铁律 `[06:00 – 14:00]`
- **散户致命伤**：稍微有点浮盈就急着把止损移到开仓价（Breakeven），结果在正常的二次回踩中被精确打掉，随即目送行情飞奔向终极目标。
- **ICT 止损推进法则**：止损只允许移动到**已确认的中期高点（ITH，空单）**上方，或**中期低点（ITL，多单）**下方。在新的 ITH/ITL 尚未被后续结构确认之前，绝不盲目移动止损。

````carousel
![Ep.12 [04:30] 三层市场结构层级关系 (LTH / ITH / STH)](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep12_market_structure_hierarchy.png)
<!-- slide -->
![Ep.12 [10:15] 嵌套 MSS 与止损梯级保护](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep12_nested_mss_nq_chart.png)
````

> [!IMPORTANT]
> 真正的结构破坏（MSS）必须是击穿 ITH 或 ITL，仅仅刺穿一个孤立的 STH 往往只是小级别的流动性收集，切忌误认反转。

---
"""

CHAPTERS[13] = """## Ep. 13：第 12 集三层市场结构的实战应用与回放（Advanced Price Action in Action）

### 13.1 跨周期分形嵌套的实战检验 `[00:01 – 06:00]`
- 在 15 分钟图表上标出当日的 LTH 与 ITH 骨架，确认日内主浪由空头掌控。
- 随后降维到 5 分钟与 1 分钟图表：
  - 每一个向上的小波段反弹，只要进入了 15m 看跌 FVG，都会形成一个新的 1m/5m ITH。
  - 顺势交易员不需要抓最高点，只需在 1m 图观察 STH 失败并跌穿 STL 的瞬间，顺应大趋势回踩开单。

### 13.2 订单块 50% 均衡位的精准承接 `[06:00 – 12:00]`
- 当价格回调至看涨订单块（Bullish Order Block）时，重点观察该连续阴线柱体 50% 的中轴位置（Mean Threshold）。
- 若实体收盘价牢牢守在 50% 中轴之上，即便下影线向下虚刺，也代表机构在深折价区积极吸筹，是加仓或多头入场的极强信号。

````carousel
![Ep.13 [05:45] 订单块 50% 折价区承接与进场](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep13_order_block_50_discount.png)
````

> [!TIP]
> 复盘时用水平虚线画出每个 Order Block 柱体实体的 50% 位置，观察价格在此处的微观价格反应（Tape Reading）。

---
"""

CHAPTERS[14] = """## Ep. 14：单边波段中的多重 FVG 处理与实盘复盘（Live Trading The Model）

### 14.1 单边位移中出现多个 FVG 时的选择法则 `[00:01 – 04:30]`
在剧烈单边行情中，一段 50–100 点的快速位移往往会连续留下 2 个甚至 3 个看跌或看涨 FVG。散户往往陷入选择困难：究竟在该在哪个 FVG 挂单？
- **法则 1：50% 斐波那契均衡区过滤**：从位移起点拉至终点，若做空，只选择位于 50% 均衡位上方的**溢价区 FVG**；折价区的 FVG 直接弃用。
- **法则 2：订单块重合共振（Confluence）**：若某个 FVG 恰好与前期跌破前的 Order Block 开盘价处于同一价格带，该 FVG 拥有最高权重。
- **法则 3：深度回撤优先原则**：若前两个条件并存，优先在位置最高（最深溢价）的 FVG 挂单以换取极致盈亏比；若市场动能极强未给深回撤，接受踏空，绝不在低位追空。

````carousel
![Ep.14 [02:30] 实盘单边波段与多重 FVG 处理](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep14_live_execution_fvg_run.png)
````

> [!NOTE]
> 踏空是交易的一部分。用规则过滤掉劣质 FVG，即使偶尔踏空，也能长期避免在半山腰接刀被扫损的致命错误。

---
"""

CHAPTERS[15] = """## Ep. 15：走盘复盘：早盘剥头皮与订单块配合 FVG（Tape Reading FOMC）

### 15.1 实时走盘阅读（Tape Reading）的核心技巧 `[00:01 – 05:00]`
- **盘口语言（Tape）的本质**：不需要订阅昂贵的时间与销售（Time & Sales）明细，只需盯紧 1 分钟 K 线的收盘形态与能量释放。
- 当大阳线进入看跌 FVG 时，观察 K 线是否在触碰到 FVG 顶部的一瞬间遭遇快速压制收长上影线。
- **中轴阻击（Consequent Encroachment, CE）**：FVG 顶部与底部的中间点（50%）被称为 CE。当多头无法以实体收盘站上 CE 时，代表买力枯竭，空头算法立即接管并展开下砸。

````carousel
![Ep.15 [03:15] 走盘复盘：订单块与 FVG 重叠区反应](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep15_fomc_tape_reading_fvg.png)
````

> [!TIP]
> 剥头皮（Scalping）不是凭感觉盲目快进快出，必须在日线 DOL 顺势方向上，利用 1m FVG 的 CE 进场，博取 10–20 点的确定性利润。

---
"""

CHAPTERS[16] = """## Ep. 16：同一交易日内的多重交易设置（Multiple Trading Setups Per Session）

### 16.1 早盘与下午盘的独立二阶段结构 `[00:01 – 06:00]`
- **不要把全天看作单一不可分割的整体**。一个标准的交易日可以清晰划分为两个独立的战役：
  - **早盘战役（08:30 – 11:00）**：利用开盘流动性猎杀完成第一笔标准 2022 模型交易，达标后坚决落袋为安。
  - **午休停火（12:00 – 13:00）**：严格保持空仓，禁止开新单，让算法进行再平衡。
  - **下午盘战役（13:30 – 15:30）**：以全天产生的新最高点和新最低点重新拉取 50% 均衡线，寻找第二波独立的入场机会。

### 16.2 避免“利润回吐陷阱”的纪律守则 `[06:00 – 12:00]`
- 很多交易员在早盘赚了 2,000 美元，却在下午盘亏损 2,500 美元，全天倒亏。
- **纪律防线**：若要在下午盘交易，下午单笔的最大允许风险额度，绝不能超过早盘已实现净利润的 30%–50%。这样即便下午盘止损，全天依然锁定可观盈利。

````carousel
![Ep.16 [04:50] 同一交易日内早盘 + 下午盘多重设置](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep16_multiple_setups_manipulation.png)
````

> [!IMPORTANT]
> 如果早盘行情已经走出了超过平均真实波幅（ADR）的超级极端单边，下午盘通常会陷入窄幅震荡，此时最优策略是直接关机收工！

---
"""

print(f"handbook_ep12_16 ready with {len(CHAPTERS)} chapters")
