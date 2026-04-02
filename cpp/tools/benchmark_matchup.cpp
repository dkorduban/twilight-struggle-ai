// Benchmark native policy-vs-policy matchups without involving the Python loop.
// Supports per-side temperature-based Boltzmann sampling for the heuristic policy.

#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <optional>
#include <string_view>

#include "game_loop.hpp"
#include "human_openings.hpp"
#include "policies.hpp"

namespace {

void usage(const char* argv0) {
    std::cerr
        << "usage: " << argv0
        << " [--games N] [--seed N]"
        << " [--ussr-temperature F] [--us-temperature F]"
        << " [--json]\n";
}

}  // namespace

int main(int argc, char** argv) {
    int game_count = 100;
    std::optional<uint32_t> seed = 12345U;
    double ussr_temperature = 0.0;
    double us_temperature = 0.0;
    bool json_output = false;
    bool no_setup = false;
    bool nash_temperatures = false;
    int us_bid = 0;

    for (int i = 1; i < argc; ++i) {
        const std::string_view arg = argv[i];
        auto require_value = [&](const char* flag) -> std::string_view {
            if (i + 1 >= argc) {
                throw std::invalid_argument(std::string("missing value for ") + flag);
            }
            return argv[++i];
        };

        if (arg == "--games") {
            game_count = std::stoi(std::string(require_value("--games")));
        } else if (arg == "--seed") {
            seed = static_cast<uint32_t>(std::stoul(std::string(require_value("--seed"))));
        } else if (arg == "--ussr-temperature") {
            ussr_temperature = std::stod(std::string(require_value("--ussr-temperature")));
        } else if (arg == "--us-temperature") {
            us_temperature = std::stod(std::string(require_value("--us-temperature")));
        } else if (arg == "--temperature") {
            // Convenience: set both sides to the same temperature.
            double t = std::stod(std::string(require_value("--temperature")));
            ussr_temperature = t;
            us_temperature = t;
        } else if (arg == "--json") {
            json_output = true;
        } else if (arg == "--no-setup") {
            no_setup = true;
        } else if (arg == "--nash-temperatures") {
            nash_temperatures = true;
        } else if (arg == "--bid") {
            us_bid = std::stoi(std::string(require_value("--bid")));
        } else if (arg == "--help" || arg == "-h") {
            usage(argv[0]);
            return 0;
        } else {
            usage(argv[0]);
            return 2;
        }
    }

    // Build policy function for a given temperature.
    const auto make_policy_fn = [](double temp) -> ts::PolicyFn {
        if (temp > 0.0) {
            return [temp](const ts::PublicState& pub, const ts::CardSet& hand,
                         bool holds_china, ts::Pcg64Rng& rng)
                -> std::optional<ts::ActionEncoding> {
                return ts::choose_minimal_hybrid_sampled(pub, hand, holds_china, temp, rng);
            };
        }
        return [](const ts::PublicState& pub, const ts::CardSet& hand,
                  bool holds_china, ts::Pcg64Rng& rng)
            -> std::optional<ts::ActionEncoding> {
            return ts::choose_action(ts::PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
        };
    };

    ts::GameLoopConfig loop_config;
    loop_config.skip_setup_influence = no_setup;
    loop_config.us_bid_extra = us_bid;

    const auto start = std::chrono::steady_clock::now();

    // RNG for Nash temperature sampling (separate from game RNG)
    ts::Pcg64Rng nash_rng((seed.has_value() ? *seed : 12345U) + 999999U);

    std::vector<ts::GameResult> results;
    results.reserve(game_count);
    for (int i = 0; i < game_count; ++i) {
        double game_ussr_temp = ussr_temperature;
        double game_us_temp = us_temperature;
        if (nash_temperatures) {
            game_ussr_temp = ts::sample_nash_temperature(
                ts::kNashUSSRTemps.data(), static_cast<int>(ts::kNashUSSRTemps.size()), nash_rng);
            game_us_temp = ts::sample_nash_temperature(
                ts::kNashUSTemps.data(), static_cast<int>(ts::kNashUSTemps.size()), nash_rng);
        }
        auto ussr_fn = make_policy_fn(game_ussr_temp);
        auto us_fn = make_policy_fn(game_us_temp);
        auto game_seed = seed.has_value() ? std::optional<uint32_t>(*seed + i) : std::nullopt;
        auto traced = ts::play_game_traced_fn(ussr_fn, us_fn, game_seed, loop_config);
        results.push_back(std::move(traced.result));
    }

    const auto stop = std::chrono::steady_clock::now();
    const auto elapsed = std::chrono::duration<double>(stop - start).count();
    const auto games_per_second = elapsed > 0.0 ? static_cast<double>(results.size()) / elapsed : 0.0;

    const auto summary = ts::summarize_results(results);
    int decisive = summary.ussr_wins + summary.us_wins;
    double ussr_wr = decisive > 0 ? 100.0 * summary.ussr_wins / decisive : 0.0;
    double us_wr = decisive > 0 ? 100.0 * summary.us_wins / decisive : 0.0;

    if (json_output) {
        std::cout
            << "{\"games\":" << results.size()
            << ",\"ussr_temperature\":" << ussr_temperature
            << ",\"us_temperature\":" << us_temperature
            << ",\"elapsed_sec\":" << elapsed
            << ",\"games_per_sec\":" << games_per_second
            << ",\"ussr_wins\":" << summary.ussr_wins
            << ",\"us_wins\":" << summary.us_wins
            << ",\"draws\":" << summary.draws
            << ",\"decisive\":" << decisive
            << ",\"ussr_wr\":" << ussr_wr
            << ",\"us_wr\":" << us_wr
            << ",\"defcon1\":" << summary.defcon1
            << ",\"turn_limit\":" << summary.turn_limit
            << ",\"scoring_card_held\":" << summary.scoring_card_held
            << ",\"vp_threshold\":" << summary.vp_threshold
            << ",\"avg_turn\":" << summary.avg_turn
            << ",\"avg_final_vp\":" << summary.avg_final_vp
            << "}\n";
    } else {
        std::cout
            << "games=" << results.size()
            << " ussr_temp=" << ussr_temperature
            << " us_temp=" << us_temperature
            << " elapsed_sec=" << elapsed
            << " games_per_sec=" << games_per_second
            << " avg_turn=" << summary.avg_turn
            << " avg_final_vp=" << summary.avg_final_vp
            << '\n';

        std::cout
            << "ussr_wins=" << summary.ussr_wins
            << " us_wins=" << summary.us_wins
            << " draws=" << summary.draws
            << " ussr_wr=" << ussr_wr << "%"
            << " us_wr=" << us_wr << "%"
            << " defcon1=" << summary.defcon1
            << " turn_limit=" << summary.turn_limit
            << " scoring_card_held=" << summary.scoring_card_held
            << " vp_threshold=" << summary.vp_threshold
            << '\n';
    }

    return 0;
}
