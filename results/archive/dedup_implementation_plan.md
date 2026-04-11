# Deduplication Implementation Plan

**Date:** 2026-04-06
**Based on:** `results/codebase_duplication_audit.md`

---

## Phase 1: Centralize DEFCON-Lowering Card Lists (Correctness Hazard)

### Problem
`kDefconLoweringCards` is defined **6+ times** across files with **two different contents**:
- `policies.cpp:37` uses a 7-card list `{4, 11, 13, 24, 53, 92, 105}` + separate `kDefconProbLoweringCards` and `kDefconRandomCoupCards`
- `mcts_batched.cpp:40`, `ismcts.cpp:45`, `mcts.cpp:61`, `learned_policy.cpp:165`, `mcts_search_impl.hpp:26` all use a 13-card flat list `{4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105}`

The 13-card flat list is the union of all three sublists from `policies.cpp`. The heuristic policy intentionally uses a finer 3-tier classification, but the divergent naming is a maintenance trap.

### What changes

**New file: `cpp/tscore/card_properties.hpp`**

Add a new header (approximately 35 lines) containing:
```cpp
#pragma once
#include "types.hpp"
#include <algorithm>
#include <array>

namespace ts {

// Flat list: all cards whose events can lower DEFCON (directly, probabilistically,
// or via random coups). This is the union used by NN-facing code and MCTS DEFCON
// safety checks.
inline constexpr std::array<int, 13> kDefconLoweringCardsAll = {
    4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105,
};

// Finer-grained sublists used by the heuristic policy for tiered penalties.
inline constexpr std::array<CardId, 7> kDefconLoweringCardsDirect = {4, 11, 13, 24, 53, 92, 105};
inline constexpr std::array<CardId, 1> kDefconProbLoweringCards = {20};
inline constexpr std::array<CardId, 2> kDefconRandomCoupCards = {39, 83};

[[nodiscard]] inline bool is_defcon_lowering_card(CardId card_id) {
    return std::find(kDefconLoweringCardsAll.begin(), kDefconLoweringCardsAll.end(),
                     static_cast<int>(card_id)) != kDefconLoweringCardsAll.end();
}

}  // namespace ts
```

**Files modified (delete local definitions, add `#include "card_properties.hpp"`):**

| File | Lines to delete | What to replace with |
|------|----------------|---------------------|
| `mcts_batched.cpp:40-42` | local `kDefconLoweringCards` array | `#include "card_properties.hpp"`, use `kDefconLoweringCardsAll` |
| `ismcts.cpp:45-47` | local `kDefconLoweringCards` array | same |
| `mcts.cpp:61` (approx) | local `kDefconLoweringCards` array | same |
| `learned_policy.cpp:165` (approx) | local `static constexpr` inside function body | same |
| `mcts_search_impl.hpp:26-28` | `kDefconLoweringCards` + `is_defcon_lowering_card()` | `#include "card_properties.hpp"`, use `ts::kDefconLoweringCardsAll` and `ts::is_defcon_lowering_card()` |
| `policies.cpp:37-39` | local `kDefconLoweringCards`, `kDefconProbLoweringCards`, `kDefconRandomCoupCards` | `#include "card_properties.hpp"`, use `kDefconLoweringCardsDirect`, `kDefconProbLoweringCards`, `kDefconRandomCoupCards` from the header |

The `is_defcon_lowering_card()` function currently in `mcts_search_impl.hpp:50-53` moves to `card_properties.hpp`. The `is_card_blocked_by_defcon()` function in `mcts_search_impl.hpp:55-75` stays in `mcts_search_impl.hpp` but calls the centralized `is_defcon_lowering_card()`.

**CMakeLists.txt changes:** None. `card_properties.hpp` is header-only. Add it to the install list in `cpp/tscore/CMakeLists.txt` (line ~62, add `card_properties.hpp` to the `install(FILES ...)` block).

### Verification step
```bash
cmake --build build-ninja -j && ctest --test-dir build-ninja --output-on-failure
uv run pytest tests/python/ -n 0
```
Also: run `benchmark_batched` before and after, compare games/sec (expect identical). Run a short self-play collection (100 games) and diff the output JSON — game results must be identical with same seed.

### Estimated scope
- 1 new file (~35 lines)
- 6 files edited (~5-10 lines each, mostly deletions + include adds)
- ~80 lines touched total

### Dependencies
None. This is the first phase.

### Risk
- **Low**: The actual lists are identical across all NN-facing code. The only "different" list is the heuristic policy's intentional 3-tier split, which we preserve.
- **Mitigation**: The install list update is cosmetic. The content is purely `inline constexpr`, so ODR violations are impossible.

---

## Phase 2: Extract `get_tensor()` and Action-Building Helpers into Shared Headers

### Problem
- `get_tensor()` is copy-pasted in `nn_features.cpp:59`, `learned_policy.cpp:22`, and `mcts.cpp:135`.
- `tensor_at()`, `argmax_index()`, `accessible_countries_filtered()`, `build_action_from_country_logits()` are duplicated between `learned_policy.cpp:33-50+` and `mcts_search_impl.hpp:105-196`.
- `greedy_action_from_outputs()` in `mcts_batched.cpp:3477-3645` (168 lines) is explicitly a copy of `TorchScriptPolicy::choose_action` from `learned_policy.cpp`.

### What changes

**Step 2a: Move `get_tensor()` to `nn_features.hpp` / `nn_features.cpp`**

`get_tensor()` is already defined in `nn_features.cpp:59` inside an anonymous namespace. Promote it:
- In `nn_features.hpp`, add after the `forward_model` declaration (~line 47):
  ```cpp
  torch::Tensor get_tensor(const c10::impl::GenericDict& dict, const char* key, bool required = true);
  ```
- In `nn_features.cpp`, remove the `namespace {` wrapper around `get_tensor()` (move it from anonymous namespace to `ts::nn` namespace).
- Delete the copies from `learned_policy.cpp:22-31` and `mcts.cpp:135-145`. Replace with `using ts::nn::get_tensor;` or qualify calls as `nn::get_tensor(...)`.

**Step 2b: Confirm `mcts_search_impl.hpp` is the canonical location for action helpers**

The following functions are already in `mcts_search_impl.hpp` and are the correct canonical versions:
- `tensor_at()` (line 105)
- `argmax_index()` (line 109)
- `accessible_countries_filtered()` (line 113)
- `build_action_from_country_logits()` (line 127)

Delete the duplicate copies from `learned_policy.cpp:33-48` (the `tensor_at`, `argmax_index`, `accessible_countries_filtered` definitions). Replace with `#include "mcts_search_impl.hpp"` and `using namespace ts::search_impl;` (or qualify calls).

**Note:** `learned_policy.cpp` currently has its own `build_action_from_country_logits()` at line 50. This is identical to the version in `mcts_search_impl.hpp:127-196`. Delete the `learned_policy.cpp` copy and use `search_impl::build_action_from_country_logits()`.

**Step 2c: Extract `greedy_action_from_outputs()` from `mcts_batched.cpp` into `mcts_search_impl.hpp`**

Move `greedy_action_from_outputs()` (mcts_batched.cpp:3477-3645, ~168 lines) into `mcts_search_impl.hpp`. It depends on `BatchOutputs`, `legal_cards`, `legal_modes`, `choose_action`, and the helpers already in that file. Add `#include "legal_actions.hpp"` to `mcts_search_impl.hpp` if not already present.

In `mcts_batched.cpp`, delete the function body and replace with a call to `search_impl::greedy_action_from_outputs(...)`.

In `learned_policy.cpp`, the `TorchScriptPolicy::choose_action()` function (which `greedy_action_from_outputs` mirrors) should call through to `search_impl::greedy_action_from_outputs()` after extracting the `BatchOutputs` from the single-sample forward pass. This requires creating a temporary `BatchOutputs` struct from the dict outputs. The conversion is ~10 lines.

**Files modified:**

| File | Change |
|------|--------|
| `nn_features.hpp` | Add `get_tensor()` declaration |
| `nn_features.cpp` | Move `get_tensor()` out of anonymous namespace |
| `learned_policy.cpp` | Delete `get_tensor`, `tensor_at`, `argmax_index`, `accessible_countries_filtered`, `build_action_from_country_logits`. Add includes. Refactor `choose_action` to use shared `greedy_action_from_outputs` |
| `mcts.cpp` | Delete `get_tensor`. Add `#include "nn_features.hpp"`, use `nn::get_tensor` |
| `mcts_batched.cpp` | Move `greedy_action_from_outputs` out, replace with call to shared version |
| `mcts_search_impl.hpp` | Add `greedy_action_from_outputs()` (~168 lines, moved from `mcts_batched.cpp`) |

### Verification step
```bash
cmake --build build-ninja -j && ctest --test-dir build-ninja --output-on-failure
uv run pytest tests/python/ -n 0
```
Compare `benchmark_batched` output (100 games, fixed seed) before/after — must be bit-identical.

### Estimated scope
- 6 files modified
- ~200 lines moved (not new), ~50 lines deleted, ~30 lines of new glue
- Net reduction: ~220 lines

### Dependencies
Phase 1 (card_properties.hpp) should be done first so that `mcts_search_impl.hpp` uses centralized DEFCON lists.

### Risk
- **Medium**: `greedy_action_from_outputs` in `mcts_batched.cpp` uses raw float arrays (`float card_logits_arr[kMaxCardLogits]`) in its fast path, while the `learned_policy.cpp` version uses torch tensors. They produce the same results but the `mcts_batched.cpp` version is optimized for throughput. The shared version must preserve the fast-path behavior.
- **Mitigation**: If the `mcts_batched.cpp` version has performance-critical differences from the `learned_policy.cpp` version, keep both but have the `learned_policy.cpp` version call through to the shared one, and leave the `mcts_batched.cpp` fast-path version as-is with a comment `// Performance-critical: mirrors search_impl::greedy_action_from_outputs but uses raw arrays`.
- **Alternative (safer)**: Skip moving `greedy_action_from_outputs` from `mcts_batched.cpp` if the fast-path version is materially different. Still do Steps 2a and 2b. Mark the `mcts_batched.cpp` version with a comment referencing the canonical version.

---

## Phase 3: Extract `finish_turn()` and Turn Constants into Shared Game Phases

### Problem
`finish_turn()` / `end_of_turn()` is defined identically (line-for-line) in:
- `mcts_batched.cpp:2300-2383` (named `finish_turn`)
- `ismcts.cpp:853-936` (named `finish_turn`)
- `game_loop.cpp:1053-1135` (named `end_of_turn`)

Additionally, `sync_china_flags()` / `sync_china()` is defined in 5 places, and the turn constants (`kMidWarTurn`, `kLateWarTurn`, `kMaxTurns`, `kSpaceShuttleArs`) are duplicated in at least 3 files.

### What changes

**New file: `cpp/tscore/game_phases.hpp`** (~20 lines)
**New file: `cpp/tscore/game_phases.cpp`** (~100 lines)

Contents of `game_phases.hpp`:
```cpp
#pragma once
#include "game_state.hpp"
#include "game_loop.hpp"  // for GameResult

namespace ts {

// Turn-boundary constants used by game loop and MCTS state machines.
inline constexpr int kMidWarTurn = 4;
inline constexpr int kLateWarTurn = 8;
inline constexpr int kMaxTurns = 10;
inline constexpr int kSpaceShuttleArs = 8;

// Sync GameState China booleans from PublicState.china_held_by.
void sync_china_flags(GameState& state);

// End-of-turn cleanup: milops penalty, DEFCON raise, scoring-card-held check,
// final scoring at turn 10, discard hands.
// Returns a GameResult if the game ends, otherwise nullopt.
std::optional<GameResult> finish_turn(GameState& gs, int turn);

}  // namespace ts
```

Contents of `game_phases.cpp`: the `finish_turn()` body from `mcts_batched.cpp:2300-2383` (canonical version), plus `sync_china_flags()` from `mcts_batched.cpp:352-355`.

**Files modified:**

| File | Change |
|------|--------|
| `game_loop.cpp:17-21` | Delete local `kMidWarTurn`, `kLateWarTurn`, `kMaxTurns`, `kSpaceShuttleArs`. Add `#include "game_phases.hpp"`. |
| `game_loop.cpp:33-36` | Delete `sync_china()`. Replace all calls (`sync_china(gs)`) with `sync_china_flags(gs)`. There are 3 call sites (~lines 839, 932, 1027). |
| `game_loop.cpp:1053-1135` | Delete `end_of_turn()`. Replace the single call site with `finish_turn(gs, turn)`. |
| `mcts_batched.cpp:36-39` | Delete local turn constants. Add `#include "game_phases.hpp"`. |
| `mcts_batched.cpp:352-355` | Delete local `sync_china_flags()`. Use `ts::sync_china_flags()`. |
| `mcts_batched.cpp:2300-2383` | Delete local `finish_turn()`. Use `ts::finish_turn()`. |
| `ismcts.cpp:36-39` | Delete local turn constants. Add `#include "game_phases.hpp"`. |
| `ismcts.cpp:223-226` | Delete local `sync_china_flags()`. Use `ts::sync_china_flags()`. |
| `ismcts.cpp:853-936` | Delete local `finish_turn()`. Use `ts::finish_turn()`. |
| `mcts.cpp:130-133` | Delete local `sync_china_flags()`. Use `ts::sync_china_flags()`. |
| `mcts_search_impl.hpp:100-103` | Delete `sync_china_flags()`. Add `#include "game_phases.hpp"`, use `ts::sync_china_flags()`. |
| `cpp/tscore/CMakeLists.txt` | Add `game_phases.cpp` to `add_library(tscore STATIC ...)` sources list (line 4). Add `game_phases.hpp` to install list. |

**Critical correctness check:** The `game_loop.cpp` version (`end_of_turn`) and the `mcts_batched.cpp`/`ismcts.cpp` versions (`finish_turn`) must be compared line-by-line. From my reading, they are identical except for the function name. The canonical version to keep is the one from `mcts_batched.cpp` since it's named `finish_turn` (which is what the MCTS callers already use).

### Verification step
```bash
cmake --build build-ninja -j && ctest --test-dir build-ninja --output-on-failure
uv run pytest tests/python/ -n 0
```
Run `benchmark_batched` (500 games, fixed seed) before/after — must produce identical game results. Compare games/sec — must not regress.

Additionally, diff the `game_loop.cpp:end_of_turn` and `mcts_batched.cpp:finish_turn` line-by-line before starting to confirm they are identical. If they differ, document the difference and choose the correct version based on game rules.

### Estimated scope
- 2 new files (~120 lines total)
- 8 files modified
- ~400 lines deleted across the duplicates
- Net reduction: ~280 lines

### Dependencies
Phase 1 (card_properties.hpp) should be done first.

### Risk
- **Medium-High**: The game loop state machines in `mcts_batched.cpp` and `ismcts.cpp` call `finish_turn()` from within anonymous namespaces. Moving the function to a `.cpp` file means it's no longer inlineable. However, `finish_turn()` is called once per turn (not per simulation step), so this has zero measurable performance impact.
- **Risk**: `game_loop.cpp` calls its version `end_of_turn()` — renaming the call to `finish_turn()` is trivial but must be done carefully to not miss any call site.
- **Mitigation**: `grep -rn 'end_of_turn\|finish_turn' cpp/` before and after to confirm all references resolved.

---

## Phase 4: Extract `parse_policy()` and CLI Helpers into Shared Location

### Problem
`parse_policy()` is copy-pasted in 4 tool files: `collect_selfplay_rows_jsonl.cpp:22`, `collect_trace_jsonl.cpp:16`, `learned_matchup.cpp:15`, `initial_headline_choice.cpp:64`. Similarly, `game_result_str()` and `winner_side_int()` are duplicated across tools.

### What changes

**Add to `policies.hpp`** (after the `choose_action` declaration, ~line 97):
```cpp
// Parse a policy kind from a CLI string ("random", "minimal", "minimal_hybrid").
PolicyKind parse_policy_kind(std::string_view name);
```

**Add to `policies.cpp`:**
```cpp
PolicyKind parse_policy_kind(std::string_view name) {
    if (name == "random") return PolicyKind::Random;
    if (name == "minimal" || name == "minimal_hybrid") return PolicyKind::MinimalHybrid;
    throw std::invalid_argument(std::string("unsupported policy kind: ") + std::string(name));
}
```

Note: Named `parse_policy_kind` (not `parse_policy`) to avoid collision with any existing symbols and to be more descriptive.

**Add `game_result_str()` to `game_loop.hpp`/`game_loop.cpp`** or a new `io_helpers.hpp`:
```cpp
const char* game_result_str(std::optional<Side> winner);
int winner_side_int(std::optional<Side> winner);
```

**Files modified:**

| File | Change |
|------|--------|
| `policies.hpp` | Add `parse_policy_kind()` declaration |
| `policies.cpp` | Add `parse_policy_kind()` definition |
| `collect_selfplay_rows_jsonl.cpp` | Delete local `parse_policy()`, use `ts::parse_policy_kind()` |
| `collect_trace_jsonl.cpp` | Delete local `parse_policy()`, use `ts::parse_policy_kind()` |
| `learned_matchup.cpp` | Delete local `parse_policy()`, use `ts::parse_policy_kind()` |
| `initial_headline_choice.cpp` | Delete local `parse_policy()`, use `ts::parse_policy_kind()` |

### Verification step
```bash
cmake --build build-ninja -j && ctest --test-dir build-ninja --output-on-failure
```
Run each tool with `--help` or a trivial invocation to confirm they still link and parse arguments correctly.

### Estimated scope
- 2 files modified in library (policies.hpp/cpp, ~10 lines added)
- 4 tool files modified (~8 lines deleted each)
- Net reduction: ~25 lines

### Dependencies
None. Can be done independently of other phases.

### Risk
- **Very low**: Pure mechanical refactor. The function body is identical across all copies.

---

## Phase 5: Consolidate `softmax_inplace()` and `apply_tree_action()` Duplicates

### Problem
`softmax_inplace()` is defined identically in both `mcts_batched.cpp:358-370` and `ismcts.cpp:229-246`. `apply_tree_action()` is defined in `mcts_search_impl.hpp:242-258` and also in `ismcts.cpp:248-264` (with a minor difference: `ismcts.cpp` ignores `new_pub` with `(void)new_pub`).

### What changes

`softmax_inplace()` should be added to `mcts_search_impl.hpp` since it's a search utility:
```cpp
inline void softmax_inplace(float* buf, int n) { ... }
```

Delete the copies from `mcts_batched.cpp:358-370` and `ismcts.cpp:229-246`.

For `apply_tree_action()`: it's already in `mcts_search_impl.hpp:242-258`. The `ismcts.cpp:248-264` version is nearly identical but has `(void)new_pub;` and assigns `state.pub` from `apply_action_live` differently. Verify they produce identical results, then delete the `ismcts.cpp` copy and use the shared version.

### Verification step
Same as Phase 3.

### Estimated scope
- 1 file modified (mcts_search_impl.hpp: +15 lines for softmax_inplace)
- 2 files modified (mcts_batched.cpp, ismcts.cpp: delete ~30 lines each)
- Net reduction: ~45 lines

### Dependencies
Phase 3 (game_phases.hpp) should be done first so that `sync_china_flags` references are already unified.

### Risk
- **Low**: `softmax_inplace` is a pure math function with no state dependencies. `apply_tree_action` needs careful diffing between the ismcts and mcts_search_impl versions.

---

## Phase 6: Consolidate Model Classes in `model.py`

### Problem
10 model classes in `model.py`, many inlining the trunk+heads pattern instead of using the existing `_make_trunk_and_heads()` / `_forward_trunk_and_heads()` helpers. `TSBaselineModel` (the most used) inlines everything.

### What changes

**Step 6a: Refactor `TSBaselineModel` to use `_make_trunk_and_heads` / `_forward_trunk_and_heads`**

In `TSBaselineModel.__init__()` (model.py:547-569), replace the manual trunk/head construction with:
```python
(self.trunk_proj, self.trunk_dropout, self.trunk_block1, self.trunk_block2,
 self.card_head, self.mode_head, self.strategy_heads, self.strategy_mixer,
 self.value_branch, self.value_head) = _make_trunk_and_heads(hidden_dim, dropout)
```

In `TSBaselineModel.forward()` (model.py:571-619), replace the manual forward with:
```python
trunk_input = torch.cat([h_inf, h_card, h_scalar], dim=-1)
return _forward_trunk_and_heads(
    trunk_input, self.trunk_proj, self.trunk_dropout,
    self.trunk_block1, self.trunk_block2,
    self.card_head, self.mode_head, self.strategy_heads, self.strategy_mixer,
    self.value_branch, self.value_head,
)
```

**Critical constraint**: The attribute names (`self.trunk_proj`, `self.card_head`, etc.) must remain identical so that existing checkpoint `.pt` files load without remapping. Verify by:
1. Loading a saved checkpoint with `strict=True`
2. Running inference and comparing output values

**Step 6b: Audit remaining 9 classes**

For each class that has the standard trunk+heads pattern, refactor to use the shared helpers. Classes with genuinely different architectures (GNN variants, attention model) keep their custom code.

Do NOT change any class's `forward()` output contract or parameter names.

### Verification step
```bash
uv run pytest tests/python/ -n 0
```
Load a recent checkpoint (e.g., `models/v90b.pt`) with `strict=True`. Run inference on 10 fixed inputs. Compare output dict values to pre-refactor outputs — must be identical to float32 precision.

### Estimated scope
- 1 file modified (model.py)
- ~100 lines deleted (inlined trunk/head code), ~20 lines added (calls to shared helpers)
- Net reduction: ~80 lines

### Dependencies
None. Independent of C++ phases.

### Risk
- **Medium**: If `_make_trunk_and_heads` creates attributes with different names than the existing `TSBaselineModel.__init__`, saved checkpoints will fail to load with `strict=True`.
- **Mitigation**: Before changing `TSBaselineModel.__init__`, print `sorted(model.state_dict().keys())` and confirm the factored version produces identical keys. The current `_make_trunk_and_heads` returns the same module types with the same layer structure, so keys should match when assigned to the same `self.*` attribute names.

---

## Phase 7: Add Feature Schema Documentation

### Problem
Feature layout (scalar normalization, card mask structure, influence layout) is defined implicitly in `nn_features.cpp:39-51` and `model.py:1-60` with no shared schema. Adding a feature requires changes in 5-6 files.

### What changes

**New file: `docs/feature_schema.md`** (~80 lines)

Document:
- Scalar features: index, name, normalization formula, C++ source line, Python source line
- Card mask layout: 4 slots of 112, what each slot contains
- Influence layout: 2 blocks of 86, USSR then US
- Total feature dimension: 631
- Output heads: card_logits (111), mode_logits (5), country_logits (86), strategy (4), value (1)

**Add cross-references:**
- In `nn_features.cpp:39` add comment: `// See docs/feature_schema.md for the canonical layout`
- In `model.py:1` (module docstring), add: `See docs/feature_schema.md for the canonical feature layout.`
- In `dataset.py` docstring, same cross-reference.

**Add compile-time / runtime assertion in `nn_features.cpp`:**
```cpp
static_assert(kScalarDim == 11, "Update docs/feature_schema.md if scalar dim changes");
```

**Add runtime assertion in `model.py` (module level):**
```python
assert SCALAR_DIM == 11, "Update docs/feature_schema.md if scalar dim changes"
```

### Verification step
Review the document for accuracy against the actual code. No functional changes to test.

### Estimated scope
- 1 new file (~80 lines)
- 3 files modified (add comments/assertions, ~5 lines each)

### Dependencies
None.

### Risk
- **None**: Documentation-only plus defensive assertions.

---

## Phase 8: Archive `cpp/mcts_batched_fast/`

### Problem
`cpp/mcts_batched_fast/` is a 3191-line fork of `mcts_batched.cpp` with build artifacts (`build/`, `build-asan/`) checked in. It's an orphaned experimental copy.

### What changes

1. Move the directory to `archive/mcts_batched_fast/` (using `git mv`).
2. Remove the `build/` and `build-asan/` subdirectories (compiled `.o` files should not be in version control).
3. Add a `README.md` in the archive directory noting it's a stale fork and listing the date of the last meaningful change.

### Verification step
```bash
cmake --build build-ninja -j && ctest --test-dir build-ninja --output-on-failure
```
Confirm the main build is unaffected (the fast fork has its own `CMakeLists.txt` and is not referenced from the root `CMakeLists.txt`).

### Estimated scope
- `git mv` of 1 directory
- Delete ~50MB of build artifacts

### Dependencies
None.

### Risk
- **Very low**: The directory is not referenced by any build target in the root `CMakeLists.txt`.

---

## Phase 9: Centralize NN Logit Dimension Constants

### Problem
`kMaxCardLogits = 112`, `kMaxModeLogits = 8`, `kMaxCountryLogits = 86`, `kMaxStrategies = 8` are defined locally in `mcts_batched.cpp:44-47` and `ismcts.cpp:41-44`. They should derive from the game data constants (`kCardSlots`, `kCountrySlots`) already in `types.hpp`.

### What changes

Add to `nn_features.hpp` (or `card_properties.hpp` / `types.hpp`):
```cpp
inline constexpr int kMaxCardLogits = kCardSlots;    // 112
inline constexpr int kMaxModeLogits = 8;             // ActionMode enum size
inline constexpr int kMaxCountryLogits = kCountrySlots;  // 86
inline constexpr int kMaxStrategies = 8;
```

Delete the local definitions from `mcts_batched.cpp:44-47`, `ismcts.cpp:41-44`, and any other files that redeclare them.

### Verification step
Same as Phase 3.

### Estimated scope
- 1 file modified (nn_features.hpp: +4 lines)
- 2 files modified (mcts_batched.cpp, ismcts.cpp: -4 lines each)

### Dependencies
None, but logically groups with Phase 1.

### Risk
- **Very low**: Pure constant consolidation.

---

## DO NOT DO

These changes look tempting but should be avoided:

1. **DO NOT rewrite the MCTS state machine.** The `BatchedGameStage` enum + `advance_until_decision()` pattern in `mcts_batched.cpp` is performance-critical and battle-tested. Factoring it to share with `game_loop.cpp` would require a state-machine abstraction that adds complexity without clear benefit. The shared `finish_turn()` and constants from Phase 3 are sufficient.

2. **DO NOT change the `PolicyFn` signature.** The current `std::function<std::optional<ActionEncoding>(const PublicState&, const CardSet&, bool, Pcg64Rng&)>` is clean and used everywhere. Adding parameters (like `Side`) or changing the return type would touch dozens of call sites for no correctness gain.

3. **DO NOT introduce virtual dispatch for policies.** The `PolicyKind` enum is vestigial but functional. Replacing it with a class hierarchy (e.g., `class Policy { virtual choose(...) = 0; }`) would add vtable overhead on the hot path and gain nothing — the current `PolicyFn` + lambda pattern already provides runtime polymorphism.

4. **DO NOT unify `PolicyKind` and `PolicyFn` into a single dispatch.** The enum handles CLI parsing; the `std::function` handles runtime dispatch. They serve different purposes. Merging them would require `PolicyKind` to know about `TorchScriptPolicy` and MCTS, creating circular dependencies.

5. **DO NOT attempt to share the game loop state machine between `mcts_batched.cpp` and `ismcts.cpp`.** These two files have different state machine enums (`BatchedGameStage` vs `IsmctsGameStage`), different slot structures, and different tree types. The shared primitives (`finish_turn`, `sync_china_flags`, constants) from Phase 3 are the right granularity.

6. **DO NOT create a Python wrapper class around the C++ `PublicState` dict.** The raw dict from `public_state_to_dict()` is the stable interface. A Python dataclass wrapper would need to be kept in sync with the C++ struct and would add a marshaling layer for no performance benefit.

7. **DO NOT refactor all 10 model classes into a single parametric class.** The GNN, attention, and embedding variants have genuinely different architectures. Forcing them into a single class with `if/else` branches would be worse than the current separate classes. Phase 6 (using shared trunk helpers) is the right granularity.

8. **DO NOT move `mcts_search_impl.hpp` into a `.cpp` file.** It's a header-only template/inline utility file. The inline functions are used in multiple translation units (`mcts_batched.cpp`, `ismcts.cpp`, `mcts.cpp`). Moving them to a `.cpp` would either require explicit instantiation or break the build.

9. **DO NOT create an `ObservationSpace` / `ActionSpace` abstraction layer.** This is a future nice-to-have but would require touching every model class, the dataset, the C++ feature extraction, and the bindings. The feature schema document (Phase 7) provides the documentation benefit at zero code cost.

10. **DO NOT change the MinimalHybrid magic numbers or add documentation for how they were derived.** They are hand-tuned and stable. Documenting "why 6.0 for influence_mode_bonus" would require archaeology that does not improve correctness.

---

## Execution Order Summary

| Phase | Priority | Est. effort | Risk | Dependencies |
|-------|----------|-------------|------|--------------|
| 1: DEFCON card lists | **Critical** | 1 hour | Low | None |
| 2: get_tensor + action helpers | High | 2 hours | Medium | Phase 1 |
| 3: finish_turn + turn constants | High | 2 hours | Medium-High | Phase 1 |
| 4: parse_policy + CLI helpers | Medium | 30 min | Very low | None |
| 5: softmax + apply_tree_action | Medium | 1 hour | Low | Phase 3 |
| 6: Model class consolidation | Medium | 1.5 hours | Medium | None |
| 7: Feature schema docs | Low | 30 min | None | None |
| 8: Archive fast_mcts_batched | Low | 15 min | Very low | None |
| 9: NN dimension constants | Low | 15 min | Very low | None |

**Total estimated effort: ~9 hours**

Each phase is independently committable. If only Phases 1-3 are completed, the highest-risk duplication (divergent DEFCON lists, triplicated finish_turn, scattered sync_china) is eliminated.
