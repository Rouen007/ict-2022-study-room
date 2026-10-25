#!/usr/bin/env python3
import json
import os
import re
import glob
import shutil
import hashlib
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSCRIPTS_DIR = os.path.join(BASE_DIR, "transcripts")
ARTIFACT_DIR = "/Users/rouen/.gemini/antigravity/brain/2f7883a2-405d-4596-a34a-2d0b4894d4c3"

# Complete metadata & Chinese study guide for all 37 episodes
LEGACY_EPISODE_META = {
    1: {
        "titleZh": "课程预期与股指期货合约底层规格",
        "module": "Module 1 · 核心模型与日内基石 (Ep 01–05)",
        "tags": ["NQ/ES规格", "Tick与Handle", "单波段预期"],
        "summaryZh": "确立本课程唯一目标：摒弃高频多空来回反手，专注在 E-mini 股指期货（NQ / ES）日内捕捉一段高确定性的单边价格腿（Intraday Price Leg）。明确 NQ（$20/点）与 ES（$50/点）及微型合约 MNQ/MES 的跳点换算与实时行情要求。",
        "keyPoints": [
            {"timeStr": "00:02", "seconds": 2, "titleZh": "高频多空反手 vs 课程单波段目标", "detailZh": "ICT 展示自己在 Thinkorswim 1 分钟图上的实盘高频交割单（早盘连续多空反手），但强调学员只需掌握最右侧从 14,798 空到 14,675 的那一段 123 点单边主跌浪。"},
            {"timeStr": "01:02", "seconds": 62, "titleZh": "三大迷你股指期货与微型合约选择", "detailZh": "核心标的为纳指期货（NQ）与标普期货（ES），道指（YM）较少参与。小资金或新手建议使用微型合约（MNQ / MES），跳点走势完全一致但杠杆仅 1/10。"},
            {"timeStr": "02:02", "seconds": 122, "titleZh": "Tick（最小跳动）与 Handle（整点）换算", "detailZh": "1 Handle（1整点）= 4 Ticks（.00 / .25 / .50 / .75）。NQ 每 Tick = $5，每整点 = $20；ES 每 Tick = $12.50，每整点 = $50。"},
            {"timeStr": "03:00", "seconds": 180, "titleZh": "TradingView 延时数据提醒与极简图表原则", "detailZh": "TradingView 默认期货行情有延时，实盘需订阅 CME 实时数据或配合经纪商终端。图表不挂任何滞后指标，保持纯裸 K + 流动性标注。"}
        ]
    },
    2: {
        "titleZh": "交易模型的四大核心要素（2022 模型总纲）",
        "module": "Module 1 · 核心模型与日内基石 (Ep 01–05)",
        "tags": ["Daily Bias", "BSL/SSL猎杀", "BMS/MSS", "FVG进场", "50%均衡矩阵"],
        "summaryZh": "首次完整拆解 ICT 2022 核心交易模型：1) 周/日线判断流动性吸引方向（DOL：旧高低点止损池或失衡区）；2) 1H/15m 观察诱空后向上猎杀相对等高点买方止损（BSL）；3) 切入 2m/1m 等待跌破短期波段低点（BMS）并在位移腿内找看跌 FVG 阳线回抽做空；4) 用 50% 斐波那契均衡点划分溢价/折价区，在折价区内部 FVG 与外部 SSL 分批止盈。",
        "keyPoints": [
            {"timeStr": "00:03", "seconds": 3, "titleZh": "要素一：周线与日线偏向（Weekly & Daily Bias）", "detailZh": "开盘前先看周线下一根 K 线倾向于向上还是向下扩张；日线价格像回形针被磁铁吸引一样，永远只奔向两类目标：1) 旧高/低点外的止损（Liquidity）；2) 失衡区（Imbalance / FVG）。"},
            {"timeStr": "04:06", "seconds": 246, "titleZh": "要素二：1H/15m 诱空陷阱与猎杀相对等高点（BSL）", "detailZh": "在日线看跌背景下，周五早盘价格先跌破短期小低点诱导散户追空（Sucker Play），随后掉头向上一举刺穿 14,820 相对等高点上方的买方止损（Buy Stops），为机构建立大额空单提供充足高价买盘对手方。"},
            {"timeStr": "08:07", "seconds": 487, "titleZh": "要素三：切入 2m/1m 识别结构跌破（BMS）与 FVG 挂单", "detailZh": "高频算法运行在 1m–3m 级别。当 15m 买方止损被扫后，在 2m 图等待价格跌破最近一个短期波段低点（14,808），并在这波下跌位移中找到三根 K 线不重叠的看跌 FVG（橙色框），在阳线向上回抽进 FVG 时做空，止损设在波段高点上方。"},
            {"timeStr": "12:09", "seconds": 729, "titleZh": "要素四：50% 均衡点（Equilibrium）与溢价/折价止盈矩阵", "detailZh": "从波段低点拉斐波那契到高点：50% 以上为溢价区（Premium，只做空），50% 以下为折价区（Discount，空单止盈区）。止盈目标设在折价区内的反向看涨 FVG（内部流动性）及下方旧低点卖方止损（外部流动性）。"}
        ]
    },
    3: {
        "titleZh": "内部区间流动性、市场结构转变（MSS）与订单块交付状态",
        "module": "Module 1 · 核心模型与日内基石 (Ep 01–05)",
        "tags": ["MSS vs MSB", "多空双向闭环", "Order Block", "交付状态改变", "纽约时间窗口"],
        "summaryZh": "界定日内市场结构转变（MSS）与跨日 MSB 的区别；在同一张 NQ 图表上完整演示先扫 14,600 SSL 做多至 14,820、再扫 14,820 BSL 反手做空的双向闭环；首次从算法 Spooling 角度定义 Order Block（连续阴/阳线开盘价被突破 = 交付状态的改变），并给出纽约时间三大流动性时段与作息铁律。",
        "keyPoints": [
            {"timeStr": "01:05", "seconds": 65, "titleZh": "日内 MSS（市场结构转变）与跨日 MSB 的区分", "detailZh": "MSS 专指日内短周期（1m/2m/5m）扫掉止损池后的反向结构突破，用于捕捉日内几十至上百点的波段，即使当天稍晚价格可能重返该区域。"},
            {"timeStr": "03:06", "seconds": 186, "titleZh": "10:20 看涨 MSS + 看涨 FVG 多头执行（扫 SSL 做多）", "detailZh": "价格跌破 14,600 卖方止损池后，强力拉升刺穿最近一个短期波段高点（14,634，无需收盘站上，盘中刺穿且留下三 K 线看涨 FVG 即可），阴线回踩 FVG 做多，直奔 14,820 相对等高点。"},
            {"timeStr": "06:06", "seconds": 366, "titleZh": "11:25 看跌 MSS + 看跌 FVG 空头执行（扫 BSL 做空）", "detailZh": "价格冲过 14,820 完成上方 Stop Raid 后跌破短期波段低点，回抽看跌 FVG 做空，目标指向 50% 均衡点下方的内部看涨 FVG 与卖方止损。"},
            {"timeStr": "08:07", "seconds": 487, "titleZh": "订单块本质：交付状态的改变（Change in the State of Delivery）", "detailZh": "价格并非被成交量推动，而是由算法连续递增/递减报价（Spooling）。刺穿卖方止损的一连串连续阴线构成看涨订单块，当价格向上突破该序列第一根阴线的开盘价时，交付状态正式由空转多（看跌订单块同理）。"},
            {"timeStr": "12:08", "seconds": 728, "titleZh": "纽约时间（NY Time）三大盘口高低点与午休禁区", "detailZh": "锁定 TradingView 时区为 New York (UTC-5/4)。标注亚盘（19:00–21:00）、伦敦盘（02:00–05:00）、纽约盘（07:00–10:00）高低点。股指早盘窗口 08:30–12:00，12:00–13:00 午休绝对禁入，下午盘关注 13:30–16:00。"}
        ]
    },
    4: {
        "titleZh": "实战案例精讲与 ICT 标准化复盘手帐规范",
        "module": "Module 1 · 核心模型与日内基石 (Ep 01–05)",
        "tags": ["ES 2m实战", "NQ 5m过滤", "强迫市场亮底牌", "Study Journal规范"],
        "summaryZh": "通过 1 月 26 日 ES 2m 与 1 月 27 日 NQ 5m 两个连续交易日案例，演示当价格扫掉 BSL 后如果第一波回落没有产生 FVG 或未跌破波段低点时，如何耐心过滤假动作、“强迫市场先亮出底牌”，并确立复盘手帐必记的四项量化指标。",
        "keyPoints": [
            {"timeStr": "00:02", "seconds": 2, "titleZh": "案例一（ES 2m）：08:30 启动猎杀与过滤无 FVG 的假回落", "detailZh": "08:30 后价格拉升扫掉前高 4,423.25 BSL；第一次小幅跌破短期低点时内部没有任何 FVG，按兵不动；随后二次冲高再下砸，同时出现 Bearish MSS + 清晰 FVG，回抽在 4,419 做空，直达折价区 4,381.75（37 个 ES 整点）。"},
            {"timeStr": "02:03", "seconds": 123, "titleZh": "ICT 复盘手帐（Study Journal）四项必记指标", "detailZh": "每张存档图表必须记录：1) MSS 到回抽填补 FVG 的耗时；2) 进场到触及目标位的持仓耗时；3) 进场后承受的最大逆向浮亏（Heat Weathered）；4) 整段行情总点数。"},
            {"timeStr": "03:35", "seconds": 215, "titleZh": "案例二（NQ 5m）：强迫市场亮底牌（Forcing the Market to Tip Its Hand）", "detailZh": "价格突破 14,282 相对等高点后第一次回调既未跌破波段低点也无 FVG，坚决不摸顶；等待二次拉升至 14,405 后长阴线真跌破并留下 14,335–14,345 看跌 FVG，回抽做空顺势击穿 14,127 均衡线，收割下方 14,044 与 14,018 目标。"}
        ]
    },
    5: {
        "titleZh": "日内订单流全景、三推诱多与下午盘 13:30 算力逼空",
        "module": "Module 1 · 核心模型与日内基石 (Ep 01–05)",
        "tags": ["合约换月H/M/U/Z", "15m风向标", "三推形态Three Drives", "大象跳泳池位移", "13:30宏与MOC"],
        "summaryZh": "详解期货季度交割月份代码（H/M/U/Z）与 Barchart 未平仓量换月法则；建立 15m 风向标图表（标注 08:30 左侧高低点与 12:00–13:00 午休禁区）；拆解早盘三推诱多（Three Drives）后的高能量位移（“大象跳进儿童泳池”）与下午盘 13:30 扫低点启动买方 Spooling 直至 15:40–16:00 MOC 收盘加速的全天剧本。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "股指期货月份代码（H/M/U/Z）与 Barchart 持仓量换月规则", "detailZh": "H=3月、M=6月、U=9月、Z=12月，第三个周五到期。到期前一周在 barchart.com 查看 Open Interest（未平仓量），一旦下季合约持仓量超越当季合约即刻换月。"},
            {"timeStr": "02:45", "seconds": 165, "titleZh": "15 分钟“风向标图表（Bellwether）”与波段高低点定义", "detailZh": "以 15m 图为日内骨架，画出 08:30 垂直线与 12:00–13:00 午休禁区，标出 08:30 左侧最近的 Swing High（三K线高点）与 Swing Low（三K线低点）作为早盘猎杀靶标。"},
            {"timeStr": "05:05", "seconds": 305, "titleZh": "早盘三推形态（Three Drives）与“大象跳进儿童泳池”式位移", "detailZh": "ES 5m 在 08:30 后走出三推抬高结构刺穿 4,514.50 伦敦高点，随后 09:30 美股开盘出现剧烈长阴线位移（如大象跳进儿童泳池般水花四溅）并留下看跌 FVG，回抽做空 15 分钟直达 4,482 低点。"},
            {"timeStr": "08:07", "seconds": 487, "titleZh": "下午盘 13:30 诱空猎杀、买方 Spooling 与 15:40–16:00 MOC 冲刺", "detailZh": "严守 12:00–13:00 午休空仓。13:30 后算法先向下刺穿下午盘第一个短期波段低点完成洗盘，随后突破早盘 4,515 相对等高点并留下看涨 FVG，开启连续阳线逼空（Spooling），并在 15:40–16:00 因收盘市价单（MOC）加速冲顶。"}
        ]
    },
    6: {
        "titleZh": "市场效率范式与机构订单流（聪明钱如何思考）",
        "module": "Module 2 · 日线偏向与 AMD 权力三段 (Ep 06–12)",
        "tags": ["市场效率范式", "机构对手盘", "真假突破", "双扫行情"],
        "summaryZh": "深入剖析散户视角与机构算法视角（Market Efficiency Paradigm）的根本对立：散户把等高/等低点当支撑阻力，而大资金必须利用这些位置的止损单作为建仓与平仓的流动性池。结合真实交割单演示早盘窄幅震荡诱空、美股开盘后冲高回落再拉升的机构订单流跟踪。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "市场效率范式（Market Efficiency Paradigm）与散户思维盲区", "detailZh": "传统技术分析教导的形态与指标往往把散户引导成为大资金的流动性提供者（对手盘）。理解每笔止损单背后都是强制市价单，才能看懂价格为何总去刺穿明显的高低点。"},
            {"timeStr": "06:00", "seconds": 360, "titleZh": "高时间框架缺口回补后的日内预期调整", "detailZh": "当价格已经回补了日线/4小时看跌失衡区并接近底部支撑时，不能再盲目死空，而要观察日内是否通过扫低点来完成多头建仓。"},
            {"timeStr": "12:00", "seconds": 720, "titleZh": "08:30 至 09:30 开盘前后的诱导与实盘订单管理", "detailZh": "拆解美股现货开盘前先向下假跌破、09:30 后向上拉升突破并回踩看涨 FVG 的完整实盘执行细节。"}
        ]
    },
    7: {
        "titleZh": "日线偏向（Daily Bias）与整固跳栏障碍（Consolidation Hurdles）",
        "module": "Module 2 · 日线偏向与 AMD 权力三段 (Ep 06–12)",
        "tags": ["Daily Bias难点", "大幅跳空/扩张后整固", "内部vs外部流动性循环"],
        "summaryZh": "专门解决学员最头疼的“日线偏向（Daily Bias）判断失误”问题：当市场经历大幅单边扩张后，往往进入数日的区间整固（Consolidation Hurdles）。讲解如何在日线大区间内部利用“外部流动性扫荡 → 内部 50% FVG 回补 → 外部流动性目标”的循环来确立每一天的偏方向。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "为什么大幅单边日之后很难直接延续趋势？", "detailZh": "大阳/大阴日之后常伴随内部回撤与震荡整固，此时需在日线及 4H/1H 级别标出大区间的高低点与 50% 均衡位。"},
            {"timeStr": "04:00", "seconds": 240, "titleZh": "外部止损池与内部 FVG 的乒乓交替法则", "detailZh": "一旦价格扫掉了某一侧的外部止损（BSL/SSL）却未能继续扩张，下一个高确定性磁铁必然是区间内部的 50% 均衡位及内部失衡区（Internal Range Liquidity）。"}
        ]
    },
    8: {
        "titleZh": "外汇市场应用：EURUSD 与 GBPUSD 伦敦/纽约狙击案例",
        "module": "Module 2 · 日线偏向与 AMD 权力三段 (Ep 06–12)",
        "tags": ["外汇通用性", "EURUSD", "GBPUSD", "Killzones联动"],
        "summaryZh": "证明 ICT 2022 模型并非只适用于美股指期货，在外汇直盘（EURUSD / GBPUSD）上同样精准有效。演示如何结合美元指数（DXY）偏向，在伦敦盘（02:00–05:00）与纽约外汇盘（07:00–10:00）运用完全相同的 Stop Raid + MSS + FVG 框架。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "外汇与股指共用同一套算法定价逻辑（IPDA）", "detailZh": "无论是股指还是外汇，算法在特定 Killzone 时间窗口内猎杀旧高低点并在 15m/5m/1m 留下 FVG 的机制完全一致。"},
            {"timeStr": "04:00", "seconds": 240, "titleZh": "EURUSD 与 GBPUSD 多周期嵌套实战拆解", "detailZh": "从日线/1H 流动性池定位，切入 15m/5m 观察伦敦开盘诱多/诱空后的结构转变与 FVG 进场。"}
        ]
    },
    9: {
        "titleZh": "Power of 3（AMD 积累-操纵-派发）与纽约早盘机会",
        "module": "Module 2 · 日线偏向与 AMD 权力三段 (Ep 06–12)",
        "tags": ["Power of 3 (AMD)", "午夜开盘价 00:00", "Judas Swing 犹大摆动"],
        "summaryZh": "引入 ICT 经典核心概念 Power of 3（Accumulation 积累 → Manipulation 操纵/诱多诱空 → Distribution 派发/真趋势）：以纽约午夜开盘价（00:00 NY Midnight Open）与 08:30 开盘价为基准，看懂为什么看跌日必须先在开盘价上方制造上影线（Judas Swing），看涨日必须先在开盘价下方制造下影线。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "日 K 线 OHLC 形成的底层解剖：Power of 3 (AMD)", "detailZh": "看涨日 K 线：开盘（Open）→ 向下操纵形成最低价（Low，积累多头）→ 向上派发拉升 → 收盘于高位（Close）。看跌日 K 线：开盘 → 向上操纵形成最高价（High，积累空头）→ 向下派发砸盘 → 收盘于低位。"},
            {"timeStr": "04:00", "seconds": 240, "titleZh": "纽约午夜 00:00 开盘价与 08:30 犹大摆动（Judas Swing）", "detailZh": "当天看空时，只等价格拉升到 00:00 午夜开盘价（及 08:30 开盘价）上方扫掉 BSL 再做空；当天看多时，只等价格砸到 00:00 开盘价下方扫掉 SSL 再做多。"}
        ]
    },
    10: {
        "titleZh": "实现 Power of 3：结合经济日历与早盘双时段猎杀",
        "module": "Module 2 · 日线偏向与 AMD 权力三段 (Ep 06–12)",
        "tags": ["经济日历驱动", "08:30数据 vs 09:30开盘", "SONAR算法脉冲"],
        "summaryZh": "教你如何把宏观经济日历（ForexFactory 高危数据时间）与 Power of 3 结合：经济数据本身不是方向的原因，而是算法用来快速扫掉流动性池、完成 Manipulation（操纵段）的时间触发器。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "用 ForexFactory 锁定每日高波动时间注入点", "detailZh": "不需要预测非农、CPI 或利率决议的利多利空，只需知道数据公布那一刻（如 08:30 或 10:00）算法会借机完成 Stop Raid。"},
            {"timeStr": "05:00", "seconds": 300, "titleZh": "08:30 期货数据脉冲与 09:30 美股现货开盘的协同剧本", "detailZh": "观察 08:30 如何先行构建诱导或第一重猎杀，09:30 现货开盘如何完成最终极值扫荡并启动全天主派发段（Distribution）。"}
        ]
    },
    11: {
        "titleZh": "纽约早盘 08:30 与 09:30 双重假动作与结构转变精析",
        "module": "Module 2 · 日线偏向与 AMD 权力三段 (Ep 06–12)",
        "tags": ["09:30开盘打桩机", "多重时间框架同向对齐", "反转确认细节"],
        "summaryZh": "通过高密度图表案例，深入剖析美股 09:30 现货开盘后常见的“上下双扫（Whipsaw）”陷阱，演示如何等待开盘噪音平息、真正刺穿 HTF 流动性池并走出干净 5m/2m/1m 位移与 FVG 后再从容扣扳机。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "为什么 09:30 开盘第一分钟极易发生双向扫损？", "detailZh": "现货开盘瞬间涌入大量隔夜指令，算法常先向一个方向假突破诱单，再向反方向刺穿真正的 15m 高低点。"},
            {"timeStr": "06:00", "seconds": 360, "titleZh": "5m / 3m / 2m / 1m 多周期 FVG 嵌套对比", "detailZh": "当大级别（15m/5m）与小级别（2m/1m）同时在同一价格带留下重叠 FVG 时，进场胜率与爆发力最高。"}
        ]
    },
    12: {
        "titleZh": "高阶市场结构拆解：中继结构（Intermediate Term）与止损铁律",
        "module": "Module 2 · 日线偏向与 AMD 权力三段 (Ep 06–12)",
        "tags": ["LTH/ITH/STH三层结构", "分形市场结构", "动态止损移动法则"],
        "summaryZh": "传授 ICT 极其核心的“三层波段高低点分类法”：长期高低点（LTH/LTL）、中期高低点（ITH/ITL）与短期高低点（STH/STL）。只要回撤形成的 ITH 没有突破前高、或完全嵌套在看跌 FVG 内部，市场结构就具有极强的单边延续性，借此实现精准加仓与保本止损移动。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "STH/STL（短期）、ITH/ITL（中期）、LTH/LTL（长期）三层结构定义", "detailZh": "1) 短期高低点（STH/STL）：基础三 K 线摆动极值；2) 中期高低点（ITH/ITL）：左右两侧各有一个更低的 STH（或更高的 STL）烘托的极值，或回抽高时间框架 FVG 形成的波段极值；3) 长期高低点（LTH/LTL）：大级别关键流动性反转点。"},
            {"timeStr": "05:00", "seconds": 300, "titleZh": "利用 ITH/ITL 判断趋势健康度与禁止过早移止损法则", "detailZh": "在空头趋势中，每一个反弹触及 FVG 形成的新 ITH 都不应被随后的反弹突破；只有当新的位移腿突破前低后，才将止损移至最近的 ITH 上方。"}
        ]
    },
    13: {
        "titleZh": "第 12 集三层市场结构的实战应用与回放",
        "module": "Module 3 · 订单块、多重失衡与多时段扩展 (Ep 13–20)",
        "tags": ["LTH/ITH/STH实战", "1m/5m分形联动", "金字塔加仓点"],
        "summaryZh": "将第 12 集的 LTH / ITH / STH 三层市场结构理论放入真实 K 线走盘中逐根标注，展示如何在 15m/5m 确立 LTH 与 ITH 后，切入 1m 图在每一次 STH 演化中顺势入场。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "在实盘图表中逐一标注 LTH、ITH 与 STH", "detailZh": "通过真实 NQ/ES 盘面演示：一旦高时间框架 FVG 孕育出 ITH，后续短周期的每一次小反弹都是顺势做空机会。"},
            {"timeStr": "08:00", "seconds": 480, "titleZh": "如何避免把正常的内部回撤误判为趋势反转", "detailZh": "只要最新的 ITH（空头中）或 ITL（多头中）未被破坏，短周期的小结构突破只是为了回补内部失衡，而非趋势终结。"}
        ]
    },
    14: {
        "titleZh": "单边波段中的多重 FVG 处里与日内实盘复盘",
        "module": "Module 3 · 订单块、多重失衡与多时段扩展 (Ep 13–20)",
        "tags": ["多重FVG选择", "溢价/折价过滤", "中继FVG vs 衰竭缺口"],
        "summaryZh": "当一波强劲位移中连续出现 2–3 个 Fair Value Gaps 时，到底该在哪一个 FVG 挂单？本集给出明确答案：结合 50% 均衡点（Equilibrium）与订单块重合度，优先选择深入溢价区（做空）或折价区（做多）的 FVG。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "位移腿中出现多个 FVG 时的优先级排序", "detailZh": "处于 50% Equilibrium 极值侧（做空选上方溢价区 FVG，做多选下方折价区 FVG）且紧贴 Order Block 的缺口最具机构防守价值。"},
            {"timeStr": "04:00", "seconds": 240, "titleZh": "什么情况下算法只回踩第一个浅层 FVG 就直接加速？", "detailZh": "当价格已经完成深度回撤并在 ITH/ITL 处启动第二波加速腿（Expansion Leg）时，浅层 FVG（Breakaway/Measuring Gap）往往直接充当加速跳板。"}
        ]
    },
    15: {
        "titleZh": "实时走盘复盘：早盘剥头皮与订单块配合 FVG",
        "module": "Module 3 · 订单块、多重失衡与多时段扩展 (Ep 13–20)",
        "tags": ["Live Tape Reading", "OB+FVG共振", "早盘快速落袋"],
        "summaryZh": "展示一段实时录屏的早盘走盘分析，重点讲解当看涨/看跌订单块（Order Block）与公允价值缺口（FVG）发生空间重叠时，如何把止损收紧、提高盈亏比。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "Order Block 与 FVG 重叠区的黄金进场位", "detailZh": "当 FVG 内部恰好包含前期订单块的开盘价或中轴（Mean Threshold 50%）时，价格往往在此出现毫秒级精准反应。"}
        ]
    },
    16: {
        "titleZh": "同一交易日内的多重交易设置（早盘 + 下午盘连击）",
        "module": "Module 3 · 订单块、多重失衡与多时段扩展 (Ep 13–20)",
        "tags": ["全天多次机会", "早盘波段+下午盘波段", "流动性重置"],
        "summaryZh": "拆解在一个趋势流畅或宽幅震荡的交易日里，如何在早盘（08:30–11:00）先吃一段波段，午休后在下午盘（13:30–15:30）利用新的流动性池重置再抓第二段独立机会。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "早盘目标达成后的离场与等待午休重置", "detailZh": "早盘一旦触及预设的折价/溢价目标池即刻平仓，绝不把盈利单拖进 12:00–13:00 午休区。"},
            {"timeStr": "04:00", "seconds": 240, "titleZh": "下午盘重新划定 Dealing Range 与二次入场", "detailZh": "以早盘形成的新高点与新低点重新拉取 50% 均衡线，在 13:30 后寻找二次 MSS + FVG 机会。"}
        ]
    },
    17: {
        "titleZh": "外汇日内多周期实战（DXY 联动与伦敦/纽约重叠区）",
        "module": "Module 3 · 订单块、多重失衡与多时段扩展 (Ep 13–20)",
        "tags": ["DXY美元指数", "外汇纽约盘", "BISI与SIBI"],
        "summaryZh": "针对外汇交易者深入演示如何先看美元指数（DXY）的日线/4H 失衡与流动性方向，再反向映射至非美货币对（EURUSD / GBPUSD），利用纽约早盘 07:00–10:00 的回撤狙击主趋势。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "美元指数（DXY）与非美货币的镜像印证", "detailZh": "当 DXY 正在奔向日线 BSL（看涨美元）时，在 EURUSD / GBPUSD 上只寻找冲高扫掉短期高点后的看跌 MSS + SIBI（看跌 FVG）做空机会。"},
            {"timeStr": "06:00", "seconds": 360, "titleZh": "伦敦盘确立日内极值后，纽约盘如何回撤续势", "detailZh": "若伦敦盘已走出强劲首波位移，纽约盘（07:00–08:30）常回撤至伦敦波段的 50%–70.5% OTE 区及内部 FVG 提供二次上车点。"}
        ]
    },
    18: {
        "titleZh": "多门资产跨周期推演：从日线 FVG 到 1 分钟狙击",
        "module": "Module 3 · 订单块、多重失衡与多时段扩展 (Ep 13–20)",
        "tags": ["Top-Down全流程", "HTF PD Array", "LTF精确触发"],
        "summaryZh": "系统串联高时间框架 PD Array（溢价/折价矩阵中的订单块、FVG、旧高低点）与低时间框架执行：只有当价格触碰高时间框架关键位（HTF Key Level）的那一刻，1m/2m 图上的 MSS + FVG 才具备真正的机构背书。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "不要在真空地带找 1 分钟 FVG！", "detailZh": "新手最大的亏损来源是在没有任何 15m/1H/Daily 关键流动性或失衡区配合的区间中部，随便找一个 1m 小缺口频繁交易。"},
            {"timeStr": "05:00", "seconds": 300, "titleZh": "HTF 关键位触碰 + LTF 结构转变的双重锁死", "detailZh": "耐心等待价格刺入 1H/15m 的 FVG 或扫掉 1H/15m 高低点后，再降维到 1m/2m 寻找反向 MSS。"}
        ]
    },
    19: {
        "titleZh": "趋势延续 vs 反转猎杀：如何读懂日内叙事（Narrative）",
        "module": "Module 3 · 订单块、多重失衡与多时段扩展 (Ep 13–20)",
        "tags": ["Market Narrative", "早晨叙事构建", "假反转识别"],
        "summaryZh": "深入讲解 ICT 常说的“市场叙事（Narrative）”：不仅要看图表上的线和框，更要结合当前所处的周内天数（周二/周三常形成周高低点）、经济数据节点以及未回补失衡，构建合理的日内剧本。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "什么是机构日内叙事（Intraday Narrative）？", "detailZh": "回答三个问题：1) 价格刚刚从哪个流动性池出来？2) 下一个最具吸引力的反向池子在哪？3) 当前时间窗口（8:30/9:30/13:30）算法需要先诱骗哪一方？"},
            {"timeStr": "09:00", "seconds": 540, "titleZh": "连续案例对比：顺势回踩单与逆势摸顶单的盈亏差异", "detailZh": "顺应日线/4H 主交付方向的日内波段往往势如破竹，而逆大势的日内反弹一旦触及内部 50% FVG 就会迅速夭折。"}
        ]
    },
    20: {
        "titleZh": "伦敦盘与纽约盘接力剖析（早盘大幅单边后的应对）",
        "module": "Module 3 · 订单块、多重失衡与多时段扩展 (Ep 13–20)",
        "tags": ["伦敦单边透支", "纽约盘盘整与二次启动", "隔夜波幅评估"],
        "summaryZh": "解决一个常见痛点：如果夜盘/伦敦盘（02:00–05:00）已经走出了一大波单边行情、提前吃掉了原本预期的目标位，到了纽约早盘（08:30–09:30）该如何应对？",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "夜盘/伦敦盘透支波幅后的纽约早盘特征", "detailZh": "若伦敦盘已大幅扩张并触及日线级目标，纽约早盘 08:30–10:00 往往先进行深幅回撤（回补伦敦盘留下的 50% 与 FVG）或进入箱体震荡，切忌在开盘高点盲目追涨杀跌。"}
        ]
    },
    21: {
        "titleZh": "跨市场相关性与 SMT 背离（Smart Money Technique）",
        "module": "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "tags": ["SMT Divergence", "ES vs NQ vs YM背离", "机构吸筹/派发铁证"],
        "summaryZh": "正式引入威力巨大的跨市场验证武器——SMT 背离（Smart Money Technique Divergence）：对比高度正相关的三大股指（ES、NQ、YM）。当某一个指数创出新高（扫掉 BSL），而另一个指数却未能同步创出新高（形成 Lower High）时，暴露出聪明钱正在暗中派发做空（底部不创新低同理）。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "顶部看跌 SMT 背离与底部看涨 SMT 背离的判定标准", "detailZh": "顶部看跌 SMT：在关键阻力/BSL 处，NQ 刺穿前高而 ES 未能刺穿前高（或反之），说明上涨并非全市场真实买盘，而是针对单一品种的止损猎杀。底部看涨 SMT：在关键支撑/SSL 处，一个品种破前低而另一个品种守住前低形成更高低点。"},
            {"timeStr": "04:00", "seconds": 240, "titleZh": "用 SMT 选出当天最强势做多品种或最弱势做空品种", "detailZh": "做空时选顶部没能创新高（相对更弱）的那个指数；做多时选底部拒绝创新低（相对更强）的那个指数！"}
        ]
    },
    22: {
        "titleZh": "美联储利率决议（FOMC）与特种消息日交易法则",
        "module": "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "tags": ["FOMC利率决议", "14:00与14:30双脉冲", "消息日风控纪律"],
        "summaryZh": "详解美联储 FOMC 议息日及重大新闻日的特殊盘面结构：FOMC 当天早盘往往极度压缩或走假方向，下午 14:00 公布声明走出第一波假突破（扫止损），14:30 鲍威尔新闻发布会才走出真正的反转或主趋势。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "FOMC 当天的生存铁律：14:00 第一波脉冲绝不追单", "detailZh": "14:00 利率决议公布瞬间点差扩大、算法上下扫盘清场，必须等 14:30 发布会开始、某一侧关键流动性被彻底扫清并出现 5m/1m MSS + FVG 后再决定是否轻仓参与。"}
        ]
    },
    23: {
        "titleZh": "FOMC 次日行情延续与周四/周五流动性收尾",
        "module": "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "tags": ["FOMC次日剧本", "周四反转/延续", "多周期FVG回补"],
        "summaryZh": "复盘 FOMC 议息日次日（周四）的价格行为：市场消化完前一日剧烈波动后，如何利用前一日大幅拉升/下砸留下的日内失衡区（FVG）与高低点构建极具规律性的次日交易模型。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "重大消息日次日的均衡回归与趋势延续", "detailZh": "FOMC 制造的大区间确立了新的高低点边界，次日早盘往往先回抽该区间 50% 均衡点或前一日尾盘 FVG，再沿主方向继续推进。"}
        ]
    },
    24: {
        "titleZh": "刺穿高点后的迟滞反转与耐心等待二次确认",
        "module": "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "tags": ["二次确认", "高位盘整派发", "Breaker破位块雏形"],
        "summaryZh": "剖析当价格刺穿高时间框架买方流动性后，并未立刻走出 V 型暴跌，而是在高位反复震荡构筑派发区时的应对策略：如何锁定真正导致结构崩塌的那根位移腿。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "高位派发耗时较长时的结构锚点选择", "detailZh": "不要在顶部小震荡箱体内部过早猜顶，把结构跌破线（MSS）牢牢设在推动最后一次冲高的那个关键波段低点下方。"}
        ]
    },
    25: {
        "titleZh": "实盘走盘片段与短周期 FVG 精准进出场细节",
        "module": "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "tags": ["1m极速执行", "分批止盈技巧", "余仓保护"],
        "summaryZh": "通过精简实盘案例，展示在 1 分钟图上看到位移与 FVG 形成后，如何在几根 K 线内完成挂单、成交、承受微小回撤并在首个流动性池减仓落袋。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "挂单位置微调：FVG 上沿/下沿 vs 50% 中轴（Consequent Encroachment）", "detailZh": "最稳妥的成交位是 FVG 的入口边缘（做空取下沿、做多取上沿）再留 1–2 ticks 缓冲；若追求极致盈亏比则关注 FVG 的 50% 中轴（CE）。"}
        ]
    },
    26: {
        "titleZh": "逆势回撤日与顺势扩张日的盘面特征对比",
        "module": "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "tags": ["趋势日 vs 震荡日", "预期管理", "目标缩放"],
        "summaryZh": "教你根据当前价格所处的日线周期位置，提前调整当天的盈利预期：处于日线顺势扩张阶段时可以博取外部远端目标；处于日线回撤修整日时，见好就收于内部 50% 流动性。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "什么时候该拿大波段，什么时候该吃一口就跑？", "detailZh": "当周线、日线、1H 与日内方向完全同向时拿向外部高低点；当与日线主趋势相反或处于大行情次日时，触及首个 15m 内部 FVG 即平仓 80%–100%。"}
        ]
    },
    27: {
        "titleZh": "在震荡与消息扰动周中保持连贯盈利的秘诀",
        "module": "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "tags": ["高难度周应对", "降低交易频率", "只做A+级设置"],
        "summaryZh": "复盘一周内既有 CPI 又有密集官员讲话的复杂行情：强调“不是每天都必须交易”，只要死守 08:30/09:30 扫除明显流动性池 + 干净位移 FVG 这一条铁律，就能避开 90% 的绞肉机行情。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "过滤垃圾时间的黄金准则", "detailZh": "如果图表上高低点模糊、K 线大量重叠、双向都没去触碰清晰的 15m/1H 止损池，最佳操作就是关掉交易软件。"}
        ]
    },
    28: {
        "titleZh": "周内演化档案（Weekly Profile）与周三/周四反转节点",
        "module": "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "tags": ["Weekly Profile", "周二/周三周极值", "周线Power of 3"],
        "summaryZh": "将日内的 Power of 3（AMD）放大到整周维度（Weekly Profile）：周一往往是小幅积累，周二或周三常走出全周的最高点或最低点（周级别 Manipulation），随后周三下午至周五走出顺周线主方向的单边派发。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "周线级别的 AMD 与周中反转窗口", "detailZh": "观察周一至周三上午是否一直在逆周线主趋势诱多/诱空并刺穿日线级关键位；一旦在周二/周三触及日线 PD Array 并发生 1H/15m MSS，周四与周五往往提供极顺畅的波段机会。"}
        ]
    },
    29: {
        "titleZh": "早盘跳空缺口（Opening Range Gap / NDOG）与回补规律",
        "module": "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "tags": ["开盘缺口回补", "NDOG/NWOG", "09:30现货缺口磁铁"],
        "summaryZh": "讲解美股 09:30 开盘与前一日 16:00 收盘价之间的跳空缺口（Opening Range Gap），以及新日/新周开盘缺口（NDOG / NWOG）如何作为日内极高权重的价格磁铁与支撑阻力参考位。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "16:00 收盘价至次日 09:30 开盘价缺口（Opening Range Gap）", "detailZh": "当早盘出现明显跳空高开或低开时，前一日 16:00 现货收盘价往往成为早盘回补的第一目标位，或回补 50%（CE）后启动反向趋势。"}
        ]
    },
    30: {
        "titleZh": "高阶走盘阅读（Tape Reading）与多周期 PD Array 矩阵对齐",
        "module": "Module 5 · 实盘走盘回放、风控与终极闭环 (Ep 30–37)",
        "tags": ["PD Array矩阵", "BPR平衡价格区间", "Breaker破位块"],
        "summaryZh": "进入课程尾声的高阶综合阶段：系统梳理溢价/折价矩阵中的各类 PD Arrays（旧高/低点、Breaker 破位块、Order Block 订单块、FVG 失衡区、Mitigation 缓解块），演示价格如何在这些层级间像阶梯一样精确跳跃。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "PD Array 优先级矩阵与 BPR（Balanced Price Range）", "detailZh": "当一段快速拉升留下看涨 FVG、随即立刻被一段快速下砸留下看跌 FVG 双向覆盖时，两者重叠区构成极具阻力的平衡价格区间（BPR）。"}
        ]
    },
    31: {
        "titleZh": "空头市中的高胜率反弹做空与下午盘尾盘收割",
        "module": "Module 5 · 实盘走盘回放、风控与终极闭环 (Ep 30–37)",
        "tags": ["熊市做空法则", "溢价区共振", "尾盘加速"],
        "summaryZh": "针对 2022 年纳指/标普的空头大周期背景，总结为什么在日线空头排列下“逢反弹进溢价区 FVG 做空”是资金曲线最平滑的策略。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "顺应宏观日线空头流向的日内复利", "detailZh": "在日线不断创出新低的熊市阶段，每一次日内早盘向上扫掉前一日高点或早盘高点的拉升，都是机构在溢价区派发空单的礼物。"}
        ]
    },
    32: {
        "titleZh": "1 分钟极致微操：如何在大级别 FVG 内部寻找 1m 触发",
        "module": "Module 5 · 实盘走盘回放、风控与终极闭环 (Ep 30–37)",
        "tags": ["15m FVG + 1m MSS", "分形嵌套", "极小止损高盈亏比"],
        "summaryZh": "解决“15 分钟 FVG 跨度太大、直接挂单止损太宽”的实战难题：教你等待价格进入 15 分钟 FVG 内部后，切到 1 分钟图等待出现微型 MSS + 1m FVG 再入场，将止损压缩到极致。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "用 15m/5m 缺口定位置，用 1m 结构定扳机", "detailZh": "当 15m FVG 宽度超过 20–30 点时，不必在边缘盲挂；等价格刺入 15m FVG（尤其是触及其中轴 50% CE）并在 1m 图走出反向 MSS + 1m FVG 时进场。"}
        ]
    },
    33: {
        "titleZh": "交易心理学、亏损恢复与一致性执行纪律",
        "module": "Module 5 · 实盘走盘回放、风控与终极闭环 (Ep 30–37)",
        "tags": ["交易心理", "遭遇止损后应对", "仓位减半法则"],
        "summaryZh": "直面实盘交易中最真实的心理挑战：当严格按照模型执行却依然遇到止损（或连续两笔亏损）时，如何防止情绪失控（Tilt）与报复性重仓？给出 ICT 经典的“亏损后仓位减半”风控铁律。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "止损后的风控降档法则（Cutting Risk After a Loss）", "detailZh": "单日一旦出现一笔止损，当天若没有绝对 A+ 级机会直接收工；若遭遇连续亏损，下一笔交易必须将风险仓位砍半，直到用减半仓位重新赢回前一次亏损额的一半以上，才允许恢复标准仓位。"}
        ]
    },
    34: {
        "titleZh": "周内多日连续案例串讲：看懂流动性的跨日传递",
        "module": "Module 5 · 实盘走盘回放、风控与终极闭环 (Ep 30–37)",
        "tags": ["跨日流动性地图", "前日高低点PDH/PDL", "前周高低点PWH/PWL"],
        "summaryZh": "把周一到周五的 15m 图拼接成一张完整的跨日流动性地图，重点演示前一日最高价（PDH）与前一日最低价（PDL）如何成为次日早盘算法最优先猎杀的目标。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "PDH（前日高点）与 PDL（前日低点）的核心磁吸效应", "detailZh": "每天开盘前先标出 PDH 与 PDL。如果早盘价格距离 PDH/PDL 很近，08:30/09:30 极大概率会先去刺穿它，从而触发日内反转或加速。"}
        ]
    },
    35: {
        "titleZh": "无序震荡市（Choppy Market）的识别与防御策略",
        "module": "Module 5 · 实盘走盘回放、风控与终极闭环 (Ep 30–37)",
        "tags": ["震荡市防御", "Seek & Destroy模式", "保住本金"],
        "summaryZh": "教你识别最危险的“搜寻与摧毁（Seek & Destroy）”日内盘面：早盘先把上方高点扫掉、紧接着把下方低点扫掉，随后反复回到区间 50% 中轴拉锯。掌握识别信号，做到及时空仓观望。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "Seek & Destroy（双向扫损绞肉机）的典型征兆", "detailZh": "通常出现在重大宏观数据（非农/CPI/FOMC）公布前夕，或前一日刚经历极端超大幅度单边波动之后。一旦发现早盘扫完高点跌回中轴、扫完低点又拉回中轴且无持续跟进，立即停止当日交易。"}
        ]
    },
    36: {
        "titleZh": "完整实盘执行演示：从盘前推演到挂单止盈全过程",
        "module": "Module 5 · 实盘走盘回放、风控与终极闭环 (Ep 30–37)",
        "tags": ["全流程实盘", "盘前-盘中-盘后闭环", "止盈分批执行"],
        "summaryZh": "将前 35 集的所有模块融会贯通，完整回放一笔标准 ICT 2022 模型交易从盘前 HTF 分析、等待开盘时间窗口、观察流动性刺穿、确认 LTF MSS 与 FVG、挂单入场到分批止盈平仓的每一秒决策细节。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "把复杂分析简化为机械化的 6 步清单", "detailZh": "盘前看清大方向与流动性池，盘中只等“时间窗口 + 扫池子 + 位移 MSS + 溢价/折价 FVG”四个条件同时亮绿灯。"}
        ]
    },
    37: {
        "titleZh": "大结局：2022 指导课终极复盘、回测方法论与职业交易之路",
        "module": "Module 5 · 实盘走盘回放、风控与终极闭环 (Ep 30–37)",
        "tags": ["终极总结", "百图回测计划", "模拟到实盘进阶"],
        "summaryZh": "全剧终章：总结 ICT 2022 模型的极简核心哲学——你不需要预测市场的每一根 K 线，只需要属于你的那一个高确定性模型（One Model for Life）。布置模拟盘连续盈利验证与个人复盘手帐图库建设路线图。",
        "keyPoints": [
            {"timeStr": "00:01", "seconds": 1, "titleZh": "构建属于你自己的 100 张标注图库（Study Deck）", "detailZh": "不要听信任何人的嘴炮，亲手在 TradingView 上把过去数月的每一天按 Ep.01–05 的标准截图标注归档，建立肌肉记忆。"},
            {"timeStr": "05:00", "seconds": 300, "titleZh": "从模拟盘（Demo）到微型合约（MNQ/MES）再到标准合约的晋级阶梯", "detailZh": "先在模拟账户或 1 手微型合约上实现连续数周稳定正向执行，用利润垫和纪律证明自己，再逐步放大合约手数。"}
        ]
    }
}

# Keyframes for Ep 01 - Ep 05 (22 high-res 1080p screenshots)
EPISODE_KEYFRAMES = {
    1: [
        {
            "id": "ep01_1",
            "file": "ep01_tos_live_executions.png",
            "timeStr": "00:40",
            "seconds": 40,
            "timeframe": "1m TOS",
            "titleZh": "Thinkorswim 1分钟实盘高频多空交割记录",
            "captionZh": "ICT 展示自己早盘在 10:30–11:45 之间连续做多、反手做空、再做多、再在顶部 14,798.25 做空的实盘成交标签。"
        },
        {
            "id": "ep01_2",
            "file": "ep01_target_one_big_leg.png",
            "timeStr": "04:50",
            "seconds": 290,
            "timeframe": "1m TOS",
            "titleZh": "课程核心目标：只抓右侧 14,798 → 14,675 单边主跌浪",
            "captionZh": "摒弃左侧复杂的短线折返，2022 模型只聚焦最右侧那一段干净利落的 123 点（$2,460/手）日内主波段。"
        }
    ],
    2: [
        {
            "id": "ep02_1",
            "file": "ep02_weekly_bias_candle.png",
            "timeStr": "00:45",
            "seconds": 45,
            "timeframe": "1W 周线",
            "mtfOrder": 1,
            "titleZh": "步骤 1（1W 周线）：评估周线向下扩张惯性（Weekly Bias）",
            "captionZh": "在每周开始前，先判断下一根周线更有可能向哪个方向扩张。此处 NQ 周线破位下行，确立周内逢高做空基调。"
        },
        {
            "id": "ep02_2",
            "file": "ep02_daily_ssl_and_imbalance.png",
            "timeStr": "01:55",
            "seconds": 115,
            "timeframe": "1D 日线",
            "mtfOrder": 2,
            "titleZh": "步骤 2（1D 日线）：锁定下方 14,366.75 旧低点卖方流动性池（DOL）",
            "captionZh": "日线前期失衡已回补，下方 2021 年 10 月旧低点（14,366.75 红线）下方堆积着大量 Sell Stops，像磁铁一样吸引价格下行。"
        },
        {
            "id": "ep02_3",
            "file": "ep02_hourly_induce_shorts_run_bsl.png",
            "timeStr": "04:55",
            "seconds": 295,
            "timeframe": "1H 小时线",
            "mtfOrder": 3,
            "titleZh": "步骤 3（1H 小时线）：早盘先破小低点诱空，再反抽拉升扫上方等高点",
            "captionZh": "周五早盘先跌破短期震荡低点（诱导突破派追空），随后迅速拉起去攻击上方相对等高点。"
        },
        {
            "id": "ep02_4",
            "file": "ep02_15m_equal_highs_stop_hunt.png",
            "timeStr": "07:20",
            "seconds": 440,
            "timeframe": "15m 十五分",
            "mtfOrder": 4,
            "titleZh": "步骤 4（15m 十五分）：先扫 14,600 Sell Stops，再猎杀 14,820 Buy Stops",
            "captionZh": "散户把 14,820 相对等高点视为强阻力并在此放置空头止损（Buy Stops）。聪明钱拉升刺穿 14,820，利用涌入的买单建立大额空头头寸。"
        },
        {
            "id": "ep02_5",
            "file": "ep02_2m_bms_and_fvg_entry.png",
            "timeStr": "11:35",
            "seconds": 695,
            "timeframe": "2m 两分钟",
            "mtfOrder": 5,
            "titleZh": "步骤 5（2m 进场触发）：跌破波段低点（BMS）+ 橙色看跌 FVG 回抽做空",
            "captionZh": "扫完 14,820 BSL 后切入 2m 图，等待跌破短期波段低点（14,808），并在位移腿内找到三 K 线不重叠的橙色 FVG，在阳线回抽时挂单做空。"
        },
        {
            "id": "ep02_6",
            "file": "ep02_2m_fib_equilibrium_matrix.png",
            "timeStr": "13:15",
            "seconds": 795,
            "timeframe": "2m 均衡矩阵",
            "mtfOrder": 6,
            "titleZh": "步骤 6（2m 溢价/折价区）：50% 斐波那契均衡点（Equilibrium）划分",
            "captionZh": "从波段低点（14,535）拉到高点（14,855）：50% 以上红色区为溢价区（Premium，只做空），50% 以下绿色区为折价区（Discount，空单平仓区）。"
        },
        {
            "id": "ep02_7",
            "file": "ep02_2m_full_setup_annotated.png",
            "timeStr": "15:05",
            "seconds": 905,
            "timeframe": "2m 止盈目标",
            "mtfOrder": 7,
            "titleZh": "步骤 7（2m 完整闭环）：在折价区内部看涨失衡（14,680 & 14,650）精准止盈",
            "captionZh": "空单从溢价区橙色 FVG 进场后，第一、二止盈目标设在 50% 以下折价区内部的看涨 FVG（蓝线）与下方 Sell Stops。"
        }
    ],
    3: [
        {
            "id": "ep03_1",
            "file": "ep03_15m_ssl_and_bsl_pools.png",
            "timeStr": "02:35",
            "seconds": 155,
            "timeframe": "15m 十五分",
            "mtfOrder": 1,
            "titleZh": "15m 盘口全景：08:30 右侧的 14,600 SSL 与 14,820 BSL 两大池子",
            "captionZh": "早盘 08:30 垂直线右侧，价格先向下刺穿 14,600 Sellside Liquidity（感叹号），随后拉升刺穿 14,820 Buyside Liquidity。"
        },
        {
            "id": "ep03_2",
            "file": "ep03_2m_bullish_mss_fvg_ob.png",
            "timeStr": "05:10",
            "seconds": 310,
            "timeframe": "2m 多头模型",
            "mtfOrder": 2,
            "titleZh": "2m 多头闭环：10:20 扫下方 Stop Raid 后突破短期高点（Bullish MSS）+ 回踩 FVG 做多",
            "captionZh": "扫掉 14,600 SSL 后，价格向上刺穿 14,634 波段高点（橙色小三角）触发 Bullish MSS，回踩橙色灯泡处的看涨 FVG 进场做多，直奔 14,820！"
        },
        {
            "id": "ep03_3",
            "file": "ep03_2m_bearish_mss_fvg_targets.png",
            "timeStr": "06:45",
            "seconds": 405,
            "timeframe": "2m 空头模型",
            "mtfOrder": 3,
            "titleZh": "2m 空头闭环：11:25 扫上方 14,820 Stop Raid 后触发 Bearish MSS + 回抽 FVG 做空",
            "captionZh": "多单在 14,820 止盈后，价格扫完 BSL 并跌破短期波段低点触发 Bearish MSS，回抽上方橙色灯泡看跌 FVG 反手做空。"
        },
        {
            "id": "ep03_4",
            "file": "ep03_1m_orderblock_state_of_delivery.png",
            "timeStr": "09:30",
            "seconds": 570,
            "timeframe": "1m 订单块机制",
            "mtfOrder": 4,
            "titleZh": "1m 深度拆解：连续阳线构成看跌订单块，跌破开盘价即改变交付状态",
            "captionZh": "冲高刺穿 BSL 的一连串连续阳线构成看跌 Order Block；当价格向下跌破这串阳线第一根 K 线的开盘价时，算法交付状态正式由买转卖。"
        },
        {
            "id": "ep03_5",
            "file": "ep03_1m_full_lipstick_chart.png",
            "timeStr": "11:45",
            "seconds": 705,
            "timeframe": "1m 全标注图",
            "mtfOrder": 5,
            "titleZh": "1m 完整标注图（Lipstick on the Chart）：比 2m 更早、更紧凑的双向信号",
            "captionZh": "在 1 分钟级别上，无论是底部的看涨订单块 + FVG 还是顶部的看跌订单块 + FVG，结构转折点都比 2m 图更早浮现。"
        }
    ],
    4: [
        {
            "id": "ep04_1",
            "file": "ep04_es_2m_equilibrium_overview.png",
            "timeStr": "00:45",
            "seconds": 45,
            "timeframe": "ES 2m 全景",
            "mtfOrder": 1,
            "titleZh": "案例一（ES 2m 全景）：50% 均衡线（4,392）上方猎杀 BSL 后直达 4,381.75",
            "captionZh": "08:30 垂直线后价格拉升至溢价区扫掉 4,423.25 买方流动性，随后空头波段一路派发至折价区 4,381.75 旧低点。"
        },
        {
            "id": "ep04_2",
            "file": "ep04_es_2m_830_zoomed_journal.png",
            "timeStr": "02:15",
            "seconds": 135,
            "timeframe": "ES 2m 放大",
            "mtfOrder": 2,
            "titleZh": "案例一（ES 2m 局部放大）：过滤无 FVG 的首次回落，抓二次冲高后的真 MSS + FVG",
            "captionZh": "首次过顶后的小幅回落内部无 FVG 故放弃；第二次冲高至 4,436 后强力跌破波段低点（橙色三角）并留下看跌 FVG（橙色灯泡），回抽 4,419 精准做空。"
        },
        {
            "id": "ep04_3",
            "file": "ep04_nq_5m_wait_for_fvg_entry.png",
            "timeStr": "04:50",
            "seconds": 290,
            "timeframe": "NQ 5m 过滤",
            "mtfOrder": 3,
            "titleZh": "案例二（NQ 5m）：强迫市场亮出底牌——耐心等待第二波真位移与 FVG",
            "captionZh": "突破 14,282 BSL 后的第一波回落既未跌破波段低点也无 FVG；耐心等到冲至 14,405 后长阴线跌破结构并留下 FVG 回抽做空，直奔 50% 以下眼睛图标目标位。"
        }
    ],
    5: [
        {
            "id": "ep05_1",
            "file": "ep05_barchart_open_interest_rollover.png",
            "timeStr": "01:55",
            "seconds": 115,
            "timeframe": "Barchart 换月",
            "mtfOrder": 1,
            "titleZh": "合约换月法则：在 Barchart.com 对比 ESH22 与 ESM22 的未平仓量（Open Int）",
            "captionZh": "交割月（3月H / 6月M / 9月U / 12月Z）第三个周五到期前一周，一旦下一季合约的 Open Int 超过当季合约即切换主力合约。"
        },
        {
            "id": "ep05_2",
            "file": "ep05_15m_daily_range_830_lunch.png",
            "timeStr": "04:15",
            "seconds": 255,
            "timeframe": "ES 15m 风向标",
            "mtfOrder": 2,
            "titleZh": "15m 风向标（Bellwether Chart）：08:30 左侧高低点与 12:00–13:00 午休禁区",
            "captionZh": "标出 08:30 垂直线左侧紧邻的 15m 波段高点（4,514.50）与波段低点（4,482.00），粉色竖条为 12:00–13:00 纽约午休禁入区。"
        },
        {
            "id": "ep05_3",
            "file": "ep05_5m_three_drives_displacement_fvg.png",
            "timeStr": "06:10",
            "seconds": 370,
            "timeframe": "ES 5m 三推诱多",
            "mtfOrder": 3,
            "titleZh": "早盘 5m：三推诱多（Three Drives）扫掉 4,514.50 高点后“大象跳泳池”式暴跌",
            "captionZh": "08:30 后连续走出三个抬高高点（Three Drives）刺穿 4,514.50 买方止损，随后 09:30 美股开盘长阴线暴力下砸直穿 4,482 低点。"
        },
        {
            "id": "ep05_4",
            "file": "ep05_5m_fvg_zoomed_in.png",
            "timeStr": "07:50",
            "seconds": 470,
            "timeframe": "ES 5m FVG进场",
            "mtfOrder": 4,
            "titleZh": "早盘 5m 放大：长阴位移留下的看跌 FVG 与下一根 K 线回抽进场点",
            "captionZh": "鼠标箭头所指处即为大阴线位移留下的 5m 看跌 FVG，随后一根 K 线向上回抽填补缺口提供完美做空点，15 分钟内砸穿 4,482。"
        },
        {
            "id": "ep05_5",
            "file": "ep05_5m_pm_session_130_stop_hunt.png",
            "timeStr": "10:40",
            "seconds": 640,
            "timeframe": "ES 5m 13:30猎杀",
            "mtfOrder": 5,
            "titleZh": "下午盘 5m 启动：13:30 后刺穿第一个短期波段低点完成洗盘诱空",
            "captionZh": "12:00–13:00 粉色午休区结束后，14:15 向下刺穿 13:30 后的首个短期小低点（手势高亮处），扫掉跟风多头止损后正式启动下午盘买方程序。"
        },
        {
            "id": "ep05_6",
            "file": "ep05_5m_pm_spooling_moc.png",
            "timeStr": "14:35",
            "seconds": 875,
            "timeframe": "ES 5m 下午逼空",
            "mtfOrder": 6,
            "titleZh": "下午盘 5m Spooling 与 15:40–16:00 MOC 收盘指令加速冲顶",
            "captionZh": "14:55 大阳线突破早盘相对等高点并留下看涨 FVG，算法开启单边连续阳线逼空（Spooling），并在最后 20 分钟因 MOC 指令加速拉升。"
        }
    ]
}

# Core ICT 2022 Glossary / Dictionary
GLOSSARY = [
    {
        "term": "DOL (Draw on Liquidity)",
        "nameZh": "流动性吸引 / 价格磁铁",
        "category": "高时间框架偏向",
        "definition": "价格在图表上移动的唯一根本目的。日线与日内价格永远像回形针被磁铁吸引一样，奔向两类目标：1) 旧高/低点外侧的止损单（BSL/SSL）；2) 未被回补的失衡区（FVG/Imbalance）。",
        "episodes": [2, 3, 5, 7, 18]
    },
    {
        "term": "BSL (Buyside Liquidity)",
        "nameZh": "买方流动性（买方止损池）",
        "category": "流动性矩阵",
        "definition": "聚集在旧高点（Old Highs）、相对等高点（Relative Equal Highs）、亚盘/伦敦盘高点或前日高点（PDH）正上方的空头止损单（Buy Stops）与突破追多单。聪明钱拉升刺穿 BSL，是为了利用这些高价买单作为自己建立大额空单（或平掉底部多单）的对手盘。",
        "episodes": [2, 3, 4, 5, 6]
    },
    {
        "term": "SSL (Sellside Liquidity)",
        "nameZh": "卖方流动性（卖方止损池）",
        "category": "流动性矩阵",
        "definition": "聚集在旧低点（Old Lows）、相对等低点（Relative Equal Lows）、时段低点或前日低点（PDL）正下方的多头止损单（Sell Stops）与追空单。聪明钱砸盘刺穿 SSL，是为了利用这些低价卖单作为自己建立大额多单（或平掉顶部空单）的对手盘。",
        "episodes": [2, 3, 5, 6, 9]
    },
    {
        "term": "MSS (Market Structure Shift)",
        "nameZh": "日内市场结构转变",
        "category": "执行触发",
        "definition": "当价格刺穿关键 BSL 或 SSL 后，在短周期（5m/3m/2m/1m）上以剧烈位移（Displacement）反向突破最近的短期波段高点（Bullish MSS）或短期波段低点（Bearish MSS），标志着日内算法交付方向正式发生反转。",
        "episodes": [2, 3, 4, 5, 11]
    },
    {
        "term": "FVG (Fair Value Gap) / BISI & SIBI",
        "nameZh": "公允价值缺口 / 失衡区",
        "category": "执行触发",
        "definition": "三根 K 线序列中，第 2 根大 K 线快速单边运动，导致第 1 根 K 线的极值与第 3 根 K 线的极值之间留出没有重叠的空白价格带。看涨缺口称为 BISI（Buyside Imbalance Sellside Inefficiency），看跌缺口称为 SIBI（Sellside Imbalance Buyside Inefficiency）。",
        "episodes": [2, 3, 4, 5, 14, 32]
    },
    {
        "term": "Equilibrium (50%) & Premium / Discount",
        "nameZh": "50% 均衡点与溢价/折价矩阵",
        "category": "流动性矩阵",
        "definition": "将斐波那契从当前交易区间（Dealing Range）最低点拉到最高点：50% 中轴为均衡点（Equilibrium）。高于 50% 为溢价区（Premium，只允许做空或平多）；低于 50% 为折价区（Discount，只允许做多或平空）。",
        "episodes": [2, 3, 4, 14]
    },
    {
        "term": "Order Block (OB) & Change in State of Delivery",
        "nameZh": "订单块与交付状态的改变",
        "category": "执行触发",
        "definition": "刺穿卖方流动性（SSL）的那一连串连续阴线构成看涨订单块，当价格随后向上突破该序列第一根阴线的开盘价时，算法交付状态（State of Delivery）正式由卖转买；刺穿买方流动性（BSL）的连续阳线构成看跌订单块，跌破其第一根阳线开盘价即由买转卖。",
        "episodes": [3, 15, 30]
    },
    {
        "term": "Displacement (Energetic Move)",
        "nameZh": "高能量位移（大象跳进儿童泳池）",
        "category": "执行触发",
        "definition": "ICT 形容真假结构突破的核心标准：真正的 MSS 必须伴随极具爆发力的大实体 K 线且内部留下干净的 FVG（“像一头大象跳进儿童充气泳池”），若只是软绵绵的重叠阴跌/慢涨（Anemic），则不可进场。",
        "episodes": [4, 5, 11]
    },
    {
        "term": "Power of 3 (AMD) & Judas Swing",
        "nameZh": "权力三段（积累-操纵-派发）与犹大摆动",
        "category": "日内时间与订单流",
        "definition": "日 K 线或时段 K 线的三阶段演变：在开盘价（00:00 纽约午夜开盘或 08:30 开盘）附近积累（Accumulation）→ 向主趋势相反方向诱多/诱空扫掉止损（Manipulation / Judas Swing）→ 向真正目标方向单边扩张（Distribution）。",
        "episodes": [9, 10, 28]
    },
    {
        "term": "Spooling & MOC (Market on Close)",
        "nameZh": "算法线性逼空报价与收盘市价加速",
        "category": "日内时间与订单流",
        "definition": "Spooling 指算法启动单边买方/卖方程序后，像线轴放线一样按固定时间步长连续向上或向下递进报价；下午盘单边趋势常在 15:40、15:50 至 16:00 因机构收盘市价指令（MOC）出现最后一波加速。",
        "episodes": [3, 5]
    },
    {
        "term": "LTH / ITH / STH (Market Structure Hierarchy)",
        "nameZh": "长/中/短期三层波段结构",
        "category": "高时间框架偏向",
        "definition": "STH/STL 为基础三 K 线高低点；两侧各有一个更低 STH（或更高 STL）簇拥的极值、或回抽 HTF FVG 形成的波段极值称为中期高低点（ITH/ITL）；大级别反转点称为长期高低点（LTH/LTL）。",
        "episodes": [12, 13]
    },
    {
        "term": "SMT Divergence (Smart Money Technique)",
        "nameZh": "聪明钱跨市场背离",
        "category": "高阶验证",
        "definition": "对比高度同向的相关资产（如 ES vs NQ vs YM，或 DXY vs EURUSD）：当一个品种刺穿前高/前低扫掉止损，而另一个品种却拒绝同步创出新高/新低时，构成机构暗中吸筹或派发的铁证。",
        "episodes": [17, 21]
    }
]

from transcript_io import parse_transcript_file, parse_mmss, transcript_identity, validate_evidence_claims

def main():
    with open(os.path.join(TRANSCRIPTS_DIR, "_index.json"), "r", encoding="utf-8") as f:
        idx = json.load(f)

    evidence = json.loads(Path(BASE_DIR, "references/lesson-evidence.json").read_text())
    frames = json.loads(Path(BASE_DIR, "references/frame-manifest.json").read_text())
    episodes = []
    for item in idx:
        ep_key = item["episode"]
        ep_num, vid_id, raw_title = transcript_identity(ep_key + ".md")
        md_path = os.path.join(TRANSCRIPTS_DIR, f"{ep_key}.md")
        _, segments = parse_transcript_file(md_path)
        meta = LEGACY_EPISODE_META.get(ep_num, {})
        keyframes = [dict(k, evidenceStatus="visual_pending", frameId=k.get("frameId") or f"ep{ep_num:02d}-{Path(k['file']).stem}") for n,k in enumerate(frames.get(str(ep_num), []))]
        claims = evidence["claims"].get(str(ep_num), [])
        validate_evidence_claims(claims, md_path, BASE_DIR)
        for frame in keyframes:
            if not Path(BASE_DIR, "study-room/lesson-assets", frame["file"]).is_file():
                raise ValueError(f"Missing keyframe: {frame['file']}")

        # Estimate duration from last segment
        duration_sec = 0
        if segments:
            end_part = segments[-1]["range"].split("-")[-1].strip()
            duration_sec = parse_mmss(end_part)

        episodes.append({
            "ep": ep_num,
            "videoId": vid_id,
            "biliUrl": f"https://www.bilibili.com/video/BV16sH963EgW/?p={ep_num}",
            "youtubeUrl": f"https://www.youtube.com/watch?v={vid_id}&list=PLOqlWG05MfW6T7mUjI2CK5BdQ6FrV3zEm",
            "hasLocalVideo": False,
            "localVideoUrl": None,
            "titleEn": raw_title.replace("2022 ICT Mentorship [No Rant] ", "").lstrip("- "),
            "titleZh": raw_title.replace("2022 ICT Mentorship [No Rant] ", "").lstrip("- "),
            "module": meta.get("module", "ICT 2022 Mentorship"),
            "tags": [],
            "summaryZh": "；".join(c["detailZh"] for c in claims) if claims else "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
            "evidenceStatus": "partial_transcript_checked" if claims else "pending",
            "legacyDraft": {"status": "unverified_archive", "metadata": meta},
            "sourcePath": str(Path(md_path).relative_to(BASE_DIR)),
            "biliTimeMapping": "unverified",
            "durationSec": duration_sec,
            "durationKind": "last_transcript_timestamp",
            "wordCount": sum(len(seg["text"].split()) for seg in segments),
            "keyPoints": claims,
            "keyframes": keyframes,
            "segments": segments
        })

    output = {
        "courseTitle": "ICT 2022 Mentorship [No Rant] · 沉浸式精读工作台",
        "bilibiliUrl": "https://www.bilibili.com/video/BV16sH963EgW/",
        "youtubePlaylistUrl": "https://www.youtube.com/playlist?list=PLOqlWG05MfW6T7mUjI2CK5BdQ6FrV3zEm",
        "totalEpisodes": len(episodes),
        "glossary": [{"term": p["title"], "definition": p["rule"]} for p in json.loads(Path(BASE_DIR,"references/framework.json").read_text())["principles"]],
        "episodes": episodes
    }

    if len(episodes) != 37 or len({e['ep'] for e in episodes}) != 37:
        raise ValueError("Expected 37 unique episodes")
    out_json_path = Path(BASE_DIR, "courseData.json")
    staged = out_json_path.with_suffix(".json.pending")
    staged.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(staged, out_json_path)
    print(f"Wrote {out_json_path}: {len(episodes)} episodes, {sum(len(e['segments']) for e in episodes)} segments")

if __name__ == "__main__":
    main()
