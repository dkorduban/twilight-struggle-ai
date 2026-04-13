---
# Opus Analysis: WS6 C++ Engine Coupling
Date: 2026-04-13T18:03:00Z
Question: WS6 progress, architecture refactoring doc, current coupling level in C++ engine
---

## Executive Summary

WS6 Phase 1 (kDefconLoweringCards consolidation) is **partially done** -- `card_properties.hpp` exists with the canonical 15-card set, and 4 of 6 C++ consumers now `#include` it. However, the consolidation goal is **not fully achieved**: `search_common.hpp` still defines its own 13-card set (missing cards 52 and 68), `policies.cpp` defines a separate 9-card set, and `mcts_search_impl.hpp` imports from `card_properties.hpp` but re-wraps helper functions. The original 7-location duplication has been reduced to 3 distinct definitions with different card counts, which is a latent bug source.

WS6 Phase 2 (search_common.hpp) is **partially done** -- the file exists and extracts 7 shared helpers (`winner_value`, `calibrate_value`, `holds_china_for`, `sync_china_flags`, `softmax_inplace`, `accessible_countries_filtered`, `is_card_blocked_by_defcon`). All three MCTS `.cpp` files include it. However, `mcts_search_impl.hpp` independently re-defines all of these same helpers plus more, and structural duplication (`ModeDraft`, `CardDraft`, `ExpansionResult`) persists across 4-5 files.

Phase 3 (FullState/Observation split) has **not started** and remains the most impactful architectural change. All three MCTS files directly access `GameState.hands[]` (53 total references across the codebase) and `GameState.deck` (2 references), meaning search code is tightly coupled to full hidden state. This coupling is structural and cannot be fixed by header extraction alone.

## WS6 Phase 1 and 2 -- What Was Done

### Phase 1: card_properties.hpp

**Created:** `cpp/tscore/card_properties.hpp` in namespace `tscore` with:
- Canonical 15-card `kDefconLoweringCards` array: {4, 11, 13, 20, 24, 39, 48, 49, 50, 52, 53, 68, 83, 92, 105}
- Helper function `is_defcon_lowering(int card_id)`
- Detailed per-card documentation comments

**Adopted by** (via `#include "card_properties.hpp"`):
- `mcts.cpp` -- includes it, but also includes `search_common.hpp` which has its own copy
- `ismcts.cpp` -- same situation
- `mcts_batched.cpp` -- same situation
- `mcts_search_impl.hpp` -- includes it, uses `using tscore::kDefconLoweringCards` to bridge namespaces
- `learned_policy.cpp` -- includes it, uses `using tscore::kDefconLoweringCards`

**NOT consolidated -- still has its own definition:**
- `search_common.hpp` -- defines `kDefconLoweringCards` with **13 cards** (missing 52 Missile Envy and 68 Grain Sales) in namespace `ts` anonymous namespace
- `policies.cpp` -- defines `kDefconLoweringCards` with **9 cards** {4, 11, 13, 24, 52, 53, 68, 92, 105} (different subset, labeled "certainly lowers DEFCON" for heuristic penalty; intentionally narrower)
- `mcts_search_impl.hpp` -- imports from `card_properties.hpp` but re-defines `is_defcon_lowering_card()` and `is_card_blocked_by_defcon()` wrapper functions

**Bug risk:** The 13-card `search_common.hpp` definition is missing cards 52 and 68. Since `mcts.cpp`, `ismcts.cpp`, and `mcts_batched.cpp` all include both `card_properties.hpp` and `search_common.hpp`, there is a namespace shadowing situation. The `search_common.hpp` helpers in `ts::anonymous_namespace` use the 13-card set, while `card_properties.hpp` has the 15-card set in `tscore::`. The MCTS files call `is_defcon_lowering_card()` and `is_card_blocked_by_defcon()` from `search_common.hpp` (anonymous namespace wins for unqualified lookup), so they effectively use the **incomplete 13-card set**.

**Python mirror:** `python/tsrl/policies/minimal_hybrid.py` has a separate `_DEFCON_LOWERING_CARDS` frozenset with 13 cards (same set as `card_properties.hpp` minus 52 and 68 in some locations, but actually includes all 13 that match the search_common set plus 52 and 68 -- total 15 cards matching card_properties.hpp). The Python side appears correct.

### Phase 2: search_common.hpp

**Created:** `cpp/tscore/search_common.hpp` (113 lines) with these shared helpers:
1. `kDefconLoweringCards` (13-card version -- should use card_properties.hpp)
2. `kVirtualLossPenalty` constant
3. `is_defcon_lowering_card()` -- linear search
4. `is_card_blocked_by_defcon()` -- DEFCON safety filter
5. `winner_value()` -- maps Side to {-1, 0, +1}
6. `calibrate_value()` -- logistic calibration transform
7. `holds_china_for()` -- China Card ownership check
8. `sync_china_flags()` -- synchronize redundant China booleans
9. `softmax_inplace()` -- float array softmax
10. `accessible_countries_filtered()` -- legal countries with spec filter

**Adopted by:** All three MCTS .cpp files include it.

**Parallel duplication that was NOT removed:**
- `mcts_search_impl.hpp` (544 lines) defines the same helpers plus much more (full expansion, selection, backpropagation logic). It is **not included by any file** -- `#include "mcts_search_impl.hpp"` returns zero matches. This file appears to be dead code or an abandoned extraction attempt.

### What Phase 2 did NOT extract (still duplicated)

| Symbol | Copies | Files |
|--------|--------|-------|
| `struct ModeDraft` | 5 | mcts.cpp, ismcts.cpp, mcts_batched.cpp, mcts_search_impl.hpp, fast_mcts_batched.cpp |
| `struct CardDraft` | 5 | same files |
| `struct ExpansionResult` | 5 | same files |
| `struct PendingDecision` | 2 | mcts_batched.hpp, ismcts.cpp |
| `struct PendingHeadlineChoice` | 2 | mcts_batched.hpp, ismcts.cpp |
| `kMaxCardLogits/kMaxModeLogits/kMaxCountryLogits/kMaxStrategies` | 3 | mcts.cpp, ismcts.cpp, mcts_batched.cpp |
| `kMidWarTurn/kLateWarTurn/kMaxTurns/kSpaceShuttleArs` | 2 | ismcts.cpp, mcts_batched.cpp |
| Expansion logic (expand node from NN outputs) | 3+ | mcts.cpp, ismcts.cpp, mcts_batched.cpp each have their own |
| Tree traversal / selection | 3+ | each file has its own select-to-leaf |

## Original Architecture Goals

The architecture refactoring doc (`docs/architecture-refactoring.md`) is a comprehensive two-part Q&A analysis recommending 8 major changes:

1. **Split ts_core into layers** with enforced dependency direction (ts_domain, ts_engine, ts_rules, ts_policy_api, ts_search_core, ts_runtime, ts_observe)
2. **Runtime policy seam** replacing template/hard-coded policy selection
3. **Canonical ActionId/ActionCodec** replacing heavy Move objects at the policy boundary
4. **Explicit Ruleset object** eliminating global registration side effects
5. **Shared runtime** for self-play, benchmarking, and data collection
6. **First-class observability** (structured telemetry/event sinks)
7. **Consolidated search core** with pluggable evaluators
8. **Multi-threaded MCTS** via clone-per-worker and root-parallel

The doc's key architectural insight is the **FullState / Observation / DeterminizedState** split:
- Perfect-info MCTS runs on `FullState`
- ISMCTS runs on `Observation + BeliefSampler -> DeterminizedState`
- Heuristic policies score from `Observation` directly

The doc explicitly recommends: "common protocol, specialized kernels" -- unify ActionId, SearchBudget, SearchContext, Evaluator, KnowledgeModel, and telemetry; do NOT unify node layout, memory arenas, batching strategy, parallelization model, or TT key space.

### What has been achieved vs. the doc's recommendations

| Recommendation | Status |
|---------------|--------|
| 1. Layer split | Not done. Everything is still in one `ts_core` / `tscore` library |
| 2. Runtime policy seam | Partially done. `PolicyKind` enum + `choose_action()` provides a simple dispatch, but policies are not pluggable at runtime |
| 3. ActionId/ActionCodec | Effectively done. `ActionEncoding` struct serves as the canonical action representation |
| 4. Explicit Ruleset | Not applicable. Current engine uses reducer pattern, not global registration |
| 5. Shared runtime | Partially done. `mcts_batched.cpp` serves as the shared runtime for self-play, benchmarking, and data collection |
| 6. Observability | Minimal. Some JSONL trace output exists, no structured telemetry |
| 7. Consolidated search core | Partially done via search_common.hpp, but the bulk of search logic is still triplicated |
| 8. Multi-threaded MCTS | Done. mcts_batched.cpp uses thread pool with virtual loss |

## Current Coupling Assessment

### File sizes (lines of code in cpp/tscore/)

| File | Lines | Role |
|------|-------|------|
| mcts_batched.cpp | 4,906 | Primary workhorse -- self-play, benchmark, rollout |
| ismcts.cpp | 2,154 | Information-set MCTS with determinization |
| policies.cpp | 779 | Heuristic policies |
| mcts.cpp | 697 | Single-game perfect-info MCTS |
| mcts_search_impl.hpp | 544 | Dead/unused shared search impl |
| learned_policy.cpp | 357 | NN greedy policy |
| search_common.hpp | 113 | Shared helpers (Phase 2 output) |
| card_properties.hpp | 46 | Canonical DEFCON cards (Phase 1 output) |
| **Total tscore** | **16,075** | All .cpp + .hpp |

### Hidden state coupling (GameState.hands[] access)

All MCTS files directly access `GameState.hands[]`, which contains the full hidden hand for both players:

| File | `hands[]` references |
|------|---------------------|
| mcts_batched.cpp | 32 |
| ismcts.cpp | 12 |
| mcts.cpp | 5 |
| mcts_search_impl.hpp | 4 |
| **Total** | **53** |

These accesses serve multiple purposes:
1. **Legal action generation:** `legal_cards(state.hands[to_index(side)], ...)` -- needs the acting side's hand
2. **Card removal after play:** `hand.reset(action.card_id)` -- mutates hand during tree simulation
3. **Determinization sampling:** `ismcts.cpp` manipulates opponent hands to create determinized states
4. **Feature extraction:** Hands are passed to NN feature encoders
5. **Hand snapshots:** Stored in PendingDecision for deferred resolution

This is the core coupling that Phase 3 would address. The search code cannot currently operate on a per-side observation -- it requires the complete `GameState` including both players' hidden hands and the deck.

### Include dependency graph (MCTS files)

```
mcts.cpp includes:
  mcts.hpp -> game_state.hpp -> public_state.hpp
  card_properties.hpp
  game_data.hpp, game_loop.hpp, nn_features.hpp, policies.hpp
  search_common.hpp -> game_data.hpp, mcts.hpp

ismcts.cpp includes:
  ismcts.hpp -> mcts.hpp -> game_state.hpp
  card_properties.hpp
  game_data.hpp, game_loop.hpp, human_openings.hpp, nn_features.hpp
  policies.hpp, scoring.hpp, step.hpp
  search_common.hpp

mcts_batched.cpp includes:
  mcts_batched.hpp -> game_loop.hpp, mcts.hpp
  card_properties.hpp
  game_data.hpp, human_openings.hpp, nn_features.hpp
  policies.hpp, policy_callback.hpp, scoring.hpp, step.hpp
  search_common.hpp
```

All three depend on `game_state.hpp` (which defines `GameState` with hidden `hands` and `deck`). There is no `Observation` type that provides a restricted view.

### Cross-file struct duplication summary

The total structural duplication count across `cpp/tscore/`:
- 3 distinct `kDefconLoweringCards` definitions with different element counts (15, 13, 9)
- 5 copies of `ModeDraft` struct
- 5 copies of `CardDraft` struct  
- 5 copies of `ExpansionResult` struct
- 2 copies of `PendingDecision` struct
- 2 copies of `PendingHeadlineChoice` struct
- 3+ copies of expansion-from-NN-outputs logic
- 3+ copies of tree selection/traversal logic
- 1 dead file (`mcts_search_impl.hpp`, 544 lines, not included anywhere)

## Phase 3 Necessity

### Arguments FOR Phase 3 (FullState/Observation split)

1. **Correctness guarantee:** Without an `Observation` type, nothing prevents search code from accidentally reading the opponent's hand during non-determinized search. The 53 `hands[]` references are manually correct today, but this is a convention, not an invariant.

2. **ISMCTS correctness:** The determinization process in `ismcts.cpp` manually removes opponent cards and re-deals. An `Observation` type would make the information boundary explicit and testable.

3. **Architecture doc alignment:** The doc's most impactful recommendation is exactly this split. It enables clean separation of perfect-info MCTS (operates on `FullState`) from ISMCTS (operates on `Observation + Sampler -> DeterminizedState`).

4. **Future extensibility:** Online play against humans requires an observation-only interface. The current `GameState` cannot be safely exposed.

### Arguments AGAINST Phase 3 (or for deferral)

1. **High cost, low immediate ROI:** 53 `hands[]` references across 4 files (mostly in mcts_batched.cpp) would need refactoring. mcts_batched.cpp at 4,906 lines is the project's critical hot path for training data generation.

2. **No active bugs from coupling:** The current direct-access pattern works correctly. There are no known bugs caused by information leakage.

3. **Month 3 priorities conflict:** The current focus is strength push, Elo stability, and release-candidate bot. A 5,000-line refactor of the primary training pipeline carries regression risk.

4. **Partial mitigation already exists:** `PublicState` is already cleanly separated. The `Observation` type would essentially be `PublicState + own_hand + china_ownership` -- the data is already structured this way conceptually.

5. **mcts_search_impl.hpp shows the risk:** An earlier attempt to extract shared search code produced a 544-line dead file. Complex extractions in this codebase have a history of being abandoned.

### Verdict

Phase 3 is **architecturally correct but practically premature** for Month 3. The coupling is real but not causing bugs. The ROI is highest when online play or a second search implementation needs the boundary. The immediate priorities (DEFCON rate, Elo ladder, training throughput) do not require it.

## Conclusions (numbered)

1. **Phase 1 is incomplete.** `card_properties.hpp` exists with the correct 15-card canonical set, but `search_common.hpp` still defines a 13-card set missing cards 52 (Missile Envy) and 68 (Grain Sales). Since MCTS files use the `search_common.hpp` version via anonymous namespace lookup, the MCTS DEFCON safety filter is using an incomplete card list. This is a **latent bug** -- these two cards' events can cause DEFCON-1 suicide at DEFCON 2.

2. **Phase 2 extracted utility helpers but not structural duplication.** `search_common.hpp` provides 7 shared functions used by all 3 MCTS files, but the heavier duplication (ModeDraft/CardDraft/ExpansionResult structs, expansion logic, tree traversal) remains triplicated.

3. **`mcts_search_impl.hpp` is dead code.** It defines the same helpers as `search_common.hpp` plus comprehensive expansion/selection/backpropagation logic, but is not included by any file. It should be either adopted or deleted.

4. **`policies.cpp` intentionally uses a narrower 9-card DEFCON set** for heuristic penalty scoring. This is a valid design choice (penalizing "certainly lowers" vs "might lower") but the distinction is not documented or tested.

5. **Hidden state coupling is deep and pervasive.** 53 direct `hands[]` accesses across MCTS files make the search code fundamentally dependent on complete game state. This is by design for perfect-info MCTS but architecturally problematic for ISMCTS.

6. **The original architecture doc's most impactful unimplemented recommendation is the FullState/Observation split** (Phase 3), which would enforce information boundaries at the type level rather than by convention.

7. **The architecture has evolved pragmatically rather than according to the refactoring doc.** ActionEncoding serves as ActionId, mcts_batched.cpp serves as the shared runtime, and the reducer pattern avoids global registration issues. But layer separation, search consolidation, and information-regime typing have not been pursued.

## Recommendations (numbered)

1. **Fix the kDefconLoweringCards inconsistency immediately.** Update `search_common.hpp` to use `card_properties.hpp`'s canonical 15-card set (add `#include "card_properties.hpp"` and `using tscore::kDefconLoweringCards`; remove the local definition). This is a one-line fix for a real correctness issue.

2. **Delete or adopt `mcts_search_impl.hpp`.** If the expansion/selection/backpropagation logic is correct and tested, refactor `mcts_batched.cpp` to use it. If not, delete the 544-line dead file to reduce confusion.

3. **Extract `ModeDraft`, `CardDraft`, `ExpansionResult` into `search_common.hpp`.** These three structs are identical across all 4-5 files. Moving them to the shared header eliminates 80+ lines of duplication with zero risk.

4. **Defer Phase 3 to Month 4 or when online play is prioritized.** The FullState/Observation split is the right long-term architecture but carries too much regression risk for Month 3's strength-push goals.

5. **Document the `policies.cpp` narrow DEFCON set as intentional.** Add a comment explaining why 9 cards vs 15 cards is the right choice for heuristic penalty scoring, to prevent future "consolidation" from breaking the heuristic.

6. **Consider a lightweight `ObservationView` as a stepping stone.** Instead of a full Phase 3 refactor, introduce a non-owning view struct (`struct ObservationView { const PublicState& pub; const CardSet& own_hand; bool holds_china; }`) that search code uses for feature extraction and legal action queries. This enforces the information boundary for reads without restructuring mutation paths.

## Open Questions

1. **Is the 13-card search_common.hpp set causing real DEFCON-1 suicides?** Cards 52 (Missile Envy) and 68 (Grain Sales) are missing from the MCTS DEFCON filter. If either card's event fires at DEFCON 2 and triggers a BG coup via `apply_ops_randomly`, the game ends in DEFCON-1. This should be tested.

2. **Is mcts_search_impl.hpp dead code or a work-in-progress?** No file includes it, yet it contains substantial logic (544 lines). Was it an abandoned Phase 2 attempt, or is it used by the `fast_mcts_batched` path?

3. **Should the Python `_DEFCON_LOWERING_CARDS` set include cards 52 and 68?** The Python set currently has 13 cards matching the search_common.hpp set. The canonical card_properties.hpp has 15. If the C++ is fixed, the Python should match.

4. **What is the actual DEFCON-1 rate with the current (incomplete) filter vs the corrected 15-card filter?** Measuring this would quantify the practical impact of recommendation #1.
