#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <optional>
#include <string_view>

#include "game_loop.hpp"

namespace {

ts::PolicyKind parse_policy(std::string_view name) {
    if (name == "random") {
        return ts::PolicyKind::Random;
    }
    if (name == "minimal" || name == "minimal_hybrid") {
        return ts::PolicyKind::MinimalHybrid;
    }
    throw std::invalid_argument("unsupported policy kind");
}

void usage(const char* argv0) {
    std::cerr
        << "usage: " << argv0
        << " [--games N] [--seed N] [--ussr-policy random|minimal_hybrid]"
        << " [--us-policy random|minimal_hybrid]\n";
}

}  // namespace

int main(int argc, char** argv) {
    int game_count = 100;
    std::optional<uint32_t> seed = 12345U;
    auto ussr_policy = ts::PolicyKind::MinimalHybrid;
    auto us_policy = ts::PolicyKind::MinimalHybrid;

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
        } else if (arg == "--ussr-policy") {
            ussr_policy = parse_policy(require_value("--ussr-policy"));
        } else if (arg == "--us-policy") {
            us_policy = parse_policy(require_value("--us-policy"));
        } else if (arg == "--help" || arg == "-h") {
            usage(argv[0]);
            return 0;
        } else {
            usage(argv[0]);
            return 2;
        }
    }

    const auto start = std::chrono::steady_clock::now();
    const auto results = ts::play_matchup(ussr_policy, us_policy, game_count, seed);
    const auto stop = std::chrono::steady_clock::now();

    const auto summary = ts::summarize_results(results);

    const auto elapsed = std::chrono::duration<double>(stop - start).count();
    const auto games_per_second = elapsed > 0.0 ? static_cast<double>(results.size()) / elapsed : 0.0;

    std::cout
        << "games=" << results.size()
        << " elapsed_sec=" << elapsed
        << " games_per_sec=" << games_per_second
        << " avg_turn=" << summary.avg_turn
        << " avg_final_vp=" << summary.avg_final_vp
        << '\n';

    std::cout
        << "ussr_wins=" << summary.ussr_wins
        << " us_wins=" << summary.us_wins
        << " draws=" << summary.draws
        << " defcon1=" << summary.defcon1
        << " turn_limit=" << summary.turn_limit
        << " scoring_card_held=" << summary.scoring_card_held
        << " vp_threshold=" << summary.vp_threshold
        << '\n';

    return 0;
}
