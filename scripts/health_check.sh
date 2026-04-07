#!/bin/bash
# Health check for twilight-struggle-ai training environment
# Logs to results/health_checks.log; prints ALERT if issues found
# Usage: bash scripts/health_check.sh
# Cron: */30 * * * * cd /home/dkord/code/twilight-struggle-ai && bash scripts/health_check.sh >> /dev/null

set -euo pipefail

REPO=/home/dkord/code/twilight-struggle-ai
LOG="$REPO/results/health_checks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
ALERTS=()

# ---- Collect metrics ----

# 1. Training process
TRAIN_PIDS=$(pgrep -f "train_ppo.py" 2>/dev/null | tr '\n' ' ' || true)
if [ -z "$TRAIN_PIDS" ]; then
    TRAINING_STATUS="NONE"
    ALERTS+=("TRAINING PROCESS DEAD (no train_ppo.py found)")
else
    TRAINING_STATUS="running pids=$TRAIN_PIDS"
fi

# 2. GPU memory
if command -v nvidia-smi &>/dev/null; then
    GPU_LINE=$(nvidia-smi --query-gpu=memory.used,memory.total,utilization.gpu --format=csv,noheader,nounits 2>/dev/null | head -1 || echo "unavailable")
    GPU_USED=$(echo "$GPU_LINE" | awk -F',' '{gsub(/ /,"",$1); print $1}')
    GPU_TOTAL=$(echo "$GPU_LINE" | awk -F',' '{gsub(/ /,"",$2); print $2}')
    GPU_UTIL=$(echo "$GPU_LINE" | awk -F',' '{gsub(/ /,"",$3); print $3}')
    if [[ "$GPU_TOTAL" =~ ^[0-9]+$ ]] && [ "$GPU_TOTAL" -gt 0 ]; then
        GPU_PCT=$(( GPU_USED * 100 / GPU_TOTAL ))
        GPU_STATUS="${GPU_USED}MiB/${GPU_TOTAL}MiB (${GPU_PCT}%) util=${GPU_UTIL}%"
        if [ "$GPU_PCT" -gt 90 ]; then
            ALERTS+=("GPU MEMORY >90%: $GPU_STATUS")
        fi
    else
        GPU_STATUS="unavailable ($GPU_LINE)"
    fi
else
    GPU_STATUS="nvidia-smi not found"
fi

# 3. Disk space
RESULTS_AVAIL=$(df -BG "$REPO/results" 2>/dev/null | awk 'NR==2{print $4}' | tr -d 'G' || echo "?")
DATA_AVAIL=$(df -BG "$REPO/data" 2>/dev/null | awk 'NR==2{print $4}' | tr -d 'G' || echo "?")
DISK_STATUS="results=${RESULTS_AVAIL}G data=${DATA_AVAIL}G free"
for AVAIL in "$RESULTS_AVAIL" "$DATA_AVAIL"; do
    if [[ "$AVAIL" =~ ^[0-9]+$ ]] && [ "$AVAIL" -lt 5 ]; then
        ALERTS+=("LOW DISK: only ${AVAIL}G free on a partition")
    fi
done

# 4. Recent log tail
RECENT_LOG=$(find "$REPO/results" -name "*.log" -newer /dev/null 2>/dev/null | xargs ls -t 2>/dev/null | head -1 || true)
if [ -n "$RECENT_LOG" ]; then
    LAST_LINES=$(tail -3 "$RECENT_LOG" 2>/dev/null | tr '\n' '|' | sed 's/|$//')
    LOG_STATUS="$RECENT_LOG: $LAST_LINES"
else
    LOG_STATUS="no .log files found"
fi

# 5. OOM kills in dmesg
OOM_COUNT=$(dmesg --since "1 hour ago" 2>/dev/null | grep -c "Out of memory\|oom_kill_process\|Killed process" 2>/dev/null || echo 0)
if [[ "$OOM_COUNT" =~ ^[0-9]+$ ]] && [ "$OOM_COUNT" -gt 0 ]; then
    ALERTS+=("OOM KILL: $OOM_COUNT events in last hour from dmesg")
    OOM_STATUS="$OOM_COUNT OOM kill events in last hour"
else
    OOM_STATUS="none in last hour"
fi

# ---- Write to log ----
mkdir -p "$REPO/results"
{
    echo "=== $TIMESTAMP ==="
    echo "training: $TRAINING_STATUS"
    echo "gpu: $GPU_STATUS"
    echo "disk: $DISK_STATUS"
    echo "oom: $OOM_STATUS"
    echo "log: $LOG_STATUS"
    if [ ${#ALERTS[@]} -gt 0 ]; then
        for A in "${ALERTS[@]}"; do
            echo "ALERT: $A"
        done
    else
        echo "status: OK"
    fi
    echo ""
} >> "$LOG"

# Print alerts to stdout for cron email / monitoring
if [ ${#ALERTS[@]} -gt 0 ]; then
    echo "[$TIMESTAMP] ALERTS:"
    for A in "${ALERTS[@]}"; do
        echo "  *** $A ***"
    done
    exit 1
else
    echo "[$TIMESTAMP] OK: training=$TRAINING_STATUS gpu=$GPU_STATUS disk=$DISK_STATUS"
fi
