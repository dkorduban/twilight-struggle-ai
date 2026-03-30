"""Filter a self-play parquet dataset to remove low-quality games.

Two filtering passes are applied in order:

1. **Early defcon1 removal** — remove any game where ``end_reason == 'defcon1'``
   AND the game ended on turn <= 2.  A nuclear war on turns 1-2 is almost
   certainly caused by a safety bug in the model (no COUP/EVENT DEFCON
   guard), not legitimate play.

2. **Excess defcon1 rate cap** — if the remaining defcon1 rate (fraction of
   games ending by defcon1) exceeds ``--max-defcon1-pct`` (default 25%),
   randomly drop excess defcon1 games to bring the rate back to the cap.

Usage
-----
    uv run python scripts/filter_bad_games.py \\
        --input data/combined_v18 \\
        --output data/combined_v18_filtered/filtered.parquet \\
        [--max-defcon1-pct 25]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import polars as pl


def load_parquet(input_path: str) -> pl.DataFrame:
    """Load one parquet file or all *.parquet files from a directory."""
    p = Path(input_path)
    if p.is_dir():
        files = sorted(p.glob("*.parquet"))
        if not files:
            print(f"ERROR: no .parquet files found in {p}", file=sys.stderr)
            sys.exit(1)
        return pl.concat([pl.read_parquet(f) for f in files])
    return pl.read_parquet(p)


def compute_game_summary(df: pl.DataFrame) -> pl.DataFrame:
    """Return one row per game_id with end_reason and max turn."""
    return (
        df.group_by("game_id")
        .agg(
            pl.col("end_reason").last().alias("end_reason"),
            pl.col("turn").max().alias("max_turn"),
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Filter bad games from a self-play parquet dataset."
    )
    parser.add_argument("--input", required=True, help="Input parquet file or directory.")
    parser.add_argument("--output", required=True, help="Output parquet file path.")
    parser.add_argument(
        "--max-defcon1-pct",
        type=float,
        default=25.0,
        help="Maximum allowed defcon1 end-reason rate (percent, default 25).",
    )
    args = parser.parse_args()

    print(f"Loading data from: {args.input}")
    df = load_parquet(args.input)

    total_rows = len(df)
    game_summary = compute_game_summary(df)
    total_games = len(game_summary)

    defcon1_total = (game_summary["end_reason"] == "defcon1").sum()
    defcon1_rate_before = 100.0 * defcon1_total / total_games if total_games > 0 else 0.0

    # --- Pass 1: remove very early defcon1 games (turn <= 2) ---
    early_defcon1_ids = (
        game_summary
        .filter(
            (pl.col("end_reason") == "defcon1") & (pl.col("max_turn") <= 2)
        )
        ["game_id"]
    )
    n_early = len(early_defcon1_ids)
    early_set = set(early_defcon1_ids.to_list())

    df = df.filter(~pl.col("game_id").is_in(early_set))
    game_summary = game_summary.filter(~pl.col("game_id").is_in(early_set))

    games_after_pass1 = len(game_summary)

    # --- Pass 2: cap excess defcon1 rate ---
    defcon1_after_pass1 = (game_summary["end_reason"] == "defcon1").sum()
    rate_after_pass1 = 100.0 * defcon1_after_pass1 / games_after_pass1 if games_after_pass1 > 0 else 0.0

    max_pct = args.max_defcon1_pct
    n_excess = 0

    if rate_after_pass1 > max_pct and games_after_pass1 > 0:
        # How many defcon1 games are allowed?
        # defcon1_kept / total_after_drop <= max_pct/100
        # Let K = defcon1 games to keep, N = non-defcon1 games (fixed).
        # K / (N + K) <= max_pct/100  =>  K <= N * max_pct / (100 - max_pct)
        non_defcon1 = games_after_pass1 - defcon1_after_pass1
        if max_pct >= 100.0:
            defcon1_to_keep = defcon1_after_pass1
        else:
            defcon1_to_keep = int(non_defcon1 * max_pct / (100.0 - max_pct))

        n_excess = max(0, defcon1_after_pass1 - defcon1_to_keep)

        if n_excess > 0:
            # Randomly sample which defcon1 games to drop.
            defcon1_game_ids = (
                game_summary
                .filter(pl.col("end_reason") == "defcon1")
                ["game_id"]
                .to_list()
            )
            # Deterministic shuffle via polars sort-by-hash for reproducibility.
            defcon1_id_df = pl.DataFrame({"game_id": defcon1_game_ids})
            defcon1_id_df = defcon1_id_df.with_columns(
                pl.col("game_id").hash(seed=42).alias("_sort_key")
            ).sort("_sort_key")
            ids_to_drop = set(defcon1_id_df["game_id"].head(n_excess).to_list())

            df = df.filter(~pl.col("game_id").is_in(ids_to_drop))
            game_summary = game_summary.filter(~pl.col("game_id").is_in(ids_to_drop))

    final_games = len(game_summary)
    defcon1_final = (game_summary["end_reason"] == "defcon1").sum()
    defcon1_rate_after = 100.0 * defcon1_final / final_games if final_games > 0 else 0.0
    final_rows = len(df)

    # --- Write output ---
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(str(output_path))

    # --- Summary ---
    print()
    print("=" * 60)
    print("Filter summary")
    print("=" * 60)
    print(f"  Input rows           : {total_rows:,}")
    print(f"  Total games (input)  : {total_games:,}")
    print(f"  Defcon1 rate (before): {defcon1_rate_before:.1f}%  ({defcon1_total} games)")
    print()
    print(f"  Removed — early defcon1 (turn <= 2) : {n_early:,} games")
    print(f"  Removed — excess rate cap ({max_pct:.0f}%)     : {n_excess:,} games")
    print()
    print(f"  Final games          : {final_games:,}")
    print(f"  Final rows           : {final_rows:,}")
    print(f"  Defcon1 rate (after) : {defcon1_rate_after:.1f}%  ({defcon1_final} games)")
    print()
    print(f"  Output written to    : {output_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
