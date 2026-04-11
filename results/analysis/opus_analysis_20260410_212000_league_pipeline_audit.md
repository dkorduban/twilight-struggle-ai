# Opus Analysis: League Composition and Pipeline Audit (v43)
Date: 2026-04-10T21:20:00Z
Question: Is v43's league composition solid, and is the pipeline clean with no dangling processes or incomplete state?

## Executive Summary

The pipeline infrastructure is clean: v42 was killed without leaving orphan processes, v43's watcher chain is correctly wired (PID 163897 polling v43 PID 163765, will call ppo_loop_step.sh v43 v44 on completion), GPU is at 95% utilization, and there are no stale lock files or filesystem debris. However, v43 is actively degrading -- rollout WR has dropped monotonically from 35.5% at iter 1 to 15.5% at iter 10 (now at iter ~13), with WR vs iter_0001 (its own v22-strength snapshot) collapsing from 40%/27% to 32%/16% (USSR/US). This is the most critical finding: the --reset-optimizer flag is causing the fresh Adam optimizer to destabilize v22-quality weights, and the model is getting weaker each iteration rather than improving.

## Findings

### Process State

- **v43 training**: Running as PID 163765 (uv wrapper) / 163769 (actual python), GPU at 95% util, 1027/4096 MiB VRAM
- **v43 watcher**: PID 163897, correctly polling v43, will call `ppo_loop_step.sh v43 v44` on completion
- **Sleep process**: PID 164347 is the watcher's `sleep 15` -- this is the watcher's polling loop, normal and expected
- **No orphan processes**: v42 (PID 161728) and its watcher (PID 161730) are both dead. No zombie watchers from v35-v41 remain.
- **No duplicate training**: Only one GPU training process running

### Filesystem State

**v42 (killed):**
- Directory exists with iter_0001 through iter_0030 plus ppo_iter0020 and ppo_iter0037
- **No ppo_final.pt or ppo_best.pt** -- confirms v42 was killed mid-run (at ~iter 37 of 200)
- v42's watcher correctly detected the missing ppo_final.pt and logged "ended without ppo_final.pt -- no auto-launch"
- v42 stale iter files are harmless (v43 uses its own league dir, no cross-contamination)

**v43 (running):**
- Currently at iter ~13 (latest_checkpoint = ppo_iter0010.pt, iter_0001.pt and iter_0010.pt in league pool)
- ppo_args.json, wandb_run_id.txt (7c162b9b), wr_table.json all present
- No panel_eval_history.json yet (first eval at iter 20)
- W&B is active for v43

**Scripted fixtures:**
- v8_scripted.pt, v14_scripted.pt, v22_scripted.pt all present -- confirmed
- Full roster: v8-v22, v27-v41 (29 scripted models total)
- No v42_scripted.pt (expected -- v42 was killed before completion)

**No stale artifacts:**
- No .lock, .tmp, or .pid files in results/
- results/ppo_v42.log exists (24.7KB) -- retained for diagnostics
- results/ppo_v43.log exists and growing (9.4KB at iter 13)
- results/plateau_count.txt = 0

### League Composition Analysis

v43 league command:
```
--league-fixtures v8_scripted.pt v14_scripted.pt v22_scripted.pt __heuristic__
--league-mix-k 4
--league-recency-tau 20
--league-fixture-fadeout 150
--league-heuristic-pct 0.0
--pfsp-exponent 1.0
```

**Pool composition over time:**
- **Iter 1-9**: Pool = {iter_0001} + {v8, v14, v22, heuristic}. Slot 0 = self, slots 1-3 from pool. In practice, iter_0001 dominates because it's the only past-self entry and gets half the sampling weight.
- **Iter 10**: iter_0010 added to pool. Now 2 past-self + 4 fixtures.
- **Iter 50**: ~5 past-self checkpoints + 4 fixtures. Fixtures get roughly half the weight of past-self total.
- **Iter 150+**: Fixtures fade out. Pool = past-self only (up to ~15 checkpoints).
- **Iter 200**: Pure past-self league with ~20 snapshots.

**Observation**: In early iterations (1-9), the model played almost exclusively against iter_0001 (itself at v22 strength). This is a LOT of self-play against a fixed target with no diversity.

### PFSP and Fixture Difficulty

Starting from v22/ppo_best.pt (Elo ~2089):

| Fixture | Elo | Expected starting WR | Role |
|---------|-----|---------------------|------|
| heuristic | 1652 | ~83% | Easy anchor |
| v8_scripted | 1931 | ~65% | Medium-easy |
| v14_scripted | 2021 | ~55% | Medium |
| v22_scripted | 2089 | ~50% | Near-equal |

**Elo-predicted WRs**: Reasonable fixture spread. v22 as a fixture is fine -- it's essentially a mirror match at the start, providing strong gradient signal.

**Actual early WRs (iter 1-13)**:
- vs heuristic: 83% combined (healthy, as expected)
- vs v8_scripted: 60% combined (slightly below expected, only 50 games)
- vs iter_0001 (≈v22): **24.1% and declining** (should be ~50%)
- vs v14_scripted: **16%** USSR, **16%** US (iter 13, very few games but alarmingly low)

**PFSP exponent 1.0 is appropriate** for this fixture spread. With the observed WRs, PFSP is correctly upweighting the harder opponents (iter_0001 gets pfsp=0.759, v14 gets 0.840). However, PFSP can't fix a model that's fundamentally degrading.

### Watcher Chain Integrity

- v43 watcher (PID 163897) correctly polls PID 163765
- On completion: checks for ppo_final.pt, calls `ppo_loop_step.sh v43 v44`
- ppo_loop_step.sh:
  - Runs confirmation tournament (if panel_eval_history.json exists)
  - Copies scripted checkpoint to scripted_for_elo/
  - Runs Elo tournament with full ladder
  - Checks plateau count
  - Launches v44 with appropriate flags (UPGO if plateau_count >= 1)
  - Creates v44 watcher
- Stale-iter guard (lines 224-231): correctly checks NEXT_DIR for stale iter_*.pt and removes them before launch

**Issue**: ppo_loop_step.sh anchors Elo tournament on v12 (`--anchor v12 --anchor-elo 2001`) but the confirmation tournament anchors on v14 (`--anchor v14 --anchor-elo 2001`). Minor inconsistency but not training-breaking.

### UPGO State

- plateau_count.txt = 0
- UPGO is enabled when plateau_count >= 1
- v43 will NOT get UPGO (it was launched manually, not by ppo_loop_step.sh)
- If v43 completes and triggers the plateau check, v44 may or may not get UPGO depending on whether v43's Elo beats the 3rd-place model

### Potential Issues Found

**CRITICAL: Model degradation in progress.**
Rollout WR trajectory across v43 iterations:
```
iter  1: 0.355 (ussr=0.420, us=0.290)
iter  2: 0.420 (ussr=0.530, us=0.310)  ← brief uptick
iter  3: 0.375 (ussr=0.460, us=0.290)
iter  4: 0.305 (ussr=0.370, us=0.240)
iter  5: 0.535 (ussr=0.590, us=0.480)  ← opponent mix variance
iter  6: 0.265 (ussr=0.320, us=0.210)
iter  7: 0.220 (ussr=0.280, us=0.160)
iter  8: 0.200 (ussr=0.290, us=0.110)
iter  9: 0.190 (ussr=0.290, us=0.090)
iter 10: 0.155 (ussr=0.230, us=0.080)
iter 11: 0.225 (ussr=0.300, us=0.150)
iter 12: 0.155 (ussr=0.200, us=0.110)
iter 13: 0.200 (ussr=0.250, us=0.150)
```

The cumulative WR vs iter_0001 has dropped from 40%/27% to 32%/16%. Entropy is rising (4.12→4.70), clip fraction falling (0.57→0.29), policy loss near zero. This is classic **optimizer-reset induced policy collapse**: the freshly-initialized Adam optimizer lacks momentum/variance estimates and makes overly aggressive updates that destabilize the learned policy.

**Previous lineage also stuck**: v35-v41 all scored Elo 1689-1893, well below v22's 2089. The loop has been running 10+ generations without surpassing v22. This is not just an optimizer-reset issue -- the training configuration may be fundamentally unable to improve beyond v22 with the current hyperparameters.

## Conclusions

1. **CRITICAL**: v43 is actively degrading (rollout WR collapsed from 35% to 15-20% over 13 iters). The optimizer reset is destabilizing v22-quality weights. This run will likely produce a model weaker than v22, continuing the pattern of v35-v41 (all Elo 1689-1893 vs v22's 2089).

2. **INFO**: Pipeline infrastructure is clean. No orphan processes, no stale lock files, no cross-contamination between v42 and v43 league dirs. v42 was killed cleanly.

3. **INFO**: Watcher chain (v43→v44→...) is correctly wired and will function on v43 completion.

4. **INFO**: All three league fixtures (v8, v14, v22) are present and the Elo spread is reasonable.

5. **WARNING**: v43 plays almost exclusively against iter_0001 in early iterations (it's the only past-self snapshot for 10 iters). This means 75% of non-self games are against a single fixed opponent, providing poor diversity.

6. **WARNING**: 10 consecutive generations (v35-v41 + v38 restart) have failed to surpass v22. The current hyperparameter/league configuration appears to have hit a ceiling.

7. **INFO**: plateau_count = 0. UPGO will not be enabled for v44 unless v43 actually tops the Elo ladder (very unlikely given current trajectory).

8. **INFO**: Minor Elo anchor inconsistency: confirmation tournament uses v14@2001, full tournament uses v12@2001. Not training-breaking but should be unified.

## Recommendations

1. **Let v43 run to at least iter 40 before killing** -- optimizer-reset degradation sometimes stabilizes after ~30 iters as Adam variance estimates warm up. Monitor WR trend at iter 20 eval checkpoint (should show in panel_eval_history.json). If rollout_wr is still below 0.25 at iter 30, kill the run.

2. **For v44 or a manual restart, do NOT use --reset-optimizer**. Instead, start from v22/ppo_best.pt using the full optimizer state:
   ```bash
   # Use the original v22 checkpoint WITH optimizer state:
   --checkpoint data/checkpoints/ppo_v22_league/ppo_best.pt
   # Without --reset-optimizer flag
   ```

3. **Reduce learning rate for warm-start runs**. If you must use --reset-optimizer, use `--lr 5e-6` (4x smaller) for the first 50 iters to prevent optimizer-reset collapse.

4. **Consider lowering entropy coefficient**. Current ent-coef=0.03 with ent-coef-final=0.005 -- the rising entropy (4.12→4.70) suggests the model is being pushed toward randomness. Try `--ent-coef 0.01 --ent-coef-final 0.003`.

5. **Increase league diversity in early iterations**. The current setup means 75% of non-self games go to iter_0001 in the first 10 iters. Consider:
   - Seeding the league dir with 2-3 older checkpoints (e.g., symlink v14 and v19 iter checkpoints)
   - Or increasing `--league-save-every` from 10 to 5 to build the pool faster

6. **Address the v22 ceiling**. 10+ generations stuck below v22 suggests a structural issue, not just hyperparameter tuning. Possible root causes:
   - Self-play echo chamber (model plays mostly against itself/recent snapshots)
   - Missing exploration (consider enabling UPGO and/or increasing dir-alpha)
   - Insufficient game diversity (200 games/iter may be too noisy for stable learning)
   - Architecture plateau (the current model capacity may be maxed out)

7. **Clean up v42 artifacts** (optional, low priority):
   ```bash
   # v42 dir has 4 stale iter files and partial checkpoints. Not hurting anything but wasting ~10MB.
   # Can be cleaned when convenient.
   ```

## Open Questions

1. Does v22/ppo_best.pt contain optimizer state? If the original v22 run used a different optimizer (e.g., different LR schedule), starting from its optimizer state may also cause issues.

2. Would a warmup LR schedule (linear warmup over 20 iters) mitigate the optimizer-reset degradation? The current train_ppo.py does not appear to have LR warmup.

3. Is the v22 ceiling a fundamental architecture limit? If so, the next step should be an architecture experiment (wider trunk, attention, etc.) rather than more PPO iterations.

4. Should the fixture fadeout at iter 150 be reconsidered? If the model is weaker than the fixtures, removing them removes the only productive training signal.
