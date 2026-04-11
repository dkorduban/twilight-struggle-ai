#!/usr/bin/env python3
"""Trim old training run checkpoint dirs to keep only best + last epoch.

For each run directory under data/checkpoints/ that matches the pattern
`baseline_epochN.pt`, keeps:
  - baseline_best.pt      (if present — saved by train_baseline.py as best val checkpoint)
  - baseline_epoch<last>.pt  (the final epoch, useful for warm-start)
  - All other .pt files not matching baseline_epoch*.pt (e.g. ppo_iter*, scripted models)

Everything else is moved to a trash dir (not deleted) so recovery is possible.

Usage:
    # Dry run — show what would be moved
    uv run python scripts/trim_checkpoints.py --dry-run

    # Trim all retrain_v* dirs (leaves ppo_v* and phase4 untouched)
    uv run python scripts/trim_checkpoints.py --pattern "retrain_v*"

    # Trim everything
    uv run python scripts/trim_checkpoints.py

    # Recover (move trash back)
    uv run python scripts/trim_checkpoints.py --restore
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import shutil
from pathlib import Path


_EPOCH_RE = re.compile(r"baseline_epoch(\d+)\.pt$")
_TRASH_DIR = Path("data/checkpoints_trimmed_epochs")


def trim_run_dir(run_dir: Path, dry_run: bool) -> tuple[int, int]:
    """Returns (kept, moved) counts."""
    pts = sorted(run_dir.glob("baseline_epoch*.pt"))
    if not pts:
        return 0, 0

    # Find last epoch number
    epochs = []
    for p in pts:
        m = _EPOCH_RE.match(p.name)
        if m:
            epochs.append((int(m.group(1)), p))
    if not epochs:
        return 0, 0

    epochs.sort()
    last_epoch_path = epochs[-1][1]

    keep = {last_epoch_path}
    best = run_dir / "baseline_best.pt"
    if best.exists():
        keep.add(best)

    to_move = [p for _, p in epochs if p not in keep]

    if not dry_run:
        for src in to_move:
            rel = src.relative_to(Path("data/checkpoints"))
            dst = _TRASH_DIR / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))

    return len(keep), len(to_move)


def restore_trash() -> None:
    if not _TRASH_DIR.exists():
        print("Nothing to restore — trash dir does not exist")
        return
    pts = list(_TRASH_DIR.rglob("*.pt"))
    for src in pts:
        rel = src.relative_to(_TRASH_DIR)
        dst = Path("data/checkpoints") / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
    print(f"Restored {len(pts)} files from {_TRASH_DIR}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dry-run", action="store_true", help="Show what would be moved, do nothing")
    p.add_argument("--pattern", default="*", help="Glob pattern for run dirs (default: all)")
    p.add_argument("--restore", action="store_true", help="Move trimmed epochs back")
    args = p.parse_args()

    if args.restore:
        restore_trash()
        return

    run_dirs = sorted(Path("data/checkpoints").glob(args.pattern))
    # Skip known important dirs that should never be trimmed
    skip = {"ppo_v1_from_v106", "ppo_v2_selfplay", "ppo_v3_league", "league_v3",
            "phase4", "checkpoints_backup_pre_migration", "checkpoints_trimmed_epochs"}
    run_dirs = [d for d in run_dirs if d.is_dir() and d.name not in skip]

    total_kept = total_moved = 0
    moved_dirs = []

    for d in run_dirs:
        kept, moved = trim_run_dir(d, dry_run=args.dry_run)
        if moved > 0:
            total_kept += kept
            total_moved += moved
            moved_dirs.append((d.name, kept, moved))
            action = "[DRY RUN] would move" if args.dry_run else "moved"
            print(f"  {d.name}: kept {kept}, {action} {moved}")

    print(f"\nTotal: kept {total_kept}, {'would move' if args.dry_run else 'moved'} {total_moved} epoch files")
    if not args.dry_run and total_moved > 0:
        # Show size saved
        trash_size = sum(f.stat().st_size for f in _TRASH_DIR.rglob("*.pt"))
        print(f"Freed ~{trash_size/1e9:.1f} GB  (recoverable from {_TRASH_DIR})")


if __name__ == "__main__":
    main()
