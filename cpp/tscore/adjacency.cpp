#include "adjacency.hpp"

#include <algorithm>
#include <fstream>
#include <queue>
#include <sstream>
#include <stdexcept>

#include "game_data.hpp"

namespace ts {
namespace {

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
    ActionMode /*mode*/
) {
    const auto& graph = adjacency();
    std::bitset<kCountrySlots> visited;
    std::queue<CountryId> queue;

    for (CountryId cid = 0; cid < kCountrySlots; ++cid) {
        if (pub.influence_of(side, cid) > 0) {
            visited.set(cid);
            queue.push(cid);
        }
    }

    while (!queue.empty()) {
        const auto current = queue.front();
        queue.pop();
        for (const auto neighbor : graph[current]) {
            if (neighbor == kUsaAnchorId || neighbor == kUssrAnchorId) {
                continue;
            }
            if (!visited.test(neighbor)) {
                visited.set(neighbor);
                queue.push(neighbor);
            }
        }
    }

    for (const auto anchor : {kUsaAnchorId, kUssrAnchorId}) {
        for (const auto neighbor : graph[anchor]) {
            if (neighbor != kUsaAnchorId && neighbor != kUssrAnchorId) {
                visited.set(neighbor);
            }
        }
    }

    std::vector<CountryId> out;
    for (CountryId cid = 0; cid < kCountrySlots; ++cid) {
        if ((cid == kUsaAnchorId || cid == kUssrAnchorId) || !visited.test(cid) || !has_country_spec(cid)) {
            continue;
        }
        out.push_back(cid);
    }
    return out;
}

}  // namespace ts
