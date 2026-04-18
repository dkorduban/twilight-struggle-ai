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
    int top_k_actions = 0;                // Keep only top-K edges by prior after expansion.
                                           // 0 = keep all (default). Typical: 20-50.
    float pw_c = 0.0f;                    // Progressive widening constant. 0 = disabled.
                                           // Active children = min(n_edges, max(1,
                                           // ceil(pw_c * n^pw_alpha))).
    float pw_alpha = 0.5f;                // Progressive widening exponent.
                                           // 0.5 = sqrt, 0.33 = cbrt.
    float prior_t_card = 1.0f;            // Temperature for card logits before softmax.
    float prior_t_mode = 1.0f;            // Temperature for mode logits before softmax.
    float prior_t_country = 1.0f;         // Temperature for country logits before softmax.
                                           // T<1 sharpens, T>1 flattens. 1.0 = no change.
    bool verbose_tree_stats = false;      // When true, collect per-node edge utilization
                                           // histogram (requires tree walk — adds ~1% overhead).
    bool record_rows = true;              // When false, skip per-step trace/search recording
                                           // and JSONL emission (benchmark mode).
};

struct RolloutStep {
    torch::Tensor influence;     // (172,) float32 on CPU
    torch::Tensor cards;         // (448,) float32 on CPU
    torch::Tensor scalars;       // (11,) float32 on CPU

    torch::Tensor card_mask;     // (111,) bool
    torch::Tensor mode_mask;     // (5,) bool
    torch::Tensor country_mask;  // (86,) bool; all-false for EVENT/SPACE

    int card_idx = -1;           // 0-indexed (card_id - 1)
    int mode_idx = -1;           // 0-4
    std::vector<int> country_targets;

    float log_prob = 0.0f;
    float value = 0.0f;

    int side_int = 0;            // 0=USSR, 1=US
    int game_index = -1;         // 0-based game index

    // Raw game state for future re-encoding (added 2026-04-07).
    // Stored alongside the NN features so rollouts can be re-encoded with
    // future feature representations without replaying games.
    //
    // Influence: pub.influence[side][country_id] for country_id in 0..85.
    // InfluenceBlock is int16_t so we store as int16_t directly.
    std::array<int16_t, 86> raw_ussr_influence = {};  // pub.influence[0][c]
    std::array<int16_t, 86> raw_us_influence = {};    // pub.influence[1][c]

    // Scalar game state at the time the action was taken.
    int raw_turn = 0;     // 1-10
    int raw_ar = 0;       // 0-8
    int raw_defcon = 5;   // 1-5
    int raw_vp = 0;       // negative = USSR ahead, positive = US ahead
    std::array<int, 2> raw_milops = {0, 0};  // [USSR, US]
    std::array<int, 2> raw_space = {0, 0};   // [USSR, US]

    // Card IDs (1-indexed) in the deciding side's known_in_hand bitset.
    std::vector<int> hand_card_ids;

    // SmallChoice event decision captured by PolicyCallback during commit_greedy_action.
    // -1 means no small_choice decision occurred for this step.
    int small_choice_target = -1;
    int small_choice_n_options = 0;  // number of legal options (0 if no decision)
    float small_choice_logprob = 0.0f;  // log-prob of the chosen option under the policy
};

struct RolloutResult {
    std::vector<GameResult> results;   // one per game, ordered by game index
    std::vector<RolloutStep> steps;    // flat, grouped by game index
    std::vector<int> game_boundaries;  // first step offset for each game
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

RolloutResult rollout_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int pool_size,
    uint32_t base_seed,
    torch::Device device = torch::kCPU,
    float temperature = 1.0f,
    bool nash_temperatures = true,
    float dir_alpha = 0.0f,
    float dir_epsilon = 0.0f
);

RolloutResult rollout_self_play_batched(
    int n_games,
    torch::jit::script::Module& model,
    int pool_size,
    uint32_t base_seed,
    torch::Device device = torch::kCPU,
    float temperature = 1.0f,
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

/// Run model-vs-model benchmark using batched greedy (argmax) inference.
/// Half the games assign model_a=USSR, model_b=US; the other half swap.
/// Both models use argmax action selection (no heuristic, no tree search).
/// Returns one GameResult per game ordered as: first n_games/2 with model_a=USSR,
/// then n_games/2 with model_a=US.
std::vector<GameResult> benchmark_model_vs_model_batched(
    int n_games,
    torch::jit::script::Module& model_a,
    torch::jit::script::Module& model_b,
    int pool_size,
    uint32_t base_seed,
    torch::Device device = torch::kCPU,
    float temperature = 0.0f,
    bool nash_temperatures = false
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
    int top_k_actions = 0,
    float pw_c = 0.0f,
    float pw_alpha = 0.5f,
    float prior_t_card = 1.0f,
    float prior_t_mode = 1.0f,
    float prior_t_country = 1.0f
);

/// Run model_a (learning model, steps recorded) vs model_b (opponent, no steps).
/// learned_side=Neutral (default): alternating — [0, half) model_a=USSR, [half, n_games) model_a=US.
/// learned_side=USSR: all n_games with model_a as USSR.
/// learned_side=US:   all n_games with model_a as US.
/// Returns RolloutResult with steps only for model_a decisions.
RolloutResult rollout_model_vs_model_batched(
    int n_games,
    torch::jit::script::Module& model_a,
    torch::jit::script::Module& model_b,
    int pool_size,
    uint32_t base_seed,
    torch::Device device = torch::kCPU,
    float temperature = 1.0f,
    bool nash_temperatures = false,
    float dir_alpha = 0.0f,
    float dir_epsilon = 0.0f,
    Side learned_side = Side::Neutral
);

}  // namespace ts

#endif
