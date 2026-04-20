# Opus Analysis: v9 Failure and v10 Plan
Date: 2026-04-20 UTC
Question: Why did v9 fail (combined=0.304) and what should v10 do?

## Executive Summary

**v9 is the fourth consecutive failed PPO run started from v6_iter20, and the first clean evidence that the dense-reward knob is not the primary strength lever we need.** Formal 500g/side bench at iter60 (the KL-aborted run's terminal checkpoint) gives combined=0.304 (USSR=0.430, US=0.178) — 15.4pp below the v6_iter20 record of 0.458, 13.7pp below v56 baseline, and 4.7pp below even v8's failed 0.351. The KL abort at iter63 is the tail of a process that began at iter 1: v9 ran ~30-50% hotter JSD vs BC than v6 at matched iterations (iter10 JSD=0.057 vs 0.039; iter60 JSD=0.106 vs 0.084), with value_mae consistently ~0.04 higher (0.30 vs 0.26 at iter10, 0.33 vs 0.28 at iter60). Dense reward shifted the value target distribution, value head lagged, advantages became noisier, policy drifted off BC faster than it could be stabilized by PPO clipping. But the **deeper pattern is not dense reward** — it is that **every run warmstarted from v6_iter20 has failed** (v7, v7-restart, v8, us_overfit_v1, v9), across four different recipes (stable fadeout; pool trim; floor=0.30; dense reward). The one run that succeeded — v6 itself — warmstarted from v56 with a schema-mismatched partial warm-start (scalar_encoder 74→82), which effectively reset part of the encoder. v6_iter20 is likely a narrow local optimum on the v56→v6 trajectory that PPO cannot escape without breaking. **v10 should revert to the v6 recipe (v56 warmstart + reset-optimizer + no dense reward) on a fresh seed, not tweak dense reward further.** Option C (teacher distillation on hard US positions) becomes the parallel lever for advancing beyond v6_iter20, since RL alone has now been falsified four ways at this checkpoint.

## Root Cause Analysis

### Evidence 1: v6_iter20 record is reproducible
Re-bench on seed 60000/60500 (`results/ppo_country_attn_v6/bench_iter20_500g_s60000.json`):
- USSR WR = 0.570, US WR = 0.348, combined = 0.459

Within 0.001 of the original seed 50000/50500 bench (0.458). The record is real, not seed noise. This matters because it means the v9 regression (combined=0.304) is a genuine 15.5pp loss from a stable baseline, not a comparison against a lucky-seed artifact.

### Evidence 2: v9 destabilized from iter 1, not just at iter63
Matched comparison v6 vs v9 (same warmstart for v9 = v6_iter20 checkpoint; v6 = v56 warmstart):

| Metric | v6_iter10 | v9_iter10 | v6_iter60 | v9_iter60 |
|---|---|---|---|---|
| KL (rollout) | 0.0057 | 0.0070 | 0.0089 | 0.0109 |
| JSD vs BC (card) | 0.0389 | 0.0571 | 0.0841 | 0.1060 |
| val_mae vs BC | 0.2572 | 0.2958 | 0.2813 | 0.3271 |
| Rollout WR (US) | 0.220 | 0.250 | 0.310 | 0.310 |
| Panel avg | 0.405 | 0.562 | (no eval) | 0.500 |

v9's policy was measurably further from BC, with higher value-head error, higher per-iteration KL, and higher clip-fraction than v6 at every matched iteration. The KL=0.1044 abort at iter63 is the statistical tail of a consistently elevated distribution, not a sudden late explosion.

### Evidence 3: Dense reward hurts monotonically with training
v9 iter-60 JSD vs BC = 0.106 ≈ v6 iter80 JSD vs BC = 0.1049. **v9 reached v6's iter80 BC-distance 20 iters early.** Dense reward is adding gradient signal that pushes the policy off its BC-compatible manifold faster than PPO clipping can contain. At alpha=0.3 with anneal over 250k steps (~iters 0-30 of training), the effect is strongest exactly when the policy is closest to v6_iter20 and most vulnerable to drift.

The dense-reward function (`_apply_dense_vp_rewards`) adds per-step `alpha * anneal * delta_vp / 20` to rewards. Magnitude is modest (0.3 * 1.0 * 1.0/20 = 0.015 per VP-scoring event), and cumulative dense reward over an episode is bounded by (final_vp - initial_vp)/20 * alpha ≈ 0.15 for typical 10-VP games. That's small relative to terminal ±1.0. The problem is not magnitude — it is **temporal redistribution**: the value head trained on sparse terminal-only rewards now has to learn a per-step shape, and the MAE vs BC value estimates (which use the same sparse target) grows. Noisier advantage estimates → larger and more directional policy updates → faster drift.

### Evidence 4: The KL climb pattern
v9 per-iteration KL: iters 1-10 mean 0.0065, iters 31-50 mean 0.0082, iters 51-62 mean 0.0084. Not a monotone climb, but a persistent elevation ~40% above v6's matched iters (v6 iters 1-10 mean 0.0057, iters 51-62 mean 0.0079). The iter63 KL=0.1044 is 12× the recent mean — that's not a gradual creep, that's a single-update outlier (probably one minibatch with large advantage magnitude triggering a large update). `--target-kl 0.015` should have triggered per-epoch early-stop before this (the configured threshold), but `--max-kl 0.1` is the run-level abort that fired. The iter63 outlier is opportunistic noise amplified by the hotter baseline KL regime dense reward created.

### Evidence 5: Rollout-vs-bench gap is structural, not recipe-specific
v9 rollout_wr (iters 10-60 mean) ≈ 0.46; bench combined = 0.304. Gap = 0.156. v8 had gap ≈ 0.05. us_overfit_v1 had gap 0.415. The gap direction is always the same: rollout overstates bench. The mechanism, already correctly identified in the v8 analysis, is that rollout opponents include self-similar past selves and BC-cluster fixtures which are systematically easier for the learned policy than heuristic — especially on the weaker side (US). Dense reward did not cause this gap; it is a general selection effect of PFSP-weighted league pools with only ~12-15% heuristic share. v9's gap of 0.156 is within the range observed across v7/v8, not a new symptom.

## v6→v9 Regression Pattern

Every PPO run warmstarted from v6_iter20 has failed:

| Run | Warmstart | Reset-opt | Dense reward | Other changes | Result |
|---|---|---|---|---|---|
| v6 | v56 (partial warm-start 74→82) | YES | 0.0 | fadeout=50 bug | **iter20=0.458 (record)**, iter80=0.270 (collapsed) |
| v7 | v6_iter20 | YES | 0.0 | fadeout=999 fix | iter80=0.423 (−3.5pp) |
| v7-restart | v7_iter13 | NO (kept) | 0.0 | --max-kl 0.1 (raised from 0.03) | part of v7 |
| v8 | v6_iter20 | YES | 0.0 | floor=0.30, trimmed fixtures | iter80=0.351 (−10.7pp) |
| us_overfit_v1 | us_only_v5 | YES | 0.0 | side=US, trimmed fixtures, floor=0.30 | iter40=0.212 (−24.6pp from us_only_v5) |
| **v9** | **v6_iter20** | **YES** | **0.3** | full pool, floor=0.15 (v6/v7 config + dense) | **iter60=0.304 (−15.4pp)** |

Key observations:
1. **--reset-optimizer is NOT the discriminator.** v6 used it and won. v7/v8/v9 used it and lost. Not causal.
2. **The discriminator is the warmstart source.** v6 started from v56 with a schema mismatch (partial warm-start reset part of scalar_encoder). Every direct warmstart from v6_iter20 has failed, regardless of hyperparameters.
3. **Dense reward is a secondary amplifier, not the primary cause.** v8 (no dense reward) failed too, just slightly less catastrophically. v9 (dense reward) failed worse.
4. **v6_iter20 is likely a narrow local optimum** on the v56→v6 policy-space trajectory. It reached 0.458 because v6's partial-reset allowed the policy to find a new minimum with structurally different value estimates and card logits. PPO restarted from v6_iter20 cannot re-find an escape because it is already at a tight local basin — small updates stay inside the basin (no progress), large updates flip it over the edge into a worse basin.

A cleaner test of the "v6_iter20 is a trap" hypothesis would be: v6-config starting from v56 (not v6_iter20), on a fresh seed. If that also lands at 0.43-0.46, the v6 recipe is repeatable and v6_iter20 is a stable baseline we can build distillation on top of. If it lands at 0.30-0.35, then the v6_iter20=0.458 outcome was partially seed luck on a volatile recipe, and we need a different tool entirely (Option C).

## v10 Recommendation

**Do NOT launch v10 = v9 with smaller dense-reward alpha or longer anneal.** The falsification pattern is broader than dense reward; tweaking that single knob tests only a narrow hypothesis and leaves three others unexamined.

**Primary recommendation: v10 = v6 recipe replay from v56 warmstart, different seed.**

Rationale:
- Tests whether v6 recipe is reproducible (repeat the only known success).
- Gives us a second v6-shaped policy at a different seed we can compare against v6_iter20 to check seed variance on this recipe (currently N=1).
- If v10 lands at 0.44-0.46, we have TWO independent champions and can candidate-tournament them → better Elo anchoring; the "0.458 record" becomes a distribution, not a point estimate.
- If v10 regresses to 0.30-0.35, the v6 recipe is seed-volatile and 0.458 was partially luck; pivot hard to Option C.
- Cheap: 25-40 min, no novel code, no new hyperparameter search. Most efficient next experiment in the expected-information-per-minute sense.

**Parallel recommendation (not alternative): launch Option C teacher distillation as soon as v10 finishes.**

After four failed PPO runs from v6_iter20, RL alone cannot advance this checkpoint. Option C (teacher search on ~100 US-side hard positions from v6_iter20 games, shallow MCTS 30 sims, KL-regularize US policy 5-10 iters from v6_iter20) is a qualitatively different gradient signal. It should be run regardless of v10's outcome, because:
- If v10 succeeds: we have two v6-like models + distillation targets, and we can compare RL-alone (v10) vs RL+distill (v10+C) head-to-head.
- If v10 fails: we have clear evidence RL is stuck, and distillation is the only remaining Month-3 strength lever per CLAUDE.md priority list.

**Do NOT re-run a variant of v7/v8/v9 recipe.** Three of those have already been falsified. Stop adding knobs to that recipe.

### Specific parameter changes from v6 → v10

Almost none. v10 is nearly a pure v6 replay with three small changes to improve observability:

| Param | v6 | v10 | Why |
|---|---|---|---|
| Warmstart | data/checkpoints/ppo_v56_league/ppo_best_6mode.pt | same | replay |
| reset-optimizer | yes | yes | same |
| dense-reward-alpha | 0.0 | 0.0 | no dense reward |
| Panel | v56, heuristic | v56, heuristic | same as v9 |
| eval-every | 20 | 10 | match v9 (finer selection signal) |
| seed | 42000 | 45000 | noise isolation |
| league-fixture-fadeout | 50 | 999 | v6's 50 caused self-play collapse past iter 50; use v7+ value |
| max-kl | 0.03 | 0.1 | don't abort on transient spikes; v7/v8/v9's 0.1 was fine |

Fadeout=999 is the one "non-trivial" change, but it's a bug-fix proved necessary by v6's own post-iter-50 collapse (iter80=0.270). v7 introduced it; we keep it. Everything else is v6-exact to avoid introducing confounds.

### Success criteria for v10
- **iter 20 combined ≥ 0.44**: v6 recipe reproducible (within noise of v6_iter20=0.458).
- **iter 40 combined ≥ 0.42**: matches v6 post-iter-40 performance (v6_iter40=0.307 was fadeout-broken; v10 with fadeout=999 should stay higher).
- **iter 80 combined ≥ 0.42**: holds past the v6 fadeout cliff.

### Abort criteria for v10
- iter 20 combined < 0.38 → v6 recipe is seed-volatile, pivot immediately to Option C. Kill v10.
- KL > 0.1 for two consecutive iters → same as v9 symptom, indicates v56 warmstart itself is unstable now; pivot to Option C.

## Option C (Teacher Distillation) Assessment

Option C should be launched **in parallel with v10**, not as a fallback. Reasons:

1. **RL has been falsified four times at v6_iter20.** Adding a fifth PPO variant from v6_iter20 is low expected value. Distillation adds orthogonal information (off-policy supervised targets from search) and is the only remaining strength lever in the CLAUDE.md Month-3 priority list besides Dirichlet noise / ISMCTS (shelved per `project_ismcts_verdict.md`).

2. **Cheap to set up.** Mining 100 US-side hard positions from v6_iter20 games is 30-60 min. Shallow MCTS at 30 sims/position with heuristic rollouts is ~1-2 hrs on the existing MCTS infrastructure. KL-regularized fine-tuning for 5-10 iters is 30 min. Total ~3 hrs of work.

3. **"Hard positions" definition**: positions where v6_iter20's US-side value_mae was highest, OR positions where v6_iter20's top-1 action was different from a small teacher-search result (disagreement positions), OR simply US-side actions in the first 3 ARs (opening is a known weakness from the US WR=0.334 bench).

4. **Regularization**: KL-regularize against v6_iter20 (NOT against BC/v56), with KL coefficient β~0.1-0.3. Student = v6_iter20, target = MCTS action distribution. Update US head only; USSR head frozen. This avoids the USSR-regression-while-fixing-US failure mode we saw in v7/v8.

5. **Pre-committed success criterion**: US vs heuristic at post-distillation bench ≥ 0.40 (+6.6pp vs v6_iter20's 0.334, +4pp vs us_only_v5's 0.360). If yes, combined will likely be ≥ 0.48 (new record). If no, distillation did not improve US-side; try harder search (100 sims, 200 positions) or different position-mining strategy.

**v10 (pure v6 replay) runs first in Bash (cheap, fast, isolates v6 reproducibility).** Option C spec should be drafted while v10 runs, and launched the moment v10 completes iter 20 regardless of whether v10 succeeds or fails.

## Conclusions

1. **v9 failed at combined=0.304, the worst of all v7-v9 runs.** Primary driver: dense reward amplified a preexisting instability in v6_iter20-warmstarted PPO runs.

2. **Dense reward caused measurable policy drift from BC.** v9 reached v6's iter80 JSD in only 60 iters. Value MAE stayed elevated throughout training. KL was ~30-50% hotter than matched v6 iters from iter 1 onward, eventually triggering the --max-kl abort.

3. **The deeper pattern is that v6_iter20 is PPO-toxic.** Four consecutive PPO runs from v6_iter20 across four different recipes have all failed. --reset-optimizer is not the discriminator (v6 used it and won). Dense reward is not the primary cause (v8 failed without it). The discriminator is the warmstart source: v56 (with partial schema-mismatch reset) → works; v6_iter20 (loaded intact) → fails.

4. **v6_iter20 record is confirmed reproducible.** Seed 60000/60500 bench = 0.459 combined vs original seed 50000/50500 = 0.458. Not seed noise.

5. **v10 should be a v6 replay**: v56 warmstart + reset-optimizer + NO dense reward + fadeout=999 (keep the one bug fix) + different seed. Primary purpose: test whether v6 recipe is reproducible and whether 0.458 is typical or lucky.

6. **Option C teacher distillation should launch in parallel, not as fallback.** RL from v6_iter20 has been falsified four times; supervised off-policy search targets are the only remaining orthogonal lever.

7. **Do not launch a fifth PPO variant from v6_iter20 with a knob tweaked.** The falsification pattern is broader than any single knob.

## Exact v10 Launch Command

```bash
mkdir -p results/ppo_country_attn_v10

OMP_NUM_THREADS=6 KMP_BLOCKTIME=0 nohup uv run python scripts/train_ppo.py \
  --checkpoint data/checkpoints/ppo_v56_league/ppo_best_6mode.pt \
  --reset-optimizer \
  --out-dir results/ppo_country_attn_v10 \
  --version country_attn_v10 \
  --n-iterations 80 \
  --games-per-iter 200 \
  --ppo-epochs 4 \
  --clip-eps 0.12 \
  --lr 5e-5 \
  --lr-schedule constant \
  --lr-warmup-iters 0 \
  --gamma 0.99 --gae-lambda 0.95 \
  --ent-coef 0.01 --ent-coef-final 0.003 \
  --global-ent-decay-start 0 --global-ent-decay-end 300 \
  --vf-coef 0.5 --val-calib-coef 0.1 \
  --minibatch-size 2048 \
  --eval-panel \
    data/checkpoints/scripted_for_elo/v56_scripted.pt \
    __heuristic__ \
  --eval-every 10 \
  --side both \
  --self-play-heuristic-mix 0.2 \
  --seed 45000 --device cuda \
  --wandb --wandb-project twilight-struggle-ai \
  --wandb-run-name ppo_country_attn_v10_v6replay \
  --ema-decay 0.995 --target-kl 0.015 \
  --reward-alpha 0.5 \
  --dense-reward-alpha 0.0 \
  --league results/ppo_country_attn_v10 \
  --league-save-every 10 \
  --league-mix-k 6 \
  --rollout-workers 1 \
  --league-fixtures \
    data/checkpoints/scripted_for_elo/v56_scripted.pt \
    data/checkpoints/scripted_for_elo/v55_scripted.pt \
    data/checkpoints/scripted_for_elo/v54_scripted.pt \
    data/checkpoints/scripted_for_elo/v44_scripted.pt \
    data/checkpoints/scripted_for_elo/v20_scripted.pt \
    results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
    results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
    __heuristic__ \
  --heuristic-floor 0.15 \
  --league-recency-tau 20.0 \
  --league-heuristic-pct 0.0 \
  --league-fixture-fadeout 999 \
  --league-self-slot \
  --pfsp-exponent 0.5 \
  --dir-alpha 0.0 --dir-epsilon 0.25 \
  --upgo \
  --jsd-probe-path data/probe_positions.parquet \
  --jsd-probe-interval 10 \
  --jsd-probe-bc-checkpoint data/checkpoints/ppo_v56_league/ppo_best_6mode_scripted.pt \
  --rollout-temp 1.0 \
  --max-kl 0.1 \
  --skip-smoke-test \
  > results/ppo_country_attn_v10/train.log 2>&1 &
```

### Rationale for each change from v6 original
- **--checkpoint v56 (not v6_iter20)**: Test v6 recipe reproducibility. Every run from v6_iter20 has failed; we need a known-good warmstart. v56 + partial warm-start 74→82 is the only winning configuration.
- **--dense-reward-alpha 0.0**: v9's new intervention is reverted. Dense reward amplified BC drift and value MAE; not worth keeping until we have a stable baseline.
- **--eval-every 10**: Match v9 for finer-grained selection signal (v6 had 20, but eval runs are cheap).
- **--league-fixture-fadeout 999**: Keep the one v6→v7 bug fix. v6's fadeout=50 caused self-play echo chamber past iter 50; v10 should not recreate that bug.
- **--seed 45000**: Isolate from v6 (seed 42000), v7 (43000), v8 (43000 different branch), v9 (44000). Fresh noise draw to test seed variance on v6 recipe.
- **--max-kl 0.1**: Keep the permissive KL abort that v7/v8/v9 used. v6 had --max-kl 0.03 which is too strict (would abort frequently). If v10 needs early stopping, --target-kl 0.015 will do per-epoch early-stop inside each iter.
- **Full 8-fixture league pool**: Same as v6/v7/v9. v8's trimmed 4-fixture pool was falsified.
- **heuristic-floor 0.15**: Same as v6/v7/v9. v8's 0.30 was falsified.

### Early observation checklist (what to watch in the first 20 iters)
- **iter 10 JSD vs BC**: should be ~0.04 (match v6_iter10 = 0.0389). If > 0.06, policy is destabilizing — same v9 pattern.
- **iter 10 val_mae vs BC**: should be ~0.26 (match v6_iter10 = 0.2572). If > 0.30, value head unstable.
- **iter 10 KL**: should be ~0.006. If > 0.010, too hot.
- **iter 20 combined (from panel)**: should be 0.43-0.50 range. If < 0.40, v6 recipe failed to reproduce → abort and launch Option C.

## Open Questions

1. **Is the v6_iter20 checkpoint itself deterministic across torch versions?** The partial warm-start code path from v56→v6 (scalar_encoder 74→82) may depend on initialization RNG, torch version, or CUDA kernel non-determinism. If v10 from v56 on a fresh env produces a different partial-warm-start pattern, the "v6 recipe" may not even be reproducible at the model-weight level. Verify by loading v56 → running load_model with partial warm-start → saving a diff of initial weights vs v6's iter_0001.pt. Cheap check.

2. **Can dense reward be made safe with smaller alpha?** v9 used alpha=0.3 which was too aggressive. A follow-up v11 could try alpha=0.05 over a longer anneal (500k steps) if v10 succeeds and we have a stable baseline. But this is not a v10 question — premature to optimize a knob when the recipe is unstable.

3. **Is the value head's instability specifically the problem?** v9 had val_mae=0.33 at iter60 (vs v6=0.28). If we added a value-head-only warmup phase (5-10 iters freezing policy, training value only), dense reward might become safer. Research direction for v11+ if v10 succeeds.

4. **For Option C, which positions to mine?** Leading candidates:
   - (a) US-side positions where v6_iter20 lost games vs heuristic (directly target failures)
   - (b) US-side positions in turns 1-3 (opening weakness hypothesis)
   - (c) US-side positions with high v6_iter20 value MAE on its own rollouts (self-disagreement between policy and value heads)
   - Suggest (a) as default — most targeted.

5. **Is the rollout_wr vs bench gap a deal-breaker for any future RL?** All four failed runs had this gap. If it is fundamental to PFSP+self-similar opponents, every future RL iter will overstate performance. Mitigations from v8 analysis (dedicated heuristic-only 200g bench every 10 iters) should be implemented regardless of v10/v11 outcome — it is an orthogonal infrastructure fix.

6. **Should we candidate-tournament v6_iter20 against v10_iter20 if both finish at ~0.45?** Yes — two checkpoints at similar heuristic WR but different training trajectories will have different Elo-vs-BC-cluster signatures. Running the full candidate_tournament gives us the best Elo anchor for Month-3 reporting.
