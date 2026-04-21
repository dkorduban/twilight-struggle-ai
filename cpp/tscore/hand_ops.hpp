// Hand-aware live-engine helpers layered above the public-state step engine.

#pragma once

#include <optional>
#include <tuple>
#include <vector>

#include "decision_frame.hpp"
#include "game_state.hpp"
#include "policy_callback.hpp"

namespace ts {

bool apply_frame_ops_impl(
    GameState& gs,
    std::vector<DecisionFrame>* frame_log,
    CardId card_id,
    Side side,
    int ops,
    Pcg64Rng& rng
);

std::tuple<PublicState, bool, std::optional<Side>> apply_action_with_hands(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr,
    std::vector<DecisionFrame>* frame_log = nullptr
);

std::tuple<PublicState, bool, std::optional<Side>> apply_headline_event_with_hands(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr,
    std::vector<DecisionFrame>* frame_log = nullptr
);

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_trap_ar(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr,
    std::vector<DecisionFrame>* frame_log = nullptr
);

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_cuban_missile_crisis_cancel(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr,
    std::vector<DecisionFrame>* frame_log = nullptr
);

}  // namespace ts
