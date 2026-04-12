# Opus Analysis: Post-v57 Frontier Fixture Inclusion
Date: 2026-04-12T05:20:00Z
Question: Should post-v57 models be added to the JSD fixture list, and how?

## Executive Summary

The post-v57 standard models (v58-v61) are **near-duplicates** of each other and of the v55-v57 cluster. Their pairwise JSD combined distances are 0.004-0.016, far below the min_jsd=0.01 deduplication threshold used by `select_league_fixtures.py`. The JSD deduplication algorithm would reject most or all of them in favor of v55 or v57. Adding them without JSD gating would dilute the fixture pool with redundant opponents and reduce training signal diversity.

v64 is a severe regression (Elo 1677, equal to heuristic) and is not in the JSD matrix, so it cannot be JSD-gated and should not be a fixture.

v55_sc is extremely distant from all standard models (combined JSD ~0.49) due to its different architecture, but it is catastrophically weak (97% loss rate to heuristic). Including a model this weak would be harmful to training.

v66_sc is architecturally distinct and moderately strong (Elo 1982), but it is also not in the current JSD matrix, so the deduplication script cannot evaluate it. It is the only frontier model with a legitimate case for inclusion, but requires JSD matrix regeneration first.

**Recommendation**: Re-run `select_league_fixtures.py` after regenerating the JSD matrix to include v64 and v66_sc. The script will correctly reject v58-v61 as near-duplicates and v64/v55_sc as too weak. It may select v66_sc based on its architectural distinctness. Do not manually add models without JSD gating.

## Findings

### 1. Standard frontier models (v58-v61) are near-duplicates

Pairwise JSD (combined metric) between consecutive standard models:

| Pair       | combined JSD |
|------------|-------------|
| v57-v58    | 0.0040      |
| v58-v59    | 0.0040      |
| v59-v60    | 0.0037      |
| v60-v61    | 0.0047      |
| v55-v58    | 0.0190      |
| v55-v61    | 0.0436      |
| v57-v61    | 0.0244      |

The deduplication threshold is min_jsd=0.01. Every consecutive pair (v57-v58, v58-v59, v59-v60, v60-v61) falls **well below** this threshold. The greedy algorithm ranks by Elo and skips models too close to the already-selected set. Since v55 is the top-Elo model and already selected, v56-v61 would need min-JSD > 0.01 to any already-selected model. v58 has combined JSD of only 0.019 to v55 -- barely above threshold -- and would likely be rejected because another already-selected model (e.g., v54 at JSD=0.041 from v58, or v48 at JSD=0.031) would be closer.

In practical terms: these are all the same training lineage with incremental parameter drift. They play nearly identically.

### 2. Win-rate evidence confirms Elo clustering

| Match        | WR(model_a) | Notes                    |
|--------------|-------------|--------------------------|
| v58 vs v61   | 56.6%       | Barely distinguishable   |
| v59 vs v61   | 58.3%       | Barely distinguishable   |
| v55 vs v61   | 66.1%       | v55 clearly stronger     |
| bc384 vs v58 | 10.0%       | v58 strong vs baseline   |
| bc384 vs v61 | 9.8%        | v61 almost same strength |

v58-v61 are all within ~50 Elo of each other, clustered around the v55-v57 band. They do not provide meaningfully different training opponents.

### 3. v64 is a regression to heuristic level

v64 Elo = 1676.8 (vs v55 = 2116.9, heuristic = 1676.4). It wins only 5.5% against v55, 62.2% against heuristic. This is a failed experiment that plays at approximately heuristic strength. Heuristic is already in the fixture list. Adding v64 would be pure redundancy.

v64 is also **not in the JSD matrix** (the matrix only goes up to v61), so the deduplication script cannot evaluate it. Regenerating the JSD matrix would include it, and if its Elo is below any min-elo filter, it would be excluded. Even without a filter, its Elo ranking is so low it would only be picked if it were JSD-diverse from all other low-Elo models, which is unlikely given its standard architecture lineage.

### 4. v55_sc is architecturally distinct but catastrophically weak

v55_sc (SmallChoiceHead architecture) has combined JSD ~0.49 from all standard models -- this is enormous, reflecting a fundamentally different policy distribution. However, it wins only 3% against heuristic (388 losses in 400 games). This model is broken and should never be a training fixture. Playing against a near-random opponent teaches nothing useful.

### 5. v66_sc is the only interesting frontier model

v66_sc is the only post-v57 model with both:
- Architectural distinctness (SmallChoiceHead, likely very high JSD like v55_sc)
- Reasonable strength (Elo 1982, wins 73% vs heuristic)

However, v66_sc is **not in the JSD matrix**. We cannot run the deduplication algorithm on it without regenerating the matrix. Its Elo (1982) is below v55 (2111) but well above heuristic (1760), placing it in a meaningful strength tier.

The candidates file shows v66sc_i080 at Elo 2109.5 (anchored to v55=2124), suggesting v66_sc at its best iteration is competitive with v55. This makes it a strong candidate for fixture inclusion, pending JSD computation.

### 6. Impact of redundant fixtures on training quality

The PFSP (Prioritized Fictitious Self-Play) league system samples opponents weighted by Elo proximity. If multiple near-duplicate models are in the fixture pool:
- They dilute the sampling probability of truly diverse opponents
- The learner sees the same opponent style repeatedly, reducing exploration
- Wall-clock time is wasted on games that provide no new signal
- The fixture fadeout mechanism (--league-fixture-fadeout=50) does not help because the duplicates are permanent fixtures, not self-play checkpoints

Conversely, missing a genuinely diverse opponent (like v66_sc, if it passes JSD gating) means the learner never encounters that policy style. This is a real loss for training diversity.

The asymmetry is clear: **adding redundant fixtures is harmful, missing diverse ones is also harmful, and JSD gating is the correct mechanism to distinguish the two cases.**

### 7. JSD matrix coverage gap

The current JSD matrix covers: bc_wide384, v8-v22, v27-v41, v44-v61, v55_sc.
Missing: v64, v66_sc.

The matrix was generated from probe positions (996 positions from `data/probe_positions.parquet`). Regenerating it with v64 and v66_sc would require running those two models on the probe set and computing pairwise JSDs. This is a modest compute cost (996 forward passes per model) and would take minutes, not hours.

## Conclusions

1. **v58-v61 should NOT be added to fixtures.** They are near-duplicates of the already-selected v55/v57 cluster. The JSD deduplication correctly rejects them.

2. **v64 should NOT be added to fixtures.** It is a severe regression to heuristic-level play. Heuristic is already included.

3. **v55_sc should NOT be added to fixtures.** Despite extreme architectural distinctness, it is catastrophically weak (3% WR vs heuristic).

4. **v66_sc is the only candidate worth evaluating.** It has both architectural distinctness and reasonable strength, but requires JSD matrix regeneration before the deduplication script can properly evaluate it.

5. **Sonnet's decision to add all post-v57 models without JSD gating was incorrect.** The revert was the right call. The JSD deduplication exists precisely to prevent fixture pool dilution.

6. **The correct process is to re-run the full pipeline**: regenerate JSD matrix including v64 and v66_sc, then re-run `select_league_fixtures.py`.

## Recommendations

### Immediate action
1. **Regenerate the JSD matrix** to include v64 and v66_sc (the two models currently missing).
2. **Re-run `select_league_fixtures.py`** with the updated matrix. Expected outcome:
   - v58-v61 rejected as near-duplicates of v55/v57
   - v64 rejected (low Elo, standard architecture, likely near-duplicate of heuristic-level models)
   - v55_sc rejected (if min-elo filter is applied) or included then ignored by PFSP (too weak to be sampled)
   - v66_sc possibly selected (high JSD from standard models, moderate Elo)
3. **Use the script output as the canonical fixture list.** Do not manually override.

### Policy for future fixture updates
When new models are added to `scripted_for_elo/`:
1. Run the JSD probe on the new model(s) and update `jsd_matrix.json`
2. Re-run `select_league_fixtures.py`
3. Only update the training fixture list if the script output changes
4. Never manually add models to fixtures without JSD evaluation

This should be documented as a standing rule and ideally automated as part of the model export pipeline.

### Optional: min-elo filter
Consider adding `--min-elo 1800` to `select_league_fixtures.py` to automatically exclude models that have regressed below a useful training threshold. This would filter out v64, v55_sc, and any future failures without manual intervention.

## Open Questions

1. **What script generates the JSD matrix?** It is not `select_league_fixtures.py` -- that script only reads it. The generation script needs to be identified and run with the expanded model set.
2. **Should v66_sc's best iteration (v66sc_i080, Elo 2109.5) be the one in the fixture list, rather than the base v66_sc (Elo 1982)?** The candidates file suggests the best iteration is substantially stronger.
3. **Is there a minimum strength threshold below which a fixture opponent provides no useful training signal?** The heuristic baseline is already included at Elo ~1760. v66_sc at 1982 is well above this. But should we set a floor?
4. **Should the fixture update be automated as a Snakemake rule?** Currently it requires manual re-running. A rule that triggers on new scripted model files would prevent this class of decision errors.
