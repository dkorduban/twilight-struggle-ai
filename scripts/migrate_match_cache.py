#!/usr/bin/env python3
"""Migrate match JSON cache to SQL match_cache table.

Reads from results/matches_archive_20260412.tar.bz2 (all historical JSONs).
Safe to re-run — uses INSERT OR REPLACE.

Usage:
    uv run python scripts/migrate_match_cache.py
"""
import json
import sys
import tarfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "python"))
sys.path.insert(0, "build-ninja/bindings")
# do NOT add build/bindings — it would shadow build-ninja (same bug as run_elo_tournament.py)

from tsrl.checkpoint_db import save_match_cache  # noqa: E402

ARCHIVE = Path("results/matches_archive_20260412.tar.bz2")


def main() -> None:
    if not ARCHIVE.exists():
        print(f"Archive not found: {ARCHIVE}", file=sys.stderr)
        sys.exit(1)

    migrated = 0
    errors = 0
    skipped = 0

    with tarfile.open(ARCHIVE, "r:bz2") as tf:
        members = tf.getmembers()
        print(f"Archive contains {len(members)} members", flush=True)
        for member in members:
            if not member.name.endswith(".json"):
                skipped += 1
                continue
            try:
                f = tf.extractfile(member)
                if f is None:
                    skipped += 1
                    continue
                entry = json.loads(f.read())
                if "model_a" not in entry or "model_b" not in entry:
                    print(f"Skipping {member.name}: missing model_a/model_b", file=sys.stderr)
                    skipped += 1
                    continue
                save_match_cache(entry)
                migrated += 1
                if migrated % 100 == 0:
                    print(f"  ... {migrated} migrated", flush=True)
            except Exception as e:
                print(f"Error on {member.name}: {e}", file=sys.stderr)
                errors += 1

    print(f"Done. Migrated {migrated} entries to match_cache ({errors} errors, {skipped} skipped)")


if __name__ == "__main__":
    main()
