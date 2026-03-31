#include "game_state.hpp"

#include <algorithm>

#include "game_data.hpp"

namespace ts {
namespace {

std::vector<CardId> build_era_deck(Era era_max, const CardSet& removed) {
    std::vector<CardId> out;
    for (const auto card_id : all_card_ids()) {
        if (card_id == kChinaCardId) {
            continue;
        }
        const auto& spec = card_spec(card_id);
        if (spec.is_scoring || static_cast<int>(spec.era) > static_cast<int>(era_max)) {
            continue;
        }
        if (removed.test(card_id)) {
            continue;
        }
        out.push_back(card_id);
    }
    return out;
}

void shuffle_vector(std::vector<CardId>& deck, std::mt19937& rng) {
    std::shuffle(deck.begin(), deck.end(), rng);
}

void reshuffle(GameState& gs, std::mt19937& rng) {
    gs.deck.clear();
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (gs.pub.discard.test(card_id)) {
            gs.deck.push_back(static_cast<CardId>(card_id));
        }
    }
    gs.pub.discard.reset();
    shuffle_vector(gs.deck, rng);
}

}  // namespace

int ars_for_turn(int turn) {
    return turn <= 3 ? 6 : 7;
}

int hand_size_for_turn(int turn) {
    return turn <= 3 ? kHandSizeEarly : kHandSizeLate;
}

GameState reset_game(std::optional<uint32_t> seed) {
    std::mt19937 rng(seed.value_or(std::random_device{}()));
    GameState gs;
    gs.pub.turn = 1;
    gs.pub.ar = 0;
    gs.pub.defcon = 5;
    gs.pub.vp = 0;
    gs.pub.milops = {0, 0};
    gs.pub.space = {0, 0};
    gs.pub.china_held_by = Side::USSR;
    gs.pub.china_playable = true;

    for (const auto cid : all_country_ids()) {
        const auto& spec = country_spec(cid);
        gs.pub.set_influence(Side::US, cid, spec.us_start);
        gs.pub.set_influence(Side::USSR, cid, spec.ussr_start);
    }

    gs.deck = build_era_deck(Era::Early, gs.pub.removed);
    shuffle_vector(gs.deck, rng);

    const auto hand_size = hand_size_for_turn(1);
    for (const auto side : {Side::USSR, Side::US}) {
        for (int i = 0; i < hand_size && !gs.deck.empty(); ++i) {
            // Python reset() deals the initial turn-1 hands from the front of
            // the shuffled deck before switching to pop-from-end draws later.
            const auto card_id = gs.deck.front();
            gs.deck.erase(gs.deck.begin());
            gs.hands[to_index(side)].set(card_id);
        }
    }

    gs.phase = GamePhase::Headline;
    gs.current_side = Side::USSR;
    gs.ar_index = 1;
    return gs;
}

GameState clone_game_state(const GameState& gs) {
    return gs;
}

void deal_cards(GameState& gs, Side side, std::mt19937& rng) {
    const auto target = hand_size_for_turn(gs.pub.turn);
    auto current = static_cast<int>(gs.hands[to_index(side)].count());
    while (current < target) {
        if (gs.deck.empty()) {
            reshuffle(gs, rng);
            if (gs.deck.empty()) {
                break;
            }
        }
        const auto card_id = gs.deck.back();
        gs.deck.pop_back();
        gs.hands[to_index(side)].set(card_id);
        ++current;
    }
}

void advance_to_mid_war(GameState& gs, std::mt19937& rng) {
    auto deck = build_era_deck(Era::Mid, gs.pub.removed);
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (gs.pub.discard.test(card_id)) {
            deck.push_back(static_cast<CardId>(card_id));
        }
    }
    gs.pub.discard.reset();
    gs.deck = std::move(deck);
    shuffle_vector(gs.deck, rng);
}

void advance_to_late_war(GameState& gs, std::mt19937& rng) {
    auto deck = build_era_deck(Era::Late, gs.pub.removed);
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (gs.pub.discard.test(card_id)) {
            deck.push_back(static_cast<CardId>(card_id));
        }
    }
    gs.pub.discard.reset();
    gs.deck = std::move(deck);
    shuffle_vector(gs.deck, rng);
}

std::vector<CardId> hand_to_vector(const CardSet& hand) {
    std::vector<CardId> cards;
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (hand.test(card_id)) {
            cards.push_back(static_cast<CardId>(card_id));
        }
    }
    return cards;
}

int hand_count(const CardSet& hand) {
    return static_cast<int>(hand.count());
}

}  // namespace ts
