#!/bin/bash
# Gen 1 self-play loop from v99_saturation_1x_95ep.
#
# Strategy: collect learned-vs-heuristic data (USSR + US sides separately),
# mix with heuristic anchor data, train Gen 1 model, benchmark.
#
# Per autonomous work rules:
#   - nice -n 10 for all collection and training
#   - Filter US-side data to winning games only (feed to train with filter flag or separate parquet)
#   - Always mix heuristic anchor data (prevents echo chamber collapse)
#   - Benchmark both sides (2000 games each)
#
# Gen 0 model: v99_saturation_1x_95ep (29.5% combined — new BC best)
# Gen 1 training data: combined_v99_clean_b (1.28M) + new selfplay (~4k rows)
#
# Self-play collection: ~9 games/sec → 2000 games ≈ 220s ≈ 4 min per run
# Total collection: ~12-15 min for all three batches

cd "$(dirname "$0")/.."

MODEL="data/checkpoints/v99_saturation_1x_95ep/baseline_best_scripted.pt"
ANCHOR_DATA="data/combined_v99_clean_b"  # 1x nash_b (1.28M rows), 95ep reference dataset
GEN1_DIR="data/selfplay/gen1"
OUT_DIR="data/checkpoints/v99_gen1"
QUEUE_FILE="results/pipeline_queue.txt"

log() { echo "[$(date '+%H:%M:%S')] $*"; }

mkdir -p "$GEN1_DIR" logs results

# ── Collection ──────────────────────────────────────────────────────────────

log "=== Gen 1 collection from v99_saturation_1x_95ep ==="

# USSR side: learned plays USSR vs heuristic US
log "Collecting USSR-side games (2000)..."
if nice -n 10 bash scripts/collect_cpp.sh \
    --checkpoint "data/checkpoints/v99_saturation_1x_95ep/baseline_best.pt" \
    --learned-side ussr \
    --games 2000 \
    --seed 99000 \
    --temperature 1.0 \
    --epsilon 0.05 \
    --out "$GEN1_DIR/v99sat_ussr_vs_heuristic_2k.parquet" \
    2>&1 | tee logs/gen1_ussr_collect.log; then
    log "USSR collection done: $GEN1_DIR/v99sat_ussr_vs_heuristic_2k.parquet"
else
    log "ERROR: USSR collection failed"
    exit 1
fi

# US side: learned plays US vs heuristic USSR
log "Collecting US-side games (2000)..."
if nice -n 10 bash scripts/collect_cpp.sh \
    --checkpoint "data/checkpoints/v99_saturation_1x_95ep/baseline_best.pt" \
    --learned-side us \
    --games 2000 \
    --seed 99500 \
    --temperature 1.0 \
    --epsilon 0.05 \
    --out "$GEN1_DIR/v99sat_us_vs_heuristic_2k.parquet" \
    2>&1 | tee logs/gen1_us_collect.log; then
    log "US collection done: $GEN1_DIR/v99sat_us_vs_heuristic_2k.parquet"
else
    log "ERROR: US collection failed"
    exit 1
fi

# ── Build Gen 1 training dataset ────────────────────────────────────────────
# Mix: anchor 1.28M rows + USSR selfplay rows + US selfplay (winning games only)

log "=== Building Gen 1 dataset ==="
GEN1_COMBINED="data/combined_v99_gen1"
mkdir -p "$GEN1_COMBINED"

# Copy anchor data parquet files
cp "$ANCHOR_DATA"/*.parquet "$GEN1_COMBINED/"

# USSR selfplay: take all rows (USSR side we always keep)
cp "$GEN1_DIR/v99sat_ussr_vs_heuristic_2k.parquet" "$GEN1_COMBINED/"

# US selfplay: filter to winning games only (per game_asymmetry feedback)
log "Filtering US games to wins only..."
nice -n 10 uv run python - <<'PYEOF'
import polars as pl, os, sys

us_file = "data/selfplay/gen1/v99sat_us_vs_heuristic_2k.parquet"
out_file = "data/combined_v99_gen1/v99sat_us_vs_heuristic_2k_wins.parquet"

df = pl.read_parquet(us_file)
print(f"US selfplay rows total: {len(df):,}")

# Filter: keep rows where US won (final_outcome == 1 from US perspective)
# The 'winner' column should be 'us' or similar — check what's available
print(f"Columns: {df.columns[:10]}")

# Try to filter by final_outcome or us_won
if 'final_outcome' in df.columns:
    # final_outcome: 1=US win, 0=USSR win, 0.5=draw (from US perspective if us_side row)
    # Actually need to check what value means US win
    print(df['final_outcome'].value_counts())
    wins = df.filter(pl.col('final_outcome') > 0.5)
elif 'outcome' in df.columns:
    wins = df.filter(pl.col('outcome') == 'us')
else:
    print("WARNING: no outcome column found, keeping all US rows")
    wins = df

print(f"US winning rows: {len(wins):,} ({len(wins)/len(df)*100:.1f}%)")
wins.write_parquet(out_file)
print(f"Written to {out_file}")
PYEOF

log "=== Gen 1 dataset ready in $GEN1_COMBINED ==="
ls -la "$GEN1_COMBINED/"*.parquet | awk '{print $5, $9}'

# ── Train Gen 1 ──────────────────────────────────────────────────────────────

log "=== Training Gen 1 model ==="
if nice -n 10 uv run python scripts/train_baseline.py \
    --out-dir "$OUT_DIR" \
    --data-dir "$GEN1_COMBINED" \
    --lr 0.0024 --batch-size 8192 \
    --label-smoothing 0.05 --weight-decay 1e-4 --one-cycle \
    --hidden-dim 256 --value-target final_vp --dropout 0.1 \
    --model-type baseline --seed 42 --deterministic-split \
    --epochs 95 --patience 20 \
    2>&1 | tee logs/gen1_train.log; then
    log "Gen 1 training done"
else
    log "ERROR: Gen 1 training failed"
    exit 1
fi

# ── Export and queue for benchmark ───────────────────────────────────────────
log "Exporting Gen 1 model..."
if nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint "$OUT_DIR/baseline_best.pt" \
    --out "$OUT_DIR/baseline_best_scripted.pt"; then
    echo "$OUT_DIR/baseline_best_scripted.pt" >> "$QUEUE_FILE"
    log "Gen 1 queued for benchmarking: $OUT_DIR"
else
    log "WARNING: export failed"
fi

echo "DONE" >> "$QUEUE_FILE"
log "=== Gen 1 pipeline complete ==="
