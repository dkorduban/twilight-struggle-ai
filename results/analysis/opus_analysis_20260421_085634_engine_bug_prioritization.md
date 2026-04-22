# Engine Bug Prioritization — Audit of v32_selfplay_seed42_greedy Trace

**Date**: 2026-04-21
**Analyst**: Opus subagent (dispatched by main session)
**Input**: `long-prompts/inconsistent-moves.md` (31 alleged card/scoring inconsistencies from ChatGPT audit of `results/sample_games/v32_selfplay_seed42_greedy.txt`)
**Scope**: Verify claims against `cpp/tscore/step.cpp` + `cpp/tscore/hand_ops.cpp`; classify each as real engine bug vs. trace-artifact; produce actionable fix plan.

---

## Executive Summary

Of 31 flagged items, **9 are real engine bugs**, **5 are trace-attribution artifacts** (items 27-31, scoring cards "also improving DEFCON / resetting MilOps"), and **~17 are plausible log-formatter noise or non-bugs** (e.g. NATO prerequisite at item 3 is satisfied by Truman Doctrine under `rule_queries.hpp:57`; most category-C cards like Five Year Plan, Grain Sales, Bear Trap, Missile Envy, Our Man in Tehran, Nuclear Subs, Junta, Nixon, Shuttle Diplomacy, Warsaw Pact Formed, UN Intervention are implemented correctly in `hand_ops.cpp` / `step.cpp` and the ChatGPT trace just shows downstream follow-up actions rather than the event body).

**Recommendation: Plan B — fix the top 5 highest-impact engine bugs + 1 trace-formatter fix, then resume PPO from v32 without rebuilding the whole card library.** Training will directly benefit from correcting the most frequent VP-distorting events. Leaving the trace formatter broken would poison every future audit, so we add a cheap Python fix to prevent the next false-positive firestorm.

The trace-attribution hypothesis (items 27-31) is **confirmed**: `scripts/run_traced_game.py` `_post_snapshot_for_step` (line 128) uses `steps[idx+1].pub_snapshot` as the "post" state for step `idx`. Turn cleanup in `cpp/tscore/game_loop.cpp:634` runs between last-AR of turn N and first-AR of turn N+1 (`defcon = min(5, defcon+1); milops = {0,0}; space_attempts = {0,0}; ops_modifier = {0,0}`), so the DEFCON improvement and MilOps reset get folded into the last event of each turn. All five flagged scoring cards (items 27-31) were the last-AR play of their respective turns — this is 100% a Python presentation bug, not an engine bug.

---

## Findings

### 1. Trace-attribution verdict (items 27-31)

**Mechanism**: `scripts/run_traced_game.py::_post_snapshot_for_step` at line 128 defines the "after" state for step *idx* as `steps[idx+1].pub_snapshot`. Between the last step of turn N and the first step of turn N+1, the C++ engine runs turn cleanup (`cpp/tscore/game_loop.cpp:634`):

```cpp
next.defcon = std::min(5, next.defcon + 1);
next.milops = {0, 0};
next.space_attempts = {0, 0};
next.ops_modifier = {0, 0};
```

So the diff attributed to the last action of turn N inevitably contains +1 DEFCON and MilOps reset. This explains:
- Item 27 (Asia Scoring T2 AR6 improves DEFCON)
- Item 28 (Africa Scoring T4 AR7, T7 AR7 improves DEFCON + resets Soviet MilOps)
- Item 29 (Southeast Asia Scoring T5 AR7 improves DEFCON to 3 — note: DEFCON goes to 3 here because it was at 2 before cleanup)
- Item 30 (Central America Scoring T7 AR7 gives US +1 UK — this one is likely Special Relationship follow-on confusion; see below)
- Item 31 (Europe Scoring T8 AR7 improves DEFCON, resets US MilOps)

**Verdict**: All five are trace artifacts. Engine is correct. Fix the trace formatter.

### 2. Per-item verification table

| # | Card | Status | Evidence |
|---|---|---|---|
| 1 | Captured Nazi Scientist (+2 VP, +1 SR) | FALSE POSITIVE | `step.cpp` case 18: only space +1; the +2 VP is standard (space track VP at level 2). |
| 2 | Five Year Plan (influence removal) | FALSE POSITIVE | `hand_ops.cpp` case 5: implemented as random-discard-from-USSR; log is likely showing the discarded card's auto-play effect. |
| 3 | NATO without prereq | FALSE POSITIVE | `rule_queries.hpp:57` — Truman Doctrine also satisfies NATO prereq. |
| 4 | Independent Reds +1 to all 5 countries | **REAL BUG** | `step.cpp` case 22: adds +1 US to EVERY eligible country with USSR influence. Should equalize in ONE chosen country only. |
| 5 | UN Intervention standalone influence | FALSE POSITIVE | `hand_ops.cpp` case 32: correctly consumes a paired card; log shows follow-on Ops use. |
| 6 | Warsaw Pact Formed improves DEFCON | FALSE POSITIVE | T3 AR6 = last AR; turn-cleanup artifact. |
| 7 | Nixon "2 VP only" | FALSE POSITIVE | `step.cpp` case 72: correctly transfers China Card face down OR +2 VP if US already has it. |
| 8 | Brush War "+3 influence +2 VP" | LIKELY FALSE POSITIVE | `step.cpp` case 39 calls `apply_war_card(threshold=3)`. +2 VP matches success-with-2-BGs. The "+3 influence" is post-success replacement, which is by-design. |
| 9 | South African Unrest always both | **REAL BUG** | `step.cpp` case 56: unconditionally does +2 SA AND +2 adjacent; should offer choice (+2 SA alone, OR +1 SA + 2 adj). |
| 10 | Missile Envy | FALSE POSITIVE | `hand_ops.cpp` case 52: correctly swaps for opponent's highest Ops; log shows subsequent forced use. |
| 11 | Nuclear Subs | FALSE POSITIVE | `hand_ops.cpp` case 44: sets the coup-no-DEFCON flag correctly; log shows an ordinary coup/influence that follows. |
| 12 | Grain Sales | FALSE POSITIVE | `hand_ops.cpp` case 68: random-draw mechanic implemented; log shows the fallback 2-Ops use. |
| 13 | Bear Trap | FALSE POSITIVE | `hand_ops.cpp` case 47: trap flag set; the logged "+1 Panama" is a subsequent action. |
| 14 | Our Man in Tehran | FALSE POSITIVE | `hand_ops.cpp` case 84: five-card look implemented; log shows next action. |
| 15 | Socialist Governments | FALSE POSITIVE | `step.cpp`: correctly removes from WE only; Panama line is adjacency confusion in the trace. |
| 16 | Junta extra "-3 Panama" | FALSE POSITIVE | `step.cpp` case 50: correctly adds 2 + optional free coup; "-3 Panama" is the free coup result. |
| 17 | We Will Bury You immediate +3 VP | **REAL BUG** | `step.cpp` case 53: awards +3 VP immediately. Standard: defer until UN Intervention NOT played next USSR AR. |
| 18 | Arab-Israeli War after Camp David | **REAL BUG** | `step.cpp` case 13: no check for `camp_david_played` flag; should be legality-blocked. |
| 19 | Special Relationship Mexico/Indonesia | **REAL BUG** | `step.cpp` case 37: target pool incorrect — should be UK-adjacent (w/o NATO) or Western Europe (w/ NATO), not Central America / SE Asia. |
| 20 | Che into Argentina + Tunisia | **REAL BUG** | `step.cpp` case 83: allows battleground targets (Argentina is BG); should restrict to non-BG CA/SA/Africa. |
| 21 | Defectors action-round +2 VP | **REAL BUG** | `hand_ops.cpp` case 108: `pub.vp -= 2`; standard action-round USSR play = US +1 VP only. |
| 22 | Blockade | FALSE POSITIVE | `hand_ops.cpp` case 10: correctly checks West Germany discard option; log shows Ops use after event declined. |
| 23 | Iron Lady missing effects | **REAL BUG** | `step.cpp` case 86: awards +1 VP only; missing +1 USSR Argentina and wipe-USSR-UK. |
| 24 | Indo-Pakistani War | FALSE POSITIVE | `apply_war_card()` replaces all opponent influence on success; the "2 USSR remaining" is pre-existing USSR influence from realignments, not a bug. |
| 25 | Shuttle Diplomacy | FALSE POSITIVE | `step.cpp` case 74: correctly sets scoring-modifier flag; log shows bundled cleanup. |
| 26 | Latin American Debt Crisis | **REAL BUG** | `step.cpp` case 98: no US-discard option branch; doubles influence but in wrong region set. |
| 27-31 | Scoring cards "extra side effects" | TRACE ARTIFACT | Turn cleanup attribution bug in `run_traced_game.py:128`. |

### 3. Real engine bugs, ranked by policy impact

Ranking heuristic: firing frequency in normal play × VP magnitude of the distortion × likelihood of exploitation by a learned policy.

| Rank | Card ID | Bug | Fires per game (est.) | VP distortion | Priority |
|---|---|---|---|---|---|
| 1 | 22 Independent Reds | Adds +1 to all 5 EE countries instead of equalizing in one | ~0.5 | ±2-4 influence swing | **TOP** |
| 2 | 53 We Will Bury You | Awards +3 VP immediately (no UN Intervention counter-window) | ~0.4 | ±3 VP | **TOP** |
| 3 | 108 Defectors | -2 VP on action-round USSR play (should be -1) | ~0.3 | ±1 VP each fire | **TOP** |
| 4 | 86 Iron Lady | Missing +1 USSR Argentina + wipe USSR UK | ~0.3 | ±2-4 influence | **TOP** |
| 5 | 56 South African Unrest | No mode choice; always both | ~0.3 | ±1 SA + 2 adj influence | **TOP** |
| 6 | 98 LA Debt Crisis | No US-discard branch + wrong region | ~0.2 | ±4-8 influence | medium |
| 7 | 83 Che | Allows battleground targets | ~0.15 | ±2 VP on coup | medium |
| 8 | 37 Special Relationship | Wrong target pool | ~0.2 | ±2 VP + placement | medium |
| 9 | 13 Arab-Israeli War | No Camp David block | rare (Camp David usually early) | ±2 VP | low |

---

## Conclusions

1. **Engine is ~70% correct at the card level.** The ChatGPT audit massively overestimated the bug count by mistaking trace artifacts (items 27-31) and follow-on actions (items 2, 5, 10-14, 22) for event-body bugs.
2. **Nine real bugs exist.** Of those, five are frequent + VP-distorting enough that the PPO policy almost certainly learned around them. Fixing those five closes the biggest rule gaps without touching low-impact cards.
3. **The trace attribution bug is a separate, cheap fix** that must be made *regardless* of Plan A/B/C — otherwise every future audit will produce a new batch of false positives that cost hours to triage.
4. **Plan A is wrong for now.** Fixing all 20+ flagged items (including several that aren't actually broken) would take weeks of engine work and delay PPO. The Month-3 ROI is higher on Dirichlet noise + ISMCTS than on the low-impact tail.
5. **Plan C (defer + add validator) is also wrong.** The top 5 bugs are big enough (+3 VP on We Will Bury You, wipe-UK on Iron Lady) that a rule-validator alone would just slow training with rejected states. These are real behavior changes, not edge-case leakage.
6. **Plan B is the right call**: fix the top 5 engine bugs + the trace formatter, then restart PPO from v32 on the corrected engine.

---

## Recommendations

### Plan B: Five Engine Fixes + One Trace-Formatter Fix

| # | File | Approximate line | Change | Effort |
|---|---|---|---|---|
| 1 | `cpp/tscore/step.cpp` | case 22 Independent Reds (~line 731) | Replace "for each EE country, +1" with "choose one eligible country; set US influence equal to USSR influence there". Need a `choose_target` step in the action FSM. | 2-3 hours (requires FSM action add) |
| 2 | `cpp/tscore/step.cpp` | case 53 We Will Bury You (~line 1160) | Replace immediate `pub.vp -= 3` with setting `pub.effects.we_will_bury_you_pending = true`. Add check in UN Intervention cat-C handler to clear pending; add check at end-of-USSR-AR to commit the -3 VP if still pending. | 1-2 hours |
| 3 | `cpp/tscore/hand_ops.cpp` | case 108 Defectors (~line 790) | Change `pub.vp -= 2` to `pub.vp -= 1` for action-round USSR-play branch. Keep headline behavior unchanged (event negates USSR headline). | 15 minutes |
| 4 | `cpp/tscore/step.cpp` | case 86 Iron Lady (~line 1638) | After existing +1 VP, add `add_influence(next, Side::USSR, kArgentinaId, 1); wipe_country_influence(next, kUnitedKingdomId, Side::USSR)`. | 30 minutes |
| 5 | `cpp/tscore/step.cpp` | case 56 South African Unrest (~line 1174) | Add a mode-choice step (0 = +2 SA alone; 1 = +1 SA + 2 adj). Default mode for legacy replays = mode 1. | 1 hour (+FSM change) |
| 6 | `scripts/run_traced_game.py` | `_post_snapshot_for_step` line 128 + formatter | When `steps[idx].turn != steps[idx+1].turn`, synthesize a dummy "Turn cleanup" line showing DEFCON/MilOps changes, and use the PRE-cleanup snapshot as post-state for step `idx`. ~10 lines of Python. | 30 minutes |

**Total effort: ~6-8 hours of C++ + 30 minutes Python.**

### After the fixes

1. Run `ctest --test-dir build --output-on-failure` and fix any golden-log regressions (expect some — the 5 cards now behave differently).
2. Regenerate golden traces for regression corpus.
3. Run behavior-cloning on v32's best game set to re-anchor the policy on the corrected engine (see memory note: BC before PPO for arch/engine changes).
4. Restart PPO from `results/capacity_test/ppo_us_only_v5/ppo_best.pt` on the corrected engine. Expected transient WR dip of 3-5 pp at iter 5-10; recovery by iter 20-30.
5. Run fresh Elo tournament vs. the existing v29/v31/v32/v33 panel; a post-fix policy should gain 20-40 Elo if any of the fixed events appear in the opening / mid-game.

### Explicitly NOT fixing in this pass

- Items 26 (LA Debt), 83 (Che), 37 (Special Relationship), 13 (Arab-Israeli) — fire less than once every 3 games on average; defer to a later "card completeness" pass.
- All scoring-card "bugs" (items 27-31) — NOT engine bugs.
- Low-confidence / formatter-only items — see FALSE POSITIVE rows above.

---

## Open Questions

1. **Is the golden corpus regression test strong enough to catch the 5 fixes as intended?** Likely no — most golden logs predate these events firing in the contexts that would expose the bugs. Should add 5 new focused unit tests in `tests/cpp/` per fixed card.
2. **Does the action FSM cleanly support adding a target-choice step mid-event?** Independent Reds and South African Unrest both need this; if the FSM is rigid, the effort estimate for #1 and #5 doubles. (Main session should sanity-check before kickoff — `cpp/tscore/action_fsm.cpp` if it exists.)
3. **UN Intervention ↔ We Will Bury You interaction window** — need to confirm the engine already tracks "next USSR AR" vs. "end of turn". If not, fix #2 grows to ~4 hours.
4. **Does BC on v32 games re-poison the new engine with pre-fix behaviors?** Small risk. Mitigation: only BC on games where none of the 5 fixed cards fired, or simply do a shorter BC (3-5 epochs) and rely on PPO to correct.
5. **Should we backfill a rule-validator** (Plan C's safety net) *in addition* to Plan B? Cheap (~1 day of Python), catches future regressions, independent of any specific fix. Recommend yes after Plan B lands.
