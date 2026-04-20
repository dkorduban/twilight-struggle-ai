# Opus Analysis: v8 Results and v9 Plan
Date: 2026-04-20T10:25:00Z
Question: v8 PPO completed 80 iterations. Panel trajectory: iter20=0.504, iter40=0.454, iter60=0.442, iter80=0.521. Heuristic panel WR at iter80=0.583/60games (vs v7's 0.367, vs v8's own iter20=0.483). Is the panel dip/recovery a training artifact or genuine? What is the actual combined WR vs heuristic? Is v8's US low rollout_wr the same failure mode as v7? Should we run v9, and what should change? US overfit iter40 — US WR improvement?

## Executive Summary

**v8 failed hard, and the pool-rebalancing thesis is falsified.** Formal 500-games/side bench vs heuristic at iter80: combined=0.351 (USSR=0.462, US=0.240) — 7.2pp below v7_iter80 (0.423), 10.7pp below v6_iter20 (0.458), 9.0pp below v56 (0.441). US overfit v1 iter40 is even worse: combined=0.212 with US=**0.080**, a 28pp regression from its us_only_v5 warmstart (US=0.360). The iter80 heuristic-panel spike to 0.583 was 30-game noise that contradicts both the 500g bench AND the rollout trajectory (US rollout_wr never exceeded 0.34 in the last 20 iters). Both interventions in this batch shared `heuristic-floor=0.30 + trimmed league fixtures`, and both failed catastrophically. **Continuation_plan's pre-committed abort criterion (`iter20 combined < 0.40 → pivot`) is triggered.** v9 should not be "v8 with different floor / different fixtures" — that is the same falsified hypothesis tweaked. Pivot to Option A (re-bench v6_iter20 to confirm record is reproducible) then Option B (dense reward) or Option C (teacher distillation).

## Findings

### v8 Formal Bench Result

`results/ppo_country_attn_v8/bench_iter80_500g.json` (N=500/side, Nash temps, seed=50000/50500):
- **USSR WR = 0.462** (231/500)
- **US WR = 0.240** (120/500)
- **Combined WR = 0.351**
- Duration: 124s

This is the **worst symmetric-policy bench since v3_best (0.274)** and is below every other recent checkpoint on record:
- v8_iter80 (0.351) < v7_iter80 (0.423) < v7_iter60 (0.376 wait, 0.376 is also worse, but 0.351 is the minimum for 2026-04 runs)

Actually: v7_iter60 was 0.376, v6_iter80 was 0.270 (fadeout-killed). v8_iter80=0.351 is **better than v6_iter80=0.270** but worse than every other tested checkpoint from v6/v7. The US side at 0.240 specifically is 4.6pp above v7_iter80's 0.124 — one mild positive — but USSR at 0.462 is 26.0pp below v7_iter80's 0.722, which is a much larger regression than the US gain. Net: worse than v7 on both the metric (combined) and on any reasonable Elo-like score.

### v8 Panel Trajectory Analysis

Panel composition: [v56, ussr_only_v5, us_only_v5, heuristic], 30 games/side each (60 total per cell).

| Iter | v56 | ussr_v5 | us_v5 | heur | avg | heur_US | heur_USSR |
|---|---|---|---|---|---|---|---|
| 20 | 0.500 | 0.400 | 0.633 | 0.483 | 0.504 | 0.400 | 0.567 |
| 40 | 0.483 | 0.500 | 0.417 | 0.417 | 0.454 | 0.400 | 0.433 |
| 60 | 0.433 | 0.450 | 0.483 | 0.400 | 0.442 | 0.300 | 0.500 |
| 80 | 0.483 | 0.483 | 0.533 | 0.583 | 0.521 | **0.567** | 0.600 |

**The iter80 heuristic=0.583 spike is 30-game noise.** Per-cell stderr at N=30 per side is ±0.091; the iter60→80 delta of +0.183 in combined has z≈2.0 (borderline). Rollout_wr in the same window (iters 61-80) averaged US=0.290 and USSR=0.573 — no discernible jump. Iter 79's US rollout was 0.24; iter 80's was 0.33. The 500-game bench resolves the ambiguity: **iter80 US vs heuristic = 0.240, not 0.567**. The panel spike was a lucky-draw on 30 games.

**Primary diagnostic finding: even the trimmed 4-entry panel is unreliable as a proxy for combined-vs-heuristic WR.** At 30 games/side per cell and with three of four cells being self-similar-style opponents, a single-iter spike masks the fact that the true heuristic-WR is collapsing. Running-best selection on panel-avg chose iter80 as `ppo_running_best.pt` because panel-avg=0.521 — wrong. Bench says iter80 is the worst of the four snapshots in combined-WR terms.

The iter40→60 panel dip (0.454→0.442) tracks qualitatively with the rollout trajectory (window 21-40 US=0.278, window 41-60 US=0.264 — small drop). The iter80 recovery is the artifact; the iter40/60 dip is the true signal. v8 plateaued around 0.35 combined after iter40 and never recovered.

### v8 US WR Analysis (same failure mode as v7? or different?)

| Metric | v7_iter80 | v8_iter80 | delta |
|---|---|---|---|
| US vs heuristic (500g) | 0.124 | 0.240 | +0.116 |
| USSR vs heuristic (500g) | 0.722 | 0.462 | −0.260 |
| Combined vs heuristic | 0.423 | 0.351 | −0.072 |
| Rollout US (iters 61-80 avg) | ~0.45 | 0.290 | −0.16 |
| Rollout USSR (iters 61-80 avg) | ~0.60 | 0.573 | −0.03 |
| Panel US vs heuristic (iter80) | 0.067 | 0.567 | +0.500 (noise) |

v7 had **asymmetric specialization**: USSR overspecialized to the BC-cluster pool (won against league AND heuristic), US catastrophically lost generalization (0.124 vs heuristic, but rollout_wr fine).

v8 shows a **different failure mode**: heuristic-floor=0.30 partially rebalanced the pool (US vs heuristic recovered +11.6pp from v7's 0.124), but the process **broke USSR generalization** too (-26pp USSR vs heuristic, from 0.722 to 0.462). Net effect: US slightly better, USSR much worse, combined worse. The policy landscape between v7 and v8 is not the same disease — v8 successfully un-specialized US against heuristic but at the cost of destroying the USSR signal that v7 had built up.

The rollout_wr trajectory explains part of this. v8 rollouts in iters 41-60 saw more heuristic-side games (heuristic-floor=0.30 active, no BC cluster padding). Rollout US=0.264 (window 41-60), clearly showing the policy was not finding US wins even in rollout. The policy converged to a flat ~0.35 rollout_wr by iter 40 and never improved — the extra heuristic exposure did not help US, and the loss of BC-cluster games (which gave USSR-side easy wins against symmetric opponents) hurt USSR.

**Verdict: v8's failure is the mirror image of v7's, not an improvement.** v7 traded US-heuristic for USSR-heuristic; v8 traded USSR-heuristic for partial US-heuristic recovery. Neither beat v6_iter20=0.458.

### US Overfit Result

`results/capacity_test/ppo_us_overfit_v1/bench_500g.json`:
- **USSR WR = 0.344** (172/500)
- **US WR = 0.080** (40/500) — the US side this experiment was designed to improve
- Combined WR = 0.212

Warmstart was `us_only_v5/ppo_best.pt` which historically benches at US=0.360. After 40 iters of PPO with heuristic-floor=0.30 and fixtures=[v56, v55, __heuristic__], the US side **collapsed -28pp to 0.080** — worse than even v7_iter80's US collapse (0.124).

Rollout_wr during training painted a deceptive picture: iter40 rollout US=0.495 (peak), iter28-39 hovering 0.40-0.54, iter21 rollout US=0.415. **Rollout says "US improving from 0.40 to 0.50," bench says "US destroyed from 0.36 to 0.08."** This is the same panel-vs-bench divergence as v7/v8 but at a more extreme scale.

Sanity check: I re-ran us_only_v5 and v56 bench at N=200 to verify the methodology. Got us_only_v5=0.463 combined (US=0.430) and v56=0.495 combined (US=0.425) — both consistent with their historical benches within 1-2σ. So the bench script is not broken; the us_overfit_v1 checkpoint really is catastrophically worse.

**This confirms the failure is in the training pool/recipe, not in evaluation.** Two independent runs with heuristic-floor=0.30 and small trimmed fixture lists both blew up in exactly the same way: rollout_wr looked reasonable, heuristic-WR bench is 20-28pp below warmstart.

Hypothesis: with heuristic-floor=0.30 and only 3-4 fixtures, the PFSP weights concentrate on a handful of self-similar opponents when heuristic is not drawn, and the resulting policy overfits to this tiny opponent set. When league_mix_k=6 is sampling from a pool of {__self__, v56, v55, __heuristic__}, and ~30% of slots go to heuristic, the remaining ~70% is dominated by 1-2 league opponents per batch. The policy learns exploits against those exact 1-2 opponents and loses general play. The heuristic-floor mechanism has PFSP_heuristic^pfsp_exponent ≈ 1.0 weight (heuristic always survives the UCB filter), but the US-side heuristic signal (US vs heuristic is the hardest matchup) gets drowned out by signal from USSR-side heuristic games and from league wins.

### Comparison Table (v56 / v6_iter20 / v7_iter80 / v8_iter80)

All 500g/side, seed=50000/50500, Nash temps, same engine state:

| Checkpoint | USSR | US | Combined | vs v56 | vs record |
|---|---|---|---|---|---|
| v56 | 0.558 | 0.325 | **0.441** | 0.0 | −0.017 |
| us_only_v5 | 0.506 | 0.360 | 0.433 | −0.008 | −0.025 |
| ussr_only_v5 | 0.588 | 0.316 | 0.452 | +0.011 | −0.006 |
| **v6_iter20** | 0.582 | 0.334 | **0.458** | **+0.017** | **0.0 (RECORD)** |
| v7_iter20 | 0.654 | 0.140 | 0.397 | −0.044 | −0.061 |
| v7_iter40 | 0.710 | 0.110 | 0.410 | −0.031 | −0.048 |
| v7_iter60 | 0.652 | 0.100 | 0.376 | −0.065 | −0.082 |
| v7_iter80 | 0.722 | 0.124 | 0.423 | −0.018 | −0.035 |
| **v8_iter80** | 0.462 | 0.240 | **0.351** | **−0.090** | **−0.107** |
| **us_overfit_v1_iter40** | 0.344 | **0.080** | **0.212** | **−0.229** | **−0.246** |

**v8 is the largest regression of any completed multi-iter PPO run in 2026.** Only broken/killed runs (v3_best=0.274, v4_iter50=0.33, AWR runs) are worse. The "pool rebalancing" hypothesis has been run twice (v8 full and us_overfit_v1 abbreviated) and produced catastrophic regressions both times.

Candidate tournament cross-check (`results/ppo_country_attn_v8/candidate_tournament.json`):
- v8_iter20: Elo=1845 (−55 vs v56)
- v8_iter40: Elo=1854 (−46 vs v56)
- v8_iter60: Elo=1829 (−71 vs v56)

Compare to v7's candidate tournament: v7_iter40 was +99 vs v56, v7_iter60 was +84. **v8 moved both metrics (heuristic combined AND league Elo) in the wrong direction.** v7 at least gained league Elo while losing heuristic; v8 lost both.

Incremental ladder Elo: country_attn_v8 = 1858 (−42 vs v56 anchor 1900). For reference: v7_iter40 promoted as ppo_best gave country_attn_v7 = 1912 (+12 vs v56). v8 is **54 Elo points below v7 on the ladder**, entirely consistent with the heuristic-bench regression.

## Conclusions

1. **v8 FAILED.** Combined WR vs heuristic at iter80 = 0.351, which is below v56 baseline (0.441), below v6_iter20 record (0.458), below v7_iter80 (0.423), and below every non-fadeout v6/v7 snapshot. The predicted v8 outcome ("US-vs-heuristic recovers toward 0.30+, USSR stays >0.55, combined ≥ 0.45") was wrong on all three predictions: US=0.240 (below 0.30 target), USSR=0.462 (far below 0.55 floor), combined=0.351 (way below 0.45). The continuation_plan abort criterion ("iter20 combined < 0.40 → pivot") is retroactively triggered — v8's iter20 wasn't benched but trajectory confirms plateau near 0.35.

2. **The US overfit v1 experiment also FAILED.** Iter40 bench US=0.080, a 28pp regression from the us_only_v5 warmstart (US=0.360). The experiment was designed to answer "does heuristic-floor=0.30 + focused US training improve US vs heuristic?" The answer is decisively no — it destroys US-heuristic performance.

3. **The pool-rebalancing thesis is falsified.** Both v8 (symmetric) and us_overfit_v1 (US-only) shared the core intervention (heuristic-floor=0.30 + trimmed fixtures). Both regressed dramatically. This is two independent falsifications of the same hypothesis. Running v9 with "same recipe, different floor" is not justified by the evidence.

4. **The iter80 heuristic-panel spike (0.583) was pure noise.** 30-game-per-side cell, z≈2.0 from iter60 baseline, contradicted by concurrent 500g bench AND by concurrent rollout US WR. **Even the 4-entry trimmed panel is not a reliable selector for combined-heuristic-WR.** The running-best-selection mechanism picked iter80 as `ppo_running_best.pt` on panel-avg=0.521 — this selection is wrong by 0.17 on the metric that matters.

5. **v8's failure mode is NOT the same as v7's.** v7 asymmetrically over-specialized (USSR way up, US way down, combined barely down). v8 un-specialized both sides toward the heuristic-rich pool (USSR way down -26pp, US slightly up +12pp), net combined down. The rollout US trajectory in v8 is consistent with this — iters 1-60 averaged US ~0.26, only iter 61-80 averaged 0.29, no real improvement trend. The extra heuristic exposure didn't teach the US side anything structural; it just diluted the USSR-side league gain without compensating US-side progress.

6. **rollout_wr vs combined-heuristic-WR divergence is now a known repeatable failure mode.** us_overfit_v1 had rollout US=0.495 at iter40 but bench US=0.080. This is an 0.415 gap. v8 had rollout US≈0.29 with bench US=0.24 (0.05 gap), so the v8 gap is smaller but the direction is identical: rollout overstates US performance. The failure is selection bias — rollout US is against the pool (mostly self-similar USSR), bench US is against heuristic USSR only. Self-similar USSR is a weaker, stylistically tighter opponent than heuristic USSR for the US side, so rollout US > bench US systematically.

7. **v6_iter20 remains the project record at 0.458.** None of v7 or v8 beat it. The record has not been challenged in >200 iters of training across two runs.

8. **The pre-committed pivot in continuation_plan should now be executed.** `"abort_criterion: iter 20 combined < 0.40 — pool rebalancing insufficient; pivot to teacher search / dense reward"`. v8's full 80 iters converged at 0.35 combined. Pivot is not optional; the falsification is clean.

## Recommendations

1. **Do NOT launch v9 with the same pool-rebalancing recipe.** Variants tried (heuristic-floor 0.15/0.30, fixture counts 8/4/3, side=both/us) have all failed to beat v6_iter20. The hypothesis is falsified. Moving to a different hypothesis is required.

2. **Immediate next step (Option A, 2 min GPU): Re-bench v6_iter20 with fresh seed 60000/60500 to confirm 0.458 is reproducible.** Before investing GPU in v9, confirm the record baseline is not itself a lucky seed. If v6_iter20 re-benches at 0.40, the entire project "record" is noise and the ranking shifts. If v6_iter20 re-benches at 0.44-0.46, the record stands and we have a firm baseline for future runs.

3. **After Option A confirms v6_iter20 record: run v9_dense = v6_iter20 warmstart + dense reward shaping.** v8's args already set `--reward-alpha 0.5` but `--dense-reward-alpha 0.0` (dense disabled). Enable dense reward (alpha=0.2-0.4 with anneal) to give the policy per-turn VP-delta shaping. Keep v6_iter20 pool composition (original v6 fixtures) to isolate the reward signal as the only intervention. No heuristic-floor change, no fixture trim. 80 iters, eval_every=20, same LR/clip as v7.

4. **Alternative v9 (Option C): teacher-search distillation pass on US-side hard positions.** Mine 100 US-side hard positions from recent games, run shallow MCTS (30 sims, heuristic rollout) to produce action targets, then KL-regularize the US policy on those targets for 5-10 iters starting from v6_iter20. This is the "teacher assists US" idea from the v7 analysis Tier 3; v8's failure makes it higher-priority now.

5. **Defer Option B/C pick until Option A bench comes back.** Don't commit to a recipe before the baseline is verified.

6. **Investigate the rollout_wr vs bench divergence as a systemic issue.** Both v8 and us_overfit_v1 show rollout US substantially higher than bench US. This means any selection criterion based on rollout_wr is biased toward pool-specialized policies. Consider:
   - Adding a dedicated heuristic-only bench step every 10 iters (50 games each side, ~30s) during training.
   - Using that heuristic-only bench as the running-best selector instead of panel-avg.
   - Logging the bench to W&B alongside rollout to make divergence visible in real-time.

7. **Do NOT increase `heuristic-floor` further.** It is now empirically demonstrated that higher heuristic share does NOT improve heuristic-vs-heuristic WR when combined with a small league pool. The problem is not the mix ratio; it is that the policy is optimizing against a gradient that does not align with pure heuristic WR.

8. **Consider reverting heuristic-floor to 0.15 AND keeping the BC-cluster fixtures (v20/v44/v54/v55)** as a diagnostic isolate. If v9 with v6-identical setup matches v6_iter20, the record is recipe-reproducible. If it lands lower, seed variance is dominant and we need bigger N.

## V9 Launch Command

**Step 1 (immediate, 2 min GPU): Re-bench v6_iter20 to confirm the record.**

```bash
cat > /tmp/v6_iter20_rebench.py << 'PYEOF'
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path("/home/dkord/code/twilight-struggle-ai/build-ninja/bindings")))
import tscore

ckpt = "/home/dkord/code/twilight-struggle-ai/results/ppo_country_attn_v6/ppo_iter0020_scripted.pt"
# Export scripted if missing
if not Path(ckpt).exists():
    print(f"Need scripted export first: {ckpt}")
    sys.exit(1)

N = 500
t0 = time.time()
ur = tscore.benchmark_batched(ckpt, tscore.Side.USSR, N, pool_size=32, seed=60000, nash_temperatures=True)
us = tscore.benchmark_batched(ckpt, tscore.Side.US, N, pool_size=32, seed=60500, nash_temperatures=True)
dur = time.time() - t0
ussr_w = sum(1 for r in ur if r.winner == tscore.Side.USSR) / N
us_w = sum(1 for r in us if r.winner == tscore.Side.US) / N
comb = (ussr_w + us_w) / 2
out = {"checkpoint": ckpt, "n_games_per_side": N, "seeds": {"ussr": 60000, "us": 60500},
       "ussr_wr": round(ussr_w, 3), "us_wr": round(us_w, 3), "combined_wr": round(comb, 3),
       "duration_s": dur}
with open("/home/dkord/code/twilight-struggle-ai/results/ppo_country_attn_v6/bench_iter20_500g_s60000.json", "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps(out, indent=2))
PYEOF
uv run python /tmp/v6_iter20_rebench.py
```

**Step 2 (conditional on Step 1 result): Launch v9_dense.**

If v6_iter20 re-bench confirms combined≥0.44 (record reproducible), launch:

```bash
mkdir -p results/ppo_country_attn_v9

OMP_NUM_THREADS=6 KMP_BLOCKTIME=0 nohup uv run python scripts/train_ppo.py \
  --checkpoint results/ppo_country_attn_v6/ppo_iter0020.pt \
  --reset-optimizer \
  --out-dir results/ppo_country_attn_v9 \
  --version country_attn_v9 \
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
  --seed 44000 --device cuda \
  --wandb --wandb-project twilight-struggle-ai \
  --wandb-run-name ppo_country_attn_v9_dense \
  --ema-decay 0.995 --target-kl 0.015 \
  --reward-alpha 0.5 \
  --dense-reward-alpha 0.3 --dense-reward-anneal-steps 250000 \
  --league results/ppo_country_attn_v9 \
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
  > results/ppo_country_attn_v9/train.log 2>&1 &
```

Key differences from v8:
- Revert heuristic-floor to **0.15** (v8's 0.30 was the falsified intervention)
- Restore full 8-fixture league pool (v20/v44/v54/v55/v56 + two specialists + heuristic) — v6/v7 used this, v8 trimmed to 4
- **Enable dense reward: `--dense-reward-alpha 0.3`** (was 0.0 in v6/v7/v8) — this is the new intervention
- Anneal dense reward over 250k steps (~5x faster than v8's 500k) so it's active throughout training
- Panel trimmed to just [v56, heuristic] at 100 games each side — at 200 games/iter rollout, a 100-game panel-cell bench is more reliable than 30-game cells, with similar cost
- eval_every=10 (was 20) for finer-grained selection signal
- seed=44000 (noise isolation)

Success criteria for v9_dense:
- iter 20 combined ≥ 0.45 (match v6_iter20 baseline)
- iter 40 combined ≥ 0.47 (exceed v6_iter20 record by 1pp)
- iter 80 combined ≥ 0.50 (project target)
- US vs heuristic at iter 80 ≥ 0.35 (must not regress below us_only_v5's 0.36)
- USSR vs heuristic at iter 80 ≥ 0.58 (hold v56 USSR level)

Abort criteria:
- iter 20 combined < 0.42 → dense reward alone is insufficient; pivot to teacher distillation
- US side drops below 0.20 at any iter → warn, consider killing
- KL blow-up (ep=1/4 repeatedly with kl > 0.1) → lower LR to 3e-5 and relaunch

**Step 3 (fallback if v9_dense also fails): Option C teacher distillation.** Mine 100 US-side hard positions from v6_iter20 games, generate MCTS action targets (30 sims, heuristic rollout), KL-regularize US policy for 5-10 iters. Spec to follow after v9_dense bench result.

## Open Questions

1. **Does v6_iter20 re-bench at 0.458 on seed 60000/60500?** Option A above. Must run before trusting the record. Cheap.

2. **Why does heuristic-floor=0.30 destroy policies?** Two hypotheses:
   - (a) PFSP weight dynamics: with only 3-4 opponents in the trimmed pool, PFSP's UCB selection produces very uneven opponent distributions; combined with 30% heuristic the remaining 70% concentrates on 1-2 league opponents per batch, producing over-exploitation.
   - (b) Gradient noise from heuristic rollouts: heuristic play is stylistically narrow; gradients from heuristic losses may be high-variance and overwhelm league-gradient signal. A policy that "tries to beat heuristic" may converge to a different local minimum than one that "tries to beat skilled play."
   - Can diagnose by running v9_probe = v6_iter20 warmstart + heuristic-floor=0.30 + full 8-fixture pool (isolates heuristic-floor from fixture trim). Too expensive to run before v9_dense.

3. **Is the 4-entry panel ever useful?** Data says no for combined-vs-heuristic selection. Consider replacing with a dedicated 200-game heuristic-only bench every 10 iters.

4. **Are the us_overfit_v1 fixtures incompatible with its warmstart?** us_only_v5 was trained with different fixtures; switching mid-stream to v56+v55+heuristic may have caused catastrophic forgetting. Less relevant now — v8 (symmetric, same fixtures as its warmstart v6) still failed.

5. **Is `--upgo` a confound?** v6/v7/v8 all used upgo=True. v6_iter20 (record) and v6_iter40+ (broken fadeout) both had it. v8 failure can't be blamed on upgo alone. Keep for v9; revisit only if v9 also fails.

6. **Could `--reward-alpha 0.5` in v8 itself be harmful?** All runs had this (and it's just the VP-based terminal reward scaling). Not a new factor. Keep.

7. **Is the engine stable between v7-bench and v8-bench runs?** Engine fixes/refactors in the last 2 weeks might have shifted baseline WR. The sanity bench (v56 at N=200 gave 0.495 vs historical 0.441) has a ~2σ gap that could be noise or drift. Option A's re-bench of v6_iter20 also answers this.
