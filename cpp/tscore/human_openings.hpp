#pragma once

#include "types.hpp"
#include "rng.hpp"

#include <array>
#include <span>

namespace ts {

// Setup placement for a single country during opening phase.
struct SetupPlacement {
    CountryId country;
    int amount;
};

// One complete opening configuration (sorted by country ID for determinism).
// Padded with {0, 0} sentinels to fixed length.
struct SetupOpening {
    std::array<SetupPlacement, 6> placements;  // max 6 free placements per side
    int count;  // actual number of valid entries
    double weight;  // frequency weight: count / total games (e.g., 24.0/52.0)
};

// Extracted from 58 human game logs (raw_logs + raw_log_extras).
// Each entry represents an actual opening configuration played by humans.
// All games used +2 bid for US (9 total free influence).

inline constexpr std::array<SetupOpening, 3> kHumanUSSROpenings = {
    // Austria+1 EG+1 Poland+4 = 6.  Played 29/58 (0.500).
    SetupOpening{
        .placements = {SetupPlacement{0, 1}, SetupPlacement{5, 1}, SetupPlacement{12, 4}, {}, {}, {}},
        .count = 3,
        .weight = 29.0 / 58.0,
    },
    // EG+1 Poland+4 Yugoslavia+1 = 6.  Played 24/58 (0.414).
    SetupOpening{
        .placements = {SetupPlacement{5, 1}, SetupPlacement{12, 4}, SetupPlacement{19, 1}, {}, {}, {}},
        .count = 3,
        .weight = 24.0 / 58.0,
    },
    // EG+1 Poland+5 = 6.  Played 5/58 (0.086).
    SetupOpening{
        .placements = {SetupPlacement{5, 1}, SetupPlacement{12, 5}, {}, {}, {}, {}},
        .count = 2,
        .weight = 5.0 / 58.0,
    },
};

// US openings with +2 bid (9 influence total) — extracted from 58 human games.
// 57/58 games used bid; the +2 consistently went to Iran(28)+1 across all variants.
// The 7 WE influence + 1 Iran bid = atomic 9-influence opening unit.
// One game (1.7%) had no bid (7 total) — included for completeness.
inline constexpr std::array<SetupOpening, 6> kHumanUSOpeningsBid2 = {
    // Italy+4 WG+4 Iran+1 = 9.  Played 44/58 (0.759).
    SetupOpening{.placements = {SetupPlacement{10, 4}, SetupPlacement{18, 4}, SetupPlacement{28, 1}, {}, {}, {}}, .count = 3, .weight = 44.0 / 58.0},
    // France+3 Italy+2 WG+3 Iran+1 = 9.  Played 6/58 (0.103).
    SetupOpening{.placements = {SetupPlacement{7, 3}, SetupPlacement{10, 2}, SetupPlacement{18, 3}, SetupPlacement{28, 1}, {}, {}}, .count = 4, .weight = 6.0 / 58.0},
    // France+2 Italy+3 WG+3 Iran+1 = 9.  Played 5/58 (0.086).
    SetupOpening{.placements = {SetupPlacement{7, 2}, SetupPlacement{10, 3}, SetupPlacement{18, 3}, SetupPlacement{28, 1}, {}, {}}, .count = 4, .weight = 5.0 / 58.0},
    // Canada+1 Italy+3 Turkey+1 WG+3 Iran+1 = 9.  Played 1/58 (0.017).
    SetupOpening{.placements = {SetupPlacement{2, 1}, SetupPlacement{10, 3}, SetupPlacement{16, 1}, SetupPlacement{18, 3}, SetupPlacement{28, 1}, {}}, .count = 5, .weight = 1.0 / 58.0},
    // France+1 Italy+3 WG+4 Iran+1 = 9.  Played 1/58 (0.017).
    SetupOpening{.placements = {SetupPlacement{7, 1}, SetupPlacement{10, 3}, SetupPlacement{18, 4}, SetupPlacement{28, 1}, {}, {}}, .count = 4, .weight = 1.0 / 58.0},
    // Italy+3 WG+4 = 7 (no bid game).  Played 1/58 (0.017).
    SetupOpening{.placements = {SetupPlacement{10, 3}, SetupPlacement{18, 4}, {}, {}, {}, {}}, .count = 2, .weight = 1.0 / 58.0},
};

// Choose a random opening proportional to historical frequency weights.
// Uses cumulative distribution function (CDF) sampling.
inline const SetupOpening* choose_random_opening(
    const SetupOpening* openings_array,
    int count,
    Pcg64Rng& rng) {
    if (count <= 0) return nullptr;
    if (count == 1) return &openings_array[0];

    double r = rng.random_double();

    // Walk CDF: cumsum += weight, check if r <= cumsum
    double cumsum = 0.0;
    for (int i = 0; i < count; ++i) {
        cumsum += openings_array[i].weight;
        if (r <= cumsum) {
            return &openings_array[i];
        }
    }

    // Fallback (should never reach here if weights sum to ~1.0)
    return &openings_array[count - 1];
}

// Nash equilibrium mixed strategies over Boltzmann temperatures.
// Derived from the 6×6 heuristic temperature matrix (bid+2, human openings).
// Game value: USSR 66.09%, US 33.91%.
//
// Each entry is {temperature, probability}.
struct TempWeight {
    float temperature;
    float probability;
};

inline constexpr std::array<TempWeight, 3> kNashUSSRTemps = {{
    {0.5f, 0.3396f},
    {1.0f, 0.3229f},
    {3.0f, 0.3374f},
}};

inline constexpr std::array<TempWeight, 3> kNashUSTemps = {{
    {1.5f, 0.3775f},
    {2.0f, 0.6108f},
    {3.0f, 0.0117f},
}};

// Sample a temperature from a Nash mixed strategy.
inline float sample_nash_temperature(
    const TempWeight* weights, int count, Pcg64Rng& rng) {
    double r = rng.random_double();
    double cumsum = 0.0;
    for (int i = 0; i < count; ++i) {
        cumsum += weights[i].probability;
        if (r <= cumsum) return weights[i].temperature;
    }
    return weights[count - 1].temperature;
}

}  // namespace ts
