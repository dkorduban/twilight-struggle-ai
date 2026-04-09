# Spec: JSD Probe Evaluation for PPO Training

## Goal
Compute Jensen-Shannon Divergence (JSD) between two model checkpoints at a frozen set of
1000 board positions, stratified by turn/side/DEFCON/VP. Reports per-head (card, mode,
country) and per-phase (early/mid/late) JSD plus value MAE. Integrates into `train_ppo.py`
to log to W&B every K iterations. Also provides a one-shot script to build the frozen probe
set from existing parquet rollout data.

## Files to create

- `python/tsrl/policies/jsd_probe.py` — `ProbeEvaluator` class: loads probe parquet,
  runs both models in eval mode, computes masked JSD per head, returns metric dict
- `scripts/build_probe_set.py` — one-shot: reads existing parquet data, stratified-samples
  1000 positions, writes `data/probe_positions.parquet`
- `tests/python/test_jsd_probe.py` — unit tests

## Files to modify

- `scripts/train_ppo.py` — instantiate `ProbeEvaluator` after model load; call every
  `args.probe_every` iterations (default 10); merge metrics into `log_dict`
- `python/tsrl/policies/__init__.py` — export `ProbeEvaluator`

## Interfaces / signatures

### `python/tsrl/policies/jsd_probe.py`

```python
import torch
import polars as pl
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
import torch.nn as nn

CARD_SLOTS = 111   # valid card indices 0..110
MODE_SLOTS = 5
COUNTRY_SLOTS = 86

@dataclass
class ProbeMetrics:
    card_jsd: float          # JSD on masked card logits, mean over positions
    mode_jsd: float          # JSD on masked mode logits, mean over positions
    country_jsd: float       # JSD on country logits (positions with country head)
    value_mae: float         # mean |v_a - v_b| over positions
    top1_card_agree: float   # fraction where argmax card matches
    top1_mode_agree: float   # fraction where argmax mode matches
    # per-phase (early=t1-3, mid=t4-7, late=t8-10)
    card_jsd_early: float
    card_jsd_mid: float
    card_jsd_late: float
    n_positions: int


class ProbeEvaluator:
    """Evaluate JSD between two models at a frozen probe position set."""

    def __init__(
        self,
        probe_path: str | Path,
        device: str = "cpu",
        batch_size: int = 256,
    ):
        """Load probe positions from parquet. Called once after model init."""
        ...

    def compare(
        self,
        model_a: nn.Module,
        model_b: nn.Module,
    ) -> ProbeMetrics:
        """Run both models on all probe positions; return divergence metrics."""
        ...

    @staticmethod
    def _jsd(p: torch.Tensor, q: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        """Compute JSD(P||Q) ∈ [0, log2] per row, with illegal actions zeroed.
        
        Args:
            p, q: (B, N) raw logits (pre-softmax)
            mask: (B, N) bool — True = legal action
        Returns:
            (B,) JSD values in [0, 1] (normalized by log 2)
        """
        ...
```

### `scripts/build_probe_set.py`

```
Usage: uv run python scripts/build_probe_set.py \
    --data-dir data/ppo_rollout_combined \
    --out data/probe_positions.parquet \
    --n 1000 \
    --seed 42

Reads all parquet files in --data-dir, stratified-samples --n rows by
(turn_bucket × side × defcon_bucket × vp_bucket), writes minimal columns needed
for ProbeEvaluator to --out.

Required output columns:
  influence  list[float]   (172,)
  cards      list[float]   (448,)
  scalars    list[float]   (32,)
  card_mask  list[bool]    (111,)  -- precomputed from hand_card_ids
  mode_mask  list[bool]    (5,)    -- all True (simplified, DEFCON safety skipped)
  raw_turn   int
  side_int   int           0=USSR 1=US
  raw_defcon int
  raw_vp     int
```

### Integration in `scripts/train_ppo.py`

New CLI args (add to `parse_args()`):
```python
p.add_argument("--probe-set", type=str, default=None,
               help="Path to probe_positions.parquet for JSD evaluation")
p.add_argument("--probe-every", type=int, default=10,
               help="Compute JSD probe every N iterations (0=disabled)")
p.add_argument("--probe-bc-checkpoint", type=str, default=None,
               help="BC baseline checkpoint for JSD comparison")
```

After model load in `main()`, before the training loop:
```python
probe_eval: Optional[ProbeEvaluator] = None
if args.probe_set and args.probe_every > 0 and Path(args.probe_set).exists():
    from tsrl.policies.jsd_probe import ProbeEvaluator
    probe_eval = ProbeEvaluator(args.probe_set, device=device)
    # Optionally load BC model for comparison
    probe_bc_model: Optional[nn.Module] = None
    if args.probe_bc_checkpoint:
        probe_bc_model = load_model(args.probe_bc_checkpoint, device=device)
        probe_bc_model.eval()
```

Inside the iteration loop, after PPO update, before W&B logging:
```python
if probe_eval is not None and iteration % args.probe_every == 0:
    with torch.no_grad():
        # vs previous checkpoint (policy drift)
        if last_rolling_ckpt and Path(last_rolling_ckpt).exists():
            prev_model = load_model(last_rolling_ckpt, device=device)
            prev_model.eval()
            m = probe_eval.compare(model, prev_model)
            log_dict.update({
                "probe/card_jsd_vs_prev": m.card_jsd,
                "probe/mode_jsd_vs_prev": m.mode_jsd,
                "probe/country_jsd_vs_prev": m.country_jsd,
                "probe/value_mae_vs_prev": m.value_mae,
                "probe/top1_card_agree_vs_prev": m.top1_card_agree,
                "probe/card_jsd_early_vs_prev": m.card_jsd_early,
                "probe/card_jsd_mid_vs_prev": m.card_jsd_mid,
                "probe/card_jsd_late_vs_prev": m.card_jsd_late,
            })
            del prev_model
        # vs BC baseline (cumulative drift)
        if probe_bc_model is not None:
            m_bc = probe_eval.compare(model, probe_bc_model)
            log_dict.update({
                "probe/card_jsd_vs_bc": m_bc.card_jsd,
                "probe/mode_jsd_vs_bc": m_bc.mode_jsd,
                "probe/value_mae_vs_bc": m_bc.value_mae,
            })
```

## Test cases (required)

- `test_jsd_identical_models`: models with identical weights → all JSD = 0.0, top1 agree = 1.0
- `test_jsd_random_models`: two randomly-initialized models → JSD > 0, values in [0,1]
- `test_jsd_masking`: positions with only 1 legal card → card JSD = 0 (only one outcome)
- `test_probe_metrics_phases`: probe set has positions from t1..t10 → early/mid/late
  all populated (not NaN)
- `test_build_probe_set_stratification`: build_probe_set output has ≥1 row per stratum
  (early/mid/late × USSR/US)
- `test_probe_evaluator_load`: ProbeEvaluator loads parquet, stores correct tensor shapes

## Acceptance criteria

- [ ] `uv run python scripts/build_probe_set.py --data-dir data/ppo_rollout_combined --out /tmp/probe_test.parquet --n 100 --seed 42` runs without error
- [ ] `ProbeEvaluator("/tmp/probe_test.parquet").compare(model, model)` returns all-zero JSD
- [ ] All test cases pass: `uv run pytest tests/python/test_jsd_probe.py -q`
- [ ] No regressions: `uv run pytest tests/python/ -q -n auto` green
- [ ] W&B logs `probe/card_jsd_vs_prev` when `--probe-set` provided
- [ ] `probe_every=0` disables probe with no error

## Constraints

- No new pip dependencies (torch, polars, pyarrow already available)
- Legal masking: zero out illegal logits before softmax, renormalize; positions where
  mask has 0 legal actions are skipped
- JSD formula: `JSD = 0.5 * KL(P||M) + 0.5 * KL(Q||M)` where `M = 0.5*(P+Q)`; normalize
  by log(2) to bound to [0,1]; use log-sum-exp stable implementation
- Country head: only include positions where country head is active (mode in {0,2,3})
- `build_probe_set.py` must be deterministic given same seed
- Probe parquet is immutable after creation; never overwrite without explicit `--force` flag
- `ProbeEvaluator` runs models in `torch.no_grad()` eval mode; restore `model.train()`
  after comparison
- card_mask in probe parquet: precompute from `hand_card_ids` column (set True for each
  card_id-1 index present in hand); if column missing, fall back to all-True
- Use polars for parquet I/O (already used in dataset.py)
- `ppo_rollout_combined` parquet uses columns: `influence`, `cards`, `scalars`,
  `raw_turn`, `side_int`, `raw_defcon`, `raw_vp`, `hand_card_ids`, `mode_id`
