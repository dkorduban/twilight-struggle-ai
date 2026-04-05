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

struct PendingExpansion {
    std::vector<std::pair<MctsNode*, int>> path;
    GameState sim_state;
    bool is_root_expansion = false;
};

struct GameSlot {
    GameState root_state;
    std::unique_ptr<MctsNode> root;
    std::vector<PendingExpansion> pending;
    int sims_completed = 0;
    int sims_target = 0;
    bool move_done = false;
    bool game_done = false;
    bool emitted = false;
    bool active = false;
    Pcg64Rng rng;

    std::string game_id;
    std::vector<StepTrace> traces;
    std::vector<SearchResult> search_results;
    GameResult result;

    BatchedGameStage stage = BatchedGameStage::TurnSetup;
    int turn = 1;
    int total_ars = 0;
    int current_ar = 0;
    int decisions_started = 0;
    Side current_side = Side::USSR;
    std::array<std::optional<PendingHeadlineChoice>, 2> pending_headlines = {};
    std::vector<PendingHeadlineChoice> headline_order;
    size_t headline_order_index = 0;
    std::optional<PendingDecision> decision;
    // Saved RNG state before MCTS search starts, used in heuristic_teacher_mode to
    // restore the game RNG so heuristic move selection is identical to pure heuristic.
    std::optional<Pcg64Rng> rng_before_mcts;
    // Per-game heuristic temperature (0 = deterministic argmax).
    float heuristic_temperature = 0.0f;
};

struct BatchedMctsConfig {
    MctsConfig mcts;
    int pool_size = 32;
    int virtual_loss_weight = 3;
    int max_pending = 32;  // max concurrent leaves per game slot
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
    bool nash_temperatures = true
);

}  // namespace ts

#endif
