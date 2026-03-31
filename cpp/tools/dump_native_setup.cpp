#include <cstdint>
#include <optional>
#include <dlfcn.h>
#include <iostream>
#include <string>

#include "game_data.hpp"
#include "game_state.hpp"
#include "rng.hpp"

namespace {

struct NumpyBitgen {
    void* state;
    uint64_t (*next_uint64)(void* st);
    uint32_t (*next_uint32)(void* st);
    double (*next_double)(void* st);
    uint64_t (*next_raw)(void* st);
};

using RandomIntervalFn = uint64_t (*)(NumpyBitgen*, uint64_t);

uint64_t bitgen_next_uint64(void* st) {
    return static_cast<ts::Pcg64Rng*>(st)->next_u64();
}

uint32_t bitgen_next_uint32(void* st) {
    return static_cast<ts::Pcg64Rng*>(st)->next_u32();
}

double bitgen_next_double(void* st) {
    constexpr double scale = 1.0 / static_cast<double>(uint64_t{1} << 53);
    return static_cast<double>(static_cast<ts::Pcg64Rng*>(st)->next_u64() >> 11) * scale;
}

uint64_t bitgen_next_raw(void* st) {
    return static_cast<ts::Pcg64Rng*>(st)->next_u64();
}

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

void shuffle_with_numpy_interval(std::vector<ts::CardId>& deck, ts::Pcg64Rng& rng, RandomIntervalFn random_interval) {
    NumpyBitgen bitgen{
        .state = &rng,
        .next_uint64 = bitgen_next_uint64,
        .next_uint32 = bitgen_next_uint32,
        .next_double = bitgen_next_double,
        .next_raw = bitgen_next_raw,
    };
    for (size_t i = deck.size(); i > 1; --i) {
        const auto j = static_cast<size_t>(random_interval(&bitgen, i - 1));
        if (j != i - 1) {
            std::swap(deck[i - 1], deck[j]);
        }
    }
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
    if (numpy_generator_so.has_value()) {
        void* handle = dlopen(numpy_generator_so->c_str(), RTLD_NOW | RTLD_GLOBAL);
        if (handle == nullptr) {
            throw std::runtime_error(std::string("failed to dlopen numpy generator: ") + dlerror());
        }
        auto* random_interval = reinterpret_cast<RandomIntervalFn>(dlsym(handle, "random_interval"));
        if (random_interval == nullptr) {
            dlclose(handle);
            throw std::runtime_error("failed to resolve random_interval");
        }
        shuffle_with_numpy_interval(gs.deck, rng, random_interval);
        dlclose(handle);
    } else {
        ts::shuffle_with_rng(gs.deck, rng);
    }

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

    if (python_lib.has_value()) {
        void* py = dlopen(python_lib->c_str(), RTLD_NOW | RTLD_GLOBAL);
        if (py == nullptr) {
            throw std::runtime_error(std::string("failed to dlopen libpython: ") + dlerror());
        }
    }

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
