// Single-action application for the native engine, including event dispatch.

#pragma once

#include "legal_actions.hpp"
#include "policy_callback.hpp"
#include "rng.hpp"
#include "scoring.hpp"

namespace ts {

/// Apply an action (card play) to the public state.
/// When policy_cb is non-null, event decisions that would normally be random
/// are delegated to the callback instead.  Pass nullptr for backward compat.
std::tuple<PublicState, bool, std::optional<Side>> apply_action(
    const PublicState& pub,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

std::tuple<bool, std::optional<Side>> check_vp_win(const PublicState& pub);

}  // namespace ts
