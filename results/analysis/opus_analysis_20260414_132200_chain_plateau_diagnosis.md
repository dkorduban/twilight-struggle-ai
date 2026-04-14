---
# Opus Analysis: 6-Mode Chain Plateau Diagnosis
Date: 2026-04-14 UTC
Question: Why can't the 6-mode PPO chain exceed the v217_sc restart anchor (1837 Elo)?

## Executive Summary

The restart chain (v222_sc, v232_sc) cannot exceed v217_sc(1837) because the "fix" applied to the training config -- switching from ent=0.01->0.003 decay to flat ent=0.003 -- actually **removed the exploration phase** that was critical to the peak era's success. The peak era (v205-v209, reaching 1875) used a 0.01->0.003 entropy decay over 30 iters per run PLUS optimizer reset, giving each run ~10-15 iters of high-entropy exploration before exploitation. The current chain starts at flat 0.003 (pure exploitation from iter 1) and preserves stale Adam state, trapping the policy in a local optimum near its initialization. Additionally, the 220-Elo gap between 5-mode (2097) and 6-mode (1875) is largely an artifact of incompatible Elo measurement pools: 5-mode models were measured against a dense round-robin of 30+ similar-era models, while 6-mode models are placed incrementally against 8 opponents spanning different eras.

## Findings

### Finding 1: The entropy "fix" is the primary regression cause

Evidence from training logs:

| Model | ent config | ent_coef curve (wandb) | Outcome |
|-------|-----------|------------------------|---------|
| v205_sc | ent=0.01, decay->0.003 | `███▇▇▇▇▆▆▆▅▅▅▅▄▄▃▃▃▂▂▂▁▁▁` | 1849 Elo |
| v206_sc | ent=0.01, decay->0.003 | same | 1846 |
| v207_sc | ent=0.01, decay->0.003 | same | 1859 |
| v208_sc | ent=0.01, decay->0.003 | same | 1858 |
| v209_sc | ent=0.01, decay->0.003 | same | **1875 (peak)** |
| v232_sc | ent=0.003, flat | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` | 1811 |
| v233_sc | ent=0.003, flat | same | 1793 |

The memory file (`project_ppo_chain_state.md`) incorrectly states "Peak era ent_coef was effectively 0.003 (past decay window)." This is **wrong**. Every peak-era run started at ent=0.01 and decayed to 0.003 over 30 iterations. The ent_coef_final was 0.003, but the ent_coef (initial) was 0.01. The annealing schedule gave each run:

- **Iters 1-10**: ent ~0.01-0.0075 (high exploration, large policy changes tolerated)
- **Iters 11-20**: ent ~0.0075-0.005 (moderate exploration, starting to commit)
- **Iters 21-30**: ent ~0.005-0.003 (exploitation, policy sharpens)

The current chain gets ent=0.003 from iter 1. This immediately penalizes exploration. With low entropy, the PPO loss landscape has sharper optima and the policy cannot escape the basin inherited from v217_sc.

### Finding 2: Optimizer reset complemented entropy annealing

Peak era: every run used `--reset-optimizer` (fresh Adam). This means:
- Fresh momentum estimates (no stale directions from previous run)
- Combined with high initial entropy: the first ~10 iters are genuinely exploratory
- The fresh Adam + high entropy combo allows discovering new strategies each run

Current chain: preserves Adam state (`reset_optimizer=false` for chained runs). This means:
- Momentum carries over from previous run's exploitation phase (low entropy, narrow policy)
- Combined with flat ent=0.003: the model continues in the same narrow gradient direction
- No opportunity for the model to "forget" and re-explore

The peak era's approach was effectively: **warm-restart with annealing** (fresh optimizer + entropy decay), which is known to be effective for escaping local optima in RL. The current approach is **greedy continuation** (stale optimizer + no exploration), which is prone to getting stuck.

### Finding 3: v205_sc had a special advantage -- random EventFirst head

v205_sc loaded from v132_sc (5-mode) and **skipped mode_head weights** because of shape mismatch (5 vs 6 modes):
```
[load_model] skipped incompatible mode_head.weight: torch.Size([5, 256]) vs torch.Size([6, 256])
[load_model] skipped incompatible mode_head.bias: torch.Size([5]) vs torch.Size([6])
```

This means v205_sc's mode_head was **randomly initialized** while trunk/card/country/value weights were strong from v132_sc. This created a regime where:
- The model needed to learn EventFirst mode from scratch
- High initial entropy (0.01) was essential to explore EventFirst policy
- Strong value function guided exploration efficiently
- The random mode_head acted as an implicit "lottery ticket" -- it started from a different region of parameter space than any PPO-continued checkpoint

v217_sc's mode_head is fully PPO-trained and committed. Restarting from v217_sc with low entropy (0.003) means there's no exploration pressure to revise EventFirst decisions, even if they're suboptimal.

### Finding 4: The 5-mode vs 6-mode Elo gap is partly a measurement artifact

5-mode models (v72-v78_sc, 2093-2097 Elo) were measured via **full round-robin** across 30+ models in the same era, with 400 games per match. Their Elo estimates are based on hundreds of match pairs and are well-anchored.

6-mode models (v205-v233_sc, 1793-1875 Elo) are placed via **incremental placement** against only 8 opponents: 5 panel models (v55, v54, v44, v45, v14) + 3 diverse picks. Their Elo estimates are based on ~8 match pairs with 200 games each.

Critical issue: the panel models (v44-v55) are all from the **5-mode era** (Elo 2095-2118). Beating them at 90%+ WR provides very little Elo discrimination. The incremental placement algorithm picks 3 "diverse" opponents from the ladder, but these are dominated by 5-mode models too. A 6-mode model that beats the 5-mode panel at 93% and loses to the heuristic at 50% will get a very different Elo than one measured against a dense pool of same-era peers.

Evidence: v232_sc has panel eval avg_wr=0.931, v233_sc has 0.944, yet v233_sc's Elo (1793) is LOWER than v232_sc (1811). This implies the Elo variation comes from the 3 diverse opponents, not the panel. With only 200 games per diverse opponent, this introduces ~50 Elo of noise.

### Finding 5: PPO-trained weights may genuinely be in a harder-to-escape basin

Even correcting for entropy and measurement, there may be a real local optimum issue. BC-initialized or randomly-perturbed weights have higher effective entropy in weight space. PPO refines weights toward a narrow policy, and the loss landscape around PPO-trained weights has sharper curvature (lower effective learning rate for large policy changes).

This is supported by the pattern in both peak-era and restart-era chains:
- v205_sc(1849): fresh from incompatible checkpoint (random mode_head) -- strong start
- v206-v209: small improvements from annealed exploration -- reaches 1875
- v210-v217: slow decline despite same config -- PPO basin narrows
- v222/v232 restart from v217: cannot improve because starting inside a narrow basin with no exploration mechanism

### Finding 6: The panel eval WR ceiling creates an improvement detection problem

Both v205_sc(panel=0.875) and v232_sc(panel=0.908) are already in the 87-94% range against the panel. At 93%+ WR, the panel cannot distinguish between "1850 Elo" and "1950 Elo" -- the WR difference is within noise for 30-game samples. This means:
- Panel eval cannot detect whether a checkpoint is genuinely stronger
- `ppo_running_best.pt` selection may pick lucky iterations rather than truly better ones
- The candidate tournament (8 top checkpoints, 150 games each) also suffers from this ceiling

## Conclusions

1. **The primary cause is the entropy "fix" (0.003 flat) removing the exploration phase.** The peak era used 0.01->0.003 annealing, giving each run 10-15 iters of exploration. The restart era uses flat 0.003, providing no exploration. This was a misdiagnosis: the conclusion that "peak era effectively ran at 0.003" was wrong -- every peak run started at 0.01.

2. **The secondary cause is optimizer preservation (reset_optimizer=false).** The peak era reset Adam every run, creating a genuine warm-restart effect. The current chain preserves stale Adam state, locking in the previous run's gradient direction.

3. **The peak era's success was specifically due to the combo of fresh random mode_head + high initial entropy + fresh optimizer.** This combination allowed v205_sc to explore EventFirst strategies from scratch while leveraging strong inherited features. Restarting from v217_sc provides no such perturbation.

4. **The 5-mode vs 6-mode Elo gap (~220 Elo) is substantially inflated by measurement differences.** 5-mode models were measured via dense round-robin; 6-mode via sparse incremental placement. The true gap may be 100-150 Elo, not 220.

5. **Panel eval at 90%+ WR provides no discrimination signal.** The panel cannot distinguish 1850 from 1950 Elo, making best-checkpoint selection essentially random within that range.

6. **PPO-trained weights are in a narrow basin.** Without a perturbation mechanism (random head init, high entropy, optimizer reset), small learning rate adjustments cannot escape the local optimum.

## Recommendations

### Immediate (next 1-2 runs): Restore peak-era config

1. **Restore ent=0.01->0.003 annealing** for every 30-iter run. Set `--ent-coef 0.01 --ent-coef-final 0.003 --global-ent-decay-start <prev_total> --global-ent-decay-end <prev_total+30>`. This is what the peak era actually used. The "fix" to 0.003 flat was based on incorrect reasoning and should be reverted.

2. **Restore `--reset-optimizer` for every run**, not just lineage restarts. The peak era reset Adam every 30 iterations. This is the known-good config. Preserving Adam state across runs is an untested "improvement" that coincides with the plateau.

3. **These two changes together** (ent annealing + optimizer reset) should restore the peak-era training dynamics. Expected effect: +30-60 Elo over the current flat-0.003 config within 3-5 runs.

### Short-term (next 5 runs): Fix Elo measurement

4. **Run a dense round-robin for 6-mode _sc models.** Include v205_sc through v233_sc + the top 5 non-sc models (v55, v54, v44, v45, v48) + heuristic. This will produce a true Elo ladder for 6-mode models and reveal the actual gap vs 5-mode.

5. **Add same-era _sc opponents to the panel.** Replace 2-3 of the 5-mode panel models (which are all at 90%+ WR saturation) with _sc models that the current model beats at ~50-70%. This provides better signal for checkpoint selection.

### Medium-term: Consider perturbation strategies

6. **If peak-era config still plateaus at ~1875:** Try BC re-initialization. Train BC on v209_sc self-play games (the strongest 6-mode checkpoint's games), then start PPO from BC weights. This provides the same "fresh weight space" benefit that v205_sc got from the random mode_head.

7. **Consider periodic mode_head perturbation.** Every N runs, add small random noise to the mode_head weights (scale ~0.01-0.05 of current weight norm). This forces the model to re-learn mode selection, which may escape the local optimum.

8. **Population-based training (PBT):** Run 2-3 parallel chains with different entropy schedules (0.01->0.003, 0.015->0.005, 0.01->0.001) and select the best every 5 runs. This is the most principled approach but requires 2-3x compute.

## Open Questions

1. **Was there an ent_coef_final in the peak-era Snakefile config?** The wandb logs confirm decay, but the exact schedule (linear? exponential?) and whether global_ent_decay_start/end were set differently matters. Check git history for the Snakefile.ppo around 2026-04-14 06:42 UTC (v205_sc launch time).

2. **Does the entropy metric (ent=3.8-3.9 for v232 vs 3.9-4.0 for v205) reflect the ent_coef difference?** v205_sc had higher policy entropy (3.92-4.04 in early iters) vs v232_sc (3.71-3.84). This ~0.2 nats difference in policy entropy may be significant for exploration quality.

3. **Is the value function still accurate after many chained runs?** The value loss is comparable (v205: vl=0.28-0.46, v232: vl=0.27-0.34), but if the value function has overfit to the v217_sc era's game distribution, it may provide poor advantage estimates for novel strategies.

4. **What is the true Elo of the best 6-mode model when measured via dense round-robin?** The panel WR of 0.93-0.94 against 2095-2118 Elo opponents, if taken at face value, would imply ~2000+ Elo. The incremental placement may be underestimating.

5. **Would lowering the learning rate (1e-5 instead of 5e-5) help with exploitation near the optimum?** If the policy is near a good solution, smaller steps might allow fine-tuning without overshooting. But this should only be tried AFTER restoring the exploration phase, not as a replacement.
---
