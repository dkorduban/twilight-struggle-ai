#include "search.hpp"

#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <memory>
#include <optional>
#include <sstream>
#include <string_view>
#include <vector>

#include "callback_script.hpp"
#include "evaluator.hpp"
#include "game_data.hpp"
#include "hand_ops.hpp"
#include "logging.hpp"
#include "planner.hpp"
#include "profile.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts::experimental {
namespace {

constexpr double kSafetyRefineThreshold = -6.0;
constexpr size_t kSafetyExtraRefineCount = 4;

bool search_progress_logging_enabled() {
    static const bool enabled = [] {
        const char* value = std::getenv("TS_EXP_LOG_SEARCH_PROGRESS");
        return value != nullptr && value[0] != '\0' && value[0] != '0';
    }();
    return enabled;
}

void log_search_progress(const GameState& gs, Side side, std::string_view message) {
    if (!search_progress_logging_enabled()) {
        return;
    }
    std::ostringstream line;
    line << logging::prefix(__FILE__, __LINE__)
         << "search_progress"
         << " turn=" << gs.pub.turn
         << " ar=" << gs.pub.ar
         << " side=" << (side == Side::USSR ? "USSR" : "US")
         << " " << message;
    std::cerr << line.str() << std::endl;
}

double bounded_search_value(double value) {
    constexpr double kScale = 40.0;
    return kScale * std::tanh(value / kScale);
}

double final_plan_score(const PlannedAction& plan) {
    const double rollout_weight = plan.search_visits > 0 ? 0.8 : 0.0;
    const double static_weight = 1.0 - rollout_weight;
    return rollout_weight * bounded_search_value(plan.rollout_score) + static_weight * plan.static_score;
}

struct SearchEdge;

struct SearchNode {
    int visits = 0;
    std::vector<SearchEdge> edges;
};

struct SearchEdge {
    ActionEncoding action;
    double prior = 0.0;
    double q0 = 0.0;
    int visits = 0;
    int availability = 0;
    double total_value = 0.0;
    std::unique_ptr<SearchNode> child;
};

struct AdvanceResult {
    bool terminal = false;
    std::optional<Side> winner;
    bool turn_ended = false;
};

void sync_china(GameState& gs) {
    gs.ussr_holds_china = gs.pub.china_held_by == Side::USSR;
    gs.us_holds_china = gs.pub.china_held_by == Side::US;
}

bool holds_china_for(const GameState& gs, Side side) {
    return side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
}

bool action_needs_exact_root_eval(const ActionEncoding& action) {
    return action.mode == ActionMode::Event;
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
    const auto script = solve_callback_script(root, evaluation_side, resolution, root_rng, evaluation_side, config, label);
    const auto replay = make_replay_callback(script);
    auto outcome = resolution(gs, rng, &replay);
    sync_china(gs);
    return outcome;
}

AdvanceResult apply_end_of_turn(GameState& gs) {
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
        return AdvanceResult{.terminal = true, .winner = winner};
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int raw = 1; raw <= kMaxCardId; ++raw) {
            const auto card_id = static_cast<CardId>(raw);
            if (gs.hands[to_index(side)].test(card_id) && card_spec(card_id).is_scoring) {
                return AdvanceResult{.terminal = true, .winner = other_side(side)};
            }
        }
    }

    if (gs.pub.turn == 10) {
        auto final = apply_final_scoring(gs.pub);
        gs.pub.vp += final.vp_delta;
        if (final.game_over) {
            return AdvanceResult{.terminal = true, .winner = final.winner};
        }
        return AdvanceResult{
            .terminal = true,
            .winner = gs.pub.vp >= 0 ? std::optional<Side>(Side::USSR) : std::optional<Side>(Side::US),
        };
    }

    return AdvanceResult{
        .terminal = false,
        .winner = std::nullopt,
        .turn_ended = true,
    };
}

int max_action_rounds_for_side(const GameState& gs, Side side) {
    int rounds = ars_for_turn(gs.pub.turn);
    if (gs.pub.space[to_index(side)] >= 8) {
        rounds = std::max(rounds, 8);
    }
    if (side == Side::US && gs.pub.north_sea_oil_extra_ar) {
        rounds = std::max(rounds, ars_for_turn(gs.pub.turn) + 1);
    }
    return rounds;
}

void advance_action_pointer(GameState& gs) {
    if (gs.pub.phasing == Side::USSR) {
        gs.pub.phasing = Side::US;
    } else {
        ++gs.pub.ar;
        gs.pub.phasing = Side::USSR;
    }
}

AdvanceResult normalize_to_decision_point(
    GameState& gs,
    Pcg64Rng& rng,
    const HeuristicConfig& config
) {
    const profile::ScopedTimer timer(profile::Slot::NormalizeToDecisionPoint);
    while (true) {
        const auto side = gs.pub.phasing;
        if (gs.pub.ar > max_action_rounds_for_side(gs, side)) {
            if (side == Side::USSR) {
                gs.pub.phasing = Side::US;
                continue;
            }
            if (side == Side::US && gs.pub.glasnost_free_ops > 0) {
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
                    return AdvanceResult{.terminal = true, .winner = outcome.winner};
                }
            }
            return apply_end_of_turn(gs);
        }

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
                return AdvanceResult{.terminal = true, .winner = outcome.winner};
            }
        }

        const bool trapped = (side == Side::USSR && gs.pub.bear_trap_active) || (side == Side::US && gs.pub.quagmire_active);
        if (trapped) {
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
                return AdvanceResult{.terminal = true, .winner = outcome.winner};
            }
            const bool still_trapped = (side == Side::USSR && gs.pub.bear_trap_active) || (side == Side::US && gs.pub.quagmire_active);
            if (still_trapped) {
                advance_action_pointer(gs);
                continue;
            }
        }

        if (has_legal_action(gs.hands[to_index(side)], gs.pub, side, holds_china_for(gs, side))) {
            return AdvanceResult{
                .terminal = false,
                .winner = std::nullopt,
                .turn_ended = false,
            };
        }
        advance_action_pointer(gs);
    }
}

AdvanceResult apply_planned_action(
    GameState& gs,
    Side acting_side,
    const PlannedAction& plan,
    Pcg64Rng& rng,
    const HeuristicConfig& config
) {
    const auto replay = make_replay_callback(plan.script);
    auto& hand = gs.hands[to_index(acting_side)];
    if (hand.test(plan.action.card_id)) {
        hand.reset(plan.action.card_id);
    }
    auto [new_pub, over, winner] = apply_action_with_hands(gs, plan.action, acting_side, rng, &replay);
    (void)new_pub;
    sync_china(gs);
    if (over) {
        return AdvanceResult{.terminal = true, .winner = winner};
    }

    if (acting_side == Side::USSR && gs.pub.norad_active && gs.pub.defcon == 2) {
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
            return AdvanceResult{.terminal = true, .winner = outcome.winner};
        }
    }

    advance_action_pointer(gs);
    return AdvanceResult{
        .terminal = false,
        .winner = std::nullopt,
        .turn_ended = false,
    };
}

double exact_action_value(
    const GameState& gs,
    Side acting_side,
    const ActionEncoding& action,
    Pcg64Rng& rng,
    const HeuristicConfig& config
) {
    const profile::ScopedTimer timer(profile::Slot::ExactActionValue);
    auto sim = gs;
    auto plan = plan_specific_action(sim, acting_side, rng, config, action);
    const auto outcome = apply_planned_action(sim, acting_side, plan, rng, config);
    if (outcome.terminal) {
        return evaluate_terminal_for_side(outcome.winner, acting_side, config);
    }
    const auto advance = normalize_to_decision_point(sim, rng, config);
    if (advance.terminal) {
        return evaluate_terminal_for_side(advance.winner, acting_side, config);
    }
    return evaluate_state_for_side(sim, acting_side, config);
}

double exact_planned_value(
    const GameState& gs,
    Side acting_side,
    const PlannedAction& plan,
    Pcg64Rng& rng,
    const HeuristicConfig& config
) {
    auto sim = gs;
    const auto outcome = apply_planned_action(sim, acting_side, plan, rng, config);
    if (outcome.terminal) {
        return evaluate_terminal_for_side(outcome.winner, acting_side, config);
    }
    const auto advance = normalize_to_decision_point(sim, rng, config);
    if (advance.terminal) {
        return evaluate_terminal_for_side(advance.winner, acting_side, config);
    }
    return evaluate_state_for_side(sim, acting_side, config);
}

double rollout_value(
    GameState gs,
    Side root_side,
    Pcg64Rng& rng,
    const HeuristicConfig& config,
    int ply_budget
) {
    for (int ply = 0; ply < ply_budget; ++ply) {
        auto advance = normalize_to_decision_point(gs, rng, config);
        if (advance.terminal) {
            return evaluate_terminal_for_side(advance.winner, root_side, config);
        }
        if (advance.turn_ended) {
            return evaluate_state_for_side(gs, root_side, config);
        }

        const auto acting_side = gs.pub.phasing;
        auto plan = choose_greedy_action_plan(gs, acting_side, rng, config);
        const auto outcome = apply_planned_action(gs, acting_side, plan, rng, config);
        if (outcome.terminal) {
            return evaluate_terminal_for_side(outcome.winner, root_side, config);
        }
    }
    return evaluate_state_for_side(gs, root_side, config);
}

double edge_mean(const SearchEdge& edge, const HeuristicConfig& config) {
    if (edge.visits > 0) {
        return edge.total_value / static_cast<double>(edge.visits);
    }
    return config.q0_weight * edge.q0;
}

int find_edge_index(const SearchNode& node, const ActionEncoding& action) {
    for (int idx = 0; idx < static_cast<int>(node.edges.size()); ++idx) {
        if (node.edges[static_cast<size_t>(idx)].action == action) {
            return idx;
        }
    }
    return -1;
}

double simulate_node(
    SearchNode& node,
    GameState& gs,
    Side root_side,
    Pcg64Rng& rng,
    const HeuristicConfig& config,
    int depth
) {
    auto advance = normalize_to_decision_point(gs, rng, config);
    if (advance.terminal) {
        return bounded_search_value(evaluate_terminal_for_side(advance.winner, root_side, config));
    }
    if (advance.turn_ended || depth >= config.ismcts_max_depth) {
        return bounded_search_value(evaluate_state_for_side(gs, root_side, config));
    }

    const auto acting_side = gs.pub.phasing;
    const auto proposals = enumerate_action_proposals(gs, acting_side, config);
    if (proposals.empty()) {
        return bounded_search_value(evaluate_state_for_side(gs, root_side, config));
    }

    ++node.visits;
    for (const auto& proposal : proposals) {
        const int idx = find_edge_index(node, proposal.action);
        if (idx >= 0) {
            ++node.edges[static_cast<size_t>(idx)].availability;
        }
    }

    const int widening_limit = std::max(
        1,
        static_cast<int>(std::floor(config.progressive_widening_base * std::pow(static_cast<double>(std::max(1, node.visits)), config.progressive_widening_alpha)))
    );

    int chosen_edge = -1;
    for (const auto& proposal : proposals) {
        if (find_edge_index(node, proposal.action) >= 0) {
            continue;
        }
        if (static_cast<int>(node.edges.size()) < std::min(widening_limit, static_cast<int>(proposals.size()))) {
            auto planned = plan_specific_action(gs, acting_side, rng, config, proposal.action);
            node.edges.push_back(SearchEdge{
                .action = proposal.action,
                .prior = proposal.prior,
                .q0 = planned.static_score,
                .visits = 0,
                .availability = 1,
                .total_value = 0.0,
                .child = std::make_unique<SearchNode>(),
            });
            chosen_edge = static_cast<int>(node.edges.size()) - 1;

            GameState next = gs;
            auto sim_rng = Pcg64Rng(rng.next_u64());
            const auto outcome = apply_planned_action(next, acting_side, planned, sim_rng, config);
            double value = 0.0;
            if (outcome.terminal) {
                value = bounded_search_value(evaluate_terminal_for_side(outcome.winner, root_side, config));
            } else if (depth + 1 >= config.ismcts_max_depth) {
                value = bounded_search_value(evaluate_state_for_side(next, root_side, config));
            } else {
                value = bounded_search_value(
                    rollout_value(std::move(next), root_side, sim_rng, config, std::max(0, config.rollout_plies - depth - 1))
                );
            }
            auto& edge = node.edges[static_cast<size_t>(chosen_edge)];
            ++edge.visits;
            edge.total_value += value;
            return value;
        }
    }

    double best_score = -std::numeric_limits<double>::infinity();
    for (int idx = 0; idx < static_cast<int>(node.edges.size()); ++idx) {
        auto& edge = node.edges[static_cast<size_t>(idx)];
        if (edge.availability <= 0) {
            continue;
        }
        const double q = edge_mean(edge, config);
        const double signed_q = acting_side == root_side ? q : -q;
        const double explore = config.uct_c * edge.prior
            * std::sqrt(std::log(static_cast<double>(node.visits) + 1.0) / static_cast<double>(edge.availability + 1));
        const double score = signed_q + explore;
        if (score > best_score) {
            best_score = score;
            chosen_edge = idx;
        }
    }

    if (chosen_edge < 0) {
        return bounded_search_value(evaluate_state_for_side(gs, root_side, config));
    }

    auto& edge = node.edges[static_cast<size_t>(chosen_edge)];
    auto planned = plan_specific_action(gs, acting_side, rng, config, edge.action);
    GameState next = gs;
    auto sim_rng = Pcg64Rng(rng.next_u64());
    const auto outcome = apply_planned_action(next, acting_side, planned, sim_rng, config);
    double value = 0.0;
    if (outcome.terminal) {
        value = bounded_search_value(evaluate_terminal_for_side(outcome.winner, root_side, config));
    } else {
        value = simulate_node(*edge.child, next, root_side, sim_rng, config, depth + 1);
    }
    ++edge.visits;
    edge.total_value += value;
    return value;
}

}  // namespace

PlannedAction choose_ismcts_action_plan(
    const GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const HeuristicConfig& config
) {
    const profile::ScopedTimer timer(profile::Slot::ChooseSearchAction);
    log_search_progress(gs, side, "start");
    if (gs.pub.ar == 0 || config.ismcts_simulations <= 0 || config.ismcts_determinizations <= 0) {
        return choose_greedy_action_plan(gs, side, rng, config);
    }

    const auto obs = make_observation(gs, side);
    std::vector<GameState> determinizations;
    determinizations.reserve(static_cast<size_t>(config.ismcts_determinizations));
    for (int idx = 0; idx < config.ismcts_determinizations; ++idx) {
        auto det_rng = Pcg64Rng(rng.next_u64());
        determinizations.push_back(determinize(obs, det_rng));
        determinizations.back().pub.phasing = side;
        determinizations.back().pub.ar = gs.pub.ar;
        determinizations.back().pub.turn = gs.pub.turn;
        sync_china(determinizations.back());
    }
    {
        std::ostringstream msg;
        msg << "determinizations=" << determinizations.size();
        log_search_progress(gs, side, msg.str());
    }

    if (config.ismcts_max_depth <= 1) {
        const auto proposals = enumerate_action_proposals(gs, side, config);
        if (proposals.empty()) {
            return choose_greedy_action_plan(gs, side, rng, config);
        }
        {
            std::ostringstream msg;
            msg << "depth1 proposals=" << proposals.size()
                << " nsim=" << config.ismcts_simulations
                << " exact_root_eval_limit=" << config.exact_root_eval_limit;
            log_search_progress(gs, side, msg.str());
        }

        std::vector<std::vector<double>> cached_values(
            determinizations.size(),
            std::vector<double>(proposals.size(), std::numeric_limits<double>::quiet_NaN())
        );
        const size_t exact_root_eval_limit = std::min(
            proposals.size(),
            static_cast<size_t>(std::max(0, config.exact_root_eval_limit))
        );
        auto cached_value = [&](size_t det_idx, size_t action_idx) -> double {
            if (action_idx >= exact_root_eval_limit && !action_needs_exact_root_eval(proposals[action_idx].action)) {
                return bounded_search_value(proposals[action_idx].heuristic_score);
            }
            auto& slot = cached_values[det_idx][action_idx];
            if (std::isnan(slot)) {
                auto det_rng = Pcg64Rng(rng.next_u64());
                slot = bounded_search_value(exact_action_value(
                    determinizations[det_idx],
                    side,
                    proposals[action_idx].action,
                    det_rng,
                    config
                ));
            }
            return slot;
        };
        log_search_progress(gs, side, "depth1_cached_value_ready");

        std::vector<int> visits(proposals.size(), 0);
        std::vector<double> totals(proposals.size(), 0.0);
        for (int sim = 0; sim < config.ismcts_simulations; ++sim) {
            const size_t det_idx = static_cast<size_t>(sim % determinizations.size());
            int best_idx = 0;
            double best_score = -std::numeric_limits<double>::infinity();
            for (int action_idx = 0; action_idx < static_cast<int>(proposals.size()); ++action_idx) {
                const double q = visits[static_cast<size_t>(action_idx)] > 0
                    ? totals[static_cast<size_t>(action_idx)] / static_cast<double>(visits[static_cast<size_t>(action_idx)])
                    : config.q0_weight * (std::isnan(cached_values[det_idx][static_cast<size_t>(action_idx)])
                        ? bounded_search_value(proposals[static_cast<size_t>(action_idx)].heuristic_score)
                        : cached_values[det_idx][static_cast<size_t>(action_idx)]);
                const double u = config.uct_c * proposals[static_cast<size_t>(action_idx)].prior
                    * std::sqrt(std::log(static_cast<double>(sim) + 2.0) / static_cast<double>(visits[static_cast<size_t>(action_idx)] + 1));
                const double score = q + u;
                if (score > best_score) {
                    best_score = score;
                    best_idx = action_idx;
                }
            }
            ++visits[static_cast<size_t>(best_idx)];
            totals[static_cast<size_t>(best_idx)] += cached_value(det_idx, static_cast<size_t>(best_idx));
            if (search_progress_logging_enabled() && ((sim + 1) % 50 == 0 || sim + 1 == config.ismcts_simulations)) {
                std::ostringstream msg;
                msg << "depth1_sim=" << (sim + 1) << "/" << config.ismcts_simulations;
                log_search_progress(gs, side, msg.str());
            }
        }
        log_search_progress(gs, side, "depth1_sim_done");

        std::vector<size_t> ranked(proposals.size());
        for (size_t idx = 0; idx < ranked.size(); ++idx) {
            ranked[idx] = idx;
        }
        std::sort(ranked.begin(), ranked.end(), [&](size_t lhs, size_t rhs) {
            if (visits[lhs] != visits[rhs]) {
                return visits[lhs] > visits[rhs];
            }
            const double lhs_score = visits[lhs] > 0 ? totals[lhs] / static_cast<double>(visits[lhs]) : 0.0;
            const double rhs_score = visits[rhs] > 0 ? totals[rhs] / static_cast<double>(visits[rhs]) : 0.0;
            return lhs_score > rhs_score;
        });

        PlannedAction best_plan;
        bool have_best = false;
        double best_score = -std::numeric_limits<double>::infinity();
        const size_t initial_refine_count = std::min<size_t>(
            static_cast<size_t>(std::max(1, config.search_candidate_limit)),
            ranked.size()
        );
        auto refine_rank = [&](size_t rank) {
            const auto idx = ranked[rank];
            if (rank >= initial_refine_count &&
                visits[idx] == 0 &&
                proposals[idx].action.mode == ActionMode::EventFirst) {
                log_search_progress(gs, side, "depth1_refine_skip_zero_visit_eventfirst");
                return;
            }
            if (search_progress_logging_enabled()) {
                std::ostringstream msg;
                msg << "depth1_refine_start rank=" << rank
                    << " card=" << static_cast<int>(proposals[idx].action.card_id)
                    << " mode=" << static_cast<int>(proposals[idx].action.mode)
                    << " visits=" << visits[idx];
                log_search_progress(gs, side, msg.str());
            }
            auto candidate = plan_specific_action(gs, side, rng, config, proposals[idx].action);
            log_search_progress(gs, side, "depth1_refine_planned");
            auto exact_rng = Pcg64Rng(rng.next_u64());
            const double exact_root_score = exact_planned_value(gs, side, candidate, exact_rng, config);
            log_search_progress(gs, side, "depth1_refine_exact_done");
            candidate.static_score = exact_root_score;
            candidate.rollout_score = exact_root_score;
            candidate.search_visits = visits[idx];
            const double candidate_score = final_plan_score(candidate);
            const bool better = !have_best ||
                candidate_score > best_score ||
                (candidate_score == best_score && candidate.search_visits > best_plan.search_visits);
            if (better) {
                best_score = candidate_score;
                best_plan = std::move(candidate);
                have_best = true;
            }
        };
        for (size_t rank = 0; rank < initial_refine_count; ++rank) {
            refine_rank(rank);
        }
        if (have_best && best_score <= kSafetyRefineThreshold && ranked.size() > initial_refine_count) {
            const size_t safety_refine_count = std::min<size_t>(
                ranked.size(),
                std::max(initial_refine_count, kSafetyExtraRefineCount)
            );
            for (size_t rank = initial_refine_count; rank < safety_refine_count; ++rank) {
                refine_rank(rank);
            }
        }
        if (have_best) {
            return best_plan;
        }
        return choose_greedy_action_plan(gs, side, rng, config);
    }

    SearchNode root;
    for (int sim = 0; sim < config.ismcts_simulations; ++sim) {
        auto sim_rng = Pcg64Rng(rng.next_u64());
        auto state = determinizations[static_cast<size_t>(sim % determinizations.size())];
        simulate_node(root, state, side, sim_rng, config, 0);
        if (search_progress_logging_enabled() && ((sim + 1) % 50 == 0 || sim + 1 == config.ismcts_simulations)) {
            std::ostringstream msg;
            msg << "deep_sim=" << (sim + 1) << "/" << config.ismcts_simulations;
            log_search_progress(gs, side, msg.str());
        }
    }
    log_search_progress(gs, side, "deep_sim_done");

    if (root.edges.empty()) {
        return choose_greedy_action_plan(gs, side, rng, config);
    }

    std::vector<size_t> ranked(root.edges.size());
    for (size_t idx = 0; idx < ranked.size(); ++idx) {
        ranked[idx] = idx;
    }
    std::sort(ranked.begin(), ranked.end(), [&](size_t lhs, size_t rhs) {
        const auto& left = root.edges[lhs];
        const auto& right = root.edges[rhs];
        if (left.visits != right.visits) {
            return left.visits > right.visits;
        }
        return edge_mean(left, config) > edge_mean(right, config);
    });

    PlannedAction best_plan;
    bool have_best = false;
    double best_score = -std::numeric_limits<double>::infinity();
    const size_t initial_refine_count = std::min<size_t>(
        static_cast<size_t>(std::max(6, config.search_candidate_limit + 2)),
        ranked.size()
    );
    auto refine_rank = [&](size_t rank) {
        const auto idx = ranked[rank];
        const auto& edge = root.edges[idx];
        if (rank >= initial_refine_count &&
            edge.visits == 0 &&
            edge.action.mode == ActionMode::EventFirst) {
            log_search_progress(gs, side, "deep_refine_skip_zero_visit_eventfirst");
            return;
        }
        if (search_progress_logging_enabled()) {
            std::ostringstream msg;
            msg << "deep_refine_start rank=" << rank
                << " card=" << static_cast<int>(edge.action.card_id)
                << " mode=" << static_cast<int>(edge.action.mode)
                << " visits=" << edge.visits;
            log_search_progress(gs, side, msg.str());
        }
        auto candidate = plan_specific_action(gs, side, rng, config, edge.action);
        log_search_progress(gs, side, "deep_refine_planned");
        auto exact_rng = Pcg64Rng(rng.next_u64());
        const double exact_root_score = exact_planned_value(gs, side, candidate, exact_rng, config);
        log_search_progress(gs, side, "deep_refine_exact_done");
        candidate.static_score = exact_root_score;
        candidate.rollout_score = exact_root_score;
        candidate.search_visits = edge.visits;
        const double candidate_score = final_plan_score(candidate);
        const bool better = !have_best ||
            candidate_score > best_score ||
            (candidate_score == best_score && candidate.search_visits > best_plan.search_visits);
        if (better) {
            best_score = candidate_score;
            best_plan = std::move(candidate);
            have_best = true;
        }
    };
    for (size_t rank = 0; rank < initial_refine_count; ++rank) {
        refine_rank(rank);
    }
    if (have_best && best_score <= kSafetyRefineThreshold && ranked.size() > initial_refine_count) {
        const size_t safety_refine_count = std::min<size_t>(
            ranked.size(),
            std::max(initial_refine_count, kSafetyExtraRefineCount)
        );
        for (size_t rank = initial_refine_count; rank < safety_refine_count; ++rank) {
            refine_rank(rank);
        }
    }
    if (have_best) {
        return best_plan;
    }
    return choose_greedy_action_plan(gs, side, rng, config);
}

}  // namespace ts::experimental
