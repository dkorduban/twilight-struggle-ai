#include <catch2/catch_test_macros.hpp>

#include <atomic>
#include <algorithm>
#include <optional>
#include <vector>

#include "game_loop.hpp"
#include "game_state.hpp"
#include "hand_ops.hpp"

using namespace ts;

namespace {

GameState make_socialist_governments_trace_state() {
    auto gs = reset_game(0);
    gs.pub.set_influence(Side::US, 1, 2);
    gs.pub.set_influence(Side::US, 2, 1);
    return gs;
}

PolicyFn socialist_governments_policy() {
    return [](const PublicState& pub, const CardSet&, bool, Pcg64Rng&) -> std::optional<ActionEncoding> {
        if (pub.ar == 0) {
            return std::nullopt;
        }
        return ActionEncoding{
            .card_id = static_cast<CardId>(7),
            .mode = ActionMode::Event,
            .targets = {},
        };
    };
}

PolicyFn pass_policy() {
    return [](const PublicState&, const CardSet&, bool, Pcg64Rng&) -> std::optional<ActionEncoding> {
        return std::nullopt;
    };
}

GameLoopConfig trace_test_config() {
    GameLoopConfig config;
    config.skip_setup_influence = true;
    return config;
}

}  // namespace

TEST_CASE("test_decision_frame_chosen_action_smallchoice", "[subframe_logging]") {
    DecisionFrame frame;
    frame.kind = FrameKind::SmallChoice;
    frame.eligible_n = 3;
    frame.budget_remaining = 2;

    std::vector<DecisionFrame> frame_log;
    const auto logged = logged_frame_copy(frame, &frame_log, FrameAction{.option_index = 2});

    REQUIRE(logged.chosen_action.option_index == 2);
    REQUIRE(logged.criteria_bits == 2);
}

TEST_CASE("test_decision_frame_chosen_action_countrypick", "[subframe_logging]") {
    DecisionFrame frame;
    frame.kind = FrameKind::CountryPick;

    std::vector<DecisionFrame> frame_log;
    const auto logged = logged_frame_copy(frame, &frame_log, FrameAction{.country_id = 42});

    REQUIRE(logged.chosen_action.option_index == 0);
    REQUIRE(logged.chosen_action.card_id == 0);
    REQUIRE(logged.chosen_action.country_id == 42);
}

TEST_CASE("test_decision_frame_chosen_action_cardselect", "[subframe_logging]") {
    DecisionFrame frame;
    frame.kind = FrameKind::CardSelect;

    std::vector<DecisionFrame> frame_log;
    const auto logged = logged_frame_copy(frame, &frame_log, FrameAction{.card_id = 17});

    REQUIRE(logged.chosen_action.option_index == 0);
    REQUIRE(logged.chosen_action.card_id == 17);
    REQUIRE(logged.chosen_action.country_id == 0);
}

TEST_CASE("test_traced_game_captures_subframes", "[subframe_logging]") {
    auto gs = make_socialist_governments_trace_state();
    Pcg64Rng rng(0);
    PolicyCallbackFn subframe_cb = [](const PublicState&, const EventDecision&) {
        return 0;
    };

    const auto traced = play_game_traced_from_state_with_rng(
        gs,
        socialist_governments_policy(),
        pass_policy(),
        rng,
        trace_test_config(),
        &subframe_cb
    );

    const auto step = std::find_if(
        traced.steps.begin(),
        traced.steps.end(),
        [](const StepTrace& trace_step) {
            return trace_step.action.card_id == static_cast<CardId>(7) &&
                !trace_step.sub_frames.empty();
        }
    );
    REQUIRE(step != traced.steps.end());
    REQUIRE(step->sub_frames.front().kind == FrameKind::CountryPick);
}

TEST_CASE("test_policy_cb_is_invoked_per_subframe", "[subframe_logging]") {
    auto gs = make_socialist_governments_trace_state();
    Pcg64Rng rng(0);
    std::atomic<int> callback_count{0};
    PolicyCallbackFn subframe_cb = [&](const PublicState&, const EventDecision&) {
        ++callback_count;
        return 0;
    };

    (void)play_game_traced_from_state_with_rng(
        gs,
        socialist_governments_policy(),
        pass_policy(),
        rng,
        trace_test_config(),
        &subframe_cb
    );

    REQUIRE(callback_count.load() >= 1);
}
