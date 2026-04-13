---
# Opus Analysis: WS6 Architecture Refactoring — Updated Plan
Date: 2026-04-13
Question: How applicable is docs/architecture-refactoring.md to WS6? What is the concrete updated plan?

## Executive Summary

The design document in `docs/architecture-refactoring.md` was written against a different upstream codebase (TSGE on GitHub) and proposes 8 major refactoring streams. Our codebase has already organically solved several of the problems it identifies — we have no polymorphic `Move` hierarchy, no global card-generator registration, and our `PolicyFn` is already a runtime `std::function` seam rather than a compile-time template. However, three proposals remain highly applicable and directly unblock current Month-3 priorities: (1) extracting duplicated search primitives into a shared header, (2) centralizing DEFCON-lowering card logic into `legal_actions.cpp`, and (3) formalizing the FullState/Observation split for ISMCTS. The rest — library splitting, `ActionId`/`ActionCodec`, `MatchRunner` abstraction, telemetry sinks — are over-engineered relative to our current scale (17k lines of C++, one binary target) and should be deferred.

## Findings

### What the design doc proposes

The document (a Q&A conversation with a senior SWE analyzing TSGE) proposes 8 major changes:

1. **Split `ts_core` into layered libraries** (`ts_domain`, `ts_engine`, `ts_rules`, `ts_policy_api`, `ts_search_core`, `ts_runtime`, `ts_observe`) with enforced dependency direction.
2. **Replace template policy seam with runtime `IPolicy`** — `MatchRunner` owns engine + two `IPolicy` objects.
3. **Introduce canonical `ActionId` and `ActionCodec`** — stop passing heavy `Move` objects; use integer IDs at the policy boundary.
4. **Extract `Ruleset` object** — kill implicit global card-generator registration.
5. **Create shared runtime** (`MatchRunner`, `SeriesRunner`, `BenchmarkService`, `SelfPlayService`, `TournamentService`).
6. **First-class observability** — structured telemetry/event sink.
7. **Consolidate search into one reusable core** — shared node stats, scheduler, pluggable evaluator, pluggable determinizer.
8. **Multi-threading via clone-per-worker and root-parallel** — explicit `worker_index`, per-worker arenas.

Additionally proposes `FullState` / `Observation` / `DeterminizedState` as three state forms, and a migration strategy with lock-step differential harness.

### Current codebase state (what's done vs missing)

Our codebase (`cpp/tscore/`, 17,272 lines across 20 `.cpp`/`.hpp` files + 1,090 lines in `bindings/`) diverges significantly from the TSGE codebase the doc analyzed:

**Already solved (not in TSGE):**
- `PolicyFn` is `std::function<optional<ActionEncoding>(PublicState, CardSet, bool, Pcg64Rng&)>` — a runtime callable, not a template.
- No polymorphic `Move` hierarchy — we use flat `ActionEncoding{card_id, mode, targets}` everywhere.
- No global card-generator registration — card effects are in `step.cpp` as a direct switch/dispatch.
- `GameState` is a clean value type (trivially copyable aside from `InlineDeck`/`CardSet`) — no wide mutable `Board` surface.
- `Pcg64Rng` is deterministic and explicitly passed — no `random_device` in production paths.
- `PolicyCallbackFn` exists for event-resolution sub-decisions (card/country/option selection within events).

**Partially addressed:**
- `mcts_search_impl.hpp` was created as a shared header for search primitives — but duplication persists across `mcts.cpp`, `ismcts.cpp`, `mcts_batched.cpp` (see below).
- `sample_determinization()` exists in `ismcts.cpp`/`.hpp` — but there's no formal `Observation` type or `FullState`/`Observation` split.
- Virtual loss is scaffolded in `MctsEdge` and `IsmctsConfig` — but true multi-threaded search is not working.

**Not addressed (duplication is severe):**
- `kDefconLoweringCards` is defined in **6 separate files** (with two different lengths: 7-element in `policies.cpp`, 13-element elsewhere — this is likely a bug).
- `ModeDraft` / `CardDraft` / `ExpansionResult` structs are defined in **5 separate files**.
- `softmax_inplace()` is defined in **5 separate files**.
- `is_defcon_lowering_card()` / `is_card_blocked_by_defcon()` is defined in **4 separate files**.
- DEFCON-blocking logic is in search code (`mcts_search_impl.hpp`, `mcts.cpp`, `ismcts.cpp`, `mcts_batched.cpp`) but **not** in `legal_actions.cpp` — meaning the legal-action API used by `PolicyFn` callers does not filter DEFCON-suicide moves, only the MCTS expansion code does.

### Applicability assessment (per major proposal)

| # | Proposal | Status | Assessment |
|---|----------|--------|------------|
| 1 | Split into layered libraries | 🚫 defer | 17k lines, one binary. Library splitting adds CMake complexity with no practical benefit until we have multiple binaries or external consumers. |
| 2 | Runtime policy seam (`IPolicy`) | ✅ done | `PolicyFn = std::function<...>` is already our runtime seam. `PolicyCallbackFn` handles sub-decisions. No template-locked `Game`. |
| 3 | `ActionId` / `ActionCodec` | 🚫 defer | Our `ActionEncoding{card_id, mode, targets}` is already a stable value type with `operator==`. An integer `ActionId` would add a codec layer for marginal benefit — we don't have the TSGE problem of polymorphic `Move*` comparisons. |
| 4 | Extract `Ruleset` object | ✅ done | No global registration. Card effects are direct dispatch in `step.cpp`. |
| 5 | Shared runtime (`MatchRunner`, etc.) | 🟡 partial | `play_game_fn`, `play_matchup_fn`, `play_game_traced_fn`, `play_ismcts_matchup_pooled` already provide this via free functions. Missing: a unified config-driven runner that handles self-play + benchmark + collection without separate entry points. Priority: **LOW** — current functions work. |
| 6 | First-class observability / telemetry | 🟡 partial | `StepTrace` captures decisions. `TracedGame` records full games. Missing: structured search telemetry (MCTS visit stats per node, determinization quality). Priority: **LOW** — not blocking anything. |
| 7 | Consolidate search core | 🟡 partial — **HIGH priority** | `mcts_search_impl.hpp` started this but adoption is incomplete. `ModeDraft`, `CardDraft`, `softmax_inplace`, `kDefconLoweringCards`, `is_defcon_lowering_card`, `is_card_blocked_by_defcon`, and NN expansion logic are duplicated 4-5x. This is the #1 source of bugs (the inconsistent `kDefconLoweringCards` lists are evidence). |
| 8 | Clone-per-worker + root-parallel | 🟡 partial | Virtual loss scaffolded. `sample_determinization()` exists. Missing: actual `std::thread` workers, `SearchContext{worker_index, rng}`, root-stat aggregation by canonical action key. Priority: **MED** — needed for parallel MCTS but not the immediate bottleneck. |

**Additional proposal: FullState / Observation / DeterminizedState split**
- ❌ not started — **HIGH priority for ISMCTS correctness**
- Currently `GameState` is used for all three roles. ISMCTS calls `sample_determinization()` which mutates a `GameState` clone. There's no type-level distinction between "this state has full info" and "this state has masked opponent hand." This makes it easy to accidentally read opponent hand data from an observation context.

## Conclusions

1. **The design doc is ~40% applicable.** Proposals 2 and 4 are already done. Proposals 1, 3, and 6 are over-engineered for our scale. Proposals 5 and 8 are partially done and low-to-medium priority. Only **proposal 7 (search consolidation)** and the **FullState/Observation split** are both unfinished and high-leverage.

2. **The #1 concrete problem is duplicated DEFCON-lowering logic.** `kDefconLoweringCards` exists in 6 files with two different definitions (7-element vs 13-element). The DEFCON-blocking function `is_card_blocked_by_defcon()` lives in search code but NOT in `legal_actions.cpp`. This means the legal-action API that policies call does not block DEFCON-suicide plays — only MCTS expansion filters them. This is a direct contributor to the 29% DEFCON-1 rate for non-MCTS policies.

3. **The #2 concrete problem is search struct duplication.** `ModeDraft`, `CardDraft`, `ExpansionResult`, `SelectionResult`, `softmax_inplace()` are defined identically in 4-5 files. Any bug fix must be applied 4-5 times, and they will inevitably drift (as `kDefconLoweringCards` already has).

4. **The FullState/Observation split is valuable but should be lightweight** — a `using` alias or thin wrapper, not a deep type hierarchy. The goal is to make ISMCTS code unable to accidentally access hidden info from the acting player's perspective.

5. **Library splitting, `ActionId`/`ActionCodec`, `MatchRunner` abstraction, and telemetry sinks should all be deferred.** They solve real problems in a larger codebase but add indirection without payoff at our current scale.

6. **The migration strategy (freeze behavior, then refactor structurally) is sound** and partially already in place — we have seeded deterministic games and `TracedGame` for regression. The lock-step differential harness is unnecessary for the small refactors recommended here.

## Recommendations (Updated WS6 Plan)

### Phase 1: Centralize DEFCON-lowering logic into legal_actions (Effort: S, <1 day)

**Why:** Directly fixes the 29% DEFCON-1 rate for non-MCTS policies. Currently `is_card_blocked_by_defcon()` only exists in search code. Moving it to `legal_actions.cpp` means ALL callers (heuristic, learned, random, PPO rollout) get the filter for free.

**Files to touch:**
- `cpp/tscore/legal_actions.hpp` — add `bool is_defcon_lowering_card(CardId)` and `bool is_card_blocked_by_defcon(const PublicState&, Side, CardId)` declarations
- `cpp/tscore/legal_actions.cpp` — implement using the canonical 13-element list; integrate into `legal_cards()` and `enumerate_actions()` so DEFCON-suicide cards are filtered at the legal-action level
- `cpp/tscore/mcts_search_impl.hpp` — remove local definitions, `#include "legal_actions.hpp"` instead
- `cpp/tscore/mcts.cpp` — remove local `kDefconLoweringCards`, `is_defcon_lowering_card()`, `is_card_blocked_by_defcon()`; use `legal_actions.hpp`
- `cpp/tscore/ismcts.cpp` — same removal
- `cpp/tscore/mcts_batched.cpp` — same removal
- `cpp/tscore/learned_policy.cpp` — same removal, use `legal_actions.hpp`
- `cpp/tscore/policies.cpp` — remove 7-element `kDefconLoweringCards` (likely a bug — missing 6 cards), use `legal_actions.hpp`

**Verification:** Run existing benchmark suite; DEFCON-1 rate for heuristic policy should drop from ~29% to <10%. Traced-game regression tests should still pass (games that were already legal remain so; newly-blocked moves would have caused DEFCON-1 anyway).

**Risk:** The 7-element list in `policies.cpp` is suspicious — it may be intentionally shorter (only the most common ones) or a bug. Verify against `docs/` and the full 13-element list before canonicalizing.

### Phase 2: Extract shared search types into mcts_search_impl.hpp (Effort: S, <1 day)

**Why:** Eliminates 4-5x duplication of `ModeDraft`, `CardDraft`, `ExpansionResult`, `SelectionResult`, `softmax_inplace()`. Makes future bug fixes single-point.

**Files to touch:**
- `cpp/tscore/mcts_search_impl.hpp` — already has these types; ensure it's the single source of truth. Add `softmax_inplace()` if not already there.
- `cpp/tscore/mcts.cpp` — remove local struct definitions and `softmax_inplace()`; `#include "mcts_search_impl.hpp"` (already included)
- `cpp/tscore/ismcts.cpp` — same
- `cpp/tscore/mcts_batched.cpp` — same

**Verification:** Build succeeds. Unit tests pass. No behavioral change.

### Phase 3: Lightweight Observation wrapper for ISMCTS (Effort: M, 1-3 days)

**Why:** ISMCTS correctness requires distinguishing "what the acting player can see" from "full game state." Currently `GameState` is used for both, and `sample_determinization()` takes a `GameState` with full opponent hand visible. A thin wrapper prevents accidental information leakage.

**Concrete change:**
- `cpp/tscore/game_state.hpp` — add:
  ```cpp
  // Observation: what one player can see. The opponent's hand is cleared.
  struct Observation {
      PublicState pub;
      CardSet own_hand;
      bool holds_china;
      int opp_hand_size;  // known from game rules
      Side acting_side;
      // Deck is hidden in observation (empty).
  };
  
  Observation make_observation(const GameState& gs, Side acting_side);
  GameState determinize(const Observation& obs, Pcg64Rng& rng);
  ```
- `cpp/tscore/game_state.cpp` — implement `make_observation()` (copies pub + own hand, computes opp hand size) and `determinize()` (wraps existing `sample_determinization` logic)
- `cpp/tscore/ismcts.hpp` — change `ismcts_search()` to take `const Observation&` instead of `const GameState&` + separate `opp_hand_size`
- `cpp/tscore/ismcts.cpp` — adapt internals; `sample_determinization` still produces `GameState` for the inner MCTS
- `bindings/tscore_bindings.cpp` — expose `Observation` and updated `ismcts_search` signature

**Verification:** ISMCTS benchmark games produce same results (the observation was already being constructed manually; now it's explicit). Add a test that `make_observation()` does not expose opponent hand.

### Phase 4: SearchContext for parallel MCTS prep (Effort: M, 1-3 days)

**Why:** Prerequisite for multi-threaded search. Currently worker identity is implicit.

**Concrete change:**
- `cpp/tscore/mcts_search_impl.hpp` — add:
  ```cpp
  struct SearchContext {
      int worker_index = 0;
      Pcg64Rng rng;
      // Future: scratch arena, trace sink
  };
  ```
- Refactor `mcts_search()` and `ismcts_search()` to accept `SearchContext&` instead of bare `Pcg64Rng&`
- ISMCTS determinization loop creates per-determinization `SearchContext` with `rng` seeded from `(base_seed, worker_index, det_index)`

**Verification:** Deterministic search results unchanged for `worker_index=0`. Add test for reproducibility with explicit worker index.

## What to Defer

| Proposal | Reason to defer |
|----------|----------------|
| **Library splitting** (ts_domain, ts_engine, ts_rules, etc.) | 17k lines, one build target, one team. CMake complexity not justified. Revisit if we add a second consumer binary or external API. |
| **`ActionId` / `ActionCodec`** | `ActionEncoding` is already a clean value type with `operator==`. Integer IDs would require a codec that maps to/from `ActionEncoding`, adding a translation layer for zero practical benefit. Our search already uses `ActionEncoding` directly as node keys. |
| **`MatchRunner` / `SeriesRunner` / service abstractions** | Current `play_game_fn`, `play_matchup_fn`, `play_game_traced_fn` free functions are sufficient. Adding runner objects would be pure ceremony at current scale. |
| **Telemetry sinks** | `StepTrace` + `TracedGame` cover game-level observability. Search-level telemetry (MCTS visit distributions) can be added ad hoc when debugging specific search issues, not as upfront infrastructure. |
| **Lock-step differential harness** | Valuable for large-scale migration. Overkill for the targeted refactors recommended here. Our existing traced-game regression tests and benchmark comparison are sufficient guards. |
| **Named RNG streams** (deck, dice, policy, search, etc.) | Conceptually clean but requires touching every RNG call site. Current single `Pcg64Rng` passed explicitly is deterministic and sufficient. Revisit only if RNG-ordering bugs become a real problem. |

## Open Questions

1. **`kDefconLoweringCards` inconsistency:** `policies.cpp` uses a 7-element list `{4, 11, 13, 24, 53, 92, 105}` while all search files use a 13-element list `{4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105}`. Which is correct? The 13-element list likely includes cards whose events can chain into DEFCON reduction (e.g., ABM Treaty #48 can lead to coup). Need to verify against rules. The discrepancy means heuristic policy may be making DEFCON-dangerous plays that MCTS would avoid.

2. **Where should DEFCON blocking live?** Two options: (a) in `legal_cards()` — remove the card from legal choices entirely, or (b) in `legal_modes()` — allow the card but block `Event` mode (player can still use for ops). Option (b) is rules-correct: you can play an opponent's DEFCON-lowering card for ops via coup/influence/space. Only the Event mode is dangerous. Need to verify the current search-code implementation handles this correctly.

3. **`mcts_batched.cpp` at 5,000 lines:** This file is the largest and most complex. Phase 2 deduplication will reduce it somewhat, but it may warrant further decomposition later. Not urgent — it's a self-contained search backend.

4. **`Observation` type granularity:** Should `Observation` include the deck (for card-counting agents) or only pub + own hand? Current `sample_determinization()` uses deck info from `GameState`. Decision: start with `Observation` excluding deck (strict information barrier), and have `determinize()` reconstruct deck from `pub.discard + pub.removed + own_hand + opponent_hand_size`.
---
