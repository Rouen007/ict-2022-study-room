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
    }
  ]
};
