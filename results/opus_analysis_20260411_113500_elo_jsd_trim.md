# Opus Analysis: Elo Board JSD Trimming
Date: 2026-04-11
Question: Can we trim the ELO board by removing JSD-close duplicates? Keeping best of each cluster only. Full square matrix replay not needed -- just sliding window of 50 ELO width?

## Executive Summary

Yes, the Elo ladder is heavily compressible. 34 models span only 373 Elo points, with a median consecutive gap of just 4.8 Elo -- well below the ~12-point CI width per model. A 50-Elo sliding window yields 4 natural clusters (13, 8, 9, 3 models each) plus the heuristic. Keeping 1-2 representatives per cluster (best + most stylistically distinct) would cut the fixture set from 34 to ~8-10 with negligible information loss for both Elo measurement and PPO training. JSD on a fixed probe set is useful as a secondary signal to pick within clusters, but head-to-head WR overlap is the more direct and already-available criterion. A full square matrix replay is not needed: a chain or star schedule through cluster representatives suffices.

## Findings

### Current fixture cost in PPO training

The fixture set costs are **not** in the Elo tournament (that is one-time and cached). The real cost is during PPO training:

- **34 fixtures** are passed via `--league-fixtures` with `--league-fixture-fadeout 999` (never fade).
- With `--league-mix-k 6`, each iteration samples 6 opponents from a combined pool of past-self checkpoints + fixtures.
- Fixtures collectively receive ~50% of the non-self sampling mass (the `0.5` factor in `fixture_each` weighting).
- PFSP exponent 2.0 concentrates on harder opponents, but with 34 fixtures the probability of hitting any specific fixture is ~1.5% per slot.

The cost of 34 fixtures is **not primarily wall-clock** (sampling is O(N) but trivially fast). The real costs are:

1. **Diluted training signal**: With 34 fixtures + growing past-self pool, each fixture gets very few games. PFSP needs ~20 games per opponent for stable WR estimates. At 6 slots/iter with ~3 fixture slots and 34 fixtures, a given fixture appears every ~11 iterations = ~33 games before WR stabilizes. This is marginal.
2. **Disk and management**: 34 TorchScript files at ~5MB each = 170MB. Not a bottleneck.
3. **Elo tournament cost**: Full round-robin of 34 models = 561 pairs x 400 games = 224,400 games. Already cached, but adding a new model requires 33 new matches = 13,200 games (~45 min on CPU). This is the main scaling concern.

### Elo distribution analysis

```
Cluster 1 (Elo ~2079-2124, 13 models): v55 v46 v54 v44 v45 v48 v47 v56 v22 v49 v57 v21 v20
Cluster 2 (Elo ~2036-2072,  8 models): v19 v50 v17 v58 v15 v18 v16 v59
Cluster 3 (Elo ~1977-2020,  9 models): v60 v14 v51 v12 v13 v53 v52 v61 v11
Cluster 4 (Elo ~1915-1953,  3 models): v10 v9 v8
Cluster 5 (Elo ~1751,       1 model):  heuristic
```

Key observations:
- **13 models** within a 45-Elo band at the top. Their 95% CI widths are ~12 Elo. Many of these are statistically indistinguishable.
- The median gap (4.8 Elo) is less than half the CI width (12 Elo). Most adjacent models cannot be distinguished by H2H results.
- v27-v41 already excluded (corrupted era), so the gap from v22 to v44 is real (different training lineage, but both land in Cluster 1).

### Is JSD the right metric?

**JSD is useful but secondary.** Here's why:

Pros of JSD:
- Directly measures policy divergence, which is what "functionally equivalent" means.
- Can detect two models with different Elo but identical policy (unlikely but possible with noisy Elo).
- Can detect two models with similar Elo but very different policies (style diversity worth preserving).
- Fast: 1000 probe positions x 2 forward passes per model pair = seconds on GPU.

Cons of JSD:
- Requires a fixed probe dataset (the spec at `.claude/plan/jsd-probe-eval.md` is designed but not yet built).
- JSD is head-specific: two models might have identical card policies but different value functions, or vice versa.
- It doesn't directly measure what matters for training: whether the opponent produces different game trajectories.

**Head-to-head WR is more direct for clustering.** Two models with 50/50 H2H are interchangeable as opponents. We already have the full 561-pair round-robin matrix. A simple criterion: if models A and B have H2H WR within 48-52% AND their Elo gap is < 20, they are duplicates.

**Recommended: use H2H WR overlap as primary, JSD as tiebreaker.** Within an H2H-equivalent cluster, keep the model with highest JSD from the cluster's best model (maximizes diversity).

### Sliding window of 50 Elo: design

A "50 Elo window" around the current training model makes sense in principle. Models far below provide no gradient signal (too easy); models far above are too hard for meaningful learning.

However, the current Elo range is only 373 points, and 50 Elo corresponds to ~57% expected WR. This means:
- A model at Elo 2100 would only face opponents at 2050-2150. Currently that's still ~15 models.
- The heuristic (Elo 1751) would be dropped immediately. But it's a valuable diversity anchor.
- v8-v10 (Elo 1915-1953) would be dropped for any model above 2003. But weak opponents serve as "gradient health checks" (if WR vs v8 drops, something is wrong).

**A fixed sliding window is too aggressive.** Better: keep a sparse ladder with guaranteed coverage:
- 1 model per ~75-100 Elo band (ensures every band is represented)
- Always keep heuristic (floor reference)
- Always keep current strongest (ceiling reference)
- PFSP naturally downweights easy opponents anyway

### What would a JSD probe dataset look like?

The spec at `.claude/plan/jsd-probe-eval.md` describes exactly this:
- 1000 positions stratified by turn/side/DEFCON/VP
- Sourced from `data/ppo_rollout_combined` parquet
- Columns: influence, cards, scalars, card_mask, mode_mask, raw_turn, side_int, raw_defcon, raw_vp
- Created once by `scripts/build_probe_set.py`, immutable thereafter

This is sufficient for JSD clustering. The spec is ready to implement.

### Risks of pruning

1. **Elo collapse**: Removing models removes comparison paths. BayesElo needs a connected graph. Mitigation: keep chain connectivity (if you remove B between A and C, ensure A-C match exists).
2. **Lost diversity**: Two models at the same Elo might play very differently (e.g., aggressive USSR vs defensive USSR). JSD can detect this. Mitigation: use JSD as a diversity check before pruning.
3. **Losing diagnostic value**: Weak models (v8, v9) are useful for detecting regressions. If a new model suddenly loses to v8, that's a signal. Mitigation: keep at least one model per Elo band.
4. **Stale WR estimates**: With fewer fixtures, each gets more games per iteration = faster PFSP convergence. This is actually a benefit.

## Conclusions

1. The Elo ladder has massive redundancy: 34 models in 373 Elo points with median gap 4.8 (below the 12-point CI). At least 20 models are statistically indistinguishable from their neighbors.

2. A 50-Elo sliding window is directionally correct but too narrow for a 373-Elo range. A "sparse ladder" of 8-10 representatives with ~40-75 Elo spacing is better.

3. JSD is not needed for the initial pruning -- the existing H2H round-robin matrix already identifies duplicates (48-52% WR pairs). JSD adds value as a secondary diversity check within equivalent-Elo clusters.

4. The main cost of too many fixtures is not wall-clock but diluted PFSP signal: each fixture gets too few games for stable WR estimates, making PFSP weighting noisy.

5. Full round-robin replay is not needed for the pruned set. A chain schedule through the 8-10 representatives + the full cached matrix provides sufficient connectivity.

6. Recommended pruned fixture set (8 models + heuristic = 9 total):
   - heuristic (1751) -- floor anchor
   - v8 (1915) -- weakest learned model, regression canary
   - v11 (1977) -- low tier
   - v14 (2015) -- anchor model, mid tier
   - v16 (2044) -- lower-mid tier
   - v19 (2072) -- upper-mid tier
   - v22 (2096) -- strong, different lineage
   - v55 (2124) -- strongest overall
   - v46 or v54 (2108) -- second-strongest cluster, diversity pick (use JSD to choose)

7. Adding new models to Elo only requires 8-9 matches (vs representatives) instead of 33, saving ~70% of tournament compute.

## Recommendations

1. **Immediate (no code needed)**: Edit `ppo_loop_step.sh` to use a curated 9-fixture list instead of all 34. This requires changing the fixture-building loop to a hardcoded list. Expected effect: each fixture gets ~3.7x more games per iteration, PFSP converges faster.

2. **Build the JSD probe set** (spec exists at `.claude/plan/jsd-probe-eval.md`): implement `build_probe_set.py` and `ProbeEvaluator`. Then run JSD between all models in the top cluster (v44-v56) to pick the most diverse pair to keep.

3. **Add a `--fixture-preset` option** to `ppo_loop_step.sh` with presets like `sparse9` (the 9-model set above) and `full` (current 34-model set). Default to `sparse9`.

4. **For future Elo tournaments**: Switch from round-robin to chain-through-representatives. New model plays only vs the 9 representatives + 1-2 bracketing models. Total: 10-11 matches vs 33.

5. **Keep the full round-robin cache**: Never delete `results/matches/`. The cached 561-pair matrix is valuable for retrospective analysis even after pruning the active fixture set.

6. **Monitor for pruning-induced blind spots**: After switching to sparse fixtures, watch for cases where a new model beats all sparse fixtures but loses to a pruned model. Periodically (every 5 generations) run a spot-check vs 2-3 pruned models.

## Open Questions

1. Should we keep v46 or v54 as the diversity pick in the top cluster? JSD will answer this once the probe set is built.
2. Is `--league-fixture-fadeout 999` still the right setting, or should fixtures fade after some iterations to give more weight to past-self play?
3. The corrupted-era models (v27-v41) are excluded from both Elo and fixtures. Should any be reinstated as "adversarial diversity" opponents, or is their training corruption a permanent disqualifier?
4. Would an adaptive scheme work better: start with 9 fixtures, add back models whose PFSP weight exceeds a threshold (indicating the model struggles against them)?
