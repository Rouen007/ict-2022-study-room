window.STUDY_COURSE = {
  "version": 2,
  "policyVersion": "study-ny-v2",
  "batches": [
    {
      "id": "ict-training-v2-1",
      "title": "第 01 组 · 区间锚点与模拟入场",
      "desc": "合成教学练习 · study-ny-v2；动作仅代表模拟状态，不授权下单。图为概念示意，不提供真实成交证据。",
      "lesson": "ep03",
      "questions": [
        {
          "id": "ict-v2-1-0",
          "title": "A / 缺少结构确认",
          "context": "纽约10:15，已观察到价格扫过候选BSL，但没有可确认的反向MSS，也未形成三根已收盘K线的看跌FVG。",
          "answer": "Wait",
          "explanation": "本训练模型证据不足。清扫不保证反转，也不允许推测尚未形成的FVG。",
          "prompt": "还缺哪些可观察证据？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-1-1",
          "title": "B / 条件成立但未回抽",
          "context": "纽约11:25，先扫BSL后出现已确认的反向MSS与位移。11:24已冻结区间14735–14855，中点14795。三根已收盘K线形成看跌FVG 14798–14805，全部在溢价区。MES模拟计划E=14798、S=14856、T=14675，1张，计划风险290美元，成本另计；假设已通过本练习风险上限检查。当前14785，尚未回抽。",
          "answer": "Armed",
          "explanation": "11:25在本训练08:30–12:00新开仓窗口内。已知锚点与风险条件齐全，但尚未模拟成交；12:00前未触发则取消。",
          "prompt": "计算中点与风险金额，并写出取消时刻。",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-1-2",
          "title": "C / 模拟触价",
          "context": "延续B题，同一冻结区间和风险检查仍有效。11:27价格回抽至14798，尚未触及止损或目标；本题明确采用触价即视作模拟成交的假设。",
          "answer": "Execute",
          "explanation": "仅在本题的模拟成交假设下转为Execute。真实限价单是否成交需检查成交回报，不等当前K线最终收阳。目标依据预先计划，不以跨过0.5作为唯一标准。",
          "prompt": "区分模拟触价与真实成交。",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        }
      ]
    },
    {
      "id": "ict-training-v2-2",
      "title": "第 02 组 · 证据不足与取消条件",
      "desc": "合成教学练习 · study-ny-v2；动作仅代表模拟状态，不授权下单。图为概念示意，不提供真实成交证据。",
      "lesson": "ep03",
      "questions": [
        {
          "id": "ict-v2-2-0",
          "title": "A / 只有交付开盘价被突破",
          "context": "10:20，扫SSL后价格突破一串阴线的指定开盘价，但尚未突破记录的短期swing high，也没有已确认FVG。",
          "answer": "Wait",
          "explanation": "交付变化不替代本模型要求的结构与FVG证据。",
          "prompt": "为什么不能用CISD替代MSS？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-2-1",
          "title": "B / 午休出现候选形态",
          "context": "12:25纽约时间，当前无持仓、无挂单；出现完整局部形态。study-ny-v2新开仓窗口已结束。",
          "answer": "Wait",
          "explanation": "本训练午休不新增交易。这是训练限制，不表示市场停止运动，也不定义已有仓位的处理。",
          "prompt": "新开仓限制与持仓管理有何不同？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-2-2",
          "title": "C / 目标先于入场到达",
          "context": "11:40，挂单仍未成交，价格已经先触及原计划目标。本题取消规则规定目标先到即撤销原挂单。",
          "answer": "Cancel",
          "explanation": "原路径已完成，取消未成交计划。没有持仓，因此不是Exit。",
          "prompt": "写出Cancel和Exit的区别。",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        }
      ]
    },
    {
      "id": "ict-training-v2-3",
      "title": "第 03 组 · 反例、仓位方向与退出",
      "desc": "合成教学练习 · study-ny-v2；动作仅代表模拟状态，不授权下单。图为概念示意，不提供真实成交证据。",
      "lesson": "ep03",
      "questions": [
        {
          "id": "ict-v2-3-0",
          "title": "A / SMT不足以执行",
          "context": "10:00，ES创出可比前高，NQ未创新高。数据时间已对齐，但没有本模型所需的清扫后MSS与FVG确认。",
          "answer": "Wait",
          "explanation": "SMT只增加观察信息，不能证明机构派发，也不是单独入场触发。",
          "prompt": "哪些替代解释或反例仍然成立？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-3-1",
          "title": "B / 多单风险参数方向错误",
          "context": "14:15，局部形态满足，但多单计划E=100、S=110、T=90。没有真实持仓，也没有已提交挂单。",
          "answer": "Wait",
          "explanation": "多单应S<E<T。绝对值计算出的正R:R不能修复方向错误；纠正计划后重新检查。",
          "prompt": "为什么不能直接用abs计算并执行？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-3-2",
          "title": "C / 训练退出时刻",
          "context": "15:55，已有模拟多单。事前约定15:55退出，当前尚未触及价格目标。",
          "answer": "Exit",
          "explanation": "按预设持仓计划退出。16:00是本训练的日内边界，不是所有期货休市；无需假定MOC必然加速。",
          "prompt": "退出依赖什么事前规则？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        }
      ]
    },
    {
      "id": "ict-training-v2-4",
      "title": "第 04 组 · 2C 价格行为与微通道避坑",
      "desc": "2C Trading 实战练习 · 覆盖单边微通道 50% 限价、震荡交错区间禁用 50% 挂单排雷、三推楔形 Second Entry 确认。",
      "lesson": "ep03",
      "questions": [
        {
          "id": "ict-v2-4-0",
          "title": "A / 震荡交错区间禁用 50% 挂单（反规则排雷）",
          "context": "10:10 纽约时间，开盘后价格处于明显窄幅震荡区间（全天预期波幅不足 20 点），强阳强阴交替。此时多头连续出现 3 根反弹阳线，学员计划在第 3 根收盘后整段 50% 回撤处挂限价单做多。当前无持仓。",
          "answer": "Wait",
          "explanation": "2C 核心禁忌：在强阳强阴交错的震荡交易区间（Trading Range）内，严禁使用 3 根 K 50% 挂单！区间内缺乏单边推力，极易发生深幅回撤打穿窄止损。中间 1/3 是噪音死区，应观望（Wait），仅允许在上 1/3 做空或下 1/3 做多。",
          "prompt": "为什么震荡交错区间严禁使用 3 根 K 50% 限价单？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-4-1",
          "title": "B / 单边强趋势微通道 50% 限价挂单（Armed 待命）",
          "context": "09:50 纽约时间，开盘单边突破后形成极流畅的单边微通道（Micro Channel），连续 3 根 5m K 线实体饱满无重叠。第 3 根收盘于 14850，整段 50% 位于 14820，止损放通道起点 14805（风险 15 点），第一阻力目标 14860（收益 40 点，Space R = 2.67R ≥ 1.5R）。计划已下达，当前 14845 尚未回抽。",
          "answer": "Armed",
          "explanation": "单边强势微通道推进，形态完全符合 2C 微通道 50% 挂单标准，且 Space R = 2.67R 空间充足。计划已下达等待触价，状态为 Armed；若未回抽直接突破目标则取消。",
          "prompt": "计算该计划的 Space R 并说明为什么此时允许使用 50% 挂单。",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-4-2",
          "title": "C / 三推楔形动能竭尽与二次确认（Execute 模拟触发）",
          "context": "10:25，早盘单边冲高出现第三次脉冲（3-Push / Wedge），斜率变缓、引线增多。第三推刺破前高后收长上影阴线，回踩不创新高收出反向信号 K 确认。学员执行做空，止损放在第三推极值外 1 tick，目标看回测 EMA20（Space R = 2.2R）。本题采用确认信号收盘即视作模拟触发的假设。",
          "answer": "Execute",
          "explanation": "符合 2C 三推楔形（Wedge）动能竭尽与 Second Entry 二次确认模型。不盲目在第一推摸顶，等二次确认信号 K 收盘确认后入场，转为 Execute。",
          "prompt": "为什么三推楔形必须等二次确认（Second Entry）才执行？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        }
      ]
    },
    {
      "id": "ict-training-v2-5",
      "title": "第 05 组 · Junkman 体系 B/T/E/S 状态机与空间否决",
      "desc": "Junkman（JM 体系）实战练习 · 覆盖 B/T/E/S 执行状态机、黄线观察位与 Space R < 1.5R 空间否决门。",
      "lesson": "ep03",
      "questions": [
        {
          "id": "ict-v2-5-0",
          "title": "A / 近端黄线撞墙导致 Space R 不足（Cancel 空间否决）",
          "context": "10:05，SPX 突破 5m 箱体边界 B (5840.00)，回踩打出 T (5838.50)，破微型高点 H (5842.00) 计划做多 E=5842.00，止损 S=5838.00（风险 4 点）。但上方仅 3.5 点处 (5845.50) 存在强正 Gamma 黄线大壁垒。测算 Space R = 3.5 / 4.0 = 0.88R < 1.5R。尚未成交。",
          "answer": "Cancel",
          "explanation": "空间 R 否决门生效！虽然 B/T/E/S 形态合格，但距离上方真实反应壁垒（黄线）不足 5 点，且 Space R = 0.88R 远低于 1.5R 门槛。黄线是大概率减速摩擦区，不能假设价格直接穿墙，必须果断 Cancel 计划，坚决弃权。",
          "prompt": "为什么形态走得再好，Space R < 1.5R 也必须一票否决？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-5-1",
          "title": "B / 完整 B/T/E/S 突破回踩微型结构确认（Execute 模拟触发）",
          "context": "10:15，SPX 5m 大实体彻底收在日内核心边界 B (5800) 上方；随后 1m 回踩未重新跌回 B 核心区下方，打出最远回测端点 T (5802.50)；随后出现回踩后的局部微型高点 H (5806.00)。当前价格正放量突破 5806.00，第一真实目标上方 CW 位于 5818.00（风险 4 点，空间 12 点，Space R = 3.0R）。",
          "answer": "Execute",
          "explanation": "完整走完 Junkman 标准多头链：大实体破 B ➔ 回踩打出 T ➔ 确认微型 H ➔ 突破 H 在 E (5806) 成交，止损置于 T 外侧 (5802)，第一目标 5818（Space R = 3.0R ≥ 1.5R）。符合全部确认条件，转为 Execute。",
          "prompt": "写出该交易的 B、T、E、S 和第一目标数值。",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-5-2",
          "title": "C / 凭先验黄线直接开单的跨层违规（Wait 先验不能当扳机）",
          "context": "09:48，SPX 现价跌落至下方关键黄线 (5790.00) 附近，尚未形成任何反向价格行为反转，K 线仍为大实体阴线向下贯穿。某学员认为“黄线是黄金支撑墙，碰线必反弹”，准备直接在 5790 挂多单。",
          "answer": "Wait",
          "explanation": "跨层严重违规！Junkman 体系铁律：线是先验地图，价格行为才是开单扳机。黄线只回答“在哪里观察”，绝不能直接拿来扣动扳机；实测碰线直接开单为长期负期望。必须等价格在黄线区域产生接受或拒绝的价格行为确认，当前只能 Wait。",
          "prompt": "为什么“黄线是观察位而非买入信号”？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        }
      ]
    },
    {
      "id": "ict-training-v2-6",
      "title": "第 06 组 · 日内反规则秒杀与动态熔断",
      "desc": "实战纪律与反规则练习 · 覆盖死鱼盘整整天弃权、走不顺平保（BE）主动跑、单日双损日内熔断。",
      "lesson": "ep03",
      "questions": [
        {
          "id": "ict-v2-6-0",
          "title": "A / 买入后不顺收反向大实体（Exit 平保主动跑）",
          "context": "10:12，模拟多单在 5810 入场，预期应当干脆利落向上推进。然而随后 2 根 K 线停滞不前，第 3 根直接收出反向大实体阴线吞没入场 K，价格短暂抽回入场成本位 5810。此时尚未触及硬止损 5804。",
          "answer": "Exit",
          "explanation": "2C 实盘核心心法：买入后预期破灭（未顺畅拉开盈利且出现反向大实体），只要市场给平保（BE）机会立即平仓撤离，绝不心存侥幸坐以待毙等打满硬止损。保本离场不丢人，“涨上去就涨上去，涨上去又不赔钱”，转为 Exit。",
          "prompt": "为什么走势迟疑不顺时应平保（BE）主动跑而非硬抗止损？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-6-1",
          "title": "B / 日内预期波幅小于 15 点（Wait 死鱼盘整整天弃权）",
          "context": "09:45，大盘处于重大事件前夕，开盘前 15 分钟 SPX 波幅仅 6 个点，全天日历空白，日均 ATR 极度萎缩，预期日内波幅不足 15 点，均线死缠且长影线乱飞。学员寻找做单机会。",
          "answer": "Wait",
          "explanation": "2C 10 条反规则黑名单 #7 与 Junkman 铁律：日内波幅 < 15 点时直接关电脑休息。低波动窄幅震荡不仅没有盈亏比空间，且做市商算法频繁假突破扫损，强行开单必遭反复打脸。整天弃权（Wait / No Trade）。",
          "prompt": "面对日内波幅 < 15 点的市场，职业交易员的最佳动作是什么？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        },
        {
          "id": "ict-v2-6-2",
          "title": "C / 连续遭遇两笔止损后的单日熔断（Wait 强制收工）",
          "context": "10:40，上午盘两笔符合规则的计划均被止损打出（单日累计亏损达账户 1.5%）。盘面再次出现一个看似符合 FVG / 3根K 的局部小机会，学员产生“再来一把翻本”的冲动。",
          "answer": "Wait",
          "explanation": "触发日内双损熔断铁律！连续被止损 2 次说明今日市场节奏或个人状态与盘面严重脱节。此时再开单极易陷入报复性重仓和纪律崩溃的恶性循环。必须立即关闭交易软件，强制休息，拒绝任何新开仓（Wait）。",
          "prompt": "为什么单日连续 2 笔亏损后必须强制熔断关电脑？",
          "sourceType": "synthetic",
          "policyVersion": "study-ny-v2"
        }
      ]
    }
  ]
};
