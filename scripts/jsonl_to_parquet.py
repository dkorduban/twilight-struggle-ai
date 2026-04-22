"""Convert C++ self-play JSONL rows to a Parquet file for training.

The C++ tool (ts_collect_selfplay_rows_jsonl) emits one JSON object per line
with the same schema as Python-collected self-play data (see
python/tsrl/selfplay/collector.py for the canonical field list).

This converter reads one or more JSONL files and writes a single Parquet file
compatible with train_baseline.py.

Usage::

    uv run python scripts/jsonl_to_parquet.py --input rows.jsonl --out data.parquet

    # Multiple input files:
    uv run python scripts/jsonl_to_parquet.py \\
        --input rows_0000.jsonl rows_0001.jsonl \\
        --out data.parquet

    # Or glob:
    uv run python scripts/jsonl_to_parquet.py \\
        --input-dir /tmp/cpp_chunks \\
        --out data.parquet
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

import polars as pl

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)
log = logging.getLogger(__name__)

# Columns that store list[int] and must be stored as Polars Array types.
# Each entry: (column_name, list_length).
_ARRAY_COLUMNS: list[tuple[str, int]] = [
    ("ussr_influence", 86),
    ("us_influence", 86),
    ("discard_mask", 112),
    ("removed_mask", 112),
    ("actor_known_in", 112),
    ("actor_known_not_in", 112),
    ("actor_possible", 112),
    ("opp_known_in", 112),
    ("opp_known_not_in", 112),
    ("opp_possible", 112),
    ("lbl_actor_hand", 112),
    ("lbl_card_quality", 112),
    ("lbl_opponent_possible", 112),
]

_ARRAY_COLUMN_NAMES: frozenset[str] = frozenset(c for c, _ in _ARRAY_COLUMNS)

_SUBFRAME_NUMERIC_DEFAULTS: dict[str, int] = {
    "frame_kind": 0,
    "source_card": 0,
    "parent_card": 0,
    "step_index": 0,
    "total_steps": 1,
    "budget_remaining": 0,
    "stack_depth": 0,
    "criteria_bits": 0,
    "eligible_n": 0,
    "chosen_option_index": 0,
    "chosen_card": 0,
    "chosen_country": 0,
    "target_head": 0,
}

_SUBFRAME_LIST_COLUMNS: tuple[str, ...] = ("eligible_cards", "eligible_countries")


def _load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open() as fh:
        for lineno, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                log.warning("skip malformed line %d in %s: %s", lineno, path, exc)
    return rows


def _rows_to_polars(rows: list[dict]) -> pl.DataFrame:
    """Convert list of row dicts to a Polars DataFrame with correct types."""
    if not rows:
        raise ValueError("no rows to convert")

    # Separate scalar and array columns.
    scalar_cols: dict[str, list] = {}
    array_cols: dict[str, list[list[int]]] = {name: [] for name, _ in _ARRAY_COLUMNS}

    for row in rows:
        row.setdefault("row_kind", "ar")
        for col, default in _SUBFRAME_NUMERIC_DEFAULTS.items():
            row.setdefault(col, default)
        for col in _SUBFRAME_LIST_COLUMNS:
            row.setdefault(col, [])
        for col, _ in _ARRAY_COLUMNS:
            val = row.get(col)
            if val is None:
                val = []
            array_cols[col].append(list(val))
        for key, val in row.items():
            if key in _ARRAY_COLUMN_NAMES:
                continue
            if key not in scalar_cols:
                scalar_cols[key] = []
            scalar_cols[key].append(val)

    # Build scalar DataFrame.
    df = pl.DataFrame(scalar_cols)

    # Add array columns as pl.Array (fixed-size list).
    for col, length in _ARRAY_COLUMNS:
        series = pl.Series(col, array_cols[col], dtype=pl.List(pl.Int32)).cast(
            pl.Array(pl.Int32, length)
        )
        df = df.with_columns(series)
    df = _with_subframe_defaults(df)

    return df


def _cast_array_columns(df: pl.DataFrame) -> pl.DataFrame:
    """Cast list columns to fixed-size Array types for consistent Parquet schema."""
    for col, length in _ARRAY_COLUMNS:
        if col in df.columns:
            dtype = df[col].dtype
            if dtype == pl.List(pl.Int64):
                df = df.with_columns(pl.col(col).cast(pl.List(pl.Int32)))
            if df[col].dtype != pl.Array(pl.Int32, length):
                try:
                    df = df.with_columns(pl.col(col).cast(pl.Array(pl.Int32, length)))
                except Exception:
                    pass  # leave as list if cast fails
    return df


def _with_subframe_defaults(df: pl.DataFrame) -> pl.DataFrame:
    """Ensure old JSONL and new sub-frame JSONL write a uniform Parquet schema."""
    if "row_kind" not in df.columns:
        df = df.with_columns(pl.lit("ar").alias("row_kind"))
    exprs = []
    for col, default in _SUBFRAME_NUMERIC_DEFAULTS.items():
        if col not in df.columns:
            exprs.append(pl.lit(default, dtype=pl.Int16).alias(col))
        else:
            exprs.append(pl.col(col).fill_null(default).cast(pl.Int16).alias(col))
    if exprs:
        df = df.with_columns(exprs)
    for col in _SUBFRAME_LIST_COLUMNS:
        if col not in df.columns:
            df = df.with_columns(
                pl.Series(col, [[] for _ in range(len(df))], dtype=pl.List(pl.Int32))
            )
        else:
            df = df.with_columns(pl.col(col).cast(pl.List(pl.Int32)).alias(col))
    return df


def convert(
    input_paths: list[Path],
    output_path: Path,
) -> int:
    """Convert JSONL files to Parquet. Returns total row count.

    Uses pl.read_ndjson per chunk for speed — avoids Python-dict intermediary.
    """
    chunks: list[pl.DataFrame] = []
    total = 0
    for path in input_paths:
        try:
            df = pl.read_ndjson(path)
            df = _cast_array_columns(df)
            df = _with_subframe_defaults(df)
            total += len(df)
            chunks.append(df)
            log.info("loaded %d rows from %s (running total: %d)", len(df), path, total)
        except Exception as exc:
            log.warning("failed to read %s with ndjson, falling back to manual: %s", path, exc)
            rows = _load_jsonl(path)
            if rows:
                df = _rows_to_polars(rows)
                total += len(df)
                chunks.append(df)
                log.info("loaded %d rows from %s (fallback, running total: %d)", len(df), path, total)

    if not chunks:
        log.error("no rows loaded from any input file")
        return 0

    log.info("concatenating %d chunks (%d total rows) ...", len(chunks), total)
    df = pl.concat(chunks, how="diagonal_relaxed")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(str(output_path))
    log.info("wrote %d rows to %s", len(df), output_path)
    return len(df)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        nargs="+",
        type=Path,
        default=[],
        help="One or more JSONL input files.",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=None,
        help="Directory of *.jsonl files to process.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        required=True,
        help="Output Parquet file path.",
    )
    args = parser.parse_args(argv)

    input_paths: list[Path] = list(args.input)
    if args.input_dir is not None:
        input_paths.extend(sorted(args.input_dir.glob("*.jsonl")))

    if not input_paths:
        parser.error("provide at least one --input file or --input-dir")

    n_rows = convert(input_paths, args.out)
    return 0 if n_rows > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
