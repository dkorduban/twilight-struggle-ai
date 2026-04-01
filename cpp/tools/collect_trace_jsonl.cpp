// Collect whole-game native traces as JSONL for parity debugging and offline
// inspection.

#include <cstdint>
#include <fstream>
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
    throw std::invalid_argument("unsupported policy kind");
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
    }
    return "Unknown";
}

void usage(const char* argv0) {
    std::cerr
        << "usage: " << argv0
        << " --out trace.jsonl [--games N] [--seed N]"
        << " [--ussr-policy random|minimal_hybrid] [--us-policy random|minimal_hybrid]"
        << " [--learned-model scripted.pt --learned-side ussr|us]\n";
}

}  // namespace

int main(int argc, char** argv) {
    std::optional<std::string> out_path;
    int game_count = 10;
    std::optional<uint32_t> seed = 12345U;
    auto ussr_policy_kind = ts::PolicyKind::MinimalHybrid;
    auto us_policy_kind = ts::PolicyKind::Random;
    std::optional<std::string> learned_model;
    auto learned_side = ts::Side::USSR;

    for (int i = 1; i < argc; ++i) {
        const std::string_view arg = argv[i];
        auto require_value = [&](const char* flag) -> std::string_view {
            if (i + 1 >= argc) {
                throw std::invalid_argument(std::string("missing value for ") + flag);
            }
            return argv[++i];
        };

        if (arg == "--out") {
            out_path = std::string(require_value("--out"));
        } else if (arg == "--games") {
            game_count = std::stoi(std::string(require_value("--games")));
        } else if (arg == "--seed") {
            seed = static_cast<uint32_t>(std::stoul(std::string(require_value("--seed"))));
        } else if (arg == "--ussr-policy") {
            ussr_policy_kind = parse_policy(require_value("--ussr-policy"));
        } else if (arg == "--us-policy") {
            us_policy_kind = parse_policy(require_value("--us-policy"));
        } else if (arg == "--learned-model") {
            learned_model = std::string(require_value("--learned-model"));
        } else if (arg == "--learned-side") {
            const auto side = require_value("--learned-side");
            learned_side = side == "us" ? ts::Side::US : ts::Side::USSR;
        } else if (arg == "--help" || arg == "-h") {
            usage(argv[0]);
            return 0;
        } else {
            usage(argv[0]);
            return 2;
        }
    }

    if (!out_path.has_value()) {
        usage(argv[0]);
        return 2;
    }

    std::optional<ts::TorchScriptPolicy> learned_policy;
    if (learned_model.has_value()) {
        learned_policy.emplace(*learned_model);
    }

    const ts::PolicyFn ussr_policy = [ussr_policy_kind, &learned_policy, learned_side](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
        if (learned_policy.has_value() && learned_side == ts::Side::USSR) {
            return learned_policy->choose_action(pub, hand, holds_china, rng);
        }
        return ts::choose_action(ussr_policy_kind, pub, hand, holds_china, rng);
    };
    const ts::PolicyFn us_policy = [us_policy_kind, &learned_policy, learned_side](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
        if (learned_policy.has_value() && learned_side == ts::Side::US) {
            return learned_policy->choose_action(pub, hand, holds_china, rng);
        }
        return ts::choose_action(us_policy_kind, pub, hand, holds_china, rng);
    };

    std::ofstream out(*out_path);
    if (!out) {
        throw std::runtime_error("failed to open output file");
    }

    const auto base_seed = seed.value_or(12345U);
    for (int game_index = 0; game_index < game_count; ++game_index) {
        const auto traced = ts::play_game_traced_fn(ussr_policy, us_policy, base_seed + static_cast<uint32_t>(game_index));
        for (size_t step_index = 0; step_index < traced.steps.size(); ++step_index) {
            const auto& step = traced.steps[step_index];
            out
                << "{\"game_index\":" << game_index
                << ",\"step_index\":" << step_index
                << ",\"turn\":" << step.turn
                << ",\"ar\":" << step.ar
                << ",\"side\":\"" << side_name(step.side) << "\""
                << ",\"holds_china\":" << (step.holds_china ? "true" : "false")
                << ",\"card_id\":" << static_cast<int>(step.action.card_id)
                << ",\"mode\":\"" << mode_name(step.action.mode) << "\""
                << ",\"targets\":[";
            for (size_t i = 0; i < step.action.targets.size(); ++i) {
                if (i > 0) {
                    out << ",";
                }
                out << static_cast<int>(step.action.targets[i]);
            }
            out
                << "],\"vp_before\":" << step.vp_before
                << ",\"vp_after\":" << step.vp_after
                << ",\"defcon_before\":" << step.defcon_before
                << ",\"defcon_after\":" << step.defcon_after
                << ",\"winner\":\"";
            if (!traced.result.winner.has_value()) {
                out << "Draw";
            } else {
                out << side_name(*traced.result.winner);
            }
            out
                << "\",\"end_turn\":" << traced.result.end_turn
                << ",\"end_reason\":\"" << traced.result.end_reason << "\"}\n";
        }
    }

    return 0;
}
