// Single-action application for the native engine, including event dispatch.

#pragma once

#include "legal_actions.hpp"
#include "rng.hpp"
#include "scoring.hpp"

namespace ts {

std::tuple<PublicState, bool, std::optional<Side>> apply_action(
    const PublicState& pub,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng
);

std::tuple<bool, std::optional<Side>> check_vp_win(const PublicState& pub);

}  // namespace ts
