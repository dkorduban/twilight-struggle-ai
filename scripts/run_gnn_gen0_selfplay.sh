#!/bin/bash
# GNN Gen 0 self-play loop.
#
# Base model: v106_cf_gnn_s7 (combined=37.2%, best 4-seed GNN)
# Strategy:
#   1. Collect 2000 games learned-vs-heuristic (USSR side)
#   2. Collect 2000 games learned-vs-heuristic (US side)
#   3. Mix with nash_c_only anchor data (all rows)
#   4. Filter US-side selfplay to winning games only
#   5. Train v107_cf_gnn_gen0 (same hyperparams as v106)
#   6. Benchmark both sides (500 games each)
#
# Usage:
#   nohup bash scripts/run_gnn_gen0_selfplay.sh > results/gnn_gen0.log 2>&1 &

set -euo pipefail

cd "$(dirname "$0")/.."

BASE_MODEL="data/checkpoints/v106_cf_gnn_s42/baseline_best_scripted.pt"
ANCHOR_DATA="data/nash_c_only"
GEN0_DIR="data/selfplay/gnn_gen0"
OUT_DIR="data/checkpoints/v107_cf_gnn_gen0"
COMBINED_DIR="data/combined_gnn_gen0"
SEED=107000

log() { echo "[$(date '+%H:%M:%S')] $*"; }

mkdir -p "$GEN0_DIR" "$COMBINED_DIR" results

log "=== GNN Gen 0: collecting learned-vs-heuristic ==="
log "Base model: $BASE_MODEL"

# ── Step 1: USSR-side collection ──────────────────────────────────────────────
log "Collecting USSR-side games (2000, seed=$SEED)..."
nice -n 10 bash scripts/collect_cpp.sh \
    --ussr-model "$BASE_MODEL" \
    --us-policy minimal_hybrid \
    --games 2000 \
    --seed "$SEED" \
    --epsilon 0.05 \
    --nash-temperatures \
    --out "$GEN0_DIR/gnn_s7_ussr_vs_heuristic_2k.parquet" \
    2>&1 | tee results/gnn_gen0_ussr_collect.log
log "USSR collection done."

# ── Step 2: US-side collection ────────────────────────────────────────────────
log "Collecting US-side games (2000, seed=$((SEED+500)))..."
nice -n 10 bash scripts/collect_cpp.sh \
    --us-model "$BASE_MODEL" \
    --ussr-policy minimal_hybrid \
    --games 2000 \
    --seed $((SEED+500)) \
    --epsilon 0.05 \
    --nash-temperatures \
    --out "$GEN0_DIR/gnn_s7_us_vs_heuristic_2k.parquet" \
    2>&1 | tee results/gnn_gen0_us_collect.log
log "US collection done."

# ── Step 3: Mix anchor data + self-play ──────────────────────────────────────
log "Building Gen 0 combined dataset..."

# Copy anchor data
cp "$ANCHOR_DATA"/*.parquet "$COMBINED_DIR/"

# USSR side: take all rows
cp "$GEN0_DIR/gnn_s7_ussr_vs_heuristic_2k.parquet" "$COMBINED_DIR/"

# US side: filter to winning games only (per game_asymmetry feedback)
log "Filtering US self-play to winning games..."
uv run python - <<'PYEOF'
import polars as pl

us_file = "data/selfplay/gnn_gen0/gnn_s7_us_vs_heuristic_2k.parquet"
out_file = "data/combined_gnn_gen0/gnn_s7_us_vs_heuristic_2k_wins.parquet"

df = pl.read_parquet(us_file)
print(f"US selfplay rows total: {len(df):,}")

# winner_side: 1=USSR, -1=US, 0=draw (from the dataset encoding)
# US wins when winner_side == -1
if "winner_side" in df.columns:
    # For US-side rows, filter to games where US won (winner_side == -1)
    wins = df.filter(pl.col("winner_side") == -1)
elif "final_vp" in df.columns:
    # Negative VP = US lead
    wins = df.filter(pl.col("final_vp") < 0)
else:
    print("WARNING: no winner column found, keeping all rows")
    wins = df

print(f"US selfplay winning rows: {len(wins):,} ({len(wins)/len(df)*100:.1f}%)")
wins.write_parquet(out_file)
print(f"Saved to {out_file}")
PYEOF

log "Dataset composition:"
uv run python - <<'PYEOF'
import polars as pl
import glob

total = 0
for f in sorted(glob.glob("data/combined_gnn_gen0/*.parquet")):
    n = len(pl.scan_parquet(f).collect())
    total += n
    print(f"  {f}: {n:,} rows")
print(f"  TOTAL: {total:,} rows")
PYEOF

# ── Step 4: Train ─────────────────────────────────────────────────────────────
log "=== Training v107_cf_gnn_gen0 ==="
nice -n 10 uv run python scripts/train_baseline.py \
    --data-dir "$COMBINED_DIR" \
    --out-dir "$OUT_DIR" \
    --model-type control_feat_gnn --hidden-dim 256 \
    --batch-size 8192 --lr 0.0024 --epochs 95 --patience 20 \
    --dropout 0.1 --weight-decay 1e-4 --label-smoothing 0.05 \
    --one-cycle --deterministic-split --value-target final_vp --seed 7 \
    2>&1 | tee results/v107_cf_gnn_gen0_train.log

log "Training done."

# ── Step 5: Export ────────────────────────────────────────────────────────────
log "Exporting TorchScript..."
BEST_CKPT=$(ls -t "$OUT_DIR"/baseline_epoch*.pt 2>/dev/null | head -1)
if [ -z "$BEST_CKPT" ]; then
    BEST_CKPT="$OUT_DIR/baseline_best.pt"
fi

uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint "$BEST_CKPT" \
    --out "$OUT_DIR/baseline_best_scripted.pt"
log "Exported: $OUT_DIR/baseline_best_scripted.pt"

# ── Step 6: Benchmark ─────────────────────────────────────────────────────────
log "=== Benchmarking v107_cf_gnn_gen0 ==="
PYTHONPATH=build-ninja/bindings uv run python -c "
import tscore, sys
model_path = '$OUT_DIR/baseline_best_scripted.pt'
try:
    r_ussr = tscore.benchmark_batched(model_path, tscore.Side.USSR, 500, seed=107000)
    r_us   = tscore.benchmark_batched(model_path, tscore.Side.US,   500, seed=107500)
    ussr_wr = sum(1 for x in r_ussr if x.winner == tscore.Side.USSR) / len(r_ussr) * 100
    us_wr   = sum(1 for x in r_us   if x.winner == tscore.Side.US)   / len(r_us)   * 100
    combined = (ussr_wr + us_wr) / 2
    print(f'v107_cf_gnn_gen0: USSR={ussr_wr:.1f}% US={us_wr:.1f}% Combined={combined:.1f}%')
except Exception as e:
    print(f'Benchmark failed: {e}', file=sys.stderr)
    sys.exit(1)
" 2>&1 | tee -a results/v107_cf_gnn_gen0_train.log

log "=== GNN Gen 0 pipeline complete ==="
