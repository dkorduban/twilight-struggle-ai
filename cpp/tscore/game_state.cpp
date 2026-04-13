// Native mutable game-state construction, dealing, reshuffling, and era-deck
// transitions.

#include "game_state.hpp"

#include "game_data.hpp"

namespace ts {
namespace {

// Build the draw deck for all cards up to an era (including scoring cards),
// excluding the China Card and anything already removed from the live game.
std::vector<CardId> build_era_deck(Era era_max, const CardSet& removed) {
    // Promo cards (109-111): IDs exist for log-parsing completeness but their
    // event effects are not implemented. Permanently excluded from all decks.
    static constexpr std::array<int, 3> kPromoCardIds = {109, 110, 111};
    std::vector<CardId> out;
    for (const auto card_id : all_card_ids()) {
        if (card_id == kChinaCardId) {
            continue;
        }
        const int id = static_cast<int>(card_id);
        if (std::find(kPromoCardIds.begin(), kPromoCardIds.end(), id) != kPromoCardIds.end()) {
            continue;
        }
        const auto& spec = card_spec(card_id);
        if (static_cast<int>(spec.era) > static_cast<int>(era_max)) {
            continue;
        }
        if (removed.test(card_id)) {
            continue;
        }
        out.push_back(card_id);
    }
    return out;
}

void shuffle_deck(InlineDeck& deck, Pcg64Rng& rng) {
    shuffle_with_numpy_rng(std::span<CardId>(deck.begin(), deck.end()), rng);
}

// Reshuffle exactly from the public discard pile back into the hidden deck.
void reshuffle(GameState& gs, Pcg64Rng& rng) {
    gs.deck.clear();
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (gs.pub.discard.test(card_id)) {
            gs.deck.push_back(static_cast<CardId>(card_id));
        }
    }
    gs.pub.discard.reset();
    shuffle_deck(gs.deck, rng);
}

GameState reset_game_impl(std::span<const CardId> shuffled_deck) {
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

    gs.deck.assign(shuffled_deck.begin(), shuffled_deck.end());
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

    gs.phase = GamePhase::Setup;
    gs.current_side = Side::USSR;
    gs.ar_index = 1;
    gs.setup_influence_remaining = {kUSSRSetupInfluence, kUSSetupInfluence};
    return gs;
}

}  // namespace

int ars_for_turn(int turn) {
    return turn <= 3 ? 6 : 7;
}

int hand_size_for_turn(int turn) {
    return turn <= 3 ? kHandSizeEarly : kHandSizeLate;
}

GameState reset_game(std::optional<uint32_t> seed) {
    Pcg64Rng rng(seed.value_or(std::random_device{}()));
    return reset_game_from_rng(rng);
}

GameState reset_game_from_rng(Pcg64Rng& rng) {
    auto deck = build_era_deck(Era::Early, CardSet{});
    shuffle_with_numpy_rng(deck, rng);
    return reset_game_impl(deck);
}

GameState reset_game_from_seed_words(std::array<uint64_t, 4> words) {
    auto rng = Pcg64Rng::from_seed_sequence_words(words);
    return reset_game_from_rng(rng);
}

GameState clone_game_state(const GameState& gs) {
    return gs;
}

void deal_cards(GameState& gs, Side side, Pcg64Rng& rng) {
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

// Build set of all cards accounted for (in hands, deck, discard, or removed).
// New era cards that overlap with these must NOT be added again.
CardSet all_accounted_cards(const GameState& gs) {
    CardSet accounted;
    for (const auto& hand : gs.hands) {
        accounted |= hand;
    }
    for (int i = 0; i < gs.deck.size(); ++i) {
        accounted.set(gs.deck.begin()[i]);
    }
    accounted |= gs.pub.discard;
    accounted |= gs.pub.removed;
    return accounted;
}

// TS Rules §4.4: "add the Mid War or Late War cards to the existing deck
// and reshuffle. The ignored discards remain in the discard pile for now,
// but will be reshuffled into the deck in the next reshuffle."
void advance_to_mid_war(GameState& gs, Pcg64Rng& rng) {
    const auto accounted = all_accounted_cards(gs);
    // Only add genuinely new mid-war era cards (not already in deck/hands/discard/removed).
    auto new_cards = build_era_deck(Era::Mid, gs.pub.removed);
    for (const auto c : new_cards) {
        if (!accounted.test(c)) {
            gs.deck.push_back(c);
        }
    }
    // Do NOT touch the discard pile (§4.4).
    shuffle_deck(gs.deck, rng);
}

void advance_to_late_war(GameState& gs, Pcg64Rng& rng) {
    const auto accounted = all_accounted_cards(gs);
    auto new_cards = build_era_deck(Era::Late, gs.pub.removed);
    for (const auto c : new_cards) {
        if (!accounted.test(c)) {
            gs.deck.push_back(c);
        }
    }
    shuffle_deck(gs.deck, rng);
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

Observation make_observation(const GameState& gs, Side side) {
    Observation obs;
    obs.pub = gs.pub;
    obs.own_hand = gs.hands[to_index(side)];
    obs.side = side;
    obs.opponent_hand_support.reset();
    for (int raw = 1; raw <= kMaxCardId; ++raw) {
        const auto card_id = static_cast<CardId>(raw);
        if (!obs.own_hand.test(card_id) &&
            !gs.pub.discard.test(card_id) &&
            !gs.pub.removed.test(card_id)) {
            obs.opponent_hand_support.set(card_id);
        }
    }
    return obs;
}

}  // namespace ts
