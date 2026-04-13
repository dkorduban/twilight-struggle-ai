---
# Opus Analysis: Probabilistic DEFCON-1 Masking (Corrected)
Date: 2026-04-13T19:00:00Z
Question: Are there genuinely probabilistic DEFCON-1 paths where rational risk-taking is suppressed by the mask or penalty?

## Executive Summary

After correcting the understanding of BG coups at DEFCON 2 (deterministic suicide, not probabilistic), the masking picture simplifies dramatically. The train_ppo.py mask is **nearly correct** and the C++ learned_policy.cpp mask is **fully correct**. The Python mask has one structural difference from the C++ mask: it does not block neutral DEFCON-lowering cards at card-selection level during action rounds (only at mode level for EVENT), which is actually correct because neutral cards' events don't auto-fire when played for ops.

The genuinely probabilistic DEFCON-1 paths are narrower than previously believed:

1. **No probabilistic paths exist for opponent-card-for-ops at DEFCON 2** — the Python mask correctly blocks ALL opponent DEFCON-lowering cards from the hand at DEFCON <= 2 (line 431). The C++ mask does the same (learned_policy.cpp:188-190). This is correct because the opponent's event fires automatically and deterministically when you play their card for any non-Event mode.

2. **No probabilistic paths exist for neutral-card-for-ops at DEFCON 2** — neutral cards' events do NOT auto-fire when played for ops. Only opponent-owned cards trigger mandatory event resolution (game_loop.cpp:718-726).

3. **The only remaining probabilistic DEFCON-1 path is headline sequencing at DEFCON 3** — if both players headline DEFCON-lowering cards, the resolution order matters. The mask conservatively blocks opponent DEFCON-lowering cards at DEFCON 3 during headline (ar == 0), which is correct.

4. **There are no genuinely probabilistic DEFCON-1 paths that a rational player might want to take that are suppressed by the current mask.** The mask blocks exactly the right things.

## Findings

### Guaranteed-Suicide Paths (correctly masked)

These are deterministic DEFCON-1 outcomes. The mask correctly prevents all of them:

| Action | DEFCON | Outcome | Masked by |
|--------|--------|---------|-----------|
| BG coup at DEFCON 2 (no Nuclear Subs) | 2 | DEFCON -> 1, phasing player loses | mode_mask[MODE_COUP] = False (line 474) |
| Play opponent's Duck and Cover (#4) for ops at DEFCON 2 | 2 | Event fires: DEFCON -= 1 -> 1 | card_mask skips card (line 431) |
| Play opponent's We Will Bury You (#53) for ops at DEFCON 2 | 2 | Event fires: DEFCON -= 1 -> 1 | card_mask skips card (line 431) |
| Play opponent's Korean War (#11) for ops at DEFCON 2 | 2 | Event fires: coup on South Korea (BG) -> DEFCON -= 1 | card_mask skips card (line 431) |
| Play opponent's Arab-Israeli War (#13) for ops at DEFCON 2 | 2 | Event fires: coup on Israel (BG) -> DEFCON -= 1 | card_mask skips card (line 431) |
| Play any DEFCON-lowering card as EVENT at DEFCON 2 | 2 | Event lowers DEFCON | mode_mask[MODE_EVENT] = False (line 478) |

**Key mechanism**: game_loop.cpp lines 718-726 show that when `action.mode != Event` and the card belongs to the opponent, the event fires BEFORE ops are applied. This makes playing ANY opponent DEFCON-lowering card at DEFCON 2 equivalent to suicide — the event fires regardless of chosen mode (Influence, Coup, Realign, Space).

### Probabilistic Paths via Opponent Event Resolution

**Question A from the task**: When you play an opponent's card for ops, does the opponent's event firing create a probabilistic DEFCON-1 path?

**Answer: No, because the card-level mask already blocks it.**

The Python mask (train_ppo.py:426-432) checks:
```python
if card_id in DEFCON_LOWERING_CARDS:
    if is_opp and defcon <= 2:
        continue  # card is entirely excluded from hand selection
```

This means opponent DEFCON-lowering cards cannot even be selected as the card to play at DEFCON <= 2. The model cannot play them for ops, influence, realign, or space. The mode mask for EVENT (line 478) is a belt-and-suspenders redundancy.

The C++ learned_policy.cpp (lines 185-191) does the same:
```cpp
if (is_opponent_card) {
    // Opponent danger card: event fires for any ops mode → always unsafe at DEFCON 2.
    if (pub.defcon <= 2) {
        continue;  // leave as -inf
    }
```

**Cards where this matters (opponent owns them, you'd want to dump for ops):**

For USSR player holding US cards:
- Duck and Cover (#4, US, 3 ops) — event lowers DEFCON directly
- Grain Sales to Soviets (#68, US, 2 ops) — event calls apply_ops_randomly which can coup BG
- SALT Negotiations (#92, US, 4 ops) — event raises DEFCON (actually safe, but conservatively blocked)

For US player holding USSR cards:
- Korean War (#11, USSR, 2 ops) — event coups South Korea (BG)
- Arab-Israeli War (#13, USSR, 2 ops) — event coups Israel (BG)
- Indo-Pakistani War (#24, Neutral but listed) — event coups India/Pakistan (BG)
- Brush War (#39, USSR, 3 ops) — event coups stability <= 2 country (may be BG)
- We Will Bury You (#53, USSR, 4 ops) — event lowers DEFCON directly
- Che (#83, USSR, 3 ops) — event randomly coups in Latin America/Africa (may be BG)

All correctly blocked at card-selection level for their respective opponent sides.

### Probabilistic Paths via Neutral Card Events

**Neutral DEFCON-lowering cards** (#20 Olympic Games, #24 Indo-Pakistani War, #48 Summit, #49 HLSTW, #50 Junta, #52 Missile Envy, #105 Iran-Iraq War) are NOT blocked at card-selection level during action rounds (only at headline).

**This is correct because neutral card events do NOT auto-fire when played for ops.** The mandatory event-fire mechanism in game_loop.cpp:718-726 only triggers when `card_spec(action.card_id).side == other_side(side)` — i.e., the card belongs specifically to the opponent. Neutral cards are neither side's card, so playing them for ops does NOT fire the event.

Therefore:
- Playing Junta (#50) for ops at DEFCON 2 = safe (event doesn't fire, ops are applied normally)
- Playing Summit (#48) for ops at DEFCON 2 = safe
- Playing Missile Envy (#52) for ops at DEFCON 2 = safe (event doesn't fire; the apply_ops_randomly effect only happens when played as Event)

The EVENT mode block (line 478) correctly prevents playing these as Event at DEFCON 2.

### Probabilistic Paths via apply_free_coup in Events

Several events call `apply_free_coup` with `defcon_immune = false`, meaning a BG target WILL lower DEFCON:

| Card | Event | Target Selection | BG possible? | DEFCON drop? |
|------|-------|------------------|--------------|--------------|
| #11 Korean War | coup South Korea | Fixed (kSouthKoreaId) | Yes (always) | Yes, always |
| #13 Arab-Israeli War | coup Israel | Fixed (kIsraelId) | Yes (always) | Yes, always |
| #24 Indo-Pakistani War | coup India or Pakistan | Policy choice | Yes (both BG) | Yes, always |
| #39 Brush War | coup stability <= 2 | Policy/random | Some are BG | Maybe |
| #50 Junta (OAS) | coup Central/South America | Policy choice | Some are BG (Cuba, Panama) | Maybe |
| #83 Che | coup LatAm/Africa stability <= 2 | Random | Some are BG (Cuba) | Maybe |
| #105 Iran-Iraq War | coup Iran or Iraq | Random | Iran is BG, Iraq is not | 50% |

But ALL of these are event effects. They only trigger when:
1. The card is played as EVENT (blocked by mode mask at DEFCON <= 2), OR
2. The card is played for ops by someone holding an opponent's card (blocked by card mask at DEFCON <= 2)

**No unmasked probabilistic path exists through these events.**

### Probabilistic Paths via Hand Management

**Question C from the task**: Is the real risk from card hand management — e.g., being forced to play a dangerous card later?

**Yes, but this is correctly handled by the existing system:**

1. **Bear Trap / Quagmire** (cards #45/#47): Force the player to discard a 2+ ops card each action round until they roll 1-4 on a d6. If the player's hand contains only opponent DEFCON-lowering cards with 2+ ops, they are forced to discard one. The `resolve_trap_ar` function in game_loop.cpp handles this. The discarded card's event does NOT fire (it's a discard, not a play). So no DEFCON risk from Bear Trap/Quagmire directly.

2. **Last card in hand**: If all other cards have been played and only an opponent DEFCON-lowering card remains, the player must play it. The card-level mask has a fallback (lines 439-444): if ALL cards are masked, it allows all hand cards. This is the "genuinely unavoidable" case — the player has no choice. The -1.5 penalty still applies, but as the prior analysis correctly notes, GAE propagates this backward to penalize the hand-management decisions that led to this situation.

3. **Able Archer at DEFCON 3**: Able Archer (#82) raises DEFCON by 1 if DEFCON < 5, but is not in the DEFCON-lowering set. It doesn't lower DEFCON. Not a risk.

4. **Holding scoring cards**: Scoring cards must be played before end of turn. If a player holds a scoring card and opponent DEFCON-lowering cards, they may need to play the DEFCON-lowering card to make room. This is a hand-management decision, not a probabilistic DEFCON path.

### The Rational Risk-Taking Regime

**Are there situations where a rational player behind on points would WANT to risk DEFCON-1?**

In theory, if DEFCON-1 were probabilistic (e.g., "30% chance the event targets a BG country"), a losing player might rationally take the gamble. But in practice:

1. **BG coups at DEFCON 2 are deterministic suicide**, not a gamble. No rational player takes this.

2. **Opponent events at DEFCON 2 are also deterministic** for cards like Duck and Cover, We Will Bury You (always lower DEFCON) and Korean War, Arab-Israeli War (always target BG). For cards like Brush War or Che, the targeting is random/policy-driven but the event fires deterministically. A rational player cannot choose to risk "maybe the event won't target a BG."

3. **The only genuine "calculated risk" scenario is at DEFCON 3, not DEFCON 2.** At DEFCON 3, playing a card whose event might lower DEFCON to 2 is not immediately fatal. The risk is that a subsequent action (by either player) then drops DEFCON to 1. The current mask already handles DEFCON 3 conservatively during headlines (blocking opponent and neutral DEFCON-lowering cards when ar == 0).

4. **At DEFCON 3 during action rounds**, opponent DEFCON-lowering cards are NOT blocked by the card mask. This is correct — at DEFCON 3, the event firing would drop DEFCON to 2, not 1. The player can still take action rounds at DEFCON 2 (just with restricted coup targets). This is genuinely a rational play: dump an opponent's dangerous card at DEFCON 3 for ops, accepting the DEFCON drop to 2, which restricts future coup targets but doesn't cause immediate loss.

**Conclusion: The mask does NOT suppress any rational risk-taking at DEFCON 2. At DEFCON 3, the mask correctly allows calculated risk during action rounds and blocks it during headlines.**

## Conclusions

1. **The BG coup at DEFCON 2 is deterministic suicide, and the mask is correct to block it unconditionally** (with the Nuclear Subs exception for US, now implemented).

2. **Playing opponent DEFCON-lowering cards for ops at DEFCON 2 is also deterministic suicide**, because game_loop.cpp fires the opponent's event automatically before ops are applied. The card-level mask correctly blocks this.

3. **There are NO genuinely probabilistic DEFCON-1 paths at DEFCON 2 that a rational player would want to take.** Every path to DEFCON-1 from DEFCON 2 is deterministic or near-deterministic (the "random target" events like Brush War and Che still have the event fire deterministically — only the target is random, but the DEFCON drop happens regardless if any BG is targeted).

4. **The Python mask in train_ppo.py is correctly structured** with card-level blocking for opponent DEFCON-lowering cards and mode-level blocking for EVENT and COUP. Neutral DEFCON-lowering cards are correctly allowed for ops (their events don't auto-fire).

5. **The only suppressed plays are at DEFCON 3 during headlines**, where both opponent and neutral DEFCON-lowering cards are blocked. This is conservative but correct — headline resolution order is unpredictable, and a DEFCON drop from 3 to 2 followed by the opponent's headline dropping to 1 is a real risk.

6. **The "last card forced play" scenario (fallback at lines 439-444) is the only genuinely unavoidable DEFCON-1 path.** It is correctly handled: the mask falls back to allowing all cards, and the -1.5 penalty propagates backward through GAE to penalize the hand-management decisions that created the forced situation.

7. **The current mask and C++ learned_policy.cpp mask are consistent in their approach** — both block opponent DEFCON-lowering cards at card-selection level and use belt-and-suspenders mode blocking. The C++ version is slightly more aggressive (also blocks at mode level with heuristic fallback), which is appropriate for MCTS where mode selection interacts with search.

8. **SALT Negotiations (#92) is conservatively blocked at DEFCON 2 but its event actually RAISES DEFCON** (card_spec says it "affects DEFCON" but the event raises it). This is a false positive in the danger set but has negligible impact — at DEFCON 2, the player would prefer to play other cards anyway, and SALT's 4 ops are not irreplaceable.

## Recommendations

1. **No changes needed to the Python mask in train_ppo.py.** The mask correctly blocks all deterministic DEFCON-1 paths and does not suppress any rational risk-taking.

2. **Consider removing SALT Negotiations (#92) from kDefconLoweringCards** — its event raises DEFCON, not lowers it. However, this is very low priority since the false-positive impact is negligible (SALT at DEFCON 2 would raise DEFCON to 3, which is benign but the mask prevents it). Leave for a future cleanup pass.

3. **The -1.5 reward penalty for DEFCON-1 losses remains appropriate.** Since all DEFCON-1 paths at DEFCON 2 are deterministic (not probabilistic), the penalty is always penalizing a genuinely bad decision (or a forced situation that traces back to bad hand management).

4. **No "rational risk-taking regime" exists at DEFCON 2** that the mask is suppressing. The concern from the task description — that probabilistic DEFCON paths might be rationally worth taking when behind — does not apply because there are no probabilistic paths at DEFCON 2.

5. **At DEFCON 3, the mask correctly allows calculated risk** during action rounds. A player can choose to dump an opponent's DEFCON-lowering card for ops at DEFCON 3, accepting the DEFCON drop to 2. This is a legitimate strategic choice and the mask does not block it.

6. **Monitor for one edge case**: the `apply_ops_randomly` function (game_loop.cpp:207-212) has its own DEFCON-2 safety guard that falls back to influence placement when coup would lower DEFCON to 1. This means even if Missile Envy or Grain Sales events fire at DEFCON 2, the apply_ops_randomly code prevents the coup. However, the card-level mask blocks these cards before they can be selected, so this is a defense-in-depth redundancy.

## Open Questions

1. **Is SALT Negotiations (#92) event actually safe at DEFCON 2?** The step.cpp code for case 46 (which appears to be the SALT event slot) does `next.defcon = std::min(5, next.defcon + 1)` and sets `salt_active = true`. If 92 maps to a different code path, verify. If SALT always raises DEFCON, it can be safely removed from kDefconLoweringCards.

2. **Does the "forced last card" fallback (lines 439-444) interact with the DEFCON penalty in undesirable ways?** If the model learns to avoid holding opponent DEFCON-lowering cards (which is correct), does it sometimes make worse plays earlier to avoid the forced situation later? This is hard to detect but could be measured by tracking "fraction of games where fallback triggers."

3. **Should the mask block opponent DEFCON-lowering cards at DEFCON 3 during action rounds?** Currently it does not (only during headlines). At DEFCON 3, playing an opponent's card for ops drops DEFCON to 2, which is survivable but restricts future coup targets. A very conservative mask might block this, but it would suppress legitimate "card dumping" strategy. Current behavior (allow during ARs, block during headlines) is correct.
---
