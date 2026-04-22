# Opus Analysis: Overnight Experiment History v6→v16
Date: 2026-04-20T17:50:00Z
Question: What happened overnight from v6 to v16?

## Executive Summary

Between v6 (project record 0.459 combined, seed=42000 from v56 warmstart) and v16, every intervention attacked pool composition, warm-start data, or architecture — and none moved the needle beyond v13's 0.427. PPO v7–v12 were seed sweeps under the v13 recipe that produced an 18pp seed-variance band (0.215–0.427) while the 30-game panel repeatedly flagged echo-chamber iter80 checkpoints as "best" despite 500g benches showing they had regressed on heuristic play; GNN pivots (v14/v15) collapsed because BC warm-start never crossed ~0.19 combined and PPO cannot close a 25–33pp gap in 80 iters; and BC v3/v4/v5 confirmed that supervised fine-tuning from either heuristic data, learned-model data, or MCTS data could not produce a launch-quality warm-start. The ceiling-break analysis diagnosed that the *actual* root cause is elsewhere: `dir_alpha=0`, `rollout_temp=1.0`, `val_calib_coef=0`, and an equal-weighted v56+heuristic selector were silently identical across v6–v15, so exploration was argmax-deterministic and the running-best selector was actively promoting self-similar overfits. PPO v16 (launched 17:45Z) is the first run to enable Dirichlet root noise (`--dir-alpha 0.3 --dir-epsilon 0.25`), rollout temperature (`--rollout-temp 1.2`), US-win value upweight (`--val-calib-coef 0.5`), and a 3x-heuristic-weighted running-best selector, resuming from v13_iter20 at seed=42000.

## Findings

### PPO variants v7–v12: echo chamber and seed variance

v7 through v12 were all country_attn_side PPO runs with near-identical recipes (lr=5e-5, clip=0.12, ent=0.01, heuristic-floor=0.15, league-fixture-fadeout=999), varying almost exclusively by seed and warm-start. v11/v12/v13 are *literally identical recipes* differing only in seed (46000/47000/42000) and produced combined scores of 0.250/0.295/**0.427** — a 17.7pp spread attributable to seed alone. v7 started from v7/iter0013 (0.397), v8 raised heuristic-floor to 0.30 (→0.351 at iter80), v9 and v10 tried both v6-derived and v56-derived warm-starts (0.304 and 0.215 respectively), and v11/v12 bumped pfsp-exponent to 1.0 (0.250, 0.295). None beat v13.

The deeper issue surfaced by post-mortems: the 30-game panel SE≈0.091 means panel readings routinely produce false positives. v11 panel hit 0.517 at iter70, v12 hit 0.508 at iter30, v13 panel read 0.583 at iter80 — but v13's iter80 at a 500g bench is **0.257** (USSR=0.402, US=0.112) versus iter20's **0.427**. The selector (`panel_avg = (v56_WR + heuristic_WR)/2` with `_PANEL_WEIGHTS={}`) was rewarding late-iter checkpoints that had gained +0.034 vs v56 while silently regressing by 0.166 vs heuristic on 500g ground truth. The "PFSP echo chamber causes training to peak at iter20" belief is therefore partially wrong: the training policy keeps gaining skill vs self-similar opponents; the *selector* can't tell this apart from real improvement because its heuristic signal is noise-masked at 30g.

### GNN architecture pivot (v14, v15)

After the v7–v12 sweep exhausted the country_attn_side recipe, the plan pivoted to swap the architecture to `control_feat_gnn_film` (GNN+FiLM). v14 trained PPO on top of a GNN BC warm-start fed purely from heuristic-nash games and collapsed to **combined=0.192** (USSR=0.336, US=0.048) at iter20. The post-mortem blamed warm-start weakness: GNN BC started at ~0.19 versus country_attn's v56 start at ~0.441 — PPO cannot recover a 25pp gap in 20 iterations because PFSP keeps folding the policy into its own pool.

v15 tried to fix warm-start by using *v13 self-play games* (3000 games, 334K rows) as the BC corpus. BC v2 mixed 70% v13 with 30% nash and saw value_mse degrade from 0.58 to 0.80 mid-training (mix contamination, killed at epoch 15). BC v3 used pure v13 3000g data, 80 epochs — card top-1 reached 0.686 at epoch 12 but val_value_mse worsened to 0.81 (train overfit 0.09–0.17, val 0.81+), gate bench combined=0.140 (fail). BC v4 added soft teacher distillation from v13_iter20 forward passes (`v13_3000g_soft_teacher.parquet`), improved val_value_mse to 0.675, and produced PPO v15 = **combined=0.112** (USSR=0.196, US=0.028) at iter10 running_best. The 33pp warm-start gap never closed. The consolidated lesson: BC→PPO is a broken pipeline for new architectures; argmax BC on self-play captures only the argmax slice of the teacher policy and PPO's variance compounds onto that gap.

### BC warm-start experiments (v3, v4, v5)

BC v3 (GNN, pure v13 3000g, 80 epochs): gate bench 0.140 — fail. Root cause: winner_side target is too noisy for learned-model games; value head memorizes training set but val_value_mse stays at 0.81.

BC v4 (GNN, v13 + teacher KL distillation from v13 soft logits): better value head, PPO v15 → 0.112. Teacher distillation helped labels but couldn't overcome the architectural fresh-start gap.

BC v5 (country_attn_side, fine-tune v13_iter20 on MCTS visit-count soft targets from `mcts_dir_1000g.parquet`, 40 epochs, teacher_weight=0.7, teacher_value_weight=1.0): **gate bench combined=0.090** — catastrophic forgetting. Starting from a working 0.427 checkpoint, 40 epochs on MCTS-only data shifted the action distribution away from heuristic-opponent regions. The permanent lesson captured in `pivot3_mcts_distillation.lesson`: never fine-tune exclusively on MCTS data without mixing heuristic-opponent games. MCTS positions are AI-vs-AI distributions and do not transfer to heuristic benches.

### Root cause diagnosis (from ceiling_break analysis)

The ceiling_break analysis (run immediately before v16) reframed the problem from "beat 0.427" to "why does the recipe have 10pp seed variance and an adversarial selector." The analysis inventoried PPO args across v6–v15 and found four levers that have been scaffolded in `scripts/train_ppo.py` for months but never turned on in any run:

1. `dir_alpha=0.0` in all runs — Dirichlet root noise is silently disabled (`dir_epsilon=0.25` is nonzero but multiplied by zero alpha). `_call_rollout_with_optional_dirichlet` at line 1237 probes the C++ binding and falls back silently.
2. `rollout_temp=1.0` in all runs — no exploration temperature on the sampling distribution.
3. `val_calib_coef=0.0` in v13 (and 0.1 max elsewhere) — the US-win value upweight documented in `feedback_us_win_value_weighting.md` as active in v56 has been silently regressed in every PPO run since.
4. `_PANEL_WEIGHTS={}` in source — the running-best selector averages v56_WR and heuristic_WR equally, letting v56-overfitting drag iter80 above iter20 even when heuristic_WR has collapsed on 500g.

These are CLAUDE.md's Month-3 priority #1 and #2 ("Dirichlet noise + temperature-based action sampling" and "self-play exploration noise"). They are not additional complexity — they are finished scaffolding that nobody has switched on. The analysis also noted US-side WR has declined since v56 (0.325 → 0.246 at best, 0.028 at worst), and that `us_only_v5` reaches US=0.360 when trained US-only, so US-side collapse is a training-distribution problem (symmetric rollouts on a USSR-favored engine with zero US-win weighting), not a capacity problem.

PPO v16 was launched at 17:45Z with four simultaneous changes off v13_iter20: `--dir-alpha 0.3 --dir-epsilon 0.25` (core intervention, 25% Dirichlet-mixed card noise at rollout), `--rollout-temp 1.2` (gentle widening of sampling distribution), `--val-calib-coef 0.5` (restore US-win upweight), and `_PANEL_WEIGHTS={"__heuristic__": 3.0}` (heuristic 3x weight in running-best selection). Seed=42000 retained for fair v13 comparison. Run length dropped from 80 to 30 iters (eval every 5) since v13 analysis showed no value past iter20. iter1 log shows `rollout_wr=0.455 (ussr=0.646, us=0.263), panel=0.545`, diagnostics clean, ~33s/iter — all three interventions confirmed active.

## Conclusions

1. **v13=0.427 is a seed outlier, not a structural ceiling.** The v11/v12/v13 identical-recipe trio produced 0.250/0.295/0.427, meaning the recipe's iter20 distribution is centered near 0.30–0.33 with σ≈6–8pp. v13 is ~1.5σ above its own mean. The real problem is distribution mean + variance, not a specific barrier at 0.427.
2. **The running-best selector has been promoting worse checkpoints.** v13 iter80 running_best (0.257 combined) vs iter20 (0.427) is a 17pp anti-correlated selection. Equal-weighted panel on a noisy heuristic arm and an echo-chamber v56 arm lets self-similar overfits win. This mechanism was operating in every v6–v15 run.
3. **BC→PPO for new architectures is a falsified pipeline.** Four attempts (BC v1 heuristic, BC v2 mix, BC v3 pure v13, BC v4 teacher-distill v13) all capped near 0.11–0.20 warm-start, and PPO could not close the 25–33pp gap to v56's 0.441 within 80 iters. Going forward, new architectures need weight transfer or direct MCTS distillation, not cold-start BC.
4. **MCTS-only fine-tuning destroys heuristic WR.** BC v5 took a working 0.427 checkpoint and fine-tuned it on MCTS data for 40 epochs, ending at 0.09. The distribution shift from heuristic-opponent games to AI-vs-AI games is catastrophic without mixed data.
5. **Four exploration/selector levers were never turned on in v6–v15 despite being fully scaffolded.** Dirichlet noise, rollout temperature, US-win value upweight, and heuristic-weighted selector are infrastructure-complete and listed as Month-3 priorities in CLAUDE.md. v16 is the first run to use any of them.
6. **US-side collapse is a training-distribution problem, not capacity.** us_only_v5 hits US=0.360; every symmetric PPO since v56 is ≤0.246 US. Asymmetric engine bias + removed US-win weighting + symmetric PFSP opponents all compound to starve the US gradient.

## Recommendations

1. **Monitor v16 iter10 and iter20 closely.** Primary success metric is 500g/side bench at seed=50000/50500. Iter20 combined ≥0.45 confirms the intervention; 0.43–0.45 matches v13 at reduced variance (proceed to a 3-seed confirmation run at 42001/42002/42003); <0.42 means the single intervention did not help and we fall back to multi-seed harvesting.
2. **Add an out-of-band 100-game heuristic-only bench at iter10 and iter20** and log to wandb as `bench/heuristic_100g_combined`. Do NOT trust the 30g panel this round as the running-best selector when the signal is actually important — use the 100g bench for selection.
3. **Verify Dirichlet binding is actually live.** Grep first-iter log for an explicit "dirichlet: enabled" line or equivalent. If `_call_rollout_with_optional_dirichlet` silently fell back (C++ binding lacks kwargs), lever (A) degrades to temperature-only and expected impact drops to +2–3pp.
4. **If v16 underperforms, run lever (C) — multi-seed iter20 harvest at seeds 42001/42002/42003/42004** on the v13 recipe before trying anything new. 4x 25-iter runs sequentially overnight; best of 4 draws should land 0.42–0.47. Attacks variance directly.
5. **Never again run a PPO experiment without confirming `val_calib_coef > 0`.** The silent regression from v56 to v6 has cost 5+ experiments of US-side underperformance. Consider making this a required arg with an explicit default.
6. **Replace 30-game panel with 100-game heuristic-only bench every 10 iters** as a standing change to `scripts/train_ppo.py`, independent of v16 outcome. This is lever (D); ~15s extra per eval and removes the noise that burned v11/v12 "panel=0.5" false positives.
7. **If v16 shows that Dirichlet+temperature+selector genuinely raised the distribution mean, DO NOT chain more interventions onto the same run.** Layer adds one at a time so we can attribute effect size. v17 should add one new lever (e.g. val_calib_coef swept, or US-specialist ensemble) rather than stacking.

## Open Questions

1. **Is v13_iter20=0.427 itself reproducible at seed=42000?** Only one draw. If v16 underperforms, the charitable assumption "v13 is the recipe's upper tail" may actually be "v13 is an implausibly lucky draw." Answering definitively requires 3x re-runs at seed=42000, which has not been done.
2. **Does the C++ binding on this build accept `dir_alpha/dir_epsilon` kwargs?** The probe is silent on fallback. Worth confirming at iter1.
3. **Would disabling PFSP entirely (fixture-only league) produce a cleaner signal?** Not in the ranked interventions because Finding 3 suggests the echo chamber's true magnitude is smaller than believed — most of the "decline past iter20" is selector noise, not policy collapse. Deserves a side experiment only if v16 fails.
4. **What is v13's actual iter-by-iter 500g trajectory?** Only iter20 and running_best (iter80) have been benched at 500g. An 8-minute iter10/30/40/50/60 sweep would definitively answer "does training degrade past iter20 or just plateau in noise." Cheap and worth doing opportunistically.
5. **Should a fresh US-specialist be trained from v13_iter20 as an ensemble companion?** us_only_v5 reaches US=0.360; if v16 fails to raise US WR above 0.30, a parallel 20-iter US-only PPO becomes the next move.
6. **Is there a principled way to detect echo-chamber specialization online without running 500g benches?** Some candidate signals: card entropy at self-frames vs heuristic-frames diverging, value head mean prediction drifting toward 0.5, KL between policy-vs-pool and policy-vs-heuristic growing. None currently logged.
