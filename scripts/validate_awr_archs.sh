#!/bin/bash
# Validate AWR architecture ranking via mini rollout benchmarks.
# For each candidate: train AWR → export TorchScript → benchmark 500 games/side vs heuristic.
# Output: results/awr_sweep/validation/results.txt
#
# Opus recommendation: 200-400 paired-seed games catches distributional shift that offline
# metrics miss. We use 500/side for 95% CI ~±3pp.

set -e
OUTDIR="results/awr_sweep/validation"
DATA="data/awr_eval/awr_panel_v5.parquet"
LOG="$OUTDIR/validation.log"
RESULTS="$OUTDIR/results.txt"
SEED_USSR=50000
SEED_US=50500
GAMES=500

mkdir -p "$OUTDIR"
echo "[$(date -u)] Starting AWR validation benchmark" | tee -a "$LOG"
echo "Candidates: country_attn_side h256, gnn_side h256, gnn_side h384, gnn_card_attn h256, baseline h256" | tee -a "$LOG"

# Candidates: "arch hidden_dim" pairs
CANDIDATES=(
    "country_attn_side 256"
    "control_feat_gnn_side 256"
    "control_feat_gnn_side 384"
    "control_feat_gnn_card_attn 256"
    "baseline 256"
)

printf "%-40s %8s %8s %10s\n" "Architecture" "USSR_WR" "US_WR" "Combined" | tee "$RESULTS"
printf "%-40s %8s %8s %10s\n" "----------------------------------------" "-------" "------" "--------" | tee -a "$RESULTS"

for CAND in "${CANDIDATES[@]}"; do
    ARCH=$(echo "$CAND" | awk '{print $1}')
    HDIM=$(echo "$CAND" | awk '{print $2}')
    TAG="${ARCH}_h${HDIM}"
    CKPT_DIR="$OUTDIR/$TAG"

    echo "" | tee -a "$LOG"
    echo "[$(date -u)] Training $TAG ..." | tee -a "$LOG"

    # Step 1: AWR training (5 epochs, τ=1.0, seed=42)
    PYTHONPATH=python nice -n 15 uv run python scripts/train_awr.py \
        --data "$DATA" \
        --model-type "$ARCH" \
        --hidden-dim "$HDIM" \
        --tau 1.0 \
        --epochs 5 \
        --seed 42 \
        --device cuda \
        --out-dir "$CKPT_DIR" \
        2>&1 | tee -a "$LOG"

    # Step 2: Export to TorchScript
    echo "[$(date -u)] Exporting $TAG to TorchScript ..." | tee -a "$LOG"
    PYTHONPATH=python uv run python cpp/tools/export_baseline_to_torchscript.py \
        --checkpoint "$CKPT_DIR/awr_best.pt" \
        --out "$CKPT_DIR/awr_best_scripted.pt" \
        2>&1 | tee -a "$LOG"

    # Step 3: Benchmark both sides vs heuristic
    echo "[$(date -u)] Benchmarking $TAG ($GAMES games/side) ..." | tee -a "$LOG"
    BENCH=$(PYTHONPATH=build-ninja/bindings uv run python -c "
import tscore, sys
model_path = '$CKPT_DIR/awr_best_scripted.pt'
games = $GAMES

ussr_results = tscore.benchmark_batched(model_path, tscore.Side.USSR, games, seed=$SEED_USSR)
us_results   = tscore.benchmark_batched(model_path, tscore.Side.US,   games, seed=$SEED_US)

ussr_wr = sum(1 for r in ussr_results if r.winner == tscore.Side.USSR) / games
us_wr   = sum(1 for r in us_results   if r.winner == tscore.Side.US)   / games
combined = (ussr_wr + us_wr) / 2

print(f'{ussr_wr:.4f} {us_wr:.4f} {combined:.4f}')
" 2>/dev/null)

    USSR_WR=$(echo "$BENCH" | awk '{print $1}')
    US_WR=$(echo "$BENCH"   | awk '{print $2}')
    COMBINED=$(echo "$BENCH" | awk '{print $3}')

    echo "[$(date -u)] $TAG: USSR=$USSR_WR US=$US_WR Combined=$COMBINED" | tee -a "$LOG"
    printf "%-40s %8s %8s %10s\n" "$TAG" "$USSR_WR" "$US_WR" "$COMBINED" | tee -a "$RESULTS"
done

echo "" | tee -a "$LOG"
echo "[$(date -u)] Validation complete. Results:" | tee -a "$LOG"
cat "$RESULTS" | tee -a "$LOG"
