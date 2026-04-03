// Emit native self-play rows in the JSONL shape used by downstream validation
// and collection experiments.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <string_view>

#include "game_loop.hpp"
#include "human_openings.hpp"
#include "learned_policy.hpp"
#include "policies.hpp"

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

// Returns a sorted list of card IDs present in the set (matches game_state_from_dict format).
std::vector<int> card_ids(const ts::CardSet& cards) {
    std::vector<int> ids;
    for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
        if (cards.test(card_id)) {
            ids.push_back(card_id);
        }
    }
    return ids;
}

// Converts a vector<CardId> (uint8_t / int) to vector<int> for JSON output.
std::vector<int> deck_to_ints(const std::vector<ts::CardId>& deck) {
    std::vector<int> ids;
    ids.reserve(deck.size());
    for (const auto cid : deck) {
        ids.push_back(static_cast<int>(cid));
    }
    return ids;
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
        << " [--epsilon P]"
        << " [--temperature F]"
        << " [--ussr-temperature F] [--us-temperature F]"
        << " [--exploration-rate P]"
        << " [--ussr-policy random|minimal_hybrid] [--us-policy random|minimal_hybrid]"
        << " [--learned-model scripted.pt --learned-side ussr|us]"
        << " [--ussr-model scripted.pt] [--us-model scripted.pt]\n";
}

struct CountedAction {
    ts::ActionEncoding action;
    int visit_count = 0;
};

void record_action_visit(std::vector<CountedAction>& visit_counts, const ts::ActionEncoding& action) {
    const auto found = std::find_if(
        visit_counts.begin(),
        visit_counts.end(),
        [&action](const CountedAction& counted) { return counted.action == action; }
    );
    if (found != visit_counts.end()) {
        found->visit_count += 1;
        return;
    }
    visit_counts.push_back(CountedAction{
        .action = action,
        .visit_count = 1,
    });
}

std::optional<ts::ActionEncoding> sample_action_by_visit_counts(
    const std::vector<CountedAction>& visit_counts,
    float temperature,
    ts::Pcg64Rng& rng
) {
    if (temperature <= 0.0f || visit_counts.empty()) {
        return std::nullopt;
    }

    std::vector<std::pair<size_t, double>> scaled_log_weights;
    scaled_log_weights.reserve(visit_counts.size());
    double max_scaled_log_weight = -std::numeric_limits<double>::infinity();
    for (size_t i = 0; i < visit_counts.size(); ++i) {
        const auto visits = visit_counts[i].visit_count;
        if (visits <= 0) {
            continue;
        }
        const auto scaled_log_weight = std::log(static_cast<double>(visits)) / static_cast<double>(temperature);
        scaled_log_weights.emplace_back(i, scaled_log_weight);
        max_scaled_log_weight = std::max(max_scaled_log_weight, scaled_log_weight);
    }

    if (scaled_log_weights.empty()) {
        return std::nullopt;
    }

    std::vector<std::pair<size_t, double>> weights;
    weights.reserve(scaled_log_weights.size());
    double total_weight = 0.0;
    for (const auto& [action_index, scaled_log_weight] : scaled_log_weights) {
        const auto weight = std::exp(scaled_log_weight - max_scaled_log_weight);
        if (!(weight > 0.0) || !std::isfinite(weight)) {
            continue;
        }
        total_weight += weight;
        weights.emplace_back(action_index, total_weight);
    }

    if (!(total_weight > 0.0)) {
        return std::nullopt;
    }

    const auto draw = rng.random_double() * total_weight;
    for (const auto& [action_index, cumulative_weight] : weights) {
        if (draw < cumulative_weight) {
            return visit_counts[action_index].action;
        }
    }
    return visit_counts[weights.back().first].action;
}

std::optional<ts::ActionEncoding> choose_action_with_temperature(
    const ts::PolicyFn& base_policy,
    bool supports_temperature,
    int move_number,
    float temperature,
    const ts::PublicState& pub,
    const ts::CardSet& hand,
    bool holds_china,
    ts::Pcg64Rng& rng
) {
    if (!supports_temperature || temperature <= 0.0f || move_number > 30) {
        return base_policy(pub, hand, holds_china, rng);
    }

    constexpr int kVisitCountSamples = 16;
    std::vector<CountedAction> visit_counts;
    visit_counts.reserve(kVisitCountSamples);
    for (int sample_index = 0; sample_index < kVisitCountSamples; ++sample_index) {
        ts::Pcg64Rng sample_rng(rng.next_u64());
        const auto action = base_policy(pub, hand, holds_china, sample_rng);
        if (action.has_value()) {
            record_action_visit(visit_counts, *action);
        }
    }

    if (const auto sampled = sample_action_by_visit_counts(visit_counts, temperature, rng); sampled.has_value()) {
        return sampled;
    }
    return base_policy(pub, hand, holds_china, rng);
}

}  // namespace

int main(int argc, char** argv) {
    std::optional<std::string> out_path;
    int game_count = 10;
    std::optional<uint32_t> seed = 12345U;
    float epsilon = 0.0f;
    float temperature = 0.0f;
    float ussr_heuristic_temperature = 0.0f;
    float us_heuristic_temperature = 0.0f;
    bool nash_temperatures = false;
    float exploration_rate = 0.0f;
    int us_bid = 0;
    auto ussr_policy_kind = ts::PolicyKind::MinimalHybrid;
    auto us_policy_kind = ts::PolicyKind::Random;
    std::optional<std::string> learned_model;
    auto learned_side = ts::Side::USSR;
    std::optional<std::string> ussr_model_path;
    std::optional<std::string> us_model_path;

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
        } else if (arg == "--epsilon") {
            epsilon = std::stof(std::string(require_value("--epsilon")));
        } else if (arg == "--temperature") {
            temperature = std::stof(std::string(require_value("--temperature")));
        } else if (arg == "--ussr-temperature") {
            ussr_heuristic_temperature = std::stof(std::string(require_value("--ussr-temperature")));
        } else if (arg == "--us-temperature") {
            us_heuristic_temperature = std::stof(std::string(require_value("--us-temperature")));
        } else if (arg == "--exploration-rate") {
            exploration_rate = std::stof(std::string(require_value("--exploration-rate")));
        } else if (arg == "--ussr-policy") {
            ussr_policy_kind = parse_policy(require_value("--ussr-policy"));
        } else if (arg == "--us-policy") {
            us_policy_kind = parse_policy(require_value("--us-policy"));
        } else if (arg == "--learned-model") {
            learned_model = std::string(require_value("--learned-model"));
        } else if (arg == "--learned-side") {
            const auto side = require_value("--learned-side");
            learned_side = side == "us" ? ts::Side::US : ts::Side::USSR;
        } else if (arg == "--nash-temperatures") {
            nash_temperatures = true;
        } else if (arg == "--bid") {
            us_bid = std::stoi(std::string(require_value("--bid")));
        } else if (arg == "--ussr-model") {
            ussr_model_path = std::string(require_value("--ussr-model"));
        } else if (arg == "--us-model") {
            us_model_path = std::string(require_value("--us-model"));
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
    if (epsilon < 0.0f || epsilon > 1.0f) {
        throw std::invalid_argument("--epsilon must be in [0, 1]");
    }
    if (temperature < 0.0f) {
        throw std::invalid_argument("--temperature must be non-negative");
    }
    if (exploration_rate < 0.0f || exploration_rate > 1.0f) {
        throw std::invalid_argument("--exploration-rate must be in [0, 1]");
    }

    // Resolve per-side model paths: explicit --ussr-model/--us-model take priority
    // over the legacy --learned-model + --learned-side combination.
    if (!ussr_model_path.has_value() && learned_model.has_value() && learned_side == ts::Side::USSR) {
        ussr_model_path = learned_model;
    }
    if (!us_model_path.has_value() && learned_model.has_value() && learned_side == ts::Side::US) {
        us_model_path = learned_model;
    }

    std::optional<ts::TorchScriptPolicy> ussr_learned_policy;
    if (ussr_model_path.has_value()) {
        ussr_learned_policy.emplace(*ussr_model_path);
        ussr_learned_policy->set_exploration_rate(exploration_rate);
    }
    std::optional<ts::TorchScriptPolicy> us_learned_policy;
    if (us_model_path.has_value()) {
        us_learned_policy.emplace(*us_model_path);
        us_learned_policy->set_exploration_rate(exploration_rate);
    }

    // Helper to build a heuristic base policy with a given temperature.
    auto make_base_policy = [&](ts::PolicyKind kind, float temp,
                                std::optional<ts::TorchScriptPolicy>& learned) -> ts::PolicyFn {
        return [kind, temp, &learned](const ts::PublicState& pub, const ts::CardSet& hand,
                                      bool holds_china, ts::Pcg64Rng& rng) {
            if (learned.has_value()) {
                return learned->choose_action(pub, hand, holds_china, rng);
            }
            if (temp > 0.0f && kind == ts::PolicyKind::MinimalHybrid) {
                return ts::choose_minimal_hybrid_sampled(pub, hand, holds_china, temp, rng);
            }
            return ts::choose_action(kind, pub, hand, holds_china, rng);
        };
    };

    const ts::GameLoopConfig loop_config{
        .exploration_rate = epsilon,
        .us_bid_extra = us_bid,
        .use_atomic_setup = true,  // always use atomic setup with kHumanUSOpeningsBid2
    };

    std::ofstream out(*out_path);
    if (!out) {
        throw std::runtime_error("failed to open output file");
    }

    // RNG for Nash temperature sampling (separate from game RNG)
    ts::Pcg64Rng nash_rng(seed.value_or(12345U) + 999999U);

    const auto base_seed = seed.value_or(12345U);
    for (int game_index = 0; game_index < game_count; ++game_index) {
        // Per-game temperature: Nash mixed strategy or fixed.
        float game_ussr_temp = ussr_heuristic_temperature;
        float game_us_temp = us_heuristic_temperature;
        if (nash_temperatures) {
            game_ussr_temp = ts::sample_nash_temperature(
                ts::kNashUSSRTemps.data(), static_cast<int>(ts::kNashUSSRTemps.size()), nash_rng);
            game_us_temp = ts::sample_nash_temperature(
                ts::kNashUSTemps.data(), static_cast<int>(ts::kNashUSTemps.size()), nash_rng);
        }

        const auto ussr_base_policy = make_base_policy(ussr_policy_kind, game_ussr_temp, ussr_learned_policy);
        const auto us_base_policy = make_base_policy(us_policy_kind, game_us_temp, us_learned_policy);

        int move_number = 0;
        const ts::PolicyFn ussr_policy = [&, move_number_ptr = &move_number](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
            return choose_action_with_temperature(
                ussr_base_policy,
                ussr_learned_policy.has_value(),
                ++(*move_number_ptr),
                temperature,
                pub,
                hand,
                holds_china,
                rng
            );
        };
        const ts::PolicyFn us_policy = [&, move_number_ptr = &move_number](const ts::PublicState& pub, const ts::CardSet& hand, bool holds_china, ts::Pcg64Rng& rng) {
            return choose_action_with_temperature(
                us_base_policy,
                us_learned_policy.has_value(),
                ++(*move_number_ptr),
                temperature,
                pub,
                hand,
                holds_china,
                rng
            );
        };
        const auto traced = ts::play_game_traced_fn(
            ussr_policy,
            us_policy,
            base_seed + static_cast<uint32_t>(game_index),
            loop_config
        );
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
            // Full state fields for teacher search (game_state_from_dict compatible)
            out << ",\"warsaw_pact_played\":" << (pub.warsaw_pact_played ? "true" : "false")
                << ",\"marshall_plan_played\":" << (pub.marshall_plan_played ? "true" : "false")
                << ",\"truman_doctrine_played\":" << (pub.truman_doctrine_played ? "true" : "false")
                << ",\"john_paul_ii_played\":" << (pub.john_paul_ii_played ? "true" : "false")
                << ",\"nato_active\":" << (pub.nato_active ? "true" : "false")
                << ",\"de_gaulle_active\":" << (pub.de_gaulle_active ? "true" : "false")
                << ",\"willy_brandt_active\":" << (pub.willy_brandt_active ? "true" : "false")
                << ",\"us_japan_pact_active\":" << (pub.us_japan_pact_active ? "true" : "false")
                << ",\"nuclear_subs_active\":" << (pub.nuclear_subs_active ? "true" : "false")
                << ",\"norad_active\":" << (pub.norad_active ? "true" : "false")
                << ",\"shuttle_diplomacy_active\":" << (pub.shuttle_diplomacy_active ? "true" : "false")
                << ",\"flower_power_active\":" << (pub.flower_power_active ? "true" : "false")
                << ",\"flower_power_cancelled\":" << (pub.flower_power_cancelled ? "true" : "false")
                << ",\"salt_active\":" << (pub.salt_active ? "true" : "false")
                << ",\"opec_cancelled\":" << (pub.opec_cancelled ? "true" : "false")
                << ",\"awacs_active\":" << (pub.awacs_active ? "true" : "false")
                << ",\"north_sea_oil_extra_ar\":" << (pub.north_sea_oil_extra_ar ? "true" : "false")
                << ",\"glasnost_extra_ar\":" << (pub.glasnost_extra_ar ? "true" : "false")
                << ",\"formosan_active\":" << (pub.formosan_active ? "true" : "false")
                << ",\"cuban_missile_crisis_active\":" << (pub.cuban_missile_crisis_active ? "true" : "false")
                << ",\"vietnam_revolts_active\":" << (pub.vietnam_revolts_active ? "true" : "false")
                << ",\"bear_trap_active\":" << (pub.bear_trap_active ? "true" : "false")
                << ",\"quagmire_active\":" << (pub.quagmire_active ? "true" : "false")
                << ",\"iran_hostage_crisis_active\":" << (pub.iran_hostage_crisis_active ? "true" : "false")
                << ",\"handicap_ussr\":" << pub.handicap_ussr
                << ",\"handicap_us\":" << pub.handicap_us
                << ",\"ops_modifier\":[" << pub.ops_modifier[0] << "," << pub.ops_modifier[1] << "]";
            // Hands and deck (for MCTS teacher search)
            const auto ussr_hand_ids = card_ids(step.side == ts::Side::USSR ? step.hand_snapshot : step.opp_hand_snapshot);
            const auto us_hand_ids = card_ids(step.side == ts::Side::US ? step.hand_snapshot : step.opp_hand_snapshot);
            const auto deck_ids = deck_to_ints(step.deck_snapshot);
            out << ",\"ussr_hand\":";
            write_int_array(out, ussr_hand_ids);
            out << ",\"us_hand\":";
            write_int_array(out, us_hand_ids);
            out << ",\"deck\":";
            write_int_array(out, deck_ids);
            out << ",\"ussr_holds_china\":" << (step.ussr_holds_china_snapshot ? "true" : "false")
                << ",\"us_holds_china\":" << (step.us_holds_china_snapshot ? "true" : "false")
                << ",\"state_dict_complete\":true"
                << ",\"game_result\":\"" << game_result_str(traced.result.winner) << "\""
                << ",\"winner_side\":" << winner_side_int(traced.result.winner)
                << ",\"final_vp\":" << traced.result.final_vp
                << ",\"end_turn\":" << traced.result.end_turn
                << ",\"end_reason\":\"" << traced.result.end_reason << "\"}\n";
        }
    }

    return 0;
}
