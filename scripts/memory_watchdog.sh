#!/bin/bash
# Memory watchdog: kills largest non-essential python process when RAM > 27GB used
# Run in background: bash scripts/memory_watchdog.sh &
MIN_AVAIL_MB=4000   # kill when <4GB available (RAM - buffers/cache)
CHECK_INTERVAL=10   # seconds

while true; do
    AVAIL_MB=$(free -m | awk 'NR==2{print $7}')
    if [ "$AVAIL_MB" -lt "$MIN_AVAIL_MB" ]; then
        # Find largest python process that is NOT training (train_baseline.py)
        VICTIM=$(ps aux --sort=-%mem | grep python | grep -v 'train_baseline\|wandb-core\|grep' | head -1)
        VICTIM_PID=$(echo "$VICTIM" | awk '{print $2}')
        VICTIM_RSS=$(echo "$VICTIM" | awk '{printf "%.0f", $6/1024}')
        if [ -n "$VICTIM_PID" ] && [ "$VICTIM_RSS" -gt 2000 ]; then
            echo "[$(date '+%H:%M:%S')] WATCHDOG: only ${AVAIL_MB}MB available. Killing PID $VICTIM_PID (${VICTIM_RSS}MB RSS)"
            kill -9 "$VICTIM_PID" 2>/dev/null
        fi
    fi
    sleep "$CHECK_INTERVAL"
done
