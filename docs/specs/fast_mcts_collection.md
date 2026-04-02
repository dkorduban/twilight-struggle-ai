# Fast MCTS Collection: Engineering Plan

Machine-readable spec for getting n_sim=200 MCTS data collection to
>=1 game/sec on RTX 3050 4GB.

---

## 0. Current State and Bottleneck Analysis

### Measured throughput
- n_sim=0 (pure policy): ~6.3 games/sec (single-threaded C++ binary)
- n_sim=50 (serial MCTS, Python benchmark): ~0.109 games/sec = 9.2 sec/game
- n_sim=200 (estimated): ~0.03 games/sec = ~35 sec/game

### Where time goes at n_sim=200
A typical game has ~120 decision points (both sides). Each decision
requires 200 MCTS simulations. Each simulation expands one leaf node,
which requires one `nn::forward_model()` call plus the root expansion.
So: ~120 moves * 201 forward passes = ~24,120 forward passes per game.

Each `nn::forward_model()` call currently:
1. Builds 3 input tensors from C++ game state (~5-10 us)
2. Calls `model.forward()` via libtorch TorchScript (batch_size=1)
3. Returns dict of output tensors

At batch_size=1 on RTX 3050, a 447K-param model forward pass takes
~0.3-0.5 ms (dominated by kernel launch overhead, not compute).
So: 24,120 * 0.4 ms = ~9.6 sec of GPU time per game.

At batch_size=32-64, the same model could process 32-64 states in
~0.5-1.0 ms total, because the GPU ALUs are barely utilized at
batch_size=1. Theoretical speedup from batching: 20-40x on the
forward pass component.

### Why BarrierBatcher failed
The BarrierBatcher required all N concurrent game threads to reach
the same synchronization point before firing one batch. MCTS trees
diverge immediately (different depths, different branching), so
threads spent most of their time waiting at the barrier. Result:
4.9x SLOWER than serial.

---

## 1. Recommended Approach

**Combination: A + C + E, implemented in phases.**

### Phase 1: Multi-process serial MCTS (Approach C) -- quick win
Run K independent game processes, each doing full serial MCTS.
No batching complexity. Each process loads its own model copy.

- K = 4-6 processes (constrained by 4GB VRAM: each libtorch model
  instance uses ~50-100 MB VRAM including CUDA context overhead;
  4 processes = ~400 MB, 6 = ~600 MB, leaving headroom)
- Expected: ~4-5x throughput = 0.12-0.15 games/sec at n_sim=200
- Trivial to implement (fork the binary, different seeds)
- **Not sufficient alone** to reach 1 game/sec, but a useful baseline.

### Phase 2: Batched leaf evaluation within a single process (Approach A)
Run M concurrent MCTS trees inside one process using a leaf-collection
loop (NOT barriers). This is the key speedup.

**Architecture: wavefront leaf collector**

```
Single process, single GPU, single model instance:

1. Maintain a pool of G active games, each with its own MCTS tree
2. For each "wave":
   a. For each active game, run one MCTS simulation's SELECT phase
      (traverse tree to leaf), applying virtual loss to selected edges
   b. Collect all G leaf states into a batch tensor
   c. Fire ONE batched forward pass (batch_size = G)
   d. Distribute results back to each game's pending expansion
   e. Complete EXPAND + BACKPROP for each game
3. When a game's current move finishes all n_sim simulations,
   commit the best action, advance the game, start next move's MCTS
4. When a game finishes entirely, replace it with a new game
```

This avoids the BarrierBatcher problem because:
- There is NO barrier. A single thread drives all G trees.
- Each wave does exactly one forward pass for G leaves.
- Games that finish a move early just start the next move.
- No thread synchronization at all -- it is single-threaded + GPU.

**Key insight**: MCTS simulations are independent within a move.
Simulation i does not depend on simulation i-1's result (they both
start from the root). The only dependency is that the tree is updated
between simulations (visit counts change selection). With virtual loss,
we can run G simulations in parallel across G different games, each
doing one simulation step per wave, and update the tree after each wave.

At G=32 games in the pool:
- Each wave: 32 leaf evaluations batched in one forward pass
- Forward pass at batch_size=32: ~0.8-1.2 ms (vs 32 * 0.4 = 12.8 ms serial)
- Speedup on forward pass: ~10-15x
- Per game: 201 waves * 1.0 ms / 32 games = ~6.3 ms of GPU time per game
- Plus CPU work (select, expand, backprop, game state copy): ~2-3 ms per sim
  = ~600 ms per game for 200 sims
- Total: ~0.6-0.8 sec per game
- Throughput: ~1.2-1.6 games/sec

At G=64:
- Forward pass at batch_size=64: ~1.0-1.5 ms
- Per game GPU: 201 * 1.25 ms / 64 = ~4 ms
- CPU still dominates at ~600 ms per game
- Throughput: ~1.5-2.0 games/sec
- VRAM: one model + 64 game states = ~200 MB total, fits easily

### Phase 3: Selective teacher search (Approach E) for 3-5x on top
Don't use n_sim=200 for every move. Use n_sim=0 (pure policy) for
most moves and n_sim=200 only for positions flagged as "hard":
- High value uncertainty (value head output near 0)
- Critical game moments (scoring card plays, DEFCON=2, late-war)
- Headline decisions
- First N action rounds of each turn

At ~10 hard positions per game (out of ~120 total moves):
- 110 moves at n_sim=0: ~17 ms total (negligible)
- 10 moves at n_sim=200 with batched evaluation: ~50-80 ms per move
- Total per game: ~0.5-0.8 sec
- Throughput: 1.2-2.0 games/sec per process
- With 2-3 processes: 2.5-6.0 games/sec

### Phase summary

| Phase | Approach | Throughput (n_sim=200) | Complexity | Incremental |
|-------|----------|----------------------|------------|-------------|
| 1     | Multi-process (C) | 0.12-0.15 g/s | 0.5 days | Baseline |
| 2     | Wavefront batching (A) | 1.2-2.0 g/s | 3-5 days | 10-15x over serial |
| 3     | Selective teacher (E) | 2.5-6.0 g/s | 1-2 days | 2-3x over Phase 2 |

**Target: Phase 2 alone reaches >=1 game/sec. Phase 3 is gravy.**

---

## 2. Expected Throughput

### Conservative estimate (Phase 2 only, G=32)
- 1.0-1.5 games/sec at n_sim=200 on RTX 3050
- ~3,600-5,400 games/hour
- ~2,000 games takes 22-33 minutes

### Optimistic estimate (Phase 2 + 3, G=64, selective)
- 3-5 games/sec effective
- ~2,000 games in 7-11 minutes

### For comparison
- Current n_sim=0: 6.3 games/sec = 2,000 games in 5.3 minutes
- Current n_sim=200 serial: ~0.03 games/sec = 2,000 games in 18 hours

---

## 3. Implementation Steps

### Phase 1: Multi-process wrapper (0.5 days)

No C++ changes needed. Write a shell/Python wrapper.

**File: `scripts/collect_mcts_multiproc.sh`**
```
# Launch K copies of ts_mcts_collect with different seed ranges
# Concatenate output JSONL files
# K = min(4, available_gpu_memory / 800MB)
```

But first, we need to build the MCTS collection binary (Phase 2
subsumes this).

### Phase 2: Wavefront batched MCTS collector (3-5 days)

#### Step 2.1: Batched forward pass function

**File: `cpp/tscore/nn_features.hpp` (modify)**

Add:
```cpp
namespace ts::nn {

// Batched forward pass: takes G states, returns G sets of outputs.
// Input tensors are pre-allocated and filled in-place.
struct BatchInputs {
    torch::Tensor influence;       // [G, 2*kCountrySlots]
    torch::Tensor cards;           // [G, 4*kCardSlots]
    torch::Tensor scalars;         // [G, kScalarDim]
    int capacity = 0;
    int filled = 0;

    void allocate(int batch_capacity);
    void fill_slot(int idx, const PublicState& pub, const CardSet& hand,
                   bool holds_china, Side side);
    void reset() { filled = 0; }
};

struct BatchOutputs {
    torch::Tensor card_logits;     // [G, kCardSlots]
    torch::Tensor mode_logits;     // [G, kModeCount]
    torch::Tensor country_logits;  // [G, kCountrySlots] or empty
    torch::Tensor strategy_logits; // [G, kStrategies] or empty
    torch::Tensor country_strategy_logits; // [G, kStrategies, kCountrySlots] or empty
    torch::Tensor value;           // [G, 1]
};

BatchOutputs forward_model_batched(
    torch::jit::script::Module& model,
    const BatchInputs& inputs
);

}  // namespace ts::nn
```

**File: `cpp/tscore/nn_features.cpp` (modify)**

Implement `BatchInputs::allocate`, `BatchInputs::fill_slot`, and
`forward_model_batched`. The key optimization: pre-allocate tensors
once, fill them via direct data pointer access (not index_put_),
and call `model.forward()` once for the full batch.

Use `tensor.data_ptr<float>()` for zero-copy fill:
```cpp
void BatchInputs::fill_slot(int idx, const PublicState& pub,
                             const CardSet& hand, bool holds_china, Side side) {
    float* inf_ptr = influence.data_ptr<float>() + idx * 2 * kCountrySlots;
    // Fill influence directly into pre-allocated memory
    // ... (same logic as extract_influence but writing to pointer)
    filled = std::max(filled, idx + 1);
}
```

#### Step 2.2: Virtual loss support in MctsNode

**File: `cpp/tscore/mcts.hpp` (modify)**

Add to `MctsEdge`:
```cpp
int virtual_loss = 0;  // temporary penalty during batched selection
```

Modify `MctsNode::select_edge` to account for virtual loss:
```cpp
int MctsNode::select_edge(float c_puct) const {
    // ... existing logic but:
    // effective_visits = edge.visit_count + edge.virtual_loss
    // effective_value = edge.total_value - edge.virtual_loss * VIRTUAL_LOSS_PENALTY
    // Use effective values in PUCT formula
}
```

#### Step 2.3: Wavefront MCTS engine

**File: `cpp/tscore/mcts_batched.hpp` (NEW)**

```cpp
#pragma once
#include "mcts.hpp"
#include "nn_features.hpp"

namespace ts {

struct GameSlot {
    GameState root_state;           // state at start of current move
    GameState sim_state;            // scratch state for current simulation
    std::unique_ptr<MctsNode> root; // MCTS tree for current move
    std::vector<std::pair<MctsNode*, int>> path; // current select path
    int sims_completed = 0;
    int sims_target = 0;            // = config.n_simulations
    bool pending_expansion = false; // waiting for batched NN result
    bool move_done = false;         // all sims done, ready to commit
    bool game_done = false;
    Pcg64Rng rng;

    // Per-game bookkeeping for JSONL output
    std::string game_id;
    std::vector<StepTrace> traces;
    GameResult result;
};

struct BatchedMctsConfig {
    MctsConfig mcts;
    int pool_size = 32;             // number of concurrent games
    int virtual_loss_weight = 3;    // virtual loss per pending edge
};

// Main entry point: collect N complete games using wavefront batched MCTS.
// Writes JSONL rows to `out_stream`.
void collect_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    const BatchedMctsConfig& config,
    uint32_t base_seed,
    std::ostream& out_stream
);

}  // namespace ts
```

**File: `cpp/tscore/mcts_batched.cpp` (NEW)**

Core loop pseudocode:
```
pool = [GameSlot for i in 0..pool_size], each with a fresh game

batch_inputs.allocate(pool_size)
while any game in pool is not done:
    batch_inputs.reset()
    active_count = 0

    for each slot in pool:
        if slot.game_done:
            if more_games_to_start:
                replace slot with new game
            else:
                continue

        if slot.move_done:
            commit_best_action(slot)  // write trace row, advance game
            if slot.game_done:
                continue
            start_new_mcts(slot)      // fresh tree for new move

        if slot.sims_completed >= slot.sims_target:
            slot.move_done = true
            continue

        // SELECT phase: traverse tree to leaf
        select_to_leaf(slot, config.mcts.c_puct)

        if slot.pending_expansion:
            // Leaf found, needs NN evaluation
            batch_inputs.fill_slot(active_count, ...)
            slot_map[active_count] = &slot
            active_count++
        else:
            // Terminal node or already-expanded node
            backprop(slot)
            slot.sims_completed++

    if active_count > 0:
        // ONE batched forward pass for all pending leaves
        outputs = forward_model_batched(model, batch_inputs)

        for i in 0..active_count:
            expand_from_outputs(slot_map[i], outputs, i)
            backprop(slot_map[i])
            remove_virtual_loss(slot_map[i])
            slot_map[i]->sims_completed++
```

Key implementation details:
- `select_to_leaf()` applies virtual loss to all edges on the path
- Virtual loss prevents the same leaf from being selected by
  multiple slots in the same wave (only relevant if we later do
  multi-sim-per-wave, but costs nothing to include)
- `expand_from_outputs()` reads batch output at index i, creates
  the MctsNode with priors, computes leaf value
- `backprop()` propagates leaf value up the path and clears virtual loss

**Estimated lines of code**: ~400-600 for mcts_batched.cpp

#### Step 2.4: Collection binary

**File: `cpp/tools/collect_mcts_games_jsonl.cpp` (NEW)**

CLI:
```
collect_mcts_games_jsonl
    --model <path.pt>
    --out <rows.jsonl>
    --games <N>
    --n-sim <int>           (default: 200)
    --pool-size <int>       (default: 32)
    --c-puct <float>        (default: 1.5)
    --seed <uint32>
    [--selective-k <int>]   (Phase 3: only search top-K hard positions)
    [--hard-threshold <float>]  (value uncertainty threshold)
```

Reuse the JSONL row format from `collect_selfplay_rows_jsonl.cpp`
but add MCTS columns:
- `mcts_visit_counts`: array of (card_id, mode, visits) for root edges
- `mcts_root_value`: root value from search
- `mcts_n_sim`: actual n_sim used for this move (0 or config value)

#### Step 2.5: CMake integration

**File: `cpp/tools/CMakeLists.txt` (modify)**

Add `collect_mcts_games_jsonl` target, link against tscore + torch.

#### Step 2.6: Integration test

**File: `tests/cpp/test_mcts_batched.cpp` (NEW)**

- Test that wavefront MCTS with pool_size=1 produces identical results
  to serial `mcts_search()` (same seed, same model)
- Test that pool_size=4 produces valid games (legal actions, no crashes)
- Test throughput: pool_size=32 should be >5x faster than pool_size=1
  at n_sim=50

### Phase 3: Selective teacher search (1-2 days)

#### Step 3.1: Hard position detector

**File: `cpp/tscore/mcts_batched.hpp` (modify)**

Add to `BatchedMctsConfig`:
```cpp
int selective_k = 0;               // 0 = search all moves
float hard_value_threshold = 0.3f; // |value| < threshold => hard
bool hard_scoring_cards = true;    // always search scoring card plays
bool hard_headlines = true;        // always search headlines
```

**File: `cpp/tscore/mcts_batched.cpp` (modify)**

In the move-start logic:
```cpp
bool should_search(const GameSlot& slot, const BatchedMctsConfig& config) {
    if (config.selective_k <= 0) return true;  // search everything
    if (config.hard_headlines && slot.root_state.pub.ar == 0) return true;
    // Run a quick policy-only forward pass to get value estimate
    // If |value| < hard_value_threshold, mark as hard
    // Also: scoring cards, DEFCON=2, late-war turns 8-10
    return is_hard;
}
```

For non-hard positions: use pure policy (n_sim=0). The policy-only
forward pass is already part of the batch, so zero extra cost.

---

## 4. Complexity Estimate

| Step | Description | Effort |
|------|-------------|--------|
| 2.1 | BatchInputs + batched forward | 1 day |
| 2.2 | Virtual loss in MctsNode | 0.25 days |
| 2.3 | Wavefront engine (mcts_batched.cpp) | 2-3 days |
| 2.4 | Collection binary + JSONL output | 0.5 days |
| 2.5 | CMake + build integration | 0.25 days |
| 2.6 | Tests | 0.5 days |
| 3.1-3.2 | Selective teacher search | 1 day |
| **Total** | | **5-6 Codex-days** |

"Codex-days" means elapsed days with a Codex agent doing the work
with human review. Actual wall-clock with iteration: ~1 week.

---

## 5. Fallback Plan

If Phase 2 wavefront batching does not reach 1 game/sec (e.g. due
to CPU bottleneck in game state cloning or action application):

### Fallback A: Reduce n_sim with temperature
Use n_sim=50 instead of 200. At 50 sims with batched evaluation:
- 50/200 = 4x fewer forward passes
- ~4 games/sec with pool_size=32
- Quality tradeoff: n_sim=50 already shows meaningful improvement
  over pure policy in the benchmark data

### Fallback B: TensorRT (Approach D)
Convert the TorchScript model to TensorRT with INT8 quantization.
Expected 2-4x speedup on small models due to kernel fusion and
reduced overhead.

```python
import torch_tensorrt
model = torch.jit.load("baseline_best.pt")
trt_model = torch_tensorrt.compile(model, inputs=[...],
    enabled_precisions={torch.float16, torch.int8})
```

Complexity: 1-2 days. Risk: TensorRT on WSL2 can have driver issues.
This is additive with Phase 2 batching.

### Fallback C: Cloud burst (Approach F)
Use Modal or Vast.ai for production collection. An A10G GPU
(24GB VRAM) can run pool_size=128 with batch_size=128 forward
passes. Expected throughput:

- A10G: ~5-10x faster forward pass than RTX 3050
- pool_size=128: better GPU utilization
- Estimated: 5-10 games/sec at n_sim=200
- Cost: ~$0.60/hr on Modal, so 2,000 games in ~5 min = $0.05

This is the escape hatch if local GPU is insufficient.

---

## 6. Non-Recommendations (Dead Ends)

### BarrierBatcher (barrier-synchronized batching across threads)
**Dead end.** Already benchmarked: 4.9x SLOWER than serial.
The fundamental problem is that MCTS trees diverge, so barrier
synchronization creates massive idle time. The wavefront approach
(Phase 2) solves this by driving all trees from a single thread
with no synchronization.

### Approach B: Dedicated inference thread with async queue
**Not recommended for Phase 2.** Adds threading complexity
(lock-free queues, futures, cache coherence) for marginal benefit
over the wavefront approach. The wavefront approach achieves the
same batching without any thread synchronization because one thread
drives everything.

Could revisit if CPU becomes the bottleneck (unlikely with a 447K
param model -- the CPU work per simulation is ~20-50 us for select +
backprop, and ~100-200 us for game state clone + action application).

### Full multi-threaded MCTS per game
**Dead end.** libtorch TorchScript is not thread-safe for concurrent
forward calls on the same Module without explicit locking. Multiple
model copies waste VRAM. And the GPU is the bottleneck, not CPU --
more CPU threads doing serial GPU calls just increase contention.

### TensorRT as primary strategy
**Not recommended as primary.** TensorRT gives 2-4x on the forward
pass, but the forward pass is only ~60% of the total time at n_sim=200
(rest is CPU game simulation). Batching gives 10-15x on the forward
pass AND amortizes CPU overhead. TensorRT is a good **additive**
optimization on top of batching, not a replacement.

### Model size reduction
**Not recommended.** The model is already 447K params. Halving it
would save ~0.1 ms per forward pass (from ~0.4 to ~0.3 ms at
batch_size=1). Not worth the quality hit. The problem is kernel
launch overhead and GPU underutilization, not model compute.

---

## 7. Memory Budget

### VRAM (4 GB RTX 3050)
- libtorch CUDA context: ~300 MB
- Model weights (447K params, FP32): ~2 MB
- Batch tensors at pool_size=64:
  - influence: 64 * 172 * 4 = 44 KB
  - cards: 64 * 448 * 4 = 115 KB
  - scalars: 64 * 11 * 4 = 3 KB
  - outputs: ~200 KB total
- CUDA workspace: ~200 MB
- **Total: ~500-600 MB. Fits easily.**

### RAM (16 GB, WSL2)
- Per GameSlot: GameState (~10 KB) * 2 (root + sim) + MCTS tree
- MCTS tree at n_sim=200: ~200 nodes * ~500 bytes = 100 KB per tree
- 64 slots * 120 KB = ~8 MB
- libtorch runtime: ~500 MB
- **Total: ~600-700 MB. No OOM risk.**

---

## 8. Batch Size Tuning Guide

The optimal pool_size depends on GPU saturation vs CPU overhead.
Profile with these pool sizes and pick the knee of the curve:

| pool_size | Expected batch latency (ms) | Per-game GPU (ms) | Notes |
|-----------|---------------------------|-------------------|-------|
| 1         | 0.4                       | 80                | Serial baseline |
| 8         | 0.5                       | 12.5              | 3x speedup |
| 16        | 0.6                       | 7.5               | Good start |
| 32        | 0.8                       | 5.0               | Sweet spot |
| 64        | 1.2                       | 3.75              | Near-optimal |
| 128       | 2.0                       | 3.1               | Diminishing returns |

RTX 3050 has 2560 CUDA cores and 128-bit memory bus. A 447K-param
model at FP32 has ~1.8 MB of weights. At batch_size=32, the compute
is ~28M FLOPs -- still far below the GPU's ~9 TFLOPS capacity.
Saturation likely begins around batch_size=256-512, which is larger
than we need. The latency increase from 1 to 64 is mainly kernel
launch amortization, not compute saturation.

**Recommended starting point: pool_size=32, tune from there.**

---

## 9. Testing and Validation Plan

### Correctness
1. `pool_size=1` wavefront MCTS must produce identical search results
   to serial `mcts_search()` given the same seed and model
2. All generated JSONL rows must pass the existing schema validator
3. No DEFCON-1 violations (rate must stay <5%)
4. No illegal actions after masking

### Performance
1. Measure games/sec at pool_size=1,8,16,32,64 with n_sim=50
2. Measure games/sec at pool_size=32 with n_sim=50,100,200
3. Compare search quality: MCTS root value distribution should be
   similar between serial and batched at same n_sim
4. GPU utilization via `nvidia-smi`: should exceed 50% at pool_size>=16

### Regression
1. Train a model on batched MCTS data, compare win rate vs model
   trained on serial MCTS data -- should be equivalent
2. No performance regression on n_sim=0 collection path

---

## 10. File Change Summary

| File | Action | Phase |
|------|--------|-------|
| `cpp/tscore/nn_features.hpp` | Add BatchInputs, BatchOutputs, forward_model_batched | 2.1 |
| `cpp/tscore/nn_features.cpp` | Implement batched forward + direct-pointer fill | 2.1 |
| `cpp/tscore/mcts.hpp` | Add virtual_loss field to MctsEdge | 2.2 |
| `cpp/tscore/mcts.cpp` | Account for virtual_loss in select_edge | 2.2 |
| `cpp/tscore/mcts_batched.hpp` | NEW: GameSlot, BatchedMctsConfig, collect_games_batched | 2.3 |
| `cpp/tscore/mcts_batched.cpp` | NEW: Wavefront engine (~500 lines) | 2.3 |
| `cpp/tools/collect_mcts_games_jsonl.cpp` | NEW: Collection binary | 2.4 |
| `cpp/tools/CMakeLists.txt` | Add new binary target | 2.5 |
| `tests/cpp/test_mcts_batched.cpp` | NEW: Correctness + perf tests | 2.6 |
