#include <algorithm>
#include <array>
#include <vector>

#include <catch2/catch_test_macros.hpp>

#include "game_data.hpp"
#include "game_loop.hpp"
#include "rng.hpp"
#include "step.hpp"
#include "types.hpp"

using namespace ts;

TEST_CASE("SALT Negotiations raises DEFCON by two and clamps at five", "[cards][step]") {
    constexpr CardId kSaltNegotiations = 46;
    constexpr std::array<std::pair<int, int>, 2> kCases = {{{2, 4}, {4, 5}}};

    for (const auto [initial_defcon, expected_defcon] : kCases) {
        PublicState pub;
        pub.defcon = initial_defcon;

        const ActionEncoding action{.card_id = kSaltNegotiations, .mode = ActionMode::Event, .targets = {}};
        Pcg64Rng rng(0);
        const auto [next, over, winner] = apply_action(pub, action, Side::USSR, rng);

        REQUIRE_FALSE(over);
        REQUIRE_FALSE(winner.has_value());
        REQUIRE(next.defcon == expected_defcon);
        REQUIRE(next.salt_active);
    }
}

TEST_CASE("Independent Reds equalizes only the chosen Eastern European country", "[cards][step]") {
    constexpr CountryId kRomaniaId = 13;
    constexpr CountryId kYugoslaviaId = 19;

    PublicState pub;
    pub.set_influence(Side::USSR, kRomaniaId, 3);
    pub.set_influence(Side::US, kRomaniaId, 1);
    pub.set_influence(Side::USSR, kYugoslaviaId, 2);

    int choice_count = 0;
    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
        REQUIRE(decision.kind == DecisionKind::CountrySelect);
        REQUIRE(decision.source_card == static_cast<CardId>(22));
        REQUIRE(decision.acting_side == Side::US);
        ++choice_count;
        for (int idx = 0; idx < decision.n_options; ++idx) {
            if (decision.eligible_ids[idx] == kRomaniaId) {
                return idx;
            }
        }
        FAIL("Romania must be eligible for Independent Reds");
        return 0;
    };

    const ActionEncoding action{.card_id = 22, .mode = ActionMode::Event, .targets = {}};
    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action(pub, action, Side::US, rng, &policy_cb);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(choice_count == 1);
    REQUIRE(next.influence_of(Side::US, kRomaniaId) == 3);
    REQUIRE(next.influence_of(Side::US, kYugoslaviaId) == 0);
}

TEST_CASE("South African Unrest applies only the selected mode", "[cards][step]") {
    constexpr CardId kSouthAfricanUnrest = 56;
    constexpr CountryId kAngolaId = 57;
    constexpr CountryId kBotswanaId = 58;
    constexpr CountryId kSouthAfricaId = 71;

    auto apply_with_mode = [=](int mode_choice, CountryId country_choice) {
        int option_calls = 0;
        int country_calls = 0;
        PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
            REQUIRE(decision.source_card == static_cast<CardId>(56));
            REQUIRE(decision.acting_side == Side::USSR);
            if (decision.kind == DecisionKind::SmallChoice) {
                ++option_calls;
                REQUIRE(decision.n_options == 2);
                return mode_choice;
            }
            REQUIRE(decision.kind == DecisionKind::CountrySelect);
            ++country_calls;
            for (int idx = 0; idx < decision.n_options; ++idx) {
                if (decision.eligible_ids[idx] == country_choice) {
                    return idx;
                }
            }
            FAIL("Requested South African Unrest neighbor was not eligible");
            return 0;
        };

        PublicState pub;
        const ActionEncoding action{.card_id = kSouthAfricanUnrest, .mode = ActionMode::Event, .targets = {}};
        Pcg64Rng rng(0);
        const auto [next, over, winner] = apply_action(pub, action, Side::USSR, rng, &policy_cb);

        REQUIRE_FALSE(over);
        REQUIRE_FALSE(winner.has_value());
        REQUIRE(option_calls == 1);
        REQUIRE(country_calls == (mode_choice == 0 ? 0 : 1));
        return next;
    };

    const auto south_africa_only = apply_with_mode(0, kAngolaId);
    REQUIRE(south_africa_only.influence_of(Side::USSR, kSouthAfricaId) == 2);
    REQUIRE(south_africa_only.influence_of(Side::USSR, kAngolaId) == 0);
    REQUIRE(south_africa_only.influence_of(Side::USSR, kBotswanaId) == 0);

    const auto split = apply_with_mode(1, kBotswanaId);
    REQUIRE(split.influence_of(Side::USSR, kSouthAfricaId) == 1);
    REQUIRE(split.influence_of(Side::USSR, kAngolaId) == 0);
    REQUIRE(split.influence_of(Side::USSR, kBotswanaId) == 2);
}

TEST_CASE("Latin American Debt Crisis doubles all USSR LatAm influence when US cannot pay", "[cards][game_loop]") {
    constexpr CardId kLatinAmericanDebtCrisis = 98;
    constexpr CountryId kArgentinaId = 46;
    constexpr CountryId kBrazilId = 48;
    constexpr CountryId kVenezuelaId = 55;

    GameState gs;
    gs.pub.set_influence(Side::USSR, kBrazilId, 2);
    gs.pub.set_influence(Side::USSR, kArgentinaId, 1);
    gs.hands[to_index(Side::US)].set(12);
    gs.hands[to_index(Side::US)].set(15);

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(
        gs,
        ActionEncoding{.card_id = kLatinAmericanDebtCrisis, .mode = ActionMode::Event, .targets = {}},
        Side::USSR,
        rng
    );

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.influence_of(Side::USSR, kBrazilId) == 4);
    REQUIRE(next.influence_of(Side::USSR, kArgentinaId) == 2);
    REQUIRE(next.influence_of(Side::USSR, kVenezuelaId) == 0);
    REQUIRE(gs.hands[to_index(Side::US)].test(12));
    REQUIRE(gs.hands[to_index(Side::US)].test(15));
}

TEST_CASE("Yuri and Samantha scores future USSR space attempts and clears at turn end", "[cards][game_loop]") {
    constexpr CardId kYuriSamantha = 106;
    constexpr CardId kSpaceCard = 1;

    PublicState pub;
    pub.space_attempts[to_index(Side::USSR)] = 2;
    pub.space_attempts[to_index(Side::US)] = 3;

    Pcg64Rng rng(0);
    const auto [after_yuri, event_over, event_winner] = apply_action(
        pub,
        ActionEncoding{.card_id = kYuriSamantha, .mode = ActionMode::Event, .targets = {}},
        Side::USSR,
        rng
    );

    REQUIRE_FALSE(event_over);
    REQUIRE_FALSE(event_winner.has_value());
    REQUIRE(after_yuri.vp == 0);
    REQUIRE(after_yuri.yuri_samantha_active);

    auto before_space = after_yuri;
    before_space.space[to_index(Side::USSR)] = 8;
    const auto [after_space, space_over, space_winner] = apply_action(
        before_space,
        ActionEncoding{.card_id = kSpaceCard, .mode = ActionMode::Space, .targets = {}},
        Side::USSR,
        rng
    );

    REQUIRE_FALSE(space_over);
    REQUIRE_FALSE(space_winner.has_value());
    REQUIRE(after_space.vp == -1);
    REQUIRE(after_space.space_attempts[to_index(Side::USSR)] == 3);

    GameState gs;
    gs.phase = GamePhase::Headline;
    gs.setup_influence_remaining = {0, 0};
    gs.pub.yuri_samantha_active = true;

    const PolicyFn no_action = [](const PublicState&, const CardSet&, bool, Pcg64Rng&)
        -> std::optional<ActionEncoding> {
        return std::nullopt;
    };

    Pcg64Rng loop_rng(1);
    (void)play_game_traced_from_state_ref_with_rng(
        gs,
        no_action,
        no_action,
        loop_rng,
        GameLoopConfig{.skip_setup_influence = true}
    );

    REQUIRE_FALSE(gs.pub.yuri_samantha_active);
}

TEST_CASE("We Will Bury You waits for the next US action round and UN can cancel it", "[cards][game_loop]") {
    constexpr CardId kWeWillBuryYou = 53;
    constexpr CardId kUnIntervention = 32;
    constexpr CardId kArabIsraeliWar = 13;

    auto make_state = [] {
        GameState gs;
        gs.pub = PublicState{};
        gs.pub.turn = 4;
        gs.pub.defcon = 5;
        gs.hands[to_index(Side::USSR)].set(kWeWillBuryYou);
        return gs;
    };

    const PolicyFn ussr_wwby = [](const PublicState&, const CardSet& hand, bool, Pcg64Rng&)
        -> std::optional<ActionEncoding> {
        if (hand.test(kWeWillBuryYou)) {
            return ActionEncoding{.card_id = kWeWillBuryYou, .mode = ActionMode::Event, .targets = {}};
        }
        return std::nullopt;
    };
    const PolicyFn no_us_action = [](const PublicState&, const CardSet&, bool, Pcg64Rng&)
        -> std::optional<ActionEncoding> {
        return std::nullopt;
    };

    auto awarded = make_state();
    Pcg64Rng award_rng(0);
    const auto award_result = run_action_rounds_live(awarded, ussr_wwby, no_us_action, award_rng, 1);

    REQUIRE_FALSE(award_result.has_value());
    REQUIRE(awarded.pub.defcon == 4);
    REQUIRE(awarded.pub.vp == 3);
    REQUIRE_FALSE(awarded.pub.we_will_bury_you_pending);
    REQUIRE(awarded.pub.we_will_bury_you_turn_ar == -1);

    auto canceled = make_state();
    canceled.hands[to_index(Side::US)].set(kUnIntervention);
    canceled.hands[to_index(Side::US)].set(kArabIsraeliWar);
    const PolicyFn us_un = [](const PublicState&, const CardSet& hand, bool, Pcg64Rng&)
        -> std::optional<ActionEncoding> {
        if (hand.test(kUnIntervention)) {
            return ActionEncoding{.card_id = kUnIntervention, .mode = ActionMode::Event, .targets = {}};
        }
        return std::nullopt;
    };

    Pcg64Rng cancel_rng(0);
    const auto cancel_result = run_action_rounds_live(canceled, ussr_wwby, us_un, cancel_rng, 1);

    REQUIRE_FALSE(cancel_result.has_value());
    REQUIRE(canceled.pub.defcon == 4);
    REQUIRE(canceled.pub.vp == 0);
    REQUIRE_FALSE(canceled.pub.we_will_bury_you_pending);
    REQUIRE(canceled.pub.we_will_bury_you_turn_ar == -1);
}

TEST_CASE("Lone Gunman lets USSR use this card for one operation", "[cards][game_loop]") {
    constexpr CardId kLoneGunman = 109;
    constexpr CardId kUsHeldCard = 13;
    constexpr CountryId kPoland = 12;

    GameState gs;
    gs.frame_stack_mode = true;
    gs.pub.set_influence(Side::USSR, kPoland, 1);
    gs.hands[to_index(Side::USSR)].set(kLoneGunman);
    gs.hands[to_index(Side::US)].set(kUsHeldCard);

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(
        gs,
        ActionEncoding{.card_id = kLoneGunman, .mode = ActionMode::Event, .targets = {}},
        Side::USSR,
        rng,
        nullptr,
        false,
        &gs.frame_stack
    );

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.influence_of(Side::USSR, kPoland) == 1);
    REQUIRE(gs.frame_stack.size() == 1);
    REQUIRE(gs.frame_stack.back().kind == FrameKind::DeferredOps);
    REQUIRE(gs.frame_stack.back().source_card == kLoneGunman);
    REQUIRE(gs.frame_stack.back().acting_side == Side::USSR);
    REQUIRE(gs.frame_stack.back().parent_card == kLoneGunman);

    const auto mode_step = engine_step_subframe(gs, FrameAction{.option_index = 0}, rng);
    REQUIRE(mode_step.pushed_subframe);
    REQUIRE(gs.frame_stack.size() == 1);
    REQUIRE(gs.frame_stack.back().kind == FrameKind::DeferredOps);
    REQUIRE(gs.frame_stack.back().eligible_countries.test(static_cast<size_t>(kPoland)));
    REQUIRE(gs.frame_stack.back().parent_card == kLoneGunman);

    const auto country_step = engine_step_subframe(gs, FrameAction{.country_id = kPoland}, rng);
    REQUIRE_FALSE(country_step.pushed_subframe);
    REQUIRE(gs.frame_stack.empty());
    REQUIRE(gs.pub.influence_of(Side::USSR, kPoland) == 2);
    REQUIRE(gs.hands[to_index(Side::US)].test(kUsHeldCard));
    REQUIRE(gs.pub.removed.test(kLoneGunman));
    REQUIRE_FALSE(gs.pub.discard.test(kLoneGunman));
}

TEST_CASE("Colonial Rear Guards adds US influence to four distinct Africa or Southeast Asia countries", "[cards][step]") {
    constexpr CardId kColonialRearGuards = 110;
    const std::array<CountryId, 4> picks = {57, 75, 79, 84};
    std::vector<CountryId> chosen;

    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
        REQUIRE(decision.kind == DecisionKind::CountrySelect);
        REQUIRE(decision.source_card == kColonialRearGuards);
        REQUIRE(decision.acting_side == Side::USSR);
        REQUIRE(chosen.size() < picks.size());
        const auto wanted = picks[chosen.size()];
        for (int idx = 0; idx < decision.n_options; ++idx) {
            const auto candidate = static_cast<CountryId>(decision.eligible_ids[idx]);
            const auto region = country_spec(candidate).region;
            REQUIRE((region == Region::Africa || region == Region::SoutheastAsia));
            REQUIRE(std::find(chosen.begin(), chosen.end(), candidate) == chosen.end());
            if (candidate == wanted) {
                chosen.push_back(candidate);
                return idx;
            }
        }
        FAIL("Colonial Rear Guards expected country was not eligible");
        return 0;
    };

    PublicState pub;
    const ActionEncoding action{.card_id = kColonialRearGuards, .mode = ActionMode::Event, .targets = {}};
    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action(pub, action, Side::USSR, rng, &policy_cb);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    const std::vector<CountryId> expected{picks.begin(), picks.end()};
    REQUIRE(chosen == expected);
    for (const auto cid : picks) {
        REQUIRE(next.influence_of(Side::US, cid) == 1);
    }
    REQUIRE(next.influence_of(Side::US, 45) == 0);
    REQUIRE(next.discard.test(kColonialRearGuards));
    REQUIRE_FALSE(next.removed.test(kColonialRearGuards));
}

TEST_CASE("Panama Canal Returned adds US influence to Panama Costa Rica and Venezuela", "[cards][step]") {
    constexpr CardId kPanamaCanalReturned = 111;
    constexpr CountryId kPanama = 44;
    constexpr CountryId kCostaRica = 45;
    constexpr CountryId kVenezuela = 55;

    PublicState pub;
    const auto panama_before = pub.influence_of(Side::US, kPanama);
    const auto costa_rica_before = pub.influence_of(Side::US, kCostaRica);
    const auto venezuela_before = pub.influence_of(Side::US, kVenezuela);

    const ActionEncoding action{.card_id = kPanamaCanalReturned, .mode = ActionMode::Event, .targets = {}};
    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action(pub, action, Side::US, rng);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.influence_of(Side::US, kPanama) == panama_before + 1);
    REQUIRE(next.influence_of(Side::US, kCostaRica) == costa_rica_before + 1);
    REQUIRE(next.influence_of(Side::US, kVenezuela) == venezuela_before + 1);
    REQUIRE(next.removed.test(kPanamaCanalReturned));
    REQUIRE_FALSE(next.discard.test(kPanamaCanalReturned));
}
