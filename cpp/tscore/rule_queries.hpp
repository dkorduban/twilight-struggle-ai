#pragma once

#include "game_data.hpp"
#include "legal_actions.hpp"

namespace ts {

inline constexpr CardId kNatoCardId = static_cast<CardId>(21);
inline constexpr CardId kWargamesCardId = static_cast<CardId>(103);
inline constexpr CardId kSolidarityCardId = static_cast<CardId>(104);

[[nodiscard]] inline bool is_chernobyl_blocked(const PublicState& pub, Side side, CountryId country_id) {
    return side == Side::USSR &&
        pub.chernobyl_blocked_region.has_value() &&
        country_spec(country_id).region == *pub.chernobyl_blocked_region;
}

[[nodiscard]] inline bool is_trap_blocked(const PublicState& pub, Side side, CardId card_id) {
    if (card_spec(card_id).is_scoring) {
        return false;
    }
    return (pub.bear_trap_active && side == Side::USSR) || (pub.quagmire_active && side == Side::US);
}

[[nodiscard]] inline bool nato_prerequisite_met(const PublicState& pub) {
    return pub.warsaw_pact_played || pub.marshall_plan_played || pub.truman_doctrine_played;
}

[[nodiscard]] inline bool is_card_defcon_blocked(const PublicState& pub, CardId card_id) {
    return pub.defcon <= 2 && is_defcon_lowering_card(card_id);
}

[[nodiscard]] inline bool is_wargames_event_legal(const PublicState& pub) {
    return pub.defcon == 2;
}

[[nodiscard]] inline bool is_solidarity_event_legal(const PublicState& pub) {
    return pub.john_paul_ii_played;
}

[[nodiscard]] inline bool is_event_play_allowed(const PublicState& pub, Side side, CardId card_id) {
    if (is_card_defcon_blocked(pub, card_id)) {
        return false;
    }
    if (is_trap_blocked(pub, side, card_id)) {
        return false;
    }
    if (card_id == kNatoCardId && !nato_prerequisite_met(pub)) {
        return false;
    }
    if (card_id == kWargamesCardId && !is_wargames_event_legal(pub)) {
        return false;
    }
    if (card_id == kSolidarityCardId && !is_solidarity_event_legal(pub)) {
        return false;
    }
    return true;
}

}  // namespace ts
