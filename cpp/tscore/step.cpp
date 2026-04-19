// Single-action application and event dispatch for the native engine.

#include "step.hpp"

#include <algorithm>

#include "adjacency.hpp"
#include "dice.hpp"
#include "game_data.hpp"

namespace ts {

namespace {

uint8_t clamp_frame_count(size_t value) {
    return static_cast<uint8_t>(std::min<size_t>(value, 255));
}

DecisionFrame make_decision_frame(
    FrameKind kind,
    CardId card_id,
    Side side,
    size_t eligible_n,
    const std::vector<DecisionFrame>& frame_log
) {
    DecisionFrame frame;
    frame.kind = kind;
    frame.source_card = card_id;
    frame.acting_side = side;
    frame.eligible_n = clamp_frame_count(eligible_n);
    frame.stack_depth = clamp_frame_count(frame_log.size());
    return frame;
}

void record_option_frame(
    CardId card_id,
    Side side,
    int n_options,
    std::vector<DecisionFrame>* frame_log
) {
    if (frame_log == nullptr) {
        return;
    }
    frame_log->push_back(make_decision_frame(
        FrameKind::SmallChoice,
        card_id,
        side,
        static_cast<size_t>(n_options),
        *frame_log
    ));
}

void record_country_frame(
    CardId card_id,
    Side side,
    std::span<const CountryId> pool,
    std::vector<DecisionFrame>* frame_log
) {
    if (frame_log == nullptr) {
        return;
    }
    auto frame = make_decision_frame(FrameKind::CountryPick, card_id, side, pool.size(), *frame_log);
    for (const auto cid : pool) {
        frame.eligible_countries.set(static_cast<size_t>(cid));
    }
    frame_log->push_back(frame);
}

void record_card_frame(
    CardId card_id,
    Side side,
    std::span<const CardId> pool,
    std::vector<DecisionFrame>* frame_log
) {
    if (frame_log == nullptr) {
        return;
    }
    auto frame = make_decision_frame(FrameKind::CardSelect, card_id, side, pool.size(), *frame_log);
    for (const auto eligible_card : pool) {
        frame.eligible_cards.set(eligible_card);
    }
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
    frame.step_index = clamp_frame_count(static_cast<size_t>(std::max(0, step_index)));
    frame.total_steps = clamp_frame_count(static_cast<size_t>(std::max(1, total_steps)));
    frame.criteria_bits = criteria_bits;
}

}  // namespace

int choose_option(
    const PublicState& pub,
    CardId card_id,
    Side side,
    int n_options,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log,
    bool frame_stack_mode
) {
    if (n_options <= 0) {
        return 0;
    }
    if (policy_cb == nullptr && frame_stack_mode && frame_log != nullptr) {
        record_option_frame(card_id, side, n_options, frame_log);
        return -1;
    }
    int choice = 0;
    if (policy_cb != nullptr && n_options > 1) {
        EventDecision decision;
        decision.source_card = card_id;
        decision.kind = DecisionKind::SmallChoice;
        decision.n_options = n_options;
        decision.acting_side = side;
        choice = std::clamp((*policy_cb)(pub, decision), 0, n_options - 1);
    } else {
        choice = static_cast<int>(rng.choice_index(static_cast<size_t>(n_options)));
    }
    record_option_frame(card_id, side, n_options, frame_log);
    return choice;
}

CountryId choose_country(
    const PublicState& pub,
    CardId card_id,
    Side side,
    std::span<const CountryId> pool,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log,
    bool frame_stack_mode
) {
    const auto n_options = static_cast<int>(pool.size());
    if (n_options <= 0) {
        return 0;
    }
    if (policy_cb == nullptr && frame_stack_mode && frame_log != nullptr) {
        record_country_frame(card_id, side, pool, frame_log);
        return 0;
    }
    CountryId selected = 0;
    if (policy_cb != nullptr && n_options > 1) {
        EventDecision decision;
        decision.source_card = card_id;
        decision.kind = DecisionKind::CountrySelect;
        decision.n_options = n_options;
        decision.acting_side = side;
        for (int i = 0; i < n_options; ++i) {
            decision.eligible_ids[i] = static_cast<int>(pool[static_cast<size_t>(i)]);
        }
        const auto choice = std::clamp((*policy_cb)(pub, decision), 0, n_options - 1);
        selected = pool[static_cast<size_t>(choice)];
    } else {
        selected = pool[rng.choice_index(pool.size())];
    }
    record_country_frame(card_id, side, pool, frame_log);
    return selected;
}

CardId choose_card(
    const PublicState& pub,
    CardId card_id,
    Side side,
    std::span<const CardId> pool,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log,
    bool frame_stack_mode
) {
    const auto n_options = static_cast<int>(pool.size());
    if (n_options <= 0) {
        return 0;
    }
    if (policy_cb == nullptr && frame_stack_mode && frame_log != nullptr) {
        record_card_frame(card_id, side, pool, frame_log);
        return 0;
    }
    CardId selected = 0;
    if (policy_cb != nullptr && n_options > 1) {
        EventDecision decision;
        decision.source_card = card_id;
        decision.kind = DecisionKind::CardSelect;
        decision.n_options = n_options;
        decision.acting_side = side;
        for (int i = 0; i < n_options; ++i) {
            decision.eligible_ids[i] = static_cast<int>(pool[static_cast<size_t>(i)]);
        }
        const auto choice = std::clamp((*policy_cb)(pub, decision), 0, n_options - 1);
        selected = pool[static_cast<size_t>(choice)];
    } else {
        selected = pool[rng.choice_index(pool.size())];
    }
    record_card_frame(card_id, side, pool, frame_log);
    return selected;
}

WarResult apply_war_card(
    PublicState& next,
    Side attacker,
    CountryId target,
    int card_ops,
    int influence_on_success,
    Pcg64Rng& rng
) {
    const auto defender = other_side(attacker);
    const auto die_roll = static_cast<int>((rng() % 6) + 1);
    const auto threshold = 2 * country_spec(target).stability;
    const auto success = (die_roll + card_ops) >= threshold;
    if (success) {
        next.set_influence(attacker, target, next.influence_of(attacker, target) + influence_on_success);
        next.set_influence(defender, target, 0);
        if (attacker == Side::USSR) {
            next.vp += 2;
        } else {
            next.vp -= 2;
        }
    } else if (attacker == Side::USSR) {
        next.vp -= 1;
    } else {
        next.vp += 1;
    }
    return WarResult{
        .success = success,
        .die_roll = die_roll,
        .threshold = threshold,
    };
}

int apply_free_coup(
    PublicState& pub,
    Side side,
    CountryId country_id,
    int ops,
    Pcg64Rng& rng,
    bool defcon_immune
) {
    const auto opponent = other_side(side);
    const auto net = coup_result(ops, country_spec(country_id).stability, rng);
    if (net > 0) {
        const auto removed = std::min(net, pub.influence_of(opponent, country_id));
        pub.set_influence(opponent, country_id, pub.influence_of(opponent, country_id) - removed);
        if (const auto excess = net - removed; excess > 0) {
            pub.set_influence(side, country_id, pub.influence_of(side, country_id) + excess);
        }
    }
    if (country_spec(country_id).is_battleground && !defcon_immune) {
        pub.defcon = std::max(1, pub.defcon - 1);
    }
    pub.milops[to_index(side)] = std::max(pub.milops[to_index(side)], ops);
    return net;
}

namespace {

// Card-group constants used by event implementations below.
constexpr std::array<CardId, 5> kWarCardIds = {11, 13, 24, 39, 105};
constexpr std::array<CountryId, 7> kEasternBlocIds = {3, 5, 9, 12, 13, 19, 83};
constexpr std::array<CountryId, 12> kWesternEuropeIds = {1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18};
constexpr CountryId kIndiaId = 21;
constexpr CountryId kJapanId = 22;
constexpr CountryId kPakistanId = 24;
constexpr CountryId kEgyptId = 26;
constexpr CountryId kSouthKoreaId = 25;
constexpr CountryId kIranId = 28;
constexpr CountryId kIraqId = 29;
constexpr CountryId kIsraelId = 30;
constexpr CountryId kJordanId = 31;
constexpr CountryId kLebanonId = 32;
constexpr CountryId kLibyaId = 33;
constexpr CountryId kSaudiArabiaId = 34;
constexpr CountryId kCubaId = 36;
constexpr CountryId kNicaraguaId = 43;
constexpr CountryId kChileId = 49;
constexpr CountryId kVenezuelaId = 55;
constexpr CountryId kAngolaId = 57;
constexpr CountryId kBotswanaId = 58;
constexpr CountryId kMozambiqueId = 66;
constexpr CountryId kSouthAfricaId = 71;
constexpr CountryId kZimbabweId = 74;
constexpr CountryId kFranceId = 7;
constexpr CountryId kUkId = 17;
constexpr CountryId kWestGermanyId = 18;
constexpr CountryId kPolandId = 12;
constexpr CountryId kRomaniaId = 13;
constexpr CountryId kVietnamId = 80;
constexpr std::array<CountryId, 7> kOpecIds = {kEgyptId, kIranId, kLibyaId, kSaudiArabiaId, kIraqId, 27, kVenezuelaId};

bool contains(std::span<const CardId> values, CardId value) {
    return std::find(values.begin(), values.end(), value) != values.end();
}

template <typename T>
const T& sample_one(std::span<const T> values, Pcg64Rng& rng) {
    return values[rng.choice_index(values.size())];
}

CountryId resolve_event_country_choice(
    const PublicState& pub,
    const ActionEncoding& action,
    CardId card_id,
    Side side,
    std::span<const CountryId> pool,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log
) {
    if (!action.targets.empty()) {
        const auto requested = action.targets.front();
        if (std::find(pool.begin(), pool.end(), requested) != pool.end()) {
            return requested;
        }
    }
    return choose_country(pub, card_id, side, pool, rng, policy_cb, frame_log);
}

void apply_vp_delta(PublicState& pub, Side side, int delta) {
    if (side == Side::USSR) {
        pub.vp += delta;
    } else {
        pub.vp -= delta;
    }
}

void add_influence(PublicState& pub, Side side, CountryId country_id, int delta) {
    pub.set_influence(side, country_id, std::max(0, pub.influence_of(side, country_id) + delta));
}

void remove_all_influence(PublicState& pub, Side side, CountryId country_id) {
    pub.set_influence(side, country_id, 0);
}

void gain_control(PublicState& pub, Side side, CountryId country_id) {
    const auto opponent = other_side(side);
    const auto needed = pub.influence_of(opponent, country_id) + country_spec(country_id).stability;
    if (pub.influence_of(side, country_id) < needed) {
        pub.set_influence(side, country_id, needed);
    }
}

void advance_space_track(PublicState& pub, Side side, int steps) {
    static constexpr std::array<std::pair<int, int>, 9> kSpaceVp = {{
        {0, 0}, {2, 0}, {0, 0}, {2, 0}, {0, 0}, {3, 1}, {0, 0}, {4, 2}, {2, 0},
    }};
    const auto opponent = other_side(side);
    for (int i = 0; i < steps; ++i) {
        const auto current = pub.space[to_index(side)];
        if (current >= 8) {
            break;
        }
        const auto next_level = current + 1;
        pub.space[to_index(side)] = next_level;
        const auto [first_vp, second_vp] = kSpaceVp[next_level];
        const auto vp = pub.space[to_index(opponent)] < next_level ? first_vp : second_vp;
        apply_vp_delta(pub, side, vp);
    }
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
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr,
    std::vector<DecisionFrame>* frame_log = nullptr,
    bool frame_stack_mode = false
) {
    auto next = pub;
    bool force_game_over = false;
    std::optional<Side> forced_winner;

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

    switch (action.card_id) {
        case 9:
            add_influence(next, Side::USSR, kVietnamId, 2);
            next.vietnam_revolts_active = true;
            break;

        case 4: {
            const auto pre_defcon = next.defcon;
            next.vp -= (5 - pre_defcon);
            next.defcon = std::max(1, next.defcon - 1);
            break;
        }

        case 7: {
            std::vector<CountryId> pool;
            for (const auto cid : kWesternEuropeIds) {
                if (!controls_country(Side::US, cid, next) && next.influence_of(Side::USSR, cid) < 2) {
                    pool.push_back(cid);
                }
            }
            const int total_steps = std::min<int>(3, static_cast<int>(pool.size()));
            for (int i = 0; i < total_steps; ++i) {
                const auto cid = choose_country(
                    next,
                    static_cast<CardId>(7),
                    Side::USSR,
                    pool,
                    rng,
                    policy_cb,
                    frame_log,
                    frame_stack_mode
                );
                if (cid == 0) {
                    annotate_latest_frame(frame_log, i, total_steps);
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::USSR, cid, 1);
                pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
            }
            break;
        }

        case 8:
            remove_all_influence(next, Side::US, kCubaId);
            gain_control(next, Side::USSR, kCubaId);
            break;

        case 11: {
            apply_war_card(next, Side::USSR, kSouthKoreaId, 2, 2, rng);
            break;
        }

        case 12:
            remove_all_influence(next, Side::US, kRomaniaId);
            gain_control(next, Side::USSR, kRomaniaId);
            break;

        case 13: {
            apply_war_card(next, Side::USSR, kIsraelId, 2, 2, rng);
            break;
        }

        case 14: {
            std::vector<CountryId> pool;
            for (const auto cid : kEasternBlocIds) {
                if (!controls_country(Side::US, cid, next)) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 4; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid =
                    choose_country(next, static_cast<CardId>(14), Side::USSR, pool, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, std::min<int>(4, i + static_cast<int>(pool.size())));
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::USSR, cid, 1);
                pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
            }
            break;
        }

        case 15: {
            add_influence(next, Side::USSR, kEgyptId, 2);
            const auto remove = (next.influence_of(Side::US, kEgyptId) + 1) / 2;
            add_influence(next, Side::US, kEgyptId, -remove);
            break;
        }

        case 16: {
            // Warsaw Pact: 0 = remove US influence from 4 E.Europe, 1 = add USSR to 5 E.Europe
            const auto choice = choose_option(next, 16, Side::USSR, 2, rng, policy_cb, frame_log, frame_stack_mode);
            if (choice < 0) {
                return {next, false, std::nullopt};
            }
            if (choice == 0) {
                std::vector<CountryId> pool;
                for (const auto cid : kEasternBlocIds) {
                    if (next.influence_of(Side::US, cid) > 0) {
                        pool.push_back(cid);
                    }
                }
                for (int i = 0; i < 4; ++i) {
                    if (pool.empty()) {
                        break;
                    }
                    const auto cid = choose_country(
                        next,
                        static_cast<CardId>(16),
                        Side::USSR,
                        pool,
                        rng,
                        policy_cb,
                        frame_log,
                        frame_stack_mode
                    );
                    if (cid == 0) {
                        annotate_latest_frame(frame_log, i, std::min<int>(4, i + static_cast<int>(pool.size())), 0);
                        return {next, false, std::nullopt};
                    }
                    remove_all_influence(next, Side::US, cid);
                    pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
                }
            } else {
                const std::vector<CountryId> pool(kEasternBlocIds.begin(), kEasternBlocIds.end());
                for (int i = 0; i < 5; ++i) {
                    if (pool.empty()) {
                        break;
                    }
                    const auto cid = choose_country(
                        next,
                        static_cast<CardId>(16),
                        Side::USSR,
                        pool,
                        rng,
                        policy_cb,
                        frame_log,
                        frame_stack_mode
                    );
                    if (cid == 0) {
                        annotate_latest_frame(frame_log, i, 5, 1);
                        return {next, false, std::nullopt};
                    }
                    add_influence(next, Side::USSR, cid, 1);
                }
            }
            next.warsaw_pact_played = true;
            break;
        }

        case 20: {
            // Olympic Games: 0 = boycott (DEFCON -1, place 4 inf), 1 = compete (dice)
            if (choose_option(next, 20, other_side(side), 2, rng, policy_cb, frame_log) == 0) {
                next.defcon = std::max(1, next.defcon - 1);
                const auto accessible = accessible_countries(side, next, ActionMode::Influence);
                if (!accessible.empty()) {
                    for (int i = 0; i < 4; ++i) {
                        const auto cid =
                            choose_country(next, static_cast<CardId>(20), side, accessible, rng, policy_cb, frame_log);
                        add_influence(next, side, cid, 1);
                    }
                }
            } else {
                const auto opponent = other_side(side);
                auto my_roll = roll_d6(rng);
                auto opp_roll = roll_d6(rng);
                while (my_roll == opp_roll) {
                    my_roll = roll_d6(rng);
                    opp_roll = roll_d6(rng);
                }
                apply_vp_delta(next, my_roll > opp_roll ? side : opponent, 2);
            }
            break;
        }

        case 21:
            next.nato_active = true;
            break;

        case 22:
            for (const auto cid : {CountryId{19}, CountryId{13}, CountryId{83}, CountryId{9}, CountryId{3}}) {
                add_influence(next, Side::US, cid, 1);
            }
            break;

        case 23: {
            std::vector<CountryId> pool;
            for (const auto cid : kWesternEuropeIds) {
                if (!controls_country(Side::USSR, cid, next)) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 7; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid =
                    choose_country(next, static_cast<CardId>(23), Side::US, pool, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, std::min<int>(7, i + static_cast<int>(pool.size())));
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::US, cid, 1);
                pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
            }
            next.marshall_plan_played = true;
            break;
        }

        case 24: {
            static constexpr std::array<CountryId, 2> kTargets = {kIndiaId, kPakistanId};
            const auto target = resolve_event_country_choice(
                next, action, 24, side, std::span<const CountryId>(kTargets), rng, policy_cb, frame_log
            );
            apply_war_card(next, side, target, 2, 2, rng);
            break;
        }

        case 17:
            add_influence(next, Side::US, kFranceId, -2);
            add_influence(next, Side::USSR, kFranceId, 1);
            next.de_gaulle_active = true;
            break;

        case 18:
            advance_space_track(next, side, 1);
            break;

        case 19: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (country_spec(cid).region != Region::Europe) {
                    continue;
                }
                if (next.influence_of(Side::USSR, cid) <= 0) {
                    continue;
                }
                if (!controls_country(Side::USSR, cid, next)) {
                    pool.push_back(cid);
                }
            }
            if (!pool.empty()) {
                const auto cid =
                    choose_country(next, static_cast<CardId>(19), Side::US, pool, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, 0, 1);
                    return {next, false, std::nullopt};
                }
                remove_all_influence(next, Side::USSR, cid);
            }
            next.truman_doctrine_played = true;
            break;
        }

        case 25:
            next.ops_modifier[to_index(Side::US)] += 1;
            break;

        case 27:
            next.us_japan_pact_active = true;
            gain_control(next, Side::US, kJapanId);
            break;

        case 28: {
            std::vector<CountryId> pool = {kFranceId, kUkId, kIsraelId};
            for (int i = 0; i < 2; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid = choose_country(
                    next,
                    static_cast<CardId>(28),
                    Side::USSR,
                    pool,
                    rng,
                    policy_cb,
                    frame_log,
                    frame_stack_mode
                );
                if (cid == 0) {
                    annotate_latest_frame(frame_log, i, std::min<int>(2, i + static_cast<int>(pool.size())));
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::US, cid, -2);
                pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
            }
            break;
        }

        case 29: {
            // East European Unrest: remove 1 USSR influence from 3 E.Europe countries
            // (2 each in Late War, turns 8-10).
            const int amount = (next.turn >= 8) ? 2 : 1;
            std::vector<CountryId> pool(kEasternBlocIds.begin(), kEasternBlocIds.end());
            for (int i = 0; i < 3; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid =
                    choose_country(next, static_cast<CardId>(29), Side::US, pool, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, std::min<int>(3, i + static_cast<int>(pool.size())));
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::USSR, cid, -amount);
                pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
            }
            break;
        }

        case 30: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                const auto region = country_spec(cid).region;
                if (region == Region::Africa || region == Region::SoutheastAsia) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 4; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid =
                    choose_country(next, static_cast<CardId>(30), Side::USSR, pool, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, 4);
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::USSR, cid, 1);
            }
            break;
        }

        case 31:
            next.ops_modifier[to_index(other_side(side))] -= 1;
            break;

        case 33: {
            std::vector<CountryId> sources;
            std::vector<CountryId> destinations;
            for (const auto cid : all_country_ids()) {
                if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                    continue;
                }
                if (next.influence_of(Side::USSR, cid) > 0) {
                    sources.push_back(cid);
                }
                if (!controls_country(Side::US, cid, next)) {
                    destinations.push_back(cid);
                }
            }
            int total_to_move = 0;
            for (const auto cid : sources) {
                total_to_move += next.influence_of(Side::USSR, cid);
            }
            total_to_move = std::min(total_to_move, 4);
            for (int i = 0; i < total_to_move; ++i) {
                std::vector<CountryId> available_sources;
                for (const auto cid : sources) {
                    if (next.influence_of(Side::USSR, cid) > 0) {
                        available_sources.push_back(cid);
                    }
                }
                if (available_sources.empty() || destinations.empty()) {
                    break;
                }
                const auto src =
                    choose_country(next, static_cast<CardId>(33), Side::USSR, available_sources, rng, policy_cb, frame_log);
                const auto dst =
                    choose_country(next, static_cast<CardId>(33), Side::USSR, destinations, rng, policy_cb, frame_log);
                add_influence(next, Side::USSR, src, -1);
                add_influence(next, Side::USSR, dst, 1);
            }
            break;
        }

        case 34: {
            const auto vp_gain = std::max(0, next.defcon - 2);
            apply_vp_delta(next, side, vp_gain);
            next.defcon = std::min(5, next.defcon + 2);
            break;
        }

        case 35:
            next.formosan_active = true;
            break;

        case 37:
            if (controls_country(Side::US, kUkId, next) && next.nato_active) {
                next.vp -= 2;
                std::vector<CountryId> pool;
                for (const auto cid : all_country_ids()) {
                    if (cid != 64 && cid != kUsaAnchorId && cid != kUssrAnchorId) {
                        pool.push_back(cid);
                    }
                }
                for (int i = 0; i < 2 && !pool.empty(); ++i) {
                    const auto cid = choose_country(next, static_cast<CardId>(37), Side::US, pool, rng, policy_cb, frame_log);
                    add_influence(next, Side::US, cid, 1);
                }
            } else {
                add_influence(
                    next,
                    Side::US,
                    choose_country(next, static_cast<CardId>(37), Side::US, kWesternEuropeIds, rng, policy_cb, frame_log),
                    1
                );
            }
            break;

        case 38:
            next.norad_active = true;
            break;

        case 39: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                    continue;
                }
                if (country_spec(cid).stability <= 2) {
                    pool.push_back(cid);
                }
            }
            if (!pool.empty()) {
                const auto target = resolve_event_country_choice(
                    next, action, 39, side, std::span<const CountryId>(pool), rng, policy_cb, frame_log
                );
                apply_war_card(next, side, target, 3, 3, rng);
            }
            break;
        }

        case 42: {
            const auto own = next.milops[to_index(side)];
            const auto opp = next.milops[to_index(other_side(side))];
            if (own > opp) {
                apply_vp_delta(next, side, own >= next.defcon ? 3 : 1);
            }
            break;
        }

        case 43:
            next.defcon = 2;
            next.cuban_missile_crisis_active = true;
            break;

        case 44:
            next.nuclear_subs_active = true;
            break;

        case 46:
            next.defcon = std::min(5, next.defcon + 1);
            next.salt_active = true;
            break;

        case 48: {
            auto ussr_roll = roll_d6(rng);
            auto us_roll = roll_d6(rng);
            const auto winner =
                side == Side::USSR ? (ussr_roll >= us_roll ? Side::USSR : Side::US)
                                   : (us_roll >= ussr_roll ? Side::US : Side::USSR);
            // Summit: winner chooses DEFCON direction. 0 = lower (-1), 1 = raise (+1)
            const auto defcon_delta = choose_option(next, 48, winner, 2, rng, policy_cb, frame_log) == 0 ? -1 : 1;
            next.defcon = std::clamp(next.defcon + defcon_delta, 1, 5);
            apply_vp_delta(next, winner, 2);
            break;
        }

        case 49: {
            // How I Learned: player sets DEFCON to 2-5 (never 1 — suicide for phasing player).
            // Options: 0→DEFCON 2, 1→DEFCON 3, 2→DEFCON 4, 3→DEFCON 5
            const auto choice = choose_option(next, 49, side, 4, rng, policy_cb, frame_log, frame_stack_mode);
            if (choice < 0) {
                return {next, false, std::nullopt};
            }
            next.defcon = choice + 2;
            next.milops[to_index(side)] = 5;
            break;
        }

        case 50: {
            // OAS Founded: +2 influence and free coup in Central/South America
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                const auto region = country_spec(cid).region;
                if (region == Region::CentralAmerica || region == Region::SouthAmerica) {
                    pool.push_back(cid);
                }
            }
            if (!pool.empty()) {
                const auto inf_target = choose_country(next, 50, side, pool, rng, policy_cb, frame_log);
                add_influence(next, side, inf_target, 2);
                const auto coup_target = choose_country(next, 50, side, pool, rng, policy_cb, frame_log);
                apply_free_coup(next, side, coup_target, 2, rng, false);
            }
            break;
        }

        case 51: {
            int us_bg = 0;
            int ussr_bg = 0;
            for (const auto cid : all_country_ids()) {
                if ((cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) || !country_spec(cid).is_battleground) {
                    continue;
                }
                if (controls_country(Side::US, cid, next)) {
                    ++us_bg;
                }
                if (controls_country(Side::USSR, cid, next)) {
                    ++ussr_bg;
                }
            }
            if (const auto excess = us_bg - ussr_bg; excess > 0) {
                next.vp -= excess;
            }
            break;
        }

        case 53:
            next.defcon = std::max(1, next.defcon - 1);
            next.vp += 3;
            break;

        case 54:
            next.ops_modifier[to_index(Side::USSR)] += 1;
            break;

        case 55:
            add_influence(next, Side::USSR, kAngolaId, 2);
            add_influence(next, Side::USSR, kMozambiqueId, 2);
            break;

        case 56: {
            // South African Unrest: +2 to South Africa, +2 to chosen neighbor
            add_influence(next, Side::USSR, kSouthAfricaId, 2);
            static constexpr std::array<CountryId, 3> kSaNeighbors = {kBotswanaId, 69, kZimbabweId};
            const auto neighbor = choose_country(
                next,
                56,
                Side::USSR,
                kSaNeighbors,
                rng,
                policy_cb,
                frame_log,
                frame_stack_mode
            );
            if (neighbor == 0) {
                annotate_latest_frame(frame_log, 0, 1);
                return {next, false, std::nullopt};
            }
            add_influence(next, Side::USSR, neighbor, 2);
            break;
        }

        case 57:
            add_influence(next, Side::USSR, kChileId, 2);
            break;

        case 58:
            next.vp += 1;
            add_influence(next, Side::USSR, kWestGermanyId, 1);
            next.willy_brandt_active = true;
            break;

        case 59: {
            static constexpr std::array<CountryId, 8> kPool = {72, kIranId, kIraqId, kEgyptId, kLibyaId, kSaudiArabiaId, 35, kJordanId};
            std::vector<CountryId> eligible;
            for (const auto cid : kPool) {
                if (next.influence_of(Side::US, cid) > 0) {
                    eligible.push_back(cid);
                }
            }
            if (eligible.size() < 2) {
                eligible.assign(kPool.begin(), kPool.end());
            }
            for (int i = 0; i < 2; ++i) {
                if (eligible.empty()) {
                    break;
                }
                const auto cid = choose_country(
                    next,
                    static_cast<CardId>(59),
                    Side::USSR,
                    eligible,
                    rng,
                    policy_cb,
                    frame_log,
                    frame_stack_mode
                );
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, std::min<int>(2, i + static_cast<int>(eligible.size())));
                    return {next, false, std::nullopt};
                }
                remove_all_influence(next, Side::US, cid);
                eligible.erase(std::remove(eligible.begin(), eligible.end(), cid), eligible.end());
            }
            break;
        }

        case 60: {
            next.defcon = std::min(5, next.defcon + 1);
            apply_vp_delta(next, side, 1);
            std::vector<CountryId> eligible;
            for (const auto cid : all_country_ids()) {
                if (next.influence_of(side, cid) > 0) {
                    eligible.push_back(cid);
                }
            }
            for (int i = 0; i < 2 && !eligible.empty(); ++i) {
                const auto cid =
                    choose_country(next, static_cast<CardId>(60), side, eligible, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, 2);
                    return {next, false, std::nullopt};
                }
                add_influence(next, side, cid, 1);
            }
            break;
        }

        case 61:
            if (next.china_held_by == Side::US) {
                next.china_held_by = Side::USSR;
                next.china_playable = false;
            } else {
                next.vp += 1;
            }
            break;

        case 62:
            next.flower_power_active = true;
            break;

        case 63:
            next.vp += 1;
            break;

        case 64: {
            if (!next.opec_cancelled) {
                int count = 0;
                for (const auto cid : kOpecIds) {
                    if (cid == kSaudiArabiaId && next.awacs_active) {
                        continue;
                    }
                    if (next.influence_of(Side::USSR, cid) > 0) {
                        ++count;
                    }
                }
                next.vp += count;
            }
            break;
        }

        case 65:
            next.defcon = std::min(5, next.defcon + 1);
            next.vp -= 1;
            break;

        case 70:
            next.latam_coup_bonus = side;
            break;

        case 66:
            apply_vp_delta(next, Side::US, 1);
            add_influence(next, Side::US, kIsraelId, 1);
            add_influence(next, Side::US, kEgyptId, 1);
            add_influence(next, Side::US, kJordanId, 1);
            break;

        case 67: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                    continue;
                }
                if (next.influence_of(Side::USSR, cid) == 0 && next.influence_of(Side::US, cid) == 0) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 3; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid =
                    choose_country(next, static_cast<CardId>(67), Side::US, pool, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, std::min<int>(3, i + static_cast<int>(pool.size())));
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::US, cid, 1);
                pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
            }
            break;
        }

        case 69:
            add_influence(next, Side::USSR, kPolandId, -2);
            add_influence(next, Side::US, kPolandId, 1);
            next.john_paul_ii_played = true;
            break;

        case 71: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                const auto region = country_spec(cid).region;
                if (region == Region::CentralAmerica || region == Region::SouthAmerica) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 2 && !pool.empty(); ++i) {
                const auto cid =
                    choose_country(next, static_cast<CardId>(71), Side::US, pool, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, 2);
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::US, cid, 1);
            }
            break;
        }

        case 72:
            if (next.china_held_by == Side::USSR) {
                next.vp -= 2;
                next.china_held_by = Side::US;
                next.china_playable = false;
            } else if (next.china_held_by == Side::US) {
                next.china_playable = true;
            }
            break;

        case 73:
            remove_all_influence(next, Side::USSR, kEgyptId);
            add_influence(next, Side::US, kEgyptId, 1);
            break;

        case 74:
            next.shuttle_diplomacy_active = true;
            break;

        case 75: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                    continue;
                }
                if (country_spec(cid).region == Region::Europe) {
                    continue;
                }
                if (next.influence_of(Side::USSR, cid) >= 1) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 4; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid =
                    choose_country(next, static_cast<CardId>(75), Side::US, pool, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, std::min<int>(4, i + static_cast<int>(pool.size())));
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::USSR, cid, -1);
                pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
            }
            break;
        }

        case 76: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (country_spec(cid).region == Region::CentralAmerica && next.influence_of(Side::USSR, cid) < 2) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 3; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid = choose_country(
                    next,
                    static_cast<CardId>(76),
                    Side::USSR,
                    pool,
                    rng,
                    policy_cb,
                    frame_log,
                    frame_stack_mode
                );
                if (cid == 0) {
                    annotate_latest_frame(frame_log, i, 3);
                    return {next, false, std::nullopt};
                }
                add_influence(next, Side::USSR, cid, 1);
            }
            break;
        }

        case 77: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid != 64 && cid != kUsaAnchorId && cid != kUssrAnchorId) {
                    pool.push_back(cid);
                }
            }
            const Side acting = next.china_held_by;
            if (next.china_held_by == Side::USSR) {
                next.china_held_by = Side::US;
            } else {
                next.china_held_by = Side::USSR;
            }
            next.china_playable = true;
            for (int i = 0; i < 4 && !pool.empty(); ++i) {
                const auto cid =
                    choose_country(next, static_cast<CardId>(77), acting, pool, rng, policy_cb, frame_log, frame_stack_mode);
                if (cid == 0 && frame_stack_mode && policy_cb == nullptr && frame_log != nullptr) {
                    annotate_latest_frame(frame_log, i, 4);
                    return {next, false, std::nullopt};
                }
                add_influence(next, acting, cid, 1);
            }
            break;
        }

        case 79: {
            int count = 0;
            for (const auto cid : all_country_ids()) {
                const auto region = country_spec(cid).region;
                if (
                    (region == Region::CentralAmerica || region == Region::SouthAmerica) &&
                    country_spec(cid).is_battleground &&
                    controls_country(Side::US, cid, next)
                ) {
                    ++count;
                }
            }
            next.vp -= count;
            break;
        }

        case 81:
            if (next.space[to_index(side)] < next.space[to_index(other_side(side))]) {
                advance_space_track(next, side, 2);
            }
            break;

        case 83: {
            auto region_key = [&](CountryId cid) {
                const auto region = country_spec(cid).region;
                if (region == Region::CentralAmerica) {
                    return 0;
                }
                if (region == Region::SouthAmerica) {
                    return 1;
                }
                return 2;
            };
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid == 64) {
                    continue;
                }
                const auto region = country_spec(cid).region;
                if (
                    (region == Region::CentralAmerica || region == Region::SouthAmerica || region == Region::Africa) &&
                    country_spec(cid).stability <= 2
                ) {
                    pool.push_back(cid);
                }
            }
            if (!pool.empty()) {
                const auto first = choose_country(next, static_cast<CardId>(83), Side::USSR, pool, rng, policy_cb, frame_log);
                const auto first_region = region_key(first);
                apply_free_coup(next, Side::USSR, first, 3, rng, false);
                std::vector<CountryId> second_pool;
                for (const auto cid : pool) {
                    if (region_key(cid) != first_region) {
                        second_pool.push_back(cid);
                    }
                }
                if (!second_pool.empty()) {
                    apply_free_coup(
                        next,
                        Side::USSR,
                        choose_country(next, static_cast<CardId>(83), Side::USSR, second_pool, rng, policy_cb, frame_log),
                        3,
                        rng,
                        false
                    );
                }
            }
            break;
        }

        case 85:
            remove_all_influence(next, Side::US, kIranId);
            add_influence(next, Side::USSR, kIranId, 2);
            next.iran_hostage_crisis_active = true;
            break;

        case 89:
            next.opec_cancelled = true;
            next.north_sea_oil_extra_ar = true;
            break;

        case 90: {
            // The Reformer: 4 influence in non-US-controlled Europe + DEFCON+1.
            // +2 extra influence if USSR ahead on space race.
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (country_spec(cid).region == Region::Europe && !controls_country(Side::US, cid, next)) {
                    pool.push_back(cid);
                }
            }
            const int base = 4;
            const int bonus = (next.space[to_index(Side::USSR)] > next.space[to_index(Side::US)]) ? 2 : 0;
            for (int i = 0; i < (base + bonus); ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid = choose_country(next, static_cast<CardId>(90), Side::USSR, pool, rng, policy_cb, frame_log);
                add_influence(next, Side::USSR, cid, 1);
            }
            next.defcon = std::min(5, next.defcon + 1);
            break;
        }

        case 91: {
            remove_all_influence(next, Side::US, kLebanonId);
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (country_spec(cid).region != Region::MiddleEast || cid == kLebanonId) {
                    continue;
                }
                if (next.influence_of(Side::US, cid) >= 1) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 2; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid = choose_country(next, static_cast<CardId>(91), Side::US, pool, rng, policy_cb, frame_log);
                add_influence(next, Side::US, cid, -1);
                pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
            }
            break;
        }

        case 86:
            next.vp -= 1;
            remove_all_influence(next, Side::USSR, kUkId);
            next.opec_cancelled = true;
            break;

        case 87:
            next.vp -= next.influence_of(Side::USSR, kLibyaId);
            break;

        case 92:
            next.defcon = std::max(1, next.defcon - 1);
            next.vp -= 2;
            if (next.china_held_by == Side::USSR) {
                next.china_held_by = Side::US;
                next.china_playable = true;
            }
            break;

        case 93:
            next.vp += 2;
            next.defcon = std::min(5, next.defcon + 1);
            if (next.salt_active) {
                next.glasnost_free_ops = 4;
            }
            break;

        case 94: {
            // Junta: remove US from Nicaragua, free coup on Cuba/Chile/Nicaragua
            remove_all_influence(next, Side::US, kNicaraguaId);
            static constexpr std::array<CountryId, 3> kJuntaTargets = {38, 41, 45};  // Cuba, Chile, Nicaragua
            const auto target = choose_country(next, 94, Side::USSR, kJuntaTargets, rng, policy_cb, frame_log);
            apply_free_coup(next, Side::USSR, target, 2, rng, false);
            break;
        }

        case 96:
            next.ops_modifier[to_index(Side::US)] -= 1;
            break;

        case 98:
            next.vp += 2;
            break;

        case 99:
            remove_all_influence(next, Side::USSR, 5);
            add_influence(next, Side::US, 5, 3);
            next.willy_brandt_active = false;
            break;

        case 97: {
            // Chernobyl: US chooses region to block USSR influence placement
            // 0=Europe, 1=Asia, 2=MiddleEast, 3=CentralAmerica, 4=SouthAmerica, 5=Africa
            static constexpr std::array<Region, 6> kRegions = {
                Region::Europe,
                Region::Asia,
                Region::MiddleEast,
                Region::CentralAmerica,
                Region::SouthAmerica,
                Region::Africa,
            };
            const int idx = choose_option(next, 97, Side::US, 6, rng, policy_cb, frame_log);
            next.chernobyl_blocked_region = kRegions[idx];
            break;
        }

        case 100:
            next.vp -= 1;
            next.flower_power_cancelled = true;
            next.flower_power_active = false;
            break;

        case 103:
            if (next.defcon == 2) {
                apply_vp_delta(next, other_side(side), 6);
                force_game_over = true;
                if (next.vp > 0) {
                    forced_winner = Side::USSR;
                } else if (next.vp < 0) {
                    forced_winner = Side::US;
                } else {
                    forced_winner = std::nullopt;
                }
            }
            break;

        case 104:
            if (next.john_paul_ii_played) {
                add_influence(next, Side::US, kPolandId, 3);
            }
            break;

        case 102: {
            next.vp += 1;
            std::vector<CountryId> pool;
            for (const auto cid : kWesternEuropeIds) {
                if (next.influence_of(Side::US, cid) >= 1) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 3; ++i) {
                if (pool.empty()) {
                    break;
                }
                const auto cid =
                    (policy_cb != nullptr && pool.size() > 1)
                    ? choose_country(next, static_cast<CardId>(102), Side::USSR, pool, rng, policy_cb, frame_log)
                    : pool.front();
                add_influence(next, Side::US, cid, -1);
                pool.erase(std::remove(pool.begin(), pool.end(), cid), pool.end());
            }
            break;
        }

        case 105: {
            static constexpr std::array<CountryId, 2> kTargets = {kIranId, kIraqId};
            const auto target = resolve_event_country_choice(
                next, action, 105, side, std::span<const CountryId>(kTargets), rng, policy_cb, frame_log
            );
            apply_war_card(next, side, target, 2, 2, rng);
            break;
        }

        case 106:
            next.vp += next.space_attempts[to_index(Side::US)];
            break;

        case 107:
            add_influence(next, Side::US, kSaudiArabiaId, 2);
            next.awacs_active = true;
            break;

        case kChinaCardId:
            if (side == Side::USSR) {
                next.formosan_active = false;
            }
            break;

        default:
            break;
    }

    handle_card_played(next, action.card_id, side, ActionMode::Event);
    if (force_game_over) {
        return {next, true, forced_winner};
    }
    const auto [over, winner] = check_vp_win(next);
    return {next, over, winner};
}

}  // namespace

std::tuple<PublicState, bool, std::optional<Side>> apply_action(
    const PublicState& pub,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    std::vector<DecisionFrame>* frame_log,
    bool frame_stack_mode
) {
    auto next = pub;

    switch (action.mode) {
        case ActionMode::EventFirst:
            // EventFirst is Influence with event-before-ops ordering; ordering is
            // consumed by apply_action_with_hands before this point.
            [[fallthrough]];
        case ActionMode::Influence:
            for (const auto target : action.targets) {
                next.set_influence(side, target, next.influence_of(side, target) + 1);
            }
            handle_card_played(next, action.card_id, side, ActionMode::Influence);
            break;

        case ActionMode::Coup: {
            const auto target = action.targets.front();
            if (pub.cuban_missile_crisis_active && country_spec(target).is_battleground) {
                next.defcon = 1;
                handle_card_played(next, action.card_id, side, ActionMode::Coup);
                return {next, true, other_side(side)};
            }
            auto ops = effective_ops(action.card_id, pub, side);
            if (action.card_id == kChinaCardId && country_spec(target).region == Region::Asia) {
                ++ops;
            }
            ops += vietnam_revolts_ops_bonus(pub, side, action.targets);
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
            auto [event_pub, over, winner] = apply_event(pub, action, side, rng, policy_cb, frame_log, frame_stack_mode);
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
