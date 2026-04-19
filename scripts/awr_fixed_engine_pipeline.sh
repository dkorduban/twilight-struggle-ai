#!/bin/bash
# Wait for fresh fixed-engine AWR data, then train best-arch AWR model and produce PPO v3 warmstart.
# Run in background: nohup bash scripts/awr_fixed_engine_pipeline.sh &
set -e

DATA="data/awr_eval/fixed_engine_v1/awr_fixed_engine.parquet"
LOG="results/analysis/awr_fixed_engine_train.log"
SWEEP_JSON="results/awr_sweep/fixed_engine_arch_sweep.json"
WARMSTART_DIR="results/awr_sweep/ppo_warmstart_fixed_engine"

mkdir -p results/awr_sweep results/analysis

echo "[$(date -u)] awr_fixed_engine_pipeline.sh started" | tee "$LOG"
echo "[$(date -u)] Waiting for $DATA ..." | tee -a "$LOG"

# Wait for the parquet file to appear (AWR collection is running)
until [ -f "$DATA" ]; do sleep 30; done

echo "[$(date -u)] Data ready: $(python3 -c "import polars as pl; df=pl.read_parquet('$DATA'); print(f'{len(df)} rows, {df[\"model_label\"].unique().to_list()}')" 2>/dev/null || wc -c < "$DATA" && echo " bytes")" | tee -a "$LOG"

# Phase 1: Quick arch comparison on fresh data (3 archs × 2 seeds × tau=1.0 × 10 epochs)
echo "[$(date -u)] Phase 1: arch sweep on fixed-engine data" | tee -a "$LOG"
PYTHONPATH=build-ninja/bindings nice -n 15 uv run python scripts/arch_sweep_awr.py \
  --data "$DATA" \
  --archs control_feat_gnn_card_attn gnn_card_attn_gated country_attn_side control_feat_gnn_side \
  --hidden-dims 256 \
  --taus 1.0 \
  --seeds 42 43 \
  --epochs 10 \
  --device cuda \
  --out "$SWEEP_JSON" \
  2>&1 | tee -a "$LOG"

echo "[$(date -u)] Arch sweep complete. Finding best arch..." | tee -a "$LOG"

BEST_ARCH=$(python3 -c "
import json
d = json.load(open('$SWEEP_JSON'))
agg = d.get('aggregated', [])
best = max(agg, key=lambda x: x.get('val_adv_card_acc', 0))
print(best['model_type'])
" 2>/dev/null || echo "control_feat_gnn_card_attn")

echo "[$(date -u)] Best arch: $BEST_ARCH. Training 30 epochs for warmstart..." | tee -a "$LOG"

# Phase 2: Full training on best arch using train_awr.py (saves awr_best.pt)
WARMSTART_CKPT_DIR="results/awr_sweep/fixed_engine_${BEST_ARCH}"
mkdir -p "$WARMSTART_CKPT_DIR"
PYTHONPATH=build-ninja/bindings nice -n 15 uv run python scripts/train_awr.py \
  --data "$DATA" \
  --model-type "$BEST_ARCH" \
  --hidden-dim 256 \
  --tau 1.0 \
  --seed 42 \
  --epochs 30 \
  --patience 5 \
  --device cuda \
  --out-dir "$WARMSTART_CKPT_DIR" \
  2>&1 | tee -a "$LOG"

echo "[$(date -u)] Full training complete." | tee -a "$LOG"

BEST_CKPT="$WARMSTART_CKPT_DIR/awr_best.pt"

if [ ! -f "$BEST_CKPT" ]; then
  echo "[$(date -u)] ERROR: Could not find checkpoint at $BEST_CKPT" | tee -a "$LOG"
  exit 1
fi

echo "[$(date -u)] Best AWR checkpoint: $BEST_CKPT" | tee -a "$LOG"

# Phase 3: Quick PPO warmstart validation (15 iters)
mkdir -p "$WARMSTART_DIR"
echo "[$(date -u)] Running PPO warmstart validation (15 iters)..." | tee -a "$LOG"
bash scripts/awr_to_ppo_warmstart.sh "$BEST_CKPT" 15 2>&1 | tee -a "$LOG"

echo "[$(date -u)] Pipeline complete. Warmstart scripted checkpoint in: $WARMSTART_DIR" | tee -a "$LOG"
echo "[$(date -u)] Next step: launch PPO v3 from $WARMSTART_DIR/ppo_warmstart_scripted.pt" | tee -a "$LOG"
