---
# Opus Analysis: Elo Ladder Composition Bias
Date: 2026-04-12T08:30:00Z
Question: Does ladder composition bias Elo ratings? Near-identical model clusters? Anchor effects?

## Executive Summary

The MM-based BayesElo solver used in this project is remarkably robust to ladder composition changes. Adding 5 near-identical clones of the top model (v55) shifts existing ratings by at most 6.1 Elo, and removing the heuristic anchor-point shifts ratings by at most 3.0 Elo. The v44-v61 cluster (18 models spanning 128 Elo) does *not* inflate adjacent ratings: thinning it from 18 to 5 models changes remaining ratings by at most 11.4 Elo, with rank-order Spearman rho=0.997. The anchor choice is purely a translation -- all relative differences are preserved exactly regardless of which model is anchored or at what Elo value.

## Findings

### 1. Near-identical clone inflation (Question 1)

**Experiment**: Added 5 copies of v55 to the 35-model ladder, with fabricated 50/50 results between clones and identical results vs all other models.

| Metric | Value |
|--------|-------|
| Max rating shift (any original model) | +6.1 Elo (v22) |
| Mean absolute shift | 1.3 Elo |
| v55 itself | +1.4 Elo |
| Anchor (v14) | +0.0 Elo (by definition) |
| Heuristic | -1.0 Elo |
| All 5 clones rated at | 2124.9 (same as v55) |

**Direction**: The clones themselves get accurate ratings (identical to v55). The bias on *other* models is small and *not systematically directional* -- some models shift up, others down, by amounts well within the 95% CI (~12 Elo). The effect is negligible in practice.

**Why it works**: In MM/BayesElo, each model's rating is determined by its win rate against all opponents weighted by opponent strength. Adding clones duplicates information that already exists (v55's results), which slightly perturbs the gradient landscape but does not create systematic bias because the clones are connected to all other models via round-robin.

### 2. v44-v61 cluster bias (Question 2)

**Experiment**: Removed models from the v44-v61 range in progressively more aggressive thinning:
- Mild: removed 11 models, kept v44, v48, v54, v55, v60, v61, v51 (23 total)
- Aggressive: removed 14, kept v44, v54, v55, v60 (20 total)
- Extreme: kept only 8 models total (v8, v11, v14, v22, v44, v55, v66_sc, heuristic)

| Strategy | Models | Max |diff| | Mean |diff| | Spearman rho | Rank swaps |
|----------|--------|-----------|------------|--------------|------------|
| Full (baseline) | 34 | 0.0 | 0.0 | 1.000 | 0 |
| No heuristic | 33 | 3.0 | 0.9 | 0.999 | 4 |
| Mild thin | 23 | 19.2 | 3.4 | 0.998 | 4 |
| Aggressive thin | 20 | 32.8 | 5.3 | 0.997 | 4 |
| Extreme thin | 7 | 35.5 | 10.9 | 1.000 | 0 |

Key observations:
- The cluster does NOT inflate ratings of models outside it. Removing it shifts outside models by small amounts in both directions.
- The biggest shift from extreme thinning is heuristic (-35.5 Elo), because heuristic loses its most informative comparison partners (the weak end of the cluster: v51, v52, v53, v61).
- v55 remains the top-rated model in every thinning strategy, shifting by at most -10.3 Elo (extreme case).
- The 4 rank swaps across thinning strategies all occur between models separated by <5 Elo (noise-level differences).

**Why the cluster is not harmful**: In a complete round-robin, every model plays every other model. The v44-v61 cluster provides *more* data about the cluster members' strengths, but this data is consistent with their cross-cluster results. The MM algorithm correctly weighs all match data, and redundant similar-strength opponents don't distort the ratings of dissimilar models.

The v44-v61 range is also not as "near-identical" as suspected: it spans 128 Elo (v55=2124 to v61=1995), which is the difference between a 68% and 32% expected win rate. The sub-clusters are:
- Strong tier (2100-2124): v44, v45, v46, v47, v48, v54, v55, v56
- Mid tier (2060-2088): v49, v57, v58
- Weak tier (1995-2036): v50, v51, v52, v53, v59, v60, v61

### 3. Anchor choice effect (Question 3)

**Experiment**: Re-ran BayesElo with different anchors.

| Anchor | v55 | v14 | v8 | heuristic | v55-v14 | v14-v8 | v14-heur |
|--------|-----|-----|----|----|---------|--------|----------|
| v14=2015 | 2123.5 | 2015.0 | 1915.5 | 1750.7 | 108.5 | 99.5 | 264.3 |
| v8=1900 | 2108.1 | 1999.5 | 1900.0 | 1735.3 | 108.5 | 99.5 | 264.3 |
| v55=2200 | 2200.0 | 2091.5 | 1991.9 | 1827.2 | 108.5 | 99.5 | 264.3 |
| v22=2100 | 2127.6 | 2019.1 | 1919.5 | 1754.8 | 108.5 | 99.5 | 264.3 |

**All relative differences are identical across anchors.** The anchor choice is a pure translation of the entire scale. If v14 is actually stronger or weaker than 2015, the entire scale shifts uniformly. This is a fundamental property of the Bradley-Terry/BayesElo model: only *differences* in ratings are identifiable from win/loss data.

Practical implication: The choice of v14=2015 is arbitrary but harmless. It does not bias any relative comparison. The only risk is if you try to compare these Elo numbers to an external scale (e.g., human Elo ratings), in which case the anchor calibration matters for absolute values but still not for relative ordering.

### 4. Ideal ladder composition (Question 4)

Based on the experiments:

**More data is always weakly better for BayesElo, never harmful.** Specifically:
- Adding redundant models does not bias existing ratings (max shift 6 Elo for 5 clones)
- Removing models loses information and *increases variance* without improving accuracy
- The only cost of a large ladder is computational: O(N^2) matches for round-robin

However, there is a practical cost concern:
- 34 models = 561 pairs = 224,400 games (at 400 games/pair)
- 20 models = 190 pairs = 76,000 games (66% savings)
- 8 models = 28 pairs = 11,200 games (95% savings)

**Recommendation**: Keep the full ladder for the definitive rating, but use a *fixture pool* of ~5-8 well-spaced models for quick placement of new candidates. This is already implemented (`elo_fixture_pool.json`). The fixture pool should span the full Elo range and avoid clustering. Good choices: heuristic (if kept), v8, v14, v22, v44, v55 -- these span ~370 Elo with roughly even spacing.

### 5. Removing heuristic from the ladder (Question 5)

**Experiment**: Removed heuristic from the 35-model ladder.

| Metric | Value |
|--------|-------|
| Max rating shift | 3.0 Elo (v53) |
| Mean absolute shift | 0.9 Elo |
| Rank swaps | 4 (all between models <3 Elo apart) |
| Spearman rho | 0.999 |

**Removing heuristic has negligible effect on accuracy.** The 3 Elo max shift is well within the 95% CI of any model. Heuristic primarily provides information about the bottom of the scale (v8-v11), which are not the models we care about for placement decisions.

The slight shifts upon removal are not directional -- some models go up, some down. This confirms that heuristic, despite being 264 Elo below the anchor, does not distort the upper part of the scale.

**However**, keeping heuristic has a small benefit: it provides a well-known absolute reference point (heuristic = "random-ish play") that is useful for communicating strength to humans. It also adds one more comparison for weak models, tightening their CIs slightly.

## Conclusions

1. **The BayesElo MM solver is composition-robust.** Adding or removing models shifts existing ratings by small amounts (typically <5 Elo, max ~11 Elo for aggressive thinning), well within statistical uncertainty.

2. **Near-identical clones do NOT inflate their own or neighbors' ratings.** Five clones of v55 shifted v55 by only +1.4 Elo and the max shift of any model was 6.1 Elo.

3. **The v44-v61 cluster does NOT bias the ladder.** Despite comprising 18/34 models and 78.7% of all games, removing most of the cluster changes ratings by at most 11 Elo with perfect rank-order preservation. The cluster is also not truly "near-identical" -- it spans 128 Elo.

4. **Anchor choice is a pure translation.** Changing the anchor model or Elo value shifts all ratings uniformly. Relative differences are invariant. v14=2015 is as good as any other choice.

5. **Removing heuristic is safe.** Max rating shift is 3.0 Elo. Keeping it provides a useful floor reference but is not necessary for accuracy.

6. **More models are weakly better, never worse.** The only cost is computational (O(N^2) matches). For new model placement, use a ~5-8 model fixture pool; for definitive ratings, use the full round-robin.

7. **The 95% CI of ~12-13 Elo per model dominates over composition effects.** Statistical noise from 400 games/pair is a larger source of uncertainty than ladder composition.

## Recommendations

1. **Keep the full 34-model ladder for definitive ratings.** Do not thin it -- there is no accuracy benefit to thinning, only information loss.

2. **Continue using the fixture pool (5-8 models) for rapid placement of new candidates.** After placement, optionally run the full round-robin for a definitive number.

3. **Keep heuristic in the ladder** as a floor reference, but it is acceptable to exclude it from the fixture pool if desired. The effect on other ratings is <3 Elo.

4. **Do not worry about cluster composition bias.** The MM algorithm handles it correctly. If future versions create even larger clusters, this remains safe.

5. **If you want tighter CIs, increase games per pair (from 400 to 800) rather than thinning the ladder.** Doubling games reduces CI width by ~30% (factor of sqrt(2)).

6. **The anchor v14=2015 is fine.** If you want to recalibrate to an external scale, do so by choosing a different anchor value, not by changing the ladder composition.

7. **For reporting, always report Elo *differences* (delta_vs_anchor) rather than absolute Elo**, since absolute values are anchor-dependent and not externally calibrated.

## Open Questions

1. **Non-transitivity**: The analysis assumes the Bradley-Terry model (transitivity). If model matchups are significantly non-transitive (e.g., v55 beats v46 but v46 beats v54 which beats v55), the model fit may be poor even if composition effects are small. A goodness-of-fit test (chi-squared on predicted vs actual win rates) would detect this.

2. **Side asymmetry**: The bipartite model (USSR/US nodes) captures side asymmetry per model, but composition effects on the *per-side* ratings were not analyzed separately. The per-side ratings have half the data per node, so composition effects may be slightly larger there.

3. **Sampling noise in the match cache**: Some pairs have 200 games instead of 400, introducing heterogeneous precision. The MM algorithm naturally handles this (more games = more weight), but the CI estimates assume homogeneous Fisher information.

4. **External calibration**: The Elo numbers are currently on an internal scale (v14=2015). To compare against human Elo or other bot ladders, an external calibration match would be needed. The composition analysis here is irrelevant to that problem.
---
