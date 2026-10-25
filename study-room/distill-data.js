window.LESSON_DISTILL = {
  "schema": "ict-2022-distill",
  "version": 2,
  "framework": {
    "schema": "ict-2022-distill-framework",
    "version": 2,
    "identity": "学习室的条件分析与训练框架；除显式证据外均为主模型归纳，不是对市场机制的实证保证。",
    "chain": [
      {
        "id": "S1",
        "title": "时间与环境",
        "question": "数据、会话、新闻、风险预算是否齐全？"
      },
      {
        "id": "S2",
        "title": "流动性地图",
        "question": "候选目标和反向路径是什么？"
      },
      {
        "id": "S3",
        "title": "清扫与路径",
        "question": "观察到什么，哪些路径已经失效？"
      },
      {
        "id": "S4",
        "title": "位移与结构",
        "question": "哪个 swing 何时被突破？证据是否独立？"
      },
      {
        "id": "S5",
        "title": "位置与管理",
        "question": "区间锚点、FVG、E/S/T 和取消条件是什么？"
      },
      {
        "id": "S6",
        "title": "复盘与训练",
        "question": "当时可见证据、实际结果和反例是什么？"
      }
    ],
    "principles": [
      {
        "id": "P01",
        "stage": "S1",
        "title": "限定训练模型与风险",
        "rule": "先记录品种、合约、日期、America/New_York 时区、会话和新闻日历；入场前确定风险上限。",
        "oneLine": "先记录品种、合约、日期、America/New_York 时区、会话和新闻日历；入场前确定风险上限。",
        "trap": "将教学演示当成保证盈利的方法。",
        "how": [
          "先记录品种、合约、日期、America/New_York 时区、会话和新闻日历；入场前确定风险上限。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P02",
        "stage": "S2",
        "title": "观察与解释分开",
        "rule": "旧高低点和 FVG 是候选位置；DOL 是有条件的方向假设，必须给出失效条件。",
        "oneLine": "旧高低点和 FVG 是候选位置；DOL 是有条件的方向假设，必须给出失效条件。",
        "trap": "把价格必然扫损或必然回补作为事实。",
        "how": [
          "旧高低点和 FVG 是候选位置；DOL 是有条件的方向假设，必须给出失效条件。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P03",
        "stage": "S2",
        "title": "流动性地图有时效",
        "rule": "记录可见高低点及形成时刻，BSL/SSL 是框架中的候选止损区域，K 线不能证明实际订单数量。",
        "oneLine": "记录可见高低点及形成时刻，BSL/SSL 是框架中的候选止损区域，K 线不能证明实际订单数量。",
        "trap": "等高等低必然被刺穿，或者扫后必然反转。",
        "how": [
          "记录可见高低点及形成时刻，BSL/SSL 是框架中的候选止损区域，K 线不能证明实际订单数量。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P04",
        "stage": "S3",
        "title": "猎杀路径与反例",
        "rule": "本训练模型观察先清扫候选流动性、再出现反向确认的路径；直接延续或没有清扫时可不交易，不强行解释为陷阱。",
        "oneLine": "本训练模型观察先清扫候选流动性、再出现反向确认的路径；直接延续或没有清扫时可不交易，不强行解释为陷阱。",
        "trap": "把没有入场机会误判成市场方向错误。",
        "how": [
          "本训练模型观察先清扫候选流动性、再出现反向确认的路径；直接延续或没有清扫时可不交易，不强行解释为陷阱。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P05",
        "stage": "S4",
        "title": "MSS 与位移分别记录",
        "rule": "记录被突破 swing 的价位、确认时刻及突破方式；记录位移幅度、实体和上下文。日内 MSS 不自动意味着多日反转。",
        "oneLine": "记录被突破 swing 的价位、确认时刻及突破方式；记录位移幅度、实体和上下文。日内 MSS 不自动意味着多日反转。",
        "trap": "只要大 K 线或任何微小破位就认定 MSS。",
        "how": [
          "记录被突破 swing 的价位、确认时刻及突破方式；记录位移幅度、实体和上下文。日内 MSS 不自动意味着多日反转。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P06",
        "stage": "S4",
        "title": "OB 与交付变化不替代结构",
        "rule": "记录阴阳线串及采用的开盘价；交付变化、MSS 和位移分开核验，CISD 不作为替代 MSS 的或条件。",
        "oneLine": "记录阴阳线串及采用的开盘价；交付变化、MSS 和位移分开核验，CISD 不作为替代 MSS 的或条件。",
        "trap": "任意阴线都叫看涨 OB，或单凭开盘价突破立即入场。",
        "how": [
          "记录阴阳线串及采用的开盘价；交付变化、MSS 和位移分开核验，CISD 不作为替代 MSS 的或条件。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P07",
        "stage": "S5",
        "title": "冻结区间后计算位置",
        "rule": "事前记录 rangeLow、rangeHigh、rangeAsOf；中点=(低+高)/2。区间均衡与 FVG 的 CE 分开计算。",
        "oneLine": "事前记录 rangeLow、rangeHigh、rangeAsOf；中点=(低+高)/2。区间均衡与 FVG 的 CE 分开计算。",
        "trap": "使用未来终点重画区间，把任何入场都解释成折价或溢价。",
        "how": [
          "事前记录 rangeLow、rangeHigh、rangeAsOf；中点=(低+高)/2。区间均衡与 FVG 的 CE 分开计算。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P08",
        "stage": "S5",
        "title": "三根已完成 K 线定义 FVG",
        "rule": "看涨：Low3>High1，区间[High1,Low3]；看跌：High3<Low1，区间[High3,Low1]。限价触价与收盘确认是不同规则。无 FVG 不做仅为本训练模型限制。",
        "oneLine": "看涨：Low3>High1，区间[High1,Low3]；看跌：High3<Low1，区间[High3,Low1]。限价触价与收盘确认是不同规则。无 FVG 不做仅为本训练模型限制。",
        "trap": "把中间蜡烛实体称为无成交缺口，或用未收盘第三根确认 FVG。",
        "how": [
          "看涨：Low3>High1，区间[High1,Low3]；看跌：High3<Low1，区间[High3,Low1]。限价触价与收盘确认是不同规则。无 FVG 不做仅为本训练模型限制。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P09",
        "stage": "S5",
        "title": "计划风险、目标和取消条件",
        "rule": "先验证 E/S/T 方向、合约数、成本与可达目标；目标不要求机械跨过中点。触价仅是模拟触发，实际成交须独立确认。",
        "oneLine": "先验证 E/S/T 方向、合约数、成本与可达目标；目标不要求机械跨过中点。触价仅是模拟触发，实际成交须独立确认。",
        "trap": "把看见目标等同于实现盈利，忽略未成交、滑点及挂单失效。",
        "how": [
          "先验证 E/S/T 方向、合约数、成本与可达目标；目标不要求机械跨过中点。触价仅是模拟触发，实际成交须独立确认。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P10",
        "stage": "S1",
        "title": "分开新开仓与持仓管理",
        "rule": "Ep.03 [13:09]：早盘通常08:30–11:00，可延至中午；午休避免寻找新机会；下午偏好13:30后。本训练新开仓窗口08:30–12:00、13:30–15:30，16:00前结束日内持仓是训练规则。",
        "oneLine": "Ep.03 [13:09]：早盘通常08:30–11:00，可延至中午；午休避免寻找新机会；下午偏好13:30后。本训练新开仓窗口08:30–12:00、13:30–15:30，16:00前结束日内持仓是训练规则。",
        "trap": "把午休不开新仓说成市场算法暂停，或把16:00现金收盘说成期货休市。",
        "how": [
          "Ep.03 [13:09]：早盘通常08:30–11:00，可延至中午；午休避免寻找新机会；下午偏好13:30后。本训练新开仓窗口08:30–12:00、13:30–15:30，16:00前结束日内持仓是训练规则。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P11",
        "stage": "S3",
        "title": "SMT、三推与 AMD 是条件证据",
        "rule": "SMT 对齐相关品种、时段和 swing，作为辅助而非机构意图证明。三推和 AMD 是候选演化路径，不要求每个交易日出现。",
        "oneLine": "SMT 对齐相关品种、时段和 swing，作为辅助而非机构意图证明。三推和 AMD 是候选演化路径，不要求每个交易日出现。",
        "trap": "看见背离就断言机构派发，或按事后日高低拼接 AMD。",
        "how": [
          "SMT 对齐相关品种、时段和 swing，作为辅助而非机构意图证明。三推和 AMD 是候选演化路径，不要求每个交易日出现。"
        ],
        "layer": "条件训练框架"
      },
      {
        "id": "P12",
        "stage": "S6",
        "title": "记录所有结果",
        "rule": "保留计划、成交、取消、错过、止损与无交易样本；记录观察截止时刻、费用、结果和理由。案例标注练习不等于有统计意义的回测。",
        "oneLine": "保留计划、成交、取消、错过、止损与无交易样本；记录观察截止时刻、费用、结果和理由。案例标注练习不等于有统计意义的回测。",
        "trap": "只挑成功的确定性波段，用动作答对率代替交易能力。",
        "how": [
          "保留计划、成交、取消、错过、止损与无交易样本；记录观察截止时刻、费用、结果和理由。案例标注练习不等于有统计意义的回测。"
        ],
        "layer": "条件训练框架"
      }
    ],
    "sessionPolicy": {
      "id": "study-ny-v2",
      "timeZone": "America/New_York",
      "newEntryWindows": [
        [
          "08:30",
          "12:00"
        ],
        [
          "13:30",
          "15:30"
        ]
      ],
      "windowEndExclusive": true,
      "cancelPendingAt": [
        "12:00",
        "15:30"
      ],
      "trainingFlatBy": "16:00",
      "source": "主模型训练限制；Ep.03 [13:09] 仅支持一般时段说明。"
    },
    "states": {
      "Wait": "证据不足；可等待或当天不交易。",
      "Armed": "本训练条件与风险检查已齐，模拟挂单尚未成交。",
      "Execute": "本练习模拟触发；不授权下单，不证明实际成交。",
      "Cancel": "未成交且目标先到、结构失效或新开仓窗口结束。",
      "Exit": "已有持仓达到预设退出条件；区别于取消挂单。"
    },
    "boundaries": [
      "IRL可包含已声明区间内的短期摆动点相关流动性或失衡；ERL随所声明区间而定。",
      "Opening Range Gap、NDOG、NWOG分别记录RTH/ETH、市场与开闭市锚点，不混用，也不补造课内归属。",
      "Macro、Killzone、交易会话与数据公布时点分别记录，现金收盘不等于期货休市。",
      "FVG中点CE、所选区间0.5与OB开盘价是不同坐标。",
      "百张成功图例不是统计回测；验证需预定义窗口与规则，计入成本、失败样本并保留样本外数据。"
    ],
    "macroWindows": [
      {
        "time": "08:50–09:10",
        "session": "AM Pre-Market Macro",
        "focus": "观察开盘前是否接近候选流动性或失衡区域；不预判09:30方向。",
        "id": "ny-0850-0910",
        "evidenceStatus": "pending",
        "attribution": "用户新增观察笔记；主模型整理",
        "claimedSeries": "2024，具体年份归属与原课片段待核对",
        "sourceRefs": []
      },
      {
        "time": "09:50–10:10",
        "session": "AM Main Macro",
        "focus": "观察开盘初段之后是否形成清晰路径、位移与结构确认；不将该时段等同于高胜率。",
        "id": "ny-0950-1010",
        "evidenceStatus": "pending",
        "attribution": "用户新增观察笔记；主模型整理",
        "claimedSeries": "2024，具体年份归属与原课片段待核对",
        "sourceRefs": []
      },
      {
        "time": "10:50–11:10",
        "session": "Late Morning Macro",
        "focus": "观察早盘目标、动能延续或衰减；先记录实际价格证据。",
        "id": "ny-1050-1110",
        "evidenceStatus": "pending",
        "attribution": "用户新增观察笔记；主模型整理",
        "claimedSeries": "2024，具体年份归属与原课片段待核对",
        "sourceRefs": []
      },
      {
        "time": "11:50–12:10",
        "session": "Pre-Lunch Macro",
        "focus": "观察午休边界附近的回补或清扫候选；12:00后按当前训练不新增交易。",
        "id": "ny-1150-1210",
        "evidenceStatus": "pending",
        "attribution": "用户新增观察笔记；主模型整理",
        "claimedSeries": "2024，具体年份归属与原课片段待核对",
        "sourceRefs": []
      },
      {
        "time": "13:15–13:45",
        "session": "PM Session Macro",
        "focus": "观察下午盘前后的流动性与结构；13:30前按当前训练不新增交易。",
        "id": "ny-1315-1345",
        "evidenceStatus": "pending",
        "attribution": "用户新增观察笔记；主模型整理",
        "claimedSeries": "2024，具体年份归属与原课片段待核对",
        "sourceRefs": []
      },
      {
        "time": "15:15–15:45",
        "session": "MOC / Closing Macro",
        "focus": "观察尾盘前的波动与持仓管理；该窗口不等同于NYSE主板收盘竞价不平衡公布时段。",
        "id": "ny-1515-1545",
        "evidenceStatus": "pending",
        "attribution": "用户新增观察笔记；主模型整理",
        "claimedSeries": "2024，具体年份归属与原课片段待核对",
        "sourceRefs": []
      }
    ],
    "htfEvolution2023": {
      "dailyBiasAnchor": "分析日内偏向时，先声明日线或周线所选区间、候选PD Array及流动性位置，并记录分析截止时刻。大周期背景不清时保持偏向待定，不能凭小周期噪声补造方向。",
      "dealingRangeExpansion": "若所选大周期区间与当前价格证据支持向上扩张，可将看涨路径列为候选，并分别记录逆向回撤与反转的确认、失效条件。大周期偏向可能失败；折价向溢价的路径本身不能证明顺势期望收益更高，也不能把所有看跌信号归为弱回调。",
      "source": "用户标记为2023–2024演进补充；本轮仅完成概念与系统边界整理，尚未核读对应原课。年份、原话与规则归属待具体视频和时间戳核验。",
      "evidenceStatus": "pending",
      "sourceRefs": []
    },
    "extensionSourceNotes": {
      "checkedOn": "2026-10-25",
      "NYSE": {
        "url": "https://www.nyse.com/trade/auctions",
        "status": "official_page_read",
        "scope": "NYSE主板收盘竞价时间，不能用于证明Macro窗口或方向"
      },
      "ICT": {
        "status": "video_passages_not_read",
        "note": "检索发现官方Macro相关视频；本轮未取得对应原课正文，不据此核验六个窗口或2023–2024年份归属。"
      }
    },
    "comparativePerspectives": [
      {
        "id": "2c-trading",
        "name": "2C Trading (Al Brooks 裸K价格行为学)",
        "channel": "YouTube @2C_trading (2025.03–2026.10 · 300+ 实盘与复盘视频，含 2026-09 支阻快速寻找与 2026-10 实盘更新)",
        "role": "外部对比与补充视角（严禁混淆为 ICT 2022 官方教学）",
        "evidenceStatus": "external_verified",
        "localSource": "Documents/trading-notes/methodology/2C_trading_system/",
        "corePhilosophy": {
          "oneMethod": "只精通一种方法稳定盈利，熟练后加大仓位，而不是学更多方法",
          "probabilityMindset": "做的是概率：高概率+盈亏比差可做，低概率+盈亏比好需精确位置；交易频率上升则胜率下降",
          "disciplineOverTechnique": "走不顺就主动离场（不等止损）；连续不顺就休息；系统赚多少拿多少",
          "conservativeData": "23天实盘回测只用剥头皮（反转K+50%挂单）：36笔交易，82%胜率，2.2均R，4天零交易"
        },
        "keyComparisons": [
          {
            "dimension": "核心进场形态",
            "ict2022": {
              "title": "FVG (Fair Value Gap) 价值失衡缺口",
              "mechanism": "3根K线结构位移：第1根与第3根影线不重叠留出缺口，价格回抽触及缺口即为算法再平衡点",
              "timing": "严格位于 Killzone (08:30–11:00 / 13:30–15:30) 内且在折价/溢价区",
              "execution": "触价限价入场或收盘确认入场，止损置于摆动点外"
            },
            "twoCTrading": {
              "title": "3根K微通道剥头皮 与 50%波段限价挂单",
              "mechanism": "通道内3根连续趋势K（实体大、收盘在极值），在整组3根K的50%回调位挂限价单；未破50%极强，破了50%偏弱",
              "timing": "5分钟为主图，开盘第1-50根K内；必须由 EMA20 动态辅助提供支撑/阻力",
              "execution": "50%限价单进场，止损置于第1根K或波段起点外1 tick，止盈严格1:1 (1R)"
            },
            "synthesis": "两者本质均是在强位移波段寻找机构回踩点。ICT 用 FVG 空间失衡作为磁吸，2C 用 50% 几何平衡点结合 EMA20 作为动力反弹点。"
          },
          {
            "dimension": "反转与结构转变",
            "ict2022": {
              "title": "MSS (Market Structure Shift) 市场结构转变",
              "mechanism": "必须先完成对流动性池（BSL / SSL）的清扫刺穿，随后大实体穿透关键短期摆动高低点，完成交割方向逆转",
              "timing": "流动性清扫发生后",
              "execution": "伴随位移形成 FVG 确认，不猜顶底"
            },
            "twoCTrading": {
              "title": "反转K (Reversal Bar) 与形态验证",
              "mechanism": "连续趋势后第一根反向收盘K即为反转K；但在强趋势中第一次反转K容易失败；交易区间内80%突破为假突破",
              "timing": "在关键位置（交易区间边缘、高开/低开关键位）出现",
              "execution": "反转K收盘位直接做，或在反转K 50%挂单，止损放在反转K极值外1 tick"
            },
            "synthesis": "ICT 依赖外部流动性清扫与层级结构破坏；2C 关注单根反转K的动量衰竭与交易区间假突破（80%概率反转）。"
          },
          {
            "dimension": "过滤系统与指标哲学",
            "ict2022": {
              "title": "纯裸K + Time & Price 算法时间窗口",
              "mechanism": "杜绝一切传统均线与滞后指标；核心驱动是央行算法按时间交割订单流（Killzone、Macro 窗口、开盘基准价）",
              "timing": "时间优先于形态",
              "execution": "非交易窗口完全不开新仓"
            },
            "twoCTrading": {
              "title": "EMA20 动态磁铁与顺势顺风车",
              "mechanism": "EMA20 是强有力的动态支撑/阻力与趋势基准；日线在 EMA20 上方偏多、下方偏空；K线远离 EMA20 会被拉回，贴近 EMA20 顺势起爆",
              "timing": "开盘前50根5m K线",
              "execution": "3根K微通道必须有 EMA20 辅助才能大幅提升止盈率"
            },
            "synthesis": "ICT 以「时间基准（Macro/Killzone）」划分有效性，2C 以「均线位置（EMA20/远离拉回）」过滤虚假波动。"
          },
          {
            "dimension": "时间周期与执行颗粒度",
            "ict2022": {
              "title": "HTF (1D/1H/15m) 定偏向 → LTF (1m/2m) 精细执行",
              "mechanism": "大周期确定目标池与 Dealing Range，1m/2m 寻找微观 MSS + FVG，放大盈亏比",
              "timing": "高低周期嵌套",
              "execution": "秒级/1m 抓最小止损"
            },
            "twoCTrading": {
              "title": "坚决反对 1m 图 · 5m 主战场 · 15m 看形态",
              "mechanism": "铁律第4条明确禁止1分钟图（噪音大、过早进场导致被频繁打止损）；15m找收敛/通道/区间，5m执行进出",
              "timing": "5分钟K线收盘或50%挂单",
              "execution": "拒绝微观追单，等待5m形态成型"
            },
            "synthesis": "ICT 追求极致压缩止损（1m入场），2C 追求信号稳定性（5m主图防震荡陷阱）。初学者使用 2C 5m 图能有效避免在 1m 噪音中过度交易。"
          },
          {
            "dimension": "止盈与离场纪律",
            "ict2022": {
              "title": "非对称高盈亏比 (Asymmetric R:R) · 目标对侧流动性",
              "mechanism": "以大周期的 BSL/SSL 或未回补 FVG 为终极止盈，追求 1:3 甚至更高 R:R",
              "timing": "价格触及目标流动性池",
              "execution": "分批减仓（Partial Take Profit），止损移至保本（BE）"
            },
            "twoCTrading": {
              "title": "高概率拿 1R (1:1) · 走不顺主动离场",
              "mechanism": "高概率形态只拿 1R 利润，极强趋势才拿 2R；坚守概率思维，不贪大波段",
              "timing": "触及 1:1 或盘面走不顺",
              "execution": "铁律第1条：走不顺不等止损被动触发，差几点就主动跑；不改大止损，不加仓"
            },
            "synthesis": "ICT 靠高盈亏比拉大期望值，2C 靠高胜率（80%+）与坚决主动止损确保账户稳定增长。"
          }
        ],
        "tenBlacklistRules": [
          {
            "num": 1,
            "rule": "不追涨杀跌",
            "slogan": "高开不追多，低开不追空；宁可错过不可做错"
          },
          {
            "num": 2,
            "rule": "不在交易区间中间做单",
            "slogan": "只在区间边缘做高空低多，中间是绝对死区"
          },
          {
            "num": 3,
            "rule": "收敛三角形不做",
            "slogan": "收敛末端是观望区，绝不左侧开仓猜突破"
          },
          {
            "num": 4,
            "rule": "不看1分钟图",
            "slogan": "1分钟全是杂音与诱骗，过早进场必被打损"
          },
          {
            "num": 5,
            "rule": "不加仓",
            "slogan": "盈利想加仓=灾难，一次回调直接打穿本金"
          },
          {
            "num": 6,
            "rule": "不改止损",
            "slogan": "进场前算好止损，中途改一次2.5R直接亏空"
          },
          {
            "num": 7,
            "rule": "低波动日不做",
            "slogan": "日内预期波幅 <15点直接关电脑休息"
          },
          {
            "num": 8,
            "rule": "不跟第三推对抗",
            "slogan": "区间内第三推形成强趋势时立刻离场，绝不逆势抗单"
          },
          {
            "num": 9,
            "rule": "强趋势不做反转",
            "slogan": "强单边趋势中顺势做50%回调，不做第1次反转K"
          },
          {
            "num": 10,
            "rule": "不强迫开单",
            "slogan": "没有标准形态=最好的交易就是什么都不做"
          }
        ],
        "threeCandleMicroChannelSop": {
          "title": "3根K微通道剥头皮标准执行 SOP (3-Bar Micro Channel Scalp)",
          "steps": [
            "识别条件：在既定趋势通道内，发现连续3根（或4-5根）强趋势K线（实体饱满、无长影线、最后一根创出新极值）",
            "环境确认：K线顺应 EMA20 方向（EMA20 呈倾斜角度支撑/压制）；不在区间中间或通道最末端",
            "挂单进场：拉出这3根K线的总体波段，在 50% 回调位提前挂限价单（Limit Order）等待回踩触碰",
            "止损设定：严格放置在第 1 根 K 线起点外 1 tick（若破 50% 且破第 1 根则形态失效）",
            "止盈管理：严格 1:1（1R）止盈出场；若行情走势迟疑、回踩跌破 50% 且无买力弹起，主动提前离场"
          ],
          "keyframeShowcase": [
            {
              "file": "4zkG0jdEsy8_08m.jpg",
              "caption": "最新实盘支阻：08m 处 K14大阳包吞反转，被套空头平仓买盘转化为强支撑"
            },
            {
              "file": "4zkG0jdEsy8_11m.jpg",
              "caption": "最新交易区间：11m 处上中下 1/3 规则，上空下多，中间死区不操作"
            },
            {
              "file": "zDCnoIImHHM_18m.jpg",
              "caption": "最新实盘禁忌：18m 处交易区间内严禁 4 根阳线 50% 挂单（深回撤扫损）与平保跑路"
            },
            {
              "file": "yrtwu3BSnhQ_02m.jpg",
              "caption": "经典微通道剥头皮：2m 处 3根连续趋势K与50%回调位标记"
            },
            {
              "file": "yrtwu3BSnhQ_05m.jpg",
              "caption": "经典微通道剥头皮：5m 处 EMA20 支撑与 50% 限价单触发"
            },
            {
              "file": "muShRE-fd_Q_02m.jpg",
              "caption": "经典开盘反转：大幅高开后反转K出现与 1R 目标设定"
            }
          ]
        },
        "latestVideoEvolutions2026": {
          "supportResistanceMechanisms": {
            "title": "实盘支撑阻力快速判定与被套交易者转化机制 (4zkG0jdEsy8 · 2026-09-07)",
            "core": "支阻是区域不是单线。当合理做空位置失败时（如K14大阳反转包吞），被套空头回踩其进场点急于平保离场（买入平仓），与多头买盘合流形成强支撑。",
            "ictComparison": "与 ICT 订单块缓解（Mitigation）及突破块（Breaker Block）底层原理完全共振。"
          },
          "rangeExecutionExclusion": {
            "title": "交易区间中 3 根 K 50% 挂单的核心禁用禁忌 (zDCnoIImHHM · 2026-10-21)",
            "core": "在强阳强阴交替的震荡交易区间内，严禁使用 3 根 K 50% 挂单；因为区间内缺乏单边动量，极易出现深幅回撤打穿 1 tick 窄止损后再拉起。该挂单法必须局限在清晰的趋势通道中。",
            "ictComparison": "对应 ICT 在 Seek & Destroy 震荡日中停止使用常规 FVG 挂单的防御铁律。"
          },
          "oneMinuteBanEvolution": {
            "title": "仓位放大后彻底退出 1m 图的心理学根源 (zDCnoIImHHM · 2026-10-21)",
            "core": "1 分钟图思考时间极度匮乏，极易引发认知超载、动作变形与连续止损后的报复性重仓。成熟阶段坚定只做 5 分钟图剥头皮，少做但做精。",
            "ictComparison": "为初学者提供重要反思：盲目在 1m 图摸顶抄底是爆仓主因，5m 结构更具统计稳定性。"
          },
          "activeBreakevenExit": {
            "title": "预期不符果断平保（BE）主动跑与单日双损熔断 (zDCnoIImHHM · 2026-10-21)",
            "core": "入场后行情未如预期爆发而是反向迟疑，给平保机会立即离场，不等打满止损；一单亏损+一单平保立即收工，恪守「涨上去就涨上去呗，涨上去又不赔钱」。",
            "ictComparison": "与 ICT 的时间止损和未触发撤单规则形成坚固的资金安全网。"
          }
        }
      }
    ],
    "extensions": {
      "role": "optional_observation",
      "policyVersion": "study-ny-v2",
      "macros": [
        {
          "time": "08:50–09:10",
          "session": "AM Pre-Market Macro",
          "focus": "观察开盘前是否接近候选流动性或失衡区域；不预判09:30方向。",
          "id": "ny-0850-0910",
          "evidenceStatus": "pending",
          "attribution": "用户新增观察笔记；主模型整理",
          "claimedSeries": "2024，具体年份归属与原课片段待核对",
          "sourceRefs": [],
          "timeZone": "America/New_York",
          "durationMinutes": 20,
          "entryIntersections": [
            [
              "08:50",
              "09:10"
            ]
          ],
          "outsideEntryWindows": []
        },
        {
          "time": "09:50–10:10",
          "session": "AM Main Macro",
          "focus": "观察开盘初段之后是否形成清晰路径、位移与结构确认；不将该时段等同于高胜率。",
          "id": "ny-0950-1010",
          "evidenceStatus": "pending",
          "attribution": "用户新增观察笔记；主模型整理",
          "claimedSeries": "2024，具体年份归属与原课片段待核对",
          "sourceRefs": [],
          "timeZone": "America/New_York",
          "durationMinutes": 20,
          "entryIntersections": [
            [
              "09:50",
              "10:10"
            ]
          ],
          "outsideEntryWindows": []
        },
        {
          "time": "10:50–11:10",
          "session": "Late Morning Macro",
          "focus": "观察早盘目标、动能延续或衰减；先记录实际价格证据。",
          "id": "ny-1050-1110",
          "evidenceStatus": "pending",
          "attribution": "用户新增观察笔记；主模型整理",
          "claimedSeries": "2024，具体年份归属与原课片段待核对",
          "sourceRefs": [],
          "timeZone": "America/New_York",
          "durationMinutes": 20,
          "entryIntersections": [
            [
              "10:50",
              "11:10"
            ]
          ],
          "outsideEntryWindows": []
        },
        {
          "time": "11:50–12:10",
          "session": "Pre-Lunch Macro",
          "focus": "观察午休边界附近的回补或清扫候选；12:00后按当前训练不新增交易。",
          "id": "ny-1150-1210",
          "evidenceStatus": "pending",
          "attribution": "用户新增观察笔记；主模型整理",
          "claimedSeries": "2024，具体年份归属与原课片段待核对",
          "sourceRefs": [],
          "timeZone": "America/New_York",
          "durationMinutes": 20,
          "entryIntersections": [
            [
              "11:50",
              "12:00"
            ]
          ],
          "outsideEntryWindows": [
            [
              "12:00",
              "12:10"
            ]
          ]
        },
        {
          "time": "13:15–13:45",
          "session": "PM Session Macro",
          "focus": "观察下午盘前后的流动性与结构；13:30前按当前训练不新增交易。",
          "id": "ny-1315-1345",
          "evidenceStatus": "pending",
          "attribution": "用户新增观察笔记；主模型整理",
          "claimedSeries": "2024，具体年份归属与原课片段待核对",
          "sourceRefs": [],
          "timeZone": "America/New_York",
          "durationMinutes": 30,
          "entryIntersections": [
            [
              "13:30",
              "13:45"
            ]
          ],
          "outsideEntryWindows": [
            [
              "13:15",
              "13:30"
            ]
          ]
        },
        {
          "time": "15:15–15:45",
          "session": "MOC / Closing Macro",
          "focus": "观察尾盘前的波动与持仓管理；该窗口不等同于NYSE主板收盘竞价不平衡公布时段。",
          "id": "ny-1515-1545",
          "evidenceStatus": "pending",
          "attribution": "用户新增观察笔记；主模型整理",
          "claimedSeries": "2024，具体年份归属与原课片段待核对",
          "sourceRefs": [],
          "timeZone": "America/New_York",
          "durationMinutes": 30,
          "entryIntersections": [
            [
              "15:15",
              "15:30"
            ]
          ],
          "outsideEntryWindows": [
            [
              "15:30",
              "15:45"
            ]
          ]
        }
      ],
      "htf": {
        "dailyBiasAnchor": "分析日内偏向时，先声明日线或周线所选区间、候选PD Array及流动性位置，并记录分析截止时刻。大周期背景不清时保持偏向待定，不能凭小周期噪声补造方向。",
        "dealingRangeExpansion": "若所选大周期区间与当前价格证据支持向上扩张，可将看涨路径列为候选，并分别记录逆向回撤与反转的确认、失效条件。大周期偏向可能失败；折价向溢价的路径本身不能证明顺势期望收益更高，也不能把所有看跌信号归为弱回调。",
        "source": "用户标记为2023–2024演进补充；本轮仅完成概念与系统边界整理，尚未核读对应原课。年份、原话与规则归属待具体视频和时间戳核验。",
        "evidenceStatus": "pending",
        "sourceRefs": []
      },
      "comparative": [
        {
          "id": "2c-trading",
          "name": "2C Trading (Al Brooks 裸K价格行为学)",
          "channel": "YouTube @2C_trading (2025.03–2026.10 · 300+ 实盘与复盘视频，含 2026-09 支阻快速寻找与 2026-10 实盘更新)",
          "role": "外部对比与补充视角（严禁混淆为 ICT 2022 官方教学）",
          "evidenceStatus": "external_verified",
          "localSource": "Documents/trading-notes/methodology/2C_trading_system/",
          "corePhilosophy": {
            "oneMethod": "只精通一种方法稳定盈利，熟练后加大仓位，而不是学更多方法",
            "probabilityMindset": "做的是概率：高概率+盈亏比差可做，低概率+盈亏比好需精确位置；交易频率上升则胜率下降",
            "disciplineOverTechnique": "走不顺就主动离场（不等止损）；连续不顺就休息；系统赚多少拿多少",
            "conservativeData": "23天实盘回测只用剥头皮（反转K+50%挂单）：36笔交易，82%胜率，2.2均R，4天零交易"
          },
          "keyComparisons": [
            {
              "dimension": "核心进场形态",
              "ict2022": {
                "title": "FVG (Fair Value Gap) 价值失衡缺口",
                "mechanism": "3根K线结构位移：第1根与第3根影线不重叠留出缺口，价格回抽触及缺口即为算法再平衡点",
                "timing": "严格位于 Killzone (08:30–11:00 / 13:30–15:30) 内且在折价/溢价区",
                "execution": "触价限价入场或收盘确认入场，止损置于摆动点外"
              },
              "twoCTrading": {
                "title": "3根K微通道剥头皮 与 50%波段限价挂单",
                "mechanism": "通道内3根连续趋势K（实体大、收盘在极值），在整组3根K的50%回调位挂限价单；未破50%极强，破了50%偏弱",
                "timing": "5分钟为主图，开盘第1-50根K内；必须由 EMA20 动态辅助提供支撑/阻力",
                "execution": "50%限价单进场，止损置于第1根K或波段起点外1 tick，止盈严格1:1 (1R)"
              },
              "synthesis": "两者本质均是在强位移波段寻找机构回踩点。ICT 用 FVG 空间失衡作为磁吸，2C 用 50% 几何平衡点结合 EMA20 作为动力反弹点。"
            },
            {
              "dimension": "反转与结构转变",
              "ict2022": {
                "title": "MSS (Market Structure Shift) 市场结构转变",
                "mechanism": "必须先完成对流动性池（BSL / SSL）的清扫刺穿，随后大实体穿透关键短期摆动高低点，完成交割方向逆转",
                "timing": "流动性清扫发生后",
                "execution": "伴随位移形成 FVG 确认，不猜顶底"
              },
              "twoCTrading": {
                "title": "反转K (Reversal Bar) 与形态验证",
                "mechanism": "连续趋势后第一根反向收盘K即为反转K；但在强趋势中第一次反转K容易失败；交易区间内80%突破为假突破",
                "timing": "在关键位置（交易区间边缘、高开/低开关键位）出现",
                "execution": "反转K收盘位直接做，或在反转K 50%挂单，止损放在反转K极值外1 tick"
              },
              "synthesis": "ICT 依赖外部流动性清扫与层级结构破坏；2C 关注单根反转K的动量衰竭与交易区间假突破（80%概率反转）。"
            },
            {
              "dimension": "过滤系统与指标哲学",
              "ict2022": {
                "title": "纯裸K + Time & Price 算法时间窗口",
                "mechanism": "杜绝一切传统均线与滞后指标；核心驱动是央行算法按时间交割订单流（Killzone、Macro 窗口、开盘基准价）",
                "timing": "时间优先于形态",
                "execution": "非交易窗口完全不开新仓"
              },
              "twoCTrading": {
                "title": "EMA20 动态磁铁与顺势顺风车",
                "mechanism": "EMA20 是强有力的动态支撑/阻力与趋势基准；日线在 EMA20 上方偏多、下方偏空；K线远离 EMA20 会被拉回，贴近 EMA20 顺势起爆",
                "timing": "开盘前50根5m K线",
                "execution": "3根K微通道必须有 EMA20 辅助才能大幅提升止盈率"
              },
              "synthesis": "ICT 以「时间基准（Macro/Killzone）」划分有效性，2C 以「均线位置（EMA20/远离拉回）」过滤虚假波动。"
            },
            {
              "dimension": "时间周期与执行颗粒度",
              "ict2022": {
                "title": "HTF (1D/1H/15m) 定偏向 → LTF (1m/2m) 精细执行",
                "mechanism": "大周期确定目标池与 Dealing Range，1m/2m 寻找微观 MSS + FVG，放大盈亏比",
                "timing": "高低周期嵌套",
                "execution": "秒级/1m 抓最小止损"
              },
              "twoCTrading": {
                "title": "坚决反对 1m 图 · 5m 主战场 · 15m 看形态",
                "mechanism": "铁律第4条明确禁止1分钟图（噪音大、过早进场导致被频繁打止损）；15m找收敛/通道/区间，5m执行进出",
                "timing": "5分钟K线收盘或50%挂单",
                "execution": "拒绝微观追单，等待5m形态成型"
              },
              "synthesis": "ICT 追求极致压缩止损（1m入场），2C 追求信号稳定性（5m主图防震荡陷阱）。初学者使用 2C 5m 图能有效避免在 1m 噪音中过度交易。"
            },
            {
              "dimension": "止盈与离场纪律",
              "ict2022": {
                "title": "非对称高盈亏比 (Asymmetric R:R) · 目标对侧流动性",
                "mechanism": "以大周期的 BSL/SSL 或未回补 FVG 为终极止盈，追求 1:3 甚至更高 R:R",
                "timing": "价格触及目标流动性池",
                "execution": "分批减仓（Partial Take Profit），止损移至保本（BE）"
              },
              "twoCTrading": {
                "title": "高概率拿 1R (1:1) · 走不顺主动离场",
                "mechanism": "高概率形态只拿 1R 利润，极强趋势才拿 2R；坚守概率思维，不贪大波段",
                "timing": "触及 1:1 或盘面走不顺",
                "execution": "铁律第1条：走不顺不等止损被动触发，差几点就主动跑；不改大止损，不加仓"
              },
              "synthesis": "ICT 靠高盈亏比拉大期望值，2C 靠高胜率（80%+）与坚决主动止损确保账户稳定增长。"
            }
          ],
          "tenBlacklistRules": [
            {
              "num": 1,
              "rule": "不追涨杀跌",
              "slogan": "高开不追多，低开不追空；宁可错过不可做错"
            },
            {
              "num": 2,
              "rule": "不在交易区间中间做单",
              "slogan": "只在区间边缘做高空低多，中间是绝对死区"
            },
            {
              "num": 3,
              "rule": "收敛三角形不做",
              "slogan": "收敛末端是观望区，绝不左侧开仓猜突破"
            },
            {
              "num": 4,
              "rule": "不看1分钟图",
              "slogan": "1分钟全是杂音与诱骗，过早进场必被打损"
            },
            {
              "num": 5,
              "rule": "不加仓",
              "slogan": "盈利想加仓=灾难，一次回调直接打穿本金"
            },
            {
              "num": 6,
              "rule": "不改止损",
              "slogan": "进场前算好止损，中途改一次2.5R直接亏空"
            },
            {
              "num": 7,
              "rule": "低波动日不做",
              "slogan": "日内预期波幅 <15点直接关电脑休息"
            },
            {
              "num": 8,
              "rule": "不跟第三推对抗",
              "slogan": "区间内第三推形成强趋势时立刻离场，绝不逆势抗单"
            },
            {
              "num": 9,
              "rule": "强趋势不做反转",
              "slogan": "强单边趋势中顺势做50%回调，不做第1次反转K"
            },
            {
              "num": 10,
              "rule": "不强迫开单",
              "slogan": "没有标准形态=最好的交易就是什么都不做"
            }
          ],
          "threeCandleMicroChannelSop": {
            "title": "3根K微通道剥头皮标准执行 SOP (3-Bar Micro Channel Scalp)",
            "steps": [
              "识别条件：在既定趋势通道内，发现连续3根（或4-5根）强趋势K线（实体饱满、无长影线、最后一根创出新极值）",
              "环境确认：K线顺应 EMA20 方向（EMA20 呈倾斜角度支撑/压制）；不在区间中间或通道最末端",
              "挂单进场：拉出这3根K线的总体波段，在 50% 回调位提前挂限价单（Limit Order）等待回踩触碰",
              "止损设定：严格放置在第 1 根 K 线起点外 1 tick（若破 50% 且破第 1 根则形态失效）",
              "止盈管理：严格 1:1（1R）止盈出场；若行情走势迟疑、回踩跌破 50% 且无买力弹起，主动提前离场"
            ],
            "keyframeShowcase": [
              {
                "file": "4zkG0jdEsy8_08m.jpg",
                "caption": "最新实盘支阻：08m 处 K14大阳包吞反转，被套空头平仓买盘转化为强支撑"
              },
              {
                "file": "4zkG0jdEsy8_11m.jpg",
                "caption": "最新交易区间：11m 处上中下 1/3 规则，上空下多，中间死区不操作"
              },
              {
                "file": "zDCnoIImHHM_18m.jpg",
                "caption": "最新实盘禁忌：18m 处交易区间内严禁 4 根阳线 50% 挂单（深回撤扫损）与平保跑路"
              },
              {
                "file": "yrtwu3BSnhQ_02m.jpg",
                "caption": "经典微通道剥头皮：2m 处 3根连续趋势K与50%回调位标记"
              },
              {
                "file": "yrtwu3BSnhQ_05m.jpg",
                "caption": "经典微通道剥头皮：5m 处 EMA20 支撑与 50% 限价单触发"
              },
              {
                "file": "muShRE-fd_Q_02m.jpg",
                "caption": "经典开盘反转：大幅高开后反转K出现与 1R 目标设定"
              }
            ]
          },
          "latestVideoEvolutions2026": {
            "supportResistanceMechanisms": {
              "title": "实盘支撑阻力快速判定与被套交易者转化机制 (4zkG0jdEsy8 · 2026-09-07)",
              "core": "支阻是区域不是单线。当合理做空位置失败时（如K14大阳反转包吞），被套空头回踩其进场点急于平保离场（买入平仓），与多头买盘合流形成强支撑。",
              "ictComparison": "与 ICT 订单块缓解（Mitigation）及突破块（Breaker Block）底层原理完全共振。"
            },
            "rangeExecutionExclusion": {
              "title": "交易区间中 3 根 K 50% 挂单的核心禁用禁忌 (zDCnoIImHHM · 2026-10-21)",
              "core": "在强阳强阴交替的震荡交易区间内，严禁使用 3 根 K 50% 挂单；因为区间内缺乏单边动量，极易出现深幅回撤打穿 1 tick 窄止损后再拉起。该挂单法必须局限在清晰的趋势通道中。",
              "ictComparison": "对应 ICT 在 Seek & Destroy 震荡日中停止使用常规 FVG 挂单的防御铁律。"
            },
            "oneMinuteBanEvolution": {
              "title": "仓位放大后彻底退出 1m 图的心理学根源 (zDCnoIImHHM · 2026-10-21)",
              "core": "1 分钟图思考时间极度匮乏，极易引发认知超载、动作变形与连续止损后的报复性重仓。成熟阶段坚定只做 5 分钟图剥头皮，少做但做精。",
              "ictComparison": "为初学者提供重要反思：盲目在 1m 图摸顶抄底是爆仓主因，5m 结构更具统计稳定性。"
            },
            "activeBreakevenExit": {
              "title": "预期不符果断平保（BE）主动跑与单日双损熔断 (zDCnoIImHHM · 2026-10-21)",
              "core": "入场后行情未如预期爆发而是反向迟疑，给平保机会立即离场，不等打满止损；一单亏损+一单平保立即收工，恪守「涨上去就涨上去呗，涨上去又不赔钱」。",
              "ictComparison": "与 ICT 的时间止损和未触发撤单规则形成坚固的资金安全网。"
            }
          }
        }
      ],
      "notice": "选学观察材料，来源待核对。Macro 不新增入场权限，不自动提高信号等级；基础训练与题库规则继续独立适用。"
    }
  },
  "lessons": {
    "ep01": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep02": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep03": {
      "status": "partial_transcript_checked",
      "core": "原稿区分日内结构变化与可能持续多日的结构破坏；不能由日内 MSS 直接推出多日反转。；这一具体案例允许突破短期高点而不要求收盘在其上；随后等待蜡烛收盘检查 FVG。不可把两种确认时点混为一谈。；原稿说早盘通常08:30–11:00，可延长至中午；午休避免找新机会，下午偏好13:30后。没有在此要求12:00强制平掉所有持仓。",
      "cases": [
        {
          "title": "[01:05] 日内 MSS 的作用范围",
          "gist": "原稿区分日内结构变化与可能持续多日的结构破坏；不能由日内 MSS 直接推出多日反转。",
          "scene": "已核对本地 No-Rant Ep.03 [01:05] 字幕；摘要不等于逐字引文。",
          "figures": [],
          "read": [
            {
              "who": "主模型核读摘要",
              "text": "原稿区分日内结构变化与可能持续多日的结构破坏；不能由日内 MSS 直接推出多日反转。"
            }
          ],
          "principles": [],
          "evidenceId": "ep03-t65",
          "sourceSHA256": "6bdefcca492172728dd9c29da3ed114218a1871159d7ffb0ba8ae67464859539"
        },
        {
          "title": "[04:05] 结构突破与 FVG 确认时点",
          "gist": "这一具体案例允许突破短期高点而不要求收盘在其上；随后等待蜡烛收盘检查 FVG。不可把两种确认时点混为一谈。",
          "scene": "已核对本地 No-Rant Ep.03 [04:05] 字幕；摘要不等于逐字引文。",
          "figures": [],
          "read": [
            {
              "who": "主模型核读摘要",
              "text": "这一具体案例允许突破短期高点而不要求收盘在其上；随后等待蜡烛收盘检查 FVG。不可把两种确认时点混为一谈。"
            }
          ],
          "principles": [],
          "evidenceId": "ep03-t245",
          "sourceSHA256": "6bdefcca492172728dd9c29da3ed114218a1871159d7ffb0ba8ae67464859539"
        },
        {
          "title": "[13:09] 纽约交易时段",
          "gist": "原稿说早盘通常08:30–11:00，可延长至中午；午休避免找新机会，下午偏好13:30后。没有在此要求12:00强制平掉所有持仓。",
          "scene": "已核对本地 No-Rant Ep.03 [13:09] 字幕；摘要不等于逐字引文。",
          "figures": [],
          "read": [
            {
              "who": "主模型核读摘要",
              "text": "原稿说早盘通常08:30–11:00，可延长至中午；午休避免找新机会，下午偏好13:30后。没有在此要求12:00强制平掉所有持仓。"
            }
          ],
          "principles": [],
          "evidenceId": "ep03-t789",
          "sourceSHA256": "6bdefcca492172728dd9c29da3ed114218a1871159d7ffb0ba8ae67464859539"
        }
      ],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep04": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep05": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep06": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep07": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep08": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep09": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep10": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep11": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep12": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep13": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep14": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep15": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep16": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep17": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep18": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep19": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep20": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep21": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep22": {
      "status": "partial_transcript_checked",
      "core": "开头回顾 S&P 日线、看跌订单块、风险背景和相对等低点，随后转入小时图。本段不支持旧稿的 FOMC 14:00/14:30 时间标签。",
      "cases": [
        {
          "title": "[00:00] 日线背景与候选流动性",
          "gist": "开头回顾 S&P 日线、看跌订单块、风险背景和相对等低点，随后转入小时图。本段不支持旧稿的 FOMC 14:00/14:30 时间标签。",
          "scene": "已核对本地 No-Rant Ep.22 [00:00] 字幕；摘要不等于逐字引文。",
          "figures": [],
          "read": [
            {
              "who": "主模型核读摘要",
              "text": "开头回顾 S&P 日线、看跌订单块、风险背景和相对等低点，随后转入小时图。本段不支持旧稿的 FOMC 14:00/14:30 时间标签。"
            }
          ],
          "principles": [],
          "evidenceId": "ep22-t0",
          "sourceSHA256": "df97319ea5462d3604b904194217b1b7b6a737db1644c45b9d47e06231ecf1c7"
        }
      ],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep23": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep24": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep25": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep26": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep27": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep28": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep29": {
      "status": "partial_transcript_checked",
      "core": "开头回顾2022-05-16的看涨偏向、Nasdaq相对等高点及S&P一分图；次段讨论美联储主席讲话前波动可能收缩。本段不支持旧稿的隔夜缺口标签。",
      "cases": [
        {
          "title": "[00:00] 窄幅看涨日案例的背景",
          "gist": "开头回顾2022-05-16的看涨偏向、Nasdaq相对等高点及S&P一分图；次段讨论美联储主席讲话前波动可能收缩。本段不支持旧稿的隔夜缺口标签。",
          "scene": "已核对本地 No-Rant Ep.29 [00:00] 字幕；摘要不等于逐字引文。",
          "figures": [],
          "read": [
            {
              "who": "主模型核读摘要",
              "text": "开头回顾2022-05-16的看涨偏向、Nasdaq相对等高点及S&P一分图；次段讨论美联储主席讲话前波动可能收缩。本段不支持旧稿的隔夜缺口标签。"
            }
          ],
          "principles": [],
          "evidenceId": "ep29-t0",
          "sourceSHA256": "088acc0a1d09c9ef103140c86b7697f634d13531e1c0e2be4de880ef3ca49a1c"
        }
      ],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep30": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep31": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep32": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep33": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep34": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep35": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep36": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    },
    "ep37": {
      "status": "pending",
      "core": "本课原稿与关键帧可供学习；旧中文归纳尚待逐项核验。",
      "cases": [],
      "gaps": "其余中文推演、图注和跨平台时间偏移待核验。",
      "drill": "指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。"
    }
  },
  "coverage": {
    "sourceLessons": 37,
    "partiallyChecked": 3
  },
  "principleCases": {}
};
