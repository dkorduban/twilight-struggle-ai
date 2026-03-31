#pragma once

#include <functional>
#include <optional>
#include <vector>

#include "game_state.hpp"
#include "policies.hpp"

namespace ts {

using PolicyFn = std::function<std::optional<ActionEncoding>(
    const PublicState&,
    const CardSet&,
    bool,
    std::mt19937&
)>;

struct StepTrace {
    int turn = 0;
    int ar = 0;
    Side side = Side::USSR;
    bool holds_china = false;
    PublicState pub_snapshot;
    CardSet hand_snapshot;
    ActionEncoding action;
    int vp_before = 0;
    int vp_after = 0;
    int defcon_before = 0;
    int defcon_after = 0;
};

struct TracedGame {
    std::vector<StepTrace> steps;
    GameResult result;
};

std::tuple<PublicState, bool, std::optional<Side>> apply_action_live(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    std::mt19937& rng
);

GameResult play_game_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt
);

TracedGame play_game_traced_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt
);

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

std::vector<GameResult> play_matchup_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    int game_count,
    std::optional<uint32_t> seed = std::nullopt
);

MatchSummary summarize_results(std::span<const GameResult> results);

}  // namespace ts
