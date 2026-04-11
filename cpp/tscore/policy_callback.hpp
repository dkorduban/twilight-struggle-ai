// Callback interface for policy-driven decisions during event resolution.
// When the callback is null / absent, the engine falls back to random
// (rng.choice_index) — preserving full backward compatibility.

#pragma once

#include <functional>
#include <vector>

#include "game_state.hpp"

namespace ts {

enum class DecisionKind : int {
    SmallChoice   = 0,  // binary / small option (e.g. Warsaw Pact add vs remove)
    CountrySelect = 1,  // pick a country from eligible list
    CardSelect    = 2,  // pick a card from a candidate set
};

/// Describes a decision the engine needs a policy to resolve.
struct EventDecision {
    CardId source_card = 0;
    DecisionKind kind = DecisionKind::SmallChoice;
    int n_options = 0;           // number of legal choices (indices 0..n_options-1)
    Side acting_side = Side::Neutral;
};

/// Callback type: given the current public state and the decision description,
/// return the chosen option index in [0, decision.n_options).
/// If the callback returns an out-of-range index, the engine clamps to valid range.
using PolicyCallbackFn = std::function<int(const PublicState&, const EventDecision&)>;

}  // namespace ts
