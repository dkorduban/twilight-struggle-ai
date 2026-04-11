#!/usr/bin/env python3
"""Assemble combined PPO rollout dataset from multiple rollout directories."""

import argparse
import glob
import os
import sys

import polars as pl


def main():
    p = argparse.ArgumentParser(description="Merge PPO rollout parquets into combined dataset")
    p.add_argument("--rollout-dirs", nargs="+", required=True, help="Rollout directories to merge")
    p.add_argument("--out", required=True, help="Output parquet path")
    args = p.parse_args()

    dfs = []
    for d in args.rollout_dirs:
        files = sorted(glob.glob(os.path.join(d, "rollout_iter_*.parquet")))
        if not files:
            print(f"WARNING: No parquet files found in {d}", file=sys.stderr)
            continue
        print(f"{d}: {len(files)} files")
        for f in files:
            dfs.append(pl.read_parquet(f))

    if not dfs:
        print("ERROR: No data found", file=sys.stderr)
        sys.exit(1)

    combined = pl.concat(dfs, how="diagonal")
    print(f"Combined rows: {len(combined):,}")
    print(f"Columns: {combined.columns}")

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    combined.write_parquet(args.out)
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
