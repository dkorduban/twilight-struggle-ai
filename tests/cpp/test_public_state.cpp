#include <catch2/catch_test_macros.hpp>

#include "public_state.hpp"
#include "hand_knowledge.hpp"
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
