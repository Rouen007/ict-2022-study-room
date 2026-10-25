"""Compile optional study notes without widening the baseline entry policy."""
import re


def minutes(value):
    if not isinstance(value, str) or not re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d', value):
        raise ValueError(f'Invalid New York clock time: {value!r}')
    hour, minute = map(int, value.split(':'))
    return hour * 60 + minute


def clock(value):
    return f'{value // 60:02d}:{value % 60:02d}'


def interval(start, end):
    a, b = minutes(start), minutes(end)
    if b <= a:
        raise ValueError('Study windows must end after their start on the same local date')
    return a, b


def compile_extensions(framework):
    policy = framework['sessionPolicy']
    if policy['timeZone'] != 'America/New_York':
        raise ValueError('These extension notes use America/New_York')
    entries = sorted(interval(*w) for w in policy['newEntryWindows'])
    if any(b > c for (a, b), (c, d) in zip(entries, entries[1:])):
        raise ValueError('Baseline entry windows overlap')
    macros = []
    ids = set()
    for item in framework.get('macroWindows', []):
        parts = re.split(r'\s*[–—-]\s*', item['time'])
        if len(parts) != 2:
            raise ValueError('Macro needs one start and end')
        a, b = interval(*parts)
        if item.get('evidenceStatus') != 'pending':
            raise ValueError('Extension source passages must be verified before changing pending status')
        key = item.get('id') or f'ny-{clock(a).replace(":", "")}-{clock(b).replace(":", "")}'
        if not re.fullmatch(r'[a-z0-9-]+', key) or key in ids:
            raise ValueError('Missing or duplicated Macro identity')
        ids.add(key)
        inside = [(max(a,c),min(b,d)) for c,d in entries if max(a,c)<min(b,d)]
        outside = []
        cursor = a
        for c,d in inside:
            if cursor < c: outside.append((cursor,c))
            cursor = d
        if cursor < b: outside.append((cursor,b))
        macros.append({**item, 'id':key, 'timeZone':policy['timeZone'],
                       'durationMinutes':b-a,
                       'entryIntersections':[[clock(c),clock(d)] for c,d in inside],
                       'outsideEntryWindows':[[clock(c),clock(d)] for c,d in outside]})
    htf = framework.get('htfEvolution2023')
    if htf and htf.get('evidenceStatus') != 'pending':
        raise ValueError('HTF extension passages have not been verified')
    comparative = framework.get('comparativePerspectives', [])
    return {'role':'optional_observation','policyVersion':policy['id'],'macros':macros,'htf':htf,
            'comparative':comparative,
            'notice':'选学观察材料，来源待核对。Macro 不新增入场权限，不自动提高信号等级；基础训练与题库规则继续独立适用。'}


def extension_markdown(framework):
    ext = compile_extensions(framework)
    lines = []
    if ext['macros'] or ext['htf']:
        lines = ['## 选学补充：Macro 与高周期偏向（来源待核对）', '', ext['notice'], '',
                 '这些时间为用户新增观察窗口，年份归属与具体原课片段尚未核验；不统一称为20分钟窗口。', '',
                 '| 纽约时间 | 时长 | 观察重点 | 与训练新开仓窗口的交集 | 不新增交易的部分 |',
                 '| --- | --- | --- | --- | --- |']
        fmt = lambda items: '、'.join('–'.join(w) for w in items) or '无'
        safe = lambda text: str(text).replace('|', '\\|').replace('\n', ' ')
        for m in ext['macros']:
            lines.append(f'| {m["time"]} | {m["durationMinutes"]}分钟 | {safe(m["focus"])} | {fmt(m["entryIntersections"])} | {fmt(m["outsideEntryWindows"])} |')
        lines += ['', '交集只说明时间条件，仍需满足原有完整入场规则。右端点不含；现有持仓按事前管理计划处理。',
                  'NYSE主板15:50开始公布收盘竞价不平衡信息，16:00开始收盘竞价；15:15–15:45的观察窗口不能直接等同于该流程。参见 [NYSE Auctions](https://www.nyse.com/trade/auctions)。', '']
        if ext['htf']:
            h=ext['htf']
            lines += ['### 高周期偏向与区间扩张笔记', '', h['dailyBiasAnchor'], '', h['dealingRangeExpansion'], '', h['source'], '']
    if ext.get('comparative'):
        for comp in ext['comparative']:
            lines += ['', f'## 外部对比与补充视角：{comp["name"]}', '',
                      f'> **角色与边界声明**：{comp["role"]}。来源：{comp["channel"]}。',
                      f'> 本地资料索引：`{comp["localSource"]}`。以下内容供跨体系对照认知，严禁与 ICT 2022 教学概念混淆。', '',
                      '### 1. 核心哲学与概率思维',
                      f"- **单一方法**：{comp['corePhilosophy']['oneMethod']}",
                      f"- **概率与盈亏比**：{comp['corePhilosophy']['probabilityMindset']}",
                      f"- **离场与纪律**：{comp['corePhilosophy']['disciplineOverTechnique']}",
                      f"- **实证回测参考**：{comp['corePhilosophy']['conservativeData']}", '',
                      '### 2. ICT 2022 vs 2C Trading 核心五维深度对比', '',
                      '| 维度 | ICT 2022 核心机制 | 2C Trading (Al Brooks 裸K) | 综合对照与实践启发 |',
                      '| --- | --- | --- | --- |']
            for kc in comp['keyComparisons']:
                dim = kc['dimension']
                ict_text = f"**{kc['ict2022']['title']}**<br>{kc['ict2022']['mechanism']}<br>执行：{kc['ict2022']['execution']}"
                twoc_text = f"**{kc['twoCTrading']['title']}**<br>{kc['twoCTrading']['mechanism']}<br>执行：{kc['twoCTrading']['execution']}"
                synth = kc['synthesis']
                lines.append(f'| {dim} | {ict_text} | {twoc_text} | {synth} |')
            lines += ['', '### 3. 3根K微通道剥头皮 SOP',
                      comp['threeCandleMicroChannelSop']['title'], '']
            for step in comp['threeCandleMicroChannelSop']['steps']:
                lines.append(f'1. {step}')
            lines += ['', '### 4. 2C Trading 十条反规则黑名单', '']
            for item in comp['tenBlacklistRules']:
                lines.append(f"- **{item['num']}. {item['rule']}**：{item['slogan']}")
            if comp.get('latestVideoEvolutions2026'):
                lines += ['', '### 5. 2026 年最新视频实战演进（2026-09 至 2026-10）', '']
                for key, evo in comp['latestVideoEvolutions2026'].items():
                    lines.append(f"#### {evo['title']}")
                    lines.append(f"- **核心机制**：{evo['core']}")
                    lines.append(f"- **与 ICT 对照**：{evo['ictComparison']}")
                    lines.append('')
            lines.append('')
    return '\n'.join(lines)
