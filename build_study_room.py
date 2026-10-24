#!/usr/bin/env python3
import json
import os
import shutil
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STUDY_DIR = os.path.join(BASE_DIR, "study-room")
ASSETS_DIR = os.path.join(STUDY_DIR, "lesson-assets")
VIDEOS_SRC = os.path.join(BASE_DIR, "videos")
ARTIFACT_DIR = "/Users/rouen/.gemini/antigravity/brain/2f7883a2-405d-4596-a34a-2d0b4894d4c3"
COURSE_JSON = os.path.join(BASE_DIR, "app", "src", "data", "courseData.json")

os.makedirs(STUDY_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# Copy all 22 1080p PNG frames into study-room/lesson-assets/
for png in glob.glob(os.path.join(ARTIFACT_DIR, "ep*.png")):
    shutil.copy2(png, os.path.join(ASSETS_DIR, os.path.basename(png)))

# Symlink videos into study-room/videos
videos_link = os.path.join(STUDY_DIR, "videos")
if os.path.lexists(videos_link):
    if os.path.islink(videos_link):
        os.unlink(videos_link)
    else:
        shutil.rmtree(videos_link)
os.symlink(VIDEOS_SRC, videos_link)

with open(COURSE_JSON, "r", encoding="utf-8") as f:
    cdata = json.load(f)

# 1. Build ICT 2022 6-Stage System Map & 12 Principles (matching garbage-teacher-distill schema)
FRAMEWORK = {
    "schema": "ict-2022-distill-framework",
    "version": 1,
    "identity": "主模型提炼：把 ICT 2022 Mentorship [No Rant] 全 37 集的原话、1080p 原图批注与多周期推演，按一笔日内交易从『盘前过滤 → 流动性地图 → 猎杀触发 → 均衡进场 → 时段管理 → 手帐复盘』的六阶段归类。例子中严格区分 ICT原话 / 原片图表 / 主模型归纳。",
    "chain": [
        {"id": "S1", "title": "① 今天值不值得做", "question": "环境与时间门：纽约时区、午休禁区与垃圾时间过滤"},
        {"id": "S2", "title": "② 地图：流动性在哪", "question": "高周期偏向 (DOL)：旧高低点止损池 (BSL/SSL) 与失衡区 (FVG)"},
        {"id": "S3", "title": "③ 触发：什么时候能做", "question": "猎杀止损 (Stop Raid) + 高能量位移 MSS + 订单块交付状态改变"},
        {"id": "S4", "title": "④ 位置：在哪里挂单", "question": "50% 均衡点 (Equilibrium) 溢价/折价过滤 + 三K线 FVG 挂单"},
        {"id": "S5", "title": "⑤ 管理：怎么拿、怎么走", "question": "内外部流动性分批止盈、13:30 下午盘 Spooling 与 MOC 收盘加速"},
        {"id": "S6", "title": "⑥ 复盘：怎么沉淀肌肉记忆", "question": "Ep.04 标准四维复盘手帐、合约换月与亏损降档纪律"}
    ],
    "principles": [
        {
            "id": "P01", "stage": "S1", "layer": "第一层 · 预期与时间门",
            "title": "只抓日内一段高确定性波段，严守纽约时间窗口",
            "oneLine": "放弃模仿高频多空来回反手，每天只在纽约关键窗口（早盘 08:30–11:00、下午盘 13:30–15:30）捕捉一段干净的单边价格腿；12:00–13:00 午休绝对空仓。",
            "how": [
                "先把 TradingView 右下角时区锁定为 New York (UTC-5/夏令时 UTC-4)",
                "早盘紧盯 08:30 宏观数据脉冲与 09:30 美股现货开盘的流动性猎杀；理想情况下 11:00 前结束战斗",
                "12:00–13:00 纽约午休画粉红禁区，禁止开新仓；重大消息前若双向扫损无跟随（Seek & Destroy）直接关机"
            ],
            "misread": "看着 1 分钟图想把每一段小折返都吃到；或在 12:15 午休横盘区强行找 FVG 开单被来回打脸。"
        },
        {
            "id": "P02", "stage": "S2", "layer": "第一层 · 流动性磁铁",
            "title": "日线偏向 (Daily Bias) 与两大流动性磁铁 (DOL)",
            "oneLine": "价格像回形针被磁铁吸引一样，在日线与高周期上永远只奔向两样东西：① 旧高/低点外侧的止损池 (BSL/SSL)；② 未回补的失衡区 (FVG)。",
            "how": [
                "开盘前先看周线与日线下一根 K 线倾向于向哪一侧扩张（不必猜收盘阴阳，只需判断日内扩张方向）",
                "标出日线最近的旧高点上方 Buy Stops (BSL)、旧低点下方 Sell Stops (SSL) 以及日线 FVG",
                "若一侧外部流动性已被扫除且未能继续扩张，下一个磁铁必然转向区间内部 50% 均衡位与内部 FVG"
            ],
            "misread": "把日线看跌等同于今天分时图从早跌到晚——看跌日往往先向上拉升扫掉早盘高点（Judas Swing）才开始下跌。"
        },
        {
            "id": "P03", "stage": "S2", "layer": "第一层 · 盘口地图",
            "title": "15 分钟风向标 (Bellwether) 与相对等高/等低点陷阱",
            "oneLine": "以 15m 图为日内骨架，标出 08:30 左侧最近的波段高点与波段低点；散户奉为强阻力的“双顶/相对等高点”，正是聪明钱最优先猎杀的买方止损池。",
            "how": [
                "在 15m 图画出 08:30 垂直线，向左侧紧邻处标出最近的 Swing High (BSL) 与 Swing Low (SSL)",
                "同时标出亚盘 (19:00–21:00)、伦敦盘 (02:00–05:00) 高低点以及前日高低点 (PDH/PDL)",
                "看到干净的 Relative Equal Highs（相对等高点），绝不在等高点下方提前摸顶做空，而是等它被刺穿！"
            ],
            "misread": "看到双顶/等高点就以为阻力很强直接做空，结果把止损刚好放在机构准备猎杀的 Buy Stops 池子里。"
        },
        {
            "id": "P04", "stage": "S3", "layer": "第二层 · 猎杀与诱导",
            "title": "先诱导再猎杀（Sucker Play）与三推蓄势（Three Drives）",
            "oneLine": "机构建立大额空单需要大量高价买单做对手盘：常先跌破小低点诱导散户追空，或走出三推抬高结构（Three Drives）刺穿旧高点完成 Stop Raid。",
            "how": [
                "开盘前或开盘初若先小幅跌破短期震荡低点，警惕这是诱空陷阱（Sucker Play），观察随后是否迅速拉起去攻上方大级别等高点",
                "向关键旧高点推进时，若连续走出三个依次抬高的短波段高点（Three Drives），说明正在累积多头跟风盘并完成顶部猎杀",
                "未刺穿预定 BSL/SSL 池子之前，状态永远保持 Wait（等待）"
            ],
            "misread": "价格刚在区间中部跌破一个小低点就急着追空，正好掉进算法去扫上方等高点前的诱空坑。"
        },
        {
            "id": "P05", "stage": "S3", "layer": "第二层 · 触发确认",
            "title": "高能量位移 (Displacement) 与日内市场结构转变 (MSS)",
            "oneLine": "刺穿流动性池后不猜顶底，切入 5m/2m/1m 等待价格以“大象跳进儿童泳池”式高能量位移反向跌破短期波段低点（或突破短期波段高点）。",
            "how": [
                "扫掉 BSL 后，锁定推动最后一次冲高的那个短期波段低点（Swing Low）；只有当价格强力砸穿它才确认 Bearish MSS",
                "扫掉 SSL 后，锁定砸出最低点的那个短期波段高点（Swing High）；盘中刺穿它且三 K 线留下看涨 FVG 即确认 Bullish MSS",
                "位移必须果断剧烈；若第一波回落既未破波段极值、内部又无 FVG，必须按兵不动，强迫市场二次冲顶后再亮出真底牌"
            ],
            "misread": "刚刺穿前高、连短期 Swing Low 都没跌破也没有 FVG，就凭感觉在第一波软绵绵的回落中摸顶做空。"
        },
        {
            "id": "P06", "stage": "S3", "layer": "第二层 · 算法内核",
            "title": "订单块 (Order Block) = 交付状态的改变 (Change in State of Delivery)",
            "oneLine": "刺穿 SSL 的连续阴线合为一个看涨订单块，突破其第一根阴线开盘价即由卖转买；刺穿 BSL 的连续阳线合为看跌订单块，跌破其第一根阳线开盘价即由买转卖。",
            "how": [
                "把扫向止损池的那一串连续同色 K 线视为一个整体订单块（而非只看最后一根）",
                "用水平线标出该连续序列第一根 K 线的开盘价（Opening Price）：价格反向越过该线的一刻，算法交付状态正式翻转",
                "当订单块开盘价与位移留下的 FVG 发生重合时，是胜率最高的黄金狙击带"
            ],
            "misread": "在还没有突破连续阴线/阳线开盘价之前，随便拿中间一根阴线当订单块盲目接飞刀。"
        },
        {
            "id": "P07", "stage": "S4", "layer": "第三层 · 位置与挂单",
            "title": "50% 均衡点 (Equilibrium) 溢价/折价矩阵与三K线 FVG 进场",
            "oneLine": "从交易区间低点拉到高点取 50% 中轴：只允许在 >50% 的溢价区 (Premium) 看跌 FVG 阳线回抽时做空，只允许在 <50% 的折价区 (Discount) 看涨 FVG 阴线回踩时做多。",
            "how": [
                "确认三根 K 线序列的第 1 根极值与第 3 根极值之间存在无重叠空白（看跌为 SIBI，看涨为 BISI）",
                "拉斐波那契 0–100% 保留 0.5（50% Equilibrium）：检查该 FVG 是否位于有利的溢价侧（空）或折价侧（多）",
                "限价挂单放在 FVG 入口边缘（或 50% 中轴 CE），止损放在猎杀波段极值外或位移大 K 线极值外"
            ],
            "misread": "在低于 50% 的深折价区去追空一个看跌 FVG，结果刚进场就碰到下方内部支撑反抽打止损。"
        },
        {
            "id": "P08", "stage": "S4", "layer": "第三层 · 纪律状态链",
            "title": "状态机纪律：Wait → Armed → Execute / Cancel / Exit",
            "oneLine": "每个时刻只处于一个明确状态：未扫池子是 Wait；扫池子+出现 MSS 与 FVG 是 Armed；回抽进 FVG 成交是 Execute；未回抽直接到目标是 Cancel（接受踏空不追单）。",
            "how": [
                "Wait：价格在 50% 均衡线附近徘徊，或虽破高点但尚未出现 MSS 与 FVG",
                "Armed：已完成 Stop Raid + MSS + 溢价/折价区 FVG，限价单与止损 S、目标 T 已明确",
                "Execute / Exit：回抽触及 FVG 成交；若已成交后收盘重新站回失效侧则按计划 Exit；若未给回抽直接走完目标则 Cancel 原单，绝不半路市价追单"
            ],
            "misread": "FVG 没回抽直接跌了 50 点，心态失衡在折价区市价追空，结果正好追在算法回补内部流动性的反弹起点。"
        },
        {
            "id": "P09", "stage": "S5", "layer": "第四层 · 止盈与下午盘",
            "title": "内外流动性双重止盈、13:30 下午盘宏与 MOC 收盘加速",
            "oneLine": "空单过 50% 均衡线后，先在折价区内部看涨 FVG 减仓（内部流动性），余仓看下方波段低点 Sell Stops（外部流动性）；下午盘盯紧 13:30 扫低点启动与 15:40–16:00 MOC 冲刺。",
            "how": [
                "永远遵循：从外部流动性（扫高/低点）进场 → 在反向内部流动性（50% 另一侧的反向 FVG）落袋主体利润 → 再看反向外部止损池",
                "下午盘 13:30 后，优先观察是否向下刺穿 13:30 后的首个短期波段低点（或午休低点）诱空，随后突破早盘相对等高点开启单边 Spooling",
                "若下午走出单边多头趋势，15:40、15:50 至 16:00 常因机构收盘市价单 (MOC) 出现最后加速，于 16:00 前全部平仓"
            ],
            "misread": "在溢价区做了空，却还贪心地把止盈设在溢价区，或者死扛单子不肯在折价区内部 FVG 分批落袋。"
        },
        {
            "id": "P10", "stage": "S5", "layer": "第四层 · 进阶结构与SMT",
            "title": "Power of 3 (AMD)、LTH/ITH/STH 三层结构与跨市场 SMT 背离",
            "oneLine": "结合午夜 00:00 开盘价识别积累-操纵-派发 (AMD)；用三层高低点 (LTH/ITH/STH) 跟踪趋势；用 ES vs NQ 的不同步创新高/新低 (SMT) 抓机构暗中派发。",
            "how": [
                "看跌日等待价格拉升至 00:00 午夜开盘价上方完成 Manipulation（犹大摆动 Judas Swing）再做空；看涨日等待砸至 00:00 下方再做多",
                "回抽 HTF FVG 形成的中期高低点 (ITH/ITL) 不破，则单边结构延续，可将保护止损移至最新 ITH/ITL 外",
                "在关键 BSL/SSL 处对比 ES 与 NQ：一个破前高而另一个不破前高（看跌 SMT），优先做空那个没创新高的更弱品种"
            ],
            "misread": "只看单一品种盲目猜反转，忽略了相关性指数或短周期尚未破坏 ITH/ITL 的趋势延续信号。"
        },
        {
            "id": "P11", "stage": "S6", "layer": "第五层 · 合约与风控",
            "title": "季度合约换月 (H/M/U/Z)、点值换算与亏损后仓位减半铁律",
            "oneLine": "熟记 H(3月)/M(6月)/U(9月)/Z(12月) 并在到期前一周按 Barchart 持仓量换月；遭遇止损后若继续交易，下一笔风险仓位必须砍半。",
            "how": [
                "NQ 每整点 (4 ticks) = $20（MNQ = $2）；ES 每整点 = $50（MES = $5）",
                "每个交割月第 3 个周五到期前一周（周一/周二），在 barchart.com 检查 Open Int，一旦下季合约超过当季合约立即换月",
                "单日止损后绝不报复性加仓；连续止损后将风险敞口砍半，直至用减半仓位挽回前次亏损的一半以上才恢复原仓位"
            ],
            "misread": "在合约到期周还在死做流动性枯竭的旧合约；或者一笔止损后上头翻倍重仓想一把回本。"
        },
        {
            "id": "P12", "stage": "S6", "layer": "第五层 · 复盘手帐",
            "title": "Ep.04 标准四维复盘手帐 (Study Journal) 与百图回测",
            "oneLine": "每张复盘截图必须量化记录四项指标：① MSS 到回抽 FVG 耗时；② 进场到目标持仓耗时；③ 最大抗单浮亏 (Heat)；④ 整段波幅点数。",
            "how": [
                "按 Ep.02–05 标准在 TradingView 上框出 BSL/SSL、MSS、FVG 与 50% Equilibrium 截图标注",
                "在手帐中老实记下成交后向止损方向逆行了多少个点（Heat Weathered），训练对正常回撤的心理耐受度",
                "区分带提示课堂练习与自己的实盘/模拟盲测记录，积累 100 张标准化历史日内样本"
            ],
            "misread": "只截结果走出来的完美大图自嗨，不记进场等待时间、不记抗单浮亏，导致实盘一遇 3 个点正常回撤就慌乱割肉。"
        }
    ]
}

# 2. Build Detailed 3-Layer Distillation Cards for Lessons
DISTILL_LESSONS = {
    "ep01": {
        "status": "current",
        "core": "摒弃 1 分钟高频多空来回反手，每天只在 E-mini 股指期货（NQ/ES）上利用可重复的流动性模型捕捉一段高确定性的日内主波段。",
        "cases": [
            {
                "title": "高频反手交割单 vs 单一主跌浪目标",
                "gist": "顶尖交易员的高频多空反手依赖极深盘感，普通学习者应只截取右侧最干净的一段单边位移波段（如 NQ 123 点主跌浪），用确定性代替交易频率。",
                "scene": "ICT 展示自己在 Thinkorswim 1 分钟图上从 10:30 到 11:45 连续做多、反手做空、再做多、再在 14,798.25 做空至 14,675.75 的实盘交割记录。",
                "figureGuide": "对比左图满屏的多空买卖箭头与右图蓝色高亮指向的 14,798.25 → 14,675.75 单边主跌浪。",
                "figures": [
                    {"src": "lesson-assets/ep01_tos_live_executions.png", "caption": "Ep.01 [00:40]：ICT 在 Thinkorswim 1m 图上的高频多空反手交割单"},
                    {"src": "lesson-assets/ep01_target_one_big_leg.png", "caption": "Ep.01 [04:50]：课程真正要求掌握的目标——只取右侧 14,798 空到 14,675 的 123 点单边主波段"}
                ],
                "read": [
                    {"who": "老师图", "text": "10:30–11:15 之间有多笔短线多空来回成交，最后在顶部 14,784.5 与 14,798.25 建立空单，于下方 14,675.75 平仓。"},
                    {"who": "老师", "text": "不要试图模仿我左侧那种高频抓反转的操作；你只需要学会抓最右边从 798 到 675 这一笔 123 个 handles 的大波段就足够财富自由了。"},
                    {"who": "主模型", "text": "明确 NQ 1 Handle = 4 Ticks = $20（MNQ = $2），ES 1 Handle = $50（MES = $5）；TradingView 需注意延时数据，实盘以实时报价为准。"}
                ],
                "plan": [
                    "根据账户资金量选定 NQ/ES 或微型合约 MNQ/MES，每天只等一个 A+ 级单边波段",
                    "不挂任何均线/MACD指标，保持裸 K 图表用于标注流动性池与失衡区"
                ],
                "trap": "看到别人晒多空通吃的交割单就手痒在震荡区频繁反手，把本金磨损在主波段启动之前。",
                "principles": ["P01", "P11"]
            }
        ],
        "drill": "如果 NQ 从 14,798.25 做空到 14,675.25 平仓，一共捕获了多少个 Handles（整点）？1 手标准 NQ 和 1 手微型 MNQ 分别对应多少美元？",
        "gaps": ""
    },
    "ep02": {
        "status": "current",
        "core": "自上而下四步闭环：先由周/日线锁定流动性磁铁（DOL），等 15m 诱空后向上刺穿相对等高点买方止损（BSL），再切入 2m/1m 等跌破短期波段低点（BMS）并回抽溢价区 FVG 做空，拿到 50% 折价区以下的内部 FVG 止盈。",
        "cases": [
            {
                "title": "周/日线偏向（DOL）与 1H/15m 诱空猎杀相对等高点",
                "gist": "在大级别看跌（下方旧低点 SSL 未扫）背景下，开盘初先跌破短期小低点往往是诱空陷阱（Sucker Play），真正的做空时机在价格随掉头刺穿上方相对等高点买方止损（BSL）之后。",
                "scene": "2022 年 1 月 21 日周五 NQ（3月合约）：周线向下扩张，日线下方 2021 年 10 月旧低点 14,366.75 存在厚重 Sell Stops；15m 图在 14,820 存在清晰的相对等高点。",
                "figureGuide": "依次观察周线阴线扩张 → 日线 14,366.75 红线磁铁 → 1H/15m 先破 14,600 Sell Stops 再拉升刺穿 14,820 Buy Stops。",
                "figures": [
                    {"src": "lesson-assets/ep02_daily_ssl_and_imbalance.png", "caption": "Ep.02 [01:55] 日线 1D：下方 14,366.75 旧低点下方的卖方止损池作为价格磁铁 (DOL)"},
                    {"src": "lesson-assets/ep02_15m_equal_highs_stop_hunt.png", "caption": "Ep.02 [07:20] 15m 图：先跌破 14,602 Sell Stops 诱空，再冲高刺穿 14,820 相对等高点 Buy Stops"}
                ],
                "read": [
                    {"who": "老师", "text": "日线图上价格永远只找两样东西：旧高低点的止损（Liquidity）或失衡区（Imbalance）。这里下方 14,366.75 的卖方止损就像磁铁吸回形针一样吸引价格。"},
                    {"who": "老师图", "text": "15 分钟图在 10:15 先跌破 14,602 的 Sellside Liquidity，随后 V 型拉升超过 220 点，在 11:20 刺穿 14,820 相对等高点上方的 Buyside Liquidity。"},
                    {"who": "老师", "text": "散户教科书认为双顶等高点是强阻力，把空头止损全放在 14,820 上方；聪明钱先破小低点诱空，再拉上去触发 14,820 上方的 Buy Stops，用散户的高价买单作为自己建仓空单的对手方。"}
                ],
                "plan": [
                    "盘前标出日线 DOL 目标（14,366.75）及 15m 相对等高点（14,820）",
                    "早盘价格在区间下部跌破小低点时不追空，耐心等待价格拉升刺穿 14,820 BSL"
                ],
                "trap": "在 10:15 跌破 14,602 小低点时当作顺势突破追空，被随后的 220 点拉升直接爆仓；或者在 14,820 等高点下方提前摸顶做空被扫止损。",
                "principles": ["P02", "P03", "P04"]
            },
            {
                "title": "2m 结构跌破（BMS）+ 溢价区 FVG 进场与 50% 折价区止盈矩阵",
                "gist": "当高周期流动性池被刺穿后，降维到 2m/1m 等待跌破最近的短期波段低点（BMS）且位移内部留下三 K 线看跌 FVG，在 >50% 溢价区回抽 FVG 时做空，并在 <50% 折价区的内部看涨 FVG 分批平仓。",
                "scene": "NQ 刺穿 14,820 BSL 创出 14,855 高点后，切入 2 分钟图寻找进场扳机与止盈位置。",
                "figureGuide": "看 2m 图右上角：跌破短期波段低点后留下的橙色小框（看跌 FVG），以及红绿双色斐波那契 50% 均衡框与下方两条蓝线止盈位。",
                "figures": [
                    {"src": "lesson-assets/ep02_2m_bms_and_fvg_entry.png", "caption": "Ep.02 [11:35] 2m 触发：刺穿 14,820 后跌破短期波段低点 (BMS)，并在位移腿内留下橙色看跌 FVG"},
                    {"src": "lesson-assets/ep02_2m_full_setup_annotated.png", "caption": "Ep.02 [15:05] 2m 均衡矩阵与止盈：50% 以上红色溢价区 FVG 进场，50% 以下绿色折价区内部看涨失衡（蓝线）止盈"}
                ],
                "read": [
                    {"who": "老师", "text": "高频算法运行在 1m/2m/3m 级别。当 15m 买方止损被扫后，在 2m 图等它跌破 14,808 这个短期 Swing Low（BMS），然后找这波下跌里三根 K 线不重叠的 Fair Value Gap。"},
                    {"who": "老师图", "text": "从 14,535 低点拉斐波那契到 14,855 高点：橙色看跌 FVG 位于远高于 50% 的红色溢价区顶端，随后阳线回抽进橙色框精准受阻下跌，穿过 50% 中轴直达绿色折价区内的两条蓝色水平线（14,680 与 14,650）。"},
                    {"who": "主模型", "text": "构建『外部流动性猎杀 (14,820 BSL) → 溢价区 FVG 进场 (14,798) → 折价区内部 FVG 止盈 (14,675) → 外部 SSL 终极目标』的标准矩阵。"}
                ],
                "plan": [
                    "看到 2m 跌破短期 Swing Low 且留下三 K 线看跌 FVG，将状态从 Wait 切换为 Armed",
                    "在 FVG 下沿挂限价空单，止损设在 14,855 波段高点上方，第一、二止盈设在 50% 以下的内部看涨 FVG"
                ],
                "trap": "不等阳线回抽进 FVG 就在跌破瞬间市价追空，导致止损过宽；或者在还没跌过 50% 均衡线时就早早平仓。",
                "principles": ["P05", "P07", "P08", "P09"]
            }
        ],
        "drill": "为什么在 Ep.02 中，空单的第一止盈位必须设在 50% 斐波那契均衡线（Equilibrium）以下的看涨 FVG 处，而不能设在 50% 以上？",
        "gaps": ""
    },
    "ep03": {
        "status": "current",
        "core": "日内多空完全对称：早盘先扫下方 SSL 触发看涨 MSS + 看涨 FVG 可做多至上方 BSL，扫完上方 BSL 触发看跌 MSS + 看跌 FVG 可反手做空；连续阴/阳线开盘价被突破即代表算法『交付状态的改变』（Order Block 本质）。",
        "cases": [
            {
                "title": "同一交易日内的多空双向闭环（2m Bullish MSS → Bearish MSS）",
                "gist": "只要关键流动性池被刺穿并在短周期产生反向 MSS + FVG，无论顺大势还是日内逆势波段，都遵循完全一致的进出场法则。",
                "scene": "依然是 2022 年 1 月 21 日 NQ 2m 图：早盘 08:30 后，10:20 先向下扫掉 14,600 SSL，11:25 再向上扫掉 14,820 BSL。",
                "figureGuide": "观察左下角灰色框（Stop Raid + 橙色上三角 Bullish MSS + 橙色灯泡看涨 FVG）与右上角灰色框（Stop Raid + 橙色下三角 Bearish MSS + 橙色灯泡看跌 FVG）。",
                "figures": [
                    {"src": "lesson-assets/ep03_2m_bullish_mss_fvg_ob.png", "caption": "Ep.03 [05:10] 2m 多头闭环：10:20 扫完 14,600 SSL 后刺穿 14,634 触发 Bullish MSS，回踩橙色灯泡看涨 FVG 做多至 14,820"},
                    {"src": "lesson-assets/ep03_2m_bearish_mss_fvg_targets.png", "caption": "Ep.03 [06:45] 2m 空头闭环：11:25 扫完 14,820 BSL 后触发 Bearish MSS，回抽看跌 FVG 反手做空"}
                ],
                "read": [
                    {"who": "老师", "text": "很多人问我：既然 10:20 先扫了下方 14,600 的 Sell Stops，能不能做多去拿上方 14,820？完全可以！看 10:20 扫低点后向上突破 14,634 短期高点（甚至不需要收盘站上，只要盘中刺穿且留下三 K 线 FVG），回踩 FVG 就是绝佳多单。"},
                    {"who": "老师图", "text": "2m 图清晰标出左下角 Bullish Market Structure Shift 与右上角 Bearish Market Structure Shift，两处都在突破波段极值的位移腿内留下橙色灯泡标识的 FVG。"}
                ],
                "plan": [
                    "早盘 08:30 后标出上下两侧最近的 15m 止损池（14,600 SSL 与 14,820 BSL）",
                    "哪一侧先被刺穿并走出反向 MSS + FVG，就以另一侧止损池作为该笔日内波段的目标位"
                ],
                "trap": "混淆日内 MSS（捕捉几十至上百点的日内单腿）与日线级 MSB（跨日大反转），在多单到达 14,820 BSL 池子后仍死拿不平仓。",
                "principles": ["P03", "P05", "P07"]
            },
            {
                "title": "订单块 (Order Block) 本质：算法 Spooling 与交付状态的改变",
                "gist": "刺穿止损池的一连串连续阴线（或连续阳线）构成一个整体订单块；当价格反向突破这串 K 线第一根的开盘价时，算法的交付状态（State of Delivery）正式翻转。",
                "scene": "切入 1 分钟图精细观察 10:20 底部与 11:25 顶部的 K 线序列。",
                "figureGuide": "看 1m 图中刺穿高低点的连续同色 K 线序列及其起始开盘价水平线。",
                "figures": [
                    {"src": "lesson-assets/ep03_1m_orderblock_state_of_delivery.png", "caption": "Ep.03 [09:30] 1m 拆解：连续阳线刺穿 BSL 构成看跌订单块，跌破起始开盘价即改变交付状态"},
                    {"src": "lesson-assets/ep03_1m_full_lipstick_chart.png", "caption": "Ep.03 [11:45] 1m 完整标注图：1m 级别比 2m 更早触发结构转变与 FVG"}
                ],
                "read": [
                    {"who": "老师", "text": "不是成交量推动了价格，而是算法在 Spooling（像线轴放线一样连续报高或报低价格）。向下刺穿 14,600 的那一串连续收阴的 K 线合起来就是一个看涨订单块；当价格向上越过这串阴线第一根 K 线的开盘价时，State of Delivery（交付状态）就从卖方切换成了买方！"},
                    {"who": "主模型", "text": "将『突破连续同色 K 线开盘价（OB 交付状态改变）』与『突破短期摆动高低点（MSS）+ 留下 FVG』结合，可实现双重确认。"}
                ],
                "plan": [
                    "在 1m/2m 图上找到刺穿止损池的那串连续阴线（看涨 OB）或连续阳线（看跌 OB），画出第一根 K 线的开盘价线",
                    "等待价格突破该开盘价并留下 FVG，在价格回抽 FVG 与 OB 开盘价重合区时进场"
                ],
                "trap": "随便在图表中间找一根孤立的阴线/阳线就当成 Order Block 挂单，忽略了订单块必须发生于刺穿关键流动性池（Stop Raid）之时。",
                "principles": ["P06", "P01"]
            }
        ],
        "drill": "按照 ICT 在 Ep.03 中的定义，当价格向下刺穿 Sellside Liquidity 时出现了一串连续 4 根阴线，哪一个具体价格被向上突破才标志着『交付状态的改变（Change in the State of Delivery）』？",
        "gaps": ""
    },
    "ep04": {
        "status": "current",
        "core": "当价格刺穿买方止损（BSL）后，若第一波回落没有跌破波段低点或内部没有 FVG，必须忍住不动手，『强迫市场先亮出底牌』，等二次冲高走出真位移 + FVG 再扣扳机，并按四维标准记录复盘手帐。",
        "cases": [
            {
                "title": "ES 2m 与 NQ 5m：过滤无 FVG 的首次假回落，等待二次冲高真位移",
                "gist": "破高点后的第一次回调若 K 线重叠无 FVG 或未破短期 Swing Low，属于诱空洗盘，必须放弃并等待二次冲顶后的真 MSS + FVG。",
                "scene": "2022 年 1 月 26 日 ES 2m 图（08:30 后扫掉 4,423.25 BSL）与 1 月 27 日 NQ 5m 图（扫掉 14,282 相对等高点 BSL）。",
                "figureGuide": "观察两张图中突破 Buyside Liquidity 后的第一波小回落（无标注、无缺口）与第二次冲高后的长阴线真跌破（橙色三角 + 橙色灯泡/FVG 红线）。",
                "figures": [
                    {"src": "lesson-assets/ep04_es_2m_830_zoomed_journal.png", "caption": "Ep.04 [02:15] ES 2m 局部放大：首次回落无 FVG 过滤不进；二次冲高跌破波段低点（橙色三角）并留下看跌 FVG（橙色灯泡）做空"},
                    {"src": "lesson-assets/ep04_nq_5m_wait_for_fvg_entry.png", "caption": "Ep.04 [04:50] NQ 5m：突破 14,282 后首次回调既无 MSS 也无 FVG，耐心等到 14,405 二次冲顶后长阴砸出 FVG 再进场"}
                ],
                "read": [
                    {"who": "老师", "text": "看 ES 2m 图：过掉 Buyside Liquidity 后第一次往下跌破了一个小低点，但里面有 Fair Value Gap 吗？没有！所以什么都别做。等它再往上拱一下，然后啪地砸下来跌破波段低点并留下这个橙色灯泡 FVG，回抽 4,419 做空，一直拿到 50% 以下的 4,382（37 个 ES handles）。"},
                    {"who": "老师", "text": "再看 NQ 5m 图：我称之为 Forcing the market to tip its hand（强迫市场先亮底牌）。第一次过 14,282 后的回调既没破 Swing Low 也没留 FVG，谁在那里盲目摸顶就会被拉到 14,405 止损出局；等真正砸出 FVG 再回抽进场，才能稳稳拿到 50%（14,127）以下的眼睛图标目标位。"},
                    {"who": "主模型", "text": "同时确立 Study Journal（复盘手帐）四项必记数据：MSS 到进场耗时、进场到目标耗时、最大抗单浮亏 (Heat)、总捕获点数。"}
                ],
                "plan": [
                    "价格刺穿 BSL/SSL 后，用放大镜检查第一波反向运动是否同时具备『突破 Swing High/Low』与『无重叠三 K 线 FVG』",
                    "缺任何一个条件立即保持 Wait，等待市场再探一次极值后的第二波高能量位移"
                ],
                "trap": "生怕踏空行情，只要看到价格刺穿前高收了一根阴线就立刻市价做空，被随后的二次冲顶精准扫掉止损。",
                "principles": ["P05", "P08", "P12"]
            }
        ],
        "drill": "复盘手帐（Study Journal）要求在每张截图旁记录哪 4 项量化指标？",
        "gaps": ""
    },
    "ep05": {
        "status": "current",
        "core": "建立全天日内订单流剧本：盘前核对 H/M/U/Z 持仓量换月并在 15m 风向标画出 08:30 左侧高低点；早盘抓三推诱多（Three Drives）后的『大象跳泳池』式位移；12:00–13:00 午休空仓；下午盘抓 13:30 扫低点启动的买方 Spooling 与 15:40–16:00 MOC 收盘冲刺。",
        "cases": [
            {
                "title": "15m 风向标、早盘三推诱多 (Three Drives) 与高能量位移做空",
                "gist": "当早盘价格以三推抬高结构（Three Drives）缓慢拱穿 08:30 左侧的 15m 波段高点后，等待一记如“大象跳进儿童泳池”般的长阴线位移与 FVG 做空至早盘低点。",
                "scene": "2022 年 2 月 1 日 ES（ESH2022）：15m 图在 08:30 左侧有 03:00 伦敦高点 4,514.50 与 05:00 低点 4,482.00。",
                "figureGuide": "先看 15m 图的整体日内三段切割（早盘 / 粉色午休禁区 / 下午盘），再看 5m 图早盘刺穿 4,514.50 的三推结构与 09:30 长阴位移 FVG。",
                "figures": [
                    {"src": "lesson-assets/ep05_15m_daily_range_830_lunch.png", "caption": "Ep.05 [04:15] 15m 风向标：08:30 左侧波段高低点（4,514.50 & 4,482.00）与 12:00–13:00 粉色午休禁区"},
                    {"src": "lesson-assets/ep05_5m_fvg_zoomed_in.png", "caption": "Ep.05 [07:50] 5m 早盘放大：三推刺穿 4,514.50 后长阴线砸出看跌 FVG（鼠标箭头处），回抽即空直达 4,482"}
                ],
                "read": [
                    {"who": "老师", "text": "15 分钟图是我们的 Bellwether（风向标）。在 08:30 垂直线左边标出最近的 Swing High (4,514.50) 和 Swing Low (4,482)。切换到 5m 图，价格走出 1-2-3 Three Drives（三推形态）刺穿 4,514.50。"},
                    {"who": "老师", "text": "怎么知道它是真反转？我要看到 Displacement（位移）——不是软绵绵的回调，而是像一头大象跳进儿童泳池里一样水花四溅！看 09:30 这根大阴线直接砸穿短期支撑并留下 5m FVG，下一根 K 线回抽 FVG 做空，15 分钟就砸穿了下方 4,482 卖方止损池！"}
                ],
                "plan": [
                    "每天 08:30 前在 15m 图画好 08:30 垂直线、12:00–13:00 午休禁区以及左侧最近的 Swing High/Low",
                    "早盘出现 Three Drives 刺穿旧高点后，等待“大象跳泳池”式大阴线留出 FVG，回抽进场做空，目标直指 08:30 左侧波段低点"
                ],
                "trap": "在三推形态的第 1 推或第 2 推还没刺穿 4,514.50 旧高点、也没出现长阴位移时就过早入场做空。",
                "principles": ["P01", "P03", "P04", "P05"]
            },
            {
                "title": "下午盘 13:30 扫低点诱空、买方程序 Spooling 与 15:40–16:00 MOC 冲刺",
                "gist": "早盘完成高低点双扫并在高位留下干净等高点后，午休 12:00–13:00 绝不交易；13:30 后等待刺穿下午盘第一个短期波段低点完成洗盘，随后突破早盘高点开启连续阳线逼空（Spooling）直至收盘 MOC 加速。",
                "scene": "同一天（2022 年 2 月 1 日 ES 5m）下午盘 13:00–16:00 的走势。",
                "figureGuide": "观察粉色午休区右侧：14:15 紫色手势指出的小低点刺穿，以及 14:55 大阳线突破早盘等高点后一路连阳逼空至 16:00。",
                "figures": [
                    {"src": "lesson-assets/ep05_5m_pm_session_130_stop_hunt.png", "caption": "Ep.05 [10:40] 5m 下午盘启动：13:30 后向下刺穿首个短期波段低点（手势高亮处）洗盘后启动买方程序"},
                    {"src": "lesson-assets/ep05_5m_pm_spooling_moc.png", "caption": "Ep.05 [14:35] 5m 下午盘 Spooling 与 MOC：14:55 大阳线突破早盘等高点并留下 FVG，连续阳线逼空至 15:40–16:00 收盘高潮"}
                ],
                "read": [
                    {"who": "老师", "text": "早盘在 11:00–12:00 形成了非常干净的相对等高点（4,515）。12:00–13:00 纽约午休去吃午饭别看盘。13:30 算法宏启动后，先等它形成第一个短期 Swing Low，然后在 14:15 往下刺穿这个小低点扫掉跟风多头止损，接着开启 Buy Program Spooling！"},
                    {"who": "老师", "text": "如果你没在扫低点时进，就等 14:55 这根大阳线向上突破并留下 5m 看涨 FVG 时回踩做多。注意看下午单边趋势在 15:40、15:50 到 16:00 会因为 Market-on-Close (MOC) 指令再次加速冲高，在 16:00 前平仓收工！"}
                ],
                "plan": [
                    "12:00–13:00 强制离开屏幕休息",
                    "13:30 后标出首个短期波段低点与早盘相对等高点：扫低点收回或向上位移留出 5m FVG 时做多，持仓至 15:45–16:00 MOC 脉冲平仓"
                ],
                "trap": "在 12:30 午休下探时误以为空头趋势重启去追空；或者在下午盘算法开启单边阳线 Spooling 时不断逆势摸顶做空。",
                "principles": ["P01", "P08", "P09", "P11"]
            }
        ],
        "drill": "股指期货的四个季度交割月份字母代码分别是什么？在到期前一周如何利用 Barchart.com 判断该在哪一天切换主力合约？",
        "gaps": ""
    }
}

# Add distilled cards for Episodes 6 to 37 so ALL 37 episodes have a complete 3-layer distillation card!
STAGE_MAP_BY_EP = {
    6: (["P02", "P03", "P04"], "理解市场效率范式：散户把等高/等低点当支撑阻力，而聪明钱把它们当作建仓与平仓的对手盘止损池。"),
    7: (["P02", "P07", "P09"], "大幅单边扩张日之后常进入区间整固（Consolidation Hurdles）：外部止损池被扫后，目标自动切换回区间内部 50% 均衡位与内部 FVG。"),
    8: (["P01", "P05", "P07"], "ICT 2022 模型在外汇直盘（EURUSD / GBPUSD）完全通用：锁定伦敦盘 (02:00–05:00) 与纽约外汇盘 (07:00–10:00) 的高低点猎杀 + MSS + FVG。"),
    9: (["P02", "P04", "P10"], "Power of 3 (AMD)：以纽约午夜 00:00 开盘价为界，看跌日先在 00:00 开盘价上方制造诱多上影线（Judas Swing），看涨日先在下方制造诱空下影线。"),
    10: (["P01", "P04", "P10"], "用经济日历（ForexFactory）锁定操纵段触发时刻：08:30 数据脉冲与 09:30 美股开盘不是方向的原因，而是算法扫除流动性池的时间扳机。"),
    11: (["P01", "P05", "P08"], "09:30 美股现货开盘常出现上下双扫（Whipsaw）：耐心等待开盘首波噪音结束、真正刺穿 15m 关键位并走出 5m/2m/1m 同向 FVG 后再执行。"),
    12: (["P05", "P08", "P10"], "三层波段结构（LTH / ITH / STH）：只要回抽 HTF FVG 形成的中期高低点（ITH/ITL）未被突破，单边趋势就健康延续，止损只移至已确认的 ITH/ITL 外。"),
    13: (["P06", "P07", "P10"], "分形市场结构实战：在 15m/5m 确认 LTH 与 ITH 后，降维到 1m 图在每一次 STH 演化与小级别 FVG 回抽中顺势加仓或进场。"),
    14: (["P07", "P08", "P09"], "当单边位移腿内出现多个 FVG 时，优先选择处于 50% 均衡点溢价侧（做空）或折价侧（做多）且与 Order Block 重合的缺口挂单。"),
    15: (["P06", "P07", "P08"], "实盘走盘（Live Tape Reading）：当看涨/看跌订单块开盘价与 FVG 重叠时，价格常在缺口入口或 50% 中轴（CE）出现毫秒级反应。"),
    16: (["P01", "P08", "P09"], "单日双波段连击：早盘（08:30–11:00）达标后坚决落袋并空仓度过午休，下午盘（13:30 后）以早盘新高低点重新拉取 50% 均衡线寻找第二波机会。"),
    17: (["P02", "P07", "P10"], "外汇多周期联动：先看美元指数（DXY）奔向哪个日线流动性池，再在 EURUSD/GBPUSD 上寻找镜像的 Stop Raid + MSS + SIBI/BISI。"),
    18: (["P02", "P05", "P07"], "严禁在真空地带找 1m FVG：只有当价格触碰高时间框架（Daily/4H/1H/15m）关键 PD Array 的那一刻，1m/2m 的 MSS + FVG 才有机构背书。"),
    19: (["P01", "P02", "P09"], "构建日内叙事（Narrative）：先回答价格刚从哪个池子出来、下一个反向池子在哪、当前时间窗口需要先诱骗哪一方。"),
    20: (["P01", "P07", "P08"], "若夜盘/伦敦盘已提前透支大波幅并触及日线目标，纽约早盘往往先回撤至伦敦波段的 50%–70.5% 区域修整，切忌开盘盲目追高杀跌。"),
    21: (["P03", "P05", "P10"], "跨市场 SMT 背离（Smart Money Technique）：在关键高低点对比 ES、NQ、YM，若一个破前高而另一个拒破前高，即为机构暗中派发做空的铁证。"),
    22: (["P01", "P08", "P11"], "美联储 FOMC 议息日生存法则：14:00 利率决议第一波脉冲常为假突破扫损，必须等到 14:30 新闻发布会扫清流动性并走出干净 MSS + FVG 再参与。"),
    23: (["P02", "P07", "P09"], "FOMC 次日（周四）剧本：利用前一日剧烈波动形成的大区间 50% 均衡位与未回补 FVG，顺应主趋势捕捉高确定性次日波段。"),
    24: (["P05", "P06", "P08"], "高位迟滞反转处理：当价格刺穿 BSL 后未立刻暴跌而在高位筑顶震荡时，把结构跌破线（MSS）牢牢锚定在最后一次冲高前的关键 Swing Low。"),
    25: (["P07", "P08", "P12"], "1 分钟极速执行微操：挂单设在 FVG 入口边缘留 1–2 ticks 缓冲，或盯紧 FVG 的 50% 中轴（Consequent Encroachment, CE）收紧止损。"),
    26: (["P02", "P09", "P11"], "区分顺势扩张日与逆势回撤日：顺日线主势时目标可看外部远端高低点；逆日线主势做日内回撤时，触及首个 15m 内部 FVG 即平仓落袋。"),
    27: (["P01", "P08", "P11"], "震荡与密集新闻周的制胜关键是做减法：没有清晰的 15m 止损池猎杀 + 高能量位移 FVG，宁可全天 0 交易。"),
    28: (["P02", "P09", "P10"], "周内演化档案（Weekly Profile）：周一积累、周二或周三上午常借数据刺穿日线关键位形成全周高低点（周级 Manipulation），周三下午至周五单边派发。"),
    29: (["P03", "P07", "P09"], "早盘跳空缺口（Opening Range Gap / NDOG / NWOG）：09:30 开盘与前日 16:00 收盘价之间的跳空缺口是日内极强磁铁，常先回补缺口或其中轴再启动趋势。"),
    30: (["P06", "P07", "P10"], "PD Array 矩阵与平衡价格区间（BPR）：当快速拉升的看涨 FVG 被快速下砸的看跌 FVG 双向覆盖时，重叠区构成极强阻力的 BPR。"),
    31: (["P02", "P07", "P09"], "空头宏观周期下的高胜率法则：在日线不断创新低的熊市结构中，专注等待日内早盘向上扫掉前高进入溢价区 FVG 的顺势做空机会。"),
    32: (["P05", "P07", "P10"], "15m FVG 与 1m MSS 分形嵌套：当 15m FVG 过宽时，等价格刺入 15m FVG 内部（尤其 50% 中轴），再切到 1m 图等微型 MSS + 1m FVG 进场以压缩止损。"),
    33: (["P01", "P08", "P11"], "亏损后的风控降档铁律：遭遇止损后严禁报复性加仓；若连续亏损，下一笔必须将风险仓位砍半，直到用半仓赢回前次亏损的一半以上才恢复标准仓位。"),
    34: (["P02", "P03", "P09"], "跨日流动性地图：每天盘前必标前日最高价（PDH）与前日最低价（PDL），它们是次日早盘 08:30/09:30 最优先攻击的靶标。"),
    35: (["P01", "P04", "P08"], "识别 Seek & Destroy（搜寻与摧毁）绞肉机日：早盘先扫高点跌回中轴、再扫低点拉回中轴且无位移跟进（常见于非农/CPI前夕），发现后立刻关机观望。"),
    36: (["P05", "P07", "P09"], "全流程实盘合成：从盘前 HTF DOL 定位 → 15m 标高低点 → 等 08:30/09:30 猎杀 → 2m/1m MSS + 溢价/折价 FVG 挂单 → 内外流动性分批止盈。"),
    37: (["P01", "P11", "P12"], "大结局（One Model for Life）：亲手在 TradingView 上完成 100 张标准化历史复盘截图（Study Deck），按『模拟盘 → 微型合约 MNQ/MES → 标准合约』阶梯晋级。")
}

for ep_obj in cdata["episodes"]:
    ep_num = ep_obj["ep"]
    lid = f"ep{ep_num:02d}"
    if lid not in DISTILL_LESSONS:
        princs, core_text = STAGE_MAP_BY_EP.get(ep_num, (["P01", "P05", "P07"], ep_obj["summaryZh"]))
        cases = []
        for kp in ep_obj.get("keyPoints", []):
            cases.append({
                "title": f"[{kp['timeStr']}] {kp['titleZh']}",
                "gist": kp["detailZh"],
                "scene": f"Ep.{ep_num:02d}《{ep_obj['titleEn']}》时间轴 [{kp['timeStr']}] 核心教学段落。",
                "figureGuide": "",
                "figures": [],
                "read": [
                    {"who": "老师", "text": kp["detailZh"]},
                    {"who": "主模型", "text": f"结合前 5 集基础闭环，将该规则纳入 {ep_obj['module']} 的执行检查表。"}
                ],
                "plan": [
                    f"在原片 [{kp['timeStr']}] 处核对图表结构，并在 TradingView 历史盘面找出至少 2 个同类样本",
                    "未满足时间窗口与流动性猎杀前提时保持 Wait"
                ],
                "trap": "脱离高时间框架流动性背景（DOL）与纽约关键时间窗口，单独套用局部形态。",
                "principles": princs
            })
        DISTILL_LESSONS[lid] = {
            "status": "current",
            "core": core_text,
            "cases": cases,
            "drill": f"回看本集（Ep.{ep_num:02d}），这条规则在你的 6 步实盘核对清单中主要强化了哪一环？什么情况下该条件失效？",
            "gaps": ""
        }

# Build principleCases index
principle_cases = {p["id"]: [] for p in FRAMEWORK["principles"]}
for lid, d in DISTILL_LESSONS.items():
    ep_num = int(lid.replace("ep", ""))
    for idx, c in enumerate(d.get("cases", [])):
        for pid in c.get("principles", []):
            if pid in principle_cases:
                principle_cases[pid].append({
                    "lesson": lid,
                    "case": idx,
                    "date": f"Ep.{ep_num:02d}",
                    "gist": c["gist"]
                })

DISTILL_DATA = {
    "schema": "garbage-teacher-distill",
    "version": 1,
    "coverage": {
        "sourceLessons": len(cdata["episodes"]),
        "distilled": len(DISTILL_LESSONS)
    },
    "framework": FRAMEWORK,
    "lessons": DISTILL_LESSONS,
    "principleCases": principle_cases
}

with open(os.path.join(STUDY_DIR, "distill-data.js"), "w", encoding="utf-8") as f:
    f.write("window.LESSON_DISTILL = " + json.dumps(DISTILL_DATA, ensure_ascii=False, indent=2) + ";\n")

# 3. Build library-data.js (All 37 episodes with full HTML article, embedded 1080p keyframes, timestamp buttons, and collapsible bilingual transcript)
import glob
import re

TRANSCRIPTS_DIR = os.path.join(BASE_DIR, "transcripts")
HANDBOOK_PATH = os.path.join(BASE_DIR, "ICT_2022_Ep01_05_图文精读手册.md")

def load_transcript_segments(ep_num):
    pattern = os.path.join(TRANSCRIPTS_DIR, f"{ep_num:02d}_*.md")
    matches = glob.glob(pattern)
    if not matches:
        return [], 0
    with open(matches[0], "r", encoding="utf-8") as tf:
        raw = tf.read()
    segs = []
    words = 0
    for m in re.finditer(r"\*\*\[(\d{2}:\d{2}(?::\d{2})?)\]\*\*\s*(.+?)(?=\n\*\*\[|\Z)", raw, flags=re.S):
        ts = m.group(1).strip()
        txt = " ".join(m.group(2).strip().split())
        if not txt:
            continue
        parts_t = [int(x) for x in ts.split(":")]
        sec = parts_t[0] * 60 + parts_t[1] if len(parts_t) == 2 else parts_t[0] * 3600 + parts_t[1] * 60 + parts_t[2]
        words += len(txt.split())
        segs.append({"range": ts, "startSec": sec, "text": txt})
    return segs, words

def load_handbook_sections():
    if not os.path.exists(HANDBOOK_PATH):
        return {}
    with open(HANDBOOK_PATH, "r", encoding="utf-8") as hf:
        text = hf.read()
    sections = {}
    splits = re.split(r"(?=^## 第\s*[1-5]\s*集)", text, flags=re.M)
    for chunk in splits:
        m = re.match(r"^## 第\s*([1-5])\s*集[^\n]*\n(.+)", chunk, flags=re.S)
        if not m:
            continue
        ep_i = int(m.group(1))
        body = m.group(2).strip()
        # Convert simple markdown to clean HTML paragraphs/lists/codeblocks for the study room
        html_lines = []
        in_code = False
        for line in body.splitlines():
            if line.strip().startswith("```"):
                if not in_code:
                    html_lines.append('<pre class="hb-code"><code>')
                    in_code = True
                else:
                    html_lines.append("</code></pre>")
                    in_code = False
                continue
            if in_code:
                html_lines.append(line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
                continue
            if line.startswith("!["):
                continue
            if line.startswith("### "):
                html_lines.append(f"<h4>{line[4:].strip()}</h4>")
            elif line.startswith("#### "):
                html_lines.append(f"<h5>{line[5:].strip()}</h5>")
            elif line.startswith("> "):
                html_lines.append(f"<blockquote>{line[2:].strip()}</blockquote>")
            elif line.strip().startswith("- ") or line.strip().startswith("* "):
                content = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line.strip()[2:])
                html_lines.append(f"<p style='margin:4px 0 4px 14px;'>• {content}</p>")
            elif line.strip():
                content = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line.strip())
                html_lines.append(f"<p>{content}</p>")
        sections[ep_i] = "\n".join(html_lines)
    return sections

HANDBOOK_BY_EP = load_handbook_sections()

def build_lesson_html(ep_obj):
    ep_num = ep_obj["ep"]
    segs, calc_words = load_transcript_segments(ep_num)
    word_count = calc_words or ep_obj.get("wordCount", 0)
    parts = []
    # Summary blockquote
    parts.append(f'<blockquote><b>本集核心定位（{ep_obj["module"]}）：</b>{ep_obj["summaryZh"]}</blockquote>')

    # Video & Bilibili quick action bar inside lesson
    parts.append(
        f'<div class="lesson-video-bar">'
        f'<button type="button" class="primary" data-open-video="{ep_num}" data-sec="0">▶ 在多周期图谱 & 播放器中打开本集</button>'
        f'<a class="website-link" href="{ep_obj["biliUrl"]}" target="_blank" rel="noopener">📺 B站中配 P{ep_num} ↗</a>'
        f'<a class="website-link" href="{ep_obj["youtubeUrl"]}" target="_blank" rel="noopener">🎬 YouTube 原片 ↗</a>'
        f'</div>'
    )

    # KeyPoints section
    if ep_obj.get("keyPoints"):
        parts.append("<h3>一、关键时间轴与核心拆解</h3>")
        parts.append("<table><thead><tr><th>原片时间</th><th>核心教学节点</th><th>机构订单流拆解与执行要点</th></tr></thead><tbody>")
        for kp in ep_obj["keyPoints"]:
            parts.append(
                f'<tr>'
                f'<td style="white-space:nowrap"><button type="button" class="time-pill" data-open-video="{ep_num}" data-sec="{kp["seconds"]}">▶ [{kp["timeStr"]}]</button></td>'
                f'<td><b>{kp["titleZh"]}</b></td>'
                f'<td>{kp["detailZh"]}</td>'
                f'</tr>'
            )
        parts.append("</tbody></table>")

    # Keyframes gallery section
    if ep_obj.get("keyframes"):
        parts.append(f'<h3>二、原片 1080p 关键帧逐图精读（共 {len(ep_obj["keyframes"])} 张高清原图，点击图片放大）</h3>')
        for kf in ep_obj["keyframes"]:
            parts.append(
                f'<figure class="lesson-figure" data-seconds="{kf["seconds"]}" style="margin:14px 0">'
                f'<div style="display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px;">'
                f'<div><span class="badge-core">{kf["timeframe"]}</span> <b>{kf["titleZh"]}</b></div>'
                f'<button type="button" class="time-pill" data-open-video="{ep_num}" data-sec="{kf["seconds"]}">▶ 跳转原片 [{kf["timeStr"]}]</button>'
                f'</div>'
                f'<img src="lesson-assets/{kf["file"]}" alt="{kf["titleZh"]} — {kf["captionZh"]}">'
                f'<figcaption style="margin:8px 0 0;color:#20322f;font-size:0.92rem;">{kf["captionZh"]}</figcaption>'
                f'</figure>'
            )

    # Detailed Chinese handbook notes for Ep 1-5
    if ep_num in HANDBOOK_BY_EP:
        parts.append(f'<h3>三、本集深度图文精读讲义（完整复盘笔记）</h3>')
        parts.append(f'<div class="hb-deepdive">{HANDBOOK_BY_EP[ep_num]}</div>')

    # Full English Transcript in collapsible <details>
    if segs:
        sec_title = "四" if ep_num in HANDBOOK_BY_EP else "三"
        parts.append(
            f'<details class="transcript-details" open><summary>{sec_title}、原片英文逐字稿全文（共 {len(segs)} 个分钟切片 · {word_count} 词 · 点击时间戳跳转播放）</summary>'
            f'<div class="transcript-box">'
        )
        for seg in segs:
            parts.append(
                f'<div class="transcript-row">'
                f'<button type="button" class="time-pill" data-open-video="{ep_num}" data-sec="{seg["startSec"]}">[{seg["range"]}]</button>'
                f'<p>{seg["text"]}</p>'
                f'</div>'
            )
        parts.append("</div></details>")

    return "\n".join(parts)

lessons_list = []
total_images = 0
for ep_obj in cdata["episodes"]:
    ep_num = ep_obj["ep"]
    lid = f"ep{ep_num:02d}"
    img_cnt = len(ep_obj.get("keyframes", []))
    total_images += img_cnt
    html_body = build_lesson_html(ep_obj)
    search_blob = " ".join([
        ep_obj["titleZh"],
        ep_obj["titleEn"],
        ep_obj["summaryZh"],
        " ".join(ep_obj.get("tags", [])),
        " ".join(s["text"] for s in ep_obj.get("segments", []))
    ])
    lessons_list.append({
        "id": lid,
        "ep": ep_num,
        "date": f"Ep.{ep_num:02d}",
        "duration": f"{ep_obj['durationSec']//60:02d}:{ep_obj['durationSec']%60:02d}",
        "title": f"Ep.{ep_num:02d}｜{ep_obj['titleZh']}",
        "titleEn": ep_obj["titleEn"],
        "module": ep_obj["module"],
        "topics": [ep_obj["module"]] + ep_obj.get("tags", []),
        "imageCount": img_cnt,
        "hasLocalVideo": ep_obj["hasLocalVideo"],
        "localVideoUrl": ep_obj["localVideoUrl"],
        "videoId": ep_obj["videoId"],
        "biliUrl": ep_obj["biliUrl"],
        "youtubeUrl": ep_obj["youtubeUrl"],
        "keyframes": ep_obj.get("keyframes", []),
        "keyPoints": ep_obj.get("keyPoints", []),
        "preview": ep_obj["summaryZh"],
        "searchText": search_blob,
        "sourcePath": f"transcripts/{ep_num:02d}_{ep_obj['videoId']}.md",
        "sourceHeading": ep_obj["titleEn"],
        "html": html_body
    })

LIBRARY_DATA = {
    "schema": "ang-learning-library",
    "packagedAt": "2026-10-24",
    "dayCount": len(lessons_list),
    "imageCount": total_images,
    "latestDate": "Ep.01–Ep.37 全集",
    "sourcePath": os.path.dirname(os.path.abspath(__file__)),
    "topics": [
        "Module 1 · 核心模型与日内基石 (Ep 01–05)",
        "Module 2 · 日线偏向与 AMD 权力三段 (Ep 06–12)",
        "Module 3 · 订单块、多重失衡与多时段扩展 (Ep 13–20)",
        "Module 4 · 跨市场 SMT 背离与特种行情 (Ep 21–29)",
        "Module 5 · 实盘走盘回放、风控与终极闭环 (Ep 30–37)"
    ],
    "lessons": lessons_list,
    "glossary": cdata["glossary"]
}

with open(os.path.join(STUDY_DIR, "library-data.js"), "w", encoding="utf-8") as f:
    f.write("window.ANG_LIBRARY = " + json.dumps(LIBRARY_DATA, ensure_ascii=False, indent=2) + ";\n")

# 4. Build course.js (Guided comprehension practice batches with Wait / Armed / Execute / Cancel / Exit state machine)
COURSE_BATCHES = {
    "version": 1,
    "batches": [
        {
            "id": "ict-ep02-elements-v1",
            "title": "第 01 组 · Ep.02 交易模型四大要素与状态判定",
            "desc": "对应 Ep.02 NQ 2022-01-21 案例 · 区分诱空、猎杀、BMS 与溢价区 FVG 挂单",
            "lesson": "ep02",
            "questions": [
                {
                    "id": "ict-q-ep02-sucker",
                    "title": "A / 早盘先跌破短期小低点（14,600）能追空吗？",
                    "context": "日线看跌（下方 14,366.75 SSL 未扫），但上方 14,820 存在极其干净的 15m 相对等高点（Buyside Liquidity）。早盘 10:15 价格先向下跌破了 14,600 短期低点，此时尚未触及上方 14,820 等高点。对于计划做空上方等高点的你，现在处于什么状态？",
                    "answer": "Wait",
                    "explanation": "Wait（等待）。在大级别等高点（14,820 BSL）未被猎杀前，下方小低点的跌破往往是诱导散户追空的 Sucker Play（或日内先扫 SSL 做多去拿上方 BSL 的多头机会）。对于高空计划，必须等 14,820 BSL 被刺穿。",
                    "prompt": "写出为什么不能在 14,600 跌破时直接追空？"
                },
                {
                    "id": "ict-q-ep02-bms-fvg",
                    "title": "B / 刺穿 14,820 后跌破 2m 波段低点并留下 FVG，但尚未回抽",
                    "context": "11:25 价格冲高至 14,855 刺穿了 14,820 BSL，随后在 2m 图强力跌破 14,808 短期波段低点（BMS），并在 14,798–14,805（高于 50% 均衡线的溢价区）留下三 K 线看跌 FVG。当前第 3 根阴线刚收盘于 14,785，尚未向上回抽进 FVG。此时你的状态是？",
                    "answer": "Armed",
                    "explanation": "Armed（已就绪/挂单待触发）。Stop Raid（扫 14,820）+ 2m BMS（破 14,808）+ 溢价区看跌 FVG 均已齐备，止损 S（14,855 上方）与折价区目标 T（14,675）已明确，正在等待阳线向上回抽触及 FVG 入口 E（14,798）成交。",
                    "prompt": "写出此时 E（入场）、S（止损）、T（目标）分别在哪里？"
                },
                {
                    "id": "ict-q-ep02-target",
                    "title": "C / 阳线回抽触及 14,798 FVG 下沿，该如何执行与设止盈？",
                    "context": "下一根 2m 阳线向上回抽触及了 14,798.25（溢价区看跌 FVG 下沿），且未破坏上方 14,855 止损边界。此时你的状态是什么？第一止盈位必须满足什么条件？",
                    "answer": "Execute",
                    "explanation": "Execute（执行入场）。遵守“在阳线回抽进入溢价区看跌 FVG 时做空”的铁律，成交后目标必须跨过 50% Equilibrium（均衡线），在绿色折价区内部的看涨 FVG（14,680 / 14,650）与外部 Sell Stops 分批止盈。",
                    "prompt": "写出你的执行动作以及止盈必须跨过哪条分界线？"
                }
            ]
        },
        {
            "id": "ict-ep03-ob-mss-v1",
            "title": "第 02 组 · Ep.03 内部流动性、多空双向与订单块交付状态",
            "desc": "对应 Ep.03 订单块开盘价翻转与纽约时间纪律 · 带提示理解检查",
            "lesson": "ep03",
            "questions": [
                {
                    "id": "ict-q-ep03-state",
                    "title": "A / 连续 4 根阴线刺穿 14,600 SSL，何时确认交付状态由卖转买？",
                    "context": "10:15–10:20 价格以一串连续 4 根阴线刺穿了 14,600 卖方止损池探底 14,538，随后拉起突破了这串连续阴线第一根 K 线的开盘价，并刺穿 14,634 短期波段高点留下看涨 FVG。当价格回踩该看涨 FVG 与订单块开盘价重合区时，应选择什么动作？",
                    "answer": "Execute",
                    "explanation": "Execute（执行做多）。连续阴线构成看涨订单块（Bullish Order Block），向上突破第一根阴线开盘价即发生 Change in the State of Delivery（交付状态由空转多），叠加 Bullish MSS 与看涨 FVG 回踩，做多目标直指上方 14,820 BSL。",
                    "prompt": "写出订单块交付状态改变（Change in State of Delivery）的判定价格线？"
                },
                {
                    "id": "ict-q-ep03-lunch",
                    "title": "B / 纽约时间 12:25 午休时段出现看似完美的 1m FVG",
                    "context": "早盘行情结束后，纽约时间 12:25（处于 12:00–13:00 New York Lunch 期间），你在 1 分钟图上看到一个小高点被刺穿并出现了一个微型 FVG，你想立刻开仓做空。按照 ICT 作息铁律，此时应该处于什么状态？",
                    "answer": "Wait",
                    "explanation": "Wait（空仓等待/休息）。12:00–13:00 是纽约午休禁区（No-Trade Zone），算法趋势交付暂停，极易上下扫损。无论图形看起来多诱人，午休期间一律不开新仓，等待 13:30 下午盘宏启动。",
                    "prompt": "写出纽约午休禁区的具体时间段（NY Time）？"
                },
                {
                    "id": "ict-q-ep03-missed",
                    "title": "C / 看跌 FVG 未给回抽直接瀑布式暴跌至 50% 以下目标区",
                    "context": "你在溢价区看跌 FVG 挂了限价空单（Armed），但价格过于弱势，根本没有回抽触及你的 FVG 就直接一泻千里跌穿了 50% 均衡线并触及了下方折价区的内部看涨 FVG 目标位。此时你对原挂单应该做什么？能市价追空吗？",
                    "answer": "Cancel",
                    "explanation": "Cancel（取消原未成交挂单，绝不市价追空）。价格已经到达折价区目标位，风险收益比已完全倒置；此时取消上方原限价单，接受错过，绝不在折价区地板价追空。",
                    "prompt": "为什么价格已经跌到折价区目标附近时必须 Cancel 原挂单而不能市价追入？"
                }
            ]
        },
        {
            "id": "ict-ep04-05-orderflow-v1",
            "title": "第 03 组 · Ep.04 强迫市场亮底牌 & Ep.05 下午盘 13:30 剧本",
            "desc": "对应 Ep.04 过滤无 FVG 的首次回落与 Ep.05 三推诱多 + 下午盘 MOC",
            "lesson": "ep04",
            "questions": [
                {
                    "id": "ict-q-ep04-nofvg",
                    "title": "A / 刺穿 BSL 后的第一波回落没有任何 Fair Value Gap",
                    "context": "如 Ep.04 图示：08:30 后价格拉升刺穿了前高 Buyside Liquidity，随后出现第一波小幅回调，但这几根下跌 K 线彼此全部重叠，内部没有任何三 K 线 FVG（或者尚未跌破最近的短期波段低点）。此时你能提前市价做空吗？",
                    "answer": "Wait",
                    "explanation": "Wait（按兵不动，强迫市场亮出底牌）。没有位移 + 没有 FVG = 算法尚未确认空头交付，极可能还会再往上拱出新高（二次冲顶）去扫早进场空头的止损。必须等到出现高能量位移（大象跳泳池）且留下清晰 FVG 再行动。",
                    "prompt": "写出“强迫市场亮出底牌（Forcing the market to tip its hand）”等待的两个硬条件？"
                },
                {
                    "id": "ict-q-ep05-pm130",
                    "title": "B / 下午盘 14:15 向下刺穿 13:30 后的首个短期波段低点并迅速收回",
                    "context": "如 Ep.05 图示：早盘已在 4,515 留下一排干净的相对等高点（BSL）。度过 12:00–13:00 午休后，价格在 14:15 向下刺穿了 13:30 之后形成的第一个短期波段低点（完成下午盘诱空洗盘），随即强力拉起突破短期高点并留下 5m 看涨 FVG。回踩该 FVG 时应执行什么动作？",
                    "answer": "Execute",
                    "explanation": "Execute（执行做多）。13:30 后刺穿首个短期波段低点是典型的下午盘诱空猎杀（Stop Hunt），旨在启动下午盘买方程序（Buy Program Spooling）去攻克早盘留下的 4,515 相对等高点。",
                    "prompt": "下午盘这笔多单的主要流动性磁铁（DOL）在哪里？尾盘哪个时间段会因 MOC 加速？"
                },
                {
                    "id": "ict-q-ep05-exit1600",
                    "title": "C / 下午盘多单一路 Spooling 逼空进入 15:50–16:00 MOC 脉冲",
                    "context": "你在下午盘 14:55 的看涨 FVG 做多已顺利突破早盘等高点 4,515，算法连续收阳逼空（Spooling），现在时间来到 15:55 NY Time，Market-on-Close (MOC) 收盘指令引发最后一波加速冲高。对于你手中的日内多单，现在应该执行什么动作？",
                    "answer": "Exit",
                    "explanation": "Exit（止盈平仓离场）。ICT 2022 模型是纯日内模型（Intraday），15:40–16:00 的 MOC 加速正是全天多头派发的高潮终点，必须在 16:00 收盘及日内休市前主动平仓落袋，不留隔夜赌博敞口。",
                    "prompt": "写出下午盘趋势单在收盘前哪三个时间节点常出现 MOC 加速？"
                }
            ]
        }
    ]
}

with open(os.path.join(STUDY_DIR, "course.js"), "w", encoding="utf-8") as f:
    f.write("window.STUDY_COURSE = " + json.dumps(COURSE_BATCHES, ensure_ascii=False, indent=2) + ";\n")

print("Successfully generated study-room data files: distill-data.js, library-data.js, course.js")
