# Opus Analysis: v24-v26 Regression Root Cause
Date: 2026-04-10
Question: Root cause and explain the v24-v26 regression post v23 fix

## Executive Summary

The v24-v26 regression (2096 -> 1757/1820/~1820 Elo) has a single root cause: the C++ log_prob temperature mismatch bug (commit 41564d4) was correctly diagnosed and committed to source, but **the C++ bindings were never rebuilt before launching v24, v25, or v26**. All three runs used the old, buggy binary with `--rollout-temp 1.2`, causing systematic importance-ratio corruption that pushed entropy from v22's healthy 4.0-4.2 to a near-uniform 5.1-5.2 and compressed card logits from [-17, +12] to [-5, +2]. The v24 run from v22 repeated v23's exact collapse pattern, and v25/v26 inherited the damaged weights. Two secondary bugs (ppo_best.pt overwrite, stale league pool files) were also fixed too late to help, but the temperature bug alone is sufficient to explain the full ~340 Elo drop.

## Findings

### Timeline of events (all times UTC)

| Time | Event |
|------|-------|
| 2026-04-09 ~11:48 | v23 launched from v22 ppo_final.pt. First run with `--rollout-temp 1.2` (code change at 18:39:58Z). |
| 2026-04-09 ~19:53 | v23 finished. Elo=1733, massive collapse. Clip=0.61, entropy 3.99->5.2, logits compressed. |
| 2026-04-09 22:12 | log_prob temperature fix committed (41564d4). Modifies `cpp/tscore/mcts_batched.cpp`. |
| 2026-04-09 22:18 | v24 launched from v23 ppo_final.pt via ppo_loop_step.sh. C++ NOT rebuilt. |
| 2026-04-09 22:25 | v24 crashes (no ppo_final.pt). |
| 2026-04-09 22:26 | v24 relaunched from **v22** ppo_final.pt (skip v23 regression). PFSP+Dirichlet enabled. C++ STILL not rebuilt. |
| 2026-04-09 23:23 | v24 finishes. Elo=1757. Same entropy collapse pattern as v23. |
| 2026-04-09 23:28 | v25 launched from v24 ppo_final.pt. C++ STILL not rebuilt. |
| 2026-04-10 00:23 | v25 finishes. Elo=1820 (slight recovery from v24 baseline, but still ~270 below v22). |
| 2026-04-10 00:28 | v26 launched from v25 ppo_final.pt. C++ STILL not rebuilt. |
| 2026-04-10 01:12 | ppo_best.pt overwrite fix committed (9d228e7). |
| 2026-04-10 01:22 | Stale league pool guard committed (868125b). |
| 2026-04-10 01:43 | v26 finishes. Decision made to restart v27 from v22 with clean lineage. |

### Bug inventory (what existed when)

**Bug 1: C++ log_prob temperature mismatch (PRIMARY CAUSE)**
- Nature: When `--rollout-temp T` != 1.0, C++ stored `log_prob(logits/T)` but Python PPO recomputed `log_prob(logits/1.0)`. The importance ratio `exp(log_pi_new - log_pi_old)` was systematically wrong, creating gradient signals that pushed the policy toward maximum entropy (uniform distribution).
- Introduced: When `--rollout-temp 1.2` was first used (v23 onwards, code change logged at 18:39:58Z before v22 finished).
- Fixed in source: commit 41564d4 (2026-04-09 22:12 UTC).
- Fixed in practice: **NEVER** during v23-v26. The fix modifies `cpp/tscore/mcts_batched.cpp` which requires `cmake --build build` to take effect. No rebuild was performed. Evidence: all v24/v25/v26 logs show `"dir noise not supported by bindings"`, confirming the old binary was used.
- Impact: Complete policy collapse. Entropy inflates from 4.0 to 5.2 within 50 iterations. Card logits compress from [-17, +12] to [-5, +2]. Clip ratio spikes to 0.57+ at first iteration (instead of normal 0.07-0.11). The model becomes near-random.

**Bug 2: ppo_best.pt overwrite at run end**
- Nature: `shutil.copy2(final, best_ckpt)` unconditionally overwrote peak checkpoint with end-of-run weights.
- Fixed: commit 9d228e7 (2026-04-10 01:12 UTC).
- Impact on v24-v26: v24 and v25 ran without this fix. However, this is a secondary issue -- the peak v24 checkpoint (v24peak=1809 Elo) was still ~287 Elo below v22, so even the "best" v24 checkpoint was severely damaged by Bug 1.

**Bug 3: Stale league pool iter files**
- Nature: When v24 was restarted from v22, the v24 league directory still contained `iter_0010`, `iter_0020` etc. from earlier failed v24 runs (from v23 lineage). These stale checkpoints were from a collapsed policy.
- Fixed: commit 868125b (2026-04-10 01:22 UTC).
- Impact on v24: Moderate amplifier. At iter 1, v24 sampled stale `iter_0010` as a league opponent, contributing to the initial clip spike. However, Bug 1 alone is sufficient to cause the collapse even with a clean league pool (as v23 proved with a clean pool).

**Bug 4: UnboundLocalError in best_combined tracking**
- Nature: `best_combined` was referenced before assignment when H2H eval ran.
- Fixed: commit ad3e220 (2026-04-09 22:08 UTC).
- Impact: Caused an early v24 restart to crash at iter 20. Fixed before the final v24 run.

### v24 analysis

The v24 log contains 4 separate run attempts:
1. From v23 ppo_final.pt (first attempt, crashed at iter 20 due to Bug 4)
2. From v23 ppo_final.pt (second attempt, similar issues)
3. From v23 ppo_final.pt (third attempt with league improvements, short)
4. **From v22 ppo_final.pt** (final successful run, 200 iterations)

The final v24 run shows:
- **Iter 1**: clip=0.573, entropy=4.073, KL=0.0307, card_logits=[-17.78, +11.42]. The clip ratio 0.573 far exceeds the 0.12 clipping threshold, indicating massive off-policy mismatch. This is the temperature bug: C++ stored log_probs under T=1.2 distribution, Python recomputes under T=1.0.
- **Iter 10**: clip=0.380, entropy=4.636. Logits already compressing.
- **Iter 50**: clip=0.110, entropy=5.149. Logits fully compressed to [-5, +2].
- **Iter 100**: clip=0.064, entropy=5.009. Policy is near-uniform and stable in its damaged state.
- **Iter 200**: clip=0.068, entropy=5.154. Final H2H vs v22: 49.5% (near-random).

v24 Elo: 1757 (USSR=1798, US=1679, gap=+119). The USSR/US asymmetry (+119 Elo) contrasts sharply with v22's symmetric gap (-4). This likely reflects that the near-uniform policy accidentally retains some USSR-favorable tendencies from the starting weights while losing the learned US-specific patterns.

### v25 analysis

v25 inherited v24's damaged weights:
- **Iter 1**: clip=0.069, entropy=5.135, card_logits=[-4.26, +1.79]. The policy starts already collapsed. Low clip ratio because both old and new policies are near-uniform (both computed from the same compressed logits).
- Training shows marginal improvement (H2H peak 56.5% vs v24 at iter ~60-80) then regression.
- **Iter 200**: entropy=5.101, H2H vs v24: 45.5%.

v25 Elo: 1820 (USSR=1915, US=1682, gap=+233). Slightly higher than v24 (+63 Elo), possibly from 200 more iterations of PPO on the damaged base. But the gap widened further, suggesting the PPO signal from bug-free Python updates is slowly learning USSR patterns but unable to recover the lost US capability.

### v26 current state

v26 shows identical damage pattern:
- **Iter 1**: entropy=5.099, card_logits=[-4.58, +1.98]. "dir noise not supported by bindings" confirms old binary.
- **Iter 200**: entropy=5.153, H2H vs v25: 46.0% (USSR=0.580, US=0.340).
- Rollout times nearly doubled (24-32s vs 14-18s in v24), suggesting the near-uniform policy generates longer games.

v26 did NOT recover. The entropy is still at 5.15, card logits still compressed. The temperature bug continued to corrupt importance ratios throughout the entire run.

### Remaining risks

1. **Binary rebuild not verified**: The v27 restart from v22 will only work if `cmake --build build` is run FIRST to compile the fixed `mcts_batched.cpp`. Without this, v27 will repeat the exact same collapse.
2. **Dirichlet noise bindings**: All v24-v26 logs show "dir noise not supported by bindings", meaning the `--dir-alpha 0.3 --dir-epsilon 0.25` flags in ppo_loop_step.sh have been silently ignored for all runs. This feature requires a binding rebuild too.
3. **UPGO**: The plateau_count file should be 0 (all runs got PLATEAU_SKIP). If UPGO was enabled from plateau tracking of previous runs, it was not a factor here. Verify.
4. **ppo_best.pt integrity**: After the fix (9d228e7), ppo_loop_step.sh prefers ppo_best.pt. But if v22's original ppo_best.pt was overwritten by Bug 2 during the v22 run itself, the checkpoint used for v27 might be v22's final weights rather than peak. Check file modification timestamp.

## Conclusions

1. **The entire v24-v26 regression is caused by a single unresolved bug**: the C++ log_prob temperature mismatch fix (commit 41564d4) was never compiled into the binary. All three runs used the old, buggy `.so` with `--rollout-temp 1.2`, causing the same policy collapse as v23.

2. **The fix was correctly diagnosed but the deployment was incomplete**: the commit message and autonomous_decisions.log both describe the root cause accurately, but nobody ran `cmake --build build` to actually apply the fix to the running binary.

3. **The entropy/logits signature is diagnostic**: v22 healthy entropy is 4.0-4.2 with card_logits in [-17, +12]. All v23-v26 runs show entropy 5.0-5.2 and card_logits in [-5, +2]. This is the hallmark of importance-ratio corruption pushing toward maximum entropy.

4. **The three secondary bugs (ppo_best overwrite, stale league pool, UnboundLocalError) contributed but are not root cause**: even with all three fixed, the temperature bug alone would cause the same collapse. The stale league pool amplified the initial shock at v24 iter 1 but did not change the outcome.

5. **The v24-v26 lineage is unrecoverable**: 600 iterations of corrupted PPO training pushed the weights into a near-uniform policy basin. No amount of continued training from v26 can recover the sharp, confident logits that v22 had. The decision to restart v27 from v22 is correct.

6. **The USSR/US asymmetry in v24-v26 (119-233 Elo gap vs v22's -4 gap)** is a secondary effect of the near-uniform collapse: the model retains residual USSR patterns from its initialization but loses the more complex learned US play.

## Recommendations

1. **CRITICAL: Rebuild C++ bindings before launching v27**: `cmake --build build -j`. Verify by checking that `tscore.rollout_model_vs_model_batched` no longer prints "dir noise not supported by bindings".

2. **Add a binary version/hash check to train_ppo.py startup**: Print the hash of the `.so` file and/or a version string compiled into the binary. This prevents silent use of stale binaries after C++ changes.

3. **Add a smoke test to ppo_loop_step.sh**: Before launching the next PPO run, run a 2-game rollout and verify clip ratio < 0.3 and entropy within expected range. If the sanity check fails, abort rather than burning 200 iterations on a doomed run.

4. **Verify v22 ppo_best.pt is not corrupted by Bug 2**: Check if v22's ppo_best.pt was overwritten by ppo_final.pt during the v22 run (before the fix). If so, use the best iter_*.pt checkpoint from v22 instead (e.g., the one with highest H2H WR).

5. **For v27, verify these config elements**: (a) `--rollout-temp 1.2` works correctly with rebuilt binary, (b) Dirichlet noise is actually applied (no "not supported" warning), (c) entropy at iter 1 stays in the 4.0-4.3 range, (d) clip ratio at iter 1 is < 0.15.

6. **Consider a 10-iteration canary run before committing to 200 iterations**: Launch v27 for 10 iterations, verify healthy metrics (entropy 4.0-4.3, clip < 0.15, card_logits range > 10), then extend to 200.

## Open Questions

1. Was the C++ binary ever rebuilt between the fix commit and now? (Check `build/bindings/*.so` modification timestamps vs commit time.)
2. Is v22's ppo_best.pt the actual peak checkpoint, or was it overwritten by Bug 2 during the v22 run? (The v22 run finished BEFORE Bug 2 was fixed.)
3. Would `--rollout-temp 1.0` (disabling temperature) be a safer fallback while the fix is verified?
4. The decision to enable `--rollout-temp 1.2` and Dirichlet noise was made at 18:39:58Z "for v23 onwards". Was this feature adequately tested before deployment?
5. Should v27 use exactly v22's config (no rollout-temp, no Dirichlet) first to verify recovery, then add exploration features in v28?
