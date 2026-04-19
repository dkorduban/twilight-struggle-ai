# Opus Analysis: Engine Fix Experiment Review
Date: 2026-04-19T19:15:45Z
Question: Analyze engine fix experiment; suggest corrections

## Executive Summary

The engine fixes (Tier-1 + Tier-2, 9 cards) are correctly scoped and committed, but the *measurement* pipeline around them is unreliable: the one A/B point we have (v1 combined=0.4475) has no pre-fix counterpart, the AWR "architecture sweep" has 1 model bucket and ~1.5σ separation so its conclusion (gnn_side wins) is not statistically warranted, and PPO v2 panel-eval went 0.477 → 0.483 → 0.488 over iters 100-200 which is inside the per-opponent CI (this is **not** progress — it is "not regressing"). PPO v3 has already auto-launched (pid 647101, running since 12:14 UTC) using a 30-epoch `gnn_side` AWR warmstart that overfits past epoch 19, picked on a weak arch-sweep delta, and inherits the unresolved USSR/US asymmetry (~0.72 / ~0.40) that dominates every run in the data. The experiment as designed confounds rule-fix effect with retraining variance and arch change; corrections below.

## Findings

### F1. What was fixed

**Tier-1 (commit `7ea0486`, 2026-04-19 01:42 UTC-7, batched across all 4 cards):**
- **Card 30 Decolonization** (`d8b8934`): enforce 4 distinct countries (was allowing stacking in one Africa/SE-Asia country).
- **Card 77 Ussuri River Skirmish** (`b5e9c89`): restrict target pool to Asia (was global) + 2-per-country cap.
- **Card 33 De-Stalinization** (`2b39213`): paired src→dst remove-then-place with 2-per-country cap on placements.
- **Card 98 Latin American Debt Crisis** (`119baa0`): full reimplementation (was a wrong event entirely — no opponent-cancel-choice, no doubling of S. American influence).

**Tier-2 (committed 2026-04-19 01:50–02:04 UTC-7):**
- **Card 16 Warsaw Pact Formed** (`774dbdc`): 2-per-country cap on the "add 5 USSR" branch (previously allowed stacking 5 into one E.Europe country).
- **Card 76 Liberation Theology** (`d3d3743`): 2-per-country cap on Central America placement.
- **Card 95 Terrorism** (`f7df242`): random discard of opponent hand card (not policy-chosen).
- **Card 60 ABM Treaty** (`23b3710`): correct placement accessibility (was pulling from global accessible pool).
- **Card 28 Suez Crisis** (`b738842`): distribute 4-op removal budget across 3 countries with 2-per-country cap.

Parity harness is green at 5544/5544 as of 2026-04-19 (per continuation_plan). Per the prior rules-fix-plan analysis, Tier-1 was the semantically impactful batch (cards 30, 33 are very-high-exposure USSR Early War; 98 was mis-implemented entirely). Tier-2 fixes are systemic caps and pool errors with smaller per-card WR impact.

### F2. Before/after WR: the data is thin and partially confounded

**The only clean A/B data point:** `results/ab_benchmark_tier1.json` — `gnn_card_attn_v1_ppo_best` on post-Tier1+Tier2 engine: USSR=0.490, US=0.405, combined=0.4475 (n=200/side). No pre-fix benchmark on the same checkpoint under identical seeds exists in the file, so the "delta" is *implied*, not measured.

**Post-fix panel baselines (v56, from `v56_baseline_benchmark.txt`, n=1000/side vs heuristic):**
- USSR=0.558, US=0.325, combined=0.442. Matches `v5_weight_avg_quick.txt` v56_baseline combined=0.420 at n=500/side (within CI).

**Comparison with benchmark_history.json is INVALID.** Entries like `v56: learned_vs_heuristic: 12.8` (pre-fix) are encoded as *delta from 50% vs heuristic in percentage points*, not a combined win-rate, and were measured on the old engine. They cannot be directly subtracted from post-fix 0.442 combined. Any "v56 dropped from 62.8% to 44%" framing based on this mix is a category error.

**What is true vs heuristic on post-fix engine:**
| Checkpoint | USSR WR | US WR | Combined | Source |
|---|---|---|---|---|
| v56 | 0.558 | 0.325 | 0.442 | v56_baseline_benchmark.txt (n=1000/side) |
| ppo_ussr_only_v5 | 0.603 | — | — | v5_post_benchmark.txt (n=1000) |
| ppo_us_only_v5 | — | 0.389 | — | v5_post_benchmark.txt (n=1000) |
| gnn_card_attn_v1 | 0.490 | 0.405 | 0.4475 | ab_benchmark_tier1.json (n=200/side) |
| weight_avg_06 | 0.560 | 0.354 | 0.457 | v5_weight_avg_quick.txt (n=500/side) |

Combined WR sits around 0.42–0.46 post-fix. The relative ordering of panel models is preserved. The missing measurement is any v2-post-training A/B on same seeds against a pre-fix snapshot — that would be the only way to isolate "how much WR came from the bug-exploit."

**Asymmetry is the dominant signal.** USSR side averages ~0.55–0.70 vs heuristic; US side averages ~0.30–0.40. This gap is larger than any architecture or rule-fix effect visible in the tables. It persists in the AWR data (terminal-row mean reward: side 0 = -0.131, side 1 = -0.508 per a spot check of the parquet — i.e. the AWR training corpus itself reflects the same US-under-performance). `train_ppo.py` already applies 2× value-loss weight on US-win steps (lines 1978, 2255) unconditionally, so v2 had it on but it has not closed the gap.

### F3. PPO v2: stagnation, not progress

**Panel-eval trajectory (iters 100/150/200, `train_v2_restart.log` lines 515/1115/1700):**
- iter 100: avg=0.477 (heuristic=0.367)
- iter 150: avg=0.483 (heuristic=0.250)
- iter 200: avg=0.488 (heuristic=0.450)

Each entry is from ~30 games per opponent × 8 opponents = 240 games total per panel eval. Per-opponent CI at n=30 is roughly ±0.09 (Wilson 95% at p=0.5); the ensemble avg CI is ~±0.03. The +1.1pp observed delta over 100 iterations is inside the noise floor. The iter-150 heuristic datapoint (0.250) and iter-200 heuristic datapoint (0.450) differ by 20pp on the same model — the per-slot noise is loud.

**Rollout_wr is flat**: 0.56–0.57 throughout iters 60-200 with the USSR/US split stuck at ~0.70/0.40.

**Elo=1933 across all confirms is not stagnation** — it is a methodology bug. Every `confirm_iter*.log` entry merges the same version string into `elo_full_ladder.json`, which is why every iter reports the identical rating. This is not informative about model progression.

**Honest summary:** PPO v2 did not regress after the engine fix, but it did not improve measurably either. The chain is either at a plateau or the signal-to-noise in panel-eval is too low at 30 games/opponent to detect small gains.

### F4. AWR warmstart strategy: 4 problems

**(a) The "arch sweep" has 1 model bucket, not the advertised 4.**
- `continuation_plan.json`: `"73,981 rows, 4 models (all named ppo_best_scripted, dedup fix added to collector)"`
- But `awr_fixed_engine_train.log`: `"Per-model advantage normalization: 1 models"`.
- Verified: the parquet has `model_name` column with exactly one value: `ppo_best_scripted_vs_heuristic`.
- Consequence: the dedup fix was added to `collect_awr_data.py` *after* this parquet was written, so the per-model advantage normalization collapses to a single bucket. AWR still weights by `exp(advantage/τ)` so the *relative* advantage signal within the one model is preserved, but this sweep measures "which arch learns best from one model's rollouts under advantage weighting" — which is closer to flat BC than to multi-model AWR distillation.

**(b) The arch-ranking delta is ~1.5σ, used to justify abandoning v2's PPO-learned weights and changing architecture.**
From `fixed_engine_arch_sweep.json`:
- `control_feat_gnn_side_h256`: val_adv_card_acc = 0.581 ± 0.003 (2 seeds)
- `country_attn_side_h256`: val_adv_card_acc = 0.576 ± 0.001
- `control_feat_gnn_card_attn_h256`: val_adv_card_acc = 0.576 ± 0.000

gnn_side wins by 0.5pp with n=2 seeds. This is not a statistically reliable ranking; any run with a different random seed pool could flip. The pipeline also treats this as settled (v3 script hardcodes `fixed_engine_gnn_side/awr_best.pt` as priority 1). The correct conclusion from this sweep is "the three archs are within measurement noise on this 74k-row, 1-model corpus."

**(c) The 30-epoch "warmstart" training overfits.**
From `results/awr_sweep/fixed_engine_gnn_side/train.log`:
- Epoch 19 (best): val_adv_card=0.585, val_pl=3.6078
- Epoch 30 (final): val_adv_card=0.578, val_pl=3.6390
- Train card_acc rose 0.515 → 0.651 over the same window (memorization).

The pipeline ran all 30 epochs with no early-stopping and the saved `awr_best.pt` is selected by `best_epoch` — per the script it should be epoch 19, which is fine — but the pipeline printed `"ERROR: Could not find best checkpoint in fixed_engine_full.json"` at exit, meaning the JSON path-resolution broke. The v3 launcher's Priority-1 check (`results/awr_sweep/fixed_engine_gnn_side/awr_best.pt`) succeeded independently of that error, which is good, but it means PPO v3 is using the checkpoint despite the pipeline self-declaring failure.

**(d) The arch-switch decouples v2's and v3's PPO trajectories.**
PPO v2 = `control_feat_gnn_card_attn`. PPO v3 = `control_feat_gnn_side`. This is an architecture change, not a "continue training from warmstart" — v3 cannot be compared to v2 on any Elo/panel axis as a continuation. Any improvement we measure in v3 will confound (rule-fix effect + arch change + AWR warmstart effect + 150 extra optim steps vs v2). This was not called out as a tradeoff in the plan.

### F5. PPO v3 already launched

`pid 647101` (launched 12:14 UTC by `launch_ppo_v3.sh` pid 642803) is now ~7 hours into a 200-iter run on the arch we selected with ~1.5σ evidence. The lock check fired as soon as v2 completed (continuation_plan hadn't updated by the time I read it). The v3 config mirrors v2 with the same games-per-iter=200, lr=5e-5, clip=0.10, ent decay, and the same panel. No separate A/B measurement of the warmstart model's WR was run before PPO v3 started — we don't know whether the AWR warmstart is ahead of, behind, or equal to v2's best checkpoint on WR terms.

### F6. Process / measurement issues

1. **No pre-fix A/B baseline was preserved.** The rules-fix plan explicitly specified paired-engine A/B on frozen checkpoints (Option (d) in `opus_analysis_20260419_083500_rules_fix_plan.md` §F1). What landed instead was a single post-fix measurement of v1. This conflates bug-exploit-loss with nothing; we can't quantify how much WR drop actually came from the fixes.
2. **AWR parquet was collected from one source model** (self-play of ppo_best_scripted vs heuristic), yet the continuation plan claims 4 models. This needs a retcon-or-recollect decision before more AWR cycles.
3. **The `fixed_engine_full.json` pipeline threw an error at exit** (`"Could not find best checkpoint"`) but left the checkpoint behind on disk, so downstream code that reads the JSON instead of scanning the directory will fail. This is a latent bug.
4. **Elo is stuck at 1933** because the same version tag is re-merged every confirm. The Elo infrastructure is not tracking v2's per-iteration progress. No per-iter ratings are being produced.
5. **Panel-eval CI at n=30/opponent is too loose** to detect 1-2pp gains reliably. Panel size or game count should scale up if the target effect is <5pp.

## Conclusions

1. **Tier-1+2 fixes are correctly scoped and merged.** 9 rule corrections (cards 28, 30, 33, 60, 76, 77, 95, 98, 16) with parity harness green at 5544/5544. Tier-3 (cards 75, 50) correctly deferred.
2. **"Before vs after" numbers are not meaningful as presented.** `benchmark_history.json` is pre-fix percentage-point deltas; post-fix measurements are full WRs; the two cannot be subtracted. Only one paired A/B point exists (v1 post-fix combined=0.4475) and it has no matched pre-fix partner.
3. **PPO v2 did not improve measurably over iters 100-200.** Panel-eval avg 0.477 → 0.488 is noise; rollout_wr flat at 0.56-0.57. Elo=1933 across iters is a version-tag-merge bug, not a true plateau. Call it "stable, not progressing" — not "progressing."
4. **USSR/US asymmetry (~0.72 / ~0.40) is larger than every architecture and rule-fix effect in the data** and is present in v2 rollouts, v56 baselines, USSR-only/US-only specialists, and the AWR training data itself. The hardcoded 2× US-win value weighting in `train_ppo.py` is already on and has not closed the gap. This is the single highest-leverage problem and it is not addressed by the engine-fix / AWR / arch-change plan.
5. **The AWR arch-sweep is weak evidence.** 1 model bucket (not the 4 claimed), ~0.5pp / ~1.5σ separation, 2 seeds. Treating `gnn_side` as "the best fixed-engine arch" is not justified.
6. **The 30-epoch AWR warmstart overfits.** Val adv_card peaks at epoch 19 (0.585) and decays to 0.578 by epoch 30. The pipeline ran without early stopping and self-declared failure at exit, but v3 still launched with the epoch-19 checkpoint (correct by luck).
7. **PPO v3 is a confounded comparison to v2.** Arch change + AWR warmstart + 30-epoch BC + 200 PPO iters — any delta between v2-best and v3-best cannot be attributed to a single cause.
8. **PPO v3 has already auto-launched** (pid 647101 since 12:14 UTC, ~7h in). The decision gate the plan specified ("retrain only if USSR ΔWR >5pp or v2 shows >3pp combined drop") was not applied — no paired A/B was computed, so the gate's preconditions are unmet.

## Recommendations

1. **Do NOT stop PPO v3 now** (7h in, sunk cost). Let it finish so at least the arch + warmstart combination yields one data point. But **treat v3 as an exploratory run, not a validated continuation** — its panel-eval is the truth, not the implicit claim that "AWR gave a better warmstart."
2. **Run the paired-engine A/B that was specified in the rules-fix plan but skipped.** Take `ppo_gnn_card_attn_v1`, v2-best, v56, v44 — four frozen checkpoints. Run 500 games/side vs heuristic under both the pre-fix engine (checkout commit `d8b8934^`, rebuild) and the post-fix engine (HEAD). Identical seeds. Log per-card event-play rates on cards 30, 33, 77, 98, 16, 76, 28, 60, 95. Output: `results/ab_benchmark_paired.json`. This is the measurement that quantifies the Tier-1+2 effect.
3. **Recollect the AWR corpus with multi-model sources.** The current parquet has one `model_name` value. To make multi-model AWR meaningful, re-run `collect_awr_data.py` after the dedup fix, pointing at: {v2-best, v56, v44, ppo_ussr_only_v5, ppo_us_only_v5} — five distinct buckets, ~150k rows total minimum. Keep the existing 74k file as `awr_fixed_engine_v1_singlemodel.parquet` for reference.
4. **After v3 finishes, benchmark v3-best vs v2-best directly.** If v3-best combined ≥ v2-best combined + 3pp (n ≥ 500/side), the v3 design wins. If within 3pp, the arch change + warmstart were not worth it and we should resume `control_feat_gnn_card_attn` training with a corrected AWR corpus. Pre-register the 3pp threshold before reading results.
5. **Fix the Elo version-tag-merge bug.** Every `confirm` should register a unique version (e.g., `gnn_card_attn_v2_iter0200`), not overwrite `gnn_card_attn_v2`. Until fixed, Elo is not a metric for this chain.
6. **Address USSR/US asymmetry as a first-class experiment.** Candidate levers, ordered by expected leverage:
   - Collect US-side-only AWR corpus from a strong US-side specialist (we have `ppo_us_only_v5` at US-WR=0.389) and give it higher sampling weight than USSR-side in a fresh warmstart.
   - Increase US-win value weighting to 3× or 4× (currently 2× hardcoded at `train_ppo.py:1978`).
   - Add side-conditioned entropy bonus: keep US entropy higher longer.
   - None of these are in the current v3 plan.
7. **Add early stopping to the AWR pipeline.** Check val_adv_card_acc every epoch, stop if no improvement for 5 epochs. The current 30-epoch run memorized 14pp of train accuracy past the val peak.
8. **Fix `awr_fixed_engine_pipeline.sh` JSON path resolution** so it doesn't self-declare failure at exit while leaving a usable checkpoint behind. Downstream automation will misread this as a failed run.
9. **Update continuation_plan.json to reflect the 1-model corpus reality** (not the "4 models" claim) before the next Opus session reads it.
10. **Freeze a new Elo anchor `v14_e2` on the fixed engine** as the rules-fix plan specified, but only after the paired A/B in (2) is done so we know the fixed-engine panel WRs. Without that, the anchor is at an unknown skill level relative to the old ladder.

## Open Questions

1. Is the `ppo_best_scripted_vs_heuristic` source of the AWR parquet the v2-early checkpoint, v56, or v44? The `continuation_plan` implies v2-best but the filename is a stem-collision artifact. A small retcon audit should confirm which model actually populated the parquet.
2. Did the v1 pre-fix→post-fix WR actually drop by a meaningful amount, or is the bug-exploit-loss small? Only measurement (2) above resolves this. If ΔWR < 3pp even for v1 (the checkpoint most likely to have learned the bugs), then the rules fixes may not have needed to stop PPO at all.
3. Should PPO v3 use `ppo_gnn_card_attn_v2` as warmstart instead of an AWR-trained `gnn_side`? The v2 model trained for 200 PPO iters through the fixed engine; its policy is naturally bug-exploit-free for newly-visited states. An AWR model trained on 74k rows from one bug-exploiting source may be *more* bug-contaminated than a PPO-converged v2, not less.
4. Should we run a v3-sibling that keeps `control_feat_gnn_card_attn` arch (same as v2) warmstarted from v2-best with `--reset-optimizer` but same hyperparameters, as a control arm? Without it, any v3 result is confounded arch+warmstart+rules.
5. Does the panel-eval protocol support doubling game count to 60/opponent? At 30 games/opponent the per-opponent CI is ±0.09; at 60 games it's ±0.07 — still loose. Real progress detection probably needs n ≥ 100/opponent.
6. The fixed-engine data collection used self-play vs heuristic only. AWR quality for PPO warmstart typically benefits from diverse opponent pools (self-play, league, stronger-than-learner). Is a multi-opponent AWR corpus in scope for v4?
