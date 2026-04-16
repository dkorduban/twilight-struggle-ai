#pragma once

#include <string_view>

#include "types.hpp"

namespace ts::experimental {

CallbackScript solve_callback_script(
    const GameState& root_state,
    Side root_side,
    const ResolutionFn& resolution_fn,
    Pcg64Rng root_rng,
    Side evaluation_side,
    const HeuristicConfig& config,
    std::string_view label = {}
);

PolicyCallbackFn make_replay_callback(const CallbackScript& script);

}  // namespace ts::experimental
