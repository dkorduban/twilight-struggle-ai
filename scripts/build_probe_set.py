#!/usr/bin/env python3
"""Build a frozen probe position set from PPO rollout parquet files."""

from __future__ import annotations

import argparse
from pathlib import Path

import polars as pl

CARD_SLOTS = 111
MODE_SLOTS = 5


def _turn_bucket(turn: int) -> str:
    if turn <= 3:
        return "early"
    if turn <= 7:
        return "mid"
    return "late"


def _defcon_bucket(defcon: int) -> str:
    if defcon <= 2:
        return "low"
    if defcon == 3:
        return "mid"
    return "high"


def _vp_bucket(vp: int) -> str:
    if vp <= -7:
        return "us_ahead"
    if vp >= 7:
        return "ussr_ahead"
    return "close"


def _hand_to_card_mask(hand_card_ids: list[int] | None) -> list[bool]:
    if hand_card_ids is None:
        return [True] * CARD_SLOTS
    mask = [False] * CARD_SLOTS
    for card_id in hand_card_ids:
        idx = int(card_id) - 1
        if 0 <= idx < CARD_SLOTS:
            mask[idx] = True
    return mask


def _all_true_mode_mask() -> list[bool]:
    return [True] * MODE_SLOTS


def _source_paths(data_dir: Path) -> list[Path]:
    paths = sorted(data_dir.glob("*.parquet"))
    if not paths:
        raise FileNotFoundError(f"No *.parquet files found in {data_dir}")
    return paths


def _load_strata_index(data_dir: Path) -> pl.DataFrame:
    """Load only scalar columns needed for stratified sampling + global row index.

    Two-pass design: strata index uses <1% of the memory of the full dataset.
    """
    scalar_cols = {"raw_turn", "side_int", "raw_defcon", "raw_vp", "mode_id"}
    paths = _source_paths(data_dir)

    frames: list[pl.DataFrame] = []
    offset = 0
    for path in paths:
        available = set(pl.read_parquet_schema(path).keys())
        cols = sorted(scalar_cols & available)
        f = pl.read_parquet(path, columns=cols).with_row_index(name="_local_idx")
        f = f.with_columns(
            (pl.col("_local_idx") + offset).alias("row_idx"),
            pl.lit(str(path)).alias("_src_path"),
        ).drop("_local_idx")
        offset += len(f)
        frames.append(f)

    frame = pl.concat(frames, how="vertical_relaxed")
    for column in ("raw_turn", "side_int", "raw_defcon", "raw_vp"):
        if column not in frame.columns:
            raise ValueError(f"Source parquet missing required column {column!r}")
    if "mode_id" not in frame.columns:
        frame = frame.with_columns(pl.lit(-1, dtype=pl.Int32).alias("mode_id"))
    return frame


def _load_full_rows_for_indices(data_dir: Path, selected_idx: set[int]) -> pl.DataFrame:
    """Load full feature columns for a specific set of global row indices."""
    needed_cols = {"influence", "cards", "scalars", "raw_turn", "side_int",
                   "raw_defcon", "raw_vp", "hand_card_ids", "mode_id"}
    paths = _source_paths(data_dir)

    frames: list[pl.DataFrame] = []
    offset = 0
    for path in paths:
        available = set(pl.read_parquet_schema(path).keys())
        cols = sorted(needed_cols & available)
        f = pl.read_parquet(path, columns=cols).with_row_index(name="_local_idx")
        n_rows = len(f)
        local_needed = [i - offset for i in selected_idx if offset <= i < offset + n_rows]
        if local_needed:
            f = f.filter(pl.col("_local_idx").is_in(local_needed))
            f = f.with_columns((pl.col("_local_idx") + offset).alias("row_idx")).drop("_local_idx")
            frames.append(f)
        offset += n_rows

    if not frames:
        return pl.DataFrame()
    frame = pl.concat(frames, how="vertical_relaxed")
    if "hand_card_ids" not in frame.columns:
        frame = frame.with_columns(pl.lit(None, dtype=pl.List(pl.Int32)).alias("hand_card_ids"))
    if "mode_id" not in frame.columns:
        frame = frame.with_columns(pl.lit(-1, dtype=pl.Int32).alias("mode_id"))
    return frame


def _allocate_counts(group_sizes: dict[str, int], n: int) -> dict[str, int]:
    if not group_sizes:
        return {}

    total_rows = sum(group_sizes.values())
    if n >= total_rows:
        return dict(group_sizes)

    allocations = {key: 0 for key in group_sizes}
    ordered = sorted(group_sizes)
    remaining = n

    if n >= len(ordered):
        for key in ordered:
            allocations[key] = 1
            remaining -= 1

    spare_total = sum(max(0, group_sizes[key] - allocations[key]) for key in ordered)
    if remaining <= 0 or spare_total <= 0:
        return allocations

    fractional: list[tuple[float, str]] = []
    for key in ordered:
        spare = max(0, group_sizes[key] - allocations[key])
        if spare == 0:
            continue
        raw_share = remaining * (spare / spare_total)
        add = min(spare, int(raw_share))
        allocations[key] += add
        fractional.append((raw_share - add, key))

    used = sum(allocations.values())
    remaining = n - used
    for _, key in sorted(fractional, key=lambda item: (-item[0], item[1])):
        if remaining <= 0:
            break
        if allocations[key] < group_sizes[key]:
            allocations[key] += 1
            remaining -= 1

    return allocations


def build_probe_set(
    data_dir: str | Path,
    out_path: str | Path,
    n: int = 1000,
    seed: int = 42,
    force: bool = False,
) -> Path:
    data_dir = Path(data_dir)
    out_path = Path(out_path)
    if out_path.exists() and not force:
        raise FileExistsError(f"{out_path} already exists; pass --force to overwrite")

    # Pass 1: load only scalar columns for stratified sampling (memory-efficient).
    index_frame = _load_strata_index(data_dir)
    index_frame = index_frame.with_columns(
        pl.col("raw_turn").map_elements(_turn_bucket, return_dtype=pl.String).alias("_tb"),
        pl.col("side_int").cast(pl.String).alias("_si"),
        pl.col("raw_defcon").map_elements(_defcon_bucket, return_dtype=pl.String).alias("_db"),
        pl.col("raw_vp").map_elements(_vp_bucket, return_dtype=pl.String).alias("_vb"),
    ).with_columns(
        (pl.col("_tb") + "|" + pl.col("_si") + "|" + pl.col("_db") + "|" + pl.col("_vb")).alias("_stratum")
    )

    group_sizes = {
        row["_stratum"]: row["count"]
        for row in index_frame.group_by("_stratum").agg(pl.len().alias("count")).to_dicts()
    }
    allocations = _allocate_counts(group_sizes, n)

    # Sample row_idx values per stratum.
    selected_indices: list[int] = []
    for idx, (stratum_key, want) in enumerate(sorted(allocations.items())):
        if want <= 0:
            continue
        group = index_frame.filter(pl.col("_stratum") == stratum_key)
        if want >= len(group):
            chosen = group
        else:
            chosen = group.sample(n=want, seed=seed + idx, shuffle=True)
        selected_indices.extend(chosen["row_idx"].to_list())

    selected_indices_set = set(selected_indices)

    # Pass 2: load full feature columns only for the selected row indices.
    selected = _load_full_rows_for_indices(data_dir, selected_indices_set).sort("row_idx")

    # Build card_mask and mode_mask.
    if "hand_card_ids" in selected.columns:
        selected = selected.with_columns(
            pl.col("hand_card_ids")
            .map_elements(_hand_to_card_mask, return_dtype=pl.List(pl.Boolean))
            .alias("card_mask")
        )
    else:
        selected = selected.with_columns(
            pl.Series("card_mask", [[True] * CARD_SLOTS] * len(selected))
        )
    selected = selected.with_columns(
        pl.Series("mode_mask", [[True] * MODE_SLOTS] * len(selected))
    )

    output = selected.select(
        "influence", "cards", "scalars",
        "card_mask", "mode_mask",
        "raw_turn", "side_int", "raw_defcon", "raw_vp", "mode_id",
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    output.write_parquet(out_path)
    return out_path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build a frozen JSD probe set from PPO rollout parquet")
    p.add_argument("--data-dir", required=True, help="Directory containing rollout parquet files")
    p.add_argument("--out", required=True, help="Output probe parquet path")
    p.add_argument("--n", type=int, default=1000, help="Number of probe positions to sample")
    p.add_argument("--seed", type=int, default=42, help="Sampling seed")
    p.add_argument("--force", action="store_true", help="Overwrite output parquet if it exists")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    out_path = build_probe_set(
        data_dir=args.data_dir,
        out_path=args.out,
        n=args.n,
        seed=args.seed,
        force=args.force,
    )
    print(f"Wrote probe set to {out_path}")


if __name__ == "__main__":
    main()
