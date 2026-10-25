"""Shared parser for the local No-Rant transcript edition; no filesystem mutation."""
import re
from pathlib import Path


def parse_mmss(value):
    parts = [int(v) for v in value.split(':')]
    if len(parts) not in (2, 3) or any(v < 0 for v in parts) or any(v >= 60 for v in parts[1:]):
        raise ValueError(f'Invalid timestamp: {value}')
    return sum(n * 60 ** i for i, n in enumerate(reversed(parts)))


def parse_transcript_file(filepath):
    text = Path(filepath).read_text(encoding='utf-8')
    title = next((line[2:].strip() for line in text.splitlines() if line.startswith('# ')), '')
    marker = re.compile(r'^\s*(?:\*\*\[(?P<bold>\d{2}:\d{2}(?::\d{2})?)\]\*\*|###\s+\[(?P<header>[^\]]+)\])\s*', re.M)
    matches = list(marker.finditer(text))
    segments = []
    for i, m in enumerate(matches):
        label = m.group('bold') or m.group('header')
        start = label.split('-')[0].strip()
        content = ' '.join(text[m.end():matches[i+1].start() if i+1 < len(matches) else len(text)].split())
        if content:
            segments.append({'range': label, 'startSec': parse_mmss(start), 'text': content})
    if not title or not segments or any(b['startSec'] <= a['startSec'] for a, b in zip(segments, segments[1:])):
        raise ValueError(f'Missing title, empty transcript or non-increasing timestamps: {filepath}')
    return title, segments


def transcript_identity(path):
    match = re.fullmatch(r'(\d{2})_([A-Za-z0-9_-]{11})_(.+)\.md', Path(path).name)
    if not match:
        raise ValueError(f'Invalid episode/video filename: {path}')
    return int(match[1]), match[2], match[3]


def validate_evidence_claims(claims, transcript_path, project_root):
    """A file hash proves a version; each claimed passage must also match that version."""
    import hashlib
    source = Path(transcript_path).resolve()
    root = Path(project_root).resolve()
    _, segments = parse_transcript_file(source)
    by_time = {s['startSec']: s for s in segments}
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    ids = set()
    for claim in claims:
        if (root / claim['sourcePath']).resolve() != source:
            raise ValueError(f'Evidence belongs to another transcript: {claim.get("id")}')
        if claim['sourceSHA256'] != digest:
            raise ValueError(f'Evidence source changed: {source.name}')
        start = claim['seconds']
        if isinstance(start, bool) or not isinstance(start, int) or start not in by_time:
            raise ValueError(f'Evidence timestamp missing: {claim.get("id")}')
        if parse_mmss(claim['timeStr']) != start:
            raise ValueError(f'Evidence timestamp label inconsistent: {claim.get("id")}')
        if claim['sourceExcerpt'] != by_time[start]['text']:
            raise ValueError(f'Evidence excerpt mismatch: {claim.get("id")}')
        if not isinstance(claim['id'], str) or not claim['id'] or claim['id'] in ids:
            raise ValueError('Missing or duplicated evidence ID')
        ids.add(claim['id'])
        if claim.get('status') != 'transcript_checked':
            raise ValueError(f'Unreviewed evidence cannot be promoted: {claim["id"]}')
        frame_ids = claim.get('frameIds')
        if not isinstance(frame_ids, list) or any(not isinstance(fid, str) for fid in frame_ids) or len(frame_ids) != len(set(frame_ids)):
            raise ValueError(f'Invalid frame references: {claim["id"]}')
    return segments
