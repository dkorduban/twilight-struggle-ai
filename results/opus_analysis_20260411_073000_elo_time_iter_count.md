---
# Opus Analysis: ELO Tournament Time & Iteration Count Review
Date: 2026-04-11T07:30:00Z
Question: (1) Why does ELO tournament take much more time than training, ideas to fix? (2) Was the 80-iteration decision based on buggy confirmation tournament results with cache collisions?

## Executive Summary

The tournament overhead is real but the root cause is the **confirmation tournament** (42% of cycle time), not the main ELO tournament (11%). The 80-iteration decision was based on v44's panel_eval_history.json data, which is **not affected by cache collisions** (panel eval runs inline during training). However, the confirmation tournament itself has been severely broken by cache collisions from v46 through v52 -- all 7 runs reused v46's match results verbatim (0 new matches), meaning ppo_best.pt selection was identical across those runs regardless of actual checkpoint quality. The run-prefix fix deployed in v53 corrects this going forward, but the 87 stale bare `iter*` cache files in `results/matches/` should be purged.

## Findings

### 1. Tournament Time Breakdown (v53, the first correctly-cached run)

| Phase                          | Time    | % of cycle |
|-------------------------------|---------|------------|
| Training (80 iters)           | 43.5 min| 47%        |
| Confirmation tournament (49 new matches) | 39.6 min | 42% |
| Main ELO tournament (25 new matches)    | 10.2 min | 11% |
| **Total cycle**               | **93.4 min** | 100% |

The main ELO tournament is efficient: 25 new matches at ~25s each = ~10 min. The 300 cached matches are reused correctly (model names like `v8`, `v14` etc. are stable across runs).

The confirmation tournament is the bottleneck: 8 candidates + 4 fixtures = 12 models, C(12,2) = 66 pairs, of which ~49 are new (candidate-to-candidate and candidate-to-fixture pairs). At ~50s/match average, this takes ~40 minutes.

The user's estimate of "2.25 hours" likely reflects the **theoretical** full round-robin (325 pairs at 25s = 2.25 hours). In practice, caching reduces the main tournament to ~10 minutes. But this only holds if existing models' match results don't need refreshing.

### 2. Cache Collision Bug: Scope and Impact

**The bug:** `ppo_confirm_best.py` originally used bare `iterNNNN` names (e.g., `iter0020`) as model identifiers in the match cache. Since every PPO run saves checkpoints at the same iter numbers (10, 20, 30, ...), cache files like `iter0020__vs__v14.json` would be written by one run and reused by the next, even though they refer to completely different model weights.

**87 bare `iter*` cache files** exist in `results/matches/`, created by confirmation tournaments for v38-v52.

**Collision map across confirmation tournaments:**

| Run | Candidates | Collisions with prior runs |
|-----|-----------|---------------------------|
| v38 | iter0120, iter0160, iter0180 | (first run, no prior) |
| v39 | iter0080, iter0100, iter0120 | iter0120 from v38 |
| v40 | iter0060, iter0100, iter0140 | iter0100 from v39 |
| v41 | iter0060, iter0080, iter0180 | iter0060 from v40, iter0080 from v39, iter0180 from v38 |
| v44 | iter0020, iter0060, iter0160 | iter0060 from v40/v41, iter0160 from v38 |
| v45 | iter0020-iter0180 (8 candidates) | iter0020 from v44, iter0060 from v40/v41, iter0080 from v39/v41, iter0100 from v39/v40, iter0120 from v38/v39, iter0160 from v38/v44, iter0180 from v38/v41 |
| v46 | iter0010-iter0070 (7 candidates) | 34 of 55 matches new, 21 reused |
| **v47-v52** | iter0010-iter0070 (7 candidates each) | **0 new matches, ALL 55 reused from v46** |

**Critical finding:** From v47 through v52, the confirmation tournament ran zero new matches and returned v46's results verbatim. This means:
- ppo_best.pt selection for v47-v52 was based on v46's checkpoint quality, not their own
- The "winner" checkpoint was always whichever iter (10-70) was best in v46, regardless of whether that iter was best in v47, v48, etc.
- This is a silent correctness failure -- the code ran without errors

**v53 was the first correctly-cached run** (after the run_prefix fix), with 49 of 55 matches newly played.

### 3. Was the 80-Iteration Decision Valid?

The 80-iter decision was made in the `opus_analysis_20260411_013000_next_hyperparams.md` analysis, based on v44's data:

**Panel eval history (v44, 200 iters):**
| Iter | Avg Panel Combined WR |
|------|----------------------|
| 20   | 0.589 |
| 40   | 0.581 |
| 60   | 0.595 |
| 80   | 0.565 |
| 100  | 0.580 |
| 120  | 0.580 |
| 140  | 0.555 |
| 160  | 0.581 |
| 180  | 0.547 |

**Panel eval is NOT affected by cache collisions.** It runs inline during training via `tscore.benchmark_batched()` calls in `train_ppo.py`, not through the match-cache system. The data genuinely shows that v44's peak was at iter 20-60 with degradation afterward.

**However, the confirmation tournament for v44 WAS partially affected:**
- v44 confirmation: 21 total matches, 14 reused, 7 new
- `iter0060` and `iter0160` collided with v38-v41 (corrupted T=1.2 era) cache entries
- The confirmation Elo rankings (iter0020=2017, iter0060=1851, iter0160=1810) may be distorted for iter0060 and iter0160 specifically

**Bottom line:** The 80-iter decision is likely correct in direction (peaking early is real, as shown by unaffected panel eval), but the magnitude of the degradation after iter 60 may be overstated due to cache collisions making iter0060 and iter0160 appear weaker than they actually were.

### 4. Ideas to Reduce Tournament Time

**Current bottleneck: Confirmation tournament (42% of cycle, ~40 min)**

The confirmation tests 8 candidates against 4 fixtures (round-robin among all 12), playing 400 games per pair. Most of this time is spent on candidate-vs-candidate matches that provide limited value.

**Ideas ordered by impact:**

1. **Reduce --n-top from 8 to 3** (original default): C(7,2) = 21 pairs instead of C(12,2) = 66. With ~12 new matches instead of 49, confirmation drops from ~40 min to ~10 min. The top-3 panel eval candidates are sufficient -- the delta between rank 3 and rank 8 is typically <2% WR.

2. **Use chain schedule instead of round-robin for confirmation**: 11 matches instead of 66. Combined with --n-top 3: only 6 matches, ~5 min.

3. **Reduce --n-games from 400 to 200 for confirmation**: Each match halves in time. With 200 games, statistical power is adequate for confirming a top-3 ranking (not for precise Elo estimation, but that's not needed for best-checkpoint selection).

4. **Skip confirmation entirely -- use panel eval directly**: Panel eval already provides 4-opponent WR at every eval checkpoint. The confirmation tournament was added to address panel eval noise, but with eval-every=10 and 4 opponents, the panel data is already quite stable. Simply pick the iter with highest avg panel WR as ppo_best.pt.

5. **Reduce main ELO tournament frequency**: Run full ELO every 3-5 runs instead of every run. Use panel eval WR for intermediate quality tracking. The main ELO tournament provides stable absolute ratings but is redundant when run every 40 minutes.

6. **Reduce --games from 400 to 200 for main ELO**: Halves new-match time from 10 min to 5 min. With 200 games per pair, 95% CI widens by ~40% but is still useful for ranking.

7. **Use Swiss-system or FIDE-style pairing** instead of round-robin for main ELO: Only play informative pairs (close ratings). With 26 models, ~50 pairs (instead of 325) would suffice for stable ratings. The cache makes this mostly moot for existing pairs, but would help when adding many new models.

### 5. Stale Cache Files

87 bare `iter*__vs__*.json` files in `results/matches/` are stale and dangerous:
- They will not be reused by future runs (which use `ppo_vNN_league_iterNNNN` names)
- But if anyone reverts the run_prefix fix, they would cause silent corruption again
- Safe to delete them

## Conclusions

1. **The 80-iteration decision is directionally correct.** Panel eval data (unaffected by cache bugs) genuinely shows v44 peaking at iter 20-60 and degrading afterward. The recommendation to shorten runs from 200 to 80 iterations is sound.

2. **The cache collision bug was severe and silent.** From v47 through v52, confirmation tournaments returned v46's results without playing any new games. ppo_best.pt selection for 6 consecutive runs was effectively random (or at best, based on v46's checkpoint quality rankings applied to different runs' checkpoints).

3. **The confirmation tournament is the real time bottleneck**, consuming 42% of each cycle with the run-prefix fix active, and was effectively a no-op (0 new matches) before the fix.

4. **The v44 confirmation Elo rankings were partially corrupted** by cache collisions with v38-v41 (corrupted era). iter0060 and iter0160's Elo scores may be unreliable. iter0020's data was likely clean (first time that cache key appeared).

5. **The main ELO tournament is efficient** at ~10 min per cycle (only 25 new matches). It is not the bottleneck.

6. **87 stale bare `iter*` cache files should be purged** from `results/matches/` to prevent future issues.

## Recommendations

1. **Reduce --n-top from 8 to 3** in ppo_loop_step.sh confirmation tournament. This is the single biggest time saving: ~40 min -> ~10 min.

2. **Consider skipping confirmation entirely** and using panel eval peak directly for ppo_best.pt selection. The confirmation tournament adds complexity and ~10-40 min for marginal benefit.

3. **Delete the 87 stale bare `iter*` cache files**: `rm results/matches/iter*__vs__*.json results/matches/heuristic__vs__iter*.json`

4. **Do not change the 80-iteration count** based on cache bug concerns -- the underlying data (panel eval) was unaffected. However, consider re-evaluating with v53+ data (first clean-cache run) to see if 80 is still the right number with corrected ent_coef decay and UPGO.

5. **For faster iteration cycles**, the combined effect of recommendations 1-2 would reduce cycle time from ~93 min to ~55 min (43 min training + 0-10 min confirmation + 10 min ELO), a 40% speedup.

6. **Run the main ELO tournament every 2-3 runs** instead of every run, using panel eval for intermediate monitoring. This saves ~10 min per skipped run.

## Open Questions

1. **Should the confirmation tournament be retained at all?** It was designed to correct for panel eval noise, but with --eval-every 10 and 4 opponents, the panel signal is reasonably stable. A/B test: compare panel-eval-peak vs confirmation-winner across v53+ runs to see if confirmation adds value.

2. **Were v47-v52's ppo_best.pt selections harmful?** Since all 7 runs (v46-v52) used the same confirmation rankings, the "best" checkpoint was always the same relative position (e.g., iter0010). If iter0010 happened to be genuinely best in most 80-iter runs, the damage is limited. Worth checking whether Elo regressed across v47-v52 as a result.

3. **Is 80 still optimal with the corrected pipeline?** v44 (200 iters, constant ent_coef=0.03) peaked at iter 20. The current config (80 iters, ent_coef 0.01->0.003 decay, UPGO, more fixtures) may have a different optimal length. v53 was the first clean run with these settings -- check its panel_eval_history to see where it peaked.

4. **Should match cache entries expire?** As models are retrained, cached results from early versions become less relevant. A TTL or version-tagging system could prevent stale results from persisting indefinitely.
---
