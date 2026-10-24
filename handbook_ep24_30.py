# -*- coding: utf-8 -*-
"""Handbook text for Episodes 24 to 30 (Module 5)."""

CHAPTERS = {}

CHAPTERS[24] = """## Ep. 24：刺穿高点后的迟滞反转与避坑准则（Avoid This & Enter Properly）

### 24.1 迟滞反转（Sluggish Reversal）与虚假结构破坏 `[00:01 – 05:00]`
- **散户常见陷阱**：价格刺穿了 15m 买方流动性池（BSL）后，并没有立刻爆发出大阴线下砸，而是在高位横盘纠缠、小阴小阳交替。散户往往急不可耐地在第一根小阴线就摸顶做空，结果被随后的二次微幅破高直接扫损。
- **迟滞反转的应对铁律**：若刺穿高点后无速度（No Velocity），**严禁提前进场**！必须把 MSS 判定线牢牢锁定在**推动价格创出全天最高点的那波上涨浪的真正起点（Key Swing Low）**。只有当大实体阴线干净利落地完全收在它下方，且留下明显的看跌 FVG 时，才确认空头接管。

### 24.2 强迫市场完成二次测试 `[05:00 – 09:30]`
- 若第一次回落软绵绵无位移，强迫市场向上走出二次冲顶（甚至假突破），等待二次冲顶耗尽买力后再寻找高质量看跌 FVG 做空。

````carousel
![Ep.24 [04:15] 避开假突破与刺穿高点后的迟滞反转](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep24_avoid_false_break_entry.png)
````

> [!CAUTION]
> 永远不要为了“多赚几个点”而在结构尚未被破坏前提前摸顶；等待真结构破坏入场虽然少赚 5 点，但能帮你避开 80% 的无谓止损。

---
"""

CHAPTERS[25] = """## Ep. 25：日内再平衡理论与旧低点清扫（Daily Rebalance Theory）

### 25.1 日内再平衡理论（Daily Rebalance Theory）核心思想 `[00:01 – 06:00]`
- 价格在单边扩张过程中留下的失衡区（FVG），本质上是算法以极高速度单边执行导致的“未完成撮合”。
- 当日内主要流动性池被清扫完毕后，算法会启动再平衡程序，精准回踩每一个前期未被回补的 FVG。
- **1 分钟微操细节**：限价单挂在 FVG 入口边缘时，允许预留 1–2 个 tick 的缓冲区（Buffer），防止由于微小点差导致未触碰成交而踏空。

### 25.2 旧低点卖方流动性清扫后的 V 型反抽 `[06:00 – 12:00]`
- 当价格砸穿前期日内显著低点（Old Lows）引爆海量 Sell Stops 后，若未能连续收出大阴线破位，说明算法在此处完成了多头对手盘收集，随即展开 V 型暴力再平衡。

````carousel
![Ep.25 [05:30] 日内再平衡理论与旧低点清扫](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep25_daily_rebalance_old_lows.png)
````

> [!TIP]
> 记录每一次 FVG 回抽是刚好触碰下沿、触碰 50% CE、还是完全填满，长期观察有助于掌握特定品种（NQ vs ES）的微观习惯。

---
"""

CHAPTERS[26] = """## Ep. 26：逆势回撤日与顺势扩张日的盘面特征对比（Counter Trend Tape Reading）

### 26.1 顺势扩张日（Trending Day）vs 逆势回撤日（Counter Trend Day）`[00:01 – 04:30]`
- **顺势扩张日**：早盘 Judas Swing 极小，开盘后一路单边狂飙；所有内部 FVG 回抽极浅甚至不回抽；止盈目标直接放远到更高维度的外部流动性池（日线/周线 BSL/SSL）。
- **逆势回撤日**：大级别仍处于空头，但由于连续数日大幅下挫远离高周期均值，日内展开深幅反弹。逆势单子往往伴随反复震荡、多重重叠，推进速度缓慢。

### 26.2 逆势交易的“小富即安”离场铁律 `[04:30 – 07:00]`
- 参与逆势反抽交易时，**绝对不能贪心**！
- 止盈目标必须严格限制在区间内部首个 **15m 看跌 FVG** 或 **50% 均衡位**；一旦价格触及该位置，立即全平落袋，绝不能留仓赌“趋势大反转”。

````carousel
![Ep.26 [03:20] 逆势回撤日走盘特征与快速止盈](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep26_counter_trend_tape_reading.png)
````

> [!IMPORTANT]
> 逆势做单如同在疾驰的列车前捡硬币。如果你是初学者，建议在逆势回撤日完全空仓观望，只做顺应日线偏向的交易！

---
"""

CHAPTERS[27] = """## Ep. 27：在震荡与消息扰动周中保持连贯盈利的秘诀（Counter Trend Ideas & Choppy Days）

### 27.1 震荡周与密集新闻周的制胜关键是“做减法” `[00:01 – 04:00]`
- 当一周内面临 CPI、PPI、初请、美联储决议多重重磅数据密集轰炸时，全周价格往往呈现多段短促无规律的假突破。
- 绝大多数散户的资金不是亏在单边趋势中，而是亏在震荡周里的频繁止损与追涨杀跌。
- **顶级纪律**：在震荡周中，没有出现标准纽约时间窗口（08:30/09:30）+ 15m 极端等高/等低点双向清扫 + 大实体位移 FVG，宁可全天 0 交易。

### 27.2 等低点清扫后的下午盘反转机会 `[04:00 – 06:00]`
- 震荡日中唯一值得参与的高确定性结构是：上午盘反复在低位磨出相对平头等低点（Equal Lows），13:30 下午盘快速下砸刺穿等低点诱空，随后以高能大阳线拉回并在折价区给出 5m 看涨 FVG，做一笔直奔早盘高点的反抽。

````carousel
![Ep.27 [03:15] 震荡周等低点清扫与下午盘反转](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep27_equal_lows_afternoon_reversal.png)
````

> [!TIP]
> 统计自己每月的亏损交易：超过 70% 的亏损往往发生在不该交易的震荡日。学会识别并主动放弃震荡日，账户盈利曲线就会发生质的飞跃。

---
"""

CHAPTERS[28] = """## Ep. 28：周内演化档案与周三/周四反转节点（Weekly Profile & Live Trade Execution）

### 28.1 周内演化档案（Weekly Profiles）的宏观规律 `[00:01 – 02:00]`
一周五个交易日并非均质随机，而是遵循标准的周内生命周期：
1. **周一（Monday）**：通常为积累阶段（Accumulation），在狭窄区间内震荡建立本周初始区间，甚少走出周内最大单边。
2. **周二或周三上午（Tuesday / Wednesday AM）**：周度操纵阶段（Weekly Manipulation）。算法往往借早盘宏观数据剧烈刺穿上周或本周初的高低点，**铸造出全周的最高价或最低价（High / Low of the Week）**！
3. **周三下午至周五（Wednesday PM – Friday）**：周度派发与主单边推进（Weekly Distribution），一路向周度终极流动性目标狂飙。

### 28.2 实战短线剥头皮的极致执行 `[02:00 – 04:00]`
- 锁定周二/周三确立的周内极值点后，日内顺势交易胜率大幅提升，依托 1m/2m FVG 进行快速剥头皮狙击。

````carousel
![Ep.28 [01:10] 周内演化档案与超短线实战执行](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep28_live_scalp_execution.png)
````

> [!NOTE]
> 牢记“周二/周三造全周极值”的统计规律。如果你在周三下午还在顺着周二被逆转的方向死扛，往往会承受全周最惨烈的单边亏损。

---
"""

CHAPTERS[29] = """## Ep. 29：早盘跳空缺口与美联储前窄幅震荡（Trading Bullish Narrow Range Days）

### 29.1 开盘跳空缺口（Opening Range Gap / NDOG / NWOG）的磁铁效应 `[00:01 – 03:00]`
- 期货市场的两个关键跳空缺口：
  - **新日开盘缺口（New Day Opening Gap, NDOG）**：前一日 17:00（或 16:00 现货收盘）与次日 18:00 开盘之间的跳空。
  - **新周开盘缺口（New Week Opening Gap, NWOG）**：周五 17:00 收盘与周日 18:00 开盘之间的巨大跳空。
- 这些缺口在日内具有巨大的磁吸力，价格在启动单边前，经常会先完全回补缺口或回踩缺口 50% 均衡位以确认支撑/阻力。

### 29.2 美联储前夕极窄波动率日（Narrow Range Days）的防御 `[03:00 – 05:00]`
- 在重大议息会议公布前，市场常常走出极窄幅度的横盘震荡（Narrow Range Day）。
- 此时应降低预期，严禁在区间中部开单，只允许在区间两端极值清扫后做超短线剥头皮。

````carousel
![Ep.29 [02:30] 早盘跳空缺口与美联储前窄幅震荡](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep29_pre_fed_narrow_range_1m.png)
````

> [!TIP]
> 在图表上用水平延长线标出最近几个交易日的 NDOG 和 NWOG，当价格接近它们时往往会产生强烈的价格反应。

---
"""

CHAPTERS[30] = """## Ep. 30：高阶走盘阅读与平衡价格区间（Tape Reading & Balanced Price Range）

### 30.1 平衡价格区间（Balanced Price Range, BPR）的高级机制 `[00:01 – 04:00]`
- **什么是 BPR？**
  - 当市场先出现一段极其迅速的看涨位移，留下一个看涨 FVG（BISI）；
  - 紧接着市场立刻以更猛烈的势头爆发出看跌位移，砸穿这个看涨 FVG，同时留下一个看跌 FVG（SIBI）。
  - **这两个相反方向的失衡区重叠交叉的价格区间，就被称为平衡价格区间（BPR）！**
- **BPR 的实战意义**：由于该区间在极短时间内被多空双方双向高速穿透，算法视其为已完成双向重新平衡。未来当价格反弹测试该 BPR 时，该重叠区将构成**极其强劲的阻力铁板**，价格往往触碰即掉头暴跌！

### 30.2 鲍威尔讲话剧烈波动下的订单块承接 `[04:00 – 06:30]`
- 鲍威尔新闻发布会（14:30 NY）启动后，第一波上下快速插针是流动性大扫荡。
- 待第一波脉冲释放完毕后，在底部深折价区的看涨 Order Block 结合 BPR 构成了极高盈亏比的二次狙击点。

````carousel
![Ep.30 [02:15] 鲍威尔讲话剧烈波动下的订单块承接与 BPR](/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/lesson-assets/ep30_fed_chair_volatility_ob.png)
````

> [!IMPORTANT]
> BPR 是失衡理论中最精妙的概念之一。当你在盘面上发现多空双重 FVG 发生交叉重合时，一定要重点标记这个高阶 PD Array！

---
"""

print(f"handbook_ep24_30 ready with {len(CHAPTERS)} chapters")
