# Fast Batched MCTS Replica

This directory is an isolated optimization track for the full-information wavefront
batched search in [`cpp/tscore/mcts_batched.cpp`](/home/dkord/code/twilight-struggle-ai/cpp/tscore/mcts_batched.cpp).

Goals:

- keep all edits inside `cpp/mcts_batched_fast/`
- replicate the current batched MCTS logic closely enough to benchmark it
- force the MCTS scheduler to a single thread
- keep NN inference on CPU and allow LibTorch to use multiple threads
- prefer improvements to the non-NN path; NN throughput should stay roughly flat
- reach 10x higher sims/s than the initial single-thread baseline

Baseline source of truth:

- experiment log: `docs/experiment_log_phase1.md`
- checkpoint: `data/checkpoints/v99_cf_1x95_s7/baseline_best_scripted.pt`
- logged collection setup: 50 sims, `pool_size=32`, Dirichlet noise `(alpha=0.3, eps=0.25)`,
  temperature `1.0`

What is in this directory:

- `CMakeLists.txt`: standalone build that links against the already-built `libtscore.a`
- `fast_mcts_batched.hpp/.cpp`: isolated benchmark-oriented replica of the batched MCTS loop
- `bench_fast_mcts.cpp`: CLI benchmark tool with CPU-load gating and sims/s reporting

Working plan:

1. Build a runnable single-thread replica and measure sims/s with the `v99_cf_1x95_s7` checkpoint.
2. Keep the logic intact, but remove benchmark-only overhead from the non-NN path.
3. Tune LibTorch intra-op / inter-op threading for a single MCTS scheduler thread.
4. Add targeted hot-path improvements only inside this replica.
5. Re-benchmark until the sims/s target is met or a clear local blocker remains.

Benchmark rules:

- before each measured run, sample total CPU load across all 20 vCPUs
- if total CPU load is above `1000%`, wait and re-sample
- print the sampled load so each benchmark result includes the machine state

Latest findings:

- Experiment-log baseline reference: `2553.6 sims/s` equivalent for `v99_cf_1x95_s7`
  at the teacher-collection setup (`2.8s/game`, about `143` decisions/game, `50 sims`,
  `pool_size=32`).
- Strict `<1000%` load-gated matrix, all with `games=32`, `pool=32`, `max_pending=8`,
  `torch_threads=1`, `torch_interop=1`, and one ignored warmup run:

| n_sim | current sims/s | speedup vs baseline | avg_batch | pre_load |
|------|----------------|---------------------|-----------|----------|
| 50 | `8308.8` | `3.25x` | `191.3` | `682.0%` |
| 100 | `8004.5` | `3.13x` | `192.9` | `684.8%` |
| 200 | `8484.4` | `3.32x` | `217.6` | `776.9%` |
| 400 | `7818.8` | `3.06x` | `209.2` | `790.4%` |

- Current best measured point is `n_sim=200` at `8484.4 sims/s`, which is `3.32x`
  over the experiment-log baseline.
- The hot path remains mostly non-NN even at the best point. On the counted
  `n_sim=200` run the phase times were: `select=28.9s`, `expand=35.0s`, `nn=30.0s`,
  `commit=15.5s`.
- Higher `n_sim` helps batch amortization up to `200`, but `400` starts losing
  throughput again because tree work grows faster than the extra batching helps.

Tuning after the fixed-pool matrix:

- `max_pending` matters a lot once batching is the goal.
  - `n_sim=200`, `pool=32`, `max_pending=16`, `torch_threads=1` reached
    `8523.8 sims/s` (`3.34x` baseline), with `avg_batch=391.0`.
  - `n_sim=200`, `pool=32`, `max_pending=64`, `torch_threads=1` reached
    `12678.1 sims/s` (`4.96x` baseline), with `avg_batch=1193.3`.
- Larger NN batches finally make CPU LibTorch threading worthwhile.
  - At `n_sim=200`, `pool=32`, `max_pending=32`, `torch_threads=4` reached
    `12452.8 sims/s` (`4.88x` baseline).
  - At the same setting, `torch_threads=8` was slightly worse on the counted run
    (`12312.7 sims/s`), so `4` is the current sweet spot.
- Larger pool size still helps when the host is quiet.
  - `n_sim=200`, `games=64`, `pool=64`, `max_pending=64`, `torch_threads=4`
    reached `12896.2 sims/s` (`5.05x` baseline), with `avg_batch=2364.8`.
- More production-like tuned point:
  - `n_sim=400`, `games=32`, `pool=32`, `max_pending=32`, `torch_threads=4`
    reached `11061.0 sims/s` (`4.33x` baseline), with `avg_batch=801.0`.
- A follow-up attempt to shortcut commit by reusing cached child states did not help
  in practice and was reverted.

Latest validated gains:

- Replacing the hot select-edge call with a local inline implementation and using the
  compact legal-card scan in `expand_without_model` moved the bottleneck materially.
  On the previously best `games=64`, `pool=64`, `n_sim=200`, `max_pending=64`,
  `torch_threads=4` setup:
  - before that select-side cleanup: `12896.2 sims/s` (`5.05x` baseline),
    `select=41.8s`, `expand=59.2s`, `nn=19.7s`, `commit=24.9s`
  - after that select-side cleanup: `16292.0 sims/s` (`6.38x` baseline),
    `select=11.5s`, `expand=58.7s`, `nn=20.2s`, `commit=24.8s`
- Best cleanly validated overall throughput so far:
  - `games=64`, `pool=64`, `n_sim=200`, `max_pending=64`, `torch_threads=4`
  - `current sims/s = 16292.0`
  - `speedup vs baseline = 6.38x`
  - `avg_batch = 2364.8`
- Best cleanly validated production-like point so far:
  - `games=32`, `pool=32`, `n_sim=400`, `max_pending=64`, `torch_threads=4`
  - `current sims/s = 16271.4`
  - `speedup vs baseline = 6.37x`
  - `avg_batch = 1492.2`

Exactness correction:

- The earlier highest-throughput path used a compact expansion shortcut that was later
  reported to be non-equivalent in strength testing. The active benchmark path has
  been switched back to exact baseline-style expansion semantics.
- After restoring the exact path, raw throughput initially dropped sharply:
  - `games=32`, `pool=32`, `n_sim=400`, `max_pending=64`, `torch_threads=4`
  - `current sims/s = 6796.4`
  - `speedup vs baseline = 2.66x`
  - `select=105.8s`, `expand=107.5s`, `nn=26.3s`, `commit=29.2s`
- Re-optimization of the exact path:
  - kept the local inline `select_edge_fast`
  - restored a fast exact expansion path driven by `collect_card_drafts_cached`
    rather than the compact shortcut
  - replaced the expensive exact no-model leaf check with a zero-allocation exact
    cached predicate
- Best cleanly validated exact production-like point so far:
  - `games=32`, `pool=32`, `n_sim=400`, `max_pending=64`, `torch_threads=4`
  - `current sims/s = 13133.4`
  - `speedup vs baseline = 5.14x`
  - `avg_batch = 1415.5`
  - `select=12.5s`, `expand=84.5s`, `nn=17.7s`, `commit=24.3s`
- Best cleanly validated exact wider-wavefront point so far:
  - `games=64`, `pool=64`, `n_sim=200`, `max_pending=64`, `torch_threads=4`
  - `current sims/s = 10811.3`
  - `speedup vs baseline = 4.23x`
  - `avg_batch = 2364.6`

Build:

```bash
cmake -S cpp/mcts_batched_fast -B cpp/mcts_batched_fast/build
cmake --build cpp/mcts_batched_fast/build -j
```

Example benchmark:

```bash
cpp/mcts_batched_fast/build/ts_fast_mcts_bench \
  --model data/checkpoints/v99_cf_1x95_s7/baseline_best_scripted.pt \
  --games 32 \
  --n-sim 50 \
  --pool-size 32 \
  --temperature 1.0 \
  --torch-threads 8 \
  --torch-interop 1
```
