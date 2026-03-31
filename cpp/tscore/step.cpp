#include "step.hpp"

#include <algorithm>

#include "adjacency.hpp"
#include "dice.hpp"
#include "game_data.hpp"

namespace ts {
namespace {

constexpr std::array<CardId, 5> kWarCardIds = {11, 13, 24, 39, 105};

bool contains(std::span<const CardId> values, CardId value) {
    return std::find(values.begin(), values.end(), value) != values.end();
}

void handle_card_played(PublicState& pub, CardId card_id, Side side, ActionMode mode) {
    if (pub.discard.test(card_id) || pub.removed.test(card_id)) {
        return;
    }
    if (card_id == kChinaCardId) {
        pub.china_held_by = other_side(side);
        pub.china_playable = false;
        return;
    }
    const auto& spec = card_spec(card_id);
    if (mode == ActionMode::Event && spec.starred) {
        pub.removed.set(card_id);
    } else {
        pub.discard.set(card_id);
    }
}

std::tuple<PublicState, bool, std::optional<Side>> apply_event(
    const PublicState& pub,
    const ActionEncoding& action,
    Side side,
    std::mt19937& /*rng*/
) {
    auto next = pub;

    if (
        side == Side::US &&
        contains(kWarCardIds, action.card_id) &&
        next.flower_power_active &&
        !next.flower_power_cancelled
    ) {
        next.vp += 2;
    }

    const auto& spec = card_spec(action.card_id);
    if (spec.is_scoring) {
        auto result = apply_scoring_card(action.card_id, next);
        next.vp += result.vp_delta;
        if (result.clear_shuttle) {
            next.shuttle_diplomacy_active = false;
        }
        handle_card_played(next, action.card_id, side, ActionMode::Event);
        if (result.game_over) {
            return {next, true, result.winner};
        }
        return {next, false, std::nullopt};
    }

    handle_card_played(next, action.card_id, side, ActionMode::Event);
    return {next, false, std::nullopt};
}

}  // namespace

std::tuple<PublicState, bool, std::optional<Side>> apply_action(
    const PublicState& pub,
    const ActionEncoding& action,
    Side side,
    std::mt19937& rng
) {
    auto next = pub;

    switch (action.mode) {
        case ActionMode::Influence:
            for (const auto target : action.targets) {
                next.set_influence(side, target, next.influence_of(side, target) + 1);
            }
            handle_card_played(next, action.card_id, side, ActionMode::Influence);
            break;

        case ActionMode::Coup: {
            const auto target = action.targets.front();
            auto ops = effective_ops(action.card_id, pub, side);
            if (action.card_id == kChinaCardId && country_spec(target).region == Region::Asia) {
                ++ops;
            }
            auto net = coup_result(ops, country_spec(target).stability, rng);
            if (
                pub.latam_coup_bonus.has_value() &&
                (country_spec(target).region == Region::CentralAmerica || country_spec(target).region == Region::SouthAmerica)
            ) {
                net += side == *pub.latam_coup_bonus ? 1 : -1;
            }
            if (net > 0) {
                const auto opp = other_side(side);
                const auto removed = std::min(net, next.influence_of(opp, target));
                next.set_influence(opp, target, next.influence_of(opp, target) - removed);
                if (const auto excess = net - removed; excess > 0) {
                    next.set_influence(side, target, next.influence_of(side, target) + excess);
                }
            }
            if (country_spec(target).is_battleground && !(side == Side::US && next.nuclear_subs_active)) {
                next.defcon = std::max(1, next.defcon - 1);
            }
            next.milops[to_index(side)] = std::max(next.milops[to_index(side)], ops);
            handle_card_played(next, action.card_id, side, ActionMode::Coup);
            break;
        }

        case ActionMode::Realign: {
            const auto& graph = adjacency();
            for (const auto target : action.targets) {
                const auto ussr_inf = next.influence_of(Side::USSR, target);
                const auto us_inf = next.influence_of(Side::US, target);
                auto count_adj = [&](Side player) {
                    int total = 0;
                    for (const auto neighbor : graph[target]) {
                        if (neighbor == kUsaAnchorId || neighbor == kUssrAnchorId) {
                            continue;
                        }
                        if (controls_country(player, neighbor, next)) {
                            ++total;
                        }
                    }
                    return total;
                };
                const auto ussr_anchor = std::find(graph[target].begin(), graph[target].end(), kUssrAnchorId) != graph[target].end() ? 1 : 0;
                const auto us_anchor = std::find(graph[target].begin(), graph[target].end(), kUsaAnchorId) != graph[target].end() ? 1 : 0;
                const auto [ussr_total, us_total] = realign_result(
                    ussr_inf,
                    us_inf,
                    count_adj(Side::USSR) + ussr_anchor,
                    count_adj(Side::US) + us_anchor,
                    rng
                );
                if (ussr_total > us_total) {
                    next.set_influence(Side::US, target, std::max(0, next.influence_of(Side::US, target) - (ussr_total - us_total)));
                } else if (us_total > ussr_total) {
                    next.set_influence(Side::USSR, target, std::max(0, next.influence_of(Side::USSR, target) - (us_total - ussr_total)));
                }
            }
            handle_card_played(next, action.card_id, side, ActionMode::Realign);
            break;
        }

        case ActionMode::Space: {
            const auto current_level = next.space[to_index(side)];
            if (space_result(current_level, rng)) {
                const auto new_level = current_level + 1;
                next.space[to_index(side)] = new_level;
                if (new_level == 4 && !next.space_level4_first.has_value()) {
                    next.space_level4_first = side;
                }
                if (new_level == 6 && !next.space_level6_first.has_value()) {
                    next.space_level6_first = side;
                }
                static constexpr std::array<std::pair<int, int>, 9> kSpaceVp = {{
                    {0, 0}, {2, 0}, {0, 0}, {2, 0}, {0, 0}, {3, 1}, {0, 0}, {4, 2}, {2, 0},
                }};
                const auto [first_vp, second_vp] = kSpaceVp[new_level];
                const auto opponent_level = next.space[to_index(other_side(side))];
                const auto vp = opponent_level < new_level ? first_vp : second_vp;
                next.vp += side == Side::USSR ? vp : -vp;
            }
            next.space_attempts[to_index(side)] += 1;
            handle_card_played(next, action.card_id, side, ActionMode::Space);
            break;
        }

        case ActionMode::Event: {
            auto [event_pub, over, winner] = apply_event(pub, action, side, rng);
            return {event_pub, over, winner};
        }
    }

    const auto [over, winner] = check_vp_win(next);
    return {next, over, winner};
}

std::tuple<bool, std::optional<Side>> check_vp_win(const PublicState& pub) {
    if (pub.vp >= 20) {
        return {true, Side::USSR};
    }
    if (pub.vp <= -20) {
        return {true, Side::US};
    }
    if (pub.defcon <= 1) {
        return {true, other_side(pub.phasing)};
    }
    return {false, std::nullopt};
}

}  // namespace ts
