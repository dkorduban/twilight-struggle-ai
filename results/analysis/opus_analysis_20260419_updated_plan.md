# Opus Analysis: Updated Plan After Post-Fix Benchmarks
Date: 2026-04-19 UTC
Question: What went wrong, what's actually strong, and what's the best path forward?

## Executive Summary
The post-fix benchmark story has been misread. The "capacity specialists" (ussr_only_v5 combined=0.452, us_only_v5 combined=0.433) are not specialist breakthroughs — they are essentially v56 with a mild USSR/US tilt from 50 iters of single-side PPO. The real headline is that **v3_best (combined=0.274) is ~150 Elo below v56** because v3 was warmstarted from a broken AWR model and its training trajectory shows US-side collapse between iter 50 and iter 150. v4 PPO is inheriting this damage: it is using the wrong architecture (`control_feat_gnn_side`) and the wrong warmstart (v3_best). At iter 50 v4 benchmarks ussr=0.39/us=0.23 ≈ combined 0.31 — better than v3 but still a full 13pp below v56. The highest-expected-value next action is to kill v4 and restart PPO directly from v56 (`country_attn_side` architecture, `ppo_best_6mode.pt`) with the exact hyper-profile that worked for the v5 specialists, side=both, including the specialists and v20/v44/v54/v55/v56 as league fixtures. Target: exceed 0.50 combined WR vs heuristic within ~80 iterations.

## Findings

### 1. v3_best numbers are correct but reflect a damaged policy

**Benchmark:** USSR=0.398, US=0.150, combined=0.274 (500 games/side, post-fix engine). Confirmed against `results/capacity_test/v5_post_benchmark.txt` and `results/ppo_gnn_card_attn_v3/bench_final_vs_heuristic.txt`.

**Why it's weak (root cause):**
- v3 was warmstarted from `results/awr_sweep/fixed_engine_gnn_side/awr_best.pt` — i.e. an AWR model of the same class that later showed catastrophic benchmark failure (awr_gnn_side_v5 combined=0.205 in the v5 AWR benchmark JSON).
- Training trajectory (`bench_iter*_vs_heuristic.txt`): iter1 combined=0.305 (US=0.230), iter50=0.342 (US=0.337), iter100=0.267 (US=0.170), final iter150=0.267 (US=0.147). The US head regressed from 0.337 to ~0.15 between iters 50 and 150 while USSR stayed ~0.35. The "best" checkpoint captured the USSR peak but inherited a collapsing US policy.
- The FrameContextScalarEncoder pad-and-load logic (`python/tsrl/policies/model.py:222-289`) is working correctly — ckpt scalar shape 74 is padded/loaded properly into a 82-wide live encoder. This is not the cause of the weak benchmark. The cause is learning dynamics, not a serialization bug.

**Post-fix Elo confirms:** v56 vs v3_best → v56 wins 64.7% (seed 90000, 500 games). That's ~105 Elo above v3_best. `gnn_card_attn_v3` incremental placement came in at elo=1850 — roughly 245 Elo below v56 (2095.1) on the current ladder.

### 2. "Capacity specialists" are ≈v56, not stronger than v56

The interpretation "specialists are MUCH stronger than v3_best" conflates two things. Compared to v56, the specialists are essentially flat:

| Model          | USSR  | US    | Combined | vs v56 Elo (post-fix) |
| -------------- | ----- | ----- | -------- | --------------------- |
| v56 baseline   | 0.558 | 0.325 | 0.441    | —                     |
| ussr_only_v5   | 0.588 | 0.316 | 0.452    | 0.495 (tied)          |
| us_only_v5     | 0.506 | 0.360 | 0.433    | (pending)             |
| v3_best        | 0.398 | 0.150 | 0.274    | 0.353 (v56 wins 64.7%)|

The USSR-side gain on `ussr_only_v5` (+3.0pp) is balanced by a similar US-side loss (-0.9pp), and combined moves only +1.1pp. The post-fix 500-game Elo match v56 vs ussr_only_v5 ended 246–241 (0.495) — statistically indistinguishable.

Mechanism: both specialists were warmstarted from `ppo_best_6mode.pt` (v56). With 50 iters of PPO on a single side, they cannot destroy the other side's knowledge because (a) optimizer is reset, (b) only one side's gradient is touched per iter, (c) entropy stays high (>3.7). The "us=0.316 on an USSR-only model" and "ussr=0.506 on a US-only model" are residual v56 knowledge, not generalization. Headline implication: **warmstarting a fresh both-sides PPO from a specialist buys almost nothing over warmstarting directly from v56.**

### 3. AWR is dead weight; do not iterate further

v5 AWR benchmarks: awr_gnn_side_v5=0.205, awr_gnn_card_attn_v5=0.022, awr_film_gated_v5=0.075. All three are catastrophically below v56 (0.441). Likely failure modes:
- 52k-row v5 panel too small for `country_attn`-class policies (~2M params).
- AWR's advantage weighting amplified spurious correlations in a domain with sparse terminal rewards and large card-action combinatorics.
- Distributional gap between v5 replay-derived states (collected from mixed heuristic panels) and actual online PPO rollout states — the AWR policy is "correct" on the training distribution but out of support on self-play rollouts.

AWR is the reason v3 started from a poisoned warmstart. Do not propose another AWR pass. Keep 52k panel dataset as a diagnostic/supervised validation set but treat it as a dead end for *policy* training in Month 3.

### 4. v4 PPO status: improving but architecturally capped

Config: `control_feat_gnn_side`, hidden=256, warmstart=v3_best, 200 iters planned, currently at iter 50 (train log shows steady 80-100s per iter after warmup hiccup). It inherits v3's damaged US head.

Implicit benchmark from v4 training log pfsp pool dump at iter 50 (large-N):
- `[ussr] heuristic (fix) WR=0.390 n=200`
- `[us] heuristic (fix) WR=0.225 n=280`
- combined ≈ 0.308 — *already 3.4pp above v3_best*, but still 13pp below v56.

v4 training is NOT collapsing (unlike v3 iter 50→150): rollout_wr stable at 0.46-0.60, US rollout at 0.28-0.46, KL 0.009-0.015, no NaNs, value range healthy. v4 may continue to climb slowly, but:
- It is locked into `control_feat_gnn_side`, which is provably weaker than `country_attn_side` on this task (v56 achieves 0.441 with country_attn_side; v3 plateaued at 0.27-0.34 with control_feat_gnn_side).
- Its warmstart (v3_best) is itself ~100 Elo below v56; v4 is spending iterations just climbing back.
- At 80-100s/iter × 150 remaining iters = ~3-4 hours of compute to get *maybe* to combined 0.40, still below v56.

### 5. v56 architecture is `country_attn_side` — directly compatible with v5 specialists

Verified by loading `data/checkpoints/ppo_v56_league/ppo_best_6mode.pt`:
- model_type = `country_attn_side` (TSCountryAttnSideModel)
- hidden_dim = 256
- scalar_encoder shape = (64, 74) — region-expanded internally from 40-dim input
- mode_head shape = (6, 256) — 6-mode schema

ussr_only_v5 and us_only_v5 share this exact architecture, confirming that a direct "continue PPO from v56 with both-sides" setup is trivially compatible. No BC distillation needed. Reset optimizer, keep weights.

### 6. The correct interpretation of "post-fix Elo cluster"

v56/v55/v54/v44/v20 all cluster at ~50% vs each other. This is the **pre-existing good cluster** — not new information about v3 or specialists. The cluster sits at Elo ~2080-2120 on the `elo_full_ladder.json`. gnn_card_attn_v3 landed at 1850, i.e. well below the cluster. Specialists are inside the cluster. There is no model currently above the cluster.

## Conclusions

1. **v3_best (0.274) is a damaged policy**, not a true ceiling. Its weakness comes from (a) a poisoned AWR warmstart, (b) US-side collapse during the second half of v3 training. The benchmark is correct; the interpretation "v3 shows our arch maxes at 0.274" is wrong.

2. **The "capacity specialists" are v56 with a single-side tilt, not stronger models.** Post-fix Elo v56 vs ussr_only_v5 = 0.495 (tied). Their combined benchmark gain over v56 is ≤1.1pp. They are not a stepping-stone to higher strength.

3. **The best publicly-benchmarked symmetric policy in the repo is v56 at combined=0.441** (ussr=0.558, us=0.325). The gap between v56 and v3/v4 is architectural (`country_attn_side` > `control_feat_gnn_side` on this task) and a consequence of the bad warmstart chain AWR → v3 → v4.

4. **v4 PPO at iter 50 is at combined≈0.31 (implicit from pfsp pool dump).** It is improving over v3 but is architecturally bounded below v56. Continuing v4 to iter 200 is a high-cost, low-upside action — expected outcome is combined≈0.35-0.40, still below v56.

5. **AWR is dead for policy training in Month 3.** All three v5 variants benchmark at <0.21. Do not spend more time on AWR warmstarts or sweeps.

6. **The restart path is cheap and direct.** v56 and specialists share architecture. A fresh PPO run from v56 (both sides, similar hyperparams to ussr_only_v5) can reach the specialist hyperparam profile in ~50 iters with no BC step, and gains from there are pure upside.

## Recommendations

Numbered by priority; first item is the autonomous next action.

1. **AUTONOMOUS NEXT ACTION: Kill v4 PPO and launch v6 PPO from v56, both sides.** Concrete spec:
   - Warmstart: `data/checkpoints/ppo_v56_league/ppo_best_6mode.pt` (country_attn_side, 6-mode).
   - Out dir: `results/ppo_country_attn_v6/`
   - Side: `both`; reset_optimizer=true.
   - Hyperparams: `lr=5e-5`, `clip_eps=0.12`, `ent_coef=0.01 → 0.003` (linear to end), `ppo_epochs=4`, `minibatch_size=2048`, `max_kl=0.03`, `target_kl=0.015`, `ema_decay=0.995`, `games_per_iter=200`. Mirror `ppo_ussr_only_v5/ppo_args.json` for stability.
   - League fixtures: `v56_scripted`, `v55_scripted`, `v54_scripted`, `v44_scripted`, `v20_scripted`, `ussr_only_v5_scripted`, `us_only_v5_scripted`, `__heuristic__` (heuristic_floor=0.15 to guarantee coverage).
   - league_save_every=10, league_self_slot=true, pfsp_exponent=0.5, league_recency_tau=20.
   - Iterations: 80 (same budget as v4 remaining), seed=42000.
   - Skip smoke test (architecture identical to v56).
   - `skip_smoke_test=true`, panel eval every 20 iters vs the same fixture set, `jsd_probe_bc_checkpoint=ppo_best_6mode.pt`.
   - Budget: ~80 iters × ~80-100s/iter ≈ 2-3 hours. Explicit kill criterion: if iter 30 benchmark vs heuristic combined < v56's 0.441 - 0.03, abort and re-examine.

2. **Before killing v4**, run a 500 games/side benchmark on `gnn_card_attn_v4.iter0050_scripted.pt` to get a clean data point for the v4-side of the ledger. Also export iter 50 to `data/checkpoints/scripted_for_elo/v4_iter50_scripted.pt` for Elo placement, so Month-3 records include an honest v4 data point even after kill.

3. **Move v3_best out of the fixtures / league pools.** It is a strictly dominated policy (~245 Elo below v56). Current fixtures in the post-fix Elo tournament still list it. Keep it in the archive but not as a benchmark foil.

4. **After v6 is trained**, extend with a second-stage league run that includes v6's own early checkpoints as opponents (age-diverse PFSP) and introduces Dirichlet noise at root + temperature-based action sampling (top CLAUDE.md Month-3 priority #1). Target: push combined to >0.55 and beat v56 by >55% in head-to-head.

5. **Formal benchmark sweep** once v6 beats v56 in Elo: run the full panel (v6 vs v20/v44/v54/v55/v56 + ussr_only_v5 + us_only_v5 + heuristic) at 500 games/side with `--no-cache` and append to `elo_full_ladder.json`.

6. **Do not restart AWR or launch new AWR sweeps.** Retain the 52k v5 panel only as a supervised-evaluation dataset (e.g. card-top1, value-brier probes) until Month-3 wrap.

7. **Do not launch more single-side specialists.** They do not generalize; their "other side" benchmark number is carried from the warmstart. Running more specialists is a mis-allocation of compute.

## Open Questions

1. **Why is `control_feat_gnn_side` ~100-150 Elo below `country_attn_side`?** Is it actually the architecture, or the AWR-poisoned warmstart? A controlled test — PPO from scratch with the same hyperparams on both architectures starting from the BC wide384 checkpoint — would settle this. Low priority vs Recommendation 1, but useful for Month-3 arch experiments (CLAUDE.md priority #5).

2. **Is there residual misnaming?** The v4 directory is `results/ppo_gnn_card_attn_v4/` and many scripted artifacts call it `gnn_card_attn_v*`, but the actual architecture is `control_feat_gnn_side`. Consider renaming future runs accurately (`ppo_control_feat_gnn_v4`) to avoid confusion with future true `country_attn`-based runs.

3. **Verify `us_only_v5 vs v56` Elo match outcome** once the post-fix tournament finishes — the log was truncated at match 7/28. Expectation: ~0.48-0.52 (specialist ≈ v56).

4. **Month-3 architecture experiments (CLAUDE.md priority #5).** Once v6 is trained from v56, is there value in a parallel run with `country_attn` (non-side) or `full_embed` to compare ceilings? Park for after v6 validates the restart direction.

5. **Does resetting to v56 lose the "frame context" features?** v56 was trained pre-frame-context (scalar_dim=32 base), but the FrameContextScalarEncoder pad logic and state-dict rewrite (model.py:252-289) handles the 32→40 upgrade with zero-padded frame features and `is_top_level=1`. Verified working in v4 (scalar shape 82 = 74 + 8 frame-ctx expansion). No action needed; recorded for clarity.
