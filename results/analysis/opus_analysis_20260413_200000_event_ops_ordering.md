---
# Opus Analysis: Event/Ops Ordering Rule Verification
Date: 2026-04-13T20:00:00Z
Question: Do TS rules allow player choice of event-before-ops vs ops-before-event?

## Executive Summary

The prior analysis was **wrong**. The official Twilight Struggle Deluxe Edition rules (section 5.2, page 6) explicitly state that the phasing player **chooses** whether the opponent's event fires before or after their operations. The engine (`game_loop.cpp` lines 718-726) hardcodes event-before-ops with no player choice. This is a confirmed rules bug.

## Exact Rule Text (verbatim quote with page/section reference)

From **TS_Rules_Deluxe.pdf, page 6, section 5.2** (emphasis preserved from original):

> **5.2 Events Associated With Your Opponent:** If a player plays a card as an Operation, and the card's Event is associated only with his opponent, the Event still occurs (and the card, if it has an asterisk after the Event title, is removed).
>
> NOTE: When playing a card for operations and it triggers your opponent's event, your opponent implements the event text as if they had played the card themselves.
>
> **- The phasing player always decides whether the event is to take place before or after the Operations are conducted.**
>
> - If a card play triggers an opponent's Event, but that Event cannot occur because a prerequisite card has not been played, or a condition expressed in the Event has not been met, the Event does not occur. In this instance, cards with an asterisk Event (marked *) are returned to the discard pile, not removed from the game.
>
> - If a card play triggers an opponent's Event, but play of that event has been prohibited by a superseding Event card, then the Event does not occur, and the card remains in play for Operations points only.
>
> - If a card play triggers an opponent's Event, but the event results in no effect, the Event is still considered played, and would still be removed if it has an asterisk.

The first bullet point is the dispositive rule. It uses the word "always" and "decides" — it is an unconditional player choice, not a fixed ordering.

## What the Engine Implements (game_loop.cpp)

In `cpp/tscore/game_loop.cpp`, function `apply_action_with_hands` (lines 711-753):

```cpp
std::tuple<PublicState, bool, std::optional<Side>> apply_action_with_hands(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
) {
    // Lines 718-726: ALWAYS fire opponent event BEFORE ops, no choice
    if (action.mode != ActionMode::Event) {
        const auto owner = card_spec(action.card_id).side;
        if (owner == other_side(side)) {
            auto [new_pub, over, winner] = fire_event_with_state(gs, action.card_id, owner, rng, policy_cb);
            if (over) {
                return {new_pub, true, winner};
            }
        }
    }

    // Lines 732: Then apply the player's chosen operation
    auto [new_pub, over, winner] = apply_action(gs.pub, action, side, rng, policy_cb);
    ...
}
```

The logic is unconditional: when `action.mode != Event` and the card belongs to the opponent, fire the event first, then apply operations. There is no branch, no flag, no policy query for the ordering choice.

The `ActionMode` enum (`types.hpp` lines 23-29) has five values: `Influence`, `Coup`, `Realign`, `Space`, `Event`. There is no `InfluenceEventAfter` / `CoupEventAfter` or similar variant to encode the ordering preference.

The `ActionEncoding` struct has no `event_order` field.

## Match or Mismatch?

**Mismatch.** The rules give the phasing player an explicit choice. The engine hardcodes event-before-ops.

## Conclusions (numbered)

1. The official rules (section 5.2, bullet 1) unambiguously grant the phasing player the choice of whether the opponent's event fires before or after operations.
2. The engine (`apply_action_with_hands`, lines 718-726) unconditionally fires the opponent's event before operations, with no mechanism for the player to choose otherwise.
3. This is a confirmed **rules implementation bug** — the engine removes a strategic decision point that the rules provide.
4. The prior analysis stating "engine fires opponent events before ops, no player choice, confirmed correct per rules" was **factually incorrect** about the rules.
5. The strategic impact is significant: choosing event-before-ops vs ops-before-event can determine whether influence placement, coups, or realignment rolls are affected by the opponent's event. Classic examples include playing Red Scare/Purge for ops (wanting to place influence before the -1 modifier kicks in) or playing Blockade for ops (wanting to coup West Germany before the event forces a discard-or-lose-influence choice).

## Recommendations

1. **Add an `event_order` field to `ActionEncoding`** (or split ActionModes into `InfluenceEventBefore`/`InfluenceEventAfter` variants) so the phasing player's ordering choice is encoded in the action.
2. **Update `apply_action_with_hands`** to check the ordering preference and conditionally fire the event before or after operations.
3. **Update the legal action generator** to emit both ordering variants when the played card triggers an opponent event.
4. **Update the policy network** to output the ordering decision (this could be a binary head or folded into the mode head).
5. **Audit replay logs** to determine the empirical distribution of event-before vs event-after choices in human games, to validate the fix and calibrate training data.
6. **Priority**: This is a correctness bug that removes a real strategic decision from the game tree. It should be fixed before any further strength-push work that depends on correct game modeling.
