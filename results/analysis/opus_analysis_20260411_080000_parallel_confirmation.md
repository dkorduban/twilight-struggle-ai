---
# Opus Analysis: Parallel Confirmation Tournament
Date: 2026-04-11T08:00:00Z
Question: Can we run confirmation benchmark games in parallel as soon as checkpoints appear during training, instead of waiting for training to finish?

## Executive Summary

Yes, this is feasible and would eliminate most or all of the confirmation tournament gap. All benchmark games run on CPU (via `tscore.benchmark_batched` and `tscore.benchmark_model_vs_model_batched` with `device="cpu"`), while training uses the GPU, so there is no GPU contention. The match cache (`results/matches/`) already supports exactly this pattern: early-computed results are keyed by model name and automatically picked up by `run_elo_tournament.py`. The most practical approach is a lightweight filesystem watcher that detects new `ppo_iter*_scripted.pt` files during training and launches per-checkpoint benchmark jobs against the fixture panel. For v53 this would have saved ~40 minutes of idle GPU time.

## Findings

### Current pipeline timing

From the autonomous_decisions.log, the between-run gap consists of:
1. **Confirmation tournament** (ppo_confirm_best.py): 2s to 40min depending on cache hits
2. **Elo tournament** (run_elo_tournament.py): 8-10min
3. **Launch overhead**: ~1min

Recent data points:
| Run | Confirm | Elo | Total gap | Training | GPU idle % |
|-----|---------|-----|-----------|----------|------------|
| v53 | 40 min  | 10 min | 50 min | 43 min | 54% |
| v52 | 2 sec   | 9 min  | 9 min  | 33 min | 21% |
| v51 | 2 sec   | 8 min  | 8 min  | 32 min | 20% |
| v46 | 12 min  | 6 min  | 18 min | 31 min | 37% |
| v45 | 7 min   | 6 min  | 13 min | ~75 min | 15% |

The v53 confirmation was slow because the run-prefix naming (`ppo_v53_league_iter0010` vs old `iter0010`) caused 49 of 55 match pairs to be cache misses. With 8 candidates + 4 fixtures = 12 models, round-robin produces 66 pairs. Each 200-game match takes 27-68 seconds on CPU.

### GPU vs CPU resource separation

Training uses GPU (`--device cuda`) for the forward/backward pass. Rollout collection uses the C++ engine via `tscore` bindings, which is CPU-bound. Benchmark games also run entirely on CPU. The panel eval worker (`_panel_eval_worker`) already explicitly runs on CPU and is spawned as a background process during training. This proves the architecture supports concurrent CPU benchmark work alongside GPU training.

The RTX 3050 has 4GB VRAM. During rollout phases, the GPU is idle (rollout is C++/CPU). During gradient updates, GPU is active but CPU is mostly idle. A background benchmark process would compete for CPU during rollout collection, but since rollouts already run with `--rollout-workers 1`, there's capacity. The machine likely has multiple CPU cores (the C++ benchmark uses `pool_size` for batched game execution).

### Match cache compatibility

**This is the key enabler.** `run_elo_tournament.py` loads `results/matches/*.json` files at startup (line 406-416). Each file is keyed by `frozenset([model_a, model_b])`. The confirmation tournament inherits this behavior because it calls `run_elo_tournament.py` as a subprocess (line 132-143) and does NOT override `--match-cache-dir`, so it defaults to `results/matches/`.

The naming convention is critical. Since ppo_confirm_best.py line 99 uses `run_prefix = os.path.basename(run_dir.rstrip("/"))` to form names like `ppo_v53_league_iter0010`, a background watcher must use the **same naming convention** for cache files to be recognized. Specifically, the cache file for "ppo_v53_league_iter0010 vs v14" must be named `ppo_v53_league_iter0010__vs__v14.json` (sorted alphabetically).

### What a background watcher needs to do

For each milestone checkpoint (iter 10, 20, 30, ..., 80):
1. Detect `ppo_iter{N:04d}_scripted.pt` appearing in the run directory
2. Name it as `{run_prefix}_iter{N:04d}` (matching ppo_confirm_best.py convention)
3. Run matches against each fixture (v8, v14, v22, heuristic) = 4 matches per checkpoint
4. Write results to `results/matches/{sorted_pair_name}.json`

This pre-computes the **candidate-vs-fixture** pairs (8 candidates x 4 fixtures = 32 pairs). The **candidate-vs-candidate** pairs (8*7/2 = 28 pairs) cannot be pre-computed until both checkpoints exist, but they could be started as soon as both are available (e.g., iter0020 vs iter0010 can start after iter0020 is saved).

With 8 milestone checkpoints appearing at ~5 min intervals (80 iters, each ~30-40s), and each match taking ~45s on CPU:
- After iter0010: launch 4 fixture matches (~3 min)
- After iter0020: launch 4 fixture matches + 1 cross-candidate match (~4 min)
- ...
- After iter0080: launch 4 fixture + 7 cross-candidate matches

Most work is parallelizable. With a single CPU benchmark thread, the 4 fixture matches for each checkpoint take ~3 min, and checkpoints arrive every ~5 min, so the watcher keeps up easily. All 32 fixture matches would finish within ~3 min of the last checkpoint, and most cross-candidate matches (28 pairs) would also be done or nearly done.

### Architecture options

**Option A: Standalone watcher script (recommended)**

A new script `scripts/ppo_confirm_watcher.sh` or `scripts/ppo_confirm_watcher.py` that:
- Is launched as a background process alongside `train_ppo.py` in `ppo_loop_step.sh`
- Polls the run directory for new `ppo_iter*_scripted.pt` files every 30s
- For each new file, runs `run_elo_tournament.py` with just that checkpoint + fixtures
- Uses `--match-cache-dir results/matches` so results are cached for the confirmation tournament
- Exits when training finishes (detects `ppo_final.pt`)

Pros: Simple, decoupled, no changes to train_ppo.py. Easy to kill or restart independently.
Cons: Extra process to manage, polling overhead (minimal).

**Option B: Integrated into train_ppo.py**

Extend the existing `_panel_eval_worker` pattern to also run confirmation-style matches.

Pros: Already has the spawning infrastructure, knows exactly when checkpoints are saved.
Cons: Adds complexity to an already complex training script. Panel eval already runs as a background process; adding more concurrent benchmark work risks CPU oversubscription.

**Option C: Modified ppo_loop_step.sh**

Launch the watcher as part of the pipeline script, right after launching train_ppo.py.

Pros: Pipeline-level coordination is natural here.
Cons: The watcher needs to know the run prefix and fixture list, which ppo_loop_step.sh already has.

**Recommendation: Option A launched from Option C.** A standalone watcher script, started from ppo_loop_step.sh right after the training launch. This is the cleanest separation of concerns.

### Alternative: Skip confirmation entirely

The panel eval already runs inline during training (every 10 iterations, 200 games per opponent, 4 opponents). It provides `combined_wr` for each checkpoint against the same fixture set. The confirmation tournament re-runs these same matchups but at higher game counts (200 per pair in round-robin, so effectively more data).

**Panel eval gives 200 games per fixture (100/side).** The confirmation tournament gives 200 games per pair (100/side) in a round-robin, which includes fixture matches AND cross-candidate matches. The cross-candidate matches provide additional ranking signal.

Looking at v53 panel eval data:
- iter10: avg=0.545, iter20: 0.529, iter30: 0.522, ..., iter70: 0.463
- Panel eval clearly shows iter10 was the best checkpoint

The confirmation tournament's value-add is:
1. Cross-candidate matches for finer ranking among similar checkpoints
2. BayesElo fitting which is more statistically principled than raw WR averaging
3. Higher confidence from more total games

**However**, for iterations where there is a clear panel-eval winner (like v53 where iter10 >> iter70), the confirmation tournament is unnecessary overhead. A hybrid approach could skip confirmation when the panel-eval gap exceeds a threshold.

### Edge cases

1. **Training finishes before all benchmark games complete**: The watcher should detect `ppo_final.pt` and wait for in-flight jobs to finish. The confirmation tournament will pick up whatever is cached and re-run only the missing pairs.

2. **Checkpoints that get overwritten**: Non-milestone checkpoints (those not at `eval_every` boundaries) are deleted after the next checkpoint is saved (lines 2924-2934). Milestone checkpoints are preserved. Since confirmation uses milestone checkpoints only, this is safe. The watcher should only target milestone iterations.

3. **CPU contention during rollout collection**: Rollout collection is CPU-intensive (C++ game simulation). Running benchmark games concurrently could slow both. Mitigation: use `nice -n 15` for the watcher, or limit to 1 concurrent benchmark match. Since training already runs with `nice -n 10` (line 295), the watcher should use a higher nice value.

4. **Naming collision across runs**: The run prefix (`ppo_v53_league`) ensures v53 checkpoint names don't collide with v54 names. This is already handled correctly.

5. **Stale cache entries**: If the watcher writes a cache entry for `ppo_v53_league_iter0010 vs v14`, and the confirmation tournament reads it, the data is valid because the scripted checkpoint is immutable once written. There is no staleness risk.

## Conclusions

1. **Parallel confirmation is feasible and straightforward.** All benchmark games run on CPU; training uses GPU. The match cache in `results/matches/` already supports exactly this pattern with no code changes to `run_elo_tournament.py` or `ppo_confirm_best.py`.

2. **The time savings are significant for cache-miss runs.** When the naming convention changed (v53), the confirmation tournament took 40 minutes with the GPU idle. With pre-computation, this drops to near zero: the confirmation tournament would find all pairs cached and finish in seconds.

3. **For cache-hit runs (v47-v52), the savings are minimal** because the confirmation already completes in 2 seconds from cache. The parallel approach matters most when naming conventions change or new fixtures are added.

4. **The recommended implementation is a standalone watcher script** launched from `ppo_loop_step.sh` alongside training. It polls for new `ppo_iter*_scripted.pt` files and runs fixture matches in the background. Estimated implementation: ~80 lines of Python, ~5 lines added to ppo_loop_step.sh.

5. **An even simpler alternative: skip confirmation and trust panel eval.** Panel eval already provides 200 games per fixture per checkpoint. The confirmation tournament's additional value (cross-candidate round-robin + BayesElo) could be replaced by simply selecting the panel-eval argmax. This eliminates the gap entirely with zero new code. The cost is slightly less statistical confidence in checkpoint selection.

6. **CPU contention is manageable.** Training rollouts and benchmark games both use CPU, but at different phases. Using `nice` priorities and limiting benchmark concurrency to 1 match at a time keeps interference minimal.

7. **The Elo tournament (8-10 min) cannot be parallelized with this approach** because it runs AFTER training finishes and includes the new model. However, most of its match pairs are cached across runs, so it primarily pays for new-model-vs-existing pairs. This could also be partially pre-computed but is a smaller win.

## Recommendations

1. **Quick win (no new code):** Consider whether the confirmation tournament adds enough value over raw panel eval to justify its existence. If not, delete the confirmation step entirely and select ppo_best.pt as the panel-eval argmax. This saves 0-40 min per run with zero implementation risk.

2. **If keeping confirmation:** Implement a lightweight `scripts/ppo_confirm_watcher.py` that:
   - Takes `--run-dir`, `--fixtures`, and `--n-games` arguments
   - Polls for new `ppo_iter*_scripted.pt` files every 30 seconds
   - For each new scripted checkpoint, runs matches against all fixtures
   - Uses the run-prefix naming convention from ppo_confirm_best.py
   - Writes results to `results/matches/`
   - Runs with `nice -n 15` to avoid interfering with training rollouts
   - Exits when `ppo_final.pt` appears

3. **Launch from ppo_loop_step.sh:** Add a `nohup nice -n 15 uv run python scripts/ppo_confirm_watcher.py ...` right after the training launch.

4. **For cross-candidate matches:** After two consecutive milestone checkpoints exist, also run their head-to-head match. This is a stretch goal -- the fixture matches alone provide most of the cache benefit.

5. **Measure the actual benefit:** Compare panel-eval-selected best vs confirmation-selected best over the last 10 runs. If they agree >90% of the time, the confirmation tournament can be safely removed.

## Open Questions

1. **How often does the confirmation tournament override the panel-eval choice?** If the panel-eval argmax almost always wins the confirmation tournament, the entire confirmation step is redundant.

2. **CPU core count on the target machine?** If there are many cores (8+), multiple benchmark matches could run in parallel. If 4 cores, sequential is safer.

3. **Should the Elo tournament also be partially pre-computed?** The new-model-vs-all-existing matches could be started as soon as the scripted model is exported to `scripted_for_elo/`, which happens at the start of `ppo_loop_step.sh`. This would save another 8-10 minutes.

4. **Would reducing n_top from 8 to 3-4 be sufficient?** This cuts the round-robin from 66 pairs to ~21-28 pairs, making the confirmation tournament 3x faster even without parallelization. The original default was 3; it was recently changed to 8.
---
