# Opus Analysis: v27 Clip/KL/Entropy Spike
Date: 2026-04-09
Question: v27 PPO training shows clip frac / approx KL / policy loss spike and entropy drop — root cause investigation.

## Executive Summary

The v27 "spikes" are actually **healthy transient adaptation**, not training instability. The clip fraction starts at 0.59 and monotonically decays to 0.11 by iter 43, approx KL drops from 0.039 to 0.003, and entropy *rises* from 4.12 to 5.16. This is the expected pattern when a strong checkpoint (v22, Elo 2098) is placed into a new league pool and must adapt its policy to a different opponent distribution. The initial high clip fraction is caused by the rollout temperature (T=1.2) creating a flatter collection policy whose log-probs diverge from the model's T=1.0 log-probs stored by the C++ bindings — but this effect self-corrects as the policy adapts. There is no pathological collapse; v27 is training normally.

## Findings

### Hypothesis A: Stale value baseline
**Partially confirmed but benign.** The v22 checkpoint's value head was calibrated against v12-era league opponents. v27's league pool starts fresh (only iter_0001, plus fixtures v8/v14/v22/heuristic). The initial value loss is high (0.107) but declines steadily to 0.067 by iter 43. The value head is recalibrating normally. This contributes to early large advantages and thus high clip fractions in iters 1-5, but it does not cause a persistent problem.

### Hypothesis B: LR too high
**Not the root cause.** lr=2e-5 and clip-eps=0.12 are identical to v22, which trained successfully at these settings. v22's clip fraction started at 0.109 and stayed in the 0.05-0.13 range throughout. The difference is that v22 did NOT use rollout-temp=1.2 — it used the default T=1.0. The higher initial clip fraction in v27 (0.59 vs 0.11) is driven by the temperature mismatch, not by LR being too aggressive.

### Hypothesis C: League opponent diversity
**Minor contributor.** v27 starts with a clean league pool and faces a mix of self, iter_0001 (very early/weak snapshot), and fixtures (v8/v14/v22 scripted + heuristic). The opponent variance does cause rollout_wr to swing between 0.15-0.54 depending on which opponents are drawn, but the clip fraction and KL metrics track a smooth downward trend regardless of opponent mix. This is not the driver.

### Hypothesis D: Entropy collapse / mode collapse
**Refuted by the data.** Entropy is *increasing* throughout v27 training:
- Iter 1: 4.121
- Iter 10: 4.614
- Iter 20: 4.832
- Iter 30: 5.082
- Iter 43: 5.003-5.157

This is the opposite of entropy collapse. The entropy coefficient (0.03) is actively encouraging exploration, and the policy is becoming more uniform over time. The v23/v24 entropy collapse problem (the one that destroyed the v23-v26 lineage) was caused by the temperature-scaled log_prob bug, which was fixed before v27 launched.

### Hypothesis E: UPGO flag
**Not active for v27.** The ppo_loop_step.sh enables UPGO only when `plateau_count >= 1`. v27 was launched manually (bypassing the loop step), and the log shows no UPGO flag. The launch command from autonomous_decisions.log shows `--rollout-temp 1.2` but no `--upgo`.

### Hypothesis F: Rollout temperature mismatch (PRIMARY CAUSE of initial high clip fraction)
**Confirmed as the main driver of the initial elevated metrics, but it is self-correcting.**

The mechanism:
1. C++ rollout uses T=1.2 to sample actions (flatter distribution = more exploration).
2. However, `sample_index_from_masked_logits()` stores the log_prob at T=1.0 (unscaled logits), per the fix from commit 41564d4 that resolved the v23 collapse.
3. Python PPO update recomputes new_log_probs at T=1.0 (raw logits, no temperature).
4. **The stored old_log_prob and the recomputed new_log_prob are both at T=1.0**, so the IS ratio `exp(new_log_prob - old_log_prob)` is correct.

So why is clip fraction high? Because T=1.2 sampling selects actions that the T=1.0 policy assigns *different* probabilities to. Specifically:
- T=1.2 is more likely to sample low-probability actions.
- When the policy update encounters these low-probability actions with large advantages, the gradient pushes the ratio far from 1.0.
- The clipping mechanism then engages heavily (clip_frac = 0.59).

But this is **working as intended**: clipping prevents catastrophic updates, the policy gradually adapts, and clip fraction decays smoothly. By iter 40+, clip fraction has settled to 0.11-0.12, comparable to v22's range.

### Comparison: v27 vs v22 metrics trajectory

| Metric | v22 iter 1 | v22 iter 20 | v27 iter 1 | v27 iter 20 | v27 iter 43 |
|--------|-----------|------------|-----------|------------|------------|
| clip   | 0.109     | 0.087      | 0.592     | 0.200      | 0.122      |
| kl     | 0.0029    | 0.0024     | 0.0331    | 0.0064     | 0.0039     |
| pl     | -0.0187   | -0.0142    | 0.0232    | -0.0029    | -0.0037    |
| ent    | 4.179     | 4.117      | 4.121     | 4.832      | 5.003      |
| vl     | 0.1007    | 0.0995     | 0.1071    | 0.0730     | 0.0669     |

Key observations:
- v22 had very low clip fraction from iter 1 because it used T=1.0 (no temperature mismatch).
- v27 starts high but converges to the same range by iter 30-40.
- v27 has higher entropy than v22 at the same iteration count, which is expected with T=1.2 exploration and ent-coef=0.03.
- v27 policy loss is positive early (policy being pushed toward better actions) then turns slightly negative (policy already good at the collected data).

### Pattern analysis
- **No single spike iteration**: The elevated metrics are at iter 1 and decay monotonically. There is no sudden spike at any later iteration.
- **No correlation with league pool changes**: iter_0010 saved at iter 9, iter_0020 at iter 19, iter_0030 at iter 29. No metric discontinuity at these points.
- **No early stopping triggered**: grep confirms 0 occurrences of "early stopping" in the v27 log. max-kl=0.3 is never breached (peak approx_kl is 0.039).
- **Recovery is smooth and complete**: By iter 40, all metrics are in healthy ranges.

### H2H evaluation results
v27 shows promising strength despite early metric concerns:
- Iter 20 H2H vs v22: USSR=0.650 US=0.400 combined=0.525 (new best)
- Iter 40 H2H vs v22: USSR=0.600 US=0.420 combined=0.510 (still strong)

Combined win rate >0.50 against v22 (Elo 2098) is a positive signal.

## Conclusions

1. **There is no training instability.** The initial high clip fraction / KL / positive policy loss in v27 is a normal transient caused by rollout temperature T=1.2 creating an exploration-heavy collection policy. All metrics decay smoothly to healthy ranges within ~30 iterations.

2. **The v23 log_prob bug is correctly fixed.** The C++ bindings now store log_prob at T=1.0, matching the Python PPO recomputation. The IS ratios are mathematically correct. The elevated clip fraction is from the *action distribution shift* induced by T=1.2, not from a log_prob mismatch.

3. **v27 is NOT exhibiting the same failure mode as v23/v24/v25.** Those runs collapsed due to a bug (temperature-scaled log_prob creating systematically biased IS ratios) leading to genuine entropy collapse. v27 shows entropy *increasing*, clip fraction *decreasing*, and healthy H2H performance. The symptoms only look similar superficially.

4. **The stale value baseline effect is minor and self-correcting.** Value loss declines from 0.107 to 0.067 as the value head recalibrates to the new opponent distribution.

5. **Rollout win rate (~20-30% in league play) is expected.** The model plays against itself, past versions, and strong fixtures (v22 scripted). Low self-play win rate is not a concern.

## Recommendations

1. **Let v27 continue training to completion.** The metrics are healthy and improving. No intervention needed.

2. **Consider reducing initial clip fraction transient** by using a warmup schedule for rollout temperature: start at T=1.0 for the first 10-20 iterations, then ramp to T=1.2. This would make the initial metrics less alarming without sacrificing late-training exploration.

3. **Add a "burn-in" diagnostic** to the training log: print a note like "[warmup] iter N < 30: elevated clip/KL from T=1.2 exploration is expected" for the first 30 iterations when rollout-temp > 1.0. This prevents false alarm in future runs.

4. **Do not change lr, clip-eps, or ent-coef** for v27 or subsequent runs. These settings are working correctly.

5. **Monitor H2H at iter 60, 80, 100** to confirm continued strength improvement. If combined win rate vs v22 drops below 0.45, that would warrant investigation.

6. **For future runs**: if clip fraction > 0.4 persists past iter 50, that would be a genuine problem. In v27, it drops below 0.2 by iter 20 and below 0.15 by iter 30.

## Open Questions

1. **Is T=1.2 the optimal rollout temperature?** The exploration benefit is clear (entropy rising, diverse action sampling), but the initial transient wastes ~20 iterations of training. A/B testing T=1.1 vs T=1.2 would quantify the tradeoff.

2. **Should PPO epochs be reduced during the warmup phase?** With 4 PPO epochs and high initial IS ratios, the clipping is doing significant work in iters 1-10. Reducing to 2 epochs for the first 20 iterations might give slightly smoother adaptation.

3. **What is the Elo ceiling for this lineage?** v22 was 2098. v27's H2H vs v22 at iter 20 (0.525) suggests it may already be slightly stronger. The final Elo will depend on whether exploration quality translates to strength.
