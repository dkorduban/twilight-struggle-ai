// Single-action application for the native engine, including event dispatch.

#pragma once

#include "legal_actions.hpp"
#include "policy_callback.hpp"
#include "rng.hpp"
#include "scoring.hpp"

namespace ts {

int choose_option(
    const PublicState& pub,
    CardId card_id,
    Side side,
    int n_options,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

CountryId choose_country(
    const PublicState& pub,
    CardId card_id,
    Side side,
    std::span<const CountryId> pool,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

CardId choose_card(
    const PublicState& pub,
    CardId card_id,
    Side side,
    std::span<const CardId> pool,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

std::tuple<PublicState, bool, std::optional<Side>> apply_action(
    const PublicState& pub,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
);

std::tuple<bool, std::optional<Side>> check_vp_win(const PublicState& pub);

}  // namespace ts
