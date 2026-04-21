#include <algorithm>
#include <set>
#include <vector>
#include <catch2/catch_test_macros.hpp>

#include "public_state.hpp"
#include "game_data.hpp"
#include "game_loop.hpp"
#include "hand_knowledge.hpp"
#include "legal_actions.hpp"
#include "rng.hpp"
#include "scoring.hpp"
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

TEST_CASE("Vietnam Revolts extra influence op cannot be spent outside Southeast Asia", "[legal_actions]") {
    constexpr CountryId kVietnamId = 80;
    constexpr CountryId kPolandId = 12;
    constexpr CardId kSocialistGovernmentsId = 7;

    PublicState pub;
    pub.vietnam_revolts_active = true;
    pub.set_influence(Side::USSR, kVietnamId, 1);
    pub.set_influence(Side::USSR, kPolandId, 1);

    CardSet hand;
    hand.set(kSocialistGovernmentsId);

    const auto actions = enumerate_actions(hand, pub, Side::USSR, false);
    const auto leaked_bonus = std::any_of(actions.begin(), actions.end(), [](const ActionEncoding& action) {
        return action.card_id == kSocialistGovernmentsId &&
            action.mode == ActionMode::Influence &&
            action.targets.size() == static_cast<size_t>(card_spec(kSocialistGovernmentsId).ops + 1) &&
            std::any_of(action.targets.begin(), action.targets.end(), [](CountryId cid) {
                return country_spec(cid).region != Region::SoutheastAsia;
            });
    });

    REQUIRE_FALSE(leaked_bonus);
}

TEST_CASE("Space mode enforces the current track ops minimum", "[legal_actions]") {
    constexpr CardId kTwoOpsCard = 13;
    constexpr CardId kFourOpsCard = 23;

    PublicState pub;
    pub.space[to_index(Side::US)] = 2;

    const auto level_two_modes = legal_modes(kTwoOpsCard, pub, Side::US);
    REQUIRE(std::find(level_two_modes.begin(), level_two_modes.end(), ActionMode::Space) == level_two_modes.end());

    pub.space[to_index(Side::US)] = 6;

    const auto level_six_modes = legal_modes(kFourOpsCard, pub, Side::US);
    REQUIRE(std::find(level_six_modes.begin(), level_six_modes.end(), ActionMode::Space) == level_six_modes.end());
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

TEST_CASE("Realign legal countries exclude empty countries", "[legal_actions]") {
    constexpr CardId kOlympicGames = 20;
    constexpr CountryId kPoland = 12;
    constexpr CountryId kCanada = 2;

    PublicState pub;
    pub.defcon = 5;
    pub.set_influence(Side::US, kPoland, 1);

    const auto countries = legal_countries(kOlympicGames, ActionMode::Realign, pub, Side::USSR);

    REQUIRE(std::find(countries.begin(), countries.end(), kPoland) != countries.end());
    REQUIRE(std::find(countries.begin(), countries.end(), kCanada) == countries.end());
}

TEST_CASE("opponent ops remove starred card after its event fires", "[game_loop]") {
    constexpr CardId kUsJapanPactCard = 27;
    constexpr CountryId kPoland = 12;
    constexpr CountryId kJapan = 22;

    GameState gs;
    gs.pub = PublicState{};
    gs.pub.defcon = 5;

    const ActionEncoding action{
        .card_id = kUsJapanPactCard,
        .mode = ActionMode::Influence,
        .targets = {kPoland, kPoland, kPoland, kPoland},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(gs, action, Side::USSR, rng);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.influence_of(Side::US, kJapan) == 4);
    REQUIRE(next.removed.test(kUsJapanPactCard));
    REQUIRE_FALSE(next.discard.test(kUsJapanPactCard));
}

TEST_CASE("illegal headline events fizzle without executing", "[game_loop]") {
    constexpr CardId kNatoCard = 21;
    constexpr CardId kWargamesCard = 103;

    {
        GameState gs;
        gs.pub = PublicState{};
        gs.pub.turn = 1;
        gs.pub.defcon = 5;
        gs.hands[to_index(Side::US)].set(kNatoCard);

        const PolicyFn no_headline = [](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
            return std::nullopt;
        };
        const PolicyFn nato_headline = [](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
            return ActionEncoding{.card_id = kNatoCard, .mode = ActionMode::Event, .targets = {}};
        };

        Pcg64Rng rng(0);
        const auto result = run_headline_phase_live(gs, no_headline, nato_headline, rng);

        REQUIRE_FALSE(result.has_value());
        REQUIRE_FALSE(gs.pub.nato_active);
        REQUIRE(gs.pub.discard.test(kNatoCard));
        REQUIRE_FALSE(gs.pub.removed.test(kNatoCard));
    }

    {
        GameState gs;
        gs.pub = PublicState{};
        gs.pub.turn = 1;
        gs.pub.defcon = 3;
        gs.pub.vp = 10;
        gs.hands[to_index(Side::USSR)].set(kWargamesCard);

        const PolicyFn wargames_headline = [](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
            return ActionEncoding{.card_id = kWargamesCard, .mode = ActionMode::Event, .targets = {}};
        };
        const PolicyFn no_headline = [](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
            return std::nullopt;
        };

        Pcg64Rng rng(0);
        const auto result = run_headline_phase_live(gs, wargames_headline, no_headline, rng);

        REQUIRE_FALSE(result.has_value());
        REQUIRE(gs.pub.vp == 10);
        REQUIRE(gs.pub.discard.test(kWargamesCard));
        REQUIRE_FALSE(gs.pub.removed.test(kWargamesCard));
    }
}

TEST_CASE("Wargames played for ops reports VP threshold", "[game_loop]") {
    constexpr CardId kWargamesCard = 103;
    constexpr CountryId kPoland = 12;

    GameState gs;
    gs.phase = GamePhase::ActionRound;
    gs.pub = PublicState{};
    gs.pub.turn = 8;
    gs.pub.ar = 1;
    gs.pub.defcon = 4;
    gs.pub.vp = 20;
    gs.pub.set_influence(Side::USSR, kPoland, 1);
    gs.hands[to_index(Side::USSR)].set(kWargamesCard);

    const PolicyFn wargames_ops = [](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
        return ActionEncoding{
            .card_id = kWargamesCard,
            .mode = ActionMode::Influence,
            .targets = {kPoland, kPoland, kPoland, kPoland},
        };
    };
    const PolicyFn no_action = [](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
        return std::nullopt;
    };

    Pcg64Rng rng(0);
    const auto result = run_action_rounds_live(gs, wargames_ops, no_action, rng, 1);

    REQUIRE(result.has_value());
    REQUIRE(result->end_reason == "vp_threshold");
}

TEST_CASE("Nuclear Subs expires before next-turn battleground coup", "[game_loop]") {
    constexpr CardId kUssrCoupCard = 34;
    constexpr CardId kUsCoupCard = 38;
    constexpr CountryId kAngola = 57;
    constexpr CountryId kPanama = 44;

    GameState gs;
    gs.phase = GamePhase::Headline;
    gs.setup_influence_remaining = {0, 0};
    gs.pub = PublicState{};
    gs.pub.turn = 6;
    gs.pub.defcon = 2;
    gs.pub.nuclear_subs_active = true;
    gs.pub.set_influence(Side::US, kAngola, 1);
    gs.pub.set_influence(Side::USSR, kPanama, 1);
    gs.deck = std::vector<CardId>{
        kUsCoupCard, 4, 7, 8, 9, 10, 12, 14, 15,
        kUssrCoupCard, 16, 18, 19, 21, 22, 23, 24, 25,
    };

    const PolicyFn ussr_policy = [](const PublicState& pub, const CardSet& hand, bool, Pcg64Rng&) {
        if (pub.turn == 7 && pub.ar == 1 && hand.test(kUssrCoupCard)) {
            return ActionEncoding{.card_id = kUssrCoupCard, .mode = ActionMode::Coup, .targets = {kAngola}};
        }
        return std::optional<ActionEncoding>{};
    };
    const PolicyFn us_policy = [](const PublicState& pub, const CardSet& hand, bool, Pcg64Rng&) {
        if (pub.turn == 7 && pub.ar == 1 && hand.test(kUsCoupCard)) {
            return ActionEncoding{.card_id = kUsCoupCard, .mode = ActionMode::Coup, .targets = {kPanama}};
        }
        return std::optional<ActionEncoding>{};
    };

    const auto result = play_game_from_mid_state_fn(gs, ussr_policy, us_policy, 0);

    REQUIRE(result.end_turn == 7);
    REQUIRE(result.end_reason == "defcon1");
    REQUIRE(result.winner == Side::USSR);
}

TEST_CASE("NORAD cancels when US does not control Canada", "[game_loop]") {
    constexpr CountryId kCanada = 2;
    constexpr CountryId kMexico = 42;

    GameState gs;
    gs.pub = PublicState{};
    gs.pub.defcon = 2;
    gs.pub.norad_active = true;
    gs.pub.set_influence(Side::US, kCanada, 1);
    gs.pub.set_influence(Side::US, kMexico, 1);

    Pcg64Rng rng(0);
    const auto result = resolve_norad_live(gs, rng);

    REQUIRE_FALSE(result.has_value());
    REQUIRE_FALSE(gs.pub.norad_active);
    REQUIRE(gs.pub.influence_of(Side::US, kMexico) == 1);
}

TEST_CASE("Bear Trap headline forces USSR discard before AR action", "[game_loop]") {
    constexpr CardId kBearTrap = 47;
    constexpr CardId kForcedDiscard = 34;
    constexpr CountryId kAngola = 57;

    GameState gs;
    gs.phase = GamePhase::Headline;
    gs.pub = PublicState{};
    gs.pub.turn = 4;
    gs.pub.defcon = 5;
    gs.pub.set_influence(Side::US, kAngola, 1);
    gs.hands[to_index(Side::US)].set(kBearTrap);

    const PolicyFn no_headline = [](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
        return std::nullopt;
    };
    const PolicyFn bear_trap_headline = [](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
        return ActionEncoding{.card_id = kBearTrap, .mode = ActionMode::Event, .targets = {}};
    };

    Pcg64Rng rng(0);
    const auto headline_result = run_headline_phase_live(gs, no_headline, bear_trap_headline, rng);
    REQUIRE_FALSE(headline_result.has_value());
    REQUIRE(gs.pub.bear_trap_active);

    bool policy_called = false;
    gs.hands[to_index(Side::USSR)].set(kForcedDiscard);
    const PolicyFn trapped_ussr_policy = [&](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
        policy_called = true;
        return ActionEncoding{.card_id = kForcedDiscard, .mode = ActionMode::Coup, .targets = {kAngola}};
    };

    const auto ar_result = run_action_rounds_live(gs, trapped_ussr_policy, no_headline, rng, 1);

    REQUIRE_FALSE(ar_result.has_value());
    REQUIRE_FALSE(policy_called);
    REQUIRE_FALSE(gs.hands[to_index(Side::USSR)].test(kForcedDiscard));
    REQUIRE(gs.pub.discard.test(kForcedDiscard));
    REQUIRE(gs.pub.influence_of(Side::US, kAngola) == 1);
    REQUIRE(gs.pub.milops[to_index(Side::USSR)] == 0);
}

TEST_CASE("final scoring includes Southeast Asia", "[scoring]") {
    constexpr CountryId kThailand = 79;

    PublicState base;
    auto with_thailand = base;
    with_thailand.set_influence(Side::USSR, kThailand, 2);

    const auto base_score = apply_final_scoring(base);
    const auto thailand_score = apply_final_scoring(with_thailand);

    REQUIRE_FALSE(base_score.game_over);
    REQUIRE_FALSE(thailand_score.game_over);
    REQUIRE(thailand_score.vp_delta - base_score.vp_delta == 2);
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

TEST_CASE("Cuban Missile Crisis can be cancelled by discarding a 3-op card", "[game_loop]") {
    constexpr CardId kDuckAndCoverId = 4;

    GameState gs;
    gs.pub = PublicState{};
    gs.pub.cuban_missile_crisis_active = true;
    gs.hands[to_index(Side::US)].set(kDuckAndCoverId);

    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
        if (decision.kind == DecisionKind::SmallChoice) {
            REQUIRE(decision.source_card == static_cast<CardId>(43));
            REQUIRE(decision.n_options == 2);
            return 1;  // Cancel CMC.
        }
        if (decision.kind == DecisionKind::CardSelect) {
            REQUIRE(decision.source_card == static_cast<CardId>(43));
            REQUIRE(decision.n_options == 1);
            REQUIRE(decision.eligible_ids[0] == static_cast<int>(kDuckAndCoverId));
            return 0;
        }
        return 0;
    };

    Pcg64Rng rng(0);
    const auto result = resolve_cuban_missile_crisis_cancel_live(gs, Side::US, rng, &policy_cb);

    REQUIRE(result.has_value());
    REQUIRE_FALSE(gs.pub.cuban_missile_crisis_active);
    REQUIRE_FALSE(gs.hands[to_index(Side::US)].test(kDuckAndCoverId));
    REQUIRE(gs.pub.discard.test(kDuckAndCoverId));
}

TEST_CASE("Extra action rounds resolve Cuban Missile Crisis cancellation before actions", "[game_loop]") {
    constexpr CardId kDuckAndCoverId = 4;

    const PolicyFn no_action_policy = [](const PublicState&, const CardSet&, bool, Pcg64Rng&) {
        return std::nullopt;
    };

    bool cancelled = false;
    for (uint64_t seed = 0; seed < 64; ++seed) {
        GameState gs;
        gs.pub = PublicState{};
        gs.pub.turn = 1;
        gs.pub.ar = ars_for_turn(gs.pub.turn);
        gs.pub.cuban_missile_crisis_active = true;
        gs.hands[to_index(Side::US)].set(kDuckAndCoverId);

        Pcg64Rng rng(seed);
        const auto result = run_extra_action_round_live(gs, Side::US, no_action_policy, rng);
        REQUIRE_FALSE(result.has_value());

        if (!gs.pub.cuban_missile_crisis_active) {
            cancelled = true;
            REQUIRE_FALSE(gs.hands[to_index(Side::US)].test(kDuckAndCoverId));
            REQUIRE(gs.pub.discard.test(kDuckAndCoverId));
            break;
        }

        REQUIRE(gs.hands[to_index(Side::US)].test(kDuckAndCoverId));
        REQUIRE_FALSE(gs.pub.discard.test(kDuckAndCoverId));
    }

    REQUIRE(cancelled);
}

TEST_CASE("China Card is never a legal headline choice", "[legal_actions]") {
    constexpr CardId kDeStalinizationId = 28;

    CardSet hand;
    hand.set(kChinaCardId);
    hand.set(kDeStalinizationId);

    PublicState pub;
    pub.ar = 0;

    const auto cards = legal_cards(hand, pub, Side::USSR, /*holds_china=*/true);

    REQUIRE(std::find(cards.begin(), cards.end(), kChinaCardId) == cards.end());
    REQUIRE(std::find(cards.begin(), cards.end(), kDeStalinizationId) != cards.end());
}

TEST_CASE("Formosan Resolution counts Taiwan as a battleground for USSR scoring too", "[scoring]") {
    PublicState pub;
    pub.influence[to_index(Side::USSR)][kTaiwanId] = 3;

    const auto without_formosan = score_region(Region::Asia, pub);

    pub.formosan_active = true;
    const auto with_formosan = score_region(Region::Asia, pub);

    REQUIRE(with_formosan.vp_delta > without_formosan.vp_delta);
}

TEST_CASE("Solidarity event is illegal before John Paul II is played", "[legal_actions]") {
    const auto modes_before = legal_modes(104, PublicState{}, Side::US);
    REQUIRE(std::find(modes_before.begin(), modes_before.end(), ActionMode::Event) == modes_before.end());

    PublicState pub;
    pub.john_paul_ii_played = true;
    const auto modes_after = legal_modes(104, pub, Side::US);
    REQUIRE(std::find(modes_after.begin(), modes_after.end(), ActionMode::Event) != modes_after.end());
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

TEST_CASE("engine_step_toplevel records event sub-decision frames", "[game_loop][frame_stack]") {
    GameState gs;
    DecisionFrame stale;
    stale.source_card = 99;
    gs.frame_stack.push_back(stale);

    const ActionEncoding action{
        .card_id = 23,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto result = engine_step_toplevel(gs, action, Side::US, rng);

    REQUIRE(result.pushed_subframe);
    REQUIRE_FALSE(gs.frame_stack.empty());

    const auto& frame = gs.frame_stack.front();
    REQUIRE(frame.kind == FrameKind::CountryPick);
    REQUIRE(frame.source_card == 23);
    REQUIRE(frame.acting_side == Side::US);
    REQUIRE(frame.eligible_n > 0);
    REQUIRE(frame.eligible_countries.count() >= frame.eligible_n);
}

TEST_CASE("Glasnost free ops routes influence targets through the policy callback", "[game_loop]") {
    constexpr CardId kGlasnostId = 93;

    PublicState pub;
    pub.glasnost_free_ops = 2;
    pub.defcon = 3;

    std::array<int, kCountrySlots> expected_counts = {};
    int country_select_calls = 0;
    int small_choice_calls = 0;
    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
        if (decision.kind == DecisionKind::SmallChoice) {
            ++small_choice_calls;
            return 0;
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
    REQUIRE(small_choice_calls == 0);
    REQUIRE(pub.defcon == 3);
    REQUIRE(pub.milops[to_index(Side::USSR)] == 0);
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

TEST_CASE("Terrorism randomly discards without policy selection", "[game_loop]") {
    constexpr CardId kDuckAndCoverId = 4;
    constexpr CardId kSocialistGovernmentsId = 7;
    constexpr CardId kArabIsraeliWarId = 13;

    GameState gs;
    gs.pub = PublicState{};
    gs.pub.iran_hostage_crisis_active = true;
    gs.hands[to_index(Side::US)].set(kDuckAndCoverId);
    gs.hands[to_index(Side::US)].set(kSocialistGovernmentsId);
    gs.hands[to_index(Side::US)].set(kArabIsraeliWarId);

    int policy_calls = 0;
    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
        ++policy_calls;
        return decision.n_options - 1;
    };

    const ActionEncoding action{
        .card_id = 95,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(gs, action, Side::USSR, rng, &policy_cb);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(policy_calls == 0);
    REQUIRE(hand_count(gs.hands[to_index(Side::US)]) == 1);
    const auto discarded_originals =
        static_cast<int>(next.discard.test(kDuckAndCoverId)) +
        static_cast<int>(next.discard.test(kSocialistGovernmentsId)) +
        static_cast<int>(next.discard.test(kArabIsraeliWarId));
    REQUIRE(discarded_originals == 2);
}

TEST_CASE("Card 14 routes repeated country picks through the policy callback", "[step]") {
    PublicState pub;

    std::vector<CountryId> chosen_countries;
    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
        REQUIRE(decision.kind == DecisionKind::CountrySelect);
        REQUIRE(decision.source_card == static_cast<CardId>(14));
        REQUIRE(decision.acting_side == Side::USSR);
        REQUIRE(decision.n_options >= 4);
        const auto choice = decision.n_options - 1;
        chosen_countries.push_back(static_cast<CountryId>(decision.eligible_ids[choice]));
        return choice;
    };

    const ActionEncoding action{
        .card_id = 14,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action(pub, action, Side::USSR, rng, &policy_cb);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(chosen_countries == std::vector<CountryId>{83, 19, 13, 12});
    for (const auto cid : chosen_countries) {
        REQUIRE(next.influence_of(Side::USSR, cid) == 1);
    }
    REQUIRE(next.influence_of(Side::USSR, 3) == 0);
    REQUIRE(next.influence_of(Side::USSR, 5) == 0);
    REQUIRE(next.influence_of(Side::USSR, 9) == 0);
}

TEST_CASE("Pershing II routes repeated country removals through the policy callback", "[step]") {
    PublicState pub;
    for (const auto cid : std::array<CountryId, 12>{1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18}) {
        pub.set_influence(Side::US, cid, 1);
    }

    std::vector<CountryId> chosen_countries;
    PolicyCallbackFn policy_cb = [&](const PublicState&, const EventDecision& decision) {
        REQUIRE(decision.kind == DecisionKind::CountrySelect);
        REQUIRE(decision.source_card == static_cast<CardId>(102));
        REQUIRE(decision.acting_side == Side::USSR);
        REQUIRE(decision.n_options >= 3);
        const auto choice = decision.n_options - 1;
        chosen_countries.push_back(static_cast<CountryId>(decision.eligible_ids[choice]));
        return choice;
    };

    const ActionEncoding action{
        .card_id = 102,
        .mode = ActionMode::Event,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action(pub, action, Side::USSR, rng, &policy_cb);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.vp == 1);
    REQUIRE(chosen_countries == std::vector<CountryId>{18, 17, 16});
    for (const auto cid : chosen_countries) {
        REQUIRE(next.influence_of(Side::US, cid) == 0);
    }
    REQUIRE(next.influence_of(Side::US, 15) == 1);
    REQUIRE(next.influence_of(Side::US, 14) == 1);
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
        .mode = ActionMode::EventFirst,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(gs, action, Side::USSR, rng, &policy_cb);

    REQUIRE(over);
    REQUIRE(winner == Side::US);
    REQUIRE(ordering_calls == 0);  // event ended the game before deferred ops selection
    REQUIRE(next.influence_of(Side::USSR, kFranceId) == 0);  // ops never ran (game ended first)
    REQUIRE(next.defcon == 1);
}

TEST_CASE("Opponent-card space play never fires the opponent event", "[game_loop]") {
    constexpr CardId kDuckAndCoverId = 4;

    GameState gs;
    gs.pub = PublicState{};
    gs.pub.defcon = 2;

    const ActionEncoding action{
        .card_id = kDuckAndCoverId,
        .mode = ActionMode::Space,
        .targets = {},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(gs, action, Side::USSR, rng);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.defcon == 2);
    REQUIRE(next.discard.test(kDuckAndCoverId));
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

TEST_CASE("EventFirst actions defer country targets", "[legal_actions][event_first]") {
    constexpr CardId kNatoCard = static_cast<CardId>(21);  // NATO, US card
    constexpr CountryId kPolandId = static_cast<CountryId>(12);

    PublicState pub;
    pub.set_influence(Side::USSR, kPolandId, 1);  // Poland

    CardSet hand;
    hand.set(static_cast<int>(kNatoCard));

    const auto actions = enumerate_actions(hand, pub, Side::USSR, false);

    REQUIRE(legal_countries(kNatoCard, ActionMode::EventFirst, pub, Side::USSR).empty());

    int event_first_count = 0;
    for (const auto& a : actions) {
        if (a.card_id != kNatoCard) continue;
        if (a.mode == ActionMode::EventFirst) {
            REQUIRE(a.targets.empty());
            ++event_first_count;
        }
    }

    REQUIRE(event_first_count == 1);

    GameState gs;
    gs.pub = pub;
    const ActionEncoding action{
        .card_id = kNatoCard,
        .mode = ActionMode::EventFirst,
        .targets = {kPolandId, kPolandId, kPolandId, kPolandId},
    };

    Pcg64Rng rng(0);
    const auto [next, over, winner] = apply_action_live(gs, action, Side::USSR, rng);

    REQUIRE_FALSE(over);
    REQUIRE_FALSE(winner.has_value());
    REQUIRE(next.nato_active);
    REQUIRE(next.influence_of(Side::USSR, kPolandId) == 5);
}

namespace {

struct WarCardCase {
    CardId card_id;
    Side acting_side;
    Side attacker_side;
    CountryId target;
    bool uses_explicit_target = false;
    int card_ops = 0;
    int influence_on_success = 0;
};

constexpr std::array<WarCardCase, 5> kWarCardCases = {{
    {11, Side::USSR, Side::USSR, static_cast<CountryId>(25), false, 2, 2},
    {13, Side::USSR, Side::USSR, static_cast<CountryId>(30), false, 2, 2},
    {24, Side::USSR, Side::USSR, static_cast<CountryId>(24), true, 2, 2},
    {39, Side::USSR, Side::USSR, static_cast<CountryId>(28), true, 3, 3},
    {105, Side::US, Side::US, static_cast<CountryId>(29), true, 2, 2},
}};

ActionEncoding build_war_event_action(const WarCardCase& spec) {
    return ActionEncoding{
        .card_id = spec.card_id,
        .mode = ActionMode::Event,
        .targets = spec.uses_explicit_target ? std::vector<CountryId>{spec.target} : std::vector<CountryId>{},
    };
}

int war_success_vp_delta(const WarCardCase& spec) {
    const auto vp = spec.card_id == 39 ? 1 : 2;
    return spec.attacker_side == Side::USSR ? vp : -vp;
}

int war_failure_vp_delta(const WarCardCase& spec) {
    if (spec.card_id == 39) {
        return 0;
    }
    return spec.attacker_side == Side::USSR ? -1 : 1;
}

}  // namespace

TEST_CASE("War cards apply success effects and printed MilOps without DEFCON changes", "[step]") {
    for (const auto& spec : kWarCardCases) {
        PublicState pub;
        pub.defcon = 2;
        pub.set_influence(spec.attacker_side, spec.target, 1);
        pub.set_influence(other_side(spec.attacker_side), spec.target, 4);

        const auto action = build_war_event_action(spec);
        const auto threshold = spec.card_id == 39 ? 3 : 4;
        const auto success_possible = 6 >= threshold;
        bool found_success = false;
        for (uint64_t seed = 0; seed < 128; ++seed) {
            Pcg64Rng rng(seed);
            const auto [next, over, winner] = apply_action(pub, action, spec.acting_side, rng);
            const auto expected_vp = war_success_vp_delta(spec);
            if (next.vp != expected_vp) {
                continue;
            }

            REQUIRE_FALSE(over);
            REQUIRE_FALSE(winner.has_value());
            REQUIRE(next.defcon == pub.defcon);
            REQUIRE(next.milops[to_index(spec.attacker_side)] == spec.card_ops);
            REQUIRE(next.milops[to_index(other_side(spec.attacker_side))] ==
                pub.milops[to_index(other_side(spec.attacker_side))]);
            REQUIRE(next.influence_of(spec.attacker_side, spec.target) == 1 + spec.influence_on_success);
            REQUIRE(next.influence_of(other_side(spec.attacker_side), spec.target) == 0);
            found_success = true;
            break;
        }

        INFO("card_id=" << static_cast<int>(spec.card_id) << " success_possible=" << success_possible);
        REQUIRE(found_success == success_possible);
    }
}

TEST_CASE("War cards award opponent VP and leave board state unchanged on failure", "[step]") {
    for (const auto& spec : kWarCardCases) {
        PublicState pub;
        pub.defcon = 2;
        pub.set_influence(spec.attacker_side, spec.target, 1);
        pub.set_influence(other_side(spec.attacker_side), spec.target, 4);

        const auto action = build_war_event_action(spec);
        const auto threshold = spec.card_id == 39 ? 3 : 4;
        const auto failure_possible = 1 < threshold;
        bool found_failure = false;
        for (uint64_t seed = 0; seed < 128; ++seed) {
            Pcg64Rng rng(seed);
            const auto [next, over, winner] = apply_action(pub, action, spec.acting_side, rng);
            const auto expected_vp = war_failure_vp_delta(spec);
            if (next.vp != expected_vp) {
                continue;
            }

            REQUIRE_FALSE(over);
            REQUIRE_FALSE(winner.has_value());
            REQUIRE(next.defcon == pub.defcon);
            REQUIRE(next.milops[to_index(Side::USSR)] == pub.milops[to_index(Side::USSR)]);
            REQUIRE(next.milops[to_index(Side::US)] == pub.milops[to_index(Side::US)]);
            REQUIRE(next.influence_of(spec.attacker_side, spec.target) == pub.influence_of(spec.attacker_side, spec.target));
            REQUIRE(next.influence_of(other_side(spec.attacker_side), spec.target) ==
                pub.influence_of(other_side(spec.attacker_side), spec.target));
            found_failure = true;
            break;
        }

        INFO("card_id=" << static_cast<int>(spec.card_id) << " failure_possible=" << failure_possible);
        REQUIRE(found_failure == failure_possible);
    }
}

TEST_CASE("Brush War applies adjacent opponent-control roll modifiers", "[step]") {
    constexpr CountryId kAngolaId = static_cast<CountryId>(57);
    constexpr CountryId kBotswanaId = static_cast<CountryId>(58);
    constexpr CountryId kCongoZaireId = static_cast<CountryId>(60);

    PublicState base;
    base.defcon = 2;
    base.set_influence(Side::US, kAngolaId, 1);

    PublicState blocked = base;
    blocked.set_influence(Side::US, kBotswanaId, 2);
    blocked.set_influence(Side::US, kCongoZaireId, 2);

    const ActionEncoding action{
        .card_id = 39,
        .mode = ActionMode::Event,
        .targets = {kAngolaId},
    };

    bool found_modified_failure = false;
    for (uint64_t seed = 0; seed < 128; ++seed) {
        Pcg64Rng base_rng(seed);
        const auto [base_next, base_over, base_winner] = apply_action(base, action, Side::USSR, base_rng);
        if (base_next.vp != 1) {
            continue;
        }

        Pcg64Rng blocked_rng(seed);
        const auto [blocked_next, blocked_over, blocked_winner] = apply_action(blocked, action, Side::USSR, blocked_rng);
        if (blocked_next.vp != 0) {
            continue;
        }

        REQUIRE_FALSE(base_over);
        REQUIRE_FALSE(base_winner.has_value());
        REQUIRE_FALSE(blocked_over);
        REQUIRE_FALSE(blocked_winner.has_value());
        REQUIRE(base_next.milops[to_index(Side::USSR)] == 3);
        REQUIRE(blocked_next.milops[to_index(Side::USSR)] == 0);
        REQUIRE(base_next.influence_of(Side::US, kAngolaId) == 0);
        REQUIRE(blocked_next.influence_of(Side::US, kAngolaId) == base.influence_of(Side::US, kAngolaId));
        found_modified_failure = true;
        break;
    }

    REQUIRE(found_modified_failure);
}

TEST_CASE("War cards remain legal at DEFCON 2", "[legal_actions]") {
    PublicState pub;
    pub.defcon = 2;

    CardSet hand;
    for (const auto& spec : kWarCardCases) {
        hand.set(spec.card_id);
    }

    for (const auto side : {Side::USSR, Side::US}) {
        const auto cards = legal_cards(hand, pub, side, false);
        for (const auto& spec : kWarCardCases) {
            INFO("side=" << static_cast<int>(side) << " card_id=" << static_cast<int>(spec.card_id));
            REQUIRE(std::find(cards.begin(), cards.end(), spec.card_id) != cards.end());
        }
    }
}
