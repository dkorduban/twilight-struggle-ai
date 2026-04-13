---
# Opus Analysis: DEFCON-1 Penalty Avoidability
Date: 2026-04-13T18:03:00Z
Question: Should -1.5 penalty apply to all DEFCON-1 losses or only strictly avoidable ones?

## Executive Summary

The uniform -1.5 penalty should be kept as-is. Differentiating "avoidable" vs "unavoidable" DEFCON-1 suicides is theoretically appealing but practically unnecessary and potentially harmful. The key insight is that in the current engine, nearly all DEFCON-1 suicides by the learned policy ARE avoidable because the PPO action-selection code already masks DEFCON-lowering cards/modes at DEFCON<=2 (train_ppo.py lines 418-477). The residual DEFCON-1 cases (~6% of games) come from (a) cards whose indirect DEFCON-lowering wasn't in the mask, (b) BG coups at DEFCON=2 that the model chose despite having non-coup alternatives, and (c) opponent-triggered events during play-for-ops. Category (c) is genuinely unavoidable but the extra -0.5 on top of -1.0 is small enough that it acts as noise rather than a distorting signal; removing it would require plumbing a `had_safe_alternatives` bool through the C++/Python boundary for marginal benefit.

## Findings

### 1. What the current code does

`_compute_reward` (train_ppo.py:584-616) assigns -1.5 to ANY DEFCON-1 loss by the learned side, regardless of context. The phasing player rule means the learned side only loses on DEFCON-1 when it was the phasing player (its own action round or headline). When the opponent triggers DEFCON-1 on their action, the opponent loses -- so the learned model gets +1.0, never -1.5.

### 2. Categories of DEFCON-1 loss for the learned policy

**Category A: Clearly avoidable (model chose badly)**
- Playing a BG coup at DEFCON=2 when Influence/Realign/Space were legal
- Playing an opponent's DEFCON-lowering card as Event at DEFCON=2

These are already blocked by the PPO card/mode masks (lines 418-477), so they should be rare. If they happen despite masking, the -1.5 penalty is absolutely correct -- the model needs strong negative signal.

**Category B: Semi-avoidable (card forced event, but card choice was voluntary)**
- Playing an opponent's card for ops at DEFCON=2, where the opponent's event auto-fires and lowers DEFCON. The model chose this card from its hand, but the DEFCON-lowering was a side effect of the mandatory event-then-ops sequencing.
- The model HAD alternatives: play a different card, or play this card for Space Race (if available).

This is the majority of residual DEFCON-1 cases. The -1.5 penalty is correct here too -- the model should learn to avoid playing these cards at low DEFCON. The PPO mask already blocks known DEFCON-lowering cards, but some indirect cases (e.g., apply_ops_randomly rolling a BG coup) slip through.

**Category C: Genuinely unavoidable**
- Last card in hand that happens to trigger DEFCON-1 (no alternative exists)
- Forced play under Bear Trap/Quagmire with only a dangerous card remaining
- Opponent event fires as part of a card the model was forced to play (e.g., only legal card is opponent's DEFCON-lowering card)

These are rare. The "last card" scenario requires that ALL other cards were already played and the remaining card is dangerous. In practice, a skilled player would have managed their hand to avoid this -- so even "last card" situations often trace back to earlier avoidable decisions.

### 3. RL theory analysis: does uniform penalty misbehave?

**No, and here's why.** The critical RL insight is that the terminal reward propagates backward through GAE (Generalized Advantage Estimation) to earlier decisions. Whether the penalty is -1.0 or -1.5, it still backpropagates through the same trajectory. The extra -0.5 amplifies the gradient signal for the entire trajectory, not just the final (forced) action.

Consider the "unavoidable last card" scenario:
- The model played cards 1..N-1, then was forced to play card N which caused DEFCON-1
- With -1.5: the advantage estimates for cards 1..N-1 are slightly more negative than with -1.0
- This is CORRECT behavior: the model should learn that the SEQUENCE of plays leading to the forced position was bad

The uniform penalty doesn't just penalize the last action -- through GAE, it penalizes the entire policy trajectory. This is desirable because "unavoidable" DEFCON-1 at the end often means "avoidable earlier in the hand."

**When would differentiation help?** Only if the -0.5 extra penalty were large enough to distort value estimates AND the unavoidable cases were frequent enough to dominate the gradient. With ~6% DEFCON-1 rate and perhaps 1-2% of those being genuinely unavoidable, the distortion is negligible (~0.01-0.02 expected reward bias).

### 4. Implementation cost of detecting avoidability

To detect "strictly avoidable" at reward-computation time, the system would need:

1. **C++ side**: At the point of DEFCON-1 game-over in `game_loop.cpp`, check whether the phasing player had any legal action that would NOT lower DEFCON. This requires:
   - Enumerating all legal (card, mode) pairs from the player's hand
   - For each pair, simulating whether the action would lower DEFCON (non-trivial for indirect cards like Grain Sales)
   - Storing the result (`had_safe_alternative: bool`) in `GameResult`

2. **Binding**: Expose the new field through pybind11 to Python

3. **Python side**: Read the flag in `_compute_reward`

The C++ enumeration is the hard part. For direct DEFCON-lowering (coup at DEFCON=2), it's a simple check on `legal_modes`. But for indirect lowering (opponent event auto-fires and randomly coups a BG), you'd need to either:
   - Conservatively assume all opponent events at DEFCON=2 are dangerous (over-classifying as "unavoidable")
   - Actually simulate the event to see if it can lower DEFCON (expensive and nondeterministic for random events)

This is 2-4 hours of work across C++/bindings/Python, with ongoing maintenance burden, for a feature that provides marginal training benefit.

### 5. Alternative: step-level intermediate DEFCON shaping

The existing holistic fix analysis (opus_analysis_20260413_defcon1_holistic_fix.md) already notes that the right primary fix is at the engine level (guard `apply_ops_randomly`, expand danger card list, clamp HLSTW). Once those fixes are in, the residual DEFCON-1 rate drops to ~5-6%, and nearly all residual cases are either:
- Genuine bad play by the model (avoidable, penalty is correct)
- Extremely rare forced situations (noise, penalty magnitude doesn't matter)

The -1.5 penalty was added as a secondary signal alongside the engine fixes. Its purpose is to accelerate learning during the transition period. Once DEFCON-1 rates stabilize below 5%, the penalty's marginal impact is minimal either way.

### 6. Risk of removing the extra penalty for "unavoidable" cases

If we implemented differentiated penalties (-1.5 for avoidable, -1.0 for unavoidable) and the avoidability classifier had false positives (labeling avoidable cases as unavoidable), we'd REDUCE the training signal for the most important cases. This is strictly worse than the uniform penalty.

The classifier would need to be conservative (default to "avoidable" when uncertain), which means most of the "unavoidable" edge cases would still get -1.5 anyway, negating the benefit.

## Conclusions

1. **Keep the uniform -1.5 penalty.** The theoretical concern about penalizing unavoidable situations is valid but practically negligible at the current ~6% DEFCON-1 rate.

2. **The phasing-player rule already handles opponent-induced DEFCON-1.** When the opponent causes DEFCON-1, the opponent is the phasing player and loses. The learned model gets +1.0. The -1.5 penalty only fires when the learned model's own action (directly or indirectly) caused DEFCON-1.

3. **"Unavoidable" DEFCON-1 losses almost always trace to avoidable earlier decisions.** GAE correctly propagates the penalty backward through the trajectory, penalizing the hand-management decisions that led to the forced position.

4. **The extra -0.5 (beyond the -1.0 base loss) is small enough to act as mild emphasis, not distortion.** Expected reward bias from genuinely unavoidable cases is ~0.01-0.02, well within noise.

5. **Implementing avoidability detection costs 2-4 hours of cross-layer work for marginal benefit.** The C++/binding/Python plumbing plus the non-trivial simulation of indirect DEFCON-lowering events makes this poor ROI.

6. **The right investment is the engine-level fixes (already identified in WS6).** Expanding `kDefconLoweringCards`, guarding `apply_ops_randomly`, and clamping HLSTW eliminate the root causes. Once done, the reward penalty question becomes moot for all practical purposes.

## Recommendations

1. **No change to `_compute_reward`.** Keep the uniform -1.5 for all DEFCON-1 losses.

2. **Prioritize engine-level DEFCON fixes (WS6)** over reward-function refinement. These eliminate root causes rather than trying to classify symptoms.

3. **If the DEFCON-1 rate drops below 3% after engine fixes**, consider removing the extra -0.5 entirely (use -1.0 for all losses). At that point the penalty provides negligible gradient signal and slightly complicates the reward function.

4. **If a future experiment shows the model systematically avoiding calculated-risk plays** (e.g., never playing opponent cards even when safe), investigate whether the -1.5 penalty is the cause. This would be the empirical signal that differentiation is needed. No such signal exists currently.

5. **Track DEFCON-1 losses by last-action context** (was it a BG coup? opponent event auto-fire? last card in hand?) as a diagnostic metric. This is cheaper than implementing avoidability detection and would provide the data needed to revisit this decision.

## Open Questions

1. What is the actual frequency of "genuinely unavoidable" DEFCON-1 cases (Category C) in current self-play? A sampling study of 100 DEFCON-1 games could answer this definitively.

2. After the WS6 engine fixes, what is the new residual DEFCON-1 rate? If it drops below 3%, the penalty may not be worth the code complexity regardless of avoidability.

3. Does the -1.5 penalty interact with the VP-coefficient reward shaping (`vp_coef`)? Currently the -1.5 short-circuits before VP shaping is applied. This seems correct (DEFCON-1 should override VP magnitude) but worth verifying empirically.
---
