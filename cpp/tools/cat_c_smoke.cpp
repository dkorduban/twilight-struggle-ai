// Targeted smoke coverage for Cat C hand/deck-manipulation events.

#include <cstdlib>
#include <iostream>
#include <optional>
#include <random>
#include <string>

#include "game_loop.hpp"

namespace {

using ts::ActionEncoding;
using ts::ActionMode;
using ts::GameState;
using ts::PublicState;
using ts::Side;

[[noreturn]] void fail(const std::string& message) {
    std::cerr << "cat c smoke failed: " << message << '\n';
    std::exit(1);
}

void require(bool condition, const std::string& message) {
    if (!condition) {
        fail(message);
    }
}

std::tuple<PublicState, bool, std::optional<Side>> apply_live(GameState& gs, ts::CardId card_id, ActionMode mode, Side side) {
    ts::Pcg64Rng rng(123U);
    return ts::apply_action_live(
        gs,
        ActionEncoding{
            .card_id = card_id,
            .mode = mode,
            .targets = mode == ActionMode::Influence ? std::vector<ts::CountryId>{21} : std::vector<ts::CountryId>{},
        },
        side,
        rng
    );
}

void test_blockade() {
    GameState gs;
    gs.pub.set_influence(Side::US, 18, 4);
    auto [pub, over, winner] = apply_live(gs, 10, ActionMode::Event, Side::USSR);
    (void)over;
    (void)winner;
    require(pub.influence_of(Side::US, 18) == 0, "Blockade should remove all US influence from West Germany when no 3+ ops discard exists");
}

void test_salt_draw() {
    GameState gs;
    gs.pub.defcon = 3;
    gs.pub.discard.set(7);
    auto [pub, over, winner] = apply_live(gs, 46, ActionMode::Event, Side::USSR);
    (void)over;
    (void)winner;
    require(pub.defcon == 4, "SALT Negotiations should raise DEFCON by 1");
    require(pub.salt_active, "SALT Negotiations should set salt_active");
    require(!pub.discard.test(7), "SALT Negotiations should remove the chosen discard card from the discard pile");
    require(gs.hands[ts::to_index(Side::USSR)].test(7), "SALT Negotiations should move one discard card into the phasing hand");
}

void test_ladc_and_terrorism() {
    GameState gs;
    gs.hands[ts::to_index(Side::US)].set(4);
    gs.hands[ts::to_index(Side::US)].set(25);
    auto [pub, over, winner] = apply_live(gs, 98, ActionMode::Event, Side::USSR);
    (void)over;
    (void)winner;
    require(!gs.hands[ts::to_index(Side::US)].test(4) && !gs.hands[ts::to_index(Side::US)].test(25), "Debt Crisis should discard a valid US pair");
    require(pub.vp == 0, "Debt Crisis should not award USSR VP when US can pay");

    gs = GameState{};
    gs.pub.iran_hostage_crisis_active = true;
    gs.hands[ts::to_index(Side::US)].set(7);
    gs.hands[ts::to_index(Side::US)].set(8);
    gs.hands[ts::to_index(Side::US)].set(9);
    ts::Pcg64Rng rng(456U);
    auto result = ts::apply_action_live(
        gs,
        ActionEncoding{.card_id = 95, .mode = ActionMode::Event, .targets = {}},
        Side::USSR,
        rng
    );
    (void)result;
    require(ts::hand_count(gs.hands[ts::to_index(Side::US)]) == 1, "Terrorism should discard two US cards under Iranian Hostage Crisis");
}

void test_defectors_and_ops_trigger() {
    GameState gs;
    auto [pub, over, winner] = apply_live(gs, 108, ActionMode::Event, Side::USSR);
    (void)over;
    (void)winner;
    require(pub.vp == -1, "Defectors fired by USSR in action round should award 1 VP to US");

    gs = GameState{};
    gs.hands[ts::to_index(Side::USSR)].set(4);
    gs.pub.defcon = 3;
    ts::Pcg64Rng rng(789U);
    auto live = ts::apply_action_live(
        gs,
        ActionEncoding{.card_id = 4, .mode = ActionMode::Influence, .targets = {21}},
        Side::USSR,
        rng
    );
    (void)live;
    require(gs.pub.vp == -2, "Playing an opponent card for ops should fire its event first");
    require(gs.pub.defcon == 2, "Offside Duck and Cover should lower DEFCON before the ops effect resolves");
    require(gs.pub.influence_of(Side::USSR, 21) == 1, "Opponent-card ops play should still apply the ops effect");
}

}  // namespace

int main() {
    test_blockade();
    test_salt_draw();
    test_ladc_and_terrorism();
    test_defectors_and_ops_trigger();
    std::cout << "cat c smoke ok\n";
    return 0;
}
