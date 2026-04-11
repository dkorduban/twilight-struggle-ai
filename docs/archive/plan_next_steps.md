# Overnight Autonomous Plan: PPO v4 → v5 → Architecture Sweep

**Date**: 2026-04-08
**Author**: Working spec for Haiku-level agents
**Status**: Active

---

## MANDATORY: Decision Logging

**Every decision you make MUST be logged.** Append to `results/autonomous_decisions.log`:

```
[YYYY-MM-DD HH:MM] DECISION: <what you decided>
  REASON: <why — cite specific numbers>
  ACTION: <exact command or change>
  EXPECTED: <what you expect to happen>
```

Examples:
```
[2026-04-08 02:15] DECISION: Skip PPO v5, go to architecture sweep
  REASON: PPO v4 combined WR plateaued at 82.1% for iters 150-200 (< 2pp change)
  ACTION: Running train_baseline.py on rollout data with model-type=country_attn_side
  EXPECTED: Attention model should reach similar card_top1 as GNN on stronger data

[2026-04-08 03:30] DECISION: Reduce learning rate for PPO v5
  REASON: PPO v4 best was iter 10 (88.4%); final iter 200 regressed to 78.2%
  ACTION: --lr 1e-5 --clip-eps 0.15
  EXPECTED: More stable training, less regression
```

**If you skip a step, log why. If you change a hyperparameter, log why. If something fails, log the error.**

Create the log file at the start:
```bash
mkdir -p results
echo "=== Autonomous run started $(date -Iseconds) ===" >> results/autonomous_decisions.log
```

---

## Current State

PPO v4 is running (200 iterations). Benchmarks so far:

| Iter | USSR WR | US WR | Combined |
|------|---------|-------|----------|
| 10   | 97.2%   | 79.6% | 88.4%    |
| 20   | 96.4%   | 79.2% | 87.8%    |
| 30   | 95.2%   | 66.6% | 80.9%    |

### What's done (DO NOT redo)
- 32-dim scalars in C++ engine, both `build/` and `build-ninja/` rebuilt
- 60-dim model (32 scalars + 28 region)
- League v4 pool (10 opponents in `data/checkpoints/league_v4/`)
- `train_ppo.py` has: LR warmup, weight norm logging, logit saving in parquet
- PPO v4 training launched and in progress
- Rollout parquet files accumulating in `data/ppo_v4_rollouts/`

---

## Phase 1: Wait for PPO v4 to finish

**Do not interfere with the running PPO v4 process.** Just wait and monitor.

### Check if PPO v4 is still running
```bash
pgrep -af "train_ppo.*ppo_v4_league" || echo "PPO v4 has finished"
```

### After it finishes, extract final results
```bash
# Find the log — it's either in the background task output or W&B
# Check the latest checkpoint iteration:
ls -t data/checkpoints/ppo_v4_league/ppo_iter*.pt | head -5

# Extract all benchmark lines
grep "Benchmark" data/checkpoints/ppo_v4_league/*.log 2>/dev/null || \
grep "Benchmark" results/ppo_v4*.log 2>/dev/null || \
echo "Check W&B for benchmark results"
```

### Record PPO v4 final results
Log the final benchmark numbers to `results/autonomous_decisions.log`.

### Evaluate: which iteration was best?
```bash
uv run python -c "
import torch
for name in ['ppo_best', 'ppo_iter0050', 'ppo_iter0100', 'ppo_iter0150', 'ppo_iter0200']:
    path = f'data/checkpoints/ppo_v4_league/{name}.pt'
    try:
        sd = torch.load(path, map_location='cpu', weights_only=False)
        sd = sd.get('model_state_dict', sd)
        w = sd['scalar_encoder.weight']
        print(f'{name}: core_norm={w[:,:11].norm():.3f} new_norm={w[:,11:32].norm():.3f} region_norm={w[:,32:60].norm():.3f}')
    except FileNotFoundError:
        pass
"
```

---

## Phase 2: PPO v5 — resume from best with tuned hyperparameters

**Start this only after PPO v4 finishes.**

### Decision: choose hyperparameters based on PPO v4 outcome

Read the PPO v4 benchmarks and decide:

| PPO v4 outcome | PPO v5 action |
|----------------|---------------|
| Best combined > 85%, final iter close to best | Continue with same hyperparams, 200 more iters |
| Best combined > 85%, but final regressed > 5pp | Lower LR to 1e-5, clip to 0.15, 100 iters |
| Best combined 75-85% | Lower LR to 1e-5, raise heuristic mix to 0.3, 150 iters |
| Best combined < 75% | Lower LR to 5e-6, clip to 0.1, ent-coef to 0.02, 100 iters |

**LOG YOUR DECISION** before launching.

### PPO v5 command template
```bash
uv run python scripts/train_ppo.py \
    --checkpoint data/checkpoints/ppo_v4_league/ppo_best.pt \
    --out-dir data/checkpoints/ppo_v5_league \
    --league data/checkpoints/league_v4 \
    --league-save-every 20 \
    --n-iterations {N_ITERS} \
    --games-per-iter 200 \
    --lr {LR} \
    --lr-warmup-iters 10 \
    --ppo-epochs 1 \
    --clip-eps {CLIP} \
    --max-kl 0.15 \
    --ent-coef {ENT} \
    --ent-coef-final {ENT_FINAL} \
    --vf-coef 0.5 \
    --self-play \
    --self-play-heuristic-mix {HEUR_MIX} \
    --vp-reward-coef 0.1 \
    --save-rollout-parquet data/ppo_v5_rollouts/ \
    --benchmark-every 10 \
    --wandb \
    --seed 500000 \
    2>&1 | tee results/ppo_v5.log
```

Fill in `{...}` placeholders based on your decision table above. Typical values:
- Stable continuation: `LR=3e-5, CLIP=0.2, ENT=0.01, ENT_FINAL=0.001, HEUR_MIX=0.2, N_ITERS=200`
- Conservative recovery: `LR=1e-5, CLIP=0.15, ENT=0.015, ENT_FINAL=0.005, HEUR_MIX=0.3, N_ITERS=100`

### Monitor PPO v5
Same metrics as v4. Check benchmark every 10 iters. If combined WR drops > 10pp from v5 best at any point, **stop the run** and log why.

---

## Phase 3: Dataset assembly from rollout data

**Start this after PPO v5 finishes (or in parallel if you have spare CPU).**

This is the most important data engineering step. Be rigorous.

### 3a. Inventory rollout parquet files

```bash
uv run python -c "
import pyarrow.parquet as pq
from pathlib import Path
import json

for rollout_dir in ['data/ppo_v4_rollouts', 'data/ppo_v5_rollouts']:
    p = Path(rollout_dir)
    if not p.exists():
        print(f'{rollout_dir}: does not exist')
        continue
    files = sorted(p.glob('rollout_iter_*.parquet'))
    total_rows = 0
    for f in files:
        total_rows += pq.read_metadata(f).num_rows
    print(f'{rollout_dir}: {len(files)} files, {total_rows:,} rows')

    # Show schema from first file
    if files:
        t = pq.read_table(files[0])
        print(f'  Columns: {t.column_names}')
        has_logits = 'card_logits' in t.column_names
        print(f'  Has logits: {has_logits}')
        
        # Check meta files for checkpoint info
        metas = sorted(p.glob('*.meta.json'))
        if metas:
            with open(metas[0]) as f:
                meta = json.load(f)
            print(f'  Sample meta: {meta}')
"
```

### 3b. Combine into a single training dataset

**CRITICAL RULES:**
1. Split by game_id, NOT by row. All rows from the same game must be in the same split.
2. Use the SAME proxy eval game_ids as `data/v3_selfplay_05M_v2/EXCLUDE_GAME_IDS.txt`. Never include those games in training.
3. Validation split uses salt `"_val"` in hash: `md5(str(game_id) + "_val") % 10 == 0`.
4. Proxy eval uses `md5(str(game_id)) % 10 == 0`.
5. If a game_id appears in both proxy eval and val hashes, it goes to proxy eval (exclude from train AND val).

```bash
uv run python -c "
import pyarrow.parquet as pq
import pyarrow as pa
from pathlib import Path
import hashlib

# Collect all rollout files
all_files = []
for d in ['data/ppo_v4_rollouts', 'data/ppo_v5_rollouts']:
    p = Path(d)
    if p.exists():
        all_files.extend(sorted(p.glob('rollout_iter_*.parquet')))

print(f'Found {len(all_files)} rollout files')
if not all_files:
    print('ERROR: No rollout files found. Cannot build dataset.')
    exit(1)

# Read and concatenate
tables = [pq.read_table(f) for f in all_files]
combined = pa.concat_tables(tables)
print(f'Combined: {len(combined):,} rows')

# Check required columns exist
required = ['influence', 'cards', 'scalars', 'card_idx', 'mode_idx', 'reward']
missing = [c for c in required if c not in combined.column_names]
if missing:
    print(f'ERROR: Missing columns: {missing}')
    exit(1)

# Save combined
out_dir = Path('data/ppo_rollout_combined')
out_dir.mkdir(parents=True, exist_ok=True)
pq.write_table(combined, out_dir / 'all_rollouts.parquet')
print(f'Saved to {out_dir}/all_rollouts.parquet')

# Count rows per column for sanity
print(f'Columns: {combined.column_names}')
print(f'Null counts: { {c: combined.column(c).null_count for c in combined.column_names} }')
"
```

### 3c. Validate dataset integrity

```bash
uv run python -c "
import pyarrow.parquet as pq
import numpy as np

t = pq.read_table('data/ppo_rollout_combined/all_rollouts.parquet')
print(f'Total rows: {len(t):,}')

# Check feature dimensions
inf = t.column('influence')[0].as_py()
cards = t.column('cards')[0].as_py()
scalars = t.column('scalars')[0].as_py()
print(f'influence dim: {len(inf)} (expect 172)')
print(f'cards dim: {len(cards)} (expect 448)')  
print(f'scalars dim: {len(scalars)} (expect 32)')

# Check label ranges
card_idxs = t.column('card_idx').to_pylist()
mode_idxs = t.column('mode_idx').to_pylist()
print(f'card_idx range: [{min(card_idxs)}, {max(card_idxs)}] (expect [0, 110])')
print(f'mode_idx range: [{min(mode_idxs)}, {max(mode_idxs)}] (expect [0, 4])')

# Check reward distribution
rewards = t.column('reward').to_pylist()
nonzero_rewards = [r for r in rewards if abs(r) > 0.001]
print(f'Nonzero rewards: {len(nonzero_rewards)} (these are terminal steps)')
print(f'Reward range: [{min(rewards):.3f}, {max(rewards):.3f}]')

# Check for NaNs in features
for col in ['influence', 'cards', 'scalars']:
    vals = t.column(col).to_pylist()
    flat = [v for row in vals for v in row]
    nan_count = sum(1 for v in flat if v != v)  # NaN != NaN
    print(f'{col} NaN count: {nan_count} (must be 0)')

# If gae_return exists, check it
if 'gae_return' in t.column_names:
    returns = t.column('gae_return').to_pylist()
    print(f'gae_return range: [{min(returns):.3f}, {max(returns):.3f}]')
    print(f'gae_return mean: {np.mean(returns):.4f}')
"
```

**If any check fails, STOP and log the failure. Do not proceed to architecture sweep with bad data.**

---

## Phase 4: Architecture sweep on rollout data

**Start this only after Phase 3 dataset passes all integrity checks.**

**Prerequisites:**
- Combined rollout dataset exists at `data/ppo_rollout_combined/all_rollouts.parquet`
- At least 200,000 rows (if less, log and skip — not enough data)
- All integrity checks passed

### 4a. Train GNN baseline (current architecture) on rollout data

This is the control — we already know GNN works. Training on PPO rollout data should produce
a model comparable to or better than the original BC models, since the data comes from a
stronger policy.

```bash
uv run python scripts/train_baseline.py \
    --data-dir data/ppo_rollout_combined \
    --out-dir data/checkpoints/arch_sweep_gnn_s7 \
    --model-type control_feat_gnn_side \
    --epochs 60 \
    --patience 15 \
    --batch-size 8192 \
    --lr 0.0024 \
    --hidden-dim 256 \
    --dropout 0.1 \
    --weight-decay 1e-4 \
    --label-smoothing 0.05 \
    --one-cycle \
    --seed 7 \
    --value-target final_vp \
    --deterministic-split \
    --num-workers 4 \
    2>&1 | tee results/arch_sweep_gnn_s7.log
```

### 4b. Train attention model on rollout data

```bash
uv run python scripts/train_baseline.py \
    --data-dir data/ppo_rollout_combined \
    --out-dir data/checkpoints/arch_sweep_attn_s7 \
    --model-type country_attn_side \
    --epochs 60 \
    --patience 15 \
    --batch-size 8192 \
    --lr 0.0024 \
    --hidden-dim 256 \
    --dropout 0.1 \
    --weight-decay 1e-4 \
    --label-smoothing 0.05 \
    --one-cycle \
    --seed 7 \
    --value-target final_vp \
    --deterministic-split \
    --num-workers 4 \
    2>&1 | tee results/arch_sweep_attn_s7.log
```

**WARNING**: Attention model is ~16× slower per epoch than GNN. This is expected.
Budget ~60 min per attention run vs ~4 min for GNN.

### 4c. Train plain baseline (MLP, no graph/attention) on rollout data

```bash
uv run python scripts/train_baseline.py \
    --data-dir data/ppo_rollout_combined \
    --out-dir data/checkpoints/arch_sweep_baseline_s7 \
    --model-type control_feat \
    --epochs 60 \
    --patience 15 \
    --batch-size 8192 \
    --lr 0.0024 \
    --hidden-dim 256 \
    --dropout 0.1 \
    --weight-decay 1e-4 \
    --label-smoothing 0.05 \
    --one-cycle \
    --seed 7 \
    --value-target final_vp \
    --deterministic-split \
    --num-workers 4 \
    2>&1 | tee results/arch_sweep_baseline_s7.log
```

### 4d. Compare results

```bash
uv run python -c "
import re
from pathlib import Path

models = {
    'GNN': 'results/arch_sweep_gnn_s7.log',
    'Attention': 'results/arch_sweep_attn_s7.log',
    'Baseline MLP': 'results/arch_sweep_baseline_s7.log',
}

print(f'{\"Model\":<15} {\"val_loss\":>10} {\"card_top1\":>10} {\"mode_acc\":>10} {\"value_brier\":>12}')
print('-' * 60)

for name, logfile in models.items():
    p = Path(logfile)
    if not p.exists():
        print(f'{name:<15} NOT RUN')
        continue
    text = p.read_text()
    # Extract best metrics from [BEST] lines
    best_lines = [l for l in text.split('\n') if '[BEST]' in l]
    if not best_lines:
        print(f'{name:<15} NO BEST FOUND')
        continue
    last_best = best_lines[-1]
    vl = re.search(r'val_loss=([\d.]+)', last_best)
    ct = re.search(r'val_card_top1=([\d.]+)', last_best)
    ma = re.search(r'val_mode_acc=([\d.]+)', last_best)
    vb = re.search(r'val_value_brier=([\d.]+)', last_best)
    print(f'{name:<15} {vl.group(1) if vl else \"?\":>10} {ct.group(1) if ct else \"?\":>10} {ma.group(1) if ma else \"?\":>10} {vb.group(1) if vb else \"?\":>12}')
"
```

### 4e. Benchmark best architecture vs heuristic

For each architecture that trained successfully:
```bash
# Export best checkpoint as TorchScript and benchmark
PYTHONPATH=build-ninja/bindings uv run python -c "
import tscore, torch, sys
sys.path.insert(0, 'python')
from tsrl.policies.model import TSControlFeatGNNModel, TSCountryAttnSideModel, TSControlFeatGNNSideModel

for tag, ckpt_dir, model_cls in [
    ('GNN', 'data/checkpoints/arch_sweep_gnn_s7', TSControlFeatGNNSideModel),
    ('Attn', 'data/checkpoints/arch_sweep_attn_s7', TSCountryAttnSideModel),
    ('MLP', 'data/checkpoints/arch_sweep_baseline_s7', TSControlFeatGNNModel),
]:
    best = f'{ckpt_dir}/baseline_best.pt'
    try:
        raw = torch.load(best, map_location='cpu', weights_only=False)
    except FileNotFoundError:
        print(f'{tag}: no checkpoint')
        continue
    sd = raw.get('model_state_dict', raw)
    model = model_cls(hidden_dim=256)
    model.load_state_dict(sd, strict=False)
    model.eval()
    scripted = torch.jit.script(model)
    tmp = f'/tmp/arch_sweep_{tag}.pt'
    torch.jit.save(scripted, tmp)

    ussr = tscore.benchmark_batched(tmp, tscore.Side.USSR, 500, seed=50000)
    us = tscore.benchmark_batched(tmp, tscore.Side.US, 500, seed=50500)
    ussr_wr = sum(1 for r in ussr if r.winner == tscore.Side.USSR) / len(ussr)
    us_wr = sum(1 for r in us if r.winner == tscore.Side.US) / len(us)
    combined = (ussr_wr + us_wr) / 2
    print(f'{tag}: USSR={ussr_wr:.1%} US={us_wr:.1%} combined={combined:.1%}')
"
```

**Log the architecture comparison results.** This determines whether we switch architectures for PPO v6.

---

## Phase 5: Decision point — what architecture for PPO v6?

After Phase 4, read the comparison results and decide:

| Outcome | Action |
|---------|--------|
| Attention > GNN by > 3pp combined | Use attention for PPO v6 |
| Attention ≈ GNN (within 3pp) | Keep GNN (simpler, faster) |
| GNN > Attention | Keep GNN, attention is not worth the 16× cost |
| Both < PPO v5 best WR | Architecture isn't the bottleneck; try adversarial training |

**LOG YOUR DECISION.**

If switching to attention architecture:
```bash
# PPO v6 with attention model
uv run python scripts/train_ppo.py \
    --checkpoint data/checkpoints/arch_sweep_attn_s7/baseline_best.pt \
    --out-dir data/checkpoints/ppo_v6_attn \
    --league data/checkpoints/league_v4 \
    --league-save-every 20 \
    --n-iterations 200 \
    --games-per-iter 200 \
    --lr 1e-5 \
    --lr-warmup-iters 15 \
    --ppo-epochs 1 \
    --clip-eps 0.2 \
    --max-kl 0.25 \
    --ent-coef 0.01 \
    --ent-coef-final 0.001 \
    --vf-coef 0.5 \
    --self-play \
    --self-play-heuristic-mix 0.2 \
    --vp-reward-coef 0.1 \
    --benchmark-every 10 \
    --wandb \
    --seed 600000 \
    2>&1 | tee results/ppo_v6_attn.log
```

---

## File locations

| Item | Path |
|------|------|
| PPO v4 checkpoints | `data/checkpoints/ppo_v4_league/` |
| PPO v4 rollouts | `data/ppo_v4_rollouts/` |
| PPO v5 checkpoints | `data/checkpoints/ppo_v5_league/` |
| PPO v5 rollouts | `data/ppo_v5_rollouts/` |
| League v4 pool | `data/checkpoints/league_v4/` |
| Combined rollout data | `data/ppo_rollout_combined/` |
| Arch sweep checkpoints | `data/checkpoints/arch_sweep_{gnn,attn,baseline}_s7/` |
| Decision log | `results/autonomous_decisions.log` |
| PPO training script | `scripts/train_ppo.py` |
| BC training script | `scripts/train_baseline.py` |
| Model definitions | `python/tsrl/policies/model.py` |
| **Old plan (IGNORE)** | `docs/plan_ppo_v4.md` — DO NOT follow, steps already done |

---

## Execution order summary

```
1. Wait for PPO v4 to finish (check with pgrep)
2. Log PPO v4 results
3. Launch PPO v5 (from ppo_best.pt, tuned hyperparams based on v4 results)
4. While PPO v5 runs (or after): assemble rollout dataset (Phase 3)
5. After PPO v5: run architecture sweep (Phase 4)
6. After arch sweep: decide PPO v6 architecture (Phase 5)
7. Launch PPO v6 if architecture changed
```

**Total estimated wall time**: 4-8 hours depending on iteration speed and architecture sweep.

---

## Hard rules

1. **NEVER skip dataset validation** (Phase 3c). Bad data = wasted GPU hours.
2. **ALWAYS log decisions** to `results/autonomous_decisions.log`.
3. **NEVER modify `train_ppo.py` or `train_baseline.py`** — use them as-is.
4. **NEVER delete checkpoints** — only create new ones.
5. **If a run fails**, log the error and try the next phase. Do not retry the same command more than once.
6. **If combined WR drops below 50%**, STOP everything and log "POLICY COLLAPSE — manual intervention needed".
7. **Benchmark numbers are the ground truth**, not rollout WR (rollout WR is noisy due to league opponent mixing).
