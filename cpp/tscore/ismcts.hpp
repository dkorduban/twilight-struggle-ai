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
    int max_pending_per_det = 8;  // concurrent leaves per determinization (virtual loss)
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

/// Run benchmark games where the learned side uses ISMCTS for each decision.
/// The opponent uses the heuristic policy.  Returns one GameResult per game.
std::vector<GameResult> play_ismcts_matchup(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    const IsmctsConfig& config,
    uint32_t base_seed
);

std::vector<GameResult> play_ismcts_matchup_pooled(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    const IsmctsConfig& config,
    int pool_size,
    uint32_t base_seed,
    torch::Device device
);

#endif

}  // namespace ts
