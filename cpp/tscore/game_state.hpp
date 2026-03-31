#pragma once

#include <array>
#include <bitset>
#include <random>
#include <vector>

#include "public_state.hpp"
#include "rng.hpp"

namespace ts {

struct GameState {
    PublicState pub;
    std::array<CardSet, 2> hands;
    std::vector<CardId> deck;
    bool ussr_holds_china = true;
    bool us_holds_china = false;
    GamePhase phase = GamePhase::Setup;
    Side current_side = Side::USSR;
    int ar_index = 1;
    std::array<int, 2> ars_taken = {0, 0};
    std::array<CardId, 2> headline_card = {0, 0};
    bool game_over = false;
    std::optional<Side> winner;
};

int ars_for_turn(int turn);
int hand_size_for_turn(int turn);
GameState reset_game(std::optional<uint32_t> seed = std::nullopt);
GameState reset_game_from_rng(Pcg64Rng& rng);
GameState reset_game_from_seed_words(std::array<uint64_t, 4> words);
GameState clone_game_state(const GameState& gs);
void deal_cards(GameState& gs, Side side, Pcg64Rng& rng);
void advance_to_mid_war(GameState& gs, Pcg64Rng& rng);
void advance_to_late_war(GameState& gs, Pcg64Rng& rng);
std::vector<CardId> hand_to_vector(const CardSet& hand);
int hand_count(const CardSet& hand);

}  // namespace ts
