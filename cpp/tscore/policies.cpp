// Native heuristic-policy implementation. This file is intentionally verbose:
// parity/debuggability matters more than minimizing helper count here.

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

// Turn buckets roughly matching the Python heuristic's early/mid/late staging.
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

// Heuristic penalties remain intentionally narrower than the engine legality rules.
// Canonical DEFCON-lowering membership always comes from is_defcon_lowering_card().
constexpr std::array<CardId, 1> kHeuristicPenaltyCardsProbDefcon = {20};
constexpr std::array<CardId, 3> kHeuristicPenaltyCardsRandomCoup = {52, 68, 83};
constexpr std::array<CardId, 1> kHeuristicPenaltyCardsDoubleCoup = {83};
constexpr double kDefconLoweringDefcon3Penalty = 20.0;
constexpr double kDefconProbDefcon3Penalty = 50.0;
constexpr double kDefconRandomCoupDefcon3Penalty = 100.0;
constexpr double kDefconRandomCoupDefcon3OpsPenalty = 500.0;

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

bool is_heuristic_prob_defcon_penalty_card(CardId card_id) {
    return contains(kHeuristicPenaltyCardsProbDefcon, card_id);
}

bool is_heuristic_random_coup_penalty_card(CardId card_id) {
    return contains(kHeuristicPenaltyCardsRandomCoup, card_id);
}

bool is_heuristic_double_coup_penalty_card(CardId card_id) {
    return contains(kHeuristicPenaltyCardsDoubleCoup, card_id);
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
        // Space Race with opponent's card: the opponent's event fires automatically.
        // At DEFCON 2, a dangerous event drops DEFCON to 1 = instant loss.
        if (pub.defcon <= 2 && card.side != side && card.side != Side::Neutral) {
            if (is_defcon_lowering_card(action.card_id) ||
                is_heuristic_random_coup_penalty_card(action.card_id)) {
                return -kDefcon2BattlegroundSuicidePenalty;
            }
        }
        // At DEFCON 3, Che (double-coup risk) via Space is also dangerous.
        if (pub.defcon == 3 && card.side != side && card.side != Side::Neutral &&
            is_heuristic_double_coup_penalty_card(action.card_id)) {
            return -kDefcon2BattlegroundSuicidePenalty;
        }
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
        if (is_defcon_lowering_card(action.card_id)) {
            if (pub.defcon <= 2) {
                return -kDefcon2BattlegroundSuicidePenalty;
            }
            if (pub.defcon == 3) {
                if (card.side != side && card.side != Side::Neutral) {
                    return 50.0;
                }
                return -kDefconLoweringDefcon3Penalty;
            }
            if (pub.defcon >= 4 && card.side != side && card.side != Side::Neutral) {
                return pub.defcon >= 5 ? 200.0 : 100.0;
            }
        }
        if (is_heuristic_prob_defcon_penalty_card(action.card_id)) {
            if (pub.defcon <= 2) {
                return -kDefcon2BattlegroundSuicidePenalty;
            }
            if (pub.defcon == 3) {
                return -kDefconProbDefcon3Penalty;
            }
        }
        if (is_heuristic_random_coup_penalty_card(action.card_id)) {
            if (pub.defcon <= 2) {
                return -kDefcon2BattlegroundSuicidePenalty;
            }
            if (pub.defcon == 3) {
                // Che (83) fires TWO sequential coups: DEFCON 3→2 (first coup) then 2→1 if
                // the first succeeds (second coup) = instant nuclear war chain.
                // Hard-block Event mode for Che at DEFCON 3.
                if (is_heuristic_double_coup_penalty_card(action.card_id)) {
                    return -kDefcon2BattlegroundSuicidePenalty;
                }
                return -kDefconRandomCoupDefcon3Penalty;
            }
        }
    }

    if (
        card.side != side &&
        card.side != Side::Neutral &&
        (is_defcon_lowering_card(action.card_id) ||
         is_heuristic_prob_defcon_penalty_card(action.card_id) ||
         is_heuristic_random_coup_penalty_card(action.card_id))
    ) {
        if (pub.defcon <= 2) {
            return -kDefcon2BattlegroundSuicidePenalty;
        }
        if (is_defcon_lowering_card(action.card_id)) {
            if (pub.defcon == 3) {
                return -200.0;
            }
            if (pub.defcon >= 4) {
                return -150.0;
            }
        }
        if (is_heuristic_prob_defcon_penalty_card(action.card_id) && pub.defcon == 3) {
            return -kDefconProbDefcon3Penalty;
        }
        if (is_heuristic_random_coup_penalty_card(action.card_id)) {
            if (pub.defcon == 3) {
                return -kDefconRandomCoupDefcon3OpsPenalty;
            }
        }
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
        if (card.side != side && card.side != Side::Neutral) {
            if (is_defcon_lowering_card(action.card_id)) {
                if (pub.defcon >= 5) {
                    score += 150.0;
                } else if (pub.defcon == 4) {
                    score += 80.0;
                } else if (pub.defcon == 3) {
                    score += 40.0;
                }
            }
            if (is_heuristic_random_coup_penalty_card(action.card_id)) {
                if (pub.defcon >= 5) {
                    score += 80.0;
                } else if (pub.defcon == 4) {
                    score += 120.0;
                } else if (pub.defcon == 3) {
                    score += 300.0;
                }
            }
        }
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

    if (pub.defcon == 3 && card.side != side && card.side != Side::Neutral) {
        if (is_defcon_lowering_card(action.card_id)) {
            score += 50.0;
        } else if (is_heuristic_random_coup_penalty_card(action.card_id)) {
            score += 30.0;
        }
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
            // Any coup at DEFCON 2 drops DEFCON to 1 = instant loss for phasing player.
            // Non-BG coups are NOT safer than BG coups here — apply the same hard penalty.
            score -= kDefcon2BattlegroundSuicidePenalty;
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
        case ActionMode::EventFirst:
            // EventFirst is influence with event-before-ops ordering; score same as Influence.
            [[fallthrough]];
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
    const auto base_action = ActionEncoding{.card_id = card_id, .mode = ActionMode::Influence, .targets = {}};
    if (accessible.empty()) {
        return Candidate{
            .action = base_action,
            .score = score_action(context, base_action),
        };
    }

    const auto ops = effective_ops(card_id, context.pub, context.side);
    using Cell = std::optional<Candidate>;
    std::vector<std::vector<std::array<Cell, 2>>> dp(
        accessible.size() + 1,
        std::vector<std::array<Cell, 2>>(static_cast<size_t>(ops + 1))
    );
    dp[0][0][0] = Candidate{
        .action = base_action,
        .score = score_action(context, base_action),
    };

    for (size_t index = 0; index < accessible.size(); ++index) {
        const auto country_id = accessible[index];
        const auto country_is_asia = is_asia_or_sea(country_id);
        for (int used_ops = 0; used_ops <= ops; ++used_ops) {
            for (int has_asia = 0; has_asia <= 1; ++has_asia) {
                const auto& previous = dp[index][static_cast<size_t>(used_ops)][static_cast<size_t>(has_asia)];
                if (!previous.has_value()) {
                    continue;
                }

                for (int allocation = 0; allocation <= ops - used_ops; ++allocation) {
                    auto next_targets = previous->action.targets;
                    next_targets.insert(next_targets.end(), allocation, country_id);
                    ActionEncoding next_action{
                        .card_id = card_id,
                        .mode = ActionMode::Influence,
                        .targets = std::move(next_targets),
                    };
                    const auto next_has_asia = has_asia || (country_is_asia && allocation > 0 ? 1 : 0);
                    const auto next_score = score_action(context, next_action);
                    Candidate candidate{
                        .action = std::move(next_action),
                        .score = next_score,
                    };
                    auto& slot = dp[index + 1][static_cast<size_t>(used_ops + allocation)][static_cast<size_t>(next_has_asia)];
                    if (!slot.has_value() || better_candidate(candidate, *slot)) {
                        slot = std::move(candidate);
                    }
                }
            }
        }
    }

    auto best = dp[accessible.size()][static_cast<size_t>(ops)][0];
    auto with_asia = dp[accessible.size()][static_cast<size_t>(ops)][1];
    if (with_asia.has_value() && (!best.has_value() || better_candidate(*with_asia, *best))) {
        best = std::move(with_asia);
    }
    if (!best.has_value()) {
        return Candidate{
            .action = base_action,
            .score = score_action(context, base_action),
        };
    }
    return *best;
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
    Pcg64Rng& rng
) {
    return sample_action(hand, pub, pub.phasing, holds_china, rng);
}

std::optional<ActionEncoding> choose_minimal_hybrid(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    const MinimalHybridParams& params
) {
    auto ranked = rank_minimal_hybrid_actions(pub, hand, holds_china, params);
    if (ranked.empty()) {
        return std::nullopt;
    }
    return ranked.front().action;
}

std::vector<ScoredAction> rank_minimal_hybrid_actions(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    const MinimalHybridParams& params
) {
    const auto side = pub.phasing;
    const auto context = make_context(pub, side, params);
    std::vector<ScoredAction> ranked;

    if (pub.ar == 0) {
        auto actions = headline_actions(hand, pub, side, holds_china);
        ranked.reserve(actions.size());
        for (const auto& action : actions) {
            ranked.push_back(ScoredAction{
                .action = action,
                .score = score_action(context, action),
            });
        }
    } else {
        auto playable = legal_cards(hand, pub, side, holds_china);
        for (const auto card_id : playable) {
            auto modes = legal_modes(card_id, pub, side);
            for (const auto mode : modes) {
                if (mode == ActionMode::Event || mode == ActionMode::Space) {
                    ActionEncoding action{.card_id = card_id, .mode = mode, .targets = {}};
                    ranked.push_back(ScoredAction{
                        .action = action,
                        .score = score_action(context, action),
                    });
                    continue;
                }

            auto accessible = legal_countries(card_id, mode, pub, side);
            if (accessible.empty()) {
                continue;
            }
            std::sort(accessible.begin(), accessible.end());
            if (static_cast<int>(accessible.size()) > kMaxInfluenceTargets) {
                accessible.resize(kMaxInfluenceTargets);
            }

                if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
                    for (const auto country_id : accessible) {
                        ActionEncoding action{
                            .card_id = card_id,
                            .mode = mode,
                            .targets = {country_id},
                        };
                        ranked.push_back(ScoredAction{
                            .action = action,
                            .score = score_action(context, action),
                        });
                    }
                    continue;
                }

                auto candidate = best_influence_action(context, card_id, accessible);
                ranked.push_back(ScoredAction{
                    .action = std::move(candidate.action),
                    .score = candidate.score,
                });
            }
        }
    }

    std::sort(ranked.begin(), ranked.end(), [](const ScoredAction& lhs, const ScoredAction& rhs) {
        return better_candidate(
            Candidate{.action = lhs.action, .score = lhs.score},
            Candidate{.action = rhs.action, .score = rhs.score}
        );
    });
    if (!ranked.empty() && !std::isfinite(ranked.front().score)) {
        ranked.clear();
    }
    return ranked;
}

std::optional<ActionEncoding> choose_minimal_hybrid_sampled(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    double temperature,
    Pcg64Rng& rng,
    const MinimalHybridParams& params
) {
    auto ranked = rank_minimal_hybrid_actions(pub, hand, holds_china, params);
    if (ranked.empty()) {
        return std::nullopt;
    }
    if (temperature <= 0.0 || ranked.size() == 1) {
        return ranked.front().action;
    }

    // Boltzmann softmax: p_i = exp(score_i / T) / sum(exp(score_j / T))
    // Subtract max for numerical stability.
    double max_score = ranked.front().score;
    for (const auto& sa : ranked) {
        max_score = std::max(max_score, sa.score);
    }

    std::vector<double> weights(ranked.size());
    double total = 0.0;
    for (size_t i = 0; i < ranked.size(); ++i) {
        weights[i] = std::exp((ranked[i].score - max_score) / temperature);
        total += weights[i];
    }

    // Sample from the distribution.
    double r = rng.random_double() * total;
    double cumulative = 0.0;
    for (size_t i = 0; i < ranked.size(); ++i) {
        cumulative += weights[i];
        if (r <= cumulative) {
            return ranked[i].action;
        }
    }
    return ranked.back().action;
}

std::optional<ActionEncoding> choose_action(
    PolicyKind kind,
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    Pcg64Rng& rng
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
