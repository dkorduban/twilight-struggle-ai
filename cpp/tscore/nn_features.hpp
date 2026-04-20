// Shared TorchScript feature extraction and forward helpers.

#pragma once

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <torch/script.h>
#include <torch/torch.h>

#include <array>

#include "game_state.hpp"

namespace ts::nn {

constexpr int kScalarDim = 32;
constexpr int kFrameContextDim = 8;

struct BatchInputs {
    torch::Tensor influence;
    torch::Tensor cards;
    torch::Tensor scalars;
    int capacity = 0;
    int filled = 0;
    torch::Device device = torch::kCPU;

    void allocate(int batch_capacity, torch::Device dev = torch::kCPU);
    void fill_slot_no_count(int idx, const GameState& gs, const CardSet& hand, bool holds_china, Side side);
    void fill_slot_no_count(int idx, const PublicState& pub, const CardSet& hand, bool holds_china, Side side);
    void fill_slot_no_count(int idx, const Observation& obs);
    void fill_slot(int idx, const GameState& gs, const CardSet& hand, bool holds_china, Side side);
    void fill_slot(int idx, const PublicState& pub, const CardSet& hand, bool holds_china, Side side);
    void fill_slot(int idx, const Observation& obs);
    void reset() { filled = 0; }
};

struct BatchOutputs {
    torch::Tensor card_logits;
    torch::Tensor mode_logits;
    torch::Tensor country_logits;
    torch::Tensor strategy_logits;
    torch::Tensor country_strategy_logits;
    torch::Tensor marginal_logits;
    torch::Tensor value;
    torch::Tensor small_choice_logits;  // (B, 8) or undefined for old models
};

torch::Tensor extract_influence(const PublicState& pub);
torch::Tensor extract_influence(const Observation& obs);
torch::Tensor extract_cards(const PublicState& pub, const CardSet& hand);
torch::Tensor extract_cards(const Observation& obs);
torch::Tensor extract_scalars(const PublicState& pub, bool holds_china, Side side);
torch::Tensor extract_scalars(const Observation& obs);
std::array<float, kFrameContextDim> extract_frame_context(const GameState& gs);
BatchOutputs forward_model_batched(torch::jit::script::Module& model, const BatchInputs& inputs);

c10::impl::GenericDict forward_model(
    torch::jit::script::Module& model,
    const GameState& gs,
    const CardSet& hand,
    bool holds_china,
    Side side
);

c10::impl::GenericDict forward_model(
    torch::jit::script::Module& model,
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    Side side
);

c10::impl::GenericDict forward_model(
    torch::jit::script::Module& model,
    const Observation& obs
);

}  // namespace ts::nn

#endif
