// Shared helpers for MCTS, ISMCTS, and batched search implementations.
// Include from search .cpp files only.

#pragma once

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <optional>
#include <span>
#include <utility>
#include <vector>

#include "card_properties.hpp"
#include "game_data.hpp"
#include "game_loop.hpp"
#include "game_state.hpp"
#include "legal_actions.hpp"
#include "mcts.hpp"
#include "policies.hpp"
#include "rule_queries.hpp"
#include "scoring.hpp"

namespace ts {
namespace {

inline constexpr double kVirtualLossPenalty = 1.0;

// AR count at which the Space Shuttle gives an extra action round.
inline constexpr int kSpaceShuttleArs = 8;

struct ModeDraft {
    ActionMode mode = ActionMode::Influence;
    std::vector<ActionEncoding> edges;
};

struct CardDraft {
    CardId card_id = 0;
    std::vector<ModeDraft> modes;
};

struct AccessibleCache {
    std::vector<CountryId> influence;
    std::vector<CountryId> coup;
    std::vector<CountryId> realign;
    bool can_space = false;
    int space_ops_min = 2;

    [[nodiscard]] static AccessibleCache build(Side side, const PublicState& pub) {
        AccessibleCache cache;

        auto base_inf = accessible_countries(side, pub, ActionMode::Influence);
        auto base_coup = accessible_countries(side, pub, ActionMode::Coup);

        base_inf.erase(
            std::remove_if(
                base_inf.begin(),
                base_inf.end(),
                [&](CountryId cid) { return is_chernobyl_blocked(pub, side, cid); }
            ),
            base_inf.end()
        );
        cache.influence = std::move(base_inf);

        auto filter_military = [&](std::vector<CountryId>& countries) {
            countries.erase(
                std::remove_if(
                    countries.begin(),
                    countries.end(),
                    [&](CountryId cid) { return is_military_target_blocked(pub, side, cid); }
                ),
                countries.end()
            );
        };

        filter_military(base_coup);
        cache.realign = base_coup;

        // DEFCON=2 safety net: coup in any battleground lowers DEFCON by 1
        // -> DEFCON=1 = nuclear war = acting side loses. Strip battleground
        // countries from the coup target set at DEFCON=2 so search cannot
        // expand self-destruct edges. Realignment never lowers DEFCON, so
        // `cache.realign` keeps the full (non-battleground-filtered) set.
        if (pub.defcon == 2) {
            base_coup.erase(
                std::remove_if(
                    base_coup.begin(),
                    base_coup.end(),
                    [](CountryId cid) { return country_spec(cid).is_battleground; }
                ),
                base_coup.end()
            );
        }
        cache.coup = std::move(base_coup);

        const auto level = pub.space[to_index(side)];
        const auto opp_level = pub.space[to_index(other_side(side))];
        const auto max_space = (level >= 2 && opp_level < 2) ? 2 : 1;
        cache.can_space = (level < 8 && pub.space_attempts[to_index(side)] < max_space);
        constexpr std::array<int, 8> kSpaceOpsMin = {2, 2, 2, 2, 3, 3, 3, 4};
        cache.space_ops_min = kSpaceOpsMin[static_cast<size_t>(std::min(level, 7))];

        return cache;
    }
};

struct DraftsResult {
    std::vector<CardDraft> drafts;
    AccessibleCache cache;
};

inline void append_single_edge_mode_draft(CardDraft& card, CardId card_id, ActionMode mode) {
    card.modes.push_back(ModeDraft{
        .mode = mode,
        .edges = {ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}}},
    });
}

inline void append_country_target_mode_draft(
    CardDraft& card,
    CardId card_id,
    ActionMode mode,
    std::span<const CountryId> countries
) {
    if (countries.empty()) {
        return;
    }

    ModeDraft mode_draft{.mode = mode, .edges = {}};
    mode_draft.edges.reserve(countries.size());
    for (const auto country : countries) {
        if (!has_country_spec(country)) {
            continue;
        }
        mode_draft.edges.push_back(ActionEncoding{
            .card_id = card_id,
            .mode = mode,
            .targets = {country},
        });
    }
    if (!mode_draft.edges.empty()) {
        card.modes.push_back(std::move(mode_draft));
    }
}

template<typename Predicate>
[[nodiscard]] inline std::vector<CardDraft> collect_event_only_card_drafts(
    const CardSet& hand,
    const PublicState& pub,
    Side side,
    bool holds_china,
    Predicate&& predicate
) {
    std::vector<CardDraft> cards;
    for (const auto card_id : legal_cards(hand, pub, side, holds_china)) {
        if (!predicate(card_id)) {
            continue;
        }
        CardDraft card{.card_id = card_id, .modes = {}};
        append_single_edge_mode_draft(card, card_id, ActionMode::Event);
        cards.push_back(std::move(card));
    }
    return cards;
}

template<typename BuildFn>
[[nodiscard]] inline std::vector<CardDraft> collect_drafts_from_legal_cards(
    const CardSet& hand,
    const PublicState& pub,
    Side side,
    bool holds_china,
    BuildFn&& build_card
) {
    std::vector<CardDraft> cards;
    cards.reserve(10);
    for (const auto card_id : legal_cards(hand, pub, side, holds_china)) {
        if (is_card_blocked_by_defcon(pub, side, card_id)) {
            continue;
        }

        CardDraft card{.card_id = card_id, .modes = {}};
        build_card(card, card_id);
        if (!card.modes.empty()) {
            cards.push_back(std::move(card));
        }
    }
    return cards;
}

// Count how many scoring cards the side holds.
[[nodiscard]] inline int count_scoring_cards(const CardSet& hand) {
    int n = 0;
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (hand.test(card_id) && card_spec(static_cast<CardId>(card_id)).is_scoring) {
            ++n;
        }
    }
    return n;
}

// How many card-play decisions remain for `side` this turn (including the current AR)?
[[nodiscard]] inline int remaining_action_decisions_for_side(const GameState& state, Side side) {
    int max_ar = ars_for_turn(state.pub.turn);
    if (state.pub.space[to_index(side)] >= kSpaceShuttleArs) {
        max_ar = std::max(max_ar, kSpaceShuttleArs);
    }
    if (side == Side::US && state.pub.north_sea_oil_extra_ar) {
        max_ar += 1;
    }
    return std::max(1, max_ar - state.pub.ar + 1);
}

[[nodiscard]] inline bool must_play_scoring_card(const GameState& state, Side side) {
    if (state.pub.ar <= 0) {
        return false;
    }
    const int scoring_cards = count_scoring_cards(state.hands[to_index(side)]);
    const int remaining_decisions = remaining_action_decisions_for_side(state, side);
    return scoring_cards >= remaining_decisions;
}

// Progressive prior boost for scoring cards as their deadline approaches.
// Returns >= 1.0 (1.0 = no boost; 10-1000x as slack shrinks).
[[nodiscard]] inline double scoring_card_prior_multiplier(const GameState& state, Side side, int scoring_cards) {
    if (state.pub.ar <= 0 || scoring_cards <= 0) {
        return 1.0;
    }
    const int remaining = remaining_action_decisions_for_side(state, side);
    const int slack = remaining - scoring_cards;
    if (slack <= 0) {
        return 1.0;  // Already forced in collect_card_drafts; no additional boost needed.
    }
    const int urgency = std::max(1, 4 - std::min(slack, 3));
    return std::pow(10.0, static_cast<double>(urgency));
}


[[nodiscard]] inline double winner_value(std::optional<Side> winner) {
    if (winner == Side::USSR) {
        return 1.0;
    }
    if (winner == Side::US) {
        return -1.0;
    }
    return 0.0;
}

[[nodiscard]] inline double calibrate_value(double raw_value, const MctsConfig& config) {
    if (config.calib_a == 1.0f && config.calib_b == 0.0f) {
        return raw_value;
    }
    const auto logit = static_cast<double>(config.calib_a) * raw_value + static_cast<double>(config.calib_b);
    const auto probability = 1.0 / (1.0 + std::exp(-logit));
    return 2.0 * probability - 1.0;
}

[[nodiscard]] inline bool holds_china_for(const GameState& state, Side side) {
    return side == Side::USSR ? state.ussr_holds_china : state.us_holds_china;
}

inline void sync_china_flags(GameState& state) {
    state.ussr_holds_china = state.pub.china_held_by == Side::USSR;
    state.us_holds_china = state.pub.china_held_by == Side::US;
}

/// Compute softmax in-place over buf[0..n), writing probabilities back into buf.
inline void softmax_inplace(float* buf, int n) {
    float max_val = -std::numeric_limits<float>::infinity();
    for (int i = 0; i < n; ++i) {
        if (buf[i] > max_val) max_val = buf[i];
    }
    float sum = 0.0f;
    for (int i = 0; i < n; ++i) {
        buf[i] = std::exp(buf[i] - max_val);
        sum += buf[i];
    }
    if (sum > 0.0f) {
        const float inv_sum = 1.0f / sum;
        for (int i = 0; i < n; ++i) {
            buf[i] *= inv_sum;
        }
    }
}

[[nodiscard]] inline std::vector<CountryId> accessible_countries_filtered(
    const PublicState& pub,
    Side side,
    CardId card_id,
    ActionMode mode
) {
    auto accessible = legal_countries(card_id, mode, pub, side);
    accessible.erase(
        std::remove_if(accessible.begin(), accessible.end(), [](CountryId cid) { return !has_country_spec(cid); }),
        accessible.end()
    );
    return accessible;
}

[[nodiscard, maybe_unused]] inline double rollout_value(const GameState& state, const MctsConfig& config, Pcg64Rng& rng) {
    (void)config.rollout_depth_limit;
    const PolicyFn heuristic = [](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& local_rng) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, local_rng);
    };
    const auto result = play_game_from_mid_state_fn(state, heuristic, heuristic, rng.next_u32());
    return winner_value(result.winner);
}

// evaluate_leaf_value_raw: used by mcts_batched.cpp and ismcts.cpp (float-pointer value tensors).
// Note: mcts.cpp uses a different signature (GenericDict outputs) — not deduplicated here.
[[nodiscard, maybe_unused]] inline double evaluate_leaf_value_raw(
    const GameState& state,
    const float* value_ptr,
    int value_stride,
    int batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto value = static_cast<double>(value_ptr[batch_index * value_stride]);
    // Model outputs actor-relative value; convert to USSR-perspective for backup.
    if (state.pub.phasing == Side::US) {
        value = -value;
    }
    value = calibrate_value(value, config);
    if (!config.use_rollout_backup) {
        return value;
    }
    const auto rollout = rollout_value(state, config, rng);
    return static_cast<double>(config.value_weight) * value +
        static_cast<double>(1.0f - config.value_weight) * rollout;
}

}  // namespace
}  // namespace ts
