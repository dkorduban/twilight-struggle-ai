#pragma once
// Bounded-knapsack DP decoder for country allocation.
// Given per-country marginal scores scores[c][t] (marginal value of placing t-th op),
// finds integer allocation alloc[c] >= 0 with sum(alloc[c]) <= budget that maximizes
// sum_c prefix_scores[c][alloc[c]] subject to legal_mask and per-country caps.

#include <algorithm>
#include <cstdint>
#include <limits>
#include <vector>

namespace ts {

// scores[c][t]: marginal value of placing the (t+1)-th op in country c (0-indexed)
// Returns allocation alloc[c] = number of ops to place in country c
// Constraints: sum(alloc[c] * cost[c]) <= budget, alloc[c] <= cap[c], alloc[c]=0 if !legal[c]
inline std::vector<int> knapsack_alloc(
    const std::vector<std::vector<float>>& scores,  // [n_countries][t_max]
    int budget,
    const std::vector<bool>& legal,
    const std::vector<int>& cap,    // per-country max (default = t_max)
    const std::vector<int>& cost    // per-country op cost (default = 1)
) {
    const int n = static_cast<int>(scores.size());
    if (n == 0 || budget <= 0) return std::vector<int>(n, 0);
    const int t_max = scores.empty() ? 0 : static_cast<int>(scores[0].size());

    // Prefix sums: prefix[c][k] = sum of scores[c][0..k-1]
    std::vector<std::vector<float>> prefix(n, std::vector<float>(t_max + 1, 0.0f));
    for (int c = 0; c < n; ++c) {
        for (int t = 0; t < t_max; ++t) {
            prefix[c][t + 1] = prefix[c][t] + (t < static_cast<int>(scores[c].size()) ? scores[c][t] : 0.0f);
        }
    }

    constexpr float NEG_INF = -std::numeric_limits<float>::infinity();
    // dp[budget+1]: best total score achievable with exactly `spent` ops spent through country c
    std::vector<float> dp(budget + 1, NEG_INF);
    std::vector<std::vector<int>> choice(n, std::vector<int>(budget + 1, 0));
    dp[0] = 0.0f;

    for (int c = 0; c < n; ++c) {
        if (!legal[c] || cap[c] <= 0) continue;
        const int step = cost[c];
        // new_dp starts from current dp so "take 0" is implicitly included
        std::vector<float> new_dp = dp;
        for (int spent = 0; spent <= budget; ++spent) {
            if (dp[spent] == NEG_INF) continue;
            const int max_take = std::min(cap[c], (budget - spent) / step);
            for (int take = 1; take <= max_take; ++take) {
                const int new_spent = spent + take * step;
                const float candidate = dp[spent] + prefix[c][take];
                if (candidate > new_dp[new_spent]) {
                    new_dp[new_spent] = candidate;
                    choice[c][new_spent] = take;
                }
            }
        }
        dp = new_dp;
    }

    // Find best remaining budget
    int remaining = budget;
    if (dp[remaining] == NEG_INF) {
        // Find any feasible solution
        for (int b = budget; b >= 0; --b) {
            if (dp[b] != NEG_INF) {
                remaining = b;
                break;
            }
        }
    }

    // Traceback
    std::vector<int> alloc(n, 0);
    for (int c = n - 1; c >= 0; --c) {
        if (!legal[c]) continue;
        const int take = choice[c][remaining];
        alloc[c] = take;
        remaining -= take * cost[c];
    }
    return alloc;
}

}  // namespace ts
