#pragma once

#include <random>
#include <vector>

#include "adjacency.hpp"
#include "game_state.hpp"

namespace ts {

int effective_ops(CardId card_id, const PublicState& pub, Side side);
std::vector<CardId> legal_cards(const CardSet& hand, const PublicState& pub, Side side, bool holds_china);
std::vector<ActionMode> legal_modes(CardId card_id, const PublicState& pub, Side side);
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
    std::mt19937& rng
);
bool has_legal_action(const CardSet& hand, const PublicState& pub, Side side, bool holds_china);

}  // namespace ts
