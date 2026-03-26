#pragma once

#include <bitset>
#include <cstdint>

#include "types.hpp"

// ---------------------------------------------------------------------------
// PublicState: the fully-observable board state at a single point in time.
//
// This struct holds only information that both players can see without any
// private knowledge.  It is the authoritative input for:
//   - legality checks
//   - public-state hashing / deterministic replay regression
//   - feature extraction for the value / policy network
//
// Invariants (enforced by the reducer, not by this struct):
//   - defcon in [1, 5]
//   - turn in [1, 10]
//   - ar in [1, 8]  (headline = AR 0 by convention in the reducer)
//   - vp in [-20, 20]  (positive = US lead)
//   - milops[p] in [0, 5]
//   - space_level[p] in [0, 8]
//   - deck_remaining, discard, removed are pairwise disjoint (modulo the
//     China Card, which is tracked via china_held_by / china_playable).
//
// No methods are defined here.  All mutation goes through the reducer.
// ---------------------------------------------------------------------------

namespace ts {

struct PublicState {
    // ------------------------------------------------------------------
    // Per-country influence.
    // Indexed as influence[Superpower][CountryId].
    // Only non-negative values are legal on the actual board; the int8_t
    // type is used so that arithmetic in the reducer doesn't silently wrap.
    // ------------------------------------------------------------------
    Influence influence[2][MAX_COUNTRIES] = {};

    // ------------------------------------------------------------------
    // Per-player scalars
    // ------------------------------------------------------------------
    Ops  milops[2]      = {};   // military operations this turn; resets each turn
    uint8_t space_level[2] = {};  // 0..8

    // ------------------------------------------------------------------
    // Global scalars
    // ------------------------------------------------------------------
    int8_t  vp     = 0;    // Victory Points: positive = US lead, negative = USSR lead
    uint8_t defcon = 5;    // 1..5
    uint8_t turn   = 1;    // 1..10
    uint8_t ar     = 1;    // Action Round within the turn (headline = 0 by convention)

    Superpower phasing        = Superpower::USSR;  // whose action round it is
    Superpower china_held_by  = Superpower::USSR;  // who currently holds the China Card
    bool       china_playable = true;              // face-up (playable) vs. face-down

    // ------------------------------------------------------------------
    // Card location sets
    // Bit i is set if card with CardId == i is in that set.
    // China Card membership is tracked separately above.
    // ------------------------------------------------------------------
    std::bitset<MAX_CARDS> deck_remaining;  // cards not yet drawn / in play
    std::bitset<MAX_CARDS> discard;         // discarded cards
    std::bitset<MAX_CARDS> removed;         // permanently removed from game

    // ------------------------------------------------------------------
    // Deterministic Zobrist hash of all fields above.
    // Recomputed by the reducer on every state transition.
    // Used for golden-log regression and deduplication.
    // ------------------------------------------------------------------
    uint32_t state_hash = 0;
};

} // namespace ts
