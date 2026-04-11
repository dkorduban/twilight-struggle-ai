# Opus Analysis: ELO from Rollout History for Checkpoint Selection
Date: 2026-04-09
Question: Can we fit ELO ratings from the win/loss history accumulated during PPO league rollouts (wr_table.json) and use those ratings to select the best checkpoint, instead of the current ppo_final=ppo_best or the newly-added panel eval?

## Executive Summary

Rollout-history ELO is a theoretically attractive idea but practically inferior to the panel eval approach that is already implemented. The core problem is **non-stationarity**: wr_table.json accumulates games played by many different versions of the model across training. A game at iter 20 vs iter_0010 was played by a much weaker model than a game at iter 180 vs iter_0010, yet BayesElo treats them as evidence about the same entity. This fundamentally violates the static-rating assumption. Additionally, rollout games use exploration temperature T=1.0-1.2 with Dirichlet noise, which inflates variance and depresses skill differentiation compared to greedy T=0.0 evaluation. The uneven coverage (PFSP + recency weighting means some opponents get 5x more games) creates poorly-conditioned rating estimates.

The panel eval (200 games, T=0.0, fixed panel, controlled seeds, every 20 iters) provides a cleaner, per-checkpoint signal. The remaining gap is that panel eval has limited statistical power (~3.5% SE per matchup at 200 games). A practical improvement would be a **lightweight post-training tournament** among the top panel-eval candidates: run 200-400 games at T=0.0 between the top-3 panel-eval checkpoints and the fixture panel, fit BayesElo on those clean results, and pick the winner. This costs ~10 minutes and gives a well-anchored, stationary rating.

Rollout ELO is not worth implementing. Panel eval + post-run confirmation tournament is the recommended path.

## Findings

### 1. Data Quality: Rollout Games as ELO Signal

**wr_table.json schema**: `{opponent_key: {wins_ussr, total_ussr, wins_us, total_us}}`. Each key is either a checkpoint stem (e.g. `iter_0010`), `heuristic`, or `__self__`. Per-side win counts are accumulated across the entire training run. There is no per-iteration breakdown -- all games against a given opponent are summed.

**Temperature bias (T=1.0-1.2 with Dirichlet noise)**: Rollout games use exploration settings, not evaluation-mode play. At T=1.0 with dir_alpha=0.3, the policy is substantially noisier than at T=0.0. This has two effects:
- Win rates compress toward 50% -- a 300-Elo gap that would produce 85% WR at T=0.0 might produce only 70% WR at T=1.0. This doesn't invalidate ELO fitting (the scale just shrinks), but it reduces the **resolution** of rating differences. Small genuine improvements (~20 Elo) vanish into noise.
- The variance per game is higher, so more games are needed for the same confidence. A 200-game rollout at T=1.0 has roughly the statistical power of ~120 games at T=0.0 for rating discrimination.

**Uneven coverage**: PFSP weighting gives hard opponents more games. Recency weighting (tau=20) means recent checkpoints get ~7x more games than early ones. The `__self__` slot always gets ~25% of games (1 of 4 mix_k slots). This means:
- `iter_0010` might have 20 total games across the run
- `iter_0150` might have 200 games
- `heuristic` might have ~400 games (10% per slot + fixture slot)
- `__self__` might have ~1000 games (meaningless for ELO -- always 50/50 by symmetry)

BayesElo handles uneven coverage reasonably well -- sparse matchups just get wider CIs. But 20 games against iter_0010 gives SE of ~11% (±50 Elo), which is noise, not signal.

**Non-stationarity (the fatal flaw)**: wr_table accumulates across the entire run. Games vs iter_0010 played at iter 20 (when the model was weak) are combined with games vs iter_0010 played at iter 180 (when the model was strong). The resulting WR is an average over the model's entire training trajectory, not a measurement of any particular checkpoint. BayesElo's fundamental assumption is that each player has a fixed rating and all games are IID samples given that rating. This is violated by design.

Consider: the model at iter 30 might win 40% against iter_0010. The model at iter 180 might win 80% against iter_0010. The wr_table shows 60% -- but this is the WR of no actual model that ever existed. The fitted ELO corresponds to a fictional average model, not the best checkpoint.

**Fixture anchoring**: Fixtures (v8, v14, v22, heuristic) provide absolute scale anchoring. With heuristic_pct=10% and fixture_fadeout=50, the model plays ~200-400 total games vs fixtures before they fade out. After fadeout, the only new data comes from PFSP-sampled past-self checkpoints. 200-400 fixture games give SE ~3-5%, which is adequate for anchoring but not for precise per-checkpoint discrimination.

### 2. Comparison to Alternatives

**vs ppo_final = ppo_best (current default)**:
The current approach simply uses the last checkpoint. This is correct when training is monotonically improving, but misses regressions (as happened with v24-v26 entropy collapse). Rollout ELO would in theory detect such regressions, but the non-stationarity problem means it would detect them too late or not at all -- by the time enough games accumulate against a strong reference, the training has moved on.

**vs panel eval every 20 iters (just implemented)**:
Panel eval uses T=0.0, a fixed panel of opponents, controlled seeds, and runs as a separate process per checkpoint snapshot. This is strictly better for per-checkpoint measurement because:
- Each eval is a snapshot of one specific model version (no non-stationarity)
- T=0.0 maximizes skill differentiation
- Fixed opponents enable apples-to-apples comparison
- 200 games per opponent gives ~3.5% SE per matchup, ~2% aggregate SE

The remaining weakness of panel eval is that 200 games at 20-iter intervals may miss the exact peak (it could be at iter 137 between eval points 120 and 140). But this is a resolution issue, not a bias issue. The measurement at each eval point is clean.

**vs post-run tournament (10 min cost)**:
After training, identify the top-3 candidates from panel eval WR curves. Run 400 games at T=0.0 against the fixture panel (heuristic + v8/v12/v14/v22). Fit BayesElo on these 2000 clean games. This gives:
- Stationary ratings (each candidate plays as itself, not a training-average)
- High resolution (~30 Elo CI width at 400 games)
- Direct anchoring to the global ladder
- Cost: ~10 min on CPU (6 candidates x 5 opponents x 400 games = 12K games, ~0.05s/game)

This is clearly the best approach and is essentially what `run_elo_tournament.py` already does.

### 3. Implementation Feasibility

**What's missing from wr_table.json for BayesElo fit**:
- wr_table has no per-iteration breakdown. It tracks cumulative wins/total per opponent, not when those games were played. To fit per-checkpoint ELO, you would need to either:
  (a) Add per-iteration win tracking: `{iter_0010: {iter_20: {wins: 3, total: 5}, iter_30: {wins: 4, total: 5}, ...}}` -- this is a schema change that would make wr_table much larger
  (b) Reconstruct from rollout logs (not currently stored)

- The wr_table tracks wins of "the current model" vs each opponent, but "the current model" changes every iteration. You cannot retroactively assign those wins to specific checkpoints.

**Can run_elo_tournament.py take wr_table as input?**:
Not directly. run_elo_tournament.py expects MatchResult objects with (player_a, player_b, wins_a, wins_b) where player identities are fixed. wr_table has cumulative stats with a non-stationary "player_a". You would need to build synthetic MatchResult objects, which requires the per-iteration breakdown that doesn't exist.

**Anchoring to global ladder**:
If using the post-run tournament approach, anchoring is trivial: include v12 in the panel and set anchor_elo=2001. This is already how run_elo_tournament.py works.

### 4. The Non-Stationarity Problem in Detail

**Magnitude of bias**: In a typical 200-iter run with league_save_every=10, there are ~20 iter_*.pt checkpoints in the pool. The model improves by roughly 100-300 Elo over the full run (e.g. v22 started at ~1900 and reached ~2100). Early games (iter 1-50) against iter_0010 reflect a model ~100 Elo weaker than late games (iter 150-200). The cumulative WR averages over this entire range.

For the final checkpoint (the one we care about), the wr_table overstates its WR against weak opponents (by including early games when it was weaker) and understates its WR against strong opponents (by including early games). Wait -- it's actually the opposite: the wr_table *understates* WR against weak opponents because early-iteration games (when the model was itself weak) drag the average down. And it *overstates* WR against strong opponents because... no, it still understates, because the model was weaker in early games.

The net effect: the fitted ELO for "the current model" is biased downward relative to the final checkpoint's true strength, because it includes games from when the model was weaker. This bias is on the order of 50-150 Elo -- the entire range of improvement during training.

**Per-window ELO**: Using only games from the last N iterations would help, but:
- With league_save_every=10 and mix_k=4, each iteration produces ~50 games per opponent (200 games / 4 opponents). Over the last 50 iterations, you'd have ~50 games per opponent on average, but heavily skewed by PFSP/recency.
- Some opponents would have <10 games in the window, making their ratings useless.
- The window still contains model evolution -- the model at iter 150 differs from iter 200.
- This adds complexity for marginal benefit over panel eval.

### 5. Practical Recommendation

**Rollout-history ELO is not useful.** The non-stationarity is not a minor concern that can be corrected -- it is fundamental to the data generation process. The wr_table was designed for PFSP opponent selection (where cumulative WR is the right signal), not for per-checkpoint strength measurement.

**The recommended checkpoint selection pipeline is:**

1. **During training**: Panel eval every 20 iters (already implemented). T=0.0, 200 games vs fixed panel, async background process. Log combined WR to W&B.

2. **After training**: Identify top-3 panel-eval checkpoints by combined WR. Run `run_elo_tournament.py` with these 3 candidates + fixture panel (heuristic, v8, v12, v14, v22), 400 games per pair, round-robin schedule. Pick the highest-rated checkpoint as ppo_best.pt.

3. **Cost**: Panel eval is free (async, background). Post-run tournament is ~10-15 min. Total overhead: negligible.

4. **Fallback**: If all panel evals are within 2% WR of each other (common when training is stable), just use ppo_final.pt -- the difference is within noise.

## Conclusions

1. **Rollout ELO from wr_table.json is not a valid checkpoint selection signal.** The fundamental non-stationarity of the data (cumulative wins across a changing model) violates BayesElo's core assumption. The fitted rating would correspond to a fictional "average model across training," not to any specific checkpoint.

2. **Panel eval (already implemented) is the correct intra-training signal.** Each panel eval snapshot measures one specific model version under controlled conditions. The main limitation is sample size (200 games, ~3.5% SE), which can be addressed by a post-run confirmation tournament.

3. **The cheapest high-quality approach is panel eval + post-run tournament.** Top-3 candidates from panel eval, 400-game round-robin vs fixture panel, BayesElo fit. Adds ~10 min to the pipeline.

4. **wr_table.json should remain a PFSP-only data structure.** Its cumulative nature is exactly right for prioritized fictitious self-play (harder opponents get more training time) but wrong for static rating estimation.

5. **The schema change required to make rollout ELO work (per-iteration win tracking) is not worth the complexity.** Even with per-iteration data, the small game counts per (checkpoint, opponent) pair (~5-10 games) would give Elo estimates with 100+ Elo CI widths. Panel eval's 200 concentrated games give ~50 Elo CI width, which is better.

## Recommendations

1. **Do not implement rollout-history ELO.** It is not a useful signal for checkpoint selection.

2. **Enhance post-run selection**: After training, automatically run a short tournament among the top-3 panel-eval checkpoints using `run_elo_tournament.py`. This can be integrated into `ppo_loop_step.sh`.

3. **Consider increasing panel eval games**: Going from 200 to 400 games per panel eval halves the CI width. The async background process can absorb this without blocking training.

4. **Track panel eval WR curves in W&B** (already happening). Use the curve shape (monotone vs peaked) to decide whether ppo_final or an earlier checkpoint should be ppo_best.

## Open Questions

1. **Is 20-iter panel eval granularity sufficient?** If training regressions happen within 20 iters (as with v24 entropy collapse at iter 1), a tighter interval (every 10 iters) would catch them. Cost: 2x background evals.

2. **Should the post-run tournament be automated in ppo_loop_step.sh?** This would replace the current v_N Elo tournament with a per-checkpoint tournament within a run. The current pipeline already runs inter-run Elo; adding intra-run selection is straightforward.

3. **Is panel eval WR or BayesElo the better metric for checkpoint selection?** For a fixed panel, average WR and fitted Elo are monotonically related (both increase with strength). BayesElo adds value only when the panel is heterogeneous and coverage is uneven, which is true for the fixture panel. For a single-opponent eval (vs heuristic only), WR is sufficient.
