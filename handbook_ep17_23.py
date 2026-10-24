# -*- coding: utf-8 -*-
"""Handbook text for Episodes 17 to 23 (Module 4)."""

CHAPTERS = {}

CHAPTERS[17] = """## Ep. 17：外汇日内多周期实战与美元指数联动（Forex Application & DXY）

### 17.1 美元指数（DXY）作为外汇直盘的指南针 `[00:01 – 05:00]`
- 在分析 EURUSD 或 GBPUSD 时，不能孤立看待单一货币对。外汇市场的核心基石是**美元指数（US Dollar Index, DXY）**。
- **镜像联动机制**：
  - DXY 向上刺穿买方流动性（BSL）进入日线看跌失衡区时，EURUSD 必然正在向下刺穿卖方流动性（SSL）进入看涨折价区。
  - 当 DXY 确认 Bearish MSS 并出现看跌 FVG 时，EURUSD 会同步走出 Bullish MSS，此时做多 EURUSD 胜率极高。

### 17.2 伦敦杀手时区的犹大秋千定位 `[05:00 – 10:00]`
- 伦敦盘（02:00–05:00 NY）通常形成全天的高点（看跌日）或低点（看涨日）。
- 观察亚洲盘区间（Asian Range）：若全天看多，伦敦开盘必须先下破亚洲盘低点清扫 Sell Stops，随后迅速收回并走出 15m/5m 看涨 FVG，构成完美的 Judas Swing 入场点。

````carousel
![Ep.17 [04:15] 外汇伦敦盘犹大秋千与 DXY 联动](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep17_forex_judas_swing_london.png)
````

> [!TIP]
> 在 TradingView 上将 DXY 与 EURUSD 竖向分屏对比，观察关键高低点扫损是否在同一分钟内精准对应。

---
"""

CHAPTERS[18] = """## Ep. 18：多门资产跨周期推演与订单块深度洞察（Insights Into Order Block Theory）

### 18.1 日分割线（Daily Dividers）与日内时间切片 `[00:01 – 06:00]`
- 在图表上开启垂直分割线（纽约时间 18:00 为新交易日起点），清晰划分出亚洲盘、伦敦盘和纽约盘。
- **严禁在真空区寻找 1m FVG**：小周期的微观结构必须建立在**高时间框架（HTF Daily/4H/1H）关键 PD Array** 的碰撞反应之上。若价格没有触碰任何日线级别的流动性池或失衡区，1 分钟图上的任何形态都容易沦为随机噪音。

### 18.2 订单块的底层力学：买卖交付状态的彻底转变 `[06:00 – 12:00]`
- 看跌订单块（Bearish OB）不是普通的大阳线，而是**刺穿外部流动性后的一整串阳线上涨波段**。
- 当大阴线实体强力跌破这串阳线的第一根 K 线的开盘价时，代表算法由买入交付彻底翻转为卖出交付。回抽测试该开盘价即是机构重新定价的做空契机。

````carousel
![Ep.18 [05:20] 日分割线与 15m 订单块定位](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep18_daily_dividers_15m_ob.png)
````

> [!NOTE]
> 真正的机构订单块通常伴随着高成交量与后续的高能位移，若突破后无速度、阴阳交错，说明机构没有真正介入。

---
"""

CHAPTERS[19] = """## Ep. 19：趋势延续 vs 反转猎杀：如何读懂日内叙事（Narrative）

### 19.1 构建日内叙事（Market Narrative）的三问法则 `[00:01 – 06:00]`
每次开盘交易前，交易员必须在心里清晰回答三个问题：
1. **价格刚刚从哪来？**（刚刚扫掉了哪一个高周期的流动性池或回补了哪一个日线 FVG？）
2. **价格接下来要去哪？**（当前日内最显眼、未被触及的对手盘流动性磁铁 DOL 在哪里？）
3. **当前时间窗口需要先诱骗谁？**（为了把价格送到下一个目标，算法在开盘必须先制造哪种假象来吸引反向跟风盘？）

### 19.2 订单块交付状态转变与单边单日持有 `[06:00 – 14:00]`
- 当日内叙事与高周期偏向高度契合时，不要急于在 10–15 点微利出局。
- 只要中期高点（ITH）没有被破坏，依托看跌订单块连续下推的行情可以坚定持有到下午盘甚至收盘加速阶段（MOC）。

````carousel
![Ep.19 [06:40] 订单块交付状态转变与日内叙事](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep19_order_block_delivery_shift.png)
````

> [!IMPORTANT]
> 叙事是交易的灵魂。没有日内叙事的支撑，任何 FVG 进场都是盲目的摸奖。

---
"""

CHAPTERS[20] = """## Ep. 20：伦敦盘与纽约盘接力剖析（London Session Forex & NY Continuation）

### 20.1 伦敦盘大单边透支后的纽约盘应对策略 `[00:01 – 05:00]`
- 如果伦敦盘（02:00–05:00 NY）已经走出了极为剧烈的单边爆发并提前触碰了全天的日线 DOL 目标，纽约早盘切忌盲目追高杀跌。
- **最优化交易入场（Optimal Trade Entry, OTE）**：此时算法往往在纽约早盘（07:00–09:00）展开深度回撤，回踩伦敦单边浪的 **62% – 79%（OTE 折价/溢价黄金区）**，并在该区域测试 15m 看涨/看跌订单块。

### 20.2 顺势接力还是深幅反转的判别标志 `[05:00 – 08:00]`
- 若回撤进入 OTE 区域后迅速走出同向 MSS 与看涨 FVG，确认纽约盘顺势接力；若大阴线直接跌穿伦敦浪起点，说明全天行情演变为深幅反转。

````carousel
![Ep.20 [03:45] 伦敦盘最优化进场 OTE 与纽约盘接力](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep20_london_ote_continuation.png)
````

> [!TIP]
> 永远在伦敦盘创造的波段高低点上拉取斐波那契（0.62 / 0.705 / 0.79），等待纽约盘在 OTE 区域给出明确信号。

---
"""

CHAPTERS[21] = """## Ep. 21：跨市场相关性与风险偏好轮动（Risk On VS Risk Off Market）

### 21.1 资产类别相关性与宏观流动性 `[00:01 – 05:00]`
- **Risk-On（风险偏好）**：股票指数（ES/NQ/YM）上涨，避险资产（美元 DXY、美债价格反向波动）承压。
- **Risk-Off（风险厌恶）**：指数抛售下砸，资金回流美元与高评级避险品种。
- 观察股指与美元之间的反向背离：若 ES 刷新低点而 DXY 却未能刷新高点，说明空头动能正在衰竭，警惕日内潜在的暴力反弹。

### 21.2 相对等低点（Equal Lows）作为下行强力磁铁 `[05:00 – 09:00]`
- 盘面出现并排的平头等低点（Equal Lows）时，下方堆积了海量的散户 Sell Stops。即便盘中反复反弹，算法最终也必然会以大阴线向下暴力击穿它们。

````carousel
![Ep.21 [04:10] DXY 联动与股指等低点流动性池](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep21_dxy_es_equal_lows.png)
````

> [!NOTE]
> 记住等低点是磁铁，未击穿前任何做多都只能当作极短线的超跌反弹，切勿当成底部反转来死扛。

---
"""

CHAPTERS[22] = """## Ep. 22：跨市场聪明钱背离（Smart Money Technique, SMT Divergence）

### 22.1 SMT 背离的底层逻辑：聪明钱在不同品种间的暗中派发 `[00:01 – 05:00]`
- CME 股指期货三大品种（标普 ES、纳指 NQ、道指 YM）理论上高度同向联动。
- **看跌 SMT 背离（Bearish SMT）**：
  - 在上午冲高阶段，**ES 创出新高（Higher High, HH）**，刺穿买方流动性池；
  - 但**同期的 NQ 却未能创出新高（Lower High, LH）**，表现出明显的内生疲软。
  - **核心玄机**：机构资金已经在 NQ 上提前建立了大额空头头寸，不再允许价格走高；而 ES 的虚假破高仅仅是为了吸引最后一批突破追多的散户接盘！
  - **交易执行**：优先做空那个未能创出新高的**弱势品种（NQ）**，因为一旦大势掉头，弱势品种的下砸速度最快、幅度最大！

### 22.2 看涨 SMT 背离（Bullish SMT）与底部精准抄底 `[05:00 – 09:30]`
- 反之，当 ES 跌破前低创出更低低点（LL）而 NQ 拒绝跌破前低形成更高低点（HL）时，构成经典看涨 SMT。
- 优先做多拒绝创新高的**强势品种（NQ）**，其向上的弹性与爆发力远超同期品种。

````carousel
![Ep.22 [04:30] 跨市场聪明钱背离 SMT Divergence (ES vs NQ)](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep22_smt_divergence_es_nq.png)
````

> [!IMPORTANT]
> SMT 是 ICT 体系中胜率最高、权重最大的进阶工具之一！当 SMT 与纽约关键时间窗口、高周期 FVG 同时出现时，即为最高规格的 A+ 级交易机会。

---
"""

CHAPTERS[23] = """## Ep. 23：美联储 FOMC 决议后走盘与斐波那契通道（Post FOMC & FIB Channels）

### 23.1 FOMC 次日（周四）的高确定性波段机会 `[00:01 – 04:30]`
- 周三下午 FOMC 利率决议往往制造数百点的极端上下宽幅拉锯，普通交易员极易被扫地出门。
- **周四黄金剧本**：FOMC 决议公布次日，市场通常从极度混乱中走出真正的宏观定价方向。此时可以利用周三暴涨暴跌留下的巨大单边波段，绘制斐波那契通道（Fib Channels）。

### 23.2 斐波那契通道与终极目标锚定 `[04:30 – 08:30]`
- 从周三大单边浪的极值拉取斐波那契通道，关键点位包括 0.5（均衡位）以及 1.618 / 2.0 / 2.618 扩展位。
- 结合日内 15m 看跌 FVG，在周四早盘反弹测试均衡位时果断入场，终极目标锁定周三低点下方的卖方止损池。

````carousel
![Ep.23 [03:40] FOMC 斐波那契通道与次日目标定位](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep23_fomc_fib_channel_targets.png)
````

> [!TIP]
> 重大事件后第二天不要心急，开盘先看价格对前一天大阴线/大阳线 50% 位置的争夺，再决定顺势还是反抽。

---
"""

print(f"handbook_ep17_23 ready with {len(CHAPTERS)} chapters")
