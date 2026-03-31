#include <chrono>
#include <cstdint>
#include <iostream>
#include <optional>
#include <stdexcept>
#include <string_view>

#include "game_loop.hpp"
#include "learned_policy.hpp"

namespace {

ts::PolicyKind parse_policy(std::string_view name) {
    if (name == "random") {
        return ts::PolicyKind::Random;
    }
    if (name == "minimal" || name == "minimal_hybrid") {
        return ts::PolicyKind::MinimalHybrid;
    }
    throw std::invalid_argument("unsupported fallback policy kind");
}

void usage(const char* argv0) {
    std::cerr
        << "usage: " << argv0
        << " --model scripted.pt [--games N] [--seed N]"
        << " [--learned-side ussr|us] [--opponent-policy random|minimal_hybrid]\n";
}

}  // namespace

int main(int argc, char** argv) {
    std::optional<std::string> model_path;
    int game_count = 20;
    std::optional<uint32_t> seed = 12345U;
    auto learned_side = ts::Side::USSR;
    auto opponent_policy = ts::PolicyKind::Random;

    for (int i = 1; i < argc; ++i) {
        const std::string_view arg = argv[i];
        auto require_value = [&](const char* flag) -> std::string_view {
            if (i + 1 >= argc) {
                throw std::invalid_argument(std::string("missing value for ") + flag);
            }
            return argv[++i];
        };

        if (arg == "--model") {
            model_path = std::string(require_value("--model"));
        } else if (arg == "--games") {
            game_count = std::stoi(std::string(require_value("--games")));
        } else if (arg == "--seed") {
            seed = static_cast<uint32_t>(std::stoul(std::string(require_value("--seed"))));
        } else if (arg == "--learned-side") {
            const auto side = require_value("--learned-side");
            learned_side = side == "us" ? ts::Side::US : ts::Side::USSR;
        } else if (arg == "--opponent-policy") {
            opponent_policy = parse_policy(require_value("--opponent-policy"));
        } else if (arg == "--help" || arg == "-h") {
            usage(argv[0]);
            return 0;
        } else {
            usage(argv[0]);
            return 2;
        }
    }

    if (!model_path.has_value()) {
        usage(argv[0]);
        return 2;
    }

    ts::TorchScriptPolicy learned(*model_path);
    const ts::PolicyFn learned_fn = [&learned](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, std::mt19937& rng) {
        return learned.choose_action(pub, hand, holds_china, rng);
    };
    const ts::PolicyFn opponent_fn = [opponent_policy](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, std::mt19937& rng) {
        return ts::choose_action(opponent_policy, pub, hand, holds_china, rng);
    };

    const auto start = std::chrono::steady_clock::now();
    const auto results = learned_side == ts::Side::USSR
        ? ts::play_matchup_fn(learned_fn, opponent_fn, game_count, seed)
        : ts::play_matchup_fn(opponent_fn, learned_fn, game_count, seed);
    const auto stop = std::chrono::steady_clock::now();

    const auto summary = ts::summarize_results(results);
    const auto elapsed = std::chrono::duration<double>(stop - start).count();

    std::cout
        << "games=" << summary.games
        << " elapsed_sec=" << elapsed
        << " games_per_sec=" << (elapsed > 0.0 ? static_cast<double>(summary.games) / elapsed : 0.0)
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
