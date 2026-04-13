// Shared internal helpers for batched tree search variants.

#pragma once

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <memory>
#include <optional>
#include <utility>
#include <vector>

#include <torch/torch.h>

#include "game_data.hpp"
#include "game_loop.hpp"
#include "mcts.hpp"
#include "nn_features.hpp"
#include "policies.hpp"

namespace ts::search_impl {

inline constexpr std::array<int, 15> kDefconLoweringCards = {
    4, 11, 13, 20, 24, 39, 48, 49, 50, 52, 53, 68, 83, 92, 105,
};

struct ModeDraft {
    ActionMode mode = ActionMode::Influence;
    std::vector<ActionEncoding> edges;
};

struct CardDraft {
    CardId card_id = 0;
    std::vector<ModeDraft> modes;
};

struct ExpansionResult {
    std::unique_ptr<MctsNode> node;
    double leaf_value = 0.0;
};

struct SelectionResult {
    bool needs_batch = false;
    double leaf_value = 0.0;
};

[[nodiscard]] inline bool is_defcon_lowering_card(CardId card_id) {
    return std::find(kDefconLoweringCards.begin(), kDefconLoweringCards.end(), static_cast<int>(card_id)) !=
        kDefconLoweringCards.end();
}

[[nodiscard]] inline bool is_card_blocked_by_defcon(const PublicState& pub, Side side, CardId card_id) {
    if (!is_defcon_lowering_card(card_id)) {
        return false;
    }

    const auto& card_info = card_spec(card_id);
    const bool is_opponent_card = (card_info.side != side && card_info.side != Side::Neutral);
    const bool is_neutral_card = (card_info.side == Side::Neutral);
    if (is_opponent_card) {
        if (pub.defcon <= 2) {
            return true;
        }
        if (pub.defcon == 3 && pub.ar == 0) {
            return true;
        }
    }
    if (is_neutral_card && pub.ar == 0 && pub.defcon <= 3) {
        return true;
    }
    // Own DEFCON-lowering card in headline (ar==0) fires as event — self-nukes at DEFCON <= 2
    const bool is_own_card = !is_opponent_card && !is_neutral_card;
    if (is_own_card && pub.ar == 0 && pub.defcon <= 2) {
        return true;
    }
    return false;
}

[[nodiscard]] inline double winner_value(std::optional<Side> winner) {
    if (winner == Side::USSR) {
        return 1.0;
    }
    if (winner == Side::US) {
        return -1.0;
    }
    return 0.0;
}

[[nodiscard]] inline double calibrate_value(double raw_value, const MctsConfig& config) {
    if (config.calib_a == 1.0f && config.calib_b == 0.0f) {
        return raw_value;
    }
    const auto logit = static_cast<double>(config.calib_a) * raw_value + static_cast<double>(config.calib_b);
    const auto probability = 1.0 / (1.0 + std::exp(-logit));
    return 2.0 * probability - 1.0;
}

[[nodiscard]] inline bool holds_china_for(const GameState& state, Side side) {
    return side == Side::USSR ? state.ussr_holds_china : state.us_holds_china;
}

inline void sync_china_flags(GameState& state) {
    state.ussr_holds_china = state.pub.china_held_by == Side::USSR;
    state.us_holds_china = state.pub.china_held_by == Side::US;
}

inline torch::Tensor tensor_at(const torch::Tensor& tensor, int64_t index) {
    return tensor.index({index});
}

inline int argmax_index(const torch::Tensor& tensor) {
    return tensor.argmax(/*dim=*/0).item<int>();
}

inline std::vector<CountryId> accessible_countries_filtered(
    const PublicState& pub,
    Side side,
    CardId card_id,
    ActionMode mode
) {
    auto accessible = legal_countries(card_id, mode, pub, side);
    accessible.erase(
        std::remove_if(accessible.begin(), accessible.end(), [](CountryId cid) { return !has_country_spec(cid); }),
        accessible.end()
    );
    return accessible;
}

inline ActionEncoding build_action_from_country_logits(
    CardId card_id,
    ActionMode mode,
    const torch::Tensor& country_logits,
    const PublicState& pub,
    Side side,
    const torch::Tensor& strategy_logits,
    const torch::Tensor& country_strategy_logits
) {
    const auto accessible = accessible_countries_filtered(pub, side, card_id, mode);
    if (accessible.empty()) {
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}};
    }

    auto source_logits = country_logits;
    if (strategy_logits.defined() && country_strategy_logits.defined()) {
        const auto strategy_index = strategy_logits.argmax(/*dim=*/0).item<int64_t>();
        source_logits = country_strategy_logits.index({strategy_index});
    }

    auto masked = torch::full_like(source_logits, -std::numeric_limits<float>::infinity());
    for (const auto cid : accessible) {
        const auto index = static_cast<int64_t>(cid);
        masked.index_put_({index}, tensor_at(source_logits, index));
    }
    const auto probs = torch::softmax(masked, 0);

    if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
        const auto target = static_cast<CountryId>(argmax_index(probs));
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {target}};
    }

    const auto ops = effective_ops(card_id, pub, side);
    const auto accessible_indices = torch::tensor(
        std::vector<int64_t>(accessible.begin(), accessible.end()),
        torch::TensorOptions().dtype(torch::kInt64)
    );
    auto accessible_probs = probs.index({accessible_indices});
    auto alloc = accessible_probs * static_cast<double>(ops);
    auto floor_alloc = torch::floor(alloc).to(torch::kInt64);
    auto remainder = ops - static_cast<int>(floor_alloc.sum().item<int64_t>());
    if (remainder > 0) {
        auto fractional = alloc - floor_alloc.to(torch::kFloat32);
        std::vector<std::pair<float, CountryId>> order;
        order.reserve(accessible.size());
        for (size_t i = 0; i < accessible.size(); ++i) {
            const auto index = static_cast<int64_t>(i);
            order.emplace_back(-tensor_at(fractional, index).item<float>(), accessible[i]);
        }
        std::sort(order.begin(), order.end());
        for (int i = 0; i < remainder && i < static_cast<int>(order.size()); ++i) {
            const auto target = order[static_cast<size_t>(i)].second;
            const auto pos = static_cast<long long>(
                std::find(accessible.begin(), accessible.end(), target) - accessible.begin()
            );
            const auto pos64 = static_cast<int64_t>(pos);
            floor_alloc.index_put_({pos64}, tensor_at(floor_alloc, pos64).item<int64_t>() + 1);
        }
    }

    ActionEncoding action{.card_id = card_id, .mode = mode, .targets = {}};
    for (size_t i = 0; i < accessible.size(); ++i) {
        const auto index = static_cast<int64_t>(i);
        const auto count = tensor_at(floor_alloc, index).item<int64_t>();
        for (int64_t j = 0; j < count; ++j) {
            action.targets.push_back(accessible[i]);
        }
    }
    return action;
}

inline ActionEncoding fallback_resolved_action(const ActionEncoding& action, const PublicState& pub, Side side) {
    const auto accessible = accessible_countries_filtered(pub, side, action.card_id, action.mode);
    if (accessible.empty()) {
        return action;
    }

    if (action.mode == ActionMode::Coup || action.mode == ActionMode::Realign) {
        return ActionEncoding{.card_id = action.card_id, .mode = action.mode, .targets = {accessible.front()}};
    }

    ActionEncoding resolved{.card_id = action.card_id, .mode = action.mode, .targets = {}};
    const auto ops = effective_ops(action.card_id, pub, side);
    resolved.targets.assign(static_cast<size_t>(ops), accessible.front());
    return resolved;
}

inline ActionEncoding resolve_edge_action(
    const ActionEncoding& action,
    const PublicState& pub,
    Side side,
    const torch::Tensor& country_logits,
    const torch::Tensor& strategy_logits,
    const torch::Tensor& country_strategy_logits
) {
    if (action.mode != ActionMode::Influence) {
        return action;
    }
    if (country_logits.defined()) {
        auto resolved = build_action_from_country_logits(
            action.card_id,
            action.mode,
            country_logits,
            pub,
            side,
            strategy_logits,
            country_strategy_logits
        );
        if (!resolved.targets.empty()) {
            return resolved;
        }
    }
    return fallback_resolved_action(action, pub, side);
}

inline void apply_tree_action(GameState& state, const ActionEncoding& action, Pcg64Rng& rng) {
    const auto side = state.pub.phasing;
    auto& hand = state.hands[to_index(side)];
    if (hand.test(action.card_id)) {
        hand.reset(action.card_id);
    }

    auto [new_pub, over, winner] = apply_action_live(state, action, side, rng);
    state.pub = new_pub;
    sync_china_flags(state);
    state.game_over = over;
    state.winner = winner;
    state.current_side = over ? side : other_side(side);
    if (!over) {
        state.pub.phasing = other_side(side);
    }
}

inline double rollout_value(const GameState& state, const MctsConfig& config, Pcg64Rng& rng) {
    (void)config.rollout_depth_limit;
    const PolicyFn heuristic = [](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& local_rng) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, local_rng);
    };
    const auto result = play_game_from_mid_state_fn(state, heuristic, heuristic, rng.next_u32());
    return winner_value(result.winner);
}

inline double evaluate_leaf_value(
    const GameState& state,
    const torch::Tensor& value_tensor,
    int64_t batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto value = value_tensor.index({batch_index, 0}).item<double>();
    value = calibrate_value(value, config);
    if (!config.use_rollout_backup) {
        return value;
    }
    const auto rollout = rollout_value(state, config, rng);
    return static_cast<double>(config.value_weight) * value +
        static_cast<double>(1.0f - config.value_weight) * rollout;
}

inline std::vector<CardDraft> collect_card_drafts(const GameState& state) {
    const auto side = state.pub.phasing;
    const auto holds_china = holds_china_for(state, side);
    std::vector<CardDraft> cards;

    for (const auto card_id : legal_cards(state.hands[to_index(side)], state.pub, side, holds_china)) {
        if (is_card_blocked_by_defcon(state.pub, side, card_id)) {
            continue;
        }

        CardDraft card{.card_id = card_id, .modes = {}};
        for (const auto mode : legal_modes(card_id, state.pub, side)) {
            if (mode == ActionMode::Coup && state.pub.defcon <= 2) {
                continue;
            }
            if (mode == ActionMode::Event && state.pub.defcon <= 2 && is_defcon_lowering_card(card_id)) {
                continue;
            }

            ModeDraft mode_draft{.mode = mode, .edges = {}};
            if (mode == ActionMode::Event || mode == ActionMode::Space || mode == ActionMode::Influence) {
                mode_draft.edges.push_back(ActionEncoding{
                    .card_id = card_id,
                    .mode = mode,
                    .targets = {},
                });
            } else {
                auto countries = legal_countries(card_id, mode, state.pub, side);
                countries.erase(
                    std::remove_if(countries.begin(), countries.end(), [](CountryId cid) { return !has_country_spec(cid); }),
                    countries.end()
                );
                for (const auto country : countries) {
                    mode_draft.edges.push_back(ActionEncoding{
                        .card_id = card_id,
                        .mode = mode,
                        .targets = {country},
                    });
                }
            }

            if (!mode_draft.edges.empty()) {
                card.modes.push_back(std::move(mode_draft));
            }
        }

        if (!card.modes.empty()) {
            cards.push_back(std::move(card));
        }
    }

    return cards;
}

inline std::optional<ExpansionResult> expand_without_model(const GameState& state, Pcg64Rng& rng) {
    auto node = std::make_unique<MctsNode>();
    node->side_to_move = state.pub.phasing;

    if (state.game_over) {
        node->is_terminal = true;
        const auto terminal_value = winner_value(state.winner);
        node->terminal_value = terminal_value;
        return ExpansionResult{.node = std::move(node), .leaf_value = terminal_value};
    }

    const auto drafts = collect_card_drafts(state);
    if (!drafts.empty()) {
        return std::nullopt;
    }

    if (auto fallback = choose_action(
            PolicyKind::MinimalHybrid,
            state.pub,
            state.hands[to_index(state.pub.phasing)],
            holds_china_for(state, state.pub.phasing),
            rng
        );
        fallback.has_value()) {
        node->edges.push_back(MctsEdge{.action = *fallback, .prior = 1.0f});
        node->children.emplace_back(nullptr);
        node->applied_actions.push_back(*fallback);
        return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
    }

    node->is_terminal = true;
    return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
}

inline ExpansionResult expand_from_outputs(
    const GameState& state,
    const nn::BatchOutputs& outputs,
    int64_t batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto node = std::make_unique<MctsNode>();
    node->side_to_move = state.pub.phasing;

    const auto drafts = collect_card_drafts(state);
    const auto card_logits = outputs.card_logits.index({batch_index});
    const auto mode_logits = outputs.mode_logits.index({batch_index});
    const auto country_logits = outputs.country_logits.defined() ? outputs.country_logits.index({batch_index}) : torch::Tensor{};
    const auto strategy_logits = outputs.strategy_logits.defined() ? outputs.strategy_logits.index({batch_index}) : torch::Tensor{};
    const auto country_strategy_logits = outputs.country_strategy_logits.defined()
        ? outputs.country_strategy_logits.index({batch_index})
        : torch::Tensor{};

    auto masked_card = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto& card : drafts) {
        masked_card.index_put_({static_cast<int64_t>(card.card_id - 1)}, tensor_at(card_logits, card.card_id - 1));
    }
    const auto card_probs = torch::softmax(masked_card, 0);

    double total_prior = 0.0;
    for (const auto& card : drafts) {
        auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto& mode : card.modes) {
            masked_mode.index_put_({static_cast<int64_t>(mode.mode)}, tensor_at(mode_logits, static_cast<int>(mode.mode)));
        }
        const auto mode_probs = torch::softmax(masked_mode, 0);
        const auto card_prob = tensor_at(card_probs, card.card_id - 1).item<double>();

        for (const auto& mode : card.modes) {
            const auto mode_prob = tensor_at(mode_probs, static_cast<int>(mode.mode)).item<double>();
            if ((mode.mode == ActionMode::Coup || mode.mode == ActionMode::Realign) && country_logits.defined()) {
                auto masked_country = torch::full_like(country_logits, -std::numeric_limits<float>::infinity());
                for (const auto& edge : mode.edges) {
                    const auto country = edge.targets.front();
                    masked_country.index_put_({static_cast<int64_t>(country)}, tensor_at(country_logits, country));
                }
                const auto country_probs = torch::softmax(masked_country, 0);
                for (const auto& edge : mode.edges) {
                    const auto country = edge.targets.front();
                    const auto prior = card_prob * mode_prob * tensor_at(country_probs, country).item<double>();
                    node->edges.push_back(MctsEdge{
                        .action = edge,
                        .prior = static_cast<float>(prior),
                    });
                    node->children.emplace_back(nullptr);
                    node->applied_actions.push_back(edge);
                    total_prior += prior;
                }
                continue;
            }

            const auto per_edge_prior = card_prob * mode_prob;
            for (const auto& edge : mode.edges) {
                node->edges.push_back(MctsEdge{
                    .action = edge,
                    .prior = static_cast<float>(per_edge_prior),
                });
                node->children.emplace_back(nullptr);
                node->applied_actions.push_back(resolve_edge_action(
                    edge,
                    state.pub,
                    state.pub.phasing,
                    country_logits,
                    strategy_logits,
                    country_strategy_logits
                ));
                total_prior += per_edge_prior;
            }
        }
    }

    if (node->edges.empty()) {
        if (auto fallback = choose_action(
                PolicyKind::MinimalHybrid,
                state.pub,
                state.hands[to_index(state.pub.phasing)],
                holds_china_for(state, state.pub.phasing),
                rng
            );
            fallback.has_value()) {
            node->edges.push_back(MctsEdge{.action = *fallback, .prior = 1.0f});
            node->children.emplace_back(nullptr);
            node->applied_actions.push_back(*fallback);
            return ExpansionResult{
                .node = std::move(node),
                .leaf_value = evaluate_leaf_value(state, outputs.value, batch_index, config, rng),
            };
        }

        node->is_terminal = true;
        return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
    }

    if (total_prior > 0.0) {
        for (auto& edge : node->edges) {
            edge.prior = static_cast<float>(edge.prior / total_prior);
        }
    } else {
        const auto uniform = 1.0f / static_cast<float>(node->edges.size());
        for (auto& edge : node->edges) {
            edge.prior = uniform;
        }
    }

    return ExpansionResult{
        .node = std::move(node),
        .leaf_value = evaluate_leaf_value(state, outputs.value, batch_index, config, rng),
    };
}

template <typename Slot>
inline void backpropagate(Slot& slot, double leaf_value, int virtual_loss_weight) {
    for (auto it = slot.path.rbegin(); it != slot.path.rend(); ++it) {
        auto* ancestor = it->first;
        auto& edge = ancestor->edges[static_cast<size_t>(it->second)];
        edge.virtual_loss = std::max(0, edge.virtual_loss - virtual_loss_weight);
        edge.visit_count += 1;
        edge.total_value += leaf_value;
        ancestor->total_visits += 1;
    }
    slot.path.clear();
}

template <typename Slot>
inline SelectionResult select_to_leaf(Slot& slot, float c_puct, int virtual_loss_weight) {
    slot.path.clear();
    slot.pending_expansion = false;
    slot.pending_root_expansion = false;
    slot.sim_state = clone_game_state(slot.root_state);

    MctsNode* node = slot.root.get();
    while (node != nullptr && !node->is_terminal && !node->edges.empty()) {
        const auto edge_index = node->select_edge(c_puct);
        if (edge_index < 0) {
            break;
        }

        auto& edge = node->edges[static_cast<size_t>(edge_index)];
        edge.virtual_loss += virtual_loss_weight;
        slot.path.emplace_back(node, edge_index);
        apply_tree_action(slot.sim_state, node->applied_actions[static_cast<size_t>(edge_index)], slot.rng);
        if (node->children[static_cast<size_t>(edge_index)] == nullptr) {
            if (auto immediate = expand_without_model(slot.sim_state, slot.rng); immediate.has_value()) {
                node->children[static_cast<size_t>(edge_index)] = std::move(immediate->node);
                return SelectionResult{.needs_batch = false, .leaf_value = immediate->leaf_value};
            }
            slot.pending_expansion = true;
            return SelectionResult{.needs_batch = true};
        }
        node = node->children[static_cast<size_t>(edge_index)].get();
    }

    if (node != nullptr && node->is_terminal) {
        return SelectionResult{.needs_batch = false, .leaf_value = node->terminal_value};
    }
    return SelectionResult{.needs_batch = false, .leaf_value = 0.0};
}

}  // namespace ts::search_impl

#endif
