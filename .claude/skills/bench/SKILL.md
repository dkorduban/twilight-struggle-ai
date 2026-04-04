---
name: bench
description: "Benchmark one or more model checkpoints (2000 games/side) with auto-logging. Triggers on: /bench, benchmark this model, run benchmark, bench checkpoint."
---

# Bench — One-Command Benchmark with Auto-Logging

Benchmarks model checkpoints against the heuristic opponent (2000 games/side),
reports results, and optionally logs to the experiment log.

## Input

One or more checkpoint paths or directory names. Examples:
- `/bench data/checkpoints/v99_nash_c_95ep_s42`
- `/bench v99_nash_c_95ep_s42 v99_nash_b_95ep_s7`
- `/bench data/checkpoints/*/baseline_best_scripted.pt` (glob)

## Execution

### Step 1: Resolve checkpoints (1 turn)

For each input:
- If it's a directory: look for `baseline_best_scripted.pt` inside
- If it's a `.pt` file: use directly
- If scripted model doesn't exist but `baseline_best.pt` does: export first:
  ```bash
  uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint <dir>/baseline_best.pt --out <dir>/baseline_best_scripted.pt
  ```

### Step 2: Run benchmarks (background)

Launch as a single background command:

```bash
PYTHONPATH=build-ninja/bindings nice -n 19 uv run python -c "
import tscore, math

models = {<name: path dict>}
n = 2000
for name, path in models.items():
    ussr = tscore.benchmark_batched(path, tscore.Side.USSR, n, pool_size=32, seed=9000)
    us   = tscore.benchmark_batched(path, tscore.Side.US,   n, pool_size=32, seed=9000+n)
    uw = sum(1 for r in ussr if r.winner == tscore.Side.USSR)
    sw = sum(1 for r in us   if r.winner == tscore.Side.US)
    up = uw/n*100; sp = sw/n*100; cp = (uw+sw)/(2*n)*100
    use = math.sqrt(up/100*(1-up/100)/n)*100
    sse = math.sqrt(sp/100*(1-sp/100)/n)*100
    cse = math.sqrt((up/100*(1-up/100)+sp/100*(1-sp/100))/(4*n))*100
    print(f'{name} | USSR {up:.1f}% +/-{use:.1f} | US {sp:.1f}% +/-{sse:.1f} | Combined {cp:.1f}% +/-{cse:.1f}')
"
```

Use `run_in_background=true`. Estimated time: ~5 min per model.

### Step 3: Report results (when background completes)

Format as markdown table:

```
| Model | USSR WR | US WR | Combined |
|-------|---------|-------|----------|
| name  | X% ±Y  | X% ±Y | X% ±Y   |
```

### Step 4: Auto-log (if user confirms)

Ask: "Log to docs/experiment_log_phase1.md?" If yes, append results.

## Notes

- Always use seed=9000 for USSR, seed=9000+n for US (consistent comparison)
- pool_size=32 for batched benchmark (CPU-bound, uses ~80% CPU)
- nice -n 19 so benchmarks don't block training
- Do NOT run if `results/bench_pipeline.lock` exists and PID is alive
