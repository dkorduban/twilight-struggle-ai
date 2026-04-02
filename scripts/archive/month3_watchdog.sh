#!/bin/bash
# Month 3 dispatcher health check — run manually or via watchdog prompt.
# Checks sentinels, reports status, exits 0 if all done or dispatcher alive.
set -euo pipefail
cd /home/dkord/code/twilight-struggle-ai

echo "=== Month 3 Sentinel Status ==="
check() { eval "$2" 2>/dev/null && echo "  sec $1: DONE" || echo "  sec $1: MISSING"; }
check 1 'grep -q "dir_alpha" cpp/tscore/mcts.hpp'
check 2 'grep -q "temperature" cpp/tools/collect_selfplay_rows_jsonl.cpp'
check 3 'grep -q "epsilon\|exploration_rate" cpp/tscore/game_loop.hpp'
check 4 'test -f scripts/compute_elo.py'
check 5 'test -f scripts/run_ladder.py'
check 6 'test -f cpp/tscore/ismcts.hpp'
check 7 'grep -q "model.type\|model_type.*attn" scripts/train_baseline.py'
check 8 'test -f scripts/play_server.py'

DONE=$(grep -c "DONE" <<< "$(bash "$0" 2>/dev/null)" 2>/dev/null || true)

echo ""
echo "=== Dispatcher Status ==="
if [ -f .codex_tasks/month3_dispatcher_active ]; then
    AGE=$(( $(date +%s) - $(stat -c %Y .codex_tasks/month3_dispatcher_active) ))
    echo "  File: $(cat .codex_tasks/month3_dispatcher_active)"
    echo "  Age: ${AGE}s ($((AGE/60))m)"
    if [ "$AGE" -lt 2100 ]; then
        echo "  Status: ALIVE (< 35m)"
    else
        echo "  Status: STALE (> 35m) — respawn needed"
    fi
else
    echo "  No dispatcher file found"
fi
