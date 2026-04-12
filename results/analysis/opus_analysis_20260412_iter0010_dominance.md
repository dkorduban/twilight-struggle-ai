---
# Opus Analysis: iter_0010 Dominance in Panel Eval
Date: 2026-04-12
Question: Why is iter_0010 the best checkpoint in >50% of runs? What should we change?

## Executive Summary

iter_0010 dominates as the panel eval high-water mark due to a convergence of five
reinforcing factors, not a single root cause:

1. **First-mover bias in HWM tracking**: Option F uses a running maximum. The first
   measurement (always iter 10) sets the bar. Subsequent iters must *exceed* it,
   not merely match. With noisy 200-game panel evals (SE ~0.035 per opponent),
   a flat-to-declining true curve means the first measurement wins by coin flip >50%
   of the time.

2. **Heuristic WR decay inflates early scores (old panel)**: In the v55-v62 era panel
   (v8/v14/v22/heuristic), heuristic WR declines monotonically from ~0.90 at iter 10
   to ~0.65 at iter 70. Since heuristic had the highest weight (or equal weight), this
   systematic decline in one component drags down the avg even if model-vs-model WR
   is flat. The model is not getting weaker against strong opponents --- it is losing
   a cheap-to-beat sparring partner.

3. **No real improvement signal across 80 iterations**: Against strong panel opponents
   (v14, v22, v55), the WR is essentially flat across all 80 iterations in every run.
   Values hover at 0.45-0.52 with no upward trend. The model starts near its
   ceiling for the current architecture+data and PPO cannot push it further.

4. **Entropy decline is modest, not catastrophic**: Entropy drops from ~4.0 to ~3.7
   over 80 iters (ent_coef 0.01->0.003 linearly). KL stays well below the 0.3
   threshold (typically 0.002-0.007). This is NOT aggressive entropy collapse ---
   the policy is stable but not improving.

5. **League self-play does not generate an improvement gradient**: With UCB-PFSP
   selecting opponents the model struggles against, the model plays opponents near
   its own strength. Rollout WR hovers at 0.45-0.55 across all iterations. There is
   no easy-to-hard curriculum that could produce an upward panel WR trend.

The core issue is that **80 PPO iterations of self-play produce no measurable
improvement over the starting checkpoint**, and the panel eval measurement noise
combined with the HWM first-mover bias ensures iter 10 is selected.

## Findings

### 1. Panel WR curves are flat-to-declining across all runs

Data from logs (avg panel WR by iteration):

| Run   | i10   | i20   | i30   | i40   | i50   | i60   | i70   | Best  |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| v55   | 0.586 | 0.562 | 0.601 | 0.594 | 0.551 | 0.564 | 0.565 | i30   |
| v56   | 0.609 | 0.598 | 0.570 | 0.545 | 0.545 | 0.544 | 0.565 | i10   |
| v57   | 0.600 | 0.550 | 0.574 | 0.551 | 0.537 | 0.550 | 0.525 | i10   |
| v58   | 0.571 | 0.560 | 0.575 | 0.540 | 0.517 | 0.555 | 0.524 | i30   |
| v59   | 0.566 | 0.564 | 0.539 | 0.545 | 0.520 | 0.527 | 0.487 | i10   |
| v60   | 0.571 | 0.546 | 0.490 | 0.526 | 0.550 | 0.527 | 0.527 | i10   |
| v61   | 0.569 | 0.530 | 0.546 | 0.499 | 0.509 | 0.504 | 0.513 | i10   |
| v62   | 0.556 | 0.520 | 0.524 | 0.499 | ---   | ---   | ---   | i10   |
| v65   | 0.574 | 0.580 | 0.575 | 0.585 | 0.566 | 0.556 | 0.586 | i70*  |
| v67sc | 0.478 | ---   | ---   | ---   | ---   | ---   | ---   | i10** |

*v65 used old panel with heuristic (different weighting). **v67sc still running.

Of 9 completed runs with panel data: **6 out of 9 have iter 10 as best** (67%).
The remaining 3 have iter 30 or 70, but the differences are within noise (0.01-0.03).

### 2. Heuristic WR declines systematically while model-vs-model WR is flat

Looking at v56 (clear iter-10-wins run):
- heuristic: 0.895 -> 0.895 -> 0.835 -> 0.800 -> 0.775 -> 0.715 -> 0.750
- v14:       0.480 -> 0.510 -> 0.535 -> 0.485 -> 0.475 -> 0.475 -> 0.530
- v22:       0.520 -> 0.490 -> 0.455 -> 0.475 -> 0.505 -> 0.495 -> 0.470

The heuristic WR drops 15pp (0.895->0.750) while v14/v22 WRs are statistically
flat. The model is adapting its play style toward beating learned opponents at the
cost of exploiting heuristic patterns. This is expected and healthy behavior, but
it *looks* like regression under the old panel weighting.

The new 5-opponent panel (v55/v54/v44/v45/v14, no heuristic) eliminates this
component but does not fix the underlying no-improvement problem (v67sc iter 10
still wins with 0.478 avg).

### 3. Entropy schedule is NOT the problem

The entropy coefficient decays linearly from 0.01 to 0.003 over global iterations
1-80 (as configured in ppo_loop_step.sh: `--global-ent-decay-start 1 --global-ent-decay-end 80`).

However, the actual measured entropy values barely change:
- v60: iter 1 ent=3.867, iter 10 ent=3.820, iter 40 ent=3.819, iter 80 ent=3.745
- v56: iter 1 ent=3.989, iter 10 ent=3.989, iter 40 ent=3.871, iter 80 ent=3.951
- v65: iter 1 ent=4.124, iter 10 ent=4.040, iter 40 ent=3.946, iter 80 ent=3.902

Entropy drops only ~5% over the full run. This is NOT aggressive collapse.
The 0.5 grad-norm clipping and 0.12 clip-eps keep updates conservative.

### 4. Learning rate is constant and low

LR = 2e-5, no warmup (lr-warmup-iters=0), no decay schedule. This is already very
conservative. KL divergence is tiny (0.002-0.007) throughout, well under the 0.3
early-stop threshold. The model is making very small updates per iteration.

The problem is not LR instability --- it's that the LR is fine but the gradient
signal from league self-play is uninformative. Playing opponents near your own
strength at ~50% WR produces high-variance, low-signal advantages.

### 5. The 80-iteration run is wasted compute after ~iter 20

There is no statistically significant improvement in model-vs-model panel WR
between iter 10 and iter 80 in ANY run. The 70 iterations after iter 10 cost
~70 * 22s = ~25 minutes of GPU time per run, producing no measurable benefit.

### 6. Panel eval sample size is marginal

Each panel eval plays 200 games per opponent (100 per side). With 5 opponents,
the combined WR is based on 1000 games. The standard error of a single opponent's
combined WR at 50% is sqrt(0.25/200) = 0.035. Differences of 0.02-0.03 between
iterations are pure noise.

### 7. Global entropy schedule is misconfigured for chained runs

`--global-ent-decay-start 1 --global-ent-decay-end 80` with `global_iter_offset`
computed from the checkpoint's `total_iters`. For v60 (loaded from v59, which loaded
from v58, etc.), global_iter could be ~400+. This means `global_iter >= global_ent_decay_end`
is true from iter 1, so `current_ent_coef = ent_coef_final = 0.003` for the ENTIRE run.
The "0.01 -> 0.003" schedule logged in autonomous_decisions.log is a lie for late-chain
runs --- they start and stay at 0.003.

This is actually less harmful than it sounds (0.003 is still reasonable) but it means
the entropy schedule configuration is misleading.

### 8. Missing iter 80 panel eval (async race condition)

The panel eval is triggered at milestones (including iter 80 = n_iterations). But
the eval runs async in a background process. The training loop ends immediately after
iter 80, and the final checkpoint code terminates any still-running panel eval process
(line 3409-3411). So iter 80's panel eval is typically killed before it completes,
meaning the panel_eval_history.json never has an iter 80 entry. This is confirmed
by the logs: no run shows "panel eval iter 80" results.

This means the HWM selection can only choose from {10, 20, 30, 40, 50, 60, 70} ---
7 measurement points. Even if the model improved at iter 80, we'd never know.

## Conclusions (numbered)

1. **The model does not improve during 80 iterations of league self-play.** Against
   strong panel opponents, WR is statistically flat from iter 10 to iter 70 in all
   observed runs. The improvement signal from playing opponents near your own strength
   is too weak relative to the noise floor.

2. **iter 10 wins by first-mover bias in noisy HWM tracking.** With 7 measurement
   points on a flat curve and SE ~0.035, the probability of the first measurement
   being the maximum is roughly 1/7 * (1 + noise_bias) where noise_bias comes from
   the slight downward trend in heuristic WR. Observed 67% >> 14% expected under
   uniform, confirming the systematic downward trend.

3. **Heuristic WR decline is the dominant signal in the old panel.** The 15pp decline
   in heuristic WR over 70 iterations creates an artificial downward trend in the
   avg metric that does not reflect model-vs-model strength.

4. **The entropy schedule is not causing collapse.** Entropy barely changes, and KL
   divergence stays tiny. The issue is not policy collapse but policy stagnation.

5. **80 iterations is ~4x too long for the current configuration.** With no
   improvement signal, running beyond iter 20 wastes 75% of compute.

6. **The iter 80 panel eval is systematically lost** due to async process termination,
   removing one data point from every run.

7. **The global entropy schedule is effectively constant** for chained runs after v56,
   since global_iter_offset exceeds global_ent_decay_end (80) by then.

## Recommendations (numbered, actionable)

1. **Reduce n_iterations from 80 to 30.** No run shows improvement after iter 30.
   This saves 60% of per-run compute and produces the same or better best checkpoint
   (since there are fewer noise opportunities to regress). Re-evaluate after
   implementing recommendations 3-5.

2. **Wait for final panel eval before terminating.** After the last iteration's panel
   eval is launched, wait for it to complete (with a timeout) before writing
   ppo_best.pt. Currently iter 80 eval is always killed. Fix: add a
   `_panel_proc.join(timeout=300)` before the termination block at line 3408.

3. **Increase panel eval games from 200 to 400 per opponent.** This halves the SE
   from 0.035 to 0.025, making the HWM selection more reliable. Cost: ~2x panel eval
   time (currently ~176s, would become ~352s), which is small relative to the 25min
   training run.

4. **Remove heuristic from panel eval** (already done in v67_sc config). The heuristic
   WR decline is an artifact of learning to play model-vs-model style, not true
   regression. The new 5-opponent panel is correct.

5. **Add a curriculum or difficulty ramp to league self-play.** Currently PFSP selects
   hard opponents from iter 1. Consider:
   - Start with easier opponents (heuristic + weaker past versions) for iters 1-10
   - Gradually increase opponent difficulty via recency_tau schedule
   - Or use a population-based approach where easy wins provide clear gradient signal
   
   Without a curriculum, the model trains at ~50% WR from iter 1, which maximizes
   entropy of the reward signal and minimizes useful gradient information.

6. **Fix the global entropy schedule for chained runs.** Either:
   - Set `--global-ent-decay-end` to a much higher value (e.g., 1000) so entropy
     actually decays across the full lineage, OR
   - Remove the global schedule entirely and use per-run decay (start=1, end=80
     relative to per-run iteration), OR
   - Use a constant ent_coef=0.003 (which is what actually happens now) and simplify.

7. **Consider larger architectural or algorithmic changes for continued improvement.**
   The flat WR curve suggests the current model architecture has reached a plateau
   that PPO self-play alone cannot overcome. Candidates:
   - MCTS/search during self-play to generate stronger training targets
   - Distillation from a stronger teacher (even if the teacher is just MCTS + current model)
   - New input features or architecture improvements
   - Reward shaping beyond win/loss

8. **Log the per-opponent WR breakdown to W&B at each panel eval** (already done) and
   add a "best_iter_so_far" metric that shows which iteration is currently the HWM,
   to make the pattern visible in dashboards without post-hoc log parsing.

## Open Questions

1. Would MCTS at inference time (even shallow, 50-100 simulations) produce enough
   improvement signal to break the plateau when used during self-play training?

2. Is the flat curve a property of the minimal_hybrid architecture, or would the
   attention model (TSCountryAttnModel) show the same pattern?

3. The v65 run (iter 70 best with 0.586) is an outlier --- it used old panel weights
   with heuristic. Was its improvement real, or did iter 70 just get lucky with the
   heuristic WR measurement?

4. Would value function bootstrapping quality improve with a separate value network
   (currently shared trunk), and would that provide better advantage estimates for
   the PPO update?
---
