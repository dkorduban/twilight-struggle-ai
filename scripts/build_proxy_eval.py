#!/usr/bin/env python3
"""Build Phase 5 proxy eval set from the deterministic val split.

Extracts val rows (by game_id hash, same logic as TS_SelfPlayDataset.deterministic_split)
and saves them as a standalone parquet file. These rows are then EXCLUDED from training
so the proxy eval is a true held-out set.

Usage:
    uv run python scripts/build_proxy_eval.py \
        --data-dir data/v3_selfplay_05M_v2 \
        --out data/proxy_eval_v3.parquet \
        --val-fraction 0.1

Produces:
    data/proxy_eval_v3.parquet          — held-out eval rows
    data/v3_selfplay_05M_v2/EXCLUDE_GAME_IDS.txt  — game_ids to exclude from training
"""

import argparse
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data-dir", required=True, help="Source parquet directory")
    p.add_argument("--out", required=True, help="Output proxy eval parquet path")
    p.add_argument("--val-fraction", type=float, default=0.10,
                   help="Fraction of games to hold out (default 0.10)")
    args = p.parse_args()

    import polars as pl
    import glob, time

    paths = sorted(glob.glob(os.path.join(args.data_dir, "*.parquet")))
    if not paths:
        print(f"No parquet files in {args.data_dir}")
        sys.exit(1)

    print(f"Loading {len(paths)} files from {args.data_dir}...")
    t0 = time.time()
    df = pl.concat([pl.read_parquet(p) for p in paths])
    print(f"Loaded {len(df):,} rows in {time.time()-t0:.1f}s")

    if "game_id" not in df.columns:
        print("ERROR: 'game_id' column required for deterministic split")
        sys.exit(1)

    # Same hash logic as TS_SelfPlayDataset.deterministic_split
    denominator = max(1, round(1.0 / args.val_fraction))
    unique_ids = df["game_id"].unique().to_list()

    val_games = set()
    for gid in unique_ids:
        h = int(hashlib.md5(str(gid).encode()).hexdigest(), 16)
        if h % denominator == 0:
            val_games.add(gid)

    train_games = set(unique_ids) - val_games
    print(f"Games: {len(unique_ids):,} total → {len(train_games):,} train, {len(val_games):,} val ({args.val_fraction:.0%})")

    proxy_df = df.filter(pl.col("game_id").is_in(list(val_games)))
    train_df = df.filter(pl.col("game_id").is_in(list(train_games)))

    print(f"Proxy eval: {len(proxy_df):,} rows | Training: {len(train_df):,} rows")

    # Write proxy eval
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    proxy_df.write_parquet(args.out)
    print(f"Wrote proxy eval → {args.out}")

    # Write exclude list alongside the data so training scripts can read it
    exclude_path = os.path.join(args.data_dir, "EXCLUDE_GAME_IDS.txt")
    with open(exclude_path, "w") as f:
        for gid in sorted(val_games):
            f.write(f"{gid}\n")
    print(f"Wrote {len(val_games):,} excluded game_ids → {exclude_path}")

    # Distribution
    dist = proxy_df.group_by(["turn", "phasing"]).len().sort(["turn", "phasing"])
    print(f"\nProxy eval distribution ({len(proxy_df):,} rows):")
    print(dist)


if __name__ == "__main__":
    main()
