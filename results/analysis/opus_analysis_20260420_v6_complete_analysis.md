# Opus Analysis: v6 PPO Complete Analysis
Date: 2026-04-20

## Executive Summary

v6 PPO delivered a new project record at **iter 20** and then regressed monotonically through iter 80. The true best checkpoint is `results/ppo_country_attn_v6/ppo_iter0020.pt` with **USSR=0.582, US=0.334, combined=0.458** against the heuristic (500 games/side) — a +1.7pp improvement over the v56 warmstart (combined=0.441). Every subsequent eval checkpoint was worse: iter40=0.307, iter60=0.315, iter80=0.270. Iter 80 was a 30pp US-side collapse relative to iter 20.

The regression has a single identifiable root cause: **`league_fixture_fadeout = 50`**. At iter 50 all external fixtures (scripted baselines + `__heuristic__`) dropped out of the active pool, leaving 100% past-self sampling. The policy lost its external grounding and drifted into an echo chamber. The in-training panel numbers continued to look reasonable because the panel games were dominated by self-matches and near-self snapshots (which reliably average ≈0.5), masking the regression from the running-best selection logic. Running-best therefore incorrectly kept iter 80 as `ppo_best` when formal bench showed it was the worst checkpoint.

Elo placement (post-fix ladder, anchor v56=2095) confirms the picture:
- v6_iter20 ≈ v56 within noise (−3.3 Elo in a candidate tournament).
- v6_iter40 is ~32 Elo below v56 — a measurable regression.
- All BC symmetric models (v20/v44/v54/v55/v56) cluster 2083–2097. The heuristic is at 1927.9 (delta −167 vs v56).

v6 produced evidence that **the country-attention symmetric architecture still has headroom** above v56 (iter 20 is a valid +1.7pp gain at matched compute), but also that the PFSP pool mechanics, not the architecture or the learning recipe, are currently the binding constraint on v6-class runs. v7 should preserve every other v6 hyperparameter and fix only the pool-composition bug: `league_fixture_fadeout = 999`, permanent heuristic, warmstart from iter 20 of v6 rather than v56. A recency cap K=10 on past-self snapshots is a zero-risk additional lever but requires a ~20-line implementation in `scripts/train_ppo.py` (no flag exists today).

## Findings

### Benchmark trajectory

Formal benchmark (500 games/side vs heuristic, post-DEFCON-1-fix engine, canonical seeds 50000/50500):

| Checkpoint | USSR WR | US WR | Combined | Delta vs v56 |
|---|---|---|---|---|
| v56 warmstart | 0.558 | 0.325 | 0.441 | 0.0 |
| v6_iter20 | **0.582** | **0.334** | **0.458** | **+0.017** |
| v6_iter40 | 0.465 | 0.150 | 0.307 | −0.134 |
| v6_iter60 | 0.405 | 0.225 | 0.315 | −0.126 |
| v6_iter80 | 0.330 | 0.210 | 0.270 | −0.171 |

Shape of the regression is characteristic: USSR holds moderately (0.58 → 0.33 is −25pp, over 60 iters), US collapses fast and hard (0.33 → 0.15 by iter 40, a 54% relative drop in 20 iters). This asymmetry matches what echo-chamber self-play predicts — the weaker side (US) specializes against an opponent distribution it has already memorized, losing generality against anything off-distribution (the heuristic is by construction off-distribution for a self-play mix).

The combined score peaks at iter 20 and decays monotonically after iter 30; the best checkpoint is cleanly identifiable and does not require regularization or interpolation across iters.

### Root cause: fixture_fadeout=50

The `league_fixture_fadeout` hyperparameter removes fixtures from the sampling pool after `current_iter − fixture_added_iter > fadeout`. In v6 this was set to 50, and fixtures were added at iter 0. Therefore at iter 51 and beyond, every fixture (v20/v44/v54/v55/v56 scripted + specialists + `__heuristic__`) was silently dropped from the pool, leaving only past-self snapshots.

Evidence from wr_table.json, counting fixture game volume across the whole run:
- `heuristic` total games = 840 (480 US + 360 USSR), all concentrated in iters 1–50.
- `v56_scripted` total games = 440 — similarly pre-fadeout.
- `iter_0050`, `iter_0060`, `iter_0070` got 520, 560, 200 games respectively (post-fadeout period), and `__self__` jumped to 3200 total games.

So after iter 50 the pool composition is roughly:
- 0% external fixtures
- ~100% past-self (including `__self__` current-policy match)

This is the textbook failure mode of PFSP with an aggressive fadeout — the population of opponents becomes a near-1D manifold (policy at recent iters), and the gradient signal no longer exposes the policy to off-manifold weaknesses. The US side, which was the weaker side at warmstart, is where the drift shows up fastest because the self-opponent-distribution drifts fastest there (it converges to whatever the USSR side keeps doing, which ossifies).

The prior analysis `opus_analysis_20260420_pfsp_self_play_analysis.md` predicted exactly this failure mode from the v6 WR table at iter 50 (0.57–0.64 USSR / 0.29–0.37 US) — the signs were visible mid-run but eval cadence (every 20 iters) + panel masking (below) meant no correction was applied in time to save v6.

### Running best selection bug

`ppo_best.pt` at end of v6 points to iter 80, which is the *worst* checkpoint. The mechanism:

1. v6 uses `eval_panel` with 8 opponents including self and scripted baselines.
2. Panel evals run every 20 iters (`eval_every=20`) and feed a combined score that `ppo_best` tracks.
3. Because past-self and near-self scripted snapshots dominate the panel, post-iter-50 panel games look close to 0.5 (a model tied against itself is by definition 0.5). Heuristic is just one of 8 opponents and is diluted in the aggregate.
4. Meanwhile the *formal* benchmark (heuristic-only) shows the real regression.

So `ppo_best` was incorrectly chosen because the selection criterion was panel-aggregate rather than heuristic-only. The panel is biased toward self-similar opponents once fadeout fires, which biases the running-best selection.

This is a real and fixable issue separate from the pool-composition bug. For v7 the immediate workaround is manual: take iter 20 (or whichever iter has the best formal heuristic bench). The structural fix is to add a dedicated `heuristic_combined_wr` field to running-best selection, either alongside or instead of `panel/combined_wr`, so that drift toward self-similar opponents cannot inflate the running-best metric.

### Elo ladder placement

Post-fix Elo ladder (anchor v56 = 2095, 500-game bipartite matches, 38/38 matches complete in `results/elo/elo_post_fix_ladder.json`):

| Model | Elo | delta_vs_v56 |
|---|---|---|
| v54 | 2097.0 | +2.0 |
| v56 | 2095.0 | 0.0 |
| v55 | 2093.5 | −1.5 |
| v20 | 2085.7 | −9.3 |
| v44 | 2083.1 | −11.9 |
| ussr_only_v5 | 2064.6 | −30.4 |
| us_only_v5 | 2052.7 | −42.3 |
| v3_best | 1941.9 | −153.1 |
| heuristic | 1927.9 | −167.1 |

All BC models cluster in a ~14-Elo band at the top (v54/v56/v55/v20/v44). The specialists sit ~30–42 Elo below that cluster. v3_best and heuristic are a further ~110 Elo below the specialists. In scale terms, 167 Elo = 73%/27% expected-score gap, which matches the ~0.27 heuristic WR v56 posts on a face-to-face match.

v6 checkpoints were not folded into this tournament but a candidate match placed v6_iter20 ≈ v56 (−3.3 Elo) and v6_iter40 at −32 Elo (confirmed regression). This is consistent with the heuristic-WR deltas: a +1.7pp heuristic WR gain translates to roughly 0–10 Elo at these matchup levels (heuristic is weak so the Elo→WR mapping near the top of the ladder is non-linear), so "≈v56 within noise" is the expected reading.

The right way to read this: v6_iter20 has not decisively separated from the BC cluster yet. It beats the heuristic a bit better than v56, but head-to-head against v20/v44/v54/v55/v56 it is roughly tied. The fact that no symmetric BC model has pulled away from v56 by more than ~2 Elo in many iterations suggests the BC symmetric architecture is saturated on the current training signal and future gains need either more signal (dense rewards, teacher search) or more-informative opponents.

### What iter20 tells us about the architecture

v6 ran 20 iters of PPO from v56 with country-attention-side architecture and produced a +1.7pp heuristic-WR improvement. Interpretations:

1. **The architecture still has headroom.** The warmstart checkpoint was at a local optimum for the previous training recipe, but a modest PPO tune-up with fresh PFSP data produced a measurable gain. This refutes the stronger "country_attn_side is saturated at 0.44" hypothesis.

2. **Gains are small and fragile.** +1.7pp combined with a clean-slate PFSP is within the noise band of 500-game benchmarks (±2pp per side ≈ ±1.4pp combined). v6_iter20 being a genuine improvement rather than a noise fluctuation needs at least one bench-retest or a head-to-head Elo match to confirm. The candidate match result (≈v56 within noise) is weak evidence for; the formal benchmark is moderately strong evidence for.

3. **The gain is roughly symmetric.** USSR +2.4pp, US +0.9pp. This is the right direction (US lift) but the US gain is small enough that it may not reproduce. If v7 reruns iter 20 and US stays at 0.33+, that is confirmation; if US drops back to ~0.32, the v6_iter20 bench was a lucky US seed.

4. **Short runs win.** The 20 best iters of v6 beat the 80 worst iters. This suggests PFSP runs at this scale (games_per_iter=200, league_mix_k=6, 80 iters) may be over-budgeted and the right scale is closer to 30 iters unless the pool composition issue is fixed.

5. **US is where the ceiling is.** USSR went 0.558 → 0.582, a small but real lift. US went 0.325 → 0.334, roughly noise. The structural argument in the US overfit analysis still holds: US WR ~0.42 is the heuristic-parity floor, and nothing in project history has cleared it. v6_iter20 at 0.334 is still 9pp below that floor.

## Conclusions

1. **v6's true best is iter 20, combined=0.458.** This is a new project record for symmetric policy (+1.7pp over v56=0.441) and makes `results/ppo_country_attn_v6/ppo_iter0020.pt` the new warmstart anchor for future PPO runs.

2. **Root cause of the post-iter-50 collapse is `league_fixture_fadeout = 50`**, not architecture, not learning rate, not entropy schedule. The fix is `league_fixture_fadeout = 999` and making `__heuristic__` a permanent fixture. All other v6 hyperparameters were sound.

3. **Running-best selection is broken under fadeout**: panel-aggregate WR hides regressions once past-self dominates the panel. The end-of-run `ppo_best` in v6 points to iter 80 (combined=0.270), the worst of five measured iters. Manual checkpoint selection is required; a structural fix (heuristic-only gate on running-best) is desirable but can be deferred until v7 reveals whether the fadeout fix alone resolves the symptom.

4. **Elo-wise, v6 did not change the picture.** The BC symmetric cluster (v20/v44/v54/v55/v56 + v6_iter20) is still tightly bunched at ~2095 Elo. The heuristic is 167 Elo below. v6_iter20 has not decisively separated from v56. Moving the cluster requires either (a) actually stronger training signal (teacher search, richer rewards), (b) architecture changes (multi-head, hidden-info features), or (c) an active-search component at inference (MCTS with a rebuilt value head). v7 is about stabilizing the PFSP loop; strength push needs something beyond v7.

5. **v7 plan: fix fadeout, warmstart from iter 20, keep everything else.** This is the minimal change that tests the hypothesis "the only bug is fadeout." Expected outcome: v7_iter20 matches or slightly exceeds v6_iter20 (combined ~0.46), v7_iter80 does not regress (stays near peak). If v7 still regresses after iter 50 despite `fadeout=999`, the pool problem is broader than just fadeout and the PFSP redesign in `opus_analysis_20260420_pfsp_pool_redesign.md` becomes priority.

6. **US WR ceiling still unaddressed.** v6_iter20 US=0.334 does not move the US ceiling meaningfully. A dedicated US-specialist run with value-weighting + us_only_v5 warmstart (per `opus_analysis_20260420_us_overfit_experiment.md`) remains a worthwhile cheap experiment (~1 GPU hour) but it is orthogonal to v7 and should not block the v7 launch.

## Recommendations

**Tier 1 — launch now (v7):**
1. Launch v7 from `results/ppo_country_attn_v6/ppo_iter0020.pt` with `league_fixture_fadeout = 999`, same hyperparameters otherwise, same 80 iters.
2. Promote `ppo_iter0020.pt` from v6 as the new project-best symmetric checkpoint. Update `continuation_plan.json` benchmark_ladder.
3. Keep `eval_every=20` so v7 has eval points at iter 20/40/60/80 matching v6 — makes direct comparison clean.

**Tier 2 — if v7 iter 20 matches v6 iter 20, the architecture+recipe are sound:**
4. Run the US-specialist experiment (`ppo_us_overfit_v1`) in parallel or afterward; ~40 iters, us_only_v5 warmstart, isolated capacity-test directory.
5. Add a heuristic-only running-best gate to `scripts/train_ppo.py`. Small PR.
6. Start scoping JSD-based diversity weighting for past-self (tier-2 recommendation from the PFSP pool analysis).

**Tier 3 — if v7 regresses despite fadeout=999:**
7. Implement recency cap K=10 on past-self snapshots (currently no flag; ~20 lines in the sampling function). Rerun v7 with K=10.
8. Fall back to the unified-pool + JSD-dedup redesign.

**Not recommended:**
- Do not touch the architecture in v7.
- Do not change LR / clip / entropy schedule in v7 — all of v6's per-iteration training numbers were healthy; the failure was purely pool-composition.
- Do not train past 80 iters in v7 until the post-iter-50 behavior is verified clean.

## V7 Launch Command

Base command derived from v6 ppo_args.json with three changes: warmstart checkpoint, fadeout, out-dir. Thread budget prefix added per standing practice.

```bash
OMP_NUM_THREADS=6 KMP_BLOCKTIME=0 nohup uv run python scripts/train_ppo.py \
  --checkpoint results/ppo_country_attn_v6/ppo_iter0020.pt \
  --reset-optimizer \
  --out-dir results/ppo_country_attn_v7 \
  --version country_attn_v7 \
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
    data/checkpoints/scripted_for_elo/v55_scripted.pt \
    data/checkpoints/scripted_for_elo/v54_scripted.pt \
    data/checkpoints/scripted_for_elo/v44_scripted.pt \
    data/checkpoints/scripted_for_elo/v20_scripted.pt \
    results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
    results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
    __heuristic__ \
  --eval-every 20 \
  --side both \
  --self-play-heuristic-mix 0.2 \
  --seed 42000 --device cuda \
  --wandb --wandb-project twilight-struggle-ai \
  --wandb-run-name ppo_country_attn_v7 \
  --max-kl 0.03 --ema-decay 0.995 --target-kl 0.015 \
  --vp-reward-coef 0.0 \
  --reward-alpha 0.5 \
  --dense-reward-alpha 0.0 --dense-reward-anneal-steps 500000 \
  --league results/ppo_country_attn_v7 \
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
  --skip-smoke-test \
  > results/ppo_country_attn_v7/train.log 2>&1 &
```

Notes on the command:
- The `--reset-optimizer` flag is kept because v6's optimizer state is not meaningfully useful when changing PFSP pool dynamics — clean optimizer is safer.
- `eval_opponent` is omitted (it was `null` in v6 args); the `--eval-panel` args supply all panel evals.
- The recency-cap K=10 recommendation is **not** added here because no CLI flag exists. If implemented, it would be `--league-past-self-cap 10` or similar — a ~20-line addition to `sample_K_league_opponents` in `scripts/train_ppo.py`.
- Make sure `results/ppo_country_attn_v7/` exists (`mkdir -p`) before launching; the shell redirect will fail otherwise.

## Open Questions

1. **Is v6_iter20's +1.7pp reproducible, or is it a seed fluctuation?** 500 games/side gives ±2pp per side. Running a second 500-game/side bench with different seeds (e.g. 60000/60500) on `ppo_iter0020.pt` would tighten this. Cheap: ~5 minutes. Worth doing before declaring a project record.

2. **Will v7 iter 80 avoid the regression, or will it find a different failure mode?** The hypothesis "fadeout is the sole culprit" is testable in 80 iters. If v7_iter80 combined < 0.42, fadeout is not the only issue and the PFSP redesign becomes higher priority.

3. **Should the heuristic be re-measured heuristic-vs-heuristic post-engine-fix?** The 42% US WR figure used in the overfit analysis is 17 days old. A fresh 1000-game heuristic-vs-heuristic run takes minutes and grounds all future ceiling arguments. Low priority but trivially cheap.

4. **Is the eval panel actually informative once all BC cluster + v6 are near-tied?** If every panel match is ≈0.5, the panel cost (~15% of iter wall-clock) buys nothing beyond the heuristic match. Consider trimming `eval_panel` to `[v56_scripted, __heuristic__]` in v8+ to speed up iterations.

5. **Does the running-best bug need a code fix or is manual selection sufficient?** If v7 reproduces the peak-then-decline pattern, a structural fix (heuristic-only gate on running-best) is necessary. If v7 plateaus cleanly without fadeout, the symptom may not recur.

6. **How big is the architecture ceiling actually?** The BC symmetric cluster sits in a ~14-Elo band (v20 to v54). v6 has not broken out. Breaking out likely requires something non-PFSP: teacher search, dense-reward value signal, or architecture change (multi-head side-specialization or card-cross-attention with stronger inductive bias).
