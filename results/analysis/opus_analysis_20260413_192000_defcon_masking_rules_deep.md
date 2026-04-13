---
# Opus Analysis: DEFCON Masking — Rules Deep Dive
Date: 2026-04-13T19:20:00Z
---

## Executive Summary

This analysis examines four questions about the DEFCON-1 masking and penalty system. Key findings:

1. **Event timing (Q1):** The C++ engine implements event-BEFORE-ops for opponent cards, which is correct per TS rules. The player does NOT get to choose ops-before-event for opponent cards. At DEFCON 2, playing an opponent's DEFCON-lowering card is always suicidal because the event fires first (unconditionally), lowering DEFCON to 1 before ops execute. The mask is correct to block these.

2. **DEFCON 3 headline masking (Q2):** The headline mask at DEFCON 3 is slightly too conservative for opponent cards but correctly conservative for neutral cards. Opponent DEFCON-lowering cards played as headline fire as the owner's event — the opponent's headline, not yours — so it only triggers if the opponent's headline has lower ops (resolves second). At DEFCON 3, both headlines would need to lower DEFCON for DEFCON-1. However, since the AI cannot observe the opponent's headline choice, blocking is a reasonable safety measure for self-play training. For competitive play with belief modeling, this mask should be relaxed.

3. **Penalty value (Q3):** The -1.5 penalty is now marginally justified. With comprehensive masking, the only remaining DEFCON-1 losses are: forced last-card play, headline collisions, and indirect event chains. These are partially unavoidable, so a harsh penalty risks teaching the model to fear situations it cannot control. Recommendation: reduce to -1.2 or -1.0 and monitor DEFCON-1 rate.

4. **DEFCON-choice cards (Q4):** Three cards allow DEFCON level selection: Summit (48, winner chooses +1/-1), How I Learned to Stop Worrying (49, sets DEFCON 2-5), and Olympic Games (20, opponent chooses boycott which lowers DEFCON). The current blanket inclusion of all three in kDefconLoweringCards is correct for DEFCON 2 but overly broad for DEFCON 3 headline masking — How I Learned can never cause DEFCON-1 (minimum set is 2), and Summit only lowers if the winner chooses to.

**Bug found:** The comment in `card_properties.hpp` line 33 says "92 SALT Negotiations" but card 92 is actually "Soviets Shoot Down KAL 007". SALT is card 46 and RAISES DEFCON. The list membership is correct; only the comment is wrong.

## Q1: Event Timing — Does Ops-Before-Event Change DEFCON Safety?

### Rules Question
When a player plays an opponent's card for ops, does the player choose whether the event fires before or after ops?

### Answer: No — Event Always Fires First (for opponent cards)

**Official TS rules (Deluxe Edition):** When you play an opponent's card for Operations, the opponent's event occurs. The timing is NOT a player choice — the event fires as part of card resolution. The standard rule is:

- If you play the card for **Ops**: the opponent's event fires (mandatory), then your ops resolve.
- If you play the card for **Event**: your event fires (but opponent cards can't be played "for event" by you — only the card owner's event fires).

**Engine implementation** (`game_loop.cpp:718-726`):
```cpp
if (action.mode != ActionMode::Event) {
    const auto owner = card_spec(action.card_id).side;
    if (owner == other_side(side)) {
        auto [new_pub, over, winner] = fire_event_with_state(gs, action.card_id, owner, rng, policy_cb);
        if (over) {
            return {new_pub, true, winner};
        }
    }
}
```

This fires the opponent's event BEFORE the player's ops (influence/coup/realignment). If the event causes DEFCON-1, the game ends immediately (`if (over) return`). The player never gets to execute ops.

**Conclusion for DEFCON safety:** At DEFCON 2, playing an opponent's DEFCON-lowering card for ops is always suicidal. The event fires first, drops DEFCON to 1, and the game ends before ops execute. There is no "ops-before-event" option.

**Note on competitive TS variants:** Some older editions had ambiguous wording about event/ops ordering. The Deluxe Edition and ITS competitive rules are clear: opponent events are mandatory and fire as part of card play, not as a separate timing choice. The engine correctly implements this.

### DEFCON-1 check timing
The DEFCON-1 check happens in `check_vp_win()` (`step.cpp:1244-1255`), which is called after each action resolution. When `pub.defcon <= 1`, the phasing player loses. This means DEFCON-1 is checked immediately after the event fires, not deferred to end-of-round.

## Q2: DEFCON 3 Headline Masking — Too Conservative?

### Current Implementation

In `train_ppo.py:431-436`:
```python
if is_opp and defcon == 3 and ar == 0:
    continue  # Block opponent DEFCON-lowering cards at headline, DEFCON 3
if is_neutral and ar == 0 and defcon <= 3:
    continue  # Block neutral DEFCON-lowering cards at headline, DEFCON <= 3
```

In C++ `learned_policy.cpp:192-203`: identical logic.

### Headline Resolution Rules

From the engine (`game_loop.cpp:852-859`):
```cpp
std::sort(ordered.begin(), ordered.end(), [](const auto& lhs, const auto& rhs) {
    const auto lhs_ops = card_spec(lhs.action.card_id).ops;
    const auto rhs_ops = card_spec(rhs.action.card_id).ops;
    if (lhs_ops != rhs_ops) {
        return lhs_ops > rhs_ops;
    }
    // USSR (side=0) resolves first on headline tiebreak per official TS rules.
    return static_cast<int>(lhs.side) < static_cast<int>(rhs.side);
});
```

Headlines resolve in **descending ops order**, with USSR first on ties. Each headline fires sequentially — first one resolves completely (including DEFCON changes), then the second.

### Analysis: When Can DEFCON 3 Headline Cause DEFCON-1?

For DEFCON to drop from 3 to 1 during headlines, TWO separate DEFCON-lowering events must fire. Scenarios:

**Scenario A: Both players headline DEFCON-lowering cards**
- Higher-ops card resolves first → DEFCON drops to 2
- Lower-ops card resolves second → DEFCON drops to 1
- Phasing player of the second headline loses

**Scenario B: One headline triggers a chain (e.g., Olympic Games boycott + the event itself)**
- Theoretically possible but requires specific card interactions

**Is blocking too conservative?**

For **opponent cards** at DEFCON 3 headline: Yes, slightly. If you (say, USSR) play an opponent's DEFCON-lowering card as headline, the event fires as the card owner's event. But here's the subtlety: you're playing it as your headline, so it fires in YOUR headline slot. If your headline has higher ops, it fires first, dropping DEFCON from 3→2. Then the opponent's headline fires. If THEIR headline also lowers DEFCON, it drops 2→1 and THEY lose (they're the phasing player of the second headline).

The risk to YOU only materializes if:
1. Your DEFCON-lowering headline has LOWER ops than the opponent's DEFCON-lowering headline
2. So opponent's fires first (3→2), then yours fires (2→1), and YOU lose

This means the mask should consider the ops value of the card. A 4-ops DEFCON-lowering headline at DEFCON 3 is much safer than a 2-ops one (fewer cards have higher ops to resolve before it).

For **neutral cards** at DEFCON 3 headline: The blocking is reasonable because neutral events like Olympic Games (20, 2 ops) involve opponent choices (boycott). The opponent can choose to boycott, lowering DEFCON. Combined with the opponent's own headline, this creates uncontrollable DEFCON-1 risk.

**Quantitative assessment:**
- At DEFCON 3, there are 15 DEFCON-lowering cards total
- Probability both players headline one depends on hand composition
- In practice, both players having DEFCON-lowering cards AND both choosing to headline them is uncommon
- Blocking removes genuine strategic options (e.g., headlining We Will Bury You at DEFCON 3 for the VP + DEFCON pressure)

**Verdict:** The mask is somewhat too conservative for training. It removes legitimate strategic choices. However, for PPO training where DEFCON-1 losses create noisy negative signal, the conservatism is pragmatically useful. For competitive play / MCTS, the mask should be relaxed or replaced with probabilistic risk assessment.

## Q3: Is -1.5 Penalty Still Justified?

### Current Penalty Logic (`train_ppo.py:597-600`):
```python
# DEFCON-1 suicide penalty: losing via DEFCON-1 is worse than a normal loss.
# Give a -1.5 signal (below -1.0) so the model learns DEFCON-1 is catastrophic.
if end_reason == "defcon1" and not won:
    return -1.5
```

### What the mask covers (avoidable DEFCON-1 causes):
1. Direct coups at DEFCON 2 on battleground countries: **masked** (mode_mask blocks MODE_COUP)
2. Opponent DEFCON-lowering cards for ops at DEFCON 2: **masked** (card_mask blocks)
3. Own DEFCON-lowering events at DEFCON 2: **masked** (mode_mask blocks MODE_EVENT)
4. Headline DEFCON-lowering cards at DEFCON 3: **masked** (card_mask blocks at ar==0)
5. Nuclear Subs exemption: **fixed** (correctly allows US coups with Nuclear Subs)

### What remains unmasked (residual DEFCON-1 causes):
1. **Last-card forced play:** Hand has only one card and it's a DEFCON-lowering opponent card. Fallback logic (`card_mask.any()` check at line 439-444) correctly allows it — can't skip your action round.
2. **Headline collision at DEFCON 3:** If both players headline DEFCON-lowering cards, the second player to resolve loses. Masked in training but could be relaxed.
3. **Indirect event chains:** Cards like Missile Envy (52) or Grain Sales (68) that call `apply_ops_randomly` — the random ops might coup a battleground at DEFCON 2. These are in kDefconLoweringCards and masked at card level, so they're mostly covered.
4. **Opponent-forced DEFCON lowering:** Events like Cuban Missile Crisis (43) that force DEFCON pressure through game mechanics rather than direct action.
5. **Multi-step chains:** A card event lowers DEFCON to 2, then a subsequent forced action (e.g., Junta's free coup) triggers DEFCON-1. This is partially handled by including Junta (50) in the DEFCON-lowering list.

### Assessment

The -1.5 penalty was introduced when the mask was incomplete and DEFCON-1 losses were common (~6% rate). With comprehensive masking, residual DEFCON-1 losses fall into two categories:

**Category A — Truly unavoidable:** Last-card forced play. The model cannot prevent these. Penalizing at -1.5 instead of -1.0 punishes the model for situations it has no control over, which adds noise to the value function.

**Category B — Partially avoidable with lookahead:** Some indirect chains could be avoided with deeper reasoning (e.g., not couping at DEFCON 3 when you know the opponent has We Will Bury You). The -1.5 penalty provides gradient to learn these deeper patterns. But the mask already blocks most of these at DEFCON 2.

**Recommendation:** Reduce to **-1.2** as a compromise. This still signals that DEFCON-1 is worse than a normal loss (incentivizing DEFCON management earlier in the game) but doesn't over-penalize truly unavoidable situations. If the DEFCON-1 rate drops below 2% with current masking, further reduce to -1.0.

## Q4: Cards That Allow DEFCON Level Selection

### Cards with DEFCON choice mechanics

| Card ID | Name | Side | DEFCON Effect | Choice? | Notes |
|---------|------|------|---------------|---------|-------|
| 48 | Summit | Neutral | ±1 | Yes — winner chooses raise or lower | `choose_option(next, 48, winner, 2, ...)`: 0=lower, 1=raise |
| 49 | How I Learned to Stop Worrying | Neutral | Set to 2-5 | Yes — player sets level | `choose_option(next, 49, side, 4, ...) + 2`: minimum is DEFCON 2, never 1 |
| 20 | Olympic Games | Neutral | -1 (boycott) | Opponent chooses boycott vs compete | If opponent boycotts, DEFCON drops by 1 |
| 34 | Nuclear Test Ban | Neutral | +2 (raises) | No — always raises | `next.defcon = std::min(5, next.defcon + 2)` — NOT DEFCON-lowering |
| 46 | SALT Negotiations | Neutral | +1 (raises) | No — always raises | `next.defcon = std::min(5, next.defcon + 1)` — NOT DEFCON-lowering |

### Cards that unconditionally lower DEFCON (no choice)

| Card ID | Name | Side | Effect |
|---------|------|------|--------|
| 4 | Duck and Cover | US | DEFCON -1, VP penalty |
| 53 | We Will Bury You | USSR | DEFCON -1, VP +3 |
| 92 | Soviets Shoot Down KAL 007 | US | DEFCON -1, VP -2 |

### Cards that lower DEFCON via coup mechanics

| Card ID | Name | Side | Mechanism |
|---------|------|------|-----------|
| 11 | Korean War | USSR | War card — coup in Korea |
| 13 | Arab-Israeli War | USSR | War card — coup in Israel |
| 24 | Indo-Pakistani War | Neutral | War card — coup |
| 39 | Brush War | USSR | Free coup |
| 50 | Junta | Neutral | Free coup in Central/South America |
| 83 | Che | USSR | Free coup in Latin America/Africa |
| 105 | Iran-Iraq War | USSR | War card — coup |

### Cards that lower DEFCON via random ops

| Card ID | Name | Side | Mechanism |
|---------|------|------|-----------|
| 52 | Missile Envy | Neutral | `apply_ops_randomly` — can coup BG |
| 68 | Grain Sales to Soviets | US | `apply_ops_randomly` — can coup BG |

### Masking recommendations for choice cards

**Summit (48):** Currently in kDefconLoweringCards. At DEFCON 2, the winner COULD choose to lower DEFCON to 1, but this would be suicidal (the phasing player loses). The engine allows setting DEFCON to 1 via `std::clamp(next.defcon + defcon_delta, 1, 5)`. However, the policy callback should never choose "lower" at DEFCON 2. The mask is correct to block it at DEFCON 2 (prevents a bad policy choice from being catastrophic) and reasonable at DEFCON 3 headline (opponent could win Summit and choose to lower, then combined with another event, reach DEFCON 1).

**How I Learned to Stop Worrying (49):** Currently in kDefconLoweringCards. The engine implementation sets DEFCON to `choose_option(...) + 2`, meaning the MINIMUM possible DEFCON is 2, never 1. This card **cannot cause DEFCON-1 by itself**. However, setting DEFCON to 2 at headline could combine with the opponent's headline to reach DEFCON 1. Blocking at DEFCON 3 headline is therefore correct, but blocking at DEFCON 2 during action rounds is **overly conservative** — the player can choose to set DEFCON to 2, 3, 4, or 5, and should be free to choose higher values. The mask should allow this card at DEFCON 2 with the understanding that the event decision callback will choose DEFCON 3+ if at DEFCON 2.

**Olympic Games (20):** The OPPONENT decides whether to boycott. At DEFCON 2, if the opponent boycotts, DEFCON drops to 1 and the phasing player (who played Olympic Games) loses. The mask correctly blocks this at DEFCON 2. At DEFCON 3 headline, blocking is reasonable since the interaction is unpredictable.

### Comment Bug

`card_properties.hpp` line 33 states:
```
//   92  SALT Negotiations (Neutral): affects DEFCON
```
This is incorrect. Card 92 is "Soviets Shoot Down KAL 007" (US, Late War). SALT Negotiations is card 46 and RAISES DEFCON (not in the lowering list). The list membership {92} is correct; the comment should be fixed.

## Conclusions

1. **Event timing is correct.** The engine fires opponent events BEFORE ops, with no player choice on ordering. At DEFCON 2, playing an opponent's DEFCON-lowering card is always suicidal. The card-level mask is correct and necessary.

2. **DEFCON 3 headline masking is pragmatically useful but strategically conservative.** It removes legitimate plays (e.g., headlining We Will Bury You at DEFCON 3 when behind). For PPO training, this is an acceptable tradeoff. For competitive play, it should be relaxed with belief-based risk assessment.

3. **The -1.5 penalty is now excessive given comprehensive masking.** Residual DEFCON-1 losses are mostly unavoidable (last-card, headline collisions). Over-penalizing these adds value-function noise. Reduce to -1.2 short-term, -1.0 long-term.

4. **How I Learned to Stop Worrying (49) cannot cause DEFCON-1 alone** — minimum set level is 2. The mask should allow it during action rounds at DEFCON 2, trusting the event decision callback to choose a safe DEFCON level.

5. **Summit (48) has a self-destructive option** (lowering at DEFCON 2), but this is the winner's choice and a rational policy would never choose it. The mask is a safety net, not a strategic restriction.

6. **Bug: comment in card_properties.hpp misidentifies card 92** as SALT Negotiations; it is Soviets Shoot Down KAL 007. List membership is correct.

## Recommendations

1. **Fix the card_properties.hpp comment** for card 92: change "SALT Negotiations" to "Soviets Shoot Down KAL 007 (US)".

2. **Reduce DEFCON-1 penalty from -1.5 to -1.2** as an immediate change, with plan to move to -1.0 once DEFCON-1 rate is confirmed below 2%.

3. **Consider removing How I Learned (49) from kDefconLoweringCards for action-round masking** (keep it for headline masking at DEFCON 3). The card's minimum DEFCON set is 2, and the policy callback controls the actual level chosen.

4. **Keep DEFCON 3 headline masking for now** in PPO training. Add a config flag (`allow_defcon3_headline_risk`) to enable relaxation for MCTS / competitive play later.

5. **Add event-decision-level DEFCON safety** for Summit (48) and How I Learned (49): in the policy callback for `choose_option`, mask the "lower DEFCON" option when DEFCON <= 2. This is defense-in-depth beyond the card-level mask.

6. **Do not implement ops-before-event ordering** — this is not a real TS rule variant. The engine correctly implements mandatory opponent event before ops.

7. **Track residual DEFCON-1 loss causes** in training logs (last-card, headline, indirect chain) to validate that the penalty level matches the avoidability distribution.
