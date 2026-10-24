# -*- coding: utf-8 -*-
import os, sys, re, json
import handbook_ep06_11
import handbook_ep12_16
import handbook_ep17_23
import handbook_ep24_30
import handbook_ep31_37

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OLD_HB = os.path.join(BASE_DIR, "ICT_2022_Ep01_05_图文精读手册.md")
OUT_HB = os.path.join(BASE_DIR, "ICT_2022_全37讲_图文精读手册.md")

with open(OLD_HB, "r", encoding="utf-8") as f:
    old_content = f.read()

# Extract ep 1 to 5 from old handbook
splits = re.split(r"(?=^## Ep\.\s*\d+)", old_content, flags=re.M)
ep1_5_chapters = {}
for s in splits:
    m = re.match(r"^## Ep\.\s*(\d+)", s)
    if m:
        ep_i = int(m.group(1))
        ep1_5_chapters[ep_i] = s.strip()

# Combine all chapters 1 to 37
all_chapters = {}
for i in range(1, 6):
    all_chapters[i] = ep1_5_chapters[i]

for i in range(6, 12):
    all_chapters[i] = handbook_ep06_11.CHAPTERS[i].strip()

for i in range(12, 17):
    all_chapters[i] = handbook_ep12_16.CHAPTERS[i].strip()

for i in range(17, 24):
    all_chapters[i] = handbook_ep17_23.CHAPTERS[i].strip()

for i in range(24, 31):
    all_chapters[i] = handbook_ep24_30.CHAPTERS[i].strip()

for i in range(31, 38):
    all_chapters[i] = handbook_ep31_37.CHAPTERS[i].strip()

print(f"Loaded all {len(all_chapters)} chapters.")

# Load courseData.json for metadata table
with open(os.path.join(BASE_DIR, "courseData.json"), "r", encoding="utf-8") as cf:
    cdata = json.load(cf)

ep_map = {ep["ep"]: ep for ep in cdata["episodes"]}

# Build comprehensive header
header = """# ICT 2022 Mentorship [No Rant] 全 37 讲图文精读手册（Ep. 01 – Ep. 37）

> [!NOTE]
> **版本与资料说明**：B 站视频 `BV16sH963EgW`（《【中配】【ICT 2022 no rant】- 精简无废话完整版》）对应 YouTube 频道 **SirTrader** 整理的 37 集精简版播放列表（将 ICT 原版 41 集约 45 小时课程浓缩为 5.7 小时纯干货）。全套 37 集英文逐字稿已提取并保存在本地工作区 [transcripts](file:///Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/transcripts)，本手册覆盖 **全 37 集（全六大模块）完整图文深度精读**，配合 **63 张原片 1080p 关键帧高清图解与架构图谱** 逐图拆解。

---

## 目录与全 37 讲六大演进模块知识图谱

```mermaid
flowchart TD
    subgraph M1["模块一 · 基础模型与日内架构 (Ep.01-05)"]
        E1["Ep.01 预期与合约规格"] --> E2["Ep.02 交易模型四大要素"]
        E2 --> E3["Ep.03 内部流动性与 MSS"]
        E3 --> E4["Ep.04 模型实战手帐规范"]
        E4 --> E5["Ep.05 日内订单流与全天结构"]
    end

    subgraph M2["模块二 · 机构订单流与日内偏向 (Ep.06-11)"]
        E6["Ep.06 市场效率范式与 FVG 原理"] --> E7["Ep.07 日线偏向与整固跳栏"]
        E7 --> E8["Ep.08 外汇直盘与伦敦杀手时区"]
        E8 --> E9["Ep.09 Power of 3 (AMD) 与午夜开盘价"]
        E9 --> E10["Ep.10 经济日历与 08:30 数据脉冲"]
        E10 --> E11["Ep.11 09:30 假动作与结构破坏精析"]
    end

    subgraph M3["模块三 · 进阶市场结构与单边日 (Ep.12-16)"]
        E12["Ep.12 LTH/ITH/STH 三层结构"] --> E13["Ep.13 订单块 50% 均衡位承接"]
        E13 --> E14["Ep.14 单边位移多重 FVG 筛选"]
        E14 --> E15["Ep.15 走盘复盘与 Tape Reading"]
        E15 --> E16["Ep.16 早盘+下午盘多重交易设置"]
    end

    subgraph M4["模块四 · 跨市场联动与特种行情 (Ep.17-23)"]
        E17["Ep.17 DXY 联动与外汇应用"] --> E18["Ep.18 日分割线与订单块底层"]
        E18 --> E19["Ep.19 日内叙事 Narrative 构建"]
        E19 --> E20["Ep.20 伦敦盘透支与纽约盘 OTE 接力"]
        E20 --> E21["Ep.21 风险偏好与等低点引力"]
        E21 --> E22["Ep.22 SMT 聪明钱跨市场背离"]
        E22 --> E23["Ep.23 FOMC 斐波通道与次日延续"]
    end

    subgraph M5["模块五 · 高级技术与复盘细节 (Ep.24-30)"]
        E24["Ep.24 迟滞反转与二次确认"] --> E25["Ep.25 日内再平衡理论与微观 FVG"]
        E25 --> E26["Ep.26 顺势扩张 vs 逆势回撤"]
        E26 --> E27["Ep.27 震荡周生存与下午盘反转"]
        E27 --> E28["Ep.28 周内演化档案 Weekly Profile"]
        E28 --> E29["Ep.29 早盘跳空缺口 NDOG/NWOG"]
        E29 --> E30["Ep.30 平衡价格区间 BPR 高阶机制"]
    end

    subgraph M6["模块六 · 职业化执行与心法大结局 (Ep.31-37)"]
        E31["Ep.31 熊市大势顺势反弹做空"] --> E32["Ep.32 15m FVG 嵌套 1m MSS 极致微操"]
        E32 --> E33["Ep.33 止损后风险减半与心理学"]
        E33 --> E34["Ep.34 PDH/PDL 跨日流动性地图"]
        E34 --> E35["Ep.35 识别 Seek & Destroy 绞肉机日"]
        E35 --> E36["Ep.36 全流程 6 步机械化清单"]
        E36 --> E37["Ep.37 大结局：百图回测与职业之路"]
    end

    M1 --> M2 --> M3 --> M4 --> M5 --> M6
```

### 全 37 讲目录清单与核心解决问题速查表

| 集数 | 原片英文标题 | 模块归属 | 高清图解 | 核心解决问题与机构技术要点 |
| :--- | :--- | :--- | :--- | :--- |
"""

# Append table rows
for ep_i in range(1, 38):
    ep = ep_map[ep_i]
    kf_cnt = len(ep.get("keyframes", []))
    header += f"| **Ep. {ep_i:02d}** | {ep['titleEn']} | {ep['module']} | `{kf_cnt} 张` | {ep['summaryZh']} |\n"

header += "\n---\n\n"

# Assemble body
body_parts = [header]
for ep_i in range(1, 38):
    body_parts.append(all_chapters[ep_i])
    body_parts.append("\n\n---\n\n")

full_handbook_text = "".join(body_parts)

with open(OUT_HB, "w", encoding="utf-8") as out_f:
    out_f.write(full_handbook_text)

print(f"Generated {OUT_HB} successfully! Total size: {len(full_handbook_text)} bytes, lines: {len(full_handbook_text.splitlines())}")
