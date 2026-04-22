// Hand-aware live-engine helpers layered above the public-state step engine.

#include "hand_ops.hpp"

#include <algorithm>
#include <array>
#include <span>
#include <vector>

#include "dice.hpp"
#include "game_data.hpp"
#include "game_loop.hpp"
#include "rule_queries.hpp"
#include "step.hpp"

namespace ts {
namespace {

constexpr CountryId kWestGermanyId = 18;
constexpr std::array<CardId, 17> kCatCCardIds = {5, 10, 26, 32, 36, 45, 46, 47, 52, 68, 78, 84, 88, 95, 98, 101, 108};

bool is_cat_c_card(CardId card_id) {
    return std::find(kCatCCardIds.begin(), kCatCCardIds.end(), card_id) != kCatCCardIds.end();
}

void card_played(PublicState& pub, CardId card_id, Side side) {
    if (pub.removed.test(card_id)) {
        return;
    }
    if (card_id == kChinaCardId) {
        pub.china_held_by = other_side(side);
        pub.china_playable = false;
        return;
    }
    const auto& spec = card_spec(card_id);
    if (spec.starred) {
        pub.discard.reset(card_id);
        pub.removed.set(card_id);
    } else {
        pub.discard.set(card_id);
    }
}

void discard_without_event(PublicState& pub, CardId card_id, Side side) {
    if (pub.removed.test(card_id)) {
        return;
    }
    if (card_id == kChinaCardId) {
        pub.china_held_by = other_side(side);
        pub.china_playable = false;
        return;
    }
    pub.discard.set(card_id);
}

void discard_from_hand(GameState& gs, Side side, CardId card_id, PublicState& pub) {
    gs.hands[to_index(side)].reset(card_id);
    if (card_id == kChinaCardId) {
        card_played(pub, card_id, side);
        gs.ussr_holds_china = pub.china_held_by == Side::USSR;
        gs.us_holds_china = pub.china_held_by == Side::US;
        return;
    }
    const auto& spec = card_spec(card_id);
    if (spec.starred) {
        pub.removed.set(card_id);
    } else {
        pub.discard.set(card_id);
    }
}

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

std::tuple<PublicState, bool, std::optional<Side>> apply_hand_event(
    GameState& gs,
    CardId card_id,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log
);

std::tuple<PublicState, bool, std::optional<Side>> fire_event_with_state(
    GameState& gs,
    CardId card_id,
    Side event_side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log
) {
    if (is_cat_c_card(card_id)) {
        return apply_hand_event(gs, card_id, event_side, rng, policy_cb, frame_log);
    }
    ActionEncoding action{
        .card_id = card_id,
        .mode = ActionMode::Event,
        .targets = {},
    };
    auto [new_pub, over, winner] = apply_action(
        gs.pub,
        action,
        event_side,
        rng,
        policy_cb,
        frame_log,
        gs.frame_stack_mode
    );
    gs.pub = new_pub;
    if (over && card_spec(card_id).is_scoring) {
        gs.scoring_auto_win = true;
    }
    return {new_pub, over, winner};
}

uint8_t frame_count(size_t value) {
    return static_cast<uint8_t>(std::min<size_t>(value, 255));
}

void push_option_frame(
    std::vector<DecisionFrame>* frame_log,
    FrameKind kind,
    CardId source_card,
    Side acting_side,
    int n_options,
    int step_index,
    int total_steps
) {
    if (frame_log == nullptr || n_options <= 0) {
        return;
    }
    DecisionFrame frame;
    frame.kind = kind;
    frame.source_card = source_card;
    frame.acting_side = acting_side;
    frame.step_index = frame_count(static_cast<size_t>(std::max(0, step_index)));
    frame.total_steps = frame_count(static_cast<size_t>(std::max(1, total_steps)));
    frame.stack_depth = frame_count(frame_log->size());
    frame.eligible_n = frame_count(static_cast<size_t>(n_options));
    frame_log->push_back(frame);
}

void push_card_frame(
    std::vector<DecisionFrame>* frame_log,
    FrameKind kind,
    CardId source_card,
    Side acting_side,
    std::span<const CardId> eligible_cards,
    int step_index,
    int total_steps
) {
    if (frame_log == nullptr || eligible_cards.empty()) {
        return;
    }
    DecisionFrame frame;
    frame.kind = kind;
    frame.source_card = source_card;
    frame.acting_side = acting_side;
    frame.step_index = frame_count(static_cast<size_t>(std::max(0, step_index)));
    frame.total_steps = frame_count(static_cast<size_t>(std::max(1, total_steps)));
    frame.stack_depth = frame_count(frame_log->size());
    for (const auto card_id : eligible_cards) {
        frame.eligible_cards.set(card_id);
    }
    frame.eligible_n = frame_count(eligible_cards.size());
    frame_log->push_back(frame);
}

void annotate_latest_frame(
    std::vector<DecisionFrame>* frame_log,
    int step_index,
    int total_steps,
    uint16_t criteria_bits = 0
) {
    if (frame_log == nullptr || frame_log->empty()) {
        return;
    }
    auto& frame = frame_log->back();
    frame.step_index = frame_count(static_cast<size_t>(std::max(0, step_index)));
    frame.total_steps = frame_count(static_cast<size_t>(std::max(1, total_steps)));
    frame.criteria_bits = criteria_bits;
}

void set_latest_frame_eligible_cards(
    std::vector<DecisionFrame>* frame_log,
    std::span<const CardId> eligible_cards
) {
    if (frame_log == nullptr || frame_log->empty()) {
        return;
    }
    auto& frame = frame_log->back();
    frame.eligible_cards.reset();
    for (const auto card_id : eligible_cards) {
        frame.eligible_cards.set(card_id);
    }
}

void set_latest_frame_budget(std::vector<DecisionFrame>* frame_log, int budget) {
    if (frame_log == nullptr || frame_log->empty()) {
        return;
    }
    frame_log->back().budget_remaining = static_cast<int16_t>(budget);
}

std::vector<CountryId> frame_eligible_countries(const DecisionFrame& frame) {
    std::vector<CountryId> countries;
    countries.reserve(frame.eligible_countries.count());
    for (int raw = 0; raw < static_cast<int>(frame.eligible_countries.size()); ++raw) {
        if (frame.eligible_countries.test(static_cast<size_t>(raw))) {
            countries.push_back(static_cast<CountryId>(raw));
        }
    }
    return countries;
}

int choose_frame_option(
    const PublicState& pub,
    const DecisionFrame& frame,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    const auto n_options = static_cast<int>(frame.eligible_n);
    if (n_options <= 1) {
        return 0;
    }
    if (policy_cb == nullptr) {
        return static_cast<int>(rng.choice_index(static_cast<size_t>(n_options)));
    }

    EventDecision decision;
    decision.source_card = frame.source_card;
    decision.kind = DecisionKind::SmallChoice;
    decision.n_options = n_options;
    decision.acting_side = frame.acting_side;
    return std::clamp((*policy_cb)(pub, decision), 0, n_options - 1);
}

CountryId choose_frame_country(
    const PublicState& pub,
    const DecisionFrame& frame,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    const auto countries = frame_eligible_countries(frame);
    if (countries.empty()) {
        return kInvalidCountryId;
    }
    if (countries.size() == 1) {
        return countries.front();
    }
    if (policy_cb == nullptr) {
        return countries[rng.choice_index(countries.size())];
    }

    EventDecision decision;
    decision.source_card = frame.source_card;
    decision.kind = DecisionKind::CountrySelect;
    decision.n_options = static_cast<int>(countries.size());
    decision.acting_side = frame.acting_side;
    for (int idx = 0; idx < decision.n_options; ++idx) {
        decision.eligible_ids[idx] = static_cast<int>(countries[static_cast<size_t>(idx)]);
    }
    const auto choice = std::clamp((*policy_cb)(pub, decision), 0, decision.n_options - 1);
    return countries[static_cast<size_t>(choice)];
}

FrameAction choose_frame_action(
    const PublicState& pub,
    const DecisionFrame& frame,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    switch (frame.kind) {
        case FrameKind::SmallChoice:
            return FrameAction{.option_index = choose_frame_option(pub, frame, rng, policy_cb)};
        case FrameKind::CountryPick:
            return FrameAction{.country_id = choose_frame_country(pub, frame, rng, policy_cb)};
        default:
            return FrameAction{};
    }
}

bool apply_frame_ops_or_resolve(
    GameState& gs,
    std::vector<DecisionFrame>* frame_log,
    CardId card_id,
    Side side,
    int ops,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    if (gs.frame_stack_mode && policy_cb == nullptr) {
        return apply_frame_ops_impl(gs, frame_log, card_id, side, ops, rng);
    }

    const auto stack_base = gs.frame_stack.size();
    if (!apply_frame_ops_impl(gs, &gs.frame_stack, card_id, side, ops, rng)) {
        return false;
    }

    int subframe_steps = 0;
    while (gs.frame_stack.size() > stack_base && subframe_steps < 512) {
        const auto frame = gs.frame_stack.back();
        const auto action = choose_frame_action(gs.pub, frame, rng, policy_cb);
        if (frame_log != nullptr && frame_log != &gs.frame_stack) {
            frame_log->push_back(logged_frame_copy(frame, frame_log, action));
        }
        const auto result = engine_step_subframe(gs, action, rng);
        (void)result;
        ++subframe_steps;
    }

    return true;
}

std::vector<ActionMode> deferred_ops_modes(std::span<const ActionEncoding> ops_actions) {
    std::vector<ActionMode> modes;
    for (const auto& action : ops_actions) {
        if (std::find(modes.begin(), modes.end(), action.mode) == modes.end()) {
            modes.push_back(action.mode);
        }
    }
    std::sort(modes.begin(), modes.end(), [](ActionMode lhs, ActionMode rhs) {
        return static_cast<int>(lhs) < static_cast<int>(rhs);
    });
    return modes;
}

std::vector<CardId> cmc_cancel_cards(const GameState& gs, Side side) {
    std::vector<CardId> eligible;
    if (gs.pub.china_held_by == side) {
        eligible.push_back(kChinaCardId);
    }
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        const auto candidate = static_cast<CardId>(raw);
        if (
            gs.hands[to_index(side)].test(candidate) &&
            candidate != kChinaCardId &&
            !card_spec(candidate).is_scoring &&
            card_spec(candidate).ops >= 3
        ) {
            eligible.push_back(candidate);
        }
    }
    return eligible;
}

std::vector<CardId> debt_crisis_discard_cards(const GameState& gs) {
    std::vector<CardId> eligible;
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        const auto candidate = static_cast<CardId>(raw);
        if (
            gs.hands[to_index(Side::US)].test(candidate) &&
            candidate != kChinaCardId &&
            !card_spec(candidate).is_scoring &&
            card_spec(candidate).ops >= 3
        ) {
            eligible.push_back(candidate);
        }
    }
    return eligible;
}

void double_ussr_latin_america_influence(PublicState& pub) {
    for (const auto cid : all_country_ids()) {
        const auto region = country_spec(cid).region;
        if (region != Region::CentralAmerica && region != Region::SouthAmerica) {
            continue;
        }
        const auto influence = pub.influence_of(Side::USSR, cid);
        if (influence > 0) {
            pub.set_influence(Side::USSR, cid, influence * 2);
        }
    }
}

std::tuple<PublicState, bool, std::optional<Side>> apply_hand_event(
    GameState& gs,
    CardId card_id,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log
) {
    auto pub = gs.pub;

    switch (card_id) {
        case 5: {
            auto hand = hand_to_vector(gs.hands[to_index(Side::USSR)]);
            if (!hand.empty()) {
                const auto target = choose_card(pub, 5, Side::USSR, hand, rng, policy_cb, frame_log, gs.frame_stack_mode);
                if (target == 0) {
                    return {pub, false, std::nullopt};
                }
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
                        gs.scoring_auto_win = true;
                        return {pub, true, result.winner};
                    }
                } else if (card_spec(target).side == Side::US) {
                    auto [event_pub, over, winner] = fire_event_with_state(gs, target, Side::US, rng, policy_cb, frame_log);
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
                const auto chosen = choose_card(pub, 10, Side::US, eligible, rng, policy_cb, frame_log, gs.frame_stack_mode);
                if (chosen == 0) {
                    return {pub, false, std::nullopt};
                }
                discard_from_hand(gs, Side::US, chosen, pub);
            } else {
                pub.set_influence(Side::US, kWestGermanyId, 0);
            }
            break;
        }

        case 26: {
            const auto accessible = accessible_countries(Side::US, pub, ActionMode::Influence);
            if (!accessible.empty()) {
                const auto target = choose_country(pub, 26, Side::US, accessible, rng, policy_cb, frame_log, gs.frame_stack_mode);
                if (target == kInvalidCountryId && gs.frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    return {pub, false, std::nullopt};
                }
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
                const auto chosen = choose_card(pub, 32, side, eligible, rng, policy_cb, frame_log, gs.frame_stack_mode);
                if (chosen == 0) {
                    return {pub, false, std::nullopt};
                }
                if (side == Side::US) {
                    pub.we_will_bury_you_pending = false;
                    pub.we_will_bury_you_turn_ar = -1;
                }
                const auto ops = effective_ops(chosen, pub, side);
                discard_from_hand(gs, side, chosen, pub);
                gs.pub = pub;
                if (apply_frame_ops_or_resolve(gs, frame_log, static_cast<CardId>(32), side, ops, rng, policy_cb)) {
                    return {gs.pub, gs.game_over, gs.winner};
                }
            } else if (side == Side::US) {
                pub.we_will_bury_you_pending = false;
                pub.we_will_bury_you_turn_ar = -1;
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
            const int total_steps_36 = static_cast<int>(regions.size());
            for (int i = 0; i < total_steps_36; ++i) {
                std::vector<CountryId> pool;
                for (const auto cid : all_country_ids()) {
                    if (cid != 64 && cid != kUsaAnchorId && cid != kUssrAnchorId &&
                        country_spec(cid).region == regions[static_cast<size_t>(i)]) {
                        pool.push_back(cid);
                    }
                }
                if (!pool.empty()) {
                    const auto target = choose_country(pub, 36, Side::USSR, pool, rng, policy_cb, frame_log, gs.frame_stack_mode);
                    if (target == kInvalidCountryId) {
                        if (frame_log != nullptr && !frame_log->empty()) {
                            frame_log->back().step_index = static_cast<uint8_t>(std::min(i, 255));
                            frame_log->back().total_steps = static_cast<uint8_t>(std::max(1, std::min(total_steps_36, 255)));
                        }
                        return {pub, false, std::nullopt};
                    }
                    pub.set_influence(Side::USSR, target, pub.influence_of(Side::USSR, target) + 1);
                }
            }
            break;
        }

        case 45:
            pub.quagmire_active = true;
            break;

        case 46: {
            pub.defcon = std::min(5, pub.defcon + 2);
            pub.salt_active = true;
            auto discarded = hand_to_vector(pub.discard);
            if (!discarded.empty()) {
                const auto chosen = choose_card(pub, 46, side, discarded, rng, policy_cb, frame_log, gs.frame_stack_mode);
                if (chosen == 0) {
                    return {pub, false, std::nullopt};
                }
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
                const auto chosen = choose_card(pub, 52, side, candidates, rng, policy_cb, frame_log, gs.frame_stack_mode);
                if (chosen == 0) {
                    return {pub, false, std::nullopt};
                }
                gs.hands[to_index(opponent)].reset(chosen);
                gs.pub = pub;
                if (apply_frame_ops_or_resolve(
                    gs,
                    frame_log,
                    static_cast<CardId>(52),
                    side,
                    effective_ops(chosen, pub, side),
                    rng,
                    policy_cb
                )) {
                    gs.hands[to_index(opponent)].set(chosen);
                    return {gs.pub, gs.game_over, gs.winner};
                }
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
            const auto selections = std::min(discard_count, static_cast<int>(candidates.size()));
            for (int i = 0; i < selections; ++i) {
                if (candidates.empty()) {
                    break;
                }
                const auto chosen_index = rng.choice_index(candidates.size());
                const auto chosen = candidates[chosen_index];
                discard_from_hand(gs, opponent, chosen, pub);
                candidates.erase(candidates.begin() + static_cast<std::vector<CardId>::difference_type>(chosen_index));
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
                const auto chosen =
                    choose_card(pub, 68, Side::US, candidates, rng, policy_cb, frame_log, gs.frame_stack_mode);
                if (chosen == 0) {
                    return {pub, false, std::nullopt};
                }
                gs.hands[to_index(Side::USSR)].reset(chosen);
                gs.pub = pub;
                if (apply_frame_ops_or_resolve(
                    gs,
                    frame_log,
                    static_cast<CardId>(68),
                    Side::US,
                    effective_ops(chosen, pub, Side::US),
                    rng,
                    policy_cb
                )) {
                    gs.hands[to_index(Side::USSR)].set(chosen);
                    return {gs.pub, gs.game_over, gs.winner};
                }
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
            if (discardable.size() > 4) {
                discardable.resize(4);
            }
            const auto discard_count = choose_option(
                pub,
                static_cast<CardId>(78),
                Side::US,
                static_cast<int>(discardable.size()) + 1,
                rng,
                policy_cb,
                frame_log,
                gs.frame_stack_mode
            );
            if (discard_count < 0) {
                return {pub, false, std::nullopt};
            }
            annotate_latest_frame(
                frame_log,
                0,
                discard_count + 1,
                static_cast<uint16_t>(discard_count)
            );
            std::vector<CardId> chosen_discards;
            chosen_discards.reserve(static_cast<size_t>(discard_count));
            for (int i = 0; i < discard_count; ++i) {
                const auto chosen = choose_card(pub, 78, Side::US, discardable, rng, policy_cb, frame_log, gs.frame_stack_mode);
                if (chosen == 0) {
                    annotate_latest_frame(
                        frame_log,
                        i + 1,
                        discard_count + 1,
                        static_cast<uint16_t>(discard_count)
                    );
                    return {pub, false, std::nullopt};
                }
                annotate_latest_frame(
                    frame_log,
                    i + 1,
                    discard_count + 1,
                    static_cast<uint16_t>(discard_count)
                );
                chosen_discards.push_back(chosen);
                discardable.erase(std::remove(discardable.begin(), discardable.end(), chosen), discardable.end());
            }
            for (const auto chosen : chosen_discards) {
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
                    pub = gs.pub;
                    const auto keep_count = choose_option(
                        pub,
                        static_cast<CardId>(84),
                        Side::US,
                        static_cast<int>(drawn.size()) + 1,
                        rng,
                        policy_cb,
                        frame_log,
                        gs.frame_stack_mode
                    );
                    set_latest_frame_eligible_cards(frame_log, drawn);
                    if (keep_count < 0) {
                        return {pub, false, std::nullopt};
                    }
                    annotate_latest_frame(
                        frame_log,
                        0,
                        keep_count + 1,
                        static_cast<uint16_t>(keep_count)
                    );
                    std::vector<CardId> kept_cards;
                    kept_cards.reserve(static_cast<size_t>(keep_count));
                    for (int i = 0; i < keep_count; ++i) {
                        const auto kept_card =
                            choose_card(pub, 84, Side::US, drawn, rng, policy_cb, frame_log, gs.frame_stack_mode);
                        if (kept_card == 0) {
                            annotate_latest_frame(
                                frame_log,
                                i + 1,
                                keep_count + 1,
                                static_cast<uint16_t>(keep_count)
                            );
                            return {pub, false, std::nullopt};
                        }
                        annotate_latest_frame(
                            frame_log,
                            i + 1,
                            keep_count + 1,
                            static_cast<uint16_t>(keep_count)
                        );
                        kept_cards.push_back(kept_card);
                        drawn.erase(std::remove(drawn.begin(), drawn.end(), kept_card), drawn.end());
                    }
                    for (const auto kept_card : kept_cards) {
                        gs.hands[to_index(Side::US)].set(kept_card);
                    }
                    for (const auto discarded_card : drawn) {
                        if (card_spec(discarded_card).starred) {
                            pub.removed.set(discarded_card);
                        } else {
                            pub.discard.set(discarded_card);
                        }
                    }
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
                    const auto chosen =
                        choose_card(pub, 88, side, discarded, rng, policy_cb, frame_log, gs.frame_stack_mode);
                    if (chosen == 0) {
                        return {pub, false, std::nullopt};
                    }
                    pub.discard.reset(chosen);
                    gs.pub = pub;
                    auto [event_pub, over, winner] = fire_event_with_state(gs, chosen, side, rng, policy_cb, frame_log);
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
            const auto eligible = debt_crisis_discard_cards(gs);
            if (!eligible.empty()) {
                if (gs.frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    push_option_frame(frame_log, FrameKind::SmallChoice, 98, Side::US, 2, 0, 2);
                    return {pub, false, std::nullopt};
                }

                bool discard_card = true;
                if (policy_cb != nullptr) {
                    discard_card = choose_option(pub, 98, Side::US, 2, rng, policy_cb, frame_log, gs.frame_stack_mode) == 0;
                }
                if (discard_card) {
                    const auto chosen = choose_card(pub, 98, Side::US, eligible, rng, policy_cb, frame_log, gs.frame_stack_mode);
                    if (chosen == 0) {
                        return {pub, false, std::nullopt};
                    }
                    discard_from_hand(gs, Side::US, chosen, pub);
                    break;
                }
            }
            double_ussr_latin_america_influence(pub);
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
                const auto chosen =
                    choose_card(pub, 101, Side::US, candidates, rng, policy_cb, frame_log, gs.frame_stack_mode);
                if (chosen == 0) {
                    return {pub, false, std::nullopt};
                }
                discard_from_hand(gs, Side::US, chosen, pub);
            }
            break;
        }

        case 108:
            if (side == Side::USSR) {
                pub.vp -= 1;
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

std::tuple<PublicState, bool, std::optional<Side>> execute_deferred_ops(
    GameState& gs,
    CardId card_id,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::span<const CountryId> preferred_targets,
    std::vector<DecisionFrame>* frame_log
) {
    CardSet hand;
    hand.set(static_cast<int>(card_id));
    const auto all_actions = enumerate_actions(hand, gs.pub, side, false);

    std::vector<ActionEncoding> ops_actions;
    for (const auto& action : all_actions) {
        if (
            action.card_id == card_id &&
            action.mode != ActionMode::EventFirst &&
            action.mode != ActionMode::Event &&
            action.mode != ActionMode::Space
        ) {
            ops_actions.push_back(action);
        }
    }
    if (ops_actions.empty()) {
        return {gs.pub, false, std::nullopt};
    }

    if (gs.frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
        const auto modes = deferred_ops_modes(ops_actions);
        push_option_frame(
            frame_log,
            FrameKind::DeferredOps,
            card_id,
            side,
            static_cast<int>(modes.size()),
            0,
            1
        );
        set_latest_frame_budget(frame_log, effective_ops(card_id, gs.pub, side));
        return {gs.pub, false, std::nullopt};
    }

    const auto score_match = [](std::span<const CountryId> candidate_targets, std::span<const CountryId> targets) {
        std::array<int, kCountrySlots> candidate_counts = {};
        std::array<int, kCountrySlots> target_counts = {};
        for (const auto cid : candidate_targets) {
            ++candidate_counts[static_cast<size_t>(cid)];
        }
        for (const auto cid : targets) {
            ++target_counts[static_cast<size_t>(cid)];
        }

        int overlap = 0;
        bool exact_multiset = candidate_targets.size() == targets.size();
        for (size_t idx = 0; idx < candidate_counts.size(); ++idx) {
            overlap += std::min(candidate_counts[idx], target_counts[idx]);
            if (candidate_counts[idx] != target_counts[idx]) {
                exact_multiset = false;
            }
        }

        return std::tuple{
            exact_multiset,
            overlap,
            candidate_targets.size() == targets.size(),
            !candidate_targets.empty() && !targets.empty() && candidate_targets.front() == targets.front()
        };
    };

    int idx = 0;
    if (ops_actions.size() > 1 && !preferred_targets.empty()) {
        size_t best_idx = 0;
        auto best_score = score_match(ops_actions.front().targets, preferred_targets);
        for (size_t candidate_idx = 1; candidate_idx < ops_actions.size(); ++candidate_idx) {
            const auto candidate_score = score_match(ops_actions[candidate_idx].targets, preferred_targets);
            if (candidate_score > best_score) {
                best_idx = candidate_idx;
                best_score = candidate_score;
            }
        }
        idx = static_cast<int>(best_idx);
    } else if (policy_cb != nullptr) {
        EventDecision decision;
        decision.kind = DecisionKind::SmallChoice;
        decision.source_card = card_id;
        decision.acting_side = side;
        const auto option_count = std::min(static_cast<int>(ops_actions.size()), EventDecision::kMaxEligible);
        decision.n_options = option_count;
        for (int option = 0; option < option_count; ++option) {
            decision.eligible_ids[option] = option;
        }
        idx = std::clamp((*policy_cb)(gs.pub, decision), 0, option_count - 1);
    }

    auto [ops_pub, ops_over, ops_winner] =
        apply_action(gs.pub, ops_actions[static_cast<size_t>(idx)], side, rng, policy_cb, frame_log);
    gs.pub = ops_pub;
    return {ops_pub, ops_over, ops_winner};
}

}  // namespace

DecisionFrame logged_frame_copy(
    const DecisionFrame& frame,
    std::vector<DecisionFrame>* frame_log,
    const FrameAction& action
) {
    auto logged = frame;
    if (frame_log != nullptr) {
        logged.stack_depth = frame_count(frame_log->size());
    }
    logged.chosen_action = action;

    if (logged.kind == FrameKind::SmallChoice) {
        const auto ops = std::max(0, static_cast<int>(logged.budget_remaining));
        const auto mode_index = std::clamp(
            action.option_index,
            0,
            std::max(0, static_cast<int>(logged.eligible_n) - 1)
        );
        const auto country_steps = mode_index == 2 ? 1 : ops;
        logged.step_index = 0;
        logged.total_steps = frame_count(static_cast<size_t>(std::max(1, country_steps + 1)));
        logged.criteria_bits = static_cast<uint16_t>(mode_index);
    }
    return logged;
}

bool apply_frame_ops_impl(
    GameState& gs,
    std::vector<DecisionFrame>* frame_log,
    CardId card_id,
    Side side,
    int ops,
    Pcg64Rng& rng
) {
    (void)rng;
    if (frame_log == nullptr || ops <= 0) {
        return false;
    }

    const auto accessible = accessible_countries(side, gs.pub, ActionMode::Influence);
    if (accessible.empty()) {
        return false;
    }

    push_option_frame(frame_log, FrameKind::SmallChoice, card_id, side, 4, 0, 1);
    if (frame_log->empty()) {
        return false;
    }
    frame_log->back().budget_remaining = static_cast<int16_t>(ops);
    return true;
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_trap_ar(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log
) {
    auto* effective_frame_log = frame_log;
    if (gs.frame_stack_mode && policy_cb == nullptr && effective_frame_log == nullptr) {
        effective_frame_log = &gs.frame_stack;
    }

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

    const auto source_card = static_cast<CardId>(bear_trap ? 47 : 45);
    if (gs.frame_stack_mode && policy_cb == nullptr && effective_frame_log != nullptr) {
        push_card_frame(effective_frame_log, FrameKind::ForcedDiscard, source_card, side, eligible, 0, 1);
        return std::tuple{gs.pub, false, std::nullopt};
    }

    const auto chosen = choose_card(pub, source_card, side, eligible, rng, policy_cb, effective_frame_log);
    discard_from_hand(gs, side, chosen, pub);
    if (roll_d6(rng) >= 5) {
        if (bear_trap) {
            pub.bear_trap_active = false;
        } else {
            pub.quagmire_active = false;
        }
        gs.pub = pub;
        const auto [over, winner] = check_vp_win(pub);
        if (over) {
            return std::tuple{pub, over, winner};
        }
        return std::nullopt;
    }
    gs.pub = pub;
    const auto [over, winner] = check_vp_win(pub);
    return std::tuple{pub, over, winner};
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_cuban_missile_crisis_cancel(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log
) {
    auto* effective_frame_log = frame_log;
    if (gs.frame_stack_mode && policy_cb == nullptr && effective_frame_log == nullptr) {
        effective_frame_log = &gs.frame_stack;
    }

    if (!gs.pub.cuban_missile_crisis_active) {
        return std::nullopt;
    }

    const auto eligible = cmc_cancel_cards(gs, side);
    if (eligible.empty()) {
        return std::nullopt;
    }

    if (gs.frame_stack_mode && policy_cb == nullptr && effective_frame_log != nullptr) {
        push_option_frame(effective_frame_log, FrameKind::CancelChoice, 43, side, 2, 0, 2);
        return std::tuple{gs.pub, false, std::nullopt};
    }

    if (choose_option(gs.pub, static_cast<CardId>(43), side, 2, rng, policy_cb, effective_frame_log) == 0) {
        return std::nullopt;
    }

    auto pub = gs.pub;
    const auto chosen = choose_card(pub, static_cast<CardId>(43), side, eligible, rng, policy_cb, effective_frame_log);
    discard_from_hand(gs, side, chosen, pub);
    pub.cuban_missile_crisis_active = false;
    gs.pub = pub;
    const auto [over, winner] = check_vp_win(pub);
    return std::tuple{pub, over, winner};
}

std::tuple<PublicState, bool, std::optional<Side>> apply_action_with_hands(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log
) {
    auto* effective_frame_log = frame_log;
    if (gs.frame_stack_mode && policy_cb == nullptr && effective_frame_log == nullptr) {
        effective_frame_log = &gs.frame_stack;
    }

    if (action.mode != ActionMode::Event && action.mode != ActionMode::Space) {
        const auto owner = card_spec(action.card_id).side;
        if (owner == other_side(side)) {
            if (action.mode == ActionMode::EventFirst) {
                auto [event_pub, event_over, event_winner] =
                    fire_event_with_state(gs, action.card_id, owner, rng, policy_cb, effective_frame_log);
                gs.pub = event_pub;
                if (event_over) {
                    return {event_pub, true, event_winner};
                }
                return execute_deferred_ops(gs, action.card_id, side, rng, policy_cb, action.targets, effective_frame_log);
            }

            auto [ops_pub, ops_over, ops_winner] = apply_action(
                gs.pub,
                action,
                side,
                rng,
                policy_cb,
                effective_frame_log,
                gs.frame_stack_mode
            );
            gs.pub = ops_pub;
            if (ops_over) {
                return {ops_pub, true, ops_winner};
            }

            auto [event_pub, event_over, event_winner] =
                fire_event_with_state(gs, action.card_id, owner, rng, policy_cb, effective_frame_log);
            gs.pub = event_pub;
            if (event_over) {
                return {event_pub, true, event_winner};
            }

            return {gs.pub, false, std::nullopt};
        }
    }

    if (action.mode == ActionMode::Event && is_cat_c_card(action.card_id)) {
        auto [event_pub, over, winner] =
            apply_hand_event(gs, action.card_id, side, rng, policy_cb, effective_frame_log);
        gs.pub = event_pub;
        return {event_pub, over, winner};
    }

    auto [new_pub, over, winner] = apply_action(
        gs.pub,
        action,
        side,
        rng,
        policy_cb,
        effective_frame_log,
        gs.frame_stack_mode
    );
    gs.pub = new_pub;
    if (over && action.mode == ActionMode::Event && card_spec(action.card_id).is_scoring) {
        gs.scoring_auto_win = true;
    }
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

std::tuple<PublicState, bool, std::optional<Side>> apply_headline_event_with_hands(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log
) {
    ActionEncoding headline{
        .card_id = action.card_id,
        .mode = ActionMode::Event,
        .targets = {},
    };
    if (!is_event_play_allowed(gs.pub, side, headline.card_id)) {
        discard_without_event(gs.pub, headline.card_id, side);
        return {gs.pub, false, std::nullopt};
    }
    return apply_action_with_hands(gs, headline, side, rng, policy_cb, frame_log);
}

}  // namespace ts
