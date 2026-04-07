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

Current working target:

- original batched baseline on the boosted production-like config
  (`games=32`, `n_sim=400`, `pool=32`, `max_pending=64`, `torch_threads=4`):
  `8174.7 sims/s`
- current goal: `3x` that baseline = `24524.1 sims/s`

Current working optimization target:

- direct original-batched baseline on the boosted `games=32`, `n_sim=400`, `pool=32`,
  `max_pending=64`, `torch_threads=4` config: `8174.7 sims/s`
- current working goal: `3x` that baseline = `24524.1 sims/s`

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
- Latest exact-path work after the `02eadd6` checkpoint:
  - replaced the active exact expansion input with a compact exact legal-card
    representation instead of prebuilding per-country `ActionEncoding` drafts
  - preserved the exact card, mode, and country iteration order
  - reserved the exact node edge count up front to reduce expansion reallocations
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
- High-load directional smoke only, not validated:
  - config: `games=8`, `pool=8`, `n_sim=50`, `max_pending=64`, `torch_threads=4`,
    `warmup=0`
  - previous checkpoint `02eadd6`: `1934.5 sims/s` at `pre_load=1751.8%`,
    `expand=12.6s`, `nn=12.4s`, `commit=2.3s`
  - current exact compact-draft path: `6372.3 sims/s` at `pre_load=1143.4%`,
    `expand=3.5s`, `nn=3.3s`, `commit=1.5s`
  - host load moved a lot between runs, so this is only a directional sign that the
    compact exact draft path is worth re-validating once the machine is quiet

Latest exact verdict on the last optimization:

- The last exact optimization was the compact exact-draft rewrite:
  - replace prebuilt per-country `ActionEncoding` draft vectors with a compact
    per-card legality summary
  - preserve the exact card, mode, and country iteration order
  - reserve exact node edge counts up front
- Clean boosted `32/400`, `warmup=0`, `seed=12345` comparison:

| Variant | sims/s | vs original baseline |
|---|---:|---:|
| Original batched baseline | `8174.7` | `1.00x` |
| Pre-speedup fast checkpoint `02eadd6` | `11869.2` | `1.45x` |
| Current post-speedup build | `14740.4` | `1.80x` |

- Verdict: keep it. Against the pre-speedup fast checkpoint, the last optimization
  improved throughput by about `1.24x` (`14740.4 / 11869.2`).
- Current gap to target:
  - target = `24524.1 sims/s`
  - current = `14740.4 sims/s`
  - remaining gain needed = about `1.66x`

Next likely exact targets:

- `expand` remains the highest-value target. The next step is likely reducing node
  and action storage overhead further without changing the exact edge set.
- A local node/edge/action arena is a strong candidate:
  - pool `MctsNode`
  - pool `children` storage
  - reduce `std::vector` growth and allocator churn in expansion
- `commit` is still the second-largest bucket. The likely win is not cached-state
  copying, but splitting and optimizing the common post-action path:
  - action application
  - NORAD follow-up
  - stage advancement / cleanup
- `ActionEncoding` remains heavier than necessary on the hot path. A compact internal
  action representation for tree storage, materialized to full `ActionEncoding` only
  at apply-time, is still plausible if done without changing math or ordering.
- If expansion stays dominant after storage work, the next pass should instrument
  sub-phases inside `expand_from_raw_flat(...)` directly so the next change is driven
  by measured costs rather than guesses.

Latest findings after the compact internal tree rewrite:

- I converted the internal tree storage from `MctsNode`/`MctsEdge` plus
  `applied_actions` to a compact local representation:
  - `FastEdge` stores `{card_id, mode, country, target_offset, target_count, prior, visits, value}`
  - `FastNode` stores `edges`, `children`, and a flat `resolved_targets` array
- This removes persistent per-edge `ActionEncoding` storage and cuts hot-path
  vector churn in `expand` and `commit`.
- The first compact-tree attempt was not exact and later proved invalid:
  - the flat exact path was consuming cached military country lists directly
  - the old draft path filtered each military target with `has_country_spec(...)`
  - the flat path skipped that guard and could create an illegal `country=0` coup edge
- Fix:
  - sanitize accessible country caches locally in `AccessibleCache::build`
  - keep cheap compact-edge validity checks in materialization for safety
- I also added benchmark telemetry for:
  - `pre_load` / `post_load`
  - `pre_max_mhz` / `run_max_mhz` / `post_max_mhz`
  - in this WSL environment the observable `/proc/cpuinfo` max stayed at about
    `2995.1 MHz`, so the frequency signal is useful only as a local consistency
    check, not as a true host boost measurement

Current single-thread best validated production-like results, all `warmup=0`:

| Config | pre_load | run_max_mhz | sims/s | vs `8174.7` baseline |
|---|---:|---:|---:|---:|
| `games=32 n_sim=400 pool=32 max_pending=64 torch_threads=2` | `190.6%` | `2995.1` | `27120.7` | `3.32x` |
| `games=32 n_sim=400 pool=32 max_pending=96 torch_threads=2` | `239.7%` | `2995.1` | `27585.9` | `3.37x` |
| `games=32 n_sim=400 pool=32 max_pending=96 torch_threads=2` repeat | `201.1%` | `2995.1` | `24599.6` | `3.01x` |
| `games=32 n_sim=400 pool=32 max_pending=128 torch_threads=2` | `171.7%` | `2995.1` | `26729.2` | `3.27x` |

- Best measured throughput so far:
  - `27585.9 sims/s`
  - config: `games=32`, `n_sim=400`, `pool=32`, `max_pending=96`, `torch_threads=2`
  - speedup vs working baseline `8174.7 sims/s`: `3.37x`
- Repeated validation on the same best config stayed above the target:
  - `24599.6 sims/s`
  - `3.01x` vs baseline
- Best recent phase breakdown on the best-measured `32/400/96/2` run:
  - `advance=0.122s`
  - `select=11.474s`
  - `nn=23.731s`
  - `expand=26.703s`
  - `commit=1.431s`

Quick tuning notes after the compact-tree fix:

- `torch_threads=2` beats `3` and `4` on the current CPU-only setup.
- `forward_worker=1` did not help on the current host.
- Increasing `max_pending` from `64` to `96` helped.
- Increasing further to `128` regressed slightly from the `96` peak.

Clean zero-sharing parallel follow-up:

- The first in-process `mcts_workers=2` attempt was not viable:
  - shared Torch/Python runtime state caused initialization and runtime problems
  - even when forced past init, it was not the right zero-sharing design
- I replaced it with an exec-based multiworker launcher in `bench_fast_mcts.cpp`:
  - parent process handles load gating and telemetry
  - each worker is a separate child process launched via `exec`
  - each child loads its own model, owns its own trees/RNG/scratch, and writes a
    binary `BenchResult` back through a pipe
  - aggregate throughput is merged from child results without sharing the MCTS core

Parallel scaling results:

Best clean `1x/2x/3x/4x` scaling line so far, all `nice -n 0`, `warmup=0`,
`seed=12345`, `n_sim=400`, `torch_threads=1`, `torch_interop=1`,
`max_pending=64`, `pool_size=games`, and `games=32 * workers`:

| Workers | Config | pre_load | run_max_mhz | sims/s | Scaling vs 1x |
|---|---|---:|---:|---:|---:|
| `1x` | `games=32 pool=32 max_pending=64 mcts_workers=1` | `218.3%` | `2995.1` | `22830.9` | `1.00x` |
| `2x` | `games=64 pool=64 max_pending=64 mcts_workers=2` | `157.2%` | `2995.1` | `41657.6` | `1.82x` |
| `3x` | `games=96 pool=96 max_pending=64 mcts_workers=3` | `7.0%` | `2995.1` | `60256.4` | `2.64x` |
| `4x` | `games=128 pool=128 max_pending=64 mcts_workers=4` | `8.0%` | `2995.1` | `74438.4` | `3.26x` |

- This is the best current zero-sharing scaling shape:
  - one process per worker
  - one Torch intra-op thread per worker
  - no shared MCTS state
  - each worker owns its own model, trees, RNG, and scratch buffers
- `max_pending=64` scaled better than the nearby alternatives I tried:
  - `max_pending=96` was worse at high worker counts
  - `max_pending=48` was also worse at `4x`
- I also tried hard CPU pinning with `sched_setaffinity` in the local bench harness:
  - example `4x` pinned result: `69433.0 sims/s`
  - best `4x` unpinned result on the same shape: `74438.4 sims/s`
  - verdict: keep pinning support as an option in the harness, but leave the default
    path unpinned
- The earlier small sanity case showed the same trend:
  - single worker `games=16 n_sim=100 pool=16 max_pending=32 torch_threads=1`:
    `21623.3 sims/s`
  - two workers `games=16 n_sim=100 pool=16 max_pending=32 mcts_workers=2 torch_threads=1`:
    `36865.1 sims/s`
  - scaling: about `1.70x`
- So the current clean parallel path is not perfectly linear, but it is materially
  closer to linear than the earlier in-process thread attempt and stays faithful to
  the zero-sharing design goal.

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

K-sample exact fast-path work:

- Goal: make the production-like exact `K=4` influence-sampling path as close as
  possible to the current `K=1` fast path, without changing the math.
- Benchmark shape for all numbers below:
  - `games=32`
  - `n_sim=400`
  - `pool=32`
  - `max_pending=64` unless noted
  - `torch_threads=2`
  - `torch_interop=1`
  - `warmup=0`
  - `seed=12345`
  - `nice -n 0`
  - checkpoint/model: `data/checkpoints/v99_cf_1x95_s7/baseline_best_scripted.pt`

What was optimized in the exact `K=4` path:

- Added exact K-sample knobs to the standalone bench runner:
  - `--influence-samples`
  - `--influence-t-strategy`
  - `--influence-t-country`
  - `--influence-proportional-first`
- Ported the exact K-sample influence expansion math from `cpp/tscore/mcts_batched.cpp`
  into the local compact fast path.
- Added per-node reusable deterministic prefix caching by `ops`:
  - cache the exact proportional allocations once
  - reuse their blob refs, hashes, and densities across cards with the same `ops`
- Removed repeated deterministic work in the generic remainder path:
  - use precomputed strategy softmax for the `T_s=0, T_c=0` remainder sampler
  - special-case `temperature=1.0` multinomial sampling to skip redundant scaling
  - precompute log-prob tables for density evaluation
- Moved K-sample allocations and density-cache entries to compact fixed-size
  influence blobs instead of tiny `std::vector` objects.

Fresh clean results from the current code:

| Variant | pre_load | post_load | run_max_mhz | elapsed | sims | sims/s |
|---|---:|---:|---:|---:|---:|---:|
| `K=1` | `154.8%` | `151.8%` | `2995.1` | `62.6s` | `1,903,600` | `30403.8` |
| `K=4` | `171.6%` | `165.0%` | `2995.1` | `117.9s` | `1,878,000` | `15923.6` |

Current `K=4 / K=1` ratio:

- `15923.6 / 30403.8 = 0.524`
- Current exact `K=4` reaches about `52.4%` of the current exact `K=1` fast path.
- This is still below the target of `>= 90%`.

Progress within this K-work alone:

| K=4 exact path stage | pre_load | run_max_mhz | sims/s | expand time |
|---|---:|---:|---:|---:|
| Initial clean exact port | `704.3%` | `2995.1` | `8943.7` | `140.359s` |
| After deterministic prefix cache | `178.6%` | `2995.1` | `13381.5` | `93.207s` |
| After hot-math shortcuts + compact blobs | `171.6%` | `2995.1` | `15923.6` | `74.722s` |

Current exact phase breakdown:

- `K=1`
  - `advance=0.002s`
  - `select=11.811s`
  - `nn=23.322s`
  - `expand=26.031s`
  - `commit=1.401s`
- `K=4`
  - `advance=0.002s`
  - `select=13.814s`
  - `nn=26.909s`
  - `expand=74.722s`
  - `commit=2.410s`

Current verdict:

- The exact `K=4` fast path is materially faster than where it started.
- The dominant remaining gap is still `expand`.
- The main residual cost is not “there are too many extra edges”; it is that the
  exact `K=4` influence branch still has to do substantially more exact allocation
  generation and density work than `K=1`.
- `max_pending=96` did not beat `64` on the exact `K=4` production-like run:
  - `max_pending=96` -> `15719.0 sims/s`
  - `max_pending=64` -> `15923.6 sims/s`
