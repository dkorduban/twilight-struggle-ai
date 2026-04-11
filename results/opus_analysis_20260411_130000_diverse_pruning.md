# Opus Analysis: Diverse Fixture Pruning

Date: 2026-04-11
Question: Simple Pareto pruning in (elo_ussr, elo_us) space might kill strategic diversity. How do I get both pruned fixture count AND preserved diversity in the PPO league?

## Executive Summary

The current 34-model fixture set has heavy redundancy in the top tier (19 models between 2050-2125 Elo) but genuine diversity along two measurable axes: overall Elo (373-point spread) and side-asymmetry (41-178 USSR-US Elo gap). A pure Pareto front in (elo_ussr, elo_us) space would keep ~8-12 models but risks collapsing models from different training lineages (early-gen v8-v22 vs. late-gen v44-v61) that likely play differently despite similar Elo profiles.

**Key finding:** For PPO league training, three diversity axes matter and are cheaply measurable: (1) Elo tier, (2) side-asymmetry profile, and (3) training lineage/generation. A fourth axis -- behavioral/strategic diversity via JSD -- is theoretically valuable but expensive to implement and likely redundant with lineage diversity at the current 34-model scale.

**Recommendation:** Use a 3-axis stratified selection that keeps 12-16 models: 3-4 Elo tiers x 2-3 asymmetry bands x 2 lineage groups, with Pareto-front models as mandatory anchors and the rest filled by maximizing (elo_tier, asymmetry, lineage) coverage. This can be computed in <20 lines of Python. Defer JSD probes to a diagnostic tool rather than a pruning input.

## Findings

### What diversity axes actually matter for league PPO

In league self-play PPO, the training signal comes from gradient updates on games against opponents. The quality of that signal depends on:

1. **Strength calibration** (Elo tier): The learner needs opponents at various difficulty levels. Too-easy opponents produce trivial rollouts with no gradient signal. Too-hard opponents produce all-loss rollouts with sparse signal. The UCB-PFSP weighting already handles this by upweighting hard opponents -- but it needs a spread of difficulties to work with.

2. **Side-specific challenge** (asymmetry profile): A model with USSR-US gap of 178 (v17) and one with gap 41 (v50) present fundamentally different challenges. Against v17, the learner's US side faces extreme pressure while USSR coasts. Against v50, both sides are competitive. This directly shapes which side-specific strategies get trained. The current data shows clear bimodal structure: early-gen models (v8-v22) have high asymmetry (115-178), late-gen models (v44-v61) have low asymmetry (41-87), reflecting different training regimes.

3. **Training lineage** (generation proxy): Models from different training runs explore different strategy basins. v9-v22 are sequential PPO generations that likely share strategic DNA (each initialized from the prior). v44-v61 appear to be from a different training branch with consistently lower asymmetry. Even at identical Elo, these lineages likely differ in card-play patterns, regional priorities, and opening strategies.

4. **Behavioral strategy** (JSD-measurable): Two models at identical Elo and asymmetry could play completely differently (Europe-focused vs. Asia-focused). This is real but hard to measure without running JSD probes.

**The practical hierarchy is:** Elo tier >> side-asymmetry > lineage > behavioral JSD. The first three are free to compute from existing data. JSD requires model inference on probe positions.

### Pareto-front coverage of current data

Computing the Pareto front in (elo_ussr, elo_us) space:

The non-dominated models (no other model is better on BOTH axes) would be approximately:
- **v55** (2117 USSR, 2065 US) -- overall strongest, balanced
- **v45** (2134 USSR, 2008 US) -- strongest USSR
- **v17** (2108 USSR, 1950 US) -- extreme USSR specialist
- **v50** (2055 USSR, 2014 US) -- most balanced at high tier
- **v14** (2015 USSR, 1939 US) -- mid-tier anchor
- **v8** (1926 USSR, 1811 US) -- weak tier
- **heuristic** (1763 USSR, 1601 US) -- floor

That is ~7 models. Adding near-Pareto models (within ~30 Elo of the front) might bring it to 10-12. This misses:

- **v11** (2020 USSR, 1842 US): dominated by v45 but from a completely different training lineage
- **v52** (1997 USSR, 1917 US): similar Elo to v14 but different lineage and lower asymmetry
- **v48** (2091 USSR, 2045 US): close to v55 but different training branch

The concern is real: pure Pareto pruning would keep mostly one model per Elo tier and lose lineage diversity.

### Cheap behavioral diversity proxies (no JSD)

Several proxies for behavioral diversity are available without JSD implementation:

1. **Training lineage / version gap** (free): Models with version numbers far apart (v8 vs. v55) are more likely to play differently than adjacent versions (v47 vs. v48). Group models by lineage: early-gen (v8-v22), late-gen-A (v44-v50), late-gen-B (v51-v55), late-gen-C (v56-v61).

2. **Side-asymmetry as style proxy** (free): High-asymmetry models (>100 USSR-US gap) play fundamentally different strategies than balanced models (<60 gap). The asymmetry directly encodes strategic tendencies: USSR-tilted models likely over-invest in coups and DEFCON pressure; balanced models likely play more positionally.

3. **Match-matrix win-rate variance** (available from 1373 match files): If model A beats model B 70-30 but model C beats model B 55-45 at the same Elo, A and C likely exploit B differently. Compute the variance of win rates across common opponents as a diversity signal.

4. **Elo residual / intransitivity** (available): In a perfectly transitive Elo ladder, predicted outcomes match actual outcomes. Models with high Elo residuals (beat some opponents much better/worse than Elo predicts) have unusual strategies. This is computable from the existing match matrix.

5. **Generation index** (free): Simply the version number, as a coarse proxy. Adjacent versions are similar; distant versions are different.

**Cost comparison:**
- Lineage + asymmetry: 0 compute, 0 implementation
- Match-matrix variance: ~50 lines of Python, 0 GPU
- Elo residuals: ~30 lines of Python, 0 GPU
- JSD probes: ~300 lines of Python, GPU inference on 1000 positions per model pair

### JSD: cost vs. benefit

**Cost:**
- Implementation: ProbeEvaluator is already specced (jsd-probe-eval.md), ~300 lines
- Compute: For K models, need K*(K-1)/2 pairwise comparisons. At 34 models = 561 pairs x ~2 forward passes x 1000 positions = ~1.1M forward passes. On RTX 3050 at ~10K samples/sec = ~2 minutes. Manageable.
- Maintenance: Probe set needs to be representative and stable; adds another artifact to manage.

**Benefit:**
- Detects genuine strategic diversity that Elo/asymmetry/lineage miss
- Most useful when models from the SAME lineage have diverged (e.g., v44 and v48 both late-gen but different strategies)
- Diminishing returns: at 34 models, lineage + asymmetry likely captures 80%+ of strategic variance

**Verdict:** JSD is worth building as a diagnostic/monitoring tool (the spec is good), but NOT worth blocking fixture pruning on. Use the cheap proxies for pruning; use JSD for validation afterward. If JSD reveals that pruning killed diversity the cheap proxies missed, add it to the pruning loop later.

### Proposed algorithm

**Stratified Pareto Selection (SPS)** -- select K fixtures in 3 steps:

**Step 1: Define axes** (all free from existing data)
- `elo_tier`: quantile-bin overall Elo into T tiers (T=4: bottom, low-mid, high-mid, top)
- `asym_band`: bin USSR-US gap into B bands (B=2: low <80, high >=80)
- `lineage`: assign generation group (L=3: early v8-v22, mid v44-v50, late v51-v61)

**Step 2: Pareto anchors** (mandatory keeps)
- Compute Pareto front in (elo_ussr, elo_us). Keep all Pareto-optimal models (~7).

**Step 3: Diversity fill** (up to budget K)
- For each (tier, band, lineage) cell that has no Pareto anchor, pick the model closest to the cell centroid.
- If K budget remains, add models with highest Elo residual (intransitivity) or highest match-matrix win-rate variance.

**Concrete code sketch:**

```python
def select_diverse_fixtures(ratings: dict, K: int = 16) -> list[str]:
    import numpy as np
    
    models = []
    for name, r in ratings.items():
        models.append({
            'name': name,
            'elo': r['elo'],
            'elo_ussr': r['elo_ussr'],
            'elo_us': r['elo_us'],
            'asym': r['elo_ussr'] - r['elo_us'],
        })
    
    # Step 1: Pareto front (mandatory keeps)
    selected = set()
    for m in models:
        dominated = False
        for m2 in models:
            if m2['elo_ussr'] > m['elo_ussr'] and m2['elo_us'] > m['elo_us']:
                dominated = True; break
        if not dominated:
            selected.add(m['name'])
    
    # Step 2: Stratified fill
    elo_vals = [m['elo'] for m in models]
    elo_edges = np.quantile(elo_vals, [0, 0.25, 0.5, 0.75, 1.01])
    
    def tier(elo):
        for i in range(len(elo_edges)-1):
            if elo < elo_edges[i+1]: return i
        return len(elo_edges)-2
    
    def asym_band(asym):
        return 0 if asym < 80 else 1
    
    def lineage(name):
        if name == 'heuristic': return 0
        v = int(name[1:])
        if v <= 22: return 1
        if v <= 50: return 2
        return 3
    
    # Find empty (tier, band, lineage) cells and fill them
    cells = {}
    for m in models:
        cell = (tier(m['elo']), asym_band(m['asym']), lineage(m['name']))
        cells.setdefault(cell, []).append(m)
    
    for cell_key, cell_models in cells.items():
        if not any(m['name'] in selected for m in cell_models):
            # Pick model closest to cell centroid
            avg_elo = np.mean([m['elo'] for m in cell_models])
            best = min(cell_models, key=lambda m: abs(m['elo'] - avg_elo))
            selected.add(best['name'])
            if len(selected) >= K:
                break
    
    # Step 3: If still under K, add by Elo spread (fill gaps)
    remaining = sorted(
        [m for m in models if m['name'] not in selected],
        key=lambda m: min(abs(m['elo'] - s_m['elo']) 
                         for s_m in models if s_m['name'] in selected)
    )
    for m in reversed(remaining):  # most distant first
        if len(selected) >= K: break
        selected.add(m['name'])
    
    return sorted(selected)
```

This runs in microseconds, needs no GPU, and produces ~12-16 diverse fixtures.

**Integration point:** Add this as a function in `scripts/run_elo_tournament.py` or a standalone `scripts/select_league_fixtures.py`. Call it from `ppo_loop_step.sh` after the Elo ladder update, pipe the selected fixture paths into the training command.

## Conclusions

1. **Pure Pareto pruning is insufficient but a good starting point.** It correctly identifies the strength frontier (~7 models) but misses training-lineage and asymmetry diversity that matters for PPO signal quality.

2. **Three cheap axes capture most diversity that matters:** Elo tier, side-asymmetry band, and training lineage. These are all computable from existing `elo_full_ladder.json` with zero additional infrastructure.

3. **JSD probes are not needed for pruning** at the current 34-model scale. The lineage + asymmetry axes already separate models that play differently (early-gen high-asymmetry USSR-specialists vs. late-gen balanced models). JSD should be built as a diagnostic tool, not a pruning prerequisite.

4. **The right fixture count is 12-16**, not 7 (pure Pareto) or 34 (no pruning). This preserves 3-4 Elo tiers x 2 asymmetry bands x 2-3 lineages while cutting fixture count by 50-65%.

5. **The UCB-PFSP weighting already handles within-set allocation well.** The pruning problem is strictly about which models to INCLUDE, not how to weight them. Once included, UCB naturally upweights hard and under-explored opponents.

6. **Match-matrix intransitivity is the best free behavioral diversity signal** beyond lineage/asymmetry. Models that produce surprising H2H results (beating some opponents far above/below Elo prediction) likely have unusual strategies worth preserving.

## Recommendations

1. **Implement Stratified Pareto Selection** as described above. 20-30 lines of Python in a standalone function. Run it after each Elo ladder update in `ppo_loop_step.sh`.

2. **Set K=14 as the initial target** (7 Pareto anchors + 7 diversity fills). This is ~40% of the current 34 fixtures and preserves all three diversity axes.

3. **Always include heuristic** as a mandatory floor fixture regardless of Pareto status. It provides unique training signal as the only non-neural opponent.

4. **Build JSD probes as planned** but use them for monitoring, not pruning. Log JSD between selected fixtures at each Elo update to validate that pruning preserves behavioral spread.

5. **Add intransitivity scoring** if the initial SPS selection feels too similar after a few training iterations. This is ~30 lines of code using existing match data.

6. **Do not prune models from different lineage groups** even if they appear redundant by Elo. Keep at least 2 models from each of: early-gen (v8-v22), mid-gen (v44-v50), late-gen (v51-v61).

## Open Questions

1. **Are v44-v61 actually from different training branches, or are they sequential?** The version numbering gap (v22 to v44) and the sharp asymmetry shift suggest a different training regime, but this should be confirmed. If they are sequential descendants, lineage diversity is lower than assumed.

2. **Does the UCB-PFSP exploration bonus adequately compensate for reduced fixture count?** With fewer fixtures, each one gets played more often, which could reduce the exploration bonus faster and cause premature convergence on a subset.

3. **Should fixture selection be static across an entire PPO run, or re-evaluated every N iterations?** The current system loads fixtures at run start. Dynamic re-selection mid-run could adapt to the learner's changing weaknesses but adds complexity.

4. **What is the actual correlation between lineage and behavioral diversity?** Running JSD between a few representative pairs (e.g., v17 vs. v48, both ~2100 Elo but different lineages) would validate or invalidate the lineage-as-proxy assumption cheaply.

5. **Is there a minimum match count needed to compute reliable intransitivity scores?** The current match matrix has 17.2% coverage (1373 of 8001 possible pairs). Sparse coverage might make intransitivity estimates noisy.
