---
name: train-and-bench
description: "Chain training → export → benchmark as one background pipeline. Triggers on: /train-and-bench, train and benchmark, run training pipeline, train this model."
---

# Train-and-Bench — Full Pipeline in One Background Command

Chains training → TorchScript export → benchmark (2000 games/side) into a single
background command. Main agent stays free the entire time.

## Input

Required:
- `--data-dir` or data directory name
- `--out-dir` or checkpoint name (must include seed suffix `_s{N}`)

Optional (defaults to v99 recipe):
- `--seed` (default 42)
- `--epochs` (default 95)
- `--lr`, `--batch-size`, `--hidden-dim`, etc.

Examples:
- `/train-and-bench --data-dir data/nash_c_only --out-dir v99_nash_c_95ep_s42`
- `/train-and-bench data/combined_v99_clean/heuristic_nash_b.parquet --seed 7 --epochs 120`

## Execution

### Step 1: Validate (1 turn, inline)

Pre-launch checklist (per standing policy §2):
1. Seed in name? Check `_s{N}` suffix exists
2. Lock clear? Check `results/sweep.lock`
3. GPU free? Check `nvidia-smi`
4. Memory OK? Check `free -m` (need 4GB free)

If any check fails, report and stop.

### Step 2: Build and launch pipeline (1 turn)

Construct a single chained bash command:

```bash
# Default v99 recipe args
TRAIN_ARGS="--epochs 95 --batch-size 1024 --lr 0.0012 --weight-decay 1e-4 \
  --label-smoothing 0.05 --one-cycle --hidden-dim 256 \
  --value-target final_vp --patience 20"

# Full pipeline: train → export → bench
nice -n 10 uv run python scripts/train_baseline.py \
  --data-dir <DATA> --out-dir data/checkpoints/<NAME> --seed <SEED> \
  $TRAIN_ARGS 2>&1 && \
nice -n 10 uv run python cpp/tools/export_baseline_to_torchscript.py \
  --checkpoint data/checkpoints/<NAME>/baseline_best.pt \
  --out data/checkpoints/<NAME>/baseline_best_scripted.pt 2>&1 && \
PYTHONPATH=build-ninja/bindings nice -n 19 uv run python -c "
import tscore, math
path = 'data/checkpoints/<NAME>/baseline_best_scripted.pt'
n = 2000
ussr = tscore.benchmark_batched(path, tscore.Side.USSR, n, pool_size=32, seed=9000)
us   = tscore.benchmark_batched(path, tscore.Side.US,   n, pool_size=32, seed=9000+n)
uw = sum(1 for r in ussr if r.winner == tscore.Side.USSR)
sw = sum(1 for r in us   if r.winner == tscore.Side.US)
up = uw/n*100; sp = sw/n*100; cp = (uw+sw)/(2*n)*100
use = math.sqrt(up/100*(1-up/100)/n)*100
sse = math.sqrt(sp/100*(1-sp/100)/n)*100
cse = math.sqrt((up/100*(1-up/100)+sp/100*(1-sp/100))/(4*n))*100
print(f'<NAME> | USSR {up:.1f}% +/-{use:.1f} | US {sp:.1f}% +/-{sse:.1f} | Combined {cp:.1f}% +/-{cse:.1f}')
" 2>&1
```

Launch with `run_in_background=true`.

### Step 3: Report immediately

```
Pipeline launched: <NAME>
  Data: <DATA> | Seed: <SEED> | Epochs: <EPOCHS>
  Estimated time: ~25-40 min (training ~15-25, export ~1, bench ~10)
  Monitor: check background task notification
```

### Step 4: On completion

Report results as markdown table. Ask if user wants to log to experiment_log.

## Rules

- **MUST use `run_in_background=true`** (standing policy §5 — never block main agent)
- **MUST include seed in checkpoint name** (policy §2.6)
- Write lock file inside the script (train_baseline.py handles this if using sweep.lock pattern)
- Chain with `&&` so export/bench only run if training succeeds
- If multiple models needed: chain all in one command, or launch separate background commands
