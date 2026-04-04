#!/bin/bash
# CPU benchmark pipeline: watches queue file, benchmarks each model as it appears.
# Runs at nice -n 19 to avoid interfering with training.
set -e
cd "$(dirname "$0")/.."

# ── Lock file: prevent duplicate bench_pipeline instances ─────────────────
BENCH_LOCK="$(dirname "$0")/../results/bench_pipeline.lock"
mkdir -p "$(dirname "$0")/../results"
if [ -f "$BENCH_LOCK" ]; then
    echo "[bench_pipeline] ERROR: another instance is already running (lock: $BENCH_LOCK). Exiting."
    echo "  Lock contents: $(cat "$BENCH_LOCK")"
    echo "  To force-start: rm $BENCH_LOCK"
    exit 1
fi
echo "PID=$$  started=$(date '+%Y-%m-%d %H:%M:%S')" > "$BENCH_LOCK"
trap 'rm -f "$BENCH_LOCK"' EXIT

# Ensure W&B API key is available for bench→W&B logging
WANDB_KEY_FILE="$(dirname "$0")/../.wandb-api-key.txt"
if [ -f "$WANDB_KEY_FILE" ]; then
    export WANDB_API_KEY="$(cat "$WANDB_KEY_FILE")"
fi

QUEUE_FILE="${QUEUE_FILE:-$(dirname "$0")/../results/pipeline_queue.txt}"
RESULTS_FILE="${RESULTS_FILE:-$(dirname "$0")/../results/pipeline_results.txt}"
PROCESSED=0

echo "[bench_pipeline] Watching $QUEUE_FILE for models to benchmark..."
echo "[bench_pipeline] Results → $RESULTS_FILE"

while true; do
    # Count lines in queue
    TOTAL=$(wc -l < "$QUEUE_FILE" 2>/dev/null || echo 0)

    if [ "$TOTAL" -gt "$PROCESSED" ]; then
        # Get next unprocessed line
        LINE=$(sed -n "$((PROCESSED + 1))p" "$QUEUE_FILE")

        if [ "$LINE" = "DONE" ]; then
            echo "[bench_pipeline] All models benchmarked. Exiting."
            break
        fi

        if [ -f "$LINE" ]; then
            NAME=$(basename "$(dirname "$LINE")")
            MODEL_DIR=$(dirname "$LINE")
            WANDB_RUN_ID_FILE="$MODEL_DIR/wandb_run_id.txt"
            echo "[bench_pipeline] $(date '+%H:%M:%S') Benchmarking $NAME (2000 games/side)..."
            PYTHONPATH=build-ninja/bindings nice -n 19 uv run python -c "
import tscore, math, os, sys

model = '$LINE'
wandb_run_id_file = '$WANDB_RUN_ID_FILE'

ussr_total = us_total = 0
for seed_base in [50000, 60000, 70000, 80000]:
    ur = tscore.benchmark_batched(model, tscore.Side.USSR, 500, pool_size=32, seed=seed_base)
    usr = tscore.benchmark_batched(model, tscore.Side.US, 500, pool_size=32, seed=seed_base+500)
    ussr_total += sum(1 for r in ur if r.winner == tscore.Side.USSR)
    us_total += sum(1 for r in usr if r.winner == tscore.Side.US)
n = 2000
ussr_pct = ussr_total/n*100; us_pct = us_total/n*100
comb = (ussr_total+us_total)/(n*2)*100
se_u = math.sqrt(ussr_pct/100*(1-ussr_pct/100)/n)*100
se_s = math.sqrt(us_pct/100*(1-us_pct/100)/n)*100
se_c = math.sqrt((ussr_pct/100*(1-ussr_pct/100) + us_pct/100*(1-us_pct/100))/(4*n))*100
result_line = f'$NAME | USSR {ussr_pct:5.1f}% ±{se_u:.1f} | US {us_pct:5.1f}% ±{se_s:.1f} | Combined {comb:5.1f}% ±{se_c:.1f}'
print(result_line)

# Log benchmark win rates to the same W&B run
if os.path.exists(wandb_run_id_file):
    try:
        import wandb
        run_id = open(wandb_run_id_file).read().strip()
        run = wandb.init(id=run_id, resume='must', project='twilight-struggle-ai', entity='korduban-ai')
        wandb.summary['bench/ussr_wr'] = ussr_pct
        wandb.summary['bench/us_wr'] = us_pct
        wandb.summary['bench/combined_wr'] = comb
        wandb.summary['bench/ussr_wr_se'] = se_u
        wandb.summary['bench/us_wr_se'] = se_s
        wandb.summary['bench/combined_wr_se'] = se_c
        wandb.summary['bench/n_games_per_side'] = n
        wandb.finish()
        print(f'[bench_pipeline] W&B run {run_id} updated with benchmark results')
    except Exception as e:
        print(f'[bench_pipeline] W&B logging failed (non-fatal): {e}', file=sys.stderr)
else:
    print(f'[bench_pipeline] No wandb_run_id.txt at {wandb_run_id_file}, skipping W&B logging', file=sys.stderr)
" 2>&1 | tee -a "$RESULTS_FILE"
        else
            echo "[bench_pipeline] WARNING: $LINE not found, skipping"
        fi
        PROCESSED=$((PROCESSED + 1))
    else
        sleep 5
    fi
done

echo ""
echo "=== BENCHMARK RESULTS ==="
cat "$RESULTS_FILE"
