"""Extract rows from games where the learned side (USSR) won.

Filters vsh (vs-heuristic) parquet files to keep only rows from games where
winner_side == 1 (USSR win). These contain the model's best demonstrated play
and provide a high-quality anchor dataset.

Usage:
    uv run python scripts/mine_winning_games.py \
        --gens 55-68 \
        --out data/curated/winning_games_v55_v68.parquet
"""
from __future__ import annotations

import argparse
import glob
import os
import sys
from pathlib import Path

import polars as pl


def _lower_priority() -> None:
    try:
        os.nice(10)
    except OSError:
        pass


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--gens",
        required=True,
        help="Generation range, e.g. '55-68' or '60,61,65'",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output parquet path.",
    )
    parser.add_argument(
        "--min-win-pct",
        type=float,
        default=0.0,
        help="Only include gens with benchmark win%% >= this (default: 0, include all).",
    )
    parser.add_argument(
        "--min-vp",
        type=int,
        default=0,
        help="Minimum final_vp for USSR wins to include (default: 0, include all wins).",
    )
    parser.add_argument(
        "--include-wargames",
        action="store_true",
        default=True,
        help="Also include wargames wins (VP threshold / Europe control) regardless of VP.",
    )
    parser.add_argument(
        "--data-dir",
        default="data/selfplay",
        help="Directory containing vsh parquet files.",
    )
    return parser.parse_args()


def _parse_gens(spec: str) -> list[int]:
    gens = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-", 1)
            gens.extend(range(int(lo), int(hi) + 1))
        else:
            gens.append(int(part))
    return sorted(set(gens))


def _find_vsh_file(data_dir: str, gen: int) -> Path | None:
    pattern = f"{data_dir}/learned_v{gen}_vs_heuristic_*.parquet"
    matches = sorted(glob.glob(pattern))
    return Path(matches[0]) if matches else None


def main() -> None:
    _lower_priority()
    args = _parse_args()
    gens = _parse_gens(args.gens)
    out_path = Path(args.out)

    # Load benchmark history for filtering
    bench = {}
    bench_path = Path("results/benchmark_history.json")
    if bench_path.exists():
        import json
        with bench_path.open() as f:
            bench = json.load(f)

    frames = []
    total_wins = 0
    total_rows = 0

    for gen in gens:
        pct = bench.get(f"v{gen}", {}).get("learned_vs_heuristic", 0)
        if pct < args.min_win_pct:
            print(f"v{gen}: skipped (bench {pct:.1f}% < {args.min_win_pct}%)")
            continue

        path = _find_vsh_file(args.data_dir, gen)
        if path is None:
            print(f"v{gen}: no vsh file found")
            continue

        df = pl.read_parquet(str(path))
        # Find winning game_ids with quality filters
        game_meta = df.select("game_id", "winner_side", "final_vp", "end_reason").unique(subset="game_id")
        ussr_wins = game_meta.filter(pl.col("winner_side") == 1)

        if args.min_vp > 0:
            # Keep games with VP above threshold OR wargames-type wins
            vp_ok = ussr_wins.filter(pl.col("final_vp") > args.min_vp)
            if args.include_wargames:
                wargames = ussr_wins.filter(
                    pl.col("end_reason").is_in(["vp_threshold", "europe_control", "vp"])
                )
                qualified = pl.concat([vp_ok, wargames]).unique(subset="game_id")
            else:
                qualified = vp_ok
        else:
            qualified = ussr_wins

        win_ids = qualified["game_id"]
        n_wins = len(win_ids)

        if n_wins == 0:
            print(f"v{gen}: 0 qualifying wins, skipped")
            continue

        # Filter to only winning game rows
        win_rows = df.filter(pl.col("game_id").is_in(win_ids))
        frames.append(win_rows)
        total_wins += n_wins
        total_rows += len(win_rows)
        print(f"v{gen}: {pct:5.1f}% bench, {n_wins} wins, {len(win_rows)} rows")

    if not frames:
        print("No winning games found!")
        sys.exit(1)

    merged = pl.concat(frames, how="vertical_relaxed")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    merged.write_parquet(str(out_path))

    print(f"\nWrote {total_rows:,} rows from {total_wins} winning games to {out_path}")
    print(f"Avg rows per winning game: {total_rows / total_wins:.0f}")


if __name__ == "__main__":
    main()
