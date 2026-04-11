# Opus Analysis: Per-Side Elo and JSD for Fixture Pruning

Date: 2026-04-11
Question: Equal combined Elo is not enough for fixture pruning -- models may use different strategies, or have different USSR vs US strengths. Should we: (a) treat each model as two separate players with per-side Elo and preserve that side-strength diversity when pruning, (b) use JSD on a fixed probe set to measure strategic divergence, or (c) both? What does the current data actually show about per-side Elo spread?

## Executive Summary

The data is unambiguous: **per-side Elo spread is massive and cannot be ignored during pruning**. Across 34 models in the ladder, the USSR-US Elo gap ranges from +41 (v50) to +178 (v11), with a mean of +97 and standard deviation of 43. Multiple clusters of models with nearly identical combined Elo (within 10 points) show gap differences exceeding 80 Elo -- meaning they present fundamentally different challenges per side. For example, v45 and v48 are both ~2102 combined Elo, but v45 has a gap of +126 while v48 has +46, making v45 a far harder USSR opponent and a far easier US opponent.

The current PFSP system already tracks per-side win rates and computes per-side UCB scores, but then **averages them into a single scalar weight** for opponent sampling. This averaging masks the per-side diversity. The fix is straightforward: make PFSP sampling side-aware (select different opponent distributions for USSR vs US rollouts), and use per-side Elo as the pruning criterion rather than combined Elo.

JSD probe evaluation would add useful information about strategic diversity (card play patterns, country targeting), but it is **not necessary for the immediate pruning decision** -- per-side Elo already provides a concrete, actionable dimension that the current system fails to exploit. JSD is a complementary signal for later, more refined pruning once the per-side Elo dimension is handled.

**Recommendation: (a) first, with (b) as a follow-up. Do not wait for JSD to fix the pruning criterion.**

## Findings

### Per-side Elo in current data

The bipartite BayesElo fit is already stored per-model in `results/elo_full_ladder.json` (fields `elo_ussr`, `elo_us` alongside `elo` combined). Key observations:

1. **All models are stronger as USSR than US** -- the minimum gap is +41 (v50), consistent with TS's known USSR early-game advantage. This is expected and not the interesting finding.

2. **The gap variance is enormous** (std=43 Elo points). Some models have learned relatively balanced play (v48: gap +46, v50: gap +41, v55: gap +53) while others are extremely USSR-tilted (v11: +178, v13: +173, v17: +158, v10/v9: +176).

3. **Models with near-identical combined Elo have wildly different side profiles.** Critical examples:
   - v45 (Elo 2102, gap +126) vs v48 (Elo 2102, gap +46): delta_gap = 80
   - v17 (Elo 2063, gap +158) vs v50 (Elo 2070, gap +41): delta_gap = 117
   - v13 (Elo 2002, gap +173) vs v61 (Elo 1995, gap +69): delta_gap = 104
   - v21 (Elo 2080, gap +113) vs v50 (Elo 2070, gap +41): delta_gap = 71

4. **The top cluster (v44-v56, combined 2100-2124) spans gaps from +46 to +126.** Pruning this cluster to one representative based on combined Elo alone would discard critical side-strength diversity.

5. **Evolution over training generations**: early models (v8-v13) tend to be USSR-tilted (gaps 115-178), middle models (v44-v56) show more balance (gaps 41-87), and some recent models (v59-v61) are moderate (gaps 68-77). This suggests PPO training gradually balances side strength, but unevenly.

### PFSP already handles per-side diversity -- partially

The current PFSP system in `train_ppo.py` (`_pfsp_weight`, `_update_wr_table_from_steps`) tracks per-side WR:
- Schema: `{wins_ussr, total_ussr, wins_us, total_us}` per opponent
- UCB is computed per side: `w_ussr = _side_ucb("wins_ussr", "total_ussr")`, `w_us = _side_ucb("wins_us", "total_us")`

**But then the two per-side UCB scores are averaged**: `return (w_ussr + w_us) / 2.0` (line 932).

This averaging means an opponent that is very hard on USSR side but easy on US side gets a medium weight on BOTH sides of rollout collection. The opponent selection is the same regardless of which side the training model is about to play. This is suboptimal:

- When collecting USSR rollouts, the system should prefer opponents that are hard to beat as USSR (i.e., opponents with strong US play -- low `wins_ussr` / high `elo_us` on the opponent side).
- When collecting US rollouts, the system should prefer opponents that are hard to beat as US (i.e., opponents with strong USSR play -- low `wins_us` / high `elo_ussr` on the opponent side).

The current averaging discards exactly the per-side signal that matters.

### What JSD adds

The JSD probe spec (`.claude/plan/jsd-probe-eval.md`) defines a well-designed system: frozen 1000-position probe set, per-head JSD (card, mode, country), per-phase breakdown (early/mid/late), value MAE. The probe set already exists at `data/probe_positions.parquet`.

JSD captures **strategic divergence** that per-side Elo cannot:
- Two models at identical per-side Elo might use completely different card play strategies (aggressive coups vs peaceful influence placement)
- Card head JSD measures policy distribution divergence directly
- Per-phase JSD can reveal early-game vs late-game strategic differences

However, JSD has limitations for pruning:
1. **JSD is symmetric** -- it says "these models differ" but not "one is harder on USSR." Per-side Elo directly answers the training-relevant question.
2. **JSD magnitude is hard to threshold** -- what JSD value means "strategically different enough to keep"? Per-side Elo has a natural interpretation (Elo points map to expected win rate differences).
3. **JSD requires model inference** (loading checkpoints, running probe positions), while per-side Elo is already computed from match results.
4. **JSD measures policy, not outcome** -- a model with very different card choices might produce similar game outcomes. For PFSP, outcomes matter more than policy details.

### Pruning criterion design

The right pruning criterion depends on what we're optimizing for:

**For PFSP training signal diversity**, the goal is: ensure the opponent pool contains models that are hard for the learner on each side. This means:

1. **Per-side Elo is the primary criterion.** Keep models that are Pareto-diverse in the (elo_ussr, elo_us) space. A model should be pruned only if another model dominates it on BOTH sides (or is within noise margin on both).

2. **Combined Elo gap alone is insufficient.** v45 (gap +126) and v48 (gap +46) at combined Elo ~2102 serve completely different training roles: v45 is a hard USSR opponent (strong US defense at elo_us=2008 vs v48's elo_us=2045), while v48 is a hard US opponent (strong USSR at elo_ussr=2091 vs v45's elo_ussr=2134). Wait -- actually v45 has HIGHER USSR Elo too. The point is: for training our model's US play, v45 is harder because v45's USSR Elo is 2134 vs v48's 2091. For training our model's USSR play, v48 is harder because v48's US Elo is 2045 vs v45's 2008.

3. **JSD adds a second diversity dimension** but is not required for the MVP pruning fix.

**Proposed pruning algorithm (per-side Elo Pareto):**

```
For each candidate model m:
  - dominated(m) = exists another model m' where:
      abs(m'.elo_ussr - m.elo_ussr) < noise_margin AND
      abs(m'.elo_us - m.elo_us) < noise_margin AND
      m' was not already pruned
  - If dominated(m), prune m (keep the one with more match data / higher combined Elo)
  - If not dominated, keep m

Where noise_margin = 95% CI width of the Elo estimate (typically ~12-15 Elo points).
```

This preserves:
- Models with high USSR Elo but low US Elo (USSR-tilted, hard opponent for learner's US play)
- Models with balanced Elo (well-rounded opponents)
- Models at different overall strength levels (difficulty ladder)

### Implementation cost comparison

| Approach | Implementation cost | Data needed | Signal quality for PFSP |
|----------|-------------------|-------------|------------------------|
| (a) Per-side Elo pruning | Low: rewrite `_pfsp_weight` to use side-specific UCB, add Pareto pruning | Already have it (`elo_full_ladder.json`) | High: directly answers "which opponent is hard on which side" |
| (b) JSD probe pruning | Medium: spec exists, probe set exists, need `ProbeEvaluator` + inference pipeline | Need to run probe eval on all fixtures | Medium: measures strategy difference but not direction |
| (c) Both | Medium-high | Both | Highest, but marginal gain over (a) alone |

**Critical fix for PFSP (independent of pruning):** Make `_pfsp_weight` return per-side weights instead of averaging. The training loop already collects USSR and US rollouts separately -- it should weight opponents differently for each side.

## Conclusions

1. **The data conclusively shows that combined Elo is insufficient for pruning.** USSR-US Elo gaps range from +41 to +178 (std=43), and models within 10 combined Elo points can differ by 80+ Elo in side gap. Pruning by combined Elo alone would destroy per-side training diversity.

2. **Per-side Elo is already computed and stored.** The bipartite BayesElo fit in `run_elo_tournament.py` is correct and the values are in `elo_full_ladder.json`. No new infrastructure is needed for the pruning criterion.

3. **The current PFSP system has a concrete bug: it averages per-side UCB weights.** Line 932 of `train_ppo.py` does `(w_ussr + w_us) / 2.0`, discarding the per-side signal. This should return two values, and the training loop should use the appropriate one based on which side is being rolled out.

4. **JSD is a useful complementary signal but not the bottleneck.** The immediate value comes from per-side Elo awareness in both pruning and PFSP weighting. JSD can be added later to further refine diversity selection, especially for detecting strategic convergence between models at different strength levels.

5. **Pruning should use 2D Pareto dominance in (elo_ussr, elo_us) space**, not 1D combined Elo thresholding. This naturally preserves USSR-tilted, US-tilted, and balanced models at each strength tier.

## Recommendations

### Immediate (this session)
1. **Fix `_pfsp_weight` to return per-side weights.** Change signature to return `(w_ussr, w_us)` tuple. In `sample_K_league_opponents`, use `w_ussr` when sampling opponents for USSR rollouts and `w_us` for US rollouts.

2. **Implement Pareto-based pruning in the league pool.** When trimming fixtures, use 2D (elo_ussr, elo_us) Pareto non-dominance with a noise margin of ~15 Elo. This replaces the combined-Elo gap criterion from the previous analysis.

### Near-term (next 1-2 days)
3. **Add per-side Elo to fixture metadata.** Store `elo_ussr` and `elo_us` in the league pool config so the training loop can use them for initial PFSP weights before enough online WR data accumulates.

4. **Implement JSD probe evaluation** per the existing spec. Use it for monitoring strategic drift (W&B logging), not for pruning.

### Later
5. **Add JSD as a tiebreaker in pruning.** When two models are within noise margin on both per-side Elo dimensions, keep the one with higher JSD vs the rest of the pool (more strategically diverse).

## Open Questions

1. **Should per-side PFSP use the opponent's _opposite_ side Elo?** When training our model's USSR play, the relevant opponent strength is their US Elo (since they play US against us). The WR table already captures this correctly (wins_ussr tracks our wins as USSR), but it's worth verifying the semantics are consistent.

2. **What noise margin for Pareto pruning?** The 95% CI from the Fisher diagonal is ~6 Elo (half-width), but this likely underestimates true uncertainty given 200 games/side. A margin of 15-20 Elo is probably safer.

3. **Should we weight the per-side UCB differently?** Currently the PFSP averages equally. An alternative: weight by the side that has more room for improvement (lower WR gets higher weight). This would automatically focus training on the weaker side.

4. **How does per-side PFSP interact with the self-slot?** Self-play (slot 0) always plays both sides. Should the self-slot also be side-weighted, or only the league opponent slots?
