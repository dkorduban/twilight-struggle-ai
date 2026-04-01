// Random resolution helpers for coups, realignments, wars, and space attempts.

#pragma once

#include <utility>

#include "rng.hpp"

namespace ts {

int roll_d6(Pcg64Rng& rng);
std::pair<int, int> roll_2d6(Pcg64Rng& rng);
int coup_net(int attacker_roll, int ops, int defender_stability);
int coup_result(int ops, int defender_stability, Pcg64Rng& rng);
std::pair<int, int> realign_result(
    int ussr_influence,
    int us_influence,
    int ussr_adj_nations,
    int us_adj_nations,
    Pcg64Rng& rng
);
bool space_result(int current_level, Pcg64Rng& rng);

}  // namespace ts
