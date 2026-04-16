#include "rule_queries.hpp"

#include <algorithm>

#include "game_data.hpp"
#include "legal_actions.hpp"
#include "scoring.hpp"

namespace ts {

bool is_chernobyl_blocked(const PublicState& pub, Side side, CountryId country_id) {
    return side == Side::USSR &&
        pub.chernobyl_blocked_region.has_value() &&
        country_spec(country_id).region == *pub.chernobyl_blocked_region;
}

bool is_nato_protected(const PublicState& pub, CountryId country_id) {
    const bool in_nato =
        std::find(kNatoWesternEurope.begin(), kNatoWesternEurope.end(), country_id) != kNatoWesternEurope.end();
    if (!pub.nato_active || !in_nato) {
        return false;
    }
    if (country_id == 7 && pub.de_gaulle_active) {
        return false;
    }
    if (country_id == 18 && pub.willy_brandt_active) {
        return false;
    }
    return controls_country(Side::US, country_id, pub);
}

bool is_military_target_blocked(const PublicState& pub, Side side, CountryId country_id) {
    if (is_defcon_restricted(country_id, pub)) {
        return true;
    }
    if (side != Side::USSR) {
        return false;
    }
    return is_nato_protected(pub, country_id) ||
        (pub.us_japan_pact_active && country_id == static_cast<CountryId>(22));
}

bool is_trap_blocked(const PublicState& pub, Side side, CardId card_id) {
    if (card_spec(card_id).is_scoring) {
        return false;
    }
    return (pub.bear_trap_active && side == Side::USSR) || (pub.quagmire_active && side == Side::US);
}

bool nato_prerequisite_met(const PublicState& pub) {
    return pub.warsaw_pact_played || pub.marshall_plan_played || pub.truman_doctrine_played;
}

bool is_card_defcon_blocked(const PublicState& pub, CardId card_id) {
    return pub.defcon <= 2 && is_defcon_lowering_card(card_id);
}

bool is_wargames_event_legal(const PublicState& pub) {
    return pub.defcon == 2;
}

bool is_solidarity_event_legal(const PublicState& pub) {
    return pub.john_paul_ii_played;
}

bool is_event_play_allowed(const PublicState& pub, Side side, CardId card_id) {
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
