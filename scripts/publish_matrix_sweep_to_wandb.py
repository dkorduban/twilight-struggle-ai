#!/usr/bin/env python3
"""Publish temperature matrix sweep results to W&B as heatmaps.

Reads results/heuristic_temperature_matrix_bid2.json and creates heatmap
visualizations for USSR WR, US WR, DEFCON-1 rate, avg turn, avg VP, draws.

Usage:
    WANDB_API_KEY=... uv run python scripts/publish_matrix_sweep_to_wandb.py
"""

import argparse
import json
import sys
from pathlib import Path

import wandb


def build_heatmap_table(matrix: list[dict], temps: list[float], metric_key: str,
                        scale: float = 1.0, games_key: str = "games") -> wandb.Table:
    """Build a W&B Table suitable for heatmap plotting."""
    table = wandb.Table(columns=["ussr_temp", "us_temp", "value"])
    n = len(temps)
    for i, ussr_t in enumerate(temps):
        for j, us_t in enumerate(temps):
            cell = matrix[i * n + j]
            val = cell.get(metric_key, 0)
            if scale != 1.0:
                games = cell.get(games_key, 1000)
                val = scale * val / games
            table.add_data(str(ussr_t), str(us_t), val)
    return table


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="results/heuristic_temperature_matrix_bid2.json")
    parser.add_argument("--project", default="twilight-struggle-ai")
    parser.add_argument("--name", default="heuristic-temp-matrix-bid2")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        print(f"Not found: {path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(path.read_text())
    config = data.get("config", {})
    matrix = data["matrix"]
    temps = config["ussr_temps"]

    run = wandb.init(
        project=args.project,
        name=args.name,
        config={**config, "experiment": "heuristic_temperature_matrix"},
    )

    # Heatmap configs: (metric_key, title, scale_by_games)
    heatmaps = [
        ("ussr_wr", "USSR Win Rate (%)", False),
        ("us_wr", "US Win Rate (%)", False),
        ("defcon1", "DEFCON-1 Rate (%)", True),
        ("avg_turn", "Avg Game Length (turns)", False),
        ("avg_final_vp", "Avg Final VP (USSR perspective)", False),
        ("draws", "Draw Rate (%)", True),
    ]

    for metric_key, title, scale_by_games in heatmaps:
        if scale_by_games:
            table = build_heatmap_table(matrix, temps, metric_key, scale=100.0)
        else:
            table = build_heatmap_table(matrix, temps, metric_key)

        # Log as a custom plot — W&B will render the table
        # Use a scatter with text annotations as heatmap proxy
        wandb.log({
            f"matrix/{metric_key}_table": table,
        })

    # Also log a combined summary table with all metrics
    summary = wandb.Table(columns=[
        "ussr_temp", "us_temp", "ussr_wr", "us_wr",
        "defcon1_pct", "draws", "avg_turn", "avg_final_vp", "games_per_sec",
    ])
    n = len(temps)
    for i, ussr_t in enumerate(temps):
        for j, us_t in enumerate(temps):
            cell = matrix[i * n + j]
            games = cell.get("games", 1000)
            summary.add_data(
                ussr_t, us_t,
                cell.get("ussr_wr", 0), cell.get("us_wr", 0),
                100.0 * cell.get("defcon1", 0) / games,
                cell.get("draws", 0),
                cell.get("avg_turn", 0), cell.get("avg_final_vp", 0),
                cell.get("games_per_sec", 0),
            )
    wandb.log({"matrix/summary_table": summary})

    # Log heatmap images using matplotlib for proper visualization
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np

        for metric_key, title, scale_by_games in heatmaps:
            grid = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    cell = matrix[i * n + j]
                    val = cell.get(metric_key, 0)
                    if scale_by_games:
                        val = 100.0 * val / cell.get("games", 1000)
                    grid[i, j] = val

            fig, ax = plt.subplots(figsize=(8, 6))
            im = ax.imshow(grid, cmap="RdYlGn_r" if "defcon" in metric_key else "RdYlBu",
                          aspect="equal", origin="upper")

            ax.set_xticks(range(n))
            ax.set_xticklabels([str(t) for t in temps])
            ax.set_yticks(range(n))
            ax.set_yticklabels([str(t) for t in temps])
            ax.set_xlabel("US Temperature")
            ax.set_ylabel("USSR Temperature")
            ax.set_title(f"{title}\n(bid+2, human openings, 1k games/cell)")

            # Annotate cells
            for i in range(n):
                for j in range(n):
                    fmt = f"{grid[i, j]:.1f}"
                    color = "white" if abs(grid[i, j] - grid.mean()) > grid.std() else "black"
                    ax.text(j, i, fmt, ha="center", va="center", color=color, fontsize=9)

            fig.colorbar(im, ax=ax, shrink=0.8)
            fig.tight_layout()

            wandb.log({f"matrix/{metric_key}_heatmap": wandb.Image(fig)})
            plt.close(fig)

        print("Heatmap images logged successfully.")
    except ImportError:
        print("matplotlib not available — skipped heatmap images, tables still logged.")

    run.finish()
    print(f"Published to W&B project={args.project} name={args.name}")


if __name__ == "__main__":
    main()
