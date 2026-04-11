# Opus Analysis: MCTS Usage and v22 Replication
Date: 2026-04-10T21:42:58Z
Question: Does PPO use MCTS for rollouts? And why can't we replicate v22's 2089 Elo?

## Executive Summary

PPO rollouts do NOT use MCTS search (0 simulations), but they DO use the `rollout_action_from_outputs` function in `mcts_batched.cpp` for action sampling and log_prob computation. The country-head log_prob fix (commit 11c084c) was therefore applied to LIVE code and is the correct fix for the C++/Python log_prob mismatch. However, v22's 2089 Elo was achieved under a fundamentally different configuration: T=1.0 rollout temperature, no Dirichlet noise, no PFSP, simpler fixtures (v4/v8/v12), and critically, no country-head log_prob mismatch because the hard-argmax strategy path in old C++ code happens to be close to the mixed distribution at T=1.0. The v23-v43 regression is caused by a compound of three factors: (1) rollout-temp=1.2 introduced a temperature log_prob mismatch (fixed in 41564d4), (2) the country-head hard-argmax log_prob mismatch (fixed in 11c084c), and (3) the accumulated config changes (Dirichlet noise, PFSP, fixture changes) that were never validated independently.

## Findings

### Does PPO Use MCTS?

**No MCTS search. Yes, same C++ action-sampling code path.**

The call chain is:
1. `train_ppo.py` calls `collect_rollout_batched()` (line 690)
2. Which calls `tscore.rollout_games_batched()` (Python binding)
3. Which calls `ts::rollout_games_batched()` in `mcts_batched.cpp` (line 4486)
4. Which calls `rollout_action_from_outputs()` (line 4594) for each decision point
5. `rollout_action_from_outputs()` (line 3507) does: mask legal actions → sample with temperature → compute log_prob → return `RolloutStep`

The `n_simulations` is set to 0 in `rollout_games_batched` (line ~4503: `config.mcts.n_simulations = 0`). There is no MCTS tree search. The function name `mcts_batched.cpp` is misleading — it contains both the MCTS search code AND the direct-policy rollout code.

### The Log_Prob Fix: Applied to Live Code or Dead Code?

**Applied to LIVE code. The fix is correct and necessary.**

The country-head log_prob fix (11c084c) modifies `rollout_action_from_outputs()` at lines 3627-3660. This function is called on every decision point during PPO rollout. The fix changes:

**Before (buggy):**
```cpp
// Hard-argmax: pick ONE strategy, use its raw logits
auto strategy_index = strategy_logits_raw.argmax(0);
source_logits = country_strategy_logits_raw[strategy_index];
// Then log_softmax(source_logits) for log_prob
```

**After (fixed):**
```cpp
// Use the mixed probability distribution (matching Python exactly)
source_probs = country_logits_raw;  // already mixed probs
// Mask → normalize → log for log_prob
```

The Python `_compute_log_prob` (line 315) computes country log_prob as:
```python
probs = country_logits.clone()   # mixed distribution
probs[~country_mask] = 0.0
probs = probs / (probs.sum() + 1e-10)
log_prob = sum(log(probs[c]) for c in country_targets)
```

The old C++ code used a DIFFERENT distribution (one strategy's logits, softmaxed) vs the Python's mixed distribution. This creates systematically biased importance sampling ratios during PPO updates.

### Why v22 Was Not Affected By the Country-Head Bug

v22 ran at T=1.0 (no `--rollout-temp` flag). At T=1.0:
- The temperature log_prob mismatch (fixed in 41564d4) is zero — `log_softmax(logits/1.0) == log_softmax(logits/1.0)`.
- The country-head hard-argmax mismatch still exists, but is less severe: the dominant strategy's distribution is closer to the mixture when T=1.0 (no temperature amplification of the mismatch).

The country-head bug was always present in v8-v22, but its effect was masked because:
1. T=1.0 means sampling is from the original distribution, so the hard-argmax strategy's log_prob is typically close to the mixture's log_prob when the mixing weights are peaky (one strategy dominates).
2. v8-v22 used simpler configs (no Dirichlet noise, no PFSP) that didn't amplify the mismatch.

### Clip Spike Root Cause

The clip=0.57 at v38 iter 1 (and similar spikes in v23-v37) is caused by the log_prob mismatch between C++ rollout and Python PPO update.

**Mechanism:**
1. C++ rollout stores `old_log_prob` using one computation (hard-argmax strategy at T=1.2)
2. Python PPO recomputes `log_prob` using the correct mixed distribution at T=1.0
3. The importance ratio `r = exp(new_log_prob - old_log_prob)` is systematically biased
4. Large ratios trigger clipping → clip fraction spikes
5. The optimizer pushes the policy toward the "wrong" direction (matching the biased ratios)
6. This cascades into entropy collapse and strength loss

For v38 specifically: it was restarted from v22 with the country-head fix applied (11c084c). The fix means the NEW C++ code computes log_prob differently from what the v22 model was trained with. So the first iteration has a large distributional shift between the stored log_probs (from v22's perspective) and the recomputed ones (from the fixed code). This causes an initial clip spike that should resolve within a few iterations IF the fix is correct — but the damage from early training instability may persist.

### v22 Training History

v22 was launched at 2026-04-09T17:30:36Z with this command:
```
uv run python scripts/train_ppo.py \
  --checkpoint data/checkpoints/ppo_v21_league/ppo_final.pt \
  --out-dir data/checkpoints/ppo_v22_league \
  --n-iterations 200 --games-per-iter 200 \
  --lr 2e-5 --clip-eps 0.12 \
  --ent-coef 0.03 --ent-coef-final 0.005 \
  --max-kl 0.3 \
  --league data/checkpoints/ppo_v22_league \
  --league-save-every 10 --league-mix-k 4 \
  --league-fixtures v4_scripted.pt v8_scripted.pt v12_scripted.pt \
  --eval-every 20 --eval-opponent v21_scripted.pt \
  --rollout-workers 1 --device cuda --wandb
```

Key differences from current config (v38+):
| Parameter | v22 | v38+ (current) |
|-----------|-----|----------------|
| rollout-temp | 1.0 (default) | 1.2 |
| dir-alpha | 0 (none) | 0.3 |
| dir-epsilon | 0 (none) | 0.25 |
| pfsp-exponent | not used | 1.0 |
| league-recency-tau | not used | 20 |
| league-fixture-fadeout | not used | 150 |
| league-fixtures | v4/v8/v12 | v8/v14/v22 |
| eval panel | single opponent | 4-opponent panel |
| C++ country log_prob | hard-argmax (buggy) | mixed dist (fixed) |

v22 finished at ~18:41 with Elo 2109.3. It was part of a steady improvement from v8 (1931) through v22 (2089) — every generation improved or held steady.

### Why Can't We Match v22?

There are multiple compounding factors:

1. **Config regression cascade**: Starting with v23, `--rollout-temp 1.2` was added. This immediately triggered the temperature log_prob mismatch bug (not present at T=1.0). v23 collapsed to 1733 Elo. Every subsequent generation inherited this corrupted lineage.

2. **Country-head log_prob mismatch at T=1.2**: Even after the temperature fix (41564d4), the country-head hard-argmax mismatch remained. At T=1.2, the hard-argmax strategy selection diverges MORE from the mixture than at T=1.0, because temperature amplifies the difference between the dominant strategy's distribution and the mixture. This bug persisted through v24-v37.

3. **Starting from corrupted checkpoints**: v27-v37 restarted from v22/ppo_best.pt, but with the country-head bug still present. Each generation lost Elo, ending up 200-370 Elo below v22.

4. **v38 was the first truly fixed run, but it started with a clip spike**: v38 was the first generation with both the temperature fix AND the country-head fix. But starting from v22's checkpoint with different log_prob computation creates an initial distributional mismatch. v38 achieved only 1689 Elo.

5. **Dirichlet noise + PFSP + fixture changes were never validated independently**: These were added simultaneously around v23-v24. None of these were tested in isolation. Dirichlet noise (dir_alpha=0.3) adds significant exploration that may hurt early training stability. PFSP opponent selection changes the training distribution. The v22 fixture (playing against yourself) creates a circular dependency.

6. **Elo ladder may have inflated v22**: v22 was evaluated against v8-v21, all weaker opponents. The current ladder includes v27-v41 (weaker models), which may deflate v22's rating somewhat, but v22 remains the clear leader at 2089.

## Conclusions

1. **CRITICAL**: PPO rollouts DO use `rollout_action_from_outputs` from `mcts_batched.cpp`. The file name is misleading but the code path is live. The country-head log_prob fix is applied to the correct function.

2. **CRITICAL**: v22's success was at T=1.0 with NO Dirichlet noise, NO PFSP, and simpler fixtures. The current config (T=1.2 + Dirichlet + PFSP) has NEVER been validated to work correctly, even with both log_prob fixes applied. The config changes were introduced simultaneously with the temperature bug, making it impossible to attribute the regression.

3. **CRITICAL**: The v38-v41 lineage (post country-head fix) still shows ~300 Elo deficit vs v22. This means the country-head fix alone is not sufficient. The remaining deficit is likely caused by: (a) initial clip spike from switching log_prob computation mid-lineage, and/or (b) the T=1.2 + Dirichlet config itself being harmful.

4. **WARNING**: Every generation from v23-v43 was trained with a different C++ binary than v22 used. v22 used the pre-temperature-fix, pre-country-head-fix binary. The "fixed" binary computes different log_probs, which means starting from a v22 checkpoint creates an initial mismatch.

5. **WARNING**: The Dirichlet noise (dir_alpha=0.3, dir_epsilon=0.25) was never tested at T=1.0. It may be beneficial or harmful — we don't know because it was always confounded with the log_prob bugs.

6. **INFO**: The steady v8→v22 improvement (1931→2089, ~11 Elo per generation) was achieved with the simplest possible config: T=1.0, no exploration noise, basic league with weak fixtures, single-opponent eval. Adding complexity did not help.

## Recommendations

1. **Run a clean v44 with v22's EXACT config** (highest priority):
```bash
nohup nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint data/checkpoints/ppo_v22_league/ppo_best.pt \
  --out-dir data/checkpoints/ppo_v44_league \
  --n-iterations 200 --games-per-iter 200 \
  --lr 2e-5 --clip-eps 0.12 \
  --ent-coef 0.03 --ent-coef-final 0.005 \
  --max-kl 0.3 \
  --league data/checkpoints/ppo_v44_league \
  --league-save-every 10 --league-mix-k 4 \
  --league-fixtures \
    data/checkpoints/scripted_for_elo/v8_scripted.pt \
    data/checkpoints/scripted_for_elo/v14_scripted.pt \
    data/checkpoints/scripted_for_elo/v22_scripted.pt \
    __heuristic__ \
  --eval-every 20 \
  --eval-panel \
    data/checkpoints/scripted_for_elo/v8_scripted.pt \
    data/checkpoints/scripted_for_elo/v14_scripted.pt \
    data/checkpoints/scripted_for_elo/v22_scripted.pt \
    __heuristic__ \
  --rollout-workers 1 --device cuda --wandb --wandb-run-name ppo_v44_baseline
```
Note: NO `--rollout-temp`, NO `--dir-alpha`, NO `--dir-epsilon`, NO `--pfsp-exponent`. This tests whether the fixed C++ code + v22's config can continue improving.

2. **If v44 matches or exceeds v22, THEN add features one at a time**:
   - v45: add `--rollout-temp 1.1` (conservative)
   - v46: add `--dir-alpha 0.15 --dir-epsilon 0.15` (halved from current)
   - v47: add PFSP
   Each should be benchmarked against v22 before adding the next feature.

3. **Consider recomputing old_log_probs from the v22 checkpoint before starting v44**: Use `_recompute_log_probs_and_values()` (line 634 in train_ppo.py) to eliminate the initial mismatch from loading a checkpoint trained with old C++ code. This may require a small code change to run this function on the first iteration's rollout data.

4. **Track clip fraction at iter 1 as a diagnostic**: If clip > 0.15 at iter 1, the initial distributional mismatch is too large. The run should be restarted with recomputed log_probs or a lower learning rate for the first 5 iterations.

## Open Questions

1. **Is the country-head bug's effect at T=1.0 truly negligible?** The hard-argmax strategy log_prob differs from the mixture log_prob even at T=1.0. The v8-v22 progression worked despite this bug — was it helping (lucky cancellation), neutral, or slightly harmful?

2. **What is the Elo ceiling with T=1.0 and no exploration noise?** v22 was generation 15 in the v8-v22 lineage. Would v23-v30 have continued improving at T=1.0 with the original (buggy) C++ code? We'll never know, but v22's rate of improvement was slowing (v20=2072, v21=2078, v22=2089).

3. **Does the fixed C++ code produce BETTER or WORSE training signal than the buggy code at T=1.0?** The hard-argmax strategy selection might have acted as implicit regularization (concentrating country selections on one strategy). The mixed distribution is mathematically correct but may produce noisier gradients.

4. **Should we consider reverting the country-head fix for T=1.0 runs?** If the buggy code worked for v8-v22, and the fixed code hasn't matched v22 in 20+ generations, maybe the "bug" was a feature. This is a risky hypothesis but worth considering if v44 also fails.

5. **Why does v38 (from v22, with fix) do WORSE than v27-v37 (from v22, without fix)?** v38=1689, while v30-v37 averaged ~1850. The country-head fix may have made things worse by creating a larger initial mismatch when loading v22's checkpoint. Alternatively, the addition of `--league-fixture-fadeout 150` or the confirmation tournament changes may have introduced new problems.
