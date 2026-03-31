#include "game_loop.hpp"

#include <algorithm>

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
constexpr CountryId kWestGermanyId = 18;
constexpr std::array<CardId, 17> kCatCCardIds = {5, 10, 26, 32, 36, 45, 46, 47, 52, 68, 78, 84, 88, 95, 98, 101, 108};

struct PendingHeadline {
    Side side = Side::USSR;
    bool holds_china = false;
    CardSet hand_snapshot;
    ActionEncoding action;
};

void sync_china(GameState& gs) {
    gs.ussr_holds_china = gs.pub.china_held_by == Side::USSR;
    gs.us_holds_china = gs.pub.china_held_by == Side::US;
}

bool is_cat_c_card(CardId card_id) {
    return std::find(kCatCCardIds.begin(), kCatCCardIds.end(), card_id) != kCatCCardIds.end();
}

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
    std::mt19937& rng
);

std::optional<CardId> draw_one(GameState& gs, std::mt19937& rng) {
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
        std::shuffle(reshuffled.begin(), reshuffled.end(), rng);
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

void apply_ops_randomly(PublicState& pub, Side side, int ops, std::mt19937& rng) {
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
    const auto mode = modes[std::uniform_int_distribution<size_t>(0, modes.size() - 1)(rng)];
    const auto opponent = other_side(side);

    if (mode == ActionMode::Influence) {
        for (int i = 0; i < ops; ++i) {
            const auto target = accessible[std::uniform_int_distribution<size_t>(0, accessible.size() - 1)(rng)];
            pub.set_influence(side, target, pub.influence_of(side, target) + 1);
        }
        return;
    }

    if (mode == ActionMode::Coup) {
        auto targets = accessible;
        if (pub.defcon <= 2) {
            targets.erase(
                std::remove_if(
                    targets.begin(),
                    targets.end(),
                    [](CountryId cid) { return country_spec(cid).is_battleground; }
                ),
                targets.end()
            );
            if (targets.empty()) {
                targets = accessible;
            }
        }
        const auto target = targets[std::uniform_int_distribution<size_t>(0, targets.size() - 1)(rng)];
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
        const auto target = accessible[std::uniform_int_distribution<size_t>(0, accessible.size() - 1)(rng)];
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
    std::mt19937& rng
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

    const auto chosen = eligible[std::uniform_int_distribution<size_t>(0, eligible.size() - 1)(rng)];
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
    std::mt19937& rng
) {
    auto pub = gs.pub;

    switch (card_id) {
        case 5: {
            auto hand = hand_to_vector(gs.hands[to_index(Side::USSR)]);
            if (!hand.empty()) {
                const auto target = hand[std::uniform_int_distribution<size_t>(0, hand.size() - 1)(rng)];
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
                    auto [event_pub, over, winner] = fire_event_with_state(gs, target, Side::US, rng);
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
                discard_from_hand(gs, Side::US, eligible[std::uniform_int_distribution<size_t>(0, eligible.size() - 1)(rng)], pub);
            } else {
                pub.set_influence(Side::US, kWestGermanyId, 0);
            }
            break;
        }

        case 26: {
            const auto accessible = accessible_countries(Side::US, pub, ActionMode::Influence);
            if (!accessible.empty()) {
                const auto target = accessible[std::uniform_int_distribution<size_t>(0, accessible.size() - 1)(rng)];
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
                const auto chosen = eligible[std::uniform_int_distribution<size_t>(0, eligible.size() - 1)(rng)];
                const auto ops = effective_ops(chosen, pub, side);
                discard_from_hand(gs, side, chosen, pub);
                apply_ops_randomly(pub, side, ops, rng);
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
                    const auto target = pool[std::uniform_int_distribution<size_t>(0, pool.size() - 1)(rng)];
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
                const auto chosen = discarded[std::uniform_int_distribution<size_t>(0, discarded.size() - 1)(rng)];
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
                const auto chosen = candidates[std::uniform_int_distribution<size_t>(0, candidates.size() - 1)(rng)];
                gs.hands[to_index(opponent)].reset(chosen);
                apply_ops_randomly(pub, side, effective_ops(chosen, pub, side), rng);
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
            std::shuffle(candidates.begin(), candidates.end(), rng);
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
                const auto chosen = candidates[std::uniform_int_distribution<size_t>(0, candidates.size() - 1)(rng)];
                gs.hands[to_index(Side::USSR)].reset(chosen);
                apply_ops_randomly(pub, Side::US, effective_ops(chosen, pub, Side::US), rng);
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
            const auto discard_count = discardable.empty() ? 0 : std::uniform_int_distribution<int>(0, static_cast<int>(discardable.size()))(rng);
            std::shuffle(discardable.begin(), discardable.end(), rng);
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
                    const auto keep_count = std::uniform_int_distribution<int>(0, static_cast<int>(drawn.size()))(rng);
                    std::shuffle(drawn.begin(), drawn.end(), rng);
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
                    const auto chosen = discarded[std::uniform_int_distribution<size_t>(0, discarded.size() - 1)(rng)];
                    pub.discard.reset(chosen);
                    gs.pub = pub;
                    auto [event_pub, over, winner] = fire_event_with_state(gs, chosen, side, rng);
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
                const auto chosen = candidates[std::uniform_int_distribution<size_t>(0, candidates.size() - 1)(rng)];
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
    std::mt19937& rng
) {
    if (is_cat_c_card(card_id)) {
        return apply_hand_event(gs, card_id, event_side, rng);
    }
    ActionEncoding action{
        .card_id = card_id,
        .mode = ActionMode::Event,
        .targets = {},
    };
    auto [new_pub, over, winner] = apply_action(gs.pub, action, event_side, rng);
    gs.pub = new_pub;
    return {new_pub, over, winner};
}

std::tuple<PublicState, bool, std::optional<Side>> apply_action_with_hands(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    std::mt19937& rng
) {
    if (action.mode != ActionMode::Event) {
        const auto owner = card_spec(action.card_id).side;
        if (owner == other_side(side)) {
            auto [new_pub, over, winner] = fire_event_with_state(gs, action.card_id, owner, rng);
            if (over) {
                return {new_pub, true, winner};
            }
        }
    }

    if (action.mode == ActionMode::Event && is_cat_c_card(action.card_id)) {
        return apply_hand_event(gs, action.card_id, side, rng);
    }

    auto [new_pub, over, winner] = apply_action(gs.pub, action, side, rng);
    gs.pub = new_pub;
    return {new_pub, over, winner};
}

std::string end_reason(const PublicState& pub, std::optional<Side> winner) {
    if (pub.defcon <= 1) {
        return "defcon1";
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
    std::mt19937& rng,
    std::vector<StepTrace>* trace_steps
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
        auto action = (side == Side::USSR ? ussr_policy : us_policy)(
            headline_pub,
            gs.hands[to_index(side)],
            holds_china,
            rng
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
        return lhs.side == Side::US;
    });

    for (const auto& pending : ordered) {
        const auto side = pending.side;
        const auto& action = pending.action;
        const auto pub_snapshot = gs.pub;
        const auto vp_before = gs.pub.vp;
        const auto defcon_before = gs.pub.defcon;
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
    }

    return std::nullopt;
}

std::optional<GameResult> run_action_rounds(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::mt19937& rng,
    int total_ars,
    std::vector<StepTrace>* trace_steps
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
            auto action = (side == Side::USSR ? ussr_policy : us_policy)(
                gs.pub,
                hand,
                holds_china,
                rng
            );
            if (!action.has_value()) {
                continue;
            }
            const auto pub_snapshot = gs.pub;
            const auto hand_snapshot = hand;
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
    std::mt19937& rng
) {
    return apply_action_with_hands(gs, action, side, rng);
}

GameResult play_game_fn(const PolicyFn& ussr_policy, const PolicyFn& us_policy, std::optional<uint32_t> seed) {
    return play_game_traced_fn(ussr_policy, us_policy, seed).result;
}

TracedGame play_game_traced_fn(const PolicyFn& ussr_policy, const PolicyFn& us_policy, std::optional<uint32_t> seed) {
    std::mt19937 rng(seed.value_or(std::random_device{}()));
    auto gs = reset_game(static_cast<uint32_t>(rng()));
    TracedGame traced;

    for (int turn = 1; turn <= kMaxTurns; ++turn) {
        gs.pub.turn = turn;
        if (turn == kMidWarTurn) {
            advance_to_mid_war(gs, rng);
        } else if (turn == kLateWarTurn) {
            advance_to_late_war(gs, rng);
        }

        deal_cards(gs, Side::USSR, rng);
        deal_cards(gs, Side::US, rng);

        if (auto result = run_headline_phase(gs, ussr_policy, us_policy, rng, &traced.steps); result.has_value()) {
            traced.result = *result;
            return traced;
        }
        if (auto result = run_action_rounds(gs, ussr_policy, us_policy, rng, ars_for_turn(turn), &traced.steps); result.has_value()) {
            traced.result = *result;
            return traced;
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

GameResult play_game(PolicyKind ussr_policy, PolicyKind us_policy, std::optional<uint32_t> seed) {
    const PolicyFn ussr_fn = [ussr_policy](const PublicState& pub, const CardSet& hand, bool holds_china, std::mt19937& rng) {
        return choose_action(ussr_policy, pub, hand, holds_china, rng);
    };
    const PolicyFn us_fn = [us_policy](const PublicState& pub, const CardSet& hand, bool holds_china, std::mt19937& rng) {
        return choose_action(us_policy, pub, hand, holds_china, rng);
    };
    return play_game_fn(ussr_fn, us_fn, seed);
}

GameResult play_random_game(std::optional<uint32_t> seed) {
    return play_game(PolicyKind::Random, PolicyKind::Random, seed);
}

std::vector<GameResult> play_matchup(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    int game_count,
    std::optional<uint32_t> seed
) {
    const PolicyFn ussr_fn = [ussr_policy](const PublicState& pub, const CardSet& hand, bool holds_china, std::mt19937& rng) {
        return choose_action(ussr_policy, pub, hand, holds_china, rng);
    };
    const PolicyFn us_fn = [us_policy](const PublicState& pub, const CardSet& hand, bool holds_china, std::mt19937& rng) {
        return choose_action(us_policy, pub, hand, holds_china, rng);
    };
    return play_matchup_fn(ussr_fn, us_fn, game_count, seed);
}

std::vector<GameResult> play_matchup_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    int game_count,
    std::optional<uint32_t> seed
) {
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(std::max(0, game_count)));
    const auto base_seed = seed.value_or(std::random_device{}());
    for (int game_index = 0; game_index < game_count; ++game_index) {
        results.push_back(play_game_fn(ussr_policy, us_policy, base_seed + static_cast<uint32_t>(game_index)));
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
