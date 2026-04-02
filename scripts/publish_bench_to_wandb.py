"""Publish benchmark results JSON to W&B as a standalone run or update.

Called by the pipeline after bench_cpp.sh to log bench/win_pct and related
metrics to W&B for dashboard tracking.

Usage:
    uv run python scripts/publish_bench_to_wandb.py results/bench_v85.json [--generation v85]
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

_WANDB_API_KEY_FILE = os.path.join(os.path.dirname(__file__), "..", ".wandb-api-key.txt")
_WANDB_ENTITY = "korduban-ai"
_WANDB_PROJECT = "twilight-struggle-ai"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bench_json", help="Path to bench results JSON from bench_cpp.sh")
    parser.add_argument("--generation", default=None, help="Generation label (e.g. v85). Auto-detected from filename.")
    args = parser.parse_args()

    if not os.path.exists(args.bench_json):
        print(f"Bench results not found: {args.bench_json}")
        sys.exit(1)

    with open(args.bench_json) as f:
        results = json.load(f)

    # Detect generation
    gen = args.generation
    if not gen:
        m = re.search(r"v(\d+)", args.bench_json)
        gen = f"v{m.group(1)}" if m else "unknown"

    # Load API key
    key_path = os.path.abspath(_WANDB_API_KEY_FILE)
    if not os.path.exists(key_path):
        print(f"W&B key file not found at {key_path}; skipping.")
        sys.exit(0)
    with open(key_path) as f:
        api_key = f.read().strip()
    if not api_key:
        sys.exit(0)
    os.environ["WANDB_API_KEY"] = api_key

    try:
        import wandb
    except ImportError:
        print("wandb not installed; skipping.")
        sys.exit(0)

    # Build metrics
    win_pct = results.get("learned_win_pct", 0.0)
    metrics = {
        "bench/win_pct": win_pct,
        "bench/learned_wins": results.get("learned_wins", 0),
        "bench/heuristic_wins": results.get("heuristic_wins", 0),
        "bench/decisive_games": results.get("decisive_games", 0),
        "bench/draws": results.get("draws", 0),
        "bench/n_games": results.get("n_games", 0),
        "bench/elapsed_seconds": results.get("elapsed_seconds", 0),
    }

    sides = results.get("sides", {})
    for side_name, side_data in sides.items():
        if side_data.get("games", 0) > 0:
            metrics[f"bench/{side_name}_wins"] = side_data.get("learned_wins", 0)
            metrics[f"bench/{side_name}_games"] = side_data.get("games", 0)
            decisive = side_data.get("decisive_games", 0)
            if decisive > 0:
                metrics[f"bench/{side_name}_win_pct"] = round(
                    100.0 * side_data.get("learned_wins", 0) / decisive, 1
                )

    # Try to find and resume the training run for this generation
    run_name = f"{gen}_bench"
    run = wandb.init(
        entity=_WANDB_ENTITY,
        project=_WANDB_PROJECT,
        name=run_name,
        config={"generation": gen, "source": "bench_cpp.sh"},
        tags=["benchmark"],
        reinit=True,
    )

    for k, v in metrics.items():
        run.summary[k] = v
    run.log(metrics)
    run.finish()

    print(f"[wandb] Published {gen} bench results: win_pct={win_pct}%")


if __name__ == "__main__":
    main()
