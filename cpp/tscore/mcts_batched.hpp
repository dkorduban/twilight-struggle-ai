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

struct GameSlot {
    GameState root_state;
    GameState sim_state;
    std::unique_ptr<MctsNode> root;
    std::vector<std::pair<MctsNode*, int>> path;
    int sims_completed = 0;
    int sims_target = 0;
    bool pending_expansion = false;
    bool pending_root_expansion = false;
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
};

struct BatchedMctsConfig {
    MctsConfig mcts;
    int pool_size = 32;
    int virtual_loss_weight = 3;
    float temperature = 0.0f;
    float epsilon_greedy = 0.0f;
};

void collect_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    const BatchedMctsConfig& config,
    uint32_t base_seed,
    std::ostream& out_stream
);

}  // namespace ts

#endif
