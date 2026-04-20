# Opus Analysis: v7 Results and Next Steps
Date: 2026-04-20T09:31:00Z
Question: v7 PPO completed 80 iterations with monotone panel improvement (no post-iter-50 regression): iter20=0.550, iter40=0.552, iter60=0.554, iter80=0.579. Given the panel_avg trajectory, is the model still improving at iter 80 or plateauing? What does rollout_wr say? What is the actual combined WR vs heuristic? Should v8 start from v7_iter80? What metrics to watch on the US-overfit experiment?

## Executive Summary

**The task framing understates a material contradiction.** Panel-avg WR went up monotonically (0.550→0.579) and candidate-tournament Elo says v7_iter40 is +99 Elo over v56 — genuinely strong. But the **project's stated north star metric, combined WR vs heuristic on 500 games/side, says the opposite**: v7 never beats v6_iter20. Freshly measured: v7_iter20=0.397, iter40=0.410, iter60=0.376, iter80=0.423. **v6_iter20 (0.458) remains the project record; v7_iter80 (0.423) is 3.5pp below the record and 1.8pp below v56 (0.441).** v7 traded heuristic-side strength for league-side strength. The fadeout fix worked (no running-best collapse, no panel regression), but a *different* failure mode surfaced: US-vs-heuristic collapsed from 0.325 (v56) to 0.124 (v7_iter80) while USSR-vs-heuristic went up to 0.722. The US side is over-specialized against the self-similar BC-cluster+past-self mix and has forgotten how to respond to heuristic-style USSR. v8 should fix the heuristic-dose imbalance or pivot the north-star metric to Elo.

## Findings

### 1. The two metrics disagree, and this is the whole story

Panel-avg WR (all 8 panel opponents averaged, from `panel_eval_history.json`) climbed steadily:
| Iter | v56 | v55 | v54 | v44 | v20 | ussr_only_v5 | us_only_v5 | heuristic | avg |
|---|---|---|---|---|---|---|---|---|---|
| 20 | 0.617 | 0.617 | 0.500 | 0.533 | 0.600 | 0.567 | 0.533 | **0.433** | 0.550 |
| 40 | 0.483 | 0.567 | 0.600 | 0.533 | 0.517 | 0.550 | 0.717 | **0.450** | 0.552 |
| 60 | 0.583 | 0.517 | 0.583 | 0.617 | 0.550 | 0.517 | 0.633 | **0.433** | 0.554 |
| 80 | 0.567 | 0.733 | 0.583 | 0.567 | 0.617 | 0.583 | 0.617 | **0.367** | 0.579 |

The heuristic column is the one you care about — and it went **down** from 0.450 at iter 40 to 0.367 at iter 80 while the other 7 opponents (all BC-cluster + PFSP-class models) went up. Panel-avg improvement is dominated 7:1 by league-style opponents.

Freshly-run 500-game/side heuristic benchmarks (seeds 50000/50500, same methodology as v6 bench):
| Checkpoint | USSR WR | US WR | Combined | Delta vs v56 | Delta vs v6_iter20 |
|---|---|---|---|---|---|
| v56 | 0.558 | 0.325 | 0.441 | 0.0 | −0.017 |
| v6_iter20 (record) | 0.582 | 0.334 | **0.458** | +0.017 | 0.0 |
| v7_iter20 | 0.654 | 0.140 | 0.397 | −0.044 | −0.061 |
| v7_iter40 | 0.710 | 0.110 | 0.410 | −0.031 | −0.048 |
| v7_iter60 | 0.652 | 0.100 | 0.376 | −0.065 | −0.082 |
| v7_iter80 | 0.722 | 0.124 | 0.423 | −0.018 | −0.035 |

**Not a single v7 iteration exceeds v6_iter20 on combined WR vs heuristic.** USSR side gained +14–17pp everywhere vs v6_iter20; US side lost 19–23pp everywhere. This is not a traversal-to-a-better-optimum pattern; it is a clean asymmetric regression on the weak side.

### 2. The success criteria from continuation_plan.json are a mixed verdict

From `continuation_plan.json` `v7_plan`:
- `success_criterion_iter20: combined ≥ 0.45 (matches v6_iter20)` — **FAILED** (0.397, −5.3pp short)
- `success_criterion_iter80: combined ≥ 0.42 (within 3pp of iter20)` — **BARELY PASSED** (0.423)
- `abort_criterion: iter 20 combined < 0.40` — **MARGINAL** (0.397 is 0.3pp below the abort threshold)

On its stated own terms, v7 iter 20 is right at the abort line. The plan predicted "If v7 iter 20 combined < 0.40, fadeout was not the sole issue; escalate to PFSP redesign." We are essentially at that threshold. The fadeout fix did work in the sense it was designed for (no post-iter-50 collapse on panel; fixtures kept appearing — see wr_table.json: heuristic=1880 games distributed, scripted fixtures all in 400+ range), but the regression mechanism is different.

### 3. What the rollout_wr trajectory actually says

Rollout_wr averaged over iters 1–20 ≈ 0.505, iters 21–40 ≈ 0.540, iters 41–60 ≈ 0.565, iters 61–80 ≈ 0.585. Monotone upward. US component of rollout_wr also went up — iter 8 had us=0.200, iter 74 had us=0.610. But: rollout opponents are the PFSP mix of past-self + BC fixtures + ~15% heuristic (heuristic-floor=0.15). The rollout is *self-similar-weighted*. A US policy that plays well against "USSR that opens like v20/v54/v56/past-v7" can still be completely lost against "heuristic USSR." The rollout_wr rise is consistent with league specialization, not generalization.

Cross-check: the US peak of 0.610 at iter 74 is against a pool where only ~15–20% of games are vs heuristic; at iter 80 panel-vs-heuristic US=0.067 (60 games) and the 500-game heuristic bench says US=0.124. So 6–12% US WR vs heuristic, coexisting with 40–61% US WR in rollout. The two are not close — the US policy has bifurcated, learning a response pattern tuned to self-similar USSR styles that does not transfer.

### 4. Candidate tournament: v7 is genuinely stronger vs the BC cluster

From `candidate_tournament.json` (150-game matches, round-robin, anchor v56=1900):
| Model | Elo | Elo_USSR | Elo_US | vs anchor |
|---|---|---|---|---|
| v7_iter40 | 1999.2 | 2062.1 | 1864.1 | +99.2 |
| v7_iter60 | 1984.0 | 2038.3 | 1849.6 | +84.0 |
| v7_iter20 | 1925.1 | 2018.7 | 1736.7 | +25.1 |
| v54 | 1912 | 1904 | 1810 | +12 |
| v55 | 1911 | 1897 | 1814 | +11 |
| v20 | 1902 | 1900 | 1793 | +2 |
| v56 | 1900 | 1900 | 1787 | 0 |
| v44 | 1900 | 1881 | 1806 | −0 |

v7_iter40 vs v56 head-to-head: 97-52-1, WR=0.650. v7_iter60 vs v56: 95-53-2, WR=0.640. These are decisive wins on the league metric. If the project success criterion were "beat v56 head-to-head in a league-style tournament," v7 succeeded with room to spare — iter40 cleared the BC cluster by +87 Elo.

The incremental Elo placement into the full ladder gave country_attn_v7=1912 (iter40 promoted as ppo_best) — +12 vs v56 in the combined-ladder fit. The elo_us component dropped to 1768 (v56=1778, so iter40 is −10 vs v56 on US-side Elo), but elo_ussr=1938 (v56=1900, +38 vs v56). Same bipolar story as the heuristic bench: USSR way up, US flat-or-down.

### 5. Panel_avg 0.579 — still improving or plateau?

Looking at the panel table deltas iter 20→80: v56 −0.050, v55 +0.116, v54 +0.083, v44 +0.034, v20 +0.017, ussr_only_v5 +0.016, us_only_v5 +0.084, heuristic −0.066. Average panel gain ~+0.029 (0.550→0.579) over 60 iters is ~0.0005/iter — a plateau, not a climb. v7 iter 60→80 was +0.025 panel-avg but came almost entirely from the v55 matchup jumping to 0.733 (one 60-game match, large noise per-cell). Panel games are 60 per opponent — the stderr on a single-cell WR is ~±6pp. Cell-level iter-to-iter wiggle is at noise level; trend is plateau.

Combined heuristic trajectory iter20→80 is 0.397→0.410→0.376→0.423 — noisy around 0.4 with no direction. Also a plateau, below the v6_iter20 record.

**Verdict: plateau. Running 120 or 160 iters of v7 as-is is a waste of GPU.**

### 6. Rollout composition changed, but still self-similar

`wr_table.json` shows v7's pool distribution by game count:
- __self__ = 1880 US + 1880 USSR = 3760 games (largest category)
- ppo_best_scripted = 720 US + 920 USSR = 1640
- v55_scripted = 800 US + 600 USSR = 1400
- heuristic = 1040 US + 840 USSR = 1880 (good — heuristic is the 2nd-largest category and spread across iters)
- scripted fixtures (v20/v44/v54/v56) = ~900–1040 each
- past-self snapshots (iter_0001–iter_0070) = smaller pockets each

Heuristic saw ~23% of total rollout games — respectable. But the aggregate WR vs heuristic in rollout was US=163/1040=0.157 (15.7%), and USSR=432/840=0.514 (51.4%). The policy is getting ~15% US WR vs heuristic continuously during training, and that signal is *present* in the gradient — it just isn't strong enough to pull the policy out of a USSR-skewed optimum given the 77% league-style pool.

### 7. Same disease as v6, different symptom

v6's failure mode: fadeout=50 dropped heuristic after iter 50, policy drifted into pure self-play, both sides collapsed. v6_iter20 was the peak.

v7's failure mode: fadeout=999 kept heuristic in the pool, but the aggregate pool composition (~20% heuristic + ~80% BC+past-self) is self-similar-dominant. The *direction* of drift is the same — specialize to the dominant-style opponent — just the trajectory looks cleaner on the panel metric because the panel shares the bias. The US-vs-heuristic collapse (0.334→0.124) in v7 is quantitatively worse than the US-vs-heuristic collapse in v6 iter40 (0.334→0.150), it just doesn't show up on the aggregate panel.

Why US-side specifically: the BC cluster (v20/v44/v54/v55/v56) are symmetric-trained policies whose USSR-play is relatively coherent. When the US side of v7 fits to "beat USSR-of-v20/v54/v56/past-v7," it is fitting to a fairly narrow USSR-style manifold, and the response pattern that wins in-distribution fails spectacularly against the heuristic's un-stylized USSR play (which over-expands, plays low-IV cards, and triggers coups/realignments in patterns the BC cluster has learned to punish). Heuristic USSR is not strong, but it is *different*, and v7_US didn't see enough of it.

### 8. Why USSR-vs-heuristic went UP so much

v7 USSR vs heuristic at iter 80 = 0.722, +16pp over v56. This is the genuine positive finding. USSR side is both stronger against the league AND stronger against the heuristic — it generalizes. The asymmetry between the two sides (USSR gains 16pp, US loses 20pp) suggests the USSR problem is easier: USSR has a wider set of good openings (headlined CIA, headlined Duck and Cover, MEU Formed, etc. all work), and a USSR policy trained on self-similar data can still find stylistically-neutral moves that beat most opponents. US is structurally tighter — responses to CIA, to early Romanian Abdication, to Fidel, to Indo-Pakistani all have narrower good-move-sets. When US overfits to a pool, it loses the margin that was barely there to begin with.

This matches the long-term project record: no symmetric policy has ever cleared 0.42 US WR vs heuristic, and US-only specialists (us_only_v5 at 0.360) are only marginally better. US is the constraint.

### 9. KL behavior was clean but early-stop triggered twice

Iter 33 and iter 39 logged `ep=1/4 kl=0.074` and `ep=1/4 kl=0.069` respectively — PPO update aborted at epoch 1 due to target_kl=0.015. This is healthy behavior (value, not max_kl). Iter 50 also hit ep=1/4 kl=0.023 at the constant-LR schedule start of decay window (nothing to note). The run never hit max_kl=0.1 so the decision to remove the hard cutoff was correct.

Entropy stayed 3.43–3.81 throughout, clip fraction 0.15–0.24. No training-health red flags.

### 10. US overfit experiment — progress at iter 21

`results/capacity_test/ppo_us_overfit_v1/` launched at 02:22 UTC, now at iter 21/40. Warmstart=us_only_v5/ppo_best.pt, side=us only, fixtures=v56+v55+__heuristic__, heuristic-floor=0.3. Rollout US WR trajectory: iter1=0.265, iter4=0.215, iter10 ≈ 0.35 (estimated), iter20=0.385, iter21=0.415. Trending up, roughly matching us_only_v5 baseline trajectory. Value_loss stable 0.13–0.21. JSD iter 20 vs iter 10: card_jsd=0.0057 top1=0.902 val_mae=0.0485 — very small drift, healthy. KL 0.005–0.007 late, stable.

Too early to evaluate (iter 21/40 = ~half done). Watch for:
- iter 40 rollout_wr US ≥ 0.45 (above us_only_v5 baseline 0.36)
- 500-game heuristic bench US WR ≥ 0.40 at iter 40 (beats us_only_v5=0.360, the current US high-water)
- US WR vs heuristic in rollout plot does not plateau below 0.4
- value_loss does not spike late (sign of reward-shape overfit)

## Conclusions

1. **v6_iter20 remains the project record on the stated metric.** Combined WR vs heuristic 500g/side: v6_iter20=0.458 > v56=0.441 > v7_iter80=0.423 > v7_iter20=0.397. Do not update the record in continuation_plan.json to v7.

2. **v7 is genuinely stronger vs the BC cluster and vs past v6 on league Elo.** iter40 at +99 vs v56, iter60 at +84. In a "beat the league" framing v7 succeeded. The project goals in `continuation_plan.json` list "combined WR vs heuristic >0.50" as the top target, so the league-strength gain is orthogonal to the stated goal.

3. **The US side over-specialized to self-similar opponents.** USSR vs heuristic gained +16pp (0.558→0.722, new all-time project high for USSR side). US vs heuristic lost −20pp (0.325→0.124, new all-time project low for a symmetric policy). This is a textbook specialization pattern, not a training-instability pattern.

4. **The v7 fadeout fix worked for its designed purpose** — no running-best selection bug, no post-iter-50 panel collapse, heuristic stayed in the pool (1880 games) — but a different failure mode surfaced: league-style dominance in the pool produced US-side pool-specialization. Fixing the symptom (US-vs-heuristic collapse) needs a different change, not fadeout=999 alone.

5. **Panel-avg is a misleading north-star metric for this project.** It averages 7 league-style opponents and 1 heuristic; signal is 87.5% vs-league. Panel went up (+0.029) exactly when heuristic went down (−0.066). The panel as currently configured cannot be used as a running-best selector for a heuristic-WR goal.

6. **v7 is a plateau at iter 60+ on both metrics.** Panel-avg trajectory is flat within noise, heuristic-bench is flat-around-0.4. Running v8 as "v7 again, more iters" will not move either metric.

7. **The project needs to pick a north star**: heuristic-combined-WR (current plan) or BC-cluster Elo (what v7 actually moves). Both are legitimate but they diverge now. Recommendation: keep heuristic-WR as north star because it is the stronger test of generalization, and the cluster is already saturated near-0.5 against itself (v56 vs all BC = 0.49–0.50 WR, no information).

8. **US overfit experiment is on track but not yet decisive.** Iter 21/40, rollout_wr trending to 0.40+, healthy KL/value. Wait for iter 40 + 500-game bench.

## Recommendations

**Tier 1 — launch now (v8):**

Given the diagnosis (US over-specialized to self-similar opponents, USSR generalized well), the smallest useful change is to rebalance the rollout mix toward heuristic. Three tried-together:

1. Bump `--heuristic-floor` from 0.15 to **0.30** (doubles heuristic share of rollouts; still leaves 70% for league signal).
2. Warmstart from **v6_iter20** (the true project record), not v7_iter80 (which is US-regressed) and not v7_iter40 (which is +99 Elo vs league but still −3.5pp on heuristic combined). v6_iter20 gives the policy the smallest US-deficit starting point.
3. Drop the past-self heavy weighting: set `--league-past-self-cap 10` if the flag is implemented (per continuation_plan notes it's not), else keep `league_mix_k=6` and reduce the expected number of past-self samples indirectly by removing redundant BC-cluster fixtures. Keep `v56`, `__heuristic__`, `ussr_only_v5`, `us_only_v5`; drop `v20/v44/v54/v55` (they are near-duplicates of v56 per BC cluster Elo and contribute to the self-similar pool problem).

Expected v8 outcome: US-vs-heuristic recovers toward 0.30+, USSR-vs-heuristic stays >0.55, combined ≥ 0.45. If v8 ≥ v6_iter20's 0.458 at any iter, it is a new project record.

**Tier 2 — parallel / after v8 launches:**

4. Continue the US overfit experiment to iter 40, bench it vs heuristic, compare to us_only_v5.
5. Implement heuristic-only running-best gate (small PR). Critical because panel-avg is misleading as currently configured. Either: (a) change `ppo_best.pt` selection to use only the `heuristic` panel column, or (b) add a dedicated `heuristic_combined_wr` field and select on that.
6. Consider trimming the panel itself to just `[v56_scripted, __heuristic__]` in v9+. Reduces eval cost (~15% of iter wall-clock) and removes the false-positive signal from self-similar panel opponents.

**Tier 3 — if v8 also stalls on heuristic metric:**

7. Pivot north-star metric. The BC cluster is saturated at ~0.5 WR against each other; heuristic-WR progress requires something structurally beyond PFSP (teacher search, dense-reward value shaping, multi-head side-specialist architecture). Candidates:
   - Teacher-assisted training: run a shallow MCTS (e.g., 30 simulations with heuristic rollout) on 100 curated hard US-side positions, produce action targets, KL-regularize the US policy toward those targets for 10 iters.
   - Dense reward: re-enable `--reward-alpha` > 0 with VP-delta shaping per turn, particularly shaped against USSR's expansion rate (currently `--reward-alpha 0.5` in the args file, check if it was active).
   - Architecture change: the country-attn + control-feat-gnn trunk is shared between sides. A side-dedicated head for US (not USSR) might give more capacity to the constrained side.

**Not recommended:**
- Do not simply run v7 for 120–160 iters. Panel-avg plateaued; heuristic-combined is worse than baseline; more iters amplifies the US-specialization direction.
- Do not warmstart v8 from v7_iter80 (US=0.124 is below noise floor; restart US recovery from a better point).
- Do not increase `league_mix_k` past 6 (more opponents = more per-sample noise; current diagnosis says mix *composition*, not mix *size*).

## V8 Launch Command

Design: warmstart from v6_iter20 (real project record), keep reduced fixture list (v56 + two specialists + __heuristic__), bump heuristic-floor to 0.30, same PFSP params, same LR/clip/entropy, 80 iters with `eval_every=20`.

```bash
mkdir -p results/ppo_country_attn_v8

OMP_NUM_THREADS=6 KMP_BLOCKTIME=0 nohup uv run python scripts/train_ppo.py \
  --checkpoint results/ppo_country_attn_v6/ppo_iter0020.pt \
  --reset-optimizer \
  --out-dir results/ppo_country_attn_v8 \
  --version country_attn_v8 \
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
    results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
    results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
    __heuristic__ \
  --eval-every 20 \
  --side both \
  --self-play-heuristic-mix 0.2 \
  --seed 43000 --device cuda \
  --wandb --wandb-project twilight-struggle-ai \
  --wandb-run-name ppo_country_attn_v8 \
  --ema-decay 0.995 --target-kl 0.015 \
  --reward-alpha 0.5 \
  --dense-reward-alpha 0.0 --dense-reward-anneal-steps 500000 \
  --league results/ppo_country_attn_v8 \
  --league-save-every 10 \
  --league-mix-k 6 \
  --rollout-workers 1 \
  --league-fixtures \
    data/checkpoints/scripted_for_elo/v56_scripted.pt \
    results/capacity_test/ppo_ussr_only_v5/ppo_best_scripted.pt \
    results/capacity_test/ppo_us_only_v5/ppo_best_scripted.pt \
    __heuristic__ \
  --heuristic-floor 0.30 \
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
  > results/ppo_country_attn_v8/train.log 2>&1 &
```

Key differences from v7 command:
- `--checkpoint results/ppo_country_attn_v6/ppo_iter0020.pt` (was v7_iter13 / v6_iter20; correct anchor)
- `--heuristic-floor 0.30` (was 0.15; doubles heuristic share)
- `--league-fixtures` trimmed from 8 to 4 entries (dropped v55/v54/v44/v20 BC-cluster near-duplicates; keep v56 + USSR/US specialists + heuristic)
- `--eval-panel` matched to trimmed fixtures (smaller panel, faster eval, less self-similar masking)
- `--seed 43000` (different from v7's 42000; isolate noise)
- `--upgo` kept (it was in v6 / v7 launch commands and training was healthy)

Success criteria for v8:
- iter 20 combined ≥ 0.46 (at or above v6_iter20 baseline). If < 0.44, heuristic-floor+pool-trim was not enough.
- iter 40 combined ≥ v6_iter20 (≥ 0.458); new project record if so.
- iter 80 US vs heuristic ≥ 0.30 (recovered from v7's 0.124 collapse). US ≥ 0.36 = match us_only_v5 specialist.
- iter 80 USSR vs heuristic ≥ 0.60 (holds v7 gain).
- Panel-avg at iter 80 should be *lower* than v7's 0.579 but combined-heuristic should be higher — this inversion would confirm the diagnosis.

Abort criteria:
- iter 20 combined < 0.40 → fundamental issue beyond pool composition; pivot to teacher-search / dense reward path.
- iter 40 US vs heuristic still < 0.15 → heuristic-floor=0.30 insufficient; try 0.50 or drop BC specialists too.

## Open Questions

1. **Is panel vs heuristic at 60 games too noisy to trust as a regression signal?** 60 games has stderr ~±6pp. Heuristic went 0.433→0.450→0.433→0.367. The iter80 drop is within 2σ of mean. Formal 500-game bench confirms the trend (iter80 combined=0.423 is real, not panel noise). Low priority; resolved.

2. **Is there a v6_iter20 bench retest to cross-check +1.7pp over v56?** continuation_plan.json listed this as open question. With v7 now in hand, rerunning v6_iter20 on seed 60000/60500 would tighten the "new project record" claim. Cheap (~2 min GPU). Should do before launching v8 to anchor the comparison cleanly.

3. **Should the US-only overfit experiment use v7_iter80 as USSR opponent?** v7_iter80 USSR is at 0.722 WR vs heuristic — the strongest symmetric USSR side on record. An US-only run against THIS opponent might be the best stress test for US specialization. Future work; not a v8 blocker.

4. **Will v8 with `heuristic-floor=0.30` hurt USSR-vs-league-cluster?** Possibly. The 16pp USSR gain vs heuristic may partly be from self-similar USSR training against self-similar USSR pool. Doubling heuristic may bring USSR back to ~0.60 vs heuristic (from 0.72) while pulling US up. Net combined could still go up, but total USSR-side Elo may drop. Watch carefully.

5. **Should v8's eval panel exclude the BC cluster entirely?** The panel `[v56, ussr_only_v5, us_only_v5, heuristic]` has one heuristic out of 4, 25% weight (vs v7's 12.5%). Still not enough if heuristic-WR is the north star. Consider dropping panel entirely in favor of 100-game heuristic-only eval at same cadence.

6. **Is the candidate-tournament Elo misleading?** iter40 at +99 vs v56 seems very high given iter40's heuristic combined is only 0.410. Possible that the BC cluster is co-vulnerable to a specific US-side style that v7 exploits (self-referential weakness, not absolute strength). A cross-check tournament against Gen1 self-play or against an independently-trained model could test this. Low priority; not a v8 blocker.

7. **Does `--heuristic-floor` actually work as expected?** continuation_plan.json notes `--league-heuristic-pct=0.3` is deprecated and "coin-flip approach gives P(zero heuristic games) = (1-pct)^k per iteration." Need to verify that `--heuristic-floor 0.30` does not have similar probabilistic-zero-games-per-iter behavior. If it's a PFSP-weight floor (not a deterministic share), the iter-to-iter variance could be large. Check the train_ppo.py implementation before launching v8. If it's the same coin-flip, add `__heuristic__` to `--league-fixtures` with a weight boost instead.
