#!/usr/bin/env python3
"""PreToolUse hook: warn if C++ bindings are stale before training/benchmark commands.

Fires on Bash tool calls. Checks if command is a training or benchmark invocation,
then compares tscore.so mtime vs newest source file in cpp/ and include/.
Emits a warning system message if stale — does NOT block the command.
"""
import json
import os
import sys
from pathlib import Path


TRAINING_KEYWORDS = [
    "train_ppo.py",
    "train_baseline.py",
    "train_ppo ",
    "train_baseline ",
]
BENCH_KEYWORDS = [
    "benchmark_batched",
    "ts_collect_mcts_games",
    "collect_selfplay_rows",
]
ALL_KEYWORDS = TRAINING_KEYWORDS + BENCH_KEYWORDS

REPO_ROOT = Path(__file__).parent.parent.parent


def find_so(build_dir: Path) -> Path | None:
    for p in build_dir.glob("bindings/tscore*.so"):
        return p
    return None


def newest_source_mtime(repo: Path) -> float:
    mtime = 0.0
    for glob_pat in ("cpp/**/*.cpp", "cpp/**/*.h", "include/**/*.h", "bindings/**/*.cpp"):
        for f in repo.glob(glob_pat):
            try:
                mtime = max(mtime, f.stat().st_mtime)
            except OSError:
                pass
    return mtime


def emit(msg: str) -> None:
    print(json.dumps({"systemMessage": msg}))


try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)

command = (payload.get("tool_input") or {}).get("command", "")
if not any(kw in command for kw in ALL_KEYWORDS):
    sys.exit(0)

# Only check in the project repo
build_ninja = REPO_ROOT / "build-ninja"
so_path = find_so(build_ninja)

if so_path is None:
    emit(
        "⚠️  BINARY FRESHNESS: build-ninja/bindings/tscore*.so not found. "
        "Run: cmake --build build-ninja -j  before training/benchmark."
    )
    sys.exit(0)

so_mtime = so_path.stat().st_mtime
src_mtime = newest_source_mtime(REPO_ROOT)

if src_mtime > so_mtime:
    age_min = (src_mtime - so_mtime) / 60
    emit(
        f"⚠️  BINARY FRESHNESS: C++ sources are {age_min:.0f} minutes newer than "
        f"{so_path.name}. Rebuild first: cmake --build build-ninja -j"
    )
