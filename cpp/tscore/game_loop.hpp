// Native whole-game orchestration: headline resolution, action rounds, extra
// rounds, end-of-turn handling, and traced play helpers.

#pragma once

#include <array>
#include <functional>
#include <optional>
#include <vector>

#include "decision_frame.hpp"
#include "game_state.hpp"
#include "policies.hpp"
#include "policy_callback.hpp"

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
    // Full hidden state snapshot at decision time (for teacher search).
    CardSet opp_hand_snapshot;
    InlineDeck deck_snapshot;
    bool ussr_holds_china_snapshot = false;
    bool us_holds_china_snapshot = false;
};

struct TracedGame {
    std::vector<StepTrace> steps;
    GameResult result;
};

struct GameLoopConfig {
    float exploration_rate = 0.0f;
    bool skip_setup_influence = false;  // if true, skip §3.0 free influence placement
    int us_bid_extra = 0;  // extra influence for US in setup (competitive bid, typically +2)
    bool use_atomic_setup = false;  // if true, place setup influence atomically from opening tables
                                     // (no per-point policy callbacks, matching batched path RNG)
};

// Inspect the next pending sub-decision. Returns nullopt if no sub-frame is
// pending and the game loop needs a top-level AR action.
std::optional<DecisionFrame> engine_peek(const GameState& gs);

// Apply a top-level action. Slice 1 preserves the current live-loop behavior
// and ignores sub_policy until sub-frame producers are wired in.
StepResult engine_step_toplevel(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const SubframePolicyFn& sub_policy = {}
);

// Apply a queued sub-frame action. Slice 2 wiring is not active yet, so this is
// a no-op when no frames are pending.
StepResult engine_step_subframe(
    GameState& gs,
    const FrameAction& action,
    Pcg64Rng& rng
);

// Public wrappers used by tools and bindings so they can drive the native loop
// without duplicating phase logic.
std::tuple<PublicState, bool, std::optional<Side>> apply_action_live(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr,
    bool log_real_move = false,  // TS_ACTION_LOG env enables stderr trace for real (non-search) moves only
    std::vector<DecisionFrame>* frame_log = nullptr
);

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_trap_ar_live(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_cuban_missile_crisis_cancel_live(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_norad_live(
    GameState& gs,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

void resolve_glasnost_free_ops_live(
    PublicState& pub,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

std::optional<GameResult> run_extra_action_round_live(
    GameState& gs,
    Side side,
    const PolicyFn& policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps = nullptr,
    const GameLoopConfig& config = {}
);

std::optional<GameResult> run_headline_phase_live(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps = nullptr,
    const GameLoopConfig& config = {}
);

std::optional<GameResult> run_action_rounds_live(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    int total_ars,
    std::vector<StepTrace>* trace_steps = nullptr,
    const GameLoopConfig& config = {}
);

/// Like play_game_traced_from_state_with_rng but takes GameState by reference.
/// Use when the PolicyFn needs access to the same GameState being played
/// (e.g. ISMCTS which reads opponent hand size and deck from the full state).
TracedGame play_game_traced_from_state_ref_with_rng(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    const GameLoopConfig& config = {}
);

GameResult play_game_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

GameResult play_game_from_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

// Like play_game_from_state_fn but continues from gs.pub.turn rather than
// replaying from turn 1.  Used for mid-game rollouts (e.g. MCTS leaf eval).
GameResult play_game_from_mid_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

TracedGame play_game_traced_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

TracedGame play_game_traced_from_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

TracedGame play_game_traced_from_seed_words_fn(
    std::array<uint64_t, 4> words,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

GameResult play_game(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

GameResult play_random_game(
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

std::vector<GameResult> play_matchup(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    int game_count,
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

std::vector<GameResult> play_matchup_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    int game_count,
    std::optional<uint32_t> seed = std::nullopt,
    const GameLoopConfig& config = {}
);

MatchSummary summarize_results(std::span<const GameResult> results);

}  // namespace ts
