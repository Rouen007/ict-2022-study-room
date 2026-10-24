# -*- coding: utf-8 -*-
"""Handbook text for Episodes 06 to 11 (Module 2)."""

CHAPTERS = {}

CHAPTERS[6] = """## Ep. 06：市场效率范式与机构订单流（Market Efficiency Paradigm & Institutional Order Flow）

### 6.1 市场效率范式（IPDA）与散户思维盲区 `[00:01 – 06:00]`
- **散户认知错误**：传统技术分析把“等高点/双顶”看作强阻力，把“等低点/双底”看作强支撑；散户在支撑位买入、在阻力位卖出，并将止损紧密设在极值外侧数个点。
- **机构订单流视角**：银行间价格递送算法（Interbank Price Delivery Algorithm, IPDA）的核心目标是寻找**对手盘流动性**。每一个止损单本质上都是强制市价单（Buy Stops 是市价买单，Sell Stops 是市价卖单）。机构若要建立数十亿美元的空头仓位，必须要有天量的市价买单作为对手盘承接，因此算法必然会被编程去刺穿那些显眼的等高点，引爆 Buy Stops 后再完成派发。

### 6.2 三 K 线看跌/看涨 FVG 的底层形成原理 `[06:00 – 12:00]`
- **看跌公允价值缺口（SIBI: Sell-Side Imbalance, Buy-Side Inefficiency）**：
  - **第 1 根阳线/小阴线**：向上刺穿买方流动性（BSL）。
  - **第 2 根长实体大阴线（Displacement）**：机构算法集中砸盘，由于单边抛售速度极快，多方在此区间几乎没有成交机会。
  - **第 3 根 K 线**：第 1 根 K 线的最低点与第 3 根 K 线的最高点之间，留下一个**没有任何实体或下影线重叠的价格空白区**。
  - **再平衡（Rebalance）**：随后的阳线回抽触及该缺口时，算法对该区间进行重新定价（Deliver Buy-side Liquidity），此时是空头挂单狙击的最佳窗口。

### 6.3 高时间框架缺口回补后的日内多头转换 `[12:00 – 16:30]`
- 当价格在更高时间框架（日线/4H）回补了前期看跌失衡区并触及重要折价区时，日内预期需由空翻多。
- **日内剧本**：早盘 08:30 借消息或开盘下砸刺穿短期卖方流动性（SSL），随后以高能量位移（Displacement）放量拉起突破结构，回踩 15m/5m 看涨 FVG（BISI）展开单边逼空。

````carousel
![Ep.06 [06:15] 三 K 线看跌 FVG 机构订单流结构原理](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep06_fvg_concept_diagram.png)
<!-- slide -->
![Ep.06 [14:30] 15m 价格回踩日线 FVG 后的多头建仓走势](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep06_15m_nq_execution.png)
````

> [!IMPORTANT]
> **实战挂单铁律**：看跌 FVG 做空时，限价空单挂在 FVG 的下沿（入口处）；止损必须放在冲高形成最高点那根 K 线的最高价上方，绝不能随意移到 FVG 内部。

---
"""

CHAPTERS[7] = """## Ep. 07：日线偏向与整固跳栏障碍（Daily Bias & Consolidation Hurdles）

### 7.1 为什么大幅单边日之后很难直接延续趋势？`[00:01 – 04:00]`
- 散户在经历了一个数百点的大阳线或大阴线单边日后，往往预期第二天会继续爆发大单边，盲目在开盘追单，结果往往被震荡反复止损。
- **整固跳栏（Consolidation Hurdles）**：当算法清扫了高时间框架外部的重要止损池后，市场通常会进入再平衡与能量积聚状态（Consolidation）。此时日线往往收出孕线（Inside Bar）或十字星，波动局限在昨天极值的 50% 均衡位附近。

### 7.2 外部止损池与内部 FVG 的“乒乓交替法则”`[04:00 – 09:30]`
- **市场运动规律**：价格永远在**外部流动性（External Range Liquidity, ERL）**与**内部流动性（Internal Range Liquidity, IRL）**之间往复循环：
  - 当价格清扫了外部流动性（如前期波段最高点 BSL），若没有足够动能继续扩张，算法的下一个磁铁必然是区间内部的 **50% 均衡位（Equilibrium）** 及 **内部 FVG**。
  - 当内部 FVG 被充分再平衡后，算法又会蓄势向下一个反向外部流动性池（SSL）进军。
- **应对整固日的战术**：降低盈利预期。在整固日中，不要期待价格走出 100 点以上的大波段，空单一旦触及区间 50% 均衡位或内部首个反向 FVG，必须全部兑现离场。

````carousel
![Ep.07 [04:45] 日线偏向在均衡位震荡时的障碍识别](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep07_daily_bias_consolidation.png)
<!-- slide -->
![Ep.07 [09:20] 15m 图清扫流动性池后的单边破位](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep07_15m_liquidity_run.png)
````

> [!TIP]
> **避坑指南**：在日线 50% 均衡位纠缠且未出现明显偏向时，减少交易频次；强迫市场先刺穿 15m 等高/等低点并走出结构破坏后再做决定。

---
"""

CHAPTERS[8] = """## Ep. 08：外汇市场应用：EURUSD 与 GBPUSD 伦敦/纽约狙击案例（Forex Markets Application）

### 8.1 算法定价逻辑（IPDA）在外汇市场的完全通用性 `[00:01 – 04:00]`
- ICT 明确指出，股指期货（NQ/ES）与外汇直盘（EURUSD/GBPUSD）底层均由同源的银行间价格递送算法驱动。
- 外汇市场的核心 Killzone 时间窗口（均为纽约时间）：
  - **亚洲盘整固（Asian Range）**：19:00 – 00:00（建立初始积累区间 Accumulation）。
  - **伦敦杀手时区（London Killzone）**：02:00 – 05:00（往往制造全天的最高点或最低点，即 Judas Swing 操纵）。
  - **纽约杀手时区（New York Killzone）**：07:00 – 10:00（顺应伦敦盘趋势进行单边扩张或二次派发）。

### 8.2 EURUSD 3 分钟折价区 FVG 实战狙击 `[04:00 – 08:30]`
- **推演流程**：
  1. 日线/1小时图确认看涨偏向（DOL 指向上方旧高点 BSL）。
  2. 伦敦盘或纽约盘开盘初段，价格快速下砸跌破短期摆动低点（Swing Low），清扫卖方止损（Sell Stops），制造诱空假摔并打入深度折价区（Discount）。
  3. 切入 3 分钟或 1 分钟图，等待高能阳线收复失地并留下看涨公允价值缺口（BISI）。
  4. 回踩 3m BISI 挂单做多，止损设在假摔最低点下方，第一目标锁定上方未平的等高点 BSL。

````carousel
![Ep.08 [03:30] 外汇 3 分钟图跌破摆动低点进入折价区 FVG](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep08_forex_3m_fvg_discount.png)
<!-- slide -->
![Ep.08 [06:20] 伦敦杀手时区 (2:00-5:00 AM NY) 挂单与区间划分](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep08_london_killzone_bracket.png)
````

> [!NOTE]
> **外汇与股指差异提示**：外汇直盘受美元指数（DXY）直接制约。做多 EURUSD 时，必须同步核对 DXY 是否在溢价区承压下行，双向确认可大幅提升胜率。

---
"""

CHAPTERS[9] = """## Ep. 09：Power of 3（AMD 积累-操纵-派发）与纽约早盘机会（Power of 3 & NY PM Session）

### 9.1 日 K 线 OHLC 的底层解剖：Power of 3 (AMD) `[00:01 – 04:30]`
经典日 K 线由四部分组成：开盘价（O）、最高价（H）、最低价（L）、收盘价（C）。算法利用这四个价格点完成三阶段资金运作：
1. **积累阶段（Accumulation, A）**：以纽约午夜 00:00 开盘价为基准，在开盘价附近横盘震荡，诱导散户在狭窄区间建立双向仓位。
2. **操纵阶段（Manipulation, M / 犹大摆动 Judas Swing）**：
   - **看涨日（Bullish Day）**：开盘后必须先向下砸穿 00:00 开盘价，甚至跌破亚洲盘低点，诱骗散户追空，同时为机构收集廉价的多头筹码（最低价 L 形成）。
   - **看跌日（Bearish Day）**：开盘后必须先向上拉升越过 00:00 开盘价，刺穿早盘高点，诱骗散户追多，同时为机构在溢价区派发空单（最高价 H 形成）。
3. **派发/扩张阶段（Distribution, D）**：操纵完成后，算法开启单边主升浪或主跌浪，穿越全天交易区间，并收盘于全天极端位置附近。

### 9.2 纽约下午盘（13:30–15:30）单边逼空机会 `[04:30 – 11:00]`
- **13:30 时间窗口的特殊性**：上午盘多头获利了结后，市场在 12:00–13:00 陷入午休整固。
- 13:30 算法重新激活，往往先行微幅击穿午休低点完成最后一次洗盘（Micro Judas Swing），随后点燃看涨 FVG，展开全天第二波单边推进（Spooling），直奔早盘未平的高点。

````carousel
![Ep.09 [04:15] Power of 3（AMD 积累-操纵-派发）K 线阶段模型](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep09_power_of_3_amd_schema.png)
<!-- slide -->
![Ep.09 [09:50] 犹大秋千假摔诱空与下午盘单边反转](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep09_judas_swing_pm_rally.png)
````

> [!IMPORTANT]
> **基准线铁律**：看多时不买在 00:00 开盘价之上；看空时不卖在 00:00 开盘价之下。所有优质的入场机会，必然发生在开盘价的操纵侧！

---
"""

CHAPTERS[10] = """## Ep. 10：实现 Power of 3：结合经济日历与早盘双时段猎杀（Economic Calendar & The Open）

### 10.1 经济日历不是预测方向的工具，而是算法的时间扳机 `[00:01 – 05:00]`
- 散户关注宏观数据（非农、CPI、PPI、初请失业金）是高于预期还是低于预期。
- **ICT 核心真理**：算法早就在高周期图表上设定好了价格磁铁（DOL）；高影响新闻（ForexFactory 红色日历事件）只是**算法快速注入波动性以完成流动性猎杀的时间契机**。
- **时间锚点**：纽约时间 **08:30**（宏观经济数据集中发布）与 **09:30**（纽约证券交易所现货正式开盘）。

### 10.2 08:30 数据脉冲与 09:30 开盘的协同剧本 `[05:00 – 11:30]`
- **剧本 A（08:30 操纵，09:30 顺势派发）**：08:30 数据公布瞬间，价格产生 30–50 点的急速单针探顶或探底，清扫外部止损池完成 Judas Swing；09:30 现货开盘后直接走出高能位移，顺应大势展开单边行情。
- **剧本 B（08:30 蓄势，09:30 实施操纵）**：08:30 数据温和反弹制造虚假支撑，09:30 开盘后前 15 分钟（09:30–09:45）展开暴力洗盘扫除流动性，随后在 09:45–10:00 走出真正的市场结构破坏（MSS）。

````carousel
![Ep.10 [04:20] 经济日历 08:30 数据脉冲猎杀流动性示意](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep10_economic_calendar_830_spike.png)
<!-- slide -->
![Ep.10 [08:45] NQ 结合 AMD 与 08:30 数据脉冲图](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep10_power_of_3_nq_chart.png)
````

> [!CAUTION]
> 严禁在 08:29:55 盲目猜数据下注！必须等 08:30 脉冲释放完毕、价格结构稳定并在 5m/2m 图上留下清晰的 FVG 后，按规则从容挂单。

---
"""

CHAPTERS[11] = """## Ep. 11：纽约早盘 08:30 与 09:30 双重假动作精析（Reinforcing Past Lessons & Executions）

### 11.1 09:30 开盘双向扫荡（Whipsaw）的防御机制 `[00:01 – 05:00]`
- 现货开盘前 15 分钟往往充满极度混乱的算法交叉成交。散户极易在 09:30 看到大阳线急于追多，随即被 09:35 的暴跌直接止损。
- **强迫市场亮出真底牌**：在 09:30–09:45 期间，优秀的交易员保持冷静观察。只有当价格刺穿了 15 分钟风向标的高点或低点，并以大实体阴线跌穿短期波段低点时，真正的机构意图才被揭示。

### 11.2 3 分钟结构破坏（MSS）与二次确认挂单 `[05:00 – 11:00]`
- 当早盘经历 08:30 虚假冲高诱多后，价格在 09:30 之后再次向上测试并未能创出新高。
- **执行流程**：
  1. 确认 08:30 高点为流动性猎杀高点。
  2. 3 分钟图出现大实体阴线，果断砸破短期摆动低点（Swing Low），确立 Bearish MSS。
  3. 位移腿内形成明显的 3m SIBI（看跌公允价值缺口）。
  4. 价格反弹回踩该缺口上沿，提供绝佳的高盈亏比做空点位。

````carousel
![Ep.11 [03:40] 08:30 虚假冲高诱多陷阱](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep11_830_fake_rally_trap.png)
<!-- slide -->
![Ep.11 [08:15] 3m MSS 跌破与看跌 FVG 二次确认](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep11_3m_mss_fvg_confirmation.png)
````

> [!TIP]
> 记录复盘手帐时，重点标出从 09:30 现货开盘到 MSS 出现的时间间隔（通常在 09:40–10:10 之间），培养等待算法完成换手的耐心。

---
"""

print(f"handbook_ep06_11 ready with {len(CHAPTERS)} chapters")
