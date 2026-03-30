"""Filter a dataset directory by game quality criteria.

Removes games that end too early (shallow signal) or by specific end reasons
that indicate degenerate play. Produces a new directory of filtered parquet files.

Usage::

    uv run python scripts/filter_dataset.py \\
        --src data/combined_v13 \\
        --dst data/combined_v13_filtered \\
        --min-end-turn 4

Filters applied (in order):
  1. --min-end-turn N     : drop games where end_turn < N (default 4)
  2. --drop-end-reason R  : drop games with end_reason matching R (repeatable)
                            e.g. --drop-end-reason defcon1

Files without end_turn / end_reason columns (old schema) are kept as-is
unless --skip-no-schema is passed.
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)
log = logging.getLogger(__name__)


def filter_file(
    src: Path,
    dst: Path,
    min_end_turn: int,
    drop_end_reasons: set[str],
    skip_no_schema: bool,
) -> dict:
    import polars as pl

    df = pl.read_parquet(src)
    n_rows_in = len(df)

    has_end_turn = "end_turn" in df.columns
    has_end_reason = "end_reason" in df.columns

    if not has_end_turn and not has_end_reason:
        if skip_no_schema:
            log.info("SKIP (no schema): %s", src.name)
            return {"file": src.name, "rows_in": n_rows_in, "rows_out": 0, "skipped": True}
        # Keep as-is
        dst.parent.mkdir(parents=True, exist_ok=True)
        import shutil
        shutil.copy2(src, dst)
        log.info("COPY (no schema): %s  rows=%d", src.name, n_rows_in)
        return {"file": src.name, "rows_in": n_rows_in, "rows_out": n_rows_in, "skipped": False}

    # Build per-game filter mask
    agg_cols = ["game_id"]
    if has_end_turn:
        agg_cols.append("end_turn")
    if has_end_reason:
        agg_cols.append("end_reason")

    agg_exprs = [pl.first(c) for c in agg_cols[1:]]  # first() for all non-game_id cols
    per_game = df.group_by("game_id").agg(agg_exprs)

    keep_mask = pl.lit(True)
    if has_end_turn and min_end_turn > 1:
        keep_mask = keep_mask & (pl.col("end_turn") >= min_end_turn)
    if has_end_reason and drop_end_reasons:
        keep_mask = keep_mask & (~pl.col("end_reason").is_in(list(drop_end_reasons)))

    kept_games = per_game.filter(keep_mask).select("game_id")
    n_games_in = len(per_game)
    n_games_out = len(kept_games)

    df_filtered = df.join(kept_games, on="game_id", how="inner")
    n_rows_out = len(df_filtered)

    dst.parent.mkdir(parents=True, exist_ok=True)
    df_filtered.write_parquet(str(dst))

    log.info(
        "%-60s  games %d→%d (%.0f%%)  rows %d→%d (%.0f%%)",
        src.name,
        n_games_in, n_games_out, 100 * n_games_out / max(n_games_in, 1),
        n_rows_in, n_rows_out, 100 * n_rows_out / max(n_rows_in, 1),
    )
    return {
        "file": src.name,
        "rows_in": n_rows_in,
        "rows_out": n_rows_out,
        "games_in": n_games_in,
        "games_out": n_games_out,
        "skipped": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Filter a dataset directory by game quality.")
    parser.add_argument("--src", required=True, help="Source directory of parquet files.")
    parser.add_argument("--dst", required=True, help="Destination directory.")
    parser.add_argument(
        "--min-end-turn", type=int, default=4,
        help="Drop games with end_turn < N (default: 4).",
    )
    parser.add_argument(
        "--drop-end-reason", action="append", dest="drop_end_reasons", default=[],
        metavar="REASON",
        help="Drop games with this end_reason (repeatable). E.g. --drop-end-reason defcon1",
    )
    parser.add_argument(
        "--skip-no-schema", action="store_true",
        help="Skip (don't copy) files that lack end_turn/end_reason columns.",
    )
    args = parser.parse_args(argv)

    src_dir = Path(args.src)
    dst_dir = Path(args.dst)

    if not src_dir.is_dir():
        log.error("Source directory not found: %s", src_dir)
        return 1

    parquet_files = sorted(src_dir.glob("*.parquet"))
    if not parquet_files:
        log.error("No parquet files in %s", src_dir)
        return 1

    dst_dir.mkdir(parents=True, exist_ok=True)
    drop_reasons = set(args.drop_end_reasons)

    log.info(
        "Filtering %d files: min_end_turn=%d  drop_reasons=%s",
        len(parquet_files), args.min_end_turn,
        drop_reasons or "(none)",
    )

    totals = {"rows_in": 0, "rows_out": 0, "games_in": 0, "games_out": 0}
    for src_file in parquet_files:
        dst_file = dst_dir / src_file.name
        result = filter_file(
            src_file, dst_file,
            min_end_turn=args.min_end_turn,
            drop_end_reasons=drop_reasons,
            skip_no_schema=args.skip_no_schema,
        )
        if not result.get("skipped"):
            totals["rows_in"] += result.get("rows_in", 0)
            totals["rows_out"] += result.get("rows_out", 0)
            totals["games_in"] += result.get("games_in", 0)
            totals["games_out"] += result.get("games_out", 0)

    if totals["rows_in"]:
        log.info(
            "TOTAL: rows %d→%d (%.1f%%)  games %d→%d (%.1f%%)",
            totals["rows_in"], totals["rows_out"],
            100 * totals["rows_out"] / totals["rows_in"],
            totals["games_in"], totals["games_out"],
            100 * totals["games_out"] / totals["games_in"],
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
