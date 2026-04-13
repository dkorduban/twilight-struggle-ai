// Native PUCT MCTS with TorchScript leaf evaluation.

#include "mcts.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <cmath>
#include <cstring>
#include <limits>
#include <random>
#include <stdexcept>
#include <utility>

#include <torch/torch.h>

#include "game_data.hpp"
#include "game_loop.hpp"
#include "nn_features.hpp"
#include "policies.hpp"
#include "search_common.hpp"

namespace ts {
namespace {

constexpr int kMaxCardLogits = 112;   // kCardSlots
constexpr int kMaxModeLogits = 8;     // generous upper bound for ActionMode values
constexpr int kMaxCountryLogits = 86; // kCountrySlots
constexpr int kMaxStrategies = 8;     // generous upper bound

/// Compute softmax in-place over buf[0..n), writing probabilities back into buf.
inline void softmax_inplace(float* buf, int n) {
    float max_val = -std::numeric_limits<float>::infinity();
    for (int i = 0; i < n; ++i) {
        if (buf[i] > max_val) max_val = buf[i];
    }
    float sum = 0.0f;
    for (int i = 0; i < n; ++i) {
        buf[i] = std::exp(buf[i] - max_val);
        sum += buf[i];
    }
    if (sum > 0.0f) {
        const float inv_sum = 1.0f / sum;
        for (int i = 0; i < n; ++i) {
            buf[i] *= inv_sum;
        }
    }
}

/// Extract a contiguous float tensor slice into a stack array.
/// tensor must be 1-D and contiguous.  Returns element count (== tensor.size(0)).
inline int extract_float_array(const torch::Tensor& tensor, float* out, int max_n) {
    if (!tensor.defined()) return 0;
    const auto n = static_cast<int>(tensor.size(0));
    const int copy_n = std::min(n, max_n);
    const float* src = tensor.data_ptr<float>();
    std::memcpy(out, src, static_cast<size_t>(copy_n) * sizeof(float));
    return copy_n;
}

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

ActionEncoding build_action_from_country_logits_raw(
    CardId card_id,
    ActionMode mode,
    const float* country_logits_ptr,
    int country_logits_n,
    const PublicState& pub,
    Side side,
    const float* strategy_logits_ptr,
    int strategy_logits_n,
    const float* country_strategy_logits_ptr,
    int country_strategy_n_strategies,
    int country_strategy_n_countries
) {
    const auto accessible = accessible_countries_filtered(pub, side, card_id, mode);
    if (accessible.empty()) {
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}};
    }

    // Choose source logits: use strategy-selected slice if available, else raw country logits.
    const float* source_ptr = country_logits_ptr;
    int source_n = country_logits_n;
    float strategy_country_buf[kMaxCountryLogits];

    if (strategy_logits_ptr != nullptr && country_strategy_logits_ptr != nullptr &&
        strategy_logits_n > 0 && country_strategy_n_strategies > 0) {
        // argmax over strategy logits
        int best_strat = 0;
        float best_val = strategy_logits_ptr[0];
        for (int i = 1; i < strategy_logits_n; ++i) {
            if (strategy_logits_ptr[i] > best_val) {
                best_val = strategy_logits_ptr[i];
                best_strat = i;
            }
        }
        // Extract the row: country_strategy_logits is [n_strategies, n_countries]
        const int row_offset = best_strat * country_strategy_n_countries;
        const int copy_n = std::min(country_strategy_n_countries, kMaxCountryLogits);
        std::memcpy(strategy_country_buf, country_strategy_logits_ptr + row_offset,
                     static_cast<size_t>(copy_n) * sizeof(float));
        source_ptr = strategy_country_buf;
        source_n = copy_n;
    }

    // Build masked softmax over accessible countries
    float masked[kMaxCountryLogits];
    std::fill(masked, masked + kMaxCountryLogits, -std::numeric_limits<float>::infinity());
    for (const auto cid : accessible) {
        const int idx = static_cast<int>(cid);
        if (idx < source_n) {
            masked[idx] = source_ptr[idx];
        }
    }
    softmax_inplace(masked, std::min(source_n, kMaxCountryLogits));

    if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
        // argmax over masked probs
        int best_idx = 0;
        float best_prob = -1.0f;
        for (const auto cid : accessible) {
            const int idx = static_cast<int>(cid);
            if (masked[idx] > best_prob) {
                best_prob = masked[idx];
                best_idx = idx;
            }
        }
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {static_cast<CountryId>(best_idx)}};
    }

    // Influence placement: proportional allocation of ops
    const auto ops = effective_ops(card_id, pub, side);

    // Get accessible probs and compute allocation
    float acc_probs[kMaxCountryLogits];
    float alloc_f[kMaxCountryLogits];
    int alloc_i[kMaxCountryLogits];
    const int n_acc = static_cast<int>(accessible.size());

    int floor_sum = 0;
    for (int i = 0; i < n_acc; ++i) {
        acc_probs[i] = masked[static_cast<int>(accessible[static_cast<size_t>(i)])];
        alloc_f[i] = acc_probs[i] * static_cast<float>(ops);
        alloc_i[i] = static_cast<int>(std::floor(alloc_f[i]));
        floor_sum += alloc_i[i];
    }

    int remainder = ops - floor_sum;
    if (remainder > 0) {
        // Sort by fractional part descending, break ties by country id
        std::pair<float, int> order[kMaxCountryLogits];
        for (int i = 0; i < n_acc; ++i) {
            const float fractional = alloc_f[i] - static_cast<float>(alloc_i[i]);
            order[i] = {-fractional, i};
        }
        std::sort(order, order + n_acc);
        for (int i = 0; i < remainder && i < n_acc; ++i) {
            alloc_i[order[i].second] += 1;
        }
    }

    ActionEncoding action{.card_id = card_id, .mode = mode, .targets = {}};
    for (int i = 0; i < n_acc; ++i) {
        for (int j = 0; j < alloc_i[i]; ++j) {
            action.targets.push_back(accessible[static_cast<size_t>(i)]);
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

ActionEncoding resolve_edge_action_raw(
    const ActionEncoding& action,
    const PublicState& pub,
    Side side,
    const float* country_logits_ptr,
    int country_logits_n,
    const float* strategy_logits_ptr,
    int strategy_logits_n,
    const float* country_strategy_logits_ptr,
    int country_strategy_n_strategies,
    int country_strategy_n_countries
) {
    if (action.mode != ActionMode::Influence) {
        return action;
    }
    if (country_logits_ptr != nullptr) {
        auto resolved = build_action_from_country_logits_raw(
            action.card_id,
            action.mode,
            country_logits_ptr,
            country_logits_n,
            pub,
            side,
            strategy_logits_ptr,
            strategy_logits_n,
            country_strategy_logits_ptr,
            country_strategy_n_strategies,
            country_strategy_n_countries
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

    // --- NN forward (only torch call in hot path) ---
    const auto outputs = nn::forward_model(
        model,
        state.pub,
        state.hands[to_index(state.pub.phasing)],
        holds_china_for(state, state.pub.phasing),
        state.pub.phasing
    );

    // --- Extract raw float arrays from tensors ONCE ---
    const auto card_logits_t = get_tensor(outputs, "card_logits").index({0}).contiguous();
    const auto mode_logits_t = get_tensor(outputs, "mode_logits").index({0}).contiguous();
    const auto country_logits_raw_t = get_tensor(outputs, "country_logits", false);
    const auto strategy_logits_raw_t = get_tensor(outputs, "strategy_logits", false);
    const auto country_strategy_logits_raw_t = get_tensor(outputs, "country_strategy_logits", false);

    float card_logits_arr[kMaxCardLogits];
    float mode_logits_arr[kMaxModeLogits];
    float country_logits_arr[kMaxCountryLogits];
    float strategy_logits_arr[kMaxStrategies];
    float country_strategy_logits_arr[kMaxStrategies * kMaxCountryLogits];

    const int n_card = extract_float_array(card_logits_t, card_logits_arr, kMaxCardLogits);
    const int n_mode = extract_float_array(mode_logits_t, mode_logits_arr, kMaxModeLogits);

    const float* country_logits_ptr = nullptr;
    int n_country = 0;
    const float* strategy_logits_ptr = nullptr;
    int n_strategy = 0;
    const float* country_strategy_ptr = nullptr;
    int cs_n_strategies = 0;
    int cs_n_countries = 0;

    if (country_logits_raw_t.defined()) {
        auto cl = country_logits_raw_t.index({0}).contiguous();
        n_country = extract_float_array(cl, country_logits_arr, kMaxCountryLogits);
        country_logits_ptr = country_logits_arr;
    }
    if (strategy_logits_raw_t.defined()) {
        auto sl = strategy_logits_raw_t.index({0}).contiguous();
        n_strategy = extract_float_array(sl, strategy_logits_arr, kMaxStrategies);
        strategy_logits_ptr = strategy_logits_arr;
    }
    if (country_strategy_logits_raw_t.defined()) {
        auto csl = country_strategy_logits_raw_t.index({0}).contiguous();
        cs_n_strategies = static_cast<int>(csl.size(0));
        cs_n_countries = static_cast<int>(csl.size(1));
        const int total = std::min(cs_n_strategies * cs_n_countries, kMaxStrategies * kMaxCountryLogits);
        std::memcpy(country_strategy_logits_arr, csl.data_ptr<float>(),
                     static_cast<size_t>(total) * sizeof(float));
        country_strategy_ptr = country_strategy_logits_arr;
    }

    // --- Masked card softmax using raw arrays ---
    float masked_card[kMaxCardLogits];
    std::fill(masked_card, masked_card + n_card, -std::numeric_limits<float>::infinity());
    for (const auto& card : drafts) {
        const int idx = static_cast<int>(card.card_id) - 1;
        if (idx >= 0 && idx < n_card) {
            masked_card[idx] = card_logits_arr[idx];
        }
    }
    softmax_inplace(masked_card, n_card);

    // --- Build edges with raw float math ---
    double total_prior = 0.0;
    for (const auto& card : drafts) {
        // Masked mode softmax (recomputed per card since legal modes vary)
        float masked_mode[kMaxModeLogits];
        std::fill(masked_mode, masked_mode + n_mode, -std::numeric_limits<float>::infinity());
        for (const auto& mode : card.modes) {
            const int midx = static_cast<int>(mode.mode);
            if (midx < n_mode) {
                masked_mode[midx] = mode_logits_arr[midx];
            }
        }
        softmax_inplace(masked_mode, n_mode);

        const int cidx = static_cast<int>(card.card_id) - 1;
        const double card_prob = (cidx >= 0 && cidx < n_card) ? static_cast<double>(masked_card[cidx]) : 0.0;

        for (const auto& mode : card.modes) {
            const int midx = static_cast<int>(mode.mode);
            const double mode_prob = (midx < n_mode) ? static_cast<double>(masked_mode[midx]) : 0.0;

            if ((mode.mode == ActionMode::Coup || mode.mode == ActionMode::Realign) &&
                country_logits_ptr != nullptr) {
                // Masked country softmax
                float masked_country[kMaxCountryLogits];
                std::fill(masked_country, masked_country + n_country, -std::numeric_limits<float>::infinity());
                for (const auto& edge : mode.edges) {
                    const int ci = static_cast<int>(edge.targets.front());
                    if (ci < n_country) {
                        masked_country[ci] = country_logits_arr[ci];
                    }
                }
                softmax_inplace(masked_country, n_country);

                for (const auto& edge : mode.edges) {
                    const int ci = static_cast<int>(edge.targets.front());
                    const double country_prob = (ci < n_country) ? static_cast<double>(masked_country[ci]) : 0.0;
                    const auto prior = card_prob * mode_prob * country_prob;
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
                node->applied_actions.push_back(resolve_edge_action_raw(
                    edge,
                    state.pub,
                    state.pub.phasing,
                    country_logits_ptr,
                    n_country,
                    strategy_logits_ptr,
                    n_strategy,
                    country_strategy_ptr,
                    cs_n_strategies,
                    cs_n_countries
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
