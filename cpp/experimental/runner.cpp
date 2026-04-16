#include "runner.hpp"

#include <chrono>
#include <algorithm>
#include <atomic>
#include <cctype>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <memory>
#include <sstream>
#include <stdexcept>
#include <string_view>
#include <thread>

#include "callback_script.hpp"
#include "game_data.hpp"
#include "learned_policy.hpp"
#include "hand_ops.hpp"
#include "human_openings.hpp"
#include "logging.hpp"
#include "planner.hpp"
#include "policies.hpp"
#include "profile.hpp"
#include "rule_queries.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts::experimental {
namespace {

constexpr int kSpaceShuttleArs = 8;
constexpr double kSlowRuntimeLogMs = 100.0;

bool slow_runtime_logging_enabled() {
    static const bool enabled = [] {
        const char* value = std::getenv("TS_EXP_LOG_SLOW_RUNTIME");
        return value != nullptr && value[0] != '\0' && value[0] != '0';
    }();
    return enabled;
}

struct SearchProfileTarget {
    int turn = 0;
    int ar = 0;
    Side side = Side::USSR;
};

std::optional<SearchProfileTarget> configured_search_profile_target() {
    static const std::optional<SearchProfileTarget> target = []() -> std::optional<SearchProfileTarget> {
        const char* value = std::getenv("TS_EXP_PROFILE_SEARCH_AT");
        if (value == nullptr || value[0] == '\0') {
            return std::nullopt;
        }
        std::istringstream in(value);
        std::string turn_token;
        std::string ar_token;
        std::string side_token;
        if (!std::getline(in, turn_token, ':') || !std::getline(in, ar_token, ':') || !std::getline(in, side_token, ':')) {
            return std::nullopt;
        }
        SearchProfileTarget parsed;
        parsed.turn = std::stoi(turn_token);
        parsed.ar = std::stoi(ar_token);
        std::transform(side_token.begin(), side_token.end(), side_token.begin(), [](unsigned char ch) {
            return static_cast<char>(std::toupper(ch));
        });
        parsed.side = (side_token == "US") ? Side::US : Side::USSR;
        return parsed;
    }();
    return target;
}

bool exit_after_profiled_search() {
    static const bool enabled = [] {
        const char* value = std::getenv("TS_EXP_EXIT_AFTER_PROFILE_SEARCH");
        return value != nullptr && value[0] != '\0' && value[0] != '0';
    }();
    return enabled;
}

void log_slow_runtime(
    std::string_view stage,
    const GameState& gs,
    Side side,
    double elapsed_ms,
    std::string_view extra = {}
) {
    if (!slow_runtime_logging_enabled() || elapsed_ms < kSlowRuntimeLogMs) {
        return;
    }
    std::ostringstream line;
    line << logging::prefix(__FILE__, __LINE__)
         << "slow_runtime"
         << " stage=" << stage
         << " turn=" << gs.pub.turn
         << " ar=" << gs.pub.ar
         << " side=" << (side == Side::USSR ? "USSR" : "US")
         << " elapsed_ms=" << elapsed_ms;
    if (!extra.empty()) {
        line << " " << extra;
    }
    std::cerr << line.str() << std::endl;
}

void log_runtime_stage_start(
    std::string_view stage,
    const GameState& gs,
    Side side
) {
    if (!slow_runtime_logging_enabled()) {
        return;
    }
    std::ostringstream line;
    line << logging::prefix(__FILE__, __LINE__)
         << "runtime_stage_start"
         << " stage=" << stage
         << " turn=" << gs.pub.turn
         << " ar=" << gs.pub.ar
         << " side=" << (side == Side::USSR ? "USSR" : "US");
    std::cerr << line.str() << std::endl;
}

ExperimentalTrace play_matchup_from_state_internal(
    GameState gs,
    const ExperimentalAgentSpec& ussr_agent,
    const ExperimentalAgentSpec& us_agent,
    std::optional<uint32_t> seed,
    const HeuristicConfig& config
);

void sync_china(GameState& gs) {
    gs.ussr_holds_china = gs.pub.china_held_by == Side::USSR;
    gs.us_holds_china = gs.pub.china_held_by == Side::US;
}

bool holds_china_for(const GameState& gs, Side side) {
    return side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
}

std::string infer_terminal_cause(
    const PublicState& pub,
    std::optional<Side> winner,
    CardId card_id = 0
) {
    if (pub.defcon <= 1) {
        return "defcon1";
    }
    if (card_id == kWargamesCardId) {
        return "wargames";
    }
    if (winner.has_value()) {
        return std::abs(pub.vp) >= 20 ? "vp" : "europe_control";
    }
    return "vp";
}

PlannedAction choose_headline_fallback(
    const GameState& gs,
    Side side
) {
    PlannedAction best;
    double best_score = -std::numeric_limits<double>::infinity();
    for (const auto card_id : legal_cards(gs.hands[to_index(side)], gs.pub, side, holds_china_for(gs, side))) {
        if (card_id == kChinaCardId) {
            continue;
        }
        double score = 0.2 * static_cast<double>(card_spec(card_id).ops);
        const auto& spec = card_spec(card_id);
        if (spec.is_scoring) {
            const auto scoring = apply_scoring_card(card_id, gs.pub);
            score += side == Side::USSR ? scoring.vp_delta : -scoring.vp_delta;
        } else if (spec.side == side) {
            score += 1.4 + 0.1 * static_cast<double>(spec.ops);
        } else if (spec.side == other_side(side)) {
            score -= 0.8;
        } else {
            score += 0.15;
        }
        if (score > best_score) {
            best_score = score;
            best.action = ActionEncoding{
                .card_id = card_id,
                .mode = ActionMode::Event,
                .targets = {},
            };
        }
    }
    return best;
}

PlannedAction choose_plan_for_agent(
    const ExperimentalAgentSpec& agent,
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config
) {
    switch (agent.kind) {
        case ExperimentalAgentKind::Search: {
            log_runtime_stage_start("choose_search_action_plan", gs, side);
            const auto profile_target = configured_search_profile_target();
            const bool should_profile_search = profile_target.has_value()
                && profile_target->turn == gs.pub.turn
                && profile_target->ar == gs.pub.ar
                && profile_target->side == side;
            if (should_profile_search) {
                profile::set_enabled(true);
                profile::reset();
                std::cerr << logging::prefix(__FILE__, __LINE__)
                          << "profiling_search_call"
                          << " turn=" << gs.pub.turn
                          << " ar=" << gs.pub.ar
                          << " side=" << (side == Side::USSR ? "USSR" : "US")
                          << std::endl;
            }
            const auto start = std::chrono::steady_clock::now();
            auto plan = choose_search_action_plan(gs, side, rng, config);
            const auto elapsed_ms = std::chrono::duration<double, std::milli>(
                std::chrono::steady_clock::now() - start
            ).count();
            std::ostringstream extra;
            extra << "card=" << static_cast<int>(plan.action.card_id)
                  << " mode=" << static_cast<int>(plan.action.mode)
                  << " targets=" << plan.action.targets.size()
                  << " visits=" << plan.search_visits;
            log_slow_runtime("choose_search_action_plan", gs, side, elapsed_ms, extra.str());
            if (should_profile_search) {
                std::cerr << profile::report();
                if (exit_after_profiled_search()) {
                    std::exit(0);
                }
            }
            return plan;
        }
        case ExperimentalAgentKind::MinimalHybrid: {
            if (gs.pub.ar == 0) {
                return choose_headline_fallback(gs, side);
            }
            auto action = choose_action(
                PolicyKind::MinimalHybrid,
                gs.pub,
                gs.hands[to_index(side)],
                holds_china_for(gs, side),
                rng
            );
            PlannedAction plan;
            if (action.has_value()) {
                plan.action = *action;
            }
            return plan;
        }
        case ExperimentalAgentKind::LearnedModel: {
            if (gs.pub.ar == 0) {
                return choose_headline_fallback(gs, side);
            }
#if defined(TS_BUILD_TORCH_RUNTIME)
            thread_local std::string cached_model_path;
            thread_local std::unique_ptr<TorchScriptPolicy> cached_policy;
            if (!cached_policy || cached_model_path != agent.model_path) {
                cached_policy = std::make_unique<TorchScriptPolicy>(agent.model_path);
                cached_model_path = agent.model_path;
            }
            auto action = cached_policy->choose_action(
                gs.pub,
                gs.hands[to_index(side)],
                holds_china_for(gs, side),
                rng
            );
            PlannedAction plan;
            if (action.has_value()) {
                plan.action = *action;
            }
            return plan;
#else
            throw std::runtime_error("LearnedModel requires TS_BUILD_TORCH_RUNTIME");
#endif
        }
    }
    return PlannedAction{};
}

int max_action_rounds_for_side(const GameState& gs, Side side, int base_total_ars) {
    int rounds = base_total_ars;
    if (gs.pub.space[to_index(side)] >= kSpaceShuttleArs) {
        rounds = std::max(rounds, kSpaceShuttleArs);
    }
    if (side == Side::US && gs.pub.north_sea_oil_extra_ar) {
        rounds = std::max(rounds, base_total_ars + 1);
    }
    return rounds;
}

void run_atomic_setup(GameState& gs, Pcg64Rng& rng) {
    for (const auto side : {Side::USSR, Side::US}) {
        const SetupOpening* opening = (side == Side::USSR)
            ? choose_random_opening(kHumanUSSROpenings.data(), static_cast<int>(kHumanUSSROpenings.size()), rng)
            : choose_random_opening(kHumanUSOpeningsBid2.data(), static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
        if (opening == nullptr) {
            continue;
        }
        for (int idx = 0; idx < opening->count; ++idx) {
            const auto country = opening->placements[idx].country;
            const auto amount = opening->placements[idx].amount;
            gs.pub.set_influence(side, country, gs.pub.influence_of(side, country) + amount);
        }
    }
    gs.setup_influence_remaining = {0, 0};
    gs.phase = GamePhase::Headline;
}

GameResult end_of_turn(GameState& gs, int turn, int max_turns) {
    const auto defcon = gs.pub.defcon;
    for (const auto side : {Side::USSR, Side::US}) {
        const auto shortfall = std::max(0, defcon - gs.pub.milops[to_index(side)]);
        if (shortfall == 0) {
            continue;
        }
        if (side == Side::USSR) {
            gs.pub.vp -= shortfall;
        } else {
            gs.pub.vp += shortfall;
        }
    }

    auto [over, winner] = check_vp_win(gs.pub);
    if (over) {
        return GameResult{.winner = winner, .final_vp = gs.pub.vp, .end_turn = turn, .end_reason = "vp"};
    }

    gs.pub.defcon = std::min(5, gs.pub.defcon + 1);
    gs.pub.milops = {0, 0};
    gs.pub.space_attempts = {0, 0};
    gs.pub.ops_modifier = {0, 0};
    gs.pub.vietnam_revolts_active = false;
    gs.pub.north_sea_oil_extra_ar = false;
    gs.pub.glasnost_free_ops = 0;
    gs.pub.cuban_missile_crisis_active = false;
    gs.pub.chernobyl_blocked_region.reset();
    gs.pub.latam_coup_bonus.reset();

    for (const auto side : {Side::USSR, Side::US}) {
        for (int raw = 1; raw <= kMaxCardId; ++raw) {
            const auto card_id = static_cast<CardId>(raw);
            if (!gs.hands[to_index(side)].test(card_id)) {
                continue;
            }
            if (card_spec(card_id).is_scoring) {
                return GameResult{
                    .winner = other_side(side),
                    .final_vp = gs.pub.vp,
                    .end_turn = turn,
                    .end_reason = "scoring_card_held",
                };
            }
        }
    }

    if (turn == max_turns) {
        auto final = apply_final_scoring(gs.pub);
        gs.pub.vp += final.vp_delta;
        if (final.game_over) {
            return GameResult{.winner = final.winner, .final_vp = gs.pub.vp, .end_turn = turn, .end_reason = "europe_control"};
        }
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int raw = 1; raw <= kMaxCardId; ++raw) {
            const auto card_id = static_cast<CardId>(raw);
            if (gs.hands[to_index(side)].test(card_id)) {
                gs.pub.discard.set(card_id);
            }
        }
        gs.hands[to_index(side)].reset();
    }

    return GameResult{.winner = std::nullopt, .final_vp = gs.pub.vp, .end_turn = turn, .end_reason = "continue"};
}

template <typename ApplyFn>
ResolutionOutcome plan_and_apply_special(
    GameState& gs,
    Side evaluation_side,
    Pcg64Rng& rng,
    const HeuristicConfig& config,
    std::string_view label,
    ApplyFn&& apply_fn
) {
    auto root = gs;
    auto root_rng = rng;
    const ResolutionFn resolution = [apply_fn](GameState& sim, Pcg64Rng& sim_rng, const PolicyCallbackFn* cb) {
        auto result = apply_fn(sim, sim_rng, cb);
        if (!result.has_value()) {
            return ResolutionOutcome{};
        }
        auto& [pub, over, winner] = *result;
        (void)pub;
        return ResolutionOutcome{
            .over = over,
            .winner = winner,
        };
    };
    const auto start = std::chrono::steady_clock::now();
    const auto script = solve_callback_script(root, evaluation_side, resolution, root_rng, evaluation_side, config, label);
    const auto replay = make_replay_callback(script);
    auto outcome = resolution(gs, rng, &replay);
    const auto elapsed_ms = std::chrono::duration<double, std::milli>(
        std::chrono::steady_clock::now() - start
    ).count();
    log_slow_runtime(label, gs, evaluation_side, elapsed_ms);
    sync_china(gs);
    return outcome;
}

std::optional<GameResult> maybe_resolve_special_hooks(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config
) {
    if (gs.pub.cuban_missile_crisis_active) {
        const auto outcome = plan_and_apply_special(
            gs,
            side,
            rng,
            config,
            "cuban_missile_crisis_cancel",
            [side](GameState& sim, Pcg64Rng& sim_rng, const PolicyCallbackFn* cb) {
                return resolve_cuban_missile_crisis_cancel(sim, side, sim_rng, cb);
            }
        );
        if (outcome.over) {
            return GameResult{
                .winner = outcome.winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = infer_terminal_cause(gs.pub, outcome.winner),
            };
        }
    }
    if ((side == Side::USSR && gs.pub.bear_trap_active) || (side == Side::US && gs.pub.quagmire_active)) {
        const auto outcome = plan_and_apply_special(
            gs,
            side,
            rng,
            config,
            "trap_ar",
            [side](GameState& sim, Pcg64Rng& sim_rng, const PolicyCallbackFn* cb) {
                return resolve_trap_ar(sim, side, sim_rng, cb);
            }
        );
        if (outcome.over) {
            return GameResult{
                .winner = outcome.winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = infer_terminal_cause(gs.pub, outcome.winner),
            };
        }
        if ((side == Side::USSR && gs.pub.bear_trap_active) || (side == Side::US && gs.pub.quagmire_active)) {
            return std::nullopt;
        }
    }
    return std::nullopt;
}

std::optional<GameResult> run_headline_phase(
    GameState& gs,
    const ExperimentalAgentSpec& ussr_agent,
    const ExperimentalAgentSpec& us_agent,
    Pcg64Rng& rng,
    const HeuristicConfig& config,
    std::vector<ExperimentalStep>& trace
) {
    gs.phase = GamePhase::Headline;
    gs.pub.ar = 0;
    std::array<std::optional<PlannedAction>, 2> plans = {};
    for (const auto side : {Side::USSR, Side::US}) {
        gs.pub.phasing = side;
        const auto& agent = side == Side::USSR ? ussr_agent : us_agent;
        plans[to_index(side)] = choose_plan_for_agent(agent, gs, side, rng, config);
    }

    std::vector<std::pair<Side, PlannedAction>> ordered;
    for (const auto side : {Side::USSR, Side::US}) {
        if (plans[to_index(side)].has_value()) {
            ordered.push_back({side, *plans[to_index(side)]});
        }
    }
    std::sort(ordered.begin(), ordered.end(), [](const auto& lhs, const auto& rhs) {
        const auto lhs_ops = card_spec(lhs.second.action.card_id).ops;
        const auto rhs_ops = card_spec(rhs.second.action.card_id).ops;
        if (lhs_ops != rhs_ops) {
            return lhs_ops > rhs_ops;
        }
        return static_cast<int>(lhs.first) < static_cast<int>(rhs.first);
    });

    for (const auto& [side, plan] : ordered) {
        gs.pub.phasing = side;
        CallbackScript callback_trace;
        const auto replay = make_recording_replay_callback(plan.script, &callback_trace);
        const auto pub_before = gs.pub;
        auto& hand = gs.hands[to_index(side)];
        if (hand.test(plan.action.card_id)) {
            hand.reset(plan.action.card_id);
        }
        auto [new_pub, over, winner] = apply_action_with_hands(gs, plan.action, side, rng, &replay);
        (void)new_pub;
        sync_china(gs);
        trace.push_back(ExperimentalStep{
            .turn = gs.pub.turn,
            .ar = 0,
            .side = side,
            .action = plan.action,
            .pub_before = pub_before,
            .pub_after = gs.pub,
            .callback_trace = std::move(callback_trace),
            .static_score = plan.static_score,
            .rollout_score = plan.rollout_score,
            .search_visits = plan.search_visits,
        });
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = infer_terminal_cause(gs.pub, winner, plan.action.card_id),
            };
        }
    }
    return std::nullopt;
}

std::optional<GameResult> run_action_rounds(
    GameState& gs,
    const ExperimentalAgentSpec& ussr_agent,
    const ExperimentalAgentSpec& us_agent,
    Pcg64Rng& rng,
    const HeuristicConfig& config,
    int total_ars,
    std::vector<ExperimentalStep>& trace
) {
    gs.phase = GamePhase::ActionRound;
    for (int ar = 1; ar <= kSpaceShuttleArs; ++ar) {
        gs.pub.ar = ar;
        for (const auto side : {Side::USSR, Side::US}) {
            if (ar > max_action_rounds_for_side(gs, side, total_ars)) {
                continue;
            }
            gs.pub.phasing = side;
            if (auto special = maybe_resolve_special_hooks(gs, side, rng, config); special.has_value()) {
                if (special->end_reason != "continue") {
                    return *special;
                }
                continue;
            }
            if (!has_legal_action(gs.hands[to_index(side)], gs.pub, side, holds_china_for(gs, side))) {
                continue;
            }
            const auto& agent = side == Side::USSR ? ussr_agent : us_agent;
            auto plan = choose_plan_for_agent(agent, gs, side, rng, config);
            CallbackScript callback_trace;
            const auto replay = make_recording_replay_callback(plan.script, &callback_trace);
            const auto pub_before = gs.pub;
            auto& hand = gs.hands[to_index(side)];
            if (hand.test(plan.action.card_id)) {
                hand.reset(plan.action.card_id);
            }
            auto [new_pub, over, winner] = apply_action_with_hands(gs, plan.action, side, rng, &replay);
            (void)new_pub;
            sync_china(gs);
            trace.push_back(ExperimentalStep{
                .turn = gs.pub.turn,
                .ar = ar,
                .side = side,
                .action = plan.action,
                .pub_before = pub_before,
                .pub_after = gs.pub,
                .callback_trace = std::move(callback_trace),
                .static_score = plan.static_score,
                .rollout_score = plan.rollout_score,
                .search_visits = plan.search_visits,
            });
            if (over) {
                return GameResult{
                    .winner = winner,
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = infer_terminal_cause(gs.pub, winner, plan.action.card_id),
                };
            }
            if (side == Side::USSR && gs.pub.norad_active && gs.pub.defcon == 2) {
                const auto outcome = plan_and_apply_special(
                    gs,
                    Side::US,
                    rng,
                    config,
                    "norad",
                    [](GameState& sim, Pcg64Rng& sim_rng, const PolicyCallbackFn* cb) {
                        return resolve_norad_live(sim, sim_rng, cb);
                    }
                );
                if (outcome.over) {
                    return GameResult{
                        .winner = outcome.winner,
                        .final_vp = gs.pub.vp,
                        .end_turn = gs.pub.turn,
                        .end_reason = infer_terminal_cause(gs.pub, outcome.winner),
                    };
                }
            }
        }
    }
    return std::nullopt;
}

}  // namespace

ExperimentalTrace play_search_vs_search_from_state(
    GameState gs,
    std::optional<uint32_t> seed,
    const HeuristicConfig& config
) {
    return play_matchup_from_state_internal(
        std::move(gs),
        ExperimentalAgentSpec{.kind = ExperimentalAgentKind::Search, .model_path = {}},
        ExperimentalAgentSpec{.kind = ExperimentalAgentKind::Search, .model_path = {}},
        seed,
        config
    );
}

ExperimentalTrace play_matchup_game(
    const ExperimentalAgentSpec& ussr_agent,
    const ExperimentalAgentSpec& us_agent,
    std::optional<uint32_t> seed,
    const HeuristicConfig& config
) {
    auto gs = reset_game(seed);
    return play_matchup_from_state_internal(std::move(gs), ussr_agent, us_agent, seed, config);
}

namespace {

ExperimentalTrace play_matchup_from_state_internal(
    GameState gs,
    const ExperimentalAgentSpec& ussr_agent,
    const ExperimentalAgentSpec& us_agent,
    std::optional<uint32_t> seed,
    const HeuristicConfig& config
) {
    Pcg64Rng rng(seed.value_or(std::random_device{}()));
    ExperimentalTrace trace;

    if (gs.phase == GamePhase::Setup && gs.setup_influence_remaining[0] > 0) {
        trace.has_setup_snapshot = true;
        trace.setup_before = gs.pub;
        run_atomic_setup(gs, rng);
        trace.setup_after = gs.pub;
    }

    const int max_turns = std::max(1, config.max_turns);
    const int max_steps = std::max(1, config.max_trace_steps);
    for (int turn = std::max(1, gs.pub.turn); turn <= max_turns; ++turn) {
        gs.pub.turn = turn;
        if (turn == 4) {
            advance_to_mid_war(gs, rng);
        } else if (turn == 8) {
            advance_to_late_war(gs, rng);
        }

        deal_cards(gs, Side::USSR, rng);
        deal_cards(gs, Side::US, rng);

        if (auto result = run_headline_phase(gs, ussr_agent, us_agent, rng, config, trace.steps); result.has_value()) {
            trace.result = *result;
            return trace;
        }
        if (static_cast<int>(trace.steps.size()) >= max_steps) {
            trace.result = GameResult{
                .winner = std::nullopt,
                .final_vp = gs.pub.vp,
                .end_turn = turn,
                .end_reason = "step_limit",
            };
            return trace;
        }
        if (auto result = run_action_rounds(gs, ussr_agent, us_agent, rng, config, ars_for_turn(turn), trace.steps); result.has_value()) {
            trace.result = *result;
            return trace;
        }
        if (static_cast<int>(trace.steps.size()) >= max_steps) {
            trace.result = GameResult{
                .winner = std::nullopt,
                .final_vp = gs.pub.vp,
                .end_turn = turn,
                .end_reason = "step_limit",
            };
            return trace;
        }
        if (gs.pub.glasnost_free_ops > 0) {
            const auto outcome = plan_and_apply_special(
                gs,
                Side::USSR,
                rng,
                config,
                "glasnost_free_ops",
                [](GameState& sim, Pcg64Rng& sim_rng, const PolicyCallbackFn* cb) -> std::optional<std::tuple<PublicState, bool, std::optional<Side>>> {
                    resolve_glasnost_free_ops_live(sim.pub, sim_rng, cb);
                    auto [over, winner] = check_vp_win(sim.pub);
                    return std::tuple{sim.pub, over, winner};
                }
            );
            if (outcome.over) {
                trace.result = GameResult{
                    .winner = outcome.winner,
                    .final_vp = gs.pub.vp,
                    .end_turn = turn,
                    .end_reason = infer_terminal_cause(gs.pub, outcome.winner),
                };
                return trace;
            }
        }
        auto result = end_of_turn(gs, turn, max_turns);
        if (result.end_reason != "continue") {
            trace.result = result;
            return trace;
        }
    }

    trace.result = GameResult{
        .winner = gs.pub.vp >= 0 ? std::optional<Side>(Side::USSR) : std::optional<Side>(Side::US),
        .final_vp = gs.pub.vp,
        .end_turn = max_turns,
        .end_reason = "turn_limit",
    };
    return trace;
}

}  // namespace

ExperimentalTrace play_selfplay_game(std::optional<uint32_t> seed, const HeuristicConfig& config) {
    return play_matchup_game(
        ExperimentalAgentSpec{.kind = ExperimentalAgentKind::Search, .model_path = {}},
        ExperimentalAgentSpec{.kind = ExperimentalAgentKind::Search, .model_path = {}},
        seed,
        config
    );
}

std::vector<GameResult> play_matchup_games(
    const ExperimentalAgentSpec& ussr_agent,
    const ExperimentalAgentSpec& us_agent,
    int game_count,
    std::optional<uint32_t> seed,
    const HeuristicConfig& config,
    int thread_count
) {
    const int safe_game_count = std::max(0, game_count);
    std::vector<GameResult> results(static_cast<size_t>(safe_game_count));
    Pcg64Rng seed_rng(seed.value_or(std::random_device{}()));
    std::vector<uint32_t> seeds(static_cast<size_t>(safe_game_count));
    for (int game = 0; game < safe_game_count; ++game) {
        seeds[static_cast<size_t>(game)] = static_cast<uint32_t>(seed_rng.next_u64());
    }

    const int worker_count = std::max(1, thread_count);
    if (worker_count == 1 || safe_game_count <= 1) {
        for (int game = 0; game < safe_game_count; ++game) {
            const auto trace = play_matchup_game(
                ussr_agent,
                us_agent,
                seeds[static_cast<size_t>(game)],
                config
            );
            results[static_cast<size_t>(game)] = trace.result;
        }
        return results;
    }

    std::atomic<int> next_game{0};
    std::vector<std::thread> workers;
    workers.reserve(static_cast<size_t>(worker_count));
    for (int worker = 0; worker < worker_count; ++worker) {
        workers.emplace_back([&, worker]() {
            (void)worker;
            while (true) {
                const int game = next_game.fetch_add(1);
                if (game >= safe_game_count) {
                    break;
                }
                const auto trace = play_matchup_game(
                    ussr_agent,
                    us_agent,
                    seeds[static_cast<size_t>(game)],
                    config
                );
                results[static_cast<size_t>(game)] = trace.result;
            }
        });
    }
    for (auto& worker : workers) {
        worker.join();
    }
    return results;
}

}  // namespace ts::experimental
