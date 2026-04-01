#!/usr/bin/env python3
"""Chunked native self-play collection runner.

Runs the native JSONL collector in bounded chunks so long jobs checkpoint to
disk frequently instead of accumulating state in memory. The runner also checks
basic host memory/swap pressure before each chunk and backs off by shrinking the
next chunk when the machine is under stress. It is intentionally conservative
because the target environment is often WSL with limited effective headroom.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path


def read_meminfo_mb() -> dict[str, int]:
    values_kb: dict[str, int] = {}
    with Path("/proc/meminfo").open() as fh:
        for line in fh:
            key, raw = line.split(":", 1)
            values_kb[key] = int(raw.strip().split()[0])
    return {key: value // 1024 for key, value in values_kb.items()}


def read_swap_used_mb() -> int:
    swaps = Path("/proc/swaps")
    if not swaps.exists():
        return 0

    total_kb = 0
    used_kb = 0
    with swaps.open() as fh:
        next(fh, None)
        for line in fh:
            fields = line.split()
            if len(fields) >= 5:
                total_kb += int(fields[2])
                used_kb += int(fields[3])
    return used_kb // 1024 if total_kb else 0


def memory_snapshot() -> dict[str, int]:
    mem = read_meminfo_mb()
    total = mem.get("MemTotal", 0)
    available = mem.get("MemAvailable", 0)
    used = max(0, total - available)
    return {
        "mem_total_mb": total,
        "mem_available_mb": available,
        "mem_used_mb": used,
        "swap_used_mb": read_swap_used_mb(),
    }


def choose_chunk_size(
    requested: int,
    snapshot: dict[str, int],
    min_available_mb: int,
    max_used_mb: int,
    max_swap_used_mb: int,
) -> int:
    chunk = requested
    if (
        snapshot["mem_available_mb"] < min_available_mb
        or snapshot["mem_used_mb"] > max_used_mb
        or snapshot["swap_used_mb"] > max_swap_used_mb
    ):
        chunk = max(1, requested // 2)
    return chunk


def run_chunk(
    rows_tool: Path,
    out_path: Path,
    games: int,
    seed: int,
    ussr_policy: str,
    us_policy: str,
    learned_model: Path | None,
    learned_side: str,
) -> None:
    cmd = [
        str(rows_tool),
        "--out",
        str(out_path),
        "--games",
        str(games),
        "--seed",
        str(seed),
        "--ussr-policy",
        ussr_policy,
        "--us-policy",
        us_policy,
    ]
    if learned_model is not None:
        cmd.extend(["--learned-model", str(learned_model), "--learned-side", learned_side])
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--games", type=int, required=True)
    parser.add_argument("--chunk-size", type=int, default=128)
    parser.add_argument("--seed", type=int, default=12345)
    parser.add_argument(
        "--rows-tool",
        type=Path,
        default=Path("build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl"),
    )
    parser.add_argument("--ussr-policy", default="minimal_hybrid")
    parser.add_argument("--us-policy", default="random")
    parser.add_argument("--learned-model", type=Path, default=None)
    parser.add_argument("--learned-side", choices=("ussr", "us"), default="ussr")
    parser.add_argument("--min-available-mb", type=int, default=4096)
    parser.add_argument("--max-used-mb", type=int, default=25000)
    parser.add_argument("--max-swap-used-mb", type=int, default=2048)
    parser.add_argument("--backoff-seconds", type=float, default=5.0)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = args.out_dir / "manifest.json"

    manifest = {
        "games": args.games,
        "base_seed": args.seed,
        "requested_chunk_size": args.chunk_size,
        "ussr_policy": args.ussr_policy,
        "us_policy": args.us_policy,
        "learned_model": str(args.learned_model) if args.learned_model is not None else None,
        "learned_side": args.learned_side if args.learned_model is not None else None,
        "chunks": [],
    }

    completed = 0
    next_seed = args.seed
    while completed < args.games:
        snapshot = memory_snapshot()
        chunk_games = min(
            choose_chunk_size(
                args.chunk_size,
                snapshot,
                args.min_available_mb,
                args.max_used_mb,
                args.max_swap_used_mb,
            ),
            args.games - completed,
        )
        if chunk_games < args.chunk_size:
            time.sleep(args.backoff_seconds)

        chunk_index = len(manifest["chunks"])
        out_path = args.out_dir / f"rows_{chunk_index:04d}.jsonl"
        run_chunk(
            args.rows_tool,
            out_path,
            chunk_games,
            next_seed,
            args.ussr_policy,
            args.us_policy,
            args.learned_model,
            args.learned_side,
        )

        manifest["chunks"].append(
            {
                "index": chunk_index,
                "out_path": str(out_path),
                "games": chunk_games,
                "seed": next_seed,
                "memory_before": snapshot,
            }
        )
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

        completed += chunk_games
        next_seed += chunk_games

    print(json.dumps({"status": "ok", "chunks": len(manifest["chunks"]), "games": completed}))


if __name__ == "__main__":
    main()
