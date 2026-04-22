#include <catch2/catch_test_macros.hpp>

#include <vector>

#include "hand_ops.hpp"

using namespace ts;

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
