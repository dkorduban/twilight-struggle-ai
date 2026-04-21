#include <catch2/catch_test_macros.hpp>

#include "game_loop.hpp"
#include "rng.hpp"
#include "step.hpp"
#include "types.hpp"

using namespace ts;

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
