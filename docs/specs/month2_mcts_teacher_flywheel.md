# Month 2 Spec: C++ PUCT MCTS, Teacher Search, and Data Flywheel

Machine-readable implementation spec. Sections are ordered by dependency.

---

## 0. Scope and Non-Goals

### In scope
- C++ PUCT tree with neural-network leaf evaluation via TorchScript
- pybind11 binding for Python-driven teacher search
- Hard-position mining from self-play traces
- Teacher search pipeline that caches MCTS-improved targets
- Training integration: KL-divergence distillation loss on teacher targets
- Calibration-aware value scaling to fix +0.4 positive-prediction bias

### NOT in scope (do not implement)
- Particle filtering or belief-state tracking for hidden information
- Distributed actor fleet or cloud orchestration
- Dirichlet noise at root (defer to Month 3 league play)
- Temperature-based action sampling in MCTS (always pick most-visited)
- Virtual loss for parallel tree search (single-threaded MCTS only)
- Any changes to the Python MCTS in `python/tsrl/engine/mcts.py`
- Progressive widening or RAVE
- Transposition tables (game states are not easily hashed with stochastic elements)

### Key constraint
All MCTS search runs perfect-information games (both hands visible).
This is acceptable for teacher-target generation on self-play positions
because both hands are known in the trace. It is NOT suitable for
online play against humans. Online play requires information-set MCTS
(Month 3).

---

## 1. C++ PUCT Node and Tree Structures

### Goal
Define the tree node struct and edge data for PUCT search. Edges store
visit count, total value, and prior probability. Nodes own their children.

### File: `cpp/tscore/mcts.hpp`

```cpp
#pragma once

#include <memory>
#include <optional>
#include <string>
#include <vector>

#include "game_state.hpp"
#include "legal_actions.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)
#include <torch/script.h>
#endif

namespace ts {

struct MctsEdge {
    ActionEncoding action;
    float prior = 0.0f;      // P(s,a) from policy network
    int visit_count = 0;      // N(s,a)
    double total_value = 0.0;  // W(s,a), sum of leaf values (USSR perspective)

    [[nodiscard]] double mean_value() const {
        return visit_count > 0 ? total_value / visit_count : 0.0;
    }
};

struct MctsNode {
    std::vector<MctsEdge> edges;  // one per legal action
    int total_visits = 0;         // N(s) = sum of edge visit counts
    bool is_terminal = false;
    double terminal_value = 0.0;  // only valid when is_terminal == true
    Side side_to_move = Side::USSR;

    // Select the edge with highest PUCT score.
    // Returns index into edges vector.
    // Formula: Q(s,a) + c_puct * P(s,a) * sqrt(N(s)) / (1 + N(s,a))
    // Q is from the perspective of side_to_move.
    [[nodiscard]] int select_edge(float c_puct) const;
};

struct MctsConfig {
    int n_simulations = 200;       // total simulations per search call
    float c_puct = 1.5f;          // exploration constant
    float value_weight = 1.0f;    // blend: value_weight * V(leaf) + (1-value_weight) * rollout
                                  // 1.0 = pure value network, 0.0 = pure rollout
    bool use_rollout_backup = false;  // if true, blend value head with heuristic rollout
    int rollout_depth_limit = 0;      // 0 = play to completion (only if use_rollout_backup)
};

struct SearchResult {
    ActionEncoding best_action;
    std::vector<MctsEdge> root_edges;  // all edges at root with visit counts + priors
    double root_value;                  // mean value at root (USSR perspective)
    int total_simulations;
};

// Main search entry point.  See section 2 for semantics.
#if defined(TS_BUILD_TORCH_RUNTIME)
SearchResult mcts_search(
    const GameState& root_state,
    torch::jit::script::Module& model,
    const MctsConfig& config,
    Pcg64Rng& rng
);
#endif

}  // namespace ts
```

### Acceptance criteria
- `MctsEdge` is a plain struct, no heap allocation per edge.
- `MctsNode::select_edge` returns the argmax of PUCT scores.
- When `side_to_move == Side::US`, Q is negated (all values stored USSR perspective,
  but US wants to minimize USSR value).
- `MctsNode` edges vector is populated once at expansion, never resized after.

### Notes
- Nodes are allocated on the heap via `std::unique_ptr` in the search function (section 2).
  The tree is local to one search call and freed after.
- `SearchResult::root_edges` is a copy (not a reference) so the tree can be freed.
- `MctsConfig::value_weight` is 1.0 for Month 2. The rollout backup path
  exists for ablation but is not the default.

---

## 2. C++ MCTS Search Function

### Goal
Implement PUCT search that takes a `GameState` + TorchScript model and
returns the best action plus root statistics.

### File: `cpp/tscore/mcts.cpp`

### Interface

```cpp
SearchResult mcts_search(
    const GameState& root_state,
    torch::jit::script::Module& model,
    const MctsConfig& config,
    Pcg64Rng& rng
);
```

### Algorithm (pseudocode)

```
root_node = expand(root_state, model)
for sim in 1..config.n_simulations:
    node = root_node
    state = clone(root_state)
    path = []   // list of (node*, edge_index)

    // SELECT
    while node is expanded and not terminal:
        edge_idx = node.select_edge(config.c_puct)
        edge = node.edges[edge_idx]
        apply edge.action to state
        path.append((node, edge_idx))
        if edge has no child node:
            break
        node = edge.child_node

    // EXPAND (if not terminal)
    if not node.is_terminal:
        child = expand(state, model)
        attach child to the last edge in path
        leaf_value = child.terminal_value if child.is_terminal
                     else evaluate(state, model)
    else:
        leaf_value = node.terminal_value

    // BACKPROPAGATE (USSR perspective value)
    for (ancestor_node, edge_idx) in reversed(path):
        ancestor_node.edges[edge_idx].visit_count += 1
        ancestor_node.edges[edge_idx].total_value += leaf_value
        ancestor_node.total_visits += 1

return SearchResult from root_node
```

### `expand(state, model)` subroutine

1. Determine `side = state.pub.phasing`.
2. Determine `holds_china` from `state`.
3. Call `legal_cards(hand, pub, side, holds_china)`.
4. For each legal card, call `legal_modes(card, pub, side)`.
5. For each (card, mode) where mode is Coup/Realign, call `legal_countries(card, mode, pub, side)` and create one edge per country target.
6. For each (card, mode) where mode is Event/Space, create one edge with empty targets.
7. For each (card, mode) where mode is Influence, create ONE edge with targets = [] (the actual influence placement is deferred to a heuristic post-search; see Notes).
8. Run the model forward pass to get `card_logits`, `mode_logits`, `country_logits`, `value`.
9. Compute the prior `P(s,a)` for each edge by combining the three factored heads:
   - `P(card)` = softmax(masked card_logits)[card_id]
   - `P(mode|card)` = softmax(masked mode_logits)[mode]
   - `P(country|card,mode)` = softmax(masked country_logits)[country_id] (for Coup/Realign)
   - `P(s,a) = P(card) * P(mode|card) * P(country|card,mode)`
   - For Event/Space: `P(s,a) = P(card) * P(mode|card)`
   - For Influence: `P(s,a) = P(card) * P(mode|card)` (no country factor)
10. Normalize all priors to sum to 1.0 across edges.
11. Set `node.side_to_move = side`.
12. If `state.game_over`, mark `is_terminal = true` and store terminal value.

### `evaluate(state, model)` subroutine

1. Extract features from `state` for the phasing side (same as `TorchScriptPolicy` feature extraction in `learned_policy.cpp`).
2. Run model forward pass.
3. Return `value` output (already USSR perspective in [-1, 1]).
4. If `config.use_rollout_backup`: blend with heuristic rollout value using `config.value_weight`.

### Feature extraction

Reuse the existing `extract_influence`, `extract_cards`, `extract_scalars` functions
from `learned_policy.cpp`. **Refactor these into a shared internal header**:

```cpp
// File: cpp/tscore/nn_features.hpp (NEW)
#pragma once
#if defined(TS_BUILD_TORCH_RUNTIME)
#include <torch/torch.h>
#include "game_state.hpp"
namespace ts { namespace nn {
    torch::Tensor extract_influence(const PublicState& pub);
    torch::Tensor extract_cards(const PublicState& pub, const CardSet& hand);
    torch::Tensor extract_scalars(const PublicState& pub, bool holds_china, Side side);
    // Returns dict {card_logits, mode_logits, country_logits, value, ...}
    c10::impl::GenericDict forward_model(
        torch::jit::script::Module& model,
        const PublicState& pub,
        const CardSet& hand,
        bool holds_china,
        Side side
    );
}}
#endif
```

Move the bodies from `learned_policy.cpp` anonymous namespace into `nn_features.cpp`.
Update `learned_policy.cpp` to call through the shared functions.

### Influence action handling

Influence placement has a combinatorial target space (distribute N ops across M countries).
MCTS does not enumerate all placements. Instead:

- At search time, each (card, Influence) pair is a single edge. The MCTS tree
  treats "play card X for influence" as one action and does not branch on targets.
- After selecting the edge at apply time, use the country_logits from the model
  to deterministically allocate ops (same logic as `build_action_from_country_logits`
  in `learned_policy.cpp`).
- This means the tree does NOT reason about different influence allocations for the
  same card. This is an acceptable approximation for Month 2.

### DEFCON safety

Apply the same DEFCON safety filtering as `TorchScriptPolicy::choose_action`:
- Remove edges for opponent danger cards at DEFCON <= 2 during expand.
- Remove Coup edges at DEFCON <= 2 during expand.
- If all edges removed, fall back to MinimalHybrid for that node.

### Acceptance criteria
- `mcts_search` returns a valid `SearchResult` with `best_action` set to the
  most-visited root edge's action.
- `root_edges` contains all root edges with their final visit counts and priors.
- `root_value` is the mean value across all root simulations.
- `total_simulations` equals `config.n_simulations`.
- No memory leaks: tree is freed when `mcts_search` returns.
- Single model forward pass per node expansion (not per simulation).
- Feature extraction is shared with `TorchScriptPolicy` (no duplication).

### Notes
- Tree nodes below the root are allocated with `std::make_unique<MctsNode>`.
  Store child pointers in a parallel vector alongside edges:
  `std::vector<std::unique_ptr<MctsNode>> children;` in `MctsNode`,
  indexed same as `edges`.
- The `model` parameter is a mutable reference because `torch::jit::script::Module::forward`
  is non-const in libtorch.
- All model inference runs on CPU. GPU batching is Month 3.

---

## 3. CLI Tool: `ts_mcts_search`

### Goal
Command-line tool that runs MCTS search from a fresh game start or a serialized
mid-game position and prints the result.

### File: `cpp/tools/ts_mcts_search.cpp`

### CLI interface

```
ts_mcts_search --model <path.pt>
               --n-sim <int>        (default: 200)
               --c-puct <float>     (default: 1.5)
               [--seed <uint32>]    (default: random)
               [--state-json <path>]  (mid-game state, same format as collect_selfplay_rows_jsonl)
               [--turn <int>]       (if no state-json, play to this turn then search)
```

### Behavior
1. If `--state-json` provided: deserialize `GameState` from JSON (same format as `game_state_from_dict` in bindings).
2. Else: reset a new game, optionally advance to `--turn` using MinimalHybrid.
3. Load TorchScript model from `--model`.
4. Call `mcts_search(state, model, config, rng)`.
5. Print to stdout:
   - Best action (card_id, mode, targets)
   - Root value
   - Top-10 edges by visit count with: action, visits, mean_value, prior
   - Total wall-clock time

### Acceptance criteria
- Compiles and links against `tscore` with `TS_BUILD_TORCH_RUNTIME`.
- Prints valid JSON to stdout (for easy parsing by Python scripts).
- Exits with code 0 on success, 1 on error.

---

## 4. pybind11 Binding: `mcts_search_from_state`

### Goal
Expose MCTS search to Python for teacher search pipeline integration.

### File: `bindings/tscore_bindings.cpp` (modify existing)

### Python-visible function

```python
def mcts_search_from_state(
    state_dict: dict,           # same format as play_from_public_state
    model_path: str,            # path to TorchScript .pt file
    n_sim: int = 200,           # MCTS simulations
    c_puct: float = 1.5,       # exploration constant
    seed: int | None = None,    # RNG seed (None = random)
) -> dict:
    """Run PUCT MCTS from a full game state and return search results.

    Returns dict with keys:
        best_action: dict with card_id, mode, targets
        root_value: float (USSR perspective)
        total_simulations: int
        edges: list[dict] with keys:
            card_id: int
            mode: int
            targets: list[int]
            visits: int
            mean_value: float
            prior: float
        policy_target: list[float]  # len = len(edges), visit count distribution
                                    # (visits / total_visits), suitable as
                                    # distillation target
    """
```

### Implementation

```cpp
// In the #if defined(TS_BUILD_TORCH_RUNTIME) block of tscore_bindings.cpp:

m.def(
    "mcts_search_from_state",
    [](const py::dict& state_dict,
       const std::string& model_path,
       int n_sim,
       float c_puct,
       py::object seed_obj) -> py::dict {
        // 1. Deserialize state via existing game_state_from_dict
        ts::GameState gs = game_state_from_dict(state_dict);

        // 2. Load model (cache across calls — see Notes)
        auto model = torch::jit::load(model_path);
        model.eval();

        // 3. Build config
        ts::MctsConfig config;
        config.n_simulations = n_sim;
        config.c_puct = c_puct;

        // 4. Build RNG
        ts::Pcg64Rng rng = seed_obj.is_none()
            ? ts::Pcg64Rng()
            : ts::Pcg64Rng(seed_obj.cast<uint64_t>());

        // 5. Run search
        ts::SearchResult result = ts::mcts_search(gs, model, config, rng);

        // 6. Build return dict
        // ... (convert result to py::dict)
    },
    py::arg("state_dict"),
    py::arg("model_path"),
    py::arg("n_sim") = 200,
    py::arg("c_puct") = 1.5f,
    py::arg("seed") = py::none()
);
```

### Model caching

Loading a TorchScript model from disk per search call is expensive (~200ms).
Implement a simple thread-local cache:

```cpp
namespace {
    thread_local std::string cached_model_path;
    thread_local std::optional<torch::jit::script::Module> cached_model;
}

torch::jit::script::Module& get_or_load_model(const std::string& path) {
    if (path != cached_model_path || !cached_model.has_value()) {
        cached_model = torch::jit::load(path);
        cached_model->eval();
        cached_model_path = path;
    }
    return *cached_model;
}
```

### Acceptance criteria
- `mcts_search_from_state` is callable from Python.
- Returns a dict matching the documented schema.
- `policy_target` sums to 1.0 (within float tolerance).
- Model is loaded once and cached for repeated calls with the same path.
- Passes basic round-trip test: search from a fresh game returns a valid action.

---

## 5. Hard Position Mining

### Goal
Identify positions from self-play traces where the value head is uncertain
or where the game outcome disagreed significantly with the value prediction.
These are the positions worth spending teacher search budget on.

### File: `scripts/mine_hard_positions.py`

### CLI interface

```
uv run python scripts/mine_hard_positions.py \
    --data-dir data/combined_v47_vsh_filtered \
    --checkpoint checkpoints/v47/best.pt \
    --out hard_positions.jsonl \
    --top-k 5000 \
    [--min-turn 2] \
    [--max-turn 9] \
    [--batch-size 512] \
    [--difficulty-metric surprise]  # or "uncertainty" or "both"
```

### Difficulty metrics

1. **surprise**: `|value_target - value_pred|` -- positions where the model's
   prediction was most wrong relative to the game outcome. High surprise =
   the model had no idea this position would lead to the actual outcome.
   `value_target` comes from the dataset row (final_vp / 20).

2. **uncertainty**: `|value_pred|` is close to 0 -- positions where the model
   thinks the game is nearly even. These are the positions where search
   can add the most information.

3. **both**: rank by `surprise_score + uncertainty_score` (each normalized to [0,1]).

### Output format: JSONL

Each line is a JSON object containing the full `state_dict` needed by
`mcts_search_from_state`, plus metadata:

```json
{
    "game_id": "v47_vsh_game_00123",
    "step_index": 45,
    "turn": 5,
    "ar": 3,
    "side": 0,
    "value_pred": 0.12,
    "value_target": -0.65,
    "surprise_score": 0.77,
    "uncertainty_score": 0.88,
    "difficulty_score": 1.65,
    "state_dict": { ... full state for mcts_search_from_state ... }
}
```

### Implementation sketch

1. Load the Parquet dataset from `--data-dir`.
2. Load the model checkpoint.
3. Run inference on all rows in batches.
4. Compute difficulty scores.
5. Sort by `difficulty_score` descending.
6. Take top-K.
7. For each selected row, reconstruct the full `state_dict` from the dataset columns.
   The dataset must contain: `turn, ar, phasing, vp, defcon, milops, space,
   china_held_by, china_playable, ussr_influence, us_influence, discard, removed,
   ussr_hand, us_hand, deck` plus the boolean effect flags.
   **If the dataset does not contain hands/deck** (it currently stores only the
   acting side's known hand), the state_dict reconstruction must be documented
   as partial. For teacher search, we need full hands. Two options:
   - (a) Use the JSONL traces from `collect_selfplay_rows_jsonl` which have full state.
   - (b) Add `opponent_hand` and `deck` columns to the collection pipeline.
   **Preferred: option (a)**. Mine from JSONL trace files, not Parquet.
8. Write to `--out`.

### Acceptance criteria
- Script runs on existing self-play JSONL data and produces valid output.
- Output positions can be round-tripped through `mcts_search_from_state`.
- `difficulty_score` is deterministic for the same input + checkpoint.
- Logs summary statistics: total positions scanned, top-K stats
  (mean/median/max difficulty, turn distribution).

### Notes
- The mining script does NOT run MCTS. It only identifies candidate positions.
  MCTS is run in the teacher search pipeline (section 6).
- nice -n 10 for all data processing (per standing preference).
- Batch size 512 should fit in 4GB VRAM on RTX 3050.

---

## 6. Teacher Search Pipeline

### Goal
Run MCTS search on mined hard positions and cache the improved policy/value
targets for distillation.

### File: `scripts/teacher_search.py`

### CLI interface

```
uv run python scripts/teacher_search.py \
    --positions hard_positions.jsonl \
    --model checkpoints/v47/best.pt \
    --out teacher_targets_v47.jsonl \
    --n-sim 400 \
    --c-puct 1.5 \
    [--seed 42] \
    [--max-positions 2000] \
    [--resume]           # skip positions already in --out
    [--progress-interval 50]
```

### Output format: JSONL

Each line extends the input position with teacher targets:

```json
{
    "game_id": "v47_vsh_game_00123",
    "step_index": 45,
    "turn": 5,
    "ar": 3,
    "side": 0,
    "teacher_n_sim": 400,
    "teacher_c_puct": 1.5,
    "teacher_root_value": -0.23,
    "teacher_policy": {
        "card_visits": {"23": 180, "45": 120, "67": 100},
        "mode_visits": {"0": 200, "1": 150, "4": 50},
        "edges": [
            {"card_id": 23, "mode": 0, "targets": [], "visits": 180, "prior": 0.35, "mean_value": -0.18},
            {"card_id": 45, "mode": 1, "targets": [42], "visits": 120, "prior": 0.22, "mean_value": -0.31}
        ]
    },
    "teacher_card_target": [0.0, ..., 0.45, ..., 0.30, ...],  // len 111, visit-proportional
    "teacher_mode_target": [0.50, 0.375, 0.0, 0.0, 0.125],    // len 5, visit-proportional
    "teacher_value_target": -0.23
}
```

### `teacher_card_target` construction

For each card_id in 1..111, sum the visit counts of all root edges that used
that card, divide by total visits. This gives a probability distribution over
cards that can be used as a soft label for KL-divergence distillation.

### `teacher_mode_target` construction

Same: for each mode in 0..4, sum visit counts of all root edges with that mode,
divide by total. This is a soft label for the mode head.

### Implementation

```python
import json
import os
import time
os.nice(10)  # per standing preference

def run_teacher_search(positions_path, model_path, out_path, n_sim, c_puct, seed, ...):
    import tscore  # C++ binding

    done_keys = set()
    if resume and os.path.exists(out_path):
        with open(out_path) as f:
            for line in f:
                obj = json.loads(line)
                done_keys.add((obj["game_id"], obj["step_index"]))

    positions = []
    with open(positions_path) as f:
        for line in f:
            obj = json.loads(line)
            key = (obj["game_id"], obj["step_index"])
            if key not in done_keys:
                positions.append(obj)

    positions = positions[:max_positions]

    with open(out_path, "a") as fout:
        for i, pos in enumerate(positions):
            t0 = time.time()
            result = tscore.mcts_search_from_state(
                state_dict=pos["state_dict"],
                model_path=model_path,
                n_sim=n_sim,
                c_puct=c_puct,
                seed=seed + i if seed is not None else None,
            )
            elapsed = time.time() - t0

            # Build teacher targets from result["edges"]
            teacher_card = [0.0] * 111
            teacher_mode = [0.0] * 5
            total_v = result["total_simulations"]
            for edge in result["edges"]:
                card_idx = edge["card_id"] - 1  # 0-indexed
                if 0 <= card_idx < 111:
                    teacher_card[card_idx] += edge["visits"] / total_v
                teacher_mode[edge["mode"]] += edge["visits"] / total_v

            out_obj = {
                **pos,
                "teacher_n_sim": n_sim,
                "teacher_c_puct": c_puct,
                "teacher_root_value": result["root_value"],
                "teacher_policy": {
                    "card_visits": {str(e["card_id"]): e["visits"] for e in result["edges"]},
                    "mode_visits": {str(e["mode"]): e["visits"] for e in result["edges"]},
                    "edges": result["edges"],
                },
                "teacher_card_target": teacher_card,
                "teacher_mode_target": teacher_mode,
                "teacher_value_target": result["root_value"],
            }
            fout.write(json.dumps(out_obj) + "\n")
            fout.flush()

            if (i + 1) % progress_interval == 0:
                print(f"  [{i+1}/{len(positions)}] elapsed={elapsed:.1f}s "
                      f"root_value={result['root_value']:.3f}")
```

### Throughput estimate

With 400 simulations and ~1ms per model forward pass (CPU), each search
takes ~0.4s. For 2000 positions: ~13 minutes. Acceptable for a single-machine
pipeline.

### Acceptance criteria
- Produces valid JSONL output that can be loaded by the training script.
- `teacher_card_target` sums to 1.0 (within float tolerance).
- `teacher_mode_target` sums to 1.0 (within float tolerance).
- `--resume` correctly skips already-processed positions.
- Logs progress and ETA.
- Process priority is nice 10.

---

## 7. Training Integration: Teacher Target Distillation

### Goal
Add a KL-divergence distillation loss that trains the policy heads to match
teacher search targets, blended with the existing imitation loss.

### File: `scripts/train_baseline.py` (modify existing)

### New CLI flags

```
--teacher-targets <path>    Path to teacher_targets_v47.jsonl (or dir of .jsonl files)
--teacher-weight <float>    Weight of teacher KL-div loss relative to BC loss (default: 0.5)
--teacher-value-weight <float>  Weight of teacher value MSE vs BC value MSE (default: 0.3)
```

### Loss formulation

For a batch that contains both regular self-play rows and teacher-target rows:

```
# Regular BC loss (existing, unchanged)
L_bc = card_CE + mode_CE + country_CE + value_weight * value_MSE

# Teacher distillation loss (only on rows with teacher targets)
L_teacher_card = KL(teacher_card_target || softmax(card_logits))
L_teacher_mode = KL(teacher_mode_target || softmax(mode_logits))
L_teacher_value = MSE(value_pred, teacher_value_target)

L_teacher = L_teacher_card + L_teacher_mode + teacher_value_weight * L_teacher_value

# Combined loss
L_total = L_bc + teacher_weight * L_teacher  (on teacher rows)
L_total = L_bc                                (on non-teacher rows)
```

Where `KL(p || q) = sum(p * log(p / q))` computed via `F.kl_div(log_softmax(logits), target, reduction='batchmean')`.

### Dataset changes

#### Option A (preferred): Mixed dataset with teacher flag

Add teacher target columns to the `TS_SelfPlayDataset`:

```python
# In TS_SelfPlayDataset.__getitem__, if teacher targets exist for this row:
item["has_teacher_target"] = True
item["teacher_card_target"] = torch.tensor(row["teacher_card_target"], dtype=torch.float32)  # (111,)
item["teacher_mode_target"] = torch.tensor(row["teacher_mode_target"], dtype=torch.float32)  # (5,)
item["teacher_value_target"] = torch.tensor(row["teacher_value_target"], dtype=torch.float32)  # (1,)
```

#### Matching teacher targets to dataset rows

Teacher targets are keyed by `(game_id, step_index)`. Before training:
1. Load teacher JSONL into a dict keyed by `(game_id, step_index)`.
2. When building the dataset, check if the row's key exists in the teacher dict.
3. If yes, attach the teacher targets to the row.
4. If no, set `has_teacher_target = False` and use zero tensors for teacher targets.

### Implementation in `run_epoch`

```python
# After computing card_logits, mode_logits, value_pred:

if teacher_weight > 0:
    has_teacher = batch["has_teacher_target"].to(device, non_blocking=True).bool()
    if has_teacher.any():
        t_card = batch["teacher_card_target"].to(device, non_blocking=True)
        t_mode = batch["teacher_mode_target"].to(device, non_blocking=True)
        t_value = batch["teacher_value_target"].to(device, non_blocking=True)

        # Card KL-div: teacher_card_target is (B, 111), card_logits is (B, 111)
        log_probs_card = F.log_softmax(card_logits[has_teacher], dim=1)
        kl_card = F.kl_div(log_probs_card, t_card[has_teacher], reduction='batchmean')

        # Mode KL-div
        log_probs_mode = F.log_softmax(mode_logits[has_teacher], dim=1)
        kl_mode = F.kl_div(log_probs_mode, t_mode[has_teacher], reduction='batchmean')

        # Value MSE
        teacher_v_loss = F.mse_loss(value_pred[has_teacher], t_value[has_teacher])

        teacher_loss = kl_card + kl_mode + teacher_value_weight * teacher_v_loss
        loss = loss + teacher_weight * teacher_loss
```

### Acceptance criteria
- When `--teacher-targets` is not provided, training behavior is unchanged (backward compatible).
- When provided, teacher KL-div loss appears in epoch metrics as `teacher_kl_card`,
  `teacher_kl_mode`, `teacher_value_mse`.
- The fraction of batch rows with teacher targets is logged as `teacher_coverage`.
- Teacher targets do not leak into validation metrics (val uses BC loss only).
- Training does not OOM on RTX 3050 4GB with batch_size=256 and teacher targets.

### Notes
- KL-divergence with `reduction='batchmean'` divides by the number of teacher rows
  in the batch, not the full batch size. This ensures the gradient magnitude
  is independent of teacher coverage.
- The teacher JSONL contains the full state_dict but training only needs
  the targets. The dataset loader should extract only the target tensors
  during preprocessing, not at training time.

---

## 8. Calibration-Aware Value Scaling

### Goal
Fix the +0.4-0.6 over-confidence bias on positive value predictions from
vs-heuristic data. The value head predicts too high when it thinks USSR is
winning (from vs-heuristic games where heuristic opponents are weaker).

### Approach: Platt scaling (post-hoc)

Rather than changing the model architecture or training, apply a simple
learned affine transform to the value output at inference time:

```
v_calibrated = sigmoid(a * v_raw + b)  * 2 - 1
```

where `a` and `b` are fit on a held-out calibration set to minimize
calibration error.

### File: `scripts/fit_value_calibration.py` (NEW)

### CLI interface

```
uv run python scripts/fit_value_calibration.py \
    --data-dir data/combined_v47_vsh_filtered \
    --checkpoint checkpoints/v47/best.pt \
    --out calibration_params.json \
    [--n-bins 20]
```

### Output format

```json
{
    "method": "platt",
    "a": 1.23,
    "b": -0.15,
    "ece_before": 0.038,
    "ece_after": 0.012,
    "source": "v47_vsh_filtered",
    "n_samples": 50000
}
```

### Integration points

1. **C++ MCTS**: When using value head output in MCTS, apply calibration:

```cpp
// In mcts.cpp evaluate() function:
float raw_value = model_output_value;
float calibrated = 2.0f * sigmoid(config.calib_a * raw_value + config.calib_b) - 1.0f;
```

Add calibration parameters to `MctsConfig`:

```cpp
struct MctsConfig {
    // ... existing fields ...
    float calib_a = 1.0f;  // identity transform by default
    float calib_b = 0.0f;
};
```

When `calib_a == 1.0 && calib_b == 0.0`, the sigmoid-affine reduces to
approximately identity for values near 0, so the default config has no
calibration effect.

2. **Python binding**: Pass calibration params through:

```python
def mcts_search_from_state(
    state_dict, model_path, n_sim=200, c_puct=1.5,
    calib_a=1.0, calib_b=0.0,  # NEW
    seed=None,
) -> dict: ...
```

3. **Teacher search script**: Load calibration params from JSON and pass to search:

```python
if args.calibration:
    with open(args.calibration) as f:
        calib = json.load(f)
    calib_a, calib_b = calib["a"], calib["b"]
```

### Fitting procedure

```python
from scipy.optimize import minimize

def fit_platt(v_raw, v_target):
    """Fit a, b to minimize log-loss of sigmoid(a*v + b) predicting
    (v_target + 1) / 2 (rescaled to [0,1] for binary cross-entropy)."""
    y = (v_target + 1.0) / 2.0  # map [-1,1] to [0,1]

    def loss(params):
        a, b = params
        p = 1.0 / (1.0 + np.exp(-(a * v_raw + b)))
        p = np.clip(p, 1e-7, 1 - 1e-7)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

    result = minimize(loss, x0=[1.0, 0.0], method='Nelder-Mead')
    return result.x[0], result.x[1]
```

### Acceptance criteria
- `fit_value_calibration.py` produces a valid JSON file.
- ECE after calibration is lower than ECE before (on calibration set).
- C++ MCTS with calibration params produces different root values than without.
- Default params (a=1, b=0) produce behavior identical to uncalibrated search.

### Notes
- Platt scaling is fit ONCE per model version, not per search call.
- The calibration set should be the validation split, not the training split.
- scipy is already a transitive dependency. If not, add it: `uv add scipy`.
- Alternative: temperature scaling (single parameter T). Try Platt first
  because the bias is asymmetric (positive predictions over-confident,
  negative predictions OK).

---

## 9. Data Flywheel Integration

### Goal
Define the end-to-end pipeline that chains: train -> collect -> mine -> search -> train.

### No new code needed. This section documents the pipeline orchestration.

### Pipeline steps (per generation vN -> v(N+1))

```bash
# 1. Train vN from existing data
uv run python scripts/train_baseline.py \
    --data-dir data/combined_vN \
    --teacher-targets data/teacher_targets_v$(N-1).jsonl \
    --teacher-weight 0.5 \
    --out-dir checkpoints/vN

# 2. Export to TorchScript
uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint checkpoints/vN/best.pt \
    --out checkpoints/vN/best_traced.pt

# 3. Benchmark vN
uv run python scripts/benchmark.py \
    --model checkpoints/vN/best_traced.pt \
    --n-games 200

# 4. Collect self-play data (vN vs heuristic + vN vs v(N-1))
nice -n 10 ./build-ninja/ts_collect_selfplay_rows_jsonl \
    --ussr-model checkpoints/vN/best_traced.pt \
    --us-policy minimal_hybrid \
    --games 500 --out data/vN_vsh.jsonl

nice -n 10 ./build-ninja/ts_collect_selfplay_rows_jsonl \
    --ussr-model checkpoints/vN/best_traced.pt \
    --us-model checkpoints/v$(N-1)/best_traced.pt \
    --games 500 --out data/vN_selfplay.jsonl

# 5. Fit calibration (on validation split of new data)
uv run python scripts/fit_value_calibration.py \
    --data-dir data/combined_vN \
    --checkpoint checkpoints/vN/best.pt \
    --out checkpoints/vN/calibration.json

# 6. Mine hard positions from vN data
uv run python scripts/mine_hard_positions.py \
    --data-dir data/vN_vsh.jsonl data/vN_selfplay.jsonl \
    --checkpoint checkpoints/vN/best.pt \
    --out data/hard_positions_vN.jsonl \
    --top-k 3000

# 7. Teacher search on hard positions
uv run python scripts/teacher_search.py \
    --positions data/hard_positions_vN.jsonl \
    --model checkpoints/vN/best_traced.pt \
    --calibration checkpoints/vN/calibration.json \
    --out data/teacher_targets_vN.jsonl \
    --n-sim 400

# 8. Combine data for v(N+1)
uv run python scripts/jsonl_to_parquet.py \
    --input data/vN_vsh.jsonl data/vN_selfplay.jsonl \
    --out data/combined_v$(N+1)

# 9. Train v(N+1) with teacher targets from vN
uv run python scripts/train_baseline.py \
    --data-dir data/combined_v$(N+1) \
    --teacher-targets data/teacher_targets_vN.jsonl \
    --teacher-weight 0.5 \
    --out-dir checkpoints/v$(N+1)
```

### Automation script

Update `scripts/run_vN_pipeline.sh` to include steps 5-7 between
the existing collect and train steps.

### Acceptance criteria
- Pipeline runs end-to-end from vN to v(N+1) on a single machine.
- Teacher targets from generation N are used in training generation N+1.
- The pipeline script includes all steps and handles failures gracefully
  (exit on first error with `set -e`).
- Total wall time for steps 5-7 (calibration + mine + search) is under
  30 minutes for 3000 positions at 400 sims each.

---

## 10. Build System Changes

### File: `cpp/tscore/CMakeLists.txt`

Add `mcts.cpp` to the tscore library sources (inside the `TS_BUILD_TORCH_RUNTIME` block):

```cmake
if(TS_BUILD_TORCH_RUNTIME)
    target_sources(tscore PRIVATE learned_policy.cpp mcts.cpp nn_features.cpp)
    ...
endif()
```

### File: `cpp/tools/CMakeLists.txt`

Add `ts_mcts_search` tool:

```cmake
if(TS_BUILD_TORCH_RUNTIME)
    add_executable(ts_mcts_search ts_mcts_search.cpp)
    target_link_libraries(ts_mcts_search PRIVATE tscore)
    install(TARGETS ts_mcts_search RUNTIME DESTINATION bin)
endif()
```

### New files summary

| File | Type | Purpose |
|------|------|---------|
| `cpp/tscore/mcts.hpp` | C++ header | PUCT node/edge structs, search interface |
| `cpp/tscore/mcts.cpp` | C++ source | PUCT search implementation |
| `cpp/tscore/nn_features.hpp` | C++ header | Shared NN feature extraction |
| `cpp/tscore/nn_features.cpp` | C++ source | Shared NN feature extraction (moved from learned_policy.cpp) |
| `cpp/tools/ts_mcts_search.cpp` | C++ tool | CLI for running MCTS search |
| `scripts/mine_hard_positions.py` | Python | Mine uncertain/surprising positions |
| `scripts/teacher_search.py` | Python | Run MCTS on hard positions, cache targets |
| `scripts/fit_value_calibration.py` | Python | Fit Platt scaling for value head |

### Modified files

| File | Change |
|------|--------|
| `cpp/tscore/CMakeLists.txt` | Add mcts.cpp, nn_features.cpp |
| `cpp/tscore/learned_policy.cpp` | Refactor feature extraction to use nn_features |
| `cpp/tools/CMakeLists.txt` | Add ts_mcts_search target |
| `bindings/tscore_bindings.cpp` | Add mcts_search_from_state binding |
| `scripts/train_baseline.py` | Add --teacher-targets, --teacher-weight flags |
| `python/tsrl/policies/dataset.py` | Add teacher target columns |
| `scripts/run_vN_pipeline.sh` | Add calibration, mine, teacher search steps |

---

## 11. Implementation Order

Implement in this order to minimize blocked work:

1. **nn_features.hpp/cpp** (section 2 prereq): Extract shared feature code from learned_policy.cpp. Verify learned_policy still works (run existing benchmarks).

2. **mcts.hpp + mcts.cpp** (sections 1-2): Core PUCT implementation. Test with a smoke test that searches from a fresh game state.

3. **ts_mcts_search.cpp** (section 3): CLI tool. Validate by running search and inspecting output.

4. **tscore_bindings.cpp** (section 4): pybind11 binding. Test from Python.

5. **fit_value_calibration.py** (section 8): Calibration fitting. Run on existing v47 data.

6. **mine_hard_positions.py** (section 5): Position mining. Run on existing JSONL traces.

7. **teacher_search.py** (section 6): Teacher pipeline. Run on mined positions.

8. **train_baseline.py changes** (section 7): Distillation loss. Train v48 with teacher targets.

9. **Pipeline integration** (section 9): Update run_vN_pipeline.sh.

---

## 12. Testing Checklist

### C++ unit tests (add to `tests/cpp/`)

- `test_mcts_node_select_edge`: PUCT selection picks highest-prior unvisited edge first, then balances Q+U.
- `test_mcts_search_fresh_game`: Search from turn 1 returns a valid action and non-empty root edges.
- `test_mcts_search_terminal`: Search from a terminal state returns immediately with terminal value.
- `test_mcts_defcon_safety`: At DEFCON 2, no root edge involves a coup or opponent danger card event.
- `test_nn_features_roundtrip`: Features extracted by nn_features match those from learned_policy (regression).

### Python tests (add to `tests/python/`)

- `test_mcts_binding_smoke`: `mcts_search_from_state` returns a dict with all expected keys.
- `test_teacher_target_sum`: `teacher_card_target` sums to 1.0.
- `test_teacher_target_roundtrip`: Mine -> search -> load targets in training dataset.
- `test_calibration_identity`: With a=1, b=0, calibrated value approximately equals raw value near 0.
- `test_teacher_training_loss`: With teacher targets, total loss includes KL-div component.
- `test_backward_compat_no_teacher`: Without --teacher-targets, training produces identical results.

### Integration / regression

- Run `mcts_search` with n_sim=50 on 10 positions from the existing self-play data.
  Verify all returned actions are legal.
- Run the full pipeline (steps 1-9 from section 9) on a small dataset (100 games)
  and verify it completes without error.
- Compare v48 (with teacher distillation) win% vs heuristic against v47 (without).
  Target: measurable improvement (even +0.5% is signal with 400+ game benchmark).
