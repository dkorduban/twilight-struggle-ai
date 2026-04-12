---
# Opus Analysis: Eager Per-Checkpoint Matching During Training
Date: 2026-04-12T14:30:00Z
Question: Why not Option E — running matches eagerly as new checkpoints appear during training? As soon as iter_0010.pt appears, start running it vs the fixed 5 opponents; as soon as iter_0020.pt appears, run it vs the same 5 PLUS vs iter_0010; and so on. By the time training ends, all inter-checkpoint matchups are already done and BayesElo can instantly pick the best checkpoint with full data — no waiting, no suboptimal ppo_final.pt warm-start.

## Executive Summary

Option E (eager background matching) is already substantially implemented via two existing mechanisms: (1) async panel eval every 10 iterations during training, and (2) WS7 incremental Elo confirmation launched at every milestone. The remaining gap — inter-checkpoint head-to-head matchups — provides minimal additional signal over the existing panel WR data, while adding significant CPU contention risk on this single-GPU, single-machine setup. Option F (save ppo_running_best.pt on panel-eval high-water mark) is the better choice: it requires ~20 lines, runs with zero additional CPU cost, and eliminates the warm-start problem immediately. The inter-checkpoint matchups can be run post-training in the existing confirmation tournament if needed, adding <5 minutes.

## Findings

### Current panel eval coverage

The training loop already runs comprehensive panel evaluation:

- **Cadence**: Every 10 iterations (`--eval-every 10`), which matches `--league-save-every 10`.
- **Panel**: 4 fixed opponents (v8_scripted, v14_scripted, v22_scripted, heuristic).
- **Games per eval**: 200 games per opponent (100 as USSR, 100 as US), so 800 games total per checkpoint.
- **Execution**: Runs in a spawned background Process on CPU, non-blocking to GPU training.
- **Persistence**: Results written to `panel_eval_history.json` with per-opponent combined WR.
- **Coverage**: For an 80-iteration run, this produces panel eval data at iterations 10, 20, 30, 40, 50, 60, 70, 80 — **8 checkpoints evaluated against 4 opponents = 32 match sets already collected during training**.

Additionally, WS7 (lines 3201-3216 of train_ppo.py) already launches `post_train_confirm.sh --incremental` at every milestone iteration. This runs the checkpoint through an incremental Elo placement vs 5-6 opponents. So there is already a form of eager matching happening.

### Option E mechanics and timing

**Checkpoint save cadence**: iter_*.pt saved to the league pool every 10 iterations (line 329 of ppo_loop_step.sh). With 80 total iterations, that's 8 checkpoints: iter_0001, iter_0010, iter_0020, ..., iter_0080.

**Match timing per set**: Each match set = 200 games (100 per side). Based on the C++ batched benchmark:
- vs heuristic: ~30-45 seconds (CPU-only, pool_size=32, fast heuristic opponent)
- vs scripted model: ~60-90 seconds (CPU-only, both sides run neural inference)
- 4-opponent panel eval: ~3-5 minutes total per checkpoint

**Option E match count growth**:
- After iter_0010: 5 matches (vs 5 fixed opponents)
- After iter_0020: 6 matches (5 fixed + vs iter_0010)
- After iter_0030: 7 matches (5 fixed + vs iter_0010, iter_0020)
- ...
- After iter_0080: 12 matches (5 fixed + 7 inter-checkpoint)
- **Total inter-checkpoint matches**: 1+2+3+4+5+6+7 = 28 additional matches
- **Total match sets**: 8*5 (panel) + 28 (inter-checkpoint) = 68 match sets
- **Estimated wall time**: 68 * ~75s = ~85 minutes of CPU work

**Training wall time**: 80 iterations * ~2-3 min/iter = ~160-240 minutes. So the eager matching would consume roughly 35-50% of the training wall time in background CPU work.

### Option E vs Option F comparison

**Option F (panel-eval high-water mark, ~20 lines in train_ppo.py)**:
- After each panel eval result is collected (lines 3234-3278), compare `avg_combined_wr` to a running best.
- If new best, copy current checkpoint to `ppo_running_best.pt`.
- Zero additional CPU cost — uses data already being collected.
- Available at training end with no delay.
- Picks the checkpoint with highest average panel WR — a direct, well-calibrated quality signal.

**Option E (eager background matching)**:
- Requires a filesystem watcher or polling loop (inotifywait or cron-like).
- Requires spawning background match processes that compete for CPU.
- Provides inter-checkpoint matchups (iter_0010 vs iter_0020, etc.).
- BayesElo can theoretically separate checkpoints more precisely.

**Does inter-checkpoint matching add signal?** Marginally. The 4-opponent panel (v8, v14, v22, heuristic) spans a wide Elo range (~1200-2100). A checkpoint's average WR against this panel is already a strong single-number quality metric. Inter-checkpoint matchups between consecutive iterations (which differ by ~10-30 Elo) would produce noisy 50-55% win rates that barely shift BayesElo rankings. The panel opponents provide much sharper discrimination because they span a wider ability range.

The existing `ppo_confirm_best.py` already does the right thing: it takes the top-8 panel-eval checkpoints and runs a proper round-robin. The question is whether this should happen eagerly during training or after training. Given that the confirmation tournament takes <5 minutes for 8 candidates and the training run takes 3-4 hours, the latency savings are negligible compared to the complexity cost.

### CPU/GPU contention risk

This is the critical risk on the current hardware (single RTX 3050 4GB, WSL2):

1. **Rollout collection** already uses 1 CPU worker thread running C++ game simulations with neural inference. This is the training bottleneck — rollout collection takes ~60-70% of iteration time.

2. **Panel eval** runs in a background spawned Process on CPU. It already competes with rollout collection for CPU cores. The code uses `pool_size=32` for batched benchmark, meaning up to 32 concurrent game threads.

3. **Adding inter-checkpoint matches** would mean potentially 2-3 concurrent CPU-heavy processes:
   - Rollout collection (training, GPU + CPU)
   - Panel eval (background, CPU-only)
   - Inter-checkpoint matching (background, CPU-only)

On a machine with limited CPU cores (typical for WSL2 on a consumer desktop), this would directly slow down rollout collection and therefore training. The `nice -n 15` used by WS7 helps but doesn't prevent CPU cache thrashing or memory bandwidth contention.

4. **Match runner falling behind**: With 80 iterations at ~2.5 min each, a new checkpoint appears every 25 minutes (every 10 iters). The match backlog per checkpoint grows linearly: by iter_0080, there are 12 matches to run (~15 min). The system would stay roughly caught up but with continuous CPU pressure throughout training.

## Conclusions

1. **Option E is already ~80% implemented.** The existing panel eval (4 opponents, every 10 iters) and WS7 incremental Elo check provide most of the eager-matching value. The missing piece is inter-checkpoint matchups and a "pick best at training end" mechanism.

2. **Inter-checkpoint matchups provide minimal additional signal.** Adjacent checkpoints separated by 10 iterations differ by ~10-30 Elo. A 200-game match between them produces a ~52% win rate with wide confidence intervals. The 4-opponent panel spanning 900 Elo provides far sharper discrimination.

3. **Option F is strictly better on this hardware.** It solves the actual problem (avoiding suboptimal ppo_final.pt warm-start) with zero CPU overhead, ~20 lines of code, and no background process management. It uses the panel eval data that is already being collected.

4. **CPU contention is a real concern.** Running eager inter-checkpoint matches during training would add ~35-50% CPU load, directly competing with rollout collection — the training bottleneck. This could slow training by 10-20%, costing more wall time than the confirmation tournament saves.

5. **The confirmation tournament is fast enough post-training.** ppo_confirm_best.py with 8 candidates takes <5 minutes. This is negligible compared to the 3-4 hour training run.

## Recommendations

1. **Implement Option F immediately** (~20 lines in train_ppo.py):
   - Track `best_panel_wr` and `best_panel_iter` as running state.
   - After each panel eval result, if `avg_combined_wr > best_panel_wr`, copy the current checkpoint to `ppo_running_best.pt` and its scripted version to `ppo_running_best_scripted.pt`.
   - At training end, if `ppo_running_best.pt` exists, use it instead of `ppo_final.pt`.
   - This makes the next training run warm-start from the best checkpoint seen during training, with zero latency.

2. **Keep the existing WS7 incremental Elo check** — it provides Elo-scale feedback in the log without CPU contention (runs niced, sequential, ~2 min per milestone).

3. **Keep the existing post-training confirmation tournament** as a safety net — it validates the panel-eval-based selection with actual head-to-head matches among top candidates.

4. **Do not implement a checkpoint watcher or background match runner.** The complexity (filesystem polling, process management, match queue, fall-behind handling) is not justified by the marginal signal gain over panel WR.

5. **If inter-checkpoint matchups are ever desired**, run them in the post-training confirmation tournament by adding `--include-inter-checkpoint` to ppo_confirm_best.py. This avoids all CPU contention concerns.

## Open Questions

1. **Is the panel eval running reliably?** The async panel eval uses `daemon=True` Process with spawn context. If training crashes, the panel eval process is killed and results for the last milestone are lost. This is acceptable but worth noting.

2. **Should the running-best selection weight per-side WR differently?** The current panel eval tracks USSR and US WR separately. If the model is systematically better on one side, a combined average may not pick the best overall checkpoint. Consider weighting by `min(ussr_wr, us_wr)` or using the geometric mean to penalize lopsided performance.

3. **Should ppo_loop_step.sh prefer ppo_running_best.pt over ppo_final.pt?** If Option F is implemented, the chain becomes: `ppo_running_best.pt` (if exists) > `ppo_best.pt` (confirmation tournament winner) > `ppo_final.pt` (fallback). The running best should be the default since it's available immediately; the confirmation tournament can upgrade it to `ppo_best.pt` later.
