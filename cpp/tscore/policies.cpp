#include "policies.hpp"

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <tuple>

#include "game_data.hpp"
#include "game_state.hpp"

namespace ts {
namespace {

constexpr int kEarlyLastTurn = 3;
constexpr int kMidLastTurn = 7;
constexpr CountryId kThailandId = 79;
constexpr double kOffsideOpsPenaltyBase = 7.0;
constexpr double kOffsideOpsPenaltyPerOp = 4.0;
constexpr double kNonCoupMilopsUrgencyScale = 10.0;
constexpr double kNonCoupMilopsLatePenalty = 3.0;
constexpr double kCoupExpectedSwingScale = 5.5;
constexpr double kCoupAccessOpeningBonus = 9.0;
constexpr double kCoupMilopsUrgencyScale = 4.0;
constexpr double kOpeningIranCoupBonus = 35.0;
constexpr double kEmptyCoupPenalty = 15.0;
constexpr double kDefcon2BattlegroundSuicidePenalty = 1'000'000.0;
constexpr double kDefcon3BattlegroundSuicidePenalty = 1'000'000.0;
constexpr double kDefcon3NonBgSafeCoupBonus = 5.0;
constexpr double kDefcon2NonBgSafeCoupBonus = 12.0;
constexpr int kMaxInfluenceTargets = 86;

constexpr std::array<CardId, 7> kDefconLoweringCards = {4, 11, 13, 24, 53, 92, 105};
constexpr std::array<CardId, 1> kDefconProbLoweringCards = {20};
constexpr std::array<CardId, 2> kDefconRandomCoupCards = {39, 83};

constexpr std::array<std::string_view, 4> kEuropeCore = {
    "France",
    "Italy",
    "West Germany",
    "East Germany",
};
constexpr std::array<std::string_view, 5> kMidWarEntry = {
    "Angola",
    "South Africa",
    "Panama",
    "Mexico",
    "Chile",
};

template <typename T, size_t N>
bool contains(const std::array<T, N>& values, const T& value) {
    return std::find(values.begin(), values.end(), value) != values.end();
}

bool is_asia_or_sea(CountryId country_id) {
    const auto region = country_spec(country_id).region;
    return region == Region::Asia || region == Region::SoutheastAsia;
}

int remaining_ars(const PublicState& pub) {
    if (pub.ar <= 0) {
        return ars_for_turn(pub.turn);
    }
    return std::max(1, ars_for_turn(pub.turn) - pub.ar + 1);
}

int milops_shortfall(const PublicState& pub, Side side) {
    return std::max(0, pub.turn - pub.milops[to_index(side)]);
}

double milops_urgency(const PublicState& pub, Side side) {
    const auto shortfall = milops_shortfall(pub, side);
    if (shortfall <= 0) {
        return 0.0;
    }
    return static_cast<double>(shortfall) / static_cast<double>(std::max(1, remaining_ars(pub)));
}

double non_coup_milops_penalty(const PublicState& pub, Side side) {
    const auto shortfall = milops_shortfall(pub, side);
    if (shortfall <= 0 || pub.ar <= 0) {
        return 0.0;
    }
    double penalty = kNonCoupMilopsUrgencyScale * milops_urgency(pub, side);
    if (remaining_ars(pub) <= 2) {
        penalty += kNonCoupMilopsLatePenalty * static_cast<double>(shortfall);
    }
    return penalty;
}

double coup_expected_swing(const CountrySpec& country, int ops) {
    return std::max(0.0, 3.5 + static_cast<double>(ops) - (2.0 * static_cast<double>(country.stability)));
}

bool defcon2_battleground_coup_is_free(const PublicState& pub, Side side, const CountrySpec& country) {
    if (pub.defcon != 2 || !country.is_battleground) {
        return true;
    }
    return side == Side::US && pub.nuclear_subs_active;
}

std::string_view stage_for_turn(int turn) {
    if (turn <= kEarlyLastTurn) {
        return "early";
    }
    if (turn <= kMidLastTurn) {
        return "mid";
    }
    return "late";
}

double region_weight(std::string_view stage, Region region, const MinimalHybridParams& params) {
    const auto index = static_cast<size_t>(region);
    if (stage == "early") {
        return params.early_region_weights[index];
    }
    if (stage == "mid") {
        return params.mid_region_weights[index];
    }
    return params.late_region_weights[index];
}

double country_value_from_spec(std::string_view stage, CountryId country_id, const MinimalHybridParams& params) {
    const auto& country = country_spec(country_id);
    double score = params.country_region_scale * region_weight(stage, country.region, params);
    score += country.is_battleground ? params.country_battleground_bonus : params.country_non_battleground_bonus;
    score += params.country_stability_scale * static_cast<double>(std::min(country.stability, 4));
    if (country_id == kThailandId && stage == "early") {
        score += params.country_thailand_early_bonus;
    }
    if (std::find(kEuropeCore.begin(), kEuropeCore.end(), country.name) != kEuropeCore.end()) {
        score += params.country_europe_core_bonus;
    }
    if (stage == "mid" && std::find(kMidWarEntry.begin(), kMidWarEntry.end(), country.name) != kMidWarEntry.end()) {
        score += params.country_mid_war_entry_bonus;
    }
    return score;
}

struct DecisionContext {
    const PublicState& pub;
    Side side;
    const MinimalHybridParams& params;
    std::array<double, kCountrySlots> country_values = {};
};

DecisionContext make_context(const PublicState& pub, Side side, const MinimalHybridParams& params) {
    DecisionContext context{pub, side, params};
    const auto stage = stage_for_turn(pub.turn);
    for (const auto country_id : all_country_ids()) {
        context.country_values[static_cast<size_t>(country_id)] =
            country_value_from_spec(stage, country_id, params);
    }
    return context;
}

double country_value(const DecisionContext& context, CountryId country_id) {
    return context.country_values[static_cast<size_t>(country_id)];
}

double score_event(Side side, CardId card_id) {
    const auto& card = card_spec(card_id);
    if (card.is_scoring) {
        return 10'000.0;
    }
    if (card_id == kChinaCardId) {
        return -10.0;
    }
    if (card.side == side || card.side == Side::Neutral) {
        return 1.5;
    }
    return -3.0;
}

double headline_adjustment(const DecisionContext& context, CardId card_id) {
    const auto& card = card_spec(card_id);
    double score = context.params.headline_ops_scale * static_cast<double>(card.ops);
    if (card.side == context.side || card.side == Side::Neutral) {
        score += context.params.headline_friendly_bonus;
    }
    return score;
}

double defcon_safety_penalty(const DecisionContext& context, const ActionEncoding& action) {
    const auto& pub = context.pub;
    const auto side = context.side;
    const auto& card = card_spec(action.card_id);

    if (action.mode == ActionMode::Space) {
        return 0.0;
    }

    if (action.mode == ActionMode::Coup && !action.targets.empty()) {
        const auto& target = country_spec(action.targets.front());
        if (
            pub.defcon <= 2 &&
            target.is_battleground &&
            !defcon2_battleground_coup_is_free(pub, side, target)
        ) {
            return -kDefcon2BattlegroundSuicidePenalty;
        }
    }

    if (action.mode == ActionMode::Event) {
        if (contains(kDefconLoweringCards, action.card_id) && pub.defcon <= 2) {
            return -kDefcon2BattlegroundSuicidePenalty;
        }
        if (contains(kDefconProbLoweringCards, action.card_id) && pub.defcon <= 2) {
            return -kDefcon2BattlegroundSuicidePenalty;
        }
        if (contains(kDefconRandomCoupCards, action.card_id) && pub.defcon <= 2) {
            return -kDefcon2BattlegroundSuicidePenalty;
        }
    }

    if (
        card.side != side &&
        card.side != Side::Neutral &&
        (contains(kDefconLoweringCards, action.card_id) ||
         contains(kDefconProbLoweringCards, action.card_id) ||
         contains(kDefconRandomCoupCards, action.card_id)) &&
        pub.defcon <= 2
    ) {
        return -kDefcon2BattlegroundSuicidePenalty;
    }

    return 0.0;
}

double card_bias(const DecisionContext& context, const ActionEncoding& action) {
    const auto& pub = context.pub;
    const auto side = context.side;
    const auto& card = card_spec(action.card_id);
    double score = 0.0;

    if (action.mode == ActionMode::Event) {
        score += card.side == side || card.side == Side::Neutral ? 1.0 : -3.0;
    }

    if (action.mode == ActionMode::Space) {
        if (card.side != side && card.side != Side::Neutral && !card.is_scoring) {
            score += 5.0;
        }
        if (pub.space[to_index(side)] < pub.space[to_index(other_side(side))]) {
            score += 2.5;
        }
        if (card.ops >= 4) {
            score += 1.0;
        }
    }

    if (
        (action.mode == ActionMode::Influence || action.mode == ActionMode::Coup || action.mode == ActionMode::Realign) &&
        card.side != side &&
        card.side != Side::Neutral &&
        !card.is_scoring
    ) {
        score -= kOffsideOpsPenaltyBase + (kOffsideOpsPenaltyPerOp * static_cast<double>(card.ops));
    }

    if (action.card_id == kChinaCardId) {
        if (pub.turn <= kEarlyLastTurn) {
            score += context.params.china_early_penalty;
        }
        if (std::any_of(action.targets.begin(), action.targets.end(), [](CountryId cid) { return is_asia_or_sea(cid); })) {
            score += context.params.china_asia_target_bonus;
        }
        if (action.mode == ActionMode::Event) {
            score -= 10.0;
        }
    }

    return score;
}

double score_influence_targets(const DecisionContext& context, std::span<const CountryId> targets) {
    std::array<int, kCountrySlots> seen = {};
    double score = 0.0;
    const auto side = context.side;
    const auto opponent = other_side(side);

    for (const auto cid : targets) {
        auto& count = seen[static_cast<size_t>(cid)];
        ++count;
        score += country_value(context, cid) / static_cast<double>(count);

        const auto opp = context.pub.influence_of(opponent, cid);
        const auto own = context.pub.influence_of(side, cid);
        const auto stability = country_spec(cid).stability;

        if (own < opp + stability && own + count >= opp + stability) {
            score += context.params.control_break_bonus;
        }
        if (own == 0) {
            score += context.params.access_bonus;
        }
    }

    return score;
}

double score_coup(const DecisionContext& context, CountryId country_id, int ops) {
    const auto& pub = context.pub;
    const auto side = context.side;
    const auto opponent = other_side(side);
    const auto& country = country_spec(country_id);
    const auto opp_inf = pub.influence_of(opponent, country_id);
    const auto own_inf = pub.influence_of(side, country_id);

    double score = country_value(context, country_id);
    score += static_cast<double>(std::min(std::max(0, pub.turn - pub.milops[to_index(side)]), ops));
    score += coup_expected_swing(country, ops) * kCoupExpectedSwingScale;
    if (own_inf == 0 && opp_inf > 0) {
        score += kCoupAccessOpeningBonus;
    }
    score += milops_urgency(pub, side) * kCoupMilopsUrgencyScale;
    if (opp_inf == 0) {
        score -= kEmptyCoupPenalty;
    }

    if (country.is_battleground) {
        score += context.params.coup_battleground_bonus;
        if (pub.defcon == 2 && !defcon2_battleground_coup_is_free(pub, side, country)) {
            score += context.params.coup_defcon2_penalty;
            score -= kDefcon2BattlegroundSuicidePenalty;
        } else if (pub.defcon == 3) {
            score += context.params.coup_defcon3_penalty;
            if (milops_urgency(pub, side) < context.params.coup_defcon3_bg_threshold) {
                score -= kDefcon3BattlegroundSuicidePenalty;
            }
        }
    } else {
        if (pub.defcon == 3) {
            score += kDefcon3NonBgSafeCoupBonus;
        } else if (pub.defcon == 2) {
            score += kDefcon2NonBgSafeCoupBonus;
        }
    }

    if (pub.turn == 1 && side == Side::USSR && country.name == "Iran") {
        score += kOpeningIranCoupBonus;
    }

    return score;
}

double score_realign(const DecisionContext& context, CountryId country_id) {
    double score = context.params.realign_base_penalty;
    score += context.params.realign_country_scale * country_value(context, country_id);
    if (context.pub.defcon == 2) {
        score += context.params.realign_defcon2_bonus;
    }
    return score;
}

double score_space(const DecisionContext& context, CardId card_id) {
    const auto& pub = context.pub;
    const auto side = context.side;
    const auto& card = card_spec(card_id);
    double score = 0.0;
    if (pub.space[to_index(side)] < pub.space[to_index(other_side(side))]) {
        score += context.params.space_when_behind_bonus;
    }
    if (pub.turn <= kEarlyLastTurn) {
        score += context.params.space_early_bonus;
    }
    if (card.side != side && card.side != Side::Neutral && !card.is_scoring) {
        score += context.params.space_offside_bonus;
    }
    return score;
}

struct Candidate {
    ActionEncoding action;
    double score = -std::numeric_limits<double>::infinity();
};

bool better_candidate(const Candidate& lhs, const Candidate& rhs) {
    if (lhs.score != rhs.score) {
        return lhs.score > rhs.score;
    }
    const auto lhs_scoring_event =
        lhs.action.mode == ActionMode::Event && card_spec(lhs.action.card_id).is_scoring ? 0 : 1;
    const auto rhs_scoring_event =
        rhs.action.mode == ActionMode::Event && card_spec(rhs.action.card_id).is_scoring ? 0 : 1;
    return std::tuple{
        lhs_scoring_event,
        static_cast<int>(lhs.action.mode),
        static_cast<int>(lhs.action.card_id),
        lhs.action.targets
    } < std::tuple{
        rhs_scoring_event,
        static_cast<int>(rhs.action.mode),
        static_cast<int>(rhs.action.card_id),
        rhs.action.targets
    };
}

double score_action(const DecisionContext& context, const ActionEncoding& action) {
    const auto& card = card_spec(action.card_id);
    double score = 0.0;

    switch (action.mode) {
        case ActionMode::Influence:
            score += context.params.influence_mode_bonus;
            score += score_influence_targets(context, action.targets);
            break;
        case ActionMode::Coup:
            score += context.params.coup_mode_bonus;
            score += score_coup(context, action.targets.front(), card.ops);
            break;
        case ActionMode::Realign:
            score += context.params.realign_mode_bonus;
            score += score_realign(context, action.targets.front());
            break;
        case ActionMode::Space:
            score += context.params.space_mode_bonus;
            score += score_space(context, action.card_id);
            break;
        case ActionMode::Event:
            score += score_event(context.side, action.card_id);
            break;
    }

    score += card_bias(context, action);
    score += defcon_safety_penalty(context, action);
    score -= context.params.ops_card_penalty * static_cast<double>(card.ops);
    if (action.mode != ActionMode::Coup) {
        score -= non_coup_milops_penalty(context.pub, context.side);
    }
    if (context.pub.ar == 0) {
        score += headline_adjustment(context, action.card_id);
    }
    return score;
}

Candidate best_influence_action(const DecisionContext& context, CardId card_id, std::span<const CountryId> accessible) {
    Candidate best{
        .action = ActionEncoding{.card_id = card_id, .mode = ActionMode::Influence, .targets = {}},
        .score = -std::numeric_limits<double>::infinity(),
    };
    if (accessible.empty()) {
        best.score = score_action(context, best.action);
        return best;
    }

    const auto ops = effective_ops(card_id, context.pub, context.side);
    const auto side = context.side;
    const auto opponent = other_side(side);
    const auto country_count = accessible.size();
    std::vector<std::vector<double>> alloc_score(country_count, std::vector<double>(static_cast<size_t>(ops + 1), 0.0));

    for (size_t index = 0; index < country_count; ++index) {
        const auto cid = accessible[index];
        const auto own = context.pub.influence_of(side, cid);
        const auto opp = context.pub.influence_of(opponent, cid);
        const auto threshold = opp + country_spec(cid).stability;
        double total = 0.0;
        for (int allocation = 1; allocation <= ops; ++allocation) {
            total += country_value(context, cid) / static_cast<double>(allocation);
            if (own == 0) {
                total += context.params.access_bonus;
            }
            if (own < threshold && own + allocation >= threshold && own + allocation - 1 < threshold) {
                total += context.params.control_break_bonus;
            }
            alloc_score[index][static_cast<size_t>(allocation)] = total;
        }
    }

    const auto neg_inf = -std::numeric_limits<double>::infinity();
    std::vector<std::vector<double>> dp(country_count + 1, std::vector<double>(static_cast<size_t>(ops + 1), neg_inf));
    std::vector<std::vector<int>> choice(country_count + 1, std::vector<int>(static_cast<size_t>(ops + 1), 0));
    dp[0][0] = 0.0;

    for (size_t index = 0; index < country_count; ++index) {
        for (int used = 0; used <= ops; ++used) {
            if (!std::isfinite(dp[index][static_cast<size_t>(used)])) {
                continue;
            }
            for (int allocation = 0; allocation <= ops - used; ++allocation) {
                const auto candidate_score = dp[index][static_cast<size_t>(used)] + alloc_score[index][static_cast<size_t>(allocation)];
                auto& slot = dp[index + 1][static_cast<size_t>(used + allocation)];
                if (candidate_score > slot + 1e-12) {
                    slot = candidate_score;
                    choice[index + 1][static_cast<size_t>(used + allocation)] = allocation;
                }
            }
        }
    }

    std::vector<int> allocations(country_count, 0);
    int remaining = ops;
    for (size_t index = country_count; index > 0; --index) {
        const auto allocation = choice[index][static_cast<size_t>(remaining)];
        allocations[index - 1] = allocation;
        remaining -= allocation;
    }

    ActionEncoding action{.card_id = card_id, .mode = ActionMode::Influence, .targets = {}};
    for (size_t index = 0; index < country_count; ++index) {
        action.targets.insert(action.targets.end(), allocations[index], accessible[index]);
    }
    const auto action_score = score_action(context, action);
    Candidate candidate{.action = std::move(action), .score = action_score};
    if (better_candidate(candidate, best)) {
        best = std::move(candidate);
    }
    return best;
}

std::vector<ActionEncoding> headline_actions(const CardSet& hand, const PublicState& pub, Side side, bool holds_china) {
    std::vector<ActionEncoding> actions;
    for (const auto card_id : legal_cards(hand, pub, side, holds_china)) {
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

}  // namespace

std::optional<ActionEncoding> choose_random_action(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    std::mt19937& rng
) {
    return sample_action(hand, pub, pub.phasing, holds_china, rng);
}

std::optional<ActionEncoding> choose_minimal_hybrid(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    const MinimalHybridParams& params
) {
    const auto side = pub.phasing;
    const auto context = make_context(pub, side, params);

    if (pub.ar == 0) {
        auto actions = headline_actions(hand, pub, side, holds_china);
        if (actions.empty()) {
            return std::nullopt;
        }
        Candidate best{.action = actions.front(), .score = -std::numeric_limits<double>::infinity()};
        for (const auto& action : actions) {
            Candidate candidate{.action = action, .score = score_action(context, action)};
            if (better_candidate(candidate, best)) {
                best = candidate;
            }
        }
        return best.action;
    }

    auto playable = legal_cards(hand, pub, side, holds_china);
    if (playable.empty()) {
        return std::nullopt;
    }

    Candidate best{
        .action = ActionEncoding{.card_id = playable.front(), .mode = ActionMode::Event, .targets = {}},
        .score = -std::numeric_limits<double>::infinity(),
    };

    for (const auto card_id : playable) {
        auto modes = legal_modes(card_id, pub, side);
        for (const auto mode : modes) {
            if (mode == ActionMode::Event || mode == ActionMode::Space) {
                Candidate candidate{
                    .action = ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}},
                    .score = score_action(context, ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}}),
                };
                if (better_candidate(candidate, best)) {
                    best = std::move(candidate);
                }
                continue;
            }

            auto accessible = legal_countries(card_id, mode, pub, side);
            if (accessible.empty()) {
                continue;
            }
            if (static_cast<int>(accessible.size()) > kMaxInfluenceTargets) {
                accessible.resize(kMaxInfluenceTargets);
            }

            if (mode == ActionMode::Coup) {
                for (const auto country_id : accessible) {
                    ActionEncoding action{
                        .card_id = card_id,
                        .mode = mode,
                        .targets = {country_id},
                    };
                    Candidate candidate{.action = action, .score = score_action(context, action)};
                    if (better_candidate(candidate, best)) {
                        best = std::move(candidate);
                    }
                }
                continue;
            }

            if (mode == ActionMode::Realign) {
                for (const auto country_id : accessible) {
                    ActionEncoding action{
                        .card_id = card_id,
                        .mode = mode,
                        .targets = {country_id},
                    };
                    Candidate candidate{.action = action, .score = score_action(context, action)};
                    if (better_candidate(candidate, best)) {
                        best = std::move(candidate);
                    }
                }
                continue;
            }

            auto candidate = best_influence_action(context, card_id, accessible);
            if (better_candidate(candidate, best)) {
                best = std::move(candidate);
            }
        }
    }

    if (!std::isfinite(best.score)) {
        return std::nullopt;
    }
    return best.action;
}

std::optional<ActionEncoding> choose_action(
    PolicyKind kind,
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    std::mt19937& rng
) {
    switch (kind) {
        case PolicyKind::Random:
            return choose_random_action(pub, hand, holds_china, rng);
        case PolicyKind::MinimalHybrid:
            return choose_minimal_hybrid(pub, hand, holds_china);
    }
    return std::nullopt;
}

}  // namespace ts
