#include <iostream>
#include <optional>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <string_view>
#include <vector>

#include "game_data.hpp"
#include "game_loop.hpp"
#include "logging.hpp"
#include "profile.hpp"
#include "rng.hpp"
#include "runner.hpp"

namespace {

ts::experimental::ExperimentalAgentSpec parse_agent(std::string_view name, const std::string& model_path) {
    using ts::experimental::ExperimentalAgentKind;
    if (name == "search" || name == "experimental") {
        return {.kind = ExperimentalAgentKind::Search, .model_path = {}};
    }
    if (name == "minimal" || name == "minimal_hybrid") {
        return {.kind = ExperimentalAgentKind::MinimalHybrid, .model_path = {}};
    }
    if (name == "learned" || name == "nn") {
        return {.kind = ExperimentalAgentKind::LearnedModel, .model_path = model_path};
    }
    throw std::invalid_argument("unknown agent kind");
}

const char* side_name(ts::Side side) {
    switch (side) {
        case ts::Side::USSR: return "USSR";
        case ts::Side::US: return "US";
        case ts::Side::Neutral: return "Neutral";
    }
    return "Unknown";
}

const char* mode_name(ts::ActionMode mode) {
    switch (mode) {
        case ts::ActionMode::Influence: return "Influence";
        case ts::ActionMode::Coup: return "Coup";
        case ts::ActionMode::Realign: return "Realign";
        case ts::ActionMode::Space: return "Space";
        case ts::ActionMode::Event: return "Event";
        case ts::ActionMode::EventFirst: return "EventFirst";
    }
    return "Unknown";
}

const char* decision_kind_name(ts::DecisionKind kind) {
    switch (kind) {
        case ts::DecisionKind::SmallChoice: return "small_choice";
        case ts::DecisionKind::CountrySelect: return "country_select";
        case ts::DecisionKind::CardSelect: return "card_select";
    }
    return "unknown";
}

std::string country_name(ts::CountryId cid) {
    if (!ts::has_country_spec(cid)) {
        return std::to_string(static_cast<int>(cid));
    }
    return ts::country_spec(cid).name;
}

std::string card_name(ts::CardId card_id) {
    if (!ts::has_card_spec(card_id)) {
        return std::to_string(static_cast<int>(card_id));
    }
    return ts::card_spec(card_id).name;
}

std::string joined_target_names(const std::vector<ts::CountryId>& targets) {
    std::ostringstream out;
    for (size_t idx = 0; idx < targets.size(); ++idx) {
        if (idx > 0) {
            out << ", ";
        }
        out << country_name(targets[idx]) << "(" << static_cast<int>(targets[idx]) << ")";
    }
    return out.str();
}

std::string event_timing_desc(ts::Side side, const ts::ActionEncoding& action) {
    const auto mode = action.mode;
    if (mode == ts::ActionMode::Event) {
        return "event_only";
    }
    if (mode == ts::ActionMode::EventFirst) {
        return "opponent_event_before_ops";
    }
    if ((mode == ts::ActionMode::Influence || mode == ts::ActionMode::Coup || mode == ts::ActionMode::Realign)
        && ts::has_card_spec(action.card_id)
        && ts::card_spec(action.card_id).side == ts::other_side(side)) {
        return "opponent_event_after_ops";
    }
    return "-";
}

std::vector<ts::CountryId> changed_countries(const ts::PublicState& before, const ts::PublicState& after) {
    std::vector<ts::CountryId> changed;
    for (int cid = 0; cid <= ts::kMaxCountryId; ++cid) {
        const auto country = static_cast<ts::CountryId>(cid);
        if (!ts::has_country_spec(country)) {
            continue;
        }
        if (before.influence_of(ts::Side::USSR, country) != after.influence_of(ts::Side::USSR, country)
            || before.influence_of(ts::Side::US, country) != after.influence_of(ts::Side::US, country)) {
            changed.push_back(country);
        }
    }
    return changed;
}

void log_setup_delta(
    ts::experimental::logging::TeeLogger& logger,
    const ts::PublicState& before,
    const ts::PublicState& after,
    ts::Side side
) {
    std::ostringstream line;
    line << "setup " << side_name(side) << " added: ";
    bool any = false;
    for (int cid = 0; cid <= ts::kMaxCountryId; ++cid) {
        const auto country = static_cast<ts::CountryId>(cid);
        if (!ts::has_country_spec(country)) {
            continue;
        }
        const int delta = after.influence_of(side, country) - before.influence_of(side, country);
        if (delta <= 0) {
            continue;
        }
        if (any) {
            line << ", ";
        }
        any = true;
        line << country_name(country) << "(+" << delta << ")";
    }
    if (!any) {
        line << "-";
    }
    TS_EXP_LOG(logger, line.str());
}

std::string callback_choice_desc(const ts::experimental::ScriptDecision& decision) {
    std::ostringstream out;
    out << decision_kind_name(decision.kind)
        << " source=" << card_name(decision.source_card)
        << " acting_side=" << side_name(decision.acting_side)
        << " choice=";
    if (decision.kind == ts::DecisionKind::CountrySelect) {
        out << country_name(static_cast<ts::CountryId>(decision.chosen_id))
            << "(" << decision.chosen_id << ")";
    } else if (decision.kind == ts::DecisionKind::CardSelect) {
        out << card_name(static_cast<ts::CardId>(decision.chosen_id))
            << "(" << decision.chosen_id << ")";
    } else {
        out << decision.chosen_index;
    }
    return out.str();
}

void print_usage() {
    std::cerr << "usage: ts_experimental_matchup "
              << "[--games N] [--seed N] [--ussr search|minimal|learned] [--us search|minimal|learned] "
              << "[--ussr-model PATH] [--us-model PATH] [--proposal-europe-support-pressure-bonus X] "
              << "[--proposal-europe-support-pressure-bonus-ussr X] [--proposal-europe-support-pressure-bonus-us X] "
              << "[--max-turns N] [--max-steps N] "
              << "[--profile] [--progress] [--log-file PATH]\n";
}

}  // namespace

int main(int argc, char** argv) {
    int game_count = 4;
    std::optional<uint32_t> seed = 12345u;
    bool trace = false;
    bool profile = false;
    bool progress = false;
    std::string ussr_name = "search";
    std::string us_name = "minimal";
    std::string ussr_model_path;
    std::string us_model_path;
    std::optional<std::string> log_file_path;
    ts::experimental::HeuristicConfig config;

    for (int idx = 1; idx < argc; ++idx) {
        const std::string arg = argv[idx];
        auto require_value = [&](const char* flag) -> std::string {
            if (idx + 1 >= argc) {
                throw std::invalid_argument(std::string("missing value for ") + flag);
            }
            return argv[++idx];
        };
        if (arg == "--games") {
            game_count = std::stoi(require_value("--games"));
        } else if (arg == "--seed") {
            seed = static_cast<uint32_t>(std::stoul(require_value("--seed")));
        } else if (arg == "--ussr") {
            ussr_name = require_value("--ussr");
        } else if (arg == "--us") {
            us_name = require_value("--us");
        } else if (arg == "--ussr-model") {
            ussr_model_path = require_value("--ussr-model");
        } else if (arg == "--us-model") {
            us_model_path = require_value("--us-model");
        } else if (arg == "--proposal-limit") {
            config.proposal_limit = std::stoi(require_value("--proposal-limit"));
        } else if (arg == "--proposal-limit-ussr") {
            config.proposal_limit_ussr = std::stoi(require_value("--proposal-limit-ussr"));
        } else if (arg == "--proposal-limit-us") {
            config.proposal_limit_us = std::stoi(require_value("--proposal-limit-us"));
        } else if (arg == "--proposal-europe-support-pressure-bonus") {
            config.proposal_europe_support_pressure_bonus = std::stod(require_value("--proposal-europe-support-pressure-bonus"));
        } else if (arg == "--proposal-europe-support-pressure-bonus-ussr") {
            config.proposal_europe_support_pressure_bonus_ussr = std::stod(require_value("--proposal-europe-support-pressure-bonus-ussr"));
        } else if (arg == "--proposal-europe-support-pressure-bonus-us") {
            config.proposal_europe_support_pressure_bonus_us = std::stod(require_value("--proposal-europe-support-pressure-bonus-us"));
        } else if (arg == "--search-candidate-limit") {
            config.search_candidate_limit = std::stoi(require_value("--search-candidate-limit"));
        } else if (arg == "--exact-root-eval-limit") {
            config.exact_root_eval_limit = std::stoi(require_value("--exact-root-eval-limit"));
        } else if (arg == "--ndet") {
            config.ismcts_determinizations = std::stoi(require_value("--ndet"));
        } else if (arg == "--nsim") {
            config.ismcts_simulations = std::stoi(require_value("--nsim"));
        } else if (arg == "--depth") {
            config.ismcts_max_depth = std::stoi(require_value("--depth"));
        } else if (arg == "--rollout-plies") {
            config.rollout_plies = std::stoi(require_value("--rollout-plies"));
        } else if (arg == "--threads") {
            config.benchmark_threads = std::stoi(require_value("--threads"));
        } else if (arg == "--max-turns") {
            config.max_turns = std::stoi(require_value("--max-turns"));
        } else if (arg == "--max-steps") {
            config.max_trace_steps = std::stoi(require_value("--max-steps"));
        } else if (arg == "--trace") {
            trace = true;
        } else if (arg == "--profile") {
            profile = true;
        } else if (arg == "--progress") {
            progress = true;
        } else if (arg == "--log-file") {
            log_file_path = require_value("--log-file");
        } else if (arg == "--help" || arg == "-h") {
            print_usage();
            return 0;
        } else {
            throw std::invalid_argument("unknown arg: " + arg);
        }
    }

    const auto ussr_agent = parse_agent(ussr_name, ussr_model_path);
    const auto us_agent = parse_agent(us_name, us_model_path);
    ts::experimental::logging::TeeLogger logger(log_file_path);
    ts::experimental::profile::set_enabled(profile);
    ts::experimental::profile::reset();
    if (trace) {
        const auto traced = ts::experimental::play_matchup_game(ussr_agent, us_agent, seed, config);
        std::ostringstream winner;
        if (traced.result.winner == ts::Side::USSR) {
            winner << "USSR";
        } else if (traced.result.winner == ts::Side::US) {
            winner << "US";
        } else {
            winner << "draw";
        }
        TS_EXP_LOG(
            logger,
            "winner=",
            winner.str(),
            " final_vp=",
            traced.result.final_vp,
            " end_turn=",
            traced.result.end_turn,
            " end_reason=",
            traced.result.end_reason,
            " steps=",
            traced.steps.size()
        );
        if (traced.has_setup_snapshot) {
            TS_EXP_LOG(
                logger,
                "setup vp=",
                traced.setup_before.vp,
                "->",
                traced.setup_after.vp,
                " defcon=",
                traced.setup_before.defcon,
                "->",
                traced.setup_after.defcon
            );
            log_setup_delta(logger, traced.setup_before, traced.setup_after, ts::Side::USSR);
            log_setup_delta(logger, traced.setup_before, traced.setup_after, ts::Side::US);
        }
        for (const auto& step : traced.steps) {
            std::ostringstream header;
            header << "turn=" << step.turn
                   << " ar=" << step.ar
                   << " phase=" << (step.ar == 0 ? "headline" : "action")
                   << " side=" << side_name(step.side)
                   << " card=" << card_name(step.action.card_id)
                   << "(" << static_cast<int>(step.action.card_id) << ")"
                   << " mode=" << mode_name(step.action.mode)
                   << " event_timing=" << event_timing_desc(step.side, step.action)
                   << " targets=[" << joined_target_names(step.action.targets) << "]"
                   << " vp=" << step.pub_before.vp << "->" << step.pub_after.vp
                   << " defcon=" << step.pub_before.defcon << "->" << step.pub_after.defcon
                   << " static=" << step.static_score
                   << " rollout=" << step.rollout_score
                   << " visits=" << step.search_visits;
            TS_EXP_LOG(logger, header.str());

            const auto changed = changed_countries(step.pub_before, step.pub_after);
            if (changed.empty()) {
                TS_EXP_LOG(logger, "  changed_countries: -");
            } else {
                for (const auto cid : changed) {
                    std::ostringstream delta;
                    delta << "  " << country_name(cid)
                          << ": USSR " << step.pub_before.influence_of(ts::Side::USSR, cid)
                          << "->" << step.pub_after.influence_of(ts::Side::USSR, cid)
                          << ", US " << step.pub_before.influence_of(ts::Side::US, cid)
                          << "->" << step.pub_after.influence_of(ts::Side::US, cid);
                    TS_EXP_LOG(logger, delta.str());
                }
            }

            if (step.callback_trace.decisions.empty()) {
                TS_EXP_LOG(logger, "  callback_choices: -");
            } else {
                for (const auto& decision : step.callback_trace.decisions) {
                    TS_EXP_LOG(logger, "  callback_choice: ", callback_choice_desc(decision));
                }
            }
        }
        if (profile) {
            logger.raw(ts::experimental::profile::report());
        }
        return 0;
    }

    if (progress) {
        std::vector<ts::GameResult> results;
        results.reserve(static_cast<size_t>(std::max(0, game_count)));
        ts::Pcg64Rng seed_rng(seed.value_or(std::random_device{}()));
        for (int game = 0; game < game_count; ++game) {
            const auto game_seed = static_cast<uint32_t>(seed_rng.next_u64());
            const auto trace_result = ts::experimental::play_matchup_game(
                ussr_agent,
                us_agent,
                game_seed,
                config
            );
            results.push_back(trace_result.result);
            std::ostringstream winner;
            if (trace_result.result.winner == ts::Side::USSR) {
                winner << "USSR";
            } else if (trace_result.result.winner == ts::Side::US) {
                winner << "US";
            } else {
                winner << "draw";
            }
            TS_EXP_LOG(
                logger,
                "game=",
                (game + 1),
                " seed=",
                game_seed,
                " winner=",
                winner.str(),
                " final_vp=",
                trace_result.result.final_vp,
                " end_turn=",
                trace_result.result.end_turn,
                " end_reason=",
                trace_result.result.end_reason
            );
            const auto running = ts::summarize_results(results);
            TS_EXP_LOG(
                logger,
                "games=",
                running.games,
                " ussr_wins=",
                running.ussr_wins,
                " us_wins=",
                running.us_wins,
                " draws=",
                running.draws,
                " avg_turn=",
                running.avg_turn,
                " avg_final_vp=",
                running.avg_final_vp,
                " scoring_card_held=",
                running.scoring_card_held,
                " defcon1=",
                running.defcon1,
                " wargames=",
                running.wargames,
                " europe_control=",
                running.europe_control,
                " vp_threshold=",
                running.vp_threshold,
                " turn_limit=",
                running.turn_limit
            );
        }
    } else {
        const auto results = ts::experimental::play_matchup_games(
            ussr_agent,
            us_agent,
            game_count,
            seed,
            config,
            config.benchmark_threads > 0 ? config.benchmark_threads : 1
        );
        const auto summary = ts::summarize_results(results);
        TS_EXP_LOG(
            logger,
            "games=",
            summary.games,
            " ussr_wins=",
            summary.ussr_wins,
            " us_wins=",
            summary.us_wins,
            " draws=",
            summary.draws,
            " avg_turn=",
            summary.avg_turn,
            " avg_final_vp=",
            summary.avg_final_vp,
            " scoring_card_held=",
            summary.scoring_card_held,
            " defcon1=",
            summary.defcon1,
            " wargames=",
            summary.wargames,
            " europe_control=",
            summary.europe_control,
            " vp_threshold=",
            summary.vp_threshold,
            " turn_limit=",
            summary.turn_limit
        );
    }
    if (profile) {
        logger.raw(ts::experimental::profile::report());
    }
    return 0;
}
