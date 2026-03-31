#pragma once

#include <optional>
#include <string>
#include <vector>

#include "legal_actions.hpp"
#include "rng.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)
#include <torch/script.h>
#endif

namespace ts {

#if defined(TS_BUILD_TORCH_RUNTIME)

class TorchScriptPolicy {
public:
    explicit TorchScriptPolicy(std::string model_path, bool use_country_head = true);

    [[nodiscard]] const std::string& model_path() const { return model_path_; }

    std::optional<ActionEncoding> choose_action(
        const PublicState& pub,
        const CardSet& hand,
        bool holds_china,
        Pcg64Rng& rng
    );

private:
    std::string model_path_;
    bool use_country_head_ = true;
    torch::jit::script::Module module_;
};

#endif

}  // namespace ts
