---
# Opus Analysis: League Mix Ratio and Self-Play Fraction
Date: 2026-04-09T22:00:00Z
Question: Is ~25% self-play from league-mix-k=4 with 3 fixtures reasonable?

## Executive Summary

The initial estimate of ~25% self-play is incorrect. The actual sampling mechanism draws each of the K=4 opponent slots independently from a unified pool of past-self checkpoints + fixtures, with a 10% per-slot chance of heuristic. Because past-self checkpoints accumulate over training (1 at iter 1, then +1 every 10 iterations), past-self fraction grows from ~40% early to ~72% late in training, while fixture fraction shrinks from ~48% to ~16%. Over the full v23 run (200 iterations), the empirical breakdown was: 11.5% heuristic, 25.4% fixtures, 63.1% past-self. The problem is not too little self-play -- it is that early training is dominated by weak fixtures, and late training is dominated by stale past-self checkpoints from when the model was weaker.

## Findings

### 1. Sampling Mechanism (lines 794-816 of train_ppo.py)

The function `sample_K_league_opponents` works as follows:
- **Pool construction**: all `iter_*.pt` files in the league directory + all fixture paths. This is a flat list -- no weighting, no recency bias.
- **Per-slot sampling**: For each of K=4 slots independently:
  - 10% chance: heuristic (None)
  - 90% chance: uniform random from the full pool (fixtures + past-self combined)
- **Key insight**: Fixtures are NOT guaranteed slots. They are mixed into the same pool as past-self checkpoints. The 3 fixture paths (v8, v14, v19) compete uniformly with all iter_*.pt entries.

### 2. Pool Growth and Its Effect on Distribution

With `--league-save-every 10`, the pool grows as:
- Iter 1: pool = [iter_0001] + 3 fixtures = 4 entries. P(fixture per 90% slot) = 3/4 = 75%.
- Iter 10: pool = [iter_0001, iter_0010] + 3 fixtures = 5 entries. P(fixture) = 3/5 = 60%.
- Iter 50: pool = 6 checkpoints + 3 fixtures = 9 entries. P(fixture) = 3/9 = 33%.
- Iter 100: pool = 11 checkpoints + 3 fixtures = 14 entries. P(fixture) = 3/14 = 21%.
- Iter 200: pool = 21 checkpoints + 3 fixtures = 24 entries. P(fixture) = 3/24 = 12.5%.

### 3. Empirical Distribution from v23 Log (200 iterations, 800 slots)

| Phase | Heuristic | Fixtures | Past-Self |
|-------|-----------|----------|-----------|
| Early (1-50) | 12.5% | 47.5% | 40.0% |
| Mid (51-100) | 9.0% | 22.5% | 68.5% |
| Late (101-200) | 12.2% | 15.8% | 72.0% |
| **Overall** | **11.5%** | **25.4%** | **63.1%** |

v24 (only 6 iterations logged): 20.8% heuristic, 33.3% fixtures, 45.8% past-self.

### 4. Problems with the Current Distribution

**Problem A: No recency bias in past-self sampling.** At iteration 200, there are 21 past-self checkpoints spanning iter_0001 to iter_0200. The model plays against iter_0001 (its weakest version) just as often as iter_0200 (its strongest). This means most "self-play" games are against significantly weaker versions of itself, which provides easy wins but poor gradient signal.

**Problem B: Early training is fixture-dominated.** In the first 50 iterations, 47.5% of training is against fixtures (v8/v14/v19), which are 83-156 Elo below v22. The model learns to beat weak opponents rather than improve against challenging ones.

**Problem C: Heuristic fraction is hardcoded at 10%.** The 10% heuristic rate is reasonable as a floor but is not tunable via CLI args.

**Problem D: No current-self slot.** The model never plays against its current parameters (live self-play). It only plays against the most recently saved checkpoint, which could be up to 9 iterations old. True self-play (model vs copy of itself) would provide the strongest gradient signal for policy improvement.

### 5. Relevance to v23 Regression (v23=1733 vs v22=2109)

The regression is likely caused by a combination of factors, but the league mix contributes:
- Early iterations train heavily against fixtures 83-156 Elo below v22. This pulls the policy toward exploiting weak opponents rather than maintaining the strategies that made v22 strong.
- The uniform past-self sampling means 72% of late training is against checkpoints from throughout the run, many of which represent the already-regressed model. This creates a feedback loop where the model learns to beat its own degraded versions.
- There is no mechanism to prioritize training against strong opponents or to detect and halt regression.

## Conclusions

1. The 25% self-play estimate is wrong. Actual past-self fraction is ~63% overall, rising from ~40% early to ~72% late, because past-self checkpoints accumulate and dilute the fixture share.
2. The real issue is not the self-play fraction but (a) uniform sampling across all historical checkpoints with no recency weighting, (b) all non-heuristic opponents being substantially weaker than the starting model, and (c) no true current-self play.
3. Fixture-dominated early training (~48% of slots in first 50 iters) against opponents 83-156 Elo weaker is likely contributing to the v23 regression by rewarding weak-opponent exploitation.
4. The 10% heuristic rate is reasonable but should be configurable.
5. The pool construction is correct in principle (flat list + uniform sampling is simple and stable), but needs recency weighting to be effective past the first ~50 iterations.

## Recommendations

1. **Add recency-weighted sampling for past-self checkpoints.** Instead of uniform random from all iter_*.pt, weight recent checkpoints exponentially higher (e.g., P(iter_i) proportional to exp(i / tau) where tau controls recency half-life). This ensures the model mostly trains against near-current-strength versions of itself.
2. **Add a guaranteed current-self slot.** Reserve 1 of the K=4 slots for live self-play (model vs its own current parameters), not a stale checkpoint. This provides the strongest gradient signal. Implementation: pass `None`-as-self or export the model once and use it as both sides.
3. **Reduce fixture weight or gate it.** Either (a) cap fixtures to at most 1 of K slots, or (b) phase fixtures out after N iterations (e.g., stop including them after iter 50). Once the model is substantially stronger than fixtures, training against them provides diminishing returns.
4. **Make heuristic fraction a CLI arg** (`--league-heuristic-pct 0.10`) for easier tuning.
5. **For the immediate v24 run**: Consider `--league-mix-k 2` with the pool restricted to only the last 3-5 checkpoints plus heuristic (no old fixtures). This would maximize training signal from near-strength opponents and avoid the dilution problem.
6. **Add Elo-gated opponent selection (medium-term).** Track approximate Elo of each pool entry and preferentially sample opponents within a target Elo band (e.g., within 100 Elo of current model). This is the gold standard for league training in AlphaZero-style systems.

## Open Questions

1. Is the v23 regression primarily caused by the league mix, or are there other factors (learning rate, entropy coefficient, clip ratio) that are more impactful?
2. Would pure self-play (K=1, current model only) outperform the league at this stage, given that the model is already regressing?
3. What is the optimal `--league-save-every` frequency? Saving every 10 iterations means up to 9 iterations of staleness, which may be too coarse.
4. Should the league pool be pruned (e.g., remove checkpoints that are more than 200 Elo below current) to avoid training against very weak versions?
