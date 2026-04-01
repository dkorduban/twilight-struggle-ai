// Focused event-level regression checks for the native step/event layer.

#include <cstdlib>
#include <iostream>
#include <optional>
#include <random>
#include <string>

#include "step.hpp"

namespace {

using ts::ActionEncoding;
using ts::ActionMode;
using ts::CountryId;
using ts::PublicState;
using ts::Side;

[[noreturn]] void fail(const std::string& message) {
    std::cerr << "event parity smoke failed: " << message << '\n';
    std::exit(1);
}

void require(bool condition, const std::string& message) {
    if (!condition) {
        fail(message);
    }
}

PublicState apply_event(PublicState pub, ts::CardId card_id, Side side, uint32_t seed) {
    ts::Pcg64Rng rng(seed);
    const auto [next, over, winner] = ts::apply_action(
        pub,
        ActionEncoding{
            .card_id = card_id,
            .mode = ActionMode::Event,
            .targets = {},
        },
        side,
        rng
    );
    (void)over;
    (void)winner;
    return next;
}

std::tuple<PublicState, bool, std::optional<Side>> apply_event_result(PublicState pub, ts::CardId card_id, Side side, uint32_t seed) {
    ts::Pcg64Rng rng(seed);
    return ts::apply_action(
        pub,
        ActionEncoding{
            .card_id = card_id,
            .mode = ActionMode::Event,
            .targets = {},
        },
        side,
        rng
    );
}

void test_duck_and_cover() {
    PublicState pub;
    pub.defcon = 3;
    const auto next = apply_event(pub, 4, Side::US, 1U);
    require(next.defcon == 2, "Duck and Cover should lower DEFCON by 1");
    require(next.vp == -2, "Duck and Cover should award US (5-defcon) VP");
    require(next.discard.test(4), "Duck and Cover should be discarded");
}

void test_fidel() {
    PublicState pub;
    pub.set_influence(Side::US, 36, 3);
    const auto next = apply_event(pub, 8, Side::USSR, 14U);
    require(next.influence_of(Side::US, 36) == 0, "Fidel should remove all US influence from Cuba");
    require(ts::controls_country(Side::USSR, 36, next), "Fidel should give USSR control of Cuba");
}

void test_we_will_bury_you() {
    PublicState pub;
    pub.defcon = 4;
    const auto next = apply_event(pub, 53, Side::USSR, 2U);
    require(next.defcon == 3, "We Will Bury You should lower DEFCON by 1");
    require(next.vp == 3, "We Will Bury You should award 3 VP to USSR");
    require(next.removed.test(53), "We Will Bury You should be removed");
}

void test_kal_007() {
    PublicState pub;
    pub.defcon = 4;
    pub.china_held_by = Side::USSR;
    pub.china_playable = false;
    const auto next = apply_event(pub, 92, Side::US, 3U);
    require(next.defcon == 3, "KAL 007 should lower DEFCON by 1");
    require(next.vp == -2, "KAL 007 should award 2 VP to US");
    require(next.china_held_by == Side::US, "KAL 007 should pass China to US when USSR holds it");
    require(next.china_playable, "KAL 007 should make passed China immediately playable");
    require(next.removed.test(92), "KAL 007 should be removed");
}

void test_cuban_missile_crisis() {
    PublicState pub;
    pub.defcon = 5;
    const auto next = apply_event(pub, 43, Side::USSR, 4U);
    require(next.defcon == 2, "Cuban Missile Crisis should set DEFCON to 2");
    require(next.cuban_missile_crisis_active, "Cuban Missile Crisis should set its active flag");
}

void test_ops_and_flags_batch() {
    PublicState pub;
    auto next = apply_event(pub, 44, Side::US, 5U);
    require(next.nuclear_subs_active, "Nuclear Subs should enable the US battleground coup exemption");

    next = apply_event(pub, 46, Side::USSR, 6U);
    require(next.defcon == 5, "SALT Negotiations should clamp DEFCON upward at 5");
    require(next.salt_active, "SALT Negotiations should set the SALT flag");

    next = apply_event(pub, 54, Side::USSR, 7U);
    require(next.ops_modifier[ts::to_index(Side::USSR)] == 1, "Brezhnev Doctrine should add 1 USSR ops");

    next = apply_event(pub, 62, Side::USSR, 8U);
    require(next.flower_power_active, "Flower Power should set its active flag");

    next = apply_event(pub, 96, Side::USSR, 9U);
    require(next.ops_modifier[ts::to_index(Side::US)] == -1, "Iran-Contra Scandal should reduce US ops by 1");

    next = apply_event(pub, 97, Side::US, 10U);
    require(next.chernobyl_blocked_region.has_value(), "Chernobyl should choose a blocked region");
}

void test_truman_doctrine() {
    PublicState pub;
    pub.set_influence(Side::US, 7, 1);
    pub.set_influence(Side::USSR, 7, 1);
    const auto next = apply_event(pub, 19, Side::US, 11U);
    require(next.influence_of(Side::USSR, 7) == 0, "Truman Doctrine should remove USSR influence from an eligible Europe country");
    require(next.truman_doctrine_played, "Truman Doctrine should set the NATO prerequisite flag");
}

void test_captured_nazi_scientist() {
    PublicState pub;
    const auto next = apply_event(pub, 18, Side::US, 22U);
    require(next.space[ts::to_index(Side::US)] == 1, "Captured Nazi Scientist should advance the phasing side one space level");
    require(next.vp == -2, "Captured Nazi Scientist should award first-to-level VP to US");
}

void test_warsaw_pact() {
    PublicState pub;
    pub.set_influence(Side::US, 13, 2);
    const auto next = apply_event(pub, 16, Side::USSR, 15U);
    require(next.warsaw_pact_played, "Warsaw Pact should set the NATO prerequisite flag");
    const bool removed_us = next.influence_of(Side::US, 13) == 0;
    const bool added_ussr = next.influence_of(Side::USSR, 13) >= 1;
    require(removed_us || added_ussr, "Warsaw Pact should either remove US influence or add USSR influence in Eastern Bloc");
}

void test_us_japan_pact() {
    PublicState pub;
    pub.set_influence(Side::USSR, 22, 2);
    const auto next = apply_event(pub, 27, Side::US, 12U);
    require(next.us_japan_pact_active, "US/Japan Pact should set its ongoing protection flag");
    require(ts::controls_country(Side::US, 22, next), "US/Japan Pact should give the US control of Japan");
}

void test_nixon_and_hostage_crisis() {
    PublicState pub;
    pub.china_held_by = Side::USSR;
    pub.china_playable = true;
    auto next = apply_event(pub, 72, Side::US, 23U);
    require(next.vp == -2, "Nixon Plays the China Card should award 2 VP to US when taking China from USSR");
    require(next.china_held_by == Side::US, "Nixon Plays the China Card should transfer China to US");
    require(!next.china_playable, "Nixon Plays the China Card should take China face-down");

    pub = PublicState{};
    pub.set_influence(Side::US, 28, 2);
    next = apply_event(pub, 85, Side::USSR, 24U);
    require(next.influence_of(Side::US, 28) == 0, "Iranian Hostage Crisis should remove all US influence from Iran");
    require(next.influence_of(Side::USSR, 28) == 2, "Iranian Hostage Crisis should add 2 USSR influence to Iran");
    require(next.iran_hostage_crisis_active, "Iranian Hostage Crisis should set its ongoing flag");
}

void test_camp_david_accords() {
    PublicState pub;
    const auto next = apply_event(pub, 66, Side::US, 16U);
    require(next.vp == -1, "Camp David Accords should award 1 VP to US");
    require(next.influence_of(Side::US, 30) == 1, "Camp David Accords should add 1 US influence to Israel");
    require(next.influence_of(Side::US, 26) == 1, "Camp David Accords should add 1 US influence to Egypt");
    require(next.influence_of(Side::US, 31) == 1, "Camp David Accords should add 1 US influence to Jordan");
}

void test_opec_and_awacs() {
    PublicState pub;
    pub.set_influence(Side::USSR, 26, 1);
    pub.set_influence(Side::USSR, 34, 1);
    pub.set_influence(Side::USSR, 55, 1);
    auto next = apply_event(pub, 64, Side::USSR, 17U);
    require(next.vp == 3, "OPEC should score one VP per eligible USSR-held OPEC country");

    pub.awacs_active = true;
    next = apply_event(pub, 64, Side::USSR, 18U);
    require(next.vp == 2, "AWACS should exclude Saudi Arabia from OPEC scoring");

    pub = PublicState{};
    next = apply_event(pub, 107, Side::US, 19U);
    require(next.influence_of(Side::US, 34) == 2, "AWACS Sale should add 2 US influence to Saudi Arabia");
    require(next.awacs_active, "AWACS Sale should set the AWACS flag");
}

void test_iron_lady_and_yuri() {
    PublicState pub;
    pub.set_influence(Side::USSR, 17, 3);
    auto next = apply_event(pub, 86, Side::US, 20U);
    require(next.vp == -1, "Iron Lady should award 1 VP to US");
    require(next.influence_of(Side::USSR, 17) == 0, "Iron Lady should remove all USSR influence from UK");
    require(next.opec_cancelled, "Iron Lady should cancel OPEC");

    pub = PublicState{};
    pub.space_attempts[ts::to_index(Side::US)] = 2;
    next = apply_event(pub, 106, Side::USSR, 21U);
    require(next.vp == 2, "Yuri and Samantha should award USSR VP equal to US space attempts");
}

void test_flower_power_cancel() {
    PublicState pub;
    pub.flower_power_active = true;
    const auto next = apply_event(pub, 100, Side::US, 13U);
    require(next.vp == -1, "An Evil Empire should cost USSR 1 VP");
    require(next.flower_power_cancelled, "An Evil Empire should set the Flower Power cancelled flag");
    require(!next.flower_power_active, "An Evil Empire should deactivate Flower Power");
}

void test_wargames() {
    PublicState pub;
    pub.defcon = 2;
    pub.vp = 1;
    const auto [next, over, winner] = apply_event_result(pub, 103, Side::USSR, 25U);
    require(over, "Wargames should end the game immediately at DEFCON 2");
    require(next.vp == -5, "Wargames should transfer 6 VP to the opponent");
    require(winner.has_value() && *winner == Side::US, "Wargames winner should be the side ahead after the VP transfer");
}

void test_korean_war() {
    PublicState pub;
    pub.defcon = 4;
    pub.set_influence(Side::US, 25, 2);
    const auto next = apply_event(pub, 11, Side::USSR, 1U);
    require(next.defcon == 4, "Korean War should be DEFCON-immune");
    require(next.milops[ts::to_index(Side::USSR)] == 2, "Korean War should set USSR milops to 2");
    require(next.vp == 2 || next.vp == -1, "Korean War should produce either +2 USSR VP or +1 US VP");
}

void test_olympic_games() {
    PublicState pub;
    pub.defcon = 4;
    const auto next = apply_event(pub, 20, Side::USSR, 1U);
    int added = 0;
    for (CountryId cid = 0; cid < ts::kCountrySlots; ++cid) {
        added += next.influence_of(Side::USSR, cid) - pub.influence_of(Side::USSR, cid);
    }
    const bool boycott_branch = next.defcon == 3;
    const bool compete_branch = next.defcon == 4;
    require(boycott_branch || compete_branch, "Olympic Games should either keep or lower DEFCON by 1");
    if (boycott_branch) {
        require(added == 4, "Olympic Games boycott should add 4 influence");
        require(next.vp == 0, "Olympic Games boycott should not change VP");
    } else {
        require(added == 0, "Olympic Games compete should not add influence");
        require(next.vp == 2 || next.vp == -2, "Olympic Games compete should award 2 VP to one side");
    }
}

void test_indo_pakistani_war() {
    PublicState pub;
    pub.defcon = 4;
    pub.set_influence(Side::US, 24, 2);
    const auto next = apply_event(pub, 24, Side::USSR, 1U);
    require(next.defcon == 4, "Indo-Pakistani War should be DEFCON-immune");
    require(next.milops[ts::to_index(Side::USSR)] == 2, "Indo-Pakistani War should set milops to 2");
    require(next.vp == 2 || next.vp == -1, "Indo-Pakistani War should award +2 or -1 VP to phasing side");
}

void test_iran_iraq_war() {
    PublicState pub;
    pub.defcon = 4;
    pub.set_influence(Side::USSR, 29, 1);
    const auto next = apply_event(pub, 105, Side::US, 1U);
    require(next.defcon == 3, "Iran-Iraq War should lower DEFCON on battleground coup");
    require(next.milops[ts::to_index(Side::US)] == 2, "Iran-Iraq War should set US milops to 2");
}

}  // namespace

int main() {
    test_duck_and_cover();
    test_fidel();
    test_we_will_bury_you();
    test_kal_007();
    test_cuban_missile_crisis();
    test_ops_and_flags_batch();
    test_truman_doctrine();
    test_captured_nazi_scientist();
    test_warsaw_pact();
    test_us_japan_pact();
    test_nixon_and_hostage_crisis();
    test_camp_david_accords();
    test_opec_and_awacs();
    test_iron_lady_and_yuri();
    test_flower_power_cancel();
    test_wargames();
    test_korean_war();
    test_olympic_games();
    test_indo_pakistani_war();
    test_iran_iraq_war();
    std::cout << "event parity smoke ok\n";
    return 0;
}
