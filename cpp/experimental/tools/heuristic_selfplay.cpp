#include <iostream>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <string>

#include "game_data.hpp"
#include "logging.hpp"
#include "profile.hpp"
#include "runner.hpp"

int main(int argc, char** argv) {
    std::optional<uint32_t> seed = 12345u;
    std::optional<std::string> log_file_path;
    ts::experimental::HeuristicConfig config;
    bool profile = false;
    bool summary_only = false;
    for (int idx = 1; idx < argc; ++idx) {
        const std::string arg = argv[idx];
        auto require_value = [&](const char* flag) -> std::string {
            if (idx + 1 >= argc) {
                throw std::invalid_argument(std::string("missing value for ") + flag);
            }
            return argv[++idx];
        };
        if (arg == "--seed") {
            seed = static_cast<uint32_t>(std::stoul(require_value("--seed")));
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
        } else if (arg == "--max-turns") {
            config.max_turns = std::stoi(require_value("--max-turns"));
        } else if (arg == "--max-steps") {
            config.max_trace_steps = std::stoi(require_value("--max-steps"));
        } else if (arg == "--profile") {
            profile = true;
        } else if (arg == "--summary-only") {
            summary_only = true;
        } else if (arg == "--log-file") {
            log_file_path = require_value("--log-file");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "usage: ts_experimental_selfplay "
                      << "[--seed N] [--proposal-limit N] [--proposal-limit-ussr N] [--proposal-limit-us N] "
                      << "[--proposal-europe-support-pressure-bonus X] "
                      << "[--proposal-europe-support-pressure-bonus-ussr X] [--proposal-europe-support-pressure-bonus-us X] "
                      << "[--search-candidate-limit N] "
                      << "[--exact-root-eval-limit N] [--ndet N] [--nsim N] [--depth N] [--rollout-plies N] "
                      << "[--max-turns N] [--max-steps N] [--profile] [--summary-only] [--log-file PATH]\n";
            return 0;
        } else if (idx == 1 && !arg.starts_with("--")) {
            seed = static_cast<uint32_t>(std::stoul(arg));
        } else {
            throw std::invalid_argument("unknown arg: " + arg);
        }
    }
    ts::experimental::logging::TeeLogger logger(log_file_path);
    ts::experimental::profile::set_enabled(profile);
    ts::experimental::profile::reset();
    const auto trace = ts::experimental::play_selfplay_game(seed, config);
    std::ostringstream winner;
    if (trace.result.winner == ts::Side::USSR) {
        winner << "USSR";
    } else if (trace.result.winner == ts::Side::US) {
        winner << "US";
    } else {
        winner << "draw";
    }
    TS_EXP_LOG(
        logger,
        "winner=",
        winner.str(),
        " final_vp=",
        trace.result.final_vp,
        " end_turn=",
        trace.result.end_turn,
        " end_reason=",
        trace.result.end_reason,
        " steps=",
        trace.steps.size()
    );
    if (!summary_only) {
        for (const auto& step : trace.steps) {
            TS_EXP_LOG(
                logger,
                "turn=",
                step.turn,
                " ar=",
                step.ar,
                " side=",
                (step.side == ts::Side::USSR ? "USSR" : "US"),
                " card=",
                static_cast<int>(step.action.card_id),
                " name=\"",
                ts::card_spec(step.action.card_id).name,
                "\" mode=",
                static_cast<int>(step.action.mode),
                " targets=",
                step.action.targets.size(),
                " static=",
                step.static_score,
                " rollout=",
                step.rollout_score,
                " visits=",
                step.search_visits
            );
        }
    }
    if (profile) {
        logger.raw(ts::experimental::profile::report());
    }
    return 0;
}
