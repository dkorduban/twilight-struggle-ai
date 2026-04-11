---
# Opus Analysis: Country JSD Near Zero
Date: 2026-04-09T21:50:00Z
Question: Why is country_jsd ~0.0001 everywhere across all model pairs?

## Executive Summary

The near-zero country JSD is caused by a **double-softmax bug** in `jsd_probe.py`. The main model architectures (TSBaselineModel, TSControlFeatModel, TSControlFeatGNNModel, TSControlFeatGNNSideModel, TSCountryAttnModel, TSCountryAttnSideModel) return `country_logits` as a **mixture of already-softmaxed strategy probabilities** -- values in [0, 1] summing to ~1, NOT raw logits. The JSD probe then applies `torch.softmax()` again via `_masked_probs()`, which maps these near-zero probability values (~1/86 each) to a near-uniform distribution. This crushes all divergence: empirical testing shows a ~5000x underestimate of the true JSD. The card and mode heads are unaffected because they output genuine unnormalized logits.

## Findings

### Root cause: double-softmax on country probabilities

In `python/tsrl/policies/model.py`, 6 of the 11 model classes compute `country_logits` as:

```python
strategy_probs = torch.softmax(country_strategy_logits, dim=2)  # already softmaxed
mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
country_logits = (mixing * strategy_probs).sum(dim=1)  # convex combination of softmaxes
```

This means `country_logits` is already a valid probability distribution (values in [0, 1], summing to ~1). The name `country_logits` is misleading -- it should be `country_probs`.

In `jsd_probe.py`, `_masked_probs()` applies `torch.softmax()` unconditionally:

```python
masked_logits = torch.where(mask, logits, torch.zeros_like(logits))
probs = torch.softmax(masked_logits, dim=1)
```

When the input is already a probability distribution with values ~0.012 (1/86), softmax treats these as near-identical logits and produces an almost uniform output. Specifically:

- Raw probability range: 0.0007 -- 0.056
- After double-softmax: 0.01150 -- 0.01216 (ratio max/min = 1.06)
- JSD from double-softmax: 4.6e-05
- JSD from correct computation: 0.231
- **Underestimate factor: ~5000x**

### Affected model architectures

Models returning **pre-softmaxed probabilities** (affected by the bug):
- `TSBaselineModel` (the `_baseline_forward` helper)
- `TSCardEmbedModel`
- `TSControlFeatModel`
- `TSControlFeatGNNModel`
- `TSControlFeatGNNSideModel`
- `TSCountryAttnModel`
- `TSCountryAttnSideModel`

Models returning **actual logits** (NOT affected):
- `TSDirectCountryModel` -- uses `nn.Linear` directly
- `TSMarginalValueModel` -- uses `torch.sigmoid().sum()` (still not logits, but has wider range)

### Probe data is NOT the problem

The probe dataset has 996 positions with 768 (77%) having `mode_id` in {0, 2, 3} (country head active). This is ample coverage. The mode distribution:

| mode_id | count |
|---------|-------|
| 0       | 592   |
| 1       | 185   |
| 2       | 26    |
| 3       | 150   |
| 4       | 43    |

### Country mask is NOT the problem

The country mask only excludes index 64 (1 out of 86 countries), leaving 85 legal countries. This does not constrain the distribution enough to collapse JSD.

### Test coverage gap

The test `test_jsd_random_models` (line 142) uses `TinyProbeModel` which has a plain `nn.Linear(32, 86)` country head returning actual logits, so the double-softmax does not manifest in tests. The test correctly asserts `country_jsd > 0`, but the synthetic model does not reproduce the real model's mixture-of-softmax output. The test passes but does not catch the production bug.

## Conclusions

1. **Root cause confirmed**: `country_logits` from all main model architectures is already a probability distribution (mixture of softmaxes), but `_masked_probs()` in `jsd_probe.py` applies softmax again, collapsing all values to near-uniform and reducing JSD by ~5000x.

2. **Card and mode heads are unaffected** because they output genuine unnormalized logits from `nn.Linear`.

3. **The variable name `country_logits` is misleading** across the entire codebase -- it is actually `country_probs` for 7 of 9 model architectures.

4. **The test suite does not catch this** because the synthetic test model uses a plain linear head, unlike the real models.

5. **The data is fine**: 77% of probe positions have an active country head with 85 legal countries. The problem is purely in the JSD computation.

## Recommendations

1. **Fix `_jsd()` or `_masked_probs()` in `jsd_probe.py`** to detect when inputs are already probabilities (values in [0,1] summing to ~1) and skip the softmax, OR add a `logits_or_probs` flag to the `_jsd` call for the country head. The cleanest fix:

   ```python
   # In compare(), for the country head:
   country_jsd = self._jsd(
       out_a["country_logits"], out_b["country_logits"],
       batch_country_mask,
       already_probs=True,  # mixture-of-softmax output
   )
   ```

   Then in `_jsd`, when `already_probs=True`, apply masking and renormalization but skip the softmax step.

2. **Add a regression test** that uses a model with mixture-of-softmax country output (like the real architectures) and asserts `country_jsd > 0.01` for different random seeds.

3. **Consider renaming `country_logits` to `country_probs`** in the model output dict to prevent future confusion. This is a larger change touching training loops and loss code, so it should be done carefully.

4. **Re-run the JSD probe** after the fix to get accurate country divergence numbers across checkpoint pairs.

## Open Questions

1. Should `_jsd()` use `country_strategy_logits` (the raw per-strategy logits before softmax) instead of the mixed probabilities? This would give true logit-space JSD and is available in the model output dict for most architectures.

2. The `TSMarginalValueModel` returns `torch.sigmoid().sum()` for country_logits -- this is neither logits nor probabilities. Should it be handled separately?

3. Are there downstream consumers of the country JSD metric that made decisions based on the incorrect near-zero values?
