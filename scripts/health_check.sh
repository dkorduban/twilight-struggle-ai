#!/usr/bin/env bash
# health_check.sh — local training environment health monitor
# Run via cron: */30 * * * * /path/to/health_check.sh >> /path/to/results/health_checks.log 2>&1

set -euo pipefail

REPO="/home/dkord/code/twilight-struggle-ai"
LOG="$REPO/results/health_checks.log"
ALERTS=()

ts() { date "+%Y-%m-%d %H:%M:%S"; }

log() { echo "[$(ts)] $1" | tee -a "$LOG"; }
alert() { ALERTS+=("$1"); log "ALERT: $1"; }

log "--- health check ---"

# 1. Training process
if pgrep -f "python.*train" > /dev/null 2>&1; then
    TRAIN_PID=$(pgrep -f "python.*train" | head -1)
    TRAIN_CMD=$(ps -p "$TRAIN_PID" -o args= 2>/dev/null | cut -c1-120 || echo "unknown")
    log "TRAIN: running (PID=$TRAIN_PID) $TRAIN_CMD"
else
    alert "No training process found (pgrep python.*train returned nothing)"
fi

# 2. GPU memory
if command -v nvidia-smi &>/dev/null; then
    GPU_INFO=$(nvidia-smi --query-gpu=memory.used,memory.total,utilization.gpu \
        --format=csv,noheader,nounits 2>/dev/null | head -1 || echo "0,0,0")
    USED=$(echo "$GPU_INFO" | awk -F',' '{print $1}' | tr -d ' ')
    TOTAL=$(echo "$GPU_INFO" | awk -F',' '{print $2}' | tr -d ' ')
    UTIL=$(echo "$GPU_INFO" | awk -F',' '{print $3}' | tr -d ' ')
    if [[ "$TOTAL" -gt 0 ]]; then
        PCT=$(( USED * 100 / TOTAL ))
        log "GPU: ${USED}/${TOTAL} MB (${PCT}%), util=${UTIL}%"
        if [[ "$PCT" -ge 90 ]]; then
            alert "GPU memory at ${PCT}% (${USED}/${TOTAL} MB)"
        fi
    else
        log "GPU: nvidia-smi returned no data"
    fi
else
    log "GPU: nvidia-smi not found"
fi

# 3. Disk space
for DIR in "$REPO/results" "$REPO/data"; do
    if [[ -d "$DIR" ]]; then
        AVAIL_KB=$(df -k "$DIR" | awk 'NR==2 {print $4}')
        AVAIL_GB=$(( AVAIL_KB / 1024 / 1024 ))
        USED_HUMAN=$(du -sh "$DIR" 2>/dev/null | awk '{print $1}' || echo "?")
        log "DISK $DIR: ${USED_HUMAN} used, ${AVAIL_GB}GB free"
        if [[ "$AVAIL_GB" -lt 5 ]]; then
            alert "Low disk space at $DIR: only ${AVAIL_GB}GB free"
        fi
    fi
done

# 4. Recent log tail
LATEST_LOG=$(find "$REPO/results" -name "*.log" -newer "$LOG" -o -name "*.log" \
    2>/dev/null | grep -v health_checks | sort -t/ -k1 | tail -1 || true)
if [[ -z "$LATEST_LOG" ]]; then
    LATEST_LOG=$(find "$REPO/results" -name "*.log" 2>/dev/null | grep -v health_checks \
        | xargs ls -t 2>/dev/null | head -1 || true)
fi
if [[ -n "$LATEST_LOG" ]]; then
    log "RECENT LOG ($LATEST_LOG):"
    tail -5 "$LATEST_LOG" 2>/dev/null | while IFS= read -r line; do
        log "  | $line"
    done
else
    log "RECENT LOG: no .log files found in results/"
fi

# 5. OOM kills
OOM_COUNT=$(dmesg --level=err,crit,alert,emerg 2>/dev/null \
    | grep -c "Out of memory\|oom-kill\|Killed process" || true)
if [[ "$OOM_COUNT" -gt 0 ]]; then
    alert "OOM kill events found in dmesg: $OOM_COUNT occurrence(s)"
    dmesg --level=err 2>/dev/null | grep -i "oom\|killed process" | tail -3 | while IFS= read -r line; do
        log "  OOM: $line"
    done
else
    log "OOM: no OOM events in dmesg"
fi

# Summary
if [[ "${#ALERTS[@]}" -eq 0 ]]; then
    log "STATUS: OK (${#ALERTS[@]} alerts)"
else
    log "STATUS: ${#ALERTS[@]} ALERT(S) — ${ALERTS[*]}"
fi
log "--- end ---"
