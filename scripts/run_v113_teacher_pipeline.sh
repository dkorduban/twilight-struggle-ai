#!/bin/bash
# v113: Teacher KL with 2000sim+pruning MCTS targets
# Pipeline: wait for collection → convert → train → export → benchmark
set -euo pipefail

TEACHER_DIR="data/mcts_teacher_2000sim_pruned_1k"
TEACHER_JSONL="${TEACHER_DIR}/teacher_rows.jsonl"
TEACHER_PARQUET="${TEACHER_DIR}/teacher_targets.parquet"
CKPT_DIR="data/checkpoints/v113_teacher_2ksim_prune_s42"
COLLECTION_PID=2111989

echo "=== v113 Teacher KL Pipeline ==="
echo "Teacher: MCTS 2000sim prune=1e-4 on heuristic positions"
echo "Base recipe: v106_cf_gnn_s42 (GNN, h256, nash_c, 95ep)"
echo "Started: $(date)"

# --- Step 0: Wait for teacher collection ---
echo ""
echo "--- Step 0: Waiting for teacher collection (PID ${COLLECTION_PID}) ---"
while kill -0 ${COLLECTION_PID} 2>/dev/null; do
    rows=$(wc -l < "${TEACHER_JSONL}" 2>/dev/null || echo 0)
    echo "  $(date +%H:%M:%S) | ${rows} rows collected..."
    sleep 120
done
rows=$(wc -l < "${TEACHER_JSONL}" 2>/dev/null || echo 0)
echo "  Collection complete: ${rows} rows"

# --- Step 1: Convert JSONL → teacher target Parquet ---
echo ""
echo "--- Step 1: Converting JSONL → Parquet ---"
uv run python scripts/convert_mcts_to_teacher.py \
    --input "${TEACHER_JSONL}" \
    --output "${TEACHER_PARQUET}"

# --- Step 2: Train v113 ---
echo ""
echo "--- Step 2: Training v113 ---"
echo "  Recipe: GNN h256, nash_c_only, 95ep, teacher_weight=0.5"

# Memory check
FREE_MB=$(free -m | awk 'NR==2{print $4}')
if [ "$FREE_MB" -lt 4000 ]; then
    echo "ERROR: Only ${FREE_MB}MB free. Need 4GB minimum. Aborting."
    exit 1
fi

export WANDB_API_KEY=$(cat .wandb-api-key.txt)

nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir data/nash_c_only \
    --out-dir "${CKPT_DIR}" \
    --model-type control_feat_gnn --hidden-dim 256 \
    --batch-size 8192 --lr 0.0024 --epochs 95 --patience 20 \
    --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
    --one-cycle --deterministic-split --value-target final_vp --seed 42 \
    --teacher-targets "${TEACHER_PARQUET}" \
    --teacher-weight 0.5 --teacher-value-weight 0.3

# --- Step 3: Export to TorchScript ---
echo ""
echo "--- Step 3: Exporting to TorchScript ---"
uv run python -c "
import torch, sys, os
sys.path.insert(0, 'python')
ckpt_dir = '${CKPT_DIR}'
ckpt_path = os.path.join(ckpt_dir, 'baseline_best.pt')
ckpt = torch.load(ckpt_path, map_location='cpu', weights_only=False)
from tsrl.policies.model import TSControlFeatGNNModel
model = TSControlFeatGNNModel(**ckpt.get('model_config', {}))
model.load_state_dict(ckpt['model_state_dict'])
model.eval()
dummy_inf = torch.zeros(1, 172)
dummy_cards = torch.zeros(1, 448)
dummy_scalars = torch.zeros(1, 11)
scripted = torch.jit.trace(model, (dummy_inf, dummy_cards, dummy_scalars))
out_path = os.path.join(ckpt_dir, 'baseline_best_scripted.pt')
scripted.save(out_path)
print(f'Exported to {out_path}')
"

# --- Step 4: Benchmark (500 games/side, Nash temps) ---
echo ""
echo "--- Step 4: Benchmarking v113 (500 games/side) ---"
PYTHONPATH=build-ninja/bindings nice -n 19 uv run python -u -c "
import tscore

model = '${CKPT_DIR}/baseline_best_scripted.pt'

# Greedy benchmark
for side_name, side in [('USSR', tscore.Side.USSR), ('US', tscore.Side.US)]:
    seed = 50000 if side_name == 'USSR' else 50500
    r = tscore.benchmark_batched(model, side, 500, pool_size=32, seed=seed, nash_temperatures=True)
    wins = sum(1 for x in r if x.winner == side)
    print(f'v113 greedy {side_name}: {wins}/500 ({wins/5:.1f}%)', flush=True)
"

echo ""
echo "=== v113 Pipeline Complete: $(date) ==="
