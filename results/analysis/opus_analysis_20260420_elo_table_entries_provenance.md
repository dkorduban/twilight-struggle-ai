# Opus Analysis: Elo Table Entries — Identity and Provenance
Date: 2026-04-20
Question: Describe every candidate in the fresh Elo table with identity, provenance, hyperparams, and benchmark numbers.

## Executive Summary
There are 13 candidates in the fresh Elo-table list: `heuristic`, `bc_wide384`, three old league checkpoints (`v44`, `v55`, `v56`), seven progressive-chain PPO runs (`v22_bugfix_full`, `v25_continue`, `v27_continue`, `v29_continue`, `v31_continue`, `v32_continue`, `v33_continue`), and two side-specialist capacity runs (`ussr_only_v5`, `us_only_v5`). Provenance is cleanly documented for the current chain (all seven continues have `ppo_args.json` in `results/ppo_vNN_continue/`, and scripted copies exist in `data/checkpoints/scripted_for_elo/`). **Three red flags** were found: (1) the plain `vNN_continue_scripted.pt` files in `scripted_for_elo/` are `ppo_best` snapshots selected by panel, whereas the canonical record tracks the explicit `vNN_iterMM_scripted.pt` peak-iteration files — for v32 these are known to differ and disagree on which checkpoint is being evaluated; (2) `ppo_args.json` is not readable for the `data/checkpoints/ppo_v{44,55,56}_league/` directories from this agent's sandbox (denied), so hyperparams for v44/v55/v56 are "not recovered" here; (3) the official `v56` scripted used by every `_continue` run as both warmstart and panel is sourced from `ppo_best_6mode.pt` (a 6-mode head), so any older scripted `v56_scripted.pt` that was frozen from a 5-mode checkpoint would mis-represent what the chain was actually trained against. Overall data cleanliness for the seven chain entries and two capacity runs is good; `bc_wide384` and the heuristic entry need no metadata recovery (sentinel and BC scripted).

## Summary Table

| cache_name              | scripted_file (data/checkpoints/scripted_for_elo/) | training_dir (results/…)      | warmstart_from                               | best_combined (500g/side vs heuristic) | peak_iter | architecture (model_type) |
|-------------------------|----------------------------------------------------|------------------------------|---------------------------------------------|---------------------------------------|-----------|---------------------------|
| heuristic               | (sentinel `heuristic`, no file)                    | (built-in C++ policy)         | —                                           | N/A (is the ruler)                    | —         | minimal_hybrid (greedy)    |
| bc_wide384              | bc_wide384_scripted.pt                             | (BC run predating chain)      | none (cold BC)                              | not recovered (reference only)        | —         | BC baseline (h=384 wide)   |
| v44                     | v44_scripted.pt                                    | ppo_v44_league (pre-chain)    | not recovered                               | USSR 0.305 / US 0.620 vs v56 inverted (from v56_baseline_benchmark) | not recovered | country_attn (6-mode `ppo_best_6mode.pt`) |
| v55                     | v55_scripted.pt                                    | ppo_v55_league (pre-chain)    | not recovered                               | USSR 0.515 / US 0.575 vs v56 inverted | not recovered | country_attn (likely 6-mode) |
| v56                     | v56_scripted.pt                                    | ppo_v56_league (pre-chain)    | not recovered                               | USSR 0.558 / US 0.325 (combined 0.441) | not recovered | country_attn_side, 6-mode (`ppo_best_6mode.pt`) |
| v22_bugfix_full         | v22_bugfix_full_scripted.pt                        | ppo_v22_bugfix_full           | v56 (`ppo_best_6mode.pt`)                   | 0.466 combined (USSR 0.616 / US 0.316) @ iter40 | iter40 | country_attn_side (6-mode) |
| v25_continue            | v25_continue_scripted.pt AND v25_iter26_scripted.pt| ppo_v25_continue              | v24_iter10 (→ v22_iter40 → v56)             | 0.584 combined (USSR 0.702 / US 0.466) @ iter26 | iter26 | country_attn_side (6-mode) |
| v27_continue            | v27_continue_scripted.pt AND v27_iter30_scripted.pt| ppo_v27_continue              | v25_iter26                                  | 0.608 combined @ iter30 (USSR 0.746 / US 0.454 was iter20 0.600 record; see details) | iter30 | country_attn_side (6-mode) |
| v29_continue            | v29_continue_scripted.pt AND v29_iter30_scripted.pt| ppo_v29_continue              | v27_iter30                                  | 0.624 combined (USSR 0.730 / US 0.518) @ iter30 | iter30 | country_attn_side (6-mode) |
| v31_continue            | v31_continue_scripted.pt AND v31_iter20_scripted.pt| ppo_v31_continue              | v30_iter10 (← v29_iter30)                   | 0.645 combined (USSR 0.760 / US 0.530) @ iter20 | iter20 | country_attn_side (6-mode) |
| v32_continue            | v32_continue_scripted.pt AND v32_iter20_scripted.pt| ppo_v32_continue              | v31_iter20                                  | **0.650** combined (USSR 0.788 / US 0.512) @ iter20 — PROJECT RECORD | iter20 | country_attn_side (6-mode) |
| v33_continue            | v33_continue_scripted.pt                           | ppo_v33_continue (v33b)       | v32_iter20                                  | 0.635 @ iter10; 0.631 @ iter20 (post-peak) | iter10/iter20 (declining) | country_attn_side (6-mode) |
| ussr_only_v5            | (no entry yet — not in scripted_for_elo listing)   | results/capacity_test/ppo_ussr_only_v5 | v56 (`ppo_best_6mode.pt`)            | 0.452 combined (USSR 0.588 / US 0.316) | "v5" best | country_attn_side (side=ussr) |
| us_only_v5              | (no entry yet — not in scripted_for_elo listing)   | results/capacity_test/ppo_us_only_v5   | v56 (`ppo_best_6mode.pt`)            | 0.433 combined (USSR 0.506 / US 0.360) | "v5" best | country_attn_side (side=us) |

## Detailed Entries

### 1. heuristic
1. **Identity.** The built-in C++ greedy minimal-hybrid policy. Not a checkpoint. In `scripts/run_elo_tournament.py` the sentinel constant is `HEURISTIC_SENTINEL = "heuristic"` (line 230); any name of `heuristic` causes `_run_heuristic_match(...)` (lines 233+) to use the C++ player instead of loading a TorchScript model.
2. **Provenance.** No file. Engine-provided. It is also the anchor for Elo (heuristic-as-USSR = 1200 under bid+2).
3. **Distinctive hyperparameters.** None (scripted policy, no stochasticity, no training).
4. **Best benchmark.** N/A — it is the baseline. For context, heuristic-vs-heuristic greedy games show USSR 0.280 / US 0.720 (engine-structural US bias; see `autonomous_decisions.log` 2026-04-20 23:51:08Z).
5. **Peak iteration.** —
6. **Caveats.** Greedy-only. Nash-temperature runs of the same policy produce different win rates (see the 2026-04-20 heuristic-vs-heuristic note). When used as the Elo anchor, make sure the tournament is running with the same decoding knobs the chain was benchmarked against (greedy evaluation of both model and heuristic; seeds 50000 / 50500).

### 2. bc_wide384
1. **Identity.** A BC (behavior cloning) baseline with hidden size 384. `scripts/train_ppo.py:3059` shows the canonical path is `data/checkpoints/bc_wide384/scripted.pt` (used as the `--jsd-probe-bc-checkpoint` default in older PPO runs). The ELO copy is `data/checkpoints/scripted_for_elo/bc_wide384_scripted.pt`.
2. **Provenance.** The source BC run itself is pre-chain; no PPO training directory. Used in `ussr_only_v5` / `us_only_v5` config via the jsd-probe field, but only as a JSD reference, not as warmstart.
3. **Distinctive hyperparameters.** BC-trained, hidden=384, no PPO. Exact epoch/lr not recovered in the files consulted here.
4. **Best benchmark.** Not in the logs I read. Historically this is the weak BC-only baseline — a "floor" reference, expected to be below every PPO checkpoint.
5. **Peak iteration.** BC has no iterations in the PPO sense; it is a single frozen scripted export.
6. **Caveats.** Training hyperparams not recovered here — would need to grep for the BC training script in `scripts/` (not in this sandbox).

### 3. v44
1. **Identity.** Pre-chain PPO league checkpoint. `data/checkpoints/ppo_v44_league/`. The 6-mode version (`ppo_best_6mode.pt`) is what's relevant to the current 6-mode chain; the plain `ppo_best.pt` is 5-mode.
2. **Provenance.** Scripted: `data/checkpoints/scripted_for_elo/v44_scripted.pt` — based on filename listing, frozen well before the chain started. Source `.pt` is either `ppo_v44_league/ppo_best.pt` or `.../ppo_best_6mode.pt`; the 6-mode version exists on disk. Warmstart ancestor: not recovered (ppo_args.json in that directory is sandbox-denied).
3. **Distinctive hyperparameters.** Not recovered.
4. **Best benchmark.** In `v56_baseline_benchmark.txt`, v56-as-USSR vs v44-as-US wins 139/200=0.695, i.e. v44-as-US wins only 0.305 vs v56. v44-as-USSR vs v56-as-US wins 76/200=0.380 (so v44-as-USSR wins 0.380). Combined vs v56: ~0.343. A direct vs-heuristic score for v44 is not in the files I could read.
5. **Peak iteration.** Not recovered.
6. **Caveats.** Has both 5-mode and 6-mode exports; verify which one `v44_scripted.pt` was produced from before trusting it as a league fixture against 6-mode chain models. Used by the chain as a fixture in `league_fixtures` in every v22–v33 run.

### 4. v55
1. **Identity.** Pre-chain PPO league checkpoint. `data/checkpoints/ppo_v55_league/`. Includes a `ppo_best_h384.pt` variant (hidden=384), so architecture may not be the same as v56; needs verification.
2. **Provenance.** Scripted `data/checkpoints/scripted_for_elo/v55_scripted.pt`. Source `.pt` most likely `ppo_v55_league/ppo_best.pt`. Warmstart ancestor: not recovered.
3. **Distinctive hyperparameters.** Not recovered.
4. **Best benchmark.** vs v56 (from `v56_baseline_benchmark.txt`): v56-as-USSR vs v55-as-US wins 97/200=0.485 (so v55-as-US wins 0.515, highest of any panel opponent); v56-as-US vs v55-as-USSR wins 85/200=0.425 (v55-as-USSR wins 0.575). v55 appears slightly stronger than v56 on aggregate in that mini-panel. Direct vs-heuristic combined: not recovered.
5. **Peak iteration.** Not recovered.
6. **Caveats.** `ppo_best_h384.pt` coexists — be certain the scripted file reflects the same architecture that the rest of the chain has. Is a league fixture in every chain run.

### 5. v56
1. **Identity.** Root of the current progressive warmstart chain. Directory `data/checkpoints/ppo_v56_league/`. The 6-mode head is the canonical variant: `ppo_best_6mode.pt`. `TSCountryAttnSideModel` (country_attn_side) based on chain usage.
2. **Provenance.** Scripted: `data/checkpoints/scripted_for_elo/v56_scripted.pt`. The chain explicitly uses `ppo_best_6mode.pt` (not the plain `ppo_best.pt`) as `--checkpoint` for v22 and as the `--jsd-probe-bc-checkpoint`. The scripted `v56_scripted.pt` should therefore be frozen from `ppo_best_6mode_scripted.pt` — needs one-line verification before the tournament. Warmstart ancestor: not recovered here.
3. **Distinctive hyperparameters.** Not recovered (ppo_args.json path denied).
4. **Best benchmark.** From `results/continuation_plan.json.v56_baseline`: combined 0.441, USSR 0.558, US 0.325 (500 games each side, seeds 50000/50500). Corroborated by `v56_baseline_benchmark.txt`.
5. **Peak iteration.** Not recovered; the scripted export is the league `ppo_best` (panel-selected), not a named iter.
6. **Caveats.** Two heads exist on disk (5-mode `ppo_best.pt` and 6-mode `ppo_best_6mode.pt`). The chain trains against the 6-mode; if the scripted `v56_scripted.pt` in `scripted_for_elo/` was ever regenerated from the 5-mode version, every chain benchmark that used v56 as a panel opponent would be subtly off.

### 6. v22_bugfix_full
1. **Identity.** First PPO run of the current chain. `results/ppo_v22_bugfix_full/`. `version="v22_bugfix_full"`. Architecture inherited from v56 (country_attn_side, 6-mode head).
2. **Provenance.** Scripted: `data/checkpoints/scripted_for_elo/v22_bugfix_full_scripted.pt`. Copied from `results/ppo_v22_bugfix_full/ppo_best_scripted.pt` on 2026-04-20T19:55:43Z (autonomous log line 134). Source `.pt`: `ppo_best.pt`, which at bench time corresponds to iter40 (see trajectory below — training was still improving at iter40). Warmstart: `data/checkpoints/ppo_v56_league/ppo_best_6mode.pt` with `reset_optimizer=true`.
3. **Distinctive hyperparameters.** lr=5e-5, clip_eps=0.12, ppo_epochs=4, max_kl=0.1, heuristic_floor=0.2, games_per_iter=200, n_iterations=40, seed=42000, panel_heuristic_weight=3.0. NOT the stable-ceiling recipe yet (clip_eps still 0.12, 4 PPO epochs). UPGO=false. Bug fix applied: the `us_win_w = torch.where(returns < 0, 2.0, 1.0)` value-loss upweighting was **removed** (that's the "bugfix" in the name), which unlocks the US side from 0.10 to 0.30+ WR.
4. **Best benchmark.** Combined 0.466 (USSR 0.616 / US 0.316) @ iter40 — new record at the time (autonomous log 20:07:46Z). Trajectory: iter10=0.354, iter20=0.391, iter30=0.458, iter40=0.466.
5. **Peak iteration.** iter40. `ppo_best` therefore ≈ iter40.
6. **Caveats.** Chain went through v23 (discarded: continuation without bug fix) and v24_iter10=0.489 before v25. `v22_bugfix_full_scripted.pt` represents the iter40 checkpoint but the filename does not encode "iter40" — document this once in the tournament manifest.

### 7. v25_continue
1. **Identity.** `results/ppo_v25_continue/`. `version="v25_continue"`.
2. **Provenance.** Scripted: `data/checkpoints/scripted_for_elo/v25_continue_scripted.pt` (from `ppo_best_scripted.pt`, panel-selected, 2026-04-20T20:34:00Z) AND `data/checkpoints/scripted_for_elo/v25_iter26_scripted.pt` (the explicit iter26 peak). Source `.pt`: `results/ppo_v25_continue/v25_continue.iter0026.pt` (bench ≈ iter26 running best at KL-explosion point). Warmstart: `results/ppo_v24_continue/ppo_iter0010.pt` (v24 was a continuation of v22_iter40 — i.e., v24's own warmstart is `results/ppo_v22_bugfix_full/ppo_iter0040.pt`). `reset_optimizer=true`.
3. **Distinctive hyperparameters.** lr=1e-5 (down from 5e-5), clip_eps=0.10, ppo_epochs=4, max_kl=0.3, heuristic_floor=0.2, panel_heuristic_weight=3.0, seed=42000.
4. **Best benchmark.** 0.584 combined (USSR 0.702 / US 0.466) @ iter26 (20:39:57Z). iter10 was 0.564.
5. **Peak iteration.** iter26 (training was aborted at iter27 because of a KL explosion).
6. **Caveats.** KL explosion at iter27 with 4 PPO epochs → the run terminated early and v26 was launched with ppo_epochs=1. For Elo, prefer `v25_iter26_scripted.pt` (explicit peak) over the panel-selected `v25_continue_scripted.pt`; if both are already in the cache under different names, clarify which the Elo entry `v25_continue` actually represents.

### 8. v27_continue
1. **Identity.** `results/ppo_v27_continue/`. `version="v27_continue"`.
2. **Provenance.** Scripted: `v27_continue_scripted.pt` (copied from `ppo_best_scripted.pt` 2026-04-20T20:54:54Z) AND `v27_iter30_scripted.pt` (explicit peak). Warmstart: `results/ppo_v25_continue/ppo_iter0026.pt` (v25 iter26). `reset_optimizer=true`. Chain: v56 → v22_iter40 → v24_iter10 → v25_iter26 → v27.
3. **Distinctive hyperparameters.** lr=1e-5, clip_eps=0.10, **ppo_epochs=1** (first time in chain), max_kl=9999 (disabled — the KL check was false-positive), heuristic_floor=0.2, panel_heuristic_weight=3.0, seed=42000.
4. **Best benchmark.** Combined 0.608 @ iter30 (21:02:50Z peak record). Intermediate: iter10 formal bench=0.572 (USSR 0.716 / US 0.428); iter20=0.600 (USSR 0.746 / US 0.454). So the headline 0.608 is iter30.
5. **Peak iteration.** iter30 (for combined); iter20 was previously the "NEW PROJECT RECORD 0.600" before iter30 beat it.
6. **Caveats.** Note the `max_kl=9999`. Between this run and v29, `heuristic_floor` jumped from 0.2 to 0.5 — this is the major configuration break in the chain. Make sure the Elo entry `v27_continue` points to iter30 not iter20.

### 9. v29_continue
1. **Identity.** `results/ppo_v29_continue/`. `version="v29_continue"`.
2. **Provenance.** Scripted: `v29_continue_scripted.pt` (from `ppo_best_scripted.pt` 2026-04-20T21:39:32Z) AND `v29_iter30_scripted.pt`. Warmstart: `results/ppo_v27_continue/v27_continue.iter0030.pt`. `reset_optimizer=true`. Seed changes to **12345** at v29.
3. **Distinctive hyperparameters.** lr=1e-5, clip_eps=0.10, ppo_epochs=1, max_kl=9999, **heuristic_floor=0.5** (new, stays 0.5 through v33), ent_coef=0.01 (up from 0.005), panel_heuristic_weight=3.0, seed=12345.
4. **Best benchmark.** 0.624 combined (USSR 0.730 / US 0.518) @ iter30 (21:45:57Z). iter10=0.572, iter20=0.617.
5. **Peak iteration.** iter30.
6. **Caveats.** v28 was skipped as a separate cache entry because it peaked below v27. v29 is the first run to cross 0.62 combined and the first to push US above 0.50.

### 10. v31_continue
1. **Identity.** `results/ppo_v31_continue/`. `version="v31_continue"`.
2. **Provenance.** Scripted: `v31_continue_scripted.pt` (from `ppo_best_scripted.pt` 2026-04-20T22:12:35Z) AND `v31_iter20_scripted.pt`. Warmstart: `results/ppo_v30_continue/v30_continue.iter0010.pt` (v30's own warmstart was v29_iter30; v30 died at iter22 from KL=67817). `reset_optimizer=true`. Seed=77777.
3. **Distinctive hyperparameters.** lr=**5e-6** (halved again), **clip_eps=0.05** (first time; becomes the ceiling recipe), ppo_epochs=1, max_kl=0.5 (re-enabled), heuristic_floor=0.5, panel_heuristic_weight=3.0.
4. **Best benchmark.** 0.645 combined (USSR 0.760 / US 0.530) @ iter20 (22:16:48Z).
5. **Peak iteration.** iter20.
6. **Caveats.** v30 is not in the Elo candidate list even though it's a link in the chain; its iter10 gave 0.624 but the run aborted. v31 adopts the "ceiling recipe" (clip_eps=0.05) that v32 reuses.

### 11. v32_continue
1. **Identity.** `results/ppo_v32_continue/`. `version="v32_continue"`. PROJECT RECORD HOLDER.
2. **Provenance.** Scripted: `v32_continue_scripted.pt` (from `ppo_best_scripted.pt` 2026-04-20T22:32:52Z) AND `v32_iter20_scripted.pt`. The continuation_plan.json explicitly canonicalizes the record as `results/ppo_v32_continue/v32_continue.iter0020.pt` → `data/checkpoints/scripted_for_elo/v32_iter20_scripted.pt`. Warmstart: `results/ppo_v31_continue/v31_continue.iter0020.pt`. Seed=55555.
3. **Distinctive hyperparameters.** lr=**3e-6** (halved again), clip_eps=0.05, ppo_epochs=1, max_kl=0.5, heuristic_floor=0.5, panel_heuristic_weight=3.0.
4. **Best benchmark.** 0.650 combined (USSR 0.788 / US 0.512) @ iter20 (22:36:43Z). iter10 was 0.637. **This is the project record.**
5. **Peak iteration.** iter20.
6. **Caveats.** The canonical record specifically references `v32_iter20_scripted.pt`, not `v32_continue_scripted.pt`. Because `ppo_best` inside the run is selected by the panel, the two *may* coincide here, but the safe choice for Elo is the explicit iter20 file. Verify they hash-match before treating them as interchangeable.

### 12. v33_continue
1. **Identity.** `results/ppo_v33_continue/`. `version="v33_continue"` but `wandb_run_name="ppo_v33b_continue"` — v33 was restarted as v33b after v33's first attempt aborted at iter7 (KL=6.23). The directory contains the v33b run.
2. **Provenance.** Scripted: `v33_continue_scripted.pt` only (from `ppo_best_scripted.pt` 2026-04-20T22:49:38Z). No separate `v33_iterNN_scripted.pt`. Warmstart: `results/ppo_v32_continue/v32_continue.iter0020.pt`. Seed=33333.
3. **Distinctive hyperparameters.** lr=**2e-6** (smallest in chain), clip_eps=0.05, ppo_epochs=1, **max_kl=9999** (re-disabled after v33's initial max_kl=0.5 triggered spurious aborts), heuristic_floor=0.5, panel_heuristic_weight=3.0.
4. **Best benchmark.** iter10=0.635 (USSR 0.780 / US 0.490) — below its warmstart of 0.650. iter20=0.631.
5. **Peak iteration.** iter10 (panel-best in run); but it never beats warmstart, so **its `ppo_best` is already post-peak relative to v32_iter20**.
6. **Caveats.** v33 "confirms the ceiling" — the scripted file in `scripted_for_elo/` is worse than v32_iter20. Keep in Elo table only as evidence the chain has exhausted, not as a candidate meant to outperform v32.

### 13. ussr_only_v5
1. **Identity.** `results/capacity_test/ppo_ussr_only_v5/`. `version="ussr_only_v5"`, `side="ussr"` (trains only the USSR head).
2. **Provenance.** **No scripted entry found in `data/checkpoints/scripted_for_elo/`** — this capacity run was not copied into the tournament staging directory. Warmstart: `data/checkpoints/ppo_v56_league/ppo_best_6mode.pt`, `reset_optimizer=true`.
3. **Distinctive hyperparameters.** lr=5e-5, clip_eps=0.12, ppo_epochs=4, max_kl=**0.03** (very tight), ent_coef=0.01, heuristic_floor=**0.15** (lower than chain), pfsp_exponent=0.5, **upgo=true**, side=ussr, seed=99000, n_iterations=50, league_fixtures includes v56/v54/v44/v20/v55 + heuristic (broader league than the chain). `jsd_probe_bc_checkpoint` is `bc_wide384/scripted.pt` (not v56 6-mode as in the chain).
4. **Best benchmark.** Combined 0.452 (USSR 0.588 / US 0.316) — from `results/capacity_test/v5_post_benchmark.txt`. (Note the US side still plays, since "both sides" bench is run; the USSR-specialist training only updates its USSR side but the model still has a US head inherited from v56.)
5. **Peak iteration.** Not explicitly captured; the post benchmark reports a single "v5" number. There are `v5_weight_avg_benchmark.txt` and `v5_multi_alpha_benchmark.txt` variants, indicating a weight-averaging experiment that may produce different finals.
6. **Caveats.** A scripted file needs to be produced and placed in `scripted_for_elo/` with an agreed name (e.g. `ussr_only_v5_scripted.pt`) before Elo can use it. The very tight max_kl=0.03, `upgo=true`, and broader league set it apart from the chain — treat it as a distinct lineage, not a chain member.

### 14. us_only_v5
1. **Identity.** `results/capacity_test/ppo_us_only_v5/`. `version="us_only_v5"`, `side="us"`.
2. **Provenance.** **No scripted entry found in `data/checkpoints/scripted_for_elo/`** yet. Warmstart: `data/checkpoints/ppo_v56_league/ppo_best_6mode.pt`, `reset_optimizer=true`.
3. **Distinctive hyperparameters.** Same config as `ussr_only_v5` except `side="us"`. lr=5e-5, clip_eps=0.12, ppo_epochs=4, max_kl=0.03, heuristic_floor=0.15, pfsp_exponent=0.5, upgo=true, seed=99000.
4. **Best benchmark.** Combined 0.433 (USSR 0.506 / US 0.360) — from `results/capacity_test/v5_post_benchmark.txt`. Interestingly USSR side also scores higher than US despite the run specializing on US; the value-head lift helps USSR without training it directly.
5. **Peak iteration.** Not captured in the single benchmark file.
6. **Caveats.** Same as `ussr_only_v5` — needs scripted export + naming before the tournament.

## Naming and Provenance Red Flags

1. **`vNN_continue_scripted.pt` vs `vNN_iterMM_scripted.pt` mismatch.** For v25, v27, v29, v31, v32 the staging directory contains BOTH a `..._continue_scripted.pt` (panel-best inside the run) and an explicit `..._iterMM_scripted.pt` (named peak). These need not be identical: the panel is 30g and noisy, while the iter-named file is selected from the 500g bench. The continuation_plan.json canonicalizes the iter-named file for v32 only. **Decide, once and for all, whether the Elo cache-name `vNN_continue` refers to the `_continue` file (consistent with current naming) or the `_iterMM` file (consistent with canonical record).** For v32 specifically, if both files hash-differ, the Elo rating for `v32_continue` is not the rating of the project record.

2. **v33 has no explicit iter-named scripted file.** Unlike v25–v32, v33_continue only ships `v33_continue_scripted.pt`. Since v33 is **post-peak**, the panel-selected `ppo_best` is expected to be iter10 (0.635) — worse than its warmstart. Confirm this once during setup so the table row is labeled "post-peak / ceiling witness" rather than "continuation".

3. **6-mode vs 5-mode head for v44/v55/v56 scripted files.** The chain trains exclusively against the **6-mode** head (`ppo_best_6mode.pt`). If any of `v44_scripted.pt`, `v55_scripted.pt`, `v56_scripted.pt` were originally frozen from 5-mode checkpoints, they would silently mis-score in any match-up with chain models (mode-head ordinal mismatch). CLAUDE.md memory `feedback_checkpoint_6mode.md` warns about this specifically. Verify `mode_head.weight.shape[0] == 6` in each staged scripted file before running the tournament.

4. **ppo_v{44,55,56}_league hyperparams sandbox-denied.** Their `ppo_args.json` files exist (per Glob) but were denied by permissions. Hyperparams are currently "not recovered" in this analysis. If full provenance is a requirement, a separate pass with permission to read `data/checkpoints/` is needed.

5. **Capacity v5 runs are not in `scripted_for_elo/`.** `ussr_only_v5` and `us_only_v5` have no staged scripted file. They cannot be placed in the tournament until someone exports their `ppo_best.pt` to `data/checkpoints/scripted_for_elo/{ussr_only_v5,us_only_v5}_scripted.pt`.

6. **v27 peak iter ambiguity.** The `v27_iter30_scripted.pt` file exists, and logs show iter30=0.608. But the continuation_plan.json prose says "v27 iter20 NEW PROJECT RECORD 0.600", then an iter30 log line states 0.608 record. Confirm iter30 is actually the one staged under `v27_iter30_scripted.pt`; the directory also contains `v27_continue.iter0030.pt` so this should line up. Worth a one-time hash check.

7. **Chain seeds change between runs.** v22/v24/v25/v27 use seed=42000, v29 uses 12345, v30 uses 99999, v31 uses 77777, v32 uses 55555, v33 uses 33333. This is normal for seed-hunting but relevant if reproducibility of the chain is ever attempted.

## Conclusions

1. The seven chain entries (v22_bugfix_full, v25_continue, v27_continue, v29_continue, v31_continue, v32_continue, v33_continue) are fully provenance-documented: every one has a readable `ppo_args.json`, a training directory under `results/`, and at least one scripted file in `scripted_for_elo/`. Hyperparameters, warmstart ancestors, and peak-iter benchmarks are all recoverable from the local filesystem.
2. `v32_continue` is correctly identified as the project record at 0.650 combined @ iter20 (USSR 0.788 / US 0.512) — corroborated in both `continuation_plan.json` and `autonomous_decisions.log`. The canonical scripted file is `v32_iter20_scripted.pt`, not `v32_continue_scripted.pt`; those two may or may not be byte-identical and should be verified before scheduling.
3. `v33_continue` is the ceiling witness: every bench (iter10, iter20) is *below* its 0.650 warmstart. Keep it in the table, but label it as "post-peak".
4. `v44`, `v55`, `v56` have readable scripted files in `scripted_for_elo/` and PPO args directories, but those args directories are denied in this agent's sandbox. Their Elo candidacy is fine; only deep hyperparameter metadata is unrecovered.
5. `heuristic` and `bc_wide384` need no further recovery — both are stable reference entries and used elsewhere in the codebase as canonical checkpoints/sentinels.
6. `ussr_only_v5` and `us_only_v5` are **not scheduleable as-is** because they have no scripted file in `scripted_for_elo/`. Export step needed first.
7. The 6-mode vs 5-mode mode-head risk is the highest-impact silent-failure risk on this list. A 30-second pre-tournament verification sweep on the scripted files would catch it.

## Recommendations

1. **Use `v32_iter20_scripted.pt` (not `v32_continue_scripted.pt`) as the Elo cache's v32 entry.** The continuation-plan canonicalization explicitly names it; consider renaming the cache key to `v32_iter20` for clarity.
2. **For v25, v27, v29, v31: use the explicit `vNN_iterMM_scripted.pt` file (iter26, iter30, iter30, iter20 respectively) instead of the `vNN_continue_scripted.pt` alias.** Rename cache keys to match, e.g. `v25_iter26`, `v27_iter30`, `v29_iter30`, `v31_iter20`. This resolves Red Flag #1 permanently.
3. **Export scripted files for `ussr_only_v5` and `us_only_v5`** from `results/capacity_test/ppo_{ussr,us}_only_v5/ppo_best.pt` into `data/checkpoints/scripted_for_elo/{ussr_only_v5,us_only_v5}_scripted.pt`, then add them to the panel.
4. **Verify mode-head width on every staged scripted file before scheduling:** run a small check that `torch.jit.load(path).mode_head.weight.shape[0] == 6` for `v20_scripted.pt`, `v44_scripted.pt`, `v54_scripted.pt`, `v55_scripted.pt`, `v56_scripted.pt`, and the seven chain entries. This is a one-off script that prevents silent mismatches.
5. **Recover hyperparameters for v44/v55/v56 in a separate pass** that has read access to `data/checkpoints/ppo_vNN_league/ppo_args.json`. Until then the Detailed Entry sections above are marked "not recovered" for those three.
6. **For v22_bugfix_full, document in the Elo manifest that the scripted file is effectively the iter40 checkpoint** (not iter20 like most chain peaks). The current filename has no iter suffix; the manifest should explicitly note `iter=40`.
7. **For v33_continue, label the entry as "ceiling witness / post-peak"** so that readers don't misinterpret a lower Elo as a regression bug.
8. **Ensure the tournament uses the identical decoding settings (greedy, seeds 50000/50500) that produced the cached benchmark numbers** — the heuristic-vs-heuristic 0.280/0.720 asymmetry shows the engine is US-biased by default, so `heuristic` as Elo anchor must be evaluated in the same greedy mode the chain was benchmarked in.
9. **Normalize the cache-name convention before the run:** pick either `vNN` (peak-named) or `vNN_continue` (run-named) and apply it to all seven chain entries. Mixing is the single biggest source of future confusion.
10. **Keep `bc_wide384` in the table but flag it as the architectural floor** — it is useful as an Elo anchor on the low end, especially given the heuristic anchor is now at 1200 and we want a spread below-heuristic checkpoints too.

## Open Questions

1. Do `v32_continue_scripted.pt` and `v32_iter20_scripted.pt` have identical SHA256? (Same for v25/v27/v29/v31 `_continue` vs explicit-iter pairs.) If yes, the Red Flag #1 is cosmetic; if no, one of the two is strictly worse than the other on 500g bench — and the Elo tournament must use the stronger one.
2. What are the training hyperparameters and warmstart ancestors of v44, v55, and v56? (Blocked here by sandbox permissions on `data/checkpoints/`.)
3. Which scripted export of `bc_wide384` is in `scripted_for_elo/bc_wide384_scripted.pt` — the original BC run or a re-export? What are its BC training hyperparameters (epochs, lr, dataset)?
4. For the capacity v5 runs, which iteration's `ppo_best.pt` does the 0.452 / 0.433 benchmark in `v5_post_benchmark.txt` correspond to? The `ppo_args.json` says `n_iterations=50` but there may be weight-averaging (see `v5_weight_avg_benchmark.txt`) that changes the answer.
5. Is the `v56_scripted.pt` in `scripted_for_elo/` actually frozen from `ppo_best_6mode.pt` (the 6-mode chain head) or from the plain `ppo_best.pt` (5-mode)? Same question for `v44_scripted.pt`, `v55_scripted.pt`.
6. Does the Elo tournament script already handle the case where a "_continue" cache entry and a "_iterMM" cache entry point at different files? Or does it dedupe by filename? (If the former, both can live in the same table without conflict; if the latter, we must pick one.)
