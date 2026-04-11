# PPO Next Steps — Beyond Heuristic

**Date**: 2026-04-07
**Current state**: PPO v1 at iter 168/200, 82.4% combined vs Nash-temp heuristic (USSR=90.6%, US=74.2%).

---

## What PPO v1 Achieved

PPO warm-started from BC checkpoint v106 (GNN, 34.9% combined) and trained against
the Nash-temperature MinimalHybrid heuristic for 200 iterations (200 games/iter, both sides).

| Milestone | USSR WR | US WR | Combined | Method |
|-----------|---------|-------|----------|--------|
| BC baseline (v106_cf_gnn_s42) | 55.8% | 14.0% | 34.9% | Behavior cloning |
| PPO iter 20 | 66.2% | 13.8% | 40.0% | PPO vs heuristic |
| PPO iter 60 | 81.2% | 21.4% | 51.3% | |
| PPO iter 100 | 85.6% | 50.4% | 68.0% | |
| PPO iter 160 | 90.6% | 74.2% | 82.4% | |
| PPO iter 168 (latest) | ~92% | ~72% | ~82% | Still improving |

**Key wins**:
- US WR jumped from 14% → 74% — PPO solved the US-side problem that BC couldn't
- 23× rollout speedup from C++ batched game pool (560s → 24s per 200 games)
- Stable training: no collapse, monotonic improvement, healthy KL (0.01-0.06)
- Total wall time: ~2 hours for 200 iterations (vs ~31 hours sequential)

**Infrastructure built**:
- `rollout_games_batched()` C++ function with per-step recording
- Python log_prob recomputation (fixes TorchScript trace branch-freezing)
- Rolling checkpoints with milestone preservation
- Per-side rollout WR tracking in W&B

---

## The Ceiling Problem

PPO vs fixed heuristic has a natural ceiling: once the policy exploits heuristic weaknesses,
further training converges but stops generalizing. At 82%+ combined, the policy is likely
overfitting to heuristic patterns rather than learning general TS strategy.

Evidence:
- Rollout WR already 81.5% at iter 168 — the policy wins most games already
- Reward signal becomes sparse (mostly +1.0) — little gradient information
- The heuristic always plays the same mixed strategy — no adversarial pressure

---

## Priority Ranking of Next Steps

### 1. Self-Play PPO (highest impact, highest risk)

**What**: Train PPO against itself instead of the fixed heuristic. Both sides learn
simultaneously, creating an ever-improving opponent.

**Why**: The only way to improve beyond heuristic exploitation. Every successful RL game
AI (AlphaGo, OpenAI Five, etc.) used self-play as the primary training signal.

**How**:
- Use current PPO checkpoint as both players
- Each iteration: play N games (current model vs current model)
- Collect rollout from both sides simultaneously
- PPO update on all steps
- Periodically benchmark via cross-checkpoint Elo (heuristic WR is a ceiling metric
  at 82%+ — need model-vs-model and model-vs-MCTS to measure real strength gains)

**Risks**:
- **Policy collapse**: Both players converge to a degenerate strategy. Mitigation:
  mix 20-30% heuristic opponent games to anchor behavior.
- **Side asymmetry**: With +2 bid the game is balanced (~50/50 in pro play, ±2pp).
  Self-play WR should converge toward 50/50. If it drifts far from that, the policy
  is degenerate. Already have separate per-side advantage normalization.
- **Reward shaping**: Sparse ±1 terminal reward may be too weak. Consider intermediate
  rewards (VP delta per action round, DEFCON changes, region scoring).

**Implementation**:
- Modify `collect_rollout_batched()` to use model for both sides (currently one side
  is heuristic). This requires `rollout_games_batched` supporting learned-vs-learned.
- The C++ `play_learned_vs_learned` binding already exists (added in recent commit).
- Need a `rollout_learned_vs_learned_batched()` variant that records steps for both sides.

**Estimated effort**: 2-3 days (C++ rollout variant + PPO integration)

### 2. League Training / Population-Based

**What**: Maintain a pool of past checkpoints. Each iteration, randomly sample an opponent
from the pool (with bias toward recent checkpoints).

**Why**: Prevents catastrophic forgetting and rock-paper-scissors cycles in self-play.
Each new policy must beat not just the current best, but a distribution of past selves.

**How**:
- Save checkpoints every N iterations to the league pool
- Sample opponent: 50% latest, 30% random past, 20% heuristic anchor
- Track Elo ratings for all league members

**Dependencies**: Self-play PPO (#1) must work first.

**Estimated effort**: 1-2 days on top of self-play

### 3. Value Target Improvements

**What**: Improve the value signal for PPO.

Current setup: sparse ±1 reward on terminal step, GAE(γ=0.99, λ=0.95).

**Options**:
- **VP-scaled terminal reward**: reward = final_vp / 20 (continuous signal, preserves
  direction). Currently winning by 1VP and winning by 20VP give the same reward.
- **Intermediate rewards**: Small rewards for VP changes, scoring events, or DEFCON
  movement. Risk: reward shaping can create degenerate incentives.
- **Value bootstrapping**: Use V(s') at each step as part of the reward. Already done
  via GAE, but could tune γ (currently 0.99 — very long horizon).

**Lowest-risk option**: VP-scaled terminal reward. Change `reward = ±1.0` to
`reward = clip(final_vp * side_sign / 20, -1, 1)`. Preserves binary win/loss direction
but adds magnitude signal.

**Estimated effort**: 0.5 days

### 4. Entropy Scheduling

**What**: Decrease entropy coefficient over training to shift from exploration to exploitation.

Current: fixed ent_coef=0.01.

**Why**: Early in PPO training, high entropy helps explore diverse strategies. Later,
lower entropy lets the policy commit to its best moves. The current fixed entropy may
be preventing sharpening.

**How**: Linear decay from 0.01 → 0.001 over the training run, or cosine schedule.

**Estimated effort**: 0.5 days

### 5. MCTS-Guided PPO (medium term)

**What**: Use MCTS at rollout time to improve action quality, but train the network
to match MCTS decisions without search.

**How**:
- During rollout, run N simulations of MCTS from each state
- Use MCTS visit counts to select actions (not raw policy)
- Record the MCTS-improved action as the "old" policy for PPO
- The policy loss pushes the network toward MCTS-quality decisions

**Why**: This is essentially "Expert Iteration" (ExIt). The MCTS acts as a teacher
during self-play. Unlike teacher KL (which failed 6 times on BC), this works because:
1. The "teacher" (MCTS) runs on the current model, not a frozen one
2. No conflicting losses — just BC-style imitation of MCTS decisions
3. The value function improves from RL, making MCTS progressively stronger

**Constraint**: MCTS is 4-32× slower than greedy. With batched rollout at 24s/200 games,
adding 100 sims MCTS would increase to ~400s — still 5× faster than the old sequential
Python rollout. Manageable if self-play benefit is large.

**Dependencies**: Self-play PPO (#1). MCTS benefit was confirmed at +8.8pp (2000sim)
over greedy for BC model — likely smaller for the stronger PPO model.

**Estimated effort**: 3-5 days

### 6. Architecture: Allocation Head + DP Decoder (Phase 2c)

**What**: Replace the K=4 mixture-of-softmaxes country head with a budget-aware
marginal allocation head.

**Why**: The current country head can't reason about stacking (3 ops into 1 country),
budget constraints, or allocation tradeoffs. MCTS tree search can't help because
influence is a single collapsed edge. A DP decoder that reasons about per-country
marginal gains could improve influence placement quality directly.

**Status**: Spec was planned but not implemented. Now that PPO is working, the
question is whether PPO + DP head compounds the improvement.

**Risk**: Architecture change may break PPO training (need to retrain from scratch
or carefully fine-tune). The BC results showed K=1 was -7.8pp vs K=4, so changing
the country head is risky.

**Estimated effort**: 3-5 days

### 7. Human Game Data Integration

**What**: Fine-tune or mix human game data into PPO training.

**Status**: 51 games from ITS Convention medalists are available. Small but high-quality.

**Why**: Human expert decisions may provide signal on positions where both heuristic and
self-play are weak (e.g., headline selection, event timing, endgame VP calculations).

**How**: Could use as a BC regularization term (small KL toward human play) or as
additional rollout data with high reward for matching expert moves.

**Priority**: Low — PPO is already far beyond what human-data BC could achieve (82% vs 35%).
Human data is more useful for evaluation (does the PPO policy agree with expert moves?)
than for training.

---

## Recommended Sequence

```
Week 1: Policy statistics collection + diagnostic benchmarks
         (understand what PPO v1 actually learned before building on it)
         Self-play PPO + VP-scaled rewards + entropy scheduling
         (highest expected impact, builds on working infrastructure)

Week 2: League training + cross-checkpoint Elo tracking
         (stabilizes self-play, prevents collapse, real strength metric)

Week 3: MCTS-guided PPO (Expert Iteration)
         (uses the proven +8.8pp MCTS improvement during training)

Week 4: Evaluate allocation head, benchmark report, release candidate
```

---

## Policy Statistics Collection (diagnostic infrastructure)

**What**: During benchmarks, collect per-step policy statistics tagged by game phase,
enabling W&B slice analysis to diagnose exploitation vs real strategy learning.

**Per-step tags**:
- `turn` (1-10)
- `phase`: early (turns 1-3), mid (turns 4-7), late (turns 8-10)
- `side`: ussr / us
- `action_round`: headline, AR1-AR8

**Per-step statistics to collect**:
- `mode_distribution`: % of decisions that are Influence / Coup / Realign / Space / Event
- `country_region`: which region the target country is in (Europe, Asia, ME, Africa, CA, SA)
- `influence_split_pattern`: for influence placements, categorize as concentrated (N,0,0)
  vs spread (1,1,...,1) vs mixed. E.g., 3 ops → (3,0,0) / (2,1,0) / (1,1,1).
  Log the fraction of each pattern.
- `top_country_concentration`: how much probability mass is on the top-1 and top-3 countries
  (measures policy sharpness per position)
- `defcon_at_decision`: current DEFCON level when decision is made
- `vp_at_decision`: current VP when decision is made

**Aggregation for W&B**:
- Log per-iteration histograms/means, sliceable by phase × side
- Example W&B panels:
  - "Mode % by turn (USSR)" — reveals if PPO learned to coup early and influence late
  - "Influence split pattern by phase" — reveals if PPO stacks or spreads
  - "Region targeting by phase" — reveals if PPO abandons regions the heuristic doesn't contest
  - "DEFCON at decision (histogram)" — reveals if PPO plays at DEFCON-2 more often (exploitation signal)

**Why this matters**:
- If PPO's mode distribution matches expert play patterns, the improvement is real
- If PPO learned "always coup at DEFCON-2 on turn 1" or "always target one region",
  that's heuristic exploitation that won't transfer
- Phase-tagged statistics let us diagnose WHICH part of the game is exploited

**Implementation**: Add to the benchmark function, not the training loop (benchmark is
infrequent, can afford the overhead). Log as W&B tables or summary dicts.

**Estimated effort**: 1 day

---

## What NOT to Do (Dead Ends from Experiment Log)

These approaches failed repeatedly and should not be revisited:

1. **Teacher KL distillation** — 6 attempts, all regressed (-4 to -20pp). Incompatible with BC training.
2. **Self-play BC data mixing** — adding learned game data to BC always regresses or is within noise.
3. **Wider models** (h=384) — overfits, -6 to -9pp.
4. **K>1 influence expansion in MCTS** — catastrophic at all sim counts (-20pp).
5. **Side-conditional model** — -4 to -5pp, unnecessary complexity.
6. **Data volume increase** (2x-3x) — no benefit, can hurt with overtraining.
7. **K=1 single-softmax country head** — -7.8pp vs K=4, K=4 mixture is essential.

---

## Key Metrics to Track

| Metric | Current | Target (self-play) | Notes |
|--------|---------|-------------------|-------|
| Combined vs heuristic (Nash) | 82.4% | — | Ceiling metric; not useful for measuring further gains |
| Cross-checkpoint Elo | — | Monotonic increase | Primary strength metric from now on |
| Model vs MCTS-400sim (greedy) | — | Beat MCTS | Proves real strength, not just heuristic exploitation |
| Self-play WR (USSR/US) | — | Converge toward ~50/50 | Bid +2 makes game balanced in pro play |
| Rollout time (200 games) | 24s | <30s with self-play | Don't regress on speed |
| PPO iter time | 34s | <60s with self-play | Budget for both sides recording |
