#!/usr/bin/env python3
"""
OOM Watchdog — monitors GPU memory and kills the training process if OOM is imminent.

Usage:
    uv run python scripts/oom_watchdog.py --pid PID [--threshold 0.95] [--interval 30] [--log results/oom_watchdog.log]

Arguments:
    --pid         PID of the training process to watch (required)
    --threshold   GPU memory fraction that triggers warning/kill (default: 0.95)
    --interval    Check interval in seconds (default: 30)
    --kill        If set, SIGKILL the training process when threshold exceeded (default: warn only)
    --log         Log file path (default: results/oom_watchdog.log)
"""

import argparse
import os
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


def get_gpu_memory_fraction() -> float:
    """Return current GPU memory usage fraction (used / total). Returns 0.0 on error."""
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used,memory.total",
             "--format=csv,noheader,nounits"],
            text=True, timeout=5
        ).strip().split("\n")[0]
        used, total = (int(x.strip()) for x in out.split(","))
        return used / total if total > 0 else 0.0
    except Exception:
        return 0.0


def get_gpu_memory_mb() -> tuple[int, int]:
    """Return (used_mb, total_mb). Returns (0, 0) on error."""
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used,memory.total",
             "--format=csv,noheader,nounits"],
            text=True, timeout=5
        ).strip().split("\n")[0]
        used, total = (int(x.strip()) for x in out.split(","))
        return used, total
    except Exception:
        return 0, 0


def pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True  # exists but we can't signal it


def log(msg: str, log_path: Path) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(log_path, "a") as f:
        f.write(line + "\n")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--pid", type=int, required=True)
    p.add_argument("--threshold", type=float, default=0.95)
    p.add_argument("--interval", type=int, default=30)
    p.add_argument("--kill", action="store_true")
    p.add_argument("--log", default="results/oom_watchdog.log")
    args = p.parse_args()

    log_path = Path(args.log)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    log(f"OOM watchdog started. Watching PID {args.pid}, threshold={args.threshold:.0%}, interval={args.interval}s", log_path)

    consecutive_high = 0
    while True:
        if not pid_alive(args.pid):
            log(f"PID {args.pid} is no longer alive. Watchdog exiting.", log_path)
            break

        frac = get_gpu_memory_fraction()
        used_mb, total_mb = get_gpu_memory_mb()
        msg = f"GPU memory: {used_mb}/{total_mb} MB ({frac:.1%})"

        if frac >= args.threshold:
            consecutive_high += 1
            log(f"WARNING [{consecutive_high}x] {msg} >= threshold {args.threshold:.0%}", log_path)
            if consecutive_high >= 3:
                log(f"CRITICAL: GPU memory at {frac:.1%} for 3+ consecutive checks.", log_path)
                if args.kill:
                    log(f"Sending SIGTERM to PID {args.pid}", log_path)
                    try:
                        os.kill(args.pid, signal.SIGTERM)
                    except ProcessLookupError:
                        pass
                else:
                    log("Pass --kill to terminate the process automatically.", log_path)
        else:
            if consecutive_high > 0:
                log(f"GPU memory recovered: {msg}", log_path)
            consecutive_high = 0
            # Only log occasionally when healthy
            if int(time.time()) % 300 < args.interval:  # ~every 5 min
                log(f"OK: {msg}", log_path)

        time.sleep(args.interval)


if __name__ == "__main__":
    main()
