// Single-action application for the native engine, including event dispatch.

#pragma once

#include "legal_actions.hpp"
#include "policy_callback.hpp"
#include "rng.hpp"
#include "scoring.hpp"

namespace ts {

struct WarResult {
    bool success = false;
    int die_roll = 0;
    int threshold = 0;
};

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

WarResult apply_war_card(
    PublicState& next,
    Side attacker,
    CountryId target,
    int vp_on_success,
    int ops_for_milops,
    Pcg64Rng& rng
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
