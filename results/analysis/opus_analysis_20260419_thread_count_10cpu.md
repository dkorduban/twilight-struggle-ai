# Opus Analysis: 10-thread CPU coincidence in elo_tournament and train_ppo
Date: 2026-04-19T UTC
Question: Why do both elo_tournament and train_ppo show exactly 10 active threads in top?

## Executive Summary
Not a coincidence, and not a heuristic like "half the vCPUs". Both processes hit exactly the same PyTorch default: `torch.get_num_threads() == 10`. The host is an Intel i9-13900H with **10 physical cores × 2 SMT hyperthreads = 20 logical CPUs**. PyTorch's ATen parallel backend is OpenMP, and GNU OpenMP's `omp_get_max_threads()` defaults to the **physical core count** (10), not the logical count (20). Neither script sets `torch.set_num_threads()` nor any of `OMP_NUM_THREADS` / `MKL_NUM_THREADS`, and the C++ benchmark/rollout paths they exercise (`benchmark_games_batched`, `benchmark_model_vs_model_batched`, `rollout_games_batched`) do not call `at::set_num_threads` either. So both processes inherit the identical OpenMP default of 10 intra-op threads, and each torch forward pass fans out into exactly 10 OMP workers running near 100% CPU during inference, while the rest of the process's threads (Python helpers, tokio runtime, CUDA callback, jemalloc bg, pt_autograd, etc.) sit at 0% CPU.

## Findings

### elo_tournament parallelism
File: `scripts/run_elo_tournament.py`

- No `torch.set_num_threads` or `torch.set_num_interop_threads` calls.
- No env-var reads for `OMP_NUM_THREADS` / `MKL_NUM_THREADS`.
- No `multiprocessing.Pool`, `ProcessPoolExecutor`, or `ThreadPoolExecutor` in the tournament driver itself — matches run sequentially (one pair at a time) in the main thread (see the `round_robin` scheduler around lines 233-319).
- Per-match parallelism comes entirely from C++ via `pool_size` passed to `tscore.benchmark_batched` / `tscore.benchmark_model_vs_model_batched`:
  - `_run_heuristic_match`: `pool_size=min(32, half)` (line 242, 245) — note this is `pool_size`, i.e. number of *concurrent game slots batched for inference*, not threads.
  - `run_match` (model-vs-model): `pool_size=min(64, n_games)` (line 296).
- Critical: in `cpp/tscore/mcts_batched.cpp`, the `benchmark_games_batched` (line 3742) and `benchmark_model_vs_model_batched` (line 3899) code paths are **single-threaded driver loops** — they serialize pool-slot advancement, do one big NN forward per iteration, and do NOT spawn worker threads. The only function that calls `at::set_num_threads()` is the MCTS search in `run_mcts_batched` (`mcts_batched.cpp:2864-2878`), and the elo tournament runs with `n_simulations = 0`, so that function is never used.
- Consequence: the per-match inference is a sequence of `torch.jit` forward calls on CPU ("device=cpu" is forced at line 298), and each forward dispatches onto OpenMP with 10 workers — the PyTorch default.

### train_ppo parallelism
File: `scripts/train_ppo.py`

- No `torch.set_num_threads` or `torch.set_num_interop_threads` calls.
- No env-var reads for OMP/MKL.
- The script has a `--rollout-workers` flag (line 2995) defaulting to 1; current run uses it via `args.rollout_workers` (line 3360). It powers a `ThreadPoolExecutor` inside `collect_rollout_league_vs_K` (line 1425, 1567).
- Each worker calls a C++ rollout function (`rollout_games_batched` / `rollout_model_vs_model_batched`) that, like the benchmark functions, is a **single-threaded driver loop**. Those C++ functions do not call `at::set_num_threads`.
- `pool_size` is passed as `min(n_games, 64)` / `min(32, half)` in several collect helpers (lines 789, 868, 1299, 1350, 2390, 2697, 2707) — again, batched game slots, not threads.
- Consequence: when rollouts are happening, the main Python thread is running a `torch.jit` inference call on CPU (device="cuda" is configured, but the TorchScript path used for rollout opponents is CPU — the forward call inside `forward_model_batched` still fans out via OpenMP). That fan-out produces exactly 10 active OMP workers.

### Shared root cause hypothesis
The shared root cause is the **PyTorch / OpenMP default on a 10-core-20-thread CPU**:

- `torch.__config__.parallel_info()` on this box reports:
  ```
  at::get_num_threads() : 10
  omp_get_max_threads() : 10
  mkl_get_max_threads() : 10
  std::thread::hardware_concurrency() : 20
  ATen parallel backend: OpenMP
  ```
- GNU `libgomp` defaults `OMP_NUM_THREADS` to the number of **CPU cores as reported by `sched_getaffinity`, not threads**. On SMT/hyperthreaded Intel hardware it uses one thread per physical core unless `OMP_NUM_THREADS` / `GOMP_CPU_AFFINITY` / `OMP_PLACES` override it. Here: 10 physical cores → 10 OMP workers.
- PyTorch delegates intra-op parallelism to OpenMP, so `torch.get_num_threads()` inherits that value (10).
- Neither script, nor the benchmark/rollout C++ paths they use, override this default. The MCTS path would have forced `at::set_num_threads(4)` (`mcts_batched.cpp:2866`), but neither running process is in MCTS.
- Result: every `torch.jit::Module::forward()` call in either process saturates 10 logical CPUs with OMP workers; top's "10 running threads per process" is literally "one OMP parallel region per process, sized to the OpenMP default".

### Evidence for/against coincidence
Evidence it is NOT a coincidence:

1. `torch.get_num_threads()` returns 10 in a fresh `uv run python` on this machine, before any script logic. Both scripts import torch and use `torch.jit` forward passes, so both inherit 10 identically.
2. The host has **exactly 10 physical cores** (`lscpu`: Cores per socket 10, Threads per core 2, CPU(s) 20). This is the dominant factor; 10 = physical-core count, not 20/2.
3. `top -H -p <pid>` confirms **10 running, rest sleeping** for both processes while they are active:
   - elo PID 750631: 32 threads, 10 running, 22 sleeping.
   - train_ppo PID 796583: 110 threads, 10 running, 100 sleeping.
4. Neither script nor the exercised C++ functions call `at::set_num_threads`. The only such call is in the MCTS path, which neither process uses (elo tournament `n_simulations=0`; train_ppo rollouts also `n_simulations=0`).
5. There are no env vars (`OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `TORCH_NUM_THREADS`) set.

Evidence for a coincidence (weak):

- The `--rollout-workers` default in train_ppo is 1, and the elo tournament has no Python-level workers. So "10 Python worker threads" is not the explanation; the two scripts get to 10 via very different Python-level parallelism policies (elo: no Python threads; train_ppo: a `ThreadPoolExecutor` that defaults to 1 worker). Yet both land on 10 active threads — pointing firmly at a shared downstream mechanism (OpenMP/PyTorch), not a shared Python-level config.

## Conclusions
1. The observed "exactly 10 active threads" is dictated by PyTorch's OpenMP intra-op default, which equals the host's **physical core count** (10), not half of the 20 vCPUs.
2. Both scripts arrive at the same number via the same mechanism: they do not override `torch.set_num_threads`, and none of the C++ benchmark/rollout functions they call override it either. Only the MCTS path (unused by both processes) overrides the default (to 4).
3. It is not a coincidence, nor a hardcoded "10" anywhere in this repo, nor a 20/2 heuristic in Python. It is a direct consequence of (a) CPU topology and (b) the OpenMP default used by PyTorch's ATen backend.
4. With two concurrent processes each running 10 OMP workers at ~60-100% CPU, the machine is effectively at 20 active workers over 20 logical CPUs (and `top` confirms load average ~30). They are oversubscribing physical cores by ~2x (10 physical cores serving 20 concurrently active OMP workers across both processes), which costs throughput due to SMT contention and OMP busy-wait spinning.

## Recommendations
1. **Cap PyTorch threads per process to a smaller value** when running both jobs in parallel. For two co-tenant jobs on 10 physical cores, `OMP_NUM_THREADS=5` (or `torch.set_num_threads(5)`) per process eliminates contention without starving either. Even `OMP_NUM_THREADS=4` is reasonable because the MCTS path already chose 4 empirically.
2. **Add `torch.set_num_threads(N)` at the top of both scripts**, gated on a CLI flag (e.g. `--torch-threads`, defaulting to `min(4, os.cpu_count() // 2)`). Mirrors what `scripts/play_server.py:282` and the various `ismcts_*` scripts already do. This makes behavior deterministic across different host CPU counts (laptop vs cloud box) and removes the current "auto = 10" surprise.
3. **Set `OMP_NUM_THREADS` and `MKL_NUM_THREADS` in the launch wrappers** (`scripts/awr_chain.sh`, league runners) so the intent is visible at the shell level. Example: `OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 uv run python scripts/train_ppo.py ...`.
4. **Disable OpenMP busy-wait spinning** when co-scheduling: `OMP_WAIT_POLICY=passive` and/or `KMP_BLOCKTIME=0` reduce the "20 threads pinned at 60% CPU even during idle ticks" pattern. For PyTorch CPU inference on a laptop it is almost always a win.
5. **Consider setting interop threads to 1** (`torch.set_num_interop_threads(1)`) at script start. Currently both processes report `interop=10`, meaning small chains of ops can spawn extra TaskLauncher threads. The MCTS path forces interop=1 for a reason; extend the same policy to benchmark/rollout paths.
6. **If the two jobs must run concurrently**, align the two scripts' thread caps so they sum to <= physical core count. Suggested pairing: train_ppo at 6 threads, elo_tournament at 4 threads, both with `OMP_WAIT_POLICY=passive`. This should reduce wall time for both.
7. Lower priority: consider passing `torch_intra_threads` through the pybind wrapper for `benchmark_batched` / `benchmark_model_vs_model_batched` / `rollout_games_batched`, matching what the MCTS config already exposes. Today those entry points silently use the OpenMP default, which depends on the host CPU and has no visibility from Python.

## Open Questions
1. Under `--rollout-workers > 1`, would each Python worker thread still saturate 10 OMP threads, producing 10 × N active OMP workers and severe oversubscription? (Likely yes — OpenMP is per-process, and nested `torch.jit` forwards from different Python threads enter the same OMP pool, but the pool is sized to 10 per process.) Worth a quick measurement before bumping `--rollout-workers`.
2. Does `torch_intra_threads` propagate sanely when the pybind11 module is re-entered by a `ThreadPoolExecutor` in Python? The MCTS path sets it at the start of `run_mcts_batched`; confirm there is no thread-local vs global mismatch for ATen when Python threads interleave.
3. Would switching ATen parallel backend to `NATIVE_TBB` or `NATIVE` (set at PyTorch build time) give finer-grained control than OpenMP's "one pool per process" model? Probably not worth it given we use the standard wheel from pytorch-cu124.
4. On this WSL2 host, is `std::thread::hardware_concurrency() = 20` reliable across boots? If Windows reassigns SMT siblings the default could shift; another reason to pin `torch.set_num_threads` explicitly rather than rely on it.
