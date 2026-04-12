# Opus Analysis: SC Series Regression
Date: 2026-04-12

## Executive Summary

The SC series (v66_sc through v70_sc, Elo 1891-2016) is stuck 100-220 Elo below the non-SC top (v44-v55, Elo 2095-2119) due to **three compounding root causes**:

1. **Poisoned lineage origin**: v66_sc was trained from v65 using `lr=0.0001, clip=0.2` (5x the learning rate, 1.7x the clip of the working config). This aggressive config likely damaged the model's policy in the first generation, creating a deficit that subsequent conservative runs (lr=2e-05, clip=0.12) cannot recover from.

2. **Entropy collapse**: v44-v55 trained with `ent=0.03`; the SC series uses `ent=0.01->0.003`. The SC models have entropy ~3.4-3.6 vs v44's ~4.0-4.1. Lower entropy means less exploration, which means the model cannot discover better strategies to escape its current local optimum.

3. **No positive-signal opponents**: The SC fixture pool contains only v45/v55 (top-tier, Elo 2098-2119) and self-play iter_* snapshots. The model wins ~47-53% of rollout games -- pure noise around 50%. With no weaker opponents providing clear positive reward signal, PPO has no gradient direction to follow.

The v44-v55 line succeeded because it: (a) started from a clean v22 checkpoint, (b) used 3x higher entropy, (c) trained against its own recent self-play snapshots and heuristic (a beatable opponent), and (d) ran 200 iterations per generation (not 80).

## Root Cause Assessment (with evidence)

### Root Cause 1: Poisoned v66_sc checkpoint (the original sin)

**Evidence:**
- v66_sc log line 7: `Device: cuda, lr=0.0001, clip=0.2, ent=0.01`
- v44 log line 14: `Device: cuda, lr=2e-05, clip=0.12, ent=0.03`
- v66_sc was loaded from `ppo_v65_league/ppo_best.pt`
- v65 was itself experimental: "launching ppo_v65 from v55_best with SmallChoiceHead" (autonomous_decisions.log, 2026-04-11T22:15)
- v65 was never Elo-rated (not in elo_full_ladder.json)
- v64 (a BC warm-start) rated at Elo 1642 -- far below the v44-v55 cluster

**Mechanism:** lr=0.0001 is 5x the standard 2e-05. With clip=0.2, each PPO update moves the policy much further. Over 80 iterations, this likely pushed the model into a bad region of policy space. When v67_sc resumed with the conservative config (lr=2e-05), it inherited this damaged starting point and could not recover.

### Root Cause 2: Entropy starvation

**Evidence:**
- v44 iter 1: `ent=4.084`, v44 iter 10: `ent=4.113` (stable ~4.1 throughout)
- v67_sc iter 1: `ent=3.513`, decaying to `3.449` by end
- v68_sc iter 1: `ent=3.420`, decaying further
- v70_sc iter 1: `ent=3.571`, final: `ent=3.80` (but this is AFTER reset-optimizer, so slightly higher)

**Mechanism:** The v44-v55 line ran with ent_coef=0.03, keeping policy entropy at ~4.0-4.1 nats. The SC line uses ent_coef=0.01 decaying to 0.003, resulting in entropy ~3.4-3.6. This is a ~15% reduction in effective policy randomness. In a game with high variance like Twilight Struggle, lower entropy means:
- Fewer exploratory moves during rollouts
- Narrower policy updates
- Faster convergence to local optima
- Inability to discover new strategic patterns

### Root Cause 3: Missing beatable opponents (no positive gradient)

**Evidence from v70_sc panel evals:**
```
iter 10: avg=0.496 — v55=0.533 | v54=0.550 | v44=0.417 | v45=0.433 | v14=0.467
iter 20: avg=0.479 — v55=0.517 | v54=0.500 | v44=0.400 | v45=0.450 | v14=0.517
iter 30: avg=0.527 — v55=0.483 | v54=0.550 | v44=0.583 | v45=0.533 | v14=0.467
iter 40: avg=0.487 — v55=0.467 | v54=0.467 | v44=0.500 | v45=0.550 | v14=0.500
iter 50: avg=0.488 — v55=0.517 | v54=0.450 | v44=0.500 | v45=0.500 | v14=0.383
iter 60: avg=0.471 — v55=0.483 | v54=0.450 | v44=0.483 | v45=0.467 | v14=0.450
iter 70: avg=0.480 — v55=0.533 | v54=0.433 | v44=0.450 | v45=0.483 | v14=0.450
iter 80: HWM=0.527 (iter 30)
```

The model oscillates between 47-53% against every opponent. Even v14 (Elo 2015, the weakest panel member) is not consistently beatable. This is noise, not learning. Compare to v44's rollout WRs where it faced heuristic (Elo 1763) and consistently got 80-90% WR, providing clear positive reward signal.

**Evidence from v67_sc fixture PFSP:**
```
[ussr] v45_scripted: WR_ussr=0.47(n=40) — too strong, no signal
[us] v55_scripted: WR_us=0.28(n=40) pfsp=0.725 — losing badly, PFSP upweights it further
[ussr] iter_0001: WR_ussr=0.72(n=120) — only beatable opponent is self
```

The PFSP algorithm correctly identifies v55 as the hardest opponent and upweights it (pfsp=0.725). But this makes the problem worse: the model spends MORE time losing to v55 as US (28% WR), getting mostly negative reward.

## Why SC Models Cannot Reach v44-v55 Levels

The SC models are trapped in a **mediocrity basin**:

1. They start from a damaged checkpoint (v66_sc, trained with wrong hyperparameters)
2. They have low entropy (can't explore out of the basin)
3. They face only strong opponents (no clear reward gradient pointing uphill)
4. 80 iterations is not enough to escape when the gradient is pure noise
5. Each generation inherits the previous generation's mediocre best checkpoint, so the chain cannot improve

Meanwhile, v44-v55 succeeded because:
- v44 was deliberately reset to v22's clean checkpoint ("v22 exact config: T=1.0, no Dirichlet, no PFSP, --reset-optimizer")
- v44 used ent=0.03 (3x the SC entropy)
- v44-v55 ran 200 iterations per generation (2.5x the SC's 80)
- v44-v55 trained against heuristic + self-play snapshots, getting reliable positive signal from the beatable heuristic

## Specific Recommendations for v71_sc

### 1. Reset the lineage (CRITICAL)

Do NOT continue from v70_sc. The entire v65->v66_sc->...->v70_sc lineage is poisoned. Instead:

**Option A (recommended):** Start v71_sc from `v55_scripted.pt` (the best non-SC model). This is the known-good checkpoint at Elo 2119. Reset optimizer. This immediately gives you a model at the frontier instead of 200 Elo below it.

**Option B:** Start from v44 or v45 if you want to verify the SC pipeline can produce gains from a known-good but slightly weaker starting point.

### 2. Raise entropy coefficient

Change from `ent_coef=0.01 -> 0.003` to `ent_coef=0.03 -> 0.01` (matching the v44-v55 range). This is the single most impactful hyperparameter difference between the successful and unsuccessful lineages.

### 3. Add weaker opponents to the fixture pool

Add at least 2-3 beatable opponents:
- `heuristic` (Elo 1763) — set `--league-heuristic-pct 0.15` instead of 0.0
- `v10_scripted.pt` or `v12_scripted.pt` (Elo ~1850-1900)
- Keep some strong opponents (v55, v44) but ensure the model wins at least 60-70% against the weakest fixture

This gives PPO a reliable positive reward signal. The model learns "what winning looks like" from easy games and transfers that to harder matchups.

### 4. Reduce fixture count or change PFSP exponent

Current: 13 fixtures with pfsp_exponent=2.0. This means the model faces mostly strong opponents (which it can barely beat). Options:
- Reduce to 6-8 fixtures with a mix of weak (2), medium (3), and strong (3)
- Or reduce pfsp_exponent from 2.0 to 1.0 (more uniform fixture sampling instead of overweighting hard opponents)

### 5. Consider longer runs

If you keep 80 iterations: fine for a model that's already near-optimal. But if the model needs to climb 200 Elo, consider 120-160 iterations. v44-v55 used 200.

### Concrete v71_sc launch config

```bash
# Reset lineage to v55 (best known model)
echo "data/checkpoints/scripted_for_elo/v55_scripted.pt" > results/checkpoint_override_v71_sc.txt

# In ppo_loop_step.sh or manual launch, change:
--ent-coef 0.03 --ent-coef-final 0.01     # was 0.01 -> 0.003
--league-heuristic-pct 0.15                # was 0.0
--n-iterations 120                         # was 80 (optional, but helpful)
--pfsp-exponent 1.5                        # was 2.0 (optional, reduces hard-opponent bias)
```

## Longer-Term Recommendations

1. **Track lineage health metrics**: Log starting entropy, starting panel WR, and fixture WR distribution at iter 0 for every new generation. If starting entropy < 3.8 or starting panel WR < 45%, flag as unhealthy.

2. **Automatic lineage reset trigger**: If 3 consecutive SC generations fail to set a panel HWM > 0.52, automatically reset to the best-known non-SC checkpoint.

3. **Entropy floor**: Never let entropy decay below 3.5 nats during SC training. Add `--ent-floor 0.005` or similar mechanism. The v44-v55 line never dropped below 4.0.

4. **Mixed-difficulty fixture curriculum**: Instead of JSD-based fixture selection (which optimizes for diversity), select fixtures to cover an Elo range: 25% easy (Elo 1750-1900), 50% medium (1900-2050), 25% hard (2050-2120). This ensures positive signal at all training stages.

5. **Separate SC experiments from main lineage**: Run SC as a branch experiment, not as the primary pipeline. The main pipeline should continue the v44-v55 lineage (which is working) while SC experiments try to improve upon it.

## Open Questions

1. **Why was v66_sc trained with lr=0.0001?** Was this intentional (SmallChoiceHead warm-up?) or accidental? Understanding the original intent may reveal whether the SC concept itself is flawed or just the execution.

2. **Does SmallChoiceHead require different hyperparameters?** v65 introduced SmallChoiceHead. If this architecture change needs different training dynamics, that should be validated independently before combining with the SC fixture pool changes.

3. **Would v55 + SC fixtures actually improve over v55 + self-play?** We don't know because the SC series never started from v55 with working hyperparameters. The v71_sc experiment (Option A above) will answer this.

4. **Is the candidate tournament biasing checkpoint selection?** The panel consists of 4 strong models (v55/v54/v44/v45) + 1 anchor (v14). If the model overfits to beating v14 at the expense of the strong panel, the HWM checkpoint may not be the true best. Panel WR data shows v14 scores are NOT consistently higher than others, so this is likely not a problem.

5. **Are the Elo measurements for SC models reliable?** The prior analysis (opus_analysis_20260412_regression_chain_v67_v69.md) argued the Elo regression was a measurement artifact. With the full ladder now showing v66_sc=2013, v67_sc=2016, v68_sc=1967, v69_sc=1891, v70_sc=1903 -- the downward trend from v68_sc onward looks real, not an artifact. v67_sc and v66_sc are at v14-anchor level (~2015), which is consistent with their 50/50 panel performance.
