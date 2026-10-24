#!/usr/bin/env python3
import glob
import json
import os
import re

SUB_DIR = "/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/subs"
OUT_DIR = "/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/transcripts"
os.makedirs(OUT_DIR, exist_ok=True)


def parse_vtt(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()

    segments = []
    cur_start = None
    cur_text = []

    for line in lines:
        if "-->" in line:
            m = re.match(r"(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->", line)
            if m:
                if cur_start and cur_text:
                    txt = " ".join(cur_text).strip()
                    if txt:
                        segments.append((cur_start, txt))
                cur_start = m.group(1)[:8]  # HH:MM:SS
                cur_text = []
        elif (
            line.startswith("WEBVTT")
            or line.startswith("Kind:")
            or line.startswith("Language:")
            or not line.strip()
        ):
            continue
        else:
            clean = re.sub(r"<[^>]+>", "", line).strip()
            clean = clean.replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"')
            if clean:
                cur_text.append(clean)

    if cur_start and cur_text:
        txt = " ".join(cur_text).strip()
        if txt:
            segments.append((cur_start, txt))

    # Deduplicate rolling captions from YouTube auto-subs
    deduped = []
    seen_lines = []
    for ts, txt in segments:
        if not seen_lines or txt != seen_lines[-1]:
            # Check if txt is just a prefix/suffix duplicate
            if seen_lines and txt.startswith(seen_lines[-1]):
                new_part = txt[len(seen_lines[-1]) :].strip()
                if new_part:
                    deduped.append((ts, new_part))
                seen_lines.append(txt)
            elif seen_lines and seen_lines[-1].endswith(txt):
                continue
            else:
                deduped.append((ts, txt))
                seen_lines.append(txt)

    # Group into ~60-second paragraphs for readable timestamped indexing
    grouped = []
    bucket_ts = None
    bucket_words = []
    last_sec = -999

    for ts, txt in deduped:
        h, m, s = map(int, ts.split(":"))
        sec = h * 3600 + m * 60 + s
        if bucket_ts is None:
            bucket_ts = f"{m + h*60:02d}:{s:02d}"
            last_sec = sec
        elif sec - last_sec >= 60:
            grouped.append((bucket_ts, " ".join(bucket_words)))
            bucket_ts = f"{m + h*60:02d}:{s:02d}"
            bucket_words = []
            last_sec = sec
        bucket_words.append(txt)

    if bucket_ts and bucket_words:
        grouped.append((bucket_ts, " ".join(bucket_words)))

    return grouped


def main():
    vtt_files = sorted(glob.glob(os.path.join(SUB_DIR, "*.vtt")))
    print(f"Found {len(vtt_files)} VTT files")
    all_summary = []
    for vf in vtt_files:
        base = os.path.basename(vf).replace(".en.vtt", "")
        grouped = parse_vtt(vf)
        out_path = os.path.join(OUT_DIR, f"{base}.md")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(f"# {base}\n\n")
            for ts, paragraph in grouped:
                out.write(f"**[{ts}]** {paragraph}\n\n")
        total_words = sum(len(p.split()) for _, p in grouped)
        all_summary.append({"episode": base, "paragraphs": len(grouped), "words": total_words})
    with open(os.path.join(OUT_DIR, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(all_summary, f, indent=2, ensure_ascii=False)
    print("Done parsing all transcripts.")


if __name__ == "__main__":
    main()
