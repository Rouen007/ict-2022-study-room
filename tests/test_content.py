import hashlib
import json
from pathlib import Path
import sys
import unittest
import copy
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from transcript_io import parse_transcript_file, transcript_identity, validate_evidence_claims
ROOT = Path(__file__).resolve().parents[1]

class ContentTests(unittest.TestCase):
    def test_all_transcripts_and_ids(self):
        files = list((ROOT/'transcripts').glob('[0-9][0-9]_*.md'))
        self.assertEqual(len(files), 37)
        total = 0
        for p in files:
            ep, video, title = transcript_identity(p)
            self.assertEqual(len(video), 11)
            _, segments = parse_transcript_file(p)
            self.assertGreater(len(segments), 0)
            total += len(segments)
        self.assertGreater(total, 300)
        p = next((ROOT/'transcripts').glob('37_*.md'))
        self.assertEqual(transcript_identity(p)[1], 'FzejekE_XoM')

    def test_evidence_and_frame_links(self):
        data = json.loads((ROOT/'courseData.json').read_text())
        self.assertEqual(sum(len(e['keyframes']) for e in data['episodes']), 62)
        for e in data['episodes']:
            self.assertTrue(e['segments'])
            for f in e['keyframes']:
                self.assertTrue((ROOT/'study-room/lesson-assets'/f['file']).is_file())
            for claim in e['keyPoints']:
                raw = (ROOT/claim['sourcePath']).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), claim['sourceSHA256'])
                self.assertTrue(any(s['startSec'] == claim['seconds'] and s['text'] == claim['sourceExcerpt'] for s in e['segments']))
                self.assertTrue(set(claim['frameIds']) <= {f['frameId'] for f in e['keyframes']})

    def test_practice_risk_and_policy(self):
        rules=json.loads((ROOT/'references/framework.json').read_text())
        practice=json.loads((ROOT/'references/practice.json').read_text())
        self.assertEqual(practice['policyVersion'], rules['sessionPolicy']['id'])
        self.assertEqual([s['id'] for s in rules['chain']], [f'S{i}' for i in range(1,7)])
        self.assertTrue(all(p['stage'] in {s['id'] for s in rules['chain']} for p in rules['principles']))
        self.assertEqual((14735 + 14855) / 2, 14795)
        self.assertGreater(14798, 14795)
        self.assertEqual((14856 - 14798) * 5, 290)
        self.assertEqual(len(practice['batches']), 6)
        self.assertEqual(sum(len(b['questions']) for b in practice['batches']), 18)
        self.assertTrue(all(q['sourceType']=='synthetic' for b in practice['batches'] for q in b['questions']))

    def test_false_evidence_fails_even_with_unchanged_file_hash(self):
        evidence = json.loads((ROOT/'references/lesson-evidence.json').read_text())['claims']['3']
        source = ROOT/evidence[0]['sourcePath']
        validate_evidence_claims(evidence, source, ROOT)
        for field, value in [('seconds', 999999), ('sourceExcerpt', 'unrelated statement'), ('sourcePath', 'transcripts/other.md'), ('timeStr', '00:00')]:
            wrong = copy.deepcopy(evidence)
            wrong[0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_evidence_claims(wrong, source, ROOT)

    def test_optional_macro_intersections_preserve_entry_policy(self):
        from framework_extensions import compile_extensions
        framework = json.loads((ROOT/'references/framework.json').read_text())
        original = copy.deepcopy(framework['sessionPolicy'])
        macros = compile_extensions(framework)['macros']
        by_time = {m['time']:m for m in macros}
        self.assertEqual(by_time['11:50–12:10']['entryIntersections'], [['11:50','12:00']])
        self.assertEqual(by_time['11:50–12:10']['outsideEntryWindows'], [['12:00','12:10']])
        self.assertEqual(by_time['13:15–13:45']['entryIntersections'], [['13:30','13:45']])
        self.assertEqual(by_time['15:15–15:45']['entryIntersections'], [['15:15','15:30']])
        self.assertEqual(by_time['08:50–09:10']['durationMinutes'],20)
        self.assertEqual(by_time['13:15–13:45']['durationMinutes'],30)
        self.assertEqual(framework['sessionPolicy'],original)
        wrong=copy.deepcopy(framework)
        wrong['macroWindows'][0]['evidenceStatus']='verified'
        with self.assertRaises(ValueError): compile_extensions(wrong)
        wrong=copy.deepcopy(framework)
        wrong['macroWindows'][0]['time']='25:50–26:10'
        with self.assertRaises(ValueError): compile_extensions(wrong)

    def test_content_version_changes_when_extension_notes_change(self):
        from build_study_room import content_fingerprint
        a=content_fingerprint([],{'macroWindows':[]},{})
        b=content_fingerprint([],{'macroWindows':[{'time':'08:50–09:10'}]},{})
        self.assertNotEqual(a,b)

    def test_html_escapes_external_material(self):
        from build_study_room import escape
        self.assertNotIn('<script>', escape('<script>window.x=1</script>'))

    def test_comparative_perspective_integrity(self):
        from framework_extensions import compile_extensions
        framework = json.loads((ROOT/'references/framework.json').read_text())
        ext = compile_extensions(framework)
        self.assertIn('comparative', ext)
        comps = ext['comparative']
        self.assertEqual(len(comps), 1)
        twoc = comps[0]
        self.assertEqual(twoc['id'], '2c-trading')
        self.assertIn('外部对比与补充视角', twoc['role'])
        self.assertEqual(len(twoc['keyComparisons']), 5)
        self.assertEqual(len(twoc['tenBlacklistRules']), 10)
        sop = twoc['threeCandleMicroChannelSop']
        self.assertGreaterEqual(len(sop['steps']), 5)
        for kf in sop['keyframeShowcase']:
            img_path = ROOT/'study-room/comparative-assets/2c'/kf['file']
            self.assertTrue(img_path.is_file(), f'Missing 2C comparative asset: {kf["file"]}')

if __name__ == '__main__': unittest.main()
