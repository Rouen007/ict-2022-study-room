#!/usr/bin/env python3
"""Build offline study assets from validated metadata and explicit evidence records."""
import datetime
import hashlib
import html
import json
import os
from pathlib import Path
import re
import subprocess
from transcript_io import validate_evidence_claims
from framework_extensions import compile_extensions, extension_markdown

BASE_DIR = Path(__file__).resolve().parent
STUDY_DIR = BASE_DIR / 'study-room'

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def atomic_write(path, text):
    staged = path.with_suffix(path.suffix + '.pending')
    staged.write_text(text, encoding='utf-8')
    os.replace(staged, path)

def js_value(name, obj):
    return f'window.{name} = ' + json.dumps(obj, ensure_ascii=False, indent=2) + ';\n'

def escape(value):
    return html.escape(str(value), quote=True)

def links(ep, seconds, label):
    yt = ep['youtubeUrl'] + f'&t={int(seconds)}s'
    # No-Rant and dubbed versions may have different edit timelines.
    return f'<span class="dual-jump"><a class="time-pill yt-pill" href="{escape(yt)}" target="_blank" rel="noopener">YT [{escape(label)}] ↗</a><a class="time-pill bili-pill" href="{escape(ep["biliUrl"])}" target="_blank" rel="noopener">B站本集（时间未对齐）↗</a></span>'

def handbook_sections():
    text = (BASE_DIR / 'ICT_2022_全37讲_图文精读手册.md').read_text()
    sections = {}
    for chunk in re.split(r'(?=^##\s+Ep\.\s*\d+)', text, flags=re.M):
        m = re.match(r'^##\s+Ep\.\s*(\d+)[^\n]*\n(.+)', chunk, flags=re.S)
        if m: sections[int(m[1])] = m[2]
    return sections

def lesson_html(ep, handbook):
    parts = ['<blockquote><b>证据状态：</b>中文解释均为学习整理；只有标为“已核对字幕”的要点已在所列文本核读。图片注解与旧稿需另行复核；不据此自动下单。</blockquote>']
    if ep['keyPoints']:
        parts.append('<h3>已核对字幕的要点（主模型摘要）</h3>')
        for c in ep['keyPoints']:
            parts.append(f'<h4>{escape(c["titleZh"])}</h4>{links(ep,c["seconds"],c["timeStr"])}<p>{escape(c["detailZh"])}</p>')
    else:
        parts.append('<p>本课尚待逐项核读归纳。可以先阅读下方原稿，记录疑问；不把旧稿当标准答案。</p>')
    parts.append('<h3>本集关键帧资料（图注待视觉复核）</h3>')
    for f in ep['keyframes']:
        parts.append(f'<figure class="lesson-figure" data-seconds="{f["seconds"]}"><p>{links(ep,f["seconds"],f["timeStr"])}</p><img src="lesson-assets/{escape(f["file"])}" alt="待复核图注：{escape(f["titleZh"])}"><figcaption>待复核图注：{escape(f["captionZh"])}</figcaption></figure>')
    if ep['ep'] in handbook:
        parts.append('<details><summary>历史中文讲义（待复核资料，含已发现的概念和归因问题）</summary><p>当前训练规则以体系地图为准。以下旧稿保留用于对照，不作为老师原话或执行标准。</p><pre style="white-space:pre-wrap">' + escape(handbook[ep['ep']]) + '</pre></details>')
    parts.append(f'<details class="transcript-details" open><summary>本地 No-Rant 英文字幕（{len(ep["segments"])} 个片段；转写可能有误）</summary><div class="transcript-box">')
    for seg in ep['segments']:
        parts.append(f'<div class="transcript-row">{links(ep,seg["startSec"],seg["range"])}<p>{escape(seg["text"])}</p></div>')
    parts.append('</div></details>')
    return '\n'.join(parts)

def content_fingerprint(lessons, framework, practice):
    content = json.dumps({'lessons':lessons, 'framework':framework, 'practice':practice}, ensure_ascii=False, sort_keys=True).encode()
    return hashlib.sha256(content).hexdigest()


def build_version(lessons, framework, practice):
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=BASE_DIR, stderr=subprocess.DEVNULL, timeout=5).decode().strip()
    try:
        sha = git('rev-parse','HEAD')
        date = git('log','-1','--format=%cI')
        msg = git('log','-1','--format=%s')
        dirty = bool(git('status','--porcelain'))
    except (subprocess.SubprocessError, OSError):
        sha, date, msg, dirty = None, None, '来源版本未知', True
    return {'repo':'Rouen007/ict-2022-study-room','branch':'main','commitFullSha':sha,'commitSha':sha[:7] if sha else 'unknown',
            'commitDate':date,'commitMessage':msg,'dirty':dirty,'contentSHA256':content_fingerprint(lessons, framework, practice),
            'packagedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'version':'2.0.0',
            'lessonCount':len(lessons),'imageCount':sum(l['imageCount'] for l in lessons)}

def framework_markdown(f):
    lines = ['# ICT 2022 学习室条件训练框架 v2', '', '由 framework.json 生成；请修改该 JSON 后重建。', '', f['identity'], '', '## 六阶段', '']
    lines += [f"- **{st['id']} {st['title']}**：{st['question']}" for st in f['chain']]
    lines += ['', '## 十二条训练原则', '']
    for p in f['principles']:
        lines += [f"### {p['id']} {p['title']}（{p['stage']}）", '', p['rule'], '', '常见错误：'+p['trap'], '']
    lines += ['## 当前训练时段', '', '时区：'+f['sessionPolicy']['timeZone'], '新开仓窗口（右端不含）：'+str(f['sessionPolicy']['newEntryWindows']), '撤销未触发计划：'+str(f['sessionPolicy']['cancelPendingAt']), '训练日内持仓结束边界：'+f['sessionPolicy']['trainingFlatBy'], f['sessionPolicy']['source'], '', '## 状态语义', '']
    lines += [f"- `{key}`：{value}" for key,value in f['states'].items()]
    lines += ['', '## 其他概念边界', ''] + ['- '+value for value in f.get('boundaries', [])]
    notes = extension_markdown(f)
    if notes: lines += ['', notes]
    return '\n'.join(lines).rstrip()+'\n'

def main():
    data = read_json(BASE_DIR/'courseData.json')
    framework = read_json(BASE_DIR/'references/framework.json')
    framework['extensions'] = compile_extensions(framework)
    course = read_json(BASE_DIR/'references/practice.json')
    handbook = handbook_sections()
    episodes = data['episodes']
    if len(episodes) != 37 or any(not e['segments'] for e in episodes): raise ValueError('Need 37 nonempty transcripts')
    lessons, distilled = [], {}
    for e in episodes:
        if not re.fullmatch(r'[A-Za-z0-9_-]{11}',e['videoId']): raise ValueError('Invalid video ID')
        for f in e['keyframes']:
            if not (STUDY_DIR/'lesson-assets'/f['file']).is_file(): raise ValueError(f'Missing frame {f["file"]}')
        current_segments = validate_evidence_claims(e['keyPoints'], BASE_DIR/e['sourcePath'], BASE_DIR)
        if current_segments != e['segments']: raise ValueError('Transcript metadata stale; regenerate courseData.json')
        cases = []
        for c in e['keyPoints']:
            by_id = {f['frameId']: f for f in e['keyframes']}
            if any(fid not in by_id for fid in c['frameIds']): raise ValueError('Unknown explicit frame ID')
            figures = [{'src':'lesson-assets/'+by_id[fid]['file'],'caption':'图注待复核：'+by_id[fid]['captionZh']} for fid in c['frameIds']]
            cases.append({'title':f'[{c["timeStr"]}] {c["titleZh"]}','gist':c['detailZh'],
                          'scene':f'已核对本地 No-Rant Ep.{e["ep"]:02d} [{c["timeStr"]}] 字幕；摘要不等于逐字引文。',
                          'figures':figures,'read':[{'who':'主模型核读摘要','text':c['detailZh']}],
                          'principles':[], 'evidenceId':c['id'], 'sourceSHA256':c['sourceSHA256']})
        distilled[f'ep{e["ep"]:02d}'] = {'status':e['evidenceStatus'],'core':e['summaryZh'],'cases':cases,
              'gaps':'其余中文推演、图注和跨平台时间偏移待核验。','drill':'指出原稿中的观察事实、作者解释、你的推断和可能反例；证据不足时保持待核验。'}
        lessons.append({'id':f'ep{e["ep"]:02d}','ep':e['ep'],'date':f'Ep.{e["ep"]:02d}',
            'duration':f'字幕至 {e["durationSec"]//60:02d}:{e["durationSec"]%60:02d}',
            'title':f'Ep.{e["ep"]:02d}｜{e["titleZh"]}','titleEn':e['titleEn'],'module':e['module'],
            'topics':[e['module']], 'imageCount':len(e['keyframes']),'hasLocalVideo':False,'localVideoUrl':None,
            'videoId':e['videoId'],'biliUrl':e['biliUrl'],'youtubeUrl':e['youtubeUrl'],
            'keyframes':e['keyframes'],'keyPoints':e['keyPoints'],'preview':e['summaryZh'],
            'searchText':' '.join(s['text'] for s in e['segments']), 'sourcePath':e['sourcePath'],
            'evidenceStatus':e['evidenceStatus'],'html':lesson_html(e,handbook)})
    version = build_version(lessons, framework, course)
    library = {'schema':'ang-learning-library','packagedAt':version['packagedAt'],'versionInfo':version,
               'dayCount':37,'imageCount':version['imageCount'],'latestDate':'Ep.01–Ep.37','lessons':lessons,'glossary':data['glossary']}
    distill = {'schema':'ict-2022-distill','version':2,'framework':framework,'lessons':distilled,
               'coverage':{'sourceLessons':37,'partiallyChecked':sum(bool(e['keyPoints']) for e in episodes)},'principleCases':{}}
    outputs = {'distill-data.js':js_value('LESSON_DISTILL',distill), 'library-data.js':js_value('ANG_LIBRARY',library),
               'course.js':js_value('STUDY_COURSE',course),'version.js':js_value('ANG_VERSION',version),
               'version.json':json.dumps(version,ensure_ascii=False,indent=2)+'\n'}
    # Validate all content before publishing any generated asset. No notebook or video writes.
    for name, content in outputs.items(): atomic_write(STUDY_DIR/name,content)
    atomic_write(BASE_DIR/'references/framework.md', framework_markdown(framework))
    print(f'Built 37 lessons; {version["imageCount"]} frames; {distill["coverage"]["partiallyChecked"]} lessons with checked transcript excerpts')

if __name__ == '__main__': main()
