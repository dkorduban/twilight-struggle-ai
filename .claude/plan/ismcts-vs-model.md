# Spec: ISMCTS vs Model Benchmark

## Goal
Add `benchmark_ismcts_vs_model` to allow ISMCTS(model_a) vs raw-policy(model_b).
Currently `benchmark_ismcts` only supports ISMCTS vs heuristic.

## Why
Need to measure ISMCTS search uplift: does ISMCTS(v45) beat raw-policy(v45)?
The heuristic is too weak (v45 already wins 96% as USSR) to measure this.

## Files to modify

### `cpp/tscore/ismcts.hpp`
Add declaration:
```cpp
std::vector<GameResult> play_ismcts_vs_model_pooled(
    int n_games,
    torch::jit::script::Module& search_model,   // used for ISMCTS search
    torch::jit::script::Module& opponent_model,  // used for opponent's greedy decisions
    Side search_side,
    const IsmctsConfig& config,
    int pool_size,
    uint32_t base_seed,
    torch::Device device
);
```

### `cpp/tscore/ismcts.cpp`

1. Add a new function `resolve_model_decision(IsmctsGameSlot& slot, torch::jit::script::Module& model, torch::Device device)`:
   - Extract features from `slot.game_state` for the pending decision
   - Run single forward pass through `model` (no batching needed — opponent decisions are rare vs search)
   - Select greedy action (argmax with legal masking)
   - Apply action to game state
   - Pattern: copy from `resolve_heuristic_decision` but replace `choose_action(PolicyKind::MinimalHybrid, ...)` with model inference using `nn::extract_features()` + `model.forward()` + `nn::decode_action()`

2. Add `play_ismcts_vs_model_pooled()`:
   - Copy `play_ismcts_matchup_pooled`
   - Accept additional `torch::jit::script::Module& opponent_model` parameter
   - In `advance_until_search_or_done`: replace `resolve_heuristic_decision(slot)` calls with `resolve_model_decision(slot, opponent_model, device)`
   - Note: `advance_until_search_or_done` needs an additional parameter for the opponent model. Add `std::optional<std::reference_wrapper<torch::jit::script::Module>>` or just a pointer.

3. The main game loop structure stays the same:
   - Search side: batched ISMCTS (unchanged)
   - Opponent side: single model forward pass per decision (new)

### `bindings/tscore_bindings.cpp`
Add Python binding:
```cpp
m.def("benchmark_ismcts_vs_model",
    [](const std::string& search_model_path,
       const std::string& opponent_model_path,
       ts::Side search_side,
       int n_games, int n_determinizations, int n_simulations,
       py::object seed_obj, int pool_size,
       int max_pending_per_det, const std::string& device_str) {
        // Load both models, call play_ismcts_vs_model_pooled
    },
    // Default: pool_size=16, n_det=8, n_sim=400
);
```

Also add `benchmark_ismcts_vs_model_both_sides` variant that runs n_games/2 with
search_side=USSR and n_games/2 with search_side=US, similar to how
`benchmark_model_vs_model_batched` works.

Default hyperparams: n_determinizations=16, n_simulations=100, pool_size=16.
Literature (Cowling 2012) shows more dets helps more than more sims for hidden info games.
16×100 gives 2× better info-set coverage vs 8×400 at half the compute.

## Key patterns to follow

Look at existing code for:
- `resolve_heuristic_decision()` in `ismcts.cpp` — pattern for resolving opponent decisions
- `nn::extract_features()` + model forward — see `mcts_batched.cpp` for how to do single inference
- `play_ismcts_matchup_pooled()` — base to copy from
- `benchmark_model_vs_model_batched` binding — pattern for loading two models

## Performance notes

- Opponent inference is NOT on the critical path. Search does 8×400=3200 forward passes
  per decision; opponent does 1. Single (non-batched) inference for opponent is fine.
- Use the same device for both models to avoid GPU↔CPU transfers.
- `pool_size=16-32` is recommended for GPU throughput.

## Test cases
- ISMCTS(v45) vs raw-policy(v45), 20 games each side, verify it runs without crash
- Verify GameResult fields are correct (winner, final_vp, end_turn, end_reason)
- Verify both search_side=USSR and search_side=US work

## Acceptance criteria
- [ ] `tscore.benchmark_ismcts_vs_model(search_model, opponent_model, search_side, n_games=20)` works
- [ ] No regressions: `ctest --test-dir build-ninja --output-on-failure` passes
- [ ] Builds: `cmake --build build-ninja -j`
