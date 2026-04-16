#pragma once

#include <array>

#include "game_state.hpp"

namespace ts {

inline constexpr CardId kNatoCardId = static_cast<CardId>(21);
inline constexpr CardId kWargamesCardId = static_cast<CardId>(103);
inline constexpr CardId kSolidarityCardId = static_cast<CardId>(104);
inline constexpr std::array<CountryId, 12> kNatoWesternEurope = {1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18};

[[nodiscard]] bool is_chernobyl_blocked(const PublicState& pub, Side side, CountryId country_id);

[[nodiscard]] bool is_nato_protected(const PublicState& pub, CountryId country_id);

[[nodiscard]] bool is_military_target_blocked(const PublicState& pub, Side side, CountryId country_id);

// Returns true when Bear Trap / Quagmire forbids non-scoring card Event/Space play.
[[nodiscard]] bool is_trap_blocked(const PublicState& pub, Side side, CardId card_id);

// NATO is only playable after Warsaw Pact, Marshall Plan, or Truman Doctrine.
[[nodiscard]] bool nato_prerequisite_met(const PublicState& pub);

[[nodiscard]] bool is_card_defcon_blocked(const PublicState& pub, CardId card_id);

[[nodiscard]] bool is_wargames_event_legal(const PublicState& pub);

[[nodiscard]] bool is_solidarity_event_legal(const PublicState& pub);

[[nodiscard]] bool is_event_play_allowed(const PublicState& pub, Side side, CardId card_id);

}  // namespace ts
