// Dump the native opening setup for a given seed so it can be compared against
// Python setup state.

#include <cstdint>
#include <iostream>
#include <optional>
#include <string>

#include "game_data.hpp"
#include "game_state.hpp"
#include "rng.hpp"

namespace {

// Rebuild the early-war draw deck in spec order before any shuffle is applied.
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

ts::GameState reset_game_with_pcg64_words(std::array<uint64_t, 4> words, std::optional<std::string> numpy_generator_so) {
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
    gs.current_side = ts::Side::USSR;
    gs.ar_index = 1;
    return gs;
}

void print_cards(const ts::CardSet& hand) {
    bool first = true;
    std::cout << "[";
    for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
        if (!hand.test(card_id)) {
            continue;
        }
        if (!first) {
            std::cout << ",";
        }
        first = false;
        std::cout << card_id;
    }
    std::cout << "]";
}

void print_deck(const std::vector<ts::CardId>& deck, size_t limit) {
    std::cout << "[";
    for (size_t i = 0; i < deck.size() && i < limit; ++i) {
        if (i > 0) {
            std::cout << ",";
        }
        std::cout << static_cast<int>(deck[i]);
    }
    std::cout << "]";
}

}  // namespace

int main(int argc, char** argv) {
    std::optional<uint32_t> seed = 12345U;
    std::optional<std::array<uint64_t, 4>> words;
    std::optional<std::string> numpy_generator_so;
    std::optional<std::string> python_lib;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        if (arg == "--seed" && i + 1 < argc) {
            seed = static_cast<uint32_t>(std::stoul(argv[++i]));
        } else if (arg == "--word0" && i + 1 < argc) {
            if (!words.has_value()) {
                words = std::array<uint64_t, 4>{0, 0, 0, 0};
            }
            (*words)[0] = std::stoull(argv[++i]);
        } else if (arg == "--word1" && i + 1 < argc) {
            if (!words.has_value()) {
                words = std::array<uint64_t, 4>{0, 0, 0, 0};
            }
            (*words)[1] = std::stoull(argv[++i]);
        } else if (arg == "--word2" && i + 1 < argc) {
            if (!words.has_value()) {
                words = std::array<uint64_t, 4>{0, 0, 0, 0};
            }
            (*words)[2] = std::stoull(argv[++i]);
        } else if (arg == "--word3" && i + 1 < argc) {
            if (!words.has_value()) {
                words = std::array<uint64_t, 4>{0, 0, 0, 0};
            }
            (*words)[3] = std::stoull(argv[++i]);
        } else if (arg == "--numpy-generator-so" && i + 1 < argc) {
            numpy_generator_so = argv[++i];
        } else if (arg == "--python-lib" && i + 1 < argc) {
            python_lib = argv[++i];
        }
    }

    (void)python_lib;

    const auto gs = words.has_value() ? reset_game_with_pcg64_words(*words, numpy_generator_so) : ts::reset_game(seed);
    std::cout << "{";
    std::cout << "\"turn\":" << gs.pub.turn << ",";
    std::cout << "\"ussr_hand\":";
    print_cards(gs.hands[ts::to_index(ts::Side::USSR)]);
    std::cout << ",";
    std::cout << "\"us_hand\":";
    print_cards(gs.hands[ts::to_index(ts::Side::US)]);
    std::cout << ",";
    std::cout << "\"deck_prefix\":";
    print_deck(gs.deck, 16);
    std::cout << ",";
    std::cout << "\"deck_size\":" << gs.deck.size();
    std::cout << "}\n";
    return 0;
}
