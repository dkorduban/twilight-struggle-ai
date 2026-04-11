# PPO v4 Implementation Plan

**Date**: 2026-04-07
**Author**: Auto-generated working spec for Haiku-level implementation agents
**Status**: Ready to execute

---

## Overview

PPO v4 adds 21 strategically important scalar features (bear_trap, quagmire, CMC,
NATO, NORAD, flower_power, etc.) to the PPO v3 best checkpoint via weight migration,
then continues league PPO training with LR warmup and full rollout logging.

**Decision**: Skip Phase 4 BC architecture sweep. Go straight to PPO v4.
Rationale: PPO v3 has clear remaining headroom from 21 unseen features; arch
comparisons on weak BC data are confounded; rollout data gets collected for free.

---

## Prerequisites (already done)

These are already complete. Do NOT redo them:

- `kScalarDim = 32` in `cpp/tscore/nn_features.cpp` (line 15)
- `SCALAR_DIM = 32` in `python/tsrl/policies/model.py` (line 45)
- `SCALAR_DIM = 32` in `scripts/train_ppo.py` (line 73)
- C++ rebuilt with 32-dim scalars
- Migration script exists at `scripts/migrate_scalar_dim.py`
- PPO v3 best checkpoint at `data/checkpoints/ppo_v3_league/ppo_best.pt`
- League v3 pool at `data/checkpoints/league_v3/` (11 TorchScript checkpoints)

---

## Step 1: Migrate v3 checkpoint to 60-dim scalar encoder

### 1a. Run the migration script

**File**: `scripts/migrate_scalar_dim.py` (no changes needed)
**Command**:
```bash
mkdir -p data/checkpoints/ppo_v4_start
uv run python scripts/migrate_scalar_dim.py \
    --input data/checkpoints/ppo_v3_league/ppo_best.pt \
    --output data/checkpoints/ppo_v4_start/ppo_v3_60dim.pt
```

**Expected output**: `ppo_best.pt: 39->60 dim (with region scalars, zeros inserted before region) -> written`

**Verify**:
```bash
uv run python -c "
import torch
ckpt = torch.load('data/checkpoints/ppo_v4_start/ppo_v3_60dim.pt', map_location='cpu', weights_only=False)
sd = ckpt['model_state_dict']
w = sd['scalar_encoder.weight']
print(f'scalar_encoder.weight shape: {w.shape}')
assert w.shape[1] == 60, f'Expected 60, got {w.shape[1]}'
# Verify new columns (indices 11:32) are zero from migration
print(f'New columns L2 norm: {w[:, 11:32].norm().item():.6f}')
assert w[:, 11:32].norm().item() < 1e-6, 'New columns should be zero after migration'
print('OK: shape is [H, 60], new columns are zero')
"
```

### 1b. Patch new columns with small random init

The migration script zero-inits the 21 new columns. For PPO, zero-init creates a
flat loss landscape for new features (gradients are zero when inputs are non-zero but
weights are zero). We need small random init `U(-0.05, 0.05)` instead.

**File**: Create a one-off script `scripts/patch_v4_init.py` OR do it inline.

**Command** (inline, no script needed):
```bash
uv run python -c "
import torch

ckpt_path = 'data/checkpoints/ppo_v4_start/ppo_v3_60dim.pt'
ckpt = torch.load(ckpt_path, map_location='cpu', weights_only=False)
sd = ckpt['model_state_dict']
w = sd['scalar_encoder.weight']  # shape [64, 60]

# Patch columns 11:32 (the 21 new active-effect features)
H = w.shape[0]
w[:, 11:32] = torch.empty(H, 21).uniform_(-0.05, 0.05)
sd['scalar_encoder.weight'] = w
ckpt['model_state_dict'] = sd

out_path = 'data/checkpoints/ppo_v4_start/ppo_v4_init.pt'
torch.save(ckpt, out_path)

print(f'Patched {out_path}')
print(f'  scalar_encoder.weight shape: {w.shape}')
print(f'  New columns L2 norm: {w[:, 11:32].norm().item():.4f}')
print(f'  Old columns 0:11 unchanged: {w[:, :11].norm().item():.4f}')
print(f'  Region columns 32:60 unchanged: {w[:, 32:60].norm().item():.4f}')
"
```

**Verify**:
- `scalar_encoder.weight` shape is `[64, 60]`
- Columns 11:32 have non-zero L2 norm (should be ~0.2-0.5 from uniform init)
- Columns 0:11 and 32:60 match the original migrated checkpoint exactly

**Sanity check** (forward pass equivalence on zero-new-features input):
```bash
uv run python -c "
import torch
from pathlib import Path
import sys
sys.path.insert(0, str(Path('python')))
from tsrl.policies.model import TSControlFeatGNNModel

# Load patched checkpoint
ckpt = torch.load('data/checkpoints/ppo_v4_start/ppo_v4_init.pt', map_location='cpu', weights_only=False)
model = TSControlFeatGNNModel(hidden_dim=256)
model.load_state_dict(ckpt['model_state_dict'])
model.eval()

# Forward pass with new features = 0 should work without error
B = 2
inf = torch.randn(B, 172)
cards = torch.randn(B, 448)
scalars = torch.zeros(B, 32)  # all zeros including new features
with torch.no_grad():
    out = model(inf, cards, scalars)
print(f'Forward pass OK: card_logits shape={out[\"card_logits\"].shape}')
print(f'value shape={out[\"value\"].shape}')
"
```

---

## Step 2: Copy league v3 pool to league v4

The PPO v4 league pool starts from v3's past checkpoints for opponent diversity.
These are TorchScript files with 11-dim scalars (39-dim scalar_encoder). They remain
usable because C++ `play_callback_matchup` / `benchmark_batched` uses the scripted
model's own forward method, which expects its own input shape. The C++ rollout builds
features using the current `kScalarDim=32`, so there is a shape mismatch.

**IMPORTANT**: The league TorchScript models were exported with 11-dim (39-dim with
region) scalar_encoder. The C++ rollout now produces 32-dim (60-dim with region)
scalars. We must re-export league checkpoints with the new scalar dim.

### 2a. Migrate all league v3 checkpoints to 60-dim

**Command**:
```bash
# First, migrate all .pt (non-scripted) league checkpoints
for f in data/checkpoints/league_v3/iter_*.pt; do
    uv run python scripts/migrate_scalar_dim.py --input "$f" --output "$f" --dry-run
done
```

If the league pool only contains TorchScript archives (`.pt` files that are
TorchScript, not state_dict), we cannot migrate them directly. In that case, we need
to re-export from the corresponding PPO v3 milestone checkpoints.

**Check what league files contain**:
```bash
uv run python -c "
import torch
ckpt = torch.load('data/checkpoints/league_v3/iter_0001.pt', map_location='cpu', weights_only=False)
print(type(ckpt))
if isinstance(ckpt, dict):
    print('Keys:', list(ckpt.keys())[:10])
else:
    print('TorchScript archive — cannot migrate state_dict')
"
```

**If TorchScript** (most likely, since `_export_torchscript_model` is used in league save):

We must re-export from the PPO v3 milestone .pt files. Each milestone was saved to
`data/checkpoints/ppo_v3_league/ppo_iter{NNNN}.pt` AND to
`data/checkpoints/league_v3/iter_{NNNN}.pt` (as TorchScript).

**Steps**:
```bash
mkdir -p data/checkpoints/league_v4

# For each milestone checkpoint in ppo_v3_league, migrate and re-export
uv run python -c "
import torch, sys
from pathlib import Path
sys.path.insert(0, str(Path('python')))
from tsrl.policies.model import TSControlFeatGNNModel

# Import the migration function
sys.path.insert(0, str(Path('scripts')))
from migrate_scalar_dim import _migrate_state_dict

milestones = [1, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
for it in milestones:
    if it == 1:
        src = Path('data/checkpoints/league_v3/iter_0001.pt')
    else:
        src = Path(f'data/checkpoints/ppo_v3_league/ppo_iter{it:04d}.pt')
    if not src.exists():
        print(f'  SKIP {src} (not found)')
        continue
    
    raw = torch.load(src, map_location='cpu', weights_only=False)
    if not isinstance(raw, dict):
        print(f'  SKIP {src} (TorchScript archive)')
        continue
    
    sd = raw.get('model_state_dict', raw)
    new_sd, desc = _migrate_state_dict(sd)
    print(f'  {src.name}: {desc}')
    
    # Load into model and re-export as TorchScript
    model = TSControlFeatGNNModel(hidden_dim=256)
    model.load_state_dict(new_sd, strict=False)
    model.eval()
    
    # Export TorchScript
    out_path = Path(f'data/checkpoints/league_v4/iter_{it:04d}.pt')
    dummy_inf = torch.randn(1, 172)
    dummy_cards = torch.randn(1, 448)
    dummy_scalars = torch.randn(1, 32)
    scripted = torch.jit.script(model)
    torch.jit.save(scripted, str(out_path))
    print(f'  -> {out_path}')

print('Done.')
"
```

**Verify**:
```bash
ls -la data/checkpoints/league_v4/
# Should have 11 .pt files (iter_0001 through iter_0200)
```

**Note on iter_0001**: This was saved at PPO v3 iteration 1. It might only exist as
TorchScript in `league_v3/`. If so, skip it — having 10 league opponents is fine.

---

## Step 3: Add LR warmup support to train_ppo.py

### 3a. Add CLI arguments

**File**: `scripts/train_ppo.py`
**Function**: `parse_args()` (around line 1485)

Add two new arguments after the `--lr` argument (line 1451):

```python
    p.add_argument("--lr-warmup-iters", type=int, default=0,
                   help="Number of iterations to use warmup LR (0 = no warmup)")
    p.add_argument("--lr-warmup-factor", type=float, default=0.33,
                   help="Warmup LR = base_lr * warmup_factor (default: 0.33)")
```

### 3b. Implement LR warmup in the training loop

**File**: `scripts/train_ppo.py`
**Location**: Inside the `for iteration in range(...)` loop, just before the PPO update phase
(around line 1660, before `t_update_start = time.time()`)

Add LR adjustment:

```python
        # ── LR warmup ────────────────────────────────────────────────────────
        if args.lr_warmup_iters > 0 and iteration <= args.lr_warmup_iters:
            current_lr = args.lr * args.lr_warmup_factor
        else:
            current_lr = args.lr
        for pg in optimizer.param_groups:
            pg["lr"] = current_lr
```

### 3c. Log current LR to W&B

**File**: `scripts/train_ppo.py`
**Location**: In the W&B logging sections (around lines 1734 and 1752)

Add to both the milestone and non-milestone W&B log dicts:
```python
                log_dict["learning_rate"] = current_lr
```

### 3d. Print LR in the iteration output line

**File**: `scripts/train_ppo.py`
**Location**: In the print statement at line 1678

Add `lr={current_lr:.1e}` to the format string.

**Verify**: Run a dry test with `--n-iterations 3 --lr-warmup-iters 2 --lr-warmup-factor 0.33`:
- Iterations 1-2 should show lr=1.0e-05 (3e-5 * 0.33)
- Iteration 3 should show lr=3.0e-05

---

## Step 4: Add rollout logits to Parquet output

PPO v4 must save full policy logits for future KL-distillation arch sweep (Phase 5).
Currently `_save_rollout_parquet` saves encoded features + actions + values but not logits.

### 4a. Add logit fields to Step dataclass

**File**: `scripts/train_ppo.py`
**Location**: `Step` dataclass (line 153)

Add these fields after `hand_card_ids`:

```python
    # Policy logits for KL-distillation (Phase 5 arch sweep)
    card_logits_raw: Optional[torch.Tensor] = None    # (111,) raw logits before masking
    mode_logits_raw: Optional[torch.Tensor] = None    # (5,) raw logits before masking
    country_logits_raw: Optional[torch.Tensor] = None  # (86,) raw logits/probs before masking
    gae_return: Optional[float] = None                 # GAE return (advantage + value baseline)
```

### 4b. Populate logits during rollout collection

**File**: `scripts/train_ppo.py`
**Function**: `_sample_action()` (around line 290)

This function already computes `card_logits`, `mode_logits`, `country_logits` (lines 304-308).
It returns a `Step` object. Add the raw logits to the returned Step:

Find the section where the Step is created (around line 390-420) and add:

```python
    card_logits_raw=card_logits.detach().cpu(),
    mode_logits_raw=mode_logits.detach().cpu(),
    country_logits_raw=country_logits.detach().cpu() if country_logits is not None else None,
```

**IMPORTANT**: These must be detached and moved to CPU to avoid GPU memory accumulation
across the entire rollout.

### 4c. Populate GAE return after GAE computation

**File**: `scripts/train_ppo.py`
**Location**: After `compute_gae_batch(all_steps, ...)` call (line 1631)

Add:
```python
        # Store GAE return = advantage + value for future KL-distillation dataset
        for s in all_steps:
            s.gae_return = s.advantage + s.value
```

### 4d. Save logits in Parquet

**File**: `scripts/train_ppo.py`
**Function**: `_save_rollout_parquet()` (line 1267)

Add these columns to `table_dict` (around line 1323, before the `if has_raw:` block):

```python
    # Policy logits for KL-distillation (present when steps have logit fields)
    has_logits = steps[0].card_logits_raw is not None if steps else False
    if has_logits:
        table_dict["card_logits"] = pa.array(
            [s.card_logits_raw.numpy().tolist() for s in steps],
            type=pa.list_(pa.float32()))
        table_dict["mode_logits"] = pa.array(
            [s.mode_logits_raw.numpy().tolist() for s in steps],
            type=pa.list_(pa.float32()))
        table_dict["country_logits"] = pa.array(
            [s.country_logits_raw.numpy().tolist() if s.country_logits_raw is not None
             else [0.0] * 86 for s in steps],
            type=pa.list_(pa.float32()))
    # GAE return (always present after GAE computation)
    gae_returns = [s.gae_return if s.gae_return is not None else 0.0 for s in steps]
    table_dict["gae_return"] = pa.array(gae_returns, type=pa.float32())
```

### 4e. Update docstring

**File**: `scripts/train_ppo.py`
**Function**: `_save_rollout_parquet()` docstring

Update to mention the new columns:
```
    New columns (PPO v4+):
    - card_logits: (111,) raw card logits before masking
    - mode_logits: (5,) raw mode logits before masking
    - country_logits: (86,) raw country logits/probs before masking
    - gae_return: GAE advantage + value baseline (float)
```

**Verify**: After implementing, run a quick 1-iteration test:
```bash
mkdir -p /tmp/ppo_v4_test_rollout
uv run python scripts/train_ppo.py \
    --checkpoint data/checkpoints/ppo_v4_start/ppo_v4_init.pt \
    --out-dir /tmp/ppo_v4_test \
    --n-iterations 1 --games-per-iter 10 \
    --self-play --self-play-heuristic-mix 0.5 \
    --save-rollout-parquet /tmp/ppo_v4_test_rollout \
    --seed 99999 --device cuda

# Check parquet schema
uv run python -c "
import pyarrow.parquet as pq
t = pq.read_table('/tmp/ppo_v4_test_rollout/rollout_iter_0001.parquet')
print('Columns:', t.column_names)
print('Rows:', len(t))
assert 'card_logits' in t.column_names, 'Missing card_logits column'
assert 'mode_logits' in t.column_names, 'Missing mode_logits column'
assert 'country_logits' in t.column_names, 'Missing country_logits column'
assert 'gae_return' in t.column_names, 'Missing gae_return column'
# Check shapes
row0 = t.to_pydict()
print(f'card_logits length: {len(row0[\"card_logits\"][0])}')
print(f'mode_logits length: {len(row0[\"mode_logits\"][0])}')
print(f'country_logits length: {len(row0[\"country_logits\"][0])}')
assert len(row0['card_logits'][0]) == 111
assert len(row0['mode_logits'][0]) == 5
assert len(row0['country_logits'][0]) == 86
print('All shape checks passed')
"
```

---

## Step 5: Add new-scalar weight norm monitoring

### 5a. Add weight norm computation to PPO update metrics

**File**: `scripts/train_ppo.py`
**Location**: After the `ppo_update()` call returns `metrics` (around line 1668)

Add:
```python
        # Monitor new-feature weight norm (L2 of the 21-column block in scalar_encoder)
        with torch.no_grad():
            se_weight = model.scalar_encoder.weight  # shape [H, 60]
            new_scalar_norm = se_weight[:, 11:32].norm().item()
            old_scalar_norm = se_weight[:, :11].norm().item()
            region_norm = se_weight[:, 32:60].norm().item()
        metrics["new_scalar_weight_norm"] = new_scalar_norm
        metrics["old_scalar_weight_norm"] = old_scalar_norm
        metrics["region_weight_norm"] = region_norm
```

### 5b. Print weight norm in iteration output

Add to the print statement (around line 1678):
```
f"new_w={new_scalar_norm:.3f} "
```

### 5c. Log to W&B

The weight norm metrics are already in the `metrics` dict, so they will be logged
automatically in both the milestone and non-milestone W&B logging paths.

**Verify**: After a 1-iter test, the output should show `new_w=0.XXX` with a non-zero
value (from the random init in Step 1b).

---

## Step 6: Run PPO v4

### 6a. Full launch command

```bash
uv run python scripts/train_ppo.py \
    --checkpoint data/checkpoints/ppo_v4_start/ppo_v4_init.pt \
    --out-dir data/checkpoints/ppo_v4_league \
    --n-iterations 300 \
    --games-per-iter 200 \
    --ppo-epochs 1 \
    --clip-eps 0.2 \
    --lr 3e-5 \
    --lr-warmup-iters 15 \
    --lr-warmup-factor 0.33 \
    --max-kl 0.25 \
    --gamma 0.99 \
    --gae-lambda 0.95 \
    --ent-coef 0.01 \
    --ent-coef-final 0.001 \
    --vf-coef 0.5 \
    --vp-reward-coef 0.1 \
    --self-play \
    --self-play-heuristic-mix 0.2 \
    --league data/checkpoints/league_v4 \
    --league-save-every 20 \
    --save-rollout-parquet data/ppo_v4_rollouts \
    --benchmark-every 10 \
    --seed 400000 \
    --device cuda \
    --wandb \
    --wandb-run-name ppo_v4_60dim
```

### 6b. Hyperparameter summary

| Parameter | Value | Notes |
|-----------|-------|-------|
| checkpoint | ppo_v4_init.pt | v3 best migrated to 60-dim + random init new cols |
| n_iterations | 300 | Extended; plateau detection is manual |
| games_per_iter | 200 | Same as v3 |
| ppo_epochs | 1 | Same as v3 (1 epoch to keep KL low) |
| clip_eps | 0.2 | Standard |
| lr | 3e-5 | Same as v3 |
| lr_warmup_iters | 15 | NEW: first 15 iters use 1e-5 |
| lr_warmup_factor | 0.33 | NEW: warmup LR = 3e-5 * 0.33 = 1e-5 |
| max_kl | 0.25 | Same as v3 |
| gamma | 0.99 | Standard |
| gae_lambda | 0.95 | Standard |
| ent_coef | 0.01 -> 0.001 | Same as v3 (linear decay) |
| vf_coef | 0.5 | Standard |
| vp_reward_coef | 0.1 | Same as v3 |
| self_play | True | Same as v3 |
| heuristic_mix | 0.2 | Same as v3 |
| league | league_v4 | NEW pool seeded from v3 |
| league_save_every | 20 | Same as v3 |
| save_rollout_parquet | data/ppo_v4_rollouts | NEW: full logits + values |
| benchmark_every | 10 | Finer than v3 (was 20) for plateau detection |
| seed | 400000 | Fresh seed range |

### 6c. Expected behavior in first 15 iters (warmup)

- LR = 1e-5 (0.33x of 3e-5)
- `new_scalar_weight_norm` should grow slowly from ~0.3 (random init) as new features
  start contributing
- KL should stay very low (<0.05) during warmup
- Heuristic WR at iter 10 benchmark may dip slightly from v3 (model is adapting to
  new features) — this is OK
- Rollout WR should be similar to v3 (~0.85-0.90)

### 6d. Expected behavior after warmup (iters 16+)

- LR jumps to 3e-5
- `new_scalar_weight_norm` should grow faster
- KL may spike briefly at iter 16 (LR jump) but should stay below 0.25
- Heuristic WR should recover and start improving past v3's 89.7%

---

## Step 7: Monitoring and plateau detection

### 7a. Benchmark cadence

| Interval | Metric | Action |
|----------|--------|--------|
| Every 10 iters | vs-heuristic 500 games/side (auto) | Logged to stdout + W&B |
| Every 40 iters | H2H vs v3_best (manual) | Run `elo_tracker.py` |
| Every 40 iters | H2H vs v2b_iter140 (manual) | Run `elo_tracker.py` |

### 7b. H2H benchmark command (run manually every 40 iters)

```bash
# After PPO v4 iter N produces ppo_iterNNNN_scripted.pt:
uv run python scripts/elo_tracker.py \
    --model-a data/checkpoints/ppo_v4_league/ppo_iter{NNNN}_scripted.pt \
    --model-b data/checkpoints/ppo_v3_league/ppo_best_scripted.pt \
    --n-games 200 --seed 77800

uv run python scripts/elo_tracker.py \
    --model-a data/checkpoints/ppo_v4_league/ppo_iter{NNNN}_scripted.pt \
    --model-b data/checkpoints/ppo_v2b/ppo_iter0140_scripted.pt \
    --n-games 200 --seed 78000
```

### 7c. Plateau definition

**Stop PPO v4 when ANY of these conditions hold**:

1. **WR plateau**: Combined heuristic WR improves <0.5pp over any 30-iter window.
   Measured at 10-iter benchmark intervals, so compare WR at iter N vs iter N-30.
   Must hold for 3 consecutive benchmark points (iters N, N+10, N+20 all <0.5pp
   above iter N-30, N-20, N-10 respectively).

2. **Training instability**: Rollout KL > 0.5 for 5 consecutive iterations.

3. **Entropy collapse**: Entropy < 1.0 for 10 consecutive iterations.

4. **Iteration budget**: 300 iterations reached.

### 7d. Metrics to track in W&B

These should all appear automatically if Steps 3-5 are implemented correctly:

| Metric | Source | Expected range |
|--------|--------|---------------|
| `new_scalar_weight_norm` | Step 5 | 0.3 -> growing |
| `old_scalar_weight_norm` | Step 5 | ~stable |
| `region_weight_norm` | Step 5 | ~stable |
| `learning_rate` | Step 3 | 1e-5 for iters 1-15, then 3e-5 |
| `heuristic_wr_combined` | benchmark | 89% -> improving |
| `heuristic_wr_ussr` | benchmark | 90%+ |
| `heuristic_wr_us` | benchmark | 75%+ |
| `rollout_wr` | per-iter | ~0.85-0.90 |
| `sp_rollout_wr_ussr` | per-iter | ~0.50 (self-play) |
| `sp_rollout_wr_us` | per-iter | ~0.50 (self-play) |
| `entropy` | per-iter | 2.0-2.5 (healthy) |
| `approx_kl` | per-iter | <0.25 |
| `value_loss` | per-iter | <0.1 |
| `policy_loss` | per-iter | negative (expected) |
| `ent_coef` | per-iter | 0.01 -> 0.001 |

---

## Step 8: Rollout data accumulation for Phase 5

### 8a. Expected data volume

| PPO v4 iters | Est. steps/iter | Cumulative rows | Parquet size (est.) |
|-------------|-----------------|-----------------|-------------------|
| 50 | ~30k | ~1.5M | ~3 GB |
| 100 | ~30k | ~3.0M | ~6 GB |
| 150 | ~30k | ~4.5M | ~9 GB |
| 200 | ~30k | ~6.0M | ~12 GB |
| 300 | ~30k | ~9.0M | ~18 GB |

**Disk budget**: Rollout parquets include logit vectors (111+5+86 = 202 float32 per
row = ~808 bytes for logits alone). At ~30k rows/iter, that is ~24 MB/iter for logits.
Total per-iter parquet size: ~60-80 MB (features + actions + logits + raw state).

At 300 iters: ~18-24 GB total. This is manageable on a development machine.

### 8b. Parquet schema (full, after Step 4)

Each row in `data/ppo_v4_rollouts/rollout_iter_{NNNN}.parquet`:

| Column | Type | Shape | Description |
|--------|------|-------|-------------|
| influence | list<float32> | (172,) | Per-country influence [ussr(86), us(86)] |
| cards | list<float32> | (448,) | Card feature vector (4 masks x 112) |
| scalars | list<float32> | (32,) | Scalar game features (32-dim) |
| card_id | int32 | scalar | 1-indexed card ID (action taken) |
| mode_id | int32 | scalar | 0=influence, 1=coup, 2=realign, 3=space, 4=event |
| country_targets | list<int32> | variable | 0-indexed country IDs with repeats |
| side_int | int8 | scalar | 0=USSR, 1=US |
| reward | float32 | scalar | Terminal reward (±1.0 with VP scaling) |
| value | float32 | scalar | V(s) estimate at this step |
| iteration | int32 | scalar | PPO iteration number |
| card_logits | list<float32> | (111,) | Raw card logits before masking |
| mode_logits | list<float32> | (5,) | Raw mode logits before masking |
| country_logits | list<float32> | (86,) | Raw country logits/probs |
| gae_return | float32 | scalar | GAE advantage + value |
| raw_ussr_influence | list<int16> | (86,) | Raw USSR influence values |
| raw_us_influence | list<int16> | (86,) | Raw US influence values |
| raw_turn | int8 | scalar | Turn number (1-10) |
| raw_ar | int8 | scalar | Action round |
| raw_defcon | int8 | scalar | DEFCON level (1-5) |
| raw_vp | int16 | scalar | VP (positive = USSR ahead) |
| raw_milops | list<int8> | (2,) | Military ops [USSR, US] |
| raw_space | list<int8> | (2,) | Space race level [USSR, US] |
| hand_card_ids | list<int16> | variable | 1-indexed card IDs in hand |

---

## Phase 5: Architecture sweep using PPO v4 rollout data (after plateau)

This section is a forward reference. Do NOT implement until PPO v4 has plateaued and
rollout data has been collected.

### 5.1 Dataset construction

**Source**: `data/ppo_v4_rollouts/rollout_iter_*.parquet`

**Tiers**:
- Tier 0.5M: first ~17 parquet files (~0.5M rows)
- Tier 1M: first ~34 parquet files (~1M rows)

**Train/val split**: By iteration (not by row). Last 10% of iterations = val set.

### 5.2 Loss function

```python
# KL-distillation loss
L = (
    CE(card_pred, card_label)          # card cross-entropy
    + CE(mode_pred, mode_label)        # mode cross-entropy
    + CE(country_pred, country_label)  # country cross-entropy (if applicable)
    + 0.5 * KL(pi_v4_logits || pi_student_logits)  # KL from v4 policy
    + 0.5 * MSE(value_pred, gae_return)             # value regression
)
```

Where:
- `card_label` = `card_id - 1` (0-indexed)
- `mode_label` = `mode_id`
- `country_label` = first element of `country_targets` (simplified)
- `pi_v4_logits` = `card_logits` from parquet (detached, used as target)
- `gae_return` from parquet (used as value target)

### 5.3 Architecture candidates

1. **GNN** (`TSControlFeatGNNModel`): current production. Control variable.
2. **Attention** (`TSCountryAttnModel`): must be updated to use 32-dim scalars + 28-dim
   region scalars (matching GNN's input contract).

### 5.4 Experimental protocol

- 2 architectures x 2 dataset tiers x 3 seeds = 12 runs
- Hyperparams: same as Phase 1 BC (bs=8192, lr=0.0024, epochs=60, patience=15, h=256)
- Selection: proxy eval card_top1 + value_brier, prefer lower variance across seeds

---

## Sanity checks (run after each major step)

### After Step 1 (migration + patch)
```bash
uv run python -c "
import torch
ckpt = torch.load('data/checkpoints/ppo_v4_start/ppo_v4_init.pt', map_location='cpu', weights_only=False)
w = ckpt['model_state_dict']['scalar_encoder.weight']
assert w.shape == (64, 60), f'Wrong shape: {w.shape}'
assert w[:, 11:32].norm().item() > 0.1, 'New columns should be non-zero after random init'
assert w[:, :11].norm().item() > 1.0, 'Old columns should be non-zero'
assert w[:, 32:60].norm().item() > 1.0, 'Region columns should be non-zero'
print('Step 1 OK')
"
```

### After Step 2 (league v4 pool)
```bash
uv run python -c "
from pathlib import Path
league_dir = Path('data/checkpoints/league_v4')
pts = sorted(league_dir.glob('iter_*.pt'))
print(f'League v4 pool: {len(pts)} checkpoints')
assert len(pts) >= 10, f'Expected >= 10, got {len(pts)}'
# Verify one loads as TorchScript
import torch
m = torch.jit.load(str(pts[0]), map_location='cpu')
dummy = (torch.randn(1, 172), torch.randn(1, 448), torch.randn(1, 32))
out = m(*dummy)
print(f'  Forward pass on {pts[0].name}: OK, output keys = {list(out.keys()) if isinstance(out, dict) else \"tensor\"}')
print('Step 2 OK')
"
```

### After Steps 3-5 (code changes)
```bash
# Quick smoke test: 2 iterations with warmup, rollout saving, and weight monitoring
mkdir -p /tmp/ppo_v4_smoke
uv run python scripts/train_ppo.py \
    --checkpoint data/checkpoints/ppo_v4_start/ppo_v4_init.pt \
    --out-dir /tmp/ppo_v4_smoke \
    --n-iterations 2 --games-per-iter 10 \
    --ppo-epochs 1 --lr 3e-5 \
    --lr-warmup-iters 1 --lr-warmup-factor 0.33 \
    --self-play --self-play-heuristic-mix 0.5 \
    --save-rollout-parquet /tmp/ppo_v4_smoke/rollouts \
    --benchmark-every 2 \
    --max-kl 0.5 \
    --seed 99999 --device cuda

# Verify output
uv run python -c "
import pyarrow.parquet as pq
t = pq.read_table('/tmp/ppo_v4_smoke/rollouts/rollout_iter_0001.parquet')
cols = t.column_names
print(f'Columns ({len(cols)}): {cols}')
required = ['influence', 'cards', 'scalars', 'card_id', 'mode_id',
            'card_logits', 'mode_logits', 'country_logits', 'gae_return']
for c in required:
    assert c in cols, f'Missing required column: {c}'
print(f'Rows: {len(t)}')
print('Steps 3-5 smoke test OK')
"
```

### After Step 6 (PPO v4 running, check after iter 10)
```bash
# Check that training is progressing
uv run python -c "
import json
from pathlib import Path

# Read last few lines of stdout or check W&B
rollout_dir = Path('data/ppo_v4_rollouts')
parquets = sorted(rollout_dir.glob('rollout_iter_*.parquet'))
print(f'Rollout files: {len(parquets)}')

# Check latest parquet
if parquets:
    import pyarrow.parquet as pq
    t = pq.read_table(str(parquets[-1]))
    print(f'Latest: {parquets[-1].name}, {len(t)} rows')
    assert 'card_logits' in t.column_names
    print('Rollout data accumulating correctly')
"
```

---

## Failure modes and mitigations

### F1: KL spike at warmup->full LR transition (iter 16)

**Symptom**: KL > 0.25 at iteration 16, training stops.
**Mitigation**: Re-launch with `--start-iteration 16 --lr-warmup-iters 25` to extend
warmup, or use `--lr-warmup-factor 0.5` (less aggressive jump).

### F2: New features cause regression

**Symptom**: Heuristic WR at iter 10 drops >5pp below v3's 89.7%.
**Mitigation**: Reduce random init range from U(-0.05, 0.05) to U(-0.01, 0.01), re-run
Step 1b and restart.

### F3: League pool shape mismatch

**Symptom**: Error like `Expected input dim 39, got 60` when playing vs league opponent.
**Mitigation**: Re-check Step 2. All league pool TorchScript files must use 60-dim
scalar_encoder. If some old files leak in, delete and re-export.

### F4: Parquet files too large

**Symptom**: Disk fills up (>50 GB).
**Mitigation**: Reduce rollout save frequency. Change `_save_rollout_parquet` to only
save every 5th iteration: `if iteration % 5 == 0:`.

### F5: Value loss spikes after feature change

**Symptom**: Value loss > 0.5 in first 10 iters.
**Mitigation**: This is expected — the value head must recalibrate with new features.
Should resolve by iter 20-30. If it persists past iter 50, the random init is too large.

---

## Timeline estimate

| Step | Effort | Blocking |
|------|--------|----------|
| Step 1: Migration + patch | 10 min | None |
| Step 2: League v4 pool | 15 min | Step 1 |
| Step 3: LR warmup | 20 min | None |
| Step 4: Rollout logits | 30 min | None |
| Step 5: Weight norm monitoring | 10 min | None |
| Steps 3-5 smoke test | 10 min | Steps 3-5 |
| Step 6: Launch PPO v4 | 5 min | Steps 1-5 |
| Step 7: Monitor (ongoing) | - | Step 6 |

**Steps 3, 4, 5 can be implemented in parallel** (they touch different sections of
`train_ppo.py`). Steps 1 and 2 are sequential prerequisites.

**Total implementation time**: ~1.5 hours (excluding PPO v4 runtime).
**PPO v4 runtime**: ~3 hours for 300 iters at ~35s/iter.

---

## Files modified by this plan

| File | Steps | Changes |
|------|-------|---------|
| `scripts/train_ppo.py` | 3, 4, 5 | LR warmup args + loop logic; logit fields in Step dataclass; logit population in _sample_action; logit+gae columns in _save_rollout_parquet; weight norm monitoring |
| `scripts/migrate_scalar_dim.py` | 1a | No changes (used as-is) |
| `data/checkpoints/ppo_v4_start/` | 1a, 1b | New directory: ppo_v3_60dim.pt, ppo_v4_init.pt |
| `data/checkpoints/league_v4/` | 2 | New directory: 10-11 re-exported TorchScript files |
| `data/checkpoints/ppo_v4_league/` | 6 | New directory: PPO v4 checkpoints (created by training) |
| `data/ppo_v4_rollouts/` | 6 | New directory: rollout parquets (created by training) |

---

## Exact CLI commands (copy-paste ready)

### Full sequence
```bash
cd /home/dkord/code/twilight-struggle-ai

# Step 1a: Migrate
mkdir -p data/checkpoints/ppo_v4_start
uv run python scripts/migrate_scalar_dim.py \
    --input data/checkpoints/ppo_v3_league/ppo_best.pt \
    --output data/checkpoints/ppo_v4_start/ppo_v3_60dim.pt

# Step 1b: Patch new columns
uv run python -c "
import torch
ckpt = torch.load('data/checkpoints/ppo_v4_start/ppo_v3_60dim.pt', map_location='cpu', weights_only=False)
w = ckpt['model_state_dict']['scalar_encoder.weight']
w[:, 11:32] = torch.empty(w.shape[0], 21).uniform_(-0.05, 0.05)
ckpt['model_state_dict']['scalar_encoder.weight'] = w
torch.save(ckpt, 'data/checkpoints/ppo_v4_start/ppo_v4_init.pt')
print(f'Patched: shape={w.shape}, new_norm={w[:, 11:32].norm():.4f}')
"

# Step 2: Copy league pool (run the script from Step 2a above)

# Steps 3-5: Code changes (implement in train_ppo.py per instructions above)

# Step 6: Launch PPO v4
uv run python scripts/train_ppo.py \
    --checkpoint data/checkpoints/ppo_v4_start/ppo_v4_init.pt \
    --out-dir data/checkpoints/ppo_v4_league \
    --n-iterations 300 \
    --games-per-iter 200 \
    --ppo-epochs 1 \
    --clip-eps 0.2 \
    --lr 3e-5 \
    --lr-warmup-iters 15 \
    --lr-warmup-factor 0.33 \
    --max-kl 0.25 \
    --gamma 0.99 \
    --gae-lambda 0.95 \
    --ent-coef 0.01 \
    --ent-coef-final 0.001 \
    --vf-coef 0.5 \
    --vp-reward-coef 0.1 \
    --self-play \
    --self-play-heuristic-mix 0.2 \
    --league data/checkpoints/league_v4 \
    --league-save-every 20 \
    --save-rollout-parquet data/ppo_v4_rollouts \
    --benchmark-every 10 \
    --seed 400000 \
    --device cuda \
    --wandb \
    --wandb-run-name ppo_v4_60dim
```
