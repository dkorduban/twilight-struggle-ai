// Native implementations of the stochastic resolution helpers declared in
// `dice.hpp`.

#include "dice.hpp"

#include <array>

namespace ts {

int roll_d6(Pcg64Rng& rng) {
    return static_cast<int>(rng.numpy_bounded_uint64(1, 5));
}

std::pair<int, int> roll_2d6(Pcg64Rng& rng) {
    return {roll_d6(rng), roll_d6(rng)};
}

int coup_net(int attacker_roll, int ops, int defender_stability) {
    return attacker_roll + ops - 2 * defender_stability;
}

int coup_result(int ops, int defender_stability, Pcg64Rng& rng) {
    return coup_net(roll_d6(rng), ops, defender_stability);
}

std::pair<int, int> realign_result(
    int ussr_influence,
    int us_influence,
    int ussr_adj_nations,
    int us_adj_nations,
    Pcg64Rng& rng
) {
    const auto ussr_roll = roll_d6(rng);
    const auto us_roll = roll_d6(rng);
    const auto ussr_mod = ussr_adj_nations + (ussr_influence > us_influence ? 1 : 0);
    const auto us_mod = us_adj_nations + (us_influence > ussr_influence ? 1 : 0);
    return {ussr_roll + ussr_mod, us_roll + us_mod};
}

bool space_result(int current_level, Pcg64Rng& rng) {
    static constexpr std::array<int, 8> kSpaceAdvanceThreshold = {3, 4, 3, 4, 3, 4, 3, 2};
    if (current_level >= static_cast<int>(kSpaceAdvanceThreshold.size())) {
        return false;
    }
    return roll_d6(rng) <= kSpaceAdvanceThreshold[current_level];
}

}  // namespace ts
