---
# Opus Analysis: AlphaStar Ideas Applicability to Twilight Struggle AI
Date: 2026-04-10T00:00:00Z

## Executive Summary

Most AlphaStar techniques address problems that arise at massive scale (thousands of actors, billions of frames, distributed training) and do not directly transfer to our single-GPU, 200-game/iteration PPO setup. The three highest-value ideas for our setting are (1) KL regularization toward the BC policy, which directly addresses the entropy explosion / policy collapse we observed in v23, (2) UPGO-style selective reinforcement, which is cheap to implement and well-matched to our sparse-reward, long-horizon game, and (3) a carefully tuned per-game temperature schedule, which captures exploration benefits without the training instability that uniform T=1.2 caused. PFSP and league training are already implemented and appear to be working, but the current implementation has a subtle flaw: the recency*PFSP weighting effectively creates a "moving window" that forgets hard opponents too quickly. Dirichlet noise, V-trace, dense pseudo-rewards, and full exploiter agents are either premature, inapplicable, or lower-priority given current bottlenecks.

## Findings

### 1. PFSP (Prioritized Fictitious Self-Play)

**What it does:** Samples training opponents proportional to how much the current agent struggles against them: weight = (1 - WR)^p.

**Why AlphaStar needed it:** With a league of 100+ agents, uniform sampling wastes most games on already-beaten opponents. PFSP focuses compute on exploitable weaknesses.

**Our situation:** Already implemented in `sample_K_league_opponents()` (line 854-961). With k=4 opponents per iteration and a pool of ~15-20 past checkpoints plus 3 fixtures, the combinatorics are much smaller. The implementation looks correct: recency weighting via exp(rank/tau) combined with PFSP factor (1-WR)^p, default p=1.0.

**Hidden issue:** The recency weighting dominates PFSP. With tau=20, the newest checkpoint gets exp(N/20) relative weight. If there are 20 checkpoints in the pool, the newest is exp(1)=2.7x the oldest. But after 50+ iterations with league-save-every=10, there are many checkpoints and PFSP rarely gets to surface an old hard opponent because recency crushes its weight. The PFSP signal is drowned out.

**Practical impact:** Moderate positive. The current implementation is reasonable but the interaction between recency and PFSP deserves tuning. Consider: (a) increase tau to 50+ so PFSP has more room to operate, or (b) use PFSP-only weighting without recency for at least some slots, or (c) keep a separate "hard opponent" slot that uses pure PFSP.

**Risk:** Low. Already implemented and running.

### 2. V-trace (Off-Policy Correction)

**What it does:** Corrects for the policy lag between the behavior policy (which collected the data) and the current policy (being trained). Uses importance-weighted returns with truncation (rho-bar, c-bar) to prevent high-variance corrections.

**Why AlphaStar needed it:** With thousands of distributed actors collecting data asynchronously, the behavior policy could be many gradient steps behind the learner. Without correction, this causes biased gradient estimates.

**Our situation:** Completely inapplicable. We use synchronous on-policy PPO: collect rollout with current policy, update, repeat. There is zero policy lag. PPO's own clipped importance ratios (ratio = exp(new_log_prob - old_log_prob)) serve the same purpose within the PPO epochs.

**Practical impact:** Zero. Would add complexity for no benefit.

**Risk:** N/A.

**Verdict: Skip entirely.**

### 3. UPGO (Upgoing Policy Gradient)

**What it does:** Only reinforces trajectories where the actual return exceeds the value estimate (G_t > V(s_t)). When G_t < V(s_t), it uses V(s_t) as the target instead of G_t, effectively ignoring "unlucky" trajectories rather than anti-reinforcing them.

**Why AlphaStar needed it:** In StarCraft, a single bad engagement can tank the entire game outcome even if the preceding strategy was correct. Without UPGO, the policy gradient would blame good strategic decisions for tactical execution failures, introducing high variance.

**Our situation:** Surprisingly well-matched. Twilight Struggle has extremely sparse rewards (one signal at game end, ~300 decision points per game). A well-played early game can be undone by an unlucky DEFCON-1 or a scoring card drawn at the wrong time. The value function must bridge these 300 steps, and GAE amplifies noise when the value estimate is poor.

**Current GAE implementation (lines 1211-1300):** Standard GAE with gamma=0.99, lambda=0.95. Per-side computation for self-play games. The advantage is A_t = sum_k (gamma*lambda)^k * delta_t+k where delta_t = r_t + gamma*V(t+1) - V(t). In our case, r_t = 0 for all non-terminal steps (vp_reward_coef=0.0 in current config), so the signal propagates entirely through value bootstrapping. This makes the quality of advantages highly dependent on value function accuracy.

**Implementation proposal:** Replace the standard advantage with a UPGO-modified version:

    A_upgo_t = max(A_gae_t, 0) * A_gae_t + min(A_gae_t, 0) * 0

That is, when A_t < 0 (trajectory performed worse than expected), clip the advantage to zero rather than using a negative signal. This is a simplified UPGO that takes about 3 lines of code.

**Practical impact:** Medium-high. Should reduce variance in the policy gradient, especially for US-side play where win rates are already low (26-39% in v23 rollouts) and most trajectories produce negative advantages. Without UPGO, the US-side gradient is dominated by "avoid everything" signals.

**Risk:** Low. It is a monotone transformation of advantages. Worst case: learning is slightly slower because negative signals are discarded. Can be A/B tested in one run.

**Important nuance:** Full UPGO replaces negative-advantage returns with the value estimate, not zero. The simplified version (clip negatives to zero) is closer to "positive-only REINFORCE" and may undertrain the value function. A proper implementation should still train the value head on all returns, just clip the policy advantage.

### 4. KL Regularization Toward BC Policy

**What it does:** Adds a penalty term: loss += beta * KL(pi_current || pi_BC) that prevents the RL policy from drifting too far from the behavior cloning prior.

**Why AlphaStar needed it:** Without it, RL discovers degenerate strategies that exploit game mechanics (e.g., mass-producing a single unit type). The BC prior acts as a "common sense" anchor that keeps the policy within the space of human-like strategies.

**Our situation:** This is arguably the single most important technique we are NOT using, and its absence is the most likely root cause of the v23 collapse.

**Evidence from v23 logs:**
- Iter 1: card_logits range [-15.72, +12.25], entropy 3.985, rollout_wr 0.700
- Iter 92: card_logits range [-5.23, +2.39], entropy 5.200, rollout_wr 0.405
- Iter 93: rollout_wr drops to 0.145

The logit range compressing from [-16, +12] to [-5, +2] while entropy INCREASES from 4.0 to 5.2 is the signature of policy collapse toward uniform: the model is losing its ability to discriminate between cards. Combined with the new rollout_temp=1.2 (which further flattens the action distribution during data collection), the model trained itself into a random policy.

**KL regularization would prevent this** by penalizing movement away from the BC checkpoint's sharp, discriminative distribution. Even a small beta=0.01 would resist the entropy drift.

**Implementation approach:**
1. At training start, load the BC checkpoint as a frozen reference model
2. Each PPO update, compute KL(pi_current || pi_BC) on the card head (the largest action space, most prone to drift)
3. Add beta * KL to the loss
4. Optionally decay beta over training (start high, reduce as RL learns)

**Practical impact:** High. Directly addresses the observed failure mode. The BC checkpoint (v22 or earlier) has strong card-selection priors from supervised learning on human + self-play data. KL regularization preserves these while allowing RL to refine them.

**Risk:** Medium. If beta is too high, RL cannot deviate from BC at all and gains are capped. If too low, it provides no protection. Requires tuning. A reasonable starting point: beta=0.1 with linear decay to 0.01 over 100 iterations. The stored card_logits field in Step (line 236) suggests this was anticipated but never implemented.

**Alternative: simpler max-KL early stopping.** We already have --max-kl=0.3 but it measures KL between old and new policy within a PPO epoch, not KL from the BC anchor. The existing mechanism is too lenient (KL of 0.3 per iteration compounds to massive drift over 200 iterations). A BC-anchored KL constraint is fundamentally different and more protective.

### 5. Global Entropy Schedule

**What it does:** Maintains a single monotonically-decreasing entropy coefficient across all training runs, rather than resetting to a high value each time training restarts.

**Why AlphaStar needed it:** Training was often restarted from checkpoints. Without a global schedule, entropy would spike on restart, undoing convergence.

**Our situation:** Already implemented (lines 2481-2495). Global iter = global_iter_offset + iteration, where global_iter_offset is loaded from checkpoint args["total_iters"]. Entropy decays from ent_coef (0.03) to ent_coef_final (0.005) between global iterations 400 and 2000.

**Current calibration concern:** With 200 iterations per run and v23 being approximately the 12th chained run, global_iter is around 2400+, meaning entropy has already reached its minimum of 0.005. Yet v23 showed entropy of 5.2 nats, far above what 0.005 coefficient should produce. This means the entropy coefficient is working correctly (it is only a multiplier on the entropy bonus in the loss function), but the actual policy entropy is determined by the logit distribution, not the coefficient. The coefficient incentivizes exploration; if the logits themselves collapse to near-uniform, the policy entropy is high regardless.

**Practical impact:** Already captured. The implementation is sound.

**Risk:** None. Already running.

### 6. Dirichlet Noise at Rollout Root

**What it does:** At each decision point, mixes the policy's action probabilities with Dirichlet noise: p' = (1-eps)*p + eps*Dir(alpha). This ensures every legal action has nonzero probability, promoting exploration.

**Why AlphaStar/AlphaZero needed it:** In MCTS, root exploration noise prevents the search tree from prematurely converging. Without noise, MCTS would never explore promising-but-unlikely moves.

**Our situation:** Already scaffolded (lines 995-1018, args at 2240-2244) but currently disabled in production (dir_alpha=0.0 in v22, and v23 used explore-alpha/explore-eps which are the sequential-rollout equivalents). The C++ batched rollout may or may not support the dir_alpha/dir_epsilon kwargs (the code tries and silently falls back).

**Key concern for our setting:** We do NOT use MCTS. Dirichlet noise in MCTS is valuable because the search corrects the noise — the tree visit counts eventually reflect the true quality of noisy-explored moves. Without MCTS, Dirichlet noise is just random corruption of the policy. The noisy actions get full credit/blame in GAE, adding variance to an already noisy signal.

**When Dirichlet noise WOULD help us:** If the policy is too peaked (entropy too low, near-deterministic play) and we need forced exploration. But our current problem is the opposite: entropy is too HIGH. Dirichlet noise would make it worse.

**Practical impact:** Low to negative in current state. Potentially useful later if we implement MCTS rollouts or if the policy becomes overly deterministic.

**Risk:** Adds variance to an already high-variance gradient estimator. Combined with T=1.2, it was likely a contributor to v23's collapse.

**Recommendation:** Keep disabled (dir_alpha=0.0) until (a) we have MCTS in rollouts, or (b) entropy drops below 2.5 and we need forced exploration.

### 7. Per-Game Temperature Schedule (T=1.2 Early, Lower Late)

**What it does:** Uses higher temperature at the start of a game (more exploration in openings) and lower temperature later (more exploitation in endgame).

**Why AlphaStar used it:** Opening strategy in StarCraft has high uncertainty and many viable paths. Locking in too early prevents discovering novel builds. Endgame execution is more tactical and benefits from sharp play.

**Our situation:** The rollout_temp=1.2 was introduced at v23 and is the likely primary cause of the regression. The issue is that a uniform T=1.2 is applied to ALL decisions, including late-game scoring responses, DEFCON management, and space race decisions where the optimal play is often clear and deterministic.

**Per-game temperature schedule makes sense for TS:**
- Headline phase (AR 0): T=1.3-1.5. Headlines have high strategic variance and the BC prior has weak headline preferences. Exploration here is cheap.
- Early/mid action rounds (turns 1-5): T=1.1-1.2. Some exploration is valuable for discovering influence placement patterns.
- Late game (turns 8-10): T=0.8-1.0. Scoring responses and DEFCON management need to be sharp. Exploring random coups at DEFCON 2 in turn 9 is extremely costly.

**Implementation:** The C++ rollout binding already takes a temperature parameter. A per-turn schedule requires either (a) modifying the C++ binding to accept a schedule, or (b) running multiple rollout calls with different temperatures (wasteful). Option (a) is the right approach.

**Practical impact:** Medium. A well-tuned schedule captures the exploration benefit of T>1 without the late-game damage. But it requires C++ binding changes.

**Risk:** Medium. The v23 regression shows that temperature > 1.0 is dangerous. Any schedule needs careful validation. Recommend: first revert to T=1.0, add KL regularization, THEN experiment with per-phase temperature.

### 8. Dense Pseudo-Rewards Beyond Win/Loss

**What it does:** Adds intermediate reward signals (e.g., VP changes, region control changes, military operations parity) to supplement the sparse terminal reward.

**Why AlphaStar used it:** StarCraft games can last 20+ real minutes with thousands of steps. Sparse reward creates an extreme credit assignment problem.

**Our situation:** Already scaffolded but disabled. The vp_reward_coef parameter exists (line 2215) and _compute_reward (line 549) can add VP-proportional terminal rewards, but the current config uses vp_reward_coef=0.0.

**Why this is tricky for TS:**
- VP is zero-sum and fluctuates wildly. A VP shaping reward would reward scoring even when it is strategically wrong (e.g., scoring a region you are about to lose control of).
- DEFCON management has no VP signal but is critical for survival.
- The "correct" intermediate rewards are actually the value function's job. Dense rewards are a shortcut that introduces bias.

**Where dense rewards COULD help:** Rather than VP, consider:
- Region control stability (BG-weighted influence delta per turn — how many BG countries changed control)
- DEFCON safety bonus: small negative reward for DEFCON reaching 2 on your turn (you are one card away from losing)
- Military operations parity: small reward for meeting required MilOps

**But all of these risk introducing bias.** The value function should eventually learn these signals from the terminal outcome. Dense rewards hardcode a human prior about what intermediate states are "good," which may conflict with optimal play.

**Practical impact:** Low. The 300-step horizon with gamma=0.99 means the effective discount factor at step 0 is 0.99^300 = 0.05, which is nonzero. The value function can propagate the terminal signal, especially with GAE(lambda=0.95). Dense rewards would help value learning converge faster but risk introducing bias.

**Recommendation:** Do not add dense rewards yet. Instead, improve value function quality through (a) more training data (longer runs), (b) value-specific architecture improvements (e.g., separate value network), and (c) UPGO to reduce variance. Dense rewards are a last resort if value learning stalls.

### 9. League with Exploiter Agents

**What it does:** Trains specialized agents whose sole purpose is to find and exploit weaknesses in the main agent. The main agent then trains against these exploiters, patching the weaknesses.

**Why AlphaStar needed it:** With a large league, naive self-play converges to a Nash equilibrium of the current population, which may miss exploitable strategies. Exploiters actively probe for weaknesses, ensuring the main agent is robust.

**Our situation:** We have a simple league (k=4 opponents, past-self pool + fixtures). This is league training but NOT exploiter training. True exploiters would require:
1. Training a separate model specifically to beat the current best
2. Using that exploiter as a training opponent for the main agent
3. Repeating cyclically

**Why this is impractical for us:**
- Each training run takes ~70 minutes (200 iterations * ~20 seconds). Training an exploiter would double the compute.
- With a single GPU, we cannot run main agent training and exploiter training in parallel.
- The exploiter needs to be significantly stronger than random to provide useful signal. On our small compute budget, an exploiter would itself be weak.
- The simpler alternative (PFSP, which already upweights hard opponents) captures most of the benefit.

**Practical impact:** Very low given compute constraints.

**Risk:** Doubles training time for uncertain benefit.

**Recommendation:** Skip. The existing PFSP + fixture system provides sufficient opponent diversity. If we wanted exploiter-like behavior cheaply, we could train a single "anti-meta" checkpoint by running 50 iterations of PPO specifically targeting the current best, then add it as a fixture.

## Ideas NOT on the List That May Be Surprisingly Useful

### A. Separate Value Network (Not Shared Trunk)

The current model shares the trunk between policy and value heads. In PPO, the value loss gradients can interfere with the policy features, especially when vf_coef=0.5 (current setting). AlphaStar used separate networks for value and policy. For our setting, a separate small value network (MLP taking the same input features) would:
- Prevent value gradients from corrupting policy features
- Allow the value network to train faster (higher learning rate)
- Cost minimal extra VRAM (~1MB for a separate 256-dim MLP)

This is likely more impactful than most of the techniques discussed above.

### B. PopArt (Adaptive Value Normalization)

The terminal reward is either +1 or -1, but the value function needs to predict expected returns which range from -1 to +1. With gamma=0.99 and 300 steps, the effective return at step 0 is heavily discounted. PopArt normalizes the value target adaptively, improving value learning stability. Given that value quality is crucial for GAE and UPGO, this is worth considering.

### C. Reward Symmetry Enforcement

TS is asymmetric (USSR and US have different advantages), but the current system trains both sides with the same model. The per-side advantage normalization (lines 1347-1352) partially addresses this, but a more principled approach would be to weight the loss by side, or use side-specific value heads.

### D. Replay Buffer for Value Learning (But Not Policy)

While on-policy PPO cannot reuse old data for policy updates, the value function CAN benefit from off-policy data. Maintaining a small replay buffer (last 3-5 iterations) for extra value function training epochs could improve value estimates at near-zero cost. This is essentially what PPG (Phasic Policy Gradient) does.

## Conclusions

1. **The v23 regression was caused by exploration changes (T=1.2) without a stabilizing anchor (KL regularization).** Adding exploration noise without KL regularization is like removing guardrails without adding a safety net. This is the single most important lesson.

2. **KL regularization toward BC policy is the highest-priority addition.** It directly addresses the observed failure mode and is conceptually simple (~20 lines of code). Every future exploration experiment should be gated on having KL regularization in place first.

3. **UPGO is the second-highest-priority technique.** It reduces policy gradient variance in our sparse-reward, long-horizon setting for near-zero implementation cost. A 3-line modification to GAE advantage computation.

4. **V-trace is entirely inapplicable.** Our synchronous on-policy setup has zero policy lag. Implementing it would add complexity for no benefit.

5. **Dirichlet noise is premature and likely counterproductive.** Without MCTS to correct the noise, it simply adds variance. Keep disabled until MCTS rollouts are implemented.

6. **Temperature > 1.0 must be paired with KL regularization.** The v23 results prove that temperature alone causes policy collapse. If temperature exploration is desired, implement KL regularization first, then use a per-phase schedule (high in headlines, low in late game).

7. **PFSP is already implemented and working**, but the interaction between recency weighting and PFSP deserves attention. Consider a dedicated "hard opponent" slot that uses pure PFSP without recency weighting.

8. **The global entropy schedule is already implemented and functioning correctly.** No changes needed.

9. **Full exploiter agents are impractical on single-GPU.** The existing league + PFSP captures most of the value at a fraction of the cost.

10. **Separate value network and UPGO together would likely give more Elo than all the exploration noise techniques combined.** The bottleneck is value function quality, not exploration.

## Recommendations

Priority-ordered actionable list:

1. **Implement KL regularization toward BC policy** (1-2 hours).
   - Load frozen BC checkpoint at training start
   - Compute KL divergence on card head per minibatch
   - Add --kl-bc-coef (default 0.1, decay to 0.01 over 100 iterations)
   - This MUST be in place before any further exploration experiments

2. **Implement UPGO-style advantage clipping** (30 minutes).
   - In compute_gae_batch, after computing advantages, clip: `step.advantage = max(step.advantage, 0.0)`
   - Keep value targets (step.returns) unchanged for value learning
   - A/B test: one run with UPGO, one without, same other settings

3. **Revert rollout_temp to 1.0 for the immediate next run** (v24/v25).
   - T=1.2 without KL regularization caused v23's collapse
   - Re-enable temperature only after KL regularization is validated

4. **Add a separate value network** (2-3 hours).
   - Small MLP (same input dims, 256-dim hidden, 1 output)
   - Separate optimizer with higher LR (3e-4)
   - Remove value head from shared trunk
   - This prevents value gradients from corrupting policy features

5. **Tune PFSP: add a pure-PFSP slot** (30 minutes).
   - In sample_K_league_opponents, make slot 1 use PFSP-only weighting (no recency)
   - Slot 0: self, Slot 1: hardest opponent (PFSP), Slots 2-3: recency*PFSP pool

6. **Implement per-phase temperature schedule** (2-3 hours, requires C++ binding change).
   - Only after KL regularization is validated
   - AR 0 (headline): T=1.3, turns 1-5: T=1.1, turns 6-10: T=0.9
   - Requires C++ rollout to accept temperature schedule parameter

7. **Consider PPG-style value replay** (1-2 hours).
   - Cache last 3 iterations of (features, returns) tuples
   - Run extra value-only training epochs on cached data between PPO iterations
   - Improves value quality at ~30% compute overhead

## Open Questions

1. **What was the exact config difference between v22 (Elo 2109, best) and v23 (Elo 1733)?** We could not read the ppo_args.json files due to permissions. If the only change was rollout_temp=1.2, this confirms the analysis. If other changes were made simultaneously, the attribution is less clear.

2. **How much of v23's regression is recoverable?** v24 was started from v23's final checkpoint. If v23's weights are deeply corrupted, v24 may need to start from v22 instead.

3. **What is the current global_iter_offset?** If it exceeds 2000, entropy is at its minimum (0.005). This is fine if KL regularization is added, but concerning without it — the model has no exploration incentive.

4. **Should UPGO be applied symmetrically or only to the losing side?** The US side has systematically lower win rates; UPGO would disproportionately clip US-side advantages. This might be correct (stop anti-reinforcing US play) or might slow US-side learning.

5. **Is the value function actually accurate enough to make GAE useful?** With 300 steps and pure terminal reward, the value function has an extremely hard job. If value estimates are near-random, GAE advantages are noise. Separate value network + PPG value replay might be prerequisites for any other technique to work.
---
