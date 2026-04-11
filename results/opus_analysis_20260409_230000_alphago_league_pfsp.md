---
# Opus Analysis: AlphaGo League Training vs Our Approach
Date: 2026-04-09T23:00:00Z

## Executive Summary

AlphaGo Zero and AlphaZero used a single continuous training loop with fixed hyperparameters and no opponent diversity — the current model always played against itself. Prioritized Fictitious Self-Play (PFSP) was introduced later in AlphaStar (2019), not AlphaZero. PFSP samples opponents proportional to f(1 - WR_against_them), concentrating training time on opponents the agent struggles against. Our current league approach (recency-weighted past-self + fixtures + heuristic mix) is a reasonable budget approximation but lacks the WR-gated hard-opponent signal that PFSP provides. Adding lightweight PFSP is feasible with ~50 overhead games per Elo update and would cost under 5 minutes per iteration. For training schedule, AlphaZero's continuous loop with fixed hyperparameters is actually closer to what we want than our current 200-iteration runs with entropy decay — the key difference is that AlphaZero never reset optimizer state or decayed hyperparameters within a "run" because there was only one run.

## Findings

### PFSP and WR-gated opponent sampling

#### What AlphaGo Zero / AlphaZero actually did (no PFSP)

AlphaGo Zero (2017) and AlphaZero (2017) did NOT use league training or opponent pools at all. Their training was simple:

1. **Single self-play loop**: The current best model plays games against itself.
2. **No opponent diversity**: There is exactly one opponent — the current network (or a slightly older checkpoint used for stability, updated every N iterations).
3. **No win-rate tracking against a pool**: There was no pool to track against.
4. **Checkpoint replacement rule**: AlphaGo Zero replaced the "best player" only if the new network won >55% of evaluation games against the current best. AlphaZero simplified this further — it just used the latest checkpoint directly with no gating.

The AlphaGo Zero paper (Silver et al., 2017): "In each iteration, the neural network is trained from games of self-play with the current best player." The key insight was that MCTS + self-play alone was sufficient for perfect-information games like Go and Chess.

#### Where PFSP actually comes from: AlphaStar

Prioritized Fictitious Self-Play was introduced in **AlphaStar** (Vinyals et al., 2019) for StarCraft II, which has:
- Imperfect information (fog of war)
- Asymmetric strategies (3 races)
- Rock-paper-scissors dynamics that pure self-play collapses into

AlphaStar's league had three agent types:
1. **Main agents**: trained to beat the full league
2. **Main exploiters**: trained to find weaknesses in main agents
3. **League exploiters**: trained to beat the entire historical league

#### The PFSP formula

For a main agent selecting opponents from the league:

```
p(opponent_j) ∝ f(1 - WR(agent_i, opponent_j))
```

Where:
- `WR(agent_i, opponent_j)` = empirical win rate of agent_i against opponent_j, estimated from recent games
- `f(x)` is a weighting function. AlphaStar used `f(x) = x^p` where p was typically set to capture the right balance

Concrete variants used:
- **Hard prioritization**: `f(x) = x` — linear in difficulty. If you win 90% against opponent A and 40% against opponent B, B is sampled 6/4 = 1.5x more than A. Simple but effective.
- **Squared prioritization**: `f(x) = x^2` — harder opponents are sampled quadratically more. If WR=0.9 vs A and WR=0.4 vs B, then B is sampled (0.6^2)/(0.1^2) = 36x more.
- **Soft prioritization**: `f(x) = (1-x)^(-p)` for exploitation-focused agents.

The formula used in practice for main agents in AlphaStar:

```
p(opponent_j) ∝ (1 - WR_j)^p / Σ_k (1 - WR_k)^p
```

With p ≈ 1 for main agents (hard prioritization) and the WR estimates updated every ~100 games.

#### How WR was tracked

- **Per-pair win rates**: The league maintained a payoff matrix `WR[i][j]` for every (agent, opponent) pair.
- **Update frequency**: After every batch of games (typically after each training iteration when evaluation games were played).
- **Windowed estimation**: Only recent games counted (sliding window or exponential decay), so WR estimates tracked the current agent's improving strength.
- **Practical overhead**: Evaluation games were cheap compared to training — a few hundred games per update were sufficient for stable WR estimates.

#### How this compares to our current `sample_K_league_opponents`

Our current sampling (from `train_ppo.py:794`):

| Feature | Our approach | PFSP |
|---------|-------------|------|
| Opponent pool | Past checkpoints + fixtures + heuristic | Full historical league |
| Sampling weight | Recency (exp(rank/tau)) | Difficulty (1 - WR)^p |
| Self-play slot | Yes (slot 0 = current model) | Yes (main agents play themselves too) |
| WR tracking | None — we don't track per-opponent WR | Core mechanism |
| Fixture fadeout | Hard cutoff at iter 50 | Implicit via WR (easy fixtures get low weight) |
| Heuristic floor | 10% of slots | Not applicable (no heuristic in AlphaStar) |

The key gap: **we have no WR signal**. Our recency weighting is a proxy that assumes "newer = harder," which is approximately true when training is monotonically improving but fails when:
- A past checkpoint happens to be a stylistic counter to the current model
- The current model has developed a blind spot that an older model exploits
- Fixtures become too easy but haven't hit the fadeout threshold yet

#### Would PFSP make sense for Twilight Struggle?

**Yes, with caveats.**

Arguments for:
1. TS has imperfect information — pure self-play is less stable than in Go/Chess.
2. We've already seen policy collapse (v11/v12 regressing from echo-chamber self-play per project memory).
3. Our Elo ladder shows non-monotonic strength (v23=1733 is weaker than v8=1945), confirming that recency != difficulty.
4. PFSP would naturally handle fixture fadeout — easy opponents get low WR-weight without a hard cutoff.

Arguments against / caveats:
1. Our pool is small (~20 checkpoints). PFSP shines with 100+ agents. With <20, the WR estimates will be noisy.
2. WR estimation requires extra games. With 200 games/iter total budget, spending 50 on evaluation cuts into training data.
3. TS games are long (~300 steps) and expensive. StarCraft was also long, but AlphaStar had vastly more compute.

#### Practical implementation for our infrastructure

**Minimal PFSP addition to `sample_K_league_opponents`:**

```python
def sample_K_league_opponents_pfsp(
    league_dir: str,
    k: int,
    wr_table: dict[str, float],  # opponent_path -> estimated WR against them
    pfsp_exponent: float = 1.0,  # p in (1-WR)^p
    heuristic_pct: float = 0.10,
    self_slot: bool = True,
    current_script: Optional[str] = None,
    min_wr_games: int = 20,  # minimum games before trusting WR estimate
) -> list[Optional[str]]:
    """PFSP-weighted opponent sampling."""
    # Parse available opponents
    opponents = list_league_opponents(league_dir)  # existing logic
    
    # Compute PFSP weights
    weights = []
    for opp in opponents:
        wr = wr_table.get(opp, 0.5)  # default 50% for unknown opponents
        # (1 - WR)^p: harder opponents get higher weight
        w = max(0.01, (1.0 - wr)) ** pfsp_exponent
        weights.append(w)
    
    # Normalize
    total = sum(weights)
    weights = [w / total for w in weights]
    
    # Sample k-1 opponents (slot 0 is self)
    result = [current_script] if self_slot else []
    for _ in range(k - len(result)):
        if random.random() < heuristic_pct:
            result.append(None)  # heuristic
        else:
            result.append(random.choices(opponents, weights=weights, k=1)[0])
    return result
```

**WR tracking integration:**

```python
# In the main training loop, after each iteration's rollout:
# Track per-opponent WR from game results
wr_tracker: dict[str, list[bool]] = defaultdict(list)  # opp -> [win/loss...]

# After rollout games complete:
for opp_path, game_result in zip(opponent_assignments, game_results):
    wr_tracker[opp_path].append(game_result.won)

# Compute windowed WR estimates:
wr_table = {}
for opp, results in wr_tracker.items():
    recent = results[-100:]  # last 100 games window
    wr_table[opp] = sum(recent) / len(recent)
```

**Practical overhead estimate:**
- No extra games needed if we track WR from training rollouts themselves (which we already play).
- The WR signal is slightly noisy because the training agent changes each iteration, but with a window of 100 games it's stable enough.
- Zero GPU overhead — just bookkeeping in Python.
- Memory: negligible (dict of ~20 floats).

### AlphaZero training schedule vs our runs

#### What AlphaZero actually did

**AlphaGo Zero** (for Go):
- **One continuous training loop**, not restartable runs
- 4.9 million games of self-play over 72 hours on 4 TPUs
- **Fixed hyperparameters throughout**: lr=0.01 with scheduled drops (to 0.001 at 400k steps, 0.0001 at 600k steps — this was step-wise LR decay, not per-run)
- SGD with momentum 0.9, weight decay 1e-4
- No entropy bonus (MCTS provides exploration)
- Batch size 2048 positions
- Training window: most recent 500k games (sliding window of self-play data)
- Temperature: t=1 for first 30 moves, t→0 after (in self-play)
- Dirichlet noise at MCTS root: Dir(0.03) with weight 0.25

**AlphaZero** (for Chess, Shogi, Go):
- **One continuous loop**, 700k training steps
- Fixed learning rate 0.02 (Go) or 0.2 (Chess), with no schedule mentioned in the paper (some implementations used step-wise drops)
- SGD with momentum 0.9, weight decay 1e-4
- 5000 TPUs for self-play, 16 TPUs for training
- Batch size 4096
- Training window: most recent 1 million games
- **No evaluation gating** — latest checkpoint always used (simplified from AlphaGo Zero's 55% win-rate gate)
- Temperature: t=1 for first 30 moves, t→0 after
- Dirichlet noise: Dir(α) with α = 10/avg_legal_moves, weight 0.25

Key observation: **Neither system had "runs" that ended and restarted.** It was one continuous process. The only hyperparameter change was LR drops at predetermined step counts.

#### What we do

From `ppo_loop_step.sh` and `train_ppo.py`:

| Parameter | Our approach | AlphaZero |
|-----------|-------------|-----------|
| Training structure | 200-iteration runs, chained via ppo_loop_step.sh | One continuous loop |
| LR | Fixed 2e-5 per run | Fixed with 1-2 step drops over entire training |
| LR across runs | Same 2e-5 each run (optimizer state restored) | N/A (no runs) |
| Entropy coef | 0.03 → 0.005 linear decay per run | No entropy bonus (MCTS explores) |
| Optimizer state | Restored from checkpoint between runs | Continuous (never reset) |
| PPO epochs | Fixed per iteration | N/A (used simple SGD on MCTS targets) |
| Clip epsilon | 0.12 fixed | N/A (no PPO — used cross-entropy + MSE loss) |
| Self-play data | Fresh rollouts each iteration, no replay buffer | Sliding window of recent games |
| Exploration | rollout_temp=1.2, no Dirichlet noise | Dirichlet noise + temperature schedule |

#### Critical difference: AlphaZero didn't use PPO

AlphaZero's training was **not** policy gradient / PPO at all. It was supervised learning on MCTS-generated targets:

```
Loss = (z - v(s))^2 - π_MCTS(s)^T log p(s) + c||θ||^2
```

Where:
- `z` = game outcome (+1/-1)
- `v(s)` = value head prediction
- `π_MCTS(s)` = MCTS visit count distribution (the "teacher" target)
- `p(s)` = policy head output

This is cross-entropy loss on policy + MSE on value, trained on (state, MCTS_policy, outcome) tuples from a sliding replay buffer. No advantages, no clipping, no entropy bonus.

**This matters because:**
1. PPO's entropy decay makes sense (PPO needs explicit exploration encouragement). AlphaZero didn't need it because MCTS + Dirichlet noise provided exploration.
2. PPO's clip epsilon prevents catastrophic updates. AlphaZero didn't need this because it trained on a large replay buffer of stable targets.
3. Our 200-iteration run structure exists partly because PPO can go unstable — the run boundary is a natural checkpoint/restart point. AlphaZero's supervised loss is inherently more stable.

#### Would infinite PPO with fixed hyperparams be better for us?

**Probably yes for the training loop, but we need the entropy schedule.**

Arguments for continuous training (no run boundaries):
1. Optimizer momentum is preserved (we already do this via state restoration, so the boundary is mostly cosmetic).
2. No entropy schedule reset — currently each run re-decays from 0.03→0.005, meaning every run starts with high entropy then contracts. A continuous loop would let entropy settle at a stable level.
3. Simpler code — no ppo_loop_step.sh chaining, no watcher processes.

Arguments for keeping run boundaries:
1. **Natural Elo checkpoints**: Each run boundary triggers an Elo tournament. This is valuable.
2. **Plateau detection**: The 3-consecutive-plateau rule requires discrete boundaries.
3. **Recovery from divergence**: If a run goes bad, the previous checkpoint is clean. With continuous training, you'd need periodic snapshots (which we have — iter_*.pt every 10 iters).
4. **Entropy reset may actually help**: Re-injecting entropy every 200 iters forces re-exploration, which may prevent the policy collapse we've seen. This is similar to "restarts" in optimization.

**Recommendation**: Keep the run structure for operational reasons (Elo, plateau detection, recovery), but consider:
1. A **global entropy schedule** that doesn't reset per run (e.g., decay based on total training iterations across all runs).
2. Removing the entropy schedule entirely and using a fixed low value (e.g., 0.01) — AlphaZero showed that exploration can come from other mechanisms (temperature, Dirichlet noise).
3. The real priority is adding **Dirichlet noise at MCTS root** (already item #1 on CLAUDE.md priority list) — this is how AlphaZero achieved exploration without entropy bonuses.

#### Hyperparameter comparison table

| Hyperparameter | AlphaGo Zero | AlphaZero (Chess) | Our PPO |
|---|---|---|---|
| Algorithm | SGD on MCTS targets | SGD on MCTS targets | PPO (policy gradient) |
| Learning rate | 0.01 → 0.001 → 0.0001 | 0.2 (fixed?) | 2e-5 (fixed per run) |
| Optimizer | SGD + momentum 0.9 | SGD + momentum 0.9 | Adam |
| Weight decay | 1e-4 | 1e-4 | 0 (Adam default) |
| Batch size | 2048 | 4096 | ~all steps per iter |
| Entropy bonus | None | None | 0.03 → 0.005 |
| Clip epsilon | N/A | N/A | 0.12 |
| Replay buffer | 500k games (sliding window) | 1M games | None (on-policy) |
| MCTS sims/move | 1600 | 800 | None (direct policy) |
| Dirichlet noise | Dir(0.03), weight 0.25 | Dir(0.3), weight 0.25 | None |
| Temperature | 1.0 first 30 moves, then →0 | 1.0 first 30 moves | 1.2 (constant) |
| Training steps | 3.1M (Go), continuous | 700k, continuous | 200 iters/run × N runs |
| Self-play games | 4.9M | 44M (Chess) | 200/iter × 200 iters = 40k/run |

### Applicability to Twilight Struggle

#### Key differences from Go/Chess that affect training design

1. **Imperfect information**: TS has hidden hands, unknown opponent cards. Pure self-play is less stable because the optimal policy depends on beliefs about hidden state. This is why we've seen policy collapse — the model learns to exploit its own predictable play style rather than developing robust strategies.

2. **High variance outcomes**: A single card draw can swing a game. This means:
   - Value estimates are noisier
   - More games needed per WR estimate
   - GAE advantages have higher variance

3. **Asymmetric game**: USSR and US have fundamentally different strategies. AlphaZero's games (Chess) had symmetric positions (modulo color, which alternates). TS requires training both sides.

4. **Long games with sparse rewards**: ~300 decision points per game, with the main reward at game end. AlphaZero also had this (Go games are ~200 moves), but combined it with MCTS for intermediate value estimates.

5. **Small compute budget**: RTX 3050 4GB vs thousands of TPUs. This means:
   - We can't afford 1600 MCTS sims per move
   - We can't afford millions of training games
   - Every game counts — WR-gated sampling would extract more learning signal per game

#### What to adopt

**High value, low cost (do first):**
1. **WR tracking from existing rollouts**: Zero extra cost. Just track which opponent each game was against and whether we won. Use this to weight `sample_K_league_opponents`.
2. **Global entropy schedule**: Instead of resetting 0.03→0.005 each run, track total iterations across runs and use a single monotonic schedule (or just fix entropy at 0.01).
3. **Dirichlet noise in rollouts**: Already item #1 on CLAUDE.md. This is how AlphaZero got exploration without entropy bonuses.

**Medium value, medium cost (do second):**
4. **PFSP weighting with p=1**: Replace recency weighting with WR-based weighting. Keep recency as a tiebreaker for opponents with similar WR.
5. **Temperature schedule per game**: Use T=1.2 for early game, T→0.6 for late game (like AlphaZero's 30-move threshold, adapted to TS's ~30 action rounds).

**Lower priority for our scale:**
6. **Replay buffer**: AlphaZero used a sliding window of past games. For PPO this conflicts with on-policy requirements, but we could keep a small buffer of hard positions for auxiliary training.
7. **Main agent / exploiter split**: Only makes sense with 10+ agents training simultaneously. Not for our single-GPU setup.

## Conclusions

1. **PFSP is from AlphaStar, not AlphaZero.** AlphaZero used pure self-play with no opponent pool. The league + PFSP approach was developed for StarCraft II's imperfect-information, asymmetric-strategy setting — which is actually closer to Twilight Struggle than Go/Chess is.

2. **Our league approach is a reasonable budget PFSP approximation**, but the recency heuristic misses the core insight: train more against opponents you struggle against. Adding WR tracking is nearly free (just bookkeeping from games we already play).

3. **AlphaZero used continuous training, not runs, and it trained on MCTS targets (supervised), not PPO.** Our run structure serves operational purposes (Elo checkpoints, plateau detection) that are worth keeping. The entropy decay per run is the main thing to reconsider.

4. **The biggest gap between our approach and AlphaZero is not the training schedule — it's the lack of MCTS.** AlphaZero's strength came from MCTS-generated policy targets during self-play. Without MCTS, our policy network must discover good moves purely from game outcomes, which is much harder. Adding even 50-100 sim MCTS to rollouts (already on the CLAUDE.md roadmap as ISMCTS) would be the single largest strength improvement.

5. **For our budget (RTX 3050, 65 min/run), PFSP's efficiency gain matters more than it would at AlphaZero scale.** When every game is expensive, spending training time on informative opponents rather than easy ones has outsized returns.

## Recommendations

1. **Add WR tracking to the league loop (1-2 hours to implement)**:
   - Track per-opponent WR from rollout game results in `collect_rollout_league_batched`.
   - Persist WR table as JSON in the league directory.
   - Pass WR table to `sample_K_league_opponents` and use `(1-WR)^1` weighting instead of recency.
   - Keep recency as a secondary signal (multiply PFSP weight by recency weight).

2. **Switch to a global entropy schedule (30 min to implement)**:
   - Store total_iterations in checkpoint metadata.
   - Compute entropy coef from total iterations, not per-run iteration.
   - Target schedule: 0.03 for first 400 total iters, then linear decay to 0.005 by iter 2000, then fixed.

3. **Keep 200-iteration run boundaries for Elo and plateau detection**:
   - The operational benefits outweigh the minor inefficiency of run boundaries.
   - Optimizer state is already restored, so the boundary is mostly a checkpoint/eval trigger.

4. **Prioritize ISMCTS over PFSP for strength gains**:
   - PFSP extracts more signal from the games we play; ISMCTS generates fundamentally better signal.
   - Even 25-50 sim ISMCTS during rollouts would approximate AlphaZero's MCTS-target training.
   - PFSP and ISMCTS are complementary — do both, but ISMCTS first if forced to choose.

5. **Add Dirichlet noise to rollout action selection (already planned)**:
   - Use Dir(α) with α = 10 / average_legal_actions at the root.
   - Mix weight 0.25 (AlphaZero default).
   - This replaces some of the role that entropy bonus currently plays.

## Open Questions

1. **PFSP exponent tuning**: Should we use p=1 (linear) or p=2 (squared)? With our small pool (~20 opponents), p=1 is probably sufficient. p=2 would over-concentrate on the single hardest opponent, which with noisy WR estimates could be misleading.

2. **WR estimation window**: How many games before we trust a WR estimate? With 200 games/iter split across 4 opponents, each opponent gets ~50 games/iter. A window of 2-3 iterations (100-150 games) should give reasonable estimates. For new opponents with <20 games, default to WR=0.5 (uniform sampling).

3. **Entropy schedule vs Dirichlet noise**: If we add Dirichlet noise to rollouts, should we reduce or eliminate the entropy bonus entirely? AlphaZero used no entropy bonus. But AlphaZero trained on MCTS targets (supervised), while PPO benefits from entropy regularization to prevent premature convergence. Likely answer: keep a small fixed entropy (0.005-0.01) rather than scheduling it.

4. **Replay buffer for PPO**: AlphaZero used a sliding window of 500k-1M games as a replay buffer. PPO is on-policy and shouldn't use stale data. However, we could use a small buffer of "hard positions" (positions where the model was most uncertain or lost badly) for auxiliary supervised training alongside PPO. Is this worth the complexity?

5. **How often should PFSP weights update?**: Every iteration is fine for us — we play games every iteration and the bookkeeping cost is negligible. AlphaStar updated after each batch of games, which is equivalent.

6. **v23 at 1733 Elo**: This is a clear regression — below v8 (1945). PFSP would naturally avoid sampling v23 as an opponent (high WR against it = low PFSP weight). But it raises a question: should regressed checkpoints be pruned from the pool entirely, or does playing against them occasionally serve as a useful "easy win" calibration?
---
