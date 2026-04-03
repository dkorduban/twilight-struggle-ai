#!/bin/bash
# Quick status check for train+bench pipelines.
# Usage: ./scripts/pipeline_status.sh
cd "$(dirname "$0")/.."

QUEUE_FILE="${QUEUE_FILE:-$(dirname "$0")/../results/pipeline_queue.txt}"
RESULTS_FILE="${RESULTS_FILE:-$(dirname "$0")/../results/pipeline_results.txt}"

echo "=== PIPELINE STATUS ==="

# Training pipeline
TRAIN_PID=$(ps aux | grep 'train_pipeline\|train_baseline' | grep -v grep | head -1 | awk '{print $2}')
if [ -n "$TRAIN_PID" ]; then
    TRAIN_DIR=$(ps aux | grep 'python3.*train_baseline' | grep -v grep | sed 's/.*--out-dir //' | awk '{print $1}')
    echo "TRAINING: active (PID $TRAIN_PID) → $TRAIN_DIR"
    nvidia-smi --query-compute-apps=pid,used_gpu_memory --format=csv,noheader 2>/dev/null | head -3
else
    echo "TRAINING: idle"
fi

# Benchmark pipeline
BENCH_PID=$(ps aux | grep 'bench_pipeline\|benchmark_batched' | grep -v grep | head -1 | awk '{print $2}')
if [ -n "$BENCH_PID" ]; then
    echo "BENCHMARK: active (PID $BENCH_PID)"
else
    echo "BENCHMARK: idle"
fi

# Queue status
echo ""
echo "=== QUEUE ($QUEUE_FILE) ==="
if [ -f "$QUEUE_FILE" ]; then
    TOTAL=$(wc -l < "$QUEUE_FILE")
    echo "Queued models: $TOTAL"
    cat "$QUEUE_FILE"
else
    echo "No queue file"
fi

# Results
echo ""
echo "=== RESULTS ($RESULTS_FILE) ==="
if [ -f "$RESULTS_FILE" ]; then
    cat "$RESULTS_FILE"
else
    echo "No results yet"
fi

# Memory
echo ""
echo "=== RESOURCES ==="
free -m | head -2
nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader 2>/dev/null
