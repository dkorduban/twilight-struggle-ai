# Opus Analysis: Candidate Tournament Pool Composition
Date: 2026-04-12T06:00:00Z
Question: What is the ideal composition of the candidate tournament (post-training confirmation) used to place a newly trained model on the Elo ladder?

## Executive Summary

The current incremental placement uses 3 effective opponents (v55, v14, heuristic) with 200 games each, yielding ~600 total games. This produces confidence intervals of roughly +/-25 Elo, which is adequate for coarse placement but too noisy for detecting the 15-30 Elo improvements typical between consecutive PPO generations. The main problems are: (1) heuristic is ~350 Elo below the frontier and contributes almost no discriminative signal at the top of the ladder, (2) the opponent pool lacks diversity in the critical 1950-2100 Elo range where new models actually land, and (3) per-side Elo estimates (USSR vs US) are poorly constrained with only 3 opponents spanning a huge Elo range.

The recommended fix is to expand to 5 opponents drawn from the JSD fixture pool, drop heuristic from the incremental tournament, and keep v14 only as the BayesElo anchor (not as a discriminative opponent). The 5-opponent pool should include 2 opponents strong on each side (from the per-side JSD pools) plus the current PREV_BEST. This yields ~1000 games total and tightens the 95% CI to roughly +/-18 Elo, sufficient for reliable generation-over-generation comparison, while adding only ~3-4 minutes of wall time.

## Findings

### 1. Current ladder state and Elo spread

The full ladder (`elo_full_ladder.json`) has only 4 models: v55 (2111), v14 (2015), v66_sc (1982), heuristic (1760). The fixture pool ladder (`elo_fixture_pool.json`) has 14 models spanning 1629-2015 in a full round-robin with 200 games per pair. The candidate ladder (`elo_candidates_v65_v66sc.json`) used a chain schedule with 21 matches across 22 checkpoints anchored to v55 at 2124.

Key observations from existing data:
- **CI width**: With 400 games per pair in the candidate chain, individual CIs are ~+/-25 Elo. With 200 games in the fixture pool round-robin, CIs are ~+/-10 Elo (due to many more connecting paths).
- **Elo gap between generations**: Consecutive PPO iterations differ by 10-40 Elo. The top candidates (v65_i010, v66sc_i080) are within 15 Elo of v55.
- **Side asymmetry**: USSR vs US Elo can differ by 100-200 points for the same model (e.g., v66_sc: USSR 2079, US 1881 — a 198-point gap). This is fundamental to TS, not noise.

### 2. Statistical analysis of match count vs Elo uncertainty

For a single 200-game match at 55% win rate (typical between close models):

- **Standard error of win rate**: sqrt(p(1-p)/n) = sqrt(0.55*0.45/200) = 0.035
- **Elo SE from one match**: ~25 Elo points (400/ln(10) * SE / p(1-p))
- **95% CI from one opponent**: roughly +/-50 Elo

With k opponents in a round-robin that includes cached pairwise results:
- **3 opponents (current)**: effective 95% CI ~+/-25 to +/-30 Elo
- **5 opponents**: effective 95% CI ~+/-18 to +/-22 Elo
- **8 opponents**: effective 95% CI ~+/-14 to +/-17 Elo

The improvement from 3 to 5 opponents is substantial (roughly 30% tighter CI). Going from 5 to 8 gives diminishing returns (~20% further tightening) at nearly double the wall-clock cost.

### 3. Opponent informativeness analysis

**Heuristic (Elo ~1760)**: Against a model at Elo 2100, the expected win rate for heuristic is ~5-10%. At 200 games this means ~10-20 wins, yielding very high variance in the Elo estimate from this pair. Heuristic is useful as a sanity check (did the model catastrophically regress?) but adds negligible discriminative power for placement.

**v14 (Elo ~2015)**: ~100 Elo below the frontier. Against a 2100-rated model, expected WR ~36%. This is in a useful range for Elo estimation. v14 serves double duty as BayesElo anchor, so it should remain in the pool.

**v55 (Elo ~2111)**: The current frontier. Near-50% matchups are the most informative for Elo estimation. v55 is the single most valuable opponent.

**JSD pool models (Elo 1940-2010)**: These fill the 60-170 Elo gap between v14 and v55. Adding 2-3 of these substantially improves the information density in the relevant Elo range.

### 4. Per-side pool value

The 198-point USSR/US gap for v66_sc demonstrates that combined Elo alone is insufficient for placement. A model could have the same combined Elo as v55 but be much stronger as USSR and much weaker as US (or vice versa).

The JSD fixture pools were specifically designed to maximize per-side discrimination:
- **USSR pool**: v45, v55, v17, v20, v21, v22, v48, v15 — models with diverse USSR-side play styles
- **US pool**: v55, v48, v44, v54, v57, v50, v19, v21 — models with diverse US-side play styles

Using per-side opponents lets the incremental tournament produce per-side Elo estimates with meaningful CIs, rather than the current situation where per-side Elo is barely constrained.

### 5. Anchor selection

v14 is the current BayesElo anchor at 2015. This is a reasonable choice:
- v14 is stable (not recently trained, no risk of being overwritten)
- v14's Elo is centrally located in the historical ladder
- v14 has many cached matches (reducing tournament cost)
- v14 is not at the extreme of the Elo range

The main alternative would be v55. However, anchoring to the current best is risky because:
- It creates a moving target as new models surpass v55
- All incremental placements would be relative to a single high-Elo model, amplifying noise from that one matchup

v14 should remain the anchor.

### 6. Match caching

The current system caches match results in `results/matches/`. With 1546 cached files, most fixture-pool-internal matches are already computed. The incremental tournament only needs to run matches involving the new model. With 5 opponents and 200 games each, this is 5 * 200 = 1000 new games, taking ~3-5 minutes on the RTX 3050.

## Conclusions

1. **3 matches is insufficient for reliable generation-over-generation comparison.** The ~+/-25 Elo CI overlaps heavily when consecutive generations differ by only 15-30 Elo. This means the incremental tournament frequently cannot distinguish whether a new model is better or worse than its predecessor.

2. **5 opponents is the sweet spot.** It tightens CIs by ~30% vs 3 opponents, costs only ~2 extra minutes of wall time, and is well within the "under 5 minutes" policy target. Going to 8 opponents would cost ~5 extra minutes for diminishing statistical returns.

3. **Heuristic should be dropped from the placement tournament.** It wastes 200 games on a matchup that provides almost no information at the frontier. Instead, use a simple sanity-check threshold: if the new model's WR vs v14 drops below 30%, flag a regression without needing a separate heuristic match.

4. **The 5 opponents should be drawn from the JSD fixture pool, not hardcoded.** Specifically: PREV_BEST (v55 currently) + v14 (anchor) + 3 models from the JSD combined pool that are not already in the set. Prefer models in the 1960-2010 Elo range where discrimination is most valuable.

5. **Per-side pools should be used** if the implementation cost is low. Playing 2 USSR-pool opponents and 2 US-pool opponents (plus PREV_BEST and v14 for both sides) would produce much tighter per-side Elo estimates. However, this adds complexity. A simpler first step: use 5 opponents from the combined pool and accept the per-side CIs will be wider.

6. **v14 should remain the anchor.** It is stable, centrally located, and has extensive cached match data.

## Recommendations

### Recommended 5-opponent pool for incremental placement

| Slot | Source | Rationale |
|------|--------|-----------|
| 1 | PREV_BEST (currently v55) | Most informative matchup (near 50% WR) |
| 2 | v14 | BayesElo anchor + moderate-strength calibration |
| 3 | v48 | Mid-range (Elo ~1994), appears in both per-side pools |
| 4 | v45 | Upper-mid-range (Elo ~2000), strong USSR-side discriminator |
| 5 | v54 | Upper-mid-range (Elo ~2010), strong US-side discriminator |

This gives 5 new matches (1000 games), an estimated runtime of 3-5 minutes, and opponents spanning a 100-Elo range around the relevant placement zone.

### Implementation changes to `post_train_confirm.sh`

```bash
# Replace the hardcoded INCREMENTAL_FIXTURES with:
INCREMENTAL_FIXTURES="${PREV_BEST} v14 v48 v45 v54"
# Drop "heuristic" and "v55" (v55 is already PREV_BEST when it's the top model)
```

When PREV_BEST changes (a new model surpasses v55), the pool automatically adapts because slot 1 tracks the leader. The other 4 slots are stable reference points.

### Optional enhancement: read fixture pool dynamically

Instead of hardcoding v48/v45/v54, read `results/selected_fixtures.json` and pick the top-3 models from `combined` that are not already PREV_BEST or v14:

```python
import json
fixtures = json.load(open("results/selected_fixtures.json"))
pool = [m for m in fixtures["combined"] if m not in (prev_best, "v14")][:3]
```

This makes the pool self-updating as the JSD analysis evolves.

### Games per match

Keep 200 games per match (100 per side). This is the right balance for the incremental tournament. The full ladder rebuild should continue using 400 games.

## Open Questions

1. **Should the full ladder rebuild (`--full`) also use the JSD fixture pool instead of all-vs-all round robin?** The current full mode with 50+ models produces C(50,2)=1225 matches, most cached. But a JSD-informed sparse graph might be more efficient.

2. **Should we increase games per match from 200 to 300 for the incremental tournament?** This would cost ~50% more time but tighten CIs by ~18%. Probably not worth it given the 5-opponent expansion already provides sufficient tightening.

3. **Should we run a regression-detection heuristic?** E.g., if the new model loses >60% vs v14, abort the Elo update and flag for investigation. This replaces the heuristic-as-opponent sanity check.

4. **How should the pool adapt when models start exceeding v55?** Once a v67 or v68 becomes PREV_BEST, the pool should ideally include v55 as a known reference point. The dynamic fixture-pool approach handles this naturally.

5. **Should per-side Elo be a first-class metric for promotion decisions?** Currently combined Elo drives promotion. But a model with 2200 USSR / 1900 US Elo (combined 2050) might be worse in practice than one with 2050/2050. This is a policy question, not a statistical one.
