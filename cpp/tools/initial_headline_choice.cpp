#include <cstdint>
#include <iostream>
#include <optional>
#include <string>
#include <vector>

#include "game_data.hpp"
#include "game_state.hpp"
#include "policies.hpp"
#include "rng.hpp"

namespace {

std::vector<ts::CardId> build_early_deck() {
    std::vector<ts::CardId> deck;
    for (const auto card_id : ts::all_card_ids()) {
        if (card_id == ts::kChinaCardId) {
            continue;
        }
        const auto& spec = ts::card_spec(card_id);
        if (!spec.is_scoring && spec.era == ts::Era::Early) {
            deck.push_back(card_id);
        }
    }
    return deck;
}

ts::GameState reset_game_with_pcg64_words(
    std::array<uint64_t, 4> words,
    std::optional<std::string> numpy_generator_so
) {
    auto rng = ts::Pcg64Rng::from_seed_sequence_words(words);
    ts::GameState gs;
    gs.pub.turn = 1;
    gs.pub.ar = 0;
    gs.pub.defcon = 5;
    gs.pub.vp = 0;
    gs.pub.milops = {0, 0};
    gs.pub.space = {0, 0};
    gs.pub.china_held_by = ts::Side::USSR;
    gs.pub.china_playable = true;
    for (const auto cid : ts::all_country_ids()) {
        const auto& spec = ts::country_spec(cid);
        gs.pub.set_influence(ts::Side::US, cid, spec.us_start);
        gs.pub.set_influence(ts::Side::USSR, cid, spec.ussr_start);
    }
    gs.deck = build_early_deck();
    (void)numpy_generator_so;
    ts::shuffle_with_numpy_rng(gs.deck, rng);
    const auto hand_size = ts::hand_size_for_turn(1);
    for (const auto side : {ts::Side::USSR, ts::Side::US}) {
        for (int i = 0; i < hand_size && !gs.deck.empty(); ++i) {
            const auto card_id = gs.deck.front();
            gs.deck.erase(gs.deck.begin());
            gs.hands[ts::to_index(side)].set(card_id);
        }
    }
    gs.phase = ts::GamePhase::Headline;
    return gs;
}

ts::PolicyKind parse_policy(const std::string& name) {
    if (name == "random") {
        return ts::PolicyKind::Random;
    }
    if (name == "minimal" || name == "minimal_hybrid") {
        return ts::PolicyKind::MinimalHybrid;
    }
    throw std::invalid_argument("unsupported policy");
}

}  // namespace

int main(int argc, char** argv) {
    std::array<uint64_t, 4> words{0, 0, 0, 0};
    std::string ussr_policy_name = "minimal_hybrid";
    std::string us_policy_name = "minimal_hybrid";
    std::optional<std::string> numpy_generator_so;
    std::optional<std::string> python_lib;
    bool dump_ranked = false;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        if (arg == "--word0" && i + 1 < argc) {
            words[0] = std::stoull(argv[++i]);
        } else if (arg == "--word1" && i + 1 < argc) {
            words[1] = std::stoull(argv[++i]);
        } else if (arg == "--word2" && i + 1 < argc) {
            words[2] = std::stoull(argv[++i]);
        } else if (arg == "--word3" && i + 1 < argc) {
            words[3] = std::stoull(argv[++i]);
        } else if (arg == "--ussr-policy" && i + 1 < argc) {
            ussr_policy_name = argv[++i];
        } else if (arg == "--us-policy" && i + 1 < argc) {
            us_policy_name = argv[++i];
        } else if (arg == "--numpy-generator-so" && i + 1 < argc) {
            numpy_generator_so = argv[++i];
        } else if (arg == "--python-lib" && i + 1 < argc) {
            python_lib = argv[++i];
        } else if (arg == "--dump-ranked") {
            dump_ranked = true;
        }
    }

    (void)python_lib;

    auto gs = reset_game_with_pcg64_words(words, numpy_generator_so);
    std::mt19937 fallback_rng(0U);
    auto pub = gs.pub;
    pub.phasing = ts::Side::USSR;
    auto ussr_action = ts::choose_action(
        parse_policy(ussr_policy_name),
        pub,
        gs.hands[ts::to_index(ts::Side::USSR)],
        false,
        fallback_rng
    );
    pub.phasing = ts::Side::US;
    auto us_action = ts::choose_action(
        parse_policy(us_policy_name),
        pub,
        gs.hands[ts::to_index(ts::Side::US)],
        false,
        fallback_rng
    );

    std::vector<ts::ScoredAction> ussr_ranked;
    std::vector<ts::ScoredAction> us_ranked;
    if (dump_ranked) {
        pub.phasing = ts::Side::USSR;
        ussr_ranked = ts::rank_minimal_hybrid_actions(pub, gs.hands[ts::to_index(ts::Side::USSR)], false);
        pub.phasing = ts::Side::US;
        us_ranked = ts::rank_minimal_hybrid_actions(pub, gs.hands[ts::to_index(ts::Side::US)], false);
    }

    std::cout << "{";
    std::cout << "\"ussr_card\":" << (ussr_action.has_value() ? static_cast<int>(ussr_action->card_id) : -1) << ",";
    std::cout << "\"ussr_mode\":" << (ussr_action.has_value() ? static_cast<int>(ussr_action->mode) : -1) << ",";
    std::cout << "\"us_card\":" << (us_action.has_value() ? static_cast<int>(us_action->card_id) : -1) << ",";
    std::cout << "\"us_mode\":" << (us_action.has_value() ? static_cast<int>(us_action->mode) : -1);
    if (dump_ranked) {
        auto dump = [](const char* key, const std::vector<ts::ScoredAction>& ranked) {
            std::cout << ",\"" << key << "\":[";
            for (size_t i = 0; i < ranked.size(); ++i) {
                if (i > 0) {
                    std::cout << ",";
                }
                const auto& item = ranked[i];
                std::cout << "{";
                std::cout << "\"card\":" << static_cast<int>(item.action.card_id) << ",";
                std::cout << "\"mode\":" << static_cast<int>(item.action.mode) << ",";
                std::cout << "\"score\":" << item.score;
                std::cout << "}";
            }
            std::cout << "]";
        };
        dump("ussr_ranked", ussr_ranked);
        dump("us_ranked", us_ranked);
    }
    std::cout << "}\n";
    return 0;
}
