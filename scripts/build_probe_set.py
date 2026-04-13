#!/usr/bin/env python3
"""Build a frozen probe position set from PPO rollout parquet files."""

from __future__ import annotations

import argparse
import random
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


def _load_source_rows(data_dir: Path) -> pl.DataFrame:
    paths = sorted(data_dir.glob("*.parquet"))
    if not paths:
        raise FileNotFoundError(f"No *.parquet files found in {data_dir}")

    needed_cols = {
        "influence",
        "cards",
        "scalars",
        "raw_turn",
        "side_int",
        "raw_defcon",
        "raw_vp",
        "hand_card_ids",
        "mode_id",
    }

    frames: list[pl.DataFrame] = []
    for path in paths:
        available = set(pl.read_parquet_schema(path).keys())
        cols = sorted(needed_cols & available)
        frames.append(pl.read_parquet(path, columns=cols))

    frame = pl.concat(frames, how="vertical_relaxed")
    for column in ("influence", "cards", "scalars"):
        if column not in frame.columns:
            raise ValueError(f"Source parquet missing required column {column!r}")
    for column in ("raw_turn", "side_int", "raw_defcon", "raw_vp"):
        if column not in frame.columns:
            raise ValueError(f"Source parquet missing required column {column!r}")

    if "hand_card_ids" not in frame.columns:
        frame = frame.with_columns(
            pl.lit(None, dtype=pl.List(pl.Int32)).alias("hand_card_ids"),
        )
    if "mode_id" not in frame.columns:
        frame = frame.with_columns(pl.lit(-1, dtype=pl.Int32).alias("mode_id"))

    return frame.with_row_index(name="row_idx")


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

    frame = _load_source_rows(data_dir)
    rows = frame.to_dicts()
    strata: dict[str, list[dict]] = {}
    for row in rows:
        key = "|".join(
            (
                _turn_bucket(int(row["raw_turn"])),
                str(int(row["side_int"])),
                _defcon_bucket(int(row["raw_defcon"])),
                _vp_bucket(int(row["raw_vp"])),
            )
        )
        strata.setdefault(key, []).append(row)

    allocations = _allocate_counts({key: len(items) for key, items in strata.items()}, n)
    rng = random.Random(seed)

    selected_rows: list[dict] = []
    for key in sorted(strata):
        group = strata[key]
        want = allocations.get(key, 0)
        if want <= 0:
            continue
        if want >= len(group):
            chosen = list(group)
        else:
            chosen = rng.sample(group, want)
        selected_rows.extend(chosen)

    selected_rows.sort(key=lambda row: int(row["row_idx"]))
    out_rows = []
    for row in selected_rows:
        out_rows.append(
            {
                "influence": row["influence"],
                "cards": row["cards"],
                "scalars": row["scalars"],
                "card_mask": _hand_to_card_mask(row.get("hand_card_ids")),
                "mode_mask": _all_true_mode_mask(),
                "raw_turn": int(row["raw_turn"]),
                "side_int": int(row["side_int"]),
                "raw_defcon": int(row["raw_defcon"]),
                "raw_vp": int(row["raw_vp"]),
                "mode_id": int(row.get("mode_id", -1)),
            }
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pl.DataFrame(out_rows).write_parquet(out_path)
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
