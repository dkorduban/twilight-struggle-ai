#pragma once

#include <optional>
#include <vector>

#include "game_state.hpp"
#include "policies.hpp"

namespace ts {

GameResult play_game(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    std::optional<uint32_t> seed = std::nullopt
);

GameResult play_random_game(std::optional<uint32_t> seed = std::nullopt);

std::vector<GameResult> play_matchup(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    int game_count,
    std::optional<uint32_t> seed = std::nullopt
);

}  // namespace ts
