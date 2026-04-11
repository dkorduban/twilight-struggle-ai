---
# Opus Analysis: Auxiliary State Prediction Head
Date: 2026-04-11T12:15:00Z
Question: Should we add an auxiliary head that predicts game state after the current turn to help the model learn engine mechanics and abstract choice effects?

## Executive Summary

An auxiliary state-prediction head is a theoretically sound idea with genuine potential to improve credit assignment and sample efficiency, but for this project it is **premature and likely net-negative right now**. The value head already provides a compressed summary of future state; the SmallChoiceHead (just completed) and the upcoming CountryAllocHead DP upgrade are more direct, lower-risk ways to improve cause-effect reasoning for the specific decisions where it matters most. If pursued at all, a lightweight "delta-scalar" variant (predicting VP/DEFCON/space changes, not the full influence map) would be the right starting point -- but only after the Phase 2-3 pragmatic heads are landed and benchmarked.

## Findings

### 1. What the model currently sees and predicts

The trunk ingests three feature groups:
- **Influence** (172 floats): per-country influence for both sides (86 x 2)
- **Cards** (448 floats): 4 binary masks (known-in-hand, possible, discard, removed) x 112 card slots
- **Scalars** (32 floats): VP, DEFCON, milops, space, turn/AR, china, 17 active-effect booleans, chernobyl, ops modifiers

The model produces:
1. `card_logits` (111) -- which card to play
2. `mode_logits` (5) -- influence/coup/realign/space/event
3. `country_logits` (86) -- where to place ops (mixture-of-softmaxes, K=4)
4. `value` (1) -- game outcome prediction (tanh, [-1,1])
5. `small_choice_logits` (8) -- event-level binary/option decisions (Phase 1, just completed)

Hidden dim is 256, total model is roughly ~500K parameters. The trunk is 2 residual blocks.

### 2. What "next state" means in Twilight Struggle

This is the crux of the difficulty. TS decisions are highly heterogeneous:

- **Influence placement**: 1-4 ops spread across countries. The next state is deterministic given the allocation -- influence[c] += 1 for each op.
- **Coups**: stochastic (die roll determines influence swing). Next state is a distribution, not a point.
- **Realignment**: even more stochastic (die roll per attempt, variable number of targets).
- **Events**: hugely varied -- some are deterministic board changes (Marshall Plan adds influence), some are stochastic (war cards roll dice), some involve opponent decisions (Olympic Games boycott), some chain into sub-decisions.
- **Space race**: deterministic (advance space track, consume card).

The "state after current turn" is even harder to define because a turn consists of 7-8 action rounds per side (14-16 total decisions), plus headlines. The model sees one decision at a time. Predicting end-of-turn state from a single decision is asking the model to predict the cumulative effect of ~15 future decisions it hasn't made yet -- that is almost entirely noise from the perspective of the current step.

**More tractable**: predicting the "state after this single action resolves" (immediate next state). This is well-defined but has complications:
- For influence placement: trivially deterministic -- the model would just learn to add 1s to the target countries. This is not a useful learning signal because the model already outputs those country targets.
- For coups/realignment: stochastic, so you'd need to predict expected next state or a distribution.
- For events: the "next state" often depends on the event's internal sub-decisions (which region to block for Chernobyl, which countries for Socialist Governments, etc.). Many of these are currently resolved randomly by the engine.

### 3. Literature context

**MuZero** uses a learned dynamics model to predict next latent state for planning. This works because: (a) the dynamics model enables multi-step lookahead without a simulator, (b) it is trained on complete trajectories, and (c) the games (Go, chess, Atari) have simpler state spaces. In our case, we have an exact C++ simulator -- we don't need a learned dynamics model for planning. MCTS already uses the real engine.

**UNREAL (Jaderberg et al., 2017)** adds auxiliary tasks (reward prediction, pixel control) to improve representation learning. The key insight is that these tasks provide dense gradients for the trunk, especially when the main RL signal (rewards) is sparse. This is the strongest analogy to our case.

**VICReg, BYOL, and other self-supervised methods** in RL learn representations by predicting future observations. Again, valuable when the main signal is sparse.

**Key question**: Is the PPO signal sparse enough to justify auxiliary tasks? In our setup:
- PPO provides gradients to every head at every step (card, mode, country, value all get gradients).
- The value head already provides a dense gradient signal through GAE advantages.
- SmallChoice head provides direct supervision for event decisions.
- The main bottleneck (identified in `plan_pragmatic_heads.md`) is that ~60% of event decisions are random -- this is an *action expressiveness* gap, not a *representation learning* gap.

### 4. Data availability analysis

**PPO rollouts**: Steps are collected sequentially within each game, with `boundaries` marking game start/end. Each step stores raw state (`raw_ussr_influence`, `raw_us_influence`, `raw_vp`, `raw_defcon`, etc.). To build next-state targets, you would pair step[i] with step[i+1]'s raw state (within the same game boundary). This is feasible -- the data is already there.

**BC data (Parquet)**: Has `game_id` and `step_idx` columns, plus full state at each step. Pairing consecutive steps within a game is straightforward via Polars.

So data collection is not a blocker -- next-state labels can be derived from existing sequential data without engine changes.

### 5. Compute cost estimate

The auxiliary head would add:
- **Influence prediction** (172 outputs): `Linear(256, 172)` = 44K params, ~44K FLOPs per sample.
- **Scalar prediction** (VP, DEFCON, space, milops = ~10 values): `Linear(256, 10)` = 2.6K params, negligible.
- **Full state prediction** (172 + 10 = 182 outputs): ~47K params total.

This is ~10% of the current model size. The forward/backward cost increase would be modest (~5-8% wall time) since the trunk computation dominates. The real cost is in:
1. Building and maintaining the target pipeline (pairing consecutive steps, handling game boundaries, handling stochastic events)
2. Hyperparameter tuning (auxiliary loss weight)
3. Risk of destabilizing training (gradient competition between heads)

### 6. The gradient competition risk

This is the most serious concern. With hidden_dim=256 and already 5 heads competing for trunk capacity:

- Card head: policy-critical, needs to understand hand composition and game phase
- Mode head: policy-critical, needs to understand strategic context
- Country head: policy-critical, needs to understand board position
- Value head: already learns a compressed representation of future state
- SmallChoice head: policy-critical for event decisions

Adding a state-prediction head creates a 6th gradient source pulling on the 256-dim trunk. The state-prediction task is inherently easier than policy (just memorize the dynamics model) but produces much larger gradients (172 MSE outputs vs 1 value output). Without careful loss weighting, the trunk could shift toward being a good state predictor at the expense of being a good policy network.

The UNREAL paper mitigated this by using separate sub-networks for auxiliary tasks rather than sharing the full trunk. A compromise would be a detached auxiliary branch (trunk -> stop_gradient -> aux_branch -> state_pred), but this defeats the purpose of improving trunk representations.

### 7. What the value head already captures

The value head `v(s) = E[G | s]` is mathematically the optimal compression of all future states into a scalar. If the trunk representation is good enough to predict v(s) accurately, it already encodes the information needed to distinguish states that lead to different outcomes. The question is whether v(s) gradients alone are sufficient to learn this representation.

In practice, the value function is a very "lossy" compression. It maps fundamentally different future trajectories to similar values (e.g., "winning via Europe scoring" vs "winning via VP track" might have similar v(s) but very different intermediate states). An auxiliary state-prediction head would force the trunk to preserve these distinctions. However, if the policy heads don't need these distinctions to make good decisions, the auxiliary signal is wasted.

### 8. Where auxiliary prediction would genuinely help

The strongest case for state prediction is for **event decisions** where the model currently struggles:

- **Chernobyl region selection**: The "right" region to block depends on understanding what the opponent's influence placement would look like in each region over the next few ARs. A state-prediction head trained on "what does the board look like after this turn" could help the trunk learn regional influence dynamics.
- **Warsaw Pact (add vs remove)**: The downstream effect depends on Europe scoring likelihood and current Europe control. State prediction could help encode this.
- **Summit DEFCON direction**: Understanding DEFCON trajectory matters here.

But all of these are SmallChoice decisions (Phase 1), and the SmallChoice head with PPO advantage signal already provides a direct learning pathway for these decisions. The auxiliary head would be an indirect, roundabout way to achieve what SmallChoice + PPO already does directly.

### 9. A lighter alternative: "state-delta" auxiliary

Instead of predicting the full next state, predict only the **change** in key scalars:
- delta_vp (how much VP changes this action)
- delta_defcon (DEFCON change)
- delta_milops (milops change per side)
- any_country_flipped (binary: did control of any country change)

This is ~5 outputs, negligible compute, and directly encodes cause-effect without the noise of predicting 172 influence values. The targets are easy to compute from consecutive steps. But even this has limited value: the policy heads already implicitly learn these relationships through the advantage signal.

### 10. Timing and priority assessment

From `plan_pragmatic_heads.md`, the current priority stack is:
1. Phase 1 SmallChoiceHead -- COMPLETE
2. Phase 2 CountryAllocHead DP upgrade -- 1-2 weeks
3. Phase 3 Event Country Targets via PolicyCallback -- 2-4 weeks
4. Phase 4 CardHead Extensions -- 1 week

The v44-v46 plateau at Elo ~2106 is attributed to architecture bottleneck (action expressiveness), not representation quality. Adding an auxiliary state-prediction head does not address this bottleneck. Phases 2-3 directly address it.

The RTX 3050 (4GB VRAM) is already tight. Adding a state-prediction head with full influence targets would increase memory footprint during training by ~10-15%, which could force smaller minibatches.

## Conclusions

1. **The idea is theoretically sound but practically premature.** Auxiliary state prediction is well-established in the RL literature (UNREAL, MuZero, dreamer) but solves a problem this project does not currently have -- sparse learning signal. PPO + GAE + 5 heads already provides dense gradients.

2. **The main bottleneck is action expressiveness, not representation quality.** The Elo plateau is caused by 60% of event decisions being random (not learned). Phases 2-3 of the pragmatic heads plan directly address this. An auxiliary head does not.

3. **The value head already serves as a compressed state predictor.** Adding explicit state prediction risks gradient competition for the 256-dim trunk without proportional benefit to policy quality.

4. **Predicting "end of turn" state from a single decision is ill-posed.** A turn has ~15 decisions; the current step's contribution to end-of-turn state is small relative to the noise from all other decisions. Predicting "immediate next state" is better-defined but trivially deterministic for influence placement (the dominant action type).

5. **Coup and event stochasticity complicates target construction.** For stochastic actions, the "next state" is a sample from a distribution, not a deterministic target. MSE loss on a single sample is a noisy signal that may hurt more than it helps.

6. **Data infrastructure is not a blocker.** Both PPO rollouts and BC Parquet data contain sequential state information sufficient to construct next-state targets without engine changes.

7. **If pursued, the "delta-scalar" variant is the right entry point.** Predicting 5-10 scalar changes (VP, DEFCON, milops, space) is cheap, well-defined, and avoids the stochasticity problem for most action types. But even this should wait until after Phase 2-3 heads are landed.

8. **Memory is a real constraint.** The RTX 3050 (4GB) is already tight for PPO training. Full influence prediction (172 outputs + loss computation) would measurably increase memory pressure.

## Recommendations

1. **Do not implement now.** Focus on Phase 2 (CountryAllocHead DP upgrade) and Phase 3 (Event Country Targets) which directly address the Elo plateau.

2. **Revisit after Phase 3 if another plateau is hit.** If Elo plateaus again after Phases 2-3 give the model full event decision authority, a representation quality bottleneck becomes more plausible and auxiliary tasks would be worth testing.

3. **If revisited, start with delta-scalar variant.** Predict [delta_vp, delta_defcon, delta_milops_ussr, delta_milops_us, delta_space_ussr, delta_space_us] as a 6-output head. Use very low loss weight (0.01-0.05x policy loss). Run an A/B benchmark (200 games) before committing.

4. **If the full influence variant is ever tried, use a detached branch.** Route trunk output through a `stop_gradient` before the auxiliary branch so the state-prediction gradients don't compete with policy gradients for trunk capacity. This turns it into a diagnostic tool (measuring representation quality) rather than a training signal.

5. **Monitor value loss convergence as a proxy.** If value loss is high and not converging, that suggests the trunk representation is poor and auxiliary tasks might help. Current value loss trends should be checked on W&B before investing in auxiliary heads.

## Open Questions

1. What is the current value loss on recent PPO iterations? If it is already converging well, auxiliary state prediction is unlikely to help representation quality.

2. Has anyone measured the trunk's "state decodability" -- i.e., can a linear probe on the trunk hidden state predict VP, DEFCON, etc.? If yes, the trunk already encodes state well and auxiliary heads are redundant. If no, auxiliary heads might help.

3. For the SmallChoice decisions (Warsaw Pact, Olympic Games, etc.), how quickly does the model learn good policies through PPO alone? If it converges fast, there is no need for auxiliary signal. If it plateaus, auxiliary state prediction might provide the missing gradient.

4. Would a simple "influence delta" head (predict which countries change influence this step) be more useful than predicting the absolute next state? Deltas are sparser and more informative per bit.
---
