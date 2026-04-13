#include <catch2/catch_test_macros.hpp>

#include "public_state.hpp"
#include "game_data.hpp"
#include "hand_knowledge.hpp"
#include "legal_actions.hpp"
#include "rng.hpp"
#include "step.hpp"
#include "types.hpp"

using namespace ts;

// ---------------------------------------------------------------------------
// PublicState default-construction sanity checks.
//
// These tests verify that a default-constructed PublicState has the expected
// initial values as documented in public_state.hpp.  They are intentionally
// narrow: they do not test game logic, only that the struct initialises
// correctly and that constants in types.hpp are sane.
// ---------------------------------------------------------------------------

TEST_CASE("PublicState default construction has zero influence", "[public_state]") {
    PublicState s;
    for (int p = 0; p < 2; ++p) {
        for (int c = 0; c < MAX_COUNTRIES; ++c) {
            REQUIRE(s.influence[p][c] == 0);
        }
    }
}

TEST_CASE("PublicState default construction has zero milops and space", "[public_state]") {
    PublicState s;
    REQUIRE(s.milops[0] == 0);
    REQUIRE(s.milops[1] == 0);
    REQUIRE(s.space[0] == 0);
    REQUIRE(s.space[1] == 0);
}

TEST_CASE("PublicState default construction has correct scalar defaults", "[public_state]") {
    PublicState s;
    REQUIRE(s.vp     == 0);
    REQUIRE(s.defcon == 5);
    REQUIRE(s.turn   == 0);
    REQUIRE(s.ar     == 0);
    REQUIRE(s.phasing       == Side::USSR);
    REQUIRE(s.china_held_by == Side::USSR);
    REQUIRE(s.china_playable == true);
}

TEST_CASE("PublicState default construction has empty card sets", "[public_state]") {
    PublicState s;
    REQUIRE(s.discard.none());
    REQUIRE(s.removed.none());
}

TEST_CASE("PublicState default construction has zero hash", "[public_state]") {
    PublicState s;
    REQUIRE(s.state_hash == 0);
}

// ---------------------------------------------------------------------------
// HandKnowledge default-construction sanity checks.
// ---------------------------------------------------------------------------

TEST_CASE("HandKnowledge default construction has empty bitsets", "[hand_knowledge]") {
    HandKnowledge hk;
    REQUIRE(hk.known_in_hand.none());
    REQUIRE(hk.known_not_in_hand.none());
    REQUIRE(hk.possible_hidden.none());
}

TEST_CASE("HandKnowledge default construction has zero hand size", "[hand_knowledge]") {
    HandKnowledge hk;
    REQUIRE(hk.hand_size == 0);
    REQUIRE(hk.holds_china == false);
    REQUIRE(hk.observer == Side::Neutral);
}

// ---------------------------------------------------------------------------
// Constants sanity checks.
// ---------------------------------------------------------------------------

TEST_CASE("Hand size constants are correct per rules", "[types]") {
    // Competitive / ITS rules: 8 cards turns 1-3, 9 cards turns 4-10.
    REQUIRE(HAND_SIZE_EARLY == 8);
    REQUIRE(HAND_SIZE_LATE  == 9);
}

TEST_CASE("CHINA_CARD constant is a valid CardId value", "[types]") {
    // The exact value is a placeholder but must fit in uint8_t and be non-zero.
    REQUIRE(CHINA_CARD > 0);
    REQUIRE(CHINA_CARD < MAX_CARDS);
}

TEST_CASE("MAX_CARDS and MAX_COUNTRIES are large enough", "[types]") {
    // TS has 110 cards and ~68 countries; our arrays must accommodate them.
    REQUIRE(MAX_CARDS     >= 110);
    REQUIRE(MAX_COUNTRIES >= 68);
}

TEST_CASE("HLSTW event never sets DEFCON to 1", "[step]") {
    PublicState pub;
    pub.defcon = 5;

    const ActionEncoding action{
        .card_id = 49,
        .mode = ActionMode::Event,
        .targets = {},
    };

    for (uint64_t seed = 0; seed < 64; ++seed) {
        Pcg64Rng rng(seed);
        const auto [next, force_game_over, forced_winner] = apply_action(pub, action, Side::USSR, rng);

        REQUIRE_FALSE(force_game_over);
        REQUIRE_FALSE(forced_winner.has_value());
        REQUIRE(next.defcon >= 2);
        REQUIRE(next.defcon <= 5);
        REQUIRE(next.milops[to_index(Side::USSR)] == 5);
    }
}

TEST_CASE("Vietnam Revolts does not add a global ops modifier", "[step][legal_actions]") {
    PublicState pub;
    Pcg64Rng rng(0);

    const ActionEncoding event{
        .card_id = 9,
        .mode = ActionMode::Event,
        .targets = {},
    };

    const auto [next, over, winner] = apply_action(pub, event, Side::USSR, rng);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.vietnam_revolts_active);
    REQUIRE(next.ops_modifier[to_index(Side::USSR)] == 0);
    REQUIRE(effective_ops(7, next, Side::USSR) == card_spec(7).ops);
}

TEST_CASE("Vietnam Revolts adds one coup op only in Southeast Asia", "[step]") {
    constexpr CountryId kVietnamId = 80;

    PublicState base;
    base.set_influence(Side::US, kVietnamId, 5);

    PublicState bonus = base;
    bonus.vietnam_revolts_active = true;

    const ActionEncoding coup{
        .card_id = 7,
        .mode = ActionMode::Coup,
        .targets = {kVietnamId},
    };

    Pcg64Rng base_rng(11);
    Pcg64Rng bonus_rng(11);
    const auto [without_bonus, _, __] = apply_action(base, coup, Side::USSR, base_rng);
    const auto [with_bonus, ___, ____] = apply_action(bonus, coup, Side::USSR, bonus_rng);

    REQUIRE(with_bonus.influence_of(Side::US, kVietnamId) == without_bonus.influence_of(Side::US, kVietnamId) - 1);
    REQUIRE(with_bonus.milops[to_index(Side::USSR)] == without_bonus.milops[to_index(Side::USSR)] + 1);
}

TEST_CASE("Vietnam Revolts enumerates SEA-only influence actions with one extra op", "[legal_actions]") {
    constexpr CountryId kVietnamId = 80;

    PublicState pub;
    pub.vietnam_revolts_active = true;
    pub.set_influence(Side::USSR, kVietnamId, 1);

    CardSet hand;
    hand.set(7);

    const auto actions = enumerate_actions(hand, pub, Side::USSR, false);
    const auto found = std::any_of(actions.begin(), actions.end(), [](const ActionEncoding& action) {
        return action.card_id == 7 &&
            action.mode == ActionMode::Influence &&
            action.targets.size() == static_cast<size_t>(card_spec(7).ops + 1) &&
            std::all_of(action.targets.begin(), action.targets.end(), [](CountryId cid) {
                return country_spec(cid).region == Region::SoutheastAsia;
            });
    });

    REQUIRE(found);
}
