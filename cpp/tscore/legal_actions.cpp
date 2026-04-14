// Native legality enumeration and factorized random sampling.

#include "legal_actions.hpp"

#include <algorithm>

#include "card_properties.hpp"
#include "game_data.hpp"
#include "scoring.hpp"

namespace ts {
// DEFCON thresholds by region for coup/realignment restrictions.
constexpr std::array<int, 7> kDefconRegionThreshold = {4, 3, 2, 1, 1, 1, 3};

bool is_defcon_restricted(CountryId country_id, const PublicState& pub) {
    if (country_id == kUsaAnchorId || country_id == kUssrAnchorId) {
        return true;
    }
    const auto threshold = kDefconRegionThreshold[static_cast<size_t>(country_spec(country_id).region)];
    return pub.defcon <= threshold;
}

int vietnam_revolts_ops_bonus(const PublicState& pub, Side side, std::span<const CountryId> targets) {
    if (!pub.vietnam_revolts_active || side != Side::USSR || targets.empty()) {
        return 0;
    }
    const auto all_in_sea = std::all_of(targets.begin(), targets.end(), [](CountryId cid) {
        return country_spec(cid).region == Region::SoutheastAsia;
    });
    return all_in_sea ? 1 : 0;
}

namespace {

constexpr std::array<int, 8> kSpaceOpsMinimum = {2, 2, 3, 3, 4, 4, 5, 5};
constexpr std::array<CountryId, 12> kNatoWe = {1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18};

bool contains(std::span<const CountryId> values, CountryId value) {
    return std::find(values.begin(), values.end(), value) != values.end();
}

bool nato_prerequisite_met(const PublicState& pub) {
    return pub.warsaw_pact_played || pub.marshall_plan_played || pub.truman_doctrine_played;
}

bool nato_protected(CountryId country_id, const PublicState& pub) {
    if (!pub.nato_active) {
        return false;
    }
    if (!contains(kNatoWe, country_id)) {
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

std::vector<CountryId> filtered_accessible_countries(Side side, const PublicState& pub, ActionMode mode) {
    if (mode == ActionMode::EventFirst) {
        return {};
    }

    auto base = accessible_countries(side, pub, mode);
    if (mode == ActionMode::Influence) {
        if (side == Side::USSR && pub.chernobyl_blocked_region.has_value()) {
            base.erase(
                std::remove_if(
                    base.begin(),
                    base.end(),
                    [&](CountryId cid) { return country_spec(cid).region == *pub.chernobyl_blocked_region; }
                ),
                base.end()
            );
        }
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

template <typename T>
void enumerate_multisets(
    std::span<const T> pool,
    int size,
    int start_index,
    std::vector<T>& current,
    std::vector<std::vector<T>>& out
) {
    if (size == 0) {
        out.push_back(current);
        return;
    }
    for (int i = start_index; i < static_cast<int>(pool.size()); ++i) {
        current.push_back(pool[static_cast<size_t>(i)]);
        enumerate_multisets(pool, size - 1, i, current, out);
        current.pop_back();
    }
}

// Budget-aware influence target enumeration: places influence points costing
// sum(costs[i]) = remaining_budget total ops. Enemy-controlled countries cost 2
// ops per influence point instead of 1. Elements may repeat (multiset).
template <typename T>
void enumerate_influence_budget(
    std::span<const T> pool,
    std::span<const int> costs,
    int remaining_budget,
    int start_index,
    std::vector<T>& current,
    std::vector<std::vector<T>>& out
) {
    if (remaining_budget == 0) {
        out.push_back(current);
        return;
    }
    for (int i = start_index; i < static_cast<int>(pool.size()); ++i) {
        const int c = costs[static_cast<size_t>(i)];
        if (c > remaining_budget) continue;
        current.push_back(pool[static_cast<size_t>(i)]);
        enumerate_influence_budget(pool, costs, remaining_budget - c, i, current, out);
        current.pop_back();
    }
}

bool has_eligible_opponent_card(const CardSet& hand, Side side) {
    const auto opponent = other_side(side);
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (!hand.test(card_id)) {
            continue;
        }
        if (card_id == kChinaCardId) {
            continue;
        }
        const auto& spec = card_spec(static_cast<CardId>(card_id));
        if (spec.side == opponent && !spec.is_scoring) {
            return true;
        }
    }
    return false;
}

}  // namespace

int effective_ops(CardId card_id, const PublicState& pub, Side side) {
    return std::max(1, card_spec(card_id).ops + pub.ops_modifier[to_index(side)]);
}

bool is_defcon_lowering_card(CardId card_id) {
    return tscore::is_defcon_lowering(static_cast<int>(card_id));
}

bool is_card_blocked_by_defcon(const PublicState& pub, Side side, CardId card_id) {
    if (!is_defcon_lowering_card(card_id)) {
        return false;
    }
    const auto& card_info = card_spec(card_id);
    const bool is_opponent_card = (card_info.side != side && card_info.side != Side::Neutral);
    const bool is_neutral_card = (card_info.side == Side::Neutral);
    if (is_opponent_card) {
        if (pub.defcon <= 2) {
            return true;
        }
        if (pub.defcon == 3 && pub.ar == 0) {
            return true;
        }
    }
    if (is_neutral_card && pub.ar == 0 && pub.defcon <= 3) {
        return true;
    }
    return false;
}

std::vector<CardId> legal_cards(const CardSet& hand, const PublicState& pub, Side side, bool holds_china) {
    auto cards = hand_to_vector(hand);
    cards.erase(
        std::remove_if(
            cards.begin(),
            cards.end(),
            [&](CardId card_id) { return card_id == kChinaCardId && !holds_china; }
        ),
        cards.end()
    );
    cards.erase(
        std::remove_if(
            cards.begin(),
            cards.end(),
            [&](CardId card_id) { return is_card_blocked_by_defcon(pub, side, card_id); }
        ),
        cards.end()
    );
    return cards;
}

std::vector<ActionMode> legal_modes(CardId card_id, const PublicState& pub, Side side) {
    const auto& spec = card_spec(card_id);
    std::vector<ActionMode> modes;

    const auto accessible_inf = filtered_accessible_countries(side, pub, ActionMode::Influence);
    const auto accessible_coup = filtered_accessible_countries(side, pub, ActionMode::Coup);
    const auto accessible_realign = filtered_accessible_countries(side, pub, ActionMode::Realign);

    if (spec.ops > 0) {
        if (!accessible_inf.empty()) {
            modes.push_back(ActionMode::Influence);
            // EventFirst: fire the opponent's event first, then place influence ops after.
            // Only legal when the card strictly belongs to the opponent (not neutral).
            if (spec.side == other_side(side)) {
                modes.push_back(ActionMode::EventFirst);
            }
        }
        if (pub.defcon > 1 && !accessible_coup.empty()) {
            modes.push_back(ActionMode::Coup);
        }
        if (!accessible_realign.empty()) {
            modes.push_back(ActionMode::Realign);
        }

        const auto level = pub.space[to_index(side)];
        const auto opp_level = pub.space[to_index(other_side(side))];
        const auto max_space = (level >= 2 && opp_level < 2) ? 2 : 1;
        if (
            level < 8 &&
            pub.space_attempts[to_index(side)] < max_space &&
            effective_ops(card_id, pub, side) >= kSpaceOpsMinimum[static_cast<size_t>(level)]
        ) {
            modes.push_back(ActionMode::Space);
        }
    }

    modes.push_back(ActionMode::Event);

    if (card_id == 21 && !nato_prerequisite_met(pub)) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
    }

    const auto is_scoring = spec.is_scoring;
    if (pub.bear_trap_active && side == Side::USSR && !is_scoring) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Space), modes.end());
    }
    if (pub.quagmire_active && side == Side::US && !is_scoring) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Space), modes.end());
    }

    if (card_id == 103 && pub.defcon != 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
    }
    if (card_id == 104 && !pub.john_paul_ii_played) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
    }

    std::sort(modes.begin(), modes.end(), [](ActionMode lhs, ActionMode rhs) {
        return static_cast<int>(lhs) < static_cast<int>(rhs);
    });
    modes.erase(std::unique(modes.begin(), modes.end()), modes.end());
    return modes;
}

std::vector<CountryId> legal_countries(CardId, ActionMode mode, const PublicState& pub, Side side) {
    if (mode == ActionMode::Space || mode == ActionMode::Event || mode == ActionMode::EventFirst) {
        return {};
    }
    return filtered_accessible_countries(side, pub, mode);
}

std::vector<ActionEncoding> enumerate_actions(
    const CardSet& hand,
    const PublicState& pub,
    Side side,
    bool holds_china,
    int max_influence_targets
) {
    std::vector<ActionEncoding> actions;
    for (const auto card_id : legal_cards(hand, pub, side, holds_china)) {
        auto modes = legal_modes(card_id, pub, side);
        if (card_id == 32 && !has_eligible_opponent_card(hand, side)) {
            modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        }

        for (const auto mode : modes) {
            if (mode == ActionMode::Space || mode == ActionMode::Event) {
                actions.push_back(ActionEncoding{
                    .card_id = card_id,
                    .mode = mode,
                    .targets = {},
                });
                continue;
            }

            if (mode == ActionMode::EventFirst) {
                actions.push_back(ActionEncoding{
                    .card_id = card_id,
                    .mode = mode,
                    .targets = {},
                });
                continue;
            }

            auto accessible = filtered_accessible_countries(side, pub, mode);
            if (accessible.empty()) {
                continue;
            }

            if (mode == ActionMode::Coup) {
                for (const auto country_id : accessible) {
                    actions.push_back(ActionEncoding{
                        .card_id = card_id,
                        .mode = mode,
                        .targets = {country_id},
                    });
                }
                continue;
            }

            const auto ops = effective_ops(card_id, pub, side);
            const auto opponent = other_side(side);
            if (static_cast<int>(accessible.size()) > max_influence_targets) {
                accessible.resize(max_influence_targets);
            }

            // Per-country op costs: 2 for opponent-controlled, 1 otherwise.
            std::vector<int> inf_costs;
            inf_costs.reserve(accessible.size());
            for (const auto cid : accessible) {
                inf_costs.push_back(controls_country(opponent, cid, pub) ? 2 : 1);
            }

            std::vector<std::vector<CountryId>> combos;
            std::vector<CountryId> current;
            enumerate_influence_budget<CountryId>(accessible, inf_costs, ops, 0, current, combos);
            for (auto& combo : combos) {
                actions.push_back(ActionEncoding{
                    .card_id = card_id,
                    .mode = mode,
                    .targets = std::move(combo),
                });
            }

            if (pub.vietnam_revolts_active && side == Side::USSR) {
                std::vector<CountryId> sea_accessible;
                std::vector<int> sea_costs;
                for (size_t idx = 0; idx < accessible.size(); ++idx) {
                    if (country_spec(accessible[idx]).region == Region::SoutheastAsia) {
                        sea_accessible.push_back(accessible[idx]);
                        sea_costs.push_back(inf_costs[idx]);
                    }
                }
                if (!sea_accessible.empty()) {
                    combos.clear();
                    current.clear();
                    enumerate_influence_budget<CountryId>(sea_accessible, sea_costs, ops + 1, 0, current, combos);
                    for (auto& combo : combos) {
                        actions.push_back(ActionEncoding{
                            .card_id = card_id,
                            .mode = mode,
                            .targets = std::move(combo),
                        });
                    }
                }
            }

            if (card_id == kChinaCardId) {
                std::vector<CountryId> asia_accessible;
                std::vector<int> asia_costs;
                for (size_t idx = 0; idx < accessible.size(); ++idx) {
                    if (country_spec(accessible[idx]).region == Region::Asia) {
                        asia_accessible.push_back(accessible[idx]);
                        asia_costs.push_back(inf_costs[idx]);
                    }
                }
                if (!asia_accessible.empty()) {
                    combos.clear();
                    current.clear();
                    enumerate_influence_budget<CountryId>(asia_accessible, asia_costs, ops + 1, 0, current, combos);
                    for (auto& combo : combos) {
                        actions.push_back(ActionEncoding{
                            .card_id = card_id,
                            .mode = mode,
                            .targets = std::move(combo),
                        });
                    }
                }
            }
        }
    }
    return actions;
}

std::optional<ActionEncoding> sample_action(
    const CardSet& hand,
    const PublicState& pub,
    Side side,
    bool holds_china,
    Pcg64Rng& rng
) {
    auto playable = legal_cards(hand, pub, side, holds_china);
    shuffle_with_numpy_rng(playable, rng);

    for (const auto card_id : playable) {
        auto modes = legal_modes(card_id, pub, side);
        if (card_id == 32 && !has_eligible_opponent_card(hand, side)) {
            modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        }
        if (modes.empty()) {
            continue;
        }
        const auto mode = modes[rng.choice_index(modes.size())];
        if (mode == ActionMode::Space || mode == ActionMode::Event || mode == ActionMode::EventFirst) {
            return ActionEncoding{
                .card_id = card_id,
                .mode = mode,
                .targets = {},
            };
        }

        auto accessible = filtered_accessible_countries(side, pub, mode);
        if (accessible.empty()) {
            continue;
        }
        if (mode == ActionMode::Coup) {
            return ActionEncoding{
                .card_id = card_id,
                .mode = mode,
                .targets = {accessible[rng.choice_index(accessible.size())]},
            };
        }

        auto ops = effective_ops(card_id, pub, side);
        std::vector<CountryId> pool = accessible;
        std::vector<CountryId> sea_pool;
        if (pub.vietnam_revolts_active && side == Side::USSR) {
            std::copy_if(accessible.begin(), accessible.end(), std::back_inserter(sea_pool), [](CountryId cid) {
                return country_spec(cid).region == Region::SoutheastAsia;
            });
        }
        if (card_id == kChinaCardId) {
            std::vector<CountryId> asia_pool;
            std::copy_if(pool.begin(), pool.end(), std::back_inserter(asia_pool), [](CountryId cid) {
                return country_spec(cid).region == Region::Asia;
            });
            if (!asia_pool.empty()) {
                if (rng.bernoulli(0.5)) {
                    pool = std::move(asia_pool);
                    ++ops;
                }
            }
        }
        if (!sea_pool.empty() && rng.bernoulli(0.5)) {
            pool = std::move(sea_pool);
            ++ops;
        }

        ActionEncoding action{
            .card_id = card_id,
            .mode = mode,
            .targets = {},
        };
        for (int i = 0; i < ops; ++i) {
            action.targets.push_back(pool[rng.choice_index(pool.size())]);
        }
        return action;
    }

    return std::nullopt;
}

bool has_legal_action(const CardSet& hand, const PublicState& pub, Side side, bool holds_china) {
    for (const auto card_id : legal_cards(hand, pub, side, holds_china)) {
        if (!legal_modes(card_id, pub, side).empty()) {
            return true;
        }
    }
    return false;
}

}  // namespace ts
