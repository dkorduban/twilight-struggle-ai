#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "runner.hpp"

namespace py = pybind11;

namespace {

ts::experimental::HeuristicConfig config_from_python(const py::handle& obj) {
    ts::experimental::HeuristicConfig config;
    if (obj.is_none()) {
        return config;
    }
    const auto d = py::reinterpret_borrow<py::dict>(obj);
    auto load = [&](const char* key, auto& field) {
        if (d.contains(py::str(key))) {
            field = d[py::str(key)].cast<std::decay_t<decltype(field)>>();
        }
    };
    load("max_influence_targets", config.max_influence_targets);
    load("proposal_limit", config.proposal_limit);
    load("proposal_limit_ussr", config.proposal_limit_ussr);
    load("proposal_limit_us", config.proposal_limit_us);
    load("search_candidate_limit", config.search_candidate_limit);
    load("rollout_plies", config.rollout_plies);
    load("rollout_samples", config.rollout_samples);
    load("ismcts_determinizations", config.ismcts_determinizations);
    load("ismcts_simulations", config.ismcts_simulations);
    load("ismcts_max_depth", config.ismcts_max_depth);
    load("benchmark_threads", config.benchmark_threads);
    load("progressive_widening_base", config.progressive_widening_base);
    load("progressive_widening_alpha", config.progressive_widening_alpha);
    load("uct_c", config.uct_c);
    load("prior_temperature", config.prior_temperature);
    load("q0_weight", config.q0_weight);
    load("vp_weight", config.vp_weight);
    load("final_scoring_weight", config.final_scoring_weight);
    load("current_scoring_weight", config.current_scoring_weight);
    load("region_europe_weight", config.region_europe_weight);
    load("region_asia_weight", config.region_asia_weight);
    load("region_middle_east_weight", config.region_middle_east_weight);
    load("region_central_america_weight", config.region_central_america_weight);
    load("region_south_america_weight", config.region_south_america_weight);
    load("region_africa_weight", config.region_africa_weight);
    load("region_se_asia_weight", config.region_se_asia_weight);
    load("bg_pressure_weight", config.bg_pressure_weight);
    load("access_weight", config.access_weight);
    load("overcontrol_weight", config.overcontrol_weight);
    load("milops_edge_weight", config.milops_edge_weight);
    load("defcon_edge_weight", config.defcon_edge_weight);
    load("space_edge_weight", config.space_edge_weight);
    load("china_edge_weight", config.china_edge_weight);
    load("china_available_value", config.china_available_value);
    load("china_unavailable_value", config.china_unavailable_value);
    load("china_asia_live_bonus", config.china_asia_live_bonus);
    load("board_control_weight", config.board_control_weight);
    load("hand_ops_weight", config.hand_ops_weight);
    load("scoring_hand_weight", config.scoring_hand_weight);
    load("event_hand_weight", config.event_hand_weight);
    load("special_hand_weight", config.special_hand_weight);
    load("persistent_flag_weight", config.persistent_flag_weight);
    load("pair_threat_weight", config.pair_threat_weight);
    load("info_card_weight", config.info_card_weight);
    load("extra_ops_per_ar_weight", config.extra_ops_per_ar_weight);
    load("trap_ar_weight", config.trap_ar_weight);
    load("cmc_weight", config.cmc_weight);
    load("yuri_coup_weight", config.yuri_coup_weight);
    load("chernobyl_need_weight", config.chernobyl_need_weight);
    load("norad_trigger_weight", config.norad_trigger_weight);
    load("flower_power_war_card_weight", config.flower_power_war_card_weight);
    load("info_event_bonus_weight", config.info_event_bonus_weight);
    load("rule_event_bonus_weight", config.rule_event_bonus_weight);
    load("own_event_bonus_weight", config.own_event_bonus_weight);
    load("opp_event_penalty_weight", config.opp_event_penalty_weight);
    load("neutral_event_bonus_weight", config.neutral_event_bonus_weight);
    load("starred_event_bonus_weight", config.starred_event_bonus_weight);
    load("space_escape_weight", config.space_escape_weight);
    load("proposal_country_battleground_scale", config.proposal_country_battleground_scale);
    load("proposal_country_key_access_scale", config.proposal_country_key_access_scale);
    load("proposal_country_other_scale", config.proposal_country_other_scale);
    load("proposal_country_contested_scale", config.proposal_country_contested_scale);
    load("proposal_country_safe_nonbg_penalty", config.proposal_country_safe_nonbg_penalty);
    load("proposal_country_count_scale", config.proposal_country_count_scale);
    load("proposal_europe_support_pressure_bonus", config.proposal_europe_support_pressure_bonus);
    load("proposal_europe_support_pressure_bonus_ussr", config.proposal_europe_support_pressure_bonus_ussr);
    load("proposal_europe_support_pressure_bonus_us", config.proposal_europe_support_pressure_bonus_us);
    load("proposal_coup_country_weight", config.proposal_coup_country_weight);
    load("proposal_coup_expected_weight", config.proposal_coup_expected_weight);
    load("proposal_coup_milops_weight", config.proposal_coup_milops_weight);
    load("proposal_coup_scoring_weight", config.proposal_coup_scoring_weight);
    load("proposal_coup_access_weight", config.proposal_coup_access_weight);
    load("proposal_coup_bg_template_bonus", config.proposal_coup_bg_template_bonus);
    load("proposal_coup_nonbg_template_bonus", config.proposal_coup_nonbg_template_bonus);
    load("proposal_coup_control_break_bonus", config.proposal_coup_control_break_bonus);
    load("proposal_coup_defcon_penalty", config.proposal_coup_defcon_penalty);
    load("proposal_coup_safe_penalty", config.proposal_coup_safe_penalty);
    load("proposal_coup_shallow_penalty", config.proposal_coup_shallow_penalty);
    load("proposal_realign_country_weight", config.proposal_realign_country_weight);
    load("proposal_realign_adjacency_weight", config.proposal_realign_adjacency_weight);
    load("proposal_realign_fragility_weight", config.proposal_realign_fragility_weight);
    load("proposal_realign_scoring_weight", config.proposal_realign_scoring_weight);
    load("proposal_influence_local_weight", config.proposal_influence_local_weight);
    load("proposal_influence_defend_weight", config.proposal_influence_defend_weight);
    load("proposal_influence_attack_weight", config.proposal_influence_attack_weight);
    load("proposal_influence_access_weight", config.proposal_influence_access_weight);
    load("proposal_influence_prep_weight", config.proposal_influence_prep_weight);
    load("proposal_influence_overprotect_weight", config.proposal_influence_overprotect_weight);
    load("proposal_influence_overstack_penalty", config.proposal_influence_overstack_penalty);
    load("proposal_scoring_backlog_penalty", config.proposal_scoring_backlog_penalty);
    load("proposal_uniform_mix", config.proposal_uniform_mix);
    load("playable_china_bonus", config.playable_china_bonus);
    load("terminal_bonus", config.terminal_bonus);
    return config;
}

py::dict action_to_dict(const ts::ActionEncoding& action) {
    py::dict out;
    out["card_id"] = action.card_id;
    out["mode"] = static_cast<int>(action.mode);
    out["targets"] = action.targets;
    return out;
}

py::dict trace_to_dict(const ts::experimental::ExperimentalTrace& trace) {
    py::dict out;
    py::list steps;
    for (const auto& step : trace.steps) {
        py::dict item;
        item["turn"] = step.turn;
        item["ar"] = step.ar;
        item["side"] = static_cast<int>(step.side);
        item["action"] = action_to_dict(step.action);
        item["static_score"] = step.static_score;
        item["rollout_score"] = step.rollout_score;
        item["search_visits"] = step.search_visits;
        steps.append(item);
    }
    out["steps"] = steps;
    py::dict result;
    if (trace.result.winner.has_value()) {
        result["winner"] = py::int_(static_cast<int>(*trace.result.winner));
    } else {
        result["winner"] = py::none();
    }
    result["final_vp"] = trace.result.final_vp;
    result["end_turn"] = trace.result.end_turn;
    result["end_reason"] = trace.result.end_reason;
    out["result"] = result;
    return out;
}

}  // namespace

PYBIND11_MODULE(ts_experimental, m) {
    m.doc() = "Experimental Twilight Struggle heuristic self-play bindings";
    m.def(
        "play_selfplay_game",
        [](py::object seed_obj, py::object config_obj) {
            std::optional<uint32_t> seed = std::nullopt;
            if (!seed_obj.is_none()) {
                seed = seed_obj.cast<uint32_t>();
            }
            return trace_to_dict(ts::experimental::play_selfplay_game(seed, config_from_python(config_obj)));
        },
        py::arg("seed") = py::none(),
        py::arg("config") = py::dict()
    );
}
