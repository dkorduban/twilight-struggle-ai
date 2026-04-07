# Spec: Policy Statistics Collection + OOM Watchdog

## Goal
Two independent additions:
1. **Policy statistics** logged to W&B during PPO benchmarks — phase-tagged mode/country/allocation stats
2. **OOM watchdog script** — monitors GPU memory and kills the training process if OOM is imminent

---

## Part 1: Policy Statistics in `scripts/train_ppo.py`

### Context
- `train_ppo.py` already imports `tscore`, `torch`, `wandb`, `csv`, `collections`
- `run_benchmark()` at line ~846 calls `tscore.benchmark_batched()` and returns a dict
- `collect_rollout_batched()` at line ~515 calls `tscore.rollout_games_batched()` and returns steps with per-step dicts containing: `scalars` (11,), `mode_idx` (int), `country_targets` (list[int]), `side_int` (int)
- Scalars layout (from `extract_features()` at line ~105):
  - `scalars[0]` = vp / 20.0
  - `scalars[1]` = (defcon - 1) / 4.0
  - `scalars[8]` = turn / 10.0
- `mode_idx` values: 0=Influence, 1=Event, 2=Space, 3=Coup, 4=Realign
- `country_targets` for Influence mode: sorted list of country_id ints (may repeat if multiple ops to same country, e.g. 3 ops to France → [7, 7, 7])

### Add: `_load_country_region_map()` helper (near top of file, after imports)

```python
def _load_country_region_map() -> dict[int, str]:
    """Load country_id -> region string from data/spec/countries.csv."""
    import csv as _csv
    csv_path = Path(__file__).parent.parent / "data" / "spec" / "countries.csv"
    mapping: dict[int, str] = {}
    try:
        with open(csv_path) as f:
            for row in _csv.DictReader(r for r in f if not r.startswith("#")):
                mapping[int(row["country_id"])] = row["region"]
    except Exception:
        pass
    return mapping

_COUNTRY_REGION: dict[int, str] = {}  # lazy-loaded once
```

### Add: `collect_policy_stats()` function (near `run_benchmark`)

```python
def collect_policy_stats(
    script_path: str,
    n_games: int = 100,
    seed_base: int = 51000,
) -> dict:
    """
    Run a small rollout batch and compute per-phase policy statistics.
    Returns a flat dict of W&B-loggable scalars.

    Phase labels: early=turns 1-3, mid=turns 4-7, late=turns 8-10.
    Mode names: Influence, Event, Space, Coup, Realign.
    """
    global _COUNTRY_REGION
    if not _COUNTRY_REGION:
        _COUNTRY_REGION = _load_country_region_map()

    MODE_NAMES = ["Influence", "Event", "Space", "Coup", "Realign"]
    REGIONS = ["Europe", "Asia", "Middle East", "Africa", "Central America", "South America"]
    PHASES = ["early", "mid", "late"]

    def phase(turn: int) -> str:
        if turn <= 3:
            return "early"
        if turn <= 7:
            return "mid"
        return "late"

    def influence_split_label(targets: list[int]) -> str:
        """Classify allocation as concentrated / split / dispersed."""
        if not targets:
            return "none"
        from collections import Counter
        counts = sorted(Counter(targets).values(), reverse=True)
        total = sum(counts)
        if counts[0] == total:
            return "concentrated"   # all ops to one country
        if counts[0] == 1:
            return "dispersed"      # at most 1 op per country
        return "split"              # mixed

    # Collect steps for both sides
    all_step_dicts: list[dict] = []
    for side in [tscore.Side.USSR, tscore.Side.US]:
        try:
            _, steps, _ = tscore.rollout_games_batched(
                model_path=script_path,
                learned_side=side,
                n_games=n_games,
                pool_size=min(n_games, 32),
                seed=seed_base + (0 if side == tscore.Side.USSR else n_games),
                device="cpu",
                temperature=0.0,   # greedy — reproducible stats
                nash_temperatures=True,
            )
            for s in steps:
                s["_side_name"] = "ussr" if side == tscore.Side.USSR else "us"
            all_step_dicts.extend(steps)
        except Exception as e:
            print(f"  [stats] rollout failed for {side}: {e}", flush=True)
            return {}

    # Aggregate
    from collections import defaultdict
    mode_counts: dict[tuple, int] = defaultdict(int)       # (phase, side, mode_name)
    region_counts: dict[tuple, int] = defaultdict(int)     # (phase, side, region)
    split_counts: dict[tuple, int] = defaultdict(int)      # (phase, side, split_label)
    total_counts: dict[tuple, int] = defaultdict(int)      # (phase, side)
    inf_counts: dict[tuple, int] = defaultdict(int)        # (phase, side) influence-only total
    defcon_sum: dict[tuple, float] = defaultdict(float)
    vp_sum: dict[tuple, float] = defaultdict(float)

    for s in all_step_dicts:
        scalars = s["scalars"]           # numpy (11,)
        turn = round(float(scalars[8]) * 10)
        defcon = round(float(scalars[1]) * 4 + 1)
        vp = round(float(scalars[0]) * 20)
        mode_idx = int(s["mode_idx"])
        targets = list(s["country_targets"])
        side_name = s["_side_name"]
        ph = phase(turn)
        key = (ph, side_name)

        mode_name = MODE_NAMES[mode_idx] if 0 <= mode_idx < len(MODE_NAMES) else "Unknown"
        mode_counts[(ph, side_name, mode_name)] += 1
        total_counts[key] += 1
        defcon_sum[key] += defcon
        vp_sum[key] += vp

        if mode_idx == 0 and targets:  # Influence
            # Region of first (top) target
            region = _COUNTRY_REGION.get(targets[0], "Unknown")
            region_counts[(ph, side_name, region)] += 1
            split_counts[(ph, side_name, influence_split_label(targets))] += 1
            inf_counts[key] += 1

    # Build flat W&B dict
    stats: dict[str, float] = {}
    for ph in PHASES:
        for side_name in ["ussr", "us"]:
            key = (ph, side_name)
            n = total_counts[key]
            if n == 0:
                continue
            prefix = f"stats/{ph}/{side_name}"
            # Mode fractions
            for mn in MODE_NAMES:
                stats[f"{prefix}/mode_{mn.lower()}_frac"] = mode_counts[(ph, side_name, mn)] / n
            # Mean defcon and vp
            stats[f"{prefix}/mean_defcon"] = defcon_sum[key] / n
            stats[f"{prefix}/mean_vp"] = vp_sum[key] / n
            # Influence sub-stats
            n_inf = inf_counts[key]
            if n_inf > 0:
                for r in REGIONS:
                    stats[f"{prefix}/region_{r.lower().replace(' ', '_')}_frac"] = (
                        region_counts[(ph, side_name, r)] / n_inf
                    )
                for label in ["concentrated", "split", "dispersed"]:
                    stats[f"{prefix}/split_{label}_frac"] = split_counts[(ph, side_name, label)] / n_inf
    return stats
```

### Modify: `run_benchmark()` to optionally collect stats

Change signature to:
```python
def run_benchmark(
    checkpoint_path: str,
    n_games: int = 500,
    seed_base: int = 50000,
    collect_stats: bool = False,
    stats_n_games: int = 100,
) -> dict[str, float]:
```

After computing ussr_wr/us_wr/combined, if `collect_stats=True`:
```python
    if collect_stats:
        try:
            script_path = checkpoint_path.replace(".pt", "_scripted.pt")
            if os.path.exists(script_path):
                result["policy_stats"] = collect_policy_stats(
                    script_path, n_games=stats_n_games, seed_base=seed_base + 10000
                )
        except Exception as e:
            print(f"  [stats] policy stats failed: {e}", flush=True)
    return result
```

### Modify: benchmark call sites in the training loop

In the main training loop where `run_benchmark` is called and results logged to W&B:
- Pass `collect_stats=True` and `stats_n_games=100`
- After getting benchmark results, log `policy_stats` dict to W&B:
  ```python
  if "policy_stats" in bench and wandb_run and bench["policy_stats"]:
      wandb_run.log(bench["policy_stats"], step=iteration)
  ```

Find the benchmark call in the main loop (around line ~1050, inside `if iteration % args.benchmark_every == 0:`).

---

## Part 2: OOM Watchdog — `scripts/oom_watchdog.py`

Standalone script, runnable in background. Monitors GPU memory and the training process.

```python
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
```

---

## Acceptance criteria

1. `collect_policy_stats()` runs without error on the PPO checkpoint at `data/checkpoints/ppo_v1_from_v106/ppo_best_scripted.pt`
2. Returns a dict with keys like `stats/early/ussr/mode_influence_frac`, `stats/mid/us/split_concentrated_frac`, etc.
3. All values are floats in [0, 1] (fractions) or reasonable ranges (mean_defcon 1-5, mean_vp -20 to +20)
4. `run_benchmark()` with `collect_stats=True` returns a dict that includes `policy_stats` key
5. `oom_watchdog.py --pid 99999 --interval 1` runs for 2 seconds and exits cleanly with "no longer alive" message (PID 99999 likely doesn't exist)
6. No regressions to existing PPO training loop behavior
