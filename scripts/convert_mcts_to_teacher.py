"""Convert MCTS self-play JSONL to teacher target Parquet.

The MCTS collector outputs rows with mcts_visit_counts (a JSON array of
{card_id, mode, visits} objects), mcts_root_value, and mcts_n_sim.

This script normalizes visit counts into probability distributions for
card_id (112 entries) and mode (5 entries), producing teacher targets
compatible with the training pipeline's --teacher-targets flag.

Usage:
    uv run python scripts/convert_mcts_to_teacher.py \
        --input /tmp/mcts_v88_teacher.jsonl \
        --output data/teacher_v88/mcts_targets.parquet
"""

import argparse
import json
import sys
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq


def parse_args():
    p = argparse.ArgumentParser(description="Convert MCTS JSONL to teacher targets")
    p.add_argument("--input", required=True, help="Input MCTS JSONL file")
    p.add_argument("--output", required=True, help="Output teacher target Parquet file")
    return p.parse_args()


def convert_row(row: dict) -> dict | None:
    visit_counts = row.get("mcts_visit_counts", [])
    if not visit_counts:
        return None

    # Normalize visit counts into card probability distribution
    card_visits = [0.0] * 112  # kCardSlots = kMaxCardId + 1 = 112
    mode_visits = [0.0] * 5    # 5 action modes
    total_visits = 0

    for entry in visit_counts:
        card_id = entry["card_id"]
        mode = entry["mode"]
        visits = entry["visits"]
        if 0 <= card_id < 112:
            card_visits[card_id] += visits
        if 0 <= mode < 5:
            mode_visits[mode] += visits
        total_visits += visits

    if total_visits == 0:
        return None

    # Normalize to probabilities
    card_probs = [v / total_visits for v in card_visits]
    mode_probs = [v / total_visits for v in mode_visits]

    return {
        "game_id": row["game_id"],
        "step_idx": row["step_idx"],
        "teacher_card_target": card_probs,
        "teacher_mode_target": mode_probs,
        "teacher_value_target": row.get("mcts_root_value", 0.0),
    }


def main():
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    skipped = 0
    with open(input_path) as f:
        for line in f:
            if not line.strip():
                continue
            raw = json.loads(line)
            converted = convert_row(raw)
            if converted is not None:
                rows.append(converted)
            else:
                skipped += 1

    if not rows:
        print(f"No valid rows found in {input_path}", file=sys.stderr)
        sys.exit(1)

    # Build Arrow table
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
    print(f"Wrote {len(rows):,} teacher target rows to {output_path}")
    if skipped:
        print(f"  Skipped {skipped} rows with empty visit counts")


if __name__ == "__main__":
    main()
