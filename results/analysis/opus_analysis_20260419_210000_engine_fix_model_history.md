# Opus Analysis: Engine Fix Results and Model Version History (v20/44/54/55/56)
Date: 2026-04-19T21:00:00Z
Question: Summarize engine fix results and what happened to v20/44/54/55/56 or their retrained versions?

## Executive Summary

The engine was hardened in two broad waves: a systemic GAP inventory (GAP-001..043, completed over Feb-Apr 2026) and a targeted Rules batch on 2026-04-19 (Tier-1: cards 30, 33, 77, 98; Tier-2: cards 16, 76, 95, 60, 28; Tier-3 deferred: 75, 50). The rules-batch parity harness is green at 5544/5544 / 79/79 tests. **The panel checkpoints v20/v44/v54/v55/v56 were NOT retrained after the rules fixes** — they are preserved as frozen Elo-anchor checkpoints (scripted `.pt` files still under `data/checkpoints/scripted_for_elo/`) and were re-benchmarked against the fixed engine on 2026-04-16 showing post-fix combined WR vs heuristic of 41-45% (v56 top at 45.1%). The PPO chain that continues *past* these checkpoints is `ppo_gnn_card_attn_v1 → v2 → v3` plus specialists (ppo_ussr_only_v5, ppo_us_only_v5); the comparison-shocking "v44=16.0, v55=13.0, v56=12.8" numbers in `benchmark_history.json` are legacy *pre-fix* percentage-point deltas in a different encoding, not directly comparable to the post-fix WR figures.

## Findings

### Engine Fixes

**Wave 1 — GAP inventory (GAP-001 through GAP-043).** Documented in `results/analysis/engine_rule_gaps.md`. 46 gaps logged across 5 categories (Headline, Operations, Card Events, DEFCON, Misc). All marked DONE per `continuation_plan.json:60` ("ALL DONE — GAP-044/45/46 WONTFIX promo cards"). Highest-impact fixes in this wave:
- GAP-002/003: opponent-event ordering and Space-Race event suppression (commits 37bdd01 / 953c783)
- GAP-005: adjacency-based placement + enemy-controlled 2-op surcharge (commits d0e328c / 4326635)
- GAP-008/009: war-card mechanic for Korean War and Arab-Israeli War (commit 442643b) — previously modeled as coups
- GAP-010..013: random-target bugs on cards 16/19/20/23 routed through `choose_country` (commit 49caca4)
- Headline DEFCON-1 phasing + illegal coup target bugs (commit a9dd071)
- ISMCTS hand resampling (commit 7af5979)

**Wave 2 — Rules batch Tier-1 + Tier-2 (2026-04-19 01:42–02:04 UTC-7).** Documented in `results/analysis/opus_analysis_20260419_191545_engine_fix_experiment.md` F1.

| Tier | Card | Commit | Fix |
|---|---|---|---|
| 1 | 30 Decolonization | d8b8934 | Enforce 4 **distinct** countries (was allowing 4-stack) |
| 1 | 77 Ussuri River | b5e9c89 | Asia-only pool + 2-per-country cap (was global) |
| 1 | 33 De-Stalinization | 2b39213 | Paired src→dst remove-then-place, 2-per-country cap |
| 1 | 98 LatAm Debt Crisis | 119baa0 | **Full reimplementation** — was wrong event entirely |
| 2 | 16 Warsaw Pact | 774dbdc | 2-per-country cap on add-5 branch |
| 2 | 76 Liberation Theology | d3d3743 | 2-per-country cap on Central America |
| 2 | 95 Terrorism | f7df242 | Random discard of opponent card (was policy-chosen) |
| 2 | 60 ABM Treaty | 23b3710 | Correct placement accessibility |
| 2 | 28 Suez Crisis | b738842 | Distribute 4-op budget across 3 countries, 2-per cap |

Tier-3 (cards 75 Voice of America, 50 Junta) correctly deferred.

**Measurable impact — limited data, heavy confounds.** The ONE paired-engine point that exists is `results/ab_benchmark_tier1.json`: `gnn_card_attn_v1` on post-Tier1+2 engine scored combined=0.4475 (USSR=0.490, US=0.405, n=200/side). **No pre-fix counterpart on the same checkpoint under matched seeds was preserved**, so the actual ΔWR from the fixes is implied, not measured. The prior rules-fix plan (`opus_analysis_20260419_083500_rules_fix_plan.md`) predicted Tier-1 would cost USSR-side 3-8pp from lost bug exploits (cards 30/33 allowed 4-stacking into Angola/Italy), but the paired-engine A/B that would quantify this was specified and then skipped.

What we actually know for the fixed engine (n ≥ 200/side):

| Checkpoint | USSR WR | US WR | Combined | Source |
|---|---|---|---|---|
| ppo_v56_league | 0.546 | 0.356 | 0.451 | benchmark_all_checkpoints.txt n=500 |
| ppo_v54_league | 0.516 | 0.366 | 0.441 | benchmark_all_checkpoints.txt n=500 |
| ppo_v44_league | 0.546 | 0.332 | 0.439 | benchmark_all_checkpoints.txt n=500 |
| ppo_v20_league | 0.530 | 0.318 | 0.424 | benchmark_all_checkpoints.txt n=500 |
| ppo_v55_league | 0.484 | 0.338 | 0.411 | benchmark_all_checkpoints.txt n=500 |
| gnn_card_attn_v1 (post-fix) | 0.490 | 0.405 | 0.448 | ab_benchmark_tier1.json n=200 |
| ppo_ussr_only_v5 | 0.603 | — | — | v5_post_benchmark.txt n=1000 |
| ppo_us_only_v5 | — | 0.389 | — | v5_post_benchmark.txt n=1000 |
| weight_avg_06 | 0.560 | 0.354 | 0.457 | v5_weight_avg_quick.txt n=500 |

Asymmetry dominates: USSR ~0.48-0.60, US ~0.32-0.41 on every measured checkpoint. The 2× US-win value-loss weight in `train_ppo.py` (lines 1978, 2255) has not closed this gap. This gap is larger than any rule-fix or architecture delta observed in the chain and is the highest-leverage open problem.

### Model Version History

Terminology note: there are two distinct Elo-panel "v-series" families that overlap in number but are different chains:

- **Legacy league panel** (v15..v68) — earlier PPO league-training chain frozen as scripted checkpoints in `data/checkpoints/scripted_for_elo/`. Trained on BUGGY engine. The five asked-about checkpoints all belong here.
- **"_sc" series** (v65_sc..v310_sc) — SmallChoice-callback PPO run after the architecture refactor; different checkpoint family, still evaluated with scripted overrides (`checkpoint_override_v*_sc.txt.used`).

**v20** — Legacy league PPO snapshot (pre-fix training).
- File: `data/checkpoints/scripted_for_elo/v20_scripted.pt`
- Elo (pre-fix ladder): 2076.7 (USSR 2103.6 / US 1978.1), delta_vs_anchor = +61.7
- `benchmark_history.json` pre-fix entry: 13.9 (absent — v20 not in top list; adjacent v19=? v21=? see raw file for v21=?)
- Post-fix benchmark (2026-04-16): ussr=53.0%, us=31.8%, combined=42.4% @ n=500
- Retrained after engine fix? **No**. Frozen as Elo-panel anchor.

**v44** — Legacy league PPO snapshot.
- File: `data/checkpoints/scripted_for_elo/v44_scripted.pt`
- Elo (pre-fix): 2100.8 (USSR 2095.8 / US 2033.0), delta_vs_anchor = +85.8 — top-tier of legacy panel
- `benchmark_history.json` pre-fix legacy delta: 16.0 (this is a *percentage-point* delta from 50% baseline, not a combined WR — see Executive Summary)
- Post-fix benchmark: ussr=54.6%, us=33.2%, combined=43.9% @ n=500
- Retrained after engine fix? **No**. Used in v56_baseline head-to-head (v56 vs v44 as USSR: 0.695; as US: 0.380 — v44 is the WEAKEST panel opponent for v56 as USSR).

**v54** — Legacy league PPO snapshot.
- File: `data/checkpoints/scripted_for_elo/v54_scripted.pt`
- Elo (pre-fix): 2102.2 (USSR 2111.6 / US 2023.5), delta_vs_anchor = +87.2 — #2 of legacy panel
- Pre-fix legacy delta: 16.5
- Post-fix benchmark: ussr=51.6%, us=36.6%, combined=44.1% @ n=500
- Retrained after engine fix? **No**.

**v55** — Legacy league PPO snapshot. There are TWO scripted files: `v55_scripted.pt` (current) and `v55_scripted.pt.bak` (backup from an earlier scripting).
- Elo (pre-fix): 2118.5 (USSR 2110.2 / US 2055.8), delta_vs_anchor = +103.5 — **#1 Elo in legacy panel**
- Pre-fix legacy delta: 13.0
- Post-fix benchmark: ussr=48.4%, us=33.8%, combined=41.1% @ n=500 (note: top Elo, but not top combined-WR — post-fix engine rewards USSR-side less, v55's USSR edge shrank)
- Retrained after engine fix? **No**. Also note `v55_sc_scripted.pt` is a *different* checkpoint (the SmallChoice-series v55, not the legacy v55).
- Appears in diagnostic: `results/analysis/game_log_v55_seed3_T1.txt` and the ISMCTS self-play diagnostic file `ismcts_selfplay_v55_4det50sim.txt`.

**v56** — Legacy league PPO snapshot.
- File: `data/checkpoints/scripted_for_elo/v56_scripted.pt`
- Elo (pre-fix): 2095.1 (USSR 2086.0 / US 2029.9), delta_vs_anchor = +80.1
- Pre-fix legacy delta: 12.8
- Post-fix benchmarks (multiple):
  - benchmark_all_checkpoints.txt: ussr=54.6%, us=35.6%, combined=45.1% @ n=500 — **#1 post-fix combined-WR in panel**
  - v56_baseline_benchmark.txt: ussr=55.8%, us=32.5%, combined=44.2% @ n=1000/side
  - v5_weight_avg_quick.txt v56_baseline: ussr=54.6%, us=29.4%, combined=42.0% @ n=500 (note: US WR decays when heuristic seeds drift)
- v56 vs panel head-to-head (v56_baseline_benchmark.txt, n=200/side):
  - vs v20: ussr=59.0, us=37.0 (combined 48.0% — v56 wins)
  - vs v44: ussr=69.5, us=38.0 (combined 53.75% — v56 dominates)
  - vs v54: ussr=56.0, us=41.0 (combined 48.5% — v56 wins)
  - vs v55: ussr=48.5, us=42.5 (combined 45.5% — nearly even, v55 slight Elo edge)
  - vs v56 self: ussr=61.5, us=37.5 (50/50 by symmetry, but USSR side of the mirror wins more — same asymmetry)
- **v56 is the de-facto "best panel baseline" post-fix** per `continuation_plan.ppo_v2_benchmarks.v56_bc_baseline` = {ussr: 0.558, us: 0.325, combined: 0.442}.
- Retrained after engine fix? **No** — but its rollouts were RE-USED:
  - `data/awr_eval/v4_bc_diverse_v1/awr_v4_bc_diverse.parquet` (65,519 rows) includes v56 BC rollouts for the AWR v4 warmstart corpus.
  - v56 behaves as the reference opponent in panel-Elo and in the weight-averaging / specialist capacity experiments.

**What was trained after engine fix (the "retrained generation"):**

The chain that replaces the v20-v56 era is:
- **ppo_gnn_card_attn_v1** — first PPO trained on Tier-1+2 fixed engine. Combined=0.4475 @ n=200.
- **ppo_gnn_card_attn_v2** — continued chain, 200 iters. last20_avg rollout_wr=0.523 (USSR=0.698, US=0.348); best_rollout_iter=96 (0.635). Iter-100/150/200 panel combined: 0.388 / 0.427 / 0.422. **Plateaued**; no iter beat v56 BC combined 0.442.
- **ppo_gnn_card_attn_v3** — currently running (iter ~50/200 at the time of the 2026-04-19 snapshot), `control_feat_gnn_side` arch warm-started from `fixed_engine_gnn_side/awr_best.pt`. Iter50 combined=0.342; trajectory: warmstart 0.314 → iter1 0.305 → iter50 0.342 (still below v56 baseline).
- **ppo_ussr_only_v5 / ppo_us_only_v5** — side-specialists, post-fix. USSR specialist: 0.603 vs heuristic. US specialist: 0.389 vs heuristic.
- **weight_avg_04/05/06/07** — weight-averaged blends of v2-chain checkpoints. Best (weight_avg_06): combined=0.457 @ n=500.

**There is no v20/v44/v54/v55/v56_post_fix checkpoint.** The plan (`opus_analysis_20260419_083500_rules_fix_plan.md` §F2) explicitly recommended NOT retraining panel models as a matter of policy; they stay frozen as Elo anchors. Any retraining cost was spent on the new `ppo_gnn_card_attn_v{1,2,3}` chain instead.

### Benchmark Timeline

Chronological WR progression (all vs heuristic; post-fix unless noted).

| Date | Model | USSR | US | Combined | N/side | Engine | Source |
|---|---|---|---|---|---|---|---|
| pre-2026-04-16 | legacy panel v20..v58 pre-fix | — | — | legacy-delta 11–17 | 50–500 | BUGGY | benchmark_history.json |
| 2026-04-11 | v45 + ISMCTS (16det×100sim) | 90.0% | 99.0% | 94.5% | 100/side | partially fixed | ismcts_retest_post_fix.md |
| 2026-04-16 | v56 panel (post-fix) | 54.6% | 35.6% | 45.1% | 500 | Tier-1+2 | benchmark_all_checkpoints.txt |
| 2026-04-16 | v54 panel (post-fix) | 51.6% | 36.6% | 44.1% | 500 | Tier-1+2 | benchmark_all_checkpoints.txt |
| 2026-04-16 | v44 panel (post-fix) | 54.6% | 33.2% | 43.9% | 500 | Tier-1+2 | benchmark_all_checkpoints.txt |
| 2026-04-16 | v20 panel (post-fix) | 53.0% | 31.8% | 42.4% | 500 | Tier-1+2 | benchmark_all_checkpoints.txt |
| 2026-04-16 | v55 panel (post-fix) | 48.4% | 33.8% | 41.1% | 500 | Tier-1+2 | benchmark_all_checkpoints.txt |
| 2026-04-19 | gnn_card_attn_v1 (post-fix) | 49.0% | 40.5% | 44.75% | 200 | Tier-1+2 | ab_benchmark_tier1.json |
| 2026-04-19 | weight_avg_06 | 56.0% | 35.4% | 45.7% | 500 | Tier-1+2 | v5_weight_avg_quick.txt |
| 2026-04-19 | ppo_ussr_only_v5 (USSR side) | 60.3% | — | — | 1000 | Tier-1+2 | v5_post_benchmark.txt |
| 2026-04-19 | ppo_us_only_v5 (US side) | — | 38.9% | — | 1000 | Tier-1+2 | v5_post_benchmark.txt |
| 2026-04-19 | ppo_gnn_card_attn_v2 final | 51.5% | 33.0% | 42.2% | ~200 panel | Tier-1+2 | ppo_v2_benchmarks.iter200 |
| 2026-04-19 | ppo_gnn_card_attn_v3 iter50 | 34.7% | 33.7% | 34.2% | ~200 | Tier-1+2 | ppo_v2_benchmarks.v3_iter50 |

Observations:
1. **Headline WRs collapsed in encoding** when moving from the legacy `benchmark_history.json` ("delta from 50% in pp" format for v15..v80 — with v56=12.8 meaning pre-fix WR was ~62.8% against an *easier* heuristic on a *buggier* engine) to the full-WR tabular format post-fix (~42-45% combined). **These cannot be subtracted.**
2. **Post-fix panel spread is narrow**: v20..v56 span 41-45% combined, inside mutual 95% CI at n=500. Their relative Elo ordering (v55 > v54 > v44 > v56 > v20) is partially preserved for USSR side but US-side ordering flipped (v54 > v44 > v55 > v20 > v56 vs panel's Elo US ordering).
3. **v56 is now the effective ceiling for panel-era checkpoints**: combined 44-45%. No post-fix PPO chain (v1, v2, v3) has exceeded v56 by the 3-pp threshold the plan specified.
4. **Weight-averaged v5 (weight_avg_06) at 45.7% is marginally above v56 @ 45.1%** — within CI but the best single number post-fix.

## Conclusions

1. **Two waves of engine fixes landed**: GAP-001..043 (broad systemic, completed pre-April) and Rules Tier-1+2 (9 cards, atomic commits on 2026-04-19). Parity harness green at 5544/5544 and 79/79 tests.
2. **v20, v44, v54, v55, v56 were NOT retrained post-fix** — by explicit policy in the rules-fix plan. They remain as frozen scripted checkpoints in `data/checkpoints/scripted_for_elo/` and serve as Elo-anchor opponents for measuring the new training chain.
3. **Their post-fix combined WR vs heuristic is 41-45%** (v56 top at 45.1%, v55 bottom at 41.1%, n=500). The relative Elo ordering is partially preserved; v55 remains top Elo (2118.5) but v56 is top post-fix combined WR.
4. **The "pre-fix vs post-fix delta" for these panel models cannot be computed from available data.** The `benchmark_history.json` legacy entries (v44=16.0, v55=13.0, v56=12.8) are in a different encoding (percentage points above a 50% baseline on the buggy engine with an older heuristic), not combined WR. The paired-engine A/B specified in the rules-fix plan to quantify the fix effect was skipped.
5. **The retraining effort went into a new chain** (`ppo_gnn_card_attn_v1 → v2 → v3`) plus specialists (`ppo_ussr_only_v5`, `ppo_us_only_v5`) and weight-averaged blends. None of these beats v56 combined WR by the pre-registered 3-pp threshold; the plateau around 0.42-0.46 combined is the current post-fix ceiling.
6. **USSR/US asymmetry (~0.55 USSR, ~0.35 US) is the dominant remaining signal**, larger than any rule-fix or architecture effect. The hardcoded 2× US-win value-loss weight has not closed this gap and the current v3 arch-switch plan does not address it directly.
7. **v56 is the practical "post-fix baseline"** for everyday use: best-in-panel combined WR, used as the BC baseline in `continuation_plan.ppo_v2_benchmarks.v56_bc_baseline`, and contributed rollouts to the AWR v4 warmstart corpus.
8. **ISMCTS benchmarks against the panel are misleading as a strength signal**: 94.5% combined @ 16det×100sim reflects the value-head miscalibration on determinized states (per `continuation_plan.ismcts_verdict` — SHELVED, delta_vs_greedy = -0.225). Post-fix, ISMCTS is no longer competitive with greedy; panel-vs-heuristic remains the real measurement.

## Recommendations

1. **Run the paired-engine A/B that was skipped** (Rec #2 of the 2026-04-19 engine-fix-experiment analysis). Take v56, v44, gnn_card_attn_v1, v2-best, check out pre-Tier-1 commit (`d8b8934^`), rebuild, 500 games/side identical seeds under both engines, log per-card event-play rates for cards 30/33/77/98/16/76/28/60/95. Only this measurement quantifies the actual Tier-1+2 WR impact.
2. **Retire the legacy `benchmark_history.json` delta-encoding** or annotate every entry with engine version + encoding format. Current file mixes pre-fix pp-deltas with post-fix absolute WRs under the same `learned_vs_heuristic` key, which is a latent bug for any future analyst.
3. **Freeze a new Elo anchor `v14_e2` on the fixed engine** and re-run panel round-robin (10 pairs × 200 games) to establish the post-fix Elo baseline. Without this, the existing Elo ladder (anchor v14 = 2015.0) is not reliably comparable across the engine boundary.
4. **Address USSR/US asymmetry as a first-class experiment** — candidate levers in order of expected leverage: (a) US-specialist AWR corpus upweighting, (b) increase US-win value weighting to 3-4× (currently 2× hardcoded `train_ppo.py:1978`), (c) side-conditioned entropy bonus. None are in the v3 plan.
5. **Keep v56 as the comparison baseline for v3-best**: gate "v3 wins" at combined ≥ v56 + 3pp (pre-registered in continuation plan). If v3 plateaus below that, revert arch to `control_feat_gnn_card_attn` with corrected AWR corpus.
6. **Do not retrain v20/v44/v54/v55/v56**. Their value as frozen Elo anchors outweighs any marginal strength gain from refreshing them. If a post-fix panel is needed, build it from ppo_ussr_only_v5 / ppo_us_only_v5 / weight_avg_06 / v2-best / v3-best / gnn_card_attn_v1.

## Open Questions

1. **What is the actual pre-fix→post-fix ΔWR on the same seeded games for the panel?** Unknown — the paired A/B was not run. Without it, the strength of the claim "engine fixes improved model evaluation fairness" is qualitative.
2. **Did v55's reputation as top-Elo survive the fixes?** Partially. Its USSR Elo (2110.2) was #2 pre-fix after the 2118.5 combined, and its post-fix USSR WR dropped to 48.4% (lower than v20/v44/v54/v56). Possibly v55 was more heavily fitted to the buggy card 33 / 30 / 77 exploits. Requires per-card event-play rate comparison pre-fix vs post-fix to confirm.
3. **Is the 1.35M-row buggy-engine BC corpus still in use?** The continuation plan's `awr_datasets` dictionary lists three post-fix parquets, but the prior rules-fix plan (§F3 step 5a) mandated retiring the 1.35M-row corpus if retrain was gated ON. Retrain was not formally gated ON, so the corpus may still live in `data/` — a grep for its presence + a decision about `data/deprecated_buggy_engine/` is warranted.
4. **Why does weight_avg_06 (45.7%) beat v56 (45.1%) by a small margin?** The v5 weight-averaging was over v2-chain checkpoints, not panel-era. This is a post-fix vs post-fix comparison and is real (within CI). Suggests some gain from ensemble averaging even without architecture change.
5. **`v55_scripted.pt.bak` existence**: the `.bak` file suggests v55 was re-scripted at some point. Possibly due to the TorchScript `__constants__` fix (commit bed9e17, per continuation_plan.torchscript_fix). Worth confirming whether `.bak` and live `.pt` produce identical logits — a silent drift here would confound every v55 ladder number.
6. **Should gnn_card_attn_v1 be added to the scripted-panel for future Elo runs?** Its post-fix combined (0.4475) is within CI of v56 (0.442) and it IS a post-fix native checkpoint. Adding it gives the ladder a proper "post-fix anchor" separate from the legacy v14_e2 reset.
