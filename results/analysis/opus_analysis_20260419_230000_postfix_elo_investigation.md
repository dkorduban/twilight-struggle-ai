---
# Opus Analysis: Post-Fix Elo and Panel Strength Investigation
Date: 2026-04-19T23:00:00Z

## Executive Summary

The `results/elo/elo_full_ladder.json` ladder (anchor v14=2015, v55=2118, v54=2102, v56=2095, heuristic=1767) is **stale pre-fix data**: every single one of the 908 matches is marked `"reused": true`, the file was last modified in git on 2026-04-14 (before the Tier-1+2 card rule fixes landed on 2026-04-19), and its match pool predates BOTH the 2026-04-13 DEFCON-1 engine fixes (commit `f6800e3`) and the 2026-04-19 Tier-1+2 card-rule fixes (commits `7ea0486` through `b738842`). The panel-versus-heuristic gap that made v55 look 350 Elo above heuristic was a compound artifact of (a) the heuristic being weaker pre-DEFCON-1-fix and (b) the panel checkpoints being trained to exploit buggy card events (cards 30/33/77/98/16/76/28/60/95). Post-fix `benchmark_all_checkpoints.txt` (n=500) collapses the entire v20–v56 panel into a 41.1–45.1% combined-WR-vs-heuristic band, and the `panel_wr_matrix.json` cross-match data confirms the panel is tightly clustered (most pairs within 48–52% WR of each other). No post-fix Elo tournament with fresh matches has been run; the ladder as a numerical Elo scale cannot be trusted for any checkpoint whose rating was set before 2026-04-13.

## Findings

### DEFCON-1 Fix Timeline

The DEFCON-1 engine safety fixes landed in a single dense burst on **2026-04-13 (Pacific time)**. Key commits (from `git log --all --grep -i defcon`):

| Commit | Date (PDT) | Change |
|---|---|---|
| `f6800e3` | 2026-04-13 01:24 | **Main landing**: "fix: DEFCON-1 engine safety fixes (3 changes)" |
| `eedd07a` | 2026-04-13 01:34 | Add cards 52+68 to `fast_mcts_batched.cpp` kDefconLoweringCards |
| `55e792a` | 2026-04-13 01:25 | Additional DEFCON safety + `run_traced_game` opponent_support_mask |
| `39dfe0d` | 2026-04-13 01:44 | Add DEFCON-1 penalty (-1.5) to PPO reward shaping |
| `7fdbd11` | 2026-04-13 01:51 | WS6 phase 1 — consolidate kDefconLoweringCards into `card_properties.hpp` |
| `9e68dfb` | 2026-04-13 11:09 | Use canonical 15-card DEFCON set in `search_common.hpp` |
| `4274592` | 2026-04-13 11:35 | Allow US coups at DEFCON 2 when Nuclear Subs active |
| `c80facc` | 2026-04-13 12:02 | Refine DEFCON masking and suicide penalty |
| `01ef922` | 2026-04-13 17:17 | WS6 Phase 3: centralize DEFCON-lowering logic into legal_actions |

Three separate mechanisms were fixed (per `opus_analysis_20260413_defcon1_holistic_fix.md`):

1. **`apply_ops_randomly` guard**: Refuses Coup mode at DEFCON ≤ 2 (falls back to Influence). Blocks the dominant failure mode where cards 68 (Grain Sales) / 52 (Missile Envy) auto-fire and random coups lower DEFCON.
2. **Expanded `kDefconLoweringCards`**: Added cards 52, 68 to the 13-card list (now 15 cards) across 7+ locations (MCTS, batched rollout, learned_policy, PPO Python mirror, etc).
3. **HLSTW (card 49) clamp**: `choose_option` minimum bumped from 1 → 2 so the phasing player can never voluntarily set DEFCON = 1.

A second wave of card-rule fixes (**Tier-1 + Tier-2**, unrelated to DEFCON but relevant for panel-model fairness) landed on **2026-04-19 01:42–02:04 PDT**, correcting 9 card events (30/33/77/98/16/76/28/60/95). Parity harness is green at 5544/5544.

The DEFCON-1 fix primarily hardened the **heuristic opponent** (it can no longer be induced to self-destruct via random coup), which is the mechanism by which **learned-vs-heuristic win rates deflated by 5–10 pp** (recorded in `memory/project_benchmark_drift.md`). The Tier-1+2 fixes additionally eliminated the card-event bugs that panel models had learned to exploit (4-stack into Angola via Decolonization, etc).

### Elo Ladder Data Age

**`results/elo/elo_full_ladder.json` is PRE-fix and stale.** Evidence:

- **All 908 matches marked `"reused": true`** (grep count). Zero matches were freshly computed; every match value was pulled from a match cache populated before the current invocation of the Elo solver.
- **File's last in-repo commit was 2026-04-14** (`277dd4b: fix: Elo infrastructure, run_traced_game fixes, arch audit`). The filesystem mtime is 2026-04-19 15:26, indicating an uncommitted re-solve — but the matches it solves over still come from the cache.
- **Seed distribution**: match seeds cluster at 88000–91200 (block structure suggests these were booked before the April 13 DEFCON fix). A post-fix round-robin would use new seeds; none of the matches have a post-2026-04-13 seed batch.
- **The ladder predates the panel-Elo-fix analysis** (`opus_analysis_20260414_171000_panel_elo_fix.md`) which explicitly flagged that the 5-mode panel produces inflated ratings for 6-mode models (v260_sc showed 2393 fake Elo vs 1735 true Elo — a +658 Elo error). That measurement bug was never repaired in the current `elo_full_ladder.json`.

**Concrete ratings in the stale ladder** (all suspect as absolute numbers; relative ordering within the 5-mode panel is approximately preserved):

| Model | Combined Elo | USSR Elo | US Elo | Delta vs v14 |
|---|---|---|---|---|
| v55 | 2118.5 | 2110.2 | 2055.8 | +103.5 |
| v54 | 2102.2 | 2111.6 | 2023.5 | +87.2 |
| v44 | 2100.8 | 2095.8 | 2033.0 | +85.8 |
| v46 | 2100.4 | 2106.9 | 2023.0 | +85.4 |
| v45 | 2095.8 | 2124.8 | 1999.2 | +80.8 |
| v56 | 2095.1 | 2086.0 | 2029.9 | +80.1 |
| v20 | 2076.7 | 2103.6 | 1978.1 | +61.7 (approx) |
| heuristic | 1766.8 | 1780.5 | 1625.0 | −248.2 |
| v14 (anchor) | 2015.0 | — | — | 0 |

The ~350-point gap between v55 and heuristic corresponds to ~87% WR by the Elo formula — which matches the historical `benchmark_history.json` entries (ppo_best_scripted = 83.2%) but does **not** match the post-fix n=500 benchmark (v55 combined = 41.1% vs heuristic). Post-fix, a ~45% combined WR implies the panel-vs-heuristic Elo gap is effectively 0–50 points, not 350.

**No GNN models appear in `elo_full_ladder.json` at all.** The GNN models (gnv1, gnv2, gnv3) were never added to the Elo ladder — they only appear in the separate `panel_wr_matrix.json` (post-fix cross-matches).

### Post-Fix Benchmark Data Available

All post-fix measurements against the fixed engine (Tier-1+2 + DEFCON-1 fixes active):

**Panel-vs-heuristic (`benchmark_all_checkpoints.txt`, 2026-04-16 17:57 UTC, n=500/side, nash temperatures):**

| Model | USSR WR | US WR | Combined | Rank |
|---|---|---|---|---|
| v56 | 54.6% | 35.6% | **45.1%** | #1 panel |
| v54 | 51.6% | 36.6% | 44.1% | #2 |
| v44 | 54.6% | 33.2% | 43.9% | #3 |
| v20 | 53.0% | 31.8% | 42.4% | #4 |
| v55 | 48.4% | 33.8% | 41.1% | #5 panel |
| v22 | 53.0% | 26.5% | 39.8% | (n=200) |
| v45 | 47.0% | 25.0% | 36.0% | (n=200) |
| v58 | 40.5% | 31.0% | 35.8% | (n=200) |
| v57 | 47.0% | 24.5% | 35.8% | (n=200) |

**v56 is now the top post-fix panel baseline**, not v55 (which was top Elo pre-fix).

**v56 vs panel head-to-head (`v56_baseline_benchmark.txt`, n=200/side):**

| Opponent | v56 USSR | v56 US |
|---|---|---|
| v20 | 59.0% | 37.0% |
| v44 | 69.5% | 38.0% (best for v56) |
| v54 | 56.0% | 41.0% |
| v55 | 48.5% | 42.5% (closest matchup) |
| v56 self | 61.5% | 37.5% (self-asymmetry) |

**Post-fix cross-match matrix (`panel_wr_matrix.json`, 2026-04-19 15:53):** This is the most complete cross-match data available post-fix. Contains 9 models (heuristic, v20, v44, v54, v55, v56, gnv1, gnv2, gnv3) with most pairwise WRs at n≈200 per direction. Key post-fix findings:

| Pair | A=USSR WR | B=USSR WR | Symmetric avg |
|---|---|---|---|
| gnv1 vs heuristic | 0.475 | 0.595 | 0.535 → gnv1 slightly above heuristic |
| gnv2 vs heuristic | 0.380 | 0.670 | 0.525 → gnv2 slightly above heuristic |
| gnv3 vs heuristic | 0.415 | 0.900 | 0.658 → gnv3 strongly above heuristic |
| gnv3 vs v56 | 0.630 | 0.650 | 0.640 → gnv3 beats v56 |
| gnv3 vs v55 | 0.600 | 0.670 | 0.635 → gnv3 beats v55 |
| gnv3 vs v54 | 0.635 | 0.640 | 0.638 → gnv3 beats v54 |
| gnv3 vs v44 | 0.600 | 0.625 | 0.613 → gnv3 beats v44 |
| gnv3 vs v20 | 0.555 | 0.570 | 0.563 → gnv3 beats v20 |
| gnv3 vs gnv1 | 0.560 | 0.530 | 0.545 → gnv3 slightly above gnv1 |
| gnv3 vs gnv2 | 0.590 | 0.590 | 0.590 → gnv3 above gnv2 |
| v56 vs v55 | 0.600 | 0.590 | ~0.505 (within CI of even) |
| v56 vs v20 | 0.625 | 0.595 | 0.510 |

**gnv3 is the single strongest post-fix model in the matrix**, beating every v20/v44/v54/v55/v56 panel member AND both other GNN variants. Self-play symmetry: gnv3 vs gnv3 USSR=0.72 is notably higher than the panel's (~0.58–0.60), meaning gnv3's side asymmetry is more pronounced than the panel's — this is a known symptom of the v3 chain.

**Post-fix A/B paired data (`ab_benchmark_tier1.json` + `ab_benchmark_full.json`):**

| Model | USSR WR | US WR | Combined | N/side | Note |
|---|---|---|---|---|---|
| gnn_card_attn_v1 | 0.490 | 0.405 | 0.4475 | 200 | Tier-1+2 engine |
| v1_ppo_best | 0.437 | 0.410 | 0.423 | 300 | Tier-1+2+frame_migration |
| v56 | 0.570 | 0.413 | 0.492 | 300 | Tier-1+2+frame_migration (best!) |
| v3_best | 0.360 | 0.147 | 0.253 | 300 | Tier-1+2+frame_migration (regressed) |

Note the engine-version drift: `ab_benchmark_full.json` uses `post-Tier1+2+frame_migration`, later than `ab_benchmark_tier1.json`'s `post-Tier1+Tier2`. These numbers supersede the 2026-04-16 panel benchmark where feature coverage is equal (i.e., v56 = 0.492 @ n=300 on the later engine is likely the most current figure, vs 0.451 @ n=500 on Tier-1+2).

**Post-fix specialist checkpoints (`v5_post_benchmark.txt`, n=1000):**

- `ppo_ussr_only_v5` (USSR side only): 60.3% vs heuristic — highest measured post-fix USSR WR.
- `ppo_us_only_v5` (US side only): 38.9% vs heuristic.

**Weight-averaged blends (`v5_weight_avg_quick.txt`, n=500/side):**

- `weight_avg_06` (alpha=0.6): 0.560 USSR / 0.354 US / **0.457 combined** — marginally above v56 baseline (0.420 at same n/side).

### Reconstructed Post-Fix Strength Ordering

Using the post-fix benchmark data as primary evidence, the **current best-estimate strength ordering** (combined WR vs heuristic + cross-match evidence):

| Rank | Model | Combined vs heuristic | Evidence | Engine |
|---|---|---|---|---|
| 1 | **gnv3** | ~65.8% symmetric vs heuristic | panel_wr_matrix.json | post-Tier-1+2 |
| 2 | ppo_ussr_only_v5 + ppo_us_only_v5 (hypothetical composite) | ≥49.6% combined if side-gated | v5_post_benchmark.txt | post-Tier-1+2 |
| 3 | weight_avg_06 | 45.7% | v5_weight_avg_quick.txt n=500 | post-Tier-1+2 |
| 4 | **v56** | 45.1–49.2% | benchmark_all_checkpoints.txt n=500 / ab_benchmark_full.json n=300 | post-Tier-1+2 |
| 5 | gnn_card_attn_v1 | 44.75% | ab_benchmark_tier1.json n=200 | post-Tier-1+2 |
| 6 | v54 | 44.1% | benchmark_all_checkpoints.txt n=500 | post-Tier-1+2 |
| 7 | v44 | 43.9% | benchmark_all_checkpoints.txt n=500 | post-Tier-1+2 |
| 8 | v20 | 42.4% | benchmark_all_checkpoints.txt n=500 | post-Tier-1+2 |
| 9 | v1_ppo_best | 42.3% | ab_benchmark_full.json n=300 | post-Tier-1+2+frame_migration |
| 10 | ppo_gnn_card_attn_v2 final | 42.2% | engine_fix_model_history analysis | post-Tier-1+2 |
| 11 | v55 | 41.1% | benchmark_all_checkpoints.txt n=500 | post-Tier-1+2 |
| 12 | gnv1 | 53.5% symmetric (above heuristic) but loses 47.5% USSR to heuristic — cross-match shows ~gnv1 ≈ panel | panel_wr_matrix.json | post-Tier-1+2 |
| 13 | gnv2 | 52.5% symmetric (slightly above heuristic) | panel_wr_matrix.json | post-Tier-1+2 |
| 14 | ppo_gnn_card_attn_v3 iter50 | 34.2% | engine_fix_model_history | post-Tier-1+2 |
| 15 | heuristic | 50% (self-reference baseline) | — | — |
| 16 | v3_best | 25.3% | ab_benchmark_full.json | post-Tier-1+2+frame_migration |

**Key reversals vs the stale Elo ladder:**
- v56 was 5th in pre-fix Elo, is now #1 of the panel post-fix (excluding GNNs and specialists).
- v55 was #1 in pre-fix Elo, is now last (5th) of the 5-panel.
- The panel-vs-heuristic Elo gap shrank from ~350 Elo to roughly 0–50 Elo.
- gnv3 (not in old ladder) is the single strongest model measured post-fix, ~14pp combined WR above v56 when cross-matched.

**Elo rescale estimate**: If heuristic = 1500 anchor and 45% WR implies ~35 Elo below, then the panel is at ~1465–1495 (all near the heuristic), gnv3 is at roughly 1585–1620, and specialists sit around 1515–1535. The old ladder's 2000+ scale is obsolete; a fresh Elo tournament would compress everyone into a ±150 Elo band around the heuristic.

### Missing Data

The following cross-match data needs to be re-run on the fixed engine to build a clean post-fix Elo ladder:

1. **Full 5×5 round-robin for the panel** (v20, v44, v54, v55, v56): the `panel_wr_matrix.json` has v*-vs-v* diagonals (self-play) but NOT off-diagonals between panel members. Cross-match data exists only in `v56_baseline_benchmark.txt` (v56 vs {v20,v44,v54,v55}, n=200/side) and `v5_post_benchmark.txt` (specialists vs panel, n=200/side). Need 10 pairwise matches at n≥500/side.

2. **gnv1/gnv2/gnv3 vs each other** at higher n (currently n≈200/direction). Add gnv3-vs-gnv3 self-play confirmation.

3. **gnv{1,2,3} vs panel** at n≥500/side (currently n≈200/direction).

4. **Specialists vs panel and vs GNN models**: no data for `ppo_ussr_only_v5` or `ppo_us_only_v5` vs panel — only vs heuristic.

5. **Heuristic anchor**: `heuristic vs heuristic` is null in the matrix (as expected) but there is no "heuristic vs scripted_heuristic" or similar cross-validation, so the heuristic's absolute placement has no redundancy.

6. **A post-fix paired-engine A/B** for any panel model (v20/v44/v54/v55/v56) was **never run**. The prior rules-fix plan specified this and it was skipped. Without it we cannot quantify the Tier-1+2 ΔWR per checkpoint, only the absolute post-fix number.

7. **`ppo_gnn_card_attn_v2` final checkpoint** has no head-to-head matches against anything — only vs heuristic panel-eval at n=30/opponent (too noisy).

8. **GNN models are completely missing from `elo_full_ladder.json`**. They were never added to the Elo solver input — only to `panel_wr_matrix.json`.

## Conclusions

1. **`results/elo/elo_full_ladder.json` is stale pre-fix data.** 100% of matches are `"reused": true`; last git-tracked modification was 2026-04-14, before BOTH the DEFCON-1 fix wave and the Tier-1+2 card fixes. Its absolute ratings (v55=2118, v56=2095, heuristic=1767) reflect the buggy engine where learned models exploited random-coup-driven heuristic self-destruction and card-event bugs.

2. **The pre-fix Elo gap of ~350 Elo between panel and heuristic is inflated by at least 250 Elo.** Post-fix benchmark data (n=500) shows the panel wins only 41–45% combined vs heuristic, implying a near-zero Elo gap (heuristic ~= panel on the fixed engine).

3. **Post-fix panel ranking inverts the pre-fix Elo ranking**: v56 (pre-fix Elo #6, 2095) is now the strongest panel member at 45.1% combined, while v55 (pre-fix Elo #1, 2118) is now the weakest at 41.1%. This suggests v55 was more fitted to the buggy exploits (likely cards 33 / 30 / 77) than v56 was.

4. **gnv3 is the strongest measured model post-fix**, with a roughly 14pp combined-WR edge over v56 in the cross-match data (63.5–63.8% vs v20/v44/v54/v55/v56). It also beats gnv1 and gnv2. gnv3 was never placed on the Elo ladder.

5. **USSR/US asymmetry (~0.55 vs ~0.35 combined, post-fix) is the dominant remaining signal** across the entire panel, specialists, GNNs, and the v2/v3 chains. This asymmetry is larger than any rule-fix, architecture, or training-iteration effect visible in the data, and is not addressed by the current training plan.

6. **The panel is tightly clustered post-fix**: all of v20–v56 fall into a 4pp band (41.1–45.1%). Any absolute Elo comparison between these models on fresh post-fix data would have CI widths approaching or exceeding the mean differences; the pre-fix 85-Elo-gap between v44 and v20 is not reproducible.

7. **Weight-averaged blends (`weight_avg_06` = 45.7%) and post-fix specialists (`ppo_ussr_only_v5` USSR=60.3%, `ppo_us_only_v5` US=38.9%)** are on par with or marginally above v56 — meaning no post-fix single-policy training has produced a clear win over the panel baseline. The new training chain (`gnn_card_attn_v1 → v2 → v3`) has not beaten v56 by the 3pp threshold.

8. **The GNN models (gnv1/gnv2/gnv3) are the one area where post-fix training has delivered**: gnv3 beats the entire panel in the cross-match matrix. This is the current strength-ordering discovery most worth preserving and extending.

## Recommendations

What to run to produce a clean post-fix Elo ladder (in priority order):

### P0 — Build a post-fix anchor and re-seed the ladder (BLOCKING for any future Elo work)

1. **Invalidate the existing match cache**. Rename or move the file whose cache the Elo solver pulls from (the source that produces `"reused": true` on every match) — likely `results/match_cache/` or the `metadata.sqlite3` match table. Add an `engine_version` column/filter so future runs never mix pre-fix and post-fix matches.

2. **Define a fresh anchor**. Use **v56** (strongest post-fix panel member) or **heuristic** (stable baseline) as the new anchor. Pin its Elo to 1500 (heuristic) or 1500+35 (v56 = ~1535). The old v14 anchor at 2015 is on an inflated scale and should be retired.

3. **Run a fresh 5×5 round-robin on the panel** (v20, v44, v54, v55, v56) at n=500/side per pair on the current engine (post-Tier-1+2+frame_migration). Add gnn_card_attn_v1 to make 6×6 = 30 directional pairs × 500 games/side = 15000 games. Estimated at ~2000 games/hr, this is ~7.5 hours on CPU.

### P1 — Place the GNN models and specialists on the ladder

4. **Add gnv1, gnv2, gnv3 to the ladder** via round-robin vs the 6-model panel at n=500/side. Include gnv3 self-play at n=1000 to characterize its USSR/US asymmetry (currently shown at 72% USSR in `panel_wr_matrix.json`).

5. **Add `ppo_ussr_only_v5`, `ppo_us_only_v5`, `weight_avg_06`** to the ladder. Specialists only play their trained side (use Elo-side-restricted placement as done for v*_USSR / v*_US in the bipartite anchor scheme).

### P2 — Quantify the fix effect (was specified but skipped)

6. **Paired-engine A/B**: check out commit `d8b8934^` (last commit before Tier-1), rebuild, run 500 games/side for v56, v44, v55 vs heuristic on both engines with identical seeds. Compute per-model ΔWR. This is the measurement that quantifies the Tier-1+2 effect and was listed in the prior analysis as Rec #2 but not executed.

### P3 — Panel integrity check (cheap sanity)

7. **Verify that scripted `.pt` panel files are unchanged since pre-fix era.** Compute SHA256 of `data/checkpoints/scripted_for_elo/v{20,44,54,55,56}_scripted.pt` and cross-check against git-logged hashes / backups. Also check `v55_scripted.pt.bak` vs current `v55_scripted.pt` — if logits differ, every v55 ladder number is suspect.

### P4 — Out of scope but worth flagging

8. **Address USSR/US asymmetry as its own experiment track.** The 2× US-win value-loss weight is already on but has not closed the gap. Candidate levers: 3–4× US-win weighting, US-specialist AWR upweighting, side-conditioned entropy schedule.

## Open Questions

1. **Was `elo_full_ladder.json` re-solved on 2026-04-19 (filesystem mtime) using the same pre-fix match cache?** If yes, the ratings remained identical (no new information entered). If the solver also received new matches, they would need `"reused": false` entries — which are zero in the file. Either the solver was invoked as a no-op or the invocation ran with an empty new-match queue. Worth confirming by replaying the solver's stdout log.

2. **What match cache key does the Elo solver use?** `results/match_cache_hash_identity.md` (Task #46 in memory) explicitly flagged this problem: key by filename, not by SHA256. If the key uses filename, swapping a `_scripted.pt` would silently fetch stale matches; if by SHA256, rebuilding changes keys. This directly determines whether invalidating the cache is safe or destructive.

3. **Is gnv3 truly +14pp stronger, or is it exploiting a residual rule bug?** The post-fix engine still has Tier-3 deferrals (cards 75, 50) and the `engine_rule_gaps.md` residuals. A per-card event-play-rate audit of gnv3 vs v56 games would reveal whether gnv3 relies on any remaining bug.

4. **Should the heuristic itself be re-benchmarked against a simpler baseline** (e.g., random legal policy) to establish absolute strength? Currently every ladder is anchored relative to "the heuristic on whatever engine version" — there's no external reference point.

5. **Are the pre-fix ISMCTS "94.5% combined" numbers obsolete?** Per `ismcts_retest_post_fix.md`, ISMCTS was SHELVED with `delta_vs_greedy = −0.225` — so ISMCTS is no longer a strength option, but its pre-fix numbers still float in some dashboards and should be flagged as pre-fix-only.

6. **When was the heuristic policy itself last modified?** If the heuristic code changed between the ladder booking and the 2026-04-16 re-benchmark (beyond the engine-level DEFCON guard), the comparison is further confounded. The `policies.cpp` DEFCON-related edits on 2026-04-13 may have changed heuristic card play in non-DEFCON situations.

---
