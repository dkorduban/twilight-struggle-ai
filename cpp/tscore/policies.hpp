#pragma once

#include <optional>
#include <random>
#include <vector>

#include "legal_actions.hpp"

namespace ts {

enum class PolicyKind : uint8_t {
    Random = 0,
    MinimalHybrid = 1,
};

struct MinimalHybridParams {
    std::array<double, 7> early_region_weights = {0.85, 1.35, 1.10, 0.60, 0.55, 0.65, 1.25};
    std::array<double, 7> mid_region_weights = {0.95, 1.00, 1.00, 0.95, 1.20, 1.20, 0.90};
    std::array<double, 7> late_region_weights = {1.10, 0.95, 0.95, 1.05, 1.10, 1.20, 0.75};
    double influence_mode_bonus = 6.0;
    double coup_mode_bonus = 4.0;
    double realign_mode_bonus = -1.0;
    double space_mode_bonus = 1.0;
    double ops_card_penalty = 0.15;
    double control_break_bonus = 5.0;
    double access_bonus = 2.0;
    double coup_battleground_bonus = 2.5;
    double coup_defcon2_penalty = -8.0;
    double coup_defcon3_penalty = -6.0;
    double coup_defcon3_bg_threshold = 0.65;
    double realign_base_penalty = -4.0;
    double realign_country_scale = 0.55;
    double realign_defcon2_bonus = 2.0;
    double space_when_behind_bonus = 2.0;
    double space_early_bonus = 1.0;
    double space_offside_bonus = 2.0;
    double headline_ops_scale = 0.75;
    double headline_friendly_bonus = 2.0;
    double china_early_penalty = -2.5;
    double china_asia_target_bonus = 1.5;
    double country_region_scale = 5.0;
    double country_battleground_bonus = 7.0;
    double country_non_battleground_bonus = 1.0;
    double country_stability_scale = 0.6;
    double country_thailand_early_bonus = 6.0;
    double country_europe_core_bonus = 2.0;
    double country_mid_war_entry_bonus = 2.0;
};

std::optional<ActionEncoding> choose_random_action(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    std::mt19937& rng
);

std::optional<ActionEncoding> choose_minimal_hybrid(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    const MinimalHybridParams& params = {}
);

std::optional<ActionEncoding> choose_action(
    PolicyKind kind,
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    std::mt19937& rng
);

}  // namespace ts
