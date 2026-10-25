const STORAGE_KEY = 'ict2022.studyRoom.v1';
const NOTEBOOK_SCHEMA = 'ict-2022-study';
const NOTEBOOK_VERSION = 1;
const SAVE_DEBOUNCE_MS = 5000;

let saveTimer = null;

// Data bridge from window.ANG_LIBRARY and window.STUDY_COURSE
const RAW_LIB = window.ANG_LIBRARY || { lessons: [], glossary: [] };
const LESSON_LIBRARY = (RAW_LIB.lessons || []).map((item) => {
  const numId = String(item.ep || item.id || '').replace(/^ep/i, '').padStart(2, '0');
  return {
    ...item,
    rawId: item.id,
    id: numId,
    moduleTitle: item.module || (item.topics && item.topics[0]) || 'ICT 2022 Mentorship',
    summary: item.preview || '',
    rawText: item.searchText || '',
    videoPath: item.localVideoUrl || (Number(numId) <= 5 ? `videos/ep${numId}.mp4` : ''),
    youtubeId: item.videoId || ''
  };
});

const CURRICULUM_MODULES = [
  { id: 'm1', chapter: 'Module 01 · Ep 01–05', title: '核心模型与日内基石 (1080p图解)', episodes: ['01', '02', '03', '04', '05'] },
  { id: 'm2', chapter: 'Module 02 · Ep 06–12', title: '日线偏向与 AMD 权力三段', episodes: ['06', '07', '08', '09', '10', '11', '12'] },
  { id: 'm3', chapter: 'Module 03 · Ep 13–19', title: '机构订单流与多重共振', episodes: ['13', '14', '15', '16', '17', '18', '19'] },
  { id: 'm4', chapter: 'Module 04 · Ep 20–26', title: '伦敦/纽约波动与实盘带练', episodes: ['20', '21', '22', '23', '24', '25', '26'] },
  { id: 'm5', chapter: 'Module 05 · Ep 27–33', title: '逆势应对、SMT 与高阶FVG', episodes: ['27', '28', '29', '30', '31', '32', '33'] },
  { id: 'm6', chapter: 'Module 06 · Ep 34–37', title: '全套体系收官与职业化心智', episodes: ['34', '35', '36', '37'] }
];

const DIAGRAM_BY_BATCH = ['sweep_bsl_short', 'sweep_ssl_long', 'pm_session_reversal'];
const PRACTICE_BATCHES = ((window.STUDY_COURSE && window.STUDY_COURSE.batches) || []).map((b, idx) => ({
  id: b.id,
  title: b.title,
  focus: b.desc || '流动性猎杀 + MSS + 折价/溢价区 FVG',
  caseTitle: b.title,
  caseSummary: b.desc || '',
  diagram: DIAGRAM_BY_BATCH[idx % DIAGRAM_BY_BATCH.length],
  questions: (b.questions || []).map((q) => ({
    id: q.id,
    moment: q.title,
    prompt: q.context,
    hint: q.prompt || '先看高周期流动性池是否已被扫，再看是否有位移与 FVG。',
    expectedAction: q.answer,
    teacherWhy: q.explanation,
    nudge: q.prompt || '对照原片检查你的入场位 (E)、止损位 (S) 与流动性目标 (T)。'
  }))
}));

const ACTION_OPTIONS = [
  { value: 'Wait', label: 'Wait · 按兵不动（等扫损或等结构破坏）' },
  { value: 'Armed', label: 'Armed · 挂单待命（MSS+FVG 已出，等回抽进框）' },
  { value: 'Execute', label: 'Execute · 立即执行（回抽进折价/溢价区 FVG 触发）' },
  { value: 'Cancel', label: 'Cancel · 撤销计划（未回抽直接打到目标或过午休）' },
  { value: 'Exit', label: 'Exit · 止盈/离场（抵达对侧流动性池或 16:00 MOC）' }
];

const ORDERFLOW_STEPS = [
  {
    id: 'step-pre830',
    step: '01 · 08:30 NY 前',
    title: '盘前定位：先画高低点流动性池',
    question: '今天算法最想猎杀哪一边的止损单 (BSL / SSL)？',
    bullets: [
      '切换至紐約时间 (UTC-4/UTC-5)，在日线/1H/15m 标出前一日高点 (PDH)、前一日低点 (PDL)、伦敦盘高低点及相对平头高低点 (Equal Highs/Lows)。',
      '季度交割月（3/6/9/12月第二个周五前）先在 Barchart 检查 Open Interest，确认已切换到主力合约。',
      '在 08:30 消息公布前只画线、不猜方向，等待市场自己亮出底牌 (Tip its hand)。'
    ],
    trap: '08:30 前凭感觉提前重仓押注方向，结果被 08:30 脉冲瞬间打爆止损。',
    output: '图表上清晰标出上方 BSL 与下方 SSL 两条水平线，以及 08:30 垂直时间线。'
  },
  {
    id: 'step-am-session',
    step: '02 · 08:30–11:00 NY',
    title: '早盘猎杀：Stop Hunt → MSS → FVG',
    question: '刺穿流动性池后，是否出现了放量位移与折价/溢价区 FVG？',
    bullets: [
      '08:30 宏观数据或 09:30 美股现货开盘后，观察价格是否先刺穿一侧流动性池（或走出 Three Drives 三推诱多/诱空）。',
      '切到 5m/2m/1m 图，等待反方向大力位移 K 线突破短期摆动点，确认市场结构转换 (MSS / BMS)。',
      '从波段起点到终点拉斐波那契 0.5 均衡线：做多只看 <0.5 折价区看涨 FVG（常伴随看涨 OB）；做空只看 >0.5 溢价区看跌 FVG。'
    ],
    trap: '看到大阴线/大阳线破位就因为害怕踏空 (FOMO) 直接市价追单，不等价格回抽 0.5 均衡位后的 FVG。',
    output: '在 FVG 边缘挂好 Limit 限价单，止损放在扫损极值点外，目标对准对侧流动性池。'
  },
  {
    id: 'step-ny-lunch',
    step: '03 · 12:00–13:00 NY',
    title: '午休禁区：New York Lunch 强制护盘',
    question: '现在是不是处于算法休眠与扫损积累期？',
    bullets: [
      '12:00 到 13:00 纽约午休时段，机构算法进入震荡或诱导积累模式，绝不在此时段内开新仓。',
      '若早盘单子尚未平仓，必须在午休前大幅减仓或推保本止损。',
      '在图上标出午休时段形成的高低点 (Lunch High / Lunch Low)，它将成为 13:30 下午盘的猎杀靶子。'
    ],
    trap: '早盘没做到行情心有不甘，在 12:15 午休窄幅震荡里频繁刷单，被来回打脸。',
    output: '午休时段 0 开仓，并在 15m/5m 图上框出 12:00–13:00 的高低点流动性池。'
  },
  {
    id: 'step-pm-session',
    step: '04 · 13:30–16:00 NY',
    title: '下午盘与尾盘：13:30 二次猎杀与 MOC',
    question: '13:30 后扫了午休哪一侧？尾盘 Spooling 目标在哪？',
    bullets: [
      '13:30 下午盘窗口开启，重点观察价格是否先刺穿纽约午休高低点或早盘次级高低点完成二次 Stop Hunt。',
      '同样等待 5m/2m/1m 出现 MSS + Displacement + FVG 后挂单入场。',
      '15:00–16:00 进入 Market on Close (MOC) 尾盘时段，价格常呈现单边连续加速 (Spooling) 直奔日内对侧高低点，必须在 16:00 前平掉所有日内仓位。'
    ],
    trap: '在 15:30 尾盘单边加速 (Spooling) 时逆势摸顶抄底，或者把日内单留到隔夜。',
    output: '16:00 收盘前全部清仓落袋，并将当日 4 项核心数据填入「05 复盘手帐」。'
  }
];

const PRE_TRADE_CHECKLIST = [
  { id: 'c1', label: '① 纽约时间窗口确认 (Killzone Time)', detail: '当前处于 08:30–11:00 早盘或 13:30–15:30 下午盘，绝非 12:00–13:00 午休禁区。' },
  { id: 'c2', label: '② 流动性猎杀已发生 (Stop Hunt / Three Drives)', detail: '价格已经明确刺穿了 15m/1H 级别的旧高 (BSL) 或旧低 (SSL)，拿掉了散户止损。' },
  { id: 'c3', label: '③ 市场结构转换 + 强劲位移 (MSS + Displacement)', detail: '5m/2m/1m 图上出现了实体饱满的大阳/大阴线，明确击穿了最近的短期摆动高低点。' },
  { id: 'c4', label: '④ 0.5 均衡位过滤 (Discount / Premium)', detail: '拉斐波那契确认：做多挂单位于 <0.5 折价区，做空挂单位于 >0.5 溢价区。' },
  { id: 'c5', label: '⑤ 三根 K 线失衡缺口 (FVG + Order Block)', detail: '位移段中存在清晰的 Fair Value Gap（最好与同向 Order Block 重合），坚持挂限价单等回抽。' },
  { id: 'c6', label: '⑥ 明确的对侧流动性目标 (Draw on Liquidity)', detail: '进场前已标好止损位（扫损极值外）与第一/第二止盈位（内部 FVG 与外部高低点），盈亏比 ≥ 3:1。' }
];

window.ICT_GLOSSARY = (RAW_LIB.glossary || []).map((g) => ({
  term: g.term,
  full: g.en || g.term,
  zh: g.zh || '',
  desc: g.def || ''
}));

const COMMON_MISTAKES = [
  '看到 15m 平头高点/低点被突破，第一反应当作散户顺势突破去追涨杀跌，结果买在 Stop Hunt 最高点。',
  '刚刚扫完高点但还没有向下跌破短期低点（无 MSS、无位移），就急着在左肩摸顶做空。',
  '出了 MSS 和 FVG 后害怕踏空 (FOMO)，不等价格回抽到 0.5 均衡位以上的溢价区就直接市价追单。',
  '在 12:00–13:00 纽约午休垃圾时间里强行找形态开仓，把早盘利润全部回吐。',
  '复盘时总是幻想“如果从最高点拿到最低点能赚多少”，而不是像 Ep.04 要求那样只统计 FVG 到目标位的确定性点数。'
];

// Curated Multi-Timeframe Walkthrough Cases from Ep.01 - Ep.05
const MTF_WALKTHROUGHS = [
  {
    id: 'ep02-topdown',
    title: '案例 A · Ep.02 周线→2m 完整空头剥洋葱',
    ep: '02',
    steps: [
      {
        tf: '1W 周线',
        time: '04:33',
        seconds: 273,
        src: 'lesson-assets/ep02_weekly_old_low_sweep.png',
        goal: '看大资金已经拿掉了哪一侧流动性，下一站去哪',
        observation: '周线刚刚跌破前低 (Old Weekly Low) 完成卖方流动性清扫，随后反弹回抽周线级别失衡区。',
        action: '确立大周期偏见，准备在日线与小时线寻找拐点。'
      },
      {
        tf: '1D 日线',
        time: '05:10',
        seconds: 310,
        src: 'lesson-assets/ep02_daily_swing_high_rejection.png',
        goal: '判断当日 Daily Bias（日内方向偏见）',
        observation: '日线在阶段性摆动高点 (Swing High) 遇阻，未能有效站稳，形成向下交付预期。',
        action: '当日定调为偏空 (Bearish Bias)，等待纽约早盘先向上诱多扫损。'
      },
      {
        tf: '1H 小时线',
        time: '05:45',
        seconds: 345,
        src: 'lesson-assets/ep02_hourly_induce_shorts_run_bsl.png',
        goal: '识别散户陷阱 (Induce Shorts) 与上方止损池 (BSL)',
        observation: '小时图先制造小级别假跌破诱导散户追空，随后急速拉升清扫上方平头高点买方流动性 (Run Above BSL)。',
        action: '切入 15m/2m 图表，盯着上方高点被刺穿后的反应。'
      },
      {
        tf: '15m 猎杀池',
        time: '06:30',
        seconds: 390,
        src: 'lesson-assets/ep02_15m_equal_highs_stop_hunt.png',
        goal: '确认 08:30 窗口 Stop Hunt（止损猎杀）发生',
        observation: '价格精准刺穿 15 分钟相对平头高点 (Equal Highs) 拿掉买方止损单后迅速收回。',
        action: '进入 2m 执行周期，等待跌破短期低点产生 BMS/MSS。'
      },
      {
        tf: '2m 破坏+FVG',
        time: '07:50',
        seconds: 470,
        src: 'lesson-assets/ep02_2m_bms_and_fvg_entry.png',
        goal: '确认 BMS/MSS + Displacement，定位 FVG 挂单点',
        observation: '大阴线放量砸穿短期支撑造成市场结构破坏 (BMS)，三根 K 线中间留下清晰的看跌 FVG。',
        action: '不要追空！拉斐波那契确认 FVG 位于 >0.5 溢价区。'
      },
      {
        tf: '2m 完整复盘',
        time: '10:33',
        seconds: 633,
        src: 'lesson-assets/ep02_2m_full_setup_annotated.png',
        goal: '溢价区 FVG 限价接空 → 下方 SSL 止盈',
        observation: '价格回抽填补溢价区 FVG 后瀑布式下跌，精准打穿下方卖方流动性池 (SSL)。',
        action: '在下方旧低点下方挂 Buy Limit 止盈平仓。'
      }
    ]
  },
  {
    id: 'ep03-bothways',
    title: '案例 B · Ep.03 15m→1m 多空双向与订单块',
    ep: '03',
    steps: [
      {
        tf: '15m 流动性全景',
        time: '09:30',
        seconds: 570,
        src: 'lesson-assets/ep03_15m_ssl_and_bsl_pools.png',
        goal: '在 15m 图上框出上下两侧的流动性目标',
        observation: '下方存在明显的前低卖方流动性池 (SSL)，上方存在平头高点买方流动性池 (BSL)。',
        action: '等待纽约开盘先扫哪一侧。'
      },
      {
        tf: '2m 看涨 MSS+OB',
        time: '12:20',
        seconds: 740,
        src: 'lesson-assets/ep03_2m_bullish_mss_fvg_ob.png',
        goal: '扫 SSL 后识别看涨 MSS、FVG 与看涨订单块 (OB)',
        observation: '价格刺穿下方 SSL 后，连续阳线强势突破前高产生看涨 MSS，回调进折价区 FVG 与看涨 OB 重叠位。',
        action: '在折价区 FVG 下沿挂多单，目标直指上方 15m BSL。'
      },
      {
        tf: '2m 看跌 MSS+目标',
        time: '17:50',
        seconds: 1070,
        src: 'lesson-assets/ep03_2m_bearish_mss_fvg_targets.png',
        goal: '上方 BSL 达成后，反转做空抓内部/外部流动性',
        observation: '上方 BSL 清扫完毕后，2m 出现看跌 MSS 与看跌 FVG，形成反手做空模型。',
        action: '溢价区 FVG 做空，第一目标内部低点，第二目标外部低点。'
      },
      {
        tf: '1m 订单块交付',
        time: '21:10',
        seconds: 1270,
        src: 'lesson-assets/ep03_1m_orderblock_state_of_delivery.png',
        goal: '理解 Change in the State of Delivery（交付状态转换）',
        observation: '扫高点前的最后一根阳线构成的看跌 Order Block 被大阴线吞没瞬间，交付状态正式由多转空。',
        action: '将此 OB 与 FVG 重合处视为最高胜率机构入场区。'
      },
      {
        tf: '1m 全注释总览',
        time: '24:00',
        seconds: 1440,
        src: 'lesson-assets/ep03_1m_full_lipstick_chart.png',
        goal: '1m 显微镜下的完整 ICT 2022 标注模板',
        observation: '完整呈现 Stop Hunt → MSS → Discount/Premium → FVG + OB → Liquidity Target 闭环。',
        action: '对照此图检查你自己的每日复盘标注是否完整。'
      }
    ]
  },
  {
    id: 'ep04-execution',
    title: '案例 C · Ep.04 ES/NQ 均衡位与等待纪律',
    ep: '04',
    steps: [
      {
        tf: 'ES 2m 均衡位全景',
        time: '04:00',
        seconds: 240,
        src: 'lesson-assets/ep04_es_2m_equilibrium_overview.png',
        goal: '先用 0.5 Equilibrium 把区间一分为二',
        observation: '早盘区间高点到低点拉斐波那契，0.5 均衡位以下才是合格的多头折价区 (Discount)。',
        action: '不到 0.5 以下绝不因为害怕踏空而提前买进。'
      },
      {
        tf: 'ES 2m 四维复盘卡',
        time: '06:20',
        seconds: 380,
        src: 'lesson-assets/ep04_es_2m_830_zoomed_journal.png',
        goal: '掌握 Ep.04 要求每天必记的 4 个核心数字',
        observation: '图上清晰标注：① 入场 FVG 价位、② 止损位、③ 目标点数差、④ 折算合约美金价值。',
        action: '切到本应用「05 复盘手帐」按同样格式记录你的交易。'
      },
      {
        tf: 'NQ 5m 三推扫高',
        time: '10:30',
        seconds: 630,
        src: 'lesson-assets/ep04_nq_5m_three_drives_high.png',
        goal: '识别 Three Drives Pattern（三推诱多）',
        observation: 'NQ 连续三次推高，每一次微创新高都在诱导散户追多并消耗买盘动能。',
        action: '三推刺穿旧高后严阵以待，等待向下位移大阴线。'
      },
      {
        tf: 'NQ 5m 拒绝追单等FVG',
        time: '13:30',
        seconds: 810,
        src: 'lesson-assets/ep04_nq_5m_wait_for_fvg_entry.png',
        goal: '克制 FOMO，坚持等价格回抽 14957 看跌 FVG',
        observation: '位移大阴线砸出 MSS 后，价格先在低位徘徊再回抽 14957.00 看跌 FVG，随后直奔 14780.75（176.25 点）。',
        action: '挂单 14957.00，止盈 14780.75，单张 NQ 获利 $3,525。'
      }
    ]
  },
  {
    id: 'ep05-intraday',
    title: '案例 D · Ep.05 移仓换月 + 早午盘双窗口',
    ep: '05',
    steps: [
      {
        tf: 'Barchart 移仓检查',
        time: '02:00',
        seconds: 120,
        src: 'lesson-assets/ep05_barchart_open_interest_rollover.png',
        goal: '季度交割月用 Open Interest 确认主力合约',
        observation: '对比 3 月 (H) 与 6 月 (M) 合约的持仓量 (Open Interest)，当新季合约持仓量反超老合约即完成主力切换。',
        action: '切勿在流动性枯竭的旧合约上画 FVG。'
      },
      {
        tf: '15m 日内时间框架',
        time: '07:00',
        seconds: 420,
        src: 'lesson-assets/ep05_15m_daily_range_830_lunch.png',
        goal: '在 15m 图上画出 08:30 与 12:00–13:00 垂直时间线',
        observation: '纽约早盘与午休时段边界分明，午休期间价格往往陷入无序震荡或酝酿午后扫损池。',
        action: '12:00–13:00 强制空仓休息，等待 13:30 下午盘窗口。'
      },
      {
        tf: '5m 早盘三推+FVG',
        time: '10:30',
        seconds: 630,
        src: 'lesson-assets/ep05_5m_three_drives_displacement_fvg.png',
        goal: '早盘 Three Drives 扫高 + 位移跌破 + FVG',
        observation: '三次推高清扫买方止损后，放量跌破结构低点，回抽看跌 FVG 给出教科书早盘空单。',
        action: '早盘空单在午休前落袋为安。'
      },
      {
        tf: '5m 13:30 午盘扫损',
        time: '16:30',
        seconds: 990,
        src: 'lesson-assets/ep05_5m_pm_session_130_stop_hunt.png',
        goal: '捕捉 13:30 下午盘对午休高点的二次猎杀',
        observation: '13:30 后算法先把价格拉过 New York Lunch High 清扫空头止损，随后立刻向下破坏结构。',
        action: '午后独立机会：扫午休高点 + MSS 后在看跌 FVG 进场。'
      },
      {
        tf: '5m 尾盘 Spooling',
        time: '20:50',
        seconds: 1250,
        src: 'lesson-assets/ep05_5m_pm_spooling_moc.png',
        goal: '理解 15:00 后 MOC (Market on Close) 单边加速',
        observation: '尾盘算法不再给深幅回调，连续大阴线向日内低点下方卖方流动性池加速倾泻 (Spooling)。',
        action: '顺应尾盘单边流向在下方 SSL 目标位止盈，绝不逆势抄底。'
      }
    ]
  }
];

function createDefaultState() {
  return {
    view: 'classroom',
    moduleId: CURRICULUM_MODULES[0].id,
    epFilter: 'all',
    lessonId: '01',
    lessonQuery: '',
    flowStepId: ORDERFLOW_STEPS[0].id,
    batchId: PRACTICE_BATCHES[0].id,
    completedBatches: [],
    completedLessons: [],
    lessonNotes: {},
    answers: {},
    attemptHistory: [],
    summaryNote: '',
    mistakes: {},
    checklist: {},
    journalEntries: [
      {
        id: 'demo-ep04-nq',
        date: '2022-02-04',
        symbol: 'NQ',
        session: '08:30-11:00 NY AM',
        contracts: 1,
        direction: 'Sweep BSL → Short',
        entry: 14957.00,
        stop: 14989.50,
        target: 14780.75,
        points: 176.25,
        rr: '5.42',
        dollars: 3525.00,
        comment: '【Ep.04 原片示范】5m 图三推 (Three Drives) 扫掉买方流动性后大阴线位移跌破结构 (MSS)，耐心等待价格回抽 >0.5 溢价区的 14957.00 看跌 FVG 挂单进场，下方 SSL 14780.75 止盈。'
      }
    ],
    mtfCaseId: MTF_WALKTHROUGHS[0].id,
    mtfStepIndex: 0,
    videoEpId: '01',
    blindQuiz: false,
    updatedAt: null
  };
}

function normalizeLoadedState(parsed) {
  const base = createDefaultState();
  if (!parsed || typeof parsed !== 'object') return base;
  return {
    ...base,
    ...parsed,
    completedBatches: Array.isArray(parsed.completedBatches) ? parsed.completedBatches : [],
    completedLessons: Array.isArray(parsed.completedLessons) ? parsed.completedLessons : [],
    lessonNotes: parsed.lessonNotes && typeof parsed.lessonNotes === 'object' ? parsed.lessonNotes : {},
    answers: parsed.answers && typeof parsed.answers === 'object' ? parsed.answers : {},
    attemptHistory: Array.isArray(parsed.attemptHistory) ? parsed.attemptHistory : [],
    mistakes: parsed.mistakes && typeof parsed.mistakes === 'object' ? parsed.mistakes : {},
    checklist: parsed.checklist && typeof parsed.checklist === 'object' ? parsed.checklist : {},
    journalEntries: Array.isArray(parsed.journalEntries) && parsed.journalEntries.length ? parsed.journalEntries : base.journalEntries
  };
}

function hasProgressData(candidate) {
  if (!candidate || typeof candidate !== 'object') return false;
  return Boolean(
    (candidate.summaryNote && candidate.summaryNote.trim()) ||
    Object.keys(candidate.lessonNotes || {}).length ||
    Object.keys(candidate.answers || {}).length ||
    (candidate.attemptHistory || []).length ||
    (candidate.completedLessons || []).length ||
    (candidate.completedBatches || []).length ||
    Object.values(candidate.mistakes || {}).some(Boolean)
  );
}

function loadState() {
  let localCandidate = null;
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) localCandidate = normalizeLoadedState(JSON.parse(raw));
  } catch (err) {
    console.warn('localStorage load failed', err);
  }
  const nativeCandidate = window.nativeNotebook ? normalizeLoadedState(window.nativeNotebook) : null;
  if (nativeCandidate && hasProgressData(nativeCandidate)) return nativeCandidate;
  if (localCandidate && hasProgressData(localCandidate)) return localCandidate;
  return nativeCandidate || localCandidate || createDefaultState();
}

const state = loadState();

function buildNotebookPayload() {
  return {
    schema: NOTEBOOK_SCHEMA,
    version: NOTEBOOK_VERSION,
    updatedAt: state.updatedAt,
    view: state.view,
    moduleId: state.moduleId,
    lessonId: state.lessonId,
    flowStepId: state.flowStepId,
    batchId: state.batchId,
    completedBatches: state.completedBatches,
    completedLessons: state.completedLessons,
    lessonNotes: state.lessonNotes,
    answers: state.answers,
    attemptHistory: state.attemptHistory,
    summaryNote: state.summaryNote,
    mistakes: state.mistakes,
    checklist: state.checklist,
    journalEntries: state.journalEntries
  };
}

function setSaveStatus(text) {
  const el = document.getElementById('saveStatus');
  if (el) el.textContent = text;
}

function flushNativeNotebook() {
  if (saveTimer) {
    clearTimeout(saveTimer);
    saveTimer = null;
  }
  const payload = JSON.stringify(buildNotebookPayload(), null, 2);
  const handler = window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.saveNotebook;
  if (handler) {
    handler.postMessage(payload);
    setSaveStatus('已写入本地 notebook.json');
  } else {
    setSaveStatus('已保存在浏览器本地存储');
  }
}

function saveState(options = {}) {
  state.updatedAt = new Date().toISOString();
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(buildNotebookPayload()));
  } catch (err) {
    console.warn('localStorage save failed', err);
  }
  if (options.immediate) {
    flushNativeNotebook();
    return;
  }
  setSaveStatus('修改待落盘（5 秒内自动写入）');
  if (saveTimer) clearTimeout(saveTimer);
  saveTimer = setTimeout(flushNativeNotebook, SAVE_DEBOUNCE_MS);
}

window.onNativeNotebookSaved = function onNativeNotebookSaved(info) {
  if (info && info.ok) {
    const time = new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    setSaveStatus(`已写入 notebook.json · ${time}`);
  } else {
    setSaveStatus('本地文件保存失败，已保留在内存中');
  }
};

function escapeHtml(value) {
  return String(value || '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

function setView(view) {
  state.view = view;
  saveState();
  document.querySelectorAll('.nav-btn').forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.view === view);
  });
  document.querySelectorAll('.view').forEach((section) => {
    section.classList.toggle('active', section.id === `view-${view}`);
  });
  if (view === 'notebook') renderNotebook();
  if (view === 'mtf') renderMtfView();
  if (view === 'journal') renderJournalView();
}

function renderProgress() {
  const completedCount = state.completedLessons.length;
  const totalCount = LESSON_LIBRARY.length;
  const pct = Math.min(100, Math.round((completedCount / totalCount) * 100));
  document.getElementById('progressFill').style.width = `${pct}%`;
  document.getElementById('progressMeta').textContent = `已学完 ${completedCount} / ${totalCount} 讲 · 练习完成 ${state.completedBatches.length} / ${PRACTICE_BATCHES.length} 组`;
}

function renderClassroom() {
  const strip = document.getElementById('curriculumStrip');
  strip.innerHTML = CURRICULUM_MODULES.map((mod) => `
    <button class="module-pill ${mod.id === state.moduleId ? 'active' : ''}" data-module="${mod.id}">
      <small>${escapeHtml(mod.chapter)}</small>
      <strong>${escapeHtml(mod.title)}</strong>
    </button>
  `).join('');

  strip.querySelectorAll('[data-module]').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.moduleId = btn.dataset.module;
      const mod = CURRICULUM_MODULES.find((item) => item.id === state.moduleId);
      if (mod && mod.episodes && mod.episodes.length) {
        state.lessonId = mod.episodes[0];
      }
      saveState();
      renderClassroom();
    });
  });

  document.querySelectorAll('[data-ep-filter]').forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.epFilter === state.epFilter);
    btn.onclick = () => {
      state.epFilter = btn.dataset.epFilter;
      if (state.epFilter === 'core' && Number(state.lessonId) > 5) {
        state.lessonId = '01';
      }
      saveState();
      renderLibrary();
    };
  });

  renderLibrary();
}

function getFilteredLessons() {
  const query = (state.lessonQuery || '').trim().toLowerCase();
  return LESSON_LIBRARY.filter((lesson) => {
    if (state.epFilter === 'core' && !lesson.hasLocalVideo) return false;
    if (!query) return true;
    return (
      lesson.id.toLowerCase().includes(query) ||
      lesson.title.toLowerCase().includes(query) ||
      lesson.summary.toLowerCase().includes(query) ||
      lesson.rawText.toLowerCase().includes(query)
    );
  });
}

function renderLibrary() {
  const listEl = document.getElementById('lessonList');
  const detailEl = document.getElementById('lessonDetail');
  const filtered = getFilteredLessons();
  const activeLesson = filtered.find((item) => item.id === state.lessonId) || filtered[0] || LESSON_LIBRARY[0];

  if (activeLesson && activeLesson.id !== state.lessonId) {
    state.lessonId = activeLesson.id;
  }

  listEl.innerHTML = filtered.map((lesson) => {
    const done = state.completedLessons.includes(lesson.id);
    const hasNote = Boolean((state.lessonNotes[lesson.id] || '').trim());
    return `
      <button class="lesson-item ${lesson.id === state.lessonId ? 'active' : ''}" data-lesson="${lesson.id}">
        <small>
          <span>Ep.${escapeHtml(lesson.id)} · ${escapeHtml(lesson.duration || '')} ${done ? '· 已读' : ''}${hasNote ? ' · 有笔记' : ''}</span>
          ${lesson.hasLocalVideo ? '<span class="badge-core">1080p图解</span>' : ''}
        </small>
        <strong>${escapeHtml(lesson.title)}</strong>
      </button>
    `;
  }).join('');

  listEl.querySelectorAll('[data-lesson]').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.lessonId = btn.dataset.lesson;
      saveState();
      renderLibrary();
    });
  });

  if (!activeLesson) {
    detailEl.innerHTML = '<p class="muted">没有匹配的课程，请换一个关键词。</p>';
    return;
  }

  const isDone = state.completedLessons.includes(activeLesson.id);
  const currentNote = state.lessonNotes[activeLesson.id] || '';
  const distillHtml = window.renderLessonDistill ? window.renderLessonDistill(activeLesson) : '';
  const epUrls = buildVideoUrls(activeLesson.id, 0);

  detailEl.innerHTML = `
    <div class="lesson-meta">
      <div>
        <p class="eyebrow">Episode #${escapeHtml(activeLesson.id)} · ${escapeHtml(activeLesson.moduleTitle)} · 时长 ${escapeHtml(activeLesson.duration)}</p>
        <h3>${escapeHtml(activeLesson.title)}</h3>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center;">
        <a class="website-link small-link" href="${escapeHtml(epUrls.ytUrl)}" target="_blank" rel="noopener">🎬 YouTube 原片 ↗</a>
        <a class="website-link small-link" href="${escapeHtml(epUrls.biliUrl)}" target="_blank" rel="noopener">📺 B站中配 P${epUrls.epNum} ↗</a>
        <button class="${isDone ? 'ghost' : 'primary'}" id="markLessonDone" type="button">
          ${isDone ? '已标记学完（点此取消）' : '标记本课已学完'}
        </button>
      </div>
    </div>
    ${distillHtml}
    <div class="lesson-note-box">
      <div class="lesson-note-head">
        <strong>本课随手记（自动保存，可在“06 我的笔记”集中回看）</strong>
        <small>记录你对本集扫损位、MSS 或 FVG 入场纪律的疑问与体会</small>
      </div>
      <textarea id="lessonNoteInput" class="lesson-note-input" placeholder="写下你读完 Ep.${escapeHtml(activeLesson.id)} 的理解、疑问或实盘准备怎么用...">${escapeHtml(currentNote)}</textarea>
    </div>
    <div class="lesson-article">${activeLesson.html}</div>
  `;

  document.getElementById('markLessonDone').addEventListener('click', () => {
    const idx = state.completedLessons.indexOf(activeLesson.id);
    if (idx >= 0) {
      state.completedLessons.splice(idx, 1);
    } else {
      state.completedLessons.push(activeLesson.id);
    }
    saveState({ immediate: true });
    renderProgress();
    renderLibrary();
  });

  const lessonNoteInput = document.getElementById('lessonNoteInput');
  lessonNoteInput.addEventListener('input', () => {
    const val = lessonNoteInput.value;
    if (val.trim()) {
      state.lessonNotes[activeLesson.id] = val;
    } else {
      delete state.lessonNotes[activeLesson.id];
    }
    saveState();
  });

  detailEl.querySelectorAll('[data-open-map]').forEach((btn) => {
    btn.addEventListener('click', () => {
      if (window.openSystemMap) {
        window.openSystemMap(btn.dataset.openMap, (lessonId) => {
          state.lessonId = lessonId;
          saveState();
          renderLibrary();
        });
      }
    });
  });

  detailEl.querySelectorAll('.lesson-figure img, .dfigure img, .lesson-article img').forEach((img) => {
    img.addEventListener('click', () => {
      const fig = img.closest('figure');
      const cap = fig && fig.querySelector('figcaption') ? fig.querySelector('figcaption').textContent : img.alt;
      const sec = fig && fig.dataset.seconds ? Number(fig.dataset.seconds) : null;
      openImageViewer(img.src, img.alt || activeLesson.title, cap, activeLesson.id, sec);
    });
  });
}

function buildVideoUrls(epId, seconds = 0) {
  const padded = String(epId).replace(/^ep/i, '').padStart(2, '0');
  const epNum = parseInt(padded, 10) || 1;
  const lesson = LESSON_LIBRARY.find((l) => l.id === padded) || LESSON_LIBRARY[0] || {};
  const vid = lesson.youtubeId || lesson.videoId || '';
  const sec = Math.max(0, Math.floor(Number(seconds || 0)));
  const ytUrl = sec > 0
    ? `https://www.youtube.com/watch?v=${vid}&list=PLOqlWG05MfW6T7mUjI2CK5BdQ6FrV3zEm&t=${sec}s`
    : (lesson.youtubeUrl || `https://www.youtube.com/watch?v=${vid}&list=PLOqlWG05MfW6T7mUjI2CK5BdQ6FrV3zEm`);
  const biliUrl = sec > 0
    ? `https://www.bilibili.com/video/BV16sH963EgW/?p=${epNum}&t=${sec}`
    : (lesson.biliUrl || `https://www.bilibili.com/video/BV16sH963EgW/?p=${epNum}`);
  return { ytUrl, biliUrl, epNum, padded };
}

function openImageViewer(src, title, caption, epId, seconds) {
  const viewer = document.getElementById('imageViewer');
  const viewerImg = document.getElementById('viewerImg');
  const viewerTitle = document.getElementById('viewerTitle');
  const viewerCaption = document.getElementById('viewerCaption');
  const jumpYT = document.getElementById('viewerJumpYT');
  const jumpBili = document.getElementById('viewerJumpBili');
  viewerImg.src = src;
  viewerTitle.textContent = title || '课程原图';
  viewerCaption.textContent = caption || '';
  if (epId && seconds !== null && seconds !== undefined) {
    const urls = buildVideoUrls(epId, seconds);
    jumpYT.style.display = 'inline-block';
    jumpYT.href = urls.ytUrl;
    jumpBili.style.display = 'inline-block';
    jumpBili.href = urls.biliUrl;
  } else {
    jumpYT.style.display = 'none';
    jumpBili.style.display = 'none';
  }
  if (!viewer.open) viewer.showModal();
}

function renderMtfView() {
  const lesson = LESSON_LIBRARY.find((l) => l.id === state.videoEpId) || LESSON_LIBRARY[0];
  const epUrls = buildVideoUrls(lesson.id, 0);
  document.getElementById('videoEpBadge').textContent = `Episode ${lesson.id} · 时长 ${lesson.duration || ''} · YouTube & B站双端跳帧`;
  document.getElementById('videoEpTitle').textContent = `${lesson.title}`;

  const selector = document.getElementById('videoEpSelector');
  selector.innerHTML = ['01', '02', '03', '04', '05'].map((id) => `
    <button class="chip ${state.videoEpId === id ? 'active' : ''}" data-vep="${id}" type="button">Ep.${id}</button>
  `).join('');

  selector.querySelectorAll('[data-vep]').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.videoEpId = btn.dataset.vep;
      saveState();
      renderMtfView();
    });
  });

  const heroEl = document.getElementById('videoExternalHero');
  if (heroEl) {
    heroEl.innerHTML = `
      <p class="muted" style="margin:0 0 10px;">${escapeHtml(lesson.summary || '')}</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <a class="website-link" href="${escapeHtml(epUrls.ytUrl)}" target="_blank" rel="noopener">🎬 打开 YouTube 原片 (Ep.${escapeHtml(lesson.id)}) ↗</a>
        <a class="website-link" href="${escapeHtml(epUrls.biliUrl)}" target="_blank" rel="noopener">📺 打开 B站中配 (P${epUrls.epNum}) ↗</a>
      </div>
    `;
  }

  const jumpsEl = document.getElementById('videoKeyframeJumps');
  const kfs = lesson.keyframes || [];
  if (kfs.length) {
    jumpsEl.innerHTML = kfs.map((kf) => {
      const urls = buildVideoUrls(lesson.id, kf.seconds);
      const tStr = kf.timeStr || kf.time || '';
      const tTitle = kf.titleZh || kf.title || '';
      return `
        <div class="kf-jump-row" style="cursor:default;">
          <div>
            <span class="badge-core" style="margin-right:6px;">${escapeHtml(kf.timeframe || '')}</span>
            <strong>${escapeHtml(tTitle)}</strong>
          </div>
          <span class="dual-jump" style="flex-shrink:0;">
            <a class="time-pill yt-pill" href="${escapeHtml(urls.ytUrl)}" target="_blank" rel="noopener">🎬 YT [${escapeHtml(tStr)}] ↗</a>
            <a class="time-pill bili-pill" href="${escapeHtml(urls.biliUrl)}" target="_blank" rel="noopener">📺 B站 [${escapeHtml(tStr)}] ↗</a>
          </span>
        </div>
      `;
    }).join('');
  } else {
    jumpsEl.innerHTML = '<p class="muted">可在课堂讲义中点击任意时间节点直达 YouTube 或 B站对应秒数。</p>';
  }

  // Render MTF Slider
  const activeCase = MTF_WALKTHROUGHS.find((c) => c.id === state.mtfCaseId) || MTF_WALKTHROUGHS[0];
  if (state.mtfStepIndex >= activeCase.steps.length) state.mtfStepIndex = 0;
  const activeStep = activeCase.steps[state.mtfStepIndex];
  const stepUrls = buildVideoUrls(activeCase.ep, activeStep.seconds);

  const caseTabs = document.getElementById('mtfCaseTabs');
  caseTabs.innerHTML = MTF_WALKTHROUGHS.map((c) => `
    <button class="chip ${c.id === activeCase.id ? 'active' : ''}" data-mcase="${c.id}" type="button">${escapeHtml(c.title.split('·')[1] || c.title)}</button>
  `).join('');
  caseTabs.querySelectorAll('[data-mcase]').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.mtfCaseId = btn.dataset.mcase;
      state.mtfStepIndex = 0;
      const chosen = MTF_WALKTHROUGHS.find((c) => c.id === state.mtfCaseId);
      if (chosen) state.videoEpId = chosen.ep;
      saveState();
      renderMtfView();
    });
  });

  const tfStrip = document.getElementById('mtfTfStrip');
  tfStrip.innerHTML = activeCase.steps.map((step, idx) => `
    <button class="chip ${idx === state.mtfStepIndex ? 'active' : ''}" data-mtf-idx="${idx}" type="button">
      ${idx + 1}. ${escapeHtml(step.tf)}
    </button>
  `).join('');
  tfStrip.querySelectorAll('[data-mtf-idx]').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.mtfStepIndex = Number(btn.dataset.mtfIdx);
      saveState();
      renderMtfView();
    });
  });

  const blindBtn = document.getElementById('toggleBlindQuiz');
  blindBtn.textContent = state.blindQuiz ? '关闭盲测遮罩（已开启：悬停可偷看）' : '开启盲测遮罩模式（先自己看图判断）';
  blindBtn.className = state.blindQuiz ? 'primary' : 'ghost';

  const stageEl = document.getElementById('mtfStage');
  stageEl.innerHTML = `
    <div class="mtf-stage-card">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:8px;">
        <strong>当前层级：${escapeHtml(activeStep.tf)} · 本层任务：${escapeHtml(activeStep.goal)}</strong>
        <span class="dual-jump">
          <a class="time-pill yt-pill" href="${escapeHtml(stepUrls.ytUrl)}" target="_blank" rel="noopener">🎬 YT [${escapeHtml(activeStep.time)}] ↗</a>
          <a class="time-pill bili-pill" href="${escapeHtml(stepUrls.biliUrl)}" target="_blank" rel="noopener">📺 B站 [${escapeHtml(activeStep.time)}] ↗</a>
        </span>
      </div>
      <img src="${escapeHtml(activeStep.src)}" alt="${escapeHtml(activeStep.tf)}" id="mtfStageImg" />
      <div class="${state.blindQuiz ? 'blind-mask' : ''}" style="margin-top:12px;display:grid;gap:8px;">
        <div class="dfig-guide"><strong>盘面客观事实：</strong>${escapeHtml(activeStep.observation)}</div>
        <div class="dcore"><strong>本层执行动作：</strong>${escapeHtml(activeStep.action)}</div>
      </div>
      <div style="display:flex;justify-content:space-between;margin-top:12px;">
        <button class="ghost small" id="prevMtfStep" type="button" ${state.mtfStepIndex === 0 ? 'disabled' : ''}>← 上一周期</button>
        <small class="muted">进度：${state.mtfStepIndex + 1} / ${activeCase.steps.length}</small>
        <button class="primary small" id="nextMtfStep" type="button" ${state.mtfStepIndex >= activeCase.steps.length - 1 ? 'disabled' : ''}>下一周期 (剥洋葱) →</button>
      </div>
    </div>
  `;

  document.getElementById('mtfStageImg').addEventListener('click', () => {
    openImageViewer(activeStep.src, `${activeCase.title} · ${activeStep.tf}`, activeStep.observation, activeCase.ep, activeStep.seconds);
  });
  document.getElementById('prevMtfStep').addEventListener('click', () => {
    if (state.mtfStepIndex > 0) {
      state.mtfStepIndex -= 1;
      renderMtfView();
    }
  });
  document.getElementById('nextMtfStep').addEventListener('click', () => {
    if (state.mtfStepIndex < activeCase.steps.length - 1) {
      state.mtfStepIndex += 1;
      renderMtfView();
    }
  });
}

function renderOrderflow() {
  const stepsEl = document.getElementById('flowSteps');
  const detailEl = document.getElementById('flowDetail');
  const active = ORDERFLOW_STEPS.find((item) => item.id === state.flowStepId) || ORDERFLOW_STEPS[0];

  stepsEl.innerHTML = ORDERFLOW_STEPS.map((step) => `
    <button class="flow-step ${step.id === active.id ? 'active' : ''}" data-step="${step.id}">
      <span>STEP ${escapeHtml(step.step)}</span>
      <h3>${escapeHtml(step.title)}</h3>
      <p>${escapeHtml(step.question)}</p>
    </button>
  `).join('');

  stepsEl.querySelectorAll('[data-step]').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.flowStepId = btn.dataset.step;
      saveState();
      renderOrderflow();
    });
  });

  detailEl.innerHTML = `
    <div>
      <p class="eyebrow">步骤 ${escapeHtml(active.step)} · 核心问题</p>
      <h3>${escapeHtml(active.title)}：${escapeHtml(active.question)}</h3>
      <ul>
        ${active.bullets.map((line) => `<li>${escapeHtml(line)}</li>`).join('')}
      </ul>
    </div>
    <div>
      <div class="dtrap" style="margin-bottom:12px;">
        <strong>本时段最常见致命错误</strong>
        <p style="margin:6px 0 0;">${escapeHtml(active.trap)}</p>
      </div>
      <div class="dfig-guide">
        <strong>本时段通过标准</strong>
        <p style="margin:6px 0 0;">${escapeHtml(active.output)}</p>
      </div>
    </div>
  `;

  // Render Pre-trade Checklist
  const checkEl = document.getElementById('preTradeChecklist');
  checkEl.innerHTML = PRE_TRADE_CHECKLIST.map((item) => {
    const checked = Boolean(state.checklist[item.id]);
    return `
      <label class="check-row ${checked ? 'checked' : ''}">
        <input type="checkbox" data-check-id="${item.id}" ${checked ? 'checked' : ''} style="width:auto;margin-top:3px;" />
        <div>
          <strong>${escapeHtml(item.label)}</strong>
          <div class="muted" style="font-size:0.82rem;">${escapeHtml(item.detail)}</div>
        </div>
      </label>
    `;
  }).join('');

  checkEl.querySelectorAll('[data-check-id]').forEach((input) => {
    input.addEventListener('change', () => {
      state.checklist[input.dataset.checkId] = input.checked;
      saveState();
      renderOrderflow();
    });
  });

  // Render Glossary
  const glossaryEl = document.getElementById('glossaryList');
  glossaryEl.innerHTML = (window.ICT_GLOSSARY || []).map((g) => `
    <div class="glossary-item">
      <strong>${escapeHtml(g.term)} · ${escapeHtml(g.zh)} <small class="muted">(${escapeHtml(g.full)})</small></strong>
      <p>${escapeHtml(g.desc)}</p>
    </div>
  `).join('');
}

function diagramMarkup(type) {
  if (type === 'sweep_bsl_short') {
    return `
      <svg viewBox="0 0 520 190" role="img" aria-label="08:30 刺穿 Equal Highs 后向下 MSS 与溢价区 FVG">
        <rect x="12" y="14" width="496" height="162" rx="6" fill="#fafbf7" stroke="#d8e2d8" />
        <line x1="36" y1="54" x2="484" y2="54" stroke="#923d3d" stroke-dasharray="5 5" />
        <text x="42" y="46" fill="#923d3d" font-size="11">15m Equal Highs (BSL 买方止损池)</text>
        <line x1="36" y1="98" x2="484" y2="98" stroke="#5b6d67" stroke-dasharray="3 3" />
        <text x="42" y="92" fill="#5b6d67" font-size="10">0.5 Equilibrium (均衡位)</text>
        <rect x="255" y="64" width="140" height="22" fill="#f7e4e4" stroke="#923d3d" />
        <text x="263" y="79" fill="#923d3d" font-size="11">Bearish FVG (溢价区挂空点)</text>
        <polyline fill="none" stroke="#20322f" stroke-width="3"
          points="42,135 95,56 135,88 182,55 215,102 246,34 275,122 332,74 445,156" />
        <circle cx="246" cy="34" r="5" fill="#923d3d" />
        <text x="200" y="27" fill="#923d3d" font-size="11">08:30 Stop Hunt</text>
        <circle cx="332" cy="74" r="5" fill="#285e50" />
        <text x="342" y="76" fill="#285e50" font-size="11">Execute Short</text>
      </svg>
    `;
  }
  if (type === 'sweep_ssl_long') {
    return `
      <svg viewBox="0 0 520 190" role="img" aria-label="扫 SSL 后向上 MSS 与折价区 FVG + OB">
        <rect x="12" y="14" width="496" height="162" rx="6" fill="#fafbf7" stroke="#d8e2d8" />
        <line x1="36" y1="142" x2="484" y2="142" stroke="#285e50" stroke-dasharray="5 5" />
        <text x="42" y="158" fill="#285e50" font-size="11">Old Session Low (SSL 卖方止损池)</text>
        <rect x="245" y="106" width="145" height="24" fill="#e3eee8" stroke="#285e50" />
        <text x="253" y="122" fill="#183e35" font-size="11">Discount Bullish FVG + OB</text>
        <polyline fill="none" stroke="#20322f" stroke-width="3"
          points="44,68 110,125 160,96 218,162 268,62 325,116 446,36" />
        <circle cx="218" cy="162" r="5" fill="#9b6a1b" />
        <text x="165" y="174" fill="#9b6a1b" font-size="11">Sweep SSL</text>
        <circle cx="325" cy="116" r="5" fill="#285e50" />
        <text x="335" y="116" fill="#285e50" font-size="11">Buy Limit 成交</text>
      </svg>
    `;
  }
  return `
    <svg viewBox="0 0 520 190" role="img" aria-label="12:00 午休禁区与 13:30 下午盘扫损反手">
      <rect x="12" y="14" width="496" height="162" rx="6" fill="#fafbf7" stroke="#d8e2d8" />
      <rect x="65" y="24" width="145" height="140" fill="#f7eed8" opacity="0.65" />
      <text x="76" y="44" fill="#9b6a1b" font-size="11">12:00-13:00 NY Lunch (Wait)</text>
      <line x1="65" y1="68" x2="360" y2="68" stroke="#923d3d" stroke-dasharray="4 4" />
      <text x="75" y="62" fill="#923d3d" font-size="11">Lunch High (BSL)</text>
      <polyline fill="none" stroke="#20322f" stroke-width="3"
        points="40,115 95,72 145,108 195,70 255,42 295,118 338,82 455,158" />
      <circle cx="255" cy="42" r="5" fill="#923d3d" />
      <text x="225" y="34" fill="#923d3d" font-size="11">13:30 Sweep</text>
      <circle cx="338" cy="82" r="5" fill="#285e50" />
      <text x="348" y="84" fill="#285e50" font-size="11">PM FVG Short → MOC</text>
    </svg>
  `;
}

function renderPractice() {
  const batch = PRACTICE_BATCHES.find((item) => item.id === state.batchId) || PRACTICE_BATCHES[0];
  document.getElementById('batchTitle').textContent = batch.title;

  const tabs = document.getElementById('batchTabs');
  tabs.innerHTML = PRACTICE_BATCHES.map((item) => `
    <button class="chip ${item.id === batch.id ? 'active' : ''}" data-batch="${item.id}">
      ${escapeHtml(item.title.split('·')[0].trim())}
    </button>
  `).join('');

  tabs.querySelectorAll('[data-batch]').forEach((btn) => {
    btn.addEventListener('click', () => {
      state.batchId = btn.dataset.batch;
      saveState();
      renderPractice();
    });
  });

  document.getElementById('caseBanner').innerHTML = `
    <div>
      <p class="eyebrow">训练目标 · ${escapeHtml(batch.focus)}</p>
      <h3>${escapeHtml(batch.caseTitle)}</h3>
      <p class="muted">${escapeHtml(batch.caseSummary)}</p>
    </div>
    <div class="replay-diagram">
      ${diagramMarkup(batch.diagram)}
    </div>
  `;

  const questionList = document.getElementById('questionList');
  questionList.innerHTML = batch.questions.map((q, index) => {
    const saved = state.answers[q.id] || { action: '', reason: '', revealed: false };
    const matched = saved.action === q.expectedAction;
    return `
      <article class="q-card" data-qid="${q.id}">
        <div class="q-top">
          <small>第 ${index + 1} 题 / 共 3 题</small>
          <h3>${escapeHtml(q.moment)}</h3>
          <p class="q-prompt">${escapeHtml(q.prompt)}</p>
          <p class="muted"><strong>思考提示：</strong>${escapeHtml(q.hint)}</p>
        </div>

        <div>
          <label>你的动作判断
            <select data-field="action">
              <option value="">先选你的动作…</option>
              ${ACTION_OPTIONS.map((opt) => `
                <option value="${opt.value}" ${saved.action === opt.value ? 'selected' : ''}>${escapeHtml(opt.label)}</option>
              `).join('')}
            </select>
          </label>

          <label>为什么这样处理（写出扫损池、MSS、0.5 均衡位或 FVG 依据）
            <textarea data-field="reason" placeholder="先写你自己的判断，不要怕错...">${escapeHtml(saved.reason)}</textarea>
          </label>

          <button class="ghost small" data-reveal="${q.id}">查看导师解释</button>

          <div class="teacher-box ${saved.revealed ? 'visible' : ''}">
            <span class="verdict ${matched ? 'good' : 'warn'}">
              ${saved.action ? (matched ? '动作一致' : `建议动作：${q.expectedAction}`) : `参考动作：${q.expectedAction}`}
            </span>
            <p><strong>为什么：</strong>${escapeHtml(q.teacherWhy)}</p>
            <p class="muted"><strong>把你原话再推进一步：</strong>${escapeHtml(q.nudge)}</p>
          </div>
        </div>
      </article>
    `;
  }).join('');

  questionList.querySelectorAll('.q-card').forEach((card) => {
    const qid = card.dataset.qid;
    const actionSelect = card.querySelector('[data-field="action"]');
    const reasonBox = card.querySelector('[data-field="reason"]');
    const revealBtn = card.querySelector('[data-reveal]');

    const update = (revealedFlag) => {
      const prev = state.answers[qid] || {};
      state.answers[qid] = {
        action: actionSelect.value,
        reason: reasonBox.value,
        revealed: typeof revealedFlag === 'boolean' ? revealedFlag : Boolean(prev.revealed)
      };
      saveState();
    };

    actionSelect.addEventListener('change', () => update());
    reasonBox.addEventListener('input', () => update());
    revealBtn.addEventListener('click', () => {
      update(true);
      renderPractice();
      updateBatchFeedback(batch);
    });
  });

  updateBatchFeedback(batch);
}

function updateBatchFeedback(batch) {
  const answered = batch.questions.filter((q) => {
    const a = state.answers[q.id];
    return a && a.action && a.reason.trim().length >= 4;
  }).length;
  const matched = batch.questions.filter((q) => {
    const a = state.answers[q.id];
    return a && a.action === q.expectedAction;
  }).length;
  const feedback = document.getElementById('batchFeedback');
  if (answered < 3) {
    feedback.textContent = `本组已完整作答 ${answered} / 3 题。建议每题都写下“扫了哪侧流动性 + 是否有 MSS + FVG 是否在折价/溢价区”。`;
  } else {
    feedback.textContent = `本组 3 题已全部写完，动作与 ICT 标准答案一致 ${matched} / 3 题。点“保存原答并继续”进入下一组。`;
  }
}

function computeJournalPreview() {
  const sym = document.getElementById('jSymbol').value;
  const contracts = Math.max(1, Number(document.getElementById('jContracts').value || 1));
  const entry = Number(document.getElementById('jEntry').value || 0);
  const stop = Number(document.getElementById('jStop').value || 0);
  const target = Number(document.getElementById('jTarget').value || 0);
  const multMap = { MNQ: 2, MES: 5, NQ: 20, ES: 50 };
  const mult = multMap[sym] || 20;

  const pts = entry && target ? Math.abs(entry - target) : 0;
  const risk = entry && stop ? Math.abs(entry - stop) : 0;
  const rr = risk > 0 ? (pts / risk).toFixed(2) : '—';
  const dollars = pts * mult * contracts;

  const preview = document.getElementById('jCalcPreview');
  if (preview) {
    preview.innerHTML = `
      <span>③ 点数距离：<strong>${pts.toFixed(2)} pts</strong></span>
      <span>风险距离：<strong>${risk.toFixed(2)} pts (R:R ${rr})</strong></span>
      <span>④ 折算合约金额 (${contracts} 张 ${sym})：<strong>$${dollars.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</strong></span>
    `;
  }
  return { sym, contracts, entry, stop, target, pts, risk, rr, dollars };
}

function renderJournalView() {
  const dateInput = document.getElementById('jDate');
  if (dateInput && !dateInput.value) {
    dateInput.value = new Date().toISOString().slice(0, 10);
  }
  computeJournalPreview();
  const listEl = document.getElementById('journalEntriesList');
  const countEl = document.getElementById('journalCount');
  const entries = state.journalEntries || [];
  if (countEl) countEl.textContent = String(entries.length);

  listEl.innerHTML = entries.map((item) => `
    <div class="journal-entry-item">
      <div style="display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap;">
        <strong>${escapeHtml(item.date)} · ${escapeHtml(item.symbol)} (${item.contracts}张) · ${escapeHtml(item.direction)}</strong>
        <span class="badge-core">${escapeHtml(item.session)}</span>
      </div>
      <p style="margin:6px 0;font-size:0.88rem;">
        ① 入场 FVG：<b>${item.entry}</b> ｜ ② 止损：<b>${item.stop}</b> ｜ ③ 目标：<b>${item.target}</b>
        （<b>${Number(item.points).toFixed(2)} pts</b> · R:R <b>${escapeHtml(item.rr)}</b> · ④ 折合 <b>$${Number(item.dollars).toLocaleString('en-US', { minimumFractionDigits: 2 })}</b>）
      </p>
      <p class="muted" style="margin:4px 0 0;">${escapeHtml(item.comment || '')}</p>
    </div>
  `).join('');
}

function renderNotebook() {
  const summaryNote = document.getElementById('summaryNote');
  summaryNote.value = state.summaryNote || '';

  const mistakeList = document.getElementById('mistakeList');
  mistakeList.innerHTML = COMMON_MISTAKES.map((text, idx) => {
    const key = `m${idx}`;
    return `
      <label class="mistake-item">
        <input type="checkbox" data-mistake="${key}" ${state.mistakes[key] ? 'checked' : ''} style="width:auto;margin-top:4px;" />
        <span>${escapeHtml(text)}</span>
      </label>
    `;
  }).join('');

  mistakeList.querySelectorAll('[data-mistake]').forEach((box) => {
    box.addEventListener('change', () => {
      state.mistakes[box.dataset.mistake] = box.checked;
      saveState();
    });
  });

  const lessonNotesEl = document.getElementById('savedLessonNotes');
  const lessonNotesCount = document.getElementById('lessonNotesCount');
  const noteItems = LESSON_LIBRARY.filter((l) => (state.lessonNotes[l.id] || '').trim());
  if (lessonNotesCount) lessonNotesCount.textContent = String(noteItems.length);
  if (lessonNotesEl) {
    lessonNotesEl.innerHTML = noteItems.length
      ? noteItems.map((lesson) => `
          <div class="saved-item">
            <small>Ep.${escapeHtml(lesson.id)} · ${escapeHtml(lesson.moduleTitle)}</small>
            <p><strong>${escapeHtml(lesson.title)}</strong></p>
            <p>${escapeHtml(state.lessonNotes[lesson.id])}</p>
          </div>
        `).join('')
      : '<p class="muted">还没有分课笔记。在“01 指导课堂”里打开任意一集即可随时记录。</p>';
  }

  const savedAnswers = document.getElementById('savedAnswers');
  const allQuestions = PRACTICE_BATCHES.flatMap((batch) =>
    batch.questions.map((q) => ({ ...q, batchTitle: batch.title }))
  );
  const items = allQuestions.filter((q) => state.answers[q.id] && (state.answers[q.id].action || state.answers[q.id].reason));

  if (!items.length) {
    savedAnswers.innerHTML = '<p class="muted">还没有保存的练习回答。先去“04 理解练习”完成一组 3 题。</p>';
  } else {
    savedAnswers.innerHTML = items.map((q) => {
      const ans = state.answers[q.id];
      return `
        <div class="saved-item">
          <small>${escapeHtml(q.batchTitle)}</small>
          <p><strong>${escapeHtml(q.moment)}</strong></p>
          <p>你的动作：<b>${escapeHtml(ans.action || '未选')}</b>（建议：${escapeHtml(q.expectedAction)}）</p>
          <p class="muted">${escapeHtml(ans.reason || '未填写理由')}</p>
        </div>
      `;
    }).join('');
  }

  const historyEl = document.getElementById('attemptHistory');
  if (historyEl) {
    const history = (state.attemptHistory || []).slice().reverse();
    historyEl.innerHTML = history.length
      ? history.map((entry, idx) => `
          <div class="saved-item">
            <small>第 ${history.length - idx} 次保存 · ${escapeHtml(entry.savedAt || '')}</small>
            <p><strong>${escapeHtml(entry.batchTitle || entry.batchId)}</strong></p>
            ${(entry.items || []).map((item) => `
              <p><b>${escapeHtml(item.moment)}</b>：${escapeHtml(item.action || '未选')}（参考 ${escapeHtml(item.expectedAction)}）<br /><span class="muted">${escapeHtml(item.reason || '未写理由')}</span></p>
            `).join('')}
          </div>
        `).join('')
      : '<p class="muted">还没有历史答题版本。每次在“04 理解练习”点“保存原答并继续”都会追加一条记录。</p>';
  }
}

function buildContinuePrompt() {
  const checkedMistakes = COMMON_MISTAKES.filter((_, idx) => state.mistakes[`m${idx}`]);
  const noteLines = LESSON_LIBRARY
    .filter((l) => (state.lessonNotes[l.id] || '').trim())
    .map((l) => `- Ep.${l.id} ${l.title}：${state.lessonNotes[l.id].trim()}`);

  return [
    '请读取我在「ICT 2022 学习室」里的学习记录与复盘手帐，结合 ICT 2022 Mentorship 原片点评我的理解、指出盲点并给我下一步训练建议。',
    '',
    `已完成课程：${state.completedLessons.length} / ${LESSON_LIBRARY.length} 讲`,
    `已完成练习组：${state.completedBatches.length} / ${PRACTICE_BATCHES.length} 组`,
    `已记录 Ep.04 复盘手帐：${(state.journalEntries || []).length} 条`,
    state.summaryNote && state.summaryNote.trim() ? `核心理解：${state.summaryNote.trim()}` : '核心理解：（暂未填写）',
    checkedMistakes.length ? `自查易错项：${checkedMistakes.join('；')}` : '自查易错项：（暂未勾选）',
    noteLines.length ? `分课笔记：\n${noteLines.join('\n')}` : '分课笔记：（暂未填写）'
  ].join('\n');
}

function bindEvents() {
  document.querySelectorAll('.nav-btn').forEach((btn) => {
    btn.addEventListener('click', () => setView(btn.dataset.view));
  });

  document.getElementById('startPracticeFromClass').addEventListener('click', () => setView('practice'));
  document.getElementById('goPracticeFromFlow').addEventListener('click', () => setView('practice'));

  document.getElementById('openSystemMapTop').addEventListener('click', () => {
    if (window.openSystemMap) {
      window.openSystemMap(null, (lessonId) => {
        state.lessonId = lessonId;
        saveState();
        renderLibrary();
      });
    }
  });

  const searchInput = document.getElementById('lessonSearch');
  searchInput.addEventListener('input', () => {
    state.lessonQuery = searchInput.value;
    renderLibrary();
  });

  document.getElementById('toggleBlindQuiz').addEventListener('click', () => {
    state.blindQuiz = !state.blindQuiz;
    saveState();
    renderMtfView();
  });

  document.getElementById('resetChecklist').addEventListener('click', () => {
    state.checklist = {};
    saveState();
    renderOrderflow();
  });

  document.getElementById('revealBatch').addEventListener('click', () => {
    const batch = PRACTICE_BATCHES.find((item) => item.id === state.batchId) || PRACTICE_BATCHES[0];
    batch.questions.forEach((q) => {
      const prev = state.answers[q.id] || { action: '', reason: '' };
      state.answers[q.id] = { ...prev, revealed: true };
    });
    saveState({ immediate: true });
    renderPractice();
  });

  document.getElementById('completeBatch').addEventListener('click', () => {
    const currentIndex = PRACTICE_BATCHES.findIndex((item) => item.id === state.batchId);
    const currentBatch = PRACTICE_BATCHES[currentIndex] || PRACTICE_BATCHES[0];
    const snapshotItems = currentBatch.questions.map((q) => {
      const ans = state.answers[q.id] || {};
      return {
        questionId: q.id,
        moment: q.moment,
        action: ans.action || '',
        expectedAction: q.expectedAction,
        reason: ans.reason || ''
      };
    });
    if (snapshotItems.some((item) => item.action || item.reason.trim())) {
      state.attemptHistory.push({
        batchId: currentBatch.id,
        batchTitle: currentBatch.title,
        savedAt: new Date().toLocaleString('zh-CN', { hour12: false }),
        items: snapshotItems
      });
    }
    if (!state.completedBatches.includes(state.batchId)) {
      state.completedBatches.push(state.batchId);
    }
    if (currentIndex >= 0 && currentIndex < PRACTICE_BATCHES.length - 1) {
      state.batchId = PRACTICE_BATCHES[currentIndex + 1].id;
    }
    saveState({ immediate: true });
    renderProgress();
    renderPractice();
  });

  // Journal events
  ['jSymbol', 'jContracts', 'jEntry', 'jStop', 'jTarget'].forEach((id) => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('input', computeJournalPreview);
  });

  document.getElementById('fillDemoJournal').addEventListener('click', () => {
    document.getElementById('jDate').value = '2022-02-04';
    document.getElementById('jSymbol').value = 'NQ';
    document.getElementById('jSession').value = '08:30-11:00 NY AM';
    document.getElementById('jContracts').value = '1';
    document.getElementById('jDirection').value = 'Sweep BSL → Short';
    document.getElementById('jEntry').value = '14957.00';
    document.getElementById('jStop').value = '14989.50';
    document.getElementById('jTarget').value = '14780.75';
    document.getElementById('jComment').value = '【Ep.04 实盘复盘】5m 图三推扫高后出现位移大阴线跌破结构，耐心等回抽 14957 看跌 FVG 进场，14780.75 对侧 SSL 止盈。';
    computeJournalPreview();
  });

  document.getElementById('saveJournalEntry').addEventListener('click', () => {
    const calc = computeJournalPreview();
    if (!calc.entry || !calc.target) return;
    state.journalEntries.unshift({
      id: `j-${Date.now()}`,
      date: document.getElementById('jDate').value || new Date().toISOString().slice(0, 10),
      symbol: calc.sym,
      session: document.getElementById('jSession').value,
      contracts: calc.contracts,
      direction: document.getElementById('jDirection').value,
      entry: calc.entry,
      stop: calc.stop,
      target: calc.target,
      points: calc.pts,
      rr: calc.rr,
      dollars: calc.dollars,
      comment: document.getElementById('jComment').value
    });
    saveState({ immediate: true });
    renderJournalView();
  });

  const summaryNote = document.getElementById('summaryNote');
  summaryNote.addEventListener('input', () => {
    state.summaryNote = summaryNote.value;
    saveState();
  });

  document.getElementById('exportNotes').addEventListener('click', () => {
    flushNativeNotebook();
    const blob = new Blob([JSON.stringify(buildNotebookPayload(), null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `ict-2022-study-notes-${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  });

  const copyBtn = document.getElementById('copyContinueRequest');
  copyBtn.addEventListener('click', () => {
    flushNativeNotebook();
    const promptText = buildContinuePrompt();
    const nativeCopy = window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.copyText;
    if (nativeCopy) {
      nativeCopy.postMessage(promptText);
      copyBtn.textContent = '已复制，直接发给 AI 即可';
      setTimeout(() => { copyBtn.textContent = '复制接续请求'; }, 2400);
      return;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(promptText).then(() => {
        copyBtn.textContent = '已复制，直接发给 AI 即可';
        setTimeout(() => { copyBtn.textContent = '复制接续请求'; }, 2400);
      });
    }
  });

  document.getElementById('reloadApp').addEventListener('click', () => {
    flushNativeNotebook();
    if (window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.reloadPage) {
      window.webkit.messageHandlers.reloadPage.postMessage('reload');
    } else {
      window.location.reload();
    }
  });

  const viewer = document.getElementById('imageViewer');
  document.getElementById('closeViewer').addEventListener('click', () => viewer.close());
  viewer.addEventListener('click', (event) => {
    if (event.target === viewer) viewer.close();
  });

  const systemMap = document.getElementById('systemMap');
  const closeSystemMap = document.getElementById('closeSystemMap');
  if (systemMap && closeSystemMap) {
    closeSystemMap.addEventListener('click', () => systemMap.close());
    systemMap.addEventListener('click', (event) => {
      if (event.target === systemMap) systemMap.close();
    });
  }

  window.addEventListener('beforeunload', () => {
    flushNativeNotebook();
  });
}

// ==========================================================================
// GitHub Sync Checker & Red Dot Alert (本地慢于 GitHub 红点提示)
// ==========================================================================
let syncStatusState = {
  checking: false,
  isBehind: false,
  simulated: false,
  lastCheckTime: null,
  local: null,
  remote: null,
  error: null
};

function getLocalVersionInfo() {
  if (window.ANG_VERSION) return window.ANG_VERSION;
  if (window.ANG_LIBRARY && window.ANG_LIBRARY.versionInfo) return window.ANG_LIBRARY.versionInfo;
  return {
    repo: 'Rouen007/ict-2022-study-room',
    branch: 'main',
    commitSha: 'f58278a',
    commitFullSha: 'f58278a78265b481b47c2e0edabd21b95987bfbb',
    commitDate: '2026-10-24T22:31:05+08:00',
    commitTimestamp: 1792852265,
    commitMessage: 'docs: add master summary and full system distillation guide (Created by Xiao Ang)',
    packagedAt: '2026-10-25 08:00:00'
  };
}

async function checkGitHubSync(isManual = false) {
  const localVer = getLocalVersionInfo();
  syncStatusState.local = localVer;
  syncStatusState.checking = true;
  syncStatusState.error = null;
  updateSyncUI();

  // Support simulated behind state for instant verification
  if (localStorage.getItem('ict_simulate_behind') === 'true' || window.__ICT_FORCE_BEHIND__) {
    await new Promise((r) => setTimeout(r, 350));
    syncStatusState.checking = false;
    syncStatusState.isBehind = true;
    syncStatusState.simulated = true;
    syncStatusState.lastCheckTime = new Date();
    syncStatusState.remote = {
      sha: '9c84e1b',
      fullSha: '9c84e1b2f4837dc8a1e948c2057391da401bca99',
      date: new Date().toISOString(),
      msg: 'feat: add enhanced ICT orderflow tape-reading models and real-time alerts (Simulated)'
    };
    updateSyncUI();
    return;
  }

  let remoteData = null;

  // 1. Query GitHub Commits API
  try {
    const apiUrl = `https://api.github.com/repos/${localVer.repo}/commits/${localVer.branch}`;
    const resp = await fetch(apiUrl, {
      cache: 'no-cache',
      headers: { 'Accept': 'application/vnd.github.v3+json' }
    });
    if (resp.ok) {
      const data = await resp.json();
      const rSha = (data.sha || '').substring(0, 7);
      const rDate = data.commit?.committer?.date || data.commit?.author?.date;
      const rMsg = (data.commit?.message || '').split('\n')[0];
      remoteData = {
        sha: rSha,
        fullSha: data.sha || '',
        date: rDate,
        msg: rMsg
      };
    }
  } catch (err) {
    console.warn('[SyncCheck] GitHub API failed, attempting raw version.json...', err);
  }

  // 2. Fallback: Query raw version.json
  if (!remoteData) {
    try {
      const rawUrl = `https://raw.githubusercontent.com/${localVer.repo}/${localVer.branch}/study-room/version.json?_t=${Date.now()}`;
      const rawResp = await fetch(rawUrl, { cache: 'no-cache' });
      if (rawResp.ok) {
        const rawJson = await rawResp.json();
        remoteData = {
          sha: (rawJson.commitSha || '').substring(0, 7),
          fullSha: rawJson.commitFullSha || rawJson.commitSha || '',
          date: rawJson.commitDate,
          msg: rawJson.commitMessage || 'latest commit from version.json'
        };
      }
    } catch (err2) {
      console.warn('[SyncCheck] Fallback raw version.json failed too:', err2);
    }
  }

  syncStatusState.checking = false;
  syncStatusState.lastCheckTime = new Date();

  if (remoteData) {
    const remoteTime = new Date(remoteData.date).getTime();
    const localTime = localVer.commitTimestamp
      ? (localVer.commitTimestamp * 1000)
      : new Date(localVer.commitDate).getTime();

    // Condition for local being behind GitHub:
    // Remote SHA differs from local SHA, AND remote commit timestamp is newer (by > 5000ms buffer)
    const isBehind = (remoteData.sha !== localVer.commitSha && remoteTime > localTime + 5000);

    syncStatusState.isBehind = isBehind;
    syncStatusState.simulated = false;
    syncStatusState.remote = remoteData;
  } else {
    syncStatusState.error = '未能获取 GitHub 远程数据（可能处于离线或网络受限状态）';
    syncStatusState.isBehind = false;
  }

  updateSyncUI();
}

function updateSyncUI() {
  const chip = document.getElementById('gitSyncChip');
  const chipDot = document.getElementById('syncChipDot');
  const chipLabel = document.getElementById('syncChipLabel');
  const topBtn = document.getElementById('gitTopPill');
  const topDot = document.getElementById('syncTopDot');
  const topLabel = document.getElementById('syncTopLabel');
  const behindBanner = document.getElementById('syncBehindBanner');

  if (syncStatusState.checking) {
    if (chip) chip.className = 'git-sync-chip';
    if (chipDot) chipDot.className = 'sync-dot checking';
    if (chipLabel) chipLabel.textContent = '检测中…';
    if (topBtn) topBtn.classList.remove('has-update');
    if (topDot) topDot.className = 'sync-dot checking';
    if (topLabel) topLabel.textContent = '检测中…';
    if (behindBanner) behindBanner.style.display = 'none';
  } else if (syncStatusState.isBehind) {
    // 🔴 RED DOT: Local is behind GitHub!
    if (chip) chip.className = 'git-sync-chip has-update';
    if (chipDot) chipDot.className = 'sync-dot red';
    if (chipLabel) chipLabel.textContent = '有新数据 🔴';
    if (topBtn) topBtn.classList.add('has-update');
    if (topDot) topDot.className = 'sync-dot red';
    if (topLabel) topLabel.textContent = '发现 GitHub 更新 🔴';
    if (behindBanner) behindBanner.style.display = 'flex';
  } else if (syncStatusState.error) {
    if (chip) chip.className = 'git-sync-chip';
    if (chipDot) chipDot.className = 'sync-dot grey';
    if (chipLabel) chipLabel.textContent = '离线模式';
    if (topBtn) topBtn.classList.remove('has-update');
    if (topDot) topDot.className = 'sync-dot grey';
    if (topLabel) topLabel.textContent = '本地模式';
    if (behindBanner) behindBanner.style.display = 'none';
  } else {
    // 🟢 GREEN DOT: Local is up to date!
    if (chip) chip.className = 'git-sync-chip';
    if (chipDot) chipDot.className = 'sync-dot green';
    if (chipLabel) chipLabel.textContent = '已同步';
    if (topBtn) topBtn.classList.remove('has-update');
    if (topDot) topDot.className = 'sync-dot green';
    if (topLabel) topLabel.textContent = '已与 GitHub 同步';
    if (behindBanner) behindBanner.style.display = 'none';
  }

  renderSyncModalDetails();
}

function renderSyncModalDetails() {
  const modal = document.getElementById('syncModal');
  if (!modal) return;

  const titleEl = document.getElementById('syncModalStatusTitle');
  const subEl = document.getElementById('syncModalStatusSub');
  const iconEl = document.getElementById('syncModalIcon');
  const noticeBox = document.getElementById('syncNoticeBox');
  const noticeDesc = document.getElementById('syncNoticeDesc');
  const cmdCard = document.getElementById('syncCmdCard');
  const remoteCard = document.getElementById('remoteCard');
  const remoteBadge = document.getElementById('remoteBadge');

  const localShaEl = document.getElementById('localShaDisplay');
  const localDateEl = document.getElementById('localDateDisplay');
  const localMsgEl = document.getElementById('localMsgDisplay');

  const remoteShaEl = document.getElementById('remoteShaDisplay');
  const remoteDateEl = document.getElementById('remoteDateDisplay');
  const remoteMsgEl = document.getElementById('remoteMsgDisplay');
  const simBtn = document.getElementById('btnSimulateBehind');

  const loc = syncStatusState.local || getLocalVersionInfo();
  if (localShaEl) localShaEl.textContent = loc.commitSha || 'unknown';
  if (localDateEl) localDateEl.textContent = loc.commitDate ? loc.commitDate.replace('T', ' ').slice(0, 19) : '--';
  if (localMsgEl) localMsgEl.textContent = loc.commitMessage || '本地已构建版本';

  const rem = syncStatusState.remote;
  if (rem) {
    if (remoteShaEl) remoteShaEl.textContent = rem.sha || '-------';
    if (remoteDateEl) remoteDateEl.textContent = rem.date ? rem.date.replace('T', ' ').slice(0, 19) : '--';
    if (remoteMsgEl) remoteMsgEl.textContent = rem.msg || '最新提交';
  } else {
    if (remoteShaEl) remoteShaEl.textContent = '-------';
    if (remoteDateEl) remoteDateEl.textContent = '--';
    if (remoteMsgEl) remoteMsgEl.textContent = syncStatusState.error || '未获取到远程数据';
  }

  if (simBtn) {
    const isSim = localStorage.getItem('ict_simulate_behind') === 'true';
    simBtn.textContent = isSim ? '🟢 关闭模拟落后状态' : '🔴 模拟落后测试开关';
  }

  if (syncStatusState.checking) {
    if (iconEl) iconEl.textContent = '🔄';
    if (titleEl) titleEl.textContent = '正在检测 GitHub 仓库同步状态…';
    if (subEl) subEl.textContent = '正在连接 api.github.com 查询最新提交…';
    if (noticeBox) noticeBox.className = 'sync-notice-box';
    if (noticeDesc) noticeDesc.textContent = '正在对比本地 Commit 与 GitHub main 分支最新记录…';
    if (cmdCard) cmdCard.style.display = 'none';
    if (remoteCard) remoteCard.className = 'sync-compare-card remote';
    if (remoteBadge) { remoteBadge.className = 'card-status-badge'; remoteBadge.textContent = '检测中'; }
  } else if (syncStatusState.isBehind) {
    // RED BEHIND
    if (iconEl) iconEl.textContent = '🔴';
    if (titleEl) titleEl.textContent = '本地数据慢于 GitHub 远程仓库';
    if (subEl) subEl.textContent = syncStatusState.simulated ? '【当前为模拟测试模式】检测到 GitHub 存在更新' : '检测到 GitHub 存在新的讲义、图解或优化';
    if (noticeBox) noticeBox.className = 'sync-notice-box alert-red';
    if (noticeDesc) noticeDesc.innerHTML = `<strong>⚠️ 发现更新</strong>：GitHub 仓库上已有较新的提交（<code>${rem ? rem.sha : ''}</code>）。请在工作区拉取更新，确保学习室呈现全套最新内容。`;
    if (cmdCard) cmdCard.style.display = 'block';
    if (remoteCard) remoteCard.className = 'sync-compare-card remote has-update';
    if (remoteBadge) { remoteBadge.className = 'card-status-badge badge-update-needed'; remoteBadge.textContent = '有新提交待拉取'; }
  } else if (syncStatusState.error) {
    if (iconEl) iconEl.textContent = '⚪';
    if (titleEl) titleEl.textContent = '离线模式 / 未能连接 GitHub';
    if (subEl) subEl.textContent = '网络暂不可用或达到 API 频次限制';
    if (noticeBox) noticeBox.className = 'sync-notice-box';
    if (noticeDesc) noticeDesc.textContent = syncStatusState.error + '。当前继续流畅使用本地所有 37 讲全部离线资源。';
    if (cmdCard) cmdCard.style.display = 'none';
    if (remoteCard) remoteCard.className = 'sync-compare-card remote';
    if (remoteBadge) { remoteBadge.className = 'card-status-badge'; remoteBadge.textContent = '离线'; }
  } else {
    // GREEN LATEST
    if (iconEl) iconEl.textContent = '🟢';
    if (titleEl) titleEl.textContent = '本地数据已是最新';
    if (subEl) subEl.textContent = '与 GitHub main 分支完全一致';
    if (noticeBox) noticeBox.className = 'sync-notice-box';
    if (noticeDesc) noticeDesc.innerHTML = `<strong>✅ 状态良好</strong>：本地 Commit 与 GitHub 远程 <code>${loc.repo}</code> 完全同步，所有 37 讲 62 张高清图解与三层提炼均为最新版本。`;
    if (cmdCard) cmdCard.style.display = 'none';
    if (remoteCard) remoteCard.className = 'sync-compare-card remote';
    if (remoteBadge) { remoteBadge.className = 'card-status-badge badge-latest'; remoteBadge.textContent = '与远程一致'; }
  }
}

function openSyncModal() {
  const modal = document.getElementById('syncModal');
  if (!modal) return;
  renderSyncModalDetails();
  modal.showModal();
}

function initGitHubSyncCheck() {
  const chip = document.getElementById('gitSyncChip');
  if (chip) chip.addEventListener('click', openSyncModal);

  const topBtn = document.getElementById('gitTopPill');
  if (topBtn) topBtn.addEventListener('click', openSyncModal);

  const banner = document.getElementById('syncBehindBanner');
  if (banner) banner.addEventListener('click', openSyncModal);

  const modal = document.getElementById('syncModal');
  const closeBtn = document.getElementById('closeSyncModal');
  if (closeBtn && modal) {
    closeBtn.addEventListener('click', () => modal.close());
    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.close();
    });
  }

  const checkNowBtn = document.getElementById('btnCheckSyncNow');
  if (checkNowBtn) {
    checkNowBtn.addEventListener('click', () => {
      checkGitHubSync(true);
    });
  }

  const simBtn = document.getElementById('btnSimulateBehind');
  if (simBtn) {
    simBtn.addEventListener('click', () => {
      const isSim = localStorage.getItem('ict_simulate_behind') === 'true';
      if (isSim) {
        localStorage.removeItem('ict_simulate_behind');
        window.__ICT_FORCE_BEHIND__ = false;
      } else {
        localStorage.setItem('ict_simulate_behind', 'true');
        window.__ICT_FORCE_BEHIND__ = true;
      }
      checkGitHubSync(true);
    });
  }

  const copyPullBtn = document.getElementById('btnCopyPullCmd');
  if (copyPullBtn) {
    copyPullBtn.addEventListener('click', () => {
      const cmd = 'git pull origin main && ./study-room/native/build.sh';
      const nativeCopy = window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.copyText;
      if (nativeCopy) {
        nativeCopy.postMessage(cmd);
        copyPullBtn.textContent = '已复制！';
        setTimeout(() => { copyPullBtn.textContent = '复制更新命令'; }, 2000);
        return;
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(cmd).then(() => {
          copyPullBtn.textContent = '已复制！';
          setTimeout(() => { copyPullBtn.textContent = '复制更新命令'; }, 2000);
        });
      }
    });
  }

  // Initial check on startup
  checkGitHubSync(false);

  // Periodic check every 10 minutes
  setInterval(() => {
    checkGitHubSync(false);
  }, 10 * 60 * 1000);
}

function init() {
  renderProgress();
  renderClassroom();
  renderMtfView();
  renderOrderflow();
  renderPractice();
  renderJournalView();
  renderNotebook();
  bindEvents();
  setView(state.view || 'classroom');
  initGitHubSyncCheck();
  flushNativeNotebook();
}

init();
