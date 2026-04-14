#include <algorithm>
#include <set>
#include <catch2/catch_test_macros.hpp>

#include "public_state.hpp"
#include "game_data.hpp"
#include "game_loop.hpp"
#include "hand_knowledge.hpp"
#include "legal_actions.hpp"
#include "rng.hpp"
#include "step.hpp"
#include "types.hpp"

using namespace ts;

// ---------------------------------------------------------------------------
// PublicState default-construction sanity checks.
//
// These tests verify that a default-constructed PublicState has the expected
// initial values as documented in public_state.hpp.  They are intentionally
// narrow: they do not test game logic, only that the struct initialises
// correctly and that constants in types.hpp are sane.
// ---------------------------------------------------------------------------

TEST_CASE("PublicState default construction has zero influence", "[public_state]") {
    PublicState s;
    for (int p = 0; p < 2; ++p) {
        for (int c = 0; c < MAX_COUNTRIES; ++c) {
            REQUIRE(s.influence[p][c] == 0);
        }
    }
}

TEST_CASE("PublicState default construction has zero milops and space", "[public_state]") {
    PublicState s;
    REQUIRE(s.milops[0] == 0);
    REQUIRE(s.milops[1] == 0);
    REQUIRE(s.space[0] == 0);
    REQUIRE(s.space[1] == 0);
}

TEST_CASE("PublicState default construction has correct scalar defaults", "[public_state]") {
    PublicState s;
    REQUIRE(s.vp     == 0);
    REQUIRE(s.defcon == 5);
    REQUIRE(s.turn   == 0);
    REQUIRE(s.ar     == 0);
    REQUIRE(s.phasing       == Side::USSR);
    REQUIRE(s.china_held_by == Side::USSR);
    REQUIRE(s.china_playable == true);
}

TEST_CASE("PublicState default construction has empty card sets", "[public_state]") {
    PublicState s;
    REQUIRE(s.discard.none());
    REQUIRE(s.removed.none());
}

TEST_CASE("PublicState default construction has zero hash", "[public_state]") {
    PublicState s;
    REQUIRE(s.state_hash == 0);
}

// ---------------------------------------------------------------------------
// HandKnowledge default-construction sanity checks.
// ---------------------------------------------------------------------------

TEST_CASE("HandKnowledge default construction has empty bitsets", "[hand_knowledge]") {
    HandKnowledge hk;
    REQUIRE(hk.known_in_hand.none());
    REQUIRE(hk.known_not_in_hand.none());
    REQUIRE(hk.possible_hidden.none());
}

TEST_CASE("HandKnowledge default construction has zero hand size", "[hand_knowledge]") {
    HandKnowledge hk;
    REQUIRE(hk.hand_size == 0);
    REQUIRE(hk.holds_china == false);
    REQUIRE(hk.observer == Side::Neutral);
}

// ---------------------------------------------------------------------------
// Constants sanity checks.
// ---------------------------------------------------------------------------

TEST_CASE("Hand size constants are correct per rules", "[types]") {
    // Competitive / ITS rules: 8 cards turns 1-3, 9 cards turns 4-10.
    REQUIRE(HAND_SIZE_EARLY == 8);
    REQUIRE(HAND_SIZE_LATE  == 9);
}

TEST_CASE("CHINA_CARD constant is a valid CardId value", "[types]") {
    // The exact value is a placeholder but must fit in uint8_t and be non-zero.
    REQUIRE(CHINA_CARD > 0);
    REQUIRE(CHINA_CARD < MAX_CARDS);
}

TEST_CASE("MAX_CARDS and MAX_COUNTRIES are large enough", "[types]") {
    // TS has 110 cards and ~68 countries; our arrays must accommodate them.
    REQUIRE(MAX_CARDS     >= 110);
    REQUIRE(MAX_COUNTRIES >= 68);
}

TEST_CASE("HLSTW event never sets DEFCON to 1", "[step]") {
    PublicState pub;
    pub.defcon = 5;

    const ActionEncoding action{
        .card_id = 49,
        .mode = ActionMode::Event,
        .targets = {},
    };

    for (uint64_t seed = 0; seed < 64; ++seed) {
        Pcg64Rng rng(seed);
        const auto [next, force_game_over, forced_winner] = apply_action(pub, action, Side::USSR, rng);

        REQUIRE_FALSE(force_game_over);
        REQUIRE_FALSE(forced_winner.has_value());
        REQUIRE(next.defcon >= 2);
        REQUIRE(next.defcon <= 5);
        REQUIRE(next.milops[to_index(Side::USSR)] == 5);
    }
}

TEST_CASE("Vietnam Revolts does not add a global ops modifier", "[step][legal_actions]") {
    PublicState pub;
    Pcg64Rng rng(0);

    const ActionEncoding event{
        .card_id = 9,
        .mode = ActionMode::Event,
        .targets = {},
    };

    const auto [next, over, winner] = apply_action(pub, event, Side::USSR, rng);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.vietnam_revolts_active);
    REQUIRE(next.ops_modifier[to_index(Side::USSR)] == 0);
    REQUIRE(effective_ops(7, next, Side::USSR) == card_spec(7).ops);
}

TEST_CASE("Vietnam Revolts adds one coup op only in Southeast Asia", "[step]") {
    constexpr CountryId kVietnamId = 80;

    PublicState base;
    base.set_influence(Side::US, kVietnamId, 5);

    PublicState bonus = base;
    bonus.vietnam_revolts_active = true;

    const ActionEncoding coup{
        .card_id = 7,
        .mode = ActionMode::Coup,
        .targets = {kVietnamId},
    };

    Pcg64Rng base_rng(11);
    Pcg64Rng bonus_rng(11);
    const auto [without_bonus, _, __] = apply_action(base, coup, Side::USSR, base_rng);
    const auto [with_bonus, ___, ____] = apply_action(bonus, coup, Side::USSR, bonus_rng);

    REQUIRE(with_bonus.influence_of(Side::US, kVietnamId) == without_bonus.influence_of(Side::US, kVietnamId) - 1);
    REQUIRE(with_bonus.milops[to_index(Side::USSR)] == without_bonus.milops[to_index(Side::USSR)] + 1);
}

TEST_CASE("Vietnam Revolts enumerates SEA-only influence actions with one extra op", "[legal_actions]") {
    constexpr CountryId kVietnamId = 80;

    PublicState pub;
    pub.vietnam_revolts_active = true;
    pub.set_influence(Side::USSR, kVietnamId, 1);

    CardSet hand;
    hand.set(7);

    const auto actions = enumerate_actions(hand, pub, Side::USSR, false);
    const auto found = std::any_of(actions.begin(), actions.end(), [](const ActionEncoding& action) {
        return action.card_id == 7 &&
            action.mode == ActionMode::Influence &&
            action.targets.size() == static_cast<size_t>(card_spec(7).ops + 1) &&
            std::all_of(action.targets.begin(), action.targets.end(), [](CountryId cid) {
                return country_spec(cid).region == Region::SoutheastAsia;
            });
    });

    REQUIRE(found);
}

TEST_CASE("Cuban Missile Crisis keeps coup mode legal", "[legal_actions]") {
    constexpr CountryId kAngolaId = 67;

    PublicState pub;
    pub.defcon = 3;
    pub.cuban_missile_crisis_active = true;
    pub.set_influence(Side::USSR, kAngolaId, 1);

    const auto modes = legal_modes(7, pub, Side::USSR);

    REQUIRE(std::find(modes.begin(), modes.end(), ActionMode::Coup) != modes.end());
}

TEST_CASE("Cuban Missile Crisis battleground coup loses immediately", "[step]") {
    constexpr CountryId kThailandId = 79;

    PublicState pub;
    pub.cuban_missile_crisis_active = true;
    pub.defcon = 3;
    pub.set_influence(Side::US, kThailandId, 2);

    const ActionEncoding coup{
        .card_id = 7,
        .mode = ActionMode::Coup,
        .targets = {kThailandId},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action(pub, coup, Side::USSR, rng);

    REQUIRE(over);
    REQUIRE(winner == Side::US);
    REQUIRE(next.defcon == 1);
}

TEST_CASE("Glasnost with SALT grants four free ops", "[step]") {
    PublicState pub;
    pub.salt_active = true;

    const ActionEncoding event{
        .card_id = 93,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action(pub, event, Side::USSR, rng);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.glasnost_free_ops == 4);
}

TEST_CASE("Resolving Glasnost free ops clears the pending budget", "[game_loop]") {
    constexpr CountryId kVietnamId = 80;

    PublicState pub;
    pub.glasnost_free_ops = 4;
    pub.set_influence(Side::USSR, kVietnamId, 1);

    Pcg64Rng rng(0);
    resolve_glasnost_free_ops_live(pub, rng);

    REQUIRE(pub.glasnost_free_ops == 0);
}

TEST_CASE("Glasnost free ops routes influence targets through the policy callback", "[game_loop]") {
    constexpr CardId kGlasnostId = 93;

    PublicState pub;
    pub.glasnost_free_ops = 2;

    std::array<int, kCountrySlots> expected_counts = {};
    int country_select_calls = 0;
    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
        if (decision.kind == DecisionKind::SmallChoice) {
            return 0;  // Influence
        }
        if (decision.kind == DecisionKind::CountrySelect) {
            REQUIRE(decision.source_card == kGlasnostId);
            REQUIRE(decision.n_options > 1);
            const auto choice = decision.n_options - 1;
            ++expected_counts[decision.eligible_ids[choice]];
            ++country_select_calls;
            return choice;
        }
        return 0;
    };

    Pcg64Rng rng(0);
    resolve_glasnost_free_ops_live(pub, rng, &policy_cb);

    REQUIRE(pub.glasnost_free_ops == 0);
    REQUIRE(country_select_calls == 2);
    for (CountryId cid = 0; cid < kCountrySlots; ++cid) {
        REQUIRE(pub.influence_of(Side::USSR, cid) == expected_counts[cid]);
    }
}

TEST_CASE("Missile Envy free ops keeps the event card as the country-select context", "[game_loop]") {
    constexpr CardId kMissileEnvyId = 52;
    constexpr CardId kArabIsraeliWarId = 13;

    GameState gs;
    gs.pub = PublicState{};
    gs.hands[to_index(Side::USSR)].set(kArabIsraeliWarId);

    std::array<int, kCountrySlots> expected_counts = {};
    int country_select_calls = 0;
    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
        if (decision.kind == DecisionKind::SmallChoice) {
            return 0;  // Influence
        }
        if (decision.kind == DecisionKind::CountrySelect) {
            REQUIRE(decision.source_card == kMissileEnvyId);
            REQUIRE(decision.n_options > 1);
            const auto choice = decision.n_options - 1;
            ++expected_counts[decision.eligible_ids[choice]];
            ++country_select_calls;
            return choice;
        }
        return 0;
    };

    const ActionEncoding action{
        .card_id = kMissileEnvyId,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(gs, action, Side::US, rng, &policy_cb);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(country_select_calls == effective_ops(kArabIsraeliWarId, gs.pub, Side::US));
    for (CountryId cid = 0; cid < kCountrySlots; ++cid) {
        REQUIRE(next.influence_of(Side::US, cid) == expected_counts[cid]);
    }
    REQUIRE(gs.hands[to_index(Side::USSR)].test(kArabIsraeliWarId));
}

TEST_CASE("Opponent-card ops resolve before event with Influence mode (ops-first default)", "[game_loop]") {
    // Duck and Cover (card 4, US) played by USSR for Influence: ops-first is the default.
    // At DEFCON 2, Duck and Cover drops DEFCON to 1 → game over (US wins).
    // With ops-first: France gains +1 influence BEFORE the event fires.
    constexpr CardId kDuckAndCoverId = 4;
    constexpr CountryId kFranceId = 7;

    GameState gs;
    gs.pub = PublicState{};
    gs.pub.defcon = 2;

    int ordering_calls = 0;
    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision&) {
        ++ordering_calls;
        return 0;
    };

    const ActionEncoding action{
        .card_id = kDuckAndCoverId,
        .mode = ActionMode::Influence,  // ops first — no callback needed
        .targets = {kFranceId},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(gs, action, Side::USSR, rng, &policy_cb);

    REQUIRE(over);
    REQUIRE(winner == Side::US);
    REQUIRE(ordering_calls == 0);  // ordering is encoded in the action, no callback
    REQUIRE(next.influence_of(Side::USSR, kFranceId) == 1);  // ops placed before event
    REQUIRE(next.defcon == 1);
    REQUIRE(next.discard.test(kDuckAndCoverId));
}

TEST_CASE("Opponent-card event fires before ops with EventFirst mode", "[game_loop]") {
    // Same setup, but EventFirst: event fires before influence ops.
    // Duck and Cover drops DEFCON 2→1 → game ends immediately, ops never execute.
    constexpr CardId kDuckAndCoverId = 4;
    constexpr CountryId kFranceId = 7;

    GameState gs;
    gs.pub = PublicState{};
    gs.pub.defcon = 2;

    int ordering_calls = 0;
    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision&) {
        ++ordering_calls;
        return 0;
    };

    const ActionEncoding action{
        .card_id = kDuckAndCoverId,
        .mode = ActionMode::EventFirst,  // event fires first — no callback needed
        .targets = {kFranceId},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(gs, action, Side::USSR, rng, &policy_cb);

    REQUIRE(over);
    REQUIRE(winner == Side::US);
    REQUIRE(ordering_calls == 0);  // ordering encoded in action
    REQUIRE(next.influence_of(Side::USSR, kFranceId) == 0);  // ops never ran (game ended first)
    REQUIRE(next.defcon == 1);
}

// ---------------------------------------------------------------------------
// GAP-005b: 2-ops enemy-control surcharge in enumerate_actions (Influence mode)
//
// When placing influence in an opponent-controlled country, each influence
// point costs 2 ops instead of 1.
//
// Setup: USSR has 1 influence in East Germany (id=4).
//        US has 3 influence in Poland (id=12, stability=3) — US controls Poland.
//        Card 20 (Olympic Games, Neutral, 2 ops) played for Influence.
//
// With 2 ops:
//   {EastGermany, EastGermany} — costs 1+1=2 ✓  (2 placements in non-controlled)
//   {Poland}                   — costs 2   ✓  (1 placement in US-controlled)
//   {Poland, EastGermany}      — costs 2+1=3 ✗ (must NOT appear)
//   {Poland, Poland}           — costs 2+2=4 ✗ (must NOT appear)
// ---------------------------------------------------------------------------

TEST_CASE("enumerate_actions Influence respects 2-ops enemy-control surcharge", "[legal_actions][gap005b]") {
    // East Germany = 4, Poland = 12, card 20 (Olympic Games, 2 ops, Neutral)
    constexpr CountryId kEastGermany = static_cast<CountryId>(4);
    constexpr CountryId kPoland = static_cast<CountryId>(12);
    constexpr CardId kOlympicGames = static_cast<CardId>(20);

    PublicState pub;
    pub.set_influence(Side::USSR, kEastGermany, 1);  // USSR can reach Poland (1-hop)
    pub.set_influence(Side::US, kPoland, 3);          // US controls Poland (stability 3, USSR 0)

    CardSet hand;
    hand.set(static_cast<int>(kOlympicGames));

    const auto actions = enumerate_actions(hand, pub, Side::USSR, false);

    // Filter to Influence actions for card 20.
    bool found_poland_only = false;
    bool found_eg_eg = false;
    bool found_invalid_poland_eg = false;
    bool found_invalid_poland_poland = false;

    for (const auto& action : actions) {
        if (action.card_id != kOlympicGames || action.mode != ActionMode::Influence) continue;
        const auto& t = action.targets;
        auto count = [&](CountryId cid) {
            return static_cast<int>(std::count(t.begin(), t.end(), cid));
        };
        if (t.size() == 1 && t[0] == kPoland) found_poland_only = true;
        if (t.size() == 2 && count(kEastGermany) == 2) found_eg_eg = true;
        if (count(kPoland) == 1 && count(kEastGermany) == 1) found_invalid_poland_eg = true;
        if (count(kPoland) == 2) found_invalid_poland_poland = true;
    }

    REQUIRE(found_poland_only);             // 1 influence in US-controlled costs 2 ops — valid
    REQUIRE(found_eg_eg);                   // 2 placements in non-controlled — valid
    REQUIRE_FALSE(found_invalid_poland_eg);    // would cost 3 ops — invalid
    REQUIRE_FALSE(found_invalid_poland_poland); // would cost 4 ops — invalid
}

// ---------------------------------------------------------------------------
// EventFirst mode: legal when playing an opponent's card and Influence is legal.
// ---------------------------------------------------------------------------

TEST_CASE("legal_modes includes EventFirst for opponent cards when Influence is legal", "[legal_actions][event_first]") {
    // USSR has influence in Poland (reachable countries exist) and plays a US card.
    // Card 2 = Europe Scoring (US, scoring card — no ops, so Influence not legal from it).
    // Use card 11 (Korean War, USSR, 2 ops) — opponent for US side.
    // Use card 28 (NATO, US, 4 ops) — opponent for USSR side.
    constexpr CardId kNatoCard = static_cast<CardId>(21);  // NATO is card 21 (US)

    PublicState pub;
    pub.set_influence(Side::USSR, static_cast<CountryId>(12), 1);  // Poland

    const auto modes = legal_modes(kNatoCard, pub, Side::USSR);

    const bool has_influence = std::find(modes.begin(), modes.end(), ActionMode::Influence) != modes.end();
    const bool has_event_first = std::find(modes.begin(), modes.end(), ActionMode::EventFirst) != modes.end();
    REQUIRE(has_influence);
    REQUIRE(has_event_first);
}

TEST_CASE("legal_modes excludes EventFirst for own cards", "[legal_actions][event_first]") {
    // Card 8 (Fidel) is a USSR card — EventFirst should NOT appear when USSR plays it.
    constexpr CardId kFidalCard = static_cast<CardId>(8);  // Fidel, USSR

    PublicState pub;
    pub.set_influence(Side::USSR, static_cast<CountryId>(36), 1);  // Cuba (USSR anchor neighbor)

    const auto modes = legal_modes(kFidalCard, pub, Side::USSR);

    const bool has_event_first = std::find(modes.begin(), modes.end(), ActionMode::EventFirst) != modes.end();
    REQUIRE_FALSE(has_event_first);
}

TEST_CASE("EventFirst targets match Influence accessible countries", "[legal_actions][event_first]") {
    // enumerate_actions for an opponent card should produce EventFirst actions
    // with the same accessible countries as Influence actions.
    constexpr CardId kNatoCard = static_cast<CardId>(21);  // NATO, US card

    PublicState pub;
    pub.set_influence(Side::USSR, static_cast<CountryId>(12), 1);  // Poland

    CardSet hand;
    hand.set(static_cast<int>(kNatoCard));

    const auto actions = enumerate_actions(hand, pub, Side::USSR, false);

    std::set<std::vector<CountryId>> influence_targets, event_first_targets;
    for (const auto& a : actions) {
        if (a.card_id != kNatoCard) continue;
        if (a.mode == ActionMode::Influence) influence_targets.insert(a.targets);
        if (a.mode == ActionMode::EventFirst) event_first_targets.insert(a.targets);
    }

    REQUIRE_FALSE(influence_targets.empty());
    REQUIRE(influence_targets == event_first_targets);  // same target sets, different ordering
}
