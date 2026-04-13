# Engine Refactor Master Plan
**Date:** 2026-04-13
**Scope:** 46 rule gaps + engine/search uncoupling + regression tests + Python engine deprecation + dead code removal

---

## Executive Summary

This plan sequences all engine correctness and architecture work into six phases over an estimated 8-12 weeks. It closes all 46 known rule gaps, decouples the search layer from engine internals, builds comprehensive regression tests, deprecates the Python engine (6,541 lines), and removes dead code. The key constraint is that PPO training must never break: every phase is designed so the training pipeline can continue on the previous engine version while a new one is validated.

The plan is ordered by **blast radius** (how many downstream systems a change touches) and **correctness leverage** (how much game-play accuracy improves per change). Foundational mechanics that affect every game (ops placement, space race, opponent-event ordering) come before individual card fixes.

**Total estimated work:** ~150-200 files touched, ~80 new test cases, ~3000 lines of new C++ code, ~2000 lines removed.

---

## Constraints

1. **PPO training continuity.** The `ppo_loop_step.sh` pipeline uses `mcts_batched` and the C++ game loop. Every phase must maintain a working binary that the pipeline can link against. We use a version flag (`kEngineVersion`) bumped per phase to detect stale binaries.
2. **Model action heads are fixed.** The factorized action model (card, mode, country, value) is not redesigned. Any new sub-action queries (e.g., event decisions) flow through the existing `PolicyCallbackFn` / `EventDecision` mechanism.
3. **C++ is source of truth.** The Python engine is a legacy wrapper used only by a handful of scripts and the ETL validator. It is not updated; it is replaced.
4. **ISMCTS must stay functional.** Determinization-based search in `ismcts.cpp` cannot be broken. Refactoring the observation boundary (Phase 3) must pass ISMCTS smoke tests at every step.
5. **Promo cards (109, 110, 111) are permanently out of scope** per CLAUDE.md. They must be excluded from the deck, not implemented.
6. **No JAX, Rust, or new heavy dependencies.**

---

## Phase 0 — Foundations (No Behavior Change)

**Goal:** Clean the workspace, build test infrastructure, remove dead code, and document the target interface contract. No game behavior changes.

**Estimated complexity:** M (Medium)
**Duration:** 3-5 days
**Training impact:** None. Fully backward-compatible.

### 0A. Dead code removal

| File | Lines | Action | Rationale |
|------|-------|--------|-----------|
| `cpp/tscore/mcts_search_impl.hpp` | 544 | Delete | Not `#include`d by any `.cpp`; confirmed by grep. Its structs (`ModeDraft`, `CardDraft`, `ExpansionResult`, `SelectionResult`) are duplicated inline in `mcts.cpp`, `mcts_batched.cpp`, and `ismcts.cpp`. |
| `python/tsrl/engine/mcts.py` | 712 | Mark deprecated (add `warnings.warn`) | Python MCTS is unused in the training pipeline; C++ `mcts_batched` replaced it. Keep for now (used by `scripts/run_mcts_game.py`), deprecate in Phase 5. |

**Files to modify:**
- `cpp/tscore/mcts_search_impl.hpp` — delete
- `cpp/CMakeLists.txt` — remove from any header lists if present
- `cpp/tscore/card_properties.hpp` — remove comment referencing `mcts_search_impl.hpp` (line 8)

**Test requirement:** `cmake --build build -j && ctest --test-dir build` passes.

### 0B. Engine version constant

Add `constexpr int kEngineVersion = 1;` to `cpp/tscore/game_state.hpp`. Expose via bindings as `tscore.engine_version()`. The PPO pipeline's freshness check can use this.

**Files to create/modify:**
- `cpp/tscore/game_state.hpp` — add constant
- `bindings/tscore_bindings.cpp` — expose constant

### 0C. Golden replay test harness (C++)

Create `tests/cpp/test_golden_replays.cpp`: a data-driven test that loads a set of JSON fixtures, each specifying an initial `PublicState`, a sequence of `ActionEncoding` + `Side`, expected intermediate states, and expected final state hash. The fixture format:

```json
{
  "name": "korean_war_basic",
  "gap_id": "GAP-008",
  "setup": { "influence": {...}, "defcon": 4, "turn": 1, ... },
  "actions": [
    {"card_id": 11, "mode": "Event", "side": "USSR", "expected_vp_delta": -2}
  ],
  "expected": { "vp": -2, "milops_ussr": 2, ... }
}
```

**Files to create:**
- `tests/cpp/test_golden_replays.cpp`
- `tests/cpp/fixtures/` — directory for JSON fixtures
- `tests/cpp/CMakeLists.txt` — update to include new test

**Test requirement:** Harness compiles and runs with 0 fixtures (vacuous pass).

### 0D. Per-card event test harness (Python)

Create `tests/python/test_cpp_events.py`: a parametrized pytest file that calls `tscore` bindings to execute single card events and checks outcomes. Each test case is a tuple: `(card_id, setup_fn, assertion_fn)`. This is the workhorse test file for Phases 1-4.

**Files to create:**
- `tests/python/test_cpp_events.py`

### 0E. Document the Observation interface contract

Write `docs/observation_interface.md`: the target API contract for Phase 3. This is a design document, not code. Contents:
- `Observation` struct definition (what a partial-info agent sees)
- `FullState` struct definition (what a full-info agent sees)
- Mapping from current `GameState` fields to `Observation` vs hidden
- `hands[]` access audit: every callsite in `mcts.cpp`, `mcts_batched.cpp`, `ismcts.cpp` listed with its proposed replacement

**Files to create:**
- `docs/observation_interface.md`

### 0F. Promo card exclusion (GAP-044, GAP-045, GAP-046)

Cards 109, 110, 111 are in the deck build path (`game_state.cpp:13`) but have no event logic. Per CLAUDE.md, they are permanently out of scope. **Remove them from the deck entirely** so they never appear in games.

**Files to modify:**
- `cpp/tscore/game_state.cpp` — remove cards 109, 110, 111 from deck construction
- `tests/python/test_cpp_events.py` — add test: "cards 109-111 never in deck"

**Gaps closed:** GAP-044, GAP-045, GAP-046 (3 gaps resolved by exclusion)

---

## Phase 1 — Critical Systemic Correctness

**Goal:** Fix the 8 highest-impact systemic bugs that affect nearly every game: opponent-event ordering, space race event suppression, space legality, ops placement, Vietnam Revolts, Cuban Missile Crisis, Glasnost, and the war-card mechanic.

**Estimated complexity:** XL (Extra Large)
**Duration:** 10-14 days
**Training impact:** The action space changes (ops placement adjacency, space legality, CMC). Models trained on the old engine will have degraded performance. Plan a BC warm-start retraining after Phase 1 merges.

### 1A. GAP-002 + GAP-003: Opponent event ordering and space race suppression

**Problem:** `apply_action_with_hands()` at `game_loop.cpp:718` always fires the opponent event before ops. For space race, it fires the opponent event and then spaces — the opposite of what space race is for.

**Fix:**
1. In `apply_action_with_hands()`, check `action.mode`:
   - If `ActionMode::Space`: skip opponent event entirely (the card is sent to space).
   - If ops mode (Influence/Coup/Realign): add an `EventDecision` query (kind=`SmallChoice`, n_options=2: "event first" or "event after") to let the policy choose ordering. Default (random fallback) = event first (preserving current behavior for untrained models).
2. If "event after" is chosen, apply the ops first, then fire the event (checking for game-over between).

**New enum value:** Add `DecisionKind::EventOrdering` to the `DecisionKind` enum for clarity (or reuse `SmallChoice` with documented semantics).

**Files to modify:**
- `cpp/tscore/game_loop.cpp` — `apply_action_with_hands()` (lines 711-740)
- `cpp/tscore/step.hpp` — add `DecisionKind::EventOrdering` if desired

**Tests:**
- `test_cpp_events.py::test_space_race_suppresses_opponent_event` — Space a USSR card as US, verify event did not fire.
- `test_cpp_events.py::test_opponent_event_ordering_choice` — Play opponent card for ops, verify policy callback is queried.
- `tests/cpp/fixtures/gap002_event_ordering.json` — golden fixture.
- `tests/cpp/fixtures/gap003_space_suppression.json` — golden fixture.

**Gaps closed:** GAP-002, GAP-003

### 1B. GAP-004: Space race ops minimum

**Problem:** `legal_modes()` checks attempt count and level but never uses `kSpaceOpsMinimum` (defined but unused at `legal_actions.cpp:23`).

**Fix:** In `legal_modes()`, when considering `ActionMode::Space`, add: `if (spec.ops < kSpaceOpsMinimum[level]) { skip; }`. Account for `ops_modifier`.

**Files to modify:**
- `cpp/tscore/legal_actions.cpp` — `legal_modes()` (around line 158)

**Tests:**
- `test_cpp_events.py::test_space_race_ops_minimum` — at space level 6, a 2-ops card cannot be spaced.
- `test_cpp_events.py::test_space_race_ops_minimum_with_modifier` — with Vietnam Revolts active, a 2-ops card can be spaced (effective 3 ops).

**Gaps closed:** GAP-004

### 1C. GAP-005: Ops placement adjacency and enemy-control surcharge

**Problem:** `accessible_countries()` does a full BFS from any friendly influence, opening whole connected regions. Placement into enemy-controlled countries costs only 1 influence, not 2.

**Fix:**
1. Replace the BFS in `adjacency.cpp:65` for `ActionMode::Influence` with a 1-hop adjacency check: a country is accessible if (a) it is the US/USSR home anchor, (b) the side already has influence there, or (c) it is adjacent to a country where the side has influence.
2. In `apply_action()` at `step.cpp:1138` (influence placement), check if the target is enemy-controlled. If so, the cost is 2 ops per influence point, not 1. This means each point placed in enemy territory costs 2 from the card's ops pool.

**This is a major action-space change.** The number of legal influence targets will shrink significantly. The model's country head will need retraining.

**Files to modify:**
- `cpp/tscore/adjacency.cpp` — replace BFS with 1-hop adjacency for `ActionMode::Influence`
- `cpp/tscore/step.cpp` — influence placement cost (around line 1138)
- `cpp/tscore/legal_actions.cpp` — `enumerate_actions()` must account for ops budget when generating influence multisets

**New struct/concept:** `OpsPlacementPlan` — a sequence of (country, points) that sums to at most the card's effective ops, accounting for surcharges. This replaces the current simple multiset of country targets.

**Tests:**
- `test_cpp_events.py::test_influence_adjacency_basic` — can only place in friendly or adjacent-to-friendly.
- `test_cpp_events.py::test_influence_enemy_control_surcharge` — placing into a controlled country costs 2 ops per point.
- `test_cpp_events.py::test_influence_no_bfs_deep_chain` — cannot place in country 3 hops away with no intermediate influence.

**Gaps closed:** GAP-005

### 1D. GAP-039: Vietnam Revolts regional restriction

**Problem:** Event sets `ops_modifier[USSR] += 1` globally. Should only apply when all ops are spent in Southeast Asia.

**Fix:** Remove the `ops_modifier` increment from the Vietnam Revolts event. Instead, add a runtime check in `apply_action()`: if `vietnam_revolts_active` and `side == USSR` and the action places all influence in Southeast Asia (or the action is a coup/realign in SEA), grant +1 ops. This requires checking the action's target countries against the SEA region.

**Alternative (simpler):** Keep `vietnam_revolts_active` flag. In `effective_ops()`, do NOT add the modifier globally. Instead, add a `effective_ops_for_action()` variant that takes the action and checks if all targets are in SEA. The legal action enumeration uses this.

**Files to modify:**
- `cpp/tscore/step.cpp` — card 9 event (line 258): remove `ops_modifier` line
- `cpp/tscore/legal_actions.cpp` — `effective_ops()`: add region-aware variant
- `cpp/tscore/step.cpp` — `apply_action()` influence/coup/realign: use region-aware ops

**Tests:**
- `test_cpp_events.py::test_vietnam_revolts_sea_only_bonus` — bonus applies only in SEA.
- `test_cpp_events.py::test_vietnam_revolts_no_bonus_outside_sea` — no bonus for non-SEA actions.

**Gaps closed:** GAP-039

### 1E. GAP-041: Cuban Missile Crisis cancellation

**Problem:** `cuban_missile_crisis_active` is set but never cleared, and `legal_modes()` removes all coup actions permanently.

**Fix:**
1. In turn cleanup (`game_loop.cpp`, end-of-turn handling): clear `cuban_missile_crisis_active`.
2. In `legal_modes()`: instead of removing Coup entirely, keep it available. The CMC rule is that performing a battleground coup during CMC causes the couping player to lose the game. This should be enforced in `apply_action()` as an immediate loss condition.
3. Add a CMC cancellation path: if the affected side removes 2 influence from Cuba (US) or Turkey (USSR), the crisis is cancelled. This requires an `EventDecision` sub-action query during the affected player's action.

**Files to modify:**
- `cpp/tscore/legal_actions.cpp` — `legal_modes()` (line 179-181): remove the blanket coup erasure, add DEFCON-suicide awareness instead
- `cpp/tscore/step.cpp` — coup resolution: check CMC, enforce instant loss
- `cpp/tscore/game_loop.cpp` — turn cleanup: clear CMC flag
- `cpp/tscore/game_loop.cpp` — CMC cancellation sub-action (influence removal from Cuba/Turkey)
- `cpp/tscore/game_state.hpp` — add `cuban_missile_crisis_side` to track which side is affected

**Tests:**
- `test_cpp_events.py::test_cmc_clears_at_turn_end`
- `test_cpp_events.py::test_cmc_bg_coup_instant_loss`
- `test_cpp_events.py::test_cmc_cancellation_by_influence_removal`
- `tests/cpp/fixtures/gap041_cmc.json`

**Gaps closed:** GAP-041

### 1F. GAP-042: Glasnost SALT follow-up

**Problem:** With SALT active, Glasnost grants a full extra AR (normal card play from hand). The rule says it grants limited extra operations, not a full AR.

**Fix:** Replace `glasnost_extra_ar` with a `glasnost_free_ops` flag. When the flag is set, the game loop grants the USSR player free ops (value = Glasnost card ops, typically 4) to spend as influence/coup/realign, not a full card play from hand. Implement this as a sub-action using the existing `apply_ops_randomly()` replacement (see Phase 2) or a direct policy query.

**Files to modify:**
- `cpp/tscore/step.cpp` — card 93 event: set `glasnost_free_ops` instead of `glasnost_extra_ar`
- `cpp/tscore/game_loop.cpp` — replace the extra-AR handling with free-ops handling
- `cpp/tscore/game_state.hpp` — rename/replace `glasnost_extra_ar`

**Tests:**
- `test_cpp_events.py::test_glasnost_salt_limited_ops` — verify only free ops, not full card play.
- `test_cpp_events.py::test_glasnost_no_salt` — standard behavior without SALT.

**Gaps closed:** GAP-042

### 1G. War card mechanic (GAP-008, GAP-009, GAP-014, GAP-021, GAP-038)

**Problem:** Five war cards (Korean War #11, Arab-Israeli War #13, Indo-Pakistani War #24, Brush War #39, Iran-Iraq War #105) use `apply_free_coup()` instead of the war resolution mechanic.

**War resolution rules:**
- Roll a die. Success if roll >= (target stability + number of adjacent countries controlled by the defender - number controlled by the attacker).
- On success: attacker gains control of the target and the specified VP. The defender's influence is replaced, not just reduced by coup math.
- On failure: nothing happens (no partial influence change).
- War cards do NOT lower DEFCON (unlike coups).
- MilOps are credited at the card's ops value regardless of success.

**Fix:** Create `apply_war_card()` function in `step.cpp`:

```cpp
struct WarResult {
    bool success;
    int die_roll;
    int threshold;
};

WarResult apply_war_card(
    PublicState& pub, Side attacker, CountryId target,
    int vp_on_success, int ops_for_milops,
    Pcg64Rng& rng
);
```

Replace all 5 card events' `apply_free_coup()` calls with `apply_war_card()`.

**Per-card details:**
- Card 11 (Korean War): target=South Korea, attacker=USSR, check adjacent countries (Japan controlled by US?), +2 VP on success, 2 milops.
- Card 13 (Arab-Israeli War): target=Israel, attacker=USSR, check adjacent (Egypt, Jordan, Lebanon, Syria), +2 VP on success, 2 milops.
- Card 14 (Indo-Pakistani War): target chosen by phasing player (India or Pakistan), check adjacent, +2 VP on success, 2 milops.
- Card 39 (Brush War): target chosen by phasing player (stability 1-2 country), +1 VP on success, 3 milops. Extra effect on success: remove all opponent influence from target.
- Card 105 (Iran-Iraq War): target chosen by phasing player (Iran or Iraq), check adjacent, +2 VP on success, 2 milops.

**Files to create/modify:**
- `cpp/tscore/step.cpp` — add `apply_war_card()`, rewrite cards 11, 13, 24, 39, 105
- `cpp/tscore/step.hpp` — declare `apply_war_card()`, `WarResult`

**Tests (one per card):**
- `test_cpp_events.py::test_korean_war_success` — roll high enough, verify control change + VP.
- `test_cpp_events.py::test_korean_war_failure` — roll too low, verify no change.
- `test_cpp_events.py::test_korean_war_no_defcon_change` — verify DEFCON stays.
- `test_cpp_events.py::test_arab_israeli_war_adjacency_modifier`
- `test_cpp_events.py::test_indo_pakistani_war_target_choice`
- `test_cpp_events.py::test_brush_war_success_removes_opponent`
- `test_cpp_events.py::test_iran_iraq_war_target_choice`
- `tests/cpp/fixtures/gap008_korean_war.json`

**Gaps closed:** GAP-008, GAP-009, GAP-014, GAP-021, GAP-038

### 1H. GAP-001: China Card headline filter

**Problem:** The random/exploration headline path can select China Card.

**Fix:** In `choose_headline_action_with_config()` at `game_loop.cpp:79`, after calling `legal_cards()`, filter out `kChinaCardId`.

**Files to modify:**
- `cpp/tscore/game_loop.cpp` — `choose_headline_action_with_config()` (line 80)

**Tests:**
- `test_cpp_events.py::test_china_card_never_headlined` — run 100 random headlines, verify China never selected.

**Gaps closed:** GAP-001

### 1I. GAP-040: Formosan Resolution control check

**Problem:** `is_scoring_battleground()` checks `formosan_active` but not US control of Taiwan.

**Fix:** In `scoring.cpp:32`, add `&& controls_country(Side::US, kTaiwanId, pub)` to the Formosan check.

**Files to modify:**
- `cpp/tscore/scoring.cpp` — `is_scoring_battleground()` (line 32)

**Tests:**
- `test_cpp_events.py::test_formosan_bg_requires_us_control`

**Gaps closed:** GAP-040

### 1J. GAP-043: Solidarity prerequisite in legality

**Problem:** Solidarity (card 104) is offered as playable even without John Paul II prerequisite.

**Fix:** In `legal_modes()`, add: `if (card_id == 104 && !pub.john_paul_ii_played) { remove Event from modes; }`

**Files to modify:**
- `cpp/tscore/legal_actions.cpp` — `legal_modes()` (after line 165)

**Tests:**
- `test_cpp_events.py::test_solidarity_requires_jpii`

**Gaps closed:** GAP-043

### 1K. GAP-022: How I Learned to Stop Worrying — DEFCON 1 choice

**Problem:** DEFCON choice is hardcoded to 2-5. DEFCON 1 should be legal (suicidal but legal).

**Fix:** In `step.cpp` card 49 event handler (line 605), change choice set from {2,3,4,5} to {1,2,3,4,5}.

**Files to modify:**
- `cpp/tscore/step.cpp` — card 49 event

**Tests:**
- `test_cpp_events.py::test_how_i_learned_defcon1_legal`

**Gaps closed:** GAP-022

### Phase 1 Summary

| Sub-phase | Gaps Closed | Impact Level |
|-----------|-------------|-------------|
| 1A | GAP-002, GAP-003 | High |
| 1B | GAP-004 | High |
| 1C | GAP-005 | High |
| 1D | GAP-039 | High |
| 1E | GAP-041 | High |
| 1F | GAP-042 | High |
| 1G | GAP-008, GAP-009, GAP-014, GAP-021, GAP-038 | High |
| 1H | GAP-001 | Medium |
| 1I | GAP-040 | Medium |
| 1J | GAP-043 | Low |
| 1K | GAP-022 | Medium |
| **Total** | **16 gaps** | |

**Post-Phase 1 action:** BC warm-start retraining on heuristic-vs-heuristic games generated by the corrected engine. Then resume PPO from the new BC checkpoint.

---

## Phase 2 — Player Choice Restoration (`apply_ops_randomly` Replacement)

**Goal:** Replace all randomized player decisions with proper sub-action dispatch through the `PolicyCallbackFn` / `EventDecision` mechanism. This is the single largest category of gaps (20+ cards).

**Estimated complexity:** XL (Extra Large)
**Duration:** 10-14 days
**Training impact:** Medium. The model must learn to respond to new `EventDecision` queries. During transition, the random fallback (existing behavior) is used when no policy callback is provided, so heuristic self-play still works.

### 2A. Replace `apply_ops_randomly()` with proper sub-action dispatch

**Problem:** `apply_ops_randomly()` at `game_loop.cpp:174` randomly picks mode and targets. It is used by UN Intervention (#32), Missile Envy (#52), Grain Sales (#68), and other cards that grant free ops.

**Fix:** Create `apply_free_ops()` that uses `EventDecision` callbacks:
1. Query policy for mode choice (Influence/Coup/Realign) via `DecisionKind::SmallChoice`
2. Query policy for target selection via `DecisionKind::CountrySelect` (potentially multiple queries for influence placement)
3. Apply the chosen action through normal `apply_action()` path

```cpp
void apply_free_ops(
    PublicState& pub, Side side, int ops,
    Pcg64Rng& rng, const PolicyCallbackFn* policy_cb
);
```

**Files to modify:**
- `cpp/tscore/game_loop.cpp` — replace `apply_ops_randomly()` with `apply_free_ops()`

**Gaps addressed by this change alone:** GAP-006, GAP-018 (UN Intervention), GAP-024 (Missile Envy), GAP-027 (Grain Sales)

### 2B. Per-card event choice restoration

Each of the following cards has randomized choices that need replacement with `choose_country()` or `choose_option()` calls (both already exist in `step.cpp`). Many already have the `PolicyCallbackFn*` plumbed through but call `sample_up_to()` or `sample_without_replacement()` instead.

**Pattern:** Replace `sample_up_to(pool, N, rng)` with a loop of `choose_country(pub, card_id, side, remaining_pool, rng, policy_cb)` calls, removing chosen countries from the pool each iteration.

| Gap | Card | Current Code | Fix Description |
|-----|------|-------------|-----------------|
| GAP-007 | 7 Socialist Govts | `sample_up_to(we, 3, rng)` | 3x `choose_country()` from WE pool |
| GAP-010 | 16 Warsaw Pact | random country selection | Branch A: 4x `choose_country()` from E.Europe; Branch B: allocation via repeated `choose_country()` |
| GAP-011 | 19 Truman Doctrine | `sample_up_to(eligible, 1, rng)` | 1x `choose_country()` |
| GAP-012 | 20 Olympic Games | random boycott placement | 4x `choose_country()` from accessible |
| GAP-013 | 23 Marshall Plan | `sample_up_to(eligible, 7, rng)` | Up to 7x `choose_country()` |
| GAP-015 | 28 Suez Crisis | `sample_up_to({FR,UK,IL}, 2, rng)` | 2x `choose_country()` from {France, UK, Israel} |
| GAP-016 | 29 East European Unrest | `sample_up_to(ee, 3, rng)` | 3x `choose_country()` |
| GAP-017 | 30 Decolonization | random 4 placements | 4x `choose_country()` from Africa/SEA |
| GAP-019 | 33 De-Stalinization | random source+dest | Up to 4 pairs: `choose_country()` for source, then `choose_country()` for dest |
| GAP-020 | 37 Special Relationship | random placement | `choose_country()` for placement target |
| GAP-023 | 50 Junta | hardcoded coup, random targets | `choose_country()` for influence, `choose_option()` for coup-vs-realign, `choose_country()` for target |
| GAP-025 | 59 Muslim Revolution | random + invalid targets | 2x `choose_country()` from eligible (US influence > 0) |
| GAP-026 | 67 Puppet Govts | `sample_up_to(eligible, 3, rng)` | 3x `choose_country()` |
| GAP-028 | 71 OAS Founded | random placement | 2x `choose_country()` from C/SA |
| GAP-029 | 75 Voice of America | random removal | Up to 4x `choose_country()` from non-Europe |
| GAP-030 | 76 Liberation Theology | random 3 single placements | Allocation: `choose_country()` + `choose_option()` for 2-in-one-country |
| GAP-031 | 77 Ussuri River | random 4 placements | 4x `choose_country()` from Asia |
| GAP-032 | 78 Ask Not | random discard count+cards, no 4-cap | `choose_option()` for count (0-4), then repeated `choose_card()` for which cards |
| GAP-033 | 83 Che | random coups, forced second | `choose_country()` for first target, `choose_option()` for whether to take second, `choose_country()` for second |
| GAP-034 | 84 Our Man in Tehran | random keep/discard | `choose_card()` repeated for which to keep (up to 5 drawn) |
| GAP-035 | 90 The Reformer | random European placements | `choose_country()` repeated |
| GAP-036 | 91 Marine Barracks | random removals | Up to 2x `choose_country()` |
| GAP-037 | 98 Latin American Debt | hardcoded discard pair | `choose_card()` x2 for which cards to discard, or `choose_option()` to decline |

**Files to modify:**
- `cpp/tscore/step.cpp` — 23 card event handlers
- `cpp/tscore/game_loop.cpp` — card 32, 52, 68, 78, 84, 98 handlers (the ones that live in game_loop rather than step)

**Tests:** One test per card minimum. Each test:
1. Sets up a game state where the card is playable
2. Provides a deterministic `PolicyCallbackFn` that makes a specific choice
3. Verifies the expected outcome

**Example test names:**
- `test_cpp_events.py::test_socialist_govts_player_choice`
- `test_cpp_events.py::test_warsaw_pact_branch_a_player_choice`
- `test_cpp_events.py::test_marshall_plan_player_choice`
- `test_cpp_events.py::test_ask_not_4card_cap`
- `test_cpp_events.py::test_che_optional_second_coup`
- ... (23 tests total)

**Gaps closed:** GAP-006, GAP-007, GAP-010, GAP-011, GAP-012, GAP-013, GAP-015, GAP-016, GAP-017, GAP-018, GAP-019, GAP-020, GAP-023, GAP-024, GAP-025, GAP-026, GAP-027, GAP-028, GAP-029, GAP-030, GAP-031, GAP-032, GAP-033, GAP-034, GAP-035, GAP-036, GAP-037

**Phase 2 total:** 27 gaps closed

**Post-Phase 2 action:** BC retraining with the corrected engine, then resume PPO.

---

## Phase 3 — Engine/Search Uncoupling

**Goal:** Define the `Observation` / `FullState` boundary. Remove direct `GameState.hands[]` access from search files. Full-info and partial-info agents consume different views of the same state.

**Estimated complexity:** L (Large)
**Duration:** 7-10 days
**Training impact:** Low if done correctly. The binary interface changes but game behavior does not.

### 3A. Define `Observation` struct

```cpp
// cpp/tscore/observation.hpp
struct Observation {
    const PublicState& pub;
    CardSet own_hand;          // cards visible to this player
    bool holds_china;
    int opponent_hand_size;    // known count, not contents
    CardSet known_not_in_opponent_hand;  // from discard/removed/seen
};
```

**Key rule:** `Observation` never contains `hands[other_side]`. Full-info search can access the full `GameState`; partial-info search constructs an `Observation` and works from there.

**Files to create:**
- `cpp/tscore/observation.hpp`

### 3B. Add `Observation make_observation(const GameState&, Side)` factory

Simple function that extracts the observation for one side.

**Files to modify:**
- `cpp/tscore/observation.hpp` — add factory function

### 3C. Refactor `mcts.cpp` — use `FullState` explicitly

`mcts.cpp` (697 lines) is perfect-information search. It legitimately needs full state. Rename its state access to use a `FullState` alias (which is just `GameState`) to make the intent explicit.

Replace scattered `state.hands[to_index(side)]` with `full_state.hands[to_index(side)]` (cosmetic rename to document intent).

**Files to modify:**
- `cpp/tscore/mcts.cpp` — rename state variable, add `using FullState = GameState;` or a type alias

### 3D. Refactor `ismcts.cpp` — use `Observation` at root, `GameState` only in determinizations

`ismcts.cpp` (2154 lines) does determinized search. At the root, it should work from `Observation`. When it creates a determinization, it materializes a full `GameState` by sampling opponent hands. The inner tree search then works on `GameState` (full info within that determinization).

**Current pattern (lines 839-859):** Direct hand manipulation for determinization.
**Target pattern:**
1. `Observation obs = make_observation(root_state, acting_side);`
2. `GameState determinized = materialize_determinization(obs, sampled_opponent_hand, rng);`
3. Inner search on `determinized` (full-info within that world).

**Files to modify:**
- `cpp/tscore/ismcts.cpp` — refactor root-level hand access to use `Observation`
- `cpp/tscore/observation.hpp` — add `materialize_determinization()` helper

### 3E. Refactor `mcts_batched.cpp` — isolate hand access

`mcts_batched.cpp` (4906 lines) is the largest file and has ~30 `hands[]` access sites. This is the most laborious refactoring. Group all hand accesses into:
1. **Root observation construction** — extracted into `make_observation()` calls
2. **Determinization materialization** — extracted into `materialize_determinization()` calls  
3. **Full-state simulation** — legitimate within a determinized game, keep as-is with `FullState` alias
4. **Policy queries** — pass `Observation` to the model, not full `GameState`

**Files to modify:**
- `cpp/tscore/mcts_batched.cpp` — all 30 hand-access sites

### 3F. Extract shared search structs from inline anonymous namespaces

`ModeDraft`, `CardDraft`, `ExpansionResult`, `SelectionResult` are duplicated in `mcts.cpp`, `mcts_batched.cpp`, and `ismcts.cpp`. Extract into `search_common.hpp`.

**Files to modify:**
- `cpp/tscore/search_common.hpp` — add shared struct definitions
- `cpp/tscore/mcts.cpp` — remove local definitions, include shared
- `cpp/tscore/mcts_batched.cpp` — same
- `cpp/tscore/ismcts.cpp` — same

### 3G. Tests

- `tests/cpp/test_observation.cpp` — unit tests for `make_observation()` and `materialize_determinization()`
- `tests/python/test_mcts.py` — existing MCTS smoke tests must still pass
- Benchmark: run 100 self-play games with the refactored engine, compare win rates against pre-refactor (should be statistically identical)

---

## Phase 4 — Remaining Medium-Impact Gaps

By the end of Phase 2, all 46 gaps are already closed. This phase is reserved for **polish, edge cases, and any gaps that were deferred from Phase 2 due to complexity**. If Phase 2 is fully completed, Phase 4 becomes a pure test-hardening phase.

**Estimated complexity:** S (Small)
**Duration:** 3-5 days
**Training impact:** None.

### 4A. Comprehensive card-event golden test suite

Write golden tests for every card that was modified in Phases 1-2. Target: at least 2 test scenarios per card (success path + failure/edge path).

**Files to create/modify:**
- `tests/cpp/fixtures/` — ~50 JSON fixtures
- `tests/python/test_cpp_events.py` — ~50 additional test cases

### 4B. DEFCON safety regression suite

Dedicated test file for DEFCON-related invariants:
- No legal action can lower DEFCON below 1 outside of explicit card effects
- War cards do not lower DEFCON
- CMC cancellation works correctly
- Space race at DEFCON 2 does not trigger opponent event that could lower DEFCON

**Files to create:**
- `tests/python/test_defcon_safety_comprehensive.py`

### 4C. Full-game golden replay tests

Record 5-10 complete games played by the corrected engine with deterministic seeds. Store the full action trace + final state hash. Use as regression tests.

**Files to create:**
- `tests/cpp/fixtures/golden_game_*.json` (5-10 files)
- `tests/cpp/test_golden_replays.cpp` — updated to run these

---

## Phase 5 — Python Engine Deprecation

**Goal:** Remove the Python engine (`python/tsrl/engine/`, 6,541 lines) by migrating all callers to C++ tscore bindings.

**Estimated complexity:** L (Large)
**Duration:** 7-10 days
**Training impact:** None if done correctly. All callers are migrated to equivalent C++ calls.

### 5A. Audit all Python engine callers

External callers (outside `python/tsrl/engine/` itself):

| Caller | Uses | Migration Path |
|--------|------|---------------|
| `python/tsrl/etl/validator.py` | `legal_countries`, `legal_modes`, `accessible_countries`, `apply_scoring_card` | Replace with `tscore.legal_countries()`, `tscore.legal_modes()`, `tscore.accessible_countries()`, `tscore.apply_scoring()` via bindings |
| `python/tsrl/selfplay/collector.py` | `GameResult`, `SelfPlayStep`, `collect_self_play_game` | Already uses C++ rollout path via `cpp_rollout.py`. Replace Python MCTS references. |
| `python/tsrl/policies/minimal_hybrid.py` | `load_adjacency`, `_ars_for_turn`, `legal_cards`, `legal_modes`, etc. | Replace with tscore binding calls |
| `python/tsrl/policies/learned_policy.py` | `Policy`, `GameState`, `legal_cards`, `legal_modes`, etc. | Replace with tscore binding calls |
| `python/tsrl/policies/iter10_policy.py` | Same as minimal_hybrid | Replace with tscore binding calls |
| `scripts/collect_heuristic_selfplay.py` | `RNG`, `make_rng`, `game_loop`, `game_state`, `legal_actions`, `SelfPlayStep` | Replace with tscore bindings |
| `scripts/collect_learned_vs_heuristic.py` | Extensive use | Replace with tscore bindings |
| `scripts/collect_learned_selfplay.py` | `game_loop`, `game_state`, `legal_actions`, `SelfPlayStep` | Replace with tscore bindings |
| `scripts/play_server.py` | `accessible_countries`, `effective_ops`, `legal_modes` | Deferred (play server out of scope per CLAUDE.md) |
| `scripts/benchmark_simple.py` | `make_random_policy`, `play_game` | Replace with tscore bindings |
| `scripts/run_mcts_game.py` | `collect_self_play_game`, `SelfPlayStep`, `GameResult` | Replace with C++ MCTS call via bindings |

### 5B. Expand tscore bindings

The current bindings (`bindings/tscore_bindings.cpp`, ~400 lines) expose game loop, state serialization, and MCTS. Add:
- `legal_cards()`, `legal_modes()`, `legal_countries()` — direct Python-callable
- `effective_ops()` — direct Python-callable
- `accessible_countries()` — direct Python-callable
- `apply_scoring()` — Python-callable wrapper around `apply_scoring_card()`
- `GameResult` enum/class — Python-accessible
- `_ars_for_turn()` — small helper, expose or reimplement in Python as a 3-line function

**Files to modify:**
- `bindings/tscore_bindings.cpp` — add ~15 new binding functions

### 5C. Migrate callers

One caller at a time. For each:
1. Replace `from tsrl.engine.X import Y` with `import tscore; tscore.Y()`
2. Run the caller's tests
3. Commit

**Order:** validator.py (most critical) -> policies -> scripts -> selfplay/collector

### 5D. Remove Python engine

After all callers migrated:
1. Delete `python/tsrl/engine/` (14 files, 6,541 lines)
2. Remove any `tests/python/test_engine.py` and `test_engine_integration.py` that test the Python engine directly (keep tests that test via bindings)
3. Update `pyproject.toml` if needed

**Files to delete:**
- `python/tsrl/engine/__init__.py`
- `python/tsrl/engine/adjacency.py` (112 lines)
- `python/tsrl/engine/cat_c_events.py` (865 lines)
- `python/tsrl/engine/cpp_rollout.py` (156 lines)
- `python/tsrl/engine/dice.py` (134 lines)
- `python/tsrl/engine/events.py` (1,601 lines)
- `python/tsrl/engine/game_loop.py` (946 lines)
- `python/tsrl/engine/game_state.py` (231 lines)
- `python/tsrl/engine/legal_actions.py` (607 lines)
- `python/tsrl/engine/mcts.py` (712 lines)
- `python/tsrl/engine/rng.py` (55 lines)
- `python/tsrl/engine/scoring.py` (489 lines)
- `python/tsrl/engine/step.py` (469 lines)
- `python/tsrl/engine/vec_runner.py` (164 lines)

**Tests:** All existing Python tests must pass with the engine removed (they should be using bindings by this point).

---

## Phase Dependency Graph

```
Phase 0 (foundations)
    |
    v
Phase 1 (systemic correctness)  ─────────────────┐
    |                                              |
    v                                              v
Phase 2 (player choice restoration)    Phase 3 (engine/search uncoupling)
    |                                              |
    v                                              v
Phase 4 (test hardening)              Phase 5 (Python deprecation)
```

**Parallelism opportunities:**
- Phase 3 can run in parallel with Phase 2 (different files, different concerns)
- Phase 5 can start during Phase 2 (bindings expansion is independent of event fixes)
- Phase 4 must wait for Phase 1+2 completion
- Within Phase 1, sub-phases 1A-1K are mostly independent and can be done in any order (except 1C depends on adjacency understanding from 1D's Vietnam work)
- Within Phase 2, all card fixes are independent of each other

---

## Risk Register

| Phase | Risk | Likelihood | Impact | Mitigation |
|-------|------|-----------|--------|------------|
| 1C | Ops placement adjacency change dramatically shrinks action space, breaking model | High | High | BC retraining immediately after. Keep old engine binary for A/B comparison. |
| 1E | CMC cancellation logic is complex and easy to get wrong | Medium | High | Extensive tests. Compare with Python engine's CMC logic and rules PDF. |
| 1G | War card mechanic has subtle adjacency rules per card | Medium | Medium | Cross-check each card against `TS_Rules_Deluxe.pdf`. Use `/rules-batcher` skill for batch verification. |
| 2A | `apply_free_ops()` replacement may have cascading effects on game length / training dynamics | Medium | Medium | Run 1000-game benchmark before and after. Compare average game length, VP distribution, DEFCON-1 rate. |
| 2B | 23 card fixes is a large surface area; regression risk is high | Medium | High | One card per commit. Test each independently. Golden replay regression catches cross-card interaction bugs. |
| 3E | `mcts_batched.cpp` refactoring (4906 lines, 30 hand-access sites) is high-risk | High | High | Pure refactor, no behavior change. Compare MCTS output distributions before and after on 100 fixed seeds. |
| 5C | Python caller migration may break training pipeline | Medium | High | Migrate one caller at a time. Run full pipeline smoke test after each migration. Keep Python engine on a deprecation branch until all callers verified. |

---

## Complexity and Effort Summary

| Phase | Complexity | Gaps Closed | New Tests | Est. Days |
|-------|-----------|-------------|-----------|-----------|
| 0 | M | 3 (promo exclusion) | 5 | 3-5 |
| 1 | XL | 16 | 25 | 10-14 |
| 2 | XL | 27 | 27 | 10-14 |
| 3 | L | 0 (architecture) | 10 | 7-10 |
| 4 | S | 0 (test hardening) | 30 | 3-5 |
| 5 | L | 0 (deprecation) | 0 (migration) | 7-10 |
| **Total** | | **46** | **~97** | **40-58** |

---

## Gap-to-Phase Assignment (Complete)

| Gap ID | Card/Location | Phase | Sub-phase |
|--------|--------------|-------|-----------|
| GAP-001 | China Card headline | 1 | 1H |
| GAP-002 | Opponent event ordering | 1 | 1A |
| GAP-003 | Space race event suppression | 1 | 1A |
| GAP-004 | Space Race ops minimum | 1 | 1B |
| GAP-005 | Ops placement adjacency | 1 | 1C |
| GAP-006 | `apply_ops_randomly()` | 2 | 2A |
| GAP-007 | 7 Socialist Governments | 2 | 2B |
| GAP-008 | 11 Korean War | 1 | 1G |
| GAP-009 | 13 Arab-Israeli War | 1 | 1G |
| GAP-010 | 16 Warsaw Pact Formed | 2 | 2B |
| GAP-011 | 19 Truman Doctrine | 2 | 2B |
| GAP-012 | 20 Olympic Games | 2 | 2B |
| GAP-013 | 23 Marshall Plan | 2 | 2B |
| GAP-014 | 24 Indo-Pakistani War | 1 | 1G |
| GAP-015 | 28 Suez Crisis | 2 | 2B |
| GAP-016 | 29 East European Unrest | 2 | 2B |
| GAP-017 | 30 Decolonization | 2 | 2B |
| GAP-018 | 32 UN Intervention | 2 | 2A |
| GAP-019 | 33 De-Stalinization | 2 | 2B |
| GAP-020 | 37 Special Relationship | 2 | 2B |
| GAP-021 | 39 Brush War | 1 | 1G |
| GAP-022 | 49 How I Learned | 1 | 1K |
| GAP-023 | 50 Junta | 2 | 2B |
| GAP-024 | 52 Missile Envy | 2 | 2A |
| GAP-025 | 59 Muslim Revolution | 2 | 2B |
| GAP-026 | 67 Puppet Governments | 2 | 2B |
| GAP-027 | 68 Grain Sales | 2 | 2A |
| GAP-028 | 71 OAS Founded | 2 | 2B |
| GAP-029 | 75 Voice of America | 2 | 2B |
| GAP-030 | 76 Liberation Theology | 2 | 2B |
| GAP-031 | 77 Ussuri River | 2 | 2B |
| GAP-032 | 78 Ask Not | 2 | 2B |
| GAP-033 | 83 Che | 2 | 2B |
| GAP-034 | 84 Our Man in Tehran | 2 | 2B |
| GAP-035 | 90 The Reformer | 2 | 2B |
| GAP-036 | 91 Marine Barracks | 2 | 2B |
| GAP-037 | 98 Latin American Debt | 2 | 2B |
| GAP-038 | 105 Iran-Iraq War | 1 | 1G |
| GAP-039 | 9 Vietnam Revolts | 1 | 1D |
| GAP-040 | 35 Formosan Resolution | 1 | 1I |
| GAP-041 | 43 Cuban Missile Crisis | 1 | 1E |
| GAP-042 | 93 Glasnost | 1 | 1F |
| GAP-043 | 104 Solidarity | 1 | 1J |
| GAP-044 | 109 Lone Gunman | 0 | 0F (exclude from deck) |
| GAP-045 | 110 Colonial Rear Guards | 0 | 0F (exclude from deck) |
| GAP-046 | 111 Panama Canal Returned | 0 | 0F (exclude from deck) |

---

## Conclusions

1. **The 46 gaps reduce to two systemic problems.** The first is that player choices in card events are randomized instead of delegated to the policy (`apply_ops_randomly` and `sample_up_to` patterns, affecting 27 cards). The second is that core mechanics are simplified (war cards as coups, BFS adjacency, missing surcharges, permanent CMC, global Vietnam bonus). Fixing the two systemic patterns covers ~90% of all gaps.

2. **Phase 1 is the hardest and most impactful.** It changes the legal action surface (adjacency, space legality, CMC), the war card mechanic, and opponent-event ordering. These changes will invalidate existing trained models and require a BC retraining cycle. But they are necessary: without them, the engine is playing a fundamentally different game.

3. **Phase 2 is mechanical but large.** Each of the 23 card fixes follows the same pattern: replace `sample_up_to()` or `sample_without_replacement()` with `choose_country()`/`choose_option()`/`choose_card()` calls. The `PolicyCallbackFn` infrastructure already exists; the gaps exist because the card implementations were stubbed with random behavior.

4. **Phase 3 (engine/search uncoupling) is a pure refactor** with zero game behavior change. It can run in parallel with Phase 2. The key deliverable is the `Observation` struct that cleanly separates what full-info and partial-info agents can see.

5. **Phase 5 (Python engine deprecation) removes 6,541 lines** of code that duplicates C++ logic at lower fidelity. The migration is straightforward because the tscore bindings already expose most needed functions; ~15 new binding functions bridge the remaining gap.

6. **The promo cards (109-111) are resolved by exclusion, not implementation,** per standing project policy. Three gaps closed for free.

7. **Total test coverage after all phases: ~97 new test cases** organized into card-event tests, mechanic tests, DEFCON safety tests, and full-game golden replays. This is a permanent regression safety net.

8. **Estimated total duration: 40-58 working days** across all 6 phases. Phases 2 and 3 can overlap, reducing wall-clock time to ~30-40 days with focused effort.
