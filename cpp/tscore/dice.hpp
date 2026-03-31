#pragma once

#include <random>
#include <utility>

namespace ts {

int roll_d6(std::mt19937& rng);
std::pair<int, int> roll_2d6(std::mt19937& rng);
int coup_net(int attacker_roll, int ops, int defender_stability);
int coup_result(int ops, int defender_stability, std::mt19937& rng);
std::pair<int, int> realign_result(
    int ussr_influence,
    int us_influence,
    int ussr_adj_nations,
    int us_adj_nations,
    std::mt19937& rng
);
bool space_result(int current_level, std::mt19937& rng);

}  // namespace ts
