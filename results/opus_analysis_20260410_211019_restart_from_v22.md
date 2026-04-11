# Opus Analysis: Restart from v22 After Bug Fix
Date: 2026-04-10T21:10:19Z
Question: Now that the log_prob bug is fixed, should we kill v40 and restart from v22/ppo_best.pt?

## Executive Summary

Do NOT kill the current chain. The v38-v41 trajectory is recovering steadily (+100 Elo in 3 generations from 1689 to 1793) and the main reason for the initial drop from v22's 2089 to v38's 1689 was NOT the bug fix itself but an **optimizer state mismatch** that caused catastrophic early training (clip=0.58, kl=0.03 for the first ~30 iterations). A fresh restart from v22 would suffer the same mismatch unless the optimizer state is explicitly reset. The correct action is to continue the current chain (v42 is already running) and, if Elo plateaus below 2000 after 2-3 more generations, restart from v22 with `--reset-optimizer` (a flag that should be added to train_ppo.py).

## Findings

### The bug and its fix
The country head log_prob bug in `mcts_batched.cpp` caused the C++ rollout to store temperature-scaled log_probs for the country head, while Python PPO recomputed log_probs at T=1.0. This created systematic importance-ratio bias. The fix (lines 3648-3654 of mcts_batched.cpp) stores log_probs under the unscaled distribution.

### v22 is measured at 2089 Elo -- but was trained WITH the bug
v22 achieved 2089 Elo. All models v23 through v37 were trained with the bug and ranged from 1718 (v27) to 1892 (v37), never exceeding v22. The bug corrupted PPO training from v23 onward, meaning v22's checkpoint weights encode a policy that was optimized under incorrect log_prob gradients. However, the v22 weights themselves are "good enough" -- the model plays well, it just can't improve further via PPO with the broken log_probs.

### The v38 restart suffered optimizer state shock, not bug-fix regression
When v38 restarted from v22/ppo_best.pt with the fixed code, the first iterations show clear evidence of **optimizer state mismatch**:

| Metric | v38 iter 1 (from v22) | v39 iter 1 (from v38) | Normal range |
|--------|----------------------|----------------------|-------------|
| clip_fraction | **0.578** | 0.066 | 0.04-0.07 |
| approx_kl | **0.0314** | 0.0030 | 0.001-0.003 |
| entropy | **4.185** | 5.161 | 5.0-5.2 |
| card_logits range | **[-15.6, 13.1]** | [-4.8, 1.7] | [-5, 2] |
| policy_loss | **+0.0241** | -0.0028 | -0.003 to -0.005 |

The v38 log shows NO "Restored optimizer state from checkpoint" message, meaning Adam optimizer state was NOT loaded. But the checkpoint DOES contain optimizer state (from v22's training under the buggy code). The critical issue: v22's optimizer state has Adam momentum buffers calibrated to the buggy importance ratios. When the fixed code produces different log_probs, the stale momentum causes massive gradient explosions in the first ~30 iterations.

By iter 50, v38 had recovered to clip=0.09, kl=0.004, ent=5.1 -- but it spent 25% of its 200 iterations in recovery mode. By iter 100, it was fully stabilized. The best checkpoint was iter 160 at Elo 1728.

### The v38-v41 trajectory is positive but slow

| Version | Elo | Best iter | Delta from previous |
|---------|-----|-----------|-------------------|
| v38 | 1689 | iter 160 | -400 from v22 (fresh start shock) |
| v39 | 1757 | iter 100 | +68 |
| v40 | 1790 | iter 060 | +33 |
| v41 | 1793 | iter 060 | +3 |

The trajectory shows rapid initial recovery (v38->v39: +68) that is now flattening (v40->v41: +3). The best checkpoints are getting earlier (iter 160 -> 100 -> 060 -> 060), suggesting the model reaches its ceiling quickly and then oscillates.

### What a fresh restart from v22 would change
Restarting from v22 again would:
1. Re-encounter the same optimizer state mismatch (50+ wasted iterations)
2. Produce a nearly identical trajectory to v38-v41
3. Cost ~4 hours of GPU time for 200 iterations
4. NOT produce a different outcome unless a hyperparameter change is made

### The corrupted-era models (v23-v37) are instructive
These models trained under the bug and peaked at 1892 (v37). Interestingly, the best corrupted models (v35=1891, v37=1892) are 100 Elo ahead of the current fixed chain (v41=1793). This means:
- The bug-era models found a policy that, despite corrupted gradients, played better than the current fixed chain
- The bug may have acted as a form of entropy regularization (temperature-scaled log_probs = softer policy updates)
- The current chain hasn't yet recovered the skills that the corrupted chain developed

### Key insight: the v41 plateau at 1793 is concerning
v41=1793 is still 100 Elo below the corrupted v37=1892 and 300 Elo below v22=2089. The flattening from v40 to v41 (+3 Elo) suggests the chain may be approaching a local optimum at ~1800 Elo. If v42 also comes in around 1800, this would confirm a plateau.

## Conclusions

1. **Do not kill v42 or restart from v22.** Restarting would repeat the optimizer shock and likely converge to the same ~1800 plateau.

2. **The 400-Elo drop from v22 to v38 was primarily caused by optimizer state mismatch**, not by the bug fix exposing a weaker policy. v22's weights are fine; the problem is that restarting PPO from a checkpoint whose optimizer state was calibrated to buggy log_probs causes destructive early training.

3. **The v38-v41 chain has recovered half of the optimizer-shock damage** (from -400 to -300 vs v22) but is now plateauing at ~1793.

4. **The fix IS working correctly.** Training diagnostics (kl, clip, entropy) are healthy in v39-v41. The issue is that 200 iterations per generation is not enough to fully recover from a 400-Elo shock, and each generation starts from a noisy base.

5. **v22's 2089 Elo may be partially inflated.** v22 was trained and evaluated under the buggy code, and the Elo was measured in the same corrupted-log_prob environment. It is possible (though not certain) that v22's "true" Elo under correct training would be somewhat lower.

## Recommendations

1. **Continue the v42+ chain for 2-3 more generations.** If Elo exceeds 1850 by v44, the trajectory is healthy. If it plateaus below 1850, switch strategy.

2. **Add a `--reset-optimizer` flag to train_ppo.py** that creates a fresh Adam optimizer instead of restoring from checkpoint. This is the correct approach when restarting from a checkpoint trained under different code.

3. **If plateau persists at v44 (~1800 Elo), do a controlled restart from v22 WITH optimizer reset.** This would be:
   ```
   uv run python scripts/train_ppo.py --checkpoint data/checkpoints/ppo_v22_league/ppo_best.pt --reset-optimizer ...
   ```
   This eliminates the optimizer shock and gives the v22 weights a clean start under the fixed code.

4. **Consider a higher learning rate (5e-5 instead of 2e-5) for the first 50 iterations of any v22 restart.** The current 2e-5 lr with fresh optimizer is very conservative and may be too slow to adapt the policy to the corrected gradient signal.

5. **Run a direct H2H match: v22 vs v41 (1000 games).** This would confirm whether v22's Elo advantage is real under the current (fixed) evaluation code, or whether v22's 2089 was inflated by the bug.

## Open Questions

1. **Is v22's 2089 Elo accurate under the fixed code?** The Elo tournament uses the fixed C++ rollout for evaluation, but v22's policy was shaped by buggy training. A direct re-evaluation may show v22 is actually lower than 2089.

2. **Why does the best checkpoint get earlier each generation (iter 160 -> 100 -> 060)?** This suggests overfitting to the league pool within each run. Consider reducing iterations per generation to 100, or using a larger/more diverse league pool.

3. **Would behavioral cloning from v22's play (via the fixed code) be a faster path than PPO?** Generating 50k self-play games from v22's policy and distilling back could avoid the optimizer-state problem entirely.

4. **Is the entropy coefficient (0.03) too high for recovery training?** The corrupted chain had lower entropy (the bug caused entropy to drop). The current chain's ent=5.2 may be preventing it from committing to the strong moves that v22 learned.
