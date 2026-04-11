---
# Opus Analysis: 24h Progress + Highest ROI Path Forward
Date: 2026-04-09 UTC
Question: Analyze progress of last 24 hours and suggest highest ROI path forward towards stronger agent

## Executive Summary

Over the past 24 hours, the autonomous PPO pipeline completed 10 training generations (v13 through v22), advancing the frontier Elo from 2001 (v12) to 2094 (v19). Elo gains per generation have sharply decelerated: from +30-37 Elo in v14-v15 to +6-8 Elo in v17-v19, with v20 actually regressing below v19. The first plateau was logged at v21 (+5 Elo vs pre-3rd). The current hyperparameter configuration (lr=2e-5, clip=0.12, ent=0.03->0.005, league K=4) is approaching its ceiling within the existing GNN architecture and league training setup. The highest ROI next action is implementing Dirichlet noise at the MCTS root plus epsilon-greedy exploration in self-play rollouts, which directly addresses the exploration deficit that is the most likely cause of the deceleration.

## 24h Timeline

| Time (UTC)    | Event | Elo | Delta |
|---------------|-------|-----|-------|
| ~21:00 Apr 8  | v13 finishing, iter 171/200 | ~2007 | +6 vs v12 |
| 07:15 Apr 9   | v14 restart attempts (parallel workers, checkpoint issues) | - | - |
| 07:33          | v14 settled on workers=1, running from iter 35 | - | - |
| 08:16          | v14 finished | 2031 | +24 vs v13 |
| 08:20          | v15 launched from v14 | - | - |
| 09:29          | v15 finished | 2068 | +37 vs v14 |
| 09:33          | v16 launched from v15 | - | - |
| 10:42          | v16 finished | 2074 | +6 vs v15 |
| 10:46          | v17 launched from v16 | - | - |
| 11:54          | v17 finished | 2080 | +6 vs v16 |
| 11:59          | v18 launched from v17 | - | - |
| 13:07          | v18 finished | 2088 | +8 vs v17 |
| 13:12          | v19 launched from v18 | - | - |
| 14:20          | v19 finished | 2094 | +6 vs v18 |
| 14:26          | v20 launched from v19 | - | - |
| 15:35          | v20 finished | 2088 | -6 (REGRESSED below v19) |
| 15:41          | v21 launched from v20 | - | - |
| 16:51          | v21 finished; ELO initially missing due to bug | 2092 | +4 vs v20 |
| 17:30          | v21 ELO retroactively confirmed; PLATEAU_YES (consecutive=1) | - | - |
| 17:30          | v22 launched (recovery after crash from missing scripted file) | - | - |
| 18:21          | v22 running, iter 146/200 | - | - |
| ~19:00         | v22 at iter ~174/200, ~10 min remaining | - | - |

**Bugs encountered and fixed:**
1. v14: 3 restart attempts (parallel workers doubled iter time; wrong checkpoint format; optimizer state)
2. v21: Hardcoded model list in ELO script missed v21; fixed to dynamic discovery
3. v22: First launch crashed due to missing v21_scripted.pt; auto-copy added

## ELO Trajectory Analysis

### Per-Generation Elo (from full ladder)

| Version | Elo   | Delta vs Previous | Delta vs v12 (anchor) |
|---------|-------|-------------------|----------------------|
| v12     | 2001  | (anchor)          | 0                    |
| v13     | 2016  | +15               | +15                  |
| v14     | 2029  | +13               | +28                  |
| v15     | 2067  | +38               | +66                  |
| v16     | 2071  | +4                | +70                  |
| v17     | 2078  | +7                | +77                  |
| v18     | 2087  | +9                | +86                  |
| v19     | 2094  | +7                | +93                  |
| v20     | 2088  | -6 (regression)   | +87                  |
| v21     | 2092  | +4                | +91                  |

### Trend Assessment

**Phase 1 (v12-v15): Strong gains**, averaging +22 Elo/generation. This was the "low-hanging fruit" phase where league training with good hyperparams (lr=2e-5, clip=0.12, max-kl=0.3) drove rapid improvement from the v12 base.

**Phase 2 (v16-v19): Rapid deceleration**, averaging +7 Elo/generation. Gains are still positive but diminishing. The policy is saturating within its current representational capacity and exploration regime.

**Phase 3 (v20-v21): Plateau/regression**, with v20 actually dropping below v19 and v21 barely recovering. The 95% CI ranges on recent models overlap heavily (e.g., v19 CI=[2085,2103], v21 CI=[2083,2101]). These models are statistically indistinguishable.

**The pipeline has entered a plateau.** The formal plateau counter is at 1, but the effective plateau started at v16 (3 of the last 6 runs gained less than 10 Elo).

## Bottleneck Assessment

### 1. Exploration deficit (PRIMARY BOTTLENECK)
The current league training uses K=4 past opponents from the same lineage plus 3 scripted fixtures (v4, v8, v12). All recent models (v14-v21) are very similar to each other (within ~30 Elo). The model is playing against near-copies of itself with no mechanism to discover novel strategies. Entropy is at 4.0-4.2 (healthy but not diverse enough for exploration). There is no Dirichlet noise, no epsilon-greedy, no temperature-based sampling in rollouts.

### 2. Self-play quality ceiling
The league-mix-k=4 system samples opponents from the recent lineage, but all opponents in the v14-v21 range play nearly identically. The 3 scripted fixtures (v4, v8, v12) are all significantly weaker (50-90 Elo below frontier). The model is not being challenged by genuinely different playstyles.

### 3. Architecture capacity (SECONDARY)
The GNN architecture with hidden_dim=256 may be approaching its capacity limit, but this is less likely the primary bottleneck given that the plateau emerged over just ~5 generations without signs of underfitting (vl=0.09-0.10 is reasonable).

### 4. Hyperparameters (UNLIKELY BOTTLENECK)
lr=2e-5 is conservative and KL stays at 0.002 (well under max=0.3). The policy updates are small and stable. Larger LR or more aggressive updates would risk instability without addressing the root exploration issue.

### 5. US-side weakness
Rollout WRs show persistent US weakness: ussr=0.63-0.74, us=0.33-0.51. The US side is the harder side in Twilight Struggle, and the current model has a significant gap. Targeted improvement on US play could unlock Elo gains, but this is downstream of better exploration.

## ROI Analysis: Options Ranked

### 1. Dirichlet Noise + Exploration Noise in Self-Play (HIGHEST ROI)
- **Effort:** 4-8 hours implementation
- **Expected Elo impact:** +30-80 Elo over next 5 generations
- **Confidence:** High
- **Rationale:** This is the #1 CLAUDE.md Month-3 priority for good reason. AlphaZero's Dirichlet noise (alpha=0.3, epsilon=0.25 at root) plus temperature=1.0 for first N moves is the standard solution to the exact problem we're seeing: policy collapse in self-play from insufficient exploration. The current pipeline has zero exploration mechanisms beyond the entropy bonus.
- **Implementation:** Add `--dirichlet-alpha 0.3 --dirichlet-eps 0.25 --temp-moves 30 --temp 1.0` to train_ppo.py rollout collection. Apply Dirichlet noise to the root policy distribution before action selection. Apply temperature scaling to logits for the first N action rounds of each game.

### 2. Stronger/More Diverse League Fixtures (MEDIUM ROI, LOW EFFORT)
- **Effort:** 1-2 hours
- **Expected Elo impact:** +10-20 Elo
- **Confidence:** Medium
- **Rationale:** Replace the v4/v8/v12 fixtures with v12/v16/v19 (or auto-update fixtures to span the recent Elo range more evenly). Add the heuristic as an explicit fixture. More diverse opponents = more diverse training signal.
- **Implementation:** Update `--league-fixtures` in ppo_loop_step.sh to auto-select fixtures spanning the Elo range. Add fixture refresh rule: when frontier exceeds nearest fixture by 50+ Elo, promote a newer model.

### 3. Early Architecture Sweep (MEDIUM ROI, MEDIUM EFFORT)
- **Effort:** 4-6 hours
- **Expected Elo impact:** +10-30 Elo
- **Confidence:** Medium-Low
- **Rationale:** The plateau rule says 3 consecutive plateaus trigger a sweep. We're at 1 formally, but effectively at the plateau. A quick sweep of hidden_dim=384 or num_strategies=8 could help, but architectural changes without fixing exploration will likely just shift the ceiling slightly.
- **Implementation:** Per CLAUDE.md: try `--hidden-dim 384` or `--num-strategies 8` in one PPO run, compare Elo. No new code needed.

### 4. ISMCTS for Online Play (HIGH IMPACT, HIGH EFFORT)
- **Effort:** 20-40 hours implementation
- **Expected Elo impact:** +100-200 Elo at play time (not training Elo)
- **Confidence:** High at play time, but does not improve training strength
- **Rationale:** ISMCTS with the learned policy as a prior would be the biggest strength lever for actual play. However, it does not improve the training pipeline Elo. It should be implemented, but after exploration noise unlocks further training-time gains.

### 5. Larger Games-Per-Iter / Longer Runs (LOW ROI)
- **Effort:** 0 (config change)
- **Expected Elo impact:** +5-10 Elo
- **Confidence:** Low
- **Rationale:** 200 games/iter with 200 iterations = 40K games per generation. Doubling to 400 games/iter might reduce variance but won't address the fundamental exploration problem.

### 6. Learning Rate / Hyperparameter Tuning (LOW ROI)
- **Effort:** 2-4 hours
- **Expected Elo impact:** +5-15 Elo
- **Confidence:** Low
- **Rationale:** KL=0.002 suggests updates are already very conservative. The model is learning what it can from the data it sees; the problem is the data, not the learning rate.

## Conclusions

1. **The PPO pipeline achieved remarkable throughput:** 10 generations (v13-v22) in 24 hours, fully autonomous with self-healing bug fixes. This infrastructure investment has paid off.

2. **Elo frontier advanced from 2001 to 2094 (+93 Elo in 24h)**, but 80% of that gain came in the first 3 generations (v13-v15). The last 6 generations (v16-v21) gained only 20 Elo collectively.

3. **The system has hit a clear exploration ceiling.** Models v18-v21 are statistically indistinguishable (all within 2087-2094, overlapping 95% CIs). Continuing the current loop without changes will produce more plateaus.

4. **The formal plateau counter (1) understates the problem** because the "3rd-place comparison" metric is lagging. In reality, per-generation gains have been sub-10 Elo for 6 consecutive runs.

5. **Exploration noise is the single highest-ROI intervention.** It directly addresses the root cause (insufficient exploration in self-play rollouts) and is the #1 CLAUDE.md Month-3 priority.

6. **Architecture changes and ISMCTS are valuable but secondary.** They should follow exploration noise, not precede it.

7. **US-side play remains the weakest link** (30-50% rollout WR vs 60-74% USSR). Any intervention that improves US play disproportionately will yield Elo gains.

## Recommendations

1. **Implement Dirichlet noise + temperature-based sampling in self-play rollouts NOW.** This is the single highest-ROI action. Add to train_ppo.py: Dirichlet(alpha=0.3) mixed with policy at root (eps=0.25), and temperature=1.0 for the first 30 action rounds. Let v22 finish, then launch v23 with these changes.

2. **Update league fixtures in ppo_loop_step.sh.** The current fixtures (v4, v8, v12) are 50-90 Elo below frontier. Replace with v8, v14, v19 (or better: auto-select to span the Elo range). This is a 15-minute change.

3. **After 2-3 generations with exploration noise:** if gains resume, continue the loop. If gains plateau again, trigger the architecture sweep (hidden_dim=384 or num_strategies=8).

4. **Do NOT wait for 3 formal plateaus to act.** The effective plateau started at v16. The exploration deficit is clear from the data. Treat the exploration noise implementation as urgent.

5. **After exploration noise is proven:** begin ISMCTS implementation for online play. This is the biggest play-time strength lever and the #4 CLAUDE.md Month-3 priority.

6. **Consider a US-specific training focus.** The model's USSR play (60-74% rollout WR) is significantly stronger than US play (33-51%). If exploration noise helps but US play lags, consider asymmetric training (more US games, US-specific reward shaping).

## Open Questions

1. **What is the right Dirichlet alpha for Twilight Struggle?** AlphaZero used 0.3 for chess, 0.03 for Go. TS has a branching factor between the two (~50-200 legal actions at many decision points). Starting with alpha=0.15 and epsilon=0.25 may be more appropriate. Should be configurable and tested.

2. **Is v22 going to break the plateau or confirm it?** v22 is at iter 174/200 as of this analysis. Based on rollout WR (~0.50-0.56), it is unlikely to exceed v19's 2094 by a significant margin. This reinforces the urgency of exploration noise.

3. **Should the architecture sweep use the Attention model?** Phase 4 showed Attn marginally outperformed GNN in supervised eval, but was much slower and GNN PPO continued to improve. The GNN with wider hidden_dim is the safer sweep candidate.

4. **Is the league K=4 sampling too narrow?** With recent models all within 20 Elo, K=4 past checkpoints from the same lineage provides minimal diversity. Even before Dirichlet noise, increasing K to 8 or adding older models as fixtures could help.

5. **What is the heuristic WR ceiling?** Memory states it is 83%, but v6 reached 89.3% combined WR. Clarifying this ceiling would help calibrate expectations for rollout WR monitoring.
---
