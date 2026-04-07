# Codebase Duplication & Pluggability Audit

**Date:** 2026-04-06
**Auditor:** Opus agent, full codebase scan (52 tool calls)

---

## 1. Code Duplication

### 1a. Game Loop Duplication (Critical)

The game loop -- turn setup, headline resolution, action rounds, extra ARs, cleanup, turn limit -- is implemented **at least 3 times** in parallel:

- **`cpp/tscore/game_loop.cpp`** (1626 lines): The canonical sequential game loop, used by `play_game_fn`, `play_game_traced_fn`, etc.
- **`cpp/tscore/mcts_batched.cpp`** (3967 lines): A state-machine version (`BatchedGameStage` enum with `TurnSetup`, `HeadlineChoiceUSSR`, `ActionRound`, `Cleanup`, `Finished`, etc.) that re-implements all the same phase logic in `advance_until_decision()` and `commit_best_action()`.
- **`cpp/tscore/ismcts.cpp`** (1822 lines): Yet another copy of the same game loop state machine for ISMCTS.
- **`cpp/mcts_batched_fast/fast_mcts_batched.cpp`** (3191 lines): A fourth copy, an experimental "fast" fork of `mcts_batched.cpp`.

Concrete examples of duplication:
- **`finish_turn()`** is defined identically in `mcts_batched.cpp:2300`, `ismcts.cpp:853`, and `fast_mcts_batched.cpp:2482`. None calls a shared implementation.
- **`sync_china_flags()`** is defined in `mcts_batched.cpp:352`, `ismcts.cpp:223`, `mcts_search_impl.hpp:100`, and `game_loop.cpp:33` (as `sync_china`).
- **Constants** `kMidWarTurn`, `kLateWarTurn`, `kMaxTurns`, `kSpaceShuttleArs` are redeclared in `game_loop.cpp:18-21`, `mcts_batched.cpp:36-39`, and equivalents in `ismcts.cpp` and `fast_mcts_batched.cpp`.

### 1b. DEFCON-Lowering Card List Divergence (Potential Bug)

The `kDefconLoweringCards` array is defined **6+ times** across files with **different contents**:

- `policies.cpp:37` -- 7 cards: `{4, 11, 13, 24, 53, 92, 105}` (plus separate `kDefconProbLoweringCards` and `kDefconRandomCoupCards`)
- `mcts_batched.cpp:40` -- 13 cards: `{4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105}`
- `learned_policy.cpp:165` -- 13 cards (same as mcts_batched)
- `ismcts.cpp:45` -- 13 cards (same)
- `mcts.cpp:61` -- 13 cards (same)
- `mcts_search_impl.hpp:26` -- 13 cards (same)

The heuristic policy in `policies.cpp` uses a finer-grained 3-tier classification (7 definite + 1 probabilistic + 2 random coup), while the NN-facing code uses a flat list of 13. This is not necessarily a bug, but the divergence is a maintenance risk and the lists could easily drift further.

### 1c. `get_tensor()` Helper Defined 3 Times

`get_tensor(const c10::impl::GenericDict&, const char*, bool)` is identically copy-pasted in:
- `nn_features.cpp:59`
- `learned_policy.cpp:22`
- `mcts.cpp:135`

### 1d. `build_action_from_country_logits()` / `accessible_countries_filtered()` Duplicated

These helpers are independently defined in:
- `learned_policy.cpp:41-50`
- `mcts_batched.cpp:384-462`
- `mcts_search_impl.hpp:113-127`

The `greedy_action_from_outputs()` function in `mcts_batched.cpp:3477-3645` (168 lines) is explicitly commented as "Exact mirror of TorchScriptPolicy::choose_action logic from learned_policy.cpp" -- a fully duplicated ~170-line function.

### 1e. `parse_policy()` Copied Into Every Tool

`parse_policy(std::string_view)` is identically defined in:
- `collect_selfplay_rows_jsonl.cpp:22`
- `collect_trace_jsonl.cpp:16`
- `learned_matchup.cpp:15`
- `initial_headline_choice.cpp:64`

### 1f. Feature Extraction: Python vs C++

Feature extraction exists in two independent implementations:
- **C++**: `nn_features.cpp` (`fill_scalars`, `fill_influence_array`, `fill_cards`)
- **Python**: `learned_policy.py:29` (`_extract_features`) plus `dataset.py` (`_card_mask`, `_influence_array`)

The scalar normalization must match exactly. The C++ code uses `pub.ar / 8.0f` (`nn_features.cpp:49`), Python uses `pub.ar / 8.0` (`learned_policy.py:55`). The card mask layout is `[hand, hand, discard, removed]` in both -- second slot is `hand` again (actor_possible = actor_known_in for self-play), matching `nn_features.cpp:32-37`. However, if someone changes one without the other, training-inference mismatch is silently introduced.

---

## 2. Policy Pluggability

### 2a. The `PolicyFn` Interface Is Clean

There is a single `PolicyFn` typedef in `game_loop.hpp:16`:
```cpp
using PolicyFn = std::function<std::optional<ActionEncoding>(
    const PublicState&, const CardSet&, bool, Pcg64Rng&
)>;
```
This is used consistently across `game_loop.cpp`, all tool binaries, and the pybind11 callbacks. Adding a new policy that conforms to this signature requires touching only the callsite (wrapping it in a lambda).

### 2b. `PolicyKind` Enum Is Vestigial

The `PolicyKind` enum in `policies.hpp:14-17` has only two values (`Random`, `MinimalHybrid`). The `choose_action(PolicyKind, ...)` free function dispatches via `switch`. This enum is used heavily in tools and bindings but is not how the learned policy or MCTS operate -- those go through `TorchScriptPolicy::choose_action` or the `PolicyFn` mechanism.

Adding a new `PolicyKind` value would require changes to:
1. `policies.hpp` (enum + function signature)
2. `policies.cpp` (switch case)
3. Every tool's `parse_policy()` function (4+ copies)
4. `bindings/tscore_bindings.cpp` (pybind11 enum)

The `PolicyKind` enum and the `PolicyFn` interface are parallel dispatch mechanisms that have not been unified. `PolicyKind` is the CLI-facing dispatch; `PolicyFn` is the actual runtime dispatch.

### 2c. MCTS / Batched MCTS Are Not Policies

The batched MCTS path (`mcts_batched.cpp`) does not conform to the `PolicyFn` interface at all. It has its own game loop, its own state machine, its own action selection. Swapping MCTS in or out means choosing between entirely different code paths at the tool/binary level (different executables), not composing policies.

ISMCTS similarly has its own game loop embedded in `ismcts.cpp`.

### 2d. Hardcoded Fallbacks to MinimalHybrid

Throughout `mcts_batched.cpp`, `learned_policy.cpp`, and `ismcts.cpp`, there are ~30+ hardcoded fallbacks to `choose_action(PolicyKind::MinimalHybrid, ...)`. If you wanted to change the fallback policy, you would need to grep and edit all of these.

### 2e. Python Model Architecture Selection

`model.py` contains **10 model classes** (`TSBaselineModel`, `TSCardEmbedModel`, `TSCountryEmbedModel`, `TSFullEmbedModel`, `TSDirectCountryModel`, `TSMarginalValueModel`, `TSControlFeatModel`, `TSControlFeatGNNModel`, `TSControlFeatGNNSideModel`, `TSCountryAttnModel`). Architecture selection is done in `train_baseline.py` via an `--arch` flag that maps to a class name. The output contract (dict with keys `card_logits`, `mode_logits`, etc.) is shared, but the trunk/head construction is copy-pasted across all 10 classes rather than factored out.

The `_make_trunk_and_heads()` / `_forward_trunk_and_heads()` helpers exist (`model.py:265-326`) but are only used by some variants. Others (like `TSBaselineModel`) inline the same logic.

---

## 3. Observations / Feature Extraction

### 3a. `nn_features.cpp` Is the C++ Source of Truth

`nn_features.hpp` defines `BatchInputs::fill_slot()` and `forward_model_batched()`. This is used by `mcts_batched.cpp` for batched inference. Single-sample `forward_model()` is used by `learned_policy.cpp` and `mcts.cpp`. Feature extraction is thus unified on the C++ side.

Feature dimensions: `kScalarDim=11`, `kCardSlots=112` (4 masks = 448), `kCountrySlots=86` (2 sides = 172). Total input is 631 floats.

### 3b. No Schema Documentation

The feature vector layout is implicit in `nn_features.cpp:39-51` (scalars) and `nn_features.cpp:32-37` (card masks). The Python dataset docstring (`dataset.py:26-37`) documents the normalization but does not cross-reference the C++ code. There is no shared schema file.

### 3c. Python State Observation via Bindings

From Python, game state is exposed as:
- `public_state_to_dict()` in `tscore_bindings.cpp:46-90`: Returns a dict with ~35+ keys (turn, ar, vp, defcon, influence arrays, 20+ bool flags). This is the observation API.
- `game_state_from_dict()` in `tscore_bindings.cpp:94-186`: Deserializes back.

The observation is **not** a clean typed struct from Python's perspective -- it's a raw dict. There is no Python-side dataclass wrapping the C++ `PublicState`. The Python `PublicState` (in `schemas.py`) is a separate dataclass used by the Python engine; it is not the same type as what the bindings return.

### 3d. Adding a New Feature

Adding a new scalar feature (e.g., "VP delta since last turn") would require changes in:
1. `nn_features.cpp` -- bump `kScalarDim`, add `ptr[11] = ...`
2. `nn_features.hpp` -- nothing explicit (dim is in .cpp)
3. `model.py` -- change `SCALAR_DIM = 12`, update all 10 model classes
4. `dataset.py` -- update scalar normalization docstring and `__getitem__`
5. `learned_policy.py` -- update `_extract_features` scalar list
6. If the feature requires new state: `game_state.hpp`, `tscore_bindings.cpp`

This is 5-6 files minimum for one scalar feature. The root cause is that the feature layout is defined implicitly in code rather than declaratively.

### 3e. Train/Eval Feature Mismatch Risk

Training data features are produced by `collect_selfplay_rows_jsonl.cpp` which manually constructs influence arrays and card masks in `cpp/tools/collect_selfplay_rows_jsonl.cpp:99-104,68-86`. These are serialized as JSON arrays. The Python dataset (`dataset.py`) reads these arrays. At inference time, `nn_features.cpp` constructs the same features.

The `collect_selfplay_rows_jsonl.cpp` code for influence (`influence_array()` at line 99) uses `pub.influence_of(side, ...)` which is the same accessor used by `nn_features.cpp:27-29`. Card masks use the same `CardSet::test()`. So the features should match, but the code paths are completely separate with no shared validation.

---

## 4. Other Architectural Issues

### 4a. mcts_batched.cpp Is a 3967-Line Monolith

This file contains:
- Game loop state machine (~500 lines)
- Tree node/edge structures + selection/expansion/backup (~1500 lines)
- MCTS simulation loop (~500 lines)
- Greedy benchmark mode (~300 lines)
- K-sample influence allocation (~200 lines)
- Profiling/diagnostics (~200 lines)
- JSONL row emission (~400 lines)
- Multiple helper functions duplicated from other files

A single file doing tree search, game orchestration, NN batching, action decoding, and JSONL serialization violates separation of concerns.

### 4b. `fast_mcts_batched.cpp` Is an Orphaned Fork

The `cpp/mcts_batched_fast/` directory is a 3191-line copy of `mcts_batched.cpp` with build artifacts checked in (binary `.o` files in `build/` and `build-asan/`). It has its own `CMakeLists.txt`. Any fix applied to `mcts_batched.cpp` must be manually ported.

### 4c. Magic Numbers

- `policies.cpp:20-52`: The `MinimalHybridParams` struct has ~30 hand-tuned magic numbers with no documentation of how they were derived or what game situations they address.
- `mcts_batched.cpp:44-47`: `kMaxCardLogits = 112`, `kMaxModeLogits = 8`, `kMaxCountryLogits = 86`, `kMaxStrategies = 8` are defined locally rather than derived from the shared game data constants.
- `learned_policy.cpp:166-167`: The DEFCON card list is inside the function body as a `static constexpr` local rather than a shared constant.

### 4d. Ten Model Classes With Shared Forward Logic

`model.py` has 10 `TS*Model` classes. Many share the same trunk+head pattern but inline it. The `_make_trunk_and_heads` / `_forward_trunk_and_heads` factorization was added partway through and only some newer classes use it. `TSBaselineModel` (the original) does not use it.

### 4e. No Observation/Action Space Abstraction

There is no `ObservationSpace` or `ActionSpace` object. The feature vector dimensions are spread across `nn_features.cpp` constants, `model.py` module-level constants, and `dataset.py` normalization code. If the game adds a feature or the action encoding changes, each must be found and updated manually.

---

## Recommendations (Prioritized by ROI)

1. **Extract shared game loop primitives** from `mcts_batched.cpp`, `ismcts.cpp`, and `game_loop.cpp`. At minimum, `finish_turn()`, `sync_china_flags()`, turn setup, and deal/refill should be shared functions in a common file (e.g., `game_phases.hpp/.cpp`). The three separate state machines can call into these shared primitives. This eliminates the highest-risk class of bugs (divergent game logic).

2. **Centralize `kDefconLoweringCards` and `is_defcon_lowering_card()`** into a single header (e.g., `game_data.hpp` or a new `card_properties.hpp`). The current 6+ independent definitions with 2 different list contents is a correctness hazard.

3. **Extract `get_tensor()`, `build_action_from_country_logits()`, `accessible_countries_filtered()`** into shared headers. These are copy-pasted across 3-4 files each. `mcts_search_impl.hpp` already attempts this for some of them; the others should be consolidated there or in `nn_features.hpp`.

4. **Create a `parse_policy()` in the library** (e.g., in `policies.hpp/.cpp`) rather than having 4 copies in tool files. Similarly, move `game_result_str()`, `winner_side_int()`, and JSON serialization helpers into a shared `io_helpers.hpp`.

5. **Add a declarative feature schema** -- a single source of truth (could be a simple struct or config) that defines feature names, dimensions, normalization, and ordering. Both C++ and Python code should derive from it, or at least reference it for validation. This would make adding features a 2-file change instead of 5-6.

6. **Delete or archive `cpp/mcts_batched_fast/`**. It is a stale fork with build artifacts checked in. If it has experimental improvements worth keeping, merge them into the main `mcts_batched.cpp`.

7. **Consolidate model.py model classes** so that all 10 share the same trunk+head construction via `_make_trunk_and_heads()` / `_forward_trunk_and_heads()`. Currently `TSBaselineModel` (the most-used) inlines the forward logic, creating inconsistency with newer classes that use the factored helpers.

8. **Unify `PolicyKind` enum and `PolicyFn`** -- either extend `PolicyKind` to include `Learned` / `MCTS` variants with a factory that returns the appropriate `PolicyFn`, or deprecate the enum in favor of factory functions. The current dual-dispatch system means "which policy" is answered differently depending on the code path.
