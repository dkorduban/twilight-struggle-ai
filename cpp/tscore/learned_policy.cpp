// TorchScript model loading and native action selection for learned-policy
// matchups and collection.

#include "learned_policy.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <limits>
#include <stdexcept>
#include <tuple>

#include <torch/torch.h>

#include "decode_helpers.hpp"
#include "game_data.hpp"
#include "nn_features.hpp"
#include "policies.hpp"

namespace ts {
namespace {

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

}  // namespace

TorchScriptPolicy::TorchScriptPolicy(std::string model_path, bool use_country_head)
    : model_path_(std::move(model_path)),
      use_country_head_(use_country_head),
      module_(torch::jit::load(model_path_)) {
    module_.eval();
}

void TorchScriptPolicy::set_exploration_rate(float exploration_rate) {
    if (exploration_rate < 0.0f || exploration_rate > 1.0f) {
        throw std::invalid_argument("exploration_rate must be in [0, 1]");
    }
    exploration_rate_ = exploration_rate;
}

std::optional<ActionEncoding> TorchScriptPolicy::choose_action(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    Pcg64Rng& rng
) {
    const auto side = pub.phasing;
    auto playable = legal_cards(hand, pub, side, holds_china);
    if (playable.empty()) {
        return std::nullopt;
    }
    if (exploration_rate_ > 0.0f && rng.bernoulli(static_cast<double>(exploration_rate_))) {
        auto legal_actions = enumerate_actions(hand, pub, side, holds_china);
        if (legal_actions.empty()) {
            return std::nullopt;
        }
        return legal_actions[rng.choice_index(legal_actions.size())];
    }

    const auto outputs = nn::forward_model(module_, pub, hand, holds_china, side);
    const auto card_logits = get_tensor(outputs, "card_logits").index({0});
    const auto mode_logits = get_tensor(outputs, "mode_logits").index({0});
    const auto country_logits_raw = get_tensor(outputs, "country_logits", false);
    const auto strategy_logits_raw = get_tensor(outputs, "strategy_logits", false);
    const auto country_strategy_logits_raw = get_tensor(outputs, "country_strategy_logits", false);
    const auto country_logits = country_logits_raw.defined() ? country_logits_raw.index({0}) : torch::Tensor{};
    const auto strategy_logits = strategy_logits_raw.defined() ? strategy_logits_raw.index({0}) : torch::Tensor{};
    const auto country_strategy_logits = country_strategy_logits_raw.defined()
        ? country_strategy_logits_raw.index({0}) : torch::Tensor{};

    return decode::choose_action_from_outputs(
        pub,
        hand,
        holds_china,
        use_country_head_,
        card_logits,
        mode_logits,
        country_logits,
        strategy_logits,
        country_strategy_logits,
        rng,
        [](const torch::Tensor& masked_card) -> CardId {
            return static_cast<CardId>(masked_card.argmax(/*dim=*/0).item<int64_t>() + 1);
        },
        [](const torch::Tensor& masked_mode) -> ActionMode {
            return static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
        },
        [&]() { return ts::choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng); },
        []() -> std::optional<ActionEncoding> { return std::nullopt; }
    );
}

}  // namespace ts

#endif
