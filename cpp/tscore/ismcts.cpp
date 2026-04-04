// Determinized information-set MCTS built by sampling hidden opponent hands
// and reusing the native full-state MCTS implementation.

#include "ismcts.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <stdexcept>
#include <utility>

#include "game_loop.hpp"
#include "human_openings.hpp"
#include "mcts_search_impl.hpp"
#include "nn_features.hpp"
#include "policies.hpp"

namespace ts {
namespace {

namespace si = search_impl;

constexpr int kIsmctsVirtualLossWeight = 1;

int count_hand_excluding_china(const CardSet& hand) {
    auto count = static_cast<int>(hand.count());
    if (hand.test(kChinaCardId)) {
        --count;
    }
    return count;
}

bool action_less(const ActionEncoding& lhs, const ActionEncoding& rhs) {
    if (lhs.card_id != rhs.card_id) {
        return lhs.card_id < rhs.card_id;
    }
    if (lhs.mode != rhs.mode) {
        return static_cast<int>(lhs.mode) < static_cast<int>(rhs.mode);
    }
    return lhs.targets < rhs.targets;
}

bool aggregated_edge_better(const MctsEdge& lhs, const MctsEdge& rhs) {
    if (lhs.visit_count != rhs.visit_count) {
        return lhs.visit_count > rhs.visit_count;
    }
    if (lhs.prior != rhs.prior) {
        return lhs.prior > rhs.prior;
    }
    return action_less(lhs.action, rhs.action);
}

struct AggregatedEdgeState {
    MctsEdge edge;
    int occurrences = 0;
};

struct DeterminizationSlot {
    GameState root_state;
    GameState sim_state;
    std::unique_ptr<MctsNode> root;
    std::vector<std::pair<MctsNode*, int>> path;
    int sims_completed = 0;
    int sims_target = 0;
    bool pending_expansion = false;
    bool pending_root_expansion = false;
    bool move_done = false;
    Pcg64Rng rng;
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

SearchResult build_search_result(const DeterminizationSlot& slot) {
    SearchResult result;
    result.total_simulations = slot.sims_completed;
    if (slot.root == nullptr) {
        return result;
    }

    result.root_edges.reserve(slot.root->edges.size());
    for (size_t i = 0; i < slot.root->edges.size(); ++i) {
        auto edge = slot.root->edges[i];
        if (i < slot.root->applied_actions.size()) {
            edge.action = slot.root->applied_actions[i];
        }
        result.root_edges.push_back(std::move(edge));
    }
    result.root_value = mean_root_value(*slot.root);

    const auto best_index = best_root_edge_index(*slot.root);
    if (best_index >= 0 && static_cast<size_t>(best_index) < slot.root->applied_actions.size()) {
        result.best_action = slot.root->applied_actions[static_cast<size_t>(best_index)];
    }
    return result;
}

}  // namespace

GameState sample_determinization(
    const GameState& gs,
    Side acting_side,
    int opp_hand_size,
    Pcg64Rng& rng
) {
    if (!is_player_side(acting_side)) {
        throw std::invalid_argument("acting_side must be USSR or US");
    }
    if (opp_hand_size < 0) {
        throw std::invalid_argument("opp_hand_size must be non-negative");
    }

    auto determinized = clone_game_state(gs);
    const auto opponent = other_side(acting_side);
    auto& opponent_hand = determinized.hands[to_index(opponent)];
    const auto known_opp_count = count_hand_excluding_china(opponent_hand);
    if (known_opp_count > opp_hand_size) {
        throw std::invalid_argument("known opponent hand exceeds opp_hand_size");
    }

    auto hidden_pool = determinized.deck;
    hidden_pool.erase(
        std::remove(hidden_pool.begin(), hidden_pool.end(), kChinaCardId),
        hidden_pool.end()
    );
    shuffle_with_numpy_rng(hidden_pool, rng);

    const auto hidden_needed = opp_hand_size - known_opp_count;
    if (hidden_needed > static_cast<int>(hidden_pool.size())) {
        throw std::invalid_argument("not enough hidden cards to fill opponent hand");
    }

    for (int i = 0; i < hidden_needed; ++i) {
        opponent_hand.set(hidden_pool[static_cast<size_t>(i)]);
    }
    determinized.deck.assign(hidden_pool.begin() + hidden_needed, hidden_pool.end());
    return determinized;
}

IsmctsResult ismcts_search(
    const GameState& partial_state,
    Side acting_side,
    int opp_hand_size,
    torch::jit::script::Module& model,
    const IsmctsConfig& config,
    Pcg64Rng& rng
) {
    return ismcts_search_batched(
        partial_state,
        acting_side,
        opp_hand_size,
        model,
        config,
        rng,
        torch::kCPU
    );
}

IsmctsResult ismcts_search_batched(
    const GameState& partial_state,
    Side acting_side,
    int opp_hand_size,
    torch::jit::script::Module& model,
    const IsmctsConfig& config,
    Pcg64Rng& rng,
    torch::Device device
) {
    if (config.n_determinizations <= 0) {
        throw std::invalid_argument("n_determinizations must be positive");
    }

    std::vector<DeterminizationSlot> slots(static_cast<size_t>(config.n_determinizations));
    for (auto& slot : slots) {
        slot.rng = Pcg64Rng(rng.next_u64());
        slot.root_state = sample_determinization(partial_state, acting_side, opp_hand_size, slot.rng);
        slot.sim_state = slot.root_state;
        slot.sims_target = config.mcts_config.n_simulations;
    }

    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(config.n_determinizations, device);
    std::vector<DeterminizationSlot*> batch_slots;
    batch_slots.reserve(static_cast<size_t>(config.n_determinizations));

    while (true) {
        bool all_done = true;
        batch_inputs.reset();
        batch_slots.clear();

        for (auto& slot : slots) {
            if (slot.root == nullptr) {
                all_done = false;
                if (auto immediate = si::expand_without_model(slot.root_state, slot.rng); immediate.has_value()) {
                    slot.root = std::move(immediate->node);
                    apply_root_dirichlet_noise(*slot.root, config.mcts_config, slot.rng);
                    if (slot.sims_target == 0) {
                        slot.move_done = true;
                    }
                } else {
                    slot.pending_expansion = true;
                    slot.pending_root_expansion = true;
                    batch_inputs.fill_slot(
                        batch_inputs.filled,
                        slot.root_state.pub,
                        slot.root_state.hands[to_index(slot.root_state.pub.phasing)],
                        si::holds_china_for(slot.root_state, slot.root_state.pub.phasing),
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

            all_done = false;
            const auto selection = si::select_to_leaf(
                slot,
                config.mcts_config.c_puct,
                kIsmctsVirtualLossWeight
            );
            if (selection.needs_batch) {
                batch_inputs.fill_slot(
                    batch_inputs.filled,
                    slot.sim_state.pub,
                    slot.sim_state.hands[to_index(slot.sim_state.pub.phasing)],
                    si::holds_china_for(slot.sim_state, slot.sim_state.pub.phasing),
                    slot.sim_state.pub.phasing
                );
                batch_slots.push_back(&slot);
                continue;
            }

            si::backpropagate(slot, selection.leaf_value, kIsmctsVirtualLossWeight);
            slot.sims_completed += 1;
            if (slot.sims_completed >= slot.sims_target) {
                slot.move_done = true;
            }
        }

        if (batch_slots.empty()) {
            if (all_done) {
                break;
            }
            continue;
        }

        const auto outputs = nn::forward_model_batched(model, batch_inputs);
        for (size_t i = 0; i < batch_slots.size(); ++i) {
            auto& slot = *batch_slots[i];
            const auto batch_index = static_cast<int64_t>(i);
            if (slot.pending_root_expansion) {
                auto expansion = si::expand_from_outputs(
                    slot.root_state,
                    outputs,
                    batch_index,
                    config.mcts_config,
                    slot.rng
                );
                slot.root = std::move(expansion.node);
                apply_root_dirichlet_noise(*slot.root, config.mcts_config, slot.rng);
                slot.pending_expansion = false;
                slot.pending_root_expansion = false;
                if (slot.sims_target == 0) {
                    slot.move_done = true;
                }
                continue;
            }

            auto expansion = si::expand_from_outputs(
                slot.sim_state,
                outputs,
                batch_index,
                config.mcts_config,
                slot.rng
            );
            auto& [parent, edge_index] = slot.path.back();
            parent->children[static_cast<size_t>(edge_index)] = std::move(expansion.node);
            slot.pending_expansion = false;
            si::backpropagate(slot, expansion.leaf_value, kIsmctsVirtualLossWeight);
            slot.sims_completed += 1;
            if (slot.sims_completed >= slot.sims_target) {
                slot.move_done = true;
            }
        }
    }

    std::vector<AggregatedEdgeState> aggregated;
    aggregated.reserve(32);
    double total_root_value = 0.0;

    for (const auto& slot : slots) {
        const auto result = build_search_result(slot);
        total_root_value += result.root_value;

        for (const auto& edge : result.root_edges) {
            const auto found = std::find_if(
                aggregated.begin(),
                aggregated.end(),
                [&edge](const AggregatedEdgeState& state) { return state.edge.action == edge.action; }
            );
            if (found == aggregated.end()) {
                aggregated.push_back(AggregatedEdgeState{
                    .edge = MctsEdge{
                        .action = edge.action,
                        .prior = edge.prior,
                        .visit_count = edge.visit_count,
                        .virtual_loss = 0,
                        .total_value = edge.total_value,
                    },
                    .occurrences = 1,
                });
                continue;
            }

            found->edge.prior += edge.prior;
            found->edge.visit_count += edge.visit_count;
            found->edge.total_value += edge.total_value;
            found->occurrences += 1;
        }
    }

    IsmctsResult ismcts_result;
    ismcts_result.total_determinizations = config.n_determinizations;
    ismcts_result.mean_root_value = total_root_value / static_cast<double>(config.n_determinizations);
    ismcts_result.aggregated_edges.reserve(aggregated.size());

    for (auto& state : aggregated) {
        if (state.occurrences > 0) {
            state.edge.prior /= static_cast<float>(state.occurrences);
        }
        ismcts_result.aggregated_edges.push_back(std::move(state.edge));
    }

    std::sort(
        ismcts_result.aggregated_edges.begin(),
        ismcts_result.aggregated_edges.end(),
        [](const MctsEdge& lhs, const MctsEdge& rhs) { return aggregated_edge_better(lhs, rhs); }
    );

    if (!ismcts_result.aggregated_edges.empty()) {
        ismcts_result.best_action = ismcts_result.aggregated_edges.front().action;
    }
    return ismcts_result;
}

std::vector<GameResult> play_ismcts_matchup(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    const IsmctsConfig& config,
    uint32_t base_seed,
    torch::Device device
) {
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(std::max(0, n_games)));

    for (int i = 0; i < n_games; ++i) {
        const auto seed = base_seed + static_cast<uint32_t>(i);
        auto gs = reset_game(seed);
        Pcg64Rng rng(seed);

        // Atomic setup: place from opening tables with +2 bid.
        for (const auto side : {Side::USSR, Side::US}) {
            const SetupOpening* opening = (side == Side::USSR)
                ? choose_random_opening(kHumanUSSROpenings.data(),
                                        static_cast<int>(kHumanUSSROpenings.size()), rng)
                : choose_random_opening(kHumanUSOpeningsBid2.data(),
                                        static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
            if (opening == nullptr) continue;
            for (int j = 0; j < opening->count; ++j) {
                gs.pub.set_influence(side, opening->placements[j].country,
                    gs.pub.influence_of(side, opening->placements[j].country) + opening->placements[j].amount);
            }
        }
        gs.setup_influence_remaining = {0, 0};
        gs.phase = GamePhase::Headline;

        // ISMCTS policy for learned side: captures &gs to access full state.
        const PolicyFn ismcts_fn = [&gs, &model, &config, device](
            const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng
        ) -> std::optional<ActionEncoding> {
            const auto acting = pub.phasing;
            const auto opp_idx = to_index(other_side(acting));
            auto opp_hand_size = static_cast<int>(gs.hands[opp_idx].count());
            if (gs.hands[opp_idx].test(kChinaCardId)) {
                --opp_hand_size;
            }
            auto result = ismcts_search_batched(gs, acting, opp_hand_size, model, config, rng, device);
            return result.best_action;
        };

        const PolicyFn heuristic_fn = [](
            const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng
        ) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
        };

        GameLoopConfig loop_config;
        loop_config.skip_setup_influence = true;  // already done above

        const auto& ussr_fn = (learned_side == Side::USSR) ? ismcts_fn : heuristic_fn;
        const auto& us_fn = (learned_side == Side::US) ? ismcts_fn : heuristic_fn;

        auto traced = play_game_traced_from_state_ref_with_rng(gs, ussr_fn, us_fn, rng, loop_config);
        results.push_back(std::move(traced.result));
    }
    return results;
}

}  // namespace ts

#endif
