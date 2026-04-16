#pragma once

#include "scoring.hpp"
#include "types.hpp"

namespace ts::experimental {

double evaluate_public_state_ussr(const PublicState& pub, const HeuristicConfig& config);
double evaluate_state_for_side(const GameState& gs, Side side, const HeuristicConfig& config);
double evaluate_terminal_for_side(std::optional<Side> winner, Side side, const HeuristicConfig& config);

}  // namespace ts::experimental

