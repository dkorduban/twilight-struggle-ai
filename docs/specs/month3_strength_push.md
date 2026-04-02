# Month 3 Spec: Strength Push, Exploration, Evaluation, and Online Play

Machine-readable implementation spec. Sections are ordered by dependency.

---

## 0. Scope and Non-Goals

### In scope
- Dirichlet noise at MCTS root for exploration during self-play collection
- Temperature-based action sampling from MCTS visit counts in self-play
- Epsilon-greedy exploration noise in policy rollouts during collection
- BayesElo rating system for stable cross-generation evaluation
- Multi-agent evaluation ladder (round-robin between checkpoints)
- Information-Set MCTS via determinization for online play under hidden information
- Architecture experiment: benchmark attention model vs MLP baseline
- Online play server (HTTP/WebSocket interface)

### NOT in scope (do not implement)
- Distributed training or multi-GPU data parallelism
- Cloud deployment, container orchestration, or CI/CD pipelines
- UI frontend, web client, or mobile app
- Replay parsing, engine reducer rewrites, or dataset schema changes
- Progressive widening or RAVE in MCTS
- Transposition tables
- Promo card events (Lone Gunman #109, Colonial Rear Guards #110, Panama Canal Returned #111)
- Particle filtering or learned belief models for hidden information

### Key constraint
All changes must run on RTX 3050 4GB VRAM, 16GB system RAM, WSL2.
ISMCTS determinization count must be tunable; default N=8 to fit in memory.

---

## 1. Dirichlet Noise at MCTS Root

### Goal
Add Dirichlet noise to the prior probabilities at the MCTS root node before
the first selection. This encourages exploration of under-visited branches
during self-play collection, producing more diverse training data.

### File: `cpp/tscore/mcts.hpp` (modify existing)

Add two fields to `MctsConfig`:

```cpp
// Dirichlet noise at root (Month 3)
float dir_alpha = 0.3f;     // Dirichlet concentration parameter
float dir_epsilon = 0.0f;   // noise weight: 0.0 = no noise (default for benchmark)
                             // 0.25 = recommended for self-play collection
```

### File: `cpp/tscore/mcts.cpp` (modify existing)

After expanding the root node and before the first simulation loop iteration,
apply noise to root edge priors:

```cpp
if (config.dir_epsilon > 0.0f && !root_node->edges.empty()) {
    std::gamma_distribution<float> gamma_dist(config.dir_alpha, 1.0f);
    std::vector<float> noise(root_node->edges.size());
    float noise_sum = 0.0f;
    for (size_t i = 0; i < noise.size(); ++i) {
        noise[i] = gamma_dist(rng);
        noise_sum += noise[i];
    }
    if (noise_sum > 0.0f) {
        for (size_t i = 0; i < noise.size(); ++i) {
            noise[i] /= noise_sum;
        }
    }
    const float eps = config.dir_epsilon;
    for (size_t i = 0; i < root_node->edges.size(); ++i) {
        root_node->edges[i].prior =
            (1.0f - eps) * root_node->edges[i].prior + eps * noise[i];
    }
}
```

### Notes
- Alpha=0.3 is appropriate for TS's medium branching factor (~15-40 legal actions).
- dir_epsilon=0.0 by default means benchmarks and teacher search are unaffected.
- Deterministic given the same RNG seed.

### Sentinel check
```bash
grep -q "dir_alpha" cpp/tscore/mcts.hpp
```

---

## 2. Temperature-Based Action Sampling in Self-Play Collection

### Goal
During self-play data collection, sample actions proportional to MCTS visit
counts raised to 1/temperature. Late-game moves use greedy selection.

### File: `cpp/tools/collect_selfplay_rows_jsonl.cpp` (modify existing)

Add CLI flags:
```
--temperature <float>      Temperature for action sampling (default: 1.0)
--temp-threshold <int>     Move number after which temp drops to 0 (default: 30)
```

### File: `cpp/tscore/mcts.hpp` (modify existing)

Add helper function:
```cpp
ActionEncoding select_action_with_temperature(
    const SearchResult& result,
    float temperature,
    Pcg64Rng& rng
);
```

### Implementation
- temp=0: always pick most-visited (greedy)
- temp=1: sample proportional to visit counts
- temp>1: more uniform sampling
- Compute visit_count^(1/temp) for each edge, normalize, sample

### Sentinel check
```bash
grep -q "temperature" cpp/tools/collect_selfplay_rows_jsonl.cpp
```

---

## 3. Epsilon-Greedy Exploration in Policy Rollouts

### Goal
During self-play collection with the learned policy (non-MCTS path), inject
epsilon-greedy noise: with probability epsilon, pick a uniformly random legal
action instead of the policy's top choice.

### File: `cpp/tscore/learned_policy.hpp` (modify existing)

Add exploration_rate parameter to TorchScriptPolicy:
```cpp
float exploration_rate_ = 0.0f;
void set_exploration_rate(float eps) { exploration_rate_ = eps; }
```

### File: `cpp/tools/collect_selfplay_rows_jsonl.cpp` (modify existing)

Add CLI flag:
```
--exploration-rate <float>   Epsilon for epsilon-greedy (default: 0.0)
```

Default 0.05 during collection, 0.0 during benchmark.

### Sentinel check
```bash
grep -q "exploration_rate" cpp/tscore/learned_policy.hpp
```

---

## 4. BayesElo Rating System

### Goal
Compute BayesElo ratings from benchmark results. Replaces raw win% as primary
evaluation metric with stable cross-generation comparisons.

### File: `scripts/compute_elo.py` (NEW)

```
uv run python scripts/compute_elo.py \
    --benchmark-history results/benchmark_history.json \
    --out results/elo_ratings.json \
    --anchor-rating 1500
```

### Implementation
- Read benchmark_history.json, convert win% to W/L counts (200-game benchmarks)
- Iterative maximum-likelihood BayesElo fitting (MM algorithm)
- Anchor heuristic at 1500
- Output ratings with 95% confidence intervals
- No external dependencies beyond Python stdlib

### Sentinel check
```bash
test -f scripts/compute_elo.py
```

---

## 5. Multi-Agent Evaluation Ladder

### Goal
Play round-robin between last N checkpoints + heuristic. Feed results into Elo.

### File: `scripts/run_ladder.py` (NEW)

```
uv run python scripts/run_ladder.py \
    --checkpoints ckpt1.pt ckpt2.pt ... \
    --games-per-pair 50 \
    --out results/ladder.json
```

### Implementation
- For each pair (A, B): play N games with A as USSR, N games with B as USSR
- Use C++ collector for speed
- Output match results as JSON consumable by compute_elo.py

### Sentinel check
```bash
test -f scripts/run_ladder.py
```

---

## 6. Information-Set MCTS via Determinization

### Goal
ISMCTS for online play where opponent's hand is hidden. Sample N
determinizations, run regular MCTS on each, aggregate visit counts.

### File: `cpp/tscore/ismcts.hpp` (NEW)

```cpp
struct IsmctsConfig {
    int n_determinizations = 8;
    MctsConfig mcts_config;
};

struct IsmctsResult {
    ActionEncoding best_action;
    std::vector<MctsEdge> aggregated_edges;
    double mean_root_value = 0.0;
    int total_determinizations = 0;
};

GameState sample_determinization(
    const GameState& gs, Side acting_side,
    int opp_hand_size, Pcg64Rng& rng);

IsmctsResult ismcts_search(
    const GameState& partial_state, Side acting_side,
    int opp_hand_size, torch::jit::script::Module& model,
    const IsmctsConfig& config, Pcg64Rng& rng);
```

### File: `cpp/tscore/ismcts.cpp` (NEW)

- sample_determinization: collect unknown cards, shuffle, deal to opponent
- ismcts_search: for each determinization, run mcts_search, aggregate edges by action key
- Add to CMakeLists.txt

### Sentinel check
```bash
test -f cpp/tscore/ismcts.hpp
```

---

## 7. Architecture Experiment: Attention Model

### Goal
Benchmark TSCountryAttnModel vs TSBaselineModel. Add --model-type flag to
train_baseline.py if not already present.

### File: `scripts/train_baseline.py` (modify existing)

Add `--model-type` flag with choices=['mlp', 'attn'], default='mlp'.
When 'attn', instantiate TSCountryAttnModel.

### Sentinel check
```bash
grep -q "model.type\|model_type.*attn" scripts/train_baseline.py
```

---

## 8. Online Play Server

### Goal
Minimal HTTP server that accepts game state JSON, runs ISMCTS, returns action.

### File: `scripts/play_server.py` (NEW)

- POST /action: accepts game state, returns action via ISMCTS
- GET /health: returns {"status": "ok"}
- Uses Python stdlib http.server (no external framework needed)
- Add ismcts_search_from_state binding to tscore_bindings.cpp

### Sentinel check
```bash
test -f scripts/play_server.py
```

---

## 9. Implementation Order

1. **Dirichlet noise** (sec 1) — P0, no dependencies
2. **Epsilon-greedy** (sec 3) — P0, parallel with sec 1
3. **Temperature sampling** (sec 2) — P0, after sec 1
4. **BayesElo** (sec 4) — P1, pure Python, parallel
5. **Evaluation ladder** (sec 5) — P1, after sec 4
6. **ISMCTS** (sec 6) — P0, after secs 1-3 stable
7. **Architecture experiment** (sec 7) — P2, independent
8. **Online play server** (sec 8) — P2, after sec 6
