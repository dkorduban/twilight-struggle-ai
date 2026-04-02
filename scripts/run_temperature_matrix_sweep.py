#!/usr/bin/env python3
"""Run full matrix temperature sweep: every (ussr_temp, us_temp) pair.

Produces a JSON with a flat list of results for each cell in the matrix.
Uses ProcessPoolExecutor for parallelism (each cell is an independent subprocess).
"""

import json
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

BINARY = "/home/dkord/code/twilight-struggle-ai/build-ninja/cpp/tools/ts_benchmark_matchup"
WORKDIR = "/home/dkord/code/twilight-struggle-ai"


def run_benchmark(games: int, seed: int, ussr_temp: float, us_temp: float, bid: int) -> dict:
    cmd = [
        "nice", "-n", "10", BINARY,
        "--games", str(games),
        "--seed", str(seed),
        "--ussr-temperature", str(ussr_temp),
        "--us-temperature", str(us_temp),
        "--json",
    ]
    if bid > 0:
        cmd.extend(["--bid", str(bid)])

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=WORKDIR)

    if result.returncode != 0:
        raise RuntimeError(f"Benchmark failed for ussr_t={ussr_temp} us_t={us_temp}: {result.stderr}")

    data = json.loads(result.stdout)
    data["ussr_temperature"] = ussr_temp
    data["us_temperature"] = us_temp
    return data


def main():
    games = 1000
    seed = 42
    bid = 2
    temps = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
    workers = 8

    output_path = Path(WORKDIR) / "results" / "heuristic_temperature_matrix_bid2.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Build all (ussr_t, us_t) pairs
    pairs = [(ussr_t, us_t) for ussr_t in temps for us_t in temps]
    total = len(pairs)

    print(f"Running {total} cells with {workers} parallel workers...")
    t0 = time.time()

    # Run all cells in parallel
    cell_results: dict[tuple[float, float], dict] = {}
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(run_benchmark, games, seed, ussr_t, us_t, bid): (ussr_t, us_t)
            for ussr_t, us_t in pairs
        }
        done = 0
        for future in as_completed(futures):
            ussr_t, us_t = futures[future]
            try:
                data = future.result()
                cell_results[(ussr_t, us_t)] = data
                done += 1
                print(f"  [{done}/{total}] ussr_t={ussr_t:.1f} us_t={us_t:.1f} → ussr_wr={data['ussr_wr']:.1f}%")
            except Exception as e:
                print(f"  FAILED: ussr_t={ussr_t} us_t={us_t}: {e}", file=sys.stderr)
                sys.exit(1)

    # Assemble matrix in row-major order
    matrix = [cell_results[(ussr_t, us_t)] for ussr_t, us_t in pairs]

    elapsed = time.time() - t0

    results = {
        "config": {
            "games_per_matchup": games,
            "seed": seed,
            "bid": bid,
            "setup": "human_openings_bid2_weighted",
            "ussr_temps": temps,
            "us_temps": temps,
            "parallel_workers": workers,
        },
        "matrix": matrix,
    }

    output_path.write_text(json.dumps(results, indent=2) + "\n")

    # Print summary matrix
    n = len(temps)
    print(f"\nDone in {elapsed:.0f}s ({elapsed/60:.1f}min). Results: {output_path}")
    print(f"\n{'':>10}", end="")
    for us_t in temps:
        print(f"  us={us_t:<5}", end="")
    print()
    for i, ussr_t in enumerate(temps):
        print(f"ussr={ussr_t:<5}", end="")
        for j, us_t in enumerate(temps):
            cell = matrix[i * n + j]
            print(f"  {cell['ussr_wr']:>5.1f}%", end="")
        print()


if __name__ == "__main__":
    main()
