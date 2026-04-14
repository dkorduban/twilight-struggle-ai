// Shared NN decode helpers used by TorchScriptPolicy (learned_policy.cpp)
// and batched MCTS rollout/greedy decode (mcts_batched.cpp). Single source
// of truth for masked card/mode/country decode semantics.
//
// All functions are inline and intended for .cpp inclusion only.

#pragma once

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <limits>
#include <optional>
#include <set>
#include <type_traits>
#include <utility>
#include <vector>

#include <torch/torch.h>

#include "dp_decoder.hpp"
#include "game_data.hpp"
#include "legal_actions.hpp"
#include "rng.hpp"
#include "scoring.hpp"
#include "search_common.hpp"

namespace ts::decode {

inline torch::Tensor tensor_at(const torch::Tensor& tensor, int64_t index) {
    return tensor.index({index});
}

inline int argmax_index(const torch::Tensor& tensor) {
    return tensor.argmax(/*dim=*/0).item<int>();
}

[[nodiscard]] inline bool requires_defcon_fallback(
    const PublicState& pub,
    Side side,
    CardId card_id,
    ActionMode mode
) {
    if (pub.defcon > 2 || !ts::is_defcon_lowering_card(card_id)) {
        return false;
    }

    const auto& card_info = card_spec(card_id);
    const bool event_fires_for_any_mode = (card_info.side != side && card_info.side != Side::Neutral);
    const bool event_fires_for_event_space =
        (mode == ActionMode::Event) ||
        (mode == ActionMode::Space && event_fires_for_any_mode);
    return event_fires_for_any_mode || event_fires_for_event_space;
}

struct DecodeLogProbs {
    float card_lp = 0.0f;
    float mode_lp = 0.0f;
    float country_lp = 0.0f;
};

struct DecodeTrace {
    torch::Tensor card_mask;
    torch::Tensor mode_mask;
    torch::Tensor country_mask;
    int card_idx = -1;
    int mode_idx = -1;
    std::vector<int> country_targets;
};

struct DecodeWithLogProbsResult {
    ActionEncoding action;
    DecodeTrace trace;
    DecodeLogProbs log_probs;
    bool needs_fallback = false;
    bool should_populate_rollout_features = false;
};

inline torch::Tensor build_masked_card_logits(
    const PublicState& pub,
    Side side,
    const torch::Tensor& card_logits,
    const std::vector<CardId>& playable,
    torch::Tensor* mask = nullptr
) {
    auto masked = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto card_id : playable) {
        if (is_card_blocked_by_defcon(pub, side, card_id)) {
            continue;
        }
        const auto index = static_cast<int64_t>(card_id - 1);
        if (mask != nullptr) {
            mask->index_put_({index}, true);
        }
        masked.index_put_({index}, tensor_at(card_logits, index));
    }
    return masked;
}

inline bool has_any_unmasked_card(const std::vector<CardId>& playable, const torch::Tensor& masked_card) {
    for (const auto card_id : playable) {
        const auto index = static_cast<int64_t>(card_id - 1);
        if (tensor_at(masked_card, index).item<float>() > -std::numeric_limits<float>::infinity()) {
            return true;
        }
    }
    return false;
}

inline torch::Tensor build_masked_mode_logits(
    const torch::Tensor& mode_logits,
    const std::vector<ActionMode>& modes,
    torch::Tensor* mask = nullptr
) {
    auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
    const auto n_mode_logits = mode_logits.size(0);
    for (const auto mode : modes) {
        const auto index = static_cast<int64_t>(static_cast<int>(mode));
        if (index >= n_mode_logits) {
            continue;
        }
        if (mask != nullptr) {
            mask->index_put_({index}, true);
        }
        masked_mode.index_put_({index}, tensor_at(mode_logits, index));
    }
    return masked_mode;
}

inline void erase_mode(std::vector<ActionMode>& modes, ActionMode mode) {
    modes.erase(std::remove(modes.begin(), modes.end(), mode), modes.end());
}

inline std::pair<int64_t, float> sample_index_from_masked_logits(
    const torch::Tensor& masked,
    float temperature
) {
    auto scaled = masked / temperature;
    auto probs = torch::softmax(scaled, 0);
    const auto sampled_idx = torch::multinomial(probs, 1).item<int64_t>();
    const auto log_prob = torch::log_softmax(masked, 0).index({sampled_idx}).item<float>();
    return {sampled_idx, log_prob};
}

inline DecodeTrace make_decode_trace(const torch::Tensor& mode_logits) {
    const auto bool_opts = torch::TensorOptions().dtype(torch::kBool);
    DecodeTrace trace;
    trace.card_mask = torch::zeros({kMaxCardId}, bool_opts);
    trace.mode_mask = torch::zeros({mode_logits.size(0)}, bool_opts);
    trace.country_mask = torch::zeros({kCountrySlots}, bool_opts);
    return trace;
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

inline ActionEncoding build_action_from_marginal_logits(
    CardId card_id,
    ActionMode mode,
    const torch::Tensor& marginal_logits,
    const PublicState& pub,
    Side side,
    int t_max = 4
) {
    const auto accessible = accessible_countries_filtered(pub, side, card_id, mode);
    if (accessible.empty() || !marginal_logits.defined() || marginal_logits.numel() == 0 || marginal_logits.dim() != 2) {
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}};
    }

    const auto country_count = static_cast<int>(marginal_logits.size(0));
    const auto marginal_steps = std::min(t_max, static_cast<int>(marginal_logits.size(1)));
    if (country_count <= 0 || marginal_steps <= 0) {
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}};
    }

    if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
        auto found_target = false;
        auto best_target = CountryId{};
        auto best_logit = -std::numeric_limits<float>::infinity();
        for (const auto cid : accessible) {
            const auto country_index = static_cast<int>(cid);
            if (country_index < 0 || country_index >= country_count) {
                continue;
            }
            const auto logit =
                marginal_logits.index({static_cast<int64_t>(country_index), 0}).item<float>();
            if (!found_target || logit > best_logit) {
                found_target = true;
                best_target = cid;
                best_logit = logit;
            }
        }
        if (!found_target) {
            return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}};
        }
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {best_target}};
    }

    const auto budget = effective_ops(card_id, pub, side);
    const auto opponent = other_side(side);
    const auto accessible_set = std::set<CountryId>(accessible.begin(), accessible.end());
    std::vector<std::vector<float>> scores(static_cast<size_t>(country_count), std::vector<float>(static_cast<size_t>(marginal_steps), 0.0f));
    std::vector<bool> legal(static_cast<size_t>(country_count), false);
    const auto capped_budget = std::min(budget, marginal_steps);
    std::vector<int> cap(static_cast<size_t>(country_count), capped_budget);
    // Cost 2 for opponent-controlled countries (TS 2-ops-per-influence surcharge).
    std::vector<int> cost(static_cast<size_t>(country_count), 1);
    for (int country = 0; country < country_count; ++country) {
        const auto cid = static_cast<CountryId>(country);
        if (has_country_spec(cid) && controls_country(opponent, cid, pub)) {
            cost[static_cast<size_t>(country)] = 2;
        }
    }

    for (int country = 0; country < country_count; ++country) {
        for (int step = 0; step < marginal_steps; ++step) {
            scores[static_cast<size_t>(country)][static_cast<size_t>(step)] =
                marginal_logits.index({static_cast<int64_t>(country), static_cast<int64_t>(step)}).item<float>();
        }
        legal[static_cast<size_t>(country)] =
            accessible_set.find(static_cast<CountryId>(country)) != accessible_set.end();
    }

    const auto alloc = ts::knapsack_alloc(scores, budget, legal, cap, cost);
    ActionEncoding action{.card_id = card_id, .mode = mode, .targets = {}};
    for (int country = 0; country < country_count; ++country) {
        const auto take = alloc[static_cast<size_t>(country)];
        for (int count = 0; count < take; ++count) {
            action.targets.push_back(static_cast<CountryId>(country));
        }
    }
    return action;
}

inline ActionEncoding build_random_target_action(
    CardId card_id,
    ActionMode mode,
    const PublicState& pub,
    Side side,
    Pcg64Rng& rng
) {
    const auto accessible = accessible_countries_filtered(pub, side, card_id, mode);
    if (accessible.empty()) {
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}};
    }

    if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
        const auto target = accessible[rng.choice_index(accessible.size())];
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {target}};
    }

    const auto ops = effective_ops(card_id, pub, side);
    ActionEncoding action{.card_id = card_id, .mode = mode, .targets = {}};
    for (int i = 0; i < ops; ++i) {
        action.targets.push_back(accessible[rng.choice_index(accessible.size())]);
    }
    return action;
}

template <typename SelectCardFn, typename SelectModeFn, typename HeuristicFallbackFn, typename NoActionFn>
inline auto choose_action_from_outputs(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    bool use_country_head,
    const torch::Tensor& card_logits,
    const torch::Tensor& mode_logits,
    const torch::Tensor& country_logits,
    const torch::Tensor& strategy_logits,
    const torch::Tensor& country_strategy_logits,
    Pcg64Rng& rng,
    SelectCardFn&& select_card,
    SelectModeFn&& select_mode,
    HeuristicFallbackFn&& heuristic_fallback,
    NoActionFn&& no_action,
    const torch::Tensor& marginal_logits = torch::Tensor{}
) {
    using Result = std::invoke_result_t<NoActionFn>;
    static_assert(
        std::is_same_v<Result, std::invoke_result_t<HeuristicFallbackFn>>,
        "heuristic_fallback and no_action must return the same type"
    );

    const auto side = pub.phasing;
    auto playable = legal_cards(hand, pub, side, holds_china);
    if (playable.empty()) {
        return no_action();
    }

    auto masked_card = build_masked_card_logits(pub, side, card_logits, playable);
    if (!has_any_unmasked_card(playable, masked_card)) {
        return heuristic_fallback();
    }

    const auto sampled_card_id = static_cast<CardId>(std::forward<SelectCardFn>(select_card)(masked_card));
    auto modes = legal_modes(sampled_card_id, pub, side);
    if (modes.empty()) {
        return no_action();
    }

    auto build_masked_mode = [&]() { return build_masked_mode_logits(mode_logits, modes); };

    auto masked_mode = build_masked_mode();
    auto mode = static_cast<ActionMode>(std::forward<SelectModeFn>(select_mode)(masked_mode));

    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        erase_mode(modes, ActionMode::Coup);
        if (modes.empty()) {
            return no_action();
        }
        masked_mode = build_masked_mode();
        mode = static_cast<ActionMode>(std::forward<SelectModeFn>(select_mode)(masked_mode));
    }

    const bool is_defcon_lowering_event = pub.defcon <= 2 &&
        mode == ActionMode::Event &&
        is_defcon_lowering_card(sampled_card_id);
    if (is_defcon_lowering_event) {
        erase_mode(modes, ActionMode::Event);
        if (modes.empty()) {
            return no_action();
        }
        masked_mode = build_masked_mode();
        mode = static_cast<ActionMode>(std::forward<SelectModeFn>(select_mode)(masked_mode));
    }

    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        erase_mode(modes, ActionMode::Coup);
        if (modes.empty()) {
            return no_action();
        }
        masked_mode = build_masked_mode();
        mode = static_cast<ActionMode>(std::forward<SelectModeFn>(select_mode)(masked_mode));
    }

    if (requires_defcon_fallback(pub, side, sampled_card_id, mode)) {
        return heuristic_fallback();
    }

    if (mode == ActionMode::Event || mode == ActionMode::Space || mode == ActionMode::EventFirst) {
        return Result{ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {}}};
    }

    const auto has_marginal_logits = marginal_logits.defined() && marginal_logits.numel() > 0;
    if (use_country_head && (has_marginal_logits || country_logits.defined())) {
        ActionEncoding action;
        if (has_marginal_logits) {
            action = build_action_from_marginal_logits(
                sampled_card_id,
                mode,
                marginal_logits,
                pub,
                side
            );
        } else {
            action = build_action_from_country_logits(
                sampled_card_id,
                mode,
                country_logits,
                pub,
                side,
                strategy_logits,
                country_strategy_logits
            );
        }
        if (!action.targets.empty()) {
            return Result{std::move(action)};
        }
    }

    auto action = build_random_target_action(sampled_card_id, mode, pub, side, rng);
    if (!action.targets.empty()) {
        return Result{std::move(action)};
    }

    return heuristic_fallback();
}

inline DecodeWithLogProbsResult choose_action_from_outputs_with_logprobs(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    const torch::Tensor& card_logits,
    const torch::Tensor& mode_logits,
    const torch::Tensor& country_logits,
    float temperature
) {
    DecodeWithLogProbsResult result;
    result.trace = make_decode_trace(mode_logits);

    const auto side = pub.phasing;
    auto playable = legal_cards(hand, pub, side, holds_china);
    if (playable.empty()) {
        result.needs_fallback = true;
        return result;
    }

    auto masked_card = build_masked_card_logits(pub, side, card_logits, playable, &result.trace.card_mask);
    if (!result.trace.card_mask.any().item<bool>()) {
        result.needs_fallback = true;
        return result;
    }

    const auto [card_idx, card_lp] = sample_index_from_masked_logits(masked_card, temperature);
    const auto sampled_card_id = static_cast<CardId>(card_idx + 1);
    result.trace.card_idx = static_cast<int>(card_idx);
    result.log_probs.card_lp = card_lp;

    auto modes = legal_modes(sampled_card_id, pub, side);
    if (pub.defcon <= 2) {
        erase_mode(modes, ActionMode::Coup);
        if (is_defcon_lowering_card(sampled_card_id)) {
            erase_mode(modes, ActionMode::Event);
        }
    }
    if (modes.empty()) {
        result.needs_fallback = true;
        return result;
    }

    auto masked_mode = build_masked_mode_logits(mode_logits, modes, &result.trace.mode_mask);
    const auto [mode_idx, mode_lp] = sample_index_from_masked_logits(masked_mode, temperature);
    const auto mode = static_cast<ActionMode>(mode_idx);
    result.trace.mode_idx = static_cast<int>(mode_idx);
    result.log_probs.mode_lp = mode_lp;

    if (requires_defcon_fallback(pub, side, sampled_card_id, mode)) {
        result.needs_fallback = true;
        return result;
    }

    result.should_populate_rollout_features = true;

    if (mode == ActionMode::Event || mode == ActionMode::Space || mode == ActionMode::EventFirst) {
        result.action = ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {}};
        return result;
    }

    const auto accessible = accessible_countries_filtered(pub, side, sampled_card_id, mode);
    if (accessible.empty()) {
        result.needs_fallback = true;
        return result;
    }
    for (const auto cid : accessible) {
        result.trace.country_mask.index_put_({static_cast<int64_t>(cid)}, true);
    }

    // Rollout log-probs must be computed from the mixed country distribution
    // emitted by the model, not from a hard argmax strategy head selection.
    auto source_probs = country_logits.defined()
        ? country_logits
        : torch::zeros({kCountrySlots}, torch::TensorOptions().dtype(torch::kFloat32));
    auto masked_probs = torch::zeros_like(source_probs);
    for (const auto cid : accessible) {
        const auto index = static_cast<int64_t>(cid);
        masked_probs.index_put_({index}, tensor_at(source_probs, index));
    }

    const auto normalized_probs = masked_probs / (masked_probs.sum() + 1e-10f);
    const auto country_log_probs = torch::log(normalized_probs + 1e-10f);
    const auto country_probs = torch::softmax(country_log_probs / temperature, 0);

    ActionEncoding action{.card_id = sampled_card_id, .mode = mode, .targets = {}};
    float country_lp = 0.0f;

    if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
        const auto target = static_cast<CountryId>(torch::multinomial(country_probs, 1).item<int64_t>());
        action.targets.push_back(target);
        result.trace.country_targets.push_back(static_cast<int>(target));
        country_lp = country_log_probs.index({static_cast<int64_t>(target)}).item<float>();
    } else {
        const auto ops = effective_ops(sampled_card_id, pub, side);
        const auto accessible_indices = torch::tensor(
            std::vector<int64_t>(accessible.begin(), accessible.end()),
            torch::TensorOptions().dtype(torch::kInt64)
        );
        auto accessible_probs = country_probs.index({accessible_indices});
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

        for (size_t i = 0; i < accessible.size(); ++i) {
            const auto index = static_cast<int64_t>(i);
            const auto count = tensor_at(floor_alloc, index).item<int64_t>();
            for (int64_t j = 0; j < count; ++j) {
                action.targets.push_back(accessible[i]);
                result.trace.country_targets.push_back(static_cast<int>(accessible[i]));
                country_lp += country_log_probs.index({static_cast<int64_t>(accessible[i])}).item<float>();
            }
        }
    }

    if (action.targets.empty()) {
        result.needs_fallback = true;
        return result;
    }

    result.action = std::move(action);
    result.log_probs.country_lp = country_lp;
    return result;
}

}  // namespace ts::decode

#endif
