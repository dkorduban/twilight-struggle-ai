// Wavefront-batched MCTS collection over a pool of concurrent games.

#include "mcts_batched.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <limits>
#include <map>
#include <sstream>
#include <stdexcept>
#include <utility>
#include <vector>

#include <torch/torch.h>

#include "game_data.hpp"
#include "human_openings.hpp"
#include "mcts.hpp"
#include "mcts_search_impl.hpp"
#include "nn_features.hpp"
#include "policies.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts {
namespace {

constexpr int kMidWarTurn = 4;
constexpr int kLateWarTurn = 8;
constexpr int kMaxTurns = 10;
constexpr int kSpaceShuttleArs = 8;
namespace si = search_impl;

using si::accessible_countries_filtered;
using si::backpropagate;
using si::build_action_from_country_logits;
using si::expand_from_outputs;
using si::expand_without_model;
using si::holds_china_for;
using si::is_defcon_lowering_card;
using si::select_to_leaf;
using si::sync_china_flags;
using si::tensor_at;

struct AggregatedVisitCount {
    CardId card_id = 0;
    ActionMode mode = ActionMode::Influence;
    int visits = 0;
};
double mean_root_value(const MctsNode& root) {
    if (root.is_terminal) {
        return root.terminal_value;
    }
    if (root.total_visits == 0) {
        return 0.0;
    }

    double total = 0.0;
    for (const auto& edge : root.edges) {
        total += edge.total_value;
    }
    return total / static_cast<double>(root.total_visits);
}

int best_root_edge_index(const MctsNode& root) {
    if (root.edges.empty()) {
        return -1;
    }

    int best_index = 0;
    for (size_t i = 1; i < root.edges.size(); ++i) {
        const auto& current = root.edges[i];
        const auto& best = root.edges[static_cast<size_t>(best_index)];
        if (current.visit_count > best.visit_count) {
            best_index = static_cast<int>(i);
            continue;
        }
        if (current.visit_count == best.visit_count && current.prior > best.prior) {
            best_index = static_cast<int>(i);
        }
    }
    return best_index;
}

SearchResult build_search_result(const GameSlot& slot) {
    SearchResult result;
    result.total_simulations = slot.sims_completed;
    if (slot.root == nullptr) {
        return result;
    }

    result.root_edges = slot.root->edges;
    result.root_value = mean_root_value(*slot.root);
    const auto best_index = best_root_edge_index(*slot.root);
    if (best_index >= 0) {
        result.best_action = slot.root->applied_actions[static_cast<size_t>(best_index)];
    }
    return result;
}

// Returns the effective sampling temperature for a given move number.
// If config.temperature == 0, always returns 0 (greedy).
// Otherwise config.temperature is treated as a scale multiplier applied to
// the piecewise schedule:
//   move <= 10  -> 1.0 (full stochasticity, early game)
//   move <= 30  -> 0.5 (moderate exploration, mid game)
//   move > 30   -> 0.0 (greedy, late game)
[[nodiscard]] float effective_temperature(const PendingDecision& decision, const BatchedMctsConfig& config) {
    if (config.temperature <= 0.0f) {
        return 0.0f;
    }
    float base = 0.0f;
    if (decision.move_number <= 10) {
        base = 1.0f;
    } else if (decision.move_number <= 30) {
        base = 0.5f;
    }
    return config.temperature * base;
}

std::optional<ActionEncoding> sample_action_by_visit_counts(
    const SearchResult& search,
    float temperature,
    Pcg64Rng& rng
) {
    if (temperature <= 0.0f || search.root_edges.empty()) {
        return std::nullopt;
    }

    std::vector<std::pair<size_t, double>> scaled_log_weights;
    scaled_log_weights.reserve(search.root_edges.size());
    double max_scaled_log_weight = -std::numeric_limits<double>::infinity();
    for (size_t i = 0; i < search.root_edges.size(); ++i) {
        const auto visits = search.root_edges[i].visit_count;
        if (visits <= 0) {
            continue;
        }
        const auto scaled_log_weight = std::log(static_cast<double>(visits)) / static_cast<double>(temperature);
        scaled_log_weights.emplace_back(i, scaled_log_weight);
        max_scaled_log_weight = std::max(max_scaled_log_weight, scaled_log_weight);
    }

    if (scaled_log_weights.empty()) {
        return std::nullopt;
    }

    std::vector<std::pair<size_t, double>> weights;
    weights.reserve(scaled_log_weights.size());
    double total_weight = 0.0;
    for (const auto& [edge_index, scaled_log_weight] : scaled_log_weights) {
        const auto weight = std::exp(scaled_log_weight - max_scaled_log_weight);
        if (!(weight > 0.0) || !std::isfinite(weight)) {
            continue;
        }
        total_weight += weight;
        weights.emplace_back(edge_index, total_weight);
    }

    if (!(total_weight > 0.0)) {
        return std::nullopt;
    }

    const auto draw = rng.random_double() * total_weight;
    for (const auto& [edge_index, cumulative_weight] : weights) {
        if (draw < cumulative_weight) {
            return search.root_edges[edge_index].action;
        }
    }

    return search.root_edges[weights.back().first].action;
}

std::string game_id_for(uint32_t base_seed, int game_index) {
    std::ostringstream out;
    out << "mcts_" << base_seed << "_";
    if (game_index < 10) {
        out << "000";
    } else if (game_index < 100) {
        out << "00";
    } else if (game_index < 1000) {
        out << "0";
    }
    out << game_index;
    return out.str();
}

// Run setup influence placement (TS Deluxe §3.0), sampling from human game corpus.
// USSR places 6 in EE, US places 9 (7 WE + 2 bid) as atomic openings.
void run_setup_influence_heuristic(GameState& gs, Pcg64Rng& rng) {
    for (const auto side : {Side::USSR, Side::US}) {
        const SetupOpening* opening = (side == Side::USSR)
            ? choose_random_opening(kHumanUSSROpenings.data(),
                                    static_cast<int>(kHumanUSSROpenings.size()), rng)
            : choose_random_opening(kHumanUSOpeningsBid2.data(),
                                    static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
        if (opening == nullptr) continue;
        for (int i = 0; i < opening->count; ++i) {
            const auto country = opening->placements[i].country;
            const auto amount = opening->placements[i].amount;
            gs.pub.set_influence(side, country,
                gs.pub.influence_of(side, country) + amount);
        }
    }
    gs.setup_influence_remaining = {0, 0};
    gs.phase = GamePhase::Headline;
}

void initialize_slot(GameSlot& slot, int game_index, uint32_t base_seed, const BatchedMctsConfig& config) {
    const auto seed = base_seed + static_cast<uint32_t>(game_index);
    slot = GameSlot{};
    slot.active = true;
    slot.root_state = reset_game(seed);
    slot.rng = Pcg64Rng(seed);
    // Run setup influence placement before MCTS begins.
    run_setup_influence_heuristic(slot.root_state, slot.rng);
    slot.sim_state = slot.root_state;
    slot.game_id = game_id_for(base_seed, game_index);
    slot.turn = 1;
    slot.stage = BatchedGameStage::TurnSetup;
    slot.sims_target = config.mcts.n_simulations;
}

void reset_move_search(GameSlot& slot, const BatchedMctsConfig& config) {
    slot.root.reset();
    slot.path.clear();
    slot.sim_state = slot.root_state;
    slot.sims_completed = 0;
    slot.sims_target = config.mcts.n_simulations;
    slot.pending_expansion = false;
    slot.pending_root_expansion = false;
    slot.move_done = false;
}

void mark_game_done(GameSlot& slot, GameResult result) {
    slot.result = std::move(result);
    slot.game_done = true;
    slot.stage = BatchedGameStage::Finished;
    slot.move_done = false;
    slot.pending_expansion = false;
    slot.pending_root_expansion = false;
    slot.decision.reset();
    slot.root.reset();
    slot.path.clear();
}

std::string end_reason(const PublicState& pub, std::optional<Side> winner) {
    if (pub.defcon <= 1) {
        return "defcon1";
    }
    if (winner.has_value()) {
        return "europe_control";
    }
    return "vp_threshold";
}

std::optional<GameResult> finish_turn(GameState& gs, int turn) {
    gs.phase = GamePhase::Cleanup;

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
        return GameResult{
            .winner = winner,
            .final_vp = gs.pub.vp,
            .end_turn = gs.pub.turn,
            .end_reason = "vp",
        };
    }

    gs.pub.defcon = std::min(5, gs.pub.defcon + 1);
    gs.pub.milops = {0, 0};
    gs.pub.space_attempts = {0, 0};
    gs.pub.ops_modifier = {0, 0};
    gs.pub.vietnam_revolts_active = false;
    gs.pub.north_sea_oil_extra_ar = false;
    gs.pub.glasnost_extra_ar = false;
    gs.pub.chernobyl_blocked_region.reset();
    gs.pub.latam_coup_bonus.reset();

    if (turn == kMaxTurns) {
        auto final = apply_final_scoring(gs.pub);
        gs.pub.vp += final.vp_delta;
        if (final.game_over) {
            return GameResult{
                .winner = final.winner,
                .final_vp = gs.pub.vp,
                .end_turn = turn,
                .end_reason = "europe_control",
            };
        }
        std::tie(over, winner) = check_vp_win(gs.pub);
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = turn,
                .end_reason = "vp_threshold",
            };
        }
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
            if (!gs.hands[to_index(side)].test(card_id)) {
                continue;
            }
            if (card_spec(static_cast<CardId>(card_id)).is_scoring) {
                return GameResult{
                    .winner = other_side(side),
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = "scoring_card_held",
                };
            }
        }
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
            if (gs.hands[to_index(side)].test(card_id)) {
                gs.pub.discard.set(card_id);
            }
        }
        gs.hands[to_index(side)].reset();
    }

    return std::nullopt;
}

void advance_after_action_pair(GameSlot& slot) {
    if (slot.current_side == Side::USSR) {
        slot.current_side = Side::US;
    } else {
        slot.current_side = Side::USSR;
        slot.current_ar += 1;
    }
}

void move_to_post_round_stage(GameSlot& slot) {
    if (slot.root_state.pub.north_sea_oil_extra_ar) {
        slot.root_state.pub.north_sea_oil_extra_ar = false;
        slot.stage = BatchedGameStage::ExtraActionRoundUS;
        return;
    }
    if (slot.root_state.pub.glasnost_extra_ar) {
        slot.root_state.pub.glasnost_extra_ar = false;
        slot.stage = BatchedGameStage::ExtraActionRoundUSSR;
        return;
    }
    slot.stage = BatchedGameStage::Cleanup;
}

void move_to_followup_stage_after_extra(GameSlot& slot, Side side) {
    if (side == Side::US && slot.root_state.pub.glasnost_extra_ar) {
        slot.root_state.pub.glasnost_extra_ar = false;
        slot.stage = BatchedGameStage::ExtraActionRoundUSSR;
        return;
    }
    slot.stage = BatchedGameStage::Cleanup;
}

void queue_decision(GameSlot& slot, Side side, int ar, bool is_headline, const BatchedMctsConfig& config) {
    slot.root_state.pub.phasing = side;
    slot.root_state.pub.ar = ar;
    slot.decision = PendingDecision{
        .turn = slot.root_state.pub.turn,
        .ar = ar,
        .move_number = slot.decisions_started + 1,
        .side = side,
        .holds_china = holds_china_for(slot.root_state, side),
        .is_headline = is_headline,
        .pub_snapshot = slot.root_state.pub,
        .hand_snapshot = slot.root_state.hands[to_index(side)],
    };
    slot.decisions_started += 1;
    reset_move_search(slot, config);
}

void finalize_headline_choices(GameSlot& slot) {
    slot.headline_order.clear();
    for (const auto side : {Side::USSR, Side::US}) {
        if (slot.pending_headlines[to_index(side)].has_value()) {
            slot.headline_order.push_back(*slot.pending_headlines[to_index(side)]);
        }
    }

    if (slot.pending_headlines[to_index(Side::US)].has_value() &&
        slot.pending_headlines[to_index(Side::US)]->action.card_id == 108 &&
        slot.pending_headlines[to_index(Side::USSR)].has_value()) {
        slot.root_state.pub.discard.set(slot.pending_headlines[to_index(Side::USSR)]->action.card_id);
        slot.headline_order.erase(
            std::remove_if(
                slot.headline_order.begin(),
                slot.headline_order.end(),
                [](const PendingHeadlineChoice& pending) { return pending.side == Side::USSR; }
            ),
            slot.headline_order.end()
        );
    }

    std::sort(slot.headline_order.begin(), slot.headline_order.end(), [](const auto& lhs, const auto& rhs) {
        const auto lhs_ops = card_spec(lhs.action.card_id).ops;
        const auto rhs_ops = card_spec(rhs.action.card_id).ops;
        if (lhs_ops != rhs_ops) {
            return lhs_ops > rhs_ops;
        }
        return static_cast<int>(lhs.side) > static_cast<int>(rhs.side);
    });

    slot.headline_order_index = 0;
    slot.stage = BatchedGameStage::HeadlineResolve;
}

void advance_until_decision(GameSlot& slot, const BatchedMctsConfig& config) {
    while (slot.active && !slot.game_done && !slot.move_done && !slot.decision.has_value()) {
        switch (slot.stage) {
            case BatchedGameStage::TurnSetup: {
                slot.root_state.pub.turn = slot.turn;
                if (slot.turn == kMidWarTurn) {
                    advance_to_mid_war(slot.root_state, slot.rng);
                } else if (slot.turn == kLateWarTurn) {
                    advance_to_late_war(slot.root_state, slot.rng);
                }
                deal_cards(slot.root_state, Side::USSR, slot.rng);
                deal_cards(slot.root_state, Side::US, slot.rng);
                slot.pending_headlines = {};
                slot.headline_order.clear();
                slot.headline_order_index = 0;
                slot.total_ars = ars_for_turn(slot.turn);
                slot.current_ar = 1;
                slot.current_side = Side::USSR;
                slot.stage = BatchedGameStage::HeadlineChoiceUSSR;
                break;
            }

            case BatchedGameStage::HeadlineChoiceUSSR:
            case BatchedGameStage::HeadlineChoiceUS: {
                const auto side = slot.stage == BatchedGameStage::HeadlineChoiceUSSR ? Side::USSR : Side::US;
                const auto holds_china = holds_china_for(slot.root_state, side);
                if (!has_legal_action(slot.root_state.hands[to_index(side)], slot.root_state.pub, side, holds_china)) {
                    if (side == Side::USSR) {
                        slot.stage = BatchedGameStage::HeadlineChoiceUS;
                    } else {
                        finalize_headline_choices(slot);
                    }
                    break;
                }
                slot.root_state.phase = GamePhase::Headline;
                queue_decision(slot, side, /*ar=*/0, /*is_headline=*/true, config);
                break;
            }

            case BatchedGameStage::HeadlineResolve: {
                if (slot.headline_order_index >= slot.headline_order.size()) {
                    slot.stage = BatchedGameStage::ActionRound;
                    break;
                }

                const auto pending = slot.headline_order[slot.headline_order_index++];
                const auto pub_snapshot = slot.root_state.pub;
                const auto vp_before = slot.root_state.pub.vp;
                const auto defcon_before = slot.root_state.pub.defcon;
                auto [new_pub, over, winner] = apply_action_live(slot.root_state, pending.action, pending.side, slot.rng);
                (void)new_pub;
                slot.traces.push_back(StepTrace{
                    .turn = slot.root_state.pub.turn,
                    .ar = 0,
                    .side = pending.side,
                    .holds_china = pending.holds_china,
                    .pub_snapshot = pub_snapshot,
                    .hand_snapshot = pending.hand_snapshot,
                    .action = pending.action,
                    .vp_before = vp_before,
                    .vp_after = slot.root_state.pub.vp,
                    .defcon_before = defcon_before,
                    .defcon_after = slot.root_state.pub.defcon,
                    .opp_hand_snapshot = slot.root_state.hands[to_index(pending.side == Side::USSR ? Side::US : Side::USSR)],
                    .deck_snapshot = slot.root_state.deck,
                    .ussr_holds_china_snapshot = slot.root_state.ussr_holds_china,
                    .us_holds_china_snapshot = slot.root_state.us_holds_china,
                });
                slot.search_results.push_back(pending.search);
                sync_china_flags(slot.root_state);
                if (over) {
                    mark_game_done(slot, GameResult{
                        .winner = winner,
                        .final_vp = slot.root_state.pub.vp,
                        .end_turn = slot.root_state.pub.turn,
                        .end_reason = end_reason(slot.root_state.pub, winner),
                    });
                }
                break;
            }

            case BatchedGameStage::ActionRound: {
                if (slot.current_ar > kSpaceShuttleArs) {
                    move_to_post_round_stage(slot);
                    break;
                }

                const auto side = slot.current_side;
                if (slot.current_ar > slot.total_ars && slot.root_state.pub.space[to_index(side)] < kSpaceShuttleArs) {
                    advance_after_action_pair(slot);
                    break;
                }

                slot.root_state.phase = GamePhase::ActionRound;
                slot.root_state.pub.ar = slot.current_ar;
                slot.root_state.pub.phasing = side;
                if (auto trap_result = resolve_trap_ar_live(slot.root_state, side, slot.rng); trap_result.has_value()) {
                    auto& [new_pub, over, winner] = *trap_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.root_state.pub.vp,
                            .end_turn = slot.root_state.pub.turn,
                            .end_reason = end_reason(slot.root_state.pub, winner),
                        });
                        break;
                    }
                    advance_after_action_pair(slot);
                    break;
                }

                const auto holds_china = holds_china_for(slot.root_state, side);
                if (!has_legal_action(slot.root_state.hands[to_index(side)], slot.root_state.pub, side, holds_china)) {
                    advance_after_action_pair(slot);
                    break;
                }
                queue_decision(slot, side, slot.current_ar, /*is_headline=*/false, config);
                break;
            }

            case BatchedGameStage::ExtraActionRoundUS:
            case BatchedGameStage::ExtraActionRoundUSSR: {
                const auto side = slot.stage == BatchedGameStage::ExtraActionRoundUS ? Side::US : Side::USSR;
                slot.root_state.pub.ar = std::max(slot.root_state.pub.ar, ars_for_turn(slot.root_state.pub.turn)) + 1;
                slot.root_state.pub.phasing = side;
                auto& hand = slot.root_state.hands[to_index(side)];
                if (hand.none()) {
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }
                if (auto trap_result = resolve_trap_ar_live(slot.root_state, side, slot.rng); trap_result.has_value()) {
                    auto& [new_pub, over, winner] = *trap_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.root_state.pub.vp,
                            .end_turn = slot.root_state.pub.turn,
                            .end_reason = end_reason(slot.root_state.pub, winner),
                        });
                        break;
                    }
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }

                const auto holds_china = holds_china_for(slot.root_state, side);
                if (!has_legal_action(hand, slot.root_state.pub, side, holds_china)) {
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }
                queue_decision(slot, side, slot.root_state.pub.ar, /*is_headline=*/false, config);
                break;
            }

            case BatchedGameStage::Cleanup: {
                if (auto result = finish_turn(slot.root_state, slot.turn); result.has_value()) {
                    mark_game_done(slot, *result);
                    break;
                }
                // Turn limit: sequential game loop stops at kMaxTurns and
                // resolves winner by VP.  Mirror that here.
                if (slot.turn >= kMaxTurns) {
                    std::optional<Side> winner;
                    if (slot.root_state.pub.vp > 0) {
                        winner = Side::USSR;
                    } else if (slot.root_state.pub.vp < 0) {
                        winner = Side::US;
                    }
                    mark_game_done(slot, GameResult{
                        .winner = winner,
                        .final_vp = slot.root_state.pub.vp,
                        .end_turn = kMaxTurns,
                        .end_reason = "turn_limit",
                    });
                    break;
                }
                slot.turn += 1;
                slot.stage = BatchedGameStage::TurnSetup;
                break;
            }

            case BatchedGameStage::Finished:
                slot.game_done = true;
                break;
        }
    }
}

void commit_best_action(GameSlot& slot, const BatchedMctsConfig& config) {
    if (!slot.move_done || !slot.decision.has_value()) {
        return;
    }

    const auto search = build_search_result(slot);
    auto action = search.best_action;

    // Epsilon-greedy: with probability epsilon_greedy, pick a uniformly random
    // legal action from the root edges instead of the MCTS-recommended action.
    const bool do_epsilon = config.epsilon_greedy > 0.0f
        && !search.root_edges.empty()
        && slot.rng.random_double() < static_cast<double>(config.epsilon_greedy);
    if (do_epsilon) {
        const auto idx = slot.rng.choice_index(search.root_edges.size());
        action = search.root_edges[idx].action;
    } else if (action.card_id != 0) {
        // Temperature-based sampling with piecewise schedule.
        const float temp = effective_temperature(*slot.decision, config);
        if (const auto sampled = sample_action_by_visit_counts(search, temp, slot.rng); sampled.has_value()) {
            action = *sampled;
        }
    }
    if (action.card_id == 0) {
        action = choose_action(
            PolicyKind::MinimalHybrid,
            slot.decision->pub_snapshot,
            slot.decision->hand_snapshot,
            slot.decision->holds_china,
            slot.rng
        ).value_or(ActionEncoding{});
    }
    if (action.card_id == 0) {
        throw std::runtime_error("batched MCTS could not resolve an action");
    }

    const auto decision = *slot.decision;
    slot.decision.reset();
    slot.root.reset();
    slot.path.clear();
    slot.pending_expansion = false;
    slot.pending_root_expansion = false;
    slot.move_done = false;

    if (decision.is_headline) {
        action.mode = ActionMode::Event;
        action.targets.clear();
        auto& hand = slot.root_state.hands[to_index(decision.side)];
        if (hand.test(action.card_id)) {
            hand.reset(action.card_id);
        }
        slot.pending_headlines[to_index(decision.side)] = PendingHeadlineChoice{
            .side = decision.side,
            .holds_china = decision.holds_china,
            .hand_snapshot = decision.hand_snapshot,
            .action = action,
            .search = search,
        };
        if (decision.side == Side::USSR) {
            slot.stage = BatchedGameStage::HeadlineChoiceUS;
        } else {
            finalize_headline_choices(slot);
        }
        return;
    }

    auto& hand = slot.root_state.hands[to_index(decision.side)];
    if (hand.test(action.card_id)) {
        hand.reset(action.card_id);
    }

    const auto vp_before = slot.root_state.pub.vp;
    const auto defcon_before = slot.root_state.pub.defcon;
    auto [new_pub, over, winner] = apply_action_live(slot.root_state, action, decision.side, slot.rng);
    (void)new_pub;
    slot.traces.push_back(StepTrace{
        .turn = decision.turn,
        .ar = decision.ar,
        .side = decision.side,
        .holds_china = decision.holds_china,
        .pub_snapshot = decision.pub_snapshot,
        .hand_snapshot = decision.hand_snapshot,
        .action = action,
        .vp_before = vp_before,
        .vp_after = slot.root_state.pub.vp,
        .defcon_before = defcon_before,
        .defcon_after = slot.root_state.pub.defcon,
        .opp_hand_snapshot = slot.root_state.hands[to_index(decision.side == Side::USSR ? Side::US : Side::USSR)],
        .deck_snapshot = slot.root_state.deck,
        .ussr_holds_china_snapshot = slot.root_state.ussr_holds_china,
        .us_holds_china_snapshot = slot.root_state.us_holds_china,
    });
    slot.search_results.push_back(search);
    sync_china_flags(slot.root_state);

    if (over) {
        mark_game_done(slot, GameResult{
            .winner = winner,
            .final_vp = slot.root_state.pub.vp,
            .end_turn = slot.root_state.pub.turn,
            .end_reason = end_reason(slot.root_state.pub, winner),
        });
        return;
    }

    if (decision.side == Side::USSR && slot.root_state.pub.norad_active && slot.root_state.pub.defcon == 2) {
        if (auto norad = resolve_norad_live(slot.root_state, slot.rng); norad.has_value()) {
            auto& [norad_pub, norad_over, norad_winner] = *norad;
            (void)norad_pub;
            if (norad_over) {
                mark_game_done(slot, GameResult{
                    .winner = norad_winner,
                    .final_vp = slot.root_state.pub.vp,
                    .end_turn = slot.root_state.pub.turn,
                    .end_reason = end_reason(slot.root_state.pub, norad_winner),
                });
                return;
            }
        }
    }

    if (slot.stage == BatchedGameStage::ActionRound) {
        advance_after_action_pair(slot);
        return;
    }
    if (slot.stage == BatchedGameStage::ExtraActionRoundUS || slot.stage == BatchedGameStage::ExtraActionRoundUSSR) {
        move_to_followup_stage_after_extra(slot, decision.side);
        return;
    }

    reset_move_search(slot, config);
}

const char* game_result_str(const std::optional<Side>& winner) {
    if (!winner.has_value()) {
        return "draw";
    }
    return *winner == Side::USSR ? "ussr_win" : "us_win";
}

int winner_side_int(const std::optional<Side>& winner) {
    if (!winner.has_value()) {
        return 0;
    }
    return *winner == Side::USSR ? 1 : -1;
}

std::string targets_csv(const std::vector<CountryId>& targets) {
    std::ostringstream out;
    for (size_t i = 0; i < targets.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << static_cast<int>(targets[i]);
    }
    return out.str();
}

void write_int_array(std::ostream& out, const std::vector<int>& values) {
    out << "[";
    for (size_t i = 0; i < values.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << values[i];
    }
    out << "]";
}

std::vector<int> card_mask(const CardSet& cards) {
    std::vector<int> mask(ts::kCardSlots, 0);
    for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
        if (cards.test(card_id)) {
            mask[static_cast<size_t>(card_id)] = 1;
        }
    }
    return mask;
}

std::vector<int> influence_array(const PublicState& pub, Side side) {
    std::vector<int> values(ts::kCountrySlots, 0);
    for (int country_id = 0; country_id <= ts::kMaxCountryId; ++country_id) {
        values[static_cast<size_t>(country_id)] = pub.influence_of(side, static_cast<CountryId>(country_id));
    }
    return values;
}

std::vector<AggregatedVisitCount> aggregate_visit_counts(const SearchResult& result) {
    std::map<std::pair<int, int>, int> counts;
    for (const auto& edge : result.root_edges) {
        counts[{static_cast<int>(edge.action.card_id), static_cast<int>(edge.action.mode)}] += edge.visit_count;
    }

    std::vector<AggregatedVisitCount> aggregated;
    aggregated.reserve(counts.size());
    for (const auto& [key, visits] : counts) {
        aggregated.push_back(AggregatedVisitCount{
            .card_id = static_cast<CardId>(key.first),
            .mode = static_cast<ActionMode>(key.second),
            .visits = visits,
        });
    }
    std::sort(aggregated.begin(), aggregated.end(), [](const auto& lhs, const auto& rhs) {
        if (lhs.visits != rhs.visits) {
            return lhs.visits > rhs.visits;
        }
        if (lhs.card_id != rhs.card_id) {
            return lhs.card_id < rhs.card_id;
        }
        return static_cast<int>(lhs.mode) < static_cast<int>(rhs.mode);
    });
    return aggregated;
}

void write_visit_counts_json(std::ostream& out, const SearchResult& result) {
    const auto aggregated = aggregate_visit_counts(result);
    out << "[";
    for (size_t i = 0; i < aggregated.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << "{\"card_id\":" << static_cast<int>(aggregated[i].card_id)
            << ",\"mode\":" << static_cast<int>(aggregated[i].mode)
            << ",\"visits\":" << aggregated[i].visits
            << "}";
    }
    out << "]";
}

void write_game_rows(const GameSlot& slot, std::ostream& out) {
    for (size_t step_idx = 0; step_idx < slot.traces.size(); ++step_idx) {
        const auto& step = slot.traces[step_idx];
        const auto& pub = step.pub_snapshot;
        const auto& search = slot.search_results[step_idx];

        auto actor_hand_mask = card_mask(step.hand_snapshot);
        std::vector<int> card_quality(ts::kCardSlots, 3);
        for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
            if (step.hand_snapshot.test(card_id)) {
                card_quality[static_cast<size_t>(card_id)] = 0;
            }
        }
        auto discard_mask = card_mask(pub.discard);
        auto removed_mask = card_mask(pub.removed);
        auto actor_known_not_in = card_mask(pub.discard | pub.removed);
        auto opp_known_in = std::vector<int>(ts::kCardSlots, 0);
        auto opp_known_not_in = card_mask(step.hand_snapshot | pub.discard | pub.removed);
        auto opp_possible = std::vector<int>(ts::kCardSlots, 0);
        auto lbl_opponent_possible = std::vector<int>(ts::kCardSlots, 0);
        int actor_hand_size = 0;
        for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
            if (step.hand_snapshot.test(card_id) && card_id != ts::kChinaCardId) {
                ++actor_hand_size;
            }
        }

        out
            << "{\"game_id\":\"" << slot.game_id << "\""
            << ",\"step_idx\":" << step_idx
            << ",\"turn\":" << pub.turn
            << ",\"ar\":" << pub.ar
            << ",\"phasing\":" << static_cast<int>(step.side)
            << ",\"action_kind\":-1"
            << ",\"card_id\":" << static_cast<int>(step.action.card_id)
            << ",\"country_id\":" << (step.action.targets.empty() ? -1 : static_cast<int>(step.action.targets.front()))
            << ",\"action_card_id\":" << static_cast<int>(step.action.card_id)
            << ",\"action_mode\":" << static_cast<int>(step.action.mode)
            << ",\"action_targets\":\"" << targets_csv(step.action.targets) << "\""
            << ",\"vp\":" << pub.vp
            << ",\"defcon\":" << pub.defcon
            << ",\"milops_ussr\":" << pub.milops[to_index(Side::USSR)]
            << ",\"milops_us\":" << pub.milops[to_index(Side::US)]
            << ",\"space_ussr\":" << pub.space[to_index(Side::USSR)]
            << ",\"space_us\":" << pub.space[to_index(Side::US)]
            << ",\"china_held_by\":" << static_cast<int>(pub.china_held_by)
            << ",\"china_playable\":" << (pub.china_playable ? "true" : "false")
            << ",\"ussr_influence\":";
        write_int_array(out, influence_array(pub, Side::USSR));
        out << ",\"us_influence\":";
        write_int_array(out, influence_array(pub, Side::US));
        out << ",\"discard_mask\":";
        write_int_array(out, discard_mask);
        out << ",\"removed_mask\":";
        write_int_array(out, removed_mask);
        out << ",\"actor_known_in\":";
        write_int_array(out, actor_hand_mask);
        out << ",\"actor_known_not_in\":";
        write_int_array(out, actor_known_not_in);
        out << ",\"actor_possible\":";
        write_int_array(out, actor_hand_mask);
        out << ",\"actor_hand_size\":" << actor_hand_size
            << ",\"actor_holds_china\":" << (step.holds_china ? "true" : "false")
            << ",\"opp_known_in\":";
        write_int_array(out, opp_known_in);
        out << ",\"opp_known_not_in\":";
        write_int_array(out, opp_known_not_in);
        out << ",\"opp_possible\":";
        write_int_array(out, opp_possible);
        out << ",\"opp_hand_size\":0"
            << ",\"opp_holds_china\":" << ((pub.china_held_by != Side::Neutral && !step.holds_china) ? "true" : "false")
            << ",\"lbl_actor_hand\":";
        write_int_array(out, actor_hand_mask);
        out << ",\"lbl_step_quality\":0"
            << ",\"lbl_card_quality\":";
        write_int_array(out, card_quality);
        out << ",\"lbl_opponent_possible\":";
        write_int_array(out, lbl_opponent_possible);
        out << ",\"mcts_visit_counts\":";
        write_visit_counts_json(out, search);
        out << ",\"mcts_root_value\":" << search.root_value
            << ",\"mcts_n_sim\":" << search.total_simulations
            << ",\"game_result\":\"" << game_result_str(slot.result.winner) << "\""
            << ",\"winner_side\":" << winner_side_int(slot.result.winner)
            << ",\"final_vp\":" << slot.result.final_vp
            << ",\"end_turn\":" << slot.result.end_turn
            << ",\"end_reason\":\"" << slot.result.end_reason << "\"}\n";
    }
}

}  // namespace

void collect_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    const BatchedMctsConfig& config,
    uint32_t base_seed,
    std::ostream& out_stream
) {
    if (n_games <= 0) {
        throw std::invalid_argument("n_games must be positive");
    }
    if (config.pool_size <= 0) {
        throw std::invalid_argument("pool_size must be positive");
    }
    if (config.virtual_loss_weight <= 0) {
        throw std::invalid_argument("virtual_loss_weight must be positive");
    }
    if (config.mcts.n_simulations < 0) {
        throw std::invalid_argument("n_simulations must be non-negative");
    }

    std::vector<GameSlot> pool(static_cast<size_t>(config.pool_size));
    int games_started = 0;
    int games_emitted = 0;

    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(config.pool_size);
    std::vector<GameSlot*> batch_slots;
    batch_slots.reserve(static_cast<size_t>(config.pool_size));

    while (games_emitted < n_games) {
        batch_inputs.reset();
        batch_slots.clear();

        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                write_game_rows(slot, out_stream);
                slot.emitted = true;
                slot.active = false;
                games_emitted += 1;
            }
            if (!slot.active && games_started < n_games) {
                initialize_slot(slot, games_started, base_seed, config);
                games_started += 1;
            }
        }

        for (auto& slot : pool) {
            if (!slot.active) {
                continue;
            }

            if (slot.move_done) {
                commit_best_action(slot, config);
            }
            advance_until_decision(slot, config);
            if (slot.game_done || !slot.decision.has_value()) {
                continue;
            }

            if (slot.root == nullptr) {
                if (auto immediate = expand_without_model(slot.root_state, slot.rng); immediate.has_value()) {
                    slot.root = std::move(immediate->node);
                } else {
                    slot.pending_expansion = true;
                    slot.pending_root_expansion = true;
                    batch_inputs.fill_slot(
                        batch_inputs.filled,
                        slot.root_state.pub,
                        slot.root_state.hands[to_index(slot.root_state.pub.phasing)],
                        holds_china_for(slot.root_state, slot.root_state.pub.phasing),
                        slot.root_state.pub.phasing
                    );
                    batch_slots.push_back(&slot);
                }
                continue;
            }

            if (slot.sims_completed >= slot.sims_target) {
                slot.move_done = true;
                continue;
            }

            const auto selection = select_to_leaf(slot, config.mcts.c_puct, config.virtual_loss_weight);
            if (selection.needs_batch) {
                batch_inputs.fill_slot(
                    batch_inputs.filled,
                    slot.sim_state.pub,
                    slot.sim_state.hands[to_index(slot.sim_state.pub.phasing)],
                    holds_china_for(slot.sim_state, slot.sim_state.pub.phasing),
                    slot.sim_state.pub.phasing
                );
                batch_slots.push_back(&slot);
                continue;
            }

            backpropagate(slot, selection.leaf_value, config.virtual_loss_weight);
            slot.sims_completed += 1;
            if (slot.sims_completed >= slot.sims_target) {
                slot.move_done = true;
            }
        }

        if (!batch_slots.empty()) {
            const auto outputs = nn::forward_model_batched(model, batch_inputs);
            for (size_t i = 0; i < batch_slots.size(); ++i) {
                auto& slot = *batch_slots[i];
                const auto batch_index = static_cast<int64_t>(i);
                if (slot.pending_root_expansion) {
                    auto expansion = expand_from_outputs(slot.root_state, outputs, batch_index, config.mcts, slot.rng);
                    slot.root = std::move(expansion.node);
                    apply_root_dirichlet_noise(*slot.root, config.mcts, slot.rng);
                    slot.pending_expansion = false;
                    slot.pending_root_expansion = false;
                    if (slot.sims_target == 0) {
                        slot.move_done = true;
                    }
                    continue;
                }

                auto expansion = expand_from_outputs(slot.sim_state, outputs, batch_index, config.mcts, slot.rng);
                auto& [parent, edge_index] = slot.path.back();
                parent->children[static_cast<size_t>(edge_index)] = std::move(expansion.node);
                slot.pending_expansion = false;
                backpropagate(slot, expansion.leaf_value, config.virtual_loss_weight);
                slot.sims_completed += 1;
                if (slot.sims_completed >= slot.sims_target) {
                    slot.move_done = true;
                }
            }
        }
    }
}

// ---------------------------------------------------------------------------
// Greedy batched benchmark: same GameSlot/advance_until_decision machinery
// as MCTS collection, but uses a single argmax decode instead of tree search.
// ---------------------------------------------------------------------------

namespace {

// Exact mirror of TorchScriptPolicy::choose_action logic from learned_policy.cpp,
// but reads from BatchOutputs instead of calling forward_model individually.
ActionEncoding greedy_action_from_outputs(
    const GameState& state,
    const nn::BatchOutputs& outputs,
    int64_t batch_index,
    Pcg64Rng& rng
) {
    const auto& pub = state.pub;
    const auto side = pub.phasing;
    const auto holds_china = holds_china_for(state, side);
    const auto& hand = state.hands[to_index(side)];

    auto playable = legal_cards(hand, pub, side, holds_china);
    if (playable.empty()) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
            .value_or(ActionEncoding{});
    }

    const auto card_logits = outputs.card_logits.index({batch_index});
    const auto mode_logits = outputs.mode_logits.index({batch_index});
    const auto country_logits_raw = outputs.country_logits.defined()
        ? outputs.country_logits.index({batch_index}) : torch::Tensor{};
    const auto strategy_logits_raw = outputs.strategy_logits.defined()
        ? outputs.strategy_logits.index({batch_index}) : torch::Tensor{};
    const auto country_strategy_logits_raw = outputs.country_strategy_logits.defined()
        ? outputs.country_strategy_logits.index({batch_index}) : torch::Tensor{};

    // ── Card selection with DEFCON safety (mirrors learned_policy.cpp) ──
    auto masked_card = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto card_id : playable) {
        if (is_defcon_lowering_card(card_id)) {
            const auto& ci = card_spec(card_id);
            const bool is_opp = (ci.side != side && ci.side != Side::Neutral);
            const bool is_neutral = (ci.side == Side::Neutral);
            if (is_opp) {
                if (pub.defcon <= 2) continue;
                if (pub.defcon == 3 && pub.ar == 0) continue;
            }
            if (is_neutral && pub.ar == 0 && pub.defcon <= 3) continue;
        }
        const auto index = static_cast<int64_t>(card_id - 1);
        masked_card.index_put_({index}, tensor_at(card_logits, index));
    }

    // If all masked, fall back to heuristic.
    {
        bool all_masked = true;
        for (const auto card_id : playable) {
            const auto index = static_cast<int64_t>(card_id - 1);
            if (tensor_at(masked_card, index).item<float>() > -std::numeric_limits<float>::infinity()) {
                all_masked = false;
                break;
            }
        }
        if (all_masked) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
    }

    auto sampled_card_id = static_cast<CardId>(masked_card.argmax(/*dim=*/0).item<int64_t>() + 1);

    // ── Mode selection (mirrors learned_policy.cpp) ──
    auto modes = legal_modes(sampled_card_id, pub, side);
    if (modes.empty()) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
            .value_or(ActionEncoding{});
    }

    auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
    for (const auto m : modes) {
        const auto index = static_cast<int64_t>(static_cast<int>(m));
        masked_mode.index_put_({index}, tensor_at(mode_logits, index));
    }
    auto mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());

    // DEFCON safety: no coup at DEFCON ≤ 2.
    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto m : modes) {
            masked_mode.index_put_({static_cast<int64_t>(static_cast<int>(m))}, tensor_at(mode_logits, static_cast<int>(m)));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    // DEFCON safety: no event for DEFCON-lowering cards at DEFCON ≤ 2.
    if (pub.defcon <= 2 && mode == ActionMode::Event && is_defcon_lowering_card(sampled_card_id)) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        if (modes.empty()) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto m : modes) {
            masked_mode.index_put_({static_cast<int64_t>(static_cast<int>(m))}, tensor_at(mode_logits, static_cast<int>(m)));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    // Re-apply coup guard after event guard may have changed mode.
    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto m : modes) {
            masked_mode.index_put_({static_cast<int64_t>(static_cast<int>(m))}, tensor_at(mode_logits, static_cast<int>(m)));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    // Belt-and-suspenders DEFCON safety gate.
    if (pub.defcon <= 2 && is_defcon_lowering_card(sampled_card_id)) {
        const auto& ci = card_spec(sampled_card_id);
        const bool event_fires_for_any_mode = (ci.side != side && ci.side != Side::Neutral);
        const bool event_fires_for_event_space =
            (mode == ActionMode::Event) ||
            (mode == ActionMode::Space && event_fires_for_any_mode);
        if (event_fires_for_any_mode || event_fires_for_event_space) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
    }

    // ── Target selection ──
    if (mode == ActionMode::Event || mode == ActionMode::Space) {
        return ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {}};
    }

    if (country_logits_raw.defined()) {
        auto action = build_action_from_country_logits(
            sampled_card_id, mode, country_logits_raw,
            pub, side, strategy_logits_raw, country_strategy_logits_raw);
        if (!action.targets.empty()) {
            return action;
        }
    }

    // Fallback: random target selection (mirrors learned_policy.cpp).
    const auto accessible = accessible_countries_filtered(pub, side, sampled_card_id, mode);
    if (!accessible.empty()) {
        if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
            const auto target = accessible[rng.choice_index(accessible.size())];
            return ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {target}};
        }
        const auto ops = effective_ops(sampled_card_id, pub, side);
        ActionEncoding action{.card_id = sampled_card_id, .mode = mode, .targets = {}};
        for (int i = 0; i < ops; ++i) {
            action.targets.push_back(accessible[rng.choice_index(accessible.size())]);
        }
        return action;
    }

    return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
        .value_or(ActionEncoding{});
}

void commit_greedy_action(GameSlot& slot, const ActionEncoding& action) {
    if (!slot.decision.has_value()) {
        return;
    }

    auto resolved = action;
    if (resolved.card_id == 0) {
        resolved = choose_action(
            PolicyKind::MinimalHybrid,
            slot.decision->pub_snapshot,
            slot.decision->hand_snapshot,
            slot.decision->holds_china,
            slot.rng
        ).value_or(ActionEncoding{});
    }
    if (resolved.card_id == 0) {
        throw std::runtime_error("greedy benchmark could not resolve an action");
    }

    const auto decision = *slot.decision;
    slot.decision.reset();
    slot.root.reset();
    slot.path.clear();
    slot.pending_expansion = false;
    slot.pending_root_expansion = false;
    slot.move_done = false;

    if (decision.is_headline) {
        resolved.mode = ActionMode::Event;
        resolved.targets.clear();
        auto& hand = slot.root_state.hands[to_index(decision.side)];
        if (hand.test(resolved.card_id)) {
            hand.reset(resolved.card_id);
        }
        // Greedy benchmark doesn't need real SearchResult, use empty.
        slot.pending_headlines[to_index(decision.side)] = PendingHeadlineChoice{
            .side = decision.side,
            .holds_china = decision.holds_china,
            .hand_snapshot = decision.hand_snapshot,
            .action = resolved,
            .search = SearchResult{},
        };
        if (decision.side == Side::USSR) {
            slot.stage = BatchedGameStage::HeadlineChoiceUS;
        } else {
            finalize_headline_choices(slot);
        }
        return;
    }

    auto& hand = slot.root_state.hands[to_index(decision.side)];
    if (hand.test(resolved.card_id)) {
        hand.reset(resolved.card_id);
    }

    auto [new_pub, over, winner] = apply_action_live(slot.root_state, resolved, decision.side, slot.rng);
    (void)new_pub;
    sync_china_flags(slot.root_state);

    if (over) {
        mark_game_done(slot, GameResult{
            .winner = winner,
            .final_vp = slot.root_state.pub.vp,
            .end_turn = slot.root_state.pub.turn,
            .end_reason = end_reason(slot.root_state.pub, winner),
        });
        return;
    }

    if (decision.side == Side::USSR && slot.root_state.pub.norad_active && slot.root_state.pub.defcon == 2) {
        if (auto norad = resolve_norad_live(slot.root_state, slot.rng); norad.has_value()) {
            auto& [norad_pub, norad_over, norad_winner] = *norad;
            (void)norad_pub;
            if (norad_over) {
                mark_game_done(slot, GameResult{
                    .winner = norad_winner,
                    .final_vp = slot.root_state.pub.vp,
                    .end_turn = slot.root_state.pub.turn,
                    .end_reason = end_reason(slot.root_state.pub, norad_winner),
                });
                return;
            }
        }
    }

    if (slot.stage == BatchedGameStage::ActionRound) {
        advance_after_action_pair(slot);
        return;
    }
    if (slot.stage == BatchedGameStage::ExtraActionRoundUS || slot.stage == BatchedGameStage::ExtraActionRoundUSSR) {
        move_to_followup_stage_after_extra(slot, decision.side);
        return;
    }
}

}  // anonymous namespace

std::vector<GameResult> benchmark_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int pool_size,
    uint32_t base_seed,
    torch::Device device
) {
    if (n_games <= 0) {
        return {};
    }
    if (pool_size <= 0) {
        pool_size = std::min(n_games, 64);
    }

    // Use a minimal MCTS config just for GameSlot initialization.
    BatchedMctsConfig config;
    config.pool_size = pool_size;
    config.mcts.n_simulations = 0;  // No tree search.

    std::vector<GameSlot> pool(static_cast<size_t>(pool_size));
    int games_started = 0;
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(n_games));

    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(pool_size, device);

    // Track which batch slot corresponds to which GameSlot, and whether
    // the learned side needs NN inference for that decision.
    struct BatchEntry {
        GameSlot* slot = nullptr;
        bool needs_nn = false;  // true = learned side, false = heuristic side
    };
    std::vector<BatchEntry> batch_entries;
    batch_entries.reserve(static_cast<size_t>(pool_size));

    while (static_cast<int>(results.size()) < n_games) {
        batch_inputs.reset();
        batch_entries.clear();

        // Collect completed games, start new ones.
        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                results.push_back(slot.result);
                slot.emitted = true;
                slot.active = false;
            }
            if (!slot.active && games_started < n_games) {
                initialize_slot(slot, games_started, base_seed, config);
                games_started += 1;
            }
        }

        // Advance each active game until it needs a decision.
        for (auto& slot : pool) {
            if (!slot.active || slot.game_done) {
                continue;
            }

            if (slot.move_done) {
                // Previous action was resolved; commit it.
                // (should not happen in greedy mode, but handle anyway)
            }

            advance_until_decision(slot, config);
            if (slot.game_done || !slot.decision.has_value()) {
                continue;
            }

            const auto decision_side = slot.decision->side;
            const bool is_learned = (decision_side == learned_side);

            if (is_learned) {
                // Queue for batched NN inference.
                const auto batch_idx = batch_inputs.filled;
                batch_inputs.fill_slot(
                    batch_idx,
                    slot.root_state.pub,
                    slot.root_state.hands[to_index(decision_side)],
                    slot.decision->holds_china,
                    decision_side
                );
                batch_entries.push_back(BatchEntry{&slot, true});
            } else {
                // Heuristic side: resolve immediately.
                auto heuristic_action = choose_action(
                    PolicyKind::MinimalHybrid,
                    slot.decision->pub_snapshot,
                    slot.decision->hand_snapshot,
                    slot.decision->holds_china,
                    slot.rng
                ).value_or(ActionEncoding{});
                commit_greedy_action(slot, heuristic_action);
            }
        }

        // Run batched NN inference for all learned-side decisions.
        if (!batch_entries.empty()) {
            const auto outputs = nn::forward_model_batched(model, batch_inputs);
            int batch_idx = 0;
            for (auto& entry : batch_entries) {
                if (!entry.needs_nn) {
                    continue;
                }
                auto action = greedy_action_from_outputs(
                    entry.slot->root_state,
                    outputs,
                    static_cast<int64_t>(batch_idx),
                    entry.slot->rng
                );
                commit_greedy_action(*entry.slot, action);
                batch_idx += 1;
            }
        }
    }

    return results;
}

}  // namespace ts

#endif
