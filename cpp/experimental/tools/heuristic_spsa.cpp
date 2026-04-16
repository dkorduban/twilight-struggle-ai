#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <optional>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

#include "logging.hpp"
#include "runner.hpp"

namespace {

using ts::GameResult;
using ts::Side;
using ts::experimental::ExperimentalAgentKind;
using ts::experimental::ExperimentalAgentSpec;
using ts::experimental::HeuristicConfig;

struct TunedField {
    const char* name;
    double HeuristicConfig::*member = nullptr;
    double min_value = 0.0;
    double max_value = 0.0;
    double perturb = 0.0;
};

double clamp_value(double value, double min_value, double max_value) {
    return std::min(max_value, std::max(min_value, value));
}

double signed_vp_for_search(const GameResult& result, Side search_side) {
    return search_side == Side::USSR ? static_cast<double>(result.final_vp) : -static_cast<double>(result.final_vp);
}

double seat_objective(const std::vector<GameResult>& results, Side search_side) {
    if (results.empty()) {
        return 0.0;
    }
    double total = 0.0;
    for (const auto& result : results) {
        if (result.winner == search_side) {
            total += 1.0;
        } else if (result.winner == ts::other_side(search_side)) {
            total -= 1.0;
        }
        total += 0.02 * clamp_value(signed_vp_for_search(result, search_side), -24.0, 24.0);
    }
    return total / static_cast<double>(results.size());
}

double evaluate_vs_minimal(
    const HeuristicConfig& config,
    int games_per_seat,
    uint32_t seed,
    int thread_count,
    bool verbose,
    ts::experimental::logging::TeeLogger* logger = nullptr
) {
    const auto search = ExperimentalAgentSpec{.kind = ExperimentalAgentKind::Search, .model_path = {}};
    const auto minimal = ExperimentalAgentSpec{.kind = ExperimentalAgentKind::MinimalHybrid, .model_path = {}};
    const auto ussr_results = ts::experimental::play_matchup_games(
        search,
        minimal,
        games_per_seat,
        seed,
        config,
        thread_count
    );
    const auto us_results = ts::experimental::play_matchup_games(
        minimal,
        search,
        games_per_seat,
        seed ^ 0x9e3779b9u,
        config,
        thread_count
    );
    const double ussr_score = seat_objective(ussr_results, Side::USSR);
    const double us_score = seat_objective(us_results, Side::US);
    if (verbose) {
        const auto ussr_summary = ts::summarize_results(ussr_results);
        const auto us_summary = ts::summarize_results(us_results);
        auto& out = *logger;
        TS_EXP_LOG(
            out,
            "ussr_seat games=",
            ussr_summary.games,
            " wins=",
            ussr_summary.ussr_wins,
            " losses=",
            ussr_summary.us_wins,
            " avg_vp=",
            ussr_summary.avg_final_vp,
            " avg_turn=",
            ussr_summary.avg_turn
        );
        TS_EXP_LOG(
            out,
            "us_seat games=",
            us_summary.games,
            " wins=",
            us_summary.us_wins,
            " losses=",
            us_summary.ussr_wins,
            " avg_vp=",
            -us_summary.avg_final_vp,
            " avg_turn=",
            us_summary.avg_turn
        );
    }
    return 0.5 * (ussr_score + us_score);
}

void print_config(
    ts::experimental::logging::TeeLogger& logger,
    const HeuristicConfig& config,
    const std::vector<TunedField>& fields
) {
    for (const auto& field : fields) {
        TS_EXP_LOG(logger, field.name, "=", config.*(field.member));
    }
}

std::vector<TunedField> tuned_fields() {
    return {
        {"current_scoring_weight", &HeuristicConfig::current_scoring_weight, 0.10, 0.60, 0.05},
        {"region_europe_weight", &HeuristicConfig::region_europe_weight, 0.70, 1.80, 0.08},
        {"region_asia_weight", &HeuristicConfig::region_asia_weight, 0.60, 1.60, 0.08},
        {"region_middle_east_weight", &HeuristicConfig::region_middle_east_weight, 0.50, 1.40, 0.08},
        {"region_central_america_weight", &HeuristicConfig::region_central_america_weight, 0.40, 1.30, 0.08},
        {"region_south_america_weight", &HeuristicConfig::region_south_america_weight, 0.50, 1.40, 0.08},
        {"region_africa_weight", &HeuristicConfig::region_africa_weight, 0.40, 1.30, 0.08},
        {"region_se_asia_weight", &HeuristicConfig::region_se_asia_weight, 0.35, 1.10, 0.06},
        {"special_hand_weight", &HeuristicConfig::special_hand_weight, 0.05, 0.80, 0.05},
        {"pair_threat_weight", &HeuristicConfig::pair_threat_weight, 0.10, 1.20, 0.08},
        {"info_card_weight", &HeuristicConfig::info_card_weight, 0.10, 1.20, 0.08},
        {"china_available_value", &HeuristicConfig::china_available_value, 0.40, 1.60, 0.08},
        {"china_unavailable_value", &HeuristicConfig::china_unavailable_value, 0.10, 1.00, 0.05},
        {"proposal_coup_milops_weight", &HeuristicConfig::proposal_coup_milops_weight, 0.20, 1.60, 0.10},
        {"proposal_coup_expected_weight", &HeuristicConfig::proposal_coup_expected_weight, 0.10, 0.80, 0.08},
        {"proposal_coup_access_weight", &HeuristicConfig::proposal_coup_access_weight, 0.10, 1.20, 0.08},
        {"proposal_coup_control_break_bonus", &HeuristicConfig::proposal_coup_control_break_bonus, 0.10, 1.20, 0.08},
        {"proposal_country_battleground_scale", &HeuristicConfig::proposal_country_battleground_scale, 1.20, 3.40, 0.12},
        {"proposal_country_key_access_scale", &HeuristicConfig::proposal_country_key_access_scale, 0.20, 1.60, 0.10},
        {"proposal_country_other_scale", &HeuristicConfig::proposal_country_other_scale, 0.05, 1.10, 0.08},
        {"proposal_country_safe_nonbg_penalty", &HeuristicConfig::proposal_country_safe_nonbg_penalty, 0.10, 1.20, 0.08},
        {"proposal_country_count_scale", &HeuristicConfig::proposal_country_count_scale, 0.00, 1.20, 0.08},
        {"proposal_europe_support_pressure_bonus", &HeuristicConfig::proposal_europe_support_pressure_bonus, 0.00, 2.00, 0.10},
        {"proposal_influence_local_weight", &HeuristicConfig::proposal_influence_local_weight, 0.05, 1.20, 0.08},
        {"proposal_influence_defend_weight", &HeuristicConfig::proposal_influence_defend_weight, 0.20, 1.60, 0.10},
        {"proposal_influence_attack_weight", &HeuristicConfig::proposal_influence_attack_weight, 0.20, 1.60, 0.10},
        {"proposal_influence_access_weight", &HeuristicConfig::proposal_influence_access_weight, 0.20, 1.60, 0.10},
        {"proposal_influence_prep_weight", &HeuristicConfig::proposal_influence_prep_weight, 0.20, 1.60, 0.10},
        {"proposal_influence_overstack_penalty", &HeuristicConfig::proposal_influence_overstack_penalty, 0.02, 0.60, 0.04},
        {"proposal_influence_repeat_penalty", &HeuristicConfig::proposal_influence_repeat_penalty, 0.20, 2.20, 0.10},
        {"proposal_scoring_backlog_penalty", &HeuristicConfig::proposal_scoring_backlog_penalty, 0.20, 2.20, 0.10},
    };
}

void print_usage() {
    std::cerr << "usage: ts_experimental_spsa "
              << "[--steps N] [--games-per-seat N] [--eval-games-per-seat N] [--seed N] "
              << "[--threads N] [--proposal-limit N] [--search-candidate-limit N] "
              << "[--exact-root-eval-limit N] [--ndet N] [--nsim N] [--depth N] "
              << "[--log-file PATH]\n";
}

}  // namespace

int main(int argc, char** argv) {
    int steps = 8;
    int games_per_seat = 6;
    int eval_games_per_seat = 25;
    uint32_t seed = 12345u;
    int threads = std::max(1u, std::thread::hardware_concurrency() / 2);
    std::optional<std::string> log_file_path;
    HeuristicConfig config;

    for (int idx = 1; idx < argc; ++idx) {
        const std::string arg = argv[idx];
        auto require_value = [&](const char* flag) -> std::string {
            if (idx + 1 >= argc) {
                throw std::invalid_argument(std::string("missing value for ") + flag);
            }
            return argv[++idx];
        };
        if (arg == "--steps") {
            steps = std::stoi(require_value("--steps"));
        } else if (arg == "--games-per-seat") {
            games_per_seat = std::stoi(require_value("--games-per-seat"));
        } else if (arg == "--eval-games-per-seat") {
            eval_games_per_seat = std::stoi(require_value("--eval-games-per-seat"));
        } else if (arg == "--seed") {
            seed = static_cast<uint32_t>(std::stoul(require_value("--seed")));
        } else if (arg == "--threads") {
            threads = std::stoi(require_value("--threads"));
        } else if (arg == "--proposal-limit") {
            config.proposal_limit = std::stoi(require_value("--proposal-limit"));
        } else if (arg == "--proposal-limit-ussr") {
            config.proposal_limit_ussr = std::stoi(require_value("--proposal-limit-ussr"));
        } else if (arg == "--proposal-limit-us") {
            config.proposal_limit_us = std::stoi(require_value("--proposal-limit-us"));
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
        } else if (arg == "--log-file") {
            log_file_path = require_value("--log-file");
        } else if (arg == "--help" || arg == "-h") {
            print_usage();
            return 0;
        } else {
            throw std::invalid_argument("unknown arg: " + arg);
        }
    }

    config.benchmark_threads = threads;
    ts::experimental::logging::TeeLogger logger(log_file_path);
    const auto fields = tuned_fields();
    std::mt19937 rng(seed);
    std::uniform_int_distribution<int> sign_dist(0, 1);

    double current_score = evaluate_vs_minimal(config, games_per_seat, seed, threads, false);
    HeuristicConfig best_config = config;
    double best_score = current_score;
    TS_EXP_LOG(logger, "baseline_score=", current_score);

    constexpr double kA = 0.18;
    constexpr double kC = 1.0;
    constexpr double kStability = 4.0;
    constexpr double kAlpha = 0.602;
    constexpr double kGamma = 0.101;

    for (int step = 0; step < steps; ++step) {
        const double a_k = kA / std::pow(kStability + static_cast<double>(step) + 1.0, kAlpha);
        const double c_k = kC / std::pow(static_cast<double>(step) + 1.0, kGamma);

        std::vector<int> delta(fields.size(), 1);
        for (size_t idx = 0; idx < fields.size(); ++idx) {
            delta[idx] = sign_dist(rng) == 0 ? -1 : 1;
        }

        HeuristicConfig plus = config;
        HeuristicConfig minus = config;
        for (size_t idx = 0; idx < fields.size(); ++idx) {
            const auto& field = fields[idx];
            plus.*(field.member) = clamp_value(
                plus.*(field.member) + c_k * field.perturb * static_cast<double>(delta[idx]),
                field.min_value,
                field.max_value
            );
            minus.*(field.member) = clamp_value(
                minus.*(field.member) - c_k * field.perturb * static_cast<double>(delta[idx]),
                field.min_value,
                field.max_value
            );
        }

        const uint32_t step_seed = seed + static_cast<uint32_t>(7919 * (step + 1));
        const double plus_score = evaluate_vs_minimal(plus, games_per_seat, step_seed, threads, false);
        const double minus_score = evaluate_vs_minimal(minus, games_per_seat, step_seed, threads, false);

        for (size_t idx = 0; idx < fields.size(); ++idx) {
            const auto& field = fields[idx];
            const double grad = (plus_score - minus_score)
                / (2.0 * c_k * field.perturb * static_cast<double>(delta[idx]));
            config.*(field.member) = clamp_value(
                config.*(field.member) + a_k * grad * field.perturb,
                field.min_value,
                field.max_value
            );
        }

        current_score = evaluate_vs_minimal(config, games_per_seat, step_seed ^ 0x85ebca6bu, threads, false);
        if (current_score > best_score) {
            best_score = current_score;
            best_config = config;
        }

        TS_EXP_LOG(
            logger,
            "step=",
            (step + 1),
            " plus=",
            plus_score,
            " minus=",
            minus_score,
            " current=",
            current_score,
            " best=",
            best_score
        );
    }

    TS_EXP_LOG(logger, "best_tuning_score=", best_score);
    TS_EXP_LOG(logger, "best_config");
    print_config(logger, best_config, fields);

    const double final_score = evaluate_vs_minimal(
        best_config,
        eval_games_per_seat,
        seed ^ 0x1234abcdu,
        threads,
        true,
        &logger
    );
    TS_EXP_LOG(logger, "final_eval_score=", final_score);
    return 0;
}
