---
# Opus Analysis: DEFCON-1 Rate -- Holistic Fix
Date: 2026-04-13
Question: 29% DEFCON-1 self-termination rate -- engine + model holistic solution

## Executive Summary

The 29% DEFCON-1 self-termination rate in v55 self-play (T=1.0) has three root causes operating simultaneously: (1) an incomplete DEFCON-lowering card list that omits Grain Sales to Soviets (card 68) and Missile Envy (card 52), which can indirectly lower DEFCON via `apply_ops_randomly` triggering battleground coups; (2) the HLSTW (card 49) `choose_option` implementation allowing the heuristic/random policy to set DEFCON to 1 directly; and (3) the PPO rollout card-selection mask blocking opponent danger cards but not accounting for cards whose events trigger DEFCON-lowering side effects through intermediate random actions. The fix requires expanding the danger card list, adding a DEFCON-safety guard inside `apply_ops_randomly`, and adding targeted reward shaping -- all three are necessary and independently insufficient.

## Findings

### Engine analysis

#### Root cause 1: Incomplete kDefconLoweringCards list

The `kDefconLoweringCards` list (13 cards) is defined in 5 separate locations:
- `cpp/tscore/mcts_search_impl.hpp:26` (13 cards)
- `cpp/tscore/mcts_batched.cpp:41` (13 cards)
- `cpp/tscore/mcts.cpp:61` (13 cards)
- `cpp/tscore/ismcts.cpp:45` (13 cards)
- `cpp/tscore/learned_policy.cpp:165` (13 cards)
- `scripts/train_ppo.py:166` (Python mirror, 13 cards)
- `cpp/tscore/policies.cpp:37` (only 7 cards -- heuristic policy uses a narrower list plus separate `kDefconRandomCoupCards` and `kDefconProbLoweringCards`)

The 13-card list is: `{4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105}`.

**Missing cards whose events can lower DEFCON indirectly:**
- **Card 68 (Grain Sales to Soviets, US, 2 ops)**: Event calls `apply_ops_randomly(pub, Side::US, ops, ...)` at `game_loop.cpp:526`. This function randomly selects between Influence (50%), Coup (25%), or Realign (25%). The Coup path (`game_loop.cpp:204-235`) targets accessible countries and lowers DEFCON on battleground coups: `pub.defcon = std::max(1, pub.defcon - 1)`. **This is the #1 trigger card with 8 of 44 action-round DEFCON-1 cases.** When USSR plays Grain Sales for ops at DEFCON=2, the US event auto-fires (`apply_action_with_hands` line 713-714 fires the event for the owning side), and if the random ops land on a BG coup, DEFCON drops from 2 to 1.
- **Card 52 (Missile Envy, Neutral, 2 ops)**: Event also calls `apply_ops_randomly` at `game_loop.cpp:487`. Same mechanism. As a Neutral card, both sides can trigger this.

These cards are not blocked because they don't ALWAYS lower DEFCON -- only when the random action selection happens to pick Coup AND targets a battleground. But at DEFCON=2, the probability is ~25% (coup mode) times P(battleground target), which is high enough to cause frequent deaths.

#### Root cause 2: apply_ops_randomly has no DEFCON safety

The `apply_ops_randomly` function (`game_loop.cpp:174-243`) randomly selects a mode (Influence/Influence/Coup/Realign with 50/25/25 probability) and executes it. The Coup path:
1. Filters targets by `is_defcon_restricted(cid, pub)` -- but this only restricts WHICH countries can be couped based on DEFCON level (e.g., at DEFCON 2, only non-Europe/Asia battlegrounds). It does NOT prevent couping a battleground entirely.
2. Any battleground coup lowers DEFCON by 1 (unless `nuclear_subs_active` for US).
3. At DEFCON=2, any BG coup -> DEFCON 1 -> game over.

**The function should refuse to coup at DEFCON=2**, or at minimum refuse to coup battlegrounds at DEFCON=2. This is a pure engine-correctness fix: even a perfect player can't prevent this randomized death when the engine rolls Coup.

#### Root cause 3: HLSTW (card 49) choose_option allows DEFCON=1

Card 49 (How I Learned to Stop Worrying) at `step.cpp:608`: `next.defcon = choose_option(next, 49, side, 5, rng, policy_cb) + 1`. Option 0 sets DEFCON to 1 = immediate nuclear war attributed to the phasing player. The heuristic policy (`policies.cpp`) and random fallback can both select option 0. This accounts for several of the headline cases and some action-round cases.

**Fix**: The event should exclude option 0 (DEFCON=1) from the choice set, OR the `choose_option` for card 49 should be clamped to `max(2, chosen + 1)`. In competitive TS rules, a player would never voluntarily set DEFCON to 1 because it's suicide -- this is a degenerate choice that no rational player would make.

#### Current safety mechanisms and their gaps

**What IS currently blocked (card-level mask):**
All 5 safety implementations (MCTS, batched rollout, learned_policy, PPO Python) block:
- Opponent DEFCON-lowering cards from `kDefconLoweringCards` at DEFCON <= 2
- Opponent DEFCON-lowering cards in headline at DEFCON = 3
- Neutral DEFCON-lowering cards in headline at DEFCON <= 3
- Own DEFCON-lowering cards in headline at DEFCON <= 2

**What is NOT blocked:**
1. Cards not in the danger list (68, 52) whose events trigger indirect DEFCON drops
2. The `apply_ops_randomly` function itself has no DEFCON guard
3. HLSTW option 0 (DEFCON=1)
4. Summit (card 48) winner choosing to lower DEFCON from 2 to 1

#### Feasibility of "would this play lower DEFCON?" check

A static check at legal-action time ("would playing this opponent card for ops auto-fire an event that lowers DEFCON?") is computationally feasible for most cards because event effects are deterministic or enumerable. However, for cards like Grain Sales (68) and Missile Envy (52), the event effect depends on a random action selection -- it MIGHT coup a BG or it might not. This makes a static check insufficient.

**The correct fix is at the engine level**: `apply_ops_randomly` should not coup at DEFCON <= 2. This is both simpler and more correct than trying to predict random outcomes at card-selection time.

### Model analysis

#### DEFCON as a feature

DEFCON is already encoded as a scalar feature in the model input: `(defcon - 1) / 4.0` (`mcts_batched.cpp:267`, `train_ppo.py:219`). The model has access to DEFCON state but does not have an explicit "this card is dangerous at this DEFCON level" signal.

The model CAN in principle learn to avoid dangerous cards at low DEFCON, but this requires:
1. Enough negative signal from DEFCON-1 losses (currently ~29% of games)
2. The model to associate the specific card choice with the downstream DEFCON-1 outcome, which is difficult because the causal chain is: card selection -> event auto-fire -> random ops -> BG coup -> DEFCON drop

This credit assignment problem is extremely hard for PPO because:
- The DEFCON-1 outcome happens 1+ steps after the card selection
- The outcome is stochastic (depends on `apply_ops_randomly` rolling coup)
- The reward is terminal-only (applied to the last step of the game)

#### DEFCON-aware reward shaping

The current reward function (`_compute_reward`, `train_ppo.py:578`) is purely terminal: +1 for win, -1 for loss, with optional VP scaling. There is NO DEFCON-specific penalty.

Adding a DEFCON-1 penalty is NOT recommended as the primary fix because:
1. The model already receives -1 for losing (DEFCON-1 loss is a loss)
2. An extra penalty doesn't fix the credit assignment problem (which step caused the loss?)
3. The root cause is an engine/mask gap, not insufficient training signal

However, a small DEFCON-proximity penalty as intermediate reward shaping COULD help the model learn faster:
- At each step, add a small negative reward proportional to DEFCON danger: e.g., `-0.01 * max(0, 3 - defcon)` when the player just played an opponent's card
- This gives immediate negative signal at the decision point, not just at game end

#### DEFCON in the card-selection head

The model's card-selection head sees DEFCON through the global scalar features. Adding a per-card "DEFCON danger" feature (binary: 1 if this card is in the danger list AND DEFCON <= 2) could help, but this is an architecture change and less impactful than the engine fix.

### Training analysis

#### Should DEFCON-1 games be filtered from training data?

**No.** DEFCON-1 games contain valuable negative signal: the model learns that playing certain cards at low DEFCON leads to losses. Filtering them removes ~29% of training games and reduces sample efficiency significantly.

However, games where the DEFCON-1 was caused by a random `apply_ops_randomly` outcome (not the model's choice) provide a noisy signal. After fixing the engine, these games won't occur, making the question moot.

#### Will the problem resolve naturally with more self-play?

**Partially but slowly.** The model receives -1 for DEFCON-1 losses, so over many iterations it should learn to avoid the triggering cards. But the credit assignment problem makes convergence slow, and the model may learn superstitious avoidance (avoiding all opponent cards near low DEFCON) rather than targeted avoidance.

The engine fix is strictly superior: it prevents the degenerate outcomes entirely, allows the model to train on meaningful games, and eliminates the credit assignment problem.

#### DEFCON-aware value targets

Not recommended. The value head already predicts win probability, which implicitly captures DEFCON risk. Modifying value targets to discount by DEFCON headroom would distort the training signal.

## Conclusions

1. **The primary root cause is an engine gap, not a model problem.** Card 68 (Grain Sales to Soviets) is the #1 trigger and is NOT in the danger card list. The `apply_ops_randomly` function has no DEFCON safety guard.

2. **Three independent fixes are needed, all in the engine layer:**
   - Add cards 68 and 52 to `kDefconLoweringCards` (all 7 locations)
   - Add a DEFCON guard to `apply_ops_randomly`: refuse to coup (fall back to influence) when DEFCON <= 2
   - Clamp HLSTW (card 49) `choose_option` to exclude DEFCON=1 (option 0 -> option 1 minimum)

3. **The `apply_ops_randomly` DEFCON guard is the most impactful fix** because it blocks ALL indirect DEFCON-lowering chains, including any future cards or effects that route through this function. It also handles the case where the card passes the danger-list check but the random action still kills.

4. **Adding cards to the danger list is defense-in-depth** -- it prevents the model from even selecting these cards at DEFCON <= 2, which is the correct play in competitive TS (never voluntarily trigger an opponent event that could end the game).

5. **Model-side and training-side changes are NOT needed as primary fixes.** The engine fix eliminates the root cause. The model will naturally learn better DEFCON management once it stops dying to engine-level gaps. Optional reward shaping can accelerate convergence but is not blocking.

6. **The 6 duplicate definitions of `kDefconLoweringCards` are a maintenance hazard.** They should be consolidated into a single source of truth (e.g., `types.hpp` or a shared header).

7. **After the engine fix, expect the DEFCON-1 rate to drop from ~29% to ~5-8%** (residual cases from legitimate game scenarios like Cuban Missile Crisis, player coups at DEFCON 2, etc.). The current ~6% baseline rate mentioned in project memory aligns with this.

## Recommendations

Ordered by implementation priority. All are engine-layer changes.

### Priority 1: Guard `apply_ops_randomly` against DEFCON-1 suicide (BLOCKING)

**File:** `cpp/tscore/game_loop.cpp`, function `apply_ops_randomly` (line 174)

**Change:** When `pub.defcon <= 2`, remove `ActionMode::Coup` from the mode selection. If coup is selected and DEFCON <= 2, fall back to Influence.

```cpp
// Inside apply_ops_randomly, after mode selection (line 193):
if (mode == ActionMode::Coup && pub.defcon <= 2) {
    // Coup at DEFCON 2 would lower DEFCON to 1 on BG targets.
    // Fall back to influence placement (safest mode).
    for (int i = 0; i < ops; ++i) {
        const auto target = choose_country(pub, 0, side, accessible, rng, policy_cb);
        pub.set_influence(side, target, pub.influence_of(side, target) + 1);
    }
    return;
}
```

This single fix blocks the dominant failure mode (29 of 44 influence-mode cases where the auto-fired event's random coup lowered DEFCON).

### Priority 2: Add missing cards to kDefconLoweringCards (BLOCKING)

**Files (all 7 locations):**
- `cpp/tscore/mcts_search_impl.hpp:26`
- `cpp/tscore/mcts_batched.cpp:41`
- `cpp/tscore/mcts.cpp:61`
- `cpp/tscore/ismcts.cpp:45`
- `cpp/tscore/learned_policy.cpp:165`
- `cpp/tscore/policies.cpp:37` (also add to `kDefconRandomCoupCards`)
- `scripts/train_ppo.py:166`

**Add cards:** 68 (Grain Sales to Soviets), 52 (Missile Envy).

These cards call `apply_ops_randomly` whose event can lower DEFCON through random coup selection. Even after the Priority 1 fix guards `apply_ops_randomly`, adding these to the danger list provides defense-in-depth: the card mask will prevent the model from selecting them at DEFCON <= 2, which is the correct competitive play.

Also consider adding card 94 (Ortega?) if its event calls `apply_free_coup` with `defcon_immune = false`.

### Priority 3: Clamp HLSTW (card 49) to never set DEFCON=1 (BLOCKING)

**File:** `cpp/tscore/step.cpp`, case 49 (line 608)

**Change:** Exclude option 0 from the choice set or clamp the result:

```cpp
case 49: {
    // How I Learned: player sets DEFCON to any level 2-5 (never 1, that's suicide).
    next.defcon = choose_option(next, 49, side, 4, rng, policy_cb) + 2;
    next.milops[to_index(side)] = 5;
    break;
}
```

This changes the option count from 5 to 4 and the offset from +1 to +2, making the minimum DEFCON=2. No rational player would choose DEFCON=1 with HLSTW.

### Priority 4: Consolidate kDefconLoweringCards to single definition (RECOMMENDED)

**Action:** Move the canonical list to a shared header (e.g., `cpp/tscore/card_properties.hpp`) and have all 6 C++ locations reference it. Update the Python mirror to auto-generate from the same source or at minimum add a comment with a cross-reference.

### Priority 5: Add Summit (card 48) DEFCON-1 guard (RECOMMENDED)

**File:** `cpp/tscore/step.cpp`, case 48 (line 599)

**Change:** When `pub.defcon == 2`, force `defcon_delta = +1` (raise) instead of allowing the winner to choose lower. No rational player would choose to lower DEFCON from 2 to 1.

```cpp
const auto defcon_delta = (next.defcon <= 2)
    ? 1  // Cannot lower from 2 -> forced raise
    : (choose_option(next, 48, winner, 2, rng, policy_cb) == 0 ? -1 : 1);
```

### Priority 6: Optional reward shaping (DEFERRED)

Only consider this AFTER priorities 1-3 are implemented and the DEFCON-1 rate is measured again. If it remains above 8%, add a per-step DEFCON-proximity penalty:

```python
# In _compute_reward or as intermediate reward:
if raw_defcon is not None and raw_defcon <= 2:
    step.reward -= 0.02  # Small immediate penalty for being at DEFCON 2
```

### Priority 7: Rebuild and benchmark (VERIFICATION)

After implementing priorities 1-3:
1. `cmake --build build -j` to rebuild
2. Run 200 self-play games at T=1.0 with the current v55 checkpoint
3. Measure new DEFCON-1 rate -- target: < 8%
4. If target met, resume PPO training from v55 or latest checkpoint

## Open Questions

1. **Card 94 (step.cpp line 1016)**: This card calls `apply_free_coup` with `defcon_immune = false`. Is it in the deck? If so, it should be added to `kDefconLoweringCards`. Need to verify from `cards.csv`.

2. **Is the `defcon_immune = true` flag on cards 11, 13, 24 correct?** These war cards are in the danger list but their free coups don't lower DEFCON. They may still be dangerous through other mechanisms (VP loss? or are they included conservatively?). The current classification seems overly conservative for these three cards but erring on the side of caution is acceptable.

3. **Should `apply_ops_randomly` refuse to coup entirely at DEFCON <= 2, or only refuse BG coups?** A non-BG coup at DEFCON 2 is safe (doesn't lower DEFCON). However, the function uses `is_defcon_restricted` to filter targets, and at DEFCON 2 the restriction is on Europe/Asia only -- non-Europe/Asia BGs are still valid. The safest fix is to refuse all coups at DEFCON <= 2 (fall back to influence), as the random target selection is uncontrollable.

4. **Does the heuristic policy's `choose_option` for HLSTW already avoid option 0?** If the heuristic policy has its own DEFCON-aware logic for card 49, the clamp may be redundant. But for safety, the engine-level clamp is better.

5. **Are there other `choose_option` calls that can set DEFCON=1?** Summit (card 48) is identified above. Are there others? A systematic audit of all `choose_option` calls with DEFCON side effects is recommended.

---
