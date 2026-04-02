"""Backfill W&B with historical benchmark data from results/benchmark_history.json.

Creates one W&B run per generation with bench/win_pct logged as a summary metric,
allowing historical comparison in the W&B dashboard.

Usage:
    uv run python scripts/backfill_wandb_history.py [--dry-run]
"""

import argparse
import json
import os
import sys

_WANDB_API_KEY_FILE = os.path.join(os.path.dirname(__file__), "..", ".wandb-api-key.txt")
_WANDB_ENTITY = "korduban-ai"
_WANDB_PROJECT = "twilight-struggle-ai"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print what would be logged without writing")
    parser.add_argument("--history-file", default="results/benchmark_history.json")
    args = parser.parse_args()

    with open(args.history_file) as f:
        history = json.load(f)

    if args.dry_run:
        for key, data in sorted(history.items()):
            win_pct = data.get("learned_vs_heuristic", 0.0)
            print(f"  {key}: bench/win_pct={win_pct}")
        print(f"\n{len(history)} runs would be created.")
        return

    # Load API key
    if not os.path.exists(_WANDB_API_KEY_FILE):
        print(f"W&B key file not found at {_WANDB_API_KEY_FILE}")
        sys.exit(1)
    with open(_WANDB_API_KEY_FILE) as f:
        os.environ["WANDB_API_KEY"] = f.read().strip()

    import wandb

    for key, data in sorted(history.items()):
        win_pct = data.get("learned_vs_heuristic", 0.0)
        run_name = f"{key}_historical"

        run = wandb.init(
            entity=_WANDB_ENTITY,
            project=_WANDB_PROJECT,
            name=run_name,
            config={"generation": key, "source": "benchmark_history.json"},
            tags=["historical", "backfill"],
            reinit=True,
        )
        run.summary["bench/win_pct"] = win_pct
        run.log({"bench/win_pct": win_pct})
        run.finish()
        print(f"  {key}: bench/win_pct={win_pct}")

    print(f"\nBackfilled {len(history)} runs to W&B.")


if __name__ == "__main__":
    main()
