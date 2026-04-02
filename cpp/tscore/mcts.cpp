// Native PUCT MCTS with TorchScript leaf evaluation.

#include "mcts.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <cmath>
#include <limits>
#include <random>
#include <stdexcept>
#include <utility>

#include <torch/torch.h>

#include "game_data.hpp"
#include "game_loop.hpp"
#include "nn_features.hpp"
#include "policies.hpp"

namespace ts {
namespace {

constexpr std::array<int, 13> kDefconLoweringCards = {
    4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105,
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

[[nodiscard]] bool is_defcon_lowering_card(CardId card_id) {
    return std::find(kDefconLoweringCards.begin(), kDefconLoweringCards.end(), static_cast<int>(card_id)) !=
        kDefconLoweringCards.end();
}

[[nodiscard]] bool is_card_blocked_by_defcon(const PublicState& pub, Side side, CardId card_id) {
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
    return false;
}

[[nodiscard]] double winner_value(std::optional<Side> winner) {
    if (winner == Side::USSR) {
        return 1.0;
    }
    if (winner == Side::US) {
        return -1.0;
    }
    return 0.0;
}

[[nodiscard]] double calibrate_value(double raw_value, const MctsConfig& config) {
    if (config.calib_a == 1.0f && config.calib_b == 0.0f) {
        return raw_value;
    }
    const auto logit = static_cast<double>(config.calib_a) * raw_value + static_cast<double>(config.calib_b);
    const auto probability = 1.0 / (1.0 + std::exp(-logit));
    return 2.0 * probability - 1.0;
}

[[nodiscard]] bool holds_china_for(const GameState& state, Side side) {
    return side == Side::USSR ? state.ussr_holds_china : state.us_holds_china;
}

void sync_china_flags(GameState& state) {
    state.ussr_holds_china = state.pub.china_held_by == Side::USSR;
    state.us_holds_china = state.pub.china_held_by == Side::US;
}

torch::Tensor get_tensor(const c10::impl::GenericDict& dict, const char* key, bool required = true) {
    const auto key_value = c10::IValue(std::string(key));
    if (!dict.contains(key_value)) {
        if (required) {
            throw std::runtime_error(std::string("missing model output key: ") + key);
        }
        return {};
    }
    return dict.at(key_value).toTensor();
}

torch::Tensor tensor_at(const torch::Tensor& tensor, int64_t index) {
    return tensor.index({index});
}

int argmax_index(const torch::Tensor& tensor) {
    return tensor.argmax(/*dim=*/0).item<int>();
}

std::vector<CountryId> accessible_countries_filtered(const PublicState& pub, Side side, CardId card_id, ActionMode mode) {
    auto accessible = legal_countries(card_id, mode, pub, side);
    accessible.erase(
        std::remove_if(accessible.begin(), accessible.end(), [](CountryId cid) { return !has_country_spec(cid); }),
        accessible.end()
    );
    return accessible;
}

ActionEncoding build_action_from_country_logits(
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

ActionEncoding fallback_resolved_action(const ActionEncoding& action, const PublicState& pub, Side side) {
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

ActionEncoding resolve_edge_action(
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

void apply_tree_action(GameState& state, const ActionEncoding& action, Pcg64Rng& rng) {
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

double rollout_value(const GameState& state, const MctsConfig& config, Pcg64Rng& rng) {
    (void)config.rollout_depth_limit;
    const PolicyFn heuristic = [](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& local_rng) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, local_rng);
    };
    const auto result = play_game_from_mid_state_fn(state, heuristic, heuristic, rng.next_u32());
    return winner_value(result.winner);
}

double evaluate(
    const GameState& state,
    const c10::impl::GenericDict& outputs,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto value = get_tensor(outputs, "value").index({0, 0}).item<double>();
    value = calibrate_value(value, config);
    if (!config.use_rollout_backup) {
        return value;
    }
    const auto rollout = rollout_value(state, config, rng);
    return static_cast<double>(config.value_weight) * value +
        static_cast<double>(1.0f - config.value_weight) * rollout;
}

std::vector<CardDraft> collect_card_drafts(const GameState& state) {
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

ExpansionResult expand(
    const GameState& state,
    torch::jit::script::Module& model,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto node = std::make_unique<MctsNode>();
    node->side_to_move = state.pub.phasing;

    if (state.game_over) {
        node->is_terminal = true;
        const auto terminal_value = winner_value(state.winner);
        node->terminal_value = terminal_value;
        return {.node = std::move(node), .leaf_value = terminal_value};
    }

    const auto drafts = collect_card_drafts(state);
    if (drafts.empty()) {
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
            return {.node = std::move(node), .leaf_value = 0.0};
        }

        node->is_terminal = true;
        return {.node = std::move(node), .leaf_value = 0.0};
    }

    const auto outputs = nn::forward_model(
        model,
        state.pub,
        state.hands[to_index(state.pub.phasing)],
        holds_china_for(state, state.pub.phasing),
        state.pub.phasing
    );
    const auto card_logits = get_tensor(outputs, "card_logits").index({0});
    const auto mode_logits = get_tensor(outputs, "mode_logits").index({0});
    const auto country_logits_raw = get_tensor(outputs, "country_logits", false);
    const auto strategy_logits_raw = get_tensor(outputs, "strategy_logits", false);
    const auto country_strategy_logits_raw = get_tensor(outputs, "country_strategy_logits", false);
    const auto country_logits = country_logits_raw.defined() ? country_logits_raw.index({0}) : torch::Tensor{};
    const auto strategy_logits = strategy_logits_raw.defined() ? strategy_logits_raw.index({0}) : torch::Tensor{};
    const auto country_strategy_logits = country_strategy_logits_raw.defined()
        ? country_strategy_logits_raw.index({0})
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
            return {.node = std::move(node), .leaf_value = evaluate(state, outputs, config, rng)};
        }

        node->is_terminal = true;
        return {.node = std::move(node), .leaf_value = 0.0};
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

    return {.node = std::move(node), .leaf_value = evaluate(state, outputs, config, rng)};
}

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

}  // namespace

void apply_root_dirichlet_noise(MctsNode& root, const MctsConfig& config, Pcg64Rng& rng) {
    if (config.dir_epsilon <= 0.0f || config.dir_alpha <= 0.0f || root.edges.empty()) {
        return;
    }

    std::vector<double> noise(root.edges.size(), 0.0);
    std::gamma_distribution<double> gamma(static_cast<double>(config.dir_alpha), 1.0);

    double total_noise = 0.0;
    for (auto& sample : noise) {
        sample = gamma(rng);
        total_noise += sample;
    }

    if (total_noise <= 0.0) {
        const auto uniform = 1.0 / static_cast<double>(noise.size());
        std::fill(noise.begin(), noise.end(), uniform);
    } else {
        for (auto& sample : noise) {
            sample /= total_noise;
        }
    }

    const auto epsilon = static_cast<double>(config.dir_epsilon);
    const auto keep = 1.0 - epsilon;
    for (size_t i = 0; i < root.edges.size(); ++i) {
        root.edges[i].prior = static_cast<float>(keep * static_cast<double>(root.edges[i].prior) + epsilon * noise[i]);
    }
}

int MctsNode::select_edge(float c_puct) const {
    if (edges.empty()) {
        return -1;
    }

    constexpr double kVirtualLossPenalty = 1.0;
    int pending_visits = 0;
    for (const auto& edge : edges) {
        pending_visits += edge.virtual_loss;
    }

    const auto parent_visits = std::sqrt(static_cast<double>(std::max(1, total_visits + pending_visits)));
    int best_index = 0;
    double best_score = -std::numeric_limits<double>::infinity();
    for (size_t i = 0; i < edges.size(); ++i) {
        const auto& edge = edges[i];
        const auto effective_visits = edge.visit_count + edge.virtual_loss;
        const auto virtual_loss_term = static_cast<double>(edge.virtual_loss) * kVirtualLossPenalty;
        const auto effective_total_value = edge.total_value +
            (side_to_move == Side::US ? virtual_loss_term : -virtual_loss_term);
        auto q = effective_visits > 0 ? effective_total_value / static_cast<double>(effective_visits) : 0.0;
        if (side_to_move == Side::US) {
            q = -q;
        }
        const auto u = static_cast<double>(c_puct) * static_cast<double>(edge.prior) * parent_visits /
            static_cast<double>(1 + effective_visits);
        const auto score = q + u;
        if (score > best_score) {
            best_score = score;
            best_index = static_cast<int>(i);
        }
    }
    return best_index;
}

SearchResult mcts_search(
    const GameState& root_state,
    torch::jit::script::Module& model,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto root_expansion = expand(root_state, model, config, rng);
    auto root = std::move(root_expansion.node);
    apply_root_dirichlet_noise(*root, config, rng);

    for (int sim = 0; sim < config.n_simulations; ++sim) {
        auto state = clone_game_state(root_state);
        MctsNode* node = root.get();
        std::vector<std::pair<MctsNode*, int>> path;

        while (node != nullptr && !node->is_terminal && !node->edges.empty()) {
            const auto edge_index = node->select_edge(config.c_puct);
            if (edge_index < 0) {
                break;
            }
            path.emplace_back(node, edge_index);
            apply_tree_action(state, node->applied_actions[static_cast<size_t>(edge_index)], rng);
            if (node->children[static_cast<size_t>(edge_index)] == nullptr) {
                break;
            }
            node = node->children[static_cast<size_t>(edge_index)].get();
        }

        double leaf_value = 0.0;
        if (node != nullptr && node->is_terminal) {
            leaf_value = node->terminal_value;
        } else if (!path.empty()) {
            auto& [parent, edge_index] = path.back();
            auto child_expansion = expand(state, model, config, rng);
            leaf_value = child_expansion.leaf_value;
            parent->children[static_cast<size_t>(edge_index)] = std::move(child_expansion.node);
        } else if (root->is_terminal) {
            leaf_value = root->terminal_value;
        }

        for (auto it = path.rbegin(); it != path.rend(); ++it) {
            auto* ancestor = it->first;
            auto& edge = ancestor->edges[static_cast<size_t>(it->second)];
            edge.visit_count += 1;
            edge.total_value += leaf_value;
            ancestor->total_visits += 1;
        }
    }

    SearchResult result;
    result.root_edges = root->edges;
    result.root_value = mean_root_value(*root);
    result.total_simulations = config.n_simulations;

    const auto best_index = best_root_edge_index(*root);
    if (best_index >= 0) {
        result.best_action = root->applied_actions[static_cast<size_t>(best_index)];
    }
    return result;
}

}  // namespace ts

#endif
