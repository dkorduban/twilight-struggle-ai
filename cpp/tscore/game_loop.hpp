// Native whole-game orchestration: headline resolution, action rounds, extra
// rounds, end-of-turn handling, and traced play helpers.

#pragma once

#include <array>
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
    Pcg64Rng&
)>;

// One traced decision point plus the pre-action public state that produced it.
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

// Public wrappers used by tools and bindings so they can drive the native loop
// without duplicating phase logic.
std::tuple<PublicState, bool, std::optional<Side>> apply_action_live(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng
);

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_trap_ar_live(
    GameState& gs,
    Side side,
    Pcg64Rng& rng
);

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_norad_live(
    GameState& gs,
    Pcg64Rng& rng
);

std::optional<GameResult> run_extra_action_round_live(
    GameState& gs,
    Side side,
    const PolicyFn& policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps = nullptr
);

std::optional<GameResult> run_headline_phase_live(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps = nullptr
);

std::optional<GameResult> run_action_rounds_live(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    int total_ars,
    std::vector<StepTrace>* trace_steps = nullptr
);

GameResult play_game_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt
);

GameResult play_game_from_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt
);

// Like play_game_from_state_fn but continues from gs.pub.turn rather than
// replaying from turn 1.  Used for mid-game rollouts (e.g. MCTS leaf eval).
GameResult play_game_from_mid_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt
);

TracedGame play_game_traced_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt
);

TracedGame play_game_traced_from_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt
);

TracedGame play_game_traced_from_seed_words_fn(
    std::array<uint64_t, 4> words,
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
