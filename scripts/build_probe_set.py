#!/usr/bin/env python3
"""Build a frozen JSD probe parquet from rollout data."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_PY_DIR = str(_REPO_ROOT / "python")
if _PY_DIR not in sys.path:
    sys.path.insert(0, _PY_DIR)

from tsrl.policies.jsd_probe import build_probe_set as _build_probe_set

build_probe_set = _build_probe_set


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a frozen JSD probe set from rollout parquet")
    parser.add_argument(
        "--input",
        "--data-dir",
        dest="parquet_glob",
        default="data/ppo_rollout_combined/*.parquet",
        help="Parquet glob or directory to sample from",
    )
    parser.add_argument(
        "--output",
        "--out",
        dest="output_path",
        required=True,
        help="Output probe parquet path",
    )
    parser.add_argument("--n", type=int, default=1000, help="Number of probe positions to sample")
    parser.add_argument("--seed", type=int, default=42, help="Sampling seed")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing probe parquet")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out_path = build_probe_set(
        parquet_glob=args.parquet_glob,
        output_path=args.output_path,
        n=args.n,
        seed=args.seed,
        force=args.force,
    )
    print(f"Wrote probe set to {out_path}")


if __name__ == "__main__":
    main()
