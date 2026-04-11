// Shared TorchScript feature extraction and forward helpers.

#pragma once

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <torch/script.h>
#include <torch/torch.h>

#include "game_state.hpp"

namespace ts::nn {

struct BatchInputs {
    torch::Tensor influence;
    torch::Tensor cards;
    torch::Tensor scalars;
    int capacity = 0;
    int filled = 0;
    torch::Device device = torch::kCPU;

    void allocate(int batch_capacity, torch::Device dev = torch::kCPU);
    void fill_slot(int idx, const PublicState& pub, const CardSet& hand, bool holds_china, Side side);
    void reset() { filled = 0; }
};

struct BatchOutputs {
    torch::Tensor card_logits;
    torch::Tensor mode_logits;
    torch::Tensor country_logits;
    torch::Tensor strategy_logits;
    torch::Tensor country_strategy_logits;
    torch::Tensor value;
    torch::Tensor small_choice_logits;  // (B, 8) or undefined for old models
};

torch::Tensor extract_influence(const PublicState& pub);
torch::Tensor extract_cards(const PublicState& pub, const CardSet& hand);
torch::Tensor extract_scalars(const PublicState& pub, bool holds_china, Side side);
BatchOutputs forward_model_batched(torch::jit::script::Module& model, const BatchInputs& inputs);

c10::impl::GenericDict forward_model(
    torch::jit::script::Module& model,
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    Side side
);

}  // namespace ts::nn

#endif
