#!/usr/bin/env python3
import os
import subprocess

VID_DIR = "/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/videos"
ART_DIR = "/Users/rouen/.gemini/antigravity/brain/2f7883a2-405d-4596-a34a-2d0b4894d4c3"
os.makedirs(ART_DIR, exist_ok=True)

FRAMES = [
    # Episode 1
    ("ep01.mp4", "00:00:45", "ep01_tos_live_executions.png"),
    ("ep01.mp4", "00:04:32", "ep01_target_one_big_leg.png"),
    # Episode 2
    ("ep02.mp4", "00:00:55", "ep02_weekly_bias_candle.png"),
    ("ep02.mp4", "00:02:45", "ep02_daily_ssl_and_imbalance.png"),
    ("ep02.mp4", "00:04:50", "ep02_hourly_induce_shorts_run_bsl.png"),
    ("ep02.mp4", "00:07:20", "ep02_15m_equal_highs_stop_hunt.png"),
    ("ep02.mp4", "00:11:18", "ep02_2m_bms_and_fvg_entry.png"),
    ("ep02.mp4", "00:13:20", "ep02_2m_fib_equilibrium_matrix.png"),
    ("ep02.mp4", "00:15:30", "ep02_2m_full_setup_annotated.png"),
    # Episode 3
    ("ep03.mp4", "00:00:50", "ep03_15m_ssl_and_bsl_pools.png"),
    ("ep03.mp4", "00:05:35", "ep03_2m_bullish_mss_fvg_ob.png"),
    ("ep03.mp4", "00:06:55", "ep03_2m_bearish_mss_fvg_targets.png"),
    ("ep03.mp4", "00:09:40", "ep03_1m_orderblock_state_of_delivery.png"),
    ("ep03.mp4", "00:12:05", "ep03_1m_full_lipstick_chart.png"),
    # Episode 4
    ("ep04.mp4", "00:01:25", "ep04_es_2m_equilibrium_overview.png"),
    ("ep04.mp4", "00:02:50", "ep04_es_2m_830_zoomed_journal.png"),
    ("ep04.mp4", "00:05:20", "ep04_nq_5m_wait_for_fvg_entry.png"),
    # Episode 5
    ("ep05.mp4", "00:01:55", "ep05_barchart_open_interest_rollover.png"),
    ("ep05.mp4", "00:04:30", "ep05_15m_daily_range_830_lunch.png"),
    ("ep05.mp4", "00:07:35", "ep05_5m_three_drives_displacement_fvg.png"),
    ("ep05.mp4", "00:13:45", "ep05_5m_pm_session_130_stop_hunt.png"),
]


def main():
    for vid, ts, out_name in FRAMES:
        vid_path = os.path.join(VID_DIR, vid)
        if not os.path.exists(vid_path):
            print(f"Missing {vid_path}")
            continue
        out_path = os.path.join(ART_DIR, out_name)
        cmd = [
            "ffmpeg",
            "-y",
            "-ss",
            ts,
            "-i",
            vid_path,
            "-frames:v",
            "1",
            "-q:v",
            "2",
            out_path,
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"Extracted {out_name}")


if __name__ == "__main__":
    main()
