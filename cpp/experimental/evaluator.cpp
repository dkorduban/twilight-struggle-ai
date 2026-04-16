#include "evaluator.hpp"

#include <algorithm>
#include <array>
#include <cmath>
#include <string_view>

#include "adjacency.hpp"
#include "game_data.hpp"
#include "profile.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts::experimental {
namespace {

bool is_early_war(int turn) {
    return turn <= 3;
}

CardId scoring_card_for_region(Region region) {
    switch (region) {
        case Region::Asia: return 1;
        case Region::Europe: return 2;
        case Region::MiddleEast: return 3;
        case Region::CentralAmerica: return 40;
        case Region::SoutheastAsia: return 41;
        case Region::Africa: return 80;
        case Region::SouthAmerica: return 82;
    }
    return 0;
}

double scoring_urgency(const GameState& gs, Region region) {
    const auto scoring_card = scoring_card_for_region(region);
    if (scoring_card == 0 || gs.pub.removed.test(scoring_card)) {
        return 0.0;
    }
    if (gs.hands[to_index(Side::USSR)].test(scoring_card) || gs.hands[to_index(Side::US)].test(scoring_card)) {
        return 1.30;
    }
    if (gs.pub.discard.test(scoring_card)) {
        return 0.60;
    }
    return 1.00;
}

int remaining_action_decisions_for_side(const PublicState& pub, Side side) {
    int max_ar = ars_for_turn(pub.turn);
    if (pub.space[to_index(side)] >= 8) {
        max_ar = std::max(max_ar, 8);
    }
    if (side == Side::US && pub.north_sea_oil_extra_ar) {
        ++max_ar;
    }
    return std::max(0, max_ar - pub.ar + 1);
}

CardId card_id_by_name(std::string_view name) {
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        const auto card_id = static_cast<CardId>(raw);
        if (card_spec(card_id).name == name) {
            return card_id;
        }
    }
    return 0;
}

bool card_is_live(const GameState& gs, CardId card_id) {
    return card_id != 0 && !gs.pub.removed.test(card_id);
}

double live_threat_value(const GameState& gs, Side side, std::string_view card_name, double swing) {
    const auto card_id = card_id_by_name(card_name);
    if (card_id == 0 || !card_is_live(gs, card_id)) {
        return 0.0;
    }
    if (gs.pub.discard.test(card_id)) {
        return 0.5 * swing;
    }
    if (gs.hands[to_index(side)].test(card_id) || gs.hands[to_index(other_side(side))].test(card_id)) {
        return swing;
    }
    return 0.8 * swing;
}

bool is_key_access_country(CountryId cid) {
    const auto& name = country_spec(cid).name;
    return name == "Thailand" ||
        name == "Pakistan" ||
        name == "India" ||
        name == "Iran" ||
        name == "Egypt" ||
        name == "Panama" ||
        name == "South Africa" ||
        name == "Angola" ||
        name == "Venezuela";
}

double control_margin_score(const PublicState& pub, Side side, CountryId cid, const HeuristicConfig& config) {
    const auto& spec = country_spec(cid);
    const double region = region_weight(spec.region, config);
    const double battleground = spec.is_battleground ? 1.25 : 1.0;
    const double own = static_cast<double>(pub.influence_of(side, cid));
    const double opp = static_cast<double>(pub.influence_of(other_side(side), cid));
    const double stability = static_cast<double>(spec.stability);
    const bool own_control = controls_country(side, cid, pub);
    const bool opp_control = controls_country(other_side(side), cid, pub);

    double score = 0.1 * (own - opp);
    if (own_control != opp_control) {
        score += (own_control ? 1.0 : -1.0) * (0.95 + 0.22 * stability);
    } else {
        const double own_gap = own - (opp + stability);
        const double opp_gap = opp - (own + stability);
        score += 0.07 * (own_gap - opp_gap);
    }
    return region * battleground * score;
}

double exact_current_scoring_pressure(const GameState& gs, const HeuristicConfig& config) {
    constexpr std::array<std::pair<Region, CardId>, 7> kScoringRegions = {{
        {Region::Europe, 2},
        {Region::Asia, 1},
        {Region::MiddleEast, 3},
        {Region::CentralAmerica, 40},
        {Region::SoutheastAsia, 41},
        {Region::SouthAmerica, 82},
        {Region::Africa, 80},
    }};

    double total = 0.0;
    for (const auto& [region, scoring_card] : kScoringRegions) {
        const double urgency = scoring_urgency(gs, region);
        if (urgency <= 0.0) {
            continue;
        }
        const auto result = scoring_card == 41
            ? score_southeast_asia(gs.pub)
            : apply_scoring_card(scoring_card, gs.pub);
        if (result.game_over) {
            return result.winner == Side::USSR ? 10000.0 : -10000.0;
        }
        total += region_weight(region, config) * urgency * static_cast<double>(result.vp_delta);
    }
    return config.current_scoring_weight * total;
}

double exact_final_scoring_proxy(const PublicState& pub, const HeuristicConfig& config) {
    auto temp = pub;
    const auto final = apply_final_scoring(temp);
    if (final.game_over) {
        if (final.winner == Side::USSR) {
            return config.terminal_bonus;
        }
        if (final.winner == Side::US) {
            return -config.terminal_bonus;
        }
    }
    return config.final_scoring_weight * static_cast<double>(final.vp_delta);
}

struct RegionProfile {
    int total_battlegrounds = 0;
    int own_battlegrounds = 0;
    int opp_battlegrounds = 0;
    int own_non_battlegrounds = 0;
    int opp_non_battlegrounds = 0;
    int own_total = 0;
    int opp_total = 0;
};

RegionProfile region_profile(const PublicState& pub, Side side, Region region) {
    RegionProfile profile;
    for (const auto cid : all_country_ids()) {
        if (cid == kUsaAnchorId || cid == kUssrAnchorId || country_spec(cid).region != region) {
            continue;
        }
        const auto battleground = country_spec(cid).is_battleground || (cid == kTaiwanId && pub.formosan_active);
        if (battleground) {
            ++profile.total_battlegrounds;
        }
        if (controls_country(side, cid, pub)) {
            if (battleground) {
                ++profile.own_battlegrounds;
            } else {
                ++profile.own_non_battlegrounds;
            }
        }
        if (controls_country(other_side(side), cid, pub)) {
            if (battleground) {
                ++profile.opp_battlegrounds;
            } else {
                ++profile.opp_non_battlegrounds;
            }
        }
    }
    profile.own_total = profile.own_battlegrounds + profile.own_non_battlegrounds;
    profile.opp_total = profile.opp_battlegrounds + profile.opp_non_battlegrounds;
    return profile;
}

double europe_control_cliff_score(const PublicState& pub, const HeuristicConfig& config) {
    const auto ussr = region_profile(pub, Side::USSR, Region::Europe);
    const auto us = region_profile(pub, Side::US, Region::Europe);
    const auto total_bgs = static_cast<double>(std::max(1, ussr.total_battlegrounds));

    auto side_cliff = [&](const RegionProfile& own, const RegionProfile& opp) {
        double score = 0.0;
        if (own.own_battlegrounds >= own.total_battlegrounds - 1) {
            score += 0.90;
        }
        if (own.own_battlegrounds == own.total_battlegrounds && own.own_total == opp.own_total) {
            score += 2.10;
        }
        if (own.own_battlegrounds == own.total_battlegrounds && own.own_total == opp.own_total + 1) {
            score += 3.20;
        }
        if (own.own_battlegrounds == own.total_battlegrounds - 1 && own.own_total >= opp.own_total) {
            score += 0.95;
        }
        score += 0.35 * static_cast<double>(own.own_battlegrounds - opp.own_battlegrounds) / total_bgs;
        score += 0.20 * static_cast<double>(own.own_total - opp.own_total);
        return score;
    };

    return region_weight(Region::Europe, config) * (side_cliff(ussr, us) - side_cliff(us, ussr));
}

double battleground_pressure_score(const PublicState& pub, const HeuristicConfig& config) {
    double total = 0.0;
    for (const auto cid : all_country_ids()) {
        const auto& spec = country_spec(cid);
        if (!spec.is_battleground || cid == kUsaAnchorId || cid == kUssrAnchorId) {
            continue;
        }
        const double own = static_cast<double>(pub.influence_of(Side::USSR, cid));
        const double opp = static_cast<double>(pub.influence_of(Side::US, cid));
        total += region_weight(spec.region, config) * std::tanh((own - opp) / std::max(1.0, static_cast<double>(spec.stability)));
    }
    return total;
}

double access_score(const PublicState& pub, const HeuristicConfig& config) {
    const auto ussr_access = accessible_countries(Side::USSR, pub, ActionMode::Influence);
    const auto us_access = accessible_countries(Side::US, pub, ActionMode::Influence);
    double total = 0.0;
    for (const auto cid : all_country_ids()) {
        if (!is_key_access_country(cid)) {
            continue;
        }
        const bool ussr_can = std::find(ussr_access.begin(), ussr_access.end(), cid) != ussr_access.end();
        const bool us_can = std::find(us_access.begin(), us_access.end(), cid) != us_access.end();
        total += region_weight(country_spec(cid).region, config) * static_cast<double>(ussr_can - us_can);
    }
    return total;
}

double overcontrol_score(const PublicState& pub, const HeuristicConfig& config) {
    double total = 0.0;
    for (const auto cid : all_country_ids()) {
        const auto& spec = country_spec(cid);
        const double own_margin = std::max(
            0.0,
            static_cast<double>(pub.influence_of(Side::USSR, cid) - (pub.influence_of(Side::US, cid) + spec.stability))
        );
        const double opp_margin = std::max(
            0.0,
            static_cast<double>(pub.influence_of(Side::US, cid) - (pub.influence_of(Side::USSR, cid) + spec.stability))
        );
        total += region_weight(spec.region, config) * (spec.is_battleground ? 1.25 : 0.85) * (own_margin - opp_margin);
    }
    return total;
}

double expected_milops_edge(const PublicState& pub) {
    const double ussr_shortfall = static_cast<double>(std::max(0, pub.defcon - pub.milops[to_index(Side::USSR)]));
    const double us_shortfall = static_cast<double>(std::max(0, pub.defcon - pub.milops[to_index(Side::US)]));
    return us_shortfall - ussr_shortfall;
}

double defcon_edge(const PublicState& pub, const HeuristicConfig& config) {
    const auto ussr_coups = accessible_countries(Side::USSR, pub, ActionMode::Coup);
    const auto us_coups = accessible_countries(Side::US, pub, ActionMode::Coup);
    auto coup_pressure = [&](const std::vector<CountryId>& candidates) {
        double total = 0.0;
        for (const auto cid : candidates) {
            const auto& spec = country_spec(cid);
            total += region_weight(spec.region, config) * (spec.is_battleground ? 1.0 : 0.35);
        }
        return total;
    };
    return coup_pressure(ussr_coups) - coup_pressure(us_coups);
}

double space_edge(const PublicState& pub) {
    const double level_delta = static_cast<double>(pub.space[to_index(Side::USSR)] - pub.space[to_index(Side::US)]);
    const double first_move_delta =
        static_cast<double>(pub.space_level4_first == Side::USSR) -
        static_cast<double>(pub.space_level4_first == Side::US) +
        static_cast<double>(pub.space_level6_first == Side::USSR) -
        static_cast<double>(pub.space_level6_first == Side::US);
    return level_delta + 0.5 * first_move_delta;
}

double china_edge(const PublicState& pub, const HeuristicConfig& config) {
    double score = 0.0;
    if (pub.china_held_by == Side::USSR) {
        score += pub.china_playable ? config.china_available_value : config.china_unavailable_value;
    } else if (pub.china_held_by == Side::US) {
        score -= pub.china_playable ? config.china_available_value : config.china_unavailable_value;
    }
    if (!pub.removed.test(1)) {
        score += config.china_asia_live_bonus * (pub.china_held_by == Side::USSR ? 1.0 : pub.china_held_by == Side::US ? -1.0 : 0.0);
    }
    return score;
}

double persistent_flag_score(const PublicState& pub, const HeuristicConfig& config) {
    double score = 0.0;
    const double rem_ar_us = static_cast<double>(remaining_action_decisions_for_side(pub, Side::US));
    const double rem_ar_ussr = static_cast<double>(remaining_action_decisions_for_side(pub, Side::USSR));
    if (pub.nato_active) {
        score -= 1.9;
    }
    if (pub.de_gaulle_active) {
        score += 0.8;
    }
    if (pub.willy_brandt_active) {
        score += 0.7;
    }
    if (pub.us_japan_pact_active) {
        score -= 0.65;
    }
    if (pub.nuclear_subs_active) {
        score -= 0.55;
    }
    if (pub.norad_active) {
        score -= config.norad_trigger_weight * (pub.defcon <= 2 ? 2.2 : 1.0);
    }
    if (pub.shuttle_diplomacy_active) {
        score -= 0.5;
    }
    if (pub.flower_power_active && !pub.flower_power_cancelled) {
        score += config.flower_power_war_card_weight * 2.0;
    }
    if (pub.opec_cancelled) {
        score -= 0.25;
    }
    if (pub.awacs_active) {
        score -= 0.35;
    }
    if (pub.north_sea_oil_extra_ar) {
        score -= 2.2 * config.extra_ops_per_ar_weight;
    }
    if (pub.formosan_active) {
        score -= 0.45;
    }
    if (pub.vietnam_revolts_active) {
        score += 0.65;
    }
    if (pub.bear_trap_active) {
        score -= config.trap_ar_weight * std::min(rem_ar_ussr, 1.5);
    }
    if (pub.quagmire_active) {
        score += config.trap_ar_weight * std::min(rem_ar_us, 1.5);
    }
    if (pub.iran_hostage_crisis_active) {
        score += 0.55;
    }
    if (pub.cuban_missile_crisis_active) {
        score += pub.phasing == Side::USSR ? 0.5 * config.cmc_weight : -0.5 * config.cmc_weight;
    }
    if (pub.chernobyl_blocked_region.has_value()) {
        score -= config.chernobyl_need_weight * region_weight(*pub.chernobyl_blocked_region, config);
    }
    if (pub.latam_coup_bonus == Side::USSR) {
        score += 0.45;
    } else if (pub.latam_coup_bonus == Side::US) {
        score -= 0.45;
    }
    score += 0.4 * static_cast<double>(pub.ops_modifier[to_index(Side::USSR)] - pub.ops_modifier[to_index(Side::US)]);
    score += config.extra_ops_per_ar_weight * (rem_ar_ussr * static_cast<double>(pub.ops_modifier[to_index(Side::USSR)] > 0));
    score -= config.extra_ops_per_ar_weight * (rem_ar_us * static_cast<double>(pub.ops_modifier[to_index(Side::US)] > 0));
    return config.persistent_flag_weight * score;
}

double pair_threat_score(const GameState& gs, const HeuristicConfig& config) {
    double score = 0.0;
    if (gs.pub.john_paul_ii_played) {
        score -= config.pair_threat_weight * live_threat_value(gs, Side::US, "Solidarity", 0.8);
    }
    if (gs.pub.iran_hostage_crisis_active) {
        score += 0.40 * config.pair_threat_weight * live_threat_value(gs, Side::USSR, "Terrorism", 0.8);
    }
    if (gs.pub.awacs_active) {
        score -= 0.40 * config.pair_threat_weight * live_threat_value(gs, Side::US, "Muslim Revolution", 0.75);
    }
    if (gs.pub.opec_cancelled) {
        score -= 0.60 * config.pair_threat_weight * live_threat_value(gs, Side::USSR, "OPEC", 0.9);
    }
    const auto iron_lady = card_id_by_name("The Iron Lady");
    if (iron_lady != 0 && (gs.pub.discard.test(iron_lady) || gs.pub.removed.test(iron_lady))) {
        score -= 0.30 * config.pair_threat_weight * live_threat_value(gs, Side::US, "Socialist Governments", 0.7);
    }
    const auto camp_david = card_id_by_name("Camp David Accords");
    if (camp_david != 0 && (gs.pub.discard.test(camp_david) || gs.pub.removed.test(camp_david))) {
        score -= config.pair_threat_weight * live_threat_value(gs, Side::USSR, "Arab-Israeli War", 0.9);
    }
    if (gs.pub.flower_power_active && !gs.pub.flower_power_cancelled) {
        score += config.flower_power_war_card_weight;
    }
    return score;
}

double scoring_card_value(const PublicState& pub, Side holder, CardId card_id, const HeuristicConfig& config) {
    const auto result = apply_scoring_card(card_id, pub);
    if (result.game_over) {
        const auto signed_terminal = result.winner == Side::USSR ? config.terminal_bonus : -config.terminal_bonus;
        return holder == Side::USSR ? signed_terminal : -signed_terminal;
    }
    const double signed_vp = holder == Side::USSR ? static_cast<double>(result.vp_delta) : -static_cast<double>(result.vp_delta);
    return config.scoring_hand_weight * signed_vp;
}

double named_event_value(const PublicState& pub, Side holder, std::string_view name) {
    double score = 0.0;
    if (name == "Duck and Cover") {
        score += holder == Side::US ? 0.6 + 0.2 * static_cast<double>(pub.defcon - 2) : -0.35;
    } else if (name == "Blockade") {
        score += holder == Side::USSR ? 0.75 : -0.25;
    } else if (name == "De-Stalinization" || name == "Decolonization") {
        score += holder == Side::USSR ? (is_early_war(pub.turn) ? 0.95 : 0.45) : -0.2;
    } else if (name == "Marshall Plan") {
        score += holder == Side::US ? (pub.marshall_plan_played ? 0.25 : 0.95) : -0.15;
    } else if (name == "Warsaw Pact Formed") {
        score += holder == Side::USSR ? (pub.warsaw_pact_played ? 0.25 : 0.9) : -0.15;
    } else if (name == "Containment") {
        score += holder == Side::US ? 0.8 : -0.2;
    } else if (name == "Brezhnev Doctrine") {
        score += holder == Side::USSR ? 0.8 : -0.2;
    } else if (name == "Red Scare/Purge") {
        score += holder == Side::USSR ? 0.7 : -0.2;
    } else if (name == "Wargames") {
        if (pub.defcon == 2 && pub.turn >= 8) {
            score += holder == Side::US ? 1.4 : -1.4;
        }
    } else if (name == "Ask Not What Your Country Can Do For You") {
        score += holder == Side::US ? 0.85 : -0.2;
    } else if (name == "Lone Gunman") {
        score += holder == Side::USSR ? 0.45 : -0.15;
    } else if (name == "Brush War") {
        score += holder == Side::USSR ? 0.45 : 0.3;
    }
    return score;
}

double opponent_max_ops_card(const GameState& gs, Side side) {
    int best = 2;
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        const auto card_id = static_cast<CardId>(raw);
        if (!gs.hands[to_index(other_side(side))].test(card_id)) {
            continue;
        }
        best = std::max(best, card_spec(card_id).ops);
    }
    return static_cast<double>(best);
}

double best_bad_event_in_hand(const GameState& gs, Side side) {
    double best = 0.0;
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        const auto card_id = static_cast<CardId>(raw);
        if (!gs.hands[to_index(side)].test(card_id)) {
            continue;
        }
        const auto& spec = card_spec(card_id);
        if (spec.side == other_side(side) && !spec.is_scoring) {
            best = std::max(best, 0.5 + 0.1 * static_cast<double>(spec.ops));
        }
    }
    return best;
}

double unknown_scoring_count(const GameState& gs, Side side) {
    double total = 0.0;
    for (const auto region : {Region::Europe, Region::Asia, Region::MiddleEast, Region::CentralAmerica, Region::SouthAmerica, Region::Africa, Region::SoutheastAsia}) {
        const auto card_id = scoring_card_for_region(region);
        if (card_id == 0 || gs.pub.removed.test(card_id) || gs.hands[to_index(side)].test(card_id)) {
            continue;
        }
        total += 1.0;
    }
    return total;
}

double special_hand_override(const GameState& gs, Side side, CardId card_id, const HeuristicConfig& config) {
    const auto& name = card_spec(card_id).name;
    if (name == "Wargames") {
        if (gs.pub.defcon == 2 && gs.pub.turn >= 8) {
            if (side == Side::USSR && gs.pub.vp > 6) {
                return 0.5 * config.terminal_bonus;
            }
            if (side == Side::US && gs.pub.vp < -6) {
                return 0.5 * config.terminal_bonus;
            }
        }
        return 0.0;
    }
    if (name == "Missile Envy") {
        return 0.4 + 0.5 * (opponent_max_ops_card(gs, side) - 2.0);
    }
    if (name == "Defectors") {
        return gs.pub.ar == 0 ? 0.8 : 0.1;
    }
    if (name == "UN Intervention") {
        return 0.8 * best_bad_event_in_hand(gs, side);
    }
    if (name == "CIA Created" || name == "Lone Gunman" || name == "Aldrich Ames Remix" || name == "Cambridge Five" || name == "Our Man in Tehran") {
        double info = unknown_scoring_count(gs, side) + 0.15 * static_cast<double>(gs.hands[to_index(other_side(side))].count());
        if (name == "Cambridge Five") {
            info = unknown_scoring_count(gs, side);
        } else if (name == "Aldrich Ames Remix") {
            info += 0.5;
        } else if (name == "Our Man in Tehran") {
            info += 0.35;
        }
        return config.info_card_weight * info;
    }
    if (name == "Ask Not What Your Country Can Do For You") {
        return 0.85;
    }
    if (name == "Star Wars") {
        return 0.75;
    }
    if (name == "Grain Sales to Soviets") {
        return 0.45;
    }
    if (name == "Cultural Revolution" || name == "Nixon Plays the China Card" || name == "Ussuri River Skirmish") {
        if (gs.pub.china_held_by == other_side(side)) {
            return config.china_available_value;
        }
        return 0.3 * config.china_available_value;
    }
    return 0.0;
}

double hand_shape_score(const GameState& gs, const HeuristicConfig& config) {
    auto side_value = [&](Side holder) {
        double total = 0.0;
        for (int raw = 1; raw <= kMaxCardId; ++raw) {
            const auto card_id = static_cast<CardId>(raw);
            if (!gs.hands[to_index(holder)].test(card_id)) {
                continue;
            }
            const auto& spec = card_spec(card_id);
            if (spec.is_scoring) {
                total += scoring_card_value(gs.pub, holder, card_id, config);
                continue;
            }

            double card_score = config.hand_ops_weight * static_cast<double>(spec.ops);
            if (spec.side == holder) {
                card_score += config.event_hand_weight * (config.own_event_bonus_weight + (spec.starred ? config.starred_event_bonus_weight : 0.0));
            } else if (spec.side == other_side(holder)) {
                card_score -= config.event_hand_weight * (config.opp_event_penalty_weight + 0.08 * static_cast<double>(spec.ops));
            } else {
                card_score += config.event_hand_weight * config.neutral_event_bonus_weight;
            }
            card_score += config.event_hand_weight * named_event_value(gs.pub, holder, spec.name);
            card_score += config.special_hand_weight * special_hand_override(gs, holder, card_id, config);
            total += card_score;
        }
        return total;
    };

    double score = side_value(Side::USSR) - side_value(Side::US);
    if (gs.pub.china_playable) {
        if (gs.pub.china_held_by == Side::USSR) {
            score += config.playable_china_bonus;
        } else if (gs.pub.china_held_by == Side::US) {
            score -= config.playable_china_bonus;
        }
    }
    return score;
}

double structural_score(const GameState& gs, const HeuristicConfig& config) {
    double total = 0.0;
    total += config.bg_pressure_weight * battleground_pressure_score(gs.pub, config);
    total += config.access_weight * access_score(gs.pub, config);
    total += config.overcontrol_weight * overcontrol_score(gs.pub, config);
    total += 0.65 * europe_control_cliff_score(gs.pub, config);
    total += config.milops_edge_weight * expected_milops_edge(gs.pub);
    total += config.defcon_edge_weight * defcon_edge(gs.pub, config);
    total += config.space_edge_weight * space_edge(gs.pub);
    total += config.china_edge_weight * china_edge(gs.pub, config);
    total += config.board_control_weight * [&]() {
        double raw = 0.0;
        for (const auto cid : all_country_ids()) {
            if (cid == kUsaAnchorId || cid == kUssrAnchorId) {
                continue;
            }
            raw += control_margin_score(gs.pub, Side::USSR, cid, config);
        }
        return raw;
    }();
    return total;
}

}  // namespace

double evaluate_public_state_ussr(const PublicState& pub, const HeuristicConfig& config) {
    auto [over, winner] = check_vp_win(pub);
    if (over) {
        if (winner == Side::USSR) {
            return config.terminal_bonus;
        }
        if (winner == Side::US) {
            return -config.terminal_bonus;
        }
    }

    double score = config.vp_weight * static_cast<double>(pub.vp);
    score += exact_final_scoring_proxy(pub, config);
    score += persistent_flag_score(pub, config);
    return score;
}

double evaluate_state_for_side(const GameState& gs, Side side, const HeuristicConfig& config) {
    const profile::ScopedTimer timer(profile::Slot::EvaluateState);
    double score = evaluate_public_state_ussr(gs.pub, config);
    score += exact_current_scoring_pressure(gs, config);
    score += structural_score(gs, config);
    score += pair_threat_score(gs, config);
    score += hand_shape_score(gs, config);
    return side == Side::USSR ? score : -score;
}

double evaluate_terminal_for_side(std::optional<Side> winner, Side side, const HeuristicConfig& config) {
    if (winner == side) {
        return config.terminal_bonus;
    }
    if (winner == other_side(side)) {
        return -config.terminal_bonus;
    }
    return 0.0;
}

}  // namespace ts::experimental
