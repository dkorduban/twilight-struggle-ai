---
# Opus Analysis: Relative Region Fraction as Training Metric
Date: 2026-04-09 UTC
Question: Would tracking relative region fraction vs opponent stabilize region stats?
---

## Executive Summary

The current "region fraction" metric (`stats/{phase}/{side}/region_{name}_frac`) measures the share of a side's influence-placement actions that target each region. It varies widely across benchmark runs because it captures only one side of a reactive two-player game: the learned model's placement depends heavily on where the opponent places, which differs between heuristic (fixed stage-based region weights) and model opponents. A "relative region fraction" (model's regional share minus opponent's) would be **moderately more stable** but still noisy, because it conflates strategic choice with forced reactions (e.g., defending Europe after opponent pressure). More useful alternatives exist: **net regional influence delta** (actual board-state outcome, not action counts) and **region control rate** (how often each region ends in Presence/Domination/Control). These are cheaper to compute, less noisy, and more directly tied to game outcomes. The recommendation is to keep absolute region fractions for debugging, add net influence delta and region control rates as primary tracking metrics, and skip relative region fraction as a standalone metric since it offers modest stability gains at the cost of added complexity.

## Current Region Metric: What It Measures and Why It Varies

### What it measures

In `train_ppo.py` (lines 1585-1618), region fraction is computed as:

```
region_frac(phase, side, region) = count(influence actions targeting region) / count(all influence actions)
```

Key properties:
- Only counts **influence placement** actions (mode_idx == 0). Coups, realignments, events, and space are excluded.
- Only counts the **first target country** of each placement action (line 1587: `targets[0]`), not the full allocation.
- Bucketed into three phases: early (T1-3), mid (T4-7), late (T8-10).
- Computed separately for USSR and US sides.
- Denominator is the total number of influence actions for that side+phase.

### Why it varies

1. **Opponent-reactive dynamics.** The learned model adapts to opponent behavior. Against a heuristic that weight Asia heavily early (weight 1.35), the model may over-invest in Asia defense. Against a model opponent with different priorities, the distribution shifts.

2. **Heuristic opponent has fixed regional weights.** The MinimalHybrid heuristic uses deterministic stage-based weights:
   - Early: Europe=0.85, Asia=1.35, MiddleEast=1.10, SE Asia=1.25
   - Mid: CentralAmerica=1.20, SouthAmerica=1.20
   - Late: Europe=1.10, SouthAmerica=1.20

   This means the opponent's "pull" on the learned model's placement decisions changes predictably by phase but is invariant across runs. The **model's** response still varies due to card draws.

3. **Card draw variance.** Which cards are drawn determines which regions are relevant (scoring cards, region-specific events like Decolonization, Brush War, etc.). With only ~50-100 games per stats sample, a few extra Africa Scoring draws can swing the Africa fraction by 5-10pp.

4. **First-target-only counting.** A 4-ops influence placement split across 3 countries in 2 regions is counted only for the first target's region. This adds noise unrelated to true strategic focus.

5. **Side asymmetry.** USSR and US have fundamentally different starting positions and card pools. Comparing their region fractions directly is misleading.

6. **Small sample sizes.** The stats rollout uses a small batch (typically 50 games per side), and only influence actions are counted, so each phase/side bucket may have only 50-200 actions.

## Relative Region Fraction: Definition and Properties

### Possible definitions

**Definition A — Action-based difference:**
```
relative_frac(phase, region) = model_region_frac(phase, region) - opponent_region_frac(phase, region)
```
Positive = model places more influence in this region than opponent does.

**Definition B — Influence-weighted difference:**
```
relative_inf(phase, region) = model_ops_in_region / model_total_ops - opponent_ops_in_region / opponent_total_ops
```
Weighted by actual ops points, not just action count.

**Definition C — Board-state-based:**
```
relative_presence(region) = model_controlled_countries(region) / total_countries(region) - opponent_controlled_countries(region) / total_countries(region)
```
Measures outcome, not process.

### Properties

- Sums to zero across regions (if both sides have the same total action count, which they approximately do).
- Sign indicates relative focus: positive = overweight vs opponent.
- Magnitude indicates degree of specialization gap.

## Stability Analysis

### Would relative region fraction be more stable?

**Moderately yes, with caveats.**

Arguments for improved stability:
- If both sides react to the same card draws and board state, their region fractions are positively correlated. Differencing removes the common card-draw component. Example: when Africa Scoring appears, both sides increase Africa ops — the difference is more stable than either absolute fraction.
- Against a fixed heuristic opponent, the opponent's region fractions are nearly constant (only card draws affect heuristic region priorities). So `relative = model - constant` has the same variance as the absolute model fraction.

Arguments against significant improvement:
- Against the heuristic, the opponent's fractions are ~constant, so differencing adds no stability. The instability is entirely in the model's behavior.
- Against model opponents (Elo tournament), both models have high variance, and the difference of two high-variance quantities has variance roughly equal to the sum of their variances minus twice their covariance. The covariance is positive (both react to same board) but may not be large enough to dominate.
- The fundamental noise source — card draws creating different strategic landscapes per game — affects both sides but not symmetrically. USSR and US card pools differ. The correlation may be modest.

**Estimated stability improvement: 10-25% variance reduction against model opponents, near-zero reduction against heuristic.**

## Alternative Metrics

### 1. Net regional influence delta (recommended)

```
net_inf_delta(region) = sum(model_influence in region) - sum(opponent_influence in region) at game end (or phase end)
```

Advantages:
- Measures actual board outcomes, not action selection noise.
- Already available from the state dict (`ussr_influence`, `us_influence` arrays).
- Normalizable by region size (number of countries).
- Much more stable than action fractions because it integrates over all actions including events, coups, and realignments.

### 2. Region control rate

```
control_rate(region) = fraction of games where model achieves Domination or Control in region
```

Advantages:
- Directly tied to VP scoring.
- Binary/ternary outcome reduces noise.
- Easy to interpret: "model dominates Asia in 45% of games."

### 3. Region VP contribution

```
region_vp(region) = average VP gained from region scoring cards
```

Advantages:
- Directly measures strategic success per region.
- Requires tracking scoring card resolutions (may need engine support).

### 4. Influence efficiency

```
efficiency(region) = net_influence_gained(region) / ops_spent_in_region
```

Advantages:
- Measures ROI of regional investment.
- Detects whether a model is "wasting" ops in a region it can't win.

## Diagnostic Value Assessment

### What region metrics can detect

1. **Geographic overspecialization.** If a model puts 60% of ops into Europe and ignores Africa/South America, it will lose to opponents who contest those cheap-VP regions.

2. **Side-specific weaknesses.** US should invest more in Central/South America late; USSR should secure Asia early. Deviation from these patterns signals training issues.

3. **Policy collapse / echo-chamber effects.** If self-play produces two models that both ignore Africa, neither gets punished — but both lose to any opponent that contests it. Region fractions can flag this.

4. **Opponent exploitation.** If the model adjusts its regional focus when facing different opponents, that's healthy adaptation. If it doesn't, it's ignoring opponent behavior.

### What region metrics cannot detect

- Whether the model is placing influence on the *right countries* within a region.
- Whether coups and realignments (excluded from current fracs) are strategically sound.
- Whether event plays affect regional balance (they're huge: Decolonization, De-Stalinization, etc.).

### Relative region fraction specifically

Diagnostic value is **low-to-moderate.** It tells you whether the model is more or less regionally focused than its opponent, but:
- Against a fixed heuristic, it's just "model frac minus constant" — adds no information.
- Against model opponents, the sign is somewhat arbitrary (which side is the "model" vs "opponent"?).
- It doesn't capture whether the relative focus is strategic or forced.

## Conclusions

1. **Region fraction instability is real and expected.** It stems from card-draw variance, opponent-reactive dynamics, small sample sizes, and first-target-only counting. This is not a bug — it reflects the game's strategic diversity.

2. **Relative region fraction would provide marginal stability gains** (~10-25% variance reduction against model opponents, near-zero against heuristic). The implementation cost is low, but the diagnostic benefit over absolute fractions is small.

3. **Board-state-based metrics are strictly better** for tracking regional performance. Net influence delta, region control rate, and region VP contribution measure outcomes rather than inputs, are less noisy, and are more directly actionable.

4. **The current region fraction metric has a counting flaw** (first-target-only) that should be fixed regardless of whether relative fractions are added.

5. **The real diagnostic gap is not absolute vs relative** — it's action-counting vs outcome-measuring. The project would benefit more from adding end-of-game regional outcome stats than from refining the existing action-based fractions.

## Recommendations

1. **Do not implement relative region fraction as a standalone metric.** The stability gain is too small to justify the conceptual overhead.

2. **Add net regional influence delta** as a primary diagnostic metric. Compute at game end (or phase boundaries): `sum(model_inf) - sum(opp_inf)` per region, normalized by region size. This is trivially extractable from the existing state dict.

3. **Add region control/domination rate** per game. Track what fraction of games end with the model achieving Presence, Domination, or Control in each region. This directly reflects scoring-relevant outcomes.

4. **Fix the first-target-only counting bug.** Weight by ops allocated to each region, not just first-target membership. This reduces noise in the existing metric at zero conceptual cost.

5. **Increase stats rollout sample size** from ~50 to 200+ games if compute allows. This alone would cut variance by ~4x and may resolve the "widely different" observation without any metric redesign.

6. **Keep absolute region fractions** as secondary/debugging metrics. They're useful for spotting gross policy errors (e.g., "model never places in Africa") even if noisy for trend-tracking.

## Open Questions

1. How much of the observed variance is from card draws vs model stochasticity vs opponent effects? A controlled experiment holding seed constant while varying opponent would quantify this.

2. Should region stats be computed at the game level (per-game region fracs, then averaged) rather than pooled across all games? Per-game computation would enable proper confidence intervals.

3. Would tracking region stats from the C++ engine's end-of-game state (which has full influence arrays) be cheaper than parsing rollout steps? The state dict already contains `ussr_influence` and `us_influence` arrays.

4. Are there existing W&B dashboards or alerts that would need updating if the metric schema changes?
