#!/usr/bin/env python3
"""Benchmark all pre-sc and notable SC checkpoints. Quick 50-game pass with partial saves.

After this completes, analyze results and manually pick models for deeper (200/500) passes.
"""
import json
import os
import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime, timezone

_bindings_dir = str(Path(__file__).resolve().parent.parent / "build-ninja" / "bindings")
if _bindings_dir not in sys.path:
    sys.path.insert(0, _bindings_dir)

import tscore

RESULTS_FILE = Path("results/benchmark_all_checkpoints.json")
RESULTS_TXT = Path("results/benchmark_all_checkpoints.txt")
POOL_SIZE = 32

# Pre-sc models (v19-v61)
PRE_SC = [f"ppo_v{v}_league" for v in list(range(19, 42)) + list(range(44, 62))]
# Notable SC models
SC_NOTABLE = [f"ppo_v{v}_sc_league" for v in [66, 67, 68, 100, 150, 200, 209, 228, 250, 267, 295]]
ALL_MODELS = PRE_SC + SC_NOTABLE


def ensure_scripted(ckpt_path: str) -> str:
    scripted = ckpt_path.replace(".pt", "_scripted.pt")
    if os.path.exists(scripted):
        return scripted
    export_script = str(Path(__file__).resolve().parent.parent / "cpp" / "tools" / "export_baseline_to_torchscript.py")
    subprocess.run(["uv", "run", "python", export_script, "--checkpoint", ckpt_path, "--out", scripted],
                   check=True, capture_output=True)
    return scripted


def bench_one(scripted: str, side_enum, n_games: int, seed: int) -> dict:
    results = tscore.benchmark_batched(
        scripted, side_enum, n_games, pool_size=POOL_SIZE, seed=seed,
        device="cpu", nash_temperatures=True,
    )
    other = tscore.Side.US if side_enum == tscore.Side.USSR else tscore.Side.USSR
    wins = sum(1 for r in results if r.winner == side_enum)
    losses = sum(1 for r in results if r.winner == other)
    avg_turn = sum(r.end_turn for r in results) / len(results) if results else 0
    # Count end reasons
    reasons = {}
    for r in results:
        reasons[r.end_reason] = reasons.get(r.end_reason, 0) + 1
    return {"wins": wins, "losses": losses, "draws": n_games - wins - losses,
            "avg_turn": round(avg_turn, 1), "n_games": n_games, "end_reasons": reasons}


def save_partial(all_results: dict, n_games: int):
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_FILE, "w") as f:
        json.dump(all_results, f, indent=2)
    # Human-readable TXT
    lines = [
        "# Benchmark: All Checkpoints vs Heuristic (scoring card fix active)",
        f"# {n_games} games/side, nash temperatures, pool_size={POOL_SIZE}",
        f"# Updated: {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"{'Model':<28} {'N':>4} {'USSR WR':>8} {'US WR':>8} {'Combined':>10} {'USSR AvgT':>10} {'US AvgT':>10}",
        "-" * 86,
    ]
    scored = []
    for name, data in all_results.items():
        if "error" in data:
            continue
        n = data.get("ussr", {}).get("n_games", n_games)
        u = data.get("ussr", {})
        s = data.get("us", {})
        uwr = u.get("wins", 0) / n * 100
        swr = s.get("wins", 0) / n * 100
        cwr = (uwr + swr) / 2
        scored.append((cwr, name, uwr, swr, n, u.get("avg_turn", 0), s.get("avg_turn", 0)))
    scored.sort(reverse=True)
    for cwr, name, uwr, swr, n, ut, st in scored:
        lines.append(f"{name:<28} {n:>4} {uwr:>7.1f}% {swr:>7.1f}% {cwr:>9.1f}% {ut:>10.1f} {st:>10.1f}")
    for name, data in all_results.items():
        if "error" in data:
            lines.append(f"{name:<28} ERROR: {data['error'][:60]}")
    lines.append("")
    with open(RESULTS_TXT, "w") as f:
        f.write("\n".join(lines))


def run_pass(models: list, n_games: int, all_results: dict):
    for i, model_name in enumerate(models):
        existing = all_results.get(model_name)
        if existing and not existing.get("error") and existing.get("ussr", {}).get("n_games", 0) >= n_games:
            print(f"  [{i+1}/{len(models)}] {model_name} — already at N={existing['ussr']['n_games']}, skip")
            continue

        ckpt = f"data/checkpoints/{model_name}/ppo_best.pt"
        if not os.path.exists(ckpt):
            print(f"  [{i+1}/{len(models)}] {model_name} — not found")
            continue

        try:
            scripted = ensure_scripted(ckpt)
        except Exception as e:
            print(f"  [{i+1}/{len(models)}] {model_name} — export failed: {e}")
            all_results[model_name] = {"error": str(e)}
            save_partial(all_results, n_games)
            continue

        t0 = time.time()
        try:
            ussr = bench_one(scripted, tscore.Side.USSR, n_games, 50000)
            us = bench_one(scripted, tscore.Side.US, n_games, 50000 + n_games)
        except Exception as e:
            print(f"  [{i+1}/{len(models)}] {model_name} — bench failed: {e}")
            all_results[model_name] = {"error": str(e)}
            save_partial(all_results, n_games)
            continue

        elapsed = time.time() - t0
        cwr = (ussr["wins"] + us["wins"]) / (2 * n_games) * 100
        all_results[model_name] = {"ussr": ussr, "us": us, "elapsed": round(elapsed, 1)}
        save_partial(all_results, n_games)

        print(f"  [{i+1}/{len(models)}] {model_name}: "
              f"USSR={ussr['wins']}/{n_games} ({ussr['wins']/n_games*100:.1f}%) "
              f"US={us['wins']}/{n_games} ({us['wins']/n_games*100:.1f}%) "
              f"combined={cwr:.1f}% [{elapsed:.0f}s]")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-games", type=int, default=50)
    parser.add_argument("--models", nargs="*", help="Specific model names to benchmark (default: all)")
    args = parser.parse_args()

    all_results = {}
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE) as f:
            all_results = json.load(f)
        done = len([k for k in all_results if "error" not in all_results[k]])
        print(f"[bench] Resuming with {done} models already benchmarked")

    models = args.models if args.models else ALL_MODELS
    print(f"[bench] Pass: {args.n_games} games/side, {len(models)} models")
    run_pass(models, args.n_games, all_results)
    print(f"\n[bench] Done! Results in {RESULTS_TXT}")


if __name__ == "__main__":
    main()
