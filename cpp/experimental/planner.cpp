#include "planner.hpp"

#include <array>
#include <algorithm>
#include <cmath>
#include <limits>
#include <sstream>
#include <unordered_set>

#include "adjacency.hpp"
#include "callback_script.hpp"
#include "evaluator.hpp"
#include "game_data.hpp"
#include "hand_ops.hpp"
#include "legal_actions.hpp"
#include "profile.hpp"
#include "rule_queries.hpp"
#include "search.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts::experimental {
namespace {

bool holds_china_for(const GameState& gs, Side side) {
    return side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
}

enum class ProposalMode : uint8_t {
    Event = 0,
    Ops = 1,
    Space = 2,
};

enum class TemplateKind : uint8_t {
    None = 0,
    CoupBg = 1,
    CoupNonBgMilops = 2,
    RealignLinchpin = 3,
    DefendControl = 4,
    BreakControl = 5,
    GainAccess = 6,
    PrepScoring = 7,
    OverprotectBg = 8,
};

struct ScoredConcreteAction {
    ActionEncoding action;
    ProposalMode mode = ProposalMode::Event;
    TemplateKind templ = TemplateKind::None;
    double score = -std::numeric_limits<double>::infinity();
};

constexpr int kCardK = 5;
constexpr int kModeK = 2;
constexpr int kCoupK = 4;
constexpr int kRealignK = 4;
constexpr int kEventK = 4;
constexpr int kInfluenceK = 6;
constexpr std::array<int, 8> kSpaceOpsMinimum = {2, 2, 3, 3, 4, 4, 5, 5};
constexpr std::array<CountryId, 12> kNatoWestEurope = {1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18};

int count_scoring_cards(const CardSet& hand) {
    int total = 0;
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        const auto card_id = static_cast<CardId>(raw);
        if (hand.test(card_id) && card_spec(card_id).is_scoring) {
            ++total;
        }
    }
    return total;
}

bool has_eligible_opponent_card(const CardSet& hand, Side side) {
    const auto opponent = other_side(side);
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        const auto card_id = static_cast<CardId>(raw);
        if (!hand.test(card_id) || card_id == kChinaCardId) {
            continue;
        }
        const auto& spec = card_spec(card_id);
        if (spec.side == opponent && !spec.is_scoring) {
            return true;
        }
    }
    return false;
}

bool nato_protected(CountryId country_id, const PublicState& pub) {
    if (!pub.nato_active) {
        return false;
    }
    if (std::find(kNatoWestEurope.begin(), kNatoWestEurope.end(), country_id) == kNatoWestEurope.end()) {
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

std::vector<CountryId> filtered_accessible_countries_cached(Side side, const PublicState& pub, ActionMode mode) {
    auto base = accessible_countries(side, pub, mode);
    if (mode == ActionMode::Influence) {
        base.erase(
            std::remove_if(
                base.begin(),
                base.end(),
                [&](CountryId cid) { return is_chernobyl_blocked(pub, side, cid); }
            ),
            base.end()
        );
        return base;
    }

    base.erase(
        std::remove_if(
            base.begin(),
            base.end(),
            [&](CountryId cid) {
                return is_defcon_restricted(cid, pub) ||
                    (side == Side::USSR && (nato_protected(cid, pub) || (pub.us_japan_pact_active && cid == 22)));
            }
        ),
        base.end()
    );
    return base;
}

struct LegalContext {
    std::vector<CountryId> influence;
    std::vector<CountryId> coup;
    std::vector<CountryId> realign;
    bool can_space = false;
    int space_ops_min = 99;
    bool has_opponent_card = false;
};

LegalContext build_legal_context(const GameState& gs, Side side) {
    const auto& pub = gs.pub;
    LegalContext ctx;
    ctx.influence = filtered_accessible_countries_cached(side, pub, ActionMode::Influence);
    ctx.coup = filtered_accessible_countries_cached(side, pub, ActionMode::Coup);
    ctx.realign = filtered_accessible_countries_cached(side, pub, ActionMode::Realign);
    const auto level = pub.space[to_index(side)];
    const auto opp_level = pub.space[to_index(other_side(side))];
    const auto max_space = (level >= 2 && opp_level < 2) ? 2 : 1;
    ctx.can_space = (level < 8 && pub.space_attempts[to_index(side)] < max_space);
    ctx.space_ops_min = kSpaceOpsMinimum[static_cast<size_t>(std::min(level, 7))];
    ctx.has_opponent_card = has_eligible_opponent_card(gs.hands[to_index(side)], side);
    return ctx;
}

std::vector<ActionMode> legal_modes_from_context(
    const GameState& gs,
    Side side,
    CardId card_id,
    const LegalContext& ctx
) {
    const auto& pub = gs.pub;
    const auto& spec = card_spec(card_id);
    std::vector<ActionMode> modes;

    if (spec.ops > 0) {
        if (!ctx.influence.empty()) {
            modes.push_back(ActionMode::Influence);
            if (spec.side == other_side(side)) {
                modes.push_back(ActionMode::EventFirst);
            }
        }
        if (!ctx.coup.empty()) {
            modes.push_back(ActionMode::Coup);
        }
        if (!ctx.realign.empty()) {
            modes.push_back(ActionMode::Realign);
        }
        if (ctx.can_space && effective_ops(card_id, pub, side) >= ctx.space_ops_min) {
            modes.push_back(ActionMode::Space);
        }
    }

    modes.push_back(ActionMode::Event);

    if (card_id == kNatoCardId && !nato_prerequisite_met(pub)) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
    }
    if (is_trap_blocked(pub, side, card_id)) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Space), modes.end());
    }
    if (card_id == kWargamesCardId && !is_wargames_event_legal(pub)) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
    }
    if (card_id == kSolidarityCardId && !is_solidarity_event_legal(pub)) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
    }
    if (card_id == 32 && !ctx.has_opponent_card) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
    }

    std::sort(modes.begin(), modes.end(), [](ActionMode lhs, ActionMode rhs) {
        return static_cast<int>(lhs) < static_cast<int>(rhs);
    });
    modes.erase(std::unique(modes.begin(), modes.end()), modes.end());
    return modes;
}

int remaining_action_decisions_for_side(const GameState& state, Side side) {
    int max_ar = ars_for_turn(state.pub.turn);
    if (state.pub.space[to_index(side)] >= 8) {
        max_ar = std::max(max_ar, 8);
    }
    if (side == Side::US && state.pub.north_sea_oil_extra_ar) {
        ++max_ar;
    }
    return std::max(1, max_ar - state.pub.ar + 1);
}

bool must_play_scoring_card(const GameState& state, Side side) {
    if (state.pub.ar <= 0) {
        return false;
    }
    return count_scoring_cards(state.hands[to_index(side)]) >= remaining_action_decisions_for_side(state, side);
}

void sync_china(GameState& gs) {
    gs.ussr_holds_china = gs.pub.china_held_by == Side::USSR;
    gs.us_holds_china = gs.pub.china_held_by == Side::US;
}

struct ActionEncodingHash {
    size_t operator()(const ActionEncoding& action) const noexcept {
        size_t hash = static_cast<size_t>(action.card_id) * 1315423911u
            ^ (static_cast<size_t>(action.mode) << 17);
        for (const auto target : action.targets) {
            hash ^= static_cast<size_t>(target) + 0x9e3779b97f4a7c15ULL + (hash << 6) + (hash >> 2);
        }
        return hash;
    }
};

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

bool side_knows_scoring_now(const GameState& gs, CardId scoring_card) {
    return gs.hands[to_index(Side::USSR)].test(scoring_card) || gs.hands[to_index(Side::US)].test(scoring_card);
}

double scoring_urgency(const GameState& gs, Region region) {
    const auto scoring_card = scoring_card_for_region(region);
    if (scoring_card == 0) {
        return 0.0;
    }
    if (gs.pub.removed.test(scoring_card)) {
        return 0.0;
    }
    if (side_knows_scoring_now(gs, scoring_card)) {
        return 1.30;
    }
    if (gs.pub.discard.test(scoring_card)) {
        return 0.60;
    }
    return 1.00;
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

int side_country_count_in_region(const PublicState& pub, Side side, Region region);
int side_battleground_count_in_region(const PublicState& pub, Side side, Region region);

void apply_target_counts(PublicState& pub, Side side, const std::array<int, kCountrySlots>& target_counts);

bool europe_control_pressure(const PublicState& pub, Side side) {
    const auto profile = region_profile(pub, side, Region::Europe);
    return profile.total_battlegrounds > 0 &&
        profile.opp_battlegrounds >= profile.total_battlegrounds - 1 &&
        profile.own_total <= profile.opp_total + 1;
}

double region_score_value_for_side(const PublicState& pub, Side side, Region region, const HeuristicConfig& config) {
    const auto scoring_card = scoring_card_for_region(region);
    const auto result = scoring_card == 41 ? score_southeast_asia(pub) : apply_scoring_card(scoring_card, pub);
    if (result.game_over) {
        return result.winner == side ? config.terminal_bonus : -config.terminal_bonus;
    }
    return side == Side::USSR ? static_cast<double>(result.vp_delta) : -static_cast<double>(result.vp_delta);
}

void apply_target_counts(PublicState& pub, Side side, const std::array<int, kCountrySlots>& target_counts) {
    for (const auto cid : all_country_ids()) {
        const auto extra = target_counts[static_cast<size_t>(cid)];
        if (extra <= 0) {
            continue;
        }
        pub.set_influence(side, cid, pub.influence_of(side, cid) + extra);
    }
}

double exact_region_delta_signal(
    const GameState& gs,
    Side side,
    CountryId cid,
    const std::array<int, kCountrySlots>& target_counts,
    const HeuristicConfig& config
) {
    const auto region = country_spec(cid).region;
    const double urgency = scoring_urgency(gs, region);
    if (urgency <= 0.0) {
        return 0.0;
    }
    auto before = gs.pub;
    apply_target_counts(before, side, target_counts);
    auto after = before;
    after.set_influence(side, cid, after.influence_of(side, cid) + 1);
    const double baseline = region_score_value_for_side(before, side, region, config);
    const double stepped = region_score_value_for_side(after, side, region, config);
    return region_weight(region, config) * urgency * (stepped - baseline);
}

double full_allocation_region_delta(
    const GameState& gs,
    Side side,
    const std::array<int, kCountrySlots>& target_counts,
    const HeuristicConfig& config
) {
    std::array<bool, 7> touched = {};
    for (const auto cid : all_country_ids()) {
        if (target_counts[static_cast<size_t>(cid)] <= 0) {
            continue;
        }
        touched[static_cast<size_t>(country_spec(cid).region)] = true;
    }

    auto after = gs.pub;
    apply_target_counts(after, side, target_counts);

    double total = 0.0;
    for (int region_idx = 0; region_idx < static_cast<int>(touched.size()); ++region_idx) {
        if (!touched[static_cast<size_t>(region_idx)]) {
            continue;
        }
        const auto region = static_cast<Region>(region_idx);
        const double urgency = scoring_urgency(gs, region);
        if (urgency <= 0.0) {
            continue;
        }
        const double before = region_score_value_for_side(gs.pub, side, region, config);
        const double stepped = region_score_value_for_side(after, side, region, config);
        total += region_weight(region, config) * urgency * (stepped - before);
    }
    return total;
}

double region_urgency_for_country(const GameState& gs, CountryId cid, const HeuristicConfig& config) {
    return region_weight(country_spec(cid).region, config) * scoring_urgency(gs, country_spec(cid).region);
}

bool side_has_presence_in_region(const PublicState& pub, Side side, Region region) {
    for (const auto cid : all_country_ids()) {
        if (country_spec(cid).region != region) {
            continue;
        }
        if (pub.influence_of(side, cid) > 0) {
            return true;
        }
    }
    return false;
}

int side_country_count_in_region(const PublicState& pub, Side side, Region region) {
    int total = 0;
    for (const auto cid : all_country_ids()) {
        if (country_spec(cid).region != region) {
            continue;
        }
        if (pub.influence_of(side, cid) > pub.influence_of(other_side(side), cid)) {
            ++total;
        }
    }
    return total;
}

int side_battleground_count_in_region(const PublicState& pub, Side side, Region region) {
    int total = 0;
    for (const auto cid : all_country_ids()) {
        const auto& spec = country_spec(cid);
        if (spec.region != region || !spec.is_battleground) {
            continue;
        }
        if (controls_country(side, cid, pub)) {
            ++total;
        }
    }
    return total;
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

double country_priority(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config) {
    const auto& pub = gs.pub;
    const auto& spec = country_spec(cid);
    const double region = region_weight(spec.region, config) * (0.8 + 0.2 * scoring_urgency(gs, spec.region));
    const double battleground = spec.is_battleground
        ? config.proposal_country_battleground_scale
        : (is_key_access_country(cid) ? config.proposal_country_key_access_scale : config.proposal_country_other_scale);
    const auto own = static_cast<double>(pub.influence_of(side, cid));
    const auto opp = static_cast<double>(pub.influence_of(other_side(side), cid));
    const auto stability = static_cast<double>(spec.stability);
    const double control_gap = (opp + stability) - own;
    const double contested_bonus = opp > 0.0 ? config.proposal_country_contested_scale : 1.0;
    const double own_padding_penalty = (!spec.is_battleground && opp == 0.0 && own > 0.0)
        ? config.proposal_country_safe_nonbg_penalty
        : 1.0;
    return region * battleground * contested_bonus * own_padding_penalty
        * (1.0 - 0.15 * control_gap + 0.04 * (own - opp));
}

double milops_need(const PublicState& pub, Side side) {
    return static_cast<double>(std::max(0, pub.defcon - pub.milops[to_index(side)]));
}

double defend_control_signal(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config) {
    const auto& pub = gs.pub;
    if (!controls_country(side, cid, pub)) {
        return 0.0;
    }
    const auto own = pub.influence_of(side, cid);
    const auto opp = pub.influence_of(other_side(side), cid);
    const auto margin = own - (opp + country_spec(cid).stability);
    return country_priority(gs, side, cid, config) * std::max(0.0, 2.0 - static_cast<double>(margin));
}

double attack_control_signal(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config) {
    const auto& pub = gs.pub;
    const auto opp_side = other_side(side);
    if (!controls_country(opp_side, cid, pub)) {
        return 0.0;
    }
    const auto opp = pub.influence_of(opp_side, cid);
    const auto own = pub.influence_of(side, cid);
    const auto margin = opp - (own + country_spec(cid).stability);
    return country_priority(gs, side, cid, config) * std::max(0.0, 2.5 - static_cast<double>(margin));
}

double country_count_signal(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config);

double europe_support_pressure_signal(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config) {
    const auto& pub = gs.pub;
    const auto& spec = country_spec(cid);
    if (spec.region != Region::Europe || spec.is_battleground) {
        return 0.0;
    }

    const bool own_pressure = europe_control_pressure(pub, side);
    const bool opp_pressure = europe_control_pressure(pub, other_side(side));
    if (!own_pressure && !opp_pressure) {
        return 0.0;
    }

    const int own_countries = side_country_count_in_region(pub, side, Region::Europe);
    const int opp_countries = side_country_count_in_region(pub, other_side(side), Region::Europe);
    const bool gains_count = pub.influence_of(side, cid) + 1 > pub.influence_of(other_side(side), cid);
    double signal = 0.0;
    if (gains_count) {
        signal += opp_pressure ? 1.20 : 0.40;
    }
    if (pub.influence_of(side, cid) == 0) {
        signal += 0.20;
    }
    if (own_countries <= opp_countries) {
        signal += 0.35;
    } else if (own_countries == opp_countries + 1) {
        signal += 0.15;
    }
    if (spec.stability <= 2) {
        signal += 0.15;
    }
    return europe_support_pressure_bonus_for_side(side, config)
        * region_weight(Region::Europe, config)
        * scoring_urgency(gs, Region::Europe)
        * signal;
}

double access_gain_signal(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config) {
    const auto& pub = gs.pub;
    const auto& spec = country_spec(cid);
    const bool fresh_presence = pub.influence_of(side, cid) == 0;
    double score = 0.0;
    if (fresh_presence) {
        score += 0.35;
        if (!side_has_presence_in_region(pub, side, spec.region)) {
            score += 0.35;
        }
    }
    if (is_key_access_country(cid)) {
        score += 0.60;
    }
    if (spec.is_battleground) {
        score += 0.20;
    }
    return region_weight(spec.region, config) * score + country_count_signal(gs, side, cid, config);
}

double country_count_signal(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config) {
    const auto& pub = gs.pub;
    const auto& spec = country_spec(cid);
    const bool fresh_presence = pub.influence_of(side, cid) == 0;
    const int own_countries = side_country_count_in_region(pub, side, spec.region);
    const int opp_countries = side_country_count_in_region(pub, other_side(side), spec.region);
    const int own_bgs = side_battleground_count_in_region(pub, side, spec.region);
    const int opp_bgs = side_battleground_count_in_region(pub, other_side(side), spec.region);

    double score = 0.0;
    if (fresh_presence) {
        score += 0.10;
    }
    if (!spec.is_battleground) {
        if (own_countries <= opp_countries) {
            score += 0.55;
        }
        if (own_bgs >= opp_bgs && own_countries <= opp_countries + 1) {
            score += 0.25;
        }
        if (!side_has_presence_in_region(pub, side, spec.region)) {
            score += 0.15;
        }
    }
    if (spec.region == Region::Europe && !spec.is_battleground) {
        score *= 1.35;
    }
    return config.proposal_country_count_scale
        * region_weight(spec.region, config)
        * scoring_urgency(gs, spec.region)
        * score;
}

double prep_scoring_signal(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config) {
    return country_priority(gs, side, cid, config) * (country_spec(cid).is_battleground ? 0.9 : 0.55)
        * scoring_urgency(gs, country_spec(cid).region)
        + country_count_signal(gs, side, cid, config)
        + europe_support_pressure_signal(gs, side, cid, config);
}

double protect_battleground_signal(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config) {
    if (!country_spec(cid).is_battleground) {
        return 0.0;
    }
    return 0.75 * defend_control_signal(gs, side, cid, config) + 0.35 * country_priority(gs, side, cid, config);
}

double adjacency_edge_signal(const PublicState& pub, Side side, CountryId cid) {
    double total = 0.0;
    for (const auto neighbor : adjacency()[cid]) {
        if (!has_country_spec(neighbor)) {
            continue;
        }
        if (controls_country(side, neighbor, pub)) {
            total += 0.25;
        } else if (controls_country(other_side(side), neighbor, pub)) {
            total -= 0.15;
        }
    }
    return total;
}

double control_fragility_signal(const PublicState& pub, Side side, CountryId cid) {
    const auto opp_side = other_side(side);
    if (!controls_country(opp_side, cid, pub)) {
        return 0.0;
    }
    const auto opp = pub.influence_of(opp_side, cid);
    const auto own = pub.influence_of(side, cid);
    const auto fragility = (own + country_spec(cid).stability) - opp;
    return std::max(0.0, 2.0 + static_cast<double>(fragility));
}

double info_event_bonus(CardId card_id, const HeuristicConfig& config) {
    const auto& name = card_spec(card_id).name;
    if (name == "CIA Created" ||
        name == "Lone Gunman" ||
        name == "The Cambridge Five" ||
        name == "Aldrich Ames Remix" ||
        name == "Our Man in Tehran") {
        return config.info_event_bonus_weight;
    }
    if (name == "Defectors" ||
        name == "UN Intervention" ||
        name == "Missile Envy" ||
        name == "Ask Not What Your Country Can Do For You" ||
        name == "Star Wars" ||
        name == "Grain Sales to Soviets") {
        return 0.55 * config.info_event_bonus_weight;
    }
    return 0.0;
}

double rule_event_bonus(CardId card_id, Side side, const HeuristicConfig& config) {
    const auto& name = card_spec(card_id).name;
    if (name == "Containment" ||
        name == "Brezhnev Doctrine" ||
        name == "Red Scare/Purge" ||
        name == "Vietnam Revolts" ||
        name == "North Sea Oil" ||
        name == "Yuri and Samantha" ||
        name == "Latin American Death Squads" ||
        name == "Iran-Contra Scandal" ||
        name == "Chernobyl" ||
        name == "NORAD" ||
        name == "Quagmire" ||
        name == "Bear Trap" ||
        name == "Cuban Missile Crisis" ||
        name == "Nuclear Subs" ||
        name == "SALT Negotiations" ||
        name == "We Will Bury You" ||
        name == "U2 Incident" ||
        name == "Formosan Resolution" ||
        name == "Shuttle Diplomacy" ||
        name == "NATO" ||
        name == "US/Japan Mutual Defense Pact" ||
        name == "Willy Brandt" ||
        name == "The Reformer" ||
        name == "Flower Power") {
        return card_spec(card_id).side == side ? config.rule_event_bonus_weight : -0.58 * config.rule_event_bonus_weight;
    }
    return 0.0;
}

double scoring_card_event_score(const GameState& gs, Side side, CardId card_id, const HeuristicConfig& config);

double light_event_score(const GameState& gs, Side side, const ActionEncoding& action, const HeuristicConfig& config) {
    const auto& card = card_spec(action.card_id);
    double score = 0.15 * static_cast<double>(card.ops);
    if (card.is_scoring) {
        return scoring_card_event_score(gs, side, action.card_id, config);
    }
    if (card.side == side) {
        score += config.own_event_bonus_weight + 0.10 * static_cast<double>(card.ops)
            + (card.starred ? config.starred_event_bonus_weight : 0.0);
    } else if (card.side == other_side(side)) {
        score -= config.opp_event_penalty_weight + 0.10 * static_cast<double>(card.ops);
    } else {
        score += config.neutral_event_bonus_weight;
    }
    score += info_event_bonus(action.card_id, config);
    score += rule_event_bonus(action.card_id, side, config);
    return score;
}

double scoring_card_event_score(const GameState& gs, Side side, CardId card_id, const HeuristicConfig& config) {
    auto scored = apply_scoring_card(card_id, gs.pub);
    if (scored.game_over) {
        return scored.winner == side ? 1000.0 : -1000.0;
    }
    const auto region = [&]() {
        switch (card_id) {
            case 1: return Region::Asia;
            case 2: return Region::Europe;
            case 3: return Region::MiddleEast;
            case 40: return Region::CentralAmerica;
            case 41: return Region::SoutheastAsia;
            case 80: return Region::Africa;
            case 82: return Region::SouthAmerica;
            default: return Region::Europe;
        }
    }();
    return region_weight(region, config) * scoring_urgency(gs, region) *
        (side == Side::USSR ? static_cast<double>(scored.vp_delta) : -static_cast<double>(scored.vp_delta));
}

double space_mode_score(const GameState& gs, Side side, CardId card_id, const HeuristicConfig& config) {
    const auto& pub = gs.pub;
    const auto& card = card_spec(card_id);
    double toxic_event_penalty = 0.0;
    if (card.side == other_side(side) && !card.is_scoring) {
        toxic_event_penalty = config.space_escape_weight + 0.12 * static_cast<double>(card.ops);
    }
    const double track_gap = static_cast<double>(pub.space[to_index(other_side(side))] - pub.space[to_index(side)]);
    return toxic_event_penalty + 0.35 * track_gap + 0.10 * static_cast<double>(pub.vp) * (side == Side::USSR ? -1.0 : 1.0);
}

double coup_action_score(
    const GameState& gs,
    Side side,
    CountryId cid,
    bool battleground_template,
    CardId card_id,
    const HeuristicConfig& config
) {
    const auto& pub = gs.pub;
    const auto& spec = country_spec(cid);
    const double ops = static_cast<double>(effective_ops(card_id, pub, side));
    const double expected_coup = ops + 3.5 - 2.0 * static_cast<double>(spec.stability);
    const double milops = config.proposal_coup_milops_weight * std::max(0.0, milops_need(pub, side) - 0.5);
    const double scoring = config.proposal_coup_scoring_weight * region_urgency_for_country(gs, cid, config);
    const double access = config.proposal_coup_access_weight * access_gain_signal(gs, side, cid, config);
    const double battleground_bonus =
        battleground_template
            ? config.proposal_coup_bg_template_bonus * static_cast<double>(spec.is_battleground)
            : config.proposal_coup_nonbg_template_bonus * static_cast<double>(!spec.is_battleground);
    const double control_break = controls_country(other_side(side), cid, pub) ? config.proposal_coup_control_break_bonus : 0.0;
    const double defcon_penalty = spec.is_battleground
        ? config.proposal_coup_defcon_penalty * static_cast<double>(std::max(0, 4 - pub.defcon))
        : 0.0;
    const double already_safe_penalty = milops_need(pub, side) <= 0.0 ? config.proposal_coup_safe_penalty : 0.0;
    const double shallow_coup_penalty = expected_coup < 0.75 ? config.proposal_coup_shallow_penalty : 0.0;
    return config.proposal_coup_country_weight * country_priority(gs, side, cid, config)
        + config.proposal_coup_expected_weight * expected_coup
        + milops
        + scoring
        + access
        + battleground_bonus
        + control_break
        - defcon_penalty
        - already_safe_penalty
        - shallow_coup_penalty;
}

double realign_action_score(const GameState& gs, Side side, CountryId cid, const HeuristicConfig& config) {
    const auto& pub = gs.pub;
    return config.proposal_realign_country_weight * country_priority(gs, side, cid, config)
        + config.proposal_realign_adjacency_weight * adjacency_edge_signal(pub, side, cid)
        + config.proposal_realign_fragility_weight * control_fragility_signal(pub, side, cid)
        + config.proposal_realign_scoring_weight * region_urgency_for_country(gs, cid, config);
}

std::pair<TemplateKind, double> influence_template_score(
    const GameState& gs,
    Side side,
    const ActionEncoding& action,
    const HeuristicConfig& config
) {
    std::array<int, kCountrySlots> target_counts = {};
    for (const auto target : action.targets) {
        ++target_counts[static_cast<size_t>(target)];
    }

    double defend = 0.0;
    double attack = 0.0;
    double access = 0.0;
    double prep = 0.0;
    double overprotect = 0.0;
    double local = 0.0;
    double overstack = 0.0;
    const double region_delta = full_allocation_region_delta(gs, side, target_counts, config);
    for (const auto cid : all_country_ids()) {
        const auto placements = target_counts[static_cast<size_t>(cid)];
        if (placements <= 0) {
            continue;
        }
        defend += static_cast<double>(placements) * defend_control_signal(gs, side, cid, config);
        attack += static_cast<double>(placements) * attack_control_signal(gs, side, cid, config);
        access += static_cast<double>(placements) * access_gain_signal(gs, side, cid, config);
        prep += static_cast<double>(placements) * prep_scoring_signal(gs, side, cid, config);
        overprotect += static_cast<double>(placements) * protect_battleground_signal(gs, side, cid, config);
        local += static_cast<double>(placements) * 0.55 * country_priority(gs, side, cid, config);

        const auto& pub = gs.pub;
        const auto& spec = country_spec(cid);
        const double future_own = static_cast<double>(pub.influence_of(side, cid) + placements);
        const double opp = static_cast<double>(pub.influence_of(other_side(side), cid));
        const double softness = spec.is_battleground ? 1.0 : 0.0;
        const double future_excess = future_own - (opp + static_cast<double>(spec.stability) + softness);
        if (future_excess > 0.0) {
            overstack += (spec.is_battleground ? 0.35 : 0.90) * future_excess;
        }
    }
    const std::array<std::pair<TemplateKind, double>, 5> template_scores = {{
        {
            TemplateKind::DefendControl,
            region_delta
                + config.proposal_influence_local_weight * 0.65 * local
                + config.proposal_influence_defend_weight * defend
                + 0.30 * prep
                - config.proposal_influence_overstack_penalty * overstack,
        },
        {
            TemplateKind::BreakControl,
            region_delta
                + config.proposal_influence_local_weight * 0.60 * local
                + config.proposal_influence_attack_weight * attack
                + 0.25 * prep
                - 0.5 * config.proposal_influence_overstack_penalty * overstack,
        },
        {
            TemplateKind::GainAccess,
            region_delta
                + 0.55 * config.proposal_influence_local_weight * local
                + config.proposal_influence_access_weight * access
                + 0.15 * prep,
        },
        {
            TemplateKind::PrepScoring,
            region_delta
                + 0.55 * config.proposal_influence_local_weight * local
                + config.proposal_influence_prep_weight * prep
                + 0.25 * overprotect
                - 0.5 * config.proposal_influence_overstack_penalty * overstack,
        },
        {
            TemplateKind::OverprotectBg,
            region_delta
                + 0.55 * config.proposal_influence_local_weight * local
                + config.proposal_influence_overprotect_weight * overprotect
                + 0.20 * defend
                - 1.25 * config.proposal_influence_overstack_penalty * overstack,
        },
    }};
    const auto best = std::max_element(template_scores.begin(), template_scores.end(), [](const auto& lhs, const auto& rhs) {
        return lhs.second < rhs.second;
    });
    double score = best->second;
    if (action.mode == ActionMode::EventFirst) {
        score -= 0.45;
    }
    return {best->first, score};
}

ScoredConcreteAction score_concrete_action(
    const GameState& gs,
    Side side,
    const ActionEncoding& action,
    const HeuristicConfig& config
) {
    ScoredConcreteAction out{.action = action};
    const auto scoring_backlog_penalty = [&]() {
        if (gs.pub.ar <= 0 || card_spec(action.card_id).is_scoring) {
            return 0.0;
        }
        const int scoring_cards = count_scoring_cards(gs.hands[to_index(side)]);
        if (scoring_cards <= 0) {
            return 0.0;
        }
        const int remaining = remaining_action_decisions_for_side(gs, side);
        if (remaining <= 0) {
            return 0.0;
        }
        const double pressure = static_cast<double>(scoring_cards) / static_cast<double>(remaining);
        double penalty = config.proposal_scoring_backlog_penalty * pressure;
        if (remaining <= scoring_cards + 1) {
            penalty += 0.75 * config.proposal_scoring_backlog_penalty;
        }
        return penalty;
    }();
    switch (action.mode) {
        case ActionMode::Event:
            out.mode = ProposalMode::Event;
            out.templ = TemplateKind::None;
            out.score = card_spec(action.card_id).is_scoring
                ? scoring_card_event_score(gs, side, action.card_id, config)
                : light_event_score(gs, side, action, config);
            out.score -= scoring_backlog_penalty;
            return out;
        case ActionMode::Space:
            out.mode = ProposalMode::Space;
            out.templ = TemplateKind::None;
            out.score = space_mode_score(gs, side, action.card_id, config);
            out.score -= scoring_backlog_penalty;
            return out;
        case ActionMode::Coup:
            out.mode = ProposalMode::Ops;
            out.templ = country_spec(action.targets.front()).is_battleground ? TemplateKind::CoupBg : TemplateKind::CoupNonBgMilops;
            out.score = coup_action_score(gs, side, action.targets.front(), out.templ == TemplateKind::CoupBg, action.card_id, config);
            out.score -= scoring_backlog_penalty;
            return out;
        case ActionMode::Realign:
            out.mode = ProposalMode::Ops;
            out.templ = TemplateKind::RealignLinchpin;
            out.score = realign_action_score(gs, side, action.targets.front(), config);
            out.score -= scoring_backlog_penalty;
            return out;
        case ActionMode::Influence:
        case ActionMode::EventFirst: {
            out.mode = ProposalMode::Ops;
            const auto [templ, score] = influence_template_score(gs, side, action, config);
            out.templ = templ;
            out.score = score - scoring_backlog_penalty;
            return out;
        }
    }
    return out;
}

int mode_index(ProposalMode mode) {
    return static_cast<int>(mode);
}

size_t per_bucket_limit(ProposalMode mode, TemplateKind templ) {
    switch (mode) {
        case ProposalMode::Event:
            return kEventK;
        case ProposalMode::Space:
            return 1;
        case ProposalMode::Ops:
            if (templ == TemplateKind::CoupBg || templ == TemplateKind::CoupNonBgMilops) {
                return kCoupK;
            }
            if (templ == TemplateKind::RealignLinchpin) {
                return kRealignK;
            }
            return kInfluenceK;
    }
    return 1;
}

ResolutionFn make_action_resolution(const ActionEncoding& action, Side side) {
    return [action, side](GameState& gs, Pcg64Rng& rng, const PolicyCallbackFn* policy_cb) {
        auto& hand = gs.hands[to_index(side)];
        if (hand.test(action.card_id)) {
            hand.reset(action.card_id);
        }
        auto [new_pub, over, winner] = apply_action_with_hands(gs, action, side, rng, policy_cb);
        (void)new_pub;
        return ResolutionOutcome{
            .over = over,
            .winner = winner,
        };
    };
}

bool action_needs_script(const ActionEncoding& action) {
    return action.mode == ActionMode::Event || action.mode == ActionMode::EventFirst;
}

std::string describe_action_for_logging(const ActionEncoding& action) {
    std::ostringstream out;
    out << "card=" << static_cast<int>(action.card_id)
        << ":" << card_spec(action.card_id).name
        << " mode=" << static_cast<int>(action.mode)
        << " targets=" << action.targets.size();
    return out.str();
}

PlannedAction plan_action_once(
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config,
    const ActionEncoding& action
) {
    const profile::ScopedTimer timer(profile::Slot::PlanActionOnce);
    const auto resolution = make_action_resolution(action, side);
    const auto action_label = describe_action_for_logging(action);
    const auto script = action_needs_script(action)
        ? solve_callback_script(gs, side, resolution, rng, side, config, action_label)
        : CallbackScript{};

    auto eval_rng = rng;
    const int sample_count = std::max(1, config.rollout_samples);
    double total_score = 0.0;
    for (int sample = 0; sample < sample_count; ++sample) {
        auto sim = gs;
        auto sim_rng = sample_count == 1 ? rng : Pcg64Rng(eval_rng.next_u64());
        const auto replay = make_replay_callback(script);
        const auto outcome = resolution(sim, sim_rng, &replay);
        sync_china(sim);
        total_score += outcome.over
            ? evaluate_terminal_for_side(outcome.winner, side, config)
            : evaluate_state_for_side(sim, side, config);
    }
    const double static_score = total_score / static_cast<double>(sample_count);
    return PlannedAction{
        .action = action,
        .script = script,
        .static_score = static_score,
        .rollout_score = static_score,
        .search_visits = 0,
    };
}

std::vector<ActionEncoding> headline_candidates(const GameState& gs, Side side) {
    std::vector<ActionEncoding> actions;
    for (const auto card_id : legal_cards(gs.hands[to_index(side)], gs.pub, side, holds_china_for(gs, side))) {
        if (card_id == kChinaCardId) {
            continue;
        }
        actions.push_back(ActionEncoding{
            .card_id = card_id,
            .mode = ActionMode::Event,
            .targets = {},
        });
    }
    return actions;
}

double marginal_placement_score(
    const GameState& gs,
    Side side,
    CountryId cid,
    const std::array<int, kCountrySlots>& target_counts,
    const HeuristicConfig& config,
    TemplateKind templ
) {
    const auto& pub = gs.pub;
    const auto& spec = country_spec(cid);
    const int current_alloc = target_counts[static_cast<size_t>(cid)];
    const double repeat_decay = current_alloc <= 0 ? 1.0 : 1.0 / (1.0 + 1.75 * static_cast<double>(current_alloc));
    const double local = repeat_decay * (
        country_priority(gs, side, cid, config) + 0.55 * country_count_signal(gs, side, cid, config)
    );
    const double defend = defend_control_signal(gs, side, cid, config);
    const double attack = attack_control_signal(gs, side, cid, config);
    const double access = (current_alloc == 0 ? 1.0 : 0.20) * access_gain_signal(gs, side, cid, config);
    const double prep = (current_alloc == 0 ? 1.0 : 0.65) * prep_scoring_signal(gs, side, cid, config);
    const double protect = protect_battleground_signal(gs, side, cid, config);
    const double region_delta = exact_region_delta_signal(gs, side, cid, target_counts, config);
    const double future_own = static_cast<double>(pub.influence_of(side, cid) + current_alloc + 1);
    const double opp = static_cast<double>(pub.influence_of(other_side(side), cid));
    const double desired_buffer = spec.is_battleground ? 0.0 : -0.5;
    const double future_excess = std::max(0.0, future_own - (opp + static_cast<double>(spec.stability) + desired_buffer));
    const double repeat_penalty = config.proposal_influence_repeat_penalty * static_cast<double>(current_alloc);
    const double overstack_penalty = config.proposal_influence_overstack_penalty
        * (spec.is_battleground ? 1.75 : 1.0) * future_excess * future_excess;
    double template_bonus = 0.0;
    switch (templ) {
        case TemplateKind::DefendControl:
            template_bonus = 0.50 * defend;
            break;
        case TemplateKind::BreakControl:
            template_bonus = 0.50 * attack;
            break;
        case TemplateKind::GainAccess:
            template_bonus = 0.50 * access;
            break;
        case TemplateKind::PrepScoring:
            template_bonus = 0.50 * prep;
            break;
        case TemplateKind::OverprotectBg:
            template_bonus = 0.50 * protect;
            break;
        default:
            template_bonus = 0.20 * (defend + attack + access + prep + protect);
            break;
    }
    return region_delta
        + 0.20 * local
        + 0.35 * protect
        + 0.35 * attack
        + 0.25 * access
        + 0.30 * prep
        + template_bonus
        - repeat_penalty
        - overstack_penalty;
}

std::vector<ActionEncoding> beam_influence_actions(
    const GameState& gs,
    Side side,
    CardId card_id,
    ActionMode mode,
    TemplateKind templ,
    std::span<const CountryId> legal_influence,
    const HeuristicConfig& config
) {
    const profile::ScopedTimer timer(profile::Slot::BeamInfluenceActions);
    if (card_id == kChinaCardId || (gs.pub.vietnam_revolts_active && side == Side::USSR)) {
        CardSet single_card{};
        single_card.set(card_id);
        auto fallback = enumerate_actions(single_card, gs.pub, side, holds_china_for(gs, side), config.max_influence_targets);
        fallback.erase(
            std::remove_if(
                fallback.begin(),
                fallback.end(),
                [mode](const ActionEncoding& action) { return action.mode != mode; }
            ),
            fallback.end()
        );
        return fallback;
    }

    std::vector<CountryId> countries(legal_influence.begin(), legal_influence.end());
    if (countries.empty()) {
        return {};
    }
    std::sort(countries.begin(), countries.end(), [&](CountryId lhs, CountryId rhs) {
        std::array<int, kCountrySlots> empty = {};
        return marginal_placement_score(gs, side, lhs, empty, config, templ)
            > marginal_placement_score(gs, side, rhs, empty, config, templ);
    });
    const size_t country_limit = std::min(countries.size(), static_cast<size_t>(std::max(6, config.max_influence_targets + 2)));
    std::vector<CountryId> shortlisted;
    shortlisted.reserve(country_limit + 4);
    std::unordered_set<int> seen_ids;
    for (size_t idx = 0; idx < std::min(countries.size(), country_limit); ++idx) {
        shortlisted.push_back(countries[idx]);
        seen_ids.insert(static_cast<int>(countries[idx]));
    }
    if (europe_control_pressure(gs.pub, side) || europe_control_pressure(gs.pub, other_side(side))) {
        std::vector<std::pair<double, CountryId>> europe_support;
        europe_support.reserve(countries.size());
        std::array<int, kCountrySlots> empty = {};
        for (const auto cid : countries) {
            const auto& spec = country_spec(cid);
            if (spec.region != Region::Europe || spec.is_battleground) {
                continue;
            }
            europe_support.push_back({
                marginal_placement_score(gs, side, cid, empty, config, TemplateKind::PrepScoring),
                cid,
            });
        }
        std::sort(europe_support.begin(), europe_support.end(), [](const auto& lhs, const auto& rhs) {
            return lhs.first > rhs.first;
        });
        for (const auto& [score, cid] : europe_support) {
            (void)score;
            if (!seen_ids.insert(static_cast<int>(cid)).second) {
                continue;
            }
            shortlisted.push_back(cid);
            if (shortlisted.size() >= country_limit + 4) {
                break;
            }
        }
    }
    countries = std::move(shortlisted);

    struct PartialPlacement {
        std::array<int, kCountrySlots> target_counts{};
        int remaining_ops = 0;
        double score = 0.0;
    };

    std::vector<PartialPlacement> beam = {{
        .target_counts = {},
        .remaining_ops = effective_ops(card_id, gs.pub, side),
        .score = 0.0,
    }};

    constexpr int kBeamWidth = 8;
    constexpr int kExpandPerNode = 4;
    while (true) {
        bool expanded = false;
        std::vector<PartialPlacement> next;
        next.reserve(static_cast<size_t>(beam.size() * kExpandPerNode));
        for (const auto& partial : beam) {
            if (partial.remaining_ops <= 0) {
                next.push_back(partial);
                continue;
            }

            std::vector<std::pair<double, CountryId>> scored_countries;
            scored_countries.reserve(countries.size());
            for (const auto cid : countries) {
                const int cost = controls_country(other_side(side), cid, gs.pub) ? 2 : 1;
                if (cost > partial.remaining_ops) {
                    continue;
                }
                scored_countries.push_back({
                    marginal_placement_score(gs, side, cid, partial.target_counts, config, templ),
                    cid,
                });
            }
            if (scored_countries.empty()) {
                next.push_back(partial);
                continue;
            }

            expanded = true;
            std::sort(scored_countries.begin(), scored_countries.end(), [](const auto& lhs, const auto& rhs) {
                return lhs.first > rhs.first;
            });
            const int expand_limit = std::min<int>(kExpandPerNode, static_cast<int>(scored_countries.size()));
            for (int idx = 0; idx < expand_limit; ++idx) {
                const auto cid = scored_countries[static_cast<size_t>(idx)].second;
                const int cost = controls_country(other_side(side), cid, gs.pub) ? 2 : 1;
                auto next_partial = partial;
                ++next_partial.target_counts[static_cast<size_t>(cid)];
                next_partial.remaining_ops -= cost;
                next_partial.score += scored_countries[static_cast<size_t>(idx)].first;
                next.push_back(std::move(next_partial));
            }
        }
        if (!expanded) {
            break;
        }

        std::sort(next.begin(), next.end(), [](const auto& lhs, const auto& rhs) {
            return lhs.score > rhs.score;
        });
        if (next.size() > static_cast<size_t>(kBeamWidth)) {
            next.resize(static_cast<size_t>(kBeamWidth));
        }
        beam = std::move(next);
    }

    std::vector<ActionEncoding> actions;
    std::unordered_set<ActionEncoding, ActionEncodingHash> seen;
    for (const auto& partial : beam) {
        std::vector<CountryId> targets;
        for (const auto cid : countries) {
            const int copies = partial.target_counts[static_cast<size_t>(cid)];
            for (int count = 0; count < copies; ++count) {
                targets.push_back(cid);
            }
        }
        if (targets.empty()) {
            continue;
        }
        std::sort(targets.begin(), targets.end());
        ActionEncoding action{
            .card_id = card_id,
            .mode = mode,
            .targets = std::move(targets),
        };
        if (seen.insert(action).second) {
            actions.push_back(std::move(action));
        }
    }
    return actions;
}

std::vector<ActionEncoding> candidate_actions(
    const GameState& gs,
    Side side,
    const HeuristicConfig& config
) {
    const profile::ScopedTimer timer(profile::Slot::CandidateActions);
    if (gs.pub.ar == 0) {
        return headline_candidates(gs, side);
    }

    struct ModeEstimate {
        ActionMode mode = ActionMode::Event;
        double score = -std::numeric_limits<double>::infinity();
    };
    struct CardEstimate {
        CardId card_id = 0;
        std::vector<ModeEstimate> modes;
        double best_score = -std::numeric_limits<double>::infinity();
    };

    const auto legal = build_legal_context(gs, side);

    auto estimate_mode_score = [&](CardId card_id, ActionMode mode) {
        switch (mode) {
            case ActionMode::Event: {
                const auto event_action = ActionEncoding{.card_id = card_id, .mode = ActionMode::Event, .targets = {}};
                return score_concrete_action(gs, side, event_action, config).score;
            }
            case ActionMode::Space:
                return score_concrete_action(
                    gs,
                    side,
                    ActionEncoding{.card_id = card_id, .mode = ActionMode::Space, .targets = {}},
                    config
                ).score;
            case ActionMode::Coup: {
                double best = -std::numeric_limits<double>::infinity();
                for (const auto cid : legal.coup) {
                    best = std::max(best, coup_action_score(gs, side, cid, country_spec(cid).is_battleground, card_id, config));
                }
                return best;
            }
            case ActionMode::Realign: {
                double best = -std::numeric_limits<double>::infinity();
                for (const auto cid : legal.realign) {
                    best = std::max(best, realign_action_score(gs, side, cid, config));
                }
                return best;
            }
            case ActionMode::Influence:
            case ActionMode::EventFirst: {
                std::array<int, kCountrySlots> empty = {};
                double best = -std::numeric_limits<double>::infinity();
                for (const auto cid : legal.influence) {
                    best = std::max(best, marginal_placement_score(gs, side, cid, empty, config, TemplateKind::BreakControl));
                    best = std::max(best, marginal_placement_score(gs, side, cid, empty, config, TemplateKind::GainAccess));
                    best = std::max(best, marginal_placement_score(gs, side, cid, empty, config, TemplateKind::PrepScoring));
                    best = std::max(best, marginal_placement_score(gs, side, cid, empty, config, TemplateKind::DefendControl));
                }
                return mode == ActionMode::EventFirst ? best - 0.15 : best;
            }
        }
        return -std::numeric_limits<double>::infinity();
    };

    std::vector<CardEstimate> ranked_cards;
    for (const auto card_id : legal_cards(gs.hands[to_index(side)], gs.pub, side, holds_china_for(gs, side))) {
        CardEstimate estimate{
            .card_id = card_id,
            .modes = {},
            .best_score = -std::numeric_limits<double>::infinity(),
        };
        for (const auto mode : legal_modes_from_context(gs, side, card_id, legal)) {
            const auto score = estimate_mode_score(card_id, mode);
            estimate.modes.push_back({.mode = mode, .score = score});
            estimate.best_score = std::max(estimate.best_score, score);
        }
        ranked_cards.push_back(std::move(estimate));
    }
    std::sort(ranked_cards.begin(), ranked_cards.end(), [](const auto& lhs, const auto& rhs) {
        return lhs.best_score > rhs.best_score;
    });
    if (ranked_cards.size() > static_cast<size_t>(kCardK)) {
        ranked_cards.resize(static_cast<size_t>(kCardK));
    }

    std::vector<ActionEncoding> actions;
    for (auto& card : ranked_cards) {
        std::sort(card.modes.begin(), card.modes.end(), [](const auto& lhs, const auto& rhs) {
            return lhs.score > rhs.score;
        });
        if (card.modes.size() > static_cast<size_t>(kModeK)) {
            card.modes.resize(static_cast<size_t>(kModeK));
        }
        for (const auto& mode_estimate : card.modes) {
            const auto mode = mode_estimate.mode;
            switch (mode) {
                case ActionMode::Event:
                case ActionMode::Space:
                    actions.push_back(ActionEncoding{
                        .card_id = card.card_id,
                        .mode = mode,
                        .targets = {},
                    });
                    break;
                case ActionMode::EventFirst: {
                    bool emitted = false;
                    for (const auto templ : {
                             TemplateKind::DefendControl,
                             TemplateKind::BreakControl,
                             TemplateKind::GainAccess,
                             TemplateKind::PrepScoring,
                         }) {
                        auto event_first = beam_influence_actions(
                            gs,
                            side,
                            card.card_id,
                            ActionMode::EventFirst,
                            templ,
                            legal.influence,
                            config
                        );
                        if (!event_first.empty()) {
                            actions.insert(actions.end(), event_first.begin(), event_first.end());
                            emitted = true;
                        }
                    }
                    if (!emitted) {
                        actions.push_back(ActionEncoding{
                            .card_id = card.card_id,
                            .mode = ActionMode::EventFirst,
                            .targets = {},
                        });
                    }
                    break;
                }
                case ActionMode::Influence: {
                    for (const auto templ : {
                             TemplateKind::DefendControl,
                             TemplateKind::BreakControl,
                             TemplateKind::GainAccess,
                             TemplateKind::PrepScoring,
                             TemplateKind::OverprotectBg,
                         }) {
                        auto influence = beam_influence_actions(
                            gs,
                            side,
                            card.card_id,
                            ActionMode::Influence,
                            templ,
                            legal.influence,
                            config
                        );
                        actions.insert(actions.end(), influence.begin(), influence.end());
                    }
                    break;
                }
                case ActionMode::Coup:
                case ActionMode::Realign: {
                    const auto& countries = mode == ActionMode::Coup ? legal.coup : legal.realign;
                    for (const auto country_id : countries) {
                        actions.push_back(ActionEncoding{
                            .card_id = card.card_id,
                            .mode = mode,
                            .targets = {country_id},
                        });
                    }
                    break;
                }
            }
        }
    }
    return actions;
}

}  // namespace

std::vector<ActionProposal> enumerate_action_proposals(
    const GameState& gs,
    Side side,
    const HeuristicConfig& config
) {
    const profile::ScopedTimer timer(profile::Slot::EnumerateActionProposals);
    if (must_play_scoring_card(gs, side)) {
        std::vector<ActionEncoding> actions;
        for (int raw = 1; raw <= kMaxCardId; ++raw) {
            const auto card_id = static_cast<CardId>(raw);
            if (!gs.hands[to_index(side)].test(card_id) || !card_spec(card_id).is_scoring) {
                continue;
            }
            actions.push_back(ActionEncoding{
                .card_id = card_id,
                .mode = ActionMode::Event,
                .targets = {},
            });
        }

        std::unordered_set<ActionEncoding, ActionEncodingHash> seen;
        std::vector<ScoredConcreteAction> scored;
        scored.reserve(actions.size());
        for (const auto& action : actions) {
            if (!seen.insert(action).second) {
                continue;
            }
            scored.push_back(score_concrete_action(gs, side, action, config));
        }

        std::sort(scored.begin(), scored.end(), [](const auto& lhs, const auto& rhs) {
            return lhs.score > rhs.score;
        });

        std::vector<ActionProposal> out;
        const size_t limit = std::min(
            scored.size(),
            static_cast<size_t>(std::max(proposal_limit_for_side(side, config), config.search_candidate_limit))
        );
        out.reserve(limit);
        std::vector<double> logits;
        logits.reserve(limit);
        for (size_t idx = 0; idx < limit; ++idx) {
            logits.push_back(scored[idx].score / std::max(0.05, config.prior_temperature));
        }
        const double max_logit = logits.empty() ? 0.0 : *std::max_element(logits.begin(), logits.end());
        double denom = 0.0;
        for (size_t idx = 0; idx < logits.size(); ++idx) {
            logits[idx] = std::exp(logits[idx] - max_logit);
            denom += logits[idx];
        }
        denom = std::max(denom, 1e-9);
        const double uniform_prior = limit > 0 ? 1.0 / static_cast<double>(limit) : 0.0;
        for (size_t idx = 0; idx < limit; ++idx) {
            const double softmax_prior = logits[idx] / denom;
            const double prior = (1.0 - config.proposal_uniform_mix) * softmax_prior + config.proposal_uniform_mix * uniform_prior;
            out.push_back(ActionProposal{
                .action = scored[idx].action,
                .heuristic_score = scored[idx].score,
                .prior = prior,
            });
        }
        return out;
    }

    std::vector<ActionEncoding> actions = candidate_actions(gs, side, config);

    std::unordered_set<ActionEncoding, ActionEncodingHash> seen;
    std::vector<ScoredConcreteAction> scored;
    scored.reserve(actions.size());
    for (const auto& action : actions) {
        if (!seen.insert(action).second) {
            continue;
        }
        scored.push_back(score_concrete_action(gs, side, action, config));
    }

    std::array<double, kCardSlots> card_best{};
    std::array<std::array<double, 3>, kCardSlots> mode_best{};
    for (auto& value : card_best) {
        value = -std::numeric_limits<double>::infinity();
    }
    for (auto& modes : mode_best) {
        modes.fill(-std::numeric_limits<double>::infinity());
    }
    for (const auto& item : scored) {
        const auto card = static_cast<size_t>(item.action.card_id);
        card_best[card] = std::max(card_best[card], item.score);
        mode_best[card][static_cast<size_t>(mode_index(item.mode))] =
            std::max(mode_best[card][static_cast<size_t>(mode_index(item.mode))], item.score);
    }

    std::vector<CardId> ranked_cards;
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        if (card_best[static_cast<size_t>(raw)] > -std::numeric_limits<double>::infinity()) {
            ranked_cards.push_back(static_cast<CardId>(raw));
        }
    }
    std::sort(ranked_cards.begin(), ranked_cards.end(), [&](CardId lhs, CardId rhs) {
        return card_best[static_cast<size_t>(lhs)] > card_best[static_cast<size_t>(rhs)];
    });
    if (ranked_cards.size() > static_cast<size_t>(kCardK)) {
        ranked_cards.resize(kCardK);
    }

    std::vector<ScoredConcreteAction> filtered;
    for (const auto card_id : ranked_cards) {
        std::array<ProposalMode, 3> ranked_modes = {ProposalMode::Event, ProposalMode::Ops, ProposalMode::Space};
        std::sort(ranked_modes.begin(), ranked_modes.end(), [&](ProposalMode lhs, ProposalMode rhs) {
            return mode_best[static_cast<size_t>(card_id)][static_cast<size_t>(mode_index(lhs))] >
                mode_best[static_cast<size_t>(card_id)][static_cast<size_t>(mode_index(rhs))];
        });

        const size_t mode_limit = std::min(static_cast<size_t>(kModeK), ranked_modes.size());
        for (size_t mode_idx = 0; mode_idx < mode_limit; ++mode_idx) {
            const auto mode = ranked_modes[mode_idx];
            std::vector<ScoredConcreteAction> bucket;
            for (const auto& item : scored) {
                if (item.action.card_id == card_id && item.mode == mode) {
                    bucket.push_back(item);
                }
            }
            if (bucket.empty()) {
                continue;
            }

            if (mode == ProposalMode::Ops) {
                std::array<double, 9> template_best{};
                template_best.fill(-std::numeric_limits<double>::infinity());
                for (const auto& item : bucket) {
                    template_best[static_cast<size_t>(item.templ)] =
                        std::max(template_best[static_cast<size_t>(item.templ)], item.score);
                }
                std::sort(bucket.begin(), bucket.end(), [](const auto& lhs, const auto& rhs) {
                    return lhs.score > rhs.score;
                });
                std::unordered_set<int> seen_templates;
                for (const auto& item : bucket) {
                    const auto templ = static_cast<int>(item.templ);
                    if (seen_templates.insert(templ).second) {
                        filtered.push_back(item);
                    }
                }
                std::sort(bucket.begin(), bucket.end(), [](const auto& lhs, const auto& rhs) {
                    return lhs.score > rhs.score;
                });
                const auto bucket_limit = per_bucket_limit(mode, TemplateKind::DefendControl);
                for (const auto& item : bucket) {
                    if (filtered.size() >= bucket_limit * ranked_cards.size()) {
                        break;
                    }
                    filtered.push_back(item);
                }
                continue;
            }

            std::sort(bucket.begin(), bucket.end(), [](const auto& lhs, const auto& rhs) {
                return lhs.score > rhs.score;
            });
            const auto bucket_limit = per_bucket_limit(mode, TemplateKind::None);
            for (size_t idx = 0; idx < std::min(bucket.size(), bucket_limit); ++idx) {
                filtered.push_back(bucket[idx]);
            }
        }
    }

    if (filtered.empty()) {
        filtered = scored;
    }

    std::unordered_set<ActionEncoding, ActionEncodingHash> chosen;
    std::vector<ScoredConcreteAction> final_scored;
    final_scored.reserve(filtered.size());
    for (const auto& item : filtered) {
        if (!chosen.insert(item.action).second) {
            continue;
        }
        final_scored.push_back(item);
    }
    std::sort(final_scored.begin(), final_scored.end(), [](const auto& lhs, const auto& rhs) {
        return lhs.score > rhs.score;
    });

    std::vector<ActionProposal> out;
    const size_t limit = std::min(
        final_scored.size(),
        static_cast<size_t>(std::max(proposal_limit_for_side(side, config), config.search_candidate_limit))
    );
    out.reserve(limit);
    std::vector<double> logits;
    logits.reserve(limit);
    for (size_t idx = 0; idx < limit; ++idx) {
        logits.push_back(final_scored[idx].score / std::max(0.05, config.prior_temperature));
    }
    const double max_logit = logits.empty() ? 0.0 : *std::max_element(logits.begin(), logits.end());
    double denom = 0.0;
    for (size_t idx = 0; idx < logits.size(); ++idx) {
        logits[idx] = std::exp(logits[idx] - max_logit);
        denom += logits[idx];
    }
    denom = std::max(denom, 1e-9);
    const double uniform_prior = limit > 0 ? 1.0 / static_cast<double>(limit) : 0.0;
    for (size_t idx = 0; idx < limit; ++idx) {
        const double softmax_prior = logits[idx] / denom;
        const double prior = (1.0 - config.proposal_uniform_mix) * softmax_prior + config.proposal_uniform_mix * uniform_prior;
        out.push_back(ActionProposal{
            .action = final_scored[idx].action,
            .heuristic_score = final_scored[idx].score,
            .prior = prior,
        });
    }
    return out;
}

std::vector<ActionEncoding> enumerate_candidate_actions(
    const GameState& gs,
    Side side,
    const HeuristicConfig& config
) {
    auto proposals = enumerate_action_proposals(gs, side, config);
    std::vector<ActionEncoding> actions;
    actions.reserve(proposals.size());
    for (const auto& proposal : proposals) {
        actions.push_back(proposal.action);
    }
    return actions;
}

ActionEncoding fallback_legal_action(
    const GameState& gs,
    Side side,
    const HeuristicConfig& config
) {
    if (gs.pub.ar == 0) {
        const auto headline = headline_candidates(gs, side);
        if (!headline.empty()) {
            return headline.front();
        }
    }
    auto actions = enumerate_actions(
        gs.hands[to_index(side)],
        gs.pub,
        side,
        holds_china_for(gs, side),
        config.max_influence_targets
    );
    if (!actions.empty()) {
        return actions.front();
    }
    for (const auto card_id : legal_cards(gs.hands[to_index(side)], gs.pub, side, holds_china_for(gs, side))) {
        return ActionEncoding{
            .card_id = card_id,
            .mode = gs.pub.ar == 0 ? ActionMode::Event : ActionMode::Influence,
            .targets = {},
        };
    }
    return ActionEncoding{};
}

PlannedAction plan_specific_action(
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config,
    const ActionEncoding& action
) {
    return plan_action_once(gs, side, rng, config, action);
}

PlannedAction choose_greedy_action_plan(
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config
) {
    auto proposals = enumerate_action_proposals(gs, side, config);
    PlannedAction best;
    bool have_best = false;
    const auto evaluate_count = std::min(proposals.size(), static_cast<size_t>(config.search_candidate_limit));
    for (size_t idx = 0; idx < evaluate_count; ++idx) {
        auto plan = plan_action_once(gs, side, rng, config, proposals[idx].action);
        if (!have_best || plan.static_score > best.static_score) {
            best = std::move(plan);
            have_best = true;
        }
    }
    if (!have_best && !proposals.empty()) {
        best.action = proposals.front().action;
        have_best = true;
    }
    if (!have_best) {
        best.action = fallback_legal_action(gs, side, config);
    }
    return best;
}

PlannedAction choose_search_action_plan(
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config
) {
    return choose_ismcts_action_plan(gs, side, rng, config);
}

}  // namespace ts::experimental
