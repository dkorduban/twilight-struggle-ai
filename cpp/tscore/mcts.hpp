// Native PUCT MCTS data structures and search entrypoint.

#pragma once

#include <memory>
#include <vector>

#include "game_state.hpp"
#include "legal_actions.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)
#include <torch/script.h>
#endif

namespace ts {

struct MctsEdge {
    ActionEncoding action;
    float prior = 0.0f;
    int visit_count = 0;
    int virtual_loss = 0;
    double total_value = 0.0;

    [[nodiscard]] double mean_value() const {
        return visit_count > 0 ? total_value / static_cast<double>(visit_count) : 0.0;
    }
};

struct MctsNode {
    std::vector<MctsEdge> edges;
    std::vector<std::unique_ptr<MctsNode>> children;
    std::vector<ActionEncoding> applied_actions;
    int total_visits = 0;
    bool is_terminal = false;
    double terminal_value = 0.0;
    Side side_to_move = Side::USSR;

    [[nodiscard]] int select_edge(float c_puct) const;
};

struct MctsConfig {
    int n_simulations = 200;
    float c_puct = 1.5f;
    float dir_alpha = 0.2f;
    float dir_epsilon = 0.25f;
    float value_weight = 1.0f;
    float calib_a = 1.0f;
    float calib_b = 0.0f;
    bool use_rollout_backup = false;
    int rollout_depth_limit = 0;
};

struct SearchResult {
    ActionEncoding best_action;
    std::vector<MctsEdge> root_edges;
    double root_value = 0.0;
    int total_simulations = 0;
};

#if defined(TS_BUILD_TORCH_RUNTIME)
SearchResult mcts_search(
    const GameState& root_state,
    torch::jit::script::Module& model,
    const MctsConfig& config,
    Pcg64Rng& rng
);
#endif

// Exposed for use in batched MCTS path and tests.
void apply_root_dirichlet_noise(MctsNode& root, const MctsConfig& config, Pcg64Rng& rng);

}  // namespace ts
