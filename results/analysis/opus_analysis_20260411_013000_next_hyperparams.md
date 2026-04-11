# Opus Analysis: Next Hyperparameters to Try
Date: 2026-04-11T01:30:00Z
Question: What hyperparameters/configs to try next to push past Elo 2105?

## Executive Summary

v44 reached Elo 2105 using a near-replica of v22's config (T=1.0, no Dirichlet, PFSP=1.0, constant ent_coef=0.03, reset optimizer). Its best checkpoint was iter 20 out of 200, meaning 90% of training was wasted or harmful -- the model peaked early and degraded through the rest of the run. The most impactful changes for v46+ are: (1) shorter runs of 60-80 iterations with early stopping, (2) fix the entropy coefficient decay so it actually fires within each run (v44 used constant 0.03; v45 inherits a misleading total_iters=20 from BC training args that makes the global decay fire prematurely), (3) reduce ent_coef to 0.01-0.015 to allow policy sharpening since the policy entropy is already high at 4.2-4.6, and (4) try UPGO to reduce variance from the sparse terminal reward signal. Architecture changes and Dirichlet noise are lower priority -- the current config has not been properly exploited yet.

## Findings

### 1. v44 Peaked at Iter 20 -- Runs Are Too Long

The confirmation tournament for v44 tested three candidates: iter 20, iter 60, and iter 160. Results:
- **iter 20: Elo 2017** (winner, became ppo_best.pt)
- iter 60: Elo 1851
- iter 160: Elo 1810

This is a dramatic finding. The model was strongest at iter 20 and lost ~200 Elo over the remaining 180 iterations. The panel eval tells the same story -- avg panel WR peaked at iter 20 (0.589) and iter 60 (0.595), with later checkpoints degrading. The model is overtraining within each run.

The likely mechanism: with league self-play, the model becomes increasingly specialized at beating its own past checkpoints (PFSP WR against iter_0020 and similar pool members) while losing generalization against the fixed external opponents (v8, v14, v22, heuristic). By iter 100+, the policy has drifted substantially from the initial strong policy.

v45 at iter 130 shows a similar pattern: entropy has dropped to 4.2-4.3 from 4.24 at iter 1, rollout WR hovers around 0.40, and the PFSP WR against its own past checkpoints (iter_0060, iter_0090 etc.) is around 0.55-0.60 USSR / 0.24-0.34 US. The model is learning to beat itself but may not be getting stronger against external benchmarks.

### 2. Entropy Coefficient: Constant 0.03 for v44, Accidentally Decaying in v45

**v44**: Ran with constant `ent_coef=0.03` (no `--ent-coef-final` flag). W&B confirms this -- sparkline is flat. This matches v12-v22 era behavior where per-run linear decay was used, but v44 was manually launched without the decay.

**v45**: Launched by `ppo_loop_step.sh` with `--ent-coef 0.03 --ent-coef-final 0.005 --global-ent-decay-start 1 --global-ent-decay-end 200`. The source checkpoint (v44/ppo_best.pt = iter 20) contains `total_iters=20` in the `args` dict. However, this is **not** a PPO total_iters counter -- it is from the original BC training args (`epochs: 15` was the BC config). The PPO code reads `ckpt_args.get("total_iters", 0)` which returns 20, so `global_iter_offset=20`.

This means v45's decay schedule is:
- global_iter 21 (iter 1): ent_coef = 0.03 + (20/199)*(0.005-0.03) = 0.0275
- global_iter 120 (iter 100): ent_coef = 0.03 + (119/199)*(0.005-0.03) = 0.015
- global_iter 200 (iter 180): ent_coef = 0.005
- global_iter 220 (iter 200): ent_coef = 0.005

So v45 decays from 0.0275 to 0.005 over its run. This is **different from v44** (constant 0.03) and introduces a confound. If v45 outperforms v44, we won't know if it's from the decay or from continued training.

### 3. Policy Entropy Is High -- ent_coef=0.03 Resists Sharpening

v44 entropy trajectory:
- Iter 1: 4.084
- Iter 17: 4.214
- Iter 67: 4.385
- Iter 117: 4.348
- Iter 167: 4.484
- Iter 200: 4.539

Entropy **increased** over the run from 4.08 to 4.54. This is unusual for PPO -- normally entropy decreases as the policy sharpens. The constant `ent_coef=0.03` is actively pushing entropy up. With ~111 card choices, 5 modes, and 86 countries, maximum entropy would be ~ln(111)+ln(5)+ln(86) = 4.71+1.61+4.45 = 10.77. The current entropy of 4.5 is moderate but the trend is concerning -- it should be decreasing as the model learns, not increasing.

v45 entropy at iter 1 starts at 4.24 (from v44 iter 20 checkpoint, which had ent ~4.08) and rises to 4.3-4.4 by iter 130. Even with the accidental decay, entropy is still increasing.

The high entropy bonus likely explains why later iterations degrade: the entropy gradient overwhelms the policy gradient, pushing the model toward more uniform (weaker) play. Reducing ent_coef would let the policy sharpen.

### 4. KL and Clip Are Healthy -- No Instability

v44 metrics are stable throughout:
- clip: 0.05-0.10 (healthy, well below alarm threshold of 0.15)
- kl: 0.0018-0.0029 (very low, well below max_kl=0.3)
- policy_loss: -0.009 to -0.018 (negative = policy improving)

This means `lr=2e-5` and `clip_eps=0.12` are appropriate. There is room to increase the learning rate modestly (e.g., 3e-5) without instability, but this is not the bottleneck.

### 5. US-Side Play Remains Weak

Across both v44 and v45, the US side win rate against league opponents is consistently 0.22-0.36, while USSR side is 0.43-0.67. The panel eval confirms this asymmetry. v44 iter 20 vs v22: WR=0.509 combined but the USSR/US split is likely similar to rollouts.

This is a known TS asymmetry (USSR has structural advantages). However, the gap is large enough that targeted improvement on US play could yield significant Elo gains. UPGO would help here -- currently, most US-side trajectories produce negative advantages that anti-reinforce the policy.

### 6. PFSP Is Spending Too Much Time on Easy Self-Play

Looking at v44's PFSP weights:
- iter_0020: pfsp=0.600-0.625 (moderate difficulty)
- iter_0040: pfsp=0.648 (moderate)
- Fixtures (v8, v14, v22): pfsp=0.424-0.500 (easy)

The PFSP is dominated by self-play opponents with moderate difficulty. The external fixtures (v14 with pfsp=0.424 in v45) are actually EASY opponents that get deprioritized. Meanwhile, v22 -- the actual frontier -- doesn't appear as a PFSP opponent in most iterations because `league-fixture-fadeout=150` removes fixtures after iteration 150.

This means:
- After iter 150, the model trains exclusively against its own past checkpoints
- The hardest external benchmark (v22) is not seen in training after iter 150
- The model becomes increasingly specialized against itself

### 7. Architecture: 256-dim Trunk with 2 Residual Blocks

Current architecture: TRUNK_IN=320 -> 256-dim trunk -> 2 residual blocks -> heads. This is relatively small. The model has enough capacity for the current Elo range but may benefit from wider trunk (384 or 512) if other hyperparameter changes hit diminishing returns. However, architecture changes require restarting from scratch (BC training), which is expensive.

### 8. Comparison: v8->v22 Progression vs Current

The v8->v22 progression achieved ~11 Elo/generation over 15 generations:
- v8=1931, v12=2001, v14=2015, v19=2078, v22=2103
- Average: +11 Elo/gen, but decelerating to +6 Elo/gen by v19-v22
- Each run was 200 iterations, but the per-run decay from 0.03->0.005 meant later iterations had low entropy bonus

v44 at 2105 essentially matched v22 but did not meaningfully exceed it. The ceiling with T=1.0 + constant ent_coef=0.03 appears to be around Elo 2100-2110.

## Conclusions

1. **Runs are too long.** v44's best checkpoint was iter 20/200. The model peaks early then degrades through self-play drift. Shorter runs (60-80 iters) or more aggressive early stopping would preserve the peak.

2. **ent_coef=0.03 is too high for a mature policy.** Entropy increased throughout v44's run (4.08->4.54), meaning the entropy bonus is actively pushing the policy toward uniformity. This directly counteracts policy sharpening. The v12-v22 era used per-run decay to 0.005, which is why those runs improved -- they allowed sharpening in later iterations.

3. **The entropy decay is broken across the v44->v45 transition.** v44 used constant 0.03. v45 inherits `total_iters=20` from BC training args (not PPO), causing the global decay to fire from an incorrect offset. The decay schedule is not being managed consistently.

4. **PFSP + fixture fadeout creates a training bubble.** After iter 150, the model only trains against its own past checkpoints, losing the external signal from v22 and other fixtures. This contributes to late-run degradation.

5. **US-side weakness is a significant Elo lever.** US win rates of 22-36% in league play represent an exploitable gap. UPGO would selectively reinforce the rare US-side successes rather than anti-reinforcing the many failures.

6. **lr=2e-5 and clip_eps=0.12 are fine.** KL and clip metrics show no instability. These should not be changed.

7. **Dirichlet noise is premature.** The previous attempt (v23-v43) was confounded with the log_prob bug, but the current config has not been properly exploited. Add exploration noise only after fixing the entropy and run-length issues.

8. **Architecture changes are low ROI for now.** The 256-dim trunk is sufficient. Wider trunk would require BC retraining and is not the bottleneck.

## Recommendations

Ordered by expected impact. Each recommendation includes what to change, what to keep, and expected outcome.

### 1. Shorten runs to 80 iterations with aggressive early stopping (HIGH IMPACT)

**Change:** `--n-iterations 80` instead of 200. Consider adding panel-eval-based early stopping at iter 40+ if avg panel WR drops 2% below peak.
**Keep:** All other hyperparameters the same.
**Expected outcome:** Prevents the late-run degradation seen in v44. The best checkpoint will be closer to the final checkpoint, making the pipeline more efficient. Each run takes ~27 minutes instead of ~70 minutes, enabling faster iteration.

### 2. Reduce ent_coef to 0.01 with per-run decay to 0.003 (HIGH IMPACT)

**Change:** `--ent-coef 0.01 --ent-coef-final 0.003 --global-ent-decay-start 1 --global-ent-decay-end 80` (matched to the shorter 80-iter run).
**Keep:** lr=2e-5, clip_eps=0.12, PFSP, fixtures.
**Expected outcome:** Allows the policy to sharpen. Current entropy ~4.0-4.5 is maintained by the high entropy bonus; reducing it should let the policy specialize on high-value actions, improving both card selection and country targeting. This directly addresses the entropy-increase problem seen in v44. Risk: entropy collapse to <2.0 would indicate over-sharpening, but with ent_coef=0.01 (not 0.0) this is unlikely.

### 3. Remove fixture fadeout or extend to match run length (MEDIUM IMPACT)

**Change:** `--league-fixture-fadeout 999` (effectively no fadeout within an 80-iter run), or remove the flag entirely.
**Keep:** Fixtures v8, v14, v22, heuristic; PFSP exponent=1.0.
**Expected outcome:** Ensures the model always trains against external benchmarks, not just its own past checkpoints. This prevents the training bubble that causes late-run degradation.

### 4. Enable UPGO (MEDIUM IMPACT)

**Change:** `--upgo` flag.
**Keep:** GAE (gamma=0.99, lambda=0.95) for value function training; UPGO only affects policy advantages.
**Expected outcome:** Reduces variance in policy gradient, especially for US-side play where most trajectories are losses. Should improve US-side WR by 3-5 percentage points, which translates to ~10-20 Elo. Risk: UPGO can slow learning if the value function is accurate (because it discards informative negative signals). Monitor value_loss to check.

### 5. Fix the total_iters tracking for entropy decay (MEDIUM IMPACT, maintenance)

**Change:** In `ppo_loop_step.sh`, add explicit `--global-iter-offset-override` computed as `(finished_version_number - 44) * 80` or equivalent. Alternatively, fix the checkpoint saving to use a PPO-specific key (e.g., `ppo_total_iters`) that doesn't collide with BC training args.
**Keep:** The global decay schedule concept.
**Expected outcome:** Consistent entropy behavior across chained runs. Currently, the total_iters=20 inherited from BC args causes v45 to start decaying immediately from an incorrect offset.

### 6. Increase PFSP exponent from 1.0 to 2.0 (LOW-MEDIUM IMPACT)

**Change:** `--pfsp-exponent 2.0`
**Keep:** Everything else.
**Expected outcome:** Quadratically focuses training on hard opponents. Currently, opponents with WR=0.6 are only 1.5x more likely to be sampled than opponents with WR=0.9. With exponent=2.0, the ratio becomes 4x. This should improve the model's ability to handle its weakest matchups. Risk: training becomes noisier if the hard-opponent distribution is too narrow.

### 7. Add league-recency-tau=50 (LOW IMPACT)

**Change:** `--league-recency-tau 50` (from 20).
**Keep:** Everything else.
**Expected outcome:** With tau=20, recent checkpoints dominate the league pool even when PFSP would prefer an older, harder opponent. Increasing tau to 50 lets PFSP have more influence over opponent selection. Low risk.

### 8. Try UPGO + ent_coef=0.01 + 80-iter runs as v46 config (RECOMMENDED BUNDLE)

Combine recommendations 1, 2, 3, and 4 into a single experiment for v46:

```bash
nohup nice -n 10 uv run python scripts/train_ppo.py \
  --checkpoint data/checkpoints/ppo_v45_league/ppo_best.pt \
  --out-dir data/checkpoints/ppo_v46_league \
  --n-iterations 80 --games-per-iter 200 \
  --lr 2e-5 --clip-eps 0.12 \
  --ent-coef 0.01 --ent-coef-final 0.003 \
  --global-ent-decay-start 1 --global-ent-decay-end 80 \
  --max-kl 0.3 \
  --league data/checkpoints/ppo_v46_league \
  --league-save-every 10 \
  --league-mix-k 4 \
  --league-fixtures v8_scripted.pt v14_scripted.pt v22_scripted.pt __heuristic__ \
  --league-recency-tau 50 \
  --league-fixture-fadeout 999 \
  --league-heuristic-pct 0.0 \
  --pfsp-exponent 1.0 \
  --upgo \
  --eval-every 10 \
  --eval-panel v8_scripted.pt v14_scripted.pt v22_scripted.pt __heuristic__ \
  --rollout-workers 1 \
  --device cuda --wandb --wandb-run-name ppo_v46 \
  --reset-optimizer
```

Key changes from current config: 80 iters (not 200), ent_coef 0.01->0.003 (not 0.03->0.005), no fixture fadeout, UPGO enabled, eval every 10 iters (not 20), reset-optimizer for clean start.

### 9. Deferred experiments (for v47+, only if v46 succeeds)

- **Dirichlet noise**: `--dir-alpha 0.15 --dir-epsilon 0.15` (conservative). Only try after confirming the current config works without it.
- **Rollout temperature 1.05**: Very mild exploration. Only after confirming T=1.0 is baseline.
- **Wider trunk (384-dim)**: Requires new BC training. Only if hyperparameter changes plateau.
- **Learning rate warmup**: If reset-optimizer causes initial instability, add a 5-iter warmup from lr=5e-6 to lr=2e-5.
- **vp_reward_coef**: Currently 0.0 (only terminal reward). A small intermediate reward from VP changes (e.g., 0.01) could provide denser signal. Risk: reward shaping can distort the value function.

## Open Questions

1. **Why did v44 iter 20 peak so early?** Is this because the model quickly adapts to the PFSP opponents (which are just copies of itself from 1-20 iters ago) and then overfits? Or does the optimizer state (freshly reset) provide an initial boost that fades as momentum accumulates?

2. **Should we keep `--reset-optimizer` for every new run?** v44 used it and peaked at iter 20. If optimizer momentum is harmful, resetting every 80 iters (via ppo_loop_step.sh) would provide a natural "annealing" cycle.

3. **What is the theoretical Elo ceiling for the current architecture (256-dim, 2 residual blocks)?** The v8-v22 progression shows ~170 Elo of improvement from RL alone. Is there evidence this has saturated, or was the v22-v44 gap purely due to config bugs?

4. **Is the per-side advantage normalization correct?** US-side games consistently produce lower raw advantages (more losses). Normalizing per-side means US advantages are scaled up relative to USSR. This is theoretically correct but could amplify noise on the minority side.

5. **Would separate value heads for USSR and US improve the value function?** The current single value head must learn both sides' value functions. A side-conditioned value head might improve the quality of GAE advantages.

6. **At what Elo does the heuristic opponent stop providing useful training signal?** Current heuristic WR is 83-91%. Once it exceeds ~95%, heuristic games are pure noise. Consider removing heuristic from fixtures when the model consistently beats it >90%.
