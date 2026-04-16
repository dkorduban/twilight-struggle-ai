#pragma once

#include "game_state.hpp"

#include "types.hpp"

namespace ts::experimental {

std::vector<ActionProposal> enumerate_action_proposals(
    const GameState& gs,
    Side side,
    const HeuristicConfig& config
);

std::vector<ActionEncoding> enumerate_candidate_actions(
    const GameState& gs,
    Side side,
    const HeuristicConfig& config
);

PlannedAction plan_specific_action(
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config,
    const ActionEncoding& action
);

PlannedAction choose_greedy_action_plan(
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config
);

PlannedAction choose_search_action_plan(
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config
);

}  // namespace ts::experimental
