"""Publish heuristic temperature sweep results to W&B.

Reads results/heuristic_temperature_sweep.json and creates a W&B run
with tables and line plots showing USSR/US WR vs temperature.

Usage:
    uv run python scripts/publish_sweep_to_wandb.py [--project ts-ai] [--name heuristic-temp-sweep]
"""

import argparse
import json
import sys
from pathlib import Path

import wandb


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="results/heuristic_temperature_sweep.json")
    parser.add_argument("--project", default="twilight-struggle-ai")
    parser.add_argument("--name", default="heuristic-temp-sweep-old-setup")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        print(f"Not found: {path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(path.read_text())
    config = data.get("config", {})

    run = wandb.init(
        project=args.project,
        name=args.name,
        config={
            **config,
            "experiment": "heuristic_temperature_sweep",
        },
    )

    # --- Sweep 1: Sampled USSR vs Fixed US ---
    for r in data.get("sampled_ussr_vs_fixed_us", []):
        temp = r.get("ussr_temperature", r.get("sampled_temp", 0))
        wandb.log({
            "ussr_sweep/temperature": temp,
            "ussr_sweep/ussr_wr": r.get("ussr_wr", 0),
            "ussr_sweep/us_wr": r.get("us_wr", 0),
            "ussr_sweep/draws": r.get("draws", 0),
            "ussr_sweep/defcon1": r.get("defcon1", 0),
            "ussr_sweep/turn_limit": r.get("turn_limit", 0),
            "ussr_sweep/avg_turn": r.get("avg_turn", 0),
            "ussr_sweep/avg_final_vp": r.get("avg_final_vp", 0),
            "ussr_sweep/games_per_sec": r.get("games_per_sec", 0),
        })

    # --- Sweep 2: Fixed USSR vs Sampled US ---
    for r in data.get("fixed_ussr_vs_sampled_us", []):
        temp = r.get("us_temperature", r.get("sampled_temp", 0))
        wandb.log({
            "us_sweep/temperature": temp,
            "us_sweep/ussr_wr": r.get("ussr_wr", 0),
            "us_sweep/us_wr": r.get("us_wr", 0),
            "us_sweep/draws": r.get("draws", 0),
            "us_sweep/defcon1": r.get("defcon1", 0),
            "us_sweep/turn_limit": r.get("turn_limit", 0),
            "us_sweep/avg_turn": r.get("avg_turn", 0),
            "us_sweep/avg_final_vp": r.get("avg_final_vp", 0),
            "us_sweep/games_per_sec": r.get("games_per_sec", 0),
        })

    # --- Summary table ---
    table = wandb.Table(columns=[
        "sweep", "temperature", "ussr_wr", "us_wr", "draws",
        "decisive", "defcon1", "turn_limit", "avg_turn", "avg_final_vp",
        "games_per_sec",
    ])

    for r in data.get("sampled_ussr_vs_fixed_us", []):
        temp = r.get("ussr_temperature", r.get("sampled_temp", 0))
        table.add_data(
            "sampled_ussr", temp,
            r.get("ussr_wr", 0), r.get("us_wr", 0),
            r.get("draws", 0), r.get("decisive", 0),
            r.get("defcon1", 0), r.get("turn_limit", 0),
            r.get("avg_turn", 0), r.get("avg_final_vp", 0),
            r.get("games_per_sec", 0),
        )

    for r in data.get("fixed_ussr_vs_sampled_us", []):
        temp = r.get("us_temperature", r.get("sampled_temp", 0))
        table.add_data(
            "sampled_us", temp,
            r.get("ussr_wr", 0), r.get("us_wr", 0),
            r.get("draws", 0), r.get("decisive", 0),
            r.get("defcon1", 0), r.get("turn_limit", 0),
            r.get("avg_turn", 0), r.get("avg_final_vp", 0),
            r.get("games_per_sec", 0),
        )

    wandb.log({"results_table": table})

    # --- Combined line plots with temperature as X-axis ---
    # Win rate vs temperature (both sweeps on one chart)
    wr_table = wandb.Table(columns=["temperature", "win_rate", "sweep_side"])
    for r in data.get("sampled_ussr_vs_fixed_us", []):
        temp = r.get("ussr_temperature", r.get("sampled_temp", 0))
        # When USSR is sampled, report USSR's WR (the sampled side's strength)
        wr_table.add_data(temp, r.get("ussr_wr", 0), "USSR sampled (USSR WR)")
    for r in data.get("fixed_ussr_vs_sampled_us", []):
        temp = r.get("us_temperature", r.get("sampled_temp", 0))
        # When US is sampled, report US's WR (the sampled side's strength)
        wr_table.add_data(temp, r.get("us_wr", 0), "US sampled (US WR)")

    wandb.log({
        "wr_vs_temp": wandb.plot.line(
            wr_table, x="temperature", y="win_rate",
            stroke="sweep_side",
            title="Sampled side WR vs Temperature (bid+2, human openings)",
        ),
    })

    # DEFCON-1 rate vs temperature
    defcon_table = wandb.Table(columns=["temperature", "defcon1_pct", "sweep_side"])
    for r in data.get("sampled_ussr_vs_fixed_us", []):
        temp = r.get("ussr_temperature", r.get("sampled_temp", 0))
        games = r.get("games", 1000)
        defcon_table.add_data(temp, 100.0 * r.get("defcon1", 0) / games, "USSR sampled")
    for r in data.get("fixed_ussr_vs_sampled_us", []):
        temp = r.get("us_temperature", r.get("sampled_temp", 0))
        games = r.get("games", 1000)
        defcon_table.add_data(temp, 100.0 * r.get("defcon1", 0) / games, "US sampled")

    wandb.log({
        "defcon1_vs_temp": wandb.plot.line(
            defcon_table, x="temperature", y="defcon1_pct",
            stroke="sweep_side",
            title="DEFCON-1 rate (%) vs Temperature",
        ),
    })

    # Avg game length vs temperature
    turn_table = wandb.Table(columns=["temperature", "avg_turn", "sweep_side"])
    for r in data.get("sampled_ussr_vs_fixed_us", []):
        temp = r.get("ussr_temperature", r.get("sampled_temp", 0))
        turn_table.add_data(temp, r.get("avg_turn", 0), "USSR sampled")
    for r in data.get("fixed_ussr_vs_sampled_us", []):
        temp = r.get("us_temperature", r.get("sampled_temp", 0))
        turn_table.add_data(temp, r.get("avg_turn", 0), "US sampled")

    wandb.log({
        "avg_turn_vs_temp": wandb.plot.line(
            turn_table, x="temperature", y="avg_turn",
            stroke="sweep_side",
            title="Avg Game Length vs Temperature",
        ),
    })

    run.finish()
    print(f"Published to W&B project={args.project} name={args.name}")


if __name__ == "__main__":
    main()
