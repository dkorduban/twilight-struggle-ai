// Legal action enumeration and factorized random action sampling for the native
// engine.

#pragma once

#include <vector>

#include "adjacency.hpp"
#include "game_state.hpp"
#include "rng.hpp"

namespace ts {

int effective_ops(CardId card_id, const PublicState& pub, Side side);
int vietnam_revolts_ops_bonus(const PublicState& pub, Side side, std::span<const CountryId> targets);
bool is_defcon_restricted(CountryId country_id, const PublicState& pub);
// Returns true if card_id is in the canonical DEFCON-lowering danger list (card_properties.hpp).
[[nodiscard]] bool is_defcon_lowering_card(CardId card_id);
// Returns true if playing this card is blocked by DEFCON safety rules.
// Opponent-owned danger cards: blocked at DEFCON ≤2 or at DEFCON 3 headline.
// Neutral danger cards: blocked at DEFCON ≤3 during headline.
[[nodiscard]] bool is_card_blocked_by_defcon(const PublicState& pub, Side side, CardId card_id);
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
