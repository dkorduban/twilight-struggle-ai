#include <catch2/catch_test_macros.hpp>

#include <algorithm>
#include <atomic>
#include <chrono>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <optional>
#include <string>
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

std::filesystem::path find_collector_binary() {
    const auto cwd = std::filesystem::current_path();
    const std::vector<std::filesystem::path> candidates{
        cwd / "cpp/tools/ts_collect_selfplay_rows_jsonl",
        cwd.parent_path() / "cpp/tools/ts_collect_selfplay_rows_jsonl",
        cwd.parent_path().parent_path() / "cpp/tools/ts_collect_selfplay_rows_jsonl",
    };
    for (const auto& candidate : candidates) {
        if (std::filesystem::exists(candidate)) {
            return candidate;
        }
    }
    FAIL("ts_collect_selfplay_rows_jsonl binary was not found from " << cwd.string());
    return {};
}

std::string shell_quote(const std::filesystem::path& path) {
    return std::string("'") + path.string() + "'";
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
    REQUIRE(step->sub_frames.front().chosen_action.country_id != 0);
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

TEST_CASE("test_collect_selfplay_jsonl_emits_subframe_rows", "[subframe_logging]") {
    const auto collector = find_collector_binary();
    const auto stamp = std::chrono::steady_clock::now().time_since_epoch().count();
    const auto output = std::filesystem::path("/tmp") /
        (std::string("ts_subframe_logging_") + std::to_string(stamp) + ".jsonl");
    const auto command = shell_quote(collector) +
        " --out " + shell_quote(output) +
        " --games 3 --seed 24680 --ussr-policy minimal --us-policy minimal";

    REQUIRE(std::system(command.c_str()) == 0);

    std::ifstream in(output);
    REQUIRE(in.good());

    int ar_rows = 0;
    int subframe_rows = 0;
    bool saw_frame_kind = false;
    bool saw_chosen_country = false;
    std::string line;
    while (std::getline(in, line)) {
        if (line.find("\"row_kind\":\"ar\"") != std::string::npos) {
            ++ar_rows;
        }
        if (line.find("\"row_kind\":\"subframe\"") != std::string::npos) {
            ++subframe_rows;
            saw_frame_kind = saw_frame_kind || line.find("\"frame_kind\":") != std::string::npos;
            saw_chosen_country = saw_chosen_country || line.find("\"chosen_country\":") != std::string::npos;
        }
    }

    REQUIRE(ar_rows > 0);
    REQUIRE(subframe_rows > 0);
    REQUIRE(saw_frame_kind);
    REQUIRE(saw_chosen_country);
}
