// Emit native self-play rows in the JSONL shape used by downstream validation
// and collection experiments.

#include <cstdint>
#include <fstream>
#include <iostream>
#include <optional>
#include <sstream>
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

const char* game_result_str(const std::optional<ts::Side>& winner) {
    if (!winner.has_value()) {
        return "draw";
    }
    return *winner == ts::Side::USSR ? "ussr_win" : "us_win";
}

int winner_side_int(const std::optional<ts::Side>& winner) {
    if (!winner.has_value()) {
        return 0;
    }
    return *winner == ts::Side::USSR ? 1 : -1;
}

std::string targets_csv(const std::vector<ts::CountryId>& targets) {
    std::ostringstream out;
    for (size_t i = 0; i < targets.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << static_cast<int>(targets[i]);
    }
    return out.str();
}

void write_int_array(std::ostream& out, const std::vector<int>& values) {
    out << "[";
    for (size_t i = 0; i < values.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << values[i];
    }
    out << "]";
}

std::vector<int> card_mask(const ts::CardSet& cards) {
    std::vector<int> mask(ts::kCardSlots, 0);
    for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
        if (cards.test(card_id)) {
            mask[static_cast<size_t>(card_id)] = 1;
        }
    }
    return mask;
}

std::vector<int> influence_array(const ts::PublicState& pub, ts::Side side) {
    std::vector<int> values(ts::kCountrySlots, 0);
    for (int country_id = 0; country_id <= ts::kMaxCountryId; ++country_id) {
        values[static_cast<size_t>(country_id)] = pub.influence_of(side, static_cast<ts::CountryId>(country_id));
    }
    return values;
}

void usage(const char* argv0) {
    std::cerr
        << "usage: " << argv0
        << " --out rows.jsonl [--games N] [--seed N]"
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
        const auto game_id = std::string("selfplay_") + std::to_string(base_seed) + "_" + (game_index < 10 ? "000" : game_index < 100 ? "00" : game_index < 1000 ? "0" : "") + std::to_string(game_index);
        for (size_t step_idx = 0; step_idx < traced.steps.size(); ++step_idx) {
            const auto& step = traced.steps[step_idx];
            const auto& pub = step.pub_snapshot;

            auto actor_hand_mask = card_mask(step.hand_snapshot);
            std::vector<int> cq(ts::kCardSlots, 3);
            for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
                if (step.hand_snapshot.test(card_id)) {
                    cq[static_cast<size_t>(card_id)] = 0;
                }
            }
            auto discard_mask = card_mask(pub.discard);
            auto removed_mask = card_mask(pub.removed);
            auto actor_known_not_in = card_mask(pub.discard | pub.removed);
            auto opp_known_in = std::vector<int>(ts::kCardSlots, 0);
            auto opp_known_not_in = card_mask(step.hand_snapshot | pub.discard | pub.removed);
            auto opp_possible = std::vector<int>(ts::kCardSlots, 0);
            auto lbl_opponent_possible = std::vector<int>(ts::kCardSlots, 0);
            int actor_hand_size = 0;
            for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
                if (step.hand_snapshot.test(card_id) && card_id != ts::kChinaCardId) {
                    ++actor_hand_size;
                }
            }

            out
                << "{\"game_id\":\"" << game_id << "\""
                << ",\"step_idx\":" << step_idx
                << ",\"turn\":" << pub.turn
                << ",\"ar\":" << pub.ar
                << ",\"phasing\":" << static_cast<int>(step.side)
                << ",\"action_kind\":-1"
                << ",\"card_id\":" << static_cast<int>(step.action.card_id)
                << ",\"country_id\":" << (step.action.targets.empty() ? -1 : static_cast<int>(step.action.targets.front()))
                << ",\"action_card_id\":" << static_cast<int>(step.action.card_id)
                << ",\"action_mode\":" << static_cast<int>(step.action.mode)
                << ",\"action_targets\":\"" << targets_csv(step.action.targets) << "\""
                << ",\"vp\":" << pub.vp
                << ",\"defcon\":" << pub.defcon
                << ",\"milops_ussr\":" << pub.milops[ts::to_index(ts::Side::USSR)]
                << ",\"milops_us\":" << pub.milops[ts::to_index(ts::Side::US)]
                << ",\"space_ussr\":" << pub.space[ts::to_index(ts::Side::USSR)]
                << ",\"space_us\":" << pub.space[ts::to_index(ts::Side::US)]
                << ",\"china_held_by\":" << static_cast<int>(pub.china_held_by)
                << ",\"china_playable\":" << (pub.china_playable ? "true" : "false")
                << ",\"ussr_influence\":";
            write_int_array(out, influence_array(pub, ts::Side::USSR));
            out << ",\"us_influence\":";
            write_int_array(out, influence_array(pub, ts::Side::US));
            out << ",\"discard_mask\":";
            write_int_array(out, discard_mask);
            out << ",\"removed_mask\":";
            write_int_array(out, removed_mask);
            out << ",\"actor_known_in\":";
            write_int_array(out, actor_hand_mask);
            out << ",\"actor_known_not_in\":";
            write_int_array(out, actor_known_not_in);
            out << ",\"actor_possible\":";
            write_int_array(out, actor_hand_mask);
            out << ",\"actor_hand_size\":" << actor_hand_size
                << ",\"actor_holds_china\":" << (step.holds_china ? "true" : "false")
                << ",\"opp_known_in\":";
            write_int_array(out, opp_known_in);
            out << ",\"opp_known_not_in\":";
            write_int_array(out, opp_known_not_in);
            out << ",\"opp_possible\":";
            write_int_array(out, opp_possible);
            out << ",\"opp_hand_size\":0"
                << ",\"opp_holds_china\":" << ((pub.china_held_by != ts::Side::Neutral && !step.holds_china) ? "true" : "false")
                << ",\"lbl_actor_hand\":";
            write_int_array(out, actor_hand_mask);
            out << ",\"lbl_step_quality\":0"
                << ",\"lbl_card_quality\":";
            write_int_array(out, cq);
            out << ",\"lbl_opponent_possible\":";
            write_int_array(out, lbl_opponent_possible);
            out << ",\"game_result\":\"" << game_result_str(traced.result.winner) << "\""
                << ",\"winner_side\":" << winner_side_int(traced.result.winner)
                << ",\"final_vp\":" << traced.result.final_vp
                << ",\"end_turn\":" << traced.result.end_turn
                << ",\"end_reason\":\"" << traced.result.end_reason << "\"}\n";
        }
    }

    return 0;
}
