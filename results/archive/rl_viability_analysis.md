# Reinforcement Learning Viability Analysis for Twilight Struggle AI

Date: 2026-04-06

## Executive Summary

RL is **viable and likely the most promising path to break the BC ceiling**, but the
expected gains are moderate (5-15pp over BC greedy) and the implementation cost is
non-trivial. The recommended approach is **PPO with warm-start from the BC policy**,
using game outcome as reward, with the existing C++ engine as the environment. A
minimum viable experiment can run in ~4 hours on current hardware and should show
signal within 50K games.

The strongest alternative remains **MCTS at inference time** (already +8.8pp at 2000sim),
which requires zero training and is complementary to RL. The optimal strategy is likely
RL-trained policy + MCTS at inference = stacking both gains.

---

## 1. Algorithm Family Evaluation

### 1a. Policy Gradient (REINFORCE, PPO, A2C)

**Viability: HIGH -- recommended path**

**Pros:**
- Directly optimizes win rate, which is the actual objective (BC optimizes action
  prediction, which plateaus at ~35% combined)
- Natural fit for factorized action space: log pi(a|s) = log pi_card(c|s) +
  log pi_mode(m|s,c) + log pi_country(t|s,c,m). PG gradient decomposes cleanly
  across heads -- each head receives gradient proportional to the advantage, scaled
  by its own log-probability contribution
- Warm-start from BC policy gives a strong initialization (the BC policy already
  wins 35% of games)
- Recent literature strongly supports this: Rudolph et al. (2025, arxiv 2502.08938)
  found that over 7000 training runs, PPO outperformed all FP/DO/CFR-based deep RL
  methods for imperfect-information games. This is the single most relevant paper for
  our situation
- PPO's clipping mechanism provides stability during fine-tuning, preventing
  catastrophic forgetting of the BC initialization

**Cons:**
- High variance from ~150-step episodes with sparse reward. Mitigation: use the
  existing value head as baseline (already trained on game outcomes), and consider
  intermediate reward shaping (VP delta per turn)
- Sample efficiency: expect 50K-200K games needed (see Section 2)
- Imperfect information: the policy sees only its own hand, not the opponent's.
  Standard PG still works -- it optimizes E[R | policy], marginalizing over hidden
  info. No theoretical issue, but higher variance than perfect-info games

**Factorized action gradient:**
The factorized action pi(a) = pi_card(c) * pi_mode(m|c) * pi_country(t|c,m) means:

    grad log pi(a) = grad log pi_card(c) + grad log pi_mode(m|c) + grad log pi_country(t|c,m)

Each head receives the *same* advantage signal (game outcome minus baseline), weighted
by its own gradient. This is correct and standard -- no special handling needed. The
card head gets gradient to play better cards, the mode head to choose better modes, and
the country head to place influence better. All three improve simultaneously.

One subtlety: the country head only matters for influence/coup/realign modes (not
event/space). For event/space actions, the country gradient is near-zero (targets
are irrelevant). This is naturally handled by masking.

### 1b. Q-Learning (DQN, Dueling DQN)

**Viability: LOW -- not recommended**

**Fundamental problem:** Q(s,a) with a = (card, mode, country) requires enumerating
or sampling the joint action space. With 111 cards x 5 modes x 86 countries = ~47,730
potential actions (before legality masking), this is intractable for standard DQN.

Factorized Q-learning (Q_card + Q_mode + Q_country) loses the interaction between
action components -- the value of playing a card depends on which mode you use it for.
Dueling DQN doesn't help because the issue is action-space size, not value decomposition.

**Off-policy reuse of heuristic data** is appealing in theory, but Q-learning's
overestimation bias is severe in large action spaces with sparse reward. CQL/IQL
(conservative variants) could work but are complex to implement and tune.

**Verdict:** The factorized action space makes Q-learning awkward. PG methods handle
this naturally.

### 1c. Actor-Critic (A2C, PPO)

**Viability: HIGH -- PPO is the specific recommendation**

This is the same as 1a but with emphasis on the critic (value head). We already have:
- A trained value head (MSE loss on final_vp)
- Value predictions in [-1, 1] from USSR perspective

PPO advantage = R - V(s), where V(s) is the value head prediction. The existing value
head provides a strong baseline that reduces variance compared to REINFORCE.

**A2C vs PPO:** PPO is preferred because:
- Clipping prevents large policy updates that could destabilize the warm-started policy
- PPO is more robust to hyperparameter choices (well-documented: 37 implementation
  details paper by Huang et al. 2022)
- PPO naturally handles the on-policy / near-on-policy regime we'll be in

### 1d. AlphaZero-style (MCTS + Policy Improvement)

**Viability: MEDIUM -- good long-term, expensive short-term**

**What we have:**
- Full MCTS infrastructure (batched, pruned, 2000sim = +8.8pp)
- The policy improvement loop is: play games with MCTS -> train policy to match
  MCTS visit distribution -> repeat

**The imperfect-info problem:**
Standard AlphaZero assumes perfect information. For TS, we need determinized MCTS
(PIMC) or ISMCTS. We already have ISMCTS infrastructure. The AlphaZe** paper
(Frontiers in AI, 2023) shows that AlphaZero with determinized MCTS works
"surprisingly well" for imperfect-info games (tested on Stratego).

ReBeL (Noam Brown et al., NeurIPS 2020) is the gold standard: it uses public belief
states + CFR at each decision point + RL for value training. This is theoretically
elegant but far too complex for our setup (requires belief state tracking, CFR solver,
PBS value network).

**The cost problem:**
MCTS at 2000sim takes ~5.2s/game (2600s / 500 games). For an AlphaZero-style loop
needing 100K+ games per iteration, that's ~144 hours per generation. Unacceptable
on our hardware.

MCTS at 400sim takes ~1.5s/game. Still 42 hours per 100K games.

**Verdict:** AlphaZero-style is the theoretically optimal path but too expensive for
our hardware budget. Revisit if/when we get cloud compute or if pruned MCTS at low
sim counts (50-100) shows sufficient quality for policy improvement targets.

However, a **hybrid approach** is viable: train with PPO (cheap, ~0.16s/game), then
use MCTS at inference time for evaluation (expensive but doesn't need to be fast).
The PPO-trained policy becomes a better prior for MCTS, potentially getting more
from fewer simulations.

### 1e. Offline RL (CQL, IQL, Decision Transformer)

**Viability: LOW-MEDIUM -- unlikely to break the ceiling significantly**

**The data:**
We have ~2.7M rows of heuristic game data (BC training set). This is the "behavioral
policy" dataset for offline RL.

**The fundamental limitation:**
Offline RL methods are designed to improve over the data-generating policy without
online interaction. But:
- CQL is conservative by design -- it lower-bounds Q-values for out-of-distribution
  actions. This means it's unlikely to discover novel strategies not in the heuristic data
- IQL avoids evaluating OOD actions entirely. It can generalize within the data
  distribution but won't find radically different play
- Decision Transformer conditions on desired return, but with game-outcome reward,
  it would need to see high-return trajectories. Our heuristic wins ~35% of games
  as each side, so there are winning trajectories, but the model already imitates them
  via BC

**Key insight:** The BC ceiling exists because the heuristic policy is the *source*
of the data. Offline RL on heuristic data is fundamentally limited by the quality of
the heuristic's play. It might squeeze out 1-3pp by better weighting good trajectories,
but it cannot discover strategies the heuristic never plays.

**AWR connection:** We already tried advantage-weighted regression (v96b_aw). Result:
USSR 41.8% / US 5.7% / Combined 23.7%. The advantage weighting hurt US play by
downweighting US-losing games (86% of US games are losses). This is essentially
offline RL and it didn't break the ceiling.

**Verdict:** Offline RL is not the path forward. The data is the bottleneck, not the
loss function. We need online interaction (PPO) to discover strategies beyond the
heuristic's repertoire.

---

## 2. Minimum Viable RL Experiment

### Environment throughput

Greedy NN play: 500 games in 82s = **~6 games/sec** (batched, CPU).
Each game has ~150 decisions. That's **~900 decision steps/sec**.

For PPO, we need:
- Rollout: play N games with current policy, collecting (state, action, reward, value)
- Update: run PPO gradient updates on the collected batch
- Repeat

### Proposed MVP setup

```
Algorithm: PPO
Policy: v106 GNN (warm-start from BC checkpoint)
Value: same model's value head (also warm-started)
Environment: C++ engine via batched greedy play (pool_size=20)
Opponent: MinimalHybrid heuristic (fixed, not co-evolving)

Rollout batch: 200 games (~30K decision steps, ~33 seconds)
PPO epochs per batch: 3-4 (standard)
PPO clip epsilon: 0.2 (standard)
Learning rate: 1e-4 (10x smaller than BC to prevent catastrophic forgetting)
GAE lambda: 0.95
Discount gamma: 0.99

Reward: +1 for win, -1 for loss (from acting side's perspective)
         Applied at game end, propagated via GAE
Optional: +0.01 * VP_delta_per_turn as intermediate reward shaping

Total training: 200 batches x 200 games = 40,000 games
Wall time: 40K games / 6 games/sec = ~110 minutes rollout
           + ~50 minutes gradient updates (GPU)
           = ~3 hours total
```

### What to expect

**Optimistic case (30% probability):** PPO fine-tuning improves combined WR by 3-8pp
over BC greedy (reaching 38-43% combined). This would match or approach the MCTS 2000sim
result (43.7%) but at greedy inference cost.

**Base case (50% probability):** PPO improves by 1-3pp (36-38% combined). Modest but
real improvement that stacks with MCTS at inference time.

**Pessimistic case (20% probability):** PPO fails to improve or regresses. Possible
causes: catastrophic forgetting of BC initialization, reward signal too sparse for
150-step episodes, opponent overfitting to heuristic weaknesses.

### Warm-start is critical

Starting from random policy would require 500K+ games minimum (months of compute).
Starting from the BC policy (35% WR) means the policy already plays reasonable
Twilight Struggle and just needs to improve at the margins.

The BC policy provides:
- Reasonable card selection (65% top-1 accuracy)
- Good mode selection (83% accuracy)
- Adequate but suboptimal influence placement
- A value head that correlates with game outcome

PPO needs to improve primarily on:
- Influence placement (the identified bottleneck)
- Strategic mode selection (less coups, more events -- matching human expert profile)
- Long-term planning (sacrificing short-term VP for positional advantage)

### Reward design

**Primary: game outcome (+1/-1)**
This is the simplest and most principled. The value head provides the baseline for
variance reduction. Game outcome is the ultimate signal.

**Optional intermediate reward: VP delta per turn**
VP changes each turn during scoring. Adding small intermediate rewards (0.01 * VP_delta)
provides more frequent signal without fundamentally changing the optimization target.

**Danger: heuristic-specific reward shaping**
Do NOT add rewards for "controlling regions" or "having more influence" -- these
encode assumptions about what good play looks like and may prevent discovering novel
strategies. Keep rewards outcome-based.

### Implementation steps

1. **Trajectory collector** (~1 day): Modify `collect_games_batched` to return per-step
   log-probabilities and value estimates alongside actions and states. Currently it
   records actions but not the policy distribution.

2. **PPO loss computation** (~1 day): Standard PPO with clipped surrogate objective.
   Reuse existing model forward pass; add computation of:
   - old_log_prob (stored during rollout)
   - new_log_prob (recomputed during update)
   - advantage (GAE from value predictions and rewards)

3. **Training loop** (~0.5 day): Alternate between rollout (C++ engine) and update
   (PyTorch). Can be single-process since rollout is fast enough.

4. **Monitoring** (~0.5 day): Track policy entropy, value loss, clip fraction,
   approximate KL divergence from BC policy, and periodic benchmark WR.

Total implementation: ~3 days. First results in ~4 hours after implementation.

---

## 3. Biggest Obstacles

### 3a. Credit assignment (SERIOUS)

~150 decisions per game with reward only at game end. This is the #1 risk.

**Mitigations:**
- The warm-started value head already provides per-step value estimates (trained on
  final_vp). This V(s) baseline is the key variance reduction tool
- GAE (Generalized Advantage Estimation) with lambda=0.95 propagates credit through
  the value function, effectively providing per-step advantage signals
- Intermediate VP-delta reward shaping provides additional signal at turn boundaries
  (roughly every 15 decisions)
- The game has natural structure: each Action Round is somewhat independent, and
  scoring phases provide clear value checkpoints

**Comparison to known successes:**
- Go (AlphaZero): ~150 moves, sparse reward -> solved by MCTS+RL
- Poker (Pluribus/ReBeL): ~10-50 decisions per hand, sparse reward -> solved by CFR+RL
- Dota 2 (OpenAI Five): ~20,000 steps per game, sparse reward -> solved by PPO with
  reward shaping and massive compute
- StarCraft (AlphaStar): ~10,000 steps, sparse reward -> solved by PG + league

TS at 150 steps is well within the range where PG methods have succeeded, IF the value
baseline is good. Our value head is trained on 2.7M examples and should provide
reasonable baselines.

### 3b. Imperfect information (MODERATE)

The player doesn't see the opponent's hand (7-9 hidden cards). This means:
- The policy operates on a partial observation (own hand + public board state)
- Optimal play requires reasoning about what the opponent *might* hold
- The same board state can have very different optimal actions depending on opponent's hand

**Impact on RL:**
PG methods handle partial observability naturally -- they optimize E[R | pi] where
the expectation is over all hidden information. The policy learns to play well *on
average* against the distribution of opponent hands. This is exactly what BC already
does (the BC model never sees opponent's hand).

The issue is that the policy cannot be *optimal* without belief tracking (inferring
opponent's hand from their actions). This is a ceiling on any approach that doesn't
model opponent beliefs. But for breaking the BC ceiling, this is not the binding
constraint -- the BC model also doesn't track beliefs and still has room to improve.

**Long-term:** ISMCTS + opponent modeling would address this, but it's orthogonal to
the RL training question and can be added later.

### 3c. Opponent overfitting (MODERATE)

Training against the fixed MinimalHybrid heuristic risks learning exploit strategies
that don't generalize. For example, if the heuristic always plays a specific opening,
the RL policy might learn a counter that fails against other opponents.

**Mitigations:**
- The heuristic uses Nash-equilibrium mixed temperatures (stochastic play), providing
  some diversity
- Periodic evaluation against the BC policy (not just the heuristic) detects overfitting
- If overfitting becomes apparent, switch to a league: train against a mix of
  (heuristic, BC policy, previous RL checkpoints)
- The self-play echo chamber lesson (v11/v12 collapse) applies here -- always maintain
  the heuristic anchor in the opponent pool

**Risk level:** Moderate. The heuristic is a reasonable opponent (~1200 Elo), and
TS has enough complexity that simple exploits are unlikely to dominate. But this
should be monitored.

### 3d. Exploration (MODERATE)

The action space per decision is large (up to ~500 legal actions for influence
placement). The BC-warm-started policy concentrates >99.99% mass on a few actions.
PPO will update within this concentrated distribution, potentially never exploring
alternatives.

**Mitigations:**
- Entropy bonus in the PPO loss (standard): penalizes overly concentrated policies,
  encouraging exploration of alternative actions
- The policy already covers reasonable actions (65% top-1 card accuracy means the
  remaining 35% explores alternatives)
- For influence placement specifically, the policy's distribution over countries is
  where the most improvement is needed, and PPO gradient will push probability toward
  countries that lead to better outcomes
- Epsilon-greedy exploration during rollout (already supported in the config)

### 3e. Factorized action gradient (LOW RISK)

The decomposition log pi(a) = log pi_card + log pi_mode + log pi_country means all
three heads get the same advantage signal. This is correct but means:
- If a bad outcome was due to a bad country choice, the card and mode heads also
  get (noisy) gradient signal
- Credit is not decomposed across heads

In practice, this works because:
- Over many samples, the card head averages out the country noise and vice versa
- The warm-started heads are already near-optimal for card/mode (65%/83% accuracy),
  so gradient noise on those heads has little effect
- The country head, which needs the most improvement, will receive the strongest
  consistent signal (bad placements -> bad outcomes)

---

## 4. Literature Context

### Most relevant papers

1. **"Reevaluating Policy Gradient Methods for Imperfect-Information Games"**
   (Rudolph et al., 2025, arxiv 2502.08938)
   - 7000+ training runs across 5 large games
   - PPO outperforms FP/DO/CFR-based deep RL methods
   - Key finding: generic PG methods work better than game-theoretic RL in practice
   - Directly applicable: validates PPO as the right choice for TS

2. **"AlphaZe**: AlphaZero-like baselines for imperfect information games are
   surprisingly strong"** (Frontiers in AI, 2023)
   - AlphaZero + determinized MCTS works well for imperfect-info games
   - Tested on Stratego (large state space, hidden information)
   - Relevant: our MCTS infrastructure could support this, but compute cost is high

3. **ReBeL: Recursive Belief-based Learning** (Brown et al., NeurIPS 2020)
   - Gold standard for imperfect-info game solving
   - Combines self-play RL with CFR search at each decision point
   - Superhuman in No-Limit Texas Hold'em
   - Too complex for our setup but provides theoretical grounding

4. **Advantage-Weighted Regression** (Peng et al., 2019, arxiv 1910.00177)
   - Offline RL via advantage-weighted BC
   - We already tried this (v96b_aw) -- it didn't break the ceiling
   - Confirms that offline approaches are insufficient; online RL needed

5. **HCAPO: Hindsight Credit Assignment Policy Optimization** (2026)
   - Converts sparse trajectory-level feedback into step-level advantage signals
   - Relevant for our 150-step sparse-reward problem
   - Could be a future improvement on top of basic PPO+GAE

### Twilight Struggle specific

No published RL work on Twilight Struggle exists in the academic literature. The Steam
AI uses hand-tuned heuristics, not ML. The Playdek/Steam implementations provide no
public technical details about their AI beyond forum discussions.

This project appears to be the first serious ML/RL approach to Twilight Struggle.

### Closest analogs

- **Hanabi** (cooperative, imperfect info, cards): PPO works well (Yu et al., MAPPO)
- **Magic: The Gathering** (competitive, imperfect info, cards, complex): limited RL
  success due to extreme action space complexity
- **Stratego** (competitive, imperfect info, board game): AlphaZe** approach works
- **Poker** (competitive, imperfect info, sequential): ReBeL/Pluribus solved it, but
  poker has much shorter episodes (~10-50 decisions vs 150)

TS is harder than poker (longer horizon, larger action space, more complex state) but
easier than full Stratego (smaller board, fewer hidden units). PPO has succeeded in
games of comparable or greater complexity.

---

## 5. Concrete Recommendation

### Primary path: PPO fine-tuning of BC policy

**Algorithm:** PPO (clipped surrogate objective)
**Initialization:** v106 GNN checkpoint (BC-trained, 34.9% combined)
**Opponent:** MinimalHybrid heuristic with Nash temperatures
**Reward:** +1/-1 game outcome, optional +0.01 * VP_delta_per_turn

**Training loop sketch:**
```
load v106 checkpoint -> policy_net, value_net (shared trunk)
for iteration in range(200):
    # Rollout phase
    games = collect_games_batched(
        n_games=200, model=policy_net, opponent=heuristic,
        record_log_probs=True, record_values=True
    )  # ~33 seconds
    
    # Compute advantages via GAE
    for game in games:
        compute_gae(game.steps, gamma=0.99, lam=0.95)
    
    # PPO update phase (3-4 epochs over the batch)
    batch = flatten_steps(games)  # ~30K steps
    for ppo_epoch in range(4):
        for minibatch in batch.shuffle().split(4096):
            new_log_probs, new_values, entropy = policy_net(minibatch.states)
            ratio = exp(new_log_probs - minibatch.old_log_probs)
            clipped_ratio = clip(ratio, 1-0.2, 1+0.2)
            policy_loss = -min(ratio * advantages, clipped_ratio * advantages).mean()
            value_loss = mse(new_values, minibatch.returns)
            entropy_loss = -entropy.mean()
            loss = policy_loss + 0.5 * value_loss + 0.01 * entropy_loss
            optimizer.step(loss)
    
    # Periodic evaluation (every 20 iterations)
    if iteration % 20 == 0:
        benchmark(policy_net, n_games=500)  # ~80 seconds
```

**Expected compute:**
- Rollout: 200 iterations x 33s = 110 minutes
- Updates: 200 iterations x ~15s = 50 minutes
- Evaluation: 10 benchmarks x 80s = 13 minutes
- **Total: ~3 hours**

**Expected outcome:**
- 50% chance of 1-3pp improvement (36-38% combined greedy)
- 30% chance of 3-8pp improvement (38-43% combined greedy)
- 20% chance of no improvement or regression
- If PPO-trained policy + MCTS at inference: potentially 45-50% combined

### Secondary path: improve MCTS efficiency (complementary)

MCTS 2000sim already reaches 43.7% combined but takes 5.2s/game. Reducing this to
~1s/game (via parallel MCTS, better caching, or fewer sims with better pruning) would
make MCTS-based policy improvement more viable.

This is complementary to PPO: a better policy (from PPO) + MCTS at inference = the
best possible result.

### What NOT to try

- **Q-learning/DQN:** Action space is wrong for it
- **Offline RL (CQL/IQL):** Already at the data ceiling; AWR experiment confirmed this
- **Full AlphaZero loop:** Too expensive for current hardware (100+ hours per generation)
- **ReBeL/CFR-based:** Too complex to implement; overkill for the expected gain
- **Decision Transformer:** Needs massive data and compute; unlikely to beat PPO for games
- **Self-play without anchor:** v11/v12 collapse confirms this fails

### Priority vs alternatives

| Approach | Expected gain | Implementation cost | Compute cost | Risk |
|----------|--------------|-------------------|-------------|------|
| **PPO fine-tuning** | **+1-8pp** | **3 days** | **3 hours** | **Moderate** |
| Allocation head (DP decoder) | +2-5pp | 2-3 days | 30 min training | Low-moderate |
| More MCTS sims at inference | +8.8pp (known) | 0 days | 5s/game | Zero |
| Parallel MCTS | +0pp (speed only) | 3-5 days | N/A | Low |
| Offline RL (CQL/IQL) | +0-2pp | 2-3 days | 1 hour | High |

**Recommended order:**
1. **PPO fine-tuning** (highest expected value, moderate risk)
2. **Allocation head** (architectural improvement, complementary to PPO)
3. **Parallel MCTS** (speed improvement, enables AlphaZero-style later)

PPO and the allocation head can be developed in parallel since they address different
bottlenecks (optimization objective vs architecture).

---

## 6. Risk Mitigation

### Catastrophic forgetting
- Use small learning rate (1e-4, 10x below BC)
- PPO clipping (epsilon=0.2) limits per-update policy change
- Monitor KL divergence from initial BC policy; abort if KL > 0.1
- Keep BC checkpoint as fallback; never overwrite

### Reward hacking
- Primary reward is game outcome -- hard to hack
- If using VP shaping, keep coefficient small (0.01) and monitor for degenerate play
  (e.g., triggering scoring in losing regions just for VP signal)

### Self-play collapse (if later switching to self-play RL)
- Always maintain heuristic opponent as anchor (proven by v11/v12 failure)
- Use opponent pool: 50% heuristic, 25% BC policy, 25% latest RL checkpoint
- Monitor win rate against ALL opponents, not just the training opponent

### Debugging failures
- If WR drops during training: check entropy (too low = collapsed policy),
  clip fraction (too high = learning rate too large), value loss (diverging = bad GAE)
- If WR plateaus immediately: increase entropy coefficient, try VP shaping reward,
  increase rollout batch size
- If WR oscillates: reduce learning rate, increase PPO clip range, use more PPO epochs

---

## 7. Comparison to Alternative Paths

### The BC ceiling is real

12 dead ends confirm that no BC variant exceeds 35% combined. The ceiling is caused by
the BC objective (match heuristic actions) being misaligned with the actual goal (win
games). BC cannot improve on actions the heuristic never takes.

### MCTS is the known-good escape

MCTS 2000sim reaches 43.7% combined (+8.8pp). This proves the model's *value* head is
much better than its *policy* head -- tree search finds better actions by looking ahead
with the value function. RL could achieve a similar effect by training the policy to
directly optimize game outcomes.

### RL addresses the root cause

The root cause of the BC ceiling is that the policy optimizes action prediction, not
game outcome. RL directly optimizes game outcome. This is the principled fix.

### Expected combined ceiling with RL + MCTS

If PPO training reaches ~40% greedy (conservative estimate) and MCTS adds ~8pp on top,
the combined system could reach ~48% combined against the heuristic. This would
represent a significant milestone.

---

## Sources

- [Reevaluating Policy Gradient Methods for Imperfect-Information Games (Rudolph et al., 2025)](https://arxiv.org/abs/2502.08938)
- [AlphaZe**: AlphaZero-like baselines for imperfect information games are surprisingly strong](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2023.1014561/full)
- [ReBeL: Combining Deep Reinforcement Learning and Search for Imperfect-Information Games](https://arxiv.org/abs/2007.13544)
- [Advantage-Weighted Regression: Simple and Scalable Off-Policy RL](https://arxiv.org/abs/1910.00177)
- [The 37 Implementation Details of Proximal Policy Optimization](https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/)
- [A Policy-Gradient Approach to Solving Imperfect-Information Games with Best-Iterate Convergence](https://arxiv.org/abs/2408.00751)
- [The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games](https://arxiv.org/abs/2103.01955)
- [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8)
- [HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents](https://arxiv.org/html/2603.08754)
