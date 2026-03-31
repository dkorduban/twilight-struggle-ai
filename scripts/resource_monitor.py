"""Background resource monitor — logs CPU and GPU utilization every N seconds.

Designed to run as a background process alongside pipeline phases.
Writes timestamped lines to a log file; prints phase markers.

Usage (from pipeline script):
    python scripts/resource_monitor.py --out /tmp/monitor_vN.log --interval 5 &
    MONITOR_PID=$!
    python scripts/resource_monitor.py --tag "benchmark" --pid $MONITOR_PID  # mark phase start
    ... run benchmark ...
    python scripts/resource_monitor.py --tag "collect" --pid $MONITOR_PID    # next phase
    kill $MONITOR_PID                                                          # stop at end

Or standalone:
    uv run python scripts/resource_monitor.py --out /tmp/monitor.log --interval 5

Log format:
    2026-03-30T18:15:03 [benchmark] cpu=42.1% gpu_util=0% gpu_mem=1823/4096MB vram_pct=44.5%
"""
from __future__ import annotations

import argparse
import os
import signal
import subprocess
import sys
import time
from datetime import datetime


def gpu_stats() -> dict:
    """Query nvidia-smi for GPU utilization and memory."""
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used,memory.total",
             "--format=csv,noheader,nounits"],
            stderr=subprocess.DEVNULL, timeout=3,
        ).decode().strip()
        parts = out.split(",")
        util = float(parts[0].strip())
        mem_used = int(parts[1].strip())
        mem_total = int(parts[2].strip())
        return {"gpu_util": util, "mem_used": mem_used, "mem_total": mem_total}
    except Exception:
        return {"gpu_util": -1, "mem_used": -1, "mem_total": -1}


def cpu_percent() -> float:
    """Cheap /proc/stat-based CPU usage over a 0.1s window."""
    def read_cpu():
        with open("/proc/stat") as f:
            line = f.readline()
        vals = list(map(int, line.split()[1:]))
        idle = vals[3]
        total = sum(vals)
        return idle, total

    idle1, total1 = read_cpu()
    time.sleep(0.1)
    idle2, total2 = read_cpu()
    delta_total = total2 - total1
    delta_idle = idle2 - idle1
    if delta_total == 0:
        return 0.0
    return 100.0 * (1.0 - delta_idle / delta_total)


def monitor_loop(out_path: str, interval: float, phase: list[str]) -> None:
    with open(out_path, "a", buffering=1) as fh:
        fh.write(f"# Monitor started at {datetime.now().isoformat()}\n")
        fh.flush()
        while True:
            ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            cpu = cpu_percent()
            gpu = gpu_stats()
            tag = phase[0]
            if gpu["mem_total"] > 0:
                vram_pct = 100.0 * gpu["mem_used"] / gpu["mem_total"]
                line = (
                    f"{ts} [{tag}] cpu={cpu:.1f}%"
                    f" gpu_util={gpu['gpu_util']:.0f}%"
                    f" gpu_mem={gpu['mem_used']}/{gpu['mem_total']}MB"
                    f" vram_pct={vram_pct:.1f}%\n"
                )
            else:
                line = f"{ts} [{tag}] cpu={cpu:.1f}% gpu=unavailable\n"
            fh.write(line)
            sys.stdout.write(line)
            sys.stdout.flush()
            time.sleep(max(0, interval - 0.1))


def send_tag(pid: int, tag: str, out_path: str) -> None:
    """Write a phase-change marker into an existing monitor log."""
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    with open(out_path, "a", buffering=1) as fh:
        fh.write(f"# {ts} PHASE={tag}\n")
    # Signal monitor to update its phase label via SIGUSR1 trick isn't portable;
    # instead the tag is written to a sidecar file the monitor reads each loop.
    tag_file = out_path + ".phase"
    with open(tag_file, "w") as f:
        f.write(tag)
    print(f"[monitor] phase -> {tag}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/tmp/resource_monitor.log")
    ap.add_argument("--interval", type=float, default=5.0)
    ap.add_argument("--tag", default="",
                    help="If set, write a phase marker to --out and exit (don't start monitor)")
    ap.add_argument("--pid", type=int, default=0,
                    help="PID of running monitor (used with --tag)")
    args = ap.parse_args()

    if args.tag:
        send_tag(args.pid, args.tag, args.out)
        return

    # Monitor loop — reads phase from sidecar file if it exists
    phase = ["init"]
    tag_file = args.out + ".phase"

    def _refresh_phase():
        if os.path.exists(tag_file):
            try:
                t = open(tag_file).read().strip()
                if t:
                    phase[0] = t
            except Exception:
                pass

    with open(args.out, "a", buffering=1) as fh:
        fh.write(f"# Monitor started at {datetime.now().isoformat()}\n")
        fh.flush()
        while True:
            _refresh_phase()
            ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            cpu = cpu_percent()
            gpu = gpu_stats()
            tag = phase[0]
            if gpu["mem_total"] > 0:
                vram_pct = 100.0 * gpu["mem_used"] / gpu["mem_total"]
                line = (
                    f"{ts} [{tag}] cpu={cpu:.1f}%"
                    f" gpu_util={gpu['gpu_util']:.0f}%"
                    f" gpu_mem={gpu['mem_used']}/{gpu['mem_total']}MB"
                    f" vram_pct={vram_pct:.1f}%\n"
                )
            else:
                line = f"{ts} [{tag}] cpu={cpu:.1f}% gpu=unavailable\n"
            fh.write(line)
            time.sleep(max(0, args.interval - 0.1))


if __name__ == "__main__":
    main()
