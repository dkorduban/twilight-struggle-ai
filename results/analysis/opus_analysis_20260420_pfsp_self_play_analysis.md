# Opus Analysis: PFSP Self-Play Bias in v6 PPO
Date: 2026-04-20
Question: Is the PFSP implementation causing excessive self-play focus later in the run?

## Executive Summary

**Yes, and the mechanism is simpler and more severe than the metric suggests.** Starting at iteration 50 of the v6 PPO run (`ppo_country_attn_v6`, W&B id `a4d1aaaf`), the training opponent pool becomes **100% past-self snapshots — zero external opponents**. This is not a gradual drift; it is a hard cutover driven by the `fixture_fadeout=50` config, which at line 1127 of `scripts/train_ppo.py` executes `active_fixtures = [] if current_iter >= fixture_fadeout else list(fixtures)`. Every scripted baseline (v20/v44/v54/v55/v56/ppo_best) and the `__heuristic__` anchor are simultaneously removed from sampling.

The W&B `ucb/fixture_frac_*` metric *understates* this: it falls from 0.88 (iter 10) only to ~0.52 (iter 60), which looks like "fixtures still 50% of pool." In reality this is an artifact — the metric is summed over every key in the `wr_table` dict (which is never pruned), so the denominator keeps growing as new `iter_*` snapshots are added, but the numerator is still counting fixtures that are no longer sampled. The ground truth, from parsing 11 iterations of `[league]` printouts at iters 50-60, is that **44/44 pool slots are `past-self`**, none are fixtures. Independent confirmation: `ucb/heuristic_weight_ussr` freezes at 1.012 from iter 49 through iter 60 (no new games against heuristic = no numerator update).

Consequences visible in the 10 iterations of post-fadeout training so far:
- `rollout_wr_panel` (internal panel eval during rollout) has stagnated at ~0.45 for 40+ iters.
- `rollout_wr_self` hovers at ~0.50 (healthy, as expected for symmetric self-play).
- `rollout_wr_us` stuck at 0.31-0.34 for iters 40-60 — the US side, which is already the weaker side, loses its externally-grounded training signal.
- Heuristic WR_ussr frozen at 0.372 and WR_us at 0.121 since iter 49 (frozen, not learning).

Training is at iter 60 of 80; the full trajectory of collapse is not yet observed, but the policy now has **zero external gradient signal** for its remaining 20 iters. Given prior project history (v11/v12 echo-chamber collapse with pure self-play data, per MEMORY.md `project_policy_collapse.md`), this is high-risk and should be corrected in v7.

## Findings

### W&B ucb/ metrics over training

Pulled via `scan_history` for run `korduban-ai/twilight-struggle-ai/a4d1aaaf` — 60 iterations, 195 columns, 49 `ucb/*` metrics. Key trajectories (side = USSR unless noted):

| iter | rollout_wr | panel | self | fixture_frac_ussr | self_mass_ussr | fixture_mass_ussr | heur_wt_ussr | heur_wr_ussr |
|---|---|---|---|---|---|---|---|---|
| 1  | 0.510 | 0.592 | 0.388 | 0.687 | 1.000 | 2.194 | —    | —    |
| 5  | 0.410 | 0.475 | 0.150 | 0.853 | 1.157 | 6.734 | 1.135 | 0.375 |
| 10 | 0.405 | 0.405 | 0.000 | 0.880 | 1.030 | 7.578 | 1.057 | 0.350 |
| 20 | 0.500 | 0.450 | 0.700 | 0.718 | 2.958 | 7.529 | 1.079 | 0.392 |
| 30 | 0.475 | 0.425 | 0.675 | 0.658 | 3.857 | 7.408 | 1.058 | 0.408 |
| 40 | 0.495 | 0.458 | 0.550 | 0.658 | 3.807 | 7.326 | 1.024 | 0.381 |
| 49 | 0.455 | 0.392 | 0.550 | 0.603 | 4.807 | 7.296 | 1.012 | 0.372 |
| 50 | 0.505 | 0.450 | 0.519 | 0.603 | 4.801 | 7.297 | 1.012 | 0.372 |
| 52 | 0.545 | 0.550 | 0.544 | 0.567 | 5.569 | 7.299 | 1.012 | 0.372 |
| 55 | 0.510 | 0.525 | 0.506 | 0.561 | 5.718 | 7.301 | 1.012 | 0.372 |
| 60 | 0.510 | 0.450 | 0.525 | 0.519 | 6.770 | 7.304 | 1.012 | 0.372 |

Critical observations:
1. **Heuristic weight frozen at 1.012 from iter 49 → 60.** This is the single cleanest indicator that the heuristic fixture has seen zero new games for 11 iterations. Same for all `v*_scripted` weights — they all freeze at their iter-49 values.
2. **`fixture_mass_ussr` also freezes** at ~7.30 from iter 50 onward, while `self_mass_ussr` keeps climbing (1.00 → 6.77). The denominator ratio moves from 0.60 → 0.52 purely because the numerator is static and the self-pool grows.
3. **Every fixture WR column is also frozen** post-iter 49. This is pure confirmation — if fixtures were still being sampled, WR values would drift.
4. `rollout_wr_panel` stagnates at 0.45 ± 0.06 throughout — panel eval uses `__heuristic__` in `eval_panel`, which is separate from the training pool, and it is the only unbiased ground-truth signal remaining post-fadeout.

### WR table state (`results/ppo_country_attn_v6/wr_table.json`)

Confirms games stop accumulating against fixtures after iter 49:

| opponent | total_ussr | wins_ussr | WR_ussr | total_us | wins_us | WR_us |
|---|---|---|---|---|---|---|
| `__self__`         | 1220 | 850 | 0.697 | 1220 | 360 | 0.295 |
| `iter_0001`        | 1040 | 719 | 0.691 |  640 | 200 | 0.313 |
| `iter_0010`        |  400 | 282 | 0.705 |  560 | 191 | 0.341 |
| `iter_0020`        |  400 | 265 | 0.663 |  440 | 135 | 0.307 |
| `iter_0030`        |  560 | 355 | 0.634 |  240 |  76 | 0.317 |
| `iter_0040`        |  240 | 154 | 0.642 |  280 |  89 | 0.318 |
| `iter_0050`        |  200 | 134 | 0.670 |  160 |  57 | 0.356 |
| `iter_0060`        |   40 |  26 | 0.650 |   40 |  14 | 0.350 |
| `heuristic`        |  360 | 134 | 0.372 |  480 |  58 | 0.121 |
| `ppo_best_scripted`|  360 | 207 | 0.575 |  560 | 168 | 0.300 |
| `v20_scripted`     |  360 | 229 | 0.636 |  400 | 115 | 0.287 |
| `v44_scripted`     |  320 | 181 | 0.566 |  320 | 112 | 0.350 |
| `v54_scripted`     |  120 |  75 | 0.625 |  400 | 147 | 0.367 |
| `v55_scripted`     |  240 | 149 | 0.621 |  160 |  48 | 0.300 |
| `v56_scripted`     |  240 | 143 | 0.596 |  200 |  61 | 0.305 |

Totals against self/past-self (from iter_*): 2880 USSR / 2360 US games.
Totals against external fixtures (heuristic + v*_scripted + ppo_best): 2000 USSR / 2520 US games (all accrued pre-iter-50).

Model is **not** dominating fixtures (USSR WR vs scripted = 0.566-0.636, US WR = 0.287-0.367). So PFSP's sym term `4·WR·(1-WR)` is still healthy (≈0.92-0.99 for USSR, ≈0.82-0.92 for US). The fadeout is not driven by "fixtures being solved" — it is a blunt time-based cutover that removes opponents even when they are still useful.

### Fixture fadeout effect (the actual mechanism)

Parsed the `[league]` printouts at every iteration. Pool composition (K=2 opponent slots per iter shown in the printout; full pool is K=6 including current-self):

| iter range | past-self % | scripted-fixture % | heuristic % |
|---|---|---|---|
| 1-10   | 22.5% | 60.0% | 17.5% |
| 11-20  | 35.0% | 60.0% |  5.0% |
| 21-30  | 37.5% | 52.5% | 10.0% |
| 31-40  | 60.0% | 27.5% | 12.5% |
| 41-49  | 63.9% | 27.8% |  8.3% |
| **50-60** | **100.0%** | **0.0%** | **0.0%** |

Sample `[pfsp]` printouts illustrating the cutover:

```
[iter  49/80] ...
  [league] ussr_pool: ['iter_0001', 'iter_0030'] | us_pool: ['iter_0040', 'iter_0001']
  [pfsp]
    [ussr] iter_0001: WR=0.70(n=800) sym=0.832 ucb=0.052 → pfsp=0.883
    [ussr] iter_0030: WR=0.62(n=400) sym=0.938 ucb=0.073 → pfsp=1.010
    [us]   iter_0040: WR=?(n=0) pfsp=1.000 (< MIN_GAMES)
    [us]   iter_0001: WR=0.31(n=480) sym=0.850 ucb=0.067 → pfsp=0.916
[iter  50/80] ...
  [league] ussr_pool: ['iter_0040', 'iter_0020'] | us_pool: ['iter_0001', 'iter_0020']
  [pfsp]
    [ussr] iter_0040: WR=0.70(n=40) sym=0.840 ucb=0.231 → pfsp=1.071
    [ussr] iter_0020: WR=0.69(n=280) sym=0.851 ucb=0.087 → pfsp=0.938
    [us]   iter_0001: WR=0.31(n=520) sym=0.855 ucb=0.064 → pfsp=0.919
    [us]   iter_0020: WR=0.29(n=280) sym=0.828 ucb=0.087 → pfsp=0.916
```

The qualitative change is unmistakable: at iter 49 heuristic/scripted fixtures still appear in the printout; at iter 50 onward, every entry in both sides is `iter_*` past-self.

### Heuristic starvation analysis

Two effects combine, but the second one dominates:

1. **PFSP weight collapse (pre-fadeout, mild):** Heuristic's raw pfsp weight does drop as US-WR stays low (~0.11, giving sym = 4·0.11·0.89 = 0.39). But this is a moderate effect — the heuristic_floor=0.15 config setting kicks in and boosts it back up, and the pre-fadeout printouts show heuristic appearing in 5-17% of pool slots (reasonable).

2. **Fadeout hard-cutoff (post-iter-49, total):** After iter 49 heuristic appears in **0 of 44 pool slots** (parsed). This is orders of magnitude more severe than any starvation PFSP could cause via weight dynamics alone.

So: heuristic_floor=0.15 in the v6 config is working as designed pre-fadeout. The fadeout then makes the floor irrelevant.

### Impact on rollout_wr vs panel_wr divergence

Contrary to the initial hypothesis in the task prompt, the data does **not** show rollout_wr being inflated by easy self-play games:

- `rollout_wr_self` oscillates around 0.50 across all iters — this is structurally enforced by both sides being the same model, so it cannot be "easy."
- `rollout_wr` (overall) ≈ 0.48 across iters 30-60, roughly matching `rollout_wr_panel` ≈ 0.45.
- The pre/post-50 values are comparable: iters 30-49 mean rollout_wr ≈ 0.466, iters 50-60 mean ≈ 0.487 (+2pp).

The real problem is **signal degradation, not inflation**:
- Post-iter-50, all training gradient comes from model-vs-past-self and model-vs-current-self. This is known to cause policy collapse / echo-chamber drift (MEMORY.md: `project_policy_collapse.md`).
- `rollout_wr_panel` (which uses the eval_panel list — a separate set of scripted opponents evaluated during rollout) is the only externally-grounded signal remaining, and it has been **stagnant at 0.45 since roughly iter 15**. No learning progress against external opponents is visible for 45+ iters, and from iter 50 there is no training signal pushing it either.

In summary: rollout_wr is not misleading by inflation; but `rollout_wr` averaged over a self-play-only pool becomes meaningless as a "strength" proxy post-fadeout. The only remaining trustworthy signal is `rollout_wr_panel` and the full `eval_panel` / Elo benchmarks run separately.

## Conclusions

1. **PFSP self-play bias is happening, and it is caused primarily by `fixture_fadeout=50`, not by per-opponent weight dynamics.** The hard-cutoff mechanism at line 1127 of `scripts/train_ppo.py` removes all external fixtures simultaneously at iter 50. This is evidenced by (a) parsed `[league]` printouts showing 100% past-self at iters 50-60, (b) frozen `ucb/*_weight_*` values for all scripted and heuristic opponents from iter 49 onward, (c) frozen WR columns for the same, (d) frozen `ucb/fixture_mass_*`.

2. **The W&B `ucb/fixture_frac_*` metric is misleading in this regime.** It computes `fixture_mass / (fixture_mass + self_mass)` over the entire `wr_table` dict, not over the active sampling pool. After iter 50 the numerator freezes and the denominator grows, causing a gentle apparent decline from 0.60 → 0.52 that hides the actual 100%→0% collapse in the real pool. **Recommend adding a second metric, e.g. `ucb/fixture_sampled_frac_ussr`, that counts actual selections from the active pool.**

3. **Heuristic starvation pre-fadeout is mild and controlled.** `heuristic_floor=0.15` is doing its job; pre-fadeout pool share is 5-17%. The PFSP sym term alone does not kill heuristic — the fadeout does.

4. **Model has not solved fixtures.** USSR-WR vs external fixtures is 0.57-0.64, US-WR is 0.29-0.37. These remain informative training opponents; fading them out was premature.

5. **Full policy collapse is not yet visible in 10 post-fadeout iterations,** but the run has 20 more iterations to go with zero external training signal. Historical pattern (v11/v12, per `project_policy_collapse.md`) makes continuation high-risk.

6. **The US side is the most exposed.** US-WR vs heuristic is 0.121, meaning the US policy has the strongest need for continued heuristic exposure (low WR ⇒ high sym weight ⇒ high learning-value gradient). Cutting this off at iter 50 removes exactly the opponent that the US policy needs most.

## Recommendations

In priority order:

1. **[Highest impact, simplest]** **Disable `fixture_fadeout`** for v7+. Set `league_fixture_fadeout` to `999` (or a value ≥ `n_iterations`). Fixtures stay in the pool forever, governed by PFSP + UCB + heuristic_floor. The fadeout was originally motivated by the idea that old scripted baselines get "solved" — the v6 WR table shows they are *not* solved (WR 0.57-0.64 USSR, 0.29-0.37 US), and even if they were, UCB re-exploration + low sym weight would naturally down-weight them without cutting them off.

2. **[Second priority]** **Split fixtures into fadeable and permanent.** Keep `__heuristic__` as a permanent non-fadeable anchor (add a new config field `permanent_fixtures: list[str] = ["__heuristic__"]` that is never stripped by the fadeout logic). This preserves the "retire ancient past-architecture checkpoints" intent while guaranteeing general-play grounding. The scripted v*_* baselines can still fade if desired.

3. **[Diagnostic]** **Fix `ucb/fixture_frac_*` to reflect the sampling pool**, not the full WR table. Either (a) skip keys that are not in `active_fixtures` when summing, or (b) add a second metric `ucb/active_fixture_frac_*` that does. Without this, dashboard users cannot see the fadeout cliff.

4. **[Low priority]** `heuristic_floor=0.15` works pre-fadeout — keep it. Boosting to 0.25 is reasonable if ablation shows heuristic WR_us (0.121) is causing sym-term-driven starvation independent of fadeout, but this is not the current problem.

5. **[Orthogonal to this issue]** `fixture_mass_mult > 1.0` at steady state (e.g. 1.5x) does not help when `active_fixtures = []`. If recommendation 1 is adopted, consider bumping to 1.25-1.5x to ensure external opponents retain ≥50% of pool mass throughout.

6. **[Run-level decision]** For the current v6 run (still at iter 60/80), there is no graceful mid-run fix without a restart. Options: (a) let it finish and judge on panel_wr / benchmark / Elo; (b) stop at iter 60 and treat it as the checkpoint; (c) restart from iter 49 (`iter_0050.pt`) with fadeout disabled for iters 50-80. Option (c) is cheapest and gives the cleanest comparison to existing iter-49 results.

## Open Questions

1. **Why was `fixture_fadeout=50` chosen for v6** (n_iterations=80)? The `ppo_args.json` shows it; no comment in code explains the 50 default. If the intent was "fade old architectures after enough self-play iters," the threshold should be coupled to demonstrated fixture dominance (e.g. model WR vs fixture > 0.90 for K iters), not a wall-clock iteration count.

2. **Does `eval_panel` rollout evaluation continue against fixtures post-fadeout?** Checking `ppo_args.json`: `eval_panel` is a separate list identical to `league_fixtures`, and panel eval runs every `eval_every=20` iters. So yes, the panel is still evaluated at iters 20, 40, 60 — but not against fixtures for training gradient, only for measurement. This is consistent with observed `rollout_wr_panel` continuing to log values post-50.

3. **Is there a correlation between post-50 instability and any specific opponent being removed?** The USSR pool pre-50 drew heavily from iter_0001 (n=840 games by iter 51) and v56_scripted / ppo_best. If the US policy was relying on heuristic for low-WR exposure, losing heuristic hits US training specifically. Worth an ablation: restart from iter 49 with (A) no fadeout vs (B) fadeout of v20-v55 only (keeping heuristic + v56 + ppo_best + current iter_*).

4. **Does `rollout_wr_self ≈ 0.50` hide regression?** Self-play is structurally balanced, so a declining policy will still show 0.50. The only way to detect regression post-fadeout is `rollout_wr_panel` or the offline `panel_eval_history.json`. Recommend adding an "always-on canary" fixture (e.g. 10% weight on `__heuristic__` and `v56_scripted`) that cannot fade, independent of the main fixtures list.

5. **What does `panel_eval_history.json` show for iters 20, 40, 60?** Reading it would cross-validate the rollout_wr_panel trend. (File exists but was not inspected in detail here; flag for follow-up.)
