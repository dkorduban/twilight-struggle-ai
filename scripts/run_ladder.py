#!/usr/bin/env python3
"""Run a checkpoint ladder via the native C++ collector."""

from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import pyarrow.parquet as pq


@dataclass(frozen=True)
class RunSummary:
    ussr_model: str
    us_model: str
    ussr_wins: int
    us_wins: int
    draws: int
    games: int
    seed: int
    parquet_path: str


def checkpoint_name(path: Path) -> str:
    return path.stem


def summarize_parquet(path: Path) -> tuple[int, int, int]:
    table = pq.read_table(path, columns=["game_id", "final_vp"])
    vp_by_game: dict[str, int | None] = {}
    for game_id, final_vp in zip(table.column("game_id").to_pylist(), table.column("final_vp").to_pylist()):
        vp_by_game[str(game_id)] = final_vp

    ussr_wins = 0
    us_wins = 0
    draws = 0
    for final_vp in vp_by_game.values():
        if final_vp is None or final_vp == 0:
            draws += 1
        elif final_vp > 0:
            ussr_wins += 1
        else:
            us_wins += 1
    return ussr_wins, us_wins, draws


def run_matchup(
    collect_script: Path,
    ussr_model: Path,
    us_model: Path,
    games: int,
    seed: int,
) -> RunSummary:
    with tempfile.TemporaryDirectory(prefix="ts_ladder_", dir="/tmp") as tmpdir:
        out_path = Path(tmpdir) / "match.parquet"
        cmd = [
            "nice",
            "-n",
            "10",
            "bash",
            str(collect_script),
            "--games",
            str(games),
            "--seed",
            str(seed),
            "--ussr-model",
            str(ussr_model),
            "--us-model",
            str(us_model),
            "--out",
            str(out_path),
        ]
        subprocess.run(cmd, check=True)
        ussr_wins, us_wins, draws = summarize_parquet(out_path)
        return RunSummary(
            ussr_model=str(ussr_model),
            us_model=str(us_model),
            ussr_wins=ussr_wins,
            us_wins=us_wins,
            draws=draws,
            games=games,
            seed=seed,
            parquet_path=str(out_path),
        )


def build_output(checkpoints: list[Path], run_summaries: list[dict[str, object]], games: int) -> dict[str, object]:
    standings: dict[str, dict[str, object]] = {
        checkpoint_name(path): {
            "checkpoint": str(path),
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "games": 0,
        }
        for path in checkpoints
    }

    for match in run_summaries:
        for run in match["runs"]:
            ussr_name = run["ussr_name"]
            us_name = run["us_name"]
            ussr_wins = int(run["ussr_wins"])
            us_wins = int(run["us_wins"])
            draws = int(run["draws"])
            total_games = int(run["games"])

            standings[ussr_name]["wins"] += ussr_wins
            standings[ussr_name]["losses"] += us_wins
            standings[ussr_name]["draws"] += draws
            standings[ussr_name]["games"] += total_games

            standings[us_name]["wins"] += us_wins
            standings[us_name]["losses"] += ussr_wins
            standings[us_name]["draws"] += draws
            standings[us_name]["games"] += total_games

    ordered_standings = dict(
        sorted(
            standings.items(),
            key=lambda item: (
                -int(item[1]["wins"]),
                int(item[1]["losses"]),
                item[0],
            ),
        )
    )

    return {
        "games_per_side": games,
        "total_matches": len(run_summaries),
        "checkpoints": [str(path) for path in checkpoints],
        "matches": run_summaries,
        "standings": ordered_standings,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoints", nargs="+", required=True, help="List of .pt checkpoint paths.")
    parser.add_argument("--games", type=int, default=50, help="Games per side for each pairing.")
    parser.add_argument("--seed", type=int, default=12345, help="Base RNG seed.")
    parser.add_argument("--out", type=Path, default=Path("results/ladder.json"))
    parser.add_argument(
        "--collect-script",
        type=Path,
        default=Path("scripts/collect_cpp.sh"),
        help="Path to the native collection wrapper.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.games <= 0:
        raise ValueError("--games must be positive")

    checkpoints = [Path(path) for path in args.checkpoints]
    if len(checkpoints) < 2:
        raise ValueError("--checkpoints requires at least two paths")
    for checkpoint in checkpoints:
        if not checkpoint.exists():
            raise FileNotFoundError(checkpoint)

    collect_script = args.collect_script
    if not collect_script.exists():
        raise FileNotFoundError(collect_script)

    matches: list[dict[str, object]] = []
    match_index = 0
    for i, model_a in enumerate(checkpoints):
        for model_b in checkpoints[i + 1 :]:
            forward_seed = args.seed + match_index * 2
            reverse_seed = forward_seed + 1

            forward = run_matchup(
                collect_script=collect_script,
                ussr_model=model_a,
                us_model=model_b,
                games=args.games,
                seed=forward_seed,
            )
            reverse = run_matchup(
                collect_script=collect_script,
                ussr_model=model_b,
                us_model=model_a,
                games=args.games,
                seed=reverse_seed,
            )

            matches.append(
                {
                    "model_a": checkpoint_name(model_a),
                    "model_b": checkpoint_name(model_b),
                    "checkpoint_a": str(model_a),
                    "checkpoint_b": str(model_b),
                    "runs": [
                        {
                            "ussr_name": checkpoint_name(model_a),
                            "us_name": checkpoint_name(model_b),
                            "ussr_model": forward.ussr_model,
                            "us_model": forward.us_model,
                            "ussr_wins": forward.ussr_wins,
                            "us_wins": forward.us_wins,
                            "draws": forward.draws,
                            "games": forward.games,
                            "seed": forward.seed,
                        },
                        {
                            "ussr_name": checkpoint_name(model_b),
                            "us_name": checkpoint_name(model_a),
                            "ussr_model": reverse.ussr_model,
                            "us_model": reverse.us_model,
                            "ussr_wins": reverse.ussr_wins,
                            "us_wins": reverse.us_wins,
                            "draws": reverse.draws,
                            "games": reverse.games,
                            "seed": reverse.seed,
                        },
                    ],
                    "aggregate": {
                        checkpoint_name(model_a): forward.ussr_wins + reverse.us_wins,
                        checkpoint_name(model_b): forward.us_wins + reverse.ussr_wins,
                        "draws": forward.draws + reverse.draws,
                        "games": forward.games + reverse.games,
                    },
                }
            )
            match_index += 1

    output = build_output(checkpoints=checkpoints, run_summaries=matches, games=args.games)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
