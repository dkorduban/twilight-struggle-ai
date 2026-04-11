# Spec: Cross-Checkpoint Elo System

## Goal

Build infrastructure to measure relative strength between model checkpoints using
actual head-to-head games, enabling an Elo rating leaderboard that grows as PPO
generates new checkpoints.

Primary use: after each PPO benchmark (every 20 iters), run the new checkpoint
against the previous best and update Elo. Track monotonic improvement, detect
regressions, replace heuristic WR as the primary strength signal.

---

## New C++ function: `benchmark_model_vs_model_batched`

### Signature (add to `cpp/tscore/mcts_batched.hpp`)

```cpp
/// Run head-to-head games between two models, alternating sides.
/// First n_games/2: model_a plays USSR, model_b plays US.
/// Second n_games/2: model_a plays US, model_b plays USSR.
/// Returns one GameResult per game (ordered: USSR-as-a games first, then US-as-a games).
std::vector<GameResult> benchmark_model_vs_model_batched(
    int n_games,
    torch::jit::script::Module& model_a,
    torch::jit::script::Module& model_b,
    int pool_size,
    uint32_t base_seed,
    float temperature = 0.0f,   // 0 = greedy (argmax), else softmax
    bool nash_temperatures = false
);
```

### Implementation in `cpp/tscore/mcts_batched.cpp`

Copy `benchmark_games_batched` as the starting point. Key differences:

1. **Two models**: Accept `model_a` and `model_b` separately.
2. **Side assignment per game**: 
   - Games 0..n_games/2-1: model_a = USSR side, model_b = US side
   - Games n_games/2..n_games-1: model_a = US side, model_b = USSR side
   - Store `game_a_side[game_idx]` = Side::USSR or Side::US

3. **Two-batch eval per step**: When a game needs an action:
   - Split pending states into two groups: states where model_a acts vs model_b acts
   - Eval group_a_states with model_a, group_b_states with model_b
   - Merge results and continue

   Specifically, in the eval loop:
   ```
   for each game needing action:
       side_acting = pub.phasing  // which side needs to move
       if game_a_side[game] == side_acting:
           push to model_a_queue
       else:
           push to model_b_queue
   
   // Two separate batch evals
   batch_eval(model_a_queue, model_a)  -> outputs_a
   batch_eval(model_b_queue, model_b)  -> outputs_b
   
   // Merge and apply actions
   ```

4. **Greedy action selection** (benchmark, not rollout): use argmax like `benchmark_games_batched`, not multinomial.

5. **No step recording** — this is a benchmark function, only care about game outcomes.

### Python binding in `bindings/tscore_bindings.cpp`

Add after the existing `benchmark_batched` binding:

```python
tscore.benchmark_model_vs_model_batched(
    model_a_path: str,
    model_b_path: str,
    n_games: int = 100,
    pool_size: int = 64,
    seed: int = 0,
    temperature: float = 0.0,
    nash_temperatures: bool = False,
) -> list[GameResult]
```

Implementation (in tscore_bindings.cpp):
```cpp
m.def("benchmark_model_vs_model_batched",
    [](const std::string& path_a, const std::string& path_b, int n_games, int pool_size,
       py::object seed_obj, float temperature, bool nash_temperatures) {
        auto device = torch::kCPU;
        auto model_a = torch::jit::load(path_a, device); model_a.eval();
        auto model_b = torch::jit::load(path_b, device); model_b.eval();
        std::optional<uint32_t> seed;
        if (!seed_obj.is_none()) seed = seed_obj.cast<uint32_t>();
        auto results = ts::benchmark_model_vs_model_batched(
            n_games, model_a, model_b, pool_size,
            seed.value_or(0), temperature, nash_temperatures
        );
        // Return as Python list
        py::list out;
        for (auto& r : results) out.append(r);
        return out;
    },
    py::arg("model_a_path"), py::arg("model_b_path"),
    py::arg("n_games") = 100, py::arg("pool_size") = 64,
    py::arg("seed") = py::none(), py::arg("temperature") = 0.0f,
    py::arg("nash_temperatures") = false
);
```

---

## Python: Elo tracker script

### New file: `scripts/elo_tracker.py`

```python
#!/usr/bin/env python3
"""Elo rating tracker for model checkpoints.

Usage:
    # Run a new matchup and update ratings:
    uv run python scripts/elo_tracker.py matchup \
        --model-a data/checkpoints/ppo_v1_from_v106/ppo_best_scripted.pt \
        --model-b data/checkpoints/ppo_v2_selfplay/ppo_best_scripted.pt \
        --n-games 200 --seed 77000

    # Print current leaderboard:
    uv run python scripts/elo_tracker.py leaderboard

    # Show match history:
    uv run python scripts/elo_tracker.py history
"""
```

**Elo formula** (standard):
```python
def expected_score(rating_a: float, rating_b: float) -> float:
    return 1.0 / (1.0 + 10 ** ((rating_b - rating_a) / 400))

def update_elo(rating_a, rating_b, score_a, k=32):
    """score_a = actual score for model_a (0=loss, 0.5=draw, 1=win)"""
    expected = expected_score(rating_a, rating_b)
    new_a = rating_a + k * (score_a - expected)
    new_b = rating_b + k * ((1 - score_a) - (1 - expected))
    return new_a, new_b
```

**Storage format** (`results/elo_ratings.json`):
```json
{
  "ratings": {
    "data/checkpoints/ppo_v1_from_v106/ppo_best_scripted.pt": 1500.0,
    "data/checkpoints/ppo_v2_selfplay/ppo_best_scripted.pt": 1523.4
  },
  "history": [
    {
      "date": "2026-04-07T14:30:00",
      "model_a": "...", "model_b": "...",
      "n_games": 200, "model_a_wr": 0.58, "model_a_elo_before": 1500.0,
      "model_a_elo_after": 1523.4, "model_b_elo_before": 1500.0,
      "model_b_elo_after": 1476.6
    }
  ]
}
```

**Matchup flow** (in `matchup` subcommand):
1. Export model_a and model_b to scripted .pt if not already (check for `_scripted.pt` suffix)
2. Call `tscore.benchmark_model_vs_model_batched(model_a_path, model_b_path, n_games, ...)`
3. Compute model_a WR: count games where model_a won / total games
4. Load `results/elo_ratings.json` (create with {1500, 1500} if missing)
5. Apply Elo update (treat each game individually, not just aggregate WR)
6. Save updated JSON
7. Print summary

**Leaderboard subcommand**: print sorted by rating descending.

---

## Integration with train_ppo.py

After each benchmark call in `run_benchmark()`, optionally run a matchup against
the previous best checkpoint. Add a `--elo-matchup` flag:

```python
p.add_argument("--elo-baseline", type=str, default=None,
               help="Checkpoint path to use as Elo baseline for matchup benchmarks")
```

When `--elo-baseline` is set and a benchmark runs, call:
```bash
uv run python scripts/elo_tracker.py matchup \
    --model-a <previous_best_scripted.pt> \
    --model-b <current_scripted.pt> \
    --n-games 100 --seed <benchmark_seed + 99999>
```

Or just log the matchup result to W&B as `elo/model_a_wr`, `elo/model_a_elo`.

---

## Files to create/modify

| File | Change |
|------|--------|
| `cpp/tscore/mcts_batched.hpp` | Add `benchmark_model_vs_model_batched` declaration |
| `cpp/tscore/mcts_batched.cpp` | Implement the function |
| `bindings/tscore_bindings.cpp` | Add Python binding |
| `scripts/elo_tracker.py` | New: Elo tracking CLI |

---

## Acceptance Criteria

1. `cmake --build build-ninja -j` succeeds
2. `python -c "import tscore; print(hasattr(tscore, 'benchmark_model_vs_model_batched'))"` → True
3. Smoke test with same model vs itself → WR ≈ 50% (±5% at 100 games):
   ```python
   import tscore
   results = tscore.benchmark_model_vs_model_batched(
       "data/checkpoints/ppo_v1_from_v106/ppo_best_scripted.pt",
       "data/checkpoints/ppo_v1_from_v106/ppo_best_scripted.pt",
       n_games=100, pool_size=32, seed=0
   )
   assert 40 <= sum(1 for r in results[:50] if r.winner == tscore.Side.USSR) <= 60
   print("PASS: self-matchup WR ≈ 50%")
   ```
4. `uv run python scripts/elo_tracker.py --help` shows `matchup` and `leaderboard`
5. After a matchup run, `results/elo_ratings.json` is created and updated

---

## Notes

- Use greedy (temperature=0) for benchmark — deterministic, repeatable
- The n_games split should be even so each model gets equal turns as USSR
- K=32 is standard Elo step size. With 200 games, this gives meaningful but not volatile updates
- Initial Elo 1500 for all new models (relative scale)
- Do NOT require both models to use the same architecture — as long as both can be scripted
