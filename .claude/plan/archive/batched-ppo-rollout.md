# Spec: Batched PPO Rollout via C++ Game Pool

## Goal

Replace the sequential Python-callback PPO rollout (200 games × 2.8s = 560s) with a
C++ batched game pool that runs all games concurrently with batched NN inference,
returning per-step rollout data (features, logits, masks, actions, log_probs, values)
to Python for the PPO update phase. Expected speedup: **20-25×** on rollout.

## Design

Add a new C++ function `rollout_games_batched()` modeled on the existing
`benchmark_games_batched()` (mcts_batched.cpp:3742). The key difference: instead of
just returning `GameResult`, it also returns per-step `RolloutStep` records containing
everything PPO needs.

The existing `benchmark_games_batched` already:
- Runs N games in a pool with batched NN inference
- Calls `greedy_action_from_outputs()` for action selection (with temperature sampling)
- Handles DEFCON safety, legal card/mode masking, country target allocation
- Commits actions and advances games

We modify this to **record** at each learned-side decision point, then return the
recorded data alongside game results.

## Files to create

- None — all changes go in existing files.

## Files to modify

- `cpp/tscore/mcts_batched.hpp` — add `RolloutStep` struct and `rollout_games_batched()` declaration
- `cpp/tscore/mcts_batched.cpp` — add `rollout_action_from_outputs()` (temperature-sampling
  version that also computes log_prob and masks) and `rollout_games_batched()`
- `bindings/tscore_bindings.cpp` — expose `rollout_games_batched` to Python
- `scripts/train_ppo.py` — replace `collect_rollout()` to call the new batched function

## Interfaces / signatures

### RolloutStep struct (mcts_batched.hpp)

```cpp
struct RolloutStep {
    // Features (CPU tensors, ready for Python)
    torch::Tensor influence;     // (172,) float32
    torch::Tensor cards;         // (448,) float32
    torch::Tensor scalars;       // (11,) float32

    // Masks (CPU tensors, bool)
    torch::Tensor card_mask;     // (111,) bool
    torch::Tensor mode_mask;     // (5,) bool
    torch::Tensor country_mask;  // (86,) bool — empty if mode is EVENT/SPACE

    // Sampled action
    int card_idx;                // 0-indexed (card_id - 1)
    int mode_idx;                // 0-4
    std::vector<int> country_targets;  // 0-indexed country IDs

    // Scalars
    float log_prob;              // log π(a|s) = log π_card + log π_mode + Σ log π_country
    float value;                 // V(s) from model

    int side_int;                // 0=USSR, 1=US
    int game_index;              // which game this step belongs to (0-based)
};
```

### rollout_games_batched() (mcts_batched.hpp)

```cpp
struct RolloutResult {
    std::vector<GameResult> results;     // one per game
    std::vector<RolloutStep> steps;      // all steps across all games, flat
    std::vector<int> game_boundaries;    // steps[game_boundaries[i]] is first step of game i
};

RolloutResult rollout_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int pool_size,
    uint32_t base_seed,
    torch::Device device = torch::kCPU,
    float temperature = 1.0f,             // >0 for stochastic sampling
    bool nash_temperatures = true
);
```

### rollout_action_from_outputs() (mcts_batched.cpp, new internal function)

Modeled on `greedy_action_from_outputs()` (line 3477) but:
1. Always uses temperature sampling (temperature > 0)
2. Records the masks (card_mask, mode_mask, country_mask)
3. Computes log_prob from the masked distributions
4. Returns a `RolloutStep` instead of just an `ActionEncoding`

```cpp
// Returns (action, step) — action for game progression, step for PPO recording.
std::pair<ActionEncoding, RolloutStep> rollout_action_from_outputs(
    const GameState& state,
    const nn::BatchInputs& inputs,
    const nn::BatchOutputs& outputs,
    int64_t batch_index,
    Pcg64Rng& rng,
    float temperature,
    int game_index,
    torch::Device input_device
);
```

Implementation notes:

**Card selection**: Same as `greedy_action_from_outputs` but always sample (never argmax).
Build `card_mask` (111-bool) from `playable` cards with DEFCON filtering.
```cpp
auto card_probs = torch::softmax(masked_card / temperature, 0);
auto card_idx = torch::multinomial(card_probs, 1).item<int64_t>();
float log_prob_card = torch::log_softmax(masked_card / temperature, 0)
    .index({card_idx}).item<float>();
```

**Mode selection**: Same DEFCON safety guards. Build `mode_mask` (5-bool).
```cpp
auto mode_probs = torch::softmax(masked_mode / temperature, 0);
auto mode_idx_t = torch::multinomial(mode_probs, 1).item<int64_t>();
float log_prob_mode = torch::log_softmax(masked_mode / temperature, 0)
    .index({mode_idx_t}).item<float>();
```

**Country selection**: Use existing `build_action_from_country_logits` logic for
target selection, but also compute log_prob. Build `country_mask` (86-bool) from
`accessible_countries_filtered`. For COUP/REALIGN: single multinomial sample.
For INFLUENCE: proportional allocation (same as existing code). Log-prob for
country is sum of `log(masked_softmax[target_i])` for each target.

**Features**: Extract from `inputs` tensor at `batch_index` — already computed.
```cpp
step.influence = inputs.influence.index({batch_index}).cpu();
step.cards = inputs.cards.index({batch_index}).cpu();
step.scalars = inputs.scalars.index({batch_index}).cpu();
```

**Value**: From `outputs.value.index({batch_index, 0}).item<float>()`.

**log_prob**: `log_prob_card + log_prob_mode + log_prob_country`.

### rollout_games_batched() implementation

Copy `benchmark_games_batched()` (line 3742–3889), change:
1. Return type: `RolloutResult` instead of `vector<GameResult>`
2. In the learned-side branch, call `rollout_action_from_outputs()` instead of
   `greedy_action_from_outputs()`, storing the `RolloutStep` into `result.steps`
3. After all games complete, assign `game_index` to each step based on order

### Python binding (bindings/tscore_bindings.cpp)

```python
# Returns (results: list[GameResult], steps: list[dict], game_boundaries: list[int])
tscore.rollout_games_batched(
    model_path: str,      # TorchScript model path
    learned_side: Side,
    n_games: int,
    pool_size: int = 32,
    seed: int = None,
    device: str = "cpu",
    temperature: float = 1.0,
    nash_temperatures: bool = True,
) -> tuple[list[GameResult], list[dict], list[int]]
```

Each step dict:
```python
{
    "influence": np.ndarray,       # (172,) float32
    "cards": np.ndarray,           # (448,) float32
    "scalars": np.ndarray,         # (11,) float32
    "card_mask": np.ndarray,       # (111,) bool
    "mode_mask": np.ndarray,       # (5,) bool
    "country_mask": np.ndarray,    # (86,) bool
    "card_idx": int,
    "mode_idx": int,
    "country_targets": list[int],
    "log_prob": float,
    "value": float,
    "side_int": int,
    "game_index": int,
}
```

### train_ppo.py changes

Replace `collect_rollout()` with a new version that:
1. Exports current model to TorchScript (temp file)
2. Calls `tscore.rollout_games_batched()` for each side
3. Converts returned dicts to `Step` objects
4. Assigns rewards from `GameResult.winner`

```python
def collect_rollout_batched(
    model: nn.Module,
    n_games: int,
    learned_side: tscore.Side,
    base_seed: int,
    device: str,
    card_specs: dict,  # unused in batched mode (C++ handles DEFCON safety)
) -> list[Step]:
    # Export model to temp TorchScript file
    script_path = _export_temp_model(model)
    
    results, steps, boundaries = tscore.rollout_games_batched(
        model_path=script_path,
        learned_side=learned_side,
        n_games=n_games,
        pool_size=min(n_games, 64),
        seed=base_seed,
        device="cpu",  # C++ batched runs on CPU for now
        temperature=1.0,
        nash_temperatures=True,
    )
    
    # Convert to Step objects and assign rewards
    all_steps = []
    for s in steps:
        step = Step(
            influence=torch.from_numpy(s["influence"]).unsqueeze(0),
            cards=torch.from_numpy(s["cards"]).unsqueeze(0),
            scalars=torch.from_numpy(s["scalars"]).unsqueeze(0),
            card_mask=torch.from_numpy(s["card_mask"]),
            mode_mask=torch.from_numpy(s["mode_mask"]),
            country_mask=torch.from_numpy(s["country_mask"]) if s["country_mask"].any() else None,
            card_idx=s["card_idx"],
            mode_idx=s["mode_idx"],
            country_targets=s["country_targets"],
            old_log_prob=s["log_prob"],
            value=s["value"],
            side_int=s["side_int"],
        )
        all_steps.append(step)
    
    # Assign rewards: +1 win, -1 loss, on the last step of each game
    for i, result in enumerate(results):
        # Find last step for this game
        start = boundaries[i]
        end = boundaries[i + 1] if i + 1 < len(boundaries) else len(all_steps)
        if start < end:
            if learned_side == tscore.Side.USSR:
                reward = 1.0 if result.winner == tscore.Side.USSR else -1.0
            else:
                reward = 1.0 if result.winner == tscore.Side.US else -1.0
            all_steps[end - 1].reward = reward
            all_steps[end - 1].done = True
    
    return all_steps
```

The model export overhead (~100ms) is negligible compared to rollout time.
The PPO update still runs in Python using the original PyTorch model (with gradients).

## Test cases (required)

- **test_rollout_batched_returns_steps**: Run 4 games via `rollout_games_batched`.
  Assert len(results) == 4. Assert len(steps) > 0. Assert each step has all required
  fields. Assert step["influence"].shape == (172,). Assert step["value"] is finite.

- **test_rollout_batched_log_probs_finite**: Run 10 games. Assert all step log_probs
  are finite and negative (log of probability).

- **test_rollout_batched_game_boundaries**: Run 4 games. Assert len(game_boundaries)
  == 4. Assert game_boundaries[0] == 0. Assert all boundaries are monotonically
  increasing. Assert steps between boundaries all have the same game_index.

- **test_rollout_batched_rewards_assigned**: Use the Python wrapper
  `collect_rollout_batched()` with 4 games. Assert exactly 4 steps have `done=True`.
  Assert each done step has reward in {-1.0, +1.0}.

- **test_rollout_vs_sequential_equivalence**: Run 1 game batched (pool_size=1) and
  1 game sequential via `play_callback_matchup` with the same seed. Since pool_size=1
  means no reordering, RNG paths should be identical. Assert the same number of steps,
  same card_idx and mode_idx at each step, and same game outcome (winner, final_vp).
  This proves the batched path produces identical decisions to the sequential path.

- **test_rollout_vs_sequential_winrate**: Run 200 games batched (pool_size=32) and 200
  games sequential (same seed). Win rates should be within ~10pp (stochastic, same
  policy, but different RNG paths due to pooling order). Sanity check, not exact match.

- **test_rollout_batched_masks_valid**: Run 4 games. For each step with
  mode_idx in {0,1,2} (influence/coup/realign), assert country_mask has at least 1
  True entry. For mode_idx in {3,4} (space/event), assert country_targets is empty.

## Acceptance criteria

- [ ] All 6 test cases pass
- [ ] Build: `cmake --build build-ninja -j` succeeds
- [ ] C++ tests: `ctest --test-dir build-ninja --output-on-failure` passes
- [ ] Python tests: `uv run pytest tests/python/ -q -n 0` passes
- [ ] PPO training can run with `collect_rollout_batched()` replacing `collect_rollout()`
- [ ] Rollout time for 200 games drops from ~560s to <60s

## Constraints

- Do NOT modify `benchmark_games_batched()` — copy its structure for the new function
- Do NOT modify `greedy_action_from_outputs()` — create a new `rollout_action_from_outputs()`
- Country ID 64 has no spec — filter it from country_mask in C++ (use `has_country_spec()`)
- Temperature must be > 0 for PPO (stochastic policy)
- Features must be returned as CPU tensors (Python PPO update handles device placement)
- `game_boundaries` must be populated correctly even when games complete out of order
  in the pool (track via game_index on each step)
- The Python-side `collect_rollout()` should remain as a fallback (rename to
  `collect_rollout_sequential()`) in case the batched version has issues

## Implementation order

1. `cpp/tscore/mcts_batched.hpp` — add structs + declaration
2. `cpp/tscore/mcts_batched.cpp` — implement `rollout_action_from_outputs()` + `rollout_games_batched()`
3. Build + C++ test
4. `bindings/tscore_bindings.cpp` — expose to Python
5. Build + binding test
6. `scripts/train_ppo.py` — add `collect_rollout_batched()`, wire into main loop
7. End-to-end test with PPO
