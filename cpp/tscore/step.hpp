#pragma once

#include <random>

#include "legal_actions.hpp"
#include "scoring.hpp"

namespace ts {

std::tuple<PublicState, bool, std::optional<Side>> apply_action(
    const PublicState& pub,
    const ActionEncoding& action,
    Side side,
    std::mt19937& rng
);

std::tuple<bool, std::optional<Side>> check_vp_win(const PublicState& pub);

}  // namespace ts
