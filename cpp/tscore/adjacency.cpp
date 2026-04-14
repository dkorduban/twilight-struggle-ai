// Loading and caching of the canonical country adjacency graph.

#include "adjacency.hpp"

#include <algorithm>
#include <fstream>
#include <queue>
#include <sstream>
#include <stdexcept>

#include "game_data.hpp"

namespace ts {
namespace {

// Read the spec adjacency CSV once and normalize each neighbor list.
AdjacencyMap load_adjacency() {
    AdjacencyMap map;
    std::ifstream input(spec_dir() / "adjacency.csv");
    if (!input) {
        throw std::runtime_error("failed to open data/spec/adjacency.csv");
    }

    std::string line;
    while (std::getline(input, line)) {
        const auto comment = line.find('#');
        if (comment != std::string::npos) {
            line = line.substr(0, comment);
        }
        if (line.empty() || line[0] == '#') {
            continue;
        }
        if (line.starts_with("country_a")) {
            continue;
        }
        std::stringstream ss(line);
        std::string a_raw;
        std::string b_raw;
        if (!std::getline(ss, a_raw, ',')) {
            continue;
        }
        if (!std::getline(ss, b_raw, ',')) {
            continue;
        }
        const auto a = static_cast<CountryId>(std::stoi(a_raw));
        const auto b = static_cast<CountryId>(std::stoi(b_raw));
        map[a].push_back(b);
        map[b].push_back(a);
    }

    for (auto& neighbors : map) {
        std::sort(neighbors.begin(), neighbors.end());
        neighbors.erase(std::unique(neighbors.begin(), neighbors.end()), neighbors.end());
    }
    return map;
}

}  // namespace

const AdjacencyMap& adjacency() {
    static const AdjacencyMap map = load_adjacency();
    return map;
}

std::vector<CountryId> accessible_countries(
    Side side,
    const PublicState& pub,
    ActionMode mode
) {
    const auto& graph = adjacency();

    // Coup and Realignment: all map countries are valid targets.
    // DEFCON restrictions and NATO filtering are applied later in
    // filtered_accessible_countries() / legal_actions.cpp.
    if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
        std::vector<CountryId> out;
        for (CountryId cid = 0; cid < kCountrySlots; ++cid) {
            if (cid == kUsaAnchorId || cid == kUssrAnchorId) continue;
            if (!has_country_spec(cid)) continue;
            out.push_back(cid);
        }
        return out;
    }

    // Influence placement: 1-hop adjacency only.
    // Rules: "A player may add Influence Markers in a country in which he
    // currently has Influence Markers, OR in a country adjacent to a country
    // in which he currently has Influence Markers."
    std::bitset<kCountrySlots> visited;

    // Countries where side already has influence, plus their 1-hop neighbors.
    for (CountryId cid = 0; cid < kCountrySlots; ++cid) {
        if (pub.influence_of(side, cid) > 0) {
            visited.set(cid);
            for (const auto neighbor : graph[cid]) {
                if (neighbor != kUsaAnchorId && neighbor != kUssrAnchorId) {
                    visited.set(neighbor);
                }
            }
        }
    }

    // Own superpower anchor: neighbors of the side's own anchor are always
    // accessible (e.g., USSR can always reach Finland/Poland/Afghanistan,
    // US can always reach Canada/Cuba/Japan).
    const CountryId own_anchor = (side == Side::USSR) ? kUssrAnchorId : kUsaAnchorId;
    for (const auto neighbor : graph[own_anchor]) {
        if (neighbor != kUsaAnchorId && neighbor != kUssrAnchorId) {
            visited.set(neighbor);
        }
    }

    std::vector<CountryId> out;
    for (CountryId cid = 0; cid < kCountrySlots; ++cid) {
        if (cid == kUsaAnchorId || cid == kUssrAnchorId) continue;
        if (!visited.test(cid)) continue;
        if (!has_country_spec(cid)) continue;
        out.push_back(cid);
    }
    return out;
}

}  // namespace ts
