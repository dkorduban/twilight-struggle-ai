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

    std::mt19937 rng(11U);
    auto result = ts::resolve_norad_live(gs, rng);
    require(result.has_value(), "NORAD should resolve when the US has eligible influence");
    require(total_us_influence(gs.pub) == before_total + 1, "NORAD should add exactly one US influence");
    require(gs.pub.influence_of(Side::US, 21) >= 1, "NORAD must not remove existing US influence");
    require(gs.pub.influence_of(Side::US, 22) >= 2, "NORAD must target an already-US-influenced country");
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
        std::mt19937 rng(seed);
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

void test_space_level6_discard() {
    GameState gs;
    gs.pub.space[ts::to_index(Side::US)] = 6;
    gs.pub.space_level6_first = Side::US;
    gs.pub.space[ts::to_index(Side::USSR)] = 0;
    gs.hands[ts::to_index(Side::US)].set(7);
    gs.hands[ts::to_index(Side::US)].set(8);

    std::mt19937 rng(7U);
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

void test_extra_action_round_trace() {
    GameState gs;
    gs.pub.turn = 4;
    gs.pub.ar = ts::ars_for_turn(gs.pub.turn);
    gs.pub.phasing = Side::US;
    gs.hands[ts::to_index(Side::US)].set(4);
    gs.hands[ts::to_index(Side::US)].set(18);

    const PolicyFn policy = [](const PublicState&, const ts::CardSet&, bool, std::mt19937&) -> std::optional<ActionEncoding> {
        return ActionEncoding{
            .card_id = 18,
            .mode = ActionMode::Space,
            .targets = {},
        };
    };

    std::vector<StepTrace> trace_steps;
    std::mt19937 rng(5U);
    const auto result = ts::run_extra_action_round_live(gs, Side::US, policy, rng, &trace_steps);
    require(!result.has_value(), "A simple extra action round smoke should not end the game");
    require(trace_steps.size() == 1, "Extra action round should emit exactly one trace step");
    require(trace_steps.front().side == Side::US, "Extra action round trace should record the acting side");
    require(trace_steps.front().ar == ts::ars_for_turn(gs.pub.turn) + 1, "Extra action round should advance the trace AR beyond the normal round count");
}

}  // namespace

int main() {
    test_norad_resolution();
    test_trap_resolution();
    test_space_level6_discard();
    test_extra_action_round_trace();
    std::cout << "loop mechanics smoke ok\n";
    return 0;
}
