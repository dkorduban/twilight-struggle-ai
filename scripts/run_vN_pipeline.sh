#!/bin/bash
# Generic vN pipeline — train on combined_vN, benchmark, collect vs-heuristic, chain to v(N+1).
#
# Usage:
#   bash scripts/run_vN_pipeline.sh <N> [--threshold PCT] [--games-per-gen N] [--seed-base S]
#
# Arguments:
#   N               Version number (e.g. 18)
#   --threshold PCT Win-rate threshold to proceed to vs-heuristic collection (default: 35)
#   --games-vsh N   Games to collect for vs-heuristic (default: 2000)
#   --seed-base S   Base seed; heuristic seed = S + N*1000, vs-heu seed = S + N*1000 + 500 (default: 20000)
#
# combined_vN must already exist (symlinks to parquet files).
# The script trains, benchmarks, conditionally collects, then launches run_vN_pipeline.sh N+1.
set -euo pipefail

N=${1:?Usage: $0 <version_number>}
THRESHOLD=0   # 0 = always collect; raise to 35+ once model can consistently beat heuristic
GAMES_VSH=2000
SEED_BASE=20000

shift
while [[ $# -gt 0 ]]; do
    case $1 in
        --threshold) THRESHOLD=$2; shift 2 ;;
        --games-vsh) GAMES_VSH=$2; shift 2 ;;
        --seed-base) SEED_BASE=$2; shift 2 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

LOG=/tmp/pipeline_v${N}.log
exec >> "$LOG" 2>&1

cd /home/dkord/code/twilight-struggle-ai

echo "=== v${N} pipeline started at $(date) ==="

COMBINED=data/combined_v${N}
CKPT_DIR=data/checkpoints/retrain_v${N}
CKPT=${CKPT_DIR}/baseline_best.pt
BENCH_LOG=/tmp/benchmark_v${N}.log
VSH_SEED=$(( SEED_BASE + N * 1000 + 500 ))
VSH_OUT=data/selfplay/learned_v${N}_vs_heuristic_${GAMES_VSH}g_seed${VSH_SEED}.parquet

# ── Verify combined data exists ───────────────────────────────────────────────
FILE_COUNT=$(ls "$COMBINED"/*.parquet 2>/dev/null | wc -l)
if [ "$FILE_COUNT" -eq 0 ]; then
    echo "ERROR: No parquet files in $COMBINED — build combined_v${N} first."
    exit 1
fi
echo "[$(date)] combined_v${N}: $FILE_COUNT files"

# ── Train ─────────────────────────────────────────────────────────────────────
if [ ! -f "$CKPT" ]; then
    echo "[$(date)] Training v${N} (hidden_dim=256, 60 epochs)..."
    nice -n 10 uv run python scripts/train_baseline.py \
        --data-dir "$COMBINED" \
        --out-dir "$CKPT_DIR" \
        --epochs 60 --batch-size 1024 --lr 1.2e-3 \
        --weight-decay 1e-4 --dropout 0.1 --label-smoothing 0.05 \
        --value-target final_vp --num-workers 0 --one-cycle \
        2>&1 | tee /tmp/train_v${N}.log
    echo "[$(date)] v${N} training done."
else
    echo "[$(date)] Checkpoint already exists, skipping training."
fi

# ── Benchmark ─────────────────────────────────────────────────────────────────
# Skip if benchmark already completed (summary line present) — allows restart after failure.
if grep -q "vf_mcts50 vs heuristic" "$BENCH_LOG" 2>/dev/null && \
   grep -q "^\s*vf_mcts50" "$BENCH_LOG" 2>/dev/null; then
    echo "[$(date)] Benchmark log exists with complete results, skipping re-run."
else
    echo "[$(date)] Benchmarking v${N}..."
    nice -n 10 uv run python scripts/benchmark_vf_mcts.py \
        --checkpoint "$CKPT" \
        --n-games 60 --n-sim 50 --n-candidates 8 --seed 9999 --pool-size 30 \
        2>&1 | tee "$BENCH_LOG"
    echo "[$(date)] v${N} benchmark done."
fi

# ── Collect vs-heuristic if above threshold ───────────────────────────────────
# Benchmark summary format: "learned vs heuristic  learned  3/ 30 ( 10.0%)  heuristic ..."
# Pattern allows optional space after '(' e.g. "( 10.0%)" or "(10.0%)".
PCT=$(grep "learned vs heuristic" "$BENCH_LOG" | grep -v "^\s*\[" | grep -oP '\( *\K[0-9.]+(?=%)' | head -1 || true)
if [ -z "$PCT" ]; then
    PCT=$(grep "vf_mcts.*vs heuristic" "$BENCH_LOG" | grep -v "^\s*\[" | grep -oP '\( *\K[0-9.]+(?=%)' | head -1 || true)
fi
echo "[$(date)] v${N} vs heuristic: ${PCT:-unknown}%"

if [ ! -f "$VSH_OUT" ]; then
    PCT_INT=${PCT%.*}
    if [ "${PCT_INT:-0}" -ge "$THRESHOLD" ]; then
        echo "[$(date)] Collecting v${N}-vs-heuristic (${PCT}% >= ${THRESHOLD}%, seed=${VSH_SEED})..."
        nice -n 10 uv run python scripts/collect_learned_vs_heuristic.py \
            --checkpoint "$CKPT" --n-games "$GAMES_VSH" --workers 8 \
            --seed "$VSH_SEED" --out "$VSH_OUT" \
            2>&1 | tee /tmp/collect_v${N}_vs_heuristic.log
        echo "[$(date)] v${N}-vs-heuristic collection done."

        # ── Validate DEFCON-1 rate in collected data ──────────────────────────
        DEFCON1_RATE=$(uv run python -c "
import pyarrow.parquet as pq
from collections import Counter
tbl = pq.read_table('$VSH_OUT')
gids = tbl['game_id'].to_pylist()
reasons = tbl['end_reason'].to_pylist()
gr = {}
for g, r in zip(gids, reasons): gr[g] = r
total = len(gr)
defcon1 = sum(1 for r in gr.values() if r == 'defcon1')
print(f'{defcon1/total*100:.1f}')
" 2>/dev/null || echo "?")
        echo "[$(date)] v${N}-vs-heuristic DEFCON-1 rate: ${DEFCON1_RATE}%"
        # Warn if rate is much higher than heuristic baseline (~8%)
        DEFCON1_INT=${DEFCON1_RATE%.*}
        if [ "${DEFCON1_INT:-0}" -gt 25 ]; then
            echo "[$(date)] WARNING: DEFCON-1 rate ${DEFCON1_RATE}% > 25% — check inference safety guards"
        fi

        # ── Filter new vs-heuristic data ─────────────────────────────────────
        VSH_FILTERED=data/combined_v${N}_vsh_filtered/filtered.parquet
        echo "[$(date)] Filtering $VSH_OUT (cap defcon1 at 15%)..."
        nice -n 10 uv run python scripts/filter_bad_games.py \
            --input "$VSH_OUT" \
            --output "$VSH_FILTERED" \
            --max-defcon1-pct 15 \
            2>&1 | tee /tmp/filter_v${N}.log
        echo "[$(date)] Filter done."

        # ── Build combined_v(N+1) and launch next generation ─────────────────
        NP1=$(( N + 1 ))
        COMBINED_NP1=data/combined_v${NP1}
        mkdir -p "$COMBINED_NP1"
        rm -f "$COMBINED_NP1"/*.parquet
        # Carry forward all files from combined_vN plus the filtered new batch
        for f in "$COMBINED"/*.parquet; do
            ln -sf "$(readlink -f "$f")" "$COMBINED_NP1/$(basename "$f")"
        done
        ln -sf "$(readlink -f "$VSH_FILTERED")" \
            "$COMBINED_NP1/learned_v${N}_vs_heuristic_filtered.parquet"
        NP1_COUNT=$(ls "$COMBINED_NP1"/*.parquet | wc -l)
        echo "[$(date)] combined_v${NP1} assembled: $NP1_COUNT files"

        echo "[$(date)] Launching v${NP1} pipeline..."
        bash scripts/run_vN_pipeline.sh "$NP1" \
            --threshold "$THRESHOLD" --games-vsh "$GAMES_VSH" --seed-base "$SEED_BASE"
    else
        echo "[$(date)] SKIP: v${N} scored ${PCT:-?}% (< ${THRESHOLD}%). Stopping chain."
        echo "[$(date)] Consider: collect more heuristic data or tune architecture before continuing."
    fi
else
    echo "[$(date)] vs-heuristic data already exists: $VSH_OUT"
fi

echo "=== v${N} pipeline finished at $(date) ==="
