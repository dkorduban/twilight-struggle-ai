// Callback interface for policy-driven decisions during event resolution.
// When the callback is null / absent, the engine falls back to random
// (rng.choice_index) — preserving full backward compatibility.

#pragma once

#include <functional>

#include "game_state.hpp"

namespace ts {

enum class DecisionKind : int {
    SmallChoice = 0,
    CountrySelect = 1,
    CardSelect = 2,
};

struct EventDecision {
    CardId source_card = 0;
    DecisionKind kind = DecisionKind::SmallChoice;
    int n_options = 0;
    Side acting_side = Side::Neutral;

    // Eligible country or card ids; only the first n_options entries are valid.
    static constexpr int kMaxEligible = kCardSlots;
    int eligible_ids[kMaxEligible] = {};
};

using PolicyCallbackFn = std::function<int(const PublicState&, const EventDecision&)>;

}  // namespace ts
