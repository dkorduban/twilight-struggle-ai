---
name: check-tasks
description: "Full system status: background tasks, running processes, GPU/CPU/memory utilization, lock files. Triggers on: /check-tasks, /status, task status, what's running, system status, check background."
---

# Status — Full System Overview

Shows background tasks, running processes, resource utilization, and lock files in one view.

## Execution (main agent, 2-3 turns)

Run all checks in parallel:

### 1. Background Codex tasks
```bash
find .codex_tasks -name "status.md" 2>/dev/null | sort
```
For each `status.md`: extract STATUS, AGENT, TASK, NOTE.
For DONE/FAILED tasks, also read `result.md`.

### 2. Running processes
```bash
pgrep -a python 2>/dev/null | head -20
pgrep -a cmake 2>/dev/null
```

### 3. Resource utilization
```bash
nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader 2>/dev/null || echo "No GPU detected"
free -m | awk 'NR==2{printf "RAM: %dMB used / %dMB total (%d%% used)\n", $3, $2, $3*100/$2}'
nproc
```

### 4. Lock files
```bash
for f in results/sweep.lock results/bench_pipeline.lock; do
  if [ -f "$f" ]; then
    echo "LOCKED: $f — $(cat $f)"
    # Check if PID is still alive
    pid=$(grep -oP 'PID=\K\d+' "$f" 2>/dev/null)
    if [ -n "$pid" ] && ! kill -0 "$pid" 2>/dev/null; then
      echo "  ⚠ PID $pid is STALE (process dead)"
    fi
  fi
done
```

## Output format

```
SYSTEM STATUS
=============

RESOURCES
  GPU: 45% util | 2.1GB / 4.0GB VRAM
  RAM: 18.2GB / 30.0GB (61%)
  CPU: 10 cores

LOCKS
  results/sweep.lock — PID=12345 started=2026-04-04 03:00 (ACTIVE)
  results/bench_pipeline.lock — not present

PROCESSES (python)
  12345 uv run python scripts/train_baseline.py ...
  12400 uv run python -c "import tscore; ..."

BACKGROUND TASKS
  task_id                           | status  | note
  ----------------------------------|---------|---------------------------
  impl_ismcts_batched               | RUNNING | Codex implementing
  
  Total: 1 task (running=1)
```

### Resource warnings (per standing policy §4)
- **RAM > 24GB used**: `⚠ WARNING: memory pressure (>80%)`
- **RAM > 27GB used**: `🔴 CRITICAL: memory near limit (>90%) — consider killing lowest-priority process`
- **GPU > 0% while another GPU task planned**: `⚠ GPU in use — do not launch training`

## If nothing is running

```
SYSTEM STATUS: idle
  GPU: 0% | RAM: 12.1GB/30.0GB | No locks | No background tasks
  Ready for work.
```
