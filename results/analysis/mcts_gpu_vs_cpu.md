# GPU vs CPU MCTS Inference Benchmarks

**Date**: 2026-04-05 15:32:01
**Model**: /home/dkord/code/twilight-struggle-ai/data/checkpoints/v106_cf_gnn_s42/baseline_best_scripted.pt
**Setup**: RTX 3050 4GB, training running (~88% util), 32 games, 200 sims/game

## Results Table

| Device | Intra Threads | Pool Size | MCTS Threads | Wall Time (s) | Sims/sec | Status | Note |
|--------|---------------|-----------|--------------|---------------|----------|--------|------|
| cpu | 2 | 32 | 4 | N/A | N/A | ERROR | benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1 |
| cpu | 4 | 32 | 4 | N/A | N/A | ERROR | benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1 |
| cuda | 1 | 32 | 4 | N/A | N/A | ERROR | benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1 |
| cuda | 2 | 32 | 4 | N/A | N/A | ERROR | benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1 |
| cpu | 4 | 64 | 4 | N/A | N/A | ERROR | benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1 |
| cuda | 1 | 64 | 4 | N/A | N/A | ERROR | benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1 |

## Analysis

No successful runs to analyze.

## Detailed Results

### CPU (intra=2, pool=32)
- Status: ERROR
- Error: benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1

### CPU (intra=4, pool=32)
- Status: ERROR
- Error: benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1

### CUDA (intra=1, pool=32)
- Status: ERROR
- Error: benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1

### CUDA (intra=2, pool=32)
- Status: ERROR
- Error: benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1

### CPU (intra=4, pool=64)
- Status: ERROR
- Error: benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1

### CUDA (intra=1, pool=64)
- Status: ERROR
- Error: benchmark_mcts(): incompatible function arguments. The following argument types are supported:
    1

