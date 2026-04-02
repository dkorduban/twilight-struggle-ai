#!/usr/bin/env python3
"""Run heuristic temperature sweep with ts_benchmark_matchup binary."""

import json
import subprocess
import sys
from pathlib import Path


def run_benchmark(
    binary_path: str,
    games: int,
    seed: int,
    ussr_temp: float,
    us_temp: float,
    bid: int = 0,
) -> dict:
    """Run a single benchmark and return JSON result."""
    cmd = [
        "nice",
        "-n",
        "10",
        binary_path,
        "--games",
        str(games),
        "--seed",
        str(seed),
        "--ussr-temperature",
        str(ussr_temp),
        "--us-temperature",
        str(us_temp),
        "--json",
    ]
    if bid > 0:
        cmd.extend(["--bid", str(bid)])

    print(f"  Running: ussr_temp={ussr_temp:.2f}, us_temp={us_temp:.2f}...", end=" ", flush=True)

    result = subprocess.run(cmd, capture_output=True, text=True, cwd="/home/dkord/code/twilight-struggle-ai")

    if result.returncode != 0:
        print(f"FAILED")
        print(f"  stderr: {result.stderr}")
        sys.exit(1)

    try:
        data = json.loads(result.stdout)
        data["ussr_temperature"] = ussr_temp
        data["us_temperature"] = us_temp
        print("OK")
        return data
    except json.JSONDecodeError as e:
        print(f"JSON PARSE FAILED")
        print(f"  stdout: {result.stdout}")
        print(f"  error: {e}")
        sys.exit(1)


def main():
    binary = "/home/dkord/code/twilight-struggle-ai/build-ninja/cpp/tools/ts_benchmark_matchup"
    games = 1000
    seed = 42
    bid = 2
    temperatures = [0.0, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0]

    results = {
        "config": {
            "games_per_matchup": games,
            "seed": seed,
            "bid": bid,
            "setup": "human_openings_bid2_weighted",
        },
        "sampled_ussr_vs_fixed_us": [],
        "fixed_ussr_vs_sampled_us": [],
    }

    # Sweep 1: Sampled USSR vs Fixed US
    print("\n=== Sweep 1: Sampled USSR vs Fixed US ===")
    for t in temperatures:
        data = run_benchmark(binary, games, seed, t, 0.0, bid=bid)
        results["sampled_ussr_vs_fixed_us"].append(data)

    # Sweep 2: Fixed USSR vs Sampled US
    print("\n=== Sweep 2: Fixed USSR vs Sampled US ===")
    for t in temperatures:
        data = run_benchmark(binary, games, seed, 0.0, t, bid=bid)
        results["fixed_ussr_vs_sampled_us"].append(data)

    # Save to output file
    output_path = Path("/home/dkord/code/twilight-struggle-ai/results/heuristic_temperature_sweep_human_openings_bid2.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {output_path}")

    # Print summary table
    print("\n=== Summary Table ===\n")
    print("Sweep 1: Sampled USSR vs Fixed US (ussr_temp variable, us_temp=0.0)")
    print("=" * 90)
    print(f"{'USSR Temp':<12} {'USSR WR':<10} {'US WR':<10} {'Draws':<10} {'Avg Turn':<12} {'Elapsed':<10}")
    print("-" * 90)
    for row in results["sampled_ussr_vs_fixed_us"]:
        print(
            f"{row['ussr_temperature']:<12.2f} "
            f"{row['ussr_wr']:<9.1f}% "
            f"{row['us_wr']:<9.1f}% "
            f"{row['draws']:<10} "
            f"{row['avg_turn']:<12.2f} "
            f"{row['elapsed_sec']:<10.1f}s"
        )

    print("\n" + "=" * 90)
    print("Sweep 2: Fixed USSR vs Sampled US (us_temp variable, ussr_temp=0.0)")
    print("=" * 90)
    print(f"{'US Temp':<12} {'USSR WR':<10} {'US WR':<10} {'Draws':<10} {'Avg Turn':<12} {'Elapsed':<10}")
    print("-" * 90)
    for row in results["fixed_ussr_vs_sampled_us"]:
        print(
            f"{row['us_temperature']:<12.2f} "
            f"{row['ussr_wr']:<9.1f}% "
            f"{row['us_wr']:<9.1f}% "
            f"{row['draws']:<10} "
            f"{row['avg_turn']:<12.2f} "
            f"{row['elapsed_sec']:<10.1f}s"
        )


if __name__ == "__main__":
    main()
