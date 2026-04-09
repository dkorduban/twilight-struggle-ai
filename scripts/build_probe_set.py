#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import polars as pl

CARD_SLOTS = 111
MODE_SLOTS = 5
N_STRATA = 18


def _turn_bucket(turn: int) -> str:
    if turn <= 3:
        return "early"
    if turn <= 7:
        return "mid"
    return "late"


def _defcon_bucket(defcon: int) -> str:
    if defcon <= 2:
        return "1-2"
    if defcon == 3:
        return "3"
    return "4-5"


def _card_mask_from_hand(hand_card_ids: list[int] | None) -> list[bool]:
    if hand_card_ids is None:
        return [True] * CARD_SLOTS

    mask = [False] * CARD_SLOTS
    for card_id in hand_card_ids:
        if 1 <= int(card_id) <= CARD_SLOTS:
            mask[int(card_id) - 1] = True
    return mask


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build a frozen JSD probe set from rollout parquet files")
    p.add_argument("--data-dir", type=str, default="data/ppo_rollout_combined")
    p.add_argument("--out", type=str, default="data/probe_positions.parquet")
    p.add_argument("--n", type=int, default=1000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--force", action="store_true")
    return p.parse_args()


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
        raise FileExistsError(f"Refusing to overwrite existing probe set: {out_path}")

    parquet_paths = sorted(data_dir.glob("*.parquet"))
    if not parquet_paths:
        raise FileNotFoundError(f"No *.parquet files found in {data_dir}")

    needed_columns = [
        "influence",
        "cards",
        "scalars",
        "raw_turn",
        "side_int",
        "raw_defcon",
        "raw_vp",
        "hand_card_ids",
        "mode_id",
    ]

    frames: list[pl.DataFrame] = []
    for path in parquet_paths:
        try:
            available = set(pl.read_parquet_schema(path).keys())
        except Exception as e:
            print(f"  Skipping {path}: {e}", flush=True)
            continue
        present = [col for col in needed_columns if col in available]
        if not {"influence", "cards", "scalars", "raw_turn", "side_int", "raw_defcon", "raw_vp", "mode_id"}.issubset(available):
            continue
        frame = pl.read_parquet(path, columns=present)
        if "hand_card_ids" not in frame.columns:
            frame = frame.with_columns(
                pl.lit([], dtype=pl.List(pl.Int64)).alias("hand_card_ids")
            )
        frames.append(frame)

    if not frames:
        raise ValueError(f"No parquet files in {data_dir} contained the required probe columns")

    df = pl.concat(frames, how="vertical_relaxed")
    if len(df) == 0:
        raise ValueError(f"No probe rows found in {data_dir}")

    df = df.with_columns(
        pl.col("raw_turn").map_elements(_turn_bucket, return_dtype=pl.String).alias("turn_bucket"),
        pl.col("raw_defcon").map_elements(_defcon_bucket, return_dtype=pl.String).alias("defcon_bucket"),
    )

    grouped = df.partition_by(["turn_bucket", "side_int", "defcon_bucket"], as_dict=True)
    base_per_stratum = n // N_STRATA
    sample_counts: dict[tuple, int] = {}
    total_selected = 0

    ordered_keys = sorted(grouped, key=lambda key: (-len(grouped[key]), key))
    for key in ordered_keys:
        count = min(base_per_stratum, len(grouped[key]))
        sample_counts[key] = count
        total_selected += count

    remainder = min(n, len(df)) - total_selected
    while remainder > 0:
        progressed = False
        for key in ordered_keys:
            available = len(grouped[key]) - sample_counts[key]
            if available <= 0:
                continue
            sample_counts[key] += 1
            remainder -= 1
            progressed = True
            if remainder == 0:
                break
        if not progressed:
            break

    sampled_frames: list[pl.DataFrame] = []
    for idx, key in enumerate(ordered_keys):
        count = sample_counts[key]
        if count <= 0:
            continue
        frame = grouped[key]
        if count >= len(frame):
            sampled = frame
        else:
            sampled = frame.sample(n=count, seed=seed + idx, shuffle=True)
        sampled_frames.append(sampled)

    sampled_df = pl.concat(sampled_frames, how="vertical_relaxed") if sampled_frames else df.head(0)
    sampled_df = sampled_df.with_columns(
        pl.col("hand_card_ids")
        .map_elements(_card_mask_from_hand, return_dtype=pl.List(pl.Boolean))
        .alias("card_mask"),
        pl.lit([True] * MODE_SLOTS, dtype=pl.List(pl.Boolean)).alias("mode_mask"),
    ).select(
        "influence",
        "cards",
        "scalars",
        "raw_turn",
        "side_int",
        "raw_defcon",
        "raw_vp",
        "hand_card_ids",
        "mode_id",
        "card_mask",
        "mode_mask",
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    sampled_df.write_parquet(out_path)
    return out_path


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
