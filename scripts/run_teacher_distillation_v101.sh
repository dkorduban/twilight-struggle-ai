#!/bin/bash
# v101: Teacher distillation with fixed MCTS data (post double-softmax fix)
#
# Base data: heuristic_nash_b (1.28M rows)
# Teacher targets: MCTS 400 sims, v99_cf_s7, 2000 games self-play
# Hyperparams: proven v99 recipe (lr=0.0024, batch=8192, 95 epochs, seed=7)
# Teacher weight: sweep 0.3 and 0.5

set -euo pipefail

DATA_DIR="data/combined_v99_clean_b"
MCTS_JSONL="data/selfplay/mcts_teacher_fixed_400sim_2k.jsonl"
TEACHER_DIR="data/teacher_v99_cf_s7_fixed"
TEACHER_PARQUET="${TEACHER_DIR}/mcts_targets.parquet"

# Step 1: Convert MCTS JSONL to teacher target Parquet
echo "=== Step 1: Converting MCTS JSONL to teacher targets ==="
mkdir -p "${TEACHER_DIR}"
uv run python scripts/convert_mcts_to_teacher.py \
    --input "${MCTS_JSONL}" \
    --output "${TEACHER_PARQUET}"

# Step 2: Train v101_teacher_w05 (teacher_weight=0.5)
echo ""
echo "=== Step 2: Training v101_teacher_w05 (teacher_weight=0.5) ==="
uv run python scripts/train_baseline.py \
    --data-dirs "${DATA_DIR}" \
    --teacher-targets "${TEACHER_PARQUET}" \
    --teacher-weight 0.5 \
    --teacher-value-weight 0.3 \
    --epochs 95 \
    --batch-size 8192 \
    --lr 0.0024 \
    --dropout 0.1 \
    --label-smoothing 0.05 \
    --weight-decay 1e-4 \
    --one-cycle \
    --hidden-dim 256 \
    --seed 7 \
    --value-target final_vp \
    --run-name v101_teacher_w05 \
    --save-dir data/checkpoints/v101_teacher_w05

# Step 3: Train v101_teacher_w03 (teacher_weight=0.3)
echo ""
echo "=== Step 3: Training v101_teacher_w03 (teacher_weight=0.3) ==="
uv run python scripts/train_baseline.py \
    --data-dirs "${DATA_DIR}" \
    --teacher-targets "${TEACHER_PARQUET}" \
    --teacher-weight 0.3 \
    --teacher-value-weight 0.3 \
    --epochs 95 \
    --batch-size 8192 \
    --lr 0.0024 \
    --dropout 0.1 \
    --label-smoothing 0.05 \
    --weight-decay 1e-4 \
    --one-cycle \
    --hidden-dim 256 \
    --seed 7 \
    --value-target final_vp \
    --run-name v101_teacher_w03 \
    --save-dir data/checkpoints/v101_teacher_w03

echo ""
echo "=== Done! Benchmark with: ==="
echo "PYTHONPATH=build-ninja/bindings python3 -u -c \""
echo "import tscore"
echo "for name in ['v101_teacher_w05', 'v101_teacher_w03']:"
echo "    path = f'data/checkpoints/{name}/baseline_best_scripted.pt'"
echo "    for side_name, side in [('ussr', tscore.Side.USSR), ('us', tscore.Side.US)]:"
echo "        results = tscore.benchmark_batched(path, side, 2000, pool_size=32, seed=42000)"
echo "        wins = sum(1 for r in results if r.winner == side)"
echo "        print(f'{name} {side_name}: {wins}/2000 = {100*wins/2000:.1f}%', flush=True)"
echo "\""
