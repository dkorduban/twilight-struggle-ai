// Shared helpers for MCTS, ISMCTS, and batched search implementations.
// Include from search .cpp files only.

#pragma once

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <optional>
#include <vector>

#include "card_properties.hpp"
#include "game_data.hpp"
#include "game_loop.hpp"
#include "game_state.hpp"
#include "mcts.hpp"
#include "policies.hpp"

namespace ts {
namespace {

inline constexpr double kVirtualLossPenalty = 1.0;

// AR count at which the Space Shuttle gives an extra action round.
inline constexpr int kSpaceShuttleArs = 8;

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
