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
    MctsConfig mcts_config = []() {
        MctsConfig cfg;
        cfg.dir_alpha = 0.0f;
        cfg.dir_epsilon = 0.0f;
        return cfg;
    }();
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
    const Observation& obs,
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

/// Like play_ismcts_matchup_pooled but the opponent uses a neural network model
/// (greedy argmax) instead of the heuristic policy.
std::vector<GameResult> play_ismcts_vs_model_pooled(
    int n_games,
    torch::jit::script::Module& search_model,
    torch::jit::script::Module& opponent_model,
    Side search_side,
    const IsmctsConfig& config,
    int pool_size,
    uint32_t base_seed,
    torch::Device device
);

#endif

}  // namespace ts
