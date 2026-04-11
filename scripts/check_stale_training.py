#!/usr/bin/env python3
"""Cron watchdog: detect stale/hung PPO training runs.

Checks every PPO league directory for a latest_checkpoint.txt that hasn't
been updated in >45 minutes while a training process is still running.
Logs an alert to results/stale_training_alerts.log.

Recommended crontab entry (run every 15 minutes):
  */15 * * * * uv run python /home/dkord/code/twilight-struggle-ai/scripts/check_stale_training.py >> /home/dkord/code/twilight-struggle-ai/results/logs/stale_training_alerts.log 2>&1
"""
import glob
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).parent.parent
STALE_THRESHOLD_SECONDS = 45 * 60  # 45 minutes


def get_running_ppo_pids() -> dict[str, int]:
    """Map version name -> PID for running train_ppo.py processes."""
    result = {}
    try:
        out = subprocess.check_output(
            ["pgrep", "-a", "-f", "train_ppo.py"], text=True, timeout=5
        )
        for line in out.strip().splitlines():
            parts = line.split(None, 1)
            if len(parts) < 2:
                continue
            pid = int(parts[0])
            cmd = parts[1]
            # Extract --out-dir or --checkpoint path to get version name
            for token in cmd.split():
                if "ppo_v" in token:
                    # e.g. data/checkpoints/ppo_v65_league → v65
                    import re
                    m = re.search(r"ppo_(v\d+)", token)
                    if m:
                        result[m.group(1)] = pid
                        break
    except subprocess.CalledProcessError:
        pass  # no processes found
    except Exception as e:
        print(f"[check_stale] pgrep error: {e}", file=sys.stderr)
    return result


def check_stale():
    now = time.time()
    running = get_running_ppo_pids()
    alerts = []

    league_dirs = sorted(REPO.glob("data/checkpoints/ppo_v*_league"))
    for league_dir in league_dirs:
        pointer = league_dir / "latest_checkpoint.txt"
        if not pointer.exists():
            continue

        version = league_dir.name.replace("data/checkpoints/ppo_", "").replace("_league", "")
        if version not in running:
            continue  # not running, nothing to check

        mtime = pointer.stat().st_mtime
        age = now - mtime
        if age > STALE_THRESHOLD_SECONDS:
            alerts.append(
                f"STALE: {version} PID={running[version]} "
                f"last_checkpoint={age/60:.0f}min ago "
                f"({pointer})"
            )

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if alerts:
        for a in alerts:
            print(f"[{ts}] {a}")
    else:
        # Silent on clean check (don't fill log)
        pass


if __name__ == "__main__":
    check_stale()
