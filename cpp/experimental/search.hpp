#pragma once

#include "types.hpp"

namespace ts::experimental {

PlannedAction choose_ismcts_action_plan(
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config
);

}  // namespace ts::experimental
