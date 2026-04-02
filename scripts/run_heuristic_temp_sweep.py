#!/usr/bin/env python3
"""Run heuristic temperature sweep without setup influence and aggregate results."""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path("/home/dkord/code/twilight-struggle-ai")
BINARY = REPO_ROOT / "build-ninja/cpp/tools/ts_benchmark_matchup"
OUTPUT_JSON = REPO_ROOT / "results/heuristic_temperature_sweep_no_setup.json"

TEMPERATURES = [0.0, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0]
GAMES_PER_MATCHUP = 1000
SEED = 42


def run_matchup(ussr_temp: float, us_temp: float) -> dict:
    """Run a single matchup and return the JSON result."""
    cmd = [
        "nice", "-n", "10",
        str(BINARY),
        "--games", str(GAMES_PER_MATCHUP),
        "--seed", str(SEED),
        "--no-setup",
        "--ussr-temperature", str(ussr_temp),
        "--us-temperature", str(us_temp),
        "--json",
    ]

    print(f"  Running: USSR temp={ussr_temp}, US temp={us_temp}...", file=sys.stderr, flush=True)

    try:
        result = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=600,
        )

        if result.returncode != 0:
            print(f"    ERROR: {result.stderr}", file=sys.stderr)
            return {}

        data = json.loads(result.stdout)
        data["ussr_temperature"] = ussr_temp
        data["us_temperature"] = us_temp
        print(f"    ✓ USSR win%={data.get('ussr_wins', 0)/GAMES_PER_MATCHUP*100:.1f}%", file=sys.stderr, flush=True)
        return data

    except subprocess.TimeoutExpired:
        print(f"    TIMEOUT", file=sys.stderr)
        return {}
    except json.JSONDecodeError as e:
        print(f"    JSON decode error: {e}", file=sys.stderr)
        return {}


def main():
    """Run both sweeps and aggregate."""
    print("Starting heuristic temperature sweep (no-setup)...", file=sys.stderr)

    results = {
        "config": {
            "games_per_matchup": GAMES_PER_MATCHUP,
            "seed": SEED,
            "setup": "no_free_influence",
            "timestamp": datetime.utcnow().isoformat() + "Z",
        },
        "sampled_ussr_vs_fixed_us": [],
        "fixed_ussr_vs_sampled_us": [],
    }

    # Sweep 1: Sampled USSR vs Fixed US
    print("\nSweep 1: Sampled USSR vs Fixed US", file=sys.stderr)
    for temp in TEMPERATURES:
        data = run_matchup(temp, 0.0)
        if data:
            results["sampled_ussr_vs_fixed_us"].append(data)

    # Sweep 2: Fixed USSR vs Sampled US
    print("\nSweep 2: Fixed USSR vs Sampled US", file=sys.stderr)
    for temp in TEMPERATURES:
        data = run_matchup(0.0, temp)
        if data:
            results["fixed_ussr_vs_sampled_us"].append(data)

    # Save results
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n✓ Results saved to {OUTPUT_JSON}", file=sys.stderr)
    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
