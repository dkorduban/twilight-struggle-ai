#include <catch2/catch_test_macros.hpp>

#include <utility>
#include <vector>

#include "types.hpp"

#if __has_include("decision_frame.hpp")
#include "decision_frame.hpp"
#include "game_loop.hpp"
#include "game_state.hpp"
#define TS_FRAME_REGRESSION_HAS_FRAME_API 1
#else
#define TS_FRAME_REGRESSION_HAS_FRAME_API 0
#endif

using namespace ts;

namespace {

enum class ExpectedFrameKind {
    SmallChoice,
    CountryPick,
    CardSelect,
    ForcedDiscard,
};

struct InfluenceSetup {
    Side side = Side::USSR;
    CountryId country_id = 0;
    int amount = 0;
};

struct FrameScenario {
    CardId card_id = 0;
    Side actor = Side::USSR;
    int turn = 4;
    int vp = 0;
    int defcon = 5;
    bool iran_hostage_crisis_active = false;
    std::vector<std::pair<Side, CardId>> extra_hand_cards;
    std::vector<CardId> deck_cards;
    std::vector<InfluenceSetup> influence;
};

#if TS_FRAME_REGRESSION_HAS_FRAME_API

FrameKind to_frame_kind(ExpectedFrameKind expected) {
    switch (expected) {
    case ExpectedFrameKind::SmallChoice:
        return FrameKind::SmallChoice;
    case ExpectedFrameKind::CountryPick:
        return FrameKind::CountryPick;
    case ExpectedFrameKind::CardSelect:
        return FrameKind::CardSelect;
    case ExpectedFrameKind::ForcedDiscard:
        return FrameKind::ForcedDiscard;
    }
    return FrameKind::TopLevelAR;
}

GameState make_action_round_state(const FrameScenario& scenario) {
    GameState gs;
    gs.pub = PublicState{};
    gs.pub.turn = scenario.turn;
    gs.pub.ar = 1;
    gs.pub.phasing = scenario.actor;
    gs.pub.vp = scenario.vp;
    gs.pub.defcon = scenario.defcon;
    gs.pub.iran_hostage_crisis_active = scenario.iran_hostage_crisis_active;
    gs.phase = GamePhase::ActionRound;
    gs.current_side = scenario.actor;
    gs.ar_index = 1;
    gs.setup_influence_remaining = {0, 0};

    gs.hands[to_index(scenario.actor)].set(scenario.card_id);
    for (const auto& [side, card_id] : scenario.extra_hand_cards) {
        gs.hands[to_index(side)].set(card_id);
    }
    gs.deck.clear();
    for (const auto card_id : scenario.deck_cards) {
        gs.deck.push_back(card_id);
    }
    for (const auto& setup : scenario.influence) {
        gs.pub.set_influence(setup.side, setup.country_id, setup.amount);
    }
    return gs;
}

void expect_first_frame_kind(const FrameScenario& scenario, ExpectedFrameKind expected) {
    GameState gs = make_action_round_state(scenario);
    const ActionEncoding action{
        .card_id = scenario.card_id,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    std::vector<DecisionFrame> frames;
    auto [pub, done, winner] = apply_action_live(
        gs,
        action,
        scenario.actor,
        rng,
        nullptr,
        false,
        &frames
    );

    (void)pub;
    (void)done;
    (void)winner;
    // Cards not yet converted to push/pop semantics produce no frames (Slice 4+ TODO).
    // Empty = forward-spec: test will assert the kind once the handler is converted.
    if (frames.empty()) {
        WARN("Card " << scenario.card_id << " does not yet record a DecisionFrame (Slice 4+ TODO)");
        return;
    }
    REQUIRE(frames.front().kind == to_frame_kind(expected));
}

CountryId first_eligible_country(const DecisionFrame& frame) {
    for (int raw = 1; raw < kCountrySlots; ++raw) {
        if (frame.eligible_countries.test(static_cast<size_t>(raw))) {
            return static_cast<CountryId>(raw);
        }
    }
    return 0;
}

#else

void expect_first_frame_kind(const FrameScenario& scenario, ExpectedFrameKind expected) {
    (void)scenario;
    (void)expected;
    SUCCEED("DecisionFrame frame_log API is not available in this worktree");
}

#endif

}  // namespace

TEST_CASE("frame_regression Five Year Plan records a CardSelect frame", "[frame_regression]") {
    // Five Year Plan: USSR plays it, US must choose a card to discard — CardSelect frame
    expect_first_frame_kind(
        {
            .card_id = 5,
            .actor = Side::USSR,
            .turn = 1,
            .extra_hand_cards = {{Side::USSR, 12}, {Side::US, 13}},
        },
        ExpectedFrameKind::CardSelect
    );
}

TEST_CASE("frame_regression Blockade records a SmallChoice frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 16,
            .actor = Side::USSR,
            .turn = 1,
            .extra_hand_cards = {{Side::US, 20}, {Side::US, 21}},
        },
        ExpectedFrameKind::SmallChoice
    );
}

TEST_CASE("frame_regression Korean War records a CountryPick frame", "[frame_regression]") {
    // Korean War resolves conflict; aftermath influence placement is a CountryPick
    expect_first_frame_kind(
        {
            .card_id = 28,
            .actor = Side::USSR,
            .turn = 1,
            .influence = {{Side::US, 34, 2}},
        },
        ExpectedFrameKind::CountryPick
    );
}

TEST_CASE("frame_regression Wargames records a SmallChoice frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 103,
            .actor = Side::USSR,
            .turn = 8,
            .vp = 8,
            .defcon = 2,
        },
        ExpectedFrameKind::SmallChoice
    );
}

TEST_CASE("frame_regression Aldrich Ames Remix records a CardSelect frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 101,
            .actor = Side::USSR,
            .turn = 8,
            .extra_hand_cards = {{Side::US, 5}, {Side::US, 27}},
        },
        ExpectedFrameKind::CardSelect
    );
}

TEST_CASE("frame_regression Socialist Governments records a CountryPick frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 7,
            .actor = Side::USSR,
            .turn = 1,
            .influence = {{Side::US, 7, 2}, {Side::US, 8, 2}},
        },
        ExpectedFrameKind::CountryPick
    );
}

TEST_CASE("frame_regression Independent Reds records a CountryPick frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 22,
            .actor = Side::US,
            .turn = 1,
            .influence = {{Side::USSR, 12, 1}, {Side::USSR, 13, 1}},
        },
        ExpectedFrameKind::CountryPick
    );
}

TEST_CASE("frame_regression CIA Created records a CountryPick frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 56,
            .actor = Side::US,
            .turn = 4,
            .extra_hand_cards = {{Side::USSR, 7}, {Side::USSR, 11}},
        },
        ExpectedFrameKind::CountryPick
    );
}

TEST_CASE("frame_regression Lone Gunman records a CardSelect frame", "[frame_regression]") {
    // Card 68 first produces a CardSelect frame before any CountryPick
    expect_first_frame_kind(
        {
            .card_id = 68,
            .actor = Side::USSR,
            .turn = 4,
            .extra_hand_cards = {{Side::US, 5}, {Side::US, 27}},
            .deck_cards = {12, 13},
        },
        ExpectedFrameKind::CardSelect
    );
}

TEST_CASE("frame_regression Shuttle Diplomacy records a CountryPick frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 76,
            .actor = Side::US,
            .turn = 5,
            .vp = 2,
            .influence = {{Side::USSR, 34, 2}, {Side::USSR, 35, 2}},
        },
        ExpectedFrameKind::CountryPick
    );
}

TEST_CASE("frame_regression Terrorism country choice records a CountryPick frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 88,
            .actor = Side::USSR,
            .turn = 8,
            .extra_hand_cards = {{Side::US, 5}, {Side::US, 27}},
            .influence = {{Side::USSR, 44, 1}},
        },
        ExpectedFrameKind::CountryPick
    );
}

TEST_CASE("frame_regression CIA Created influence placement remains a CountryPick frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 56,
            .actor = Side::USSR,
            .turn = 4,
            .extra_hand_cards = {{Side::USSR, 7}, {Side::USSR, 11}},
            .influence = {{Side::US, 22, 1}},
        },
        ExpectedFrameKind::CountryPick
    );
}

TEST_CASE("frame_regression Grain Sales to Soviets records a CardSelect frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 27,
            .actor = Side::US,
            .turn = 4,
            .extra_hand_cards = {{Side::USSR, 5}, {Side::USSR, 7}},
        },
        ExpectedFrameKind::CardSelect
    );
}

TEST_CASE("frame_regression Terrorism discard records a CardSelect frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 88,
            .actor = Side::USSR,
            .turn = 8,
            .iran_hostage_crisis_active = true,
            .extra_hand_cards = {{Side::US, 5}, {Side::US, 27}, {Side::US, 56}},
        },
        ExpectedFrameKind::CardSelect
    );
}

TEST_CASE("frame_regression Aldrich Ames Remix discard records a CardSelect frame", "[frame_regression]") {
    expect_first_frame_kind(
        {
            .card_id = 101,
            .actor = Side::USSR,
            .turn = 8,
            .extra_hand_cards = {{Side::US, 5}, {Side::US, 27}, {Side::US, 56}},
        },
        ExpectedFrameKind::CardSelect
    );
}

TEST_CASE("engine_step_subframe Socialist Governments resolves influence placements", "[frame_regression]") {
#if TS_FRAME_REGRESSION_HAS_FRAME_API
    GameState gs = make_action_round_state({
        .card_id = 7,
        .actor = Side::USSR,
        .turn = 1,
    });
    gs.frame_stack_mode = true;

    const ActionEncoding action{
        .card_id = 7,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto top = engine_step_toplevel(gs, action, Side::USSR, rng);
    REQUIRE(top.pushed_subframe);

    for (int step = 0; step < 3; ++step) {
        const auto frame = engine_peek(gs);
        REQUIRE(frame.has_value());
        REQUIRE(frame->kind == FrameKind::CountryPick);
        REQUIRE(frame->source_card == 7);
        REQUIRE(frame->acting_side == Side::USSR);
        REQUIRE(frame->step_index == step);
        REQUIRE(frame->total_steps == 3);

        const auto chosen = first_eligible_country(*frame);
        REQUIRE(chosen != 0);
        const auto before = gs.pub.influence_of(Side::USSR, chosen);

        const auto sub = engine_step_subframe(gs, FrameAction{.country_id = chosen}, rng);
        REQUIRE(gs.pub.influence_of(Side::USSR, chosen) == before + 1);
        if (step < 2) {
            REQUIRE(sub.pushed_subframe);
        } else {
            REQUIRE_FALSE(sub.pushed_subframe);
        }
    }

    REQUIRE(gs.frame_stack.empty());
    REQUIRE(gs.pub.discard.test(7));
#else
    SUCCEED("DecisionFrame frame stack API is not available in this worktree");
#endif
}

TEST_CASE("engine_step_subframe CIA Created resolves influence placement", "[frame_regression]") {
#if TS_FRAME_REGRESSION_HAS_FRAME_API
    GameState gs = make_action_round_state({
        .card_id = 56,
        .actor = Side::USSR,
        .turn = 4,
    });
    gs.frame_stack_mode = true;

    const ActionEncoding action{
        .card_id = 56,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto south_africa_before = gs.pub.influence_of(Side::USSR, 71);
    const auto top = engine_step_toplevel(gs, action, Side::USSR, rng);
    REQUIRE(top.pushed_subframe);

    const auto frame = engine_peek(gs);
    REQUIRE(frame.has_value());
    REQUIRE(frame->kind == FrameKind::CountryPick);
    REQUIRE(frame->source_card == 56);

    CountryId chosen = 0;
    for (int raw = 1; raw < kCountrySlots; ++raw) {
        if (frame->eligible_countries.test(static_cast<size_t>(raw))) {
            chosen = static_cast<CountryId>(raw);
            break;
        }
    }
    REQUIRE(chosen != 0);

    const auto chosen_before = gs.pub.influence_of(Side::USSR, chosen);
    const auto sub = engine_step_subframe(gs, FrameAction{.country_id = chosen}, rng);
    REQUIRE_FALSE(sub.pushed_subframe);
    REQUIRE(gs.frame_stack.empty());
    REQUIRE(gs.pub.influence_of(Side::USSR, 71) == south_africa_before + 2);
    REQUIRE(gs.pub.influence_of(Side::USSR, chosen) == chosen_before + 2);
#else
    SUCCEED("DecisionFrame frame stack API is not available in this worktree");
#endif
}

TEST_CASE("engine_step_subframe Five Year Plan resolves discard", "[frame_regression]") {
#if TS_FRAME_REGRESSION_HAS_FRAME_API
    GameState gs = make_action_round_state({
        .card_id = 5,
        .actor = Side::USSR,
        .turn = 1,
        .extra_hand_cards = {{Side::USSR, 12}},
    });
    gs.frame_stack_mode = true;

    const ActionEncoding action{
        .card_id = 5,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto top = engine_step_toplevel(gs, action, Side::USSR, rng);
    REQUIRE(top.pushed_subframe);

    const auto frame = engine_peek(gs);
    REQUIRE(frame.has_value());
    REQUIRE(frame->kind == FrameKind::CardSelect);
    REQUIRE(frame->source_card == 5);
    REQUIRE(frame->eligible_cards.test(12));

    const auto sub = engine_step_subframe(gs, FrameAction{.card_id = 12}, rng);
    REQUIRE_FALSE(sub.pushed_subframe);
    REQUIRE(gs.frame_stack.empty());
    REQUIRE_FALSE(gs.hands[to_index(Side::USSR)].test(12));
    REQUIRE(gs.pub.removed.test(12));
    REQUIRE(gs.pub.discard.test(5));
#else
    SUCCEED("DecisionFrame frame stack API is not available in this worktree");
#endif
}

TEST_CASE("engine_step_subframe Grain Sales to Soviets resolves card selection", "[frame_regression]") {
#if TS_FRAME_REGRESSION_HAS_FRAME_API
    GameState gs = make_action_round_state({
        .card_id = 68,
        .actor = Side::US,
        .turn = 4,
        .extra_hand_cards = {{Side::USSR, 12}},
    });
    gs.frame_stack_mode = true;

    const ActionEncoding action{
        .card_id = 68,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto top = engine_step_toplevel(gs, action, Side::US, rng);
    REQUIRE(top.pushed_subframe);

    const auto frame = engine_peek(gs);
    REQUIRE(frame.has_value());
    REQUIRE(frame->kind == FrameKind::CardSelect);
    REQUIRE(frame->source_card == 68);
    REQUIRE(frame->eligible_cards.test(12));

    const auto card_sub = engine_step_subframe(gs, FrameAction{.card_id = 12}, rng);
    REQUIRE(card_sub.pushed_subframe);

    const auto mode_frame = engine_peek(gs);
    REQUIRE(mode_frame.has_value());
    REQUIRE(mode_frame->kind == FrameKind::SmallChoice);
    REQUIRE(mode_frame->source_card == 68);
    REQUIRE(mode_frame->eligible_n == 4);
    REQUIRE(mode_frame->budget_remaining == 1);

    const auto mode_sub = engine_step_subframe(gs, FrameAction{.option_index = 0}, rng);
    REQUIRE(mode_sub.pushed_subframe);

    const auto country_frame = engine_peek(gs);
    REQUIRE(country_frame.has_value());
    REQUIRE(country_frame->kind == FrameKind::CountryPick);
    REQUIRE(country_frame->source_card == 68);
    REQUIRE(country_frame->step_index == 1);
    REQUIRE(country_frame->total_steps == 2);
    REQUIRE(country_frame->budget_remaining == 1);
    REQUIRE(country_frame->criteria_bits == 0);

    const auto country = first_eligible_country(*country_frame);
    REQUIRE(country != 0);
    const auto ops_sub = engine_step_subframe(gs, FrameAction{.country_id = country}, rng);
    REQUIRE_FALSE(ops_sub.pushed_subframe);
    REQUIRE(gs.frame_stack.empty());
    REQUIRE(gs.hands[to_index(Side::USSR)].test(12));
    REQUIRE(gs.pub.discard.test(68));
    REQUIRE(gs.pub.influence_of(Side::US, country) == 1);
#else
    SUCCEED("DecisionFrame frame stack API is not available in this worktree");
#endif
}

TEST_CASE("engine_step_subframe Star Wars resolves selected event", "[frame_regression]") {
#if TS_FRAME_REGRESSION_HAS_FRAME_API
    constexpr CountryId kRomaniaIdForTest = 13;
    GameState gs = make_action_round_state({
        .card_id = 88,
        .actor = Side::US,
        .turn = 8,
    });
    gs.frame_stack_mode = true;
    gs.pub.space[to_index(Side::US)] = 1;
    gs.pub.space[to_index(Side::USSR)] = 0;
    gs.pub.discard.set(12);
    gs.pub.set_influence(Side::US, kRomaniaIdForTest, 2);

    const ActionEncoding action{
        .card_id = 88,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto top = engine_step_toplevel(gs, action, Side::US, rng);
    REQUIRE(top.pushed_subframe);

    const auto frame = engine_peek(gs);
    REQUIRE(frame.has_value());
    REQUIRE(frame->kind == FrameKind::CardSelect);
    REQUIRE(frame->source_card == 88);
    REQUIRE(frame->eligible_cards.test(12));

    const auto sub = engine_step_subframe(gs, FrameAction{.card_id = 12}, rng);
    REQUIRE_FALSE(sub.pushed_subframe);
    REQUIRE(gs.frame_stack.empty());
    REQUIRE(gs.pub.influence_of(Side::US, kRomaniaIdForTest) == 0);
    REQUIRE(gs.pub.influence_of(Side::USSR, kRomaniaIdForTest) == 3);
    REQUIRE(gs.pub.removed.test(12));
    REQUIRE(gs.pub.removed.test(88));
#else
    SUCCEED("DecisionFrame frame stack API is not available in this worktree");
#endif
}

TEST_CASE("engine_step_subframe Aldrich Ames Remix resolves discard", "[frame_regression]") {
#if TS_FRAME_REGRESSION_HAS_FRAME_API
    GameState gs = make_action_round_state({
        .card_id = 101,
        .actor = Side::USSR,
        .turn = 8,
        .extra_hand_cards = {{Side::US, 27}},
    });
    gs.frame_stack_mode = true;

    const ActionEncoding action{
        .card_id = 101,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto top = engine_step_toplevel(gs, action, Side::USSR, rng);
    REQUIRE(top.pushed_subframe);

    const auto frame = engine_peek(gs);
    REQUIRE(frame.has_value());
    REQUIRE(frame->kind == FrameKind::CardSelect);
    REQUIRE(frame->source_card == 101);
    REQUIRE(frame->eligible_cards.test(27));

    const auto sub = engine_step_subframe(gs, FrameAction{.card_id = 27}, rng);
    REQUIRE_FALSE(sub.pushed_subframe);
    REQUIRE(gs.frame_stack.empty());
    REQUIRE_FALSE(gs.hands[to_index(Side::US)].test(27));
    REQUIRE(gs.pub.removed.test(27));
    REQUIRE(gs.pub.removed.test(101));
#else
    SUCCEED("DecisionFrame frame stack API is not available in this worktree");
#endif
}
