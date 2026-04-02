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
#include "mcts.hpp"
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

struct SelectionResult {
    bool needs_batch = false;
    double leaf_value = 0.0;
};

struct AggregatedVisitCount {
    CardId card_id = 0;
    ActionMode mode = ActionMode::Influence;
    int visits = 0;
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
    (void)new_pub;
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

double evaluate_leaf_value(
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

std::optional<ExpansionResult> expand_without_model(const GameState& state, Pcg64Rng& rng) {
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

ExpansionResult expand_from_outputs(
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

[[nodiscard]] bool should_sample_with_temperature(const PendingDecision& decision, const BatchedMctsConfig& config) {
    return config.temperature > 0.0f && decision.move_number <= 30;
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

void backpropagate(GameSlot& slot, double leaf_value, int virtual_loss_weight) {
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

SelectionResult select_to_leaf(GameSlot& slot, const BatchedMctsConfig& config) {
    slot.path.clear();
    slot.pending_expansion = false;
    slot.pending_root_expansion = false;
    slot.sim_state = clone_game_state(slot.root_state);

    MctsNode* node = slot.root.get();
    while (node != nullptr && !node->is_terminal && !node->edges.empty()) {
        const auto edge_index = node->select_edge(config.mcts.c_puct);
        if (edge_index < 0) {
            break;
        }

        auto& edge = node->edges[static_cast<size_t>(edge_index)];
        edge.virtual_loss += config.virtual_loss_weight;
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

void initialize_slot(GameSlot& slot, int game_index, uint32_t base_seed, const BatchedMctsConfig& config) {
    const auto seed = base_seed + static_cast<uint32_t>(game_index);
    slot = GameSlot{};
    slot.active = true;
    slot.root_state = reset_game(seed);
    slot.sim_state = slot.root_state;
    slot.rng = Pcg64Rng(seed);
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
    if (action.card_id != 0 && should_sample_with_temperature(*slot.decision, config)) {
        if (const auto sampled = sample_action_by_visit_counts(search, config.temperature, slot.rng); sampled.has_value()) {
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

            const auto selection = select_to_leaf(slot, config);
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

}  // namespace ts

#endif
