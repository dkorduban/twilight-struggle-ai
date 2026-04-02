"""Sweep heuristic temperature vs deterministic baseline, measuring WR by side.

Two sweeps:
  1. Sampled USSR (temp T) vs Fixed US (temp 0) — does sampling help USSR?
  2. Fixed USSR (temp 0) vs Sampled US (temp T) — does sampling help US?

Usage:
    uv run python scripts/sweep_heuristic_temperature.py \
        [--games 1000] [--seed 42] [--wandb-project ts-ai]
"""

import argparse
import json
import os
import subprocess
import sys
import time

try:
    import wandb

    _WANDB = True
except ImportError:
    wandb = None
    _WANDB = False


BENCHMARK_BIN = "build-ninja/cpp/tools/ts_benchmark_matchup"
TEMPERATURES = [0.0, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0]


def run_matchup(
    games: int, seed: int, ussr_temp: float, us_temp: float
) -> dict:
    cmd = [
        BENCHMARK_BIN,
        "--games", str(games),
        "--seed", str(seed),
        "--ussr-temperature", str(ussr_temp),
        "--us-temperature", str(us_temp),
        "--json",
    ]
    start = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    wall_time = time.time() - start
    data = json.loads(result.stdout.strip())
    data["wall_time_sec"] = round(wall_time, 2)
    try:
        load = os.getloadavg()
        data["load_avg_1m"] = round(load[0], 2)
    except OSError:
        pass
    return data


def print_header():
    print(
        f"{'Matchup':30s} {'Temp':>5s} {'Games':>6s} "
        f"{'USSR WR':>8s} {'US WR':>8s} {'Draws':>6s} "
        f"{'DEFCON1':>7s} {'TurnLim':>7s} {'AvgTrn':>6s} "
        f"{'Time':>6s} {'G/s':>6s}"
    )
    print("-" * 110)


def print_row(label: str, temp: float, d: dict):
    print(
        f"{label:30s} {temp:5.2f} {d['games']:6d} "
        f"{d['ussr_wr']:7.1f}% {d['us_wr']:7.1f}% {d['draws']:6d} "
        f"{d['defcon1']:7d} {d['turn_limit']:7d} {d['avg_turn']:6.1f} "
        f"{d['wall_time_sec']:5.1f}s {d['games_per_sec']:5.1f}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb-project", default="twilight-struggle-ai")
    parser.add_argument("--no-wandb", action="store_true")
    args = parser.parse_args()

    use_wandb = _WANDB and not args.no_wandb

    all_results = []
    print_header()

    # Sweep 1: Sampled USSR vs Fixed US
    for temp in TEMPERATURES:
        data = run_matchup(args.games, args.seed, ussr_temp=temp, us_temp=0.0)
        data["sweep"] = "sampled_ussr_vs_fixed_us"
        data["sampled_side"] = "ussr"
        data["sampled_temp"] = temp
        all_results.append(data)
        print_row("Sampled USSR vs Fixed US", temp, data)

    print()

    # Sweep 2: Fixed USSR vs Sampled US
    for temp in TEMPERATURES:
        data = run_matchup(args.games, args.seed, ussr_temp=0.0, us_temp=temp)
        data["sweep"] = "fixed_ussr_vs_sampled_us"
        data["sampled_side"] = "us"
        data["sampled_temp"] = temp
        all_results.append(data)
        print_row("Fixed USSR vs Sampled US", temp, data)

    # Save JSON
    out_path = "results/heuristic_temperature_sweep.json"
    os.makedirs("results", exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(
            {"config": {"games_per_matchup": args.games, "seed": args.seed,
                        "temperatures": TEMPERATURES},
             "results": all_results},
            f, indent=2,
        )
    print(f"\nSaved to {out_path}")

    # Publish to W&B
    if use_wandb:
        run = wandb.init(
            project=args.wandb_project,
            name="heuristic-temp-sweep",
            config={
                "games_per_matchup": args.games,
                "seed": args.seed,
                "temperatures": TEMPERATURES,
                "setup": "hardcoded_3_variants",
            },
        )
        table = wandb.Table(
            columns=[
                "sweep", "sampled_side", "sampled_temp",
                "ussr_wr", "us_wr", "draws", "decisive",
                "defcon1", "turn_limit", "avg_turn", "avg_final_vp",
                "games_per_sec", "wall_time_sec",
            ],
        )
        for r in all_results:
            table.add_data(
                r["sweep"], r["sampled_side"], r["sampled_temp"],
                r["ussr_wr"], r["us_wr"], r["draws"], r["decisive"],
                r["defcon1"], r["turn_limit"], r["avg_turn"],
                r["avg_final_vp"], r["games_per_sec"], r["wall_time_sec"],
            )
            wandb.log({
                f"{r['sampled_side']}_temp": r["sampled_temp"],
                f"{r['sampled_side']}_sampled_ussr_wr": r["ussr_wr"],
                f"{r['sampled_side']}_sampled_us_wr": r["us_wr"],
            })

        wandb.log({"results_table": table})
        run.finish()
        print(f"Published to W&B project: {args.wandb_project}")
    else:
        print("(W&B not available or --no-wandb specified)")


if __name__ == "__main__":
    main()
