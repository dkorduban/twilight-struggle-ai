# MCTS Throughput Matrix Benchmark

**Timestamp**: /home/dkord/code/twilight-struggle-ai
**Model**: v106_cf_gnn_s42/baseline_best_scripted.pt
**Fixed params**: --games 32, --n-sim 200, --seed 77700, --temperature 1.0, --dir-alpha 0.3, --dir-epsilon 0.25

## Results (sorted by sims/s)

| MCTS Threads | Intra Threads | Interop Threads | Pool Size | Max Pending | Sims/s | Total Time (s) | Avg Batch | Select (s) | NN (s) | Expand (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 4 | 1 | 32 | 64 | 12706.6 | 68.578 | 1161.90 | 10.963 | 35.551 | 21.702 |
| 4 | 4 | 1 | 32 | 32 | 12077.4 | 69.460 | 735.90 | 13.882 | 34.044 | 21.162 |
| 4 | 4 | 1 | 32 | 32 | 12059.9 | 69.561 | 735.90 | 13.772 | 34.183 | 21.213 |
| 4 | 2 | 1 | 32 | 32 | 12033.1 | 69.716 | 735.90 | 13.119 | 36.875 | 19.362 |
| 8 | 4 | 1 | 32 | 32 | 11974.5 | 70.057 | 735.90 | 11.665 | 41.731 | 16.197 |
| 2 | 4 | 1 | 32 | 32 | 11570.1 | 72.506 | 735.90 | 18.351 | 22.437 | 31.402 |
| 4 | 4 | 1 | 32 | 16 | 11254.5 | 68.168 | 390.80 | 16.548 | 30.641 | 20.598 |
| 2 | 2 | 1 | 32 | 32 | 10763.0 | 77.943 | 735.90 | 17.912 | 29.747 | 29.983 |
| 4 | 1 | 1 | 32 | 32 | 10558.2 | 79.455 | 735.90 | 12.431 | 48.790 | 17.908 |
| 4 | 4 | 1 | 32 | 8 | 10418.5 | 70.550 | 216.20 | 19.233 | 32.038 | 18.902 |
| 4 | 4 | 1 | 64 | 64 | 10228.4 | 85.193 | 1161.90 | 17.377 | 31.733 | 35.736 |
| 8 | 2 | 1 | 32 | 32 | 9632.8 | 87.088 | 735.90 | 12.200 | 57.569 | 16.833 |
| 4 | 4 | 1 | 64 | 32 | 9565.7 | 87.699 | 735.90 | 20.388 | 31.722 | 35.226 |
| 2 | 1 | 1 | 32 | 32 | 8875.7 | 94.516 | 735.90 | 17.552 | 47.800 | 28.850 |
| 1 | 4 | 1 | 32 | 32 | 8259.2 | 101.571 | 735.90 | 27.961 | 21.200 | 52.113 |
| 1 | 2 | 1 | 32 | 32 | 8163.7 | 102.760 | 735.90 | 26.166 | 27.990 | 48.328 |
| 1 | 1 | 1 | 32 | 32 | 7231.7 | 116.003 | 735.90 | 25.753 | 42.400 | 47.542 |

## Analysis

**Best Overall Config**: MCTS threads=4, Intra=4, Interop=1, Pool=32, Max-Pending=64
- **Throughput**: 12706.6 sims/s
- **Latency**: 68.578s for 871390 items
- **Avg Batch Size**: 1161.90

**Best Config (≤4 MCTS threads)**: MCTS threads=4, Intra=4, Interop=1
- **Throughput**: 12706.6 sims/s (0.0% vs best)

### Bottleneck Analysis

Breakdown of total time (from best overall config):

- **Select**: 10.963s (16.0%)
- **NN**: 35.551s (51.8%)
- **Expand**: 21.702s (31.6%)
- **Advance**: 0.362s (0.5%)

**Conclusion**: NN is the dominant bottleneck. Increase torch threads or batch size to hide latency.
