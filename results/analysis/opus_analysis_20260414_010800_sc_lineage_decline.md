# Opus Analysis: SC-Lineage Elo Decline
Date: 2026-04-14T01:08:00Z
Question: Why is the sc-lineage PPO training declining from v132_sc (2092 Elo) to v171_sc (1744 Elo)?

## Executive Summary

The SC-lineage decline has three reinforcing root causes: (1) **fixture saturation** -- the training league opponents are all beaten at 95-97% WR, providing near-zero learning signal and allowing the policy to drift unchecked; (2) **the v132_sc baseline was artificially strong** -- it was a checkpoint override from v77_sc (old-engine SOTA at 2092 Elo) that had not yet adapted to the corrected engine, so its Elo reflected inherited old-engine strength rather than learned sc-engine strength; (3) **no strong calibrating opponents exist in the training loop** -- heuristic is the only opponent providing learning signal (the model only wins ~13.5% against it), but heuristic is a weak anchor (1767 Elo) that cannot teach the model to be stronger than ~1800. The combination means each generation drifts further from the strong v77_sc starting point without any force pulling it back.

## Findings

### 1. The v132_sc Jump Was a Checkpoint Override, Not a Training Breakthrough

v132_sc was created via `results/checkpoint_override_v132_sc.txt` pointing to `data/checkpoints/ppo_v77_sc_league/ppo_best.pt`. The git commit (ee23e84) confirms:

> "v95-v131_sc lineage stuck at 1514-1688 for 40+ iterations after bc_corrected_engine reset proved too weak to recover. v77_sc iter10 reached 2119 (SOTA) and is the strongest checkpoint we've produced."

So v132_sc's 2092 Elo is inherited from v77_sc, an **old-engine** model. The jump from v131_sc (1625) to v132_sc (2092) is not a training result -- it is a manual lineage restart.

### 2. Fixture Saturation: All Training Opponents Beaten at 95%+

The selected_fixtures.json contains 8 opponents:
- v142_sc (1944), v140_sc (1949), v138_sc (1979), v67_sc (2017)
- v20 (2077), v58 (2057), v45 (2096), v55 (2119)

By v165_sc, the WR table shows the model wins **94-97%** against ALL of them:

| Opponent | v135_sc WR | v155_sc WR | v170_sc WR |
|----------|-----------|-----------|-----------|
| v55 | 47.6% | 67.9% | 95.7% |
| v45 | 51.4% | 72.5% | 97.5% |
| v20 | 55.5% | 67.9% | 96.5% |
| v67_sc | -- | 66.3% | 97.0% |
| heuristic | 6.8% | 4.1% | 13.5% |

The PFSP symmetric weight at 97% WR is `4 * 0.97 * 0.03 = 0.116`, nearly zero. The UCB term adds ~0.2, but the total weight is still low compared to heuristic (0.623 weight). This means:
- **Most training signal comes from the heuristic opponent** (weight 0.623 vs 0.3-0.44 for fixtures)
- Fixtures provide almost no gradient signal (the model already wins trivially)
- Self-play iterations provide some signal but drive toward narrow strategies

### 3. Entropy Trend Shows Policy Narrowing Then Rebounding

| Version | Entropy (early) | Entropy (late) | Interpretation |
|---------|----------------|----------------|----------------|
| v132_sc | 4.58 | 4.79 | Healthy: broad policy exploring |
| v140_sc | 4.50 | 4.10 | Narrowing: learning specific strategies |
| v150_sc | 3.69 | 3.54 | Continued narrowing |
| v155_sc | 3.45 | 3.30 | Minimum entropy: highly specialized |
| v165_sc | 3.93 | 4.05 | Rebound: exploring again but not finding improvement |
| v170_sc | 4.27 | 4.18 | High entropy: no clear learning direction |

The entropy U-curve is a classic sign of **policy collapse followed by random exploration**: the model specialized too aggressively (v140-v155), then lost its knowledge base and started exploring aimlessly (v160+).

### 4. Clip Fraction and KL Divergence Escalation

| Version | Clip fraction | KL divergence | Steps/iter |
|---------|--------------|--------------|------------|
| v132_sc | 0.001-0.021 | 0.0001-0.0008 | ~2000 |
| v140_sc | 0.011-0.057 | 0.0005-0.0015 | ~2200 |
| v155_sc | 0.075-0.110 | 0.0025-0.0036 | ~2900 |
| v165_sc | 0.184-0.273 | 0.0062-0.0105 | ~8000 |
| v170_sc | 0.186-0.279 | 0.0067-0.0124 | ~10000 |

Clip fraction jumped from ~2% to ~25% and KL from 0.001 to 0.01. This indicates the PPO updates are **too aggressive** relative to the data distribution. The rising step count (from 2000 to 10000+) is also suspicious -- it suggests games are getting longer, possibly because the model plays poorly and games go to turn 10.

### 5. The Training-Evaluation WR Discrepancy Is Explained by Temperature

Training rollouts use `temperature=1.0` (sampling from the policy distribution).
Elo tournaments use `temperature=0.0` (greedy/argmax play).

At T=1.0, the model samples random actions frequently (entropy ~4.0 nats), which makes it appear to beat weak opponents easily. At T=0.0, the model plays its most-likely actions, exposing learned weaknesses. A model with high entropy under T=0 reveals that it has **no confident correct actions**, leading to poor greedy play even when sampling-based play appears acceptable.

### 6. The Entropy Decay Configuration Is Correct But Irrelevant

The global entropy decay `[PREV_TOTAL_ITERS, PREV_TOTAL_ITERS+30]` correctly gives each 30-iteration run a fresh decay from `ent_coef=0.01` to `0.003`. This is confirmed by training logs showing `ent=0.01` at the start of each run. However, the entropy coefficient is not the binding constraint -- the **model's own policy entropy** (3.3-4.3 nats) dominates the behavior, not the entropy bonus coefficient.

### 7. Panel Used for Best-Checkpoint Selection Changed Mid-Lineage

- v132_sc-v158_sc: Panel = [v55, v54, v44, v45, v14] (old-engine, ~2100 Elo)
  - v132_sc panel WR = 0.517 (appropriate -- ~50% vs peers)
- v159_sc-v161_sc: Panel = [v67_sc, v136_sc, v77_sc, v78_sc, v132_sc] (sc-lineage)
  - v160_sc panel WR = 0.953 (saturated -- 95% means no discrimination)
- v162_sc+: Panel = [v159_sc, v160_sc, v77_sc, v78_sc, v132_sc] (updated sc)
  - v165_sc panel WR = 0.850 (better but still too high for discrimination)

The panel change at v159_sc made the best-checkpoint selector useless -- every iteration looks "best" when winning 95%. This means ppo_best.pt is essentially random among the checkpoints, not selecting the actually strongest one.

### 8. Heuristic Is the Only Real Training Opponent

With all fixtures saturated, heuristic is the only opponent providing meaningful learning signal. But heuristic is rated at 1767 Elo. A model trained primarily against a 1767-Elo opponent cannot exceed ~1800 Elo. This creates a ceiling that explains why the lineage stabilized around 1720-1760 Elo after v155_sc.

## Conclusions

1. **v132_sc's 2092 Elo was inherited from v77_sc via checkpoint override, not earned through SC-lineage training.** The "decline" is really a "regression to the mean" as the inherited old-engine knowledge is gradually overwritten by PPO training against weak opponents.

2. **Fixture saturation is the primary driver of decline.** All 8 league fixtures are beaten at 95%+, providing near-zero gradient signal. The model trains almost exclusively against heuristic (1767 Elo) and self-play iterations, which caps its strength around 1750.

3. **The PFSP mechanism correctly downweights saturated opponents, but this backfires** when ALL opponents are saturated -- the model ends up with no challenging opponents to learn from.

4. **The panel-eval best-checkpoint selector lost discrimination** when the panel was changed from old-engine models (where WR was ~52%) to sc-lineage models (where WR is 85-95%). This means the "best" checkpoint from each run is no better than any other checkpoint.

5. **Rising clip fraction (25%) and KL divergence (0.01) indicate unstable PPO updates.** The max_kl=0.3 threshold is too permissive -- standard PPO uses 0.01-0.03. This allows large policy jumps that degrade previously learned behavior.

6. **The entropy rebound from 3.3 to 4.2 nats indicates the model has lost its learned strategy** and is exploring randomly, which compounds with the lack of strong opponents.

7. **Temperature mismatch (T=1.0 training vs T=0.0 eval) means training WR metrics are misleading.** The 95%+ WR against fixtures during training does not reflect deterministic play strength.

## Recommendations

1. **Immediately add strong opponents to the fixture pool.** The top old-engine models (v55=2119, v54=2102, v46=2100) should be added. Even though the training WR table shows 95%+ against them, the T=0 eval shows they beat the SC model 85%+. The WR table needs to be **reset** for these opponents so PFSP re-evaluates them fairly.

2. **Reset the lineage from v132_sc (or v77_sc ppo_best.pt) again** with the improved fixture pool. The current v170_sc has drifted too far to recover incrementally.

3. **Lower max_kl from 0.3 to 0.03.** The current value allows destructive policy jumps. Standard PPO uses 0.01-0.03 for stable learning.

4. **Restore the old-engine panel for best-checkpoint selection** (v55/v54/v44/v45/v14). These provide much better discrimination (~52% WR) than the sc-lineage panel (~85-95% WR).

5. **Add at least 2-3 opponents in the 1900-2050 Elo range to the fixtures** to create a progressive difficulty ladder instead of the current bimodal distribution (heuristic at 1767 vs everything else at 95%+).

6. **Investigate the training-vs-eval WR discrepancy** by running a manual benchmark at T=1.0 and T=0.0 for the same model pair. If T=1.0 gives 95% but T=0.0 gives 12%, the model has learned a high-entropy policy that works by chance but has no deterministic strategy.

7. **Consider reducing entropy coefficient** from 0.01->0.003 to 0.005->0.001 to encourage the model to commit to strategies rather than maintaining high entropy.

## Open Questions

1. **Why does v77_sc play so much stronger than v170_sc when both are evaluated on the corrected engine?** v77_sc was trained on the old engine but its policies apparently generalize well to the corrected engine. Understanding what makes old-engine policies more robust could inform training.

2. **Is the C++ benchmark_model_vs_model_batched using the correct opponent model loading?** The huge discrepancy between training WR and eval WR warrants verification that both pathways load the same model weights.

3. **Should the training rollouts use a lower temperature (T=0.5)?** This would make training experience more representative of eval conditions while still maintaining some exploration.

4. **Are the old-engine models (v55, v54, etc.) actually stronger, or does the Elo system have a calibration bias** between models trained on different engine versions?

5. **Would freezing the value head for the first few generations after a checkpoint reset** help preserve the inherited policy while allowing the policy head to adapt to the new engine?
