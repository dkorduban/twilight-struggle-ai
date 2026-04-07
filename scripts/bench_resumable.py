#!/usr/bin/env python3
"""Restartable benchmark runner: wraps tscore.benchmark_batched / benchmark_mcts.

Runs benchmarks in small batches with progress reporting and resume capability.
Job state is saved to a JSON file after each batch; re-run with --job-id to resume.

Seed arithmetic guarantee
--------------------------
C++ assigns game i the seed ``base_seed + i``, so batch k of size B starts at
seed ``base_seed + k*B``.  This makes batched results bit-identical to a single
500-game run — and lets resume skip completed batches without replaying them.

Usage
-----
    uv run python scripts/bench_resumable.py \\
        --checkpoint data/checkpoints/v106_cf_gnn_s42/baseline_best_scripted.pt \\
        --sides both --n-games 500 --seed 50000 --batch-size 50 \\
        --n-sim 0 --pool-size 32 --nash-temperatures \\
        --job-dir results/bench_jobs

Resume an existing job::

    uv run python scripts/bench_resumable.py --job-id a1b2c3d4

"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Ensure build-ninja bindings are importable
# ---------------------------------------------------------------------------
_bindings_dir = str(Path(__file__).resolve().parent.parent / "build-ninja" / "bindings")
if _bindings_dir not in sys.path:
    sys.path.insert(0, _bindings_dir)

import tscore  # noqa: E402

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_SIDE_ENUM = {
    "ussr": tscore.Side.USSR,
    "us": tscore.Side.US,
}

_OTHER_SIDE = {
    "ussr": tscore.Side.US,
    "us": tscore.Side.USSR,
}


def _now_iso() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def _load_job(job_path: Path) -> dict:
    with open(job_path) as f:
        return json.load(f)


def _save_job_atomic(job: dict, job_path: Path) -> None:
    """Write job JSON atomically (write to tmp, then rename)."""
    dir_ = job_path.parent
    dir_.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=dir_, suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(job, f, indent=4)
        os.replace(tmp, job_path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _ensure_scripted(checkpoint: str) -> str:
    """Return a TorchScript path; export if the checkpoint is a raw .pt file."""
    if checkpoint.endswith("_scripted.pt"):
        return checkpoint

    scripted_path = checkpoint.replace(".pt", "_scripted.pt")
    if os.path.exists(scripted_path):
        print(f"[bench] using existing scripted model: {scripted_path}")
        return scripted_path

    export_script = str(
        Path(__file__).resolve().parent.parent / "cpp" / "tools" / "export_baseline_to_torchscript.py"
    )
    print(f"[bench] exporting to TorchScript: {scripted_path}")
    subprocess.run(
        ["uv", "run", "python", export_script, "--checkpoint", checkpoint, "--out", scripted_path],
        check=True,
    )
    return scripted_path


# ---------------------------------------------------------------------------
# Core benchmark call (single batch)
# ---------------------------------------------------------------------------

def _run_batch(
    scripted_path: str,
    side: str,
    n_games: int,
    seed: int,
    n_sim: int,
    pool_size: int,
    nash_temperatures: bool,
    device: str,
) -> list:
    """Call C++ benchmark for one batch; return list[GameResult]."""
    side_enum = _SIDE_ENUM[side]

    if n_sim == 0:
        return tscore.benchmark_batched(
            scripted_path,
            side_enum,
            n_games,
            pool_size=pool_size,
            seed=seed,
            device=device,
            nash_temperatures=nash_temperatures,
        )
    else:
        return tscore.benchmark_mcts(
            scripted_path,
            side_enum,
            n_games,
            n_simulations=n_sim,
            pool_size=pool_size,
            seed=seed,
            device=device,
            nash_temperatures=nash_temperatures,
        )


def _count_results(results: list, side: str) -> tuple[int, int, int]:
    """Return (wins, losses, draws) from list[GameResult]."""
    side_enum = _SIDE_ENUM[side]
    other_enum = _OTHER_SIDE[side]
    wins = sum(1 for r in results if r.winner == side_enum)
    losses = sum(1 for r in results if r.winner == other_enum)
    draws = len(results) - wins - losses
    return wins, losses, draws


# ---------------------------------------------------------------------------
# Progress / summary printing
# ---------------------------------------------------------------------------

def _print_batch_line(side: str, batch_num: int, total_batches: int,
                      n_games: int, elapsed: float,
                      wins: int, losses: int, draws: int) -> None:
    gps = n_games / elapsed if elapsed > 0 else 0.0
    print(
        f"[bench] batch {batch_num}/{total_batches} {side.upper()}: "
        f"{n_games} games in {elapsed:.1f}s ({gps:.1f} g/s) "
        f"— {wins} wins, {losses} losses, {draws} draws"
    )


def _print_progress(job: dict) -> None:
    completed = sum(t["completed_games"] for t in job["tasks"])
    total = sum(t["total_games"] for t in job["tasks"])
    parts = []
    for t in job["tasks"]:
        side = t["side"].upper()
        done = t["completed_games"]
        if done > 0:
            pct = 100.0 * t["wins"] / done
            parts.append(f"{side} {pct:.1f}% ({t['wins']}/{done})")
        else:
            parts.append(f"{side} 0/0")
    suffix = " | ".join(parts)
    print(f"[bench] progress: {completed}/{total} games | {suffix} | cumulative")


def _print_summary(job: dict, job_path: Path, t_total: float) -> None:
    print(f"[bench] DONE job_id={job['job_id']}")
    win_strs = []
    combined_wins = 0
    combined_total = 0
    for t in job["tasks"]:
        side = t["side"].upper()
        total = t["total_games"]
        wins = t["wins"]
        pct = 100.0 * wins / total if total > 0 else 0.0
        win_strs.append(f"{side}: {pct:.1f}% ({wins}/{total})")
        combined_wins += wins
        combined_total += total
    combined_pct = 100.0 * combined_wins / combined_total if combined_total > 0 else 0.0
    parts_str = " | ".join(win_strs)
    print(f"[bench] {parts_str} | Combined: {combined_pct:.1f}%")
    print(f"[bench] Total: {t_total:.1f}s | Saved to {job_path}")


# ---------------------------------------------------------------------------
# Job creation and validation
# ---------------------------------------------------------------------------

def _make_task(side: str, task_seed: int, total_games: int) -> dict:
    return {
        "side": side,
        "seed": task_seed,
        "total_games": total_games,
        "completed_games": 0,
        "wins": 0,
        "losses": 0,
        "draws": 0,
        "elapsed_s": 0.0,
        "batches_done": 0,
    }


def _create_job(args: argparse.Namespace, job_id: str) -> dict:
    """Build a fresh job dict from parsed args."""
    tasks = []
    if args.sides in ("ussr", "both"):
        tasks.append(_make_task("ussr", args.seed, args.n_games))
    if args.sides in ("us", "both"):
        # US seed offset = n_games (matching bench_gpu.py convention and spec)
        us_seed = args.seed + args.n_games
        tasks.append(_make_task("us", us_seed, args.n_games))

    return {
        "job_id": job_id,
        "status": "running",
        "checkpoint": args.checkpoint,
        "scripted_path": None,  # filled in after export
        "sides": args.sides,
        "n_games": args.n_games,
        "seed": args.seed,
        "n_sim": args.n_sim,
        "pool_size": args.pool_size,
        "nash_temperatures": args.nash_temperatures,
        "batch_size": args.batch_size,
        "device": args.device,
        "created_at": _now_iso(),
        "updated_at": _now_iso(),
        "tasks": tasks,
    }


def _validate_resume(job: dict, args: argparse.Namespace) -> None:
    """Warn if resumed job params differ from CLI args (non-fatal)."""
    mismatches = []
    for key in ("checkpoint", "n_games", "seed", "n_sim", "pool_size", "nash_temperatures", "batch_size"):
        cli_val = getattr(args, key.replace("-", "_"), None)
        if cli_val is None:
            continue
        if job.get(key) != cli_val:
            mismatches.append(f"  {key}: job={job.get(key)!r}, cli={cli_val!r}")
    if mismatches:
        print("[bench] WARNING: resumed job params differ from CLI args:")
        for m in mismatches:
            print(m)
        print("[bench] Using job file params.")


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def run(job: dict, job_path: Path) -> None:
    scripted_path = job["scripted_path"]
    batch_size = job["batch_size"]
    n_sim = job["n_sim"]
    pool_size = job["pool_size"]
    nash_temperatures = job["nash_temperatures"]
    device = job["device"]

    t_global_start = time.time()

    for task in job["tasks"]:
        side = task["side"]
        total_games = task["total_games"]
        total_batches = (total_games + batch_size - 1) // batch_size

        remaining = total_games - task["completed_games"]
        current_seed = task["seed"] + task["completed_games"]

        while remaining > 0:
            batch = min(batch_size, remaining)
            batch_num = task["batches_done"] + 1

            t0 = time.time()
            results = _run_batch(
                scripted_path, side, batch, current_seed,
                n_sim, pool_size, nash_temperatures, device
            )
            elapsed = time.time() - t0

            wins, losses, draws = _count_results(results, side)

            task["completed_games"] += batch
            task["wins"] += wins
            task["losses"] += losses
            task["draws"] += draws
            task["elapsed_s"] = round(task["elapsed_s"] + elapsed, 3)
            task["batches_done"] += 1
            job["updated_at"] = _now_iso()

            _save_job_atomic(job, job_path)

            _print_batch_line(side, batch_num, total_batches, batch, elapsed, wins, losses, draws)
            _print_progress(job)

            remaining -= batch
            current_seed += batch

    job["status"] = "done"
    job["updated_at"] = _now_iso()
    _save_job_atomic(job, job_path)

    t_total = time.time() - t_global_start
    _print_summary(job, job_path, t_total)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Restartable benchmark runner wrapping tscore.benchmark_batched / benchmark_mcts"
    )
    parser.add_argument("--checkpoint", default=None, help="Path to .pt checkpoint (raw or scripted)")
    parser.add_argument("--sides", default="both", choices=["ussr", "us", "both"])
    parser.add_argument("--n-games", type=int, default=500)
    parser.add_argument("--seed", type=int, default=50000)
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--n-sim", type=int, default=0, help="MCTS simulations (0 = greedy batched)")
    parser.add_argument("--pool-size", type=int, default=32)
    parser.add_argument("--nash-temperatures", action="store_true", default=False)
    parser.add_argument("--device", default="cpu", choices=["cpu", "cuda"])
    parser.add_argument("--job-dir", default="results/bench_jobs")
    parser.add_argument("--job-id", default=None, help="Resume an existing job by ID")
    args = parser.parse_args()

    job_dir = Path(args.job_dir)

    # ------------------------------------------------------------------
    # Resume or create
    # ------------------------------------------------------------------
    if args.job_id:
        job_path = job_dir / f"{args.job_id}.json"
        if not job_path.exists():
            print(f"[bench] ERROR: job file not found: {job_path}", file=sys.stderr)
            sys.exit(1)
        job = _load_job(job_path)
        if args.checkpoint:
            _validate_resume(job, args)
        # Honour device override on resume (user may want cuda now)
        if args.device != "cpu":
            job["device"] = args.device
        print(f"[bench] Resuming job_id: {job['job_id']}")
    else:
        if not args.checkpoint:
            print("[bench] ERROR: --checkpoint is required when starting a new job.", file=sys.stderr)
            sys.exit(1)
        job_id = uuid.uuid4().hex[:8]
        job_path = job_dir / f"{job_id}.json"
        job = _create_job(args, job_id)
        print(f"[bench] job_id: {job_id}")

    # ------------------------------------------------------------------
    # TorchScript export (once per job)
    # ------------------------------------------------------------------
    if not job.get("scripted_path"):
        checkpoint = job["checkpoint"]
        scripted_path = _ensure_scripted(checkpoint)
        job["scripted_path"] = scripted_path
        _save_job_atomic(job, job_path)
    else:
        scripted_path = job["scripted_path"]

    if not os.path.exists(scripted_path):
        print(f"[bench] ERROR: scripted model not found: {scripted_path}", file=sys.stderr)
        sys.exit(1)

    # ------------------------------------------------------------------
    # Print startup banner
    # ------------------------------------------------------------------
    completed = sum(t["completed_games"] for t in job["tasks"])
    total = sum(t["total_games"] for t in job["tasks"])
    ussr_done = next((t["wins"] for t in job["tasks"] if t["side"] == "ussr"), 0)
    us_done = next((t["wins"] for t in job["tasks"] if t["side"] == "us"), 0)

    print(f"[bench] checkpoint: {job['checkpoint']}")
    print(
        f"[bench] config: sides={job['sides']} n_games={job['n_games']} "
        f"seed={job['seed']} n_sim={job['n_sim']} batch_size={job['batch_size']}"
    )
    print(f"[bench] progress: {completed}/{total} games ({ussr_done} USSR wins, {us_done} US wins)")

    # ------------------------------------------------------------------
    # Check if already done
    # ------------------------------------------------------------------
    if job.get("status") == "done":
        print("[bench] Job already complete. Use a new --job-id or omit it to start fresh.")
        _print_summary(job, job_path, sum(t["elapsed_s"] for t in job["tasks"]))
        return

    # ------------------------------------------------------------------
    # Run
    # ------------------------------------------------------------------
    run(job, job_path)


if __name__ == "__main__":
    main()
