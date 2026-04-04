---
name: speedup-analysis
description: "Analyze a slow process, identify bottleneck, write spec, delegate optimization to Codex. Triggers on: /speedup-analysis, speed this up, optimize performance, this is too slow, why is this slow."
---

# Speedup Analysis — Opus Analyzes, Codex Implements

Per standing policy §8: when encountering a slow process, don't accept it — analyze
and speed it up. Investment in speedups always pays off because experiments run many times.

## Input

Either:
- A description of what's slow: `/speedup-analysis ISMCTS takes 3 min/game`
- A running process to profile: `/speedup-analysis the current benchmark`
- A script path: `/speedup-analysis scripts/run_ismcts_diagnostic.sh`

## Execution

### Step 1: Measure current performance (Opus, 1-2 turns)

Profile the slow operation:
```bash
# Time a representative run
time <command> 2>&1 | tail -20

# Check resource utilization during run
nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader
top -bn1 | head -20
```

Record: wall time, GPU%, CPU%, memory usage, I/O.

### Step 2: Identify bottleneck (Opus, 1-2 turns)

Read the code being profiled. Look for:

1. **Unbatched NN inference** — AXIOM: all NN inference must be batched. If single-sample
   forward passes exist, this is the #1 bottleneck. Fix: batch across available parallelism
   (games, determinizations, time steps).

2. **Sequential loops over parallelizable work** — games, determinizations, simulations
   running one-at-a-time when they could overlap.

3. **CPU when GPU is idle** — if GPU is at 0% and the task does NN inference, move to CUDA.

4. **Single-threaded on multi-core** — if CPU utilization is 1/N_cores, add threading
   or increase pool_size.

5. **Python overhead in hot loop** — if a tight loop calls Python per iteration,
   consider moving to C++ or batching.

### Step 3: Write spec (Opus, 1 turn)

Write `specs/<name>_speedup.md` with:
- Current performance (measured)
- Bottleneck identified
- Proposed fix (specific code changes)
- Expected speedup (estimated)
- Correctness verification plan (before/after comparison)

### Step 4: Delegate to Codex (background)

```
Agent(
  subagent_type: "bg-codex-implementer",
  isolation: "worktree",
  run_in_background: true,
  prompt: "TASK_ID: speedup_<name>\nMODE: implement\nTASK: <spec content>"
)
```

Report immediately:
```
Speedup analysis complete:
  Bottleneck: <description>
  Expected improvement: <X>x
  Delegated to Codex in background worktree.
  Verify after: run same benchmark, compare results within expected variance.
```

### Step 5: Verify correctness (after Codex completes)

**CRITICAL**: Run the same benchmark/test before and after. Compare:
- Results must be bit-identical or within expected variance
- A 10× speedup that silently changes results is worse than no speedup

## Rules

- **Be proactive**: don't wait for the user to complain. When you see a slow process
  during normal work, initiate this analysis yourself.
- **Don't trust "it's hard"**: historically, simple batching/parallelization patterns
  yielded 15-20× speedups that were initially dismissed as hard.
- **Codex in background is free**: implementation cost is near-zero when done in a
  background worktree. The only cost is verification time.
- **Always verify correctness**: optimization without verification is a regression risk.
- **Increase parallelism within one process first**: two 50%-GPU processes thrash.
  One at 100% is always better. (Standing policy §3)
