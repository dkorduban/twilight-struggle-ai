# Opus Analysis: Nightly progress + next autonomous move
Date: 2026-04-21T17:39:55Z
Question: Analyze and summarize the nightly autonomous work (Apr 20 21:00 UTC → Apr 21 17:00 UTC), then propose the single most valuable next autonomous move. Evaluate on merit: (A) human-log replay bug oracle, (B) frame-migration completion, (C) stale task cleanup. Plus: summarize nightly engine-fix progress and recommend the highest-EV move given the v34/v35/v36 0.627 combined plateau.

## Executive Summary
Finish Plan B engine fixes tonight (SALT +2, Yuri timing, SA Unrest mode, LatAm Debt branch, Kitchen Debates reveal are still open) AND run a validator-triage pass on the 51 human games using the already-built `validate_game()` harness (Option A is ~30 lines of CLI, not a new system). Both are GPU-free, high-signal, and eliminate a priors-poisoning risk for v37 teacher distillation (v32 learned on the pre-fix engine; distilling it onto a now-corrected engine injects stale priors). v37 launches cleaner in 24-48h once engine is stable; frame migration (Option B) is latent cleanup and should be deferred; Option C collapses because no in-repo TaskList.md exists — the "26 tasks" are a session-local TodoWrite state not visible here.

## Findings

### Nightly engine-fix summary (what landed, what remains)

**Committed to main (a335495 and onward, 20 commits across Apr 21):**
- `a335495` inline fixes: Defectors action-round -1 VP (was -2), Iron Lady +Argentina / wipe-UK, `run_traced_game.py:128` turn-boundary attribution (5 scoring-card false positives eliminated). 86/89 Python tests pass (3 pre-existing ISMCTS fails).
- Independent Reds cluster (`a3a17d4`, `652d47f`, `616fe0a`, `0c63f81`, `bb0e0fb`): +1 to all-EE replaced with choose-one equalize via FrameKind::CountryPick + frame_parity hash updated + unit test in `tests/cpp/test_card_choice_events.cpp`.
- We Will Bury You cluster (`63a911a`..`675f397`, 11 WIP commits): `we_will_bury_you_pending` + `we_will_bury_you_turn_ar` flags; VP now defers until next US AR if not canceled by UN Intervention; unit tests present at `test_card_choice_events.cpp:78-99`.
- NORAD trigger fix (`2258bdc`): end-of-USSR-AR hook + `resolve_norad_live()` + tests at `test_public_state.cpp:447-481`. Previously the flag was set but dead.
- Camp David block (test at `test_public_state.cpp:691-710`): `step.cpp:1345` sets `camp_david_played`; `rule_queries.hpp:82` gates card 13 Arab-Israeli. Verified live.
- Teacher rollout collector (`5caddf7`, 812 lines): smoke-tested 10 games → 141 rows matching `train_baseline.py --teacher-targets` schema. Ready.
- Earlier nightly WIP: Southeast Asia final scoring, scoring auto-win end reason, headline legality fizzle, cat-c subframe state, war-card milops/rolls, bear-trap forced discard, coup milops from printed ops, NORAD cancel without Canada control, nuclear subs turn-cleanup expiry, wargames end-reason labels.

**Plan B remainders NOT landed:**
| # | Item | File:line | Status | Effort |
|---|---|---|---|---|
| 1 | SALT Negotiations DEFCON +2 (currently +1) | `step.cpp:1103`, `hand_ops.cpp:429` | OPEN | ~15 min |
| 2 | Yuri and Samantha timing (awards past attempts) | `step.cpp:1851` (`next.vp += next.space_attempts[US]`) | OPEN | ~30 min |
| 3 | South African Unrest mode choice | `step.cpp:1215` case 56 | OPEN | ~1 h (FSM) |
| 4 | Latin American Debt Crisis US-discard branch | `step.cpp:1725` case 98 | OPEN | ~1 h |
| 5 | Kitchen Debates hand-reveal (info only) | `step.cpp:1141-1159` case 71 | OPEN | low priority, info-only |
| 6 | Che non-BG restriction (case 83) | `step.cpp` | OPEN, low impact | defer |
| 7 | Special Relationship target pool | `step.cpp:37` | OPEN, low impact | defer |

**Tests status:** C++ `ctest` shows **54/54 pass** (verified). Python `pytest` not re-run this session but Plan B commits report 86/89 (3 pre-existing ISMCTS fails unchanged). `test_frame_parity.cpp` was kept in sync — WWBY + NORAD + SALT + camp_david flags all hash-included.

### Option A: Human-log replay harness (feasibility, cost, expected yield)

**PREMISE CORRECTION — the harness already exists.** `python/tsrl/etl/validator.py:1309` defines `validate_game(text, game_id, all_card_ids)` and `:1395` defines `validate_log_dir()`. No new system is needed; only a CLI wrapper (~30 lines) if we want a standalone script.

**Empirical run (just executed this session):**
```
games=51   decisions=6148   parse_failures=0   unknown_lines=0
violations by kind:
  CARD_EXCLUDED_BY_REDUCER   1805   (NOISE — smoother-conservatism; ignore)
  SCORING_VP_MISMATCH         171   (HIGH SIGNAL)
  TARGET_ILLEGAL               67   (HIGH SIGNAL)
  RESHUFFLE_EMPTY_DISCARD       5   (MEDIUM)
  HEADLINE_ORDER_MISMATCH       3   (LOW)
```

**Only 238 violations are real bug-oracle candidates** (171 + 67). Do not frame the 2051 total as "bugs"; CARD_EXCLUDED_BY_REDUCER is dominated by smoother-conservatism (unknown cards auto-excluded from support, legitimate in expectation).

**Spot-check of signal quality (manually inspected):**
- `tsreplayer_14` Europe Scoring T2 AR3: log says US +5 VP, engine says -3 (USSR +3). Cause unclear without deeper trace — could be missing influence from a pre-fix event that didn't reduce (e.g. Iron Lady pre-fix wouldn't have wiped USSR from UK, giving USSR control-count that no longer exists).
- `TARGET_ILLEGAL country 57` appears in ≥10 games (57 = Morocco-ish slot; likely a specific card-effect or adjacency gap). This is reproducible reducer/engine disagreement on ONE country — high-value narrow bug.
- `RESHUFFLE_EMPTY_DISCARD` = 5: real, small, fixable.

**Expected yield:** Opus-2's card audit found 6 bugs across 100 cards by static review. The validator triage gives **238 live dynamic violation points** against real expert play, each pointing at a specific (game, turn, AR, card, target). Even if only 10% of SCORING_VP_MISMATCH are unique engine/reducer bugs (many will be same root cause), that's ~15-20 new candidate bugs — comparable to the audit yield but for free (no Opus budget, no GPU).

**Crucial caveat:** Many SCORING_VP_MISMATCH likely trace back to **already-fixed cards** (Iron Lady, Independent Reds) because the reducer runs card effects at parse time — re-running validator AFTER all Plan B fixes land will reduce the count, and any residual is the target set.

**Minimum viable "ship":** (a) re-run validator post-Plan-B, (b) group violations by (kind, card_id, country_id) to find the top-5 unique root causes, (c) attach one golden test per root cause. Effort: 1-2 hours of Python on top of the existing harness.

### Option B: Frame migration completion (scope, blocker status)

The frame machinery (`cpp/tscore/decision_frame.hpp` + FrameKind enum, 11 kinds) is live. `test_frame_parity.cpp` hashes cover all recently added flags (norad_active, salt_active, we_will_bury_you_pending, we_will_bury_you_turn_ar — lines 131-140). The recent engine-fix work (Independent Reds CountryPick frame, WWBY frame_parity sync) proves **the frame path and the legacy path are being kept in parity** — no divergence blocking.

**What "full migration" would mean:** remove the `game_loop.cpp` legacy non-frame branch (3843 lines), collapse `apply_action` and `apply_action_live` into one path, retire frame_stack_mode toggles. That is a large refactor touching 131 call sites of `DecisionFrame`/decision_frame and 3843 lines of game_loop — closer to 2-4 engineer-days with regression risk.

**Blocking assessment:** NOT blocking Month-3 goals. The frame path carries the online hot path; the legacy path survives for parity tests and a few fallbacks. No current roadmap item (Dirichlet noise, ISMCTS, parallel MCTS, Elo infra, online server) requires the legacy path to be deleted. This is **latent cleanup**.

**Recommendation:** defer Option B until Month 3 slowdown or until a concrete subsystem (parallel MCTS, async root search) requires single-path semantics.

### Option C: Task list cleanup (live vs obsolete)

**PREMISE CORRECTION — there is no in-repo TaskList.md or tasks/ directory.** `find` confirms: no `TaskList*`, no `results/tasks/`. The "26 tasks with #83-90, #105, #96, #98/99/103/104" referenced in the prompt are a session-local TodoWrite / TaskRead state not persisted to disk. From this agent's vantage point, the authoritative to-do list is `results/continuation_plan.json["next_tasks"]` which already reflects the post-plateau state:
1. v37 distill Stage 1 (primary, Opus rec)
2. v37 distill Stage 2 (if Stage 1 passes)
3. v35 seed replicate (secondary)
4. FALLBACK: dense reward + lr=1e-6 retry; 10k self-play diagnostic
5. DO NOT RUN: us-specialist PPO, ISMCTS@200, 32-dim NP scalars (all falsified)

Because the session task list isn't inspectable from this subagent, the useful recommendation is:
- When resuming, prune any task mentioning `gnn_v14`, `gnn_v15`, `card_attn PPO`, `AWR for policy`, `us_only_v5 PPO`, `FiLM init sweep`, `alloc_head`, `Phase 2b region scalars` — all falsified per `autonomous_decisions.log` and memory notes.
- Keep live: Plan B remainders (1-5 above), v37 Stage 1 once engine stable, v35 seed replicate, human-log validator triage, match-cache hash-identity refactor (`project_match_cache_hash_identity` memory), Dirichlet/temperature root noise (Month-3 #1 goal still unstarted).

### Recommendation rationale

**Why engine-fix-completion + validator triage beats v37 launch tonight:**

1. **Priors-poisoning risk.** v32 trained on an engine that awarded Defectors -2 VP (action-round USSR), gave Iron Lady zero Argentina/UK effect, dropped NORAD entirely, and awarded WWBY +3 VP immediately. The policy learned to exploit / avoid those exact miscalibrations. Distilling v32's softmax onto a corrected engine pushes the student toward decisions that are now wrong. The correct sequence is: (a) finish engine fixes, (b) re-benchmark v32 on the fixed engine (expect transient 3-5pp dip per Opus-1 note), (c) only then decide between v37 distill vs. fresh PPO from v32 weights.

2. **238 live bug signals already on disk.** The 51-game validator result is the best bug oracle we have and it cost zero GPU. Triaging just the top-5 most-frequent (SCORING_VP_MISMATCH for specific cards, TARGET_ILLEGAL for country 57) is a few hours of work that could surface the remaining big-ROI cards before we commit weeks of PPO to v32-era priors.

3. **Engineering cost is low.** Plan B remainders 1-4 total ~2.5 engineer-hours + 30 min tests (SALT +2 is trivial, Yuri is a one-line sign flip, SA Unrest + LatAm Debt need a small FSM add each). Validator triage + top-5 root-cause identification: 1-2 hours of Python.

4. **GPU cost is zero**, preserving the 4GB 3050 for the eventual v37 run on a stable engine.

5. **Option B (frame migration)** doesn't unblock any current goal. `test_frame_parity` proves the two paths stay in sync as new flags land, so the dual-path cost is bounded. Defer.

**Why NOT v37 tonight:** the teacher (v32) encodes pre-fix-engine priors. Launching Stage 1 BEFORE engine stabilizes is the "worst of both worlds" — student inherits stale behavior but must execute on the fixed engine, and at epoch-30 you cannot cleanly attribute a low score to either the distillation pipeline or the priors mismatch.

**Why NOT human-log triage ONLY:** the engine fixes already queued in WIP commits are the proximate source of many reducer disagreements. Running triage before Plan B lands will double-count bugs that are already fixed-in-progress.

## Conclusions

1. Nightly work is substantial: 20 commits, 5 engine bugs fixed (Defectors, Iron Lady, Independent Reds, WWBY, NORAD) plus Camp David block flag wired through, plus teacher rollout collector ready for v37. All 54 C++ tests pass.
2. Plan B is ~60% complete; remainders are SALT +2 (trivial), Yuri timing (trivial), SA Unrest mode choice (FSM), LatAm Debt US-discard branch, and Kitchen Debates hand-reveal (info-only, low priority).
3. The "human-log replay harness" already exists in `python/tsrl/etl/validator.py`. A one-session run on all 51 games produced 238 high-signal violations (171 SCORING_VP_MISMATCH + 67 TARGET_ILLEGAL + 8 other), zero parse failures, zero unknown lines. This is the highest-signal engine-quality oracle on disk and cost nothing.
4. Frame-based migration is parity-maintained (test_frame_parity covers all new flags) but not fully collapsed. Not blocking any current goal; defer.
5. The v34/v35/v36 plateau confirmation (0.627 combined, US side stuck at 0.50) plus Opus-1+Opus-2 findings that NORAD alone can swing US WR +2-4pp and LatAm Debt / SALT add another +1-2pp combined means **engine correctness is the current largest unlocked lever**, larger than any hyperparameter or architecture change still on the board.
6. v37 teacher distillation is correctly built and smoke-tested, but launching it BEFORE the engine stabilizes risks injecting v32's pre-fix priors into a student that must play on a corrected engine.
7. The session TodoWrite task list is not inspectable from an isolated subagent; in-repo canonical todo lives in `results/continuation_plan.json["next_tasks"]`, which is already post-plateau and post-Opus-advice.

## Recommendations

**Primary — launch tonight:**
1. **Finish Plan B (SALT +2, Yuri sign flip, SA Unrest mode choice, LatAm Debt US-discard branch)** — dispatch Codex in a worktree; kill criteria: all 54 C++ tests + >=86 Python tests still pass. Add one focused unit test per fix under `tests/cpp/`. Estimated cost: 3 engineer-hours, 0 GPU-hours. Expected gain: +2-4 pp US WR in benchmarks once v32 is re-anchored.

**Secondary — tonight (parallel, no GPU):**
2. **Validator triage pass.** Write a 30-line CLI wrapper `scripts/validate_replays.py` over `validate_log_dir()`; re-run AFTER Plan B remainders land; group violations by (kind, card_id) and produce a top-5 root-cause list in `results/analysis/`. Expected yield: 5-10 unique residual bugs that are NOT in the Opus-1 / Opus-2 lists.
3. **Re-benchmark v32 on the fixed engine** at 500 games/side seed=50000+50500 once Plan B lands. If v32 drops below 0.60 combined, the behavioral change is large enough to warrant BC-on-fixed-engine before any PPO restart (consistent with the memory note "BC before PPO for arch/engine changes"). If v32 stays ≥0.63, proceed straight to v37.
4. **v37 Stage 1 — launch in 24-48h, NOT tonight.** Once engine is stable, collect 3k-5k teacher rollouts with `collect_teacher_rollouts.py` (teacher = v32 on the FIXED engine so its softmax reflects corrected dynamics) and start `train_baseline.py --teacher-targets`. Kill gate: epoch-5 bench combined < 0.55 abort. Success: epoch-30 ≥ 0.60. Est cost: 2 GPU-hours for rollout collection + 4-6 GPU-hours for 30 epochs.

**Explicitly defer:**
5. Frame-based migration completion (Option B) — no current blocker, 2-4 engineer-days, defer to a Month-3 slowdown.
6. Session TodoWrite cleanup (Option C) — not actionable from an isolated agent without the live TodoWrite view; prune when resuming.

## Open Questions

1. **Re-run validator after Plan B** — how much of the 171 SCORING_VP_MISMATCH + 67 TARGET_ILLEGAL collapses to already-fixed cards (Iron Lady, Independent Reds, WWBY)? Reducer must be re-run to know; the parser is stateless but `reduce_game` applies card effects.
2. **v32 post-fix dip magnitude** — Opus-1 estimated 3-5pp transient. If larger (e.g. 10pp), the chain itself needs re-anchoring and BC-on-fixed-engine becomes mandatory.
3. **NORAD test coverage** — `test_public_state.cpp:447-481` exercises `resolve_norad_live`; unclear whether it covers the DEFCON-2 end-of-USSR-AR trigger end-to-end through `apply_action_live`. Audit before declaring NORAD fully fixed.
4. **SALT +2 interaction with early-war DEFCON** — if SALT headlines at DEFCON 3 and pushes to 5 (was 4 via +1), does any card legality flip unexpectedly? Unit test should exercise at DEFCON 2/3/4 starts.
5. **Yuri timing fix requires engine state** — awarding VP for FUTURE US space attempts needs either a deferred hook at end-of-turn or a live trigger on `advance_space_track` for the US side while `yuri_active`. Probably adds a flag + end-of-turn commit similar to WWBY.
6. **Country 57 recurring TARGET_ILLEGAL** — is this a specific card's target pool bug, a parser cards-csv field mismatch, or an adjacency-dict gap in Python? Spot-check one instance in raw log to classify.
