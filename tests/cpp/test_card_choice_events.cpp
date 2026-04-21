#include <array>

#include <catch2/catch_test_macros.hpp>

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
