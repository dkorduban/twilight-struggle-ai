#pragma once

#include <array>
#include <vector>

#include "public_state.hpp"

namespace ts {

using AdjacencyMap = std::array<std::vector<CountryId>, kCountrySlots>;

const AdjacencyMap& adjacency();
std::vector<CountryId> accessible_countries(
    Side side,
    const PublicState& pub,
    ActionMode mode = ActionMode::Influence
);

}  // namespace ts
