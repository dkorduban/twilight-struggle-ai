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
#include <type_traits>
#include <utility>
#include <vector>

#include <torch/torch.h>

#include "game_data.hpp"
#include "legal_actions.hpp"
#include "rng.hpp"

namespace ts::decode {

inline constexpr std::array<int, 13> kDefconLoweringCards = {
    4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105,
};

inline torch::Tensor tensor_at(const torch::Tensor& tensor, int64_t index) {
    return tensor.index({index});
}

inline int argmax_index(const torch::Tensor& tensor) {
    return tensor.argmax(/*dim=*/0).item<int>();
}

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
    return false;
}

[[nodiscard]] inline bool requires_defcon_fallback(
    const PublicState& pub,
    Side side,
    CardId card_id,
    ActionMode mode
) {
    if (pub.defcon > 2 || !is_defcon_lowering_card(card_id)) {
        return false;
    }

    const auto& card_info = card_spec(card_id);
    const bool event_fires_for_any_mode = (card_info.side != side && card_info.side != Side::Neutral);
    const bool event_fires_for_event_space =
        (mode == ActionMode::Event) ||
        (mode == ActionMode::Space && event_fires_for_any_mode);
    return event_fires_for_any_mode || event_fires_for_event_space;
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
    NoActionFn&& no_action
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

    auto masked_card = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto card_id : playable) {
        if (is_card_blocked_by_defcon(pub, side, card_id)) {
            continue;
        }
        const auto index = static_cast<int64_t>(card_id - 1);
        masked_card.index_put_({index}, tensor_at(card_logits, index));
    }

    auto all_masked = true;
    for (const auto card_id : playable) {
        const auto index = static_cast<int64_t>(card_id - 1);
        if (tensor_at(masked_card, index).item<float>() > -std::numeric_limits<float>::infinity()) {
            all_masked = false;
            break;
        }
    }
    if (all_masked) {
        return heuristic_fallback();
    }

    const auto sampled_card_id = static_cast<CardId>(std::forward<SelectCardFn>(select_card)(masked_card));
    auto modes = legal_modes(sampled_card_id, pub, side);
    if (modes.empty()) {
        return no_action();
    }

    auto build_masked_mode = [&]() {
        auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto mode : modes) {
            const auto index = static_cast<int64_t>(static_cast<int>(mode));
            masked_mode.index_put_({index}, tensor_at(mode_logits, index));
        }
        return masked_mode;
    };

    auto masked_mode = build_masked_mode();
    auto mode = static_cast<ActionMode>(std::forward<SelectModeFn>(select_mode)(masked_mode));

    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
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
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        if (modes.empty()) {
            return no_action();
        }
        masked_mode = build_masked_mode();
        mode = static_cast<ActionMode>(std::forward<SelectModeFn>(select_mode)(masked_mode));
    }

    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return no_action();
        }
        masked_mode = build_masked_mode();
        mode = static_cast<ActionMode>(std::forward<SelectModeFn>(select_mode)(masked_mode));
    }

    if (requires_defcon_fallback(pub, side, sampled_card_id, mode)) {
        return heuristic_fallback();
    }

    if (mode == ActionMode::Event || mode == ActionMode::Space) {
        return Result{ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {}}};
    }

    if (use_country_head && country_logits.defined()) {
        auto action = build_action_from_country_logits(
            sampled_card_id,
            mode,
            country_logits,
            pub,
            side,
            strategy_logits,
            country_strategy_logits
        );
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

}  // namespace ts::decode

#endif
