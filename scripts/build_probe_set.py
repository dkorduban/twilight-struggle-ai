#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import polars as pl

CARD_SLOTS = 111
MODE_SLOTS = 5
STRATUM_COLUMNS = ["turn_bucket", "side_int", "defcon_bucket", "vp_bucket"]


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
    if vp < 0:
        return "neg"
    if vp > 0:
        return "pos"
    return "zero"


def _card_mask_from_hand(hand_card_ids: list[int] | None) -> list[bool]:
    if hand_card_ids is None:
        return [True] * CARD_SLOTS

    mask = [False] * CARD_SLOTS
    for raw_card_id in hand_card_ids:
        card_id = int(raw_card_id)
        if 1 <= card_id <= CARD_SLOTS:
            mask[card_id - 1] = True
    return mask


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a frozen JSD probe set from rollout parquet files"
    )
    parser.add_argument("--data-dir", type=str, default="data/ppo_rollout_combined")
    parser.add_argument("--out", type=str, default="data/probe_positions.parquet")
    parser.add_argument("--n", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


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

    required = {
        "influence",
        "cards",
        "scalars",
        "raw_turn",
        "side_int",
        "raw_defcon",
        "raw_vp",
    }
    optional = {"hand_card_ids", "mode_id"}

    frames: list[pl.DataFrame] = []
    for path in parquet_paths:
        try:
            schema = pl.read_parquet_schema(path)
        except Exception as exc:
            print(f"Skipping unreadable parquet {path}: {exc}", flush=True)
            continue

        available = set(schema.keys())
        if not required.issubset(available):
            continue

        columns = sorted(required | (optional & available))
        frame = pl.read_parquet(path, columns=columns)
        if "hand_card_ids" not in frame.columns:
            frame = frame.with_columns(pl.lit(None, dtype=pl.List(pl.Int64)).alias("hand_card_ids"))
        if "mode_id" not in frame.columns:
            frame = frame.with_columns(pl.lit(-1, dtype=pl.Int64).alias("mode_id"))
        frames.append(frame)

    if not frames:
        raise ValueError(f"No parquet files in {data_dir} contained the required probe columns")

    df = pl.concat(frames, how="vertical_relaxed")
    if len(df) == 0:
        raise ValueError(f"No probe rows found in {data_dir}")

    df = df.with_columns(
        pl.col("raw_turn").map_elements(_turn_bucket, return_dtype=pl.String).alias("turn_bucket"),
        pl.col("raw_defcon").map_elements(_defcon_bucket, return_dtype=pl.String).alias("defcon_bucket"),
        pl.col("raw_vp").map_elements(_vp_bucket, return_dtype=pl.String).alias("vp_bucket"),
        pl.col("hand_card_ids")
        .map_elements(_card_mask_from_hand, return_dtype=pl.List(pl.Boolean))
        .alias("card_mask"),
        pl.lit([True] * MODE_SLOTS, dtype=pl.List(pl.Boolean)).alias("mode_mask"),
    )

    sampled = _sample_stratified(df, n=n, seed=seed)
    sampled = sampled.select(
        "influence",
        "cards",
        "scalars",
        "card_mask",
        "mode_mask",
        "raw_turn",
        "side_int",
        "raw_defcon",
        "raw_vp",
        "mode_id",
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    sampled.write_parquet(out_path)
    return out_path


def _sample_stratified(df: pl.DataFrame, n: int, seed: int) -> pl.DataFrame:
    if n <= 0:
        raise ValueError(f"Probe set size must be positive, got {n}")

    groups = df.partition_by(STRATUM_COLUMNS, as_dict=True)
    ordered_keys = sorted(groups.keys(), key=lambda key: (key[0], key[1], key[2], key[3]))
    target = min(n, len(df))
    if target == 0:
        return df.head(0)

    counts = {key: 0 for key in ordered_keys}
    nonempty = [key for key in ordered_keys if len(groups[key]) > 0]
    initial_keys = nonempty
    if target < len(nonempty):
        initial_keys = sorted(nonempty, key=lambda key: (-len(groups[key]), key))[:target]

    for key in initial_keys:
        counts[key] = 1

    remaining = target - sum(counts.values())
    leftovers = {key: len(groups[key]) - counts[key] for key in ordered_keys}

    if remaining > 0:
        total_leftover = sum(max(0, leftovers[key]) for key in ordered_keys)
        if total_leftover > 0:
            fractional_allocations: list[tuple[float, int, tuple]] = []
            for key in ordered_keys:
                available = max(0, leftovers[key])
                if available == 0:
                    continue
                exact = remaining * (available / total_leftover)
                base = min(int(exact), available)
                counts[key] += base
                leftovers[key] -= base
                fractional_allocations.append((exact - base, available, key))

            assigned = sum(counts.values())
            remainder = target - assigned
            for _, _, key in sorted(fractional_allocations, key=lambda item: (-item[0], -item[1], item[2])):
                if remainder == 0:
                    break
                if leftovers[key] <= 0:
                    continue
                counts[key] += 1
                leftovers[key] -= 1
                remainder -= 1

            if remainder > 0:
                for key in sorted(ordered_keys, key=lambda item: (-leftovers[item], item)):
                    if remainder == 0:
                        break
                    if leftovers[key] <= 0:
                        continue
                    counts[key] += 1
                    leftovers[key] -= 1
                    remainder -= 1

    sampled_frames: list[pl.DataFrame] = []
    for idx, key in enumerate(ordered_keys):
        count = counts[key]
        if count <= 0:
            continue
        frame = groups[key]
        if count >= len(frame):
            sampled = frame
        else:
            sampled = frame.sample(n=count, seed=seed + idx, shuffle=True)
        sampled_frames.append(sampled)

    if not sampled_frames:
        return df.head(0)

    sampled = pl.concat(sampled_frames, how="vertical_relaxed")
    return sampled.sort(["raw_turn", "side_int", "raw_defcon", "raw_vp", "mode_id"])


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
