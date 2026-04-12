---
# Opus Analysis: Iteration Speed Regression (20s -> 187s)
Date: 2026-04-12T20:35:00Z
Question: Why did iterations go from ~20s to ~187s, and how to recover?

## Executive Summary

The 20s iterations (v10-v77_sc) ran with `--rollout-workers 1`, making 5 sequential C++ rollout calls that each use 10 intra-op torch threads on 20 cores -- efficient single-stream execution. The 187s iterations (v79_sc with `--rollout-workers 5`) launch 5 parallel threads, each loading 2 TorchScript models that internally spawn 10 intra-op threads, creating ~100 OS threads on 20 cores -- massive oversubscription that causes a 7x slowdown vs the sequential baseline. A secondary factor is that **all** prior slow observations (v1=543s, v68 iter1=700s, v78 iter1=167s, v79 workers=1=587s) coincided with concurrent background processes (candidate tournaments, Elo ladder rebuilds) consuming CPU. The intrinsic clean speed for 200 model-vs-model games with workers=1 is ~26s (v78 iters 6-10), not 587s.

## Findings

### Current architecture

The PPO rollout in `collect_rollout_league_batched()` works as follows:
- With `--league-mix-k 6` and `--league-self-slot`: total_slots = 1 (self) + 2 (USSR) + 2 (US) = **5 tasks**
- Each task gets `games_per_slot = 200 // 5 = 40` games
- Each task calls `_collect_vs_model_from_script()` which invokes `tscore.rollout_model_vs_model_batched()` in C++
- The C++ function loads 2 TorchScript models from disk, runs batched inference with `pool_size=40`
- `ThreadPoolExecutor(max_workers=N)` manages parallelism; C++ releases the GIL

Key parameters:
- `torch.get_num_threads()` = 10 (intra-op parallelism per model inference call)
- `torch.get_num_interop_threads()` = 10
- Hardware: 20 CPU cores, RTX 3050 4GB GPU (not used for rollout -- all `device="cpu"`)

### Old path (20s era)

**v10-v24 (original league, ~12-17s rollout):**
- Single opponent per iteration: `sample_league_opponent()` picked ONE opponent
- ONE C++ `rollout_model_vs_model_batched()` call with `n_games=200, pool_size=64`
- Workers=1 (feature did not exist yet)
- Clean single-stream execution: 2 models x 10 threads = 20 threads on 20 cores

**v55-v77_sc (two-pool PFSP, ~15-20s rollout):**
- 5 tasks (1 self + 2 USSR + 2 US), workers=1
- Sequential execution: 5 C++ calls x 40 games each
- Still efficient: at most 2 models x 10 threads at any moment = 20 threads
- Occasionally includes heuristic slots (0.1s each), reducing total time
- v77_sc clean: 14-15s rollout; v78_sc clean (iters 6-10): 26s rollout

### Bottleneck identification

**Primary bottleneck: CPU thread oversubscription with `--rollout-workers 5`**

| Config | Active threads | Wall time (200 games) | Per-game |
|--------|---------------|----------------------|----------|
| workers=1, no contention (v78 iter 6-10) | 20 (2 models x 10) | 26s | 0.13s |
| workers=5, no contention (v79 final) | ~100 (10 models x 10) | 179s | 0.90s |
| workers=1, contention (v79 first run) | 20 + background | 587s | 2.94s |

The workers=5 config creates 5x oversubscription (100 threads / 20 cores = 5x). This causes:
- Cache thrashing across threads
- Context switching overhead
- Memory bandwidth saturation
- Lock contention in TorchScript inference

**Secondary bottleneck: background process contention**

Every generation launch from `ppo_loop_step.sh` concurrently spawns:
1. Candidate tournament (hundreds of benchmark games)
2. Elo ladder rebuild (plays many model-vs-model games)
3. Panel evaluation (60+ games per opponent)

These background processes use the same CPU cores. Evidence:
- v68_sc iter 1 = 701s (tournament + Elo running); iter 14+ = 15s (clean)
- v78_sc iter 1 = 166s (tournament + Elo running); iter 6-10 = 26s (clean)
- v79_sc workers=1 first run = 587s (tournament + Elo running)

### Parallelism ceiling

With `device="cpu"` and `torch.get_num_threads()=10`:
- **Optimal workers = 1** for this hardware. The C++ rollout already uses all 20 cores via intra-op parallelism for batch inference of pool_size positions.
- **Workers > 1 causes slowdown**, not speedup. The GIL release enables true parallelism, but CPU threads from multiple workers compete for the same cores.
- **Workers = 2 might break even** if intra-op threads were set to 4 per task (2 tasks x 2 models x 4 threads = 16 threads on 20 cores).

## Conclusions

1. **The regression is caused by `--rollout-workers 5` oversubscribing CPU threads.** With `torch.get_num_threads()=10`, each C++ rollout call (2 models) uses ~20 threads. Five parallel workers create ~100 threads on 20 cores.

2. **The "3.2x speedup from workers=5" was an illusion.** It compared workers=5 (179s) against workers=1 with background contention (587s). The true workers=1 clean baseline is 26s -- workers=5 is actually 7x SLOWER.

3. **Background processes (candidate tournament, Elo rebuild) caused the initial 587s measurement.** Every generation launch spawns CPU-heavy background work that contends with the training rollout.

4. **The model architecture did NOT change.** v67_sc through v79_sc all use the same `country_attn_side` model. The 14-26s clean rollout range is stable across all of them.

5. **The old v10-v24 single-opponent path was slightly faster** (12-17s) because it made one C++ call with pool_size=64 instead of five calls with pool_size=40, gaining better batch inference efficiency.

6. **The intrinsic per-game inference cost is ~0.07-0.13s** for the attention model on CPU with optimal threading. This is not inherently slow.

## Recommendations

1. **Set `--rollout-workers 1` immediately.** This alone should restore ~26s iterations (7x speedup over current 187s). The current ppo_loop_step.sh already has `--rollout-workers 1` on line 292 -- verify this is what actually launches.

2. **Defer background work.** In `ppo_loop_step.sh`, do not launch candidate tournament or Elo rebuild until the training process has completed. Or: launch background eval processes with `OMP_NUM_THREADS=2 MKL_NUM_THREADS=2` and `taskset` to restrict them to specific cores, leaving the training process with the majority of cores.

3. **Set `torch.set_num_threads(1)` in C++ rollout when workers > 1.** If multi-worker parallelism is desired for the GIL-release benefit, add `at::set_num_threads(max(1, 20 / (n_workers * 2)))` at the start of each rollout call. For workers=5: `20 / 10 = 2` threads per model, yielding `5 * 2 * 2 = 20` threads total.

4. **Consolidate rollout into fewer C++ calls.** The old single-opponent path made one call with pool_size=64. If multi-opponent is needed, batch them into one C++ call (e.g., preassign games to opponents, pass an opponent schedule). This eliminates per-call model-loading overhead and maximizes batch efficiency.

5. **If workers > 1 is needed for exploration diversity, set `OMP_NUM_THREADS=2` before launching train_ppo.py.** This limits all TorchScript intra-op parallelism to 2 threads per call. With workers=5: `5 * 2 * 2 = 20` total threads on 20 cores. Expected time: ~40-60s (vs 26s with workers=1).

6. **Profile the clean workers=1 path.** Run v80_sc with `--rollout-workers 1` and no background processes. Confirm 20-26s rollout. If still slow, the cause is something else (model size growth, Python overhead).

## Open Questions

1. Why does v78_sc clean (26s) differ from v77_sc clean (14s) despite identical model architecture? Likely explanation: v77 had more heuristic slots (which complete in ~0.1s), reducing total wall time. But both are within the expected range for the attention model.

2. Would GPU inference (`device="cuda"`) be faster than CPU for the attention model? The RTX 3050 has 4GB VRAM -- the model is small enough to fit. GPU batch inference could be 2-5x faster per batch, potentially bringing rollout to ~5-10s. However, this would conflict with GPU memory needed for the training backward pass.

3. Is the SmallChoice callback overhead in `rollout_model_vs_model_batched` significant? The callback creates closures and does scalar operations per decision. Unlikely to be a major factor but worth profiling.

---
