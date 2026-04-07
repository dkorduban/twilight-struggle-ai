# Plan: MCTS Performance Deep-Dive (Barrier vs Fast)

## Goal
Understand why barrier-based MCTS threading provides zero speedup, with instrumentation
to pinpoint the bottleneck.

## Comparison matrix (sequential, nice 0, 4 torch threads)

| Run | Label | MCTS threads | Barriers | Torch threads |
|-----|-------|-------------|----------|---------------|
| A | `barrier-1t` | 1 | Yes (4 barriers/iter) | 4 |
| B | `fast-1t` | 1 | No (single-threaded loop) | 4 |

Both: 100 games, 100 sims, pool_size=32, seed=50000, learned_side=USSR, nice 0.

## Instrumentation

Add `BatchedMctsStats` struct to `mcts_batched.cpp`:

1. **NN batch sizes**: record every batch size → min/p10/p50/p90/max/mean
2. **NN wall time**: total time inside `model.forward()`
3. **Select wall time**: total time in tree selection phase
4. **Expand wall time**: total time in backpropagation/expansion phase
5. **Lifecycle wall time**: time in game emit/start/advance logic
6. **Barrier wait time** (barrier path only): time at each of 4 barriers
7. **Total NN calls**: count of forward passes
8. **Total sims completed**: sum across all games
9. **Iterations**: number of outer-loop iterations

Print summary to stderr at end of `collect_games_batched` and `benchmark_games_batched`.

## What this tells us

- If NN time dominates both equally → barriers irrelevant, NN is bottleneck
- If barrier wait is large at 1 thread → barriers cost real time even single-threaded
- If batch sizes differ → two paths compose batches differently
- If select/expand times differ → tree traversal overhead differs

## Implementation

- Modify `cpp/tscore/mcts_batched.cpp` only (stats struct + timing)
- No header changes (stats are internal)
- Always-on (cheap chrono calls)
- Print to stderr

## Files to modify

| File | Change |
|------|--------|
| `cpp/tscore/mcts_batched.cpp` | Add `BatchedMctsStats`, timing around each phase, summary print |
