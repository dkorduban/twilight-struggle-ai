---
# Opus Analysis: DEFCON Penalty and Probabilistic Risk-Taking
Date: 2026-04-13T18:35:00Z
Question: Does -1.5 penalty correctly handle rational probabilistic DEFCON risks?

## Executive Summary

The -1.5 DEFCON-1 penalty does NOT currently suppress rational probabilistic risk-taking, but for a surprising reason: **the learned policy is hard-masked from couping at DEFCON <= 2** (train_ppo.py line 472-473), so the classic "BG coup at DEFCON 2 with 1/7 suicide chance" scenario is impossible for the model. The actual DEFCON-1 losses (~6% of games) come from a different mechanism -- playing opponent cards for ops where the mandatory opponent event indirectly lowers DEFCON (e.g., Junta, ABM Treaty chaining into a BG coup via apply_ops_randomly). For these indirect cases, the 1/7 probability framing doesn't apply cleanly because the DEFCON-lowering is a side effect of the opponent's event resolution, not a direct die roll the model chose.

The analysis reveals three distinct problems:

1. **The hard coup mask at DEFCON 2 is overly conservative.** In real Twilight Struggle, BG coups at DEFCON 2 are legal and sometimes optimal. The mask eliminates a legitimate strategic option, which is a larger distortion than any reward shaping could cause.

2. **For the indirect DEFCON-1 cases that DO occur, the -0.5 extra penalty creates a distortion of ~0.036-0.071 expected reward** (depending on the probability of the dangerous event chain). This is small but non-negligible and systematically biases against playing opponent cards at low DEFCON -- even when the expected position gain from the ops is high.

3. **GAE credit assignment is adequate but not precise.** The terminal -1.5 reward propagates backward through the entire same-side trajectory, so earlier hand-management decisions receive some gradient. However, there is no step-level signal isolating the specific card-play that triggered the event chain, which means credit is smeared across ~20-40 decisions.

**Net assessment:** The coup mask is a bigger problem than the reward penalty. If the mask were relaxed (allowing BG coups at DEFCON 2), THEN the -1.5 penalty would become a material concern for rational risk-taking. Under the current mask, the penalty's main effect is mild over-penalization of indirect event chains -- a second-order issue.

## Findings

### EV Calculation: Risky Move vs Safe Move

Consider the canonical scenario: model plays a BG coup at DEFCON 2, with probability p of DEFCON lowering to 1 (suicide) and (1-p) of a strong position gain.

For a BG coup, DEFCON always drops by 1 unless Nuclear Subs is active (US only). So on a battleground target at DEFCON 2, p = 1.0 (certain suicide), not 1/7. The 1/7 framing would apply if DEFCON lowering were probabilistic (e.g., only on certain die rolls), but in TS rules, BG coups ALWAYS lower DEFCON. This is why the hard mask exists.

**However**, the 1/7-like probability DOES apply to indirect cases:

- Model plays opponent's card (e.g., card X) for ops at DEFCON 2
- Opponent event fires first (mandatory)
- Event calls apply_ops_randomly, which may or may not coup a BG
- Probability of BG coup depends on the event's random target selection

For these cases, let p = probability that the event chain lowers DEFCON to 1.

**EV with -1.5 penalty:**
```
E[R] = (1-p) * EFV + p * (-1.5)
```

**EV with -1.0 baseline penalty:**
```
E[R_base] = (1-p) * EFV + p * (-1.0)
```

**Distortion:**
```
Delta = E[R] - E[R_base] = p * (-0.5)
```

For p = 1/7: Delta = -0.071
For p = 1/14: Delta = -0.036
For p = 1/3: Delta = -0.167

**Threshold where E[R] flips sign (model should take the risk but penalty says no):**

With -1.5: E[R] = 0 when EFV = 1.5 * p / (1-p)
With -1.0: E[R] = 0 when EFV = p / (1-p)

| p    | Threshold (-1.5) | Threshold (-1.0) | Gap      |
|------|-------------------|-------------------|----------|
| 1/7  | 0.250             | 0.167             | 0.083    |
| 1/5  | 0.375             | 0.250             | 0.125    |
| 1/3  | 0.750             | 0.500             | 0.250    |
| 1/2  | 1.500             | 1.000             | 0.500    |

**Interpretation:** For p=1/7, the model needs EFV > 0.250 to justify the risk with the -1.5 penalty, vs EFV > 0.167 with -1.0. The gap of 0.083 means there is a narrow band of positions where the move is +EV under the true game but -EV under the shaped reward. This band exists but is narrow.

### GAE Credit Assignment

The current GAE implementation (train_ppo.py:1534-1574) computes advantages per side independently in self-play:

1. Only the LAST step for each side carries the terminal reward
2. All intermediate steps have reward = 0
3. GAE propagates backward: `delta = gamma * next_value - value` for non-terminal steps

This means the -1.5 terminal reward enters the advantage calculation at the last step as `delta = -1.5 - V(s_last)`. Through GAE's backward pass with lambda=0.95 and gamma=0.99, this signal decays as `(gamma * lambda)^k` per step backward.

For a typical game with ~30 model decisions, the DEFCON-1 penalty signal at the action that caused it (say, 5 steps before game end) is attenuated by factor `(0.99 * 0.95)^5 = 0.941^5 = 0.735`. At 15 steps back: `0.941^15 = 0.395`. At 25 steps back: `0.941^25 = 0.213`.

**Key insight:** The specific card-play that triggered the DEFCON-lowering event chain receives a meaningful but diluted signal. It is NOT isolated -- neighboring decisions receive similar gradient magnitude. This is fundamentally a limitation of trajectory-level reward with GAE, not specific to the penalty magnitude.

**UPGO interaction:** When --upgo is enabled, the advantage becomes `G_t = r_t + gamma * max(V(s+1), G(t+1))`. For a trajectory ending in -1.5, UPGO propagates backward using max(V, G). If the value estimates along the trajectory are higher than the realized -1.5 return, UPGO CLAMPS the advantage at V(s)-V(s) = 0 for most earlier steps, concentrating the negative signal on the steps closest to the terminal loss. This actually IMPROVES credit assignment for DEFCON-1 losses -- the penalty is more concentrated on the decisions that directly led to the loss rather than smeared across the whole game.

### The Distortion Magnitude

The distortion from -1.5 vs -1.0 has three components:

**1. Direct EV distortion on the risky action:**
- For indirect DEFCON-lowering with p~1/7: -0.071 per game where this decision is faced
- Frequency: ~6% of games end in DEFCON-1, and perhaps half involve an indirect chain = ~3%
- Population-level distortion: 0.03 * 0.071 = 0.002 expected reward per game
- This is negligible for overall training dynamics

**2. Value function bias:**
- The value head learns E[R] from states. States where indirect DEFCON-1 is possible get slightly depressed values
- This is actually CORRECT -- those states ARE slightly worse with the penalty
- The bias is self-consistent: value, advantage, and policy all reflect the shaped reward

**3. Policy distortion (the real concern):**
- In states where the model faces a choice between:
  (a) Play opponent card for ops (risk of indirect DEFCON-1) with high ops value
  (b) Play a weaker card for ops (no DEFCON risk) with lower ops value
- The -0.5 extra penalty pushes toward (b) more than the true game rewards warrant
- This is the regime where the penalty causes suboptimal play

### When Rational Risk-Taking Is Suppressed

**Current system (hard coup mask):** The learned model CANNOT coup at DEFCON 2, period. This is a binary suppression of a legal action, far more distorting than any reward shaping. A model that cannot coup at DEFCON 2 loses a critical strategic tool:

- Mid-war: opponent controls key BG countries. You need to coup to contest. DEFCON is at 2. In real TS, you weigh the coup's strategic value against the guaranteed DEFCON-1 loss. Wait -- BG coups at DEFCON 2 are CERTAIN to lower DEFCON (unlike the 1/7 framing). So the only rational reason to coup at DEFCON 2 would be if you're already losing badly enough that the coup-then-win chance outweighs the certain DEFCON-1 loss. But DEFCON-1 loss is always a loss for the phasing player, so this is never rational.

**Correction to the task's premise:** The 1/7 framing is actually not about direct BG coups. A BG coup at DEFCON 2 is 100% guaranteed to lower DEFCON to 1 (for non-US-with-Nuclear-Subs). The probabilistic cases are:

1. **Indirect event chains:** Play opponent card for ops, event randomly coups a BG. Probability varies by card/state.
2. **Non-BG coups at DEFCON 2:** Legal and don't lower DEFCON. Not a risk scenario.

So the task's "1/7 chance of DEFCON-1 suicide" maps to indirect event chains, not direct coups. For these:

**Regime where penalty suppresses good play:**
- Model is behind by 5+ VP in turn 8-9
- Best available ops card is an opponent card with a dangerous event
- The ops from this card provide 4 ops in a critical region (high EFV ~0.3-0.5)
- Alternative is a 1-2 ops neutral card (low EFV ~0.0-0.1)
- Probability of DEFCON-1 from the event chain: p ~0.15

With -1.5: E[R_risky] = 0.85 * 0.4 + 0.15 * (-1.5) = 0.340 - 0.225 = 0.115
With -1.0: E[R_risky] = 0.85 * 0.4 + 0.15 * (-1.0) = 0.340 - 0.150 = 0.190
E[R_safe] = 0.05 (weak card, still behind)

Both penalties correctly favor the risky play in this scenario. The penalty would flip the decision only if:
```
(1-p)*EFV + p*(-1.5) < E[R_safe] < (1-p)*EFV + p*(-1.0)
```

For p=0.15: the risky play becomes wrong under -1.5 but right under -1.0 when:
```
E[R_safe] is between (0.85*EFV - 0.225) and (0.85*EFV - 0.15)
```

This is a window of width 0.075. For this window to matter, E[R_safe] must fall in it, which requires a specific combination of EFV and E[R_safe]. This is possible but represents a minority of game states.

### Regime Analysis (lead vs behind)

**When ahead (VP > 0, comfortable position):**
- EFV of risky play is moderate (~0.3-0.6, likely to win anyway)
- EFV of safe play is also moderate (~0.2-0.5)
- Penalty favors safe play slightly more than baseline
- This is CORRECT behavior: when ahead, avoid unnecessary risk
- The -0.5 extra penalty aligns with good TS strategy here

**When behind (VP < -5, turn 8+):**
- EFV of risky play might be the ONLY positive option
- EFV of safe play might be negative (likely to lose anyway)
- If E[R_risky] > E[R_safe] under both penalty schemes, no distortion
- The penalty only distorts when the risky play is MARGINALLY better
- In desperate positions, risky plays tend to be SUBSTANTIALLY better, so the -0.5 rarely flips the decision

**When neutral (close game):**
- This is where the penalty has the most potential for distortion
- Both plays have moderate EFV
- The -0.5 might push toward slightly suboptimal conservative play
- But the signal is small (~0.071 for p=1/7) relative to typical advantage magnitudes

**Quantitative regime analysis:**

Advantage magnitudes in PPO are typically normalized to mean=0, std=1 per side. The -0.5 penalty distortion translates to approximately:
```
Advantage distortion = 0.5 * p * (gamma*lambda)^k / sigma_adv
```
Where k is steps from terminal and sigma_adv ~1.0 after normalization.

For the specific risky action (k~3-5 steps from end): distortion ~ 0.5 * 0.15 * 0.82 / 1.0 ~ 0.06 standard deviations. This is very small -- well within the noise of typical advantage estimates.

## Conclusions

1. **The -1.5 penalty does NOT currently suppress rational risk-taking in any significant way.** The hard coup mask at DEFCON 2 (train_ppo.py:472-473) is a far larger restriction on DEFCON-related risk-taking than the reward penalty. The penalty only affects indirect event chains, where the distortion magnitude (~0.036-0.071) is small relative to advantage normalization noise.

2. **The "BG coup at DEFCON 2 with 1/7 suicide chance" scenario is based on a rules misunderstanding.** BG coups at DEFCON 2 are not probabilistic -- they deterministically lower DEFCON to 1. The only probabilistic DEFCON-1 risks come from indirect event chains (opponent events that randomly coup battlegrounds). The 1/7 probability is not a universal constant; it varies by card and board state.

3. **The hard coup mask is more strategically distorting than the reward penalty.** Banning coups at DEFCON 2 removes a legal (if rarely optimal) action from the model's repertoire. In the rare cases where couping at DEFCON 2 makes sense for a non-US player (it essentially never does, since it's a guaranteed loss), the mask prevents it entirely. For the US with Nuclear Subs, the mask is incorrect -- Nuclear Subs prevents DEFCON drop from US coups, so couping at DEFCON 2 is safe.

4. **GAE credit assignment adequately handles the penalty magnitude.** The terminal reward propagates backward with exponential decay, and UPGO (when enabled) concentrates the signal on the decisions closest to the terminal loss. The -0.5 extra does not create qualitatively different credit assignment -- it simply amplifies the existing gradient by ~50% at the terminal step.

5. **The distortion band where the penalty flips a rational decision is narrow and rare.** For p=1/7, the EFV band where -1.5 makes a play look negative but -1.0 makes it look positive is only 0.083 wide. Given that typical decision EFV differences are much larger in TS (coup vs influence is often a 0.3+ EFV gap), this band is rarely occupied.

6. **The penalty is directionally correct: it makes the model slightly more conservative about DEFCON risk, which is good play in most positions.** Only in desperate positions (down 5+ VP late) would a more risk-neutral reward be better, and in those positions the EFV gap between risky and safe plays is large enough that the penalty doesn't flip the decision.

7. **For the US side with Nuclear Subs active, the hard coup mask is a bug.** Nuclear Subs prevents DEFCON lowering from US coups, so US should be able to coup BGs at DEFCON 2 freely when Nuclear Subs is active. The mask at line 472 does not check for Nuclear Subs.

## Recommendations

1. **Keep the -1.5 penalty as-is.** The distortion is small, directionally correct, and dominated by other factors (hard mask, advantage normalization noise). No reward change needed.

2. **Fix the coup mask to account for Nuclear Subs.** Change line 472-473 to:
   ```python
   if defcon <= 2 and not (side == "US" and nuclear_subs_active):
       mode_mask[MODE_COUP] = False
   ```
   This is a correctness fix, not a risk-tolerance tuning. The US with Nuclear Subs should be able to coup BGs at any DEFCON level.

3. **Do NOT relax the general coup mask at DEFCON 2.** For non-Nuclear-Subs situations, BG coups at DEFCON 2 are guaranteed suicide. The mask is correct to block them. The model has no reason to learn this the hard way through reward signal.

4. **If future analysis shows the model avoids playing high-ops opponent cards at low DEFCON excessively**, investigate the indirect event chain penalty as a possible cause. The diagnostic would be: compare card-play frequency for high-ops opponent cards at DEFCON 2-3 vs DEFCON 4-5, controlling for hand composition.

5. **Consider adding per-step DEFCON shaping as a complement** (not replacement) to the terminal penalty. A small negative reward (-0.05 to -0.1) when DEFCON drops from 3 to 2 on the model's action would provide earlier, more targeted signal than relying solely on terminal reward backpropagation.

6. **Track DEFCON-1 losses by triggering card and event chain** to build an empirical picture of which indirect paths are most common. This data would inform whether the DEFCON_LOWERING_CARDS set needs expansion (a WS6 deliverable).

## Open Questions

1. **How often does Nuclear Subs + DEFCON 2 arise in self-play?** If the US model never encounters this state, the mask bug (conclusion 7) is cosmetic. If it's common, it's a real strategic handicap for the US side.

2. **What is the empirical frequency of indirect DEFCON-1 chains by card?** The prior analysis gives ~6% overall, but breaking this down by triggering card would reveal whether 2-3 cards dominate or if it's spread across many.

3. **Does the UPGO variant meaningfully change the penalty's effect?** Theory suggests UPGO concentrates the negative signal closer to the terminal action, which would reduce smearing but also reduce the beneficial backward propagation to earlier hand-management decisions.

4. **Is there a position-dependent penalty that would be strictly better?** E.g., penalty = -1.0 - 0.5 * max(0, model_vp_advantage / 20). This would impose the full -1.5 when ahead (don't risk it) but relax to -1.0 when behind (take calculated risks). However, this adds complexity for marginal benefit given the small distortion magnitude.

5. **Should the coup mask be replaced by the reward penalty entirely?** Instead of hard-masking coups at DEFCON 2, allow them but let the -1.5 penalty teach the model they're almost always bad. This would be more principled (the model learns the cost rather than having it hidden) but would increase DEFCON-1 rates during training, slowing convergence. Not recommended for the current training phase.
---
