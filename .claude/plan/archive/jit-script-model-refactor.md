# Spec: jit.script-Compatible GNN Model

## Goal

Refactor `TSControlFeatGNNModel` (and its encoder) in `python/tsrl/policies/model.py`
to be `torch.jit.script()` compatible, eliminating the need for the 5s/iter Python
log_prob recomputation workaround in `scripts/train_ppo.py`.

## Background

`_export_torchscript_model` tries `jit.script` first, falls back to `jit.trace`.
`jit.trace` freezes data-dependent branches at trace time, causing log_prob divergence.
Fix: make the model `jit.script`-compatible so trace is never needed.

## Root Cause

In `python/tsrl/policies/model.py`, the GNN encoder contains data-dependent branches
that jit.trace freezes but jit.script cannot handle:

```python
# Lines around 1055, 1069, 1075 in TSControlFeatGNNEncoder (approx):
if bg_mask.any():
    bg_pooled = x[:, bg_mask, :].mean(dim=1)
else:
    bg_pooled = torch.zeros(B, D, device=x.device)

if non_bg_mask.any():
    non_bg_pooled = x[:, non_bg_mask, :].mean(dim=1)
else:
    non_bg_pooled = torch.zeros(B, D, device=x.device)
```

Also likely: boolean tensor indexing `x[:, mask, :]` which jit.script cannot handle
when `mask` is a runtime tensor (not a constant).

## Fix Strategy

Replace conditional pooling with weighted-sum pooling (no branching, no dynamic indexing):

```python
# BEFORE (jit.trace freezes branches):
if bg_mask.any():
    bg_pooled = x[:, bg_mask, :].mean(dim=1)  # dynamic boolean index
else:
    bg_pooled = torch.zeros(B, D, device=x.device)

# AFTER (jit.script compatible):
bg_weight = bg_mask.float().unsqueeze(0).unsqueeze(-1)  # (1, 86, 1)
bg_count = bg_weight.sum(dim=1).clamp(min=1.0)          # (1, 1)
bg_pooled = (x * bg_weight).sum(dim=1) / bg_count       # (B, D)
# Note: when bg_mask is all-False, bg_weight=0 → bg_pooled=zeros. Correct behavior.
```

This is mathematically equivalent: when mask entries are True it averages them,
when mask is all-False the result is zeros (same as the else branch).

## Files to Modify

1. **`python/tsrl/policies/model.py`**: Find all `if mask.any():` / `x[:, mask, :]`
   patterns in the GNN encoder and model forward pass. Replace with weighted-sum pooling.
   Also look for `.item()` calls (converting tensor to Python scalar) which also block jit.script.

2. **`scripts/train_ppo.py`**: After verifying `jit.script` now works in
   `_export_torchscript_model`, remove the `_recompute_log_probs_and_values` call
   from `collect_rollout_batched` (line ~589) and `collect_rollout_self_play_batched`.
   The function can stay for fallback but should not be called when jit.script succeeds.

## Implementation Steps

1. Read the full GNN encoder class in model.py (search for `TSControlFeatGNNEncoder`
   or `ControlFeatGNNEncoder`). Identify every:
   - `if tensor.any():` block
   - `x[:, mask, :]` dynamic boolean indexing
   - `tensor.item()` calls that go into Python-level branching

2. For each pattern, apply the weighted-sum replacement above.

3. Test locally:
   ```python
   from tsrl.policies.model import TSControlFeatGNNModel
   import torch
   m = TSControlFeatGNNModel()
   m.eval()
   scripted = torch.jit.script(m)  # must succeed without fallback to trace
   print("jit.script OK")
   ```

4. Verify numerical equivalence (scripted vs non-scripted outputs match on random inputs):
   ```python
   with torch.no_grad():
       inf = torch.randn(4, 172)
       cards = torch.randn(4, 448)
       scalars = torch.randn(4, 11)
       out_orig = m(inf, cards, scalars)
       out_scripted = scripted(inf, cards, scalars)
       for k in out_orig:
           diff = (out_orig[k] - out_scripted[k]).abs().max().item()
           assert diff < 1e-5, f"{k}: max diff {diff}"
   print("Numerical equivalence OK")
   ```

5. In `_export_torchscript_model` (train_ppo.py ~line 1032), verify the try block
   for `jit.script` succeeds (no fallback). If it does, remove the
   `_recompute_log_probs_and_values` call from both rollout functions.

## Acceptance Criteria

1. `torch.jit.script(TSControlFeatGNNModel())` succeeds without exception
2. Scripted and non-scripted outputs are numerically identical (< 1e-5 max diff)
3. `_export_torchscript_model` no longer falls back to `jit.trace`
4. `collect_rollout_batched` no longer calls `_recompute_log_probs_and_values`
   (save the ~5s overhead per iteration)
5. `uv run python -c "import ast; ast.parse(open('scripts/train_ppo.py').read())"` passes
6. No regressions: `uv run pytest tests/python/ -n 0 -x -q` still passes (if tests exist)

## Notes

- The `TSControlFeatModel` (non-GNN) may have similar issues — check and fix those too
- Do NOT change model hyperparameters, output shapes, or training behavior
- Do NOT change the training data or checkpoint format
- The fix is purely mechanical: replace conditional branches with equivalent masked ops
