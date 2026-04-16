#pragma once

#include <functional>
#include <optional>
#include <string>
#include <vector>

#include "game_loop.hpp"
#include "policy_callback.hpp"
#include "types.hpp"

namespace ts::experimental {

struct HeuristicConfig {
    int max_turns = 10;
    int max_trace_steps = 1000000;
    int max_influence_targets = 4;
    int proposal_limit = 8;
    int proposal_limit_ussr = 0;
    int proposal_limit_us = 0;
    int search_candidate_limit = 1;
    int exact_root_eval_limit = 0;
    int rollout_plies = 0;
    int rollout_samples = 1;
    int ismcts_determinizations = 8;
    int ismcts_simulations = 400;
    int ismcts_max_depth = 1;
    int benchmark_threads = 1;
    double progressive_widening_base = 1.35;
    double progressive_widening_alpha = 0.55;
    double uct_c = 1.15;
    double prior_temperature = 1.15;
    double q0_weight = 0.35;
    double vp_weight = 1.0;
    double final_scoring_weight = 0.32;
    double current_scoring_weight = 0.3843;
    double region_europe_weight = 1.3343;
    double region_asia_weight = 1.12161;
    double region_middle_east_weight = 1.05657;
    double region_central_america_weight = 0.906572;
    double region_south_america_weight = 0.921309;
    double region_africa_weight = 0.851228;
    double region_se_asia_weight = 0.672783;
    double bg_pressure_weight = 0.25;
    double access_weight = 0.18;
    double overcontrol_weight = 0.15;
    double milops_edge_weight = 0.35;
    double defcon_edge_weight = 0.35;
    double space_edge_weight = 0.25;
    double china_edge_weight = 0.75;
    double china_available_value = 0.943428;
    double china_unavailable_value = 0.428391;
    double china_asia_live_bonus = 0.25;
    double board_control_weight = 0.12;
    double hand_ops_weight = 0.06;
    double scoring_hand_weight = 0.58;
    double event_hand_weight = 0.12;
    double special_hand_weight = 0.358311;
    double persistent_flag_weight = 0.55;
    double pair_threat_weight = 0.573347;
    double info_card_weight = 0.578391;
    double extra_ops_per_ar_weight = 0.45;
    double trap_ar_weight = 1.20;
    double cmc_weight = 2.00;
    double yuri_coup_weight = 0.40;
    double chernobyl_need_weight = 0.80;
    double norad_trigger_weight = 0.35;
    double flower_power_war_card_weight = 0.35;
    double info_event_bonus_weight = 0.60;
    double rule_event_bonus_weight = 0.60;
    double own_event_bonus_weight = 0.70;
    double opp_event_penalty_weight = 0.45;
    double neutral_event_bonus_weight = 0.15;
    double starred_event_bonus_weight = 0.15;
    double space_escape_weight = 0.55;
    double proposal_country_battleground_scale = 2.8;
    double proposal_country_key_access_scale = 0.95;
    double proposal_country_other_scale = 0.35;
    double proposal_country_contested_scale = 1.20;
    double proposal_country_safe_nonbg_penalty = 0.55;
    double proposal_country_count_scale = 0.20;
    double proposal_europe_support_pressure_bonus = 0.50;
    double proposal_europe_support_pressure_bonus_ussr = 0.0;
    double proposal_europe_support_pressure_bonus_us = 0.0;
    double proposal_coup_country_weight = 0.12;
    double proposal_coup_expected_weight = 0.42;
    double proposal_coup_milops_weight = 1.00123;
    double proposal_coup_scoring_weight = 0.28;
    double proposal_coup_access_weight = 0.529256;
    double proposal_coup_bg_template_bonus = 0.15;
    double proposal_coup_nonbg_template_bonus = 0.20;
    double proposal_coup_control_break_bonus = 0.923347;
    double proposal_coup_defcon_penalty = 0.85;
    double proposal_coup_safe_penalty = 0.25;
    double proposal_coup_shallow_penalty = 0.55;
    double proposal_realign_country_weight = 0.55;
    double proposal_realign_adjacency_weight = 0.30;
    double proposal_realign_fragility_weight = 0.25;
    double proposal_realign_scoring_weight = 0.20;
    double proposal_influence_local_weight = 0.365136;
    double proposal_influence_defend_weight = 1.09343;
    double proposal_influence_attack_weight = 1.25123;
    double proposal_influence_access_weight = 1.19877;
    double proposal_influence_prep_weight = 1.11478;
    double proposal_influence_overprotect_weight = 0.45;
    double proposal_influence_overstack_penalty = 0.328691;
    double proposal_influence_repeat_penalty = 1.45123;
    double proposal_scoring_backlog_penalty = 1.25;
    double proposal_uniform_mix = 0.10;
    double playable_china_bonus = 0.55;
    double terminal_bonus = 10000.0;
};

inline double region_weight(Region region, const HeuristicConfig& config) {
    switch (region) {
        case Region::Europe: return config.region_europe_weight;
        case Region::Asia: return config.region_asia_weight;
        case Region::MiddleEast: return config.region_middle_east_weight;
        case Region::CentralAmerica: return config.region_central_america_weight;
        case Region::SouthAmerica: return config.region_south_america_weight;
        case Region::Africa: return config.region_africa_weight;
        case Region::SoutheastAsia: return config.region_se_asia_weight;
    }
    return 1.0;
}

inline int proposal_limit_for_side(Side side, const HeuristicConfig& config) {
    if (side == Side::USSR && config.proposal_limit_ussr > 0) {
        return config.proposal_limit_ussr;
    }
    if (side == Side::US && config.proposal_limit_us > 0) {
        return config.proposal_limit_us;
    }
    return config.proposal_limit;
}

inline double europe_support_pressure_bonus_for_side(Side side, const HeuristicConfig& config) {
    if (side == Side::USSR && config.proposal_europe_support_pressure_bonus_ussr > 0.0) {
        return config.proposal_europe_support_pressure_bonus_ussr;
    }
    if (side == Side::US && config.proposal_europe_support_pressure_bonus_us > 0.0) {
        return config.proposal_europe_support_pressure_bonus_us;
    }
    return config.proposal_europe_support_pressure_bonus;
}

struct ActionProposal {
    ActionEncoding action;
    double heuristic_score = 0.0;
    double prior = 0.0;
};

struct ScriptDecision {
    CardId source_card = 0;
    DecisionKind kind = DecisionKind::SmallChoice;
    Side acting_side = Side::Neutral;
    int chosen_index = 0;
    int chosen_id = 0;
};

struct CallbackScript {
    std::vector<ScriptDecision> decisions;
};

struct PlannedAction {
    ActionEncoding action;
    CallbackScript script;
    double static_score = 0.0;
    double rollout_score = 0.0;
    int search_visits = 0;
};

struct ResolutionOutcome {
    bool over = false;
    std::optional<Side> winner;
};

using ResolutionFn = std::function<ResolutionOutcome(GameState&, Pcg64Rng&, const PolicyCallbackFn*)>;

struct ExperimentalStep {
    int turn = 0;
    int ar = 0;
    Side side = Side::USSR;
    ActionEncoding action;
    double static_score = 0.0;
    double rollout_score = 0.0;
    int search_visits = 0;
};

struct ExperimentalTrace {
    std::vector<ExperimentalStep> steps;
    GameResult result;
};

}  // namespace ts::experimental
