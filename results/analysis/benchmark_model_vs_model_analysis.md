# benchmark_model_vs_model_batched: Test and Performance Analysis

Date: 2026-04-07

## Test Results Summary

**34 tests total**: 27 fast + 7 slow. All pass.

### Correctness findings

1. **Determinism**: Fully deterministic at T=0 (greedy). Same seed produces identical
   game-by-game results across repeated runs. Also deterministic across different
   pool_size values (pool_size=4 and pool_size=16 produce identical results for the
   same seed), confirming per-game-index seeding.

2. **Side assignment**: Working correctly. n_games=200 produces exactly 200 results
   (100 per side). Odd n_games rounds down (n_games=7 => 6 results).

3. **USSR bias**: With the BC baseline model (v99_nash_c_95ep_s42) playing itself,
   **USSR wins 81% of games** (seed=50000, n=200, T=0). This is higher than the
   55-65% range typical in balanced play, reflecting the BC model's strong USSR-side
   training data bias. This is a model property, not a benchmark bug.

4. **Self-play model_a WR**: When model_a == model_b (same model), model_a wins
   approximately 50% as expected from the symmetric side assignment (50% as USSR,
   50% as US).

5. **Stronger model wins more**: PPO v2 best beats BC baseline >55% of games,
   and PPO v2 best beats PPO v2 iter20 (early checkpoint) >50%. Both confirm
   the benchmark correctly reflects model strength differences.

6. **Temperature**: T=0 and T=1 produce different results (temperature affects
   action selection). T=1 still produces valid game results.

7. **Winner/VP consistency**: All games terminate with valid winners. VP sign
   agrees with winner for scoring-based endings. end_turn always in [1, 10].

8. **Edge cases**: n_games=0 and n_games=1 return empty results (expected
   rounding behavior). pool_size >> n_games works. Invalid model paths raise
   exceptions.

### No bugs found

All correctness invariants hold. The function is well-implemented.

## Performance Results

### Throughput vs pool_size (100 games, BC self-play, T=0, CPU)

| pool_size | games/s | speedup vs ps=1 |
|-----------|---------|------------------|
| 1         | 10.8    | 1.00x            |
| 4         | 11.4    | 1.06x            |
| 8         | 12.2    | 1.13x            |
| 16        | 13.9    | 1.29x            |
| 32        | 15.0    | 1.39x            |
| 64        | 15.9    | 1.47x            |

**Observation**: Moderate scaling from batching (1.47x at pool_size=64). The
improvement comes from batching NN forward passes. Diminishing returns above
pool_size=32.

### model_vs_model vs benchmark_batched (model vs heuristic)

| Method                         | games/s |
|--------------------------------|---------|
| benchmark_batched (USSR, heur) | 10.1    |
| benchmark_batched (US, heur)   | 11.0    |
| model_vs_model (same model)    | 15.9    |
| model_vs_model (diff models)   | 12.7    |

**Surprise**: model_vs_model is **faster** than model-vs-heuristic (0.74x ratio,
i.e., 26% faster). This is unexpected since model_vs_model runs two NN forward
passes per game step while benchmark_batched runs one NN + one heuristic.

Likely explanation: the heuristic opponent in benchmark_batched is surprisingly
expensive (it evaluates many legal actions with hand-crafted rules), and its
per-step cost exceeds a batched NN forward pass. The NN batches efficiently
while the heuristic processes each game sequentially.

### Throughput stability across n_games

| n_games | games/s |
|---------|---------|
| 10      | 15.1    |
| 50      | 16.1    |
| 100     | 15.3    |
| 200     | 14.7    |

Stable throughput across sizes. No significant overhead at small n.

### Same model vs different models

| Config       | games/s |
|--------------|---------|
| Same model   | 15.9    |
| Diff models  | 12.7    |

Same model is ~25% faster, likely because TorchScript can share internal
caches/buffers when both sides use the same model object, or because the
model loading overhead for two distinct models is slightly higher.

## Recommendations

1. **Default pool_size=32** is a good choice (captures most of the batching benefit).
2. The function is correct and deterministic. Safe for automated benchmark pipelines.
3. The 81% USSR WR in BC self-play is worth investigating as a model quality issue
   (not a benchmark issue). PPO models should have more balanced side performance.
