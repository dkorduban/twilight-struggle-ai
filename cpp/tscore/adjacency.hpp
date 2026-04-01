// Cached adjacency and reachability helpers shared across legality, policies,
// and event logic.

#pragma once

#include <array>
#include <vector>

#include "public_state.hpp"

namespace ts {

using AdjacencyMap = std::array<std::vector<CountryId>, kCountrySlots>;

const AdjacencyMap& adjacency();
// Return countries the side can legally touch for the selected action mode.
std::vector<CountryId> accessible_countries(
    Side side,
    const PublicState& pub,
    ActionMode mode = ActionMode::Influence
);

}  // namespace ts
