# Spec: Batched ISMCTS (cross-determinization + GPU)

## Problem

`ismcts_search()` runs N determinizations **sequentially**, each calling
`mcts_search()` which does **one unbatched `nn::forward_model()` per leaf
expansion**. For 8det x 400sims = 3,200 individual NN forward passes per
decision point, ~70 decisions/game = ~224,000 forward passes per game.

Current performance: ~3.3 min/game on CPU. GPU utilization: 0%.
CPU utilization: ~50% (single-threaded on multi-core).

## Goal

Batch NN inference **across determinizations** so all 8 leaf evaluations per
simulation round go through one `forward_model_batched()` call. Optionally
run inference on GPU. Target: 5-8x speedup (20-40 sec/game).

## Architecture

### Existing infrastructure to reuse

1. **`nn::BatchInputs` / `nn::forward_model_batched()`** — already in
   `nn_features.hpp`. Allocates batch tensors, fills slots, runs batched
   forward. Used by `mcts_batched.cpp`.

2. **`GameSlot` pattern from `mcts_batched.cpp`** — each slot has its own
   MCTS tree, `root_state`, `sim_state`, `path`, `sims_completed`,
   `pending_expansion`. The `select_to_leaf()` / `expand_from_outputs()` /
   `backpropagate()` functions are exactly what we need.

3. **`sample_determinization()`** — already in `ismcts.cpp`.

4. **`IsmctsConfig` / `IsmctsResult`** — keep the same external interface.

### New: `ismcts_search_batched()`

Replace the sequential loop in `ismcts_search()` with a wavefront loop
over determinizations:

```
struct DeterminizationSlot {
    GameState det_state;      // determinized full state
    GameState sim_state;      // current simulation state (reset each sim)
    std::unique_ptr<MctsNode> root;
    std::vector<std::pair<MctsNode*, int>> path;
    int sims_completed = 0;
    bool pending_expansion = false;
    bool pending_root_expansion = false;
    bool root_expanded = false;
    Pcg64Rng rng;
};
```

Algorithm:
```
1. Create N DeterminizationSlots, each with sample_determinization()
2. Allocate BatchInputs with capacity = N

Phase A: Expand all roots (1 batched forward call)
  For each slot:
    Try expand_without_model() first (terminal/fallback)
    If needs NN: fill_slot into batch
  forward_model_batched(batch)
  For each slot in batch: expand_from_outputs() → set root
  Apply Dirichlet noise to each root

Phase B: Run simulations in lockstep
  For sim_round = 0 .. n_simulations-1:
    batch.reset()
    For each slot:
      if sims_completed >= n_simulations: skip
      select_to_leaf()
      if needs_batch: fill_slot into batch
      else: backpropagate immediately
    if batch not empty:
      forward_model_batched(batch)
      For each batched slot:
        expand_from_outputs()
        backpropagate()

3. Aggregate edges across determinizations (existing code)
4. Return IsmctsResult
```

This does at most `n_simulations + 1` batched forward calls (each of size
<= n_determinizations) instead of `n_determinizations * n_simulations`
individual calls.

### GPU support

Add `torch::Device device` parameter to `ismcts_search_batched()` and
`play_ismcts_matchup()`. When `device != torch::kCPU`:
- Move model to device once at start: `model.to(device)`
- `BatchInputs::allocate(N, device)` — already supported
- Results come back on device, `expand_from_outputs` already handles this

The `benchmark_games_batched()` already takes a `torch::Device` parameter
as precedent (see `mcts_batched.hpp:110`).

### Game-level parallelism

`play_ismcts_matchup()` currently runs games sequentially. Add a simple
game pool (size 4-8) where multiple games run concurrently, sharing the
same batch buffer. Each game's ISMCTS search contributes its
determinization leaves to the shared batch. This increases batch size
from 8 to 32-64, better saturating GPU.

This is optional / Phase 2. The cross-determinization batching alone is
the critical fix.

## Files to modify

| File | Change |
|------|--------|
| `cpp/tscore/ismcts.cpp` | Add `ismcts_search_batched()`, refactor `play_ismcts_matchup()` to use it |
| `cpp/tscore/ismcts.hpp` | Add `ismcts_search_batched()` declaration, add `device` param to `play_ismcts_matchup()` |
| `bindings/tscore_bindings.cpp` | Add `device` parameter to `benchmark_ismcts` binding |

## Functions to reuse from mcts_batched.cpp

These are currently in an anonymous namespace in `mcts_batched.cpp`. To
reuse them, either:
- **(Preferred)** Copy the core logic (select_to_leaf, expand_from_outputs,
  backpropagate, expand_without_model) into a shared internal header
  `mcts_batched_impl.hpp`, or
- Duplicate the ~100 lines needed in `ismcts.cpp` with a comment noting
  the shared origin.

Key functions needed:
- `expand_without_model(state, rng) -> optional<ExpansionResult>`
- `expand_from_outputs(state, outputs, batch_index, config, rng) -> ExpansionResult`
- `select_to_leaf(slot, config) -> SelectionResult` (adapted for DeterminizationSlot)
- `backpropagate(slot, leaf_value, virtual_loss_weight)`

Since DeterminizationSlot is simpler than GameSlot (no game lifecycle, no
headline logic), the select_to_leaf and backpropagate can be simplified
or templated. Simplest approach: make them work on the shared fields
(root, sim_state, path, sims_completed, pending_expansion, rng).

## Existing code to extract

From `mcts_batched.cpp`, extract into `mcts_search_impl.hpp` (internal):

```cpp
// mcts_search_impl.hpp — shared MCTS tree operations for batched search
struct ExpansionResult { unique_ptr<MctsNode> node; double leaf_value; };
struct SelectionResult { bool needs_batch; double leaf_value; };

// These operate on any struct with: root, sim_state, path, 
// pending_expansion, pending_root_expansion, rng
template <typename Slot>
SelectionResult select_to_leaf(Slot& slot, const MctsConfig& config, float c_puct);

template <typename Slot>
void backpropagate(Slot& slot, double leaf_value, int virtual_loss_weight);

optional<ExpansionResult> expand_without_model(const GameState& state, Pcg64Rng& rng);
ExpansionResult expand_from_outputs(const GameState& state, const BatchOutputs& outputs,
                                     int64_t batch_index, const MctsConfig& config, Pcg64Rng& rng);
```

## Binding changes

In `bindings/tscore_bindings.cpp`, update `benchmark_ismcts`:
```python
# Before:
tscore.benchmark_ismcts(model_path, side, n_games, 
    n_determinizations=8, n_simulations=400, seed=42)

# After (backward compatible):
tscore.benchmark_ismcts(model_path, side, n_games,
    n_determinizations=8, n_simulations=400, seed=42,
    device="cpu")  # or "cuda"
```

## Testing

1. **Correctness**: Run 10 games with unbatched (`mcts_search`) and batched
   (`ismcts_search_batched`) with same seeds. Results should be identical
   (same determinization sampling, same tree traversal order).
   
   Note: exact match requires determinizations to be processed in the same
   order. The wavefront approach processes them in lockstep which preserves
   order, so results should be bit-identical.

2. **Performance**: Time 10 games with old vs new on CPU. Expect 5-8x speedup.

3. **GPU**: Time 10 games on CUDA vs CPU batched. Expect additional 2-3x.

## NOT in scope

- Game-level parallelism (multiple games sharing batch) — Phase 2
- Thread-level parallelism within determinizations — not needed with batching
- Changes to MCTS algorithm (c_puct, Dirichlet, etc.) — orthogonal
