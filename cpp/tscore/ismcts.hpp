// Determinized information-set MCTS built on top of the native full-state MCTS.

#pragma once

#include <vector>

#include "mcts.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)
#include <torch/script.h>
#endif

namespace ts {

#if defined(TS_BUILD_TORCH_RUNTIME)

struct IsmctsConfig {
    int n_determinizations = 8;
    MctsConfig mcts_config;
};

struct IsmctsResult {
    ActionEncoding best_action;
    std::vector<MctsEdge> aggregated_edges;
    double mean_root_value = 0.0;
    int total_determinizations = 0;
};

GameState sample_determinization(
    const GameState& gs,
    Side acting_side,
    int opp_hand_size,
    Pcg64Rng& rng
);

IsmctsResult ismcts_search(
    const GameState& partial_state,
    Side acting_side,
    int opp_hand_size,
    torch::jit::script::Module& model,
    const IsmctsConfig& config,
    Pcg64Rng& rng
);

#endif

}  // namespace ts
