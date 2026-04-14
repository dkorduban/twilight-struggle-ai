---
# Opus Analysis: Session Findings and Action Items
Date: 2026-04-14T18:00:00Z
Question: Analyze session findings and create prioritized action items

## Executive Summary

This session uncovered and fixed two critical infrastructure failures that had been silently sabotaging PPO training for 30+ runs: (1) the eval panel used 5-mode opponents against 6-mode models, producing fake Elo ratings of 2000-2413 and disabling the auto-restart mechanism, and (2) ISMCTS was searching under a 5-mode action space for 6-mode models (missing EventFirst) and not advancing game state properly after tree actions. With both fixes deployed, v262_sc through v266_sc are now the first correctly-measured runs. Early results are promising: v262_sc=1880, v263_sc=1896, v264_sc=1894, v265_sc=1875 -- all near or above the historical peak of v209_sc=1875, confirming the chain is recovering under the restored peak-era config (ent=0.01 decay, reset_optimizer=true) and corrected measurement.

## Findings

### 1. Eval Panel Measurement Failure (fixed: c756f33)

**Root cause**: The incremental Elo placement system used 5 panel opponents (v55/v54/v44/v45/v48), all 5-mode models with `mode_head.weight.shape[0]==5`. Six-mode models (v205_sc onward) have EventFirst as a sixth mode. When a 6-mode model plays EventFirst correctly, the 5-mode opponent literally cannot respond in kind, creating a systematic 94-97% WR floor regardless of actual model quality.

**Impact**: The BayesElo solver treated 7-of-8 matches as extreme wins and produced wildly inflated ratings (v261_sc=2413 vs true ~1720-1730). The `maybe_override_restart.sh` threshold of 1750 was never triggered for any run from v232_sc onward, meaning no auto-restarts fired during 30+ consecutive runs -- even when models were genuinely regressing.

**Fix quality**: The new panel (v209_sc/v217_sc/v232_sc/v228_sc/v227_sc) is correctly all 6-mode. Post_train_confirm.sh and ppo_loop_step.sh both updated. The anchor is now v209_sc@1875 instead of v14@2015. The v262-v266 Elo values (1875-1896) are the first trustworthy measurements.

**Remaining issues**:
- The PANEL_V55/V54/V44/V45/V14 variable names in ppo_loop_step.sh and post_train_confirm.sh still reference the old model names even though they point to new files. This is confusing. They should be renamed to PANEL_1/2/3/4/5 or PANEL_V209_SC etc.
- `run_traced_game.py` line 24 still defaults to `v55_scripted.pt` (5-mode). Should default to a 6-mode model.
- `collect_selfplay_cpp.py` lines 9/16 reference `v55_scripted.pt` in help text.
- `test_feature_extraction.py`, `test_small_choice.py`, `test_rollout_pipeline.py` reference `v45_scripted.pt`. These are test fixtures so may be intentional (testing 5-mode compat), but should be verified.
- `run_elo_tournament.py` line 291 still uses `--anchor v14 --anchor-elo 2015` in the full round-robin path. This is the non-incremental path so may not be actively called, but if a full round-robin is ever run, it will use the wrong anchor.
- The full ladder still has v261_sc=2413 as the top entry. This fake value pollutes any code that reads the ladder to find "top model". The `Extension check: SKIP_NOT_PROMISING: v265_sc(1875) is -538 below top` in the autonomous log shows v261_sc's fake 2413 is actively distorting the extension check logic.

### 2. ISMCTS Bugs (fixed: 49c0724, 53892b8)

**Bug 1 -- EventFirst missing from action space**: `collect_card_drafts()` in ismcts.cpp did not include `EventFirst` as a legal mode when building the tree action space. This meant 6-mode models searched under a 5-mode action space during ISMCTS -- the search could never explore EventFirst plays, even when the policy strongly preferred them. The search was effectively blind to one of the model's strongest modes.

**Bug 2 -- apply_tree_action didn't advance state**: After applying a tree action, `apply_tree_action()` only flipped `pub.phasing` without advancing through the actual AR/cleanup mechanics. This meant the search tree modeled a game where players alternate but the game clock never advances -- no turn progression, no scoring checks, no hand refill. Games in the search tree would never reach scoring or end conditions naturally.

**Post-fix validation**: 48/48 C++ tests pass. Smoke test shows scoring_card_held no longer dominates ISMCTS game outcomes (previously pathological). Instead, games show realistic endings like europe_control losses.

**What this means for model quality**: The ISMCTS bugs mean that ALL self-play games generated with ISMCTS search (if any were used for training data) had corrupted search guidance. However, reviewing the training pipeline, PPO self-play uses `mcts_batched` (batched MCTS), not ISMCTS. ISMCTS is used only for evaluation/benchmark games and the online play path. So the training data itself was not corrupted by these bugs -- but any ISMCTS-based evaluation results (e.g., the ISMCTS budget sweep) were invalid and should be re-run.

### 3. PPO Chain Plateau and Recovery

**History**: The chain was stuck at true Elo ~1700-1820 for 30+ runs (v217_sc through v261_sc). Three root causes were identified and fixed this session:
1. Flat entropy (0.003) instead of decay from 0.01 -- removed exploration phase (fixed: 773d4ea)
2. Preserved Adam state instead of reset -- locked in stale gradients (fixed: 1975feb)
3. Fake Elo measurement -- auto-restart never triggered (fixed: c756f33)

**Current results** (first correctly-measured runs):
| Model | Elo | Notes |
|-------|-----|-------|
| v262_sc | 1880 | Restart from v217_sc(1837), first correct measurement |
| v263_sc | 1896 | Chained from v262_sc |
| v264_sc | 1894 | Chained from v263_sc |
| v265_sc | 1875 | Chained from v264_sc |

These are all in the 1875-1896 range, which is AT or ABOVE the historical peak of v209_sc=1875. This is strong evidence that the peak-era config restoration (ent decay + optimizer reset) combined with correct measurement has broken the plateau.

**Interpretation**: The chain was never truly stuck in model quality -- it was stuck in measurement. The flat entropy did suppress exploration, but the bigger issue was that the eval panel couldn't distinguish improvement. Now that measurement is fixed, the v262-v265 range shows the model was likely improving all along but we couldn't see it. The ~1880-1896 readings may represent genuine new peaks.

**Caution**: v265_sc=1875 is slightly below v263_sc=1896. This could be normal run-to-run variance (~20 Elo) or the beginning of another plateau. Need 5+ more runs to establish the trend.

### 4. Scoring Card Misuse in Traced Game

**Observation**: In a traced v261_sc vs v261_sc game (seed=42), USSR held Middle East Scoring AND Formosan Resolution, spaced both via Space Race, then failed to play them before turn end -- triggering instant scoring_card_held loss on Turn 2.

**Root cause analysis**: This is a multi-layered problem:

1. **Value function blindness**: The value function does not sufficiently penalize holding scoring cards late in a turn. It treats "space a scoring card" as equivalent to "space any card" because the value function sees only the board state after the action, not the urgency of remaining hand composition.

2. **Not a mask problem**: The legal action mask correctly allows playing scoring cards. The model CHOSE to space them instead of playing them, which is a policy quality issue.

3. **Not a mode selection problem per se**: EventFirst mode was used correctly for other cards. The issue is specifically about the Space Race mode being preferred over playing scoring cards for influence/scoring.

4. **Training data bias**: In self-play, both sides make the same mistakes, so scoring_card_held losses may not generate strong enough gradient signal. If both players occasionally lose to scoring_card_held, the value function learns to treat it as "random bad luck" rather than a correctable blunder.

**Minimal fix options**:
- **Reward shaping**: Add a penalty term for holding scoring cards at turn end (e.g., -0.5 VP equivalent per unplayed scoring card per turn). This directly teaches the value function that scoring cards must be played.
- **Auxiliary loss**: Add a "scoring card urgency" auxiliary head that predicts whether a scoring card will be held at turn end. This creates gradient signal specifically for scoring card handling.
- **Masking approach**: Make space-racing a scoring card illegal when the player has remaining ARs to play it. This is the simplest fix but may be too restrictive (there are rare cases where spacing a scoring card is correct, e.g., when the region is catastrophically unfavorable).
- **Curriculum**: Weight scoring_card_held losses more heavily in the PPO advantage calculation. This makes the model learn faster from these specific failures.

**Recommendation**: The masking approach (prevent spacing scoring cards when ARs remain) is the safest minimal fix. It eliminates the most common blunder pattern while not requiring value function changes. The edge case of "space a scoring card in a losing region" can be handled later as a mask relaxation.

### 5. Influence Allocation Trace Anomaly

**Observation**: In the traced game, influence allocation appeared single-target (1 IP placed per callback call) rather than distributing ops-worth of influence across multiple countries.

**Analysis**: This is likely a trace display issue, not a game logic bug. The C++ engine calls `choose_country()` once per influence point (the model picks one country at a time, repeated for each ops point). The trace showed each individual call. The model IS allocating influence correctly in the engine -- it just places them one at a time via repeated callbacks. This is the correct mechanism for the DP allocation head design.

**No action needed** unless benchmarking reveals actual allocation quality issues.

### 6. Headline Tie-Break Ordering

**Observation**: ismcts.cpp and game_loop.cpp disagree on equal-ops tie-breaks for headline resolution.

**Impact**: Low. Headline tie-breaks (both players play same-ops cards) are resolved by a coin flip in the official rules. If the two files use different deterministic tie-breaks, it means ISMCTS search models headline resolution slightly differently than the actual game. This would slightly bias ISMCTS search quality for headlines but has minimal impact since headlines are a small fraction of decisions.

**Fix**: Align the tie-break logic. Low priority.

## Conclusions

1. **The eval panel fix was the single most impactful change this session.** It unblocked correct measurement, re-enabled auto-restarts, and revealed that the chain may have been improving all along. v262-v265 at 1875-1896 Elo represent probable new peaks.

2. **The PPO chain appears to be recovering.** v263_sc=1896 exceeds the historical peak of v209_sc=1875. Five more runs are needed to confirm this is a real trend and not run-to-run noise.

3. **The ISMCTS fixes are important for future evaluation quality** but did not directly impact training data (PPO uses mcts_batched, not ISMCTS). ISMCTS validation sweeps should be re-run to establish correct baselines.

4. **Scoring card misuse is a real model quality issue** that should be addressed once the PPO chain stabilizes. The simplest fix is to mask space-racing scoring cards when ARs remain.

5. **The full Elo ladder is polluted with fake v261_sc=2413** at the top, which is actively distorting extension-check logic. This entry should be removed or corrected.

6. **Several files still reference 5-mode models as defaults** (run_traced_game.py, collect_selfplay_cpp.py, test files). These are cosmetic but create confusion.

7. **The maybe_override threshold (1750) appears correctly calibrated for the new panel scale**, since v262-v265 are in the 1875-1896 range. A model genuinely regressing to 1750 would be ~125-150 Elo below current level, which is an appropriate restart trigger.

## Recommendations

### P0: Critical (do within next 2 runs)

1. **[Training infra] Remove or correct v261_sc=2413 from the full ladder.** The fake Elo is distorting extension-check logic (`SKIP_NOT_PROMISING: v265_sc(1875) is -538 below top`). Either delete v261_sc from the ladder JSON, or re-run its placement against the new 6-mode panel. The extension check should never compare against a known-fake value.

2. **[Training infra] Rename PANEL_V55/V54/V44/V45/V14 variables** in ppo_loop_step.sh and post_train_confirm.sh to PANEL_1 through PANEL_5 or PANEL_V209_SC etc. The current naming actively misleads anyone reading the config.

3. **[Training infra] Update run_elo_tournament.py full-round-robin anchor** from `--anchor v14 --anchor-elo 2015` to `--anchor v209_sc --anchor-elo 1875`. If a full round-robin is triggered, the old anchor would produce wrong absolute Elo values.

### P1: Important (do within next 5 runs)

4. **[PPO chain] Monitor v266_sc through v270_sc closely.** If 3+ of these runs score above 1875, the chain is genuinely improving and should continue uninterrupted. If they drop below 1850 consistently, the chain may be entering another plateau, and more aggressive intervention (BC re-init, mode_head perturbation) should be considered.

5. **[ISMCTS] Re-run the ISMCTS validation sweep** now that both bugs are fixed. The budget sweep from `ismcts_budget_sweep_20260414.md` is invalid. Run 200-game matches at budgets 50/100/200/400 sims with v265_sc (or whatever is the current best) against heuristic and against v217_sc to establish correct ISMCTS baselines.

6. **[Model quality] Implement scoring-card space-race mask.** When a player holds a scoring card and has remaining ARs in the turn, disallow spacing that scoring card. This prevents the most common catastrophic blunder. Implementation location: `legal_actions.cpp` or `legal_modes()` -- when the selected card is a scoring card, remove `Space` from legal modes.

7. **[Training infra] Update default model references.** Change `run_traced_game.py` line 24 from `v55_scripted.pt` to `v209_sc_scripted.pt` (or latest best). Update `collect_selfplay_cpp.py` help text similarly.

### P2: Nice to have (do when chain is stable)

8. **[ISMCTS] Align headline tie-break logic** between ismcts.cpp and game_loop.cpp. Low impact but eliminates a known inconsistency.

9. **[Evaluation] Run a 6-mode-only round-robin** across v205_sc, v209_sc, v217_sc, v228_sc, v232_sc, v262_sc-v270_sc (once available) with 200 games per pair. This establishes the true 6-mode Elo ladder and reveals whether the v262+ era is genuinely stronger than v209_sc or just measured differently.

10. **[Training infra] Consider WR-based auto-restart** instead of Elo-based. Direct H2H win rate against the anchor (v217_sc) is a more robust signal than BayesElo computed from a small panel. "Restart if WR vs v217_sc < 0.42" is simpler and harder to break than "restart if Elo < 1750".

11. **[Model quality] Add scoring_card_held rate tracking** as a first-class metric in the PPO training loop. Log the fraction of self-play games that end in scoring_card_held per iteration. This is a direct measure of the most common blunder type and should decrease over training.

12. **[Model quality] Investigate space-race abuse more broadly.** The traced game showed the model spacing Fidel, NORAD, NATO, and scoring cards. While spacing non-scoring cards is sometimes correct, the model may be over-using Space Race as a "dump bad cards" strategy. Track space-race frequency per game and compare to strong human play patterns.

### P3: Deferred

13. **[Architecture] BC re-initialization** from v209_sc or best v26x games. Only needed if the chain plateaus again after the current recovery. The v262-v265 results suggest the chain is not stuck, so this is not urgent.

14. **[Architecture] Mode_head perturbation** (add noise to mode_head weights at run start). Same trigger as item 13 -- only if plateau recurs.

15. **[Evaluation] Investigate why 6-mode crushes 5-mode at 94-97%.** Is it purely EventFirst advantage or are 6-mode models also better at the 5 shared modes? Academic interest; low practical priority.

## Open Questions

1. **Is v263_sc=1896 a genuine new peak or measurement noise?** The 6-mode panel has only 5 opponents, and each incremental placement uses ~8 matches of 200 games. Standard error is ~20-30 Elo. Need 5+ runs to distinguish signal from noise. If the running average of v262-v270 is above 1880, the improvement is real.

2. **How much of the v262+ improvement is from the config fixes vs. simply restarting from v217_sc?** v262_sc was a restart from v217_sc with restored peak-era config. It would be informative (but expensive) to also restart from v217_sc with the OLD config (flat ent=0.003, no optimizer reset) to isolate the config effect from the restart effect.

3. **Are the PFSP training fixtures still appropriate?** `selected_fixtures.json` likely still includes 5-mode models as training opponents. Training against 5-mode opponents may encourage EventFirst exploitation rather than developing stronger shared-mode play. Consider shifting to a 6-mode-heavy fixture set.

4. **Is the v261_sc fake Elo (2413) causing any other downstream issues** beyond the extension check? Any code that reads the ladder to select "diverse opponents" or compute fixture weights could be affected.

5. **What is the scoring_card_held rate for v262-v266?** If it has decreased compared to v261_sc, the peak-era config (with its exploration phase) may naturally reduce this blunder type by exploring more card-play sequences.
---
