#include <catch2/catch_test_macros.hpp>

#include "game_state.hpp"

using namespace ts;

TEST_CASE("make_observation hides opponent hand", "[game_state][observation]") {
    auto gs = reset_game(42);
    gs.pub.phasing = Side::USSR;
    gs.hands[to_index(Side::USSR)].reset();
    gs.hands[to_index(Side::US)].reset();
    gs.hands[to_index(Side::USSR)].set(5);
    gs.hands[to_index(Side::US)].set(11);
    gs.ussr_holds_china = false;
    gs.us_holds_china = false;

    const auto obs = make_observation(gs, Side::USSR);
    REQUIRE(obs.own_hand.test(5));
    REQUIRE_FALSE(obs.own_hand.test(11));
    REQUIRE(obs.opp_hand_size == 1);
    REQUIRE(obs.acting_side == Side::USSR);
    REQUIRE_FALSE(obs.holds_china);
}

TEST_CASE("determinize produces valid GameState", "[game_state][observation]") {
    Pcg64Rng rng(99);
    auto gs = reset_game(42);
    gs.pub.phasing = Side::USSR;
    gs.hands[to_index(Side::USSR)].reset();
    gs.hands[to_index(Side::US)].reset();
    gs.hands[to_index(Side::USSR)].set(5);
    gs.hands[to_index(Side::US)].set(11);
    gs.pub.discard.set(13);
    gs.pub.removed.set(14);

    const auto obs = make_observation(gs, Side::USSR);
    const auto det = determinize(obs, rng);

    REQUIRE(det.hands[to_index(Side::USSR)] == obs.own_hand);
    REQUIRE(static_cast<int>(det.hands[to_index(Side::US)].count()) == obs.opp_hand_size);
    REQUIRE_FALSE(det.hands[to_index(Side::US)].test(5));
    REQUIRE_FALSE(det.hands[to_index(Side::US)].test(13));
    REQUIRE_FALSE(det.hands[to_index(Side::US)].test(14));
}
