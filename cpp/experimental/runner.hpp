#pragma once

#include "types.hpp"

namespace ts::experimental {

enum class ExperimentalAgentKind : uint8_t {
    Search = 0,
    MinimalHybrid = 1,
    LearnedModel = 2,
};

struct ExperimentalAgentSpec {
    ExperimentalAgentKind kind = ExperimentalAgentKind::Search;
    std::string model_path;
};

ExperimentalTrace play_selfplay_game(
    std::optional<uint32_t> seed,
    const HeuristicConfig& config = {}
);

ExperimentalTrace play_matchup_game(
    const ExperimentalAgentSpec& ussr_agent,
    const ExperimentalAgentSpec& us_agent,
    std::optional<uint32_t> seed,
    const HeuristicConfig& config = {}
);

std::vector<GameResult> play_matchup_games(
    const ExperimentalAgentSpec& ussr_agent,
    const ExperimentalAgentSpec& us_agent,
    int game_count,
    std::optional<uint32_t> seed,
    const HeuristicConfig& config = {},
    int thread_count = 1
);

ExperimentalTrace play_search_vs_search_from_state(
    GameState gs,
    std::optional<uint32_t> seed,
    const HeuristicConfig& config = {}
);

}  // namespace ts::experimental
