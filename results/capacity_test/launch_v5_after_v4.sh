#!/bin/bash
set -e
cd /home/dkord/code/twilight-struggle-ai

# Wait for v4 to finish (PID 290961)
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Waiting for v4 US-only (PID 290961) to finish..."
while kill -0 290961 2>/dev/null; do
    sleep 30
done
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] V4 complete. Sleeping 10s for GPU cooldown..."
sleep 10

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Launching capacity test v5..." | tee -a results/autonomous_decisions.log
bash results/capacity_test/run_capacity_ppo_v5.sh >> results/capacity_test/v5_combined.log 2>&1
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] V5 complete." | tee -a results/autonomous_decisions.log
