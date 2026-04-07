// Wavefront-batched MCTS collection across a pool of concurrent games.

#pragma once

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <array>
#include <cstdint>
#include <memory>
#include <optional>
#include <ostream>
#include <string>
#include <vector>

#include <torch/torch.h>

#include "game_loop.hpp"
#include "mcts.hpp"

namespace ts {

enum class BatchedGameStage : uint8_t {
    TurnSetup = 0,
    HeadlineChoiceUSSR = 1,
    HeadlineChoiceUS = 2,
    HeadlineResolve = 3,
    ActionRound = 4,
    ExtraActionRoundUS = 5,
    ExtraActionRoundUSSR = 6,
    Cleanup = 7,
    Finished = 8,
};

struct PendingDecision {
    int turn = 0;
    int ar = 0;
    int move_number = 0;
    Side side = Side::USSR;
    bool holds_china = false;
    bool is_headline = false;
    PublicState pub_snapshot;
    CardSet hand_snapshot;
};

struct PendingHeadlineChoice {
    Side side = Side::USSR;
    bool holds_china = false;
    CardSet hand_snapshot;
    ActionEncoding action;
    SearchResult search;
};


struct BatchedMctsConfig {
    MctsConfig mcts;
    int pool_size = 32;
    int virtual_loss_weight = 3;
    int max_pending = 32;  // max concurrent leaves per game slot
    int n_mcts_threads = 0;  // 0 = auto (min(pool_size, hw_concurrency))
    int torch_intra_threads = 0;  // 0 = auto/default runtime behavior
    int torch_interop_threads = 0;  // 0 = auto/default
    float temperature = 0.0f;
    float epsilon_greedy = 0.0f;
    // When set, only this side uses MCTS search; the other uses heuristic
    // (or greedy NN if greedy_nn_opponent is true).
    // When nullopt, both sides use MCTS (self-play).
    std::optional<Side> learned_side;
    bool greedy_nn_opponent = false;  // opponent uses NN argmax instead of heuristic
    // When true, both sides play MinimalHybrid (heuristic) but MCTS is also run at
    // each decision to record visit count distributions as teacher targets.
    // Game trajectories are bit-identical to pure heuristic (same seed) because the
    // game RNG is saved before MCTS and restored before heuristic move selection.
    bool heuristic_teacher_mode = false;
    // Prefix used in game_id construction: "<prefix>_<seed>_<index>".
    // Default "mcts". Set to "selfplay" in heuristic_teacher_mode so produced
    // game_ids match existing heuristic dataset rows for teacher target joining.
    std::string game_id_prefix = "mcts";
    // When true, the heuristic opponent samples per-game Boltzmann temperatures
    // from the Nash equilibrium mixed strategy (matching training data).
    bool nash_temperatures = false;
    // Device for NN inference (CPU or CUDA). Batch inputs are allocated on CPU
    // and transferred to this device before forward, then outputs moved back.
    torch::Device device = torch::kCPU;

    // K-sample influence allocation knobs.
    // T_s=0, T_c=0, K=1 → bit-identical to current behavior (guard skips new path).
    float influence_t_strategy = 0.0f;    // Temperature for strategy selection.
                                           // 0 = argmax (current). >0 = sample.
    float influence_t_country = 0.0f;     // Temperature for country sampling.
                                           // 0 = proportional rounding (current).
                                           // >0 = multinomial sample.
    bool influence_proportional_first = true;
                                           // First allocation per strategy uses
                                           // deterministic proportional when K>1.
    int influence_samples = 1;            // K: number of influence edges per (card, Influence).
                                           // 1 = single edge (current). >1 = K diverse edges.
    float min_prior_threshold = 0.0f;     // After expansion, drop edges with prior < threshold
                                           // and renormalize. 0 = keep all edges (default).
                                           // Typical values: 0.001–0.01 to reduce tree width.
    float prior_t_card = 1.0f;            // Temperature for card logits before softmax.
    float prior_t_mode = 1.0f;            // Temperature for mode logits before softmax.
    float prior_t_country = 1.0f;         // Temperature for country logits before softmax.
                                           // T<1 sharpens, T>1 flattens. 1.0 = no change.
    bool verbose_tree_stats = false;      // When true, collect per-node edge utilization
                                           // histogram (requires tree walk — adds ~1% overhead).
    bool record_rows = true;              // When false, skip per-step trace/search recording
                                           // and JSONL emission (benchmark mode).
};

void collect_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    const BatchedMctsConfig& config,
    uint32_t base_seed,
    std::ostream& out_stream,
    std::vector<GameResult>* out_results = nullptr
);

/// Run benchmark games using batched greedy inference for one side.
/// The learned side uses argmax from the batched NN outputs; the opponent
/// uses the heuristic policy (or greedy NN if greedy_opponent=true).
/// Returns one GameResult per game.
std::vector<GameResult> benchmark_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int pool_size,
    uint32_t base_seed,
    torch::Device device = torch::kCPU,
    bool greedy_opponent = false,
    float temperature = 0.0f,
    bool nash_temperatures = true
);

/// Run MCTS (learned side) vs greedy NN (opponent) benchmark.
/// Returns one GameResult per game.
std::vector<GameResult> benchmark_mcts_vs_greedy(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int n_simulations,
    int pool_size,
    uint32_t base_seed,
    torch::Device device = torch::kCPU
);

/// Run MCTS benchmark. Opponent is heuristic (default) or greedy NN.
std::vector<GameResult> benchmark_mcts(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int n_simulations,
    int pool_size,
    uint32_t base_seed,
    torch::Device device = torch::kCPU,
    bool greedy_nn_opponent = false,
    bool nash_temperatures = true,
    int n_mcts_threads = 0,
    int torch_intra_threads = 0,
    int torch_interop_threads = 0,
    int influence_samples = 1,
    float influence_t_strategy = 0.0f,
    float influence_t_country = 0.0f,
    bool influence_proportional_first = true,
    float min_prior_threshold = 0.0f,
    float prior_t_card = 1.0f,
    float prior_t_mode = 1.0f,
    float prior_t_country = 1.0f
);

}  // namespace ts

#endif
