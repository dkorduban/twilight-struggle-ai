#pragma once

#include <array>
#include <optional>

#include "types.hpp"

namespace ts {

struct PublicState {
    int turn = 0;
    int ar = 0;
    Side phasing = Side::USSR;

    // Positive = USSR lead, negative = US lead.
    int vp = 0;
    int defcon = 5;
    std::array<int, 2> milops = {0, 0};
    std::array<int, 2> space = {0, 0};

    Side china_held_by = Side::USSR;
    bool china_playable = true;

    std::array<InfluenceBlock, 2> influence = {};

    CardSet discard;
    CardSet removed;

    std::array<int, 2> space_attempts = {0, 0};
    std::optional<Side> space_level4_first;
    std::optional<Side> space_level6_first;

    bool warsaw_pact_played = false;
    bool marshall_plan_played = false;
    bool truman_doctrine_played = false;
    bool john_paul_ii_played = false;
    bool nato_active = false;
    bool de_gaulle_active = false;
    bool willy_brandt_active = false;
    bool us_japan_pact_active = false;
    bool nuclear_subs_active = false;
    bool norad_active = false;
    bool shuttle_diplomacy_active = false;
    bool flower_power_active = false;
    bool flower_power_cancelled = false;
    bool salt_active = false;
    bool opec_cancelled = false;
    bool awacs_active = false;
    bool north_sea_oil_extra_ar = false;
    bool glasnost_extra_ar = false;
    bool formosan_active = false;
    bool cuban_missile_crisis_active = false;
    bool vietnam_revolts_active = false;

    bool bear_trap_active = false;
    bool quagmire_active = false;
    bool iran_hostage_crisis_active = false;

    int handicap_ussr = 0;
    int handicap_us = 0;
    std::array<int, 2> ops_modifier = {0, 0};
    std::optional<Region> chernobyl_blocked_region;
    std::optional<Side> latam_coup_bonus;

    uint32_t state_hash = 0;

    [[nodiscard]] int influence_of(Side side, CountryId country_id) const {
        return influence[to_index(side)][country_id];
    }

    void set_influence(Side side, CountryId country_id, int value) {
        influence[to_index(side)][country_id] = static_cast<int16_t>(value);
    }

    [[nodiscard]] bool has_discard(CardId card_id) const {
        return discard.test(card_id);
    }

    [[nodiscard]] bool has_removed(CardId card_id) const {
        return removed.test(card_id);
    }
};

}  // namespace ts
