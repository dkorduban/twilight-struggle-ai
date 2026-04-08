// Shared TorchScript feature extraction helpers for native model inference.

#include "nn_features.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <stdexcept>

namespace ts::nn {
namespace {

// Active-effect features are ready in fill_scalars() below (indices 11-31),
// but kScalarDim stays at 11 until PPO v3 finishes so existing checkpoints keep
// working. After v3 completes, bump to 32 and train a new BC from scratch.
// TODO(2026-04-07): bump to 32 after PPO v3 completes.
constexpr int kScalarDim = 11;
constexpr int kCardMaskLen = kCardSlots;
constexpr int kCountryMaskLen = kCountrySlots;

void fill_card_mask(float* ptr, const CardSet& cards) {
    std::fill(ptr, ptr + kCardMaskLen, 0.0f);
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (cards.test(card_id)) {
            ptr[card_id] = 1.0f;
        }
    }
}

void fill_influence_array(float* ptr, const PublicState& pub, Side side) {
    for (int country_id = 0; country_id <= kMaxCountryId; ++country_id) {
        ptr[country_id] = static_cast<float>(pub.influence_of(side, static_cast<CountryId>(country_id)));
    }
}

void fill_cards(float* ptr, const PublicState& pub, const CardSet& hand) {
    fill_card_mask(ptr, hand);
    fill_card_mask(ptr + kCardMaskLen, hand);
    fill_card_mask(ptr + (2 * kCardMaskLen), pub.discard);
    fill_card_mask(ptr + (3 * kCardMaskLen), pub.removed);
}

void fill_scalars(float* ptr, const PublicState& pub, bool holds_china, Side side) {
    // [0-10] Core game state (unchanged)
    ptr[0] = static_cast<float>(pub.vp) / 20.0f;
    ptr[1] = static_cast<float>(pub.defcon - 1) / 4.0f;
    ptr[2] = static_cast<float>(pub.milops[to_index(Side::USSR)]) / 6.0f;
    ptr[3] = static_cast<float>(pub.milops[to_index(Side::US)]) / 6.0f;
    ptr[4] = static_cast<float>(pub.space[to_index(Side::USSR)]) / 9.0f;
    ptr[5] = static_cast<float>(pub.space[to_index(Side::US)]) / 9.0f;
    ptr[6] = static_cast<float>(to_index(pub.china_held_by));
    ptr[7] = holds_china ? 1.0f : 0.0f;
    ptr[8] = static_cast<float>(pub.turn) / 10.0f;
    ptr[9] = static_cast<float>(pub.ar) / 8.0f;
    ptr[10] = static_cast<float>(to_index(side));
    // [11-21] Trap / constraint effects — highest strategic impact
    ptr[11] = pub.bear_trap_active ? 1.0f : 0.0f;
    ptr[12] = pub.quagmire_active ? 1.0f : 0.0f;
    ptr[13] = pub.cuban_missile_crisis_active ? 1.0f : 0.0f;
    ptr[14] = pub.iran_hostage_crisis_active ? 1.0f : 0.0f;
    ptr[15] = pub.norad_active ? 1.0f : 0.0f;
    ptr[16] = pub.shuttle_diplomacy_active ? 1.0f : 0.0f;
    ptr[17] = pub.salt_active ? 1.0f : 0.0f;
    ptr[18] = pub.flower_power_active ? 1.0f : 0.0f;
    ptr[19] = pub.flower_power_cancelled ? 1.0f : 0.0f;
    ptr[20] = pub.vietnam_revolts_active ? 1.0f : 0.0f;
    ptr[21] = pub.north_sea_oil_extra_ar ? 1.0f : 0.0f;
    // [22-28] Board-modifying effects
    ptr[22] = pub.glasnost_extra_ar ? 1.0f : 0.0f;
    ptr[23] = pub.nato_active ? 1.0f : 0.0f;
    ptr[24] = pub.de_gaulle_active ? 1.0f : 0.0f;
    ptr[25] = pub.nuclear_subs_active ? 1.0f : 0.0f;
    ptr[26] = pub.formosan_active ? 1.0f : 0.0f;
    ptr[27] = pub.awacs_active ? 1.0f : 0.0f;
    // [28-29] Chernobyl: active flag + which region (0-6) normalized to 0..1
    ptr[28] = pub.chernobyl_blocked_region.has_value() ? 1.0f : 0.0f;
    ptr[29] = pub.chernobyl_blocked_region.has_value()
                  ? static_cast<float>(static_cast<uint8_t>(*pub.chernobyl_blocked_region)) / 6.0f
                  : 0.0f;
    // [30-31] Per-side ops modifier (Red Scare/Purge: -1; rarely +1)
    ptr[30] = static_cast<float>(pub.ops_modifier[to_index(Side::USSR)]) / 3.0f;
    ptr[31] = static_cast<float>(pub.ops_modifier[to_index(Side::US)]) / 3.0f;
}

torch::Tensor influence_array(const PublicState& pub, Side side) {
    auto tensor = torch::zeros({kCountryMaskLen}, torch::TensorOptions().dtype(torch::kFloat32));
    fill_influence_array(tensor.data_ptr<float>(), pub, side);
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

}  // namespace

void BatchInputs::allocate(int batch_capacity, torch::Device dev) {
    if (batch_capacity <= 0) {
        throw std::invalid_argument("batch_capacity must be positive");
    }

    device = dev;
    // Always allocate CPU pinned buffers for filling; move to device before forward.
    const auto cpu_options = torch::TensorOptions().dtype(torch::kFloat32).device(torch::kCPU);
    influence = torch::zeros({batch_capacity, 2 * kCountrySlots}, cpu_options);
    cards = torch::zeros({batch_capacity, 4 * kCardSlots}, cpu_options);
    scalars = torch::zeros({batch_capacity, kScalarDim}, cpu_options);
    capacity = batch_capacity;
    filled = 0;
}

void BatchInputs::fill_slot(int idx, const PublicState& pub, const CardSet& hand, bool holds_china, Side side) {
    if (idx < 0 || idx >= capacity) {
        throw std::out_of_range("batch slot index out of range");
    }

    fill_influence_array(influence.data_ptr<float>() + (idx * 2 * kCountrySlots), pub, Side::USSR);
    fill_influence_array(
        influence.data_ptr<float>() + (idx * 2 * kCountrySlots) + kCountrySlots,
        pub,
        Side::US
    );
    fill_cards(cards.data_ptr<float>() + (idx * 4 * kCardSlots), pub, hand);
    fill_scalars(scalars.data_ptr<float>() + (idx * kScalarDim), pub, holds_china, side);
    filled = std::max(filled, idx + 1);
}

torch::Tensor extract_influence(const PublicState& pub) {
    return torch::cat({influence_array(pub, Side::USSR), influence_array(pub, Side::US)}).unsqueeze(0);
}

torch::Tensor extract_cards(const PublicState& pub, const CardSet& hand) {
    auto tensor = torch::zeros({1, 4 * kCardSlots}, torch::TensorOptions().dtype(torch::kFloat32));
    fill_cards(tensor.data_ptr<float>(), pub, hand);
    return tensor;
}

torch::Tensor extract_scalars(const PublicState& pub, bool holds_china, Side side) {
    auto tensor = torch::zeros({1, kScalarDim}, torch::TensorOptions().dtype(torch::kFloat32));
    fill_scalars(tensor.data_ptr<float>(), pub, holds_china, side);
    return tensor;
}

BatchOutputs forward_model_batched(torch::jit::script::Module& model, const BatchInputs& inputs) {
    if (inputs.filled <= 0) {
        throw std::invalid_argument("batched forward requires at least one filled slot");
    }

    // Slice to filled rows, then move to target device (GPU if configured).
    const auto dev = inputs.device;
    std::vector<torch::jit::IValue> model_inputs;
    model_inputs.push_back(inputs.influence.narrow(/*dim=*/0, /*start=*/0, /*length=*/inputs.filled).to(dev));
    model_inputs.push_back(inputs.cards.narrow(/*dim=*/0, /*start=*/0, /*length=*/inputs.filled).to(dev));
    model_inputs.push_back(inputs.scalars.narrow(/*dim=*/0, /*start=*/0, /*length=*/inputs.filled).to(dev));

    torch::NoGradGuard no_grad;
    const auto outputs = model.forward(model_inputs).toGenericDict();

    // Move all output tensors back to CPU so downstream MCTS tree code can call .item<>() freely.
    auto to_cpu = [](torch::Tensor t) -> torch::Tensor {
        if (!t.defined()) {
            return t;
        }
        return t.cpu();
    };
    return BatchOutputs{
        .card_logits = to_cpu(get_tensor(outputs, "card_logits")),
        .mode_logits = to_cpu(get_tensor(outputs, "mode_logits")),
        .country_logits = to_cpu(get_tensor(outputs, "country_logits", false)),
        .strategy_logits = to_cpu(get_tensor(outputs, "strategy_logits", false)),
        .country_strategy_logits = to_cpu(get_tensor(outputs, "country_strategy_logits", false)),
        .value = to_cpu(get_tensor(outputs, "value")),
    };
}

c10::impl::GenericDict forward_model(
    torch::jit::script::Module& model,
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    Side side
) {
    std::vector<torch::jit::IValue> inputs;
    inputs.push_back(extract_influence(pub));
    inputs.push_back(extract_cards(pub, hand));
    inputs.push_back(extract_scalars(pub, holds_china, side));

    torch::NoGradGuard no_grad;
    return model.forward(inputs).toGenericDict();
}

}  // namespace ts::nn

#endif
