// Native whole-game loop implementation, including headline handling, extra
// ARs, trap/NORAD hooks, and traced execution for parity work.

#include "game_loop.hpp"

#include <algorithm>

#include "human_openings.hpp"

#include "dice.hpp"
#include "game_data.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts {
namespace {

constexpr int kMidWarTurn = 4;
constexpr int kLateWarTurn = 8;
constexpr int kMaxTurns = 10;
constexpr int kSpaceShuttleArs = 8;

/// Choose a country from a pool: use policy callback if available, otherwise random.
template <typename Container>
CountryId choose_country(
    const PublicState& pub, CardId card_id, Side side,
    const Container& pool, Pcg64Rng& rng, const PolicyCallbackFn* cb
) {
    const int n = static_cast<int>(std::size(pool));
    if (n == 0) return 0;
    if (cb && n > 1) {
        EventDecision dec;
        dec.source_card = card_id;
        dec.kind = DecisionKind::CountrySelect;
        dec.n_options = n;
        dec.acting_side = side;
        for (int i = 0; i < n && i < EventDecision::kMaxEligible; ++i) {
            dec.eligible_ids[i] = static_cast<int>(pool[i]);
        }
        const int choice = std::clamp((*cb)(pub, dec), 0, n - 1);
        return static_cast<CountryId>(pool[choice]);
    }
    return pool[rng.choice_index(static_cast<size_t>(n))];
}

constexpr CountryId kWestGermanyId = 18;
constexpr std::array<CardId, 17> kCatCCardIds = {5, 10, 26, 32, 36, 45, 46, 47, 52, 68, 78, 84, 88, 95, 98, 101, 108};

struct PendingHeadline {
    Side side = Side::USSR;
    bool holds_china = false;
    CardSet hand_snapshot;
    ActionEncoding action;
};

// Keep China-card ownership booleans synchronized with the public-state owner.
void sync_china(GameState& gs) {
    gs.ussr_holds_china = gs.pub.china_held_by == Side::USSR;
    gs.us_holds_china = gs.pub.china_held_by == Side::US;
}

bool is_cat_c_card(CardId card_id) {
    return std::find(kCatCCardIds.begin(), kCatCCardIds.end(), card_id) != kCatCCardIds.end();
}

float normalized_exploration_rate(const GameLoopConfig& config) {
    return std::clamp(config.exploration_rate, 0.0f, 1.0f);
}

std::optional<ActionEncoding> choose_headline_action_with_config(
    const PolicyFn& policy,
    const PublicState& pub,
    const CardSet& hand,
    Side side,
    bool holds_china,
    Pcg64Rng& rng,
    const GameLoopConfig& config
) {
    const auto exploration_rate = normalized_exploration_rate(config);
    if (exploration_rate > 0.0f && rng.bernoulli(static_cast<double>(exploration_rate))) {
        const auto cards = legal_cards(hand, pub, side, holds_china);
        if (cards.empty()) {
            return std::nullopt;
        }
        return ActionEncoding{
            .card_id = cards[rng.choice_index(cards.size())],
            .mode = ActionMode::Event,
            .targets = {},
        };
    }
    return policy(pub, hand, holds_china, rng);
}

std::optional<ActionEncoding> choose_action_with_config(
    const PolicyFn& policy,
    const PublicState& pub,
    const CardSet& hand,
    Side side,
    bool holds_china,
    Pcg64Rng& rng,
    const GameLoopConfig& config
) {
    const auto exploration_rate = normalized_exploration_rate(config);
    if (exploration_rate > 0.0f && rng.bernoulli(static_cast<double>(exploration_rate))) {
        auto actions = enumerate_actions(hand, pub, side, holds_china);
        if (!actions.empty()) {
            return actions[rng.choice_index(actions.size())];
        }
    }
    return policy(pub, hand, holds_china, rng);
}

// Mirror Python card-lifecycle handling for cards that leave a hand due to a
// live game effect rather than replay reduction.
void card_played(PublicState& pub, CardId card_id, Side side) {
    if (pub.discard.test(card_id) || pub.removed.test(card_id)) {
        return;
    }
    if (card_id == kChinaCardId) {
        pub.china_held_by = other_side(side);
        pub.china_playable = false;
        return;
    }
    const auto& spec = card_spec(card_id);
    if (spec.starred) {
        pub.removed.set(card_id);
    } else {
        pub.discard.set(card_id);
    }
}

void discard_from_hand(GameState& gs, Side side, CardId card_id, PublicState& pub) {
    gs.hands[to_index(side)].reset(card_id);
    const auto& spec = card_spec(card_id);
    if (spec.starred) {
        pub.removed.set(card_id);
    } else {
        pub.discard.set(card_id);
    }
}

std::tuple<PublicState, bool, std::optional<Side>> fire_event_with_state(
    GameState& gs,
    CardId card_id,
    Side event_side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

std::optional<CardId> draw_one(GameState& gs, Pcg64Rng& rng) {
    if (gs.deck.empty()) {
        std::vector<CardId> reshuffled;
        for (int raw = 1; raw <= kMaxCardId; ++raw) {
            const auto candidate = static_cast<CardId>(raw);
            if (gs.pub.discard.test(candidate) && !gs.pub.removed.test(candidate)) {
                reshuffled.push_back(candidate);
            }
        }
        if (reshuffled.empty()) {
            return std::nullopt;
        }
        shuffle_with_numpy_rng(reshuffled, rng);
        gs.deck = std::move(reshuffled);
        gs.pub.discard.reset();
    }
    if (gs.deck.empty()) {
        return std::nullopt;
    }
    const auto card = gs.deck.back();
    gs.deck.pop_back();
    return card;
}

void apply_ops_randomly(
    PublicState& pub,
    Side side,
    int ops,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
) {
    auto accessible = accessible_countries(side, pub, ActionMode::Influence);
    if (accessible.empty()) {
        return;
    }
    const std::array<ActionMode, 4> modes = {
        ActionMode::Influence,
        ActionMode::Influence,
        ActionMode::Coup,
        ActionMode::Realign,
    };
    const auto mode = modes[static_cast<size_t>(
        choose_option(pub, 0, side, static_cast<int>(modes.size()), rng, policy_cb)
    )];
    const auto opponent = other_side(side);

    if (mode == ActionMode::Influence) {
        for (int i = 0; i < ops; ++i) {
            const auto target = choose_country(pub, 0, side, accessible, rng, policy_cb);
            pub.set_influence(side, target, pub.influence_of(side, target) + 1);
        }
        return;
    }

    if (mode == ActionMode::Coup) {
        auto targets = accessible;
        targets.erase(
            std::remove_if(
                targets.begin(),
                targets.end(),
                [&pub](CountryId cid) { return is_defcon_restricted(cid, pub); }
            ),
            targets.end()
        );
        if (targets.empty()) {
            // All coup targets are DEFCON-restricted; fall back to influence placement.
            for (int i = 0; i < ops; ++i) {
                const auto target = choose_country(pub, 0, side, accessible, rng, policy_cb);
                pub.set_influence(side, target, pub.influence_of(side, target) + 1);
            }
            return;
        }
        const auto target = choose_country(pub, 0, side, targets, rng, policy_cb);
        const auto net = coup_result(ops, country_spec(target).stability, rng);
        if (net > 0) {
            const auto removed = std::min(net, pub.influence_of(opponent, target));
            pub.set_influence(opponent, target, pub.influence_of(opponent, target) - removed);
            if (const auto excess = net - removed; excess > 0) {
                pub.set_influence(side, target, pub.influence_of(side, target) + excess);
            }
        }
        if (country_spec(target).is_battleground && !(side == Side::US && pub.nuclear_subs_active)) {
            pub.defcon = std::max(1, pub.defcon - 1);
        }
        pub.milops[to_index(side)] = std::max(pub.milops[to_index(side)], ops);
        return;
    }

    for (int i = 0; i < std::min(ops, static_cast<int>(accessible.size())); ++i) {
        const auto target = choose_country(pub, 0, side, accessible, rng, policy_cb);
        const auto ussr_inf = pub.influence_of(Side::USSR, target);
        const auto us_inf = pub.influence_of(Side::US, target);
        auto count_adj = [&](Side player) {
            int total = 0;
            for (const auto neighbor : adjacency()[target]) {
                if (neighbor == kUsaAnchorId || neighbor == kUssrAnchorId) {
                    continue;
                }
                if (controls_country(player, neighbor, pub)) {
                    ++total;
                }
            }
            return total;
        };
        const auto [ussr_total, us_total] = realign_result(ussr_inf, us_inf, count_adj(Side::USSR), count_adj(Side::US), rng);
        if (ussr_total > us_total) {
            pub.set_influence(Side::US, target, std::max(0, pub.influence_of(Side::US, target) - 1));
        } else if (us_total > ussr_total) {
            pub.set_influence(Side::USSR, target, std::max(0, pub.influence_of(Side::USSR, target) - 1));
        }
    }
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_trap_ar(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
) {
    bool trapped = false;
    bool bear_trap = false;
    if (side == Side::USSR && gs.pub.bear_trap_active) {
        trapped = true;
        bear_trap = true;
    } else if (side == Side::US && gs.pub.quagmire_active) {
        trapped = true;
    }
    if (!trapped) {
        return std::nullopt;
    }

    std::vector<CardId> eligible;
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        const auto candidate = static_cast<CardId>(raw);
        if (
            gs.hands[to_index(side)].test(candidate) &&
            candidate != kChinaCardId &&
            !card_spec(candidate).is_scoring &&
            card_spec(candidate).ops >= 2
        ) {
            eligible.push_back(candidate);
        }
    }

    auto pub = gs.pub;
    if (eligible.empty()) {
        const auto [over, winner] = check_vp_win(pub);
        gs.pub = pub;
        return std::tuple{pub, over, winner};
    }

    const auto chosen = choose_card(pub, bear_trap ? 47 : 45, side, eligible, rng, policy_cb);
    discard_from_hand(gs, side, chosen, pub);
    if (roll_d6(rng) <= 4) {
        if (bear_trap) {
            pub.bear_trap_active = false;
        } else {
            pub.quagmire_active = false;
        }
    }
    gs.pub = pub;
    const auto [over, winner] = check_vp_win(pub);
    return std::tuple{pub, over, winner};
}

std::tuple<PublicState, bool, std::optional<Side>> apply_hand_event(
    GameState& gs,
    CardId card_id,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
) {
    auto pub = gs.pub;

    switch (card_id) {
        case 5: {
            auto hand = hand_to_vector(gs.hands[to_index(Side::USSR)]);
            if (!hand.empty()) {
                const auto target = choose_card(pub, 5, Side::USSR, hand, rng, policy_cb);
                gs.hands[to_index(Side::USSR)].reset(target);
                if (card_spec(target).starred) {
                    pub.removed.set(target);
                } else {
                    pub.discard.set(target);
                }
                gs.pub = pub;
                if (card_spec(target).is_scoring) {
                    auto result = apply_scoring_card(target, pub);
                    pub.vp += result.vp_delta;
                    if (result.clear_shuttle) {
                        pub.shuttle_diplomacy_active = false;
                    }
                    if (result.game_over) {
                        card_played(pub, 5, side);
                        gs.pub = pub;
                        return {pub, true, result.winner};
                    }
                } else if (card_spec(target).side == Side::US) {
                    auto [event_pub, over, winner] = fire_event_with_state(gs, target, Side::US, rng, policy_cb);
                    pub = event_pub;
                    if (over) {
                        card_played(pub, 5, side);
                        gs.pub = pub;
                        return std::tuple{pub, true, winner};
                    }
                }
            }
            break;
        }

        case 10: {
            std::vector<CardId> eligible;
            for (int raw = 1; raw <= kMaxCardId; ++raw) {
                const auto candidate = static_cast<CardId>(raw);
                if (
                    gs.hands[to_index(Side::US)].test(candidate) &&
                    candidate != kChinaCardId &&
                    effective_ops(candidate, pub, Side::US) >= 3
                ) {
                    eligible.push_back(candidate);
                }
            }
            if (!eligible.empty()) {
                discard_from_hand(gs, Side::US, choose_card(pub, 10, Side::US, eligible, rng, policy_cb), pub);
            } else {
                pub.set_influence(Side::US, kWestGermanyId, 0);
            }
            break;
        }

        case 26: {
            // CIA Created: +1 US influence in any accessible country
            const auto accessible = accessible_countries(Side::US, pub, ActionMode::Influence);
            if (!accessible.empty()) {
                const auto target = choose_country(pub, 26, Side::US, accessible, rng, policy_cb);
                pub.set_influence(Side::US, target, pub.influence_of(Side::US, target) + 1);
            }
            break;
        }

        case 32: {
            const auto opponent = other_side(side);
            std::vector<CardId> eligible;
            for (int raw = 1; raw <= kMaxCardId; ++raw) {
                const auto candidate = static_cast<CardId>(raw);
                if (
                    gs.hands[to_index(side)].test(candidate) &&
                    candidate != kChinaCardId &&
                    card_spec(candidate).side == opponent &&
                    !card_spec(candidate).is_scoring
                ) {
                    eligible.push_back(candidate);
                }
            }
            if (!eligible.empty()) {
                const auto chosen = choose_card(pub, 32, side, eligible, rng, policy_cb);
                const auto ops = effective_ops(chosen, pub, side);
                discard_from_hand(gs, side, chosen, pub);
                apply_ops_randomly(pub, side, ops, rng, policy_cb);
            }
            break;
        }

        case 36: {
            std::vector<Region> regions;
            auto maybe_add = [&](CardId scoring_card, Region region) {
                if (gs.hands[to_index(Side::US)].test(scoring_card)) {
                    regions.push_back(region);
                }
            };
            maybe_add(1, Region::Asia);
            maybe_add(2, Region::Europe);
            maybe_add(3, Region::MiddleEast);
            maybe_add(40, Region::CentralAmerica);
            maybe_add(41, Region::SoutheastAsia);
            maybe_add(80, Region::Africa);
            maybe_add(82, Region::SouthAmerica);
            std::sort(regions.begin(), regions.end(), [](Region lhs, Region rhs) { return static_cast<int>(lhs) < static_cast<int>(rhs); });
            regions.erase(std::unique(regions.begin(), regions.end()), regions.end());
            for (const auto region : regions) {
                std::vector<CountryId> pool;
                for (const auto cid : all_country_ids()) {
                    if (cid != 64 && cid != kUsaAnchorId && cid != kUssrAnchorId && country_spec(cid).region == region) {
                        pool.push_back(cid);
                    }
                }
                if (!pool.empty()) {
                    const auto target = choose_country(pub, 36, Side::USSR, pool, rng, policy_cb);
                    pub.set_influence(Side::USSR, target, pub.influence_of(Side::USSR, target) + 1);
                }
            }
            break;
        }

        case 45:
            pub.quagmire_active = true;
            break;

        case 46: {
            pub.defcon = std::min(5, pub.defcon + 1);
            pub.salt_active = true;
            auto discarded = hand_to_vector(pub.discard);
            if (!discarded.empty()) {
                const auto chosen = choose_card(pub, 46, side, discarded, rng, policy_cb);
                pub.discard.reset(chosen);
                gs.hands[to_index(side)].set(chosen);
            }
            break;
        }

        case 47:
            pub.bear_trap_active = true;
            break;

        case 52: {
            const auto opponent = other_side(side);
            std::vector<CardId> candidates;
            int max_ops = -1;
            for (int raw = 1; raw <= kMaxCardId; ++raw) {
                const auto candidate = static_cast<CardId>(raw);
                if (
                    gs.hands[to_index(opponent)].test(candidate) &&
                    candidate != kChinaCardId &&
                    !card_spec(candidate).is_scoring
                ) {
                    const auto ops = effective_ops(candidate, pub, opponent);
                    if (ops > max_ops) {
                        max_ops = ops;
                        candidates = {candidate};
                    } else if (ops == max_ops) {
                        candidates.push_back(candidate);
                    }
                }
            }
            if (!candidates.empty()) {
                const auto chosen = choose_card(pub, 52, side, candidates, rng, policy_cb);
                gs.hands[to_index(opponent)].reset(chosen);
                apply_ops_randomly(pub, side, effective_ops(chosen, pub, side), rng, policy_cb);
                gs.hands[to_index(opponent)].set(chosen);
            }
            break;
        }

        case 95: {
            const auto opponent = other_side(side);
            const auto discard_count = opponent == Side::US && pub.iran_hostage_crisis_active ? 2 : 1;
            std::vector<CardId> candidates;
            for (int raw = 1; raw <= kMaxCardId; ++raw) {
                const auto candidate = static_cast<CardId>(raw);
                if (gs.hands[to_index(opponent)].test(candidate) && candidate != kChinaCardId) {
                    candidates.push_back(candidate);
                }
            }
            shuffle_with_numpy_rng(candidates, rng);
            candidates.resize(std::min(discard_count, static_cast<int>(candidates.size())));
            for (const auto chosen : candidates) {
                discard_from_hand(gs, opponent, chosen, pub);
            }
            break;
        }

        case 68: {
            std::vector<CardId> candidates;
            for (int raw = 1; raw <= kMaxCardId; ++raw) {
                const auto candidate = static_cast<CardId>(raw);
                if (
                    gs.hands[to_index(Side::USSR)].test(candidate) &&
                    candidate != kChinaCardId &&
                    !card_spec(candidate).is_scoring
                ) {
                    candidates.push_back(candidate);
                }
            }
            if (!candidates.empty()) {
                const auto chosen = choose_card(pub, 68, Side::US, candidates, rng, policy_cb);
                gs.hands[to_index(Side::USSR)].reset(chosen);
                apply_ops_randomly(pub, Side::US, effective_ops(chosen, pub, Side::US), rng, policy_cb);
                gs.hands[to_index(Side::USSR)].set(chosen);
            }
            break;
        }

        case 78: {
            std::vector<CardId> discardable;
            for (int raw = 1; raw <= kMaxCardId; ++raw) {
                const auto candidate = static_cast<CardId>(raw);
                if (
                    gs.hands[to_index(Side::US)].test(candidate) &&
                    candidate != kChinaCardId &&
                    !card_spec(candidate).is_scoring
                ) {
                    discardable.push_back(candidate);
                }
            }
            const auto discard_count = discardable.empty() ? 0 : rng.uniform_int(0, static_cast<int>(discardable.size()));
            shuffle_with_numpy_rng(discardable, rng);
            discardable.resize(static_cast<size_t>(discard_count));
            for (const auto chosen : discardable) {
                discard_from_hand(gs, Side::US, chosen, pub);
            }
            gs.pub = pub;
            for (int i = 0; i < discard_count; ++i) {
                if (const auto drawn = draw_one(gs, rng); drawn.has_value()) {
                    gs.hands[to_index(Side::US)].set(*drawn);
                }
            }
            pub = gs.pub;
            break;
        }

        case 84: {
            bool us_controls_me = false;
            for (const auto cid : all_country_ids()) {
                if (country_spec(cid).region == Region::MiddleEast && controls_country(Side::US, cid, pub)) {
                    us_controls_me = true;
                    break;
                }
            }
            if (us_controls_me) {
                std::vector<CardId> drawn;
                for (int i = 0; i < 5; ++i) {
                    if (const auto drawn_card = draw_one(gs, rng); drawn_card.has_value()) {
                        drawn.push_back(*drawn_card);
                    } else {
                        break;
                    }
                }
                if (!drawn.empty()) {
                    const auto keep_count = rng.uniform_int(0, static_cast<int>(drawn.size()));
                    shuffle_with_numpy_rng(drawn, rng);
                    const auto discard_split = static_cast<size_t>(drawn.size() - keep_count);
                    for (size_t i = 0; i < discard_split; ++i) {
                        if (card_spec(drawn[i]).starred) {
                            pub.removed.set(drawn[i]);
                        } else {
                            pub.discard.set(drawn[i]);
                        }
                    }
                    gs.deck.insert(gs.deck.begin(), drawn.begin() + static_cast<std::ptrdiff_t>(discard_split), drawn.end());
                }
            }
            break;
        }

        case 88: {
            if (pub.space[to_index(Side::US)] > pub.space[to_index(Side::USSR)]) {
                auto discarded = hand_to_vector(pub.discard);
                discarded.erase(
                    std::remove_if(
                        discarded.begin(),
                        discarded.end(),
                        [](CardId candidate) { return candidate == kChinaCardId || card_spec(candidate).is_scoring; }
                    ),
                    discarded.end()
                );
                if (!discarded.empty()) {
                    const auto chosen = choose_card(pub, 88, side, discarded, rng, policy_cb);
                    pub.discard.reset(chosen);
                    gs.pub = pub;
                    auto [event_pub, over, winner] = fire_event_with_state(gs, chosen, side, rng, policy_cb);
                    pub = event_pub;
                    if (over) {
                        card_played(pub, 88, side);
                        gs.pub = pub;
                        return std::tuple{pub, true, winner};
                    }
                }
            }
            break;
        }

        case 98: {
            std::vector<CardId> candidates;
            for (int raw = 1; raw <= kMaxCardId; ++raw) {
                const auto candidate = static_cast<CardId>(raw);
                if (
                    gs.hands[to_index(Side::US)].test(candidate) &&
                    candidate != kChinaCardId &&
                    !card_spec(candidate).is_scoring
                ) {
                    candidates.push_back(candidate);
                }
            }
            std::optional<std::pair<CardId, CardId>> best_pair;
            int best_total = 999;
            for (size_t i = 0; i < candidates.size(); ++i) {
                for (size_t j = i + 1; j < candidates.size(); ++j) {
                    const auto total = card_spec(candidates[i]).ops + card_spec(candidates[j]).ops;
                    if (total >= 4 && total < best_total) {
                        best_total = total;
                        best_pair = {candidates[i], candidates[j]};
                    }
                }
            }
            if (best_pair.has_value()) {
                discard_from_hand(gs, Side::US, best_pair->first, pub);
                discard_from_hand(gs, Side::US, best_pair->second, pub);
            } else {
                pub.vp += 2;
            }
            break;
        }

        case 101: {
            std::vector<CardId> candidates;
            for (int raw = 1; raw <= kMaxCardId; ++raw) {
                const auto candidate = static_cast<CardId>(raw);
                if (gs.hands[to_index(Side::US)].test(candidate) && candidate != kChinaCardId) {
                    candidates.push_back(candidate);
                }
            }
            if (!candidates.empty()) {
                const auto chosen = choose_card(pub, 101, Side::US, candidates, rng, policy_cb);
                discard_from_hand(gs, Side::US, chosen, pub);
            }
            break;
        }

        case 108:
            if (side == Side::USSR) {
                pub.vp -= 2;
            }
            break;

        default:
            break;
    }

    card_played(pub, card_id, side);
    gs.pub = pub;
    const auto [over, winner] = check_vp_win(pub);
    return {pub, over, winner};
}

std::tuple<PublicState, bool, std::optional<Side>> fire_event_with_state(
    GameState& gs,
    CardId card_id,
    Side event_side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    if (is_cat_c_card(card_id)) {
        return apply_hand_event(gs, card_id, event_side, rng, policy_cb);
    }
    ActionEncoding action{
        .card_id = card_id,
        .mode = ActionMode::Event,
        .targets = {},
    };
    auto [new_pub, over, winner] = apply_action(gs.pub, action, event_side, rng, policy_cb);
    gs.pub = new_pub;
    return {new_pub, over, winner};
}

std::tuple<PublicState, bool, std::optional<Side>> apply_action_with_hands(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
) {
    if (action.mode != ActionMode::Event) {
        const auto owner = card_spec(action.card_id).side;
        if (owner == other_side(side)) {
            auto [new_pub, over, winner] = fire_event_with_state(gs, action.card_id, owner, rng, policy_cb);
            if (over) {
                return {new_pub, true, winner};
            }
        }
    }

    if (action.mode == ActionMode::Event && is_cat_c_card(action.card_id)) {
        return apply_hand_event(gs, action.card_id, side, rng, policy_cb);
    }

    auto [new_pub, over, winner] = apply_action(gs.pub, action, side, rng, policy_cb);
    gs.pub = new_pub;
    if (!over && action.mode == ActionMode::Space) {
        const auto opponent = other_side(side);
        const auto l6_holder = gs.pub.space_level6_first;
        if (
            l6_holder.has_value() &&
            *l6_holder == opponent &&
            gs.pub.space[to_index(opponent)] >= 6 &&
            gs.pub.space[to_index(side)] < 6
        ) {
            const auto opp_hand = hand_to_vector(gs.hands[to_index(opponent)]);
            if (!opp_hand.empty()) {
                const auto discard_card = opp_hand.front();
                gs.hands[to_index(opponent)].reset(discard_card);
                gs.pub.discard.set(discard_card);
                new_pub = gs.pub;
            }
        }
    }
    return {new_pub, over, winner};
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_norad(
    GameState& gs,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
) {
    std::vector<CountryId> eligible;
    for (const auto cid : all_country_ids()) {
        if (gs.pub.influence_of(Side::US, cid) > 0) {
            eligible.push_back(cid);
        }
    }
    if (eligible.empty()) {
        return std::nullopt;
    }
    const auto target = choose_country(gs.pub, 106, Side::US, eligible, rng, policy_cb);
    gs.pub.set_influence(Side::US, target, gs.pub.influence_of(Side::US, target) + 1);
    const auto [over, winner] = check_vp_win(gs.pub);
    return std::tuple{gs.pub, over, winner};
}

std::string end_reason(const PublicState& pub, std::optional<Side> winner, int card_id = -1) {
    if (pub.defcon <= 1) {
        return "defcon1";
    }
    if (card_id == 103) {
        return "wargames";
    }
    if (winner.has_value()) {
        return "europe_control";
    }
    return "vp_threshold";
}

std::optional<GameResult> run_headline_phase(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    gs.phase = GamePhase::Headline;
    gs.pub.ar = 0;

    std::array<std::optional<PendingHeadline>, 2> chosen = {};
    for (const auto side : {Side::USSR, Side::US}) {
        gs.pub.phasing = side;
        const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
        const auto hand_snapshot = gs.hands[to_index(side)];
        auto headline_pub = gs.pub;
        headline_pub.ar = 0;
        auto action = choose_headline_action_with_config(
            side == Side::USSR ? ussr_policy : us_policy,
            headline_pub,
            gs.hands[to_index(side)],
            side,
            holds_china,
            rng,
            config
        );
        if (!action.has_value()) {
            continue;
        }
        action->mode = ActionMode::Event;
        action->targets.clear();
        if (gs.hands[to_index(side)].test(action->card_id)) {
            gs.hands[to_index(side)].reset(action->card_id);
        }
        chosen[to_index(side)] = PendingHeadline{
            .side = side,
            .holds_china = holds_china,
            .hand_snapshot = hand_snapshot,
            .action = *action,
        };
    }

    std::vector<PendingHeadline> ordered;
    for (const auto side : {Side::USSR, Side::US}) {
        if (chosen[to_index(side)].has_value()) {
            ordered.push_back(*chosen[to_index(side)]);
        }
    }

    if (chosen[to_index(Side::US)].has_value() && chosen[to_index(Side::US)]->action.card_id == 108) {
        if (chosen[to_index(Side::USSR)].has_value()) {
            gs.pub.discard.set(chosen[to_index(Side::USSR)]->action.card_id);
            ordered.erase(
                std::remove_if(
                    ordered.begin(),
                    ordered.end(),
                    [](const PendingHeadline& pending) { return pending.side == Side::USSR; }
                ),
                ordered.end()
            );
        }
    }

    std::sort(ordered.begin(), ordered.end(), [](const auto& lhs, const auto& rhs) {
        const auto lhs_ops = card_spec(lhs.action.card_id).ops;
        const auto rhs_ops = card_spec(rhs.action.card_id).ops;
        if (lhs_ops != rhs_ops) {
            return lhs_ops > rhs_ops;
        }
        return static_cast<int>(lhs.side) > static_cast<int>(rhs.side);
    });

    for (const auto& pending : ordered) {
        const auto side = pending.side;
        const auto& action = pending.action;
        const auto pub_snapshot = gs.pub;
        const auto deck_snapshot = gs.deck;
        const auto ussr_holds_china_snap = gs.ussr_holds_china;
        const auto us_holds_china_snap = gs.us_holds_china;
        const auto opp = side == Side::USSR ? Side::US : Side::USSR;
        const CardSet opp_hand_snap = chosen[to_index(opp)].has_value()
            ? chosen[to_index(opp)]->hand_snapshot
            : gs.hands[to_index(opp)];
        const auto vp_before = gs.pub.vp;
        const auto defcon_before = gs.pub.defcon;
        gs.pub.phasing = side;
        auto [new_pub, over, winner] = apply_action_with_hands(gs, action, side, rng);
        if (trace_steps != nullptr) {
            trace_steps->push_back(StepTrace{
                .turn = gs.pub.turn,
                .ar = 0,
                .side = side,
                .holds_china = pending.holds_china,
                .pub_snapshot = pub_snapshot,
                .hand_snapshot = pending.hand_snapshot,
                .action = action,
                .vp_before = vp_before,
                .vp_after = gs.pub.vp,
                .defcon_before = defcon_before,
                .defcon_after = gs.pub.defcon,
                .opp_hand_snapshot = opp_hand_snap,
                .deck_snapshot = deck_snapshot,
                .ussr_holds_china_snapshot = ussr_holds_china_snap,
                .us_holds_china_snapshot = us_holds_china_snap,
            });
        }
        sync_china(gs);
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = end_reason(gs.pub, winner, action.card_id),
            };
        }
    }

    return std::nullopt;
}

std::optional<GameResult> run_action_rounds(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    int total_ars,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    gs.phase = GamePhase::ActionRound;
    for (int ar = 1; ar <= kSpaceShuttleArs; ++ar) {
        gs.pub.ar = ar;
        for (const auto side : {Side::USSR, Side::US}) {
            if (ar > total_ars && gs.pub.space[to_index(side)] < kSpaceShuttleArs) {
                continue;
            }
            gs.pub.phasing = side;
            const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
            auto& hand = gs.hands[to_index(side)];
            if (auto trap_result = resolve_trap_ar(gs, side, rng); trap_result.has_value()) {
                auto& [new_pub, over, winner] = *trap_result;
                (void)new_pub;
                if (over) {
                    return GameResult{
                        .winner = winner,
                        .final_vp = gs.pub.vp,
                        .end_turn = gs.pub.turn,
                        .end_reason = end_reason(gs.pub, winner),
                    };
                }
                continue;
            }
            if (!has_legal_action(hand, gs.pub, side, holds_china)) {
                continue;
            }
            auto action = choose_action_with_config(
                side == Side::USSR ? ussr_policy : us_policy,
                gs.pub,
                hand,
                side,
                holds_china,
                rng,
                config
            );
            if (!action.has_value()) {
                continue;
            }
            const auto pub_snapshot = gs.pub;
            const auto hand_snapshot = hand;
            const auto deck_snapshot_ar = gs.deck;
            const auto ussr_holds_china_snap_ar = gs.ussr_holds_china;
            const auto us_holds_china_snap_ar = gs.us_holds_china;
            const auto opp_ar = side == Side::USSR ? Side::US : Side::USSR;
            const CardSet opp_hand_snap_ar = gs.hands[to_index(opp_ar)];
            if (hand.test(action->card_id)) {
                hand.reset(action->card_id);
            }
            const auto vp_before = gs.pub.vp;
            const auto defcon_before = gs.pub.defcon;
            auto [new_pub, over, winner] = apply_action_with_hands(gs, *action, side, rng);
            if (trace_steps != nullptr) {
                trace_steps->push_back(StepTrace{
                    .turn = gs.pub.turn,
                    .ar = ar,
                    .side = side,
                    .holds_china = holds_china,
                    .pub_snapshot = pub_snapshot,
                    .hand_snapshot = hand_snapshot,
                    .action = *action,
                    .vp_before = vp_before,
                    .vp_after = gs.pub.vp,
                    .defcon_before = defcon_before,
                    .defcon_after = gs.pub.defcon,
                    .opp_hand_snapshot = opp_hand_snap_ar,
                    .deck_snapshot = deck_snapshot_ar,
                    .ussr_holds_china_snapshot = ussr_holds_china_snap_ar,
                    .us_holds_china_snapshot = us_holds_china_snap_ar,
                });
            }
            sync_china(gs);
            if (over) {
                return GameResult{
                    .winner = winner,
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = end_reason(gs.pub, winner, action->card_id),
                };
            }
            if (side == Side::USSR && gs.pub.norad_active && gs.pub.defcon == 2) {
                if (auto norad = resolve_norad(gs, rng); norad.has_value()) {
                    auto& [norad_pub, norad_over, norad_winner] = *norad;
                    (void)norad_pub;
                    if (norad_over) {
                        return GameResult{
                            .winner = norad_winner,
                            .final_vp = gs.pub.vp,
                            .end_turn = gs.pub.turn,
                            .end_reason = end_reason(gs.pub, norad_winner),
                        };
                    }
                }
            }
        }
    }
    return std::nullopt;
}

std::optional<GameResult> run_extra_action_round(
    GameState& gs,
    Side side,
    const PolicyFn& policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    gs.pub.ar = std::max(gs.pub.ar, ars_for_turn(gs.pub.turn)) + 1;
    gs.pub.phasing = side;
    const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
    auto& hand = gs.hands[to_index(side)];
    if (hand.none()) {
        return std::nullopt;
    }
    if (auto trap_result = resolve_trap_ar(gs, side, rng); trap_result.has_value()) {
        auto& [new_pub, over, winner] = *trap_result;
        (void)new_pub;
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = end_reason(gs.pub, winner),
            };
        }
        return std::nullopt;
    }
    if (!has_legal_action(hand, gs.pub, side, holds_china)) {
        return std::nullopt;
    }
    auto action = choose_action_with_config(policy, gs.pub, hand, side, holds_china, rng, config);
    if (!action.has_value()) {
        return std::nullopt;
    }
    const auto pub_snapshot = gs.pub;
    const auto hand_snapshot = hand;
    const auto deck_snapshot_extra = gs.deck;
    const auto ussr_holds_china_snap_extra = gs.ussr_holds_china;
    const auto us_holds_china_snap_extra = gs.us_holds_china;
    const auto opp_extra = side == Side::USSR ? Side::US : Side::USSR;
    const CardSet opp_hand_snap_extra = gs.hands[to_index(opp_extra)];
    if (hand.test(action->card_id)) {
        hand.reset(action->card_id);
    }
    const auto vp_before = gs.pub.vp;
    const auto defcon_before = gs.pub.defcon;
    auto [new_pub, over, winner] = apply_action_with_hands(gs, *action, side, rng);
    if (trace_steps != nullptr) {
        trace_steps->push_back(StepTrace{
            .turn = gs.pub.turn,
            .ar = gs.pub.ar,
            .side = side,
            .holds_china = holds_china,
            .pub_snapshot = pub_snapshot,
            .hand_snapshot = hand_snapshot,
            .action = *action,
            .vp_before = vp_before,
            .vp_after = gs.pub.vp,
            .defcon_before = defcon_before,
            .defcon_after = gs.pub.defcon,
            .opp_hand_snapshot = opp_hand_snap_extra,
            .deck_snapshot = deck_snapshot_extra,
            .ussr_holds_china_snapshot = ussr_holds_china_snap_extra,
            .us_holds_china_snapshot = us_holds_china_snap_extra,
        });
    }
    sync_china(gs);
    if (over) {
        return GameResult{
            .winner = winner,
            .final_vp = gs.pub.vp,
            .end_turn = gs.pub.turn,
            .end_reason = end_reason(gs.pub, winner),
        };
    }
    if (side == Side::USSR && gs.pub.norad_active && gs.pub.defcon == 2) {
        if (auto norad = resolve_norad(gs, rng); norad.has_value()) {
            auto& [norad_pub, norad_over, norad_winner] = *norad;
            (void)norad_pub;
            if (norad_over) {
                return GameResult{
                    .winner = norad_winner,
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = end_reason(gs.pub, norad_winner),
                };
            }
        }
    }
    return std::nullopt;
}

std::optional<GameResult> end_of_turn(GameState& gs, int turn) {
    gs.phase = GamePhase::Cleanup;

    const auto defcon = gs.pub.defcon;
    for (const auto side : {Side::USSR, Side::US}) {
        const auto shortfall = std::max(0, defcon - gs.pub.milops[to_index(side)]);
        if (shortfall == 0) {
            continue;
        }
        if (side == Side::USSR) {
            gs.pub.vp -= shortfall;
        } else {
            gs.pub.vp += shortfall;
        }
    }

    auto [over, winner] = check_vp_win(gs.pub);
    if (over) {
        return GameResult{
            .winner = winner,
            .final_vp = gs.pub.vp,
            .end_turn = gs.pub.turn,
            .end_reason = "vp",
        };
    }

    gs.pub.defcon = std::min(5, gs.pub.defcon + 1);
    gs.pub.milops = {0, 0};
    gs.pub.space_attempts = {0, 0};
    gs.pub.ops_modifier = {0, 0};
    gs.pub.vietnam_revolts_active = false;
    gs.pub.north_sea_oil_extra_ar = false;
    gs.pub.glasnost_extra_ar = false;
    gs.pub.chernobyl_blocked_region.reset();
    gs.pub.latam_coup_bonus.reset();

    if (turn == kMaxTurns) {
        auto final = apply_final_scoring(gs.pub);
        gs.pub.vp += final.vp_delta;
        if (final.game_over) {
            return GameResult{
                .winner = final.winner,
                .final_vp = gs.pub.vp,
                .end_turn = turn,
                .end_reason = "europe_control",
            };
        }
        std::tie(over, winner) = check_vp_win(gs.pub);
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = turn,
                .end_reason = "vp_threshold",
            };
        }
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
            if (!gs.hands[to_index(side)].test(card_id)) {
                continue;
            }
            if (card_spec(static_cast<CardId>(card_id)).is_scoring) {
                return GameResult{
                    .winner = other_side(side),
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = "scoring_card_held",
                };
            }
        }
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
            if (gs.hands[to_index(side)].test(card_id)) {
                gs.pub.discard.set(card_id);
            }
        }
        gs.hands[to_index(side)].reset();
    }

    return std::nullopt;
}

}  // namespace

std::tuple<PublicState, bool, std::optional<Side>> apply_action_live(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    return apply_action_with_hands(gs, action, side, rng, policy_cb);
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_trap_ar_live(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    return resolve_trap_ar(gs, side, rng, policy_cb);
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_norad_live(
    GameState& gs,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    return resolve_norad(gs, rng, policy_cb);
}

std::optional<GameResult> run_extra_action_round_live(
    GameState& gs,
    Side side,
    const PolicyFn& policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    return run_extra_action_round(gs, side, policy, rng, trace_steps, config);
}

std::optional<GameResult> run_headline_phase_live(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    return run_headline_phase(gs, ussr_policy, us_policy, rng, trace_steps, config);
}

std::optional<GameResult> run_action_rounds_live(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    int total_ars,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    return run_action_rounds(gs, ussr_policy, us_policy, rng, total_ars, trace_steps, config);
}

// --- Setup influence placement phase (TS Deluxe §3.0) ---
// USSR places 6 in Eastern Europe, then US places 7 in Western Europe.
// Both players have seen their opening hands before placing.
void run_setup_phase(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    gs.phase = GamePhase::Setup;

    // Sample opening from human game corpus, weighted by historical frequency.
    for (const auto side : {Side::USSR, Side::US}) {
        gs.pub.phasing = side;
        const int side_idx = to_index(side);
        const auto valid_targets = [&]() -> std::vector<CountryId> {
            if (side == Side::USSR) {
                return {kSetupEasternBlocIds.begin(), kSetupEasternBlocIds.end()};
            } else {
                return {kSetupWesternEuropeIds.begin(), kSetupWesternEuropeIds.end()};
            }
        }();

        // Sample an opening weighted by human frequency.
        // All human games used +2 bid, so US openings are always 9-influence atomic units
        // (including Iran+1 bid placement). kHumanUSOpeningsBid2 is the only US table.
        const SetupOpening* opening;
        if (side == Side::USSR) {
            opening = choose_random_opening(kHumanUSSROpenings.data(),
                                            static_cast<int>(kHumanUSSROpenings.size()), rng);
        } else {
            opening = choose_random_opening(kHumanUSOpeningsBid2.data(),
                                            static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
        }

        std::vector<CountryId> heuristic_sequence;
        if (opening != nullptr) {
            for (int i = 0; i < opening->count; ++i) {
                for (int j = 0; j < opening->placements[i].amount; ++j) {
                    heuristic_sequence.push_back(opening->placements[i].country);
                }
            }
        }

        int heuristic_idx = 0;
        while (gs.setup_influence_remaining[side_idx] > 0) {
            const bool holds_china = (side == Side::USSR) ? gs.ussr_holds_china : gs.us_holds_china;
            const auto pub_snapshot = gs.pub;
            const auto hand_snapshot = gs.hands[side_idx];

            // Ask policy for placement (learned model will return meaningful targets)
            auto action_opt = (side == Side::USSR ? ussr_policy : us_policy)(
                gs.pub, gs.hands[side_idx], holds_china, rng
            );

            // Check if policy returned a valid setup target
            CountryId target = 0;
            bool valid_from_policy = false;
            if (action_opt.has_value() && !action_opt->targets.empty()) {
                const auto t = static_cast<CountryId>(action_opt->targets[0]);
                if (std::find(valid_targets.begin(), valid_targets.end(), t) != valid_targets.end()) {
                    target = t;
                    valid_from_policy = true;
                }
            }

            // Fallback: use heuristic plan
            if (!valid_from_policy) {
                if (heuristic_idx < static_cast<int>(heuristic_sequence.size())) {
                    target = heuristic_sequence[heuristic_idx++];
                } else {
                    target = valid_targets[rng.choice_index(valid_targets.size())];
                }
            }

            // Place 1 influence
            gs.pub.set_influence(side, target, gs.pub.influence_of(side, target) + 1);
            gs.setup_influence_remaining[side_idx] -= 1;

            // Record trace step for training data
            if (trace_steps) {
                ActionEncoding setup_action;
                setup_action.card_id = 0;  // no card during setup
                setup_action.mode = ActionMode::Influence;
                setup_action.targets = {target};
                trace_steps->push_back(StepTrace{
                    .turn = 0,
                    .ar = 0,
                    .side = side,
                    .holds_china = holds_china,
                    .pub_snapshot = pub_snapshot,
                    .hand_snapshot = hand_snapshot,
                    .action = setup_action,
                    .vp_before = gs.pub.vp,
                    .vp_after = gs.pub.vp,
                    .defcon_before = gs.pub.defcon,
                    .defcon_after = gs.pub.defcon,
                    .opp_hand_snapshot = {},
                    .deck_snapshot = {},
                    .ussr_holds_china_snapshot = false,
                    .us_holds_china_snapshot = false,
                });
            }
        }
    }

    // Transition to headline phase
    gs.phase = GamePhase::Headline;
}

TracedGame play_game_traced_from_state_ref_with_rng(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    const GameLoopConfig& config
) {
    TracedGame traced;

    // Apply competitive bid: US gets extra free influence in Western Europe.
    // Standard online TS bid is +2 for US.
    if (config.us_bid_extra > 0) {
        gs.setup_influence_remaining[to_index(Side::US)] += config.us_bid_extra;
    }

    // Run setup phase if game hasn't started yet (fresh game state)
    if (gs.phase == GamePhase::Setup && gs.setup_influence_remaining[0] > 0) {
        if (config.skip_setup_influence) {
            // Skip free placement, go directly to headline.
            gs.setup_influence_remaining = {0, 0};
            gs.phase = GamePhase::Headline;
        } else if (config.use_atomic_setup) {
            // Atomic setup: place from opening tables in one shot, no policy
            // callbacks.  Consumes exactly 2 RNG calls (one per side for
            // choose_random_opening), matching the batched path in
            // mcts_batched.cpp::run_setup_influence_heuristic.
            for (const auto side : {Side::USSR, Side::US}) {
                const SetupOpening* opening = (side == Side::USSR)
                    ? choose_random_opening(kHumanUSSROpenings.data(),
                                            static_cast<int>(kHumanUSSROpenings.size()), rng)
                    : choose_random_opening(kHumanUSOpeningsBid2.data(),
                                            static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
                if (opening == nullptr) continue;
                for (int i = 0; i < opening->count; ++i) {
                    const auto country = opening->placements[i].country;
                    const auto amount = opening->placements[i].amount;
                    gs.pub.set_influence(side, country,
                        gs.pub.influence_of(side, country) + amount);
                }
            }
            gs.setup_influence_remaining = {0, 0};
            gs.phase = GamePhase::Headline;
        } else {
            run_setup_phase(gs, ussr_policy, us_policy, rng, &traced.steps, config);
        }
    }

    for (int turn = 1; turn <= kMaxTurns; ++turn) {
        gs.pub.turn = turn;
        if (turn == kMidWarTurn) {
            advance_to_mid_war(gs, rng);
        } else if (turn == kLateWarTurn) {
            advance_to_late_war(gs, rng);
        }

        deal_cards(gs, Side::USSR, rng);
        deal_cards(gs, Side::US, rng);

        if (auto result = run_headline_phase(gs, ussr_policy, us_policy, rng, &traced.steps, config); result.has_value()) {
            traced.result = *result;
            return traced;
        }
        if (auto result = run_action_rounds(gs, ussr_policy, us_policy, rng, ars_for_turn(turn), &traced.steps, config); result.has_value()) {
            traced.result = *result;
            return traced;
        }
        if (gs.pub.north_sea_oil_extra_ar) {
            gs.pub.north_sea_oil_extra_ar = false;
            if (auto result = run_extra_action_round(gs, Side::US, us_policy, rng, &traced.steps, config); result.has_value()) {
                traced.result = *result;
                return traced;
            }
        }
        if (gs.pub.glasnost_extra_ar) {
            gs.pub.glasnost_extra_ar = false;
            if (auto result = run_extra_action_round(gs, Side::USSR, ussr_policy, rng, &traced.steps, config); result.has_value()) {
                traced.result = *result;
                return traced;
            }
        }
        if (auto result = end_of_turn(gs, turn); result.has_value()) {
            traced.result = *result;
            return traced;
        }
    }

    if (gs.pub.vp > 0) {
        traced.result = GameResult{.winner = Side::USSR, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
        return traced;
    }
    if (gs.pub.vp < 0) {
        traced.result = GameResult{.winner = Side::US, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
        return traced;
    }
    traced.result = GameResult{.winner = std::nullopt, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
    return traced;
}

TracedGame play_game_traced_from_state_with_rng(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    const GameLoopConfig& config
) {
    return play_game_traced_from_state_ref_with_rng(gs, ussr_policy, us_policy, rng, config);
}

GameResult play_game_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    return play_game_traced_fn(ussr_policy, us_policy, seed, config).result;
}

GameResult play_game_from_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    return play_game_traced_from_state_fn(std::move(gs), ussr_policy, us_policy, seed, config).result;
}

TracedGame play_game_traced_from_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    Pcg64Rng rng(seed.value_or(std::random_device{}()));
    return play_game_traced_from_state_with_rng(std::move(gs), ussr_policy, us_policy, rng, config);
}

GameResult play_game_from_mid_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    Pcg64Rng rng(seed.value_or(std::random_device{}()));
    const int start_turn = std::max(1, gs.pub.turn);

    // For the first turn we are continuing mid-turn: skip era advancement and
    // card dealing (the caller has already set up hands and deck).  For all
    // subsequent turns we run the normal turn sequence including dealing.
    for (int turn = start_turn; turn <= kMaxTurns; ++turn) {
        gs.pub.turn = turn;

        if (turn == start_turn) {
            // Continuing mid-game: skip era advancement and card dealing.
            // We run the headline phase and action rounds from whatever the
            // current phase is.  Simplest: always run headline then action
            // rounds; the caller should set gs.phase = Headline or ActionRound
            // appropriately.  If mid-action-round, we still re-run the full
            // round count; this is a slight over-estimate but acceptable for
            // rollouts.
        } else {
            // Normal turn setup.
            if (turn == kMidWarTurn) {
                advance_to_mid_war(gs, rng);
            } else if (turn == kLateWarTurn) {
                advance_to_late_war(gs, rng);
            }
            deal_cards(gs, Side::USSR, rng);
            deal_cards(gs, Side::US, rng);
        }

        if (auto result = run_headline_phase(gs, ussr_policy, us_policy, rng, nullptr, config); result.has_value()) {
            return *result;
        }
        if (auto result = run_action_rounds(gs, ussr_policy, us_policy, rng, ars_for_turn(turn), nullptr, config); result.has_value()) {
            return *result;
        }
        if (gs.pub.north_sea_oil_extra_ar) {
            gs.pub.north_sea_oil_extra_ar = false;
            if (auto result = run_extra_action_round(gs, Side::US, us_policy, rng, nullptr, config); result.has_value()) {
                return *result;
            }
        }
        if (gs.pub.glasnost_extra_ar) {
            gs.pub.glasnost_extra_ar = false;
            if (auto result = run_extra_action_round(gs, Side::USSR, ussr_policy, rng, nullptr, config); result.has_value()) {
                return *result;
            }
        }
        if (auto result = end_of_turn(gs, turn); result.has_value()) {
            return *result;
        }
    }

    if (gs.pub.vp > 0) {
        return GameResult{.winner = Side::USSR, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
    }
    if (gs.pub.vp < 0) {
        return GameResult{.winner = Side::US, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
    }
    return GameResult{.winner = std::nullopt, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
}

TracedGame play_game_traced_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    auto gs = reset_game(seed);
    Pcg64Rng runtime_rng(seed.value_or(std::random_device{}()));
    return play_game_traced_from_state_with_rng(std::move(gs), ussr_policy, us_policy, runtime_rng, config);
}

TracedGame play_game_traced_from_seed_words_fn(
    std::array<uint64_t, 4> words,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    auto gs = reset_game_from_seed_words(words);
    Pcg64Rng runtime_rng(seed.value_or(std::random_device{}()));
    return play_game_traced_from_state_with_rng(std::move(gs), ussr_policy, us_policy, runtime_rng, config);
}

GameResult play_game(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    const PolicyFn ussr_fn = [ussr_policy](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng) {
        return choose_action(ussr_policy, pub, hand, holds_china, rng);
    };
    const PolicyFn us_fn = [us_policy](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng) {
        return choose_action(us_policy, pub, hand, holds_china, rng);
    };
    return play_game_fn(ussr_fn, us_fn, seed, config);
}

GameResult play_random_game(std::optional<uint32_t> seed, const GameLoopConfig& config) {
    return play_game(PolicyKind::Random, PolicyKind::Random, seed, config);
}

std::vector<GameResult> play_matchup(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    int game_count,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    const PolicyFn ussr_fn = [ussr_policy](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng) {
        return choose_action(ussr_policy, pub, hand, holds_china, rng);
    };
    const PolicyFn us_fn = [us_policy](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng) {
        return choose_action(us_policy, pub, hand, holds_china, rng);
    };
    return play_matchup_fn(ussr_fn, us_fn, game_count, seed, config);
}

std::vector<GameResult> play_matchup_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    int game_count,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(std::max(0, game_count)));
    const auto base_seed = seed.value_or(std::random_device{}());
    for (int game_index = 0; game_index < game_count; ++game_index) {
        results.push_back(play_game_fn(ussr_policy, us_policy, base_seed + static_cast<uint32_t>(game_index), config));
    }
    return results;
}

MatchSummary summarize_results(std::span<const GameResult> results) {
    MatchSummary summary;
    summary.games = static_cast<int>(results.size());
    long long total_turns = 0;
    long long total_vp = 0;

    for (const auto& result : results) {
        total_turns += result.end_turn;
        total_vp += result.final_vp;

        if (!result.winner.has_value()) {
            ++summary.draws;
        } else if (*result.winner == Side::USSR) {
            ++summary.ussr_wins;
        } else if (*result.winner == Side::US) {
            ++summary.us_wins;
        }

        if (result.end_reason == "defcon1") {
            ++summary.defcon1;
        } else if (result.end_reason == "turn_limit") {
            ++summary.turn_limit;
        } else if (result.end_reason == "scoring_card_held") {
            ++summary.scoring_card_held;
        } else if (result.end_reason == "vp_threshold" || result.end_reason == "vp") {
            ++summary.vp_threshold;
        }
    }

    if (!results.empty()) {
        summary.avg_turn = static_cast<double>(total_turns) / static_cast<double>(results.size());
        summary.avg_final_vp = static_cast<double>(total_vp) / static_cast<double>(results.size());
    }
    return summary;
}

}  // namespace ts
