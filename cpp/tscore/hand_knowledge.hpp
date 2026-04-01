#pragma once

#include <bitset>
#include <cstdint>

#include "types.hpp"

// ---------------------------------------------------------------------------
// HandKnowledge: causal, online-safe hidden-information state for one player.
//
// This struct tracks everything the *observer* can legitimately deduce about
// the actor's hand from the public replay prefix seen so far.  It is updated
// only by events that are visible at the time they occur; it must never be
// back-filled using future observations.
//
// Invariants (enforced by the reducer):
//   - known_in_hand and known_not_in_hand are disjoint.
//   - possible_hidden is a superset of (actor's true hidden hand).
//     Equivalently: support_mask_false_exclusion_rate == 0.
//     A card is only removed from possible_hidden when we have *proof* it is
//     gone (discarded, removed, in the opponent's hand, etc.).
//   - |known_in_hand| <= hand_size
//   - possible_hidden is disjoint from known_not_in_hand.
//
// IMPORTANT: Never store or derive fields from OfflineSmoothedLabels here.
// This struct is the online inference state; leaking offline-smoothed labels
// would invalidate correctness guarantees during self-play and evaluation.
//
// This header is currently shared documentation plus the storage type. The
// live C++ engine does not fully use it yet, but the contract is kept here so
// future hidden-information work does not drift from the Python semantics.
// ---------------------------------------------------------------------------

namespace ts {

struct HandKnowledge {
    // Which player's hand we are modelling.
    Side observer = Side::Neutral;  // set to the observing side (USSR or US)

    // Cards we have positively observed the actor draw or hold at some point
    // in this replay prefix.  These are definitely in-hand unless a
    // subsequent event (play, discard, transfer) removes them.
    std::bitset<MAX_CARDS> known_in_hand;

    // Cards we know are NOT in the actor's hand: observed in the opponent's
    // hand, discarded, removed, or played by the opponent.
    std::bitset<MAX_CARDS> known_not_in_hand;

    // Support mask: the set of cards that *could* be in the actor's hidden
    // hand given all public observations so far.
    //
    // Correctness requirement: every card actually held by the actor must be
    // a member of possible_hidden OR known_in_hand.  We must never remove a
    // card from possible_hidden unless we have definitive evidence it is gone.
    // This guarantees false_exclusion_rate == 0.
    std::bitset<MAX_CARDS> possible_hidden;

    // Known hand size, excluding the China Card.
    // Derived from draw / play / discard events on the public record.
    uint8_t hand_size = 0;

    // Whether the actor currently holds the China Card.
    // Tracked separately from hand_size per the rules: the China Card does
    // not count toward the hand-size limit.
    bool holds_china = false;
};

} // namespace ts
