#!/bin/bash
# Waits for PPO training and all Elo tournaments to finish (both locks free),
# then runs the OMP thread micro-benchmark.
# Launch once: bash scripts/run_after_training.sh &

set -euo pipefail
cd "$(dirname "$0")/.."

LOG="results/autonomous_decisions.log"

log() { echo "[run_after_training $(date -u +%H:%M:%SZ)] $*" | tee -a "$LOG"; }

log "Waiting for train_ppo.lock and elo_tournament.lock to clear..."

# Wait for PPO lock to be released
while flock -n results/train_ppo.lock true 2>/dev/null && kill -0 "$(cat results/train_ppo.lock 2>/dev/null)" 2>/dev/null; do
    sleep 60
done
# Poll until flock succeeds (lock file released)
until flock -n results/train_ppo.lock echo ok >/dev/null 2>&1; do
    sleep 60
done
log "train_ppo.lock is free."

# Wait for Elo tournament lock to be released
until flock -n results/elo_tournament.lock echo ok >/dev/null 2>&1; do
    sleep 60
done
log "elo_tournament.lock is free."

# Extra settle: wait for load average to drop below 2.0
log "Waiting for load average to settle below 2.0..."
for _ in $(seq 1 20); do
    LOAD=$(awk '{print $1}' /proc/loadavg)
    if python3 -c "exit(0 if float('$LOAD') < 2.0 else 1)" 2>/dev/null; then
        break
    fi
    sleep 30
done
log "Load average: $(awk '{print $1}' /proc/loadavg) — starting OMP bench."

bash scripts/omp_thread_bench.sh 2>&1 | tee -a "$LOG"

log "OMP bench complete. Results in results/analysis/omp_thread_bench_*.txt"
log "Next: implement thread budgets + PPO-lock serialization based on bench knee."
