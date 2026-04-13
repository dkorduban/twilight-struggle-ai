# Opus Analysis: Decoupling-First vs Gap-Fix-First Ordering
Date: 2026-04-13 UTC
Question: Should we decouple game_loop/engine concerns first before fixing individual card gaps?

## Executive Summary

No -- decoupling first would not meaningfully reduce total work and would delay the highest-value correctness fixes by 7-10 days for marginal benefit. Of the 46 gaps, only 10 (22%) are caused by game_loop.cpp making rule decisions that belong in the engine; the other 36 gaps live in step.cpp, legal_actions.cpp, scoring.cpp, or adjacency.cpp and are completely independent of the coupling problem. The master plan's current ordering (Phase 1 systemic fixes, Phase 2 card choice restoration, Phase 3 decoupling) is already close to optimal. The one adjustment worth making is pulling the `apply_ops_randomly()` replacement (Phase 2A) into Phase 1, since it blocks 4 high-impact game_loop gaps and is essentially a decoupling step disguised as a gap fix.

## Findings

### Gap distribution by file

| File | Gap count | Percentage of 46 |
|------|-----------|-------------------|
| step.cpp | 34 | 74% |
| game_loop.cpp | 14 | 30% |
| legal_actions.cpp | 3 | 7% |
| game_state.cpp | 3 | 7% |
| scoring.cpp | 1 | 2% |
| adjacency.cpp | 1 | 2% |
| policies.cpp | 1 | 2% |

(Totals exceed 46 because some gaps touch multiple files.)

### Gap distribution by root cause

| Root cause | Count | Would decoupling help? |
|------------|-------|------------------------|
| Randomized player choice (step.cpp) | 20 | No -- these replace `sample_up_to()` with `choose_country()` calls that already exist in step.cpp |
| Game loop making rule decisions | 10 | Partially -- decoupling would move the code, but the fix is the same lines of code either way |
| Wrong mechanic (coup-as-war, etc.) | 8 | No -- these are self-contained in step.cpp event handlers |
| Missing condition check | 5 | No -- one-line fixes in legal_actions.cpp, scoring.cpp, step.cpp |
| Missing card implementation | 3 | No -- these are promo cards excluded per CLAUDE.md |

### Which gaps would be trivially resolved by decoupling

**Zero gaps are trivially resolved by decoupling alone.** Decoupling moves code from game_loop.cpp into the engine layer, but the actual bug in each gap is not "code is in the wrong file" -- it is "code does the wrong thing." Specifically:

- **GAP-002/003 (opponent event ordering, space suppression):** The bug is a missing conditional in `apply_action_with_hands()` at line 719. Moving this function into a different file does not fix the conditional. The fix is 10-15 lines of logic regardless of where the function lives.
- **GAP-006/018/024/027 (apply_ops_randomly):** The bug is that `apply_ops_randomly()` makes random choices instead of policy queries. Replacing it with `apply_free_ops()` is the same work whether it lives in game_loop.cpp or a new engine file.
- **GAP-032/034/037 (Ask Not, Our Man in Tehran, Latin American Debt):** These are Cat-C card handlers in `apply_hand_event()` that randomize decisions. The fixes are per-card logic changes, not architectural.
- **GAP-042 (Glasnost extra AR):** The game loop grants a full AR instead of limited ops. The fix changes the flag semantics and resolution path -- same work either way.

### Which gaps are architecture-independent

**36 of 46 gaps (78%)** are completely architecture-independent:
- 20 randomized-choice gaps in step.cpp: each needs `sample_up_to()` -> `choose_country()` conversion
- 8 wrong-mechanic gaps: need new `apply_war_card()` function, Vietnam Revolts region check, CMC fix
- 5 missing-check gaps: one-line additions to legal_actions.cpp or scoring.cpp
- 3 missing-implementation gaps: promo card exclusion (resolved by deck removal)

### Risk analysis of each ordering

**Ordering A: Decouple first (Phase 3 before Phase 1+2)**

Pros:
- game_loop.cpp would be cleaner before gap fixes touch it
- Observation/FullState boundary would be established, making testing slightly cleaner
- The 10 game_loop gaps could be fixed in their "correct" final location

Cons:
- **7-10 days of pure refactoring before any correctness improvement.** During this time, all 46 gaps remain, training continues on a materially wrong engine, and every self-play game generated is wasted.
- **Phase 3 is the riskiest refactoring.** It touches mcts_batched.cpp (4906 lines, 35 `hands[]` access sites), ismcts.cpp (2154 lines, 18 access sites), and mcts.cpp (697 lines, 5 access sites). A regression here breaks the PPO pipeline.
- **No gap requires the Observation struct to fix.** The Observation/FullState split is about information boundaries for MCTS, not about rule correctness.
- **Decoupling does not change the action space.** The gaps that change the action space (GAP-004 space legality, GAP-005 ops placement, GAP-041 CMC) live in legal_actions.cpp and step.cpp, not in the coupling layer.
- **The 10 game_loop gaps still need the same fix logic.** Moving code first and then fixing it means touching those functions twice -- exactly the "touching the same files twice" concern, but in reverse order.
- **Risk of mid-refactor model breakage.** If decoupling accidentally changes game behavior (easy in a 4906-line file with 35 hand-access sites), the training pipeline breaks with no correctness upside.

**Ordering B: Gap-fix first (current master plan: Phase 1 -> Phase 2 -> Phase 3)**

Pros:
- **Immediate correctness gains.** Phase 1 fixes 16 gaps including the 8 highest-impact systemic bugs in 10-14 days. Self-play quality improves immediately.
- **Each gap fix is small and testable.** One card per commit, golden test per fix. Low regression risk.
- **Phase 2 (apply_ops_randomly replacement) is a natural mini-decoupling.** Replacing `apply_ops_randomly()` with `apply_free_ops()` already establishes the "engine makes rule decisions via policy callbacks, game_loop orchestrates" pattern for 4 gaps.
- **Phase 3 becomes simpler after gap fixes.** With all rule logic correct and tested, the Phase 3 refactor is a pure structural move with no behavior change. Easier to verify, easier to test, easier to review.
- **BC retraining happens once after Phase 1, not twice.** If we decouple first and then fix gaps, we'd need BC retraining after both.

Cons:
- Some game_loop.cpp code will be edited in Phase 1/2 and then moved in Phase 3. Estimated overlap: ~150 lines in `apply_action_with_hands()` and `apply_hand_event()`.
- The `apply_hand_event()` switch cases for Cat-C cards (32, 68, 78, 84, 98, etc.) live in game_loop.cpp now. After Phase 2 fixes them, Phase 3 would ideally move them into step.cpp. This means touching ~200 lines twice.

**Net assessment of the "touching files twice" concern:**

The overlap is approximately 350 lines of game_loop.cpp (out of 1689 total). However, the Phase 2 fixes and the Phase 3 move are largely orthogonal operations:
- Phase 2 changes the *logic* inside each case statement (replace random with policy query)
- Phase 3 moves the case statements to a different file

Moving code to a new file after fixing it is trivial (cut-paste-compile). Moving code first and then fixing it is also trivial. The total work difference is approximately zero. The sequencing question is really about which ordering delivers value sooner, and gap-fix-first wins decisively on that metric.

### Would decoupling create a clean interface that makes gap testing easier?

Not significantly. The current test infrastructure (`choose_country()`, `choose_option()`, `PolicyCallbackFn`) already provides the exact interface needed to test gap fixes. The Observation struct would help MCTS testing (verifying that search doesn't peek at opponent hands) but does not affect card-event unit tests.

### Does decoupling change the action space?

No. Phase 3 (Observation/FullState split) is defined in the master plan as a pure refactor with no behavior change. The action space changes come from Phase 1 (GAP-004 space legality, GAP-005 ops placement, GAP-041 CMC) which are gap fixes, not decoupling.

### Estimated work comparison

| Ordering | Total calendar days | Days to first correctness improvement | BC retraining events |
|----------|--------------------|-----------------------------------------|---------------------|
| A: Decouple first | 40-58 (same total) | 17-24 (Phase 3 + start Phase 1) | 2 (after decouple if behavior drifts, after gaps) |
| B: Gaps first (current plan) | 40-58 | 3-5 (Phase 0 promo exclusion) + 10-14 (Phase 1) | 1-2 (after Phase 1, optionally after Phase 2) |

## Conclusions

1. **The current master plan ordering (gaps first, decouple after) is correct.** 78% of gaps are architecture-independent and will not benefit from decoupling. The 22% that live in game_loop.cpp need the same fix logic regardless of where the code lives.

2. **The "touching files twice" cost is real but small.** Approximately 350 lines of game_loop.cpp will be edited in Phase 2 and then moved in Phase 3. This is ~2 hours of cut-paste-compile work, far less than the 7-10 day delay from doing decoupling first.

3. **Decoupling first would delay correctness by 7-10 days with no compensating benefit.** Every day the engine remains incorrect, self-play generates training data with wrong game dynamics. This is the dominant cost.

4. **Phase 2A (replace apply_ops_randomly) is already a targeted mini-decoupling.** It establishes the pattern of "engine uses policy callbacks for decisions" which is the core architectural improvement. After Phase 2A, the remaining game_loop rule decisions (GAP-002/003, GAP-032/034/037, GAP-042) follow the same pattern naturally.

5. **Phase 3 becomes safer and simpler after gap fixes.** With all 46 gaps closed and tested, Phase 3 is a pure structural refactor with comprehensive regression tests. Without gap fixes, Phase 3 would be refactoring code that is known to be wrong, making it harder to distinguish refactoring regressions from pre-existing bugs.

6. **The one optimization worth considering:** promote Phase 2A (apply_ops_randomly replacement) into Phase 1. This function is the single largest coupling point -- it lives in game_loop.cpp, makes rule decisions, and is the root cause of 4 high-impact gaps. Fixing it early establishes the `apply_free_ops()` pattern that all other card fixes in Phase 2B can follow.

## Recommendations

1. **Keep the current Phase 1 -> Phase 2 -> Phase 3 ordering.** Do not reorder decoupling before gap fixes.

2. **Promote Phase 2A (apply_ops_randomly -> apply_free_ops) into Phase 1.** This is the highest-leverage single change: it fixes 4 gaps (GAP-006, GAP-018, GAP-024, GAP-027), establishes the policy-callback pattern for all subsequent card fixes, and naturally begins the decoupling of game_loop from rule decisions.

3. **When executing Phase 3, move the Cat-C card handlers from game_loop.cpp into step.cpp as part of the Observation/FullState split.** The `apply_hand_event()` function (currently ~350 lines in game_loop.cpp) should become part of the engine's event dispatch, not the game loop. By that point, all its card handlers will already be correct from Phase 2, making the move trivial.

4. **Do not combine gap fixes with decoupling in a single commit.** Keep them as separate phases with separate BC retraining checkpoints. This preserves bisectability and makes regression diagnosis straightforward.

5. **Use the "touched twice" argument as motivation to keep Phase 2 and Phase 3 close together in calendar time.** If Phase 2 ends and Phase 3 starts within 1-2 weeks, the game_loop.cpp code will be fresh in memory and the move will be fast.

## Open Questions

1. **Should the 20 randomized-choice gaps in step.cpp (Phase 2B) be done before or in parallel with the apply_ops_randomly replacement (Phase 2A)?** The master plan says 2A first, which is correct because 2A establishes the `apply_free_ops()` pattern. But individual card fixes in 2B are independent of each other and could be parallelized across developers.

2. **How much of apply_hand_event() should move to step.cpp during Phase 3?** Currently the Cat-C cards (5, 10, 26, 32, 36, 45, 46, 47, 52, 68, 78, 84, 88, 95, 98, 101, 108) are handled in game_loop.cpp because they need hand access. After Phase 3 introduces the Observation/FullState split, these could be unified with the rest of the event dispatch in step.cpp by passing `FullState&` instead of `PublicState&`. This would eliminate the game_loop/step.cpp split for card events entirely.

3. **Is there value in extracting just the Observation struct (Phase 3A-3B) early, without the full MCTS refactoring (Phase 3C-3E)?** Defining the struct costs ~1 day and would document the information boundary. But it provides no practical benefit until the MCTS files are refactored to use it, so this is a documentation-only early step.
