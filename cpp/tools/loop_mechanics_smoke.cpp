// Smoke coverage for higher-level loop mechanics such as headline ordering,
// extra AR handling, NORAD, and trap resolution.

#include <cstdlib>
#include <iostream>
#include <optional>
#include <random>
#include <string>
#include <vector>

#include "game_loop.hpp"

namespace {

using ts::ActionEncoding;
using ts::ActionMode;
using ts::GameResult;
using ts::GameState;
using ts::PolicyFn;
using ts::PublicState;
using ts::Side;
using ts::StepTrace;

[[noreturn]] void fail(const std::string& message) {
    std::cerr << "loop mechanics smoke failed: " << message << '\n';
    std::exit(1);
}

void require(bool condition, const std::string& message) {
    if (!condition) {
        fail(message);
    }
}

int total_us_influence(const PublicState& pub) {
    int total = 0;
    for (ts::CountryId cid = 0; cid < ts::kCountrySlots; ++cid) {
        total += pub.influence_of(Side::US, cid);
    }
    return total;
}

void test_norad_resolution() {
    GameState gs;
    gs.pub.norad_active = true;
    gs.pub.defcon = 2;
    gs.pub.set_influence(Side::US, 21, 1);
    gs.pub.set_influence(Side::US, 22, 2);
    const auto before_total = total_us_influence(gs.pub);

    ts::Pcg64Rng rng(11U);
    auto result = ts::resolve_norad_live(gs, rng);
    require(result.has_value(), "NORAD should resolve when the US has eligible influence");
    require(total_us_influence(gs.pub) == before_total + 1, "NORAD should add exactly one US influence");
    require(gs.pub.influence_of(Side::US, 21) >= 1, "NORAD must not remove existing US influence");
    require(gs.pub.influence_of(Side::US, 22) >= 2, "NORAD must target an already-US-influenced country");
}

PolicyFn min_space_policy() {
    return [](const PublicState&, const ts::CardSet& hand, bool, ts::Pcg64Rng&) -> std::optional<ActionEncoding> {
        for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
            if (hand.test(card_id)) {
                return ActionEncoding{
                    .card_id = static_cast<ts::CardId>(card_id),
                    .mode = ActionMode::Space,
                    .targets = {},
                };
            }
        }
        return std::nullopt;
    };
}

void test_trap_resolution() {
    GameState gs;
    gs.pub.bear_trap_active = true;
    gs.hands[ts::to_index(Side::USSR)].set(7);
    gs.hands[ts::to_index(Side::USSR)].set(8);

    bool saw_escape = false;
    bool saw_fail = false;
    for (uint32_t seed = 1; seed <= 64 && (!saw_escape || !saw_fail); ++seed) {
        auto probe = gs;
        ts::Pcg64Rng rng(seed);
        auto result = ts::resolve_trap_ar_live(probe, Side::USSR, rng);
        require(result.has_value(), "Bear Trap should consume an AR when active");
        require(ts::hand_count(probe.hands[ts::to_index(Side::USSR)]) == 1, "Trap resolution should discard exactly one eligible card");
        if (!probe.pub.bear_trap_active) {
            saw_escape = true;
        } else {
            saw_fail = true;
        }
    }

    require(saw_escape, "Trap resolution should sometimes clear Bear Trap");
    require(saw_fail, "Trap resolution should sometimes leave Bear Trap active");
}

void test_headline_order_and_defectors() {
    GameState gs = ts::reset_game(0U);
    gs.pub.turn = 1;
    gs.pub.defcon = 5;
    gs.hands[ts::to_index(Side::USSR)].reset();
    gs.hands[ts::to_index(Side::US)].reset();
    gs.hands[ts::to_index(Side::USSR)].set(12);
    gs.hands[ts::to_index(Side::US)].set(21);
    gs.ussr_holds_china = false;
    gs.us_holds_china = false;

    const PolicyFn ussr_policy = [](const PublicState&, const ts::CardSet&, bool, ts::Pcg64Rng&) -> std::optional<ActionEncoding> {
        return ActionEncoding{.card_id = 12, .mode = ActionMode::Event, .targets = {}};
    };
    const PolicyFn us_policy = [](const PublicState&, const ts::CardSet&, bool, ts::Pcg64Rng&) -> std::optional<ActionEncoding> {
        return ActionEncoding{.card_id = 21, .mode = ActionMode::Event, .targets = {}};
    };

    std::vector<StepTrace> trace_steps;
    ts::Pcg64Rng rng(1U);
    auto result = ts::run_headline_phase_live(gs, ussr_policy, us_policy, rng, &trace_steps);
    require(!result.has_value(), "Simple headline ordering smoke should not end the game");
    require(trace_steps.size() == 2, "Headline phase should trace both headline actions");
    require(trace_steps.front().side == Side::US, "Higher-op US headline should resolve before lower-op USSR headline");

    gs = ts::reset_game(0U);
    gs.pub.turn = 1;
    gs.pub.defcon = 5;
    gs.hands[ts::to_index(Side::USSR)].reset();
    gs.hands[ts::to_index(Side::US)].reset();
    gs.hands[ts::to_index(Side::USSR)].set(8);
    gs.hands[ts::to_index(Side::US)].set(108);
    gs.ussr_holds_china = false;
    gs.us_holds_china = false;

    const PolicyFn fidel_policy = [](const PublicState&, const ts::CardSet&, bool, ts::Pcg64Rng&) -> std::optional<ActionEncoding> {
        return ActionEncoding{.card_id = 8, .mode = ActionMode::Event, .targets = {}};
    };
    const PolicyFn defectors_policy = [](const PublicState&, const ts::CardSet&, bool, ts::Pcg64Rng&) -> std::optional<ActionEncoding> {
        return ActionEncoding{.card_id = 108, .mode = ActionMode::Event, .targets = {}};
    };

    trace_steps.clear();
    ts::Pcg64Rng rng2(2U);
    result = ts::run_headline_phase_live(gs, fidel_policy, defectors_policy, rng2, &trace_steps);
    require(!result.has_value(), "Defectors headline smoke should not end the game");
    require(gs.pub.influence_of(Side::USSR, 36) == 0, "Defectors headline should cancel the USSR headline event effect");
    require(gs.pub.discard.test(8), "Cancelled USSR headline card should still be discarded");
}

void test_space_level6_discard() {
    GameState gs;
    gs.pub.space[ts::to_index(Side::US)] = 6;
    gs.pub.space_level6_first = Side::US;
    gs.pub.space[ts::to_index(Side::USSR)] = 0;
    gs.hands[ts::to_index(Side::US)].set(7);
    gs.hands[ts::to_index(Side::US)].set(8);

    ts::Pcg64Rng rng(7U);
    auto result = ts::apply_action_live(
        gs,
        ActionEncoding{
            .card_id = 18,
            .mode = ActionMode::Space,
            .targets = {},
        },
        Side::USSR,
        rng
    );
    (void)result;
    require(ts::hand_count(gs.hands[ts::to_index(Side::US)]) == 1, "Level-6 advantage holder should discard one card when the opponent spaces while still below level 6");
    require(gs.pub.discard.test(7) || gs.pub.discard.test(8), "Space level-6 discard should move an advantage-holder card to discard");
}

void test_norad_action_round_gate() {
    GameState gs = ts::reset_game(0U);
    gs.pub.turn = 1;
    gs.pub.defcon = 2;
    gs.pub.norad_active = true;
    for (ts::CountryId cid = 0; cid < ts::kCountrySlots; ++cid) {
        gs.pub.set_influence(Side::US, cid, 0);
    }
    gs.pub.set_influence(Side::US, 10, 2);
    gs.hands[ts::to_index(Side::USSR)].reset();
    gs.hands[ts::to_index(Side::US)].reset();
    gs.hands[ts::to_index(Side::USSR)].set(12);
    gs.hands[ts::to_index(Side::US)].set(22);
    gs.ussr_holds_china = false;
    gs.us_holds_china = false;

    auto policy = min_space_policy();
    const auto italy_before = gs.pub.influence_of(Side::US, 10);
    ts::Pcg64Rng rng(3U);
    auto result = ts::run_action_rounds_live(gs, policy, policy, rng, 1, nullptr);
    require(!result.has_value(), "NORAD gate smoke should not end the game");
    require(gs.pub.influence_of(Side::US, 10) == italy_before + 1, "NORAD should add one US influence after a USSR AR at DEFCON 2");

    gs = ts::reset_game(0U);
    gs.pub.turn = 1;
    gs.pub.defcon = 3;
    gs.pub.norad_active = true;
    for (ts::CountryId cid = 0; cid < ts::kCountrySlots; ++cid) {
        gs.pub.set_influence(Side::US, cid, 0);
    }
    gs.pub.set_influence(Side::US, 10, 2);
    gs.hands[ts::to_index(Side::USSR)].reset();
    gs.hands[ts::to_index(Side::US)].reset();
    gs.hands[ts::to_index(Side::USSR)].set(12);
    gs.hands[ts::to_index(Side::US)].set(22);
    gs.ussr_holds_china = false;
    gs.us_holds_china = false;

    const auto italy_before_defcon3 = gs.pub.influence_of(Side::US, 10);
    ts::Pcg64Rng rng_defcon3(4U);
    result = ts::run_action_rounds_live(gs, policy, policy, rng_defcon3, 1, nullptr);
    require(!result.has_value(), "NORAD DEFCON 3 smoke should not end the game");
    require(gs.pub.influence_of(Side::US, 10) == italy_before_defcon3, "NORAD should not trigger above DEFCON 2");
}

void test_extra_action_round_trace() {
    GameState gs;
    gs.pub.turn = 4;
    gs.pub.ar = ts::ars_for_turn(gs.pub.turn);
    gs.pub.phasing = Side::US;
    gs.hands[ts::to_index(Side::US)].set(4);
    gs.hands[ts::to_index(Side::US)].set(18);

    const PolicyFn policy = [](const PublicState&, const ts::CardSet&, bool, ts::Pcg64Rng&) -> std::optional<ActionEncoding> {
        return ActionEncoding{
            .card_id = 18,
            .mode = ActionMode::Space,
            .targets = {},
        };
    };

    std::vector<StepTrace> trace_steps;
    ts::Pcg64Rng rng(5U);
    const auto result = ts::run_extra_action_round_live(gs, Side::US, policy, rng, &trace_steps);
    require(!result.has_value(), "A simple extra action round smoke should not end the game");
    require(trace_steps.size() == 1, "Extra action round should emit exactly one trace step");
    require(trace_steps.front().side == Side::US, "Extra action round trace should record the acting side");
    require(trace_steps.front().ar == ts::ars_for_turn(gs.pub.turn) + 1, "Extra action round should advance the trace AR beyond the normal round count");
}

void test_north_sea_oil_extra_ar_flow() {
    GameState gs = ts::reset_game(0U);
    gs.pub.turn = 1;
    gs.pub.defcon = 3;
    gs.pub.north_sea_oil_extra_ar = true;
    gs.hands[ts::to_index(Side::USSR)].reset();
    gs.hands[ts::to_index(Side::US)].reset();
    gs.hands[ts::to_index(Side::USSR)].set(12);
    gs.hands[ts::to_index(Side::US)].set(22);
    gs.hands[ts::to_index(Side::US)].set(28);
    gs.ussr_holds_china = false;
    gs.us_holds_china = false;

    auto policy = min_space_policy();
    ts::Pcg64Rng rng(6U);
    auto result = ts::run_action_rounds_live(gs, policy, policy, rng, 1, nullptr);
    require(!result.has_value(), "Regular action round before North Sea Oil extra AR should not end the game");
    require(ts::hand_count(gs.hands[ts::to_index(Side::US)]) == 1, "US should have one card left after the regular AR");
    require(gs.pub.north_sea_oil_extra_ar, "North Sea Oil flag should survive the regular AR loop");

    gs.pub.north_sea_oil_extra_ar = false;
    ts::Pcg64Rng extra_rng(7U);
    result = ts::run_extra_action_round_live(gs, Side::US, policy, extra_rng, nullptr);
    require(!result.has_value(), "North Sea Oil extra AR should not end the game in the smoke setup");
    require(ts::hand_count(gs.hands[ts::to_index(Side::US)]) == 0, "North Sea Oil extra AR should consume the remaining US card");
}

}  // namespace

int main() {
    test_norad_resolution();
    test_trap_resolution();
    test_headline_order_and_defectors();
    test_space_level6_discard();
    test_norad_action_round_gate();
    test_extra_action_round_trace();
    test_north_sea_oil_extra_ar_flow();
    std::cout << "loop mechanics smoke ok\n";
    return 0;
}
