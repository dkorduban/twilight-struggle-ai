"""Collect MCTS teacher targets from heuristic game positions.

Runs heuristic (MinimalHybrid) games using the batched MCTS infrastructure
with --heuristic-teacher-mode: the game plays out using the heuristic policy
(identical trajectory to a pure heuristic game with the same seed), but MCTS
is also run at every decision to record visit count distributions.

Output: Parquet file with teacher target schema compatible with
train_baseline.py --teacher-targets:
  game_id, step_idx, teacher_card_target[111], teacher_mode_target[5], teacher_value_target

Usage:
    uv run python scripts/collect_mcts_targets.py \\
        --model data/checkpoints/v99_cf_1x95_s7/baseline_best_scripted.pt \\
        --games 1000 --n-sim 100 --pool-size 32 --seed 77700 \\
        --output data/selfplay/mcts_teacher_nashc_100sim_1k.parquet
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Collect MCTS teacher targets from heuristic game positions."
    )
    p.add_argument("--model", required=True, help="Path to TorchScript model (.pt)")
    p.add_argument("--output", required=True, help="Output teacher target Parquet path")
    p.add_argument("--games", type=int, default=1000, help="Number of games (default: 1000)")
    p.add_argument("--n-sim", type=int, default=100, help="MCTS simulations per decision (default: 100)")
    p.add_argument("--pool-size", type=int, default=32, help="Concurrent game slots (default: 32)")
    p.add_argument("--max-pending", type=int, default=32, help="Max pending expansions per slot (default: 32)")
    p.add_argument("--seed", type=int, default=77700,
                   help="Base seed (default: 77700, matches nash_c dataset)")
    p.add_argument("--jsonl-path", default=None,
                   help="Keep intermediate JSONL at this path (default: tempfile, deleted after)")
    p.add_argument("--game-id-prefix", default="selfplay",
                   help="Game ID prefix (default: 'selfplay' to match nash_c game_ids)")
    return p.parse_args()


def find_binary() -> Path:
    candidates = [
        Path("build-ninja/cpp/tools/ts_collect_mcts_games_jsonl"),
        Path("build/cpp/tools/ts_collect_mcts_games_jsonl"),
        Path("cpp/mcts_batched_fast/build/ts_collect_mcts_games_jsonl"),
    ]
    for c in candidates:
        if c.exists():
            return c
    raise FileNotFoundError(
        "ts_collect_mcts_games_jsonl not found. Build first: cmake --build build-ninja -j"
    )


def run_collection(
    binary: Path,
    model: str,
    jsonl_path: Path,
    games: int,
    n_sim: int,
    pool_size: int,
    max_pending: int,
    seed: int,
    game_id_prefix: str,
) -> None:
    cmd = [
        str(binary),
        "--model", model,
        "--out", str(jsonl_path),
        "--games", str(games),
        "--n-sim", str(n_sim),
        "--pool-size", str(pool_size),
        "--max-pending", str(max_pending),
        "--seed", str(seed),
        "--heuristic-teacher-mode",
        "--game-id-prefix", game_id_prefix,
    ]
    print(f"[collect_mcts_targets] Running: {' '.join(cmd)}", flush=True)
    result = subprocess.run(cmd, check=True)
    if result.returncode != 0:
        raise RuntimeError(f"C++ collection failed with exit code {result.returncode}")


def convert_row(row: dict) -> dict | None:
    """Convert a MCTS JSONL row to teacher target dict. Same logic as convert_mcts_to_teacher.py."""
    visit_counts = row.get("mcts_visit_counts", [])
    if not visit_counts:
        return None

    card_visits = [0.0] * 111  # indices 0..110 map to card_ids 1..111
    mode_visits = [0.0] * 5    # 5 action modes
    total_visits = 0

    for entry in visit_counts:
        card_id = entry["card_id"]
        mode = entry["mode"]
        visits = entry["visits"]
        if 1 <= card_id <= 111:
            card_visits[card_id - 1] += visits
        if 0 <= mode < 5:
            mode_visits[mode] += visits
        total_visits += visits

    if total_visits == 0:
        return None

    card_probs = [v / total_visits for v in card_visits]
    mode_probs = [v / total_visits for v in mode_visits]

    return {
        "game_id": row["game_id"],
        "step_idx": row["step_idx"],
        "teacher_card_target": card_probs,
        "teacher_mode_target": mode_probs,
        "teacher_value_target": float(row.get("mcts_root_value", 0.0)),
    }


def jsonl_to_parquet(jsonl_path: Path, output_path: Path) -> int:
    rows = []
    skipped = 0
    with open(jsonl_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            converted = convert_row(raw)
            if converted is not None:
                rows.append(converted)
            else:
                skipped += 1

    if not rows:
        raise ValueError(f"No valid rows found in {jsonl_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    table = pa.table({
        "game_id": pa.array([r["game_id"] for r in rows], type=pa.string()),
        "step_idx": pa.array([r["step_idx"] for r in rows], type=pa.int64()),
        "teacher_card_target": pa.array(
            [r["teacher_card_target"] for r in rows],
            type=pa.list_(pa.float32()),
        ),
        "teacher_mode_target": pa.array(
            [r["teacher_mode_target"] for r in rows],
            type=pa.list_(pa.float32()),
        ),
        "teacher_value_target": pa.array(
            [r["teacher_value_target"] for r in rows],
            type=pa.float32(),
        ),
    })
    pq.write_table(table, str(output_path))
    if skipped:
        print(f"  Skipped {skipped} rows with empty visit counts", flush=True)
    return len(rows)


def main() -> None:
    args = parse_args()

    binary = find_binary()
    output_path = Path(args.output)

    # Determine JSONL path
    tmp_file = None
    if args.jsonl_path:
        jsonl_path = Path(args.jsonl_path)
        jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        tmp_file = tempfile.NamedTemporaryFile(suffix=".jsonl", delete=False)
        jsonl_path = Path(tmp_file.name)
        tmp_file.close()

    try:
        run_collection(
            binary=binary,
            model=args.model,
            jsonl_path=jsonl_path,
            games=args.games,
            n_sim=args.n_sim,
            pool_size=args.pool_size,
            max_pending=args.max_pending,
            seed=args.seed,
            game_id_prefix=args.game_id_prefix,
        )

        print(f"[collect_mcts_targets] Converting JSONL → Parquet...", flush=True)
        n_rows = jsonl_to_parquet(jsonl_path, output_path)
        print(f"[collect_mcts_targets] Wrote {n_rows:,} teacher target rows → {output_path}", flush=True)

    finally:
        if tmp_file is not None and jsonl_path.exists():
            jsonl_path.unlink()


if __name__ == "__main__":
    main()
