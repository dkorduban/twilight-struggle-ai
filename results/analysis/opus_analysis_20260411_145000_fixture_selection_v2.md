# Fixture Selection v2: Per-Side Pools for PPO League Training

**Date:** 2026-04-11
**Author:** Claude Opus (deep analysis agent)

## Executive Summary

The current fixture selection algorithm selects a single combined pool of 16 models using 2D Pareto-front seeding in (elo_ussr, elo_us) space, followed by greedy max-min JSD diversification. This design has four problems: (1) near-duplicate models waste Pareto slots (v46/v54 differ by JSD=0.005), (2) strong models like v22 (Elo #9) are excluded, (3) very weak models (v9/v10, Elo ~1953) are included for diversity but provide no strength challenge, and (4) the single-pool design ignores the two-pool architecture already implemented in `train_ppo.py`.

The PPO training loop already selects opponents independently for USSR and US pools via per-side UCB-PFSP weights (`sample_K_league_opponents(..., side="ussr")` and `side="us"`). Fixture selection should match this structure: select K models for the USSR opponent pool (ranked by elo_ussr) and K models for the US opponent pool (ranked by elo_us), with greedy JSD deduplication within each pool.

**Key finding:** Consecutive PPO generations are almost always near-duplicates (JSD < 0.008 for 18 adjacent pairs). Any selection algorithm that does not explicitly deduplicate will waste slots on redundant models. A minimum JSD threshold of 0.010 is recommended.

**Recommended pools (8 models each + heuristic):**

- **USSR pool** (opponents when self plays US): v45, v15, v58, v18, v20, v16, v21, v49 + heuristic
- **US pool** (opponents when self plays USSR): v55, v48, v19, v21, v22, v20, v58, v45 + heuristic
- **Overlap:** v20, v21, v45, v58 (4 models in both pools)
- **Total unique models:** 12 + heuristic

## Analysis

### Problem 1: Near-Duplicate Pollution

Consecutive PPO generations (vN, vN+1) are almost always near-duplicates. All 18 pairs below have combined JSD < 0.008:

| Pair | JSD | elo_ussr gap | elo_us gap |
|------|-----|-------------|-----------|
| v46-v54 | 0.0051 | 0.6 | 0.7 |
| v47-v48 | 0.0045 | 1.6 | 2.5 |
| v48-v49 | 0.0047 | 12.0 | 16.5 |
| v56-v57 | 0.0038 | 11.3 | 17.3 |
| v57-v58 | 0.0040 | 15.0 | 35.8 |
| v51-v52 | 0.0037 | 10.5 | 26.0 |
| v22-v44 | 0.0061 | 7.2 | 12.4 |
| v44-v45 | 0.0067 | 32.1 | -34.0 |

The v46/v54 Pareto problem is a direct consequence: both models are nearly identical (JSD=0.005) but happen to have infinitesimally different elo_ussr/elo_us values (0.55/0.73 Elo difference), creating an artificial Pareto front with two wasted slots.

**Fix:** Before any selection, deduplicate by merging models within JSD < 0.010, keeping the one with higher Elo for the relevant side. This prevents near-duplicates from ever reaching the selection algorithm.

### Problem 2: Pareto Front Is the Wrong Seed for Per-Side Selection

The 2D Pareto front in (elo_ussr, elo_us) space finds models that are not dominated in *both* dimensions. But for per-side pools, only one dimension matters:

- USSR pool: rank by elo_ussr only
- US pool: rank by elo_us only

The Pareto front adds v46 and v54 (both elo_ussr ~2119) but misses v22 (elo_ussr=2095, elo_us=2030) -- the 9th strongest model that falls in a gap between v19 (elo=2072) and the top cluster. v22 is not on the Pareto front because v44 weakly dominates it (elo_ussr: 2102>2095, elo_us: 2042>2030), but v22 is behaviorally distinct from v44 (JSD=0.006) and fills a real strength/behavior gap.

**Fix:** Replace Pareto seeding with top-K seeding per side. For the USSR pool, seed with the top 2-3 models by elo_ussr (after deduplication). For US pool, seed with top 2-3 by elo_us.

### Problem 3: Weak Models Waste Slots

v9/v10 (Elo ~1953) are 170+ Elo below the top models. They are included because they are maximally JSD-distant from the top cluster (~0.08+ combined JSD). But:

- They provide no strength challenge for a model at Elo 2120+
- They were included over v22 (Elo 2096), which is much more useful
- The heuristic (Elo 1751) already serves as the weak-opponent anchor

With per-side selection and Elo cutoffs, weak models are naturally excluded:
- USSR pool: cutoff at elo_ussr >= 2060 (keeps 19 candidates)
- US pool: cutoff at elo_us >= 1980 (keeps 16 candidates)

### Problem 4: Single-Pool vs Two-Pool Architecture Mismatch

The PPO training loop (`train_ppo.py:1298-1313`) already implements independent per-side pools:

```python
ussr_opps = sample_K_league_opponents(league_dir, k_per_side, side="ussr", ...)
us_opps   = sample_K_league_opponents(league_dir, k_per_side, side="us",   ...)
```

But the fixture list fed via `--league-fixtures` is a single flat list used by both pools. The UCB-PFSP weighting handles per-side differentiation at runtime, but the initial fixture set should already be optimized per side.

**Why this matters:** When the learner plays US, it faces opponents from the USSR pool. These opponents should be strong USSR players (high elo_ussr). When the learner plays USSR, it faces opponents from the US pool. These should be strong US players (high elo_us). A combined pool conflates these requirements.

### The Two-Pool Algorithm

**Inputs:** JSD matrix, Elo ladder, `pool_n` (per-side target), `min_jsd` (dedup threshold, default 0.010)

**Per-side selection (run independently for USSR and US):**

1. **Filter:** Keep models with `elo_{side}` >= cutoff and present in JSD matrix + scripted dir
2. **Deduplicate:** For each pair with combined JSD < `min_jsd`, remove the one with lower `elo_{side}`
3. **Seed:** Take top-1 by `elo_{side}` as initial set
4. **Greedy max-min JSD:** Repeatedly add the candidate maximizing min combined JSD distance to current set
5. **Stop** at `pool_n` models

**Heuristic handling:** Always append `__heuristic__` to both pools. The heuristic serves as a floor-strength anchor and PFSP naturally upweights it when the learner is struggling.

**Self-slot:** Handled separately in `train_ppo.py`, not part of fixture selection.

**Should pools overlap?** Yes, naturally. A model strong at both USSR and US (like v55) will appear in both pools. The algorithm does not force or prevent overlap -- it emerges from the data. In our simulation, 4 of 8 models overlap, which is healthy.

### Recommended Pool Composition

#### USSR Pool (8 models + heuristic)

When the learner plays US, these opponents play USSR against it. Selected to maximize elo_ussr diversity.

| Model | elo_ussr | elo_us | min_jsd_in_pool | Role |
|-------|----------|--------|----------------|------|
| v45 | 2134.0 | 2008.0 | 0.034 | Strongest USSR, high asymmetry |
| v21 | 2102.4 | 1989.7 | 0.030 | Strong USSR, distinct early-gen style |
| v20 | 2103.8 | 1986.0 | 0.030 | Near v21 Elo but distinct (JSD=0.030) |
| v18 | 2083.1 | 1945.5 | 0.035 | Very high asymmetry, old-style policy |
| v15 | 2083.2 | 1957.2 | 0.031 | Oldest strong USSR, maximally different |
| v16 | 2066.7 | 1948.4 | 0.031 | Fills gap between v15 and v18 |
| v58 | 2067.1 | 1983.6 | 0.029 | Recent gen, moderate asymmetry |
| v49 | 2078.6 | 2028.4 | 0.029 | Balanced model, late-gen style |

**Notable exclusions:**
- v46, v54: Near-duplicates of v45 (JSD ~0.005-0.007), lower elo_ussr
- v55: elo_ussr=2117 but JSD=0.024 from v45; appears in US pool instead
- v44: Near-duplicate of v22 (JSD=0.006); v22 excluded from USSR pool because elo_ussr=2095 is below several candidates

#### US Pool (8 models + heuristic)

When the learner plays USSR, these opponents play US against it. Selected to maximize elo_us diversity.

| Model | elo_us | elo_ussr | min_jsd_in_pool | Role |
|-------|--------|----------|----------------|------|
| v55 | 2064.6 | 2117.2 | 0.015 | Strongest US by far (+20 over #2) |
| v48 | 2044.9 | 2090.6 | 0.015 | 2nd strongest US, recent gen |
| v22 | 2029.6 | 2094.7 | 0.014 | Strong US, distinct from v44 cluster |
| v21 | 1989.7 | 2102.4 | 0.030 | Mid-tier US, high USSR asymmetry |
| v20 | 1986.0 | 2103.8 | 0.028 | Distinct from v21 (JSD=0.030) |
| v19 | 2007.0 | 2068.1 | 0.028 | Early gen, different policy |
| v58 | 1983.6 | 2067.1 | 0.019 | Recent gen, fills JSD gap |
| v45 | 2008.0 | 2134.0 | 0.014 | Different style despite lower US Elo |

**Notable inclusions:**
- v22: Now included (was absent from v1 selection). 9th overall by Elo, fills the gap between v19 and top cluster.
- v48: Included for US strength (2nd highest elo_us) -- was not in v1 selection.

**Notable exclusions:**
- v46, v54: Near-duplicates of each other (JSD=0.005) and v45 (JSD~0.006); v55 dominates both on elo_us
- v44: Near-duplicate of v22 (JSD=0.006); v22 preferred for better JSD diversity
- v47: Near-duplicate of v48 (JSD=0.005)

### JSD Metric: Should Country JSD Get Higher Weight?

The current combined metric weights all three heads equally: `combined = (card_jsd + mode_jsd + country_jsd) / 3`.

**Argument for asymmetric weighting:** USSR play involves more influence operations (coups in battlegrounds, realignments). Country-head JSD might capture more meaningful behavioral variation for the USSR pool. US play is more card-efficiency focused.

**Counter-argument:** The JSD matrix already captures policy differences. Card-head JSD is the most informative single metric (directly captures what card is played). Country-head JSD captures *where* influence goes. Mode-head JSD is the least informative (only 4 modes).

**Recommendation:** Keep equal weighting for now. The combined metric already produces good diversity. If future analysis shows that USSR opponents are too similar in influence patterns, increase country_jsd weight to 0.4 for USSR pool (card=0.4, mode=0.1, country=0.5). But this is a second-order effect.

### Proposed CLI Changes

```
--pool-n N              Target models per side pool (default: 8)
--ussr-pool-n N         Override for USSR pool (default: --pool-n)
--us-pool-n N           Override for US pool (default: --pool-n)
--min-jsd FLOAT         Dedup threshold (default: 0.010)
--elo-ussr-cutoff FLOAT Min elo_ussr for USSR pool candidates (default: 2060)
--elo-us-cutoff FLOAT   Min elo_us for US pool candidates (default: 1980)
```

Output format change: instead of a single `--league-fixtures` list, output two lists:
```
--league-fixtures-ussr path1 path2 ... __heuristic__
--league-fixtures-us   path1 path2 ... __heuristic__
```

Or, if the training loop continues using a single `--league-fixtures` flag, output the union of both pools (12 unique models + heuristic). The per-side UCB-PFSP weighting will naturally favor the appropriate models for each side.

### Migration Path

**Phase 1 (immediate):** Update `select_league_fixtures.py` to use per-side greedy selection with deduplication. Output a single union list for backward compatibility with the current `--league-fixtures` flag. Also output per-side JSON for analysis.

**Phase 2 (later):** Add `--league-fixtures-ussr` / `--league-fixtures-us` flags to `train_ppo.py` so each pool can be explicitly configured. Until then, the UCB-PFSP weighting handles per-side differentiation at runtime.

## Conclusions

1. **Near-duplicate detection is essential.** 18 adjacent-generation pairs have JSD < 0.008. Without deduplication, the selection algorithm wastes slots on behaviorally identical models that happen to differ by 0.5 Elo.

2. **Per-side selection fixes the Pareto problem.** The 2D Pareto front is the wrong seeding strategy when pools are selected independently. Ranking by single-side Elo and greedy JSD diversification produces better pools.

3. **v22 should be included.** It is the 9th strongest model overall, has the 8th highest elo_us (2030), and is behaviorally distinct from its neighbors (JSD=0.006 from v44, 0.049 from v19). It fills a real strength gap.

4. **v9, v10, v8 should be excluded.** They are 170+ Elo below top models and provide no training signal beyond what heuristic already provides. Diversity for its own sake is not valuable when it comes at the cost of strength.

5. **v46 and v54 should not both be selected.** JSD=0.005 combined. Keep v45 (highest elo_ussr in the cluster) and v55 (highest elo_us). Drop v46, v54, and v44 as near-duplicates.

6. **Recommended union pool (12 + heuristic):** v45, v55, v48, v22, v21, v20, v19, v18, v16, v15, v58, v49, heuristic. This is 4 fewer models than the v1 selection but with better strength coverage and zero near-duplicate pairs.

7. **The two-pool design is architecturally correct.** The PPO loop already uses independent per-side UCB-PFSP. Fixture selection should match. Even before adding `--league-fixtures-ussr/us` flags, the union pool with per-side UCB weighting is strictly better than the v1 selection.
