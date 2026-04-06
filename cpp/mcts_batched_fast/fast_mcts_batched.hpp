// Standalone single-thread batched MCTS benchmark replica.

#pragma once

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <cstdint>
#include <optional>

#include <torch/script.h>
#include <torch/torch.h>

#include "mcts.hpp"

namespace ts::fastmcts {

struct BenchConfig {
    MctsConfig mcts;
    int pool_size = 32;
    int max_pending = 8;
    int virtual_loss_weight = 3;
    int cache_visit_threshold = 0;
    float temperature = 0.0f;
    float epsilon_greedy = 0.0f;
    std::optional<Side> learned_side;
    bool greedy_nn_opponent = false;
    bool use_forward_worker = false;
};

struct BenchResult {
    int n_games = 0;
    int pool_size = 0;
    int n_simulations = 0;
    int64_t total_simulations = 0;
    int64_t mcts_decisions = 0;
    int64_t n_batches = 0;
    int64_t total_batch_items = 0;
    int wins = 0;
    int losses = 0;
    int draws = 0;
    double elapsed_s = 0.0;
    double sims_per_s = 0.0;
    double avg_batch = 0.0;
    double t_advance = 0.0;
    double t_select = 0.0;
    double t_nn = 0.0;
    double t_expand = 0.0;
    double t_commit = 0.0;
};

BenchResult benchmark_mcts_fast(
    int n_games,
    torch::jit::script::Module& model,
    const BenchConfig& config,
    uint32_t base_seed,
    torch::Device device = torch::kCPU
);

}  // namespace ts::fastmcts

#endif
