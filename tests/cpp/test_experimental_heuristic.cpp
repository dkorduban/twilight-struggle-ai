#include <catch2/catch_test_macros.hpp>

#include "game_loop.hpp"
#include "runner.hpp"

TEST_CASE("experimental heuristic selfplay reaches a sane full-game trace", "[experimental][heuristic]") {
    ts::experimental::HeuristicConfig config;
    config.proposal_limit = 6;
    config.search_candidate_limit = 3;
    config.ismcts_determinizations = 2;
    config.ismcts_simulations = 24;
    const auto trace = ts::experimental::play_selfplay_game(12345u, config);

    REQUIRE_FALSE(trace.steps.empty());
    REQUIRE(trace.steps.front().turn == 1);
    REQUIRE(trace.steps.size() >= 80);
    REQUIRE(trace.result.end_turn >= 7);
    REQUIRE(trace.result.end_reason != "scoring_card_held");
    REQUIRE(trace.result.final_vp >= -20);
    REQUIRE(trace.result.final_vp <= 20);
}

TEST_CASE("match summaries keep cause-based terminal counts", "[experimental][heuristic]") {
    const std::array<ts::GameResult, 5> results = {{
        ts::GameResult{.winner = ts::Side::USSR, .final_vp = 20, .end_turn = 6, .end_reason = "wargames"},
        ts::GameResult{.winner = ts::Side::US, .final_vp = -9, .end_turn = 5, .end_reason = "defcon1"},
        ts::GameResult{.winner = ts::Side::USSR, .final_vp = 22, .end_turn = 8, .end_reason = "europe_control"},
        ts::GameResult{.winner = ts::Side::US, .final_vp = -4, .end_turn = 10, .end_reason = "turn_limit"},
        ts::GameResult{.winner = ts::Side::USSR, .final_vp = 21, .end_turn = 4, .end_reason = "vp"},
    }};

    const auto summary = ts::summarize_results(results);

    REQUIRE(summary.games == 5);
    REQUIRE(summary.ussr_wins == 3);
    REQUIRE(summary.us_wins == 2);
    REQUIRE(summary.defcon1 == 1);
    REQUIRE(summary.wargames == 1);
    REQUIRE(summary.europe_control == 1);
    REQUIRE(summary.turn_limit == 1);
    REQUIRE(summary.vp_threshold == 1);
}

TEST_CASE("search no longer drops must-play scoring cards on known failing US seed", "[experimental][heuristic]") {
    ts::experimental::HeuristicConfig config;
    config.proposal_europe_support_pressure_bonus = 0.50;

    const auto trace = ts::experimental::play_matchup_game(
        ts::experimental::ExperimentalAgentSpec{
            .kind = ts::experimental::ExperimentalAgentKind::MinimalHybrid,
            .model_path = {},
        },
        ts::experimental::ExperimentalAgentSpec{
            .kind = ts::experimental::ExperimentalAgentKind::Search,
            .model_path = {},
        },
        448498040u,
        config
    );

    REQUIRE(trace.result.end_reason != "scoring_card_held");
}
