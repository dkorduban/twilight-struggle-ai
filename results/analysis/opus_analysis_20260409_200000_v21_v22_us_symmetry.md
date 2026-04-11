---
# Opus Analysis: v21/v22 US Symmetry Anomaly
Date: 2026-04-09 UTC
Question: Why do v21 and v22 show unusually strong mutual US play?
---

## Executive Summary

The v21/v22 pair shows a unique pattern: both models achieve >0.52 US win rate against each other (v21-as-US: 0.531, v22-as-US: 0.520), while the typical US WR across all model-vs-model matchups is 0.359 and the frontier-model average is 0.366. This is the ONLY pair out of 45 model pairs where both directions exceed 0.50 US WR. However, statistical significance is low: at n=50 per side, the 95% CI for each measurement spans ~0.38 to ~0.67, and under a null hypothesis of p=0.50 (equal skill on each side), both observations are within 0.4 SE of the null -- entirely expected noise. The pattern is most likely a combination of (a) genuine USSR weakness shared by both models due to their close lineage, amplified by (b) sampling noise at n=50 that makes a ~0.45 true US WR look like ~0.52. The primary training implication is that Elo ratings are NOT inflated by this effect, but the shared USSR weakness in the v20-v22 lineage suggests a need for USSR-side diversity pressure. A critical factual correction: v22 did NOT use rollout-temp 1.2 -- the log shows that change takes effect starting v23.

## Statistical Significance Assessment

### Raw numbers
- v21 as US vs v22: 0.531 (approximately 26/49 games)
- v22 as US vs v21: 0.520 (approximately 26/50 games)
- Sample size: n=50 per side per matchup (n=49 for v21|v22 based on the fraction)
- Standard error at p=0.50: SE = 0.0707

### Confidence intervals (95% Wald)
- v21|v22 US WR: 0.531 +/- 0.138 => [0.392, 0.669]
- v22|v21 US WR: 0.520 +/- 0.138 => [0.382, 0.658]

### Tests against different nulls

**Null H0: true US WR = 0.366 (frontier average)**
- P(observe >= 0.52 | p=0.366, n=50) = 0.017 per direction
- P(both directions >= 0.52) = 0.0003 (assuming independence)
- Verdict: **Significant** that this pair's US WR is above the frontier average. Both being simultaneously this high is very unlikely if the true rate were 0.366.

**Null H0: true US WR = 0.50 (equal side strength between these two)**
- P(observe >= 0.52 | p=0.50, n=50) = 0.44 per direction
- P(both >= 0.52) = 0.20
- Verdict: **Not significant.** If these two models are roughly equal in combined strength but with weak USSR play, seeing 0.52 in both directions is completely unremarkable.

### Z-scores vs frontier distribution
- v21|v22 US WR z-score: 2.10 (above frontier mean)
- v22|v21 US WR z-score: 1.97 (above frontier mean)
- These are notable outliers relative to the frontier distribution, but the frontier distribution itself has sigma=0.078, so being 2 sigma out in ONE pair out of 45 is expected (multiple comparisons: E[pairs with |z|>2] ~ 2 out of 45).

### Conclusion on significance
The v21/v22 pair genuinely has higher US WR than the frontier average. But the specific values of 0.52-0.53 are NOT distinguishable from a true rate of ~0.45-0.50 at n=50. The observation is best explained as: true mutual US WR is approximately 0.45 (significantly above average 0.37, but below 0.50), with noise pushing both observations above 0.50.

## Hypothesis Analysis

### H1: Ancestor-descent exploitation (v22 knows v21's weaknesses)
**Mechanism:** v22 was trained from v21's checkpoint with v21 as eval-opponent, so v22 learned to exploit v21's specific weaknesses.

**Evaluation:** This explains v22-as-US beating v21-as-USSR (0.520), but does NOT explain v21-as-US beating v22-as-USSR (0.531). v21 never saw v22 during training. This hypothesis is at best half the story.

**Verdict:** Partially explains one direction only. Cannot be the sole cause.

### H2: Co-adapted shared USSR weakness (both inherited weak USSR from v20 lineage)
**Mechanism:** v20, v21, and v22 share a training lineage where each generation trains primarily against its parent. If v20 developed a USSR blind spot, v21 inherited it and optimized around it rather than fixing it. v22 inherited the same flaw. Both models' US play naturally exploits the specific USSR pattern their lineage shares.

**Supporting evidence:**
- v21 as USSR has the second-lowest average USSR WR across all models (0.616, only v22 is lower at 0.612)
- v22 as USSR has the lowest average USSR WR (0.612)
- v21's USSR is specifically weak against v22 (0.480) AND v22's USSR is weak against v21 (0.469) -- both below their averages
- The adjacent pair avg US WR has been trending: v19/v20=0.331, v20/v21=0.322, then v21/v22=0.525 (sudden jump)
- v20's ELO actually regressed (2088 vs v19's 2094), suggesting v20 may be the origin of a weakness that propagated

**Verdict:** Strong hypothesis. The lineage bottleneck creates correlated USSR weaknesses that each model's US can exploit because they share similar US-side strategies.

### H3: Rollout-temp 1.2 made v22's USSR weaker
**FACTUAL CORRECTION:** The autonomous_decisions.log line 937 clearly states: "Added --rollout-temp 1.2 ... Both changes take effect starting v23." Line 930 shows v22's launch command without --rollout-temp. **v22 did NOT use rollout-temp 1.2.**

**Verdict:** Eliminated. v22 used identical training hyperparameters to v21 (both without rollout-temp).

### H4: Pure noise at n=50
**Mechanism:** With SE=0.071, a true US WR of 0.44 has a 14% chance of producing an observation >= 0.52. Seeing this in both directions has ~2% probability if the true rate is 0.44.

**Evaluation:** Not negligible but not highly probable either. More importantly, we see this pattern in exactly 1 of 45 pairs, which is consistent with it being the most extreme instance of a real but moderate effect (true rate ~0.45) amplified by noise.

**Verdict:** Noise contributes but cannot fully explain a pattern that is unique to this one pair.

### H5: Fixture stagnation amplifying co-adaptation
**Mechanism:** Both v21 and v22 trained with league fixtures v4/v8/v12 (per line 930). These fixtures are 50-90 Elo below the frontier by this era, providing little meaningful resistance. The league-mix-k=4 means at most 4 opponents are sampled, and with old fixtures, the effective opponent diversity is low.

**Supporting evidence:**
- ppo_loop_step.sh line 20 notes fixtures were updated to v8/v14/v19 precisely because "v4/v8/v12 were 50-90 Elo below frontier by v22 era"
- Low fixture diversity means both v21 and v22 primarily learned to beat each other's predecessors, not to defend against diverse US strategies

**Verdict:** Contributing factor. Weak fixtures reduce the pressure to maintain robust USSR defense.

### H6: Elo system overestimates progress due to co-adaptation
**Mechanism:** If frontier models are increasingly co-adapted (sharing weaknesses), they may beat their predecessors easily while having blind spots that an out-of-distribution opponent could exploit.

**Evaluation:** The Elo system uses round-robin across ALL models (heuristic + v13 through v22), not just adjacent pairs. The v21/v22 mutual matchup contributes only 400 out of thousands of total games. The Elo ratings are therefore NOT dominated by this co-adaptation effect. However, the narrowing Elo gaps (v18=2088, v19=2094, v20=2088, v21=2092, v22=2109) do suggest diminishing returns from the current lineage approach.

**Verdict:** Minor Elo inflation risk from this specific effect. The broader plateau concern is real but stems from training methodology, not Elo measurement.

## Most Likely Explanation

The anomaly is caused by **shared USSR fragility in the v20-v22 lineage**, amplified by **sampling noise** at n=50.

The mechanistic chain:
1. v20 regressed from v19 (Elo 2088 vs 2094), likely developing a USSR weakness that the training loop did not correct because its eval-opponent (v19) did not specifically stress-test that weakness.
2. v21 inherited v20's weights and trained against v20 as eval-opponent. It improved overall but inherited the same USSR blind spot, since beating v20 did not require fixing it.
3. v22 inherited v21's weights and trained against v21. Same dynamic: the inherited USSR weakness persisted.
4. Both models' US strategies are optimized for the same lineage of opponents, so they naturally exploit the specific USSR patterns their shared ancestry is weak at.
5. The true mutual US WR is likely ~0.44-0.47 (significantly above the 0.37 frontier average, but below 0.50). Sampling noise at n=50 (SE=0.07) pushed both observed values above 0.50.

The key evidence: v21 has the second-lowest average USSR WR (0.616) and v22 has the lowest (0.612) across all models in the tournament, despite being the highest-Elo models. This confirms their USSR play is their weakest link.

The factual correction about rollout-temp 1.2 (NOT used by v22) eliminates what seemed like a plausible mechanism and strengthens the co-adaptation hypothesis: v21 and v22 are nearly identical in training methodology, differing only in 200 PPO iterations. They are essentially the same policy with a slight perturbation, so symmetric behavior is expected.

## Implications for Training and Plateau Assessment

### Is progress real?
Yes. v22's Elo of 2109 vs v19's 2094 represents genuine improvement against the full field (including older models and heuristic). The co-adaptation effect between v21 and v22 contributes only marginally to Elo calculations because the round-robin includes 10+ opponents.

### Is there a plateau?
Partially. The Elo trend shows clear deceleration:
- v14: 2031 (+30 from v13)
- v15: 2068 (+37)
- v16: 2074 (+6)
- v17: 2080 (+6)
- v18: 2088 (+8)
- v19: 2094 (+6)
- v20: 2088 (-6, regression)
- v21: 2092 (+4)
- v22: 2109 (+17)

v22's jump is encouraging but the v16-v21 stretch shows 6-8 Elo per generation with one regression. The diminishing returns are real and stem from:
- Single-lineage training (no population diversity)
- Stale fixtures (v4/v8/v12 are too weak to provide meaningful feedback)
- No explicit USSR-defense pressure

### Does Elo overestimate these models?
Not substantially. An out-of-lineage anchor opponent would provide a useful cross-check. If an independently-trained model (or human games) revealed that v22's USSR was weaker than its Elo implies, that would confirm the co-adaptation concern. Currently the signal is suggestive but not definitive.

### The USSR weakness is the real finding
More important than the US symmetry anomaly itself: v21 and v22 are the strongest models overall but have the WEAKEST USSR play in the tournament. This suggests the training loop is improving US play faster than USSR play, creating a lopsided policy. Since USSR has a natural advantage (0.64 WR baseline), any erosion of USSR skill costs more than equivalent US improvement gains.

## Recommendations

1. **Increase per-side sample size to n=100** for frontier matchups (v20+). This halves the SE from 0.07 to 0.05 and would clearly distinguish a true 0.45 US WR from 0.50. Cost: one extra tournament run.

2. **Add an out-of-lineage anchor model.** Train a separate model from v15 or v16 (the strongest pre-plateau checkpoint) with a different random seed or different data mix. Use it as a permanent fixture. If frontier models do well against lineage neighbors but poorly against this anchor, co-adaptation is confirmed.

3. **Add explicit USSR-defense training pressure.** Options:
   - Add a per-side win rate metric to the eval loop and flag when USSR WR drops below threshold
   - Include USSR-heavy rollout games (force the learner to play USSR more often against strong US opponents)
   - Use asymmetric league: sample the learner's weaker side more often for rollouts

4. **Update fixtures immediately** (already planned for v23: v8/v14/v19). This is the highest-impact change for reducing co-adaptation.

5. **Track per-side Elo separately.** Instead of one Elo per model, compute USSR-Elo and US-Elo. This would immediately surface the pattern: v21/v22 would show high USSR-Elo (because they beat weaker models as USSR) but the gap between their overall Elo and their US-Elo would be smaller than earlier generations.

6. **Do not over-react to the 0.52-0.53 numbers.** They are within noise of 0.45, which is high but not unprecedented (v18/v19 averaged 0.445 in both directions). The broader USSR weakness trend is more important than this specific pair.

## Conclusions

The v21/v22 US symmetry anomaly is a real but statistically modest signal (true mutual US WR likely ~0.45, inflated to ~0.52 by sampling noise). It arises from shared USSR fragility in a single-lineage training pipeline with stale fixtures. It is the most visible symptom of a broader issue: the v16-v22 era models are improving US play while their USSR play stagnates or slightly declines.

The Elo system is not meaningfully inflated by this effect because it uses full round-robin, but the underlying co-adaptation concern is valid and should be addressed through fixture updates (already planned), out-of-lineage anchors, and explicit per-side training pressure.

A critical factual correction: v22 did NOT use rollout-temp 1.2. That change takes effect starting v23 (per autonomous_decisions.log line 937). This eliminates the temperature-noise hypothesis and strengthens the shared-lineage explanation.

## Open Questions

1. Does v23 (with rollout-temp 1.2 and updated fixtures v8/v14/v19) show improved USSR WR vs v21/v22? This would confirm the fixture-stagnation hypothesis.
2. Would a model trained from v16 with a different seed be a useful out-of-lineage anchor?
3. Is the USSR weakness specific to certain card plays (e.g., headline decisions, coup targets) or is it diffuse across many actions? Card-level analysis of v21/v22 USSR losses could reveal specific tactical gaps.
4. Should the league-mix-k parameter be increased from 4 to 6+ to provide more opponent diversity per training iteration?
5. At what point does the single-lineage approach hit diminishing returns hard enough to justify population-based training (multiple independent lineages merged periodically)?
