// Region scoring, final scoring, and board-control helpers for the native
// engine.

#include "scoring.hpp"

#include <algorithm>

#include "adjacency.hpp"
#include "game_data.hpp"

namespace ts {
namespace {

// Europe control is modelled as a sentinel game-winning swing.
constexpr int kGameWinEurope = 9999;

struct RegionVp {
    int presence = 0;
    int domination = 0;
    int control = 0;
};

constexpr std::array<RegionVp, 6> kRegionVp = {{
    {1, 3, kGameWinEurope},
    {3, 7, 9},
    {3, 5, 7},
    {1, 3, 5},
    {2, 5, 6},
    {1, 4, 6},
}};

bool is_scoring_battleground(CountryId country_id, const PublicState& pub) {
    return country_spec(country_id).is_battleground || (country_id == kTaiwanId && pub.formosan_active);
}

struct RegionCounts {
    int battlegrounds = 0;
    int non_battlegrounds = 0;
    int total = 0;
};

Tier compute_tier(
    int total_bgs,
    const RegionCounts& own,
    const RegionCounts& opp
) {
    if (total_bgs > 0 && own.battlegrounds == total_bgs && own.total > opp.total) {
        return Tier::Control;
    }
    if (
        own.total > opp.total &&
        own.battlegrounds > opp.battlegrounds &&
        own.battlegrounds >= 1 &&
        own.non_battlegrounds >= 1
    ) {
        return Tier::Domination;
    }
    if (own.total >= 1) {
        return Tier::Presence;
    }
    return Tier::None;
}

int side_score(
    Side side,
    Tier tier,
    int presence,
    int domination,
    int control,
    int battlegrounds,
    std::span<const CountryId> region_ids,
    const PublicState& pub
) {
    if (tier == Tier::None) {
        return 0;
    }
    const int base = [&]() {
        switch (tier) {
            case Tier::Presence: return presence;
            case Tier::Domination: return domination;
            case Tier::Control: return control;
            case Tier::None: break;
        }
        return 0;
    }();

    const auto& graph = adjacency();
    const auto enemy_anchor = side == Side::US ? kUssrAnchorId : kUsaAnchorId;
    int adjacency_bonus = 0;
    for (const auto cid : region_ids) {
        const auto& neighbors = graph[cid];
        if (
            std::find(neighbors.begin(), neighbors.end(), enemy_anchor) != neighbors.end() &&
            controls_country(side, cid, pub)
        ) {
            ++adjacency_bonus;
        }
    }

    return base + battlegrounds + adjacency_bonus;
}

}  // namespace

bool controls_country(Side side, CountryId country_id, const PublicState& pub) {
    const auto opponent = other_side(side);
    const auto own = pub.influence_of(side, country_id);
    const auto opp = pub.influence_of(opponent, country_id);
    const auto stability = country_spec(country_id).stability;
    return own >= opp + stability;
}

ScoringResult score_southeast_asia(const PublicState& pub) {
    static constexpr std::array<std::pair<CountryId, int>, 7> kSeAsiaVp = {{
        {75, 1}, {76, 1}, {77, 1}, {78, 1}, {79, 2}, {80, 1}, {84, 1},
    }};

    int delta = 0;
    for (const auto& [country_id, value] : kSeAsiaVp) {
        if (controls_country(Side::USSR, country_id, pub)) {
            delta += value;
        }
        if (controls_country(Side::US, country_id, pub)) {
            delta -= value;
        }
    }
    ScoringResult result;
    result.vp_delta = delta;
    return result;
}

int score_asia_china_bonus(const PublicState& pub) {
    return pub.china_held_by == Side::USSR ? 1 : -1;
}

ScoringResult score_region(Region region, const PublicState& pub) {
    if (region == Region::SoutheastAsia) {
        return score_southeast_asia(pub);
    }

    std::vector<CountryId> region_ids;
    std::vector<CountryId> battleground_ids;
    for (const auto cid : all_country_ids()) {
        if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
            continue;
        }
        if (country_spec(cid).region != region) {
            continue;
        }
        region_ids.push_back(cid);
        if (is_scoring_battleground(cid, pub)) {
            battleground_ids.push_back(cid);
        }
    }

    int total_bgs = static_cast<int>(battleground_ids.size());
    bool shuttle_used = false;
    if (pub.shuttle_diplomacy_active && (region == Region::Asia || region == Region::MiddleEast)) {
        if (!battleground_ids.empty()) {
            const auto top_bg = *std::max_element(
                battleground_ids.begin(),
                battleground_ids.end(),
                [](CountryId lhs, CountryId rhs) {
                    return country_spec(lhs).stability < country_spec(rhs).stability;
                }
            );
            battleground_ids.erase(std::remove(battleground_ids.begin(), battleground_ids.end(), top_bg), battleground_ids.end());
            region_ids.erase(std::remove(region_ids.begin(), region_ids.end(), top_bg), region_ids.end());
            total_bgs = static_cast<int>(battleground_ids.size());
            shuttle_used = true;
        }
    }

    auto count = [&](Side side) {
        RegionCounts counts;
        for (const auto cid : battleground_ids) {
            if (controls_country(side, cid, pub)) {
                ++counts.battlegrounds;
            }
        }
        for (const auto cid : region_ids) {
            if (std::find(battleground_ids.begin(), battleground_ids.end(), cid) != battleground_ids.end()) {
                continue;
            }
            if (controls_country(side, cid, pub)) {
                ++counts.non_battlegrounds;
            }
        }
        counts.total = counts.battlegrounds + counts.non_battlegrounds;
        return counts;
    };

    const auto ussr = count(Side::USSR);
    const auto us = count(Side::US);
    const auto ussr_tier = compute_tier(total_bgs, ussr, us);
    const auto us_tier = compute_tier(total_bgs, us, ussr);
    const auto vp = kRegionVp[static_cast<size_t>(region)];

    if (vp.control == kGameWinEurope) {
        if (ussr_tier == Tier::Control) {
            return {.game_over = true, .winner = Side::USSR, .clear_shuttle = shuttle_used};
        }
        if (us_tier == Tier::Control) {
            return {.game_over = true, .winner = Side::US, .clear_shuttle = shuttle_used};
        }
    }

    const auto ussr_score = side_score(
        Side::USSR, ussr_tier, vp.presence, vp.domination, vp.control, ussr.battlegrounds, region_ids, pub
    );
    const auto us_score = side_score(
        Side::US, us_tier, vp.presence, vp.domination, vp.control, us.battlegrounds, region_ids, pub
    );
    ScoringResult result;
    result.vp_delta = ussr_score - us_score;
    result.clear_shuttle = shuttle_used;
    return result;
}

ScoringResult score_asia_final(const PublicState& pub) {
    PublicState temp = pub;
    auto result = score_region(Region::Asia, temp);
    if (!result.game_over) {
        result.vp_delta += score_asia_china_bonus(pub);
    }
    return result;
}

ScoringResult apply_scoring_card(CardId card_id, const PublicState& pub) {
    switch (card_id) {
        case 1: {
            auto result = score_region(Region::Asia, pub);
            if (!result.game_over) {
                result.vp_delta += score_asia_china_bonus(pub);
            }
            return result;
        }
        case 2:
            return score_region(Region::Europe, pub);
        case 3:
            return score_region(Region::MiddleEast, pub);
        case 40:
            return score_region(Region::CentralAmerica, pub);
        case 41:
            return score_southeast_asia(pub);
        case 80:
            return score_region(Region::Africa, pub);
        case 82:
            return score_region(Region::SouthAmerica, pub);
        default:
            throw std::invalid_argument("card is not a scoring card");
    }
}

ScoringResult apply_final_scoring(PublicState pub) {
    int total = 0;
    for (const auto region : {
             Region::Europe,
             Region::Asia,
             Region::MiddleEast,
             Region::CentralAmerica,
             Region::SouthAmerica,
             Region::Africa,
             Region::SoutheastAsia,
         }) {
        auto result = region == Region::Asia
            ? score_asia_final(pub)
            : (region == Region::SoutheastAsia ? score_southeast_asia(pub) : score_region(region, pub));
        total += result.vp_delta;
        if (result.clear_shuttle) {
            pub.shuttle_diplomacy_active = false;
        }
        if (result.game_over) {
            return {.vp_delta = total, .game_over = true, .winner = result.winner};
        }
    }
    ScoringResult result;
    result.vp_delta = total;
    return result;
}

}  // namespace ts
