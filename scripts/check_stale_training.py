#!/usr/bin/env python3
"""Watchdog: detect stale or crashed PPO training runs.
Runs every 15 minutes via crontab. Logs to results/stale_training.log.
"""
import glob
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

STALE_THRESHOLD_MINUTES = 60
LOG_PATH = Path("results/stale_training.log")
CHECKPOINTS_DIR = Path("data/checkpoints")


def get_training_pids():
    """Return list of PIDs running train_ppo.py."""
    try:
        out = subprocess.check_output(["pgrep", "-f", "train_ppo.py"], text=True, timeout=5)
        return [int(p) for p in out.strip().splitlines() if p.strip()]
    except subprocess.CalledProcessError:
        return []
    except Exception:
        return []


def find_newest_checkpoint(league_dir: Path):
    """Return (path, mtime_seconds) of the newest .pt file in league_dir, or (None, 0)."""
    latest_txt = league_dir / "latest_checkpoint.txt"
    if latest_txt.exists():
        try:
            ckpt = Path(latest_txt.read_text().strip())
            if ckpt.exists():
                return ckpt, ckpt.stat().st_mtime
        except Exception:
            pass
    pts = list(league_dir.glob("ppo_iter*.pt"))
    if not pts:
        return None, 0
    newest = max(pts, key=lambda p: p.stat().st_mtime)
    return newest, newest.stat().st_mtime


def main():
    os.chdir(Path(__file__).parent.parent)  # ensure we're at project root
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    now = time.time()
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    pids = get_training_pids()
    league_dirs = sorted(CHECKPOINTS_DIR.glob("ppo_*_league"))

    lines = []

    if not pids:
        lines.append(f"{now_str} INFO no training process running")
        # Check for interrupted runs (no .training_complete but has checkpoints)
        for ld in league_dirs:
            if not (ld / ".training_complete").exists():
                ckpt, mtime = find_newest_checkpoint(ld)
                if ckpt and (now - mtime) < 3600 * 24:  # checkpoint < 24h old
                    age_h = (now - mtime) / 3600
                    lines.append(f"{now_str} WARN {ld.name}: no .training_complete, last ckpt {age_h:.1f}h ago — may be interrupted")
    else:
        lines.append(f"{now_str} INFO training running PIDs={pids}")
        # Check freshness of checkpoints for running runs
        for ld in league_dirs:
            if (ld / ".training_complete").exists():
                continue  # already done
            ckpt, mtime = find_newest_checkpoint(ld)
            if ckpt is None:
                continue
            age_min = (now - mtime) / 60
            if age_min > STALE_THRESHOLD_MINUTES:
                lines.append(
                    f"{now_str} WARN {ld.name}: last checkpoint {age_min:.0f}min ago (threshold={STALE_THRESHOLD_MINUTES}min) — STALE"
                )
            else:
                lines.append(f"{now_str} INFO {ld.name}: last checkpoint {age_min:.0f}min ago — OK")

    with open(LOG_PATH, "a") as f:
        for line in lines:
            f.write(line + "\n")

    # Print to stdout (for cron email / manual runs)
    for line in lines:
        print(line)

    # Exit 1 if any WARN lines (useful for monitoring hooks)
    if any("WARN" in l for l in lines):
        sys.exit(1)


if __name__ == "__main__":
    main()
