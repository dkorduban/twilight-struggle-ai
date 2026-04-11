---
# Opus Analysis: Post-v22 PPO Entropy/KL Spike Root Cause
Date: 2026-04-10T00:15:00Z
Question: Why do v23, v24, and v27 all exhibit early policy_loss/clip_fraction/approx_kl spikes and entropy drops that v22 did not show?

## Executive Summary

The root cause is a **country head log_prob computation mismatch between C++ rollout and Python PPO update** that has existed since the C++ batched rollout was introduced, but was masked when rollout temperature was 1.0 (v8-v22) and became catastrophic when temperature 1.2 was introduced (v23+). The C++ rollout computes country log_probs using `log_softmax(argmax_strategy_raw_logits)` -- a HARD strategy selection on one strategy's raw logits -- while the Python PPO update computes them using `log(soft_mixture_of_all_strategies_probs)`. These produce systematically different values, creating biased importance sampling ratios that corrupt PPO training. The temperature mismatch bug (commit 41564d4) was correctly identified and fixed for the card and mode heads, but the SAME class of mismatch in the country head was never fixed. v27's final Elo of 1762 (vs v22's 2102) confirms this is a real regression, not a transient.

## Findings

### The Country Head Mismatch (PRIMARY ROOT CAUSE)

**C++ rollout** (`rollout_action_from_outputs`, mcts_batched.cpp lines 3630-3646):
```cpp
auto source_logits = country_logits_raw;  // mixed probs from model
if (strategy_logits_raw.defined() && country_strategy_logits_raw.defined()) {
    const auto strategy_index = strategy_logits_raw.argmax(0).item<int64_t>();
    source_logits = country_strategy_logits_raw.index({strategy_index});  // RAW logits from ONE strategy
}
const auto country_log_probs = torch::log_softmax(masked_country, 0);  // log_softmax on raw logits
```

The C++ picks the highest-weight strategy via hard argmax, then computes `log_softmax` on that single strategy's raw logits. This gives the probability distribution of ONE strategy, not the mixed distribution.

**Python PPO update** (train_ppo.py lines 1583-1604):
```python
country_probs_b = country_logits_b.clone()  # model's country_logits = MIXED probs
country_probs_b = country_probs_b.masked_fill(~country_masks_b, 0.0)
country_probs_b = country_probs_b / (country_probs_b.sum(dim=1, keepdim=True) + 1e-10)
log_country_b = torch.log(country_probs_b + 1e-10)
```

Python uses `country_logits` which the model computes as:
```python
mixing = softmax(strategy_logits, dim=1).unsqueeze(2)  # soft mixing weights
strategy_probs = softmax(country_strategy_logits, dim=2)  # per-strategy probs
country_logits = (mixing * strategy_probs).sum(dim=1)  # SOFT mixture
```

Python never accesses `strategy_logits` or `country_strategy_logits` -- only the mixed result.

**Quantified magnitude**: For a state where strategy 0 has mixing weight 0.7 and strategy 1 has weight 0.3, and a country that strategy 0 favors (p=0.5) but strategy 1 disfavors (p=0.01):
- C++ log_prob = log(0.5) = -0.693 (using strategy 0's probs only)
- Python log_prob = log(0.7*0.5 + 0.3*0.01) = log(0.353) = -1.041
- Difference: 0.348 per country target

For a 4-ops influence placement with 4 targets, this accumulates to ~1.39 total log_prob difference. The importance ratio `exp(new - old)` would be `exp(-1.39) = 0.25` -- the PPO optimizer sees this as the action being 4x less likely under the new policy than the old, even though the model hasn't changed at all.

### Why v22 Was Stable Despite the Mismatch

v22 used `--rollout-temp 1.0` (the default). At T=1.0:
1. The card and mode heads had no temperature mismatch (both C++ and Python use raw logits)
2. The country head mismatch existed but was partially masked because:
   - The model was being continuously updated, so the bias was absorbed into the policy gradient
   - The strategy mixer in a well-trained model concentrates weight on one strategy, making hard-argmax approximately equal to soft-mixture
   - The magnitude of the bias was stable (same model weights in rollout and update)
3. v22's clip fraction was 0.05-0.13 throughout -- the small country head bias didn't push ratios past the clipping threshold

### Why v23+ Collapsed

v23 introduced `--rollout-temp 1.2`. This created TWO simultaneous mismatches:

1. **Temperature mismatch (card + mode heads)**: C++ stored `log_prob(logits/1.2)`, Python recomputed `log_prob(logits/1.0)`. This was fixed in commit 41564d4 for card and mode heads.

2. **Strategy mismatch (country head)**: C++ used hard-argmax strategy + log_softmax(raw_logits), Python used soft-mixture log(probs). This was NEVER fixed.

With T=1.2, the rollout samples more exploratory actions (lower-probability under T=1.0). These actions tend to be ones where the strategy distributions disagree more -- exactly the cases where the hard-argmax vs soft-mixture discrepancy is largest. The temperature amplified the country head mismatch.

### v27 Confirmation

v27 launched with the temperature fix in place (SO rebuilt at 15:45 Apr 9, v27 launched at 02:04 Apr 10). The card and mode head temperature mismatch was resolved. But:
- v27 still used `--rollout-temp 1.2`
- The country head strategy mismatch remained unfixed
- v27's final Elo: 1762 (vs v22's 2102) -- a 340 Elo regression
- The early spike pattern (clip=0.59, KL=0.033) looks similar to v23/v24

The previous analysis (opus_analysis_20260409_v27_clip_kl_spike.md) examined only the first 43 iterations and concluded the spike was "healthy transient adaptation." This conclusion was WRONG -- v27's final Elo of 1762 proves it collapsed, just more slowly than v23/v24 because the temperature mismatch was fixed for card/mode heads.

### Dirichlet Noise Is a No-Op

The `--dir-alpha 0.3 --dir-epsilon 0.25` parameters are passed to C++ but stored on `config.mcts.dir_alpha`. With `n_simulations=0` (no MCTS tree search), the Dirichlet noise is never applied. The `apply_root_dirichlet_noise_fast` function only runs during MCTS tree expansion. This is not contributing to the problem but is a separate correctness issue (Dirichlet noise is silently not applied).

### Timeline of Changes

| Date/Time | Event | Impact |
|-----------|-------|--------|
| Apr 7 17:52 | kScalarDim prepared (gated at 11) | No effect |
| Apr 9 12:38 | kScalarDim bumped to 32 (commit 756ce37) | C++ produces 32-dim scalars |
| Apr 9 15:12 | Temperature fix committed (41564d4) | Card/mode log_prob fixed for T!=1.0 |
| Apr 9 15:45 | C++ binary rebuilt (UPGO commit b6abafc) | Fix takes effect |
| Apr 9 17:30 | v22 launched (T=1.0, no rollout-temp flag) | Stable, Elo 2102 |
| Apr 9 18:39 | --rollout-temp 1.2 added to ppo_loop_step.sh | Takes effect v23+ |
| Apr 9 18:48 | v23 launched (T=1.2, old binary w/o temp fix) | Collapsed: card+mode temp bug + country strategy bug |
| Apr 9 22:26 | v24 launched (from v22, still old binary) | Collapsed: same bugs |
| Apr 10 02:04 | v27 launched (from v22, new binary w/ temp fix) | Card/mode fixed, but country strategy bug remains. Elo 1762. |

## Conclusions

1. **The country head log_prob mismatch between C++ and Python is the remaining root cause.** The C++ rollout uses hard argmax on `strategy_logits` to select one strategy, then computes `log_softmax` on that strategy's raw logits. Python PPO uses `country_logits` which is the soft-weighted mixture of all strategies' softmax probabilities. These produce systematically different log_probs, creating biased importance sampling ratios.

2. **The temperature mismatch fix (commit 41564d4) was necessary but not sufficient.** It correctly fixed the card and mode heads. The country head has an analogous but distinct mismatch that was never addressed.

3. **v27's Elo of 1762 (vs v22's 2102) confirms this is a real regression.** The previous analysis that called it "healthy transient adaptation" was incorrect because it only examined early iterations and did not wait for final Elo.

4. **The mismatch is amplified by rollout temperature > 1.0** because higher temperature causes more exploratory action sampling, which selects actions where strategy distributions disagree more -- exactly the cases with the largest log_prob discrepancy.

5. **Dirichlet noise is not being applied** despite being configured. The noise parameters go to `config.mcts` which only applies during MCTS tree expansion (n_simulations > 0). This is a separate bug but does not contribute to the observed regression.

6. **The fix is straightforward**: the C++ country head log_prob should use the SAME computation as Python -- mask the `country_logits_raw` (mixed probs), normalize, and take log. Specifically, do NOT use `country_strategy_logits_raw` with hard argmax. Alternatively, the C++ should reproduce the exact soft mixture: `mixing_weights * softmax(country_strategy_logits)` summed across strategies.

## Recommendations

1. **Fix the country head log_prob computation in C++ rollout** to match Python. Replace the hard-argmax strategy path (lines 3633-3636) with the soft mixture path. Specifically, in `rollout_action_from_outputs`, the `source_logits` variable should remain as `country_logits_raw` (the soft mixture from the model) and the `if (strategy_logits_raw.defined())` block should be REMOVED or changed to reproduce the soft mixture computation. The `log_softmax` on line 3646 should be changed to `log(masked_country / sum(masked_country))` to match Python's treatment of these as probabilities rather than logits.

2. **Also fix the sampling distribution**: The country SAMPLING (line 3644: `softmax(scaled_country)`) should similarly use the mixed probs, not the hard-argmax strategy logits. Currently the sampling and log_prob use different base distributions (masked raw logits vs masked raw logits for one strategy), which compounds the problem.

3. **Rebuild C++ after the fix** and verify by running a short (10-iteration) canary with `--rollout-temp 1.2` to confirm clip fraction stays below 0.15 and entropy stays in 4.0-4.3 range.

4. **Apply Dirichlet noise at the policy level, not MCTS level**, if exploration noise is desired during PPO rollouts. The current implementation silently drops the noise when n_simulations=0.

5. **Add a log_prob consistency test**: after each rollout batch, recompute log_probs using the Python path and compare to the C++ stored log_probs. Log the mean absolute difference. If >0.01, flag as a warning.

6. **Re-run v27 from v22 with the fix** and verify Elo improvement.

## Open Questions

1. **Why was v22 stable despite the country head mismatch?** The mismatch existed but the model adapted to it at T=1.0. Was this because (a) the magnitude was small enough to absorb, (b) the clipping prevented catastrophic updates, or (c) the strategy mixer concentrated enough to make hard-argmax approximately equal to soft-mixture? Likely all three.

2. **Would T=1.0 with the unfixed country head still work?** v22 proved it does. But the mismatch is still a source of bias that degrades training quality even at T=1.0 -- it just doesn't cause collapse.

3. **Is there a similar mismatch in the MCTS expansion path?** The `expand_from_raw_fast` function also uses `country_strategy_logits` -- check if the same hard-argmax issue applies there.

4. **Should the C++ rollout use `country_logits` directly (as probs)?** This would mean: mask to accessible, renormalize, sample from probs directly (no softmax needed). For log_prob: `log(masked_normalized_probs[target])`. This would perfectly match Python.
---
