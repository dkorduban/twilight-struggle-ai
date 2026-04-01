// Legal action enumeration and factorized random action sampling for the native
// engine.

#pragma once

#include <vector>

#include "adjacency.hpp"
#include "game_state.hpp"
#include "rng.hpp"

namespace ts {

int effective_ops(CardId card_id, const PublicState& pub, Side side);
// Cards legal to choose from hand in the current public state.
std::vector<CardId> legal_cards(const CardSet& hand, const PublicState& pub, Side side, bool holds_china);
// Modes legal for a selected card.
std::vector<ActionMode> legal_modes(CardId card_id, const PublicState& pub, Side side);
// Country targets legal for a selected card/mode.
std::vector<CountryId> legal_countries(CardId card_id, ActionMode mode, const PublicState& pub, Side side);
std::vector<ActionEncoding> enumerate_actions(
    const CardSet& hand,
    const PublicState& pub,
    Side side,
    bool holds_china,
    int max_influence_targets = 84
);
std::optional<ActionEncoding> sample_action(
    const CardSet& hand,
    const PublicState& pub,
    Side side,
    bool holds_china,
    Pcg64Rng& rng
);
bool has_legal_action(const CardSet& hand, const PublicState& pub, Side side, bool holds_china);

}  // namespace ts
