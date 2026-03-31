#include "learned_policy.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <limits>
#include <stdexcept>
#include <tuple>

#include <torch/torch.h>

#include "game_data.hpp"

namespace ts {
namespace {

constexpr int kScalarDim = 11;
constexpr int kCardMaskLen = kCardSlots;
constexpr int kCountryMaskLen = kCountrySlots;

torch::Tensor card_mask(const CardSet& cards) {
    auto tensor = torch::zeros({kCardMaskLen}, torch::TensorOptions().dtype(torch::kFloat32));
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (cards.test(card_id)) {
            tensor.index_put_({card_id}, 1.0f);
        }
    }
    return tensor;
}

torch::Tensor influence_array(const PublicState& pub, Side side) {
    auto tensor = torch::zeros({kCountryMaskLen}, torch::TensorOptions().dtype(torch::kFloat32));
    for (int country_id = 0; country_id <= kMaxCountryId; ++country_id) {
        tensor.index_put_({country_id}, static_cast<float>(pub.influence_of(side, static_cast<CountryId>(country_id))));
    }
    return tensor;
}

torch::Tensor extract_influence(const PublicState& pub) {
    return torch::cat({influence_array(pub, Side::USSR), influence_array(pub, Side::US)}).unsqueeze(0);
}

torch::Tensor extract_cards(const PublicState& pub, const CardSet& hand) {
    auto hand_tensor = card_mask(hand);
    auto discard_tensor = card_mask(pub.discard);
    auto removed_tensor = card_mask(pub.removed);
    return torch::cat({hand_tensor, hand_tensor, discard_tensor, removed_tensor}).unsqueeze(0);
}

torch::Tensor extract_scalars(const PublicState& pub, bool holds_china, Side side) {
    auto tensor = torch::zeros({1, kScalarDim}, torch::TensorOptions().dtype(torch::kFloat32));
    tensor.index_put_({0, 0}, static_cast<float>(pub.vp) / 20.0f);
    tensor.index_put_({0, 1}, static_cast<float>(pub.defcon - 1) / 4.0f);
    tensor.index_put_({0, 2}, static_cast<float>(pub.milops[to_index(Side::USSR)]) / 6.0f);
    tensor.index_put_({0, 3}, static_cast<float>(pub.milops[to_index(Side::US)]) / 6.0f);
    tensor.index_put_({0, 4}, static_cast<float>(pub.space[to_index(Side::USSR)]) / 9.0f);
    tensor.index_put_({0, 5}, static_cast<float>(pub.space[to_index(Side::US)]) / 9.0f);
    tensor.index_put_({0, 6}, static_cast<float>(to_index(pub.china_held_by)));
    tensor.index_put_({0, 7}, holds_china ? 1.0f : 0.0f);
    tensor.index_put_({0, 8}, static_cast<float>(pub.turn) / 10.0f);
    tensor.index_put_({0, 9}, static_cast<float>(pub.ar) / 8.0f);
    tensor.index_put_({0, 10}, static_cast<float>(to_index(side)));
    return tensor;
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

    auto ops = effective_ops(card_id, pub, side);
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

}  // namespace

TorchScriptPolicy::TorchScriptPolicy(std::string model_path, bool use_country_head)
    : model_path_(std::move(model_path)),
      use_country_head_(use_country_head),
      module_(torch::jit::load(model_path_)) {
    module_.eval();
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

    std::vector<torch::jit::IValue> inputs;
    inputs.push_back(extract_influence(pub));
    inputs.push_back(extract_cards(pub, hand));
    inputs.push_back(extract_scalars(pub, holds_china, side));

    torch::NoGradGuard no_grad;
    const auto outputs = module_.forward(inputs).toGenericDict();
    const auto card_logits = get_tensor(outputs, "card_logits").index({0});
    const auto mode_logits = get_tensor(outputs, "mode_logits").index({0});
    const auto country_logits_raw = get_tensor(outputs, "country_logits", false);
    const auto strategy_logits_raw = get_tensor(outputs, "strategy_logits", false);
    const auto country_strategy_logits_raw = get_tensor(outputs, "country_strategy_logits", false);

    auto masked_card = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto card_id : playable) {
        const auto index = static_cast<int64_t>(card_id - 1);
        masked_card.index_put_({index}, tensor_at(card_logits, index));
    }
    auto sampled_card_id = static_cast<CardId>(masked_card.argmax(/*dim=*/0).item<int64_t>() + 1);

    auto modes = legal_modes(sampled_card_id, pub, side);
    if (modes.empty()) {
        return std::nullopt;
    }
    auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
    for (const auto mode : modes) {
        const auto index = static_cast<int64_t>(static_cast<int>(mode));
        masked_mode.index_put_({index}, tensor_at(mode_logits, index));
    }
    auto mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());

    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return std::nullopt;
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto legal_mode : modes) {
            const auto index = static_cast<int64_t>(static_cast<int>(legal_mode));
            masked_mode.index_put_({index}, tensor_at(mode_logits, index));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    if (mode == ActionMode::Event || mode == ActionMode::Space) {
        return ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {}};
    }

    if (use_country_head_ && country_logits_raw.defined()) {
        const auto country_logits = country_logits_raw.index({0});
        const auto strategy_logits = strategy_logits_raw.defined() ? strategy_logits_raw.index({0}) : torch::Tensor{};
        const auto country_strategy_logits = country_strategy_logits_raw.defined() ? country_strategy_logits_raw.index({0}) : torch::Tensor{};
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
            return action;
        }
    }

    return sample_action(hand, pub, side, holds_china, rng);
}

}  // namespace ts

#endif
