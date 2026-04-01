#include "step.hpp"

#include <algorithm>

#include "adjacency.hpp"
#include "dice.hpp"
#include "game_data.hpp"

namespace ts {
namespace {

constexpr std::array<CardId, 5> kWarCardIds = {11, 13, 24, 39, 105};
constexpr std::array<CountryId, 7> kEasternBlocIds = {3, 5, 9, 12, 13, 19, 83};
constexpr std::array<CountryId, 12> kWesternEuropeIds = {1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18};
constexpr CountryId kIndiaId = 21;
constexpr CountryId kJapanId = 22;
constexpr CountryId kPakistanId = 24;
constexpr CountryId kEgyptId = 26;
constexpr CountryId kSouthKoreaId = 25;
constexpr CountryId kIranId = 28;
constexpr CountryId kIraqId = 29;
constexpr CountryId kIsraelId = 30;
constexpr CountryId kJordanId = 31;
constexpr CountryId kLebanonId = 32;
constexpr CountryId kLibyaId = 33;
constexpr CountryId kSaudiArabiaId = 34;
constexpr CountryId kCubaId = 36;
constexpr CountryId kNicaraguaId = 43;
constexpr CountryId kChileId = 49;
constexpr CountryId kVenezuelaId = 55;
constexpr CountryId kAngolaId = 57;
constexpr CountryId kBotswanaId = 58;
constexpr CountryId kMozambiqueId = 66;
constexpr CountryId kSouthAfricaId = 71;
constexpr CountryId kZimbabweId = 74;
constexpr CountryId kFranceId = 7;
constexpr CountryId kUkId = 17;
constexpr CountryId kWestGermanyId = 18;
constexpr CountryId kPolandId = 12;
constexpr CountryId kRomaniaId = 13;
constexpr CountryId kVietnamId = 80;
constexpr std::array<CountryId, 7> kOpecIds = {kEgyptId, kIranId, kLibyaId, kSaudiArabiaId, kIraqId, 27, kVenezuelaId};

bool contains(std::span<const CardId> values, CardId value) {
    return std::find(values.begin(), values.end(), value) != values.end();
}

template <typename T>
const T& sample_one(std::span<const T> values, Pcg64Rng& rng) {
    return values[rng.choice_index(values.size())];
}

void apply_vp_delta(PublicState& pub, Side side, int delta) {
    if (side == Side::USSR) {
        pub.vp += delta;
    } else {
        pub.vp -= delta;
    }
}

void add_influence(PublicState& pub, Side side, CountryId country_id, int delta) {
    pub.set_influence(side, country_id, std::max(0, pub.influence_of(side, country_id) + delta));
}

void remove_all_influence(PublicState& pub, Side side, CountryId country_id) {
    pub.set_influence(side, country_id, 0);
}

void gain_control(PublicState& pub, Side side, CountryId country_id) {
    const auto opponent = other_side(side);
    const auto needed = pub.influence_of(opponent, country_id) + country_spec(country_id).stability;
    if (pub.influence_of(side, country_id) < needed) {
        pub.set_influence(side, country_id, needed);
    }
}

int apply_free_coup(
    PublicState& pub,
    Side side,
    CountryId country_id,
    int ops,
    Pcg64Rng& rng,
    bool defcon_immune
) {
    const auto opponent = other_side(side);
    const auto net = coup_result(ops, country_spec(country_id).stability, rng);
    if (net > 0) {
        const auto removed = std::min(net, pub.influence_of(opponent, country_id));
        pub.set_influence(opponent, country_id, pub.influence_of(opponent, country_id) - removed);
        if (const auto excess = net - removed; excess > 0) {
            pub.set_influence(side, country_id, pub.influence_of(side, country_id) + excess);
        }
    }
    if (country_spec(country_id).is_battleground && !defcon_immune) {
        pub.defcon = std::max(1, pub.defcon - 1);
    }
    pub.milops[to_index(side)] = std::max(pub.milops[to_index(side)], ops);
    return net;
}

std::vector<CountryId> sample_up_to(std::span<const CountryId> pool, int count, Pcg64Rng& rng) {
    return sample_without_replacement(pool, static_cast<size_t>(std::max(count, 0)), rng);
}

void advance_space_track(PublicState& pub, Side side, int steps) {
    static constexpr std::array<std::pair<int, int>, 9> kSpaceVp = {{
        {0, 0}, {2, 0}, {0, 0}, {2, 0}, {0, 0}, {3, 1}, {0, 0}, {4, 2}, {2, 0},
    }};
    const auto opponent = other_side(side);
    for (int i = 0; i < steps; ++i) {
        const auto current = pub.space[to_index(side)];
        if (current >= 8) {
            break;
        }
        const auto next_level = current + 1;
        pub.space[to_index(side)] = next_level;
        const auto [first_vp, second_vp] = kSpaceVp[next_level];
        const auto vp = pub.space[to_index(opponent)] < next_level ? first_vp : second_vp;
        apply_vp_delta(pub, side, vp);
    }
}

void handle_card_played(PublicState& pub, CardId card_id, Side side, ActionMode mode) {
    if (pub.discard.test(card_id) || pub.removed.test(card_id)) {
        return;
    }
    if (card_id == kChinaCardId) {
        pub.china_held_by = other_side(side);
        pub.china_playable = false;
        return;
    }
    const auto& spec = card_spec(card_id);
    if (mode == ActionMode::Event && spec.starred) {
        pub.removed.set(card_id);
    } else {
        pub.discard.set(card_id);
    }
}

std::tuple<PublicState, bool, std::optional<Side>> apply_event(
    const PublicState& pub,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng
) {
    auto next = pub;
    bool force_game_over = false;
    std::optional<Side> forced_winner;

    if (
        side == Side::US &&
        contains(kWarCardIds, action.card_id) &&
        next.flower_power_active &&
        !next.flower_power_cancelled
    ) {
        next.vp += 2;
    }

    const auto& spec = card_spec(action.card_id);
    if (spec.is_scoring) {
        auto result = apply_scoring_card(action.card_id, next);
        next.vp += result.vp_delta;
        if (result.clear_shuttle) {
            next.shuttle_diplomacy_active = false;
        }
        handle_card_played(next, action.card_id, side, ActionMode::Event);
        if (result.game_over) {
            return {next, true, result.winner};
        }
        return {next, false, std::nullopt};
    }

    switch (action.card_id) {
        case 9:
            add_influence(next, Side::USSR, kVietnamId, 2);
            next.vietnam_revolts_active = true;
            next.ops_modifier[to_index(Side::USSR)] += 1;
            break;

        case 4: {
            const auto pre_defcon = next.defcon;
            next.vp -= (5 - pre_defcon);
            next.defcon = std::max(1, next.defcon - 1);
            break;
        }

        case 7: {
            std::vector<CountryId> pool;
            for (const auto cid : kWesternEuropeIds) {
                if (!controls_country(Side::US, cid, next) && next.influence_of(Side::USSR, cid) < 2) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 3, rng)) {
                add_influence(next, Side::USSR, cid, 1);
            }
            break;
        }

        case 8:
            remove_all_influence(next, Side::US, kCubaId);
            gain_control(next, Side::USSR, kCubaId);
            break;

        case 11: {
            const auto net = apply_free_coup(next, Side::USSR, kSouthKoreaId, 2, rng, true);
            if (net > 0) {
                next.vp += 2;
            } else {
                next.vp -= 1;
            }
            break;
        }

        case 12:
            remove_all_influence(next, Side::US, kRomaniaId);
            gain_control(next, Side::USSR, kRomaniaId);
            break;

        case 13: {
            const auto net = apply_free_coup(next, Side::USSR, kIsraelId, 2, rng, true);
            if (net <= 0) {
                next.vp -= 1;
            }
            break;
        }

        case 14: {
            std::vector<CountryId> pool;
            for (const auto cid : kEasternBlocIds) {
                if (!controls_country(Side::US, cid, next)) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 4, rng)) {
                add_influence(next, Side::USSR, cid, 1);
            }
            break;
        }

        case 15: {
            add_influence(next, Side::USSR, kEgyptId, 2);
            const auto remove = (next.influence_of(Side::US, kEgyptId) + 1) / 2;
            add_influence(next, Side::US, kEgyptId, -remove);
            break;
        }

        case 16: {
            if (rng.choice_index(2) == 0) {
                std::vector<CountryId> pool;
                for (const auto cid : kEasternBlocIds) {
                    if (next.influence_of(Side::US, cid) > 0) {
                        pool.push_back(cid);
                    }
                }
                for (const auto cid : sample_up_to(pool, 4, rng)) {
                    remove_all_influence(next, Side::US, cid);
                }
            } else {
                for (const auto cid : sample_up_to(kEasternBlocIds, 5, rng)) {
                    add_influence(next, Side::USSR, cid, 1);
                }
            }
            next.warsaw_pact_played = true;
            break;
        }

        case 20: {
            if (rng.bernoulli(0.5)) {
                next.defcon = std::max(1, next.defcon - 1);
                const auto accessible = accessible_countries(side, next, ActionMode::Influence);
                if (!accessible.empty()) {
                    for (int i = 0; i < 4; ++i) {
                        add_influence(next, side, sample_one<CountryId>(accessible, rng), 1);
                    }
                }
            } else {
                const auto opponent = other_side(side);
                auto my_roll = roll_d6(rng);
                auto opp_roll = roll_d6(rng);
                while (my_roll == opp_roll) {
                    my_roll = roll_d6(rng);
                    opp_roll = roll_d6(rng);
                }
                apply_vp_delta(next, my_roll > opp_roll ? side : opponent, 2);
            }
            break;
        }

        case 21:
            next.nato_active = true;
            break;

        case 22:
            for (const auto cid : {CountryId{19}, CountryId{13}, CountryId{83}, CountryId{9}, CountryId{3}}) {
                add_influence(next, Side::US, cid, 1);
            }
            break;

        case 23: {
            std::vector<CountryId> pool;
            for (const auto cid : kWesternEuropeIds) {
                if (!controls_country(Side::USSR, cid, next)) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 7, rng)) {
                add_influence(next, Side::US, cid, 1);
            }
            next.marshall_plan_played = true;
            break;
        }

        case 24: {
            static constexpr std::array<CountryId, 2> kTargets = {kIndiaId, kPakistanId};
            const auto target = sample_one<CountryId>(kTargets, rng);
            const auto net = apply_free_coup(next, side, target, 2, rng, true);
            apply_vp_delta(next, side, net > 0 ? 2 : -1);
            break;
        }

        case 17:
            add_influence(next, Side::US, kFranceId, -2);
            add_influence(next, Side::USSR, kFranceId, 1);
            next.de_gaulle_active = true;
            break;

        case 18:
            advance_space_track(next, side, 1);
            break;

        case 19: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (country_spec(cid).region != Region::Europe) {
                    continue;
                }
                if (next.influence_of(Side::USSR, cid) <= 0) {
                    continue;
                }
                if (!controls_country(Side::USSR, cid, next)) {
                    pool.push_back(cid);
                }
            }
            if (!pool.empty()) {
                remove_all_influence(next, Side::USSR, sample_one<CountryId>(pool, rng));
            }
            next.truman_doctrine_played = true;
            break;
        }

        case 25:
            next.ops_modifier[to_index(Side::US)] += 1;
            break;

        case 27:
            next.us_japan_pact_active = true;
            gain_control(next, Side::US, kJapanId);
            break;

        case 28:
            for (const auto cid : sample_up_to(std::array<CountryId, 3>{kFranceId, kUkId, kIsraelId}, 2, rng)) {
                add_influence(next, Side::US, cid, -2);
            }
            break;

        case 29:
            for (const auto cid : sample_up_to(kEasternBlocIds, 3, rng)) {
                add_influence(next, Side::US, cid, 1);
            }
            break;

        case 30: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                const auto region = country_spec(cid).region;
                if (region == Region::Africa || region == Region::SoutheastAsia) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 4, rng)) {
                add_influence(next, Side::USSR, cid, 1);
            }
            break;
        }

        case 31:
            next.ops_modifier[to_index(other_side(side))] -= 1;
            break;

        case 33: {
            std::vector<CountryId> sources;
            std::vector<CountryId> destinations;
            for (const auto cid : all_country_ids()) {
                if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                    continue;
                }
                if (next.influence_of(Side::USSR, cid) > 0) {
                    sources.push_back(cid);
                }
                if (!controls_country(Side::US, cid, next)) {
                    destinations.push_back(cid);
                }
            }
            int total_to_move = 0;
            for (const auto cid : sources) {
                total_to_move += next.influence_of(Side::USSR, cid);
            }
            total_to_move = std::min(total_to_move, 4);
            for (int i = 0; i < total_to_move; ++i) {
                std::vector<CountryId> available_sources;
                for (const auto cid : sources) {
                    if (next.influence_of(Side::USSR, cid) > 0) {
                        available_sources.push_back(cid);
                    }
                }
                if (available_sources.empty() || destinations.empty()) {
                    break;
                }
                const auto src = sample_one<CountryId>(available_sources, rng);
                const auto dst = sample_one<CountryId>(destinations, rng);
                add_influence(next, Side::USSR, src, -1);
                add_influence(next, Side::USSR, dst, 1);
            }
            break;
        }

        case 34: {
            const auto vp_gain = std::max(0, next.defcon - 2);
            apply_vp_delta(next, side, vp_gain);
            next.defcon = std::min(5, next.defcon + 2);
            break;
        }

        case 35:
            next.formosan_active = true;
            break;

        case 37:
            if (controls_country(Side::US, kUkId, next) && next.nato_active) {
                next.vp -= 2;
                std::vector<CountryId> pool;
                for (const auto cid : all_country_ids()) {
                    if (cid != 64 && cid != kUsaAnchorId && cid != kUssrAnchorId) {
                        pool.push_back(cid);
                    }
                }
                for (int i = 0; i < 2 && !pool.empty(); ++i) {
                    add_influence(next, Side::US, sample_one<CountryId>(pool, rng), 1);
                }
            } else {
                add_influence(next, Side::US, sample_one<CountryId>(kWesternEuropeIds, rng), 1);
            }
            break;

        case 38:
            next.norad_active = true;
            break;

        case 39: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                    continue;
                }
                if (country_spec(cid).stability <= 2) {
                    pool.push_back(cid);
                }
            }
            if (!pool.empty()) {
                const auto target = sample_one<CountryId>(pool, rng);
                const auto net = apply_free_coup(next, Side::USSR, target, 3, rng, false);
                if (net > 0) {
                    add_influence(next, Side::US, target, -std::min(2, next.influence_of(Side::US, target)));
                }
            }
            break;
        }

        case 42: {
            const auto own = next.milops[to_index(side)];
            const auto opp = next.milops[to_index(other_side(side))];
            if (own > opp) {
                apply_vp_delta(next, side, own >= next.defcon ? 3 : 1);
            }
            break;
        }

        case 43:
            next.defcon = 2;
            next.cuban_missile_crisis_active = true;
            break;

        case 44:
            next.nuclear_subs_active = true;
            break;

        case 46:
            next.defcon = std::min(5, next.defcon + 1);
            next.salt_active = true;
            break;

        case 48: {
            auto ussr_roll = roll_d6(rng);
            auto us_roll = roll_d6(rng);
            const auto winner =
                side == Side::USSR ? (ussr_roll >= us_roll ? Side::USSR : Side::US)
                                   : (us_roll >= ussr_roll ? Side::US : Side::USSR);
            const auto defcon_delta = rng.choice_index(2) == 0 ? -1 : 1;
            next.defcon = std::clamp(next.defcon + defcon_delta, 1, 5);
            apply_vp_delta(next, winner, 2);
            break;
        }

        case 49: {
            next.defcon = rng.uniform_int(1, 5);
            next.milops[to_index(side)] = 5;
            break;
        }

        case 50: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                const auto region = country_spec(cid).region;
                if (region == Region::CentralAmerica || region == Region::SouthAmerica) {
                    pool.push_back(cid);
                }
            }
            if (!pool.empty()) {
                add_influence(next, side, sample_one<CountryId>(pool, rng), 2);
                apply_free_coup(next, side, sample_one<CountryId>(pool, rng), 2, rng, false);
            }
            break;
        }

        case 51: {
            int us_bg = 0;
            int ussr_bg = 0;
            for (const auto cid : all_country_ids()) {
                if ((cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) || !country_spec(cid).is_battleground) {
                    continue;
                }
                if (controls_country(Side::US, cid, next)) {
                    ++us_bg;
                }
                if (controls_country(Side::USSR, cid, next)) {
                    ++ussr_bg;
                }
            }
            if (const auto excess = us_bg - ussr_bg; excess > 0) {
                next.vp -= excess;
            }
            break;
        }

        case 53:
            next.defcon = std::max(1, next.defcon - 1);
            next.vp += 3;
            break;

        case 54:
            next.ops_modifier[to_index(Side::USSR)] += 1;
            break;

        case 55:
            add_influence(next, Side::USSR, kAngolaId, 2);
            add_influence(next, Side::USSR, kMozambiqueId, 2);
            break;

        case 56:
            add_influence(next, Side::USSR, kSouthAfricaId, 2);
            add_influence(
                next,
                Side::USSR,
                sample_one<CountryId>(std::array<CountryId, 3>{kBotswanaId, 69, kZimbabweId}, rng),
                2
            );
            break;

        case 57:
            add_influence(next, Side::USSR, kChileId, 2);
            break;

        case 58:
            next.vp += 1;
            add_influence(next, Side::USSR, kWestGermanyId, 1);
            next.willy_brandt_active = true;
            break;

        case 59: {
            static constexpr std::array<CountryId, 8> kPool = {72, kIranId, kIraqId, kEgyptId, kLibyaId, kSaudiArabiaId, 35, kJordanId};
            std::vector<CountryId> eligible;
            for (const auto cid : kPool) {
                if (next.influence_of(Side::US, cid) > 0) {
                    eligible.push_back(cid);
                }
            }
            if (eligible.size() < 2) {
                eligible.assign(kPool.begin(), kPool.end());
            }
            for (const auto cid : sample_up_to(eligible, 2, rng)) {
                remove_all_influence(next, Side::US, cid);
            }
            break;
        }

        case 60: {
            next.defcon = std::min(5, next.defcon + 1);
            apply_vp_delta(next, side, 1);
            std::vector<CountryId> eligible;
            for (const auto cid : all_country_ids()) {
                if (next.influence_of(side, cid) > 0) {
                    eligible.push_back(cid);
                }
            }
            for (int i = 0; i < 2 && !eligible.empty(); ++i) {
                add_influence(next, side, sample_one<CountryId>(eligible, rng), 1);
            }
            break;
        }

        case 61:
            if (next.china_held_by == Side::US) {
                next.china_held_by = Side::USSR;
                next.china_playable = false;
            } else {
                next.vp += 1;
            }
            break;

        case 62:
            next.flower_power_active = true;
            break;

        case 63:
            next.vp += 1;
            break;

        case 64: {
            if (!next.opec_cancelled) {
                int count = 0;
                for (const auto cid : kOpecIds) {
                    if (cid == kSaudiArabiaId && next.awacs_active) {
                        continue;
                    }
                    if (next.influence_of(Side::USSR, cid) > 0) {
                        ++count;
                    }
                }
                next.vp += count;
            }
            break;
        }

        case 65:
            next.defcon = std::min(5, next.defcon + 1);
            next.vp -= 1;
            break;

        case 70:
            next.latam_coup_bonus = side;
            break;

        case 66:
            apply_vp_delta(next, Side::US, 1);
            add_influence(next, Side::US, kIsraelId, 1);
            add_influence(next, Side::US, kEgyptId, 1);
            add_influence(next, Side::US, kJordanId, 1);
            break;

        case 67: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                    continue;
                }
                if (next.influence_of(Side::USSR, cid) == 0 && next.influence_of(Side::US, cid) == 0) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 3, rng)) {
                add_influence(next, Side::US, cid, 1);
            }
            break;
        }

        case 69:
            add_influence(next, Side::USSR, kPolandId, -2);
            add_influence(next, Side::US, kPolandId, 1);
            next.john_paul_ii_played = true;
            break;

        case 71: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                const auto region = country_spec(cid).region;
                if (region == Region::CentralAmerica || region == Region::SouthAmerica) {
                    pool.push_back(cid);
                }
            }
            for (int i = 0; i < 2 && !pool.empty(); ++i) {
                add_influence(next, Side::US, sample_one<CountryId>(pool, rng), 1);
            }
            break;
        }

        case 72:
            if (next.china_held_by == Side::USSR) {
                next.vp -= 2;
                next.china_held_by = Side::US;
                next.china_playable = false;
            } else if (next.china_held_by == Side::US) {
                next.china_playable = true;
            }
            break;

        case 73:
            remove_all_influence(next, Side::USSR, kEgyptId);
            add_influence(next, Side::US, kEgyptId, 1);
            break;

        case 74:
            next.shuttle_diplomacy_active = true;
            break;

        case 75: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                    continue;
                }
                if (country_spec(cid).region == Region::Europe) {
                    continue;
                }
                if (next.influence_of(Side::USSR, cid) >= 1) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 4, rng)) {
                add_influence(next, Side::USSR, cid, -1);
            }
            break;
        }

        case 76: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (country_spec(cid).region == Region::CentralAmerica && next.influence_of(Side::USSR, cid) < 2) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 3, rng)) {
                add_influence(next, Side::USSR, cid, 1);
            }
            break;
        }

        case 77: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid != 64 && cid != kUsaAnchorId && cid != kUssrAnchorId) {
                    pool.push_back(cid);
                }
            }
            if (next.china_held_by == Side::USSR) {
                next.china_held_by = Side::US;
                next.china_playable = true;
                for (int i = 0; i < 4 && !pool.empty(); ++i) {
                    add_influence(next, Side::USSR, sample_one<CountryId>(pool, rng), 1);
                }
            } else {
                next.china_held_by = Side::USSR;
                next.china_playable = true;
                for (int i = 0; i < 4 && !pool.empty(); ++i) {
                    add_influence(next, Side::US, sample_one<CountryId>(pool, rng), 1);
                }
            }
            break;
        }

        case 79: {
            int count = 0;
            for (const auto cid : all_country_ids()) {
                const auto region = country_spec(cid).region;
                if (
                    (region == Region::CentralAmerica || region == Region::SouthAmerica) &&
                    country_spec(cid).is_battleground &&
                    controls_country(Side::US, cid, next)
                ) {
                    ++count;
                }
            }
            next.vp -= count;
            break;
        }

        case 81:
            if (next.space[to_index(side)] < next.space[to_index(other_side(side))]) {
                advance_space_track(next, side, 2);
            }
            break;

        case 83: {
            auto region_key = [&](CountryId cid) {
                const auto region = country_spec(cid).region;
                if (region == Region::CentralAmerica) {
                    return 0;
                }
                if (region == Region::SouthAmerica) {
                    return 1;
                }
                return 2;
            };
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (cid == 64) {
                    continue;
                }
                const auto region = country_spec(cid).region;
                if (
                    (region == Region::CentralAmerica || region == Region::SouthAmerica || region == Region::Africa) &&
                    country_spec(cid).stability <= 2
                ) {
                    pool.push_back(cid);
                }
            }
            if (!pool.empty()) {
                const auto first = sample_one<CountryId>(pool, rng);
                const auto first_region = region_key(first);
                apply_free_coup(next, Side::USSR, first, 3, rng, false);
                std::vector<CountryId> second_pool;
                for (const auto cid : pool) {
                    if (region_key(cid) != first_region) {
                        second_pool.push_back(cid);
                    }
                }
                if (!second_pool.empty()) {
                    apply_free_coup(next, Side::USSR, sample_one<CountryId>(second_pool, rng), 3, rng, false);
                }
            }
            break;
        }

        case 85:
            remove_all_influence(next, Side::US, kIranId);
            add_influence(next, Side::USSR, kIranId, 2);
            next.iran_hostage_crisis_active = true;
            break;

        case 89:
            next.opec_cancelled = true;
            next.north_sea_oil_extra_ar = true;
            break;

        case 90: {
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (country_spec(cid).region == Region::Europe && !controls_country(Side::US, cid, next)) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 4, rng)) {
                add_influence(next, Side::USSR, cid, 1);
            }
            next.defcon = std::min(5, next.defcon + 1);
            break;
        }

        case 91: {
            remove_all_influence(next, Side::US, kLebanonId);
            std::vector<CountryId> pool;
            for (const auto cid : all_country_ids()) {
                if (country_spec(cid).region != Region::MiddleEast || cid == kLebanonId) {
                    continue;
                }
                if (next.influence_of(Side::US, cid) >= 1) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 2, rng)) {
                add_influence(next, Side::US, cid, -1);
            }
            break;
        }

        case 86:
            next.vp -= 1;
            remove_all_influence(next, Side::USSR, kUkId);
            next.opec_cancelled = true;
            break;

        case 87:
            next.vp -= next.influence_of(Side::USSR, kLibyaId);
            break;

        case 92:
            next.defcon = std::max(1, next.defcon - 1);
            next.vp -= 2;
            if (next.china_held_by == Side::USSR) {
                next.china_held_by = Side::US;
                next.china_playable = true;
            }
            break;

        case 93:
            next.vp += 2;
            next.defcon = std::min(5, next.defcon + 1);
            if (next.salt_active) {
                next.glasnost_extra_ar = true;
            }
            break;

        case 94:
            remove_all_influence(next, Side::US, kNicaraguaId);
            apply_free_coup(next, Side::USSR, sample_one<CountryId>(std::array<CountryId, 3>{38, 41, 45}, rng), 2, rng, false);
            break;

        case 96:
            next.ops_modifier[to_index(Side::US)] -= 1;
            break;

        case 98:
            next.vp += 2;
            break;

        case 99:
            remove_all_influence(next, Side::USSR, 5);
            add_influence(next, Side::US, 5, 3);
            next.willy_brandt_active = false;
            break;

        case 97: {
            static constexpr std::array<Region, 6> kRegions = {
                Region::Europe,
                Region::Asia,
                Region::MiddleEast,
                Region::CentralAmerica,
                Region::SouthAmerica,
                Region::Africa,
            };
            next.chernobyl_blocked_region = sample_one<Region>(kRegions, rng);
            break;
        }

        case 100:
            next.vp -= 1;
            next.flower_power_cancelled = true;
            next.flower_power_active = false;
            break;

        case 103:
            if (next.defcon == 2) {
                apply_vp_delta(next, other_side(side), 6);
                force_game_over = true;
                if (next.vp > 0) {
                    forced_winner = Side::USSR;
                } else if (next.vp < 0) {
                    forced_winner = Side::US;
                } else {
                    forced_winner = std::nullopt;
                }
            }
            break;

        case 104:
            if (next.john_paul_ii_played) {
                add_influence(next, Side::US, kPolandId, 3);
            }
            break;

        case 102: {
            next.vp += 1;
            std::vector<CountryId> pool;
            for (const auto cid : kWesternEuropeIds) {
                if (next.influence_of(Side::US, cid) >= 1) {
                    pool.push_back(cid);
                }
            }
            for (const auto cid : sample_up_to(pool, 3, rng)) {
                add_influence(next, Side::US, cid, -1);
            }
            break;
        }

        case 105: {
            static constexpr std::array<CountryId, 2> kTargets = {kIranId, kIraqId};
            const auto target = sample_one<CountryId>(kTargets, rng);
            const auto net = apply_free_coup(next, side, target, 2, rng, false);
            apply_vp_delta(next, side, net > 0 ? 2 : -1);
            break;
        }

        case 106:
            next.vp += next.space_attempts[to_index(Side::US)];
            break;

        case 107:
            add_influence(next, Side::US, kSaudiArabiaId, 2);
            next.awacs_active = true;
            break;

        case kChinaCardId:
            if (side == Side::USSR) {
                next.formosan_active = false;
            }
            break;

        default:
            break;
    }

    handle_card_played(next, action.card_id, side, ActionMode::Event);
    if (force_game_over) {
        return {next, true, forced_winner};
    }
    const auto [over, winner] = check_vp_win(next);
    return {next, over, winner};
}

}  // namespace

std::tuple<PublicState, bool, std::optional<Side>> apply_action(
    const PublicState& pub,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng
) {
    auto next = pub;

    switch (action.mode) {
        case ActionMode::Influence:
            for (const auto target : action.targets) {
                next.set_influence(side, target, next.influence_of(side, target) + 1);
            }
            handle_card_played(next, action.card_id, side, ActionMode::Influence);
            break;

        case ActionMode::Coup: {
            const auto target = action.targets.front();
            auto ops = effective_ops(action.card_id, pub, side);
            if (action.card_id == kChinaCardId && country_spec(target).region == Region::Asia) {
                ++ops;
            }
            auto net = coup_result(ops, country_spec(target).stability, rng);
            if (
                pub.latam_coup_bonus.has_value() &&
                (country_spec(target).region == Region::CentralAmerica || country_spec(target).region == Region::SouthAmerica)
            ) {
                net += side == *pub.latam_coup_bonus ? 1 : -1;
            }
            if (net > 0) {
                const auto opp = other_side(side);
                const auto removed = std::min(net, next.influence_of(opp, target));
                next.set_influence(opp, target, next.influence_of(opp, target) - removed);
                if (const auto excess = net - removed; excess > 0) {
                    next.set_influence(side, target, next.influence_of(side, target) + excess);
                }
            }
            if (country_spec(target).is_battleground && !(side == Side::US && next.nuclear_subs_active)) {
                next.defcon = std::max(1, next.defcon - 1);
            }
            next.milops[to_index(side)] = std::max(next.milops[to_index(side)], ops);
            handle_card_played(next, action.card_id, side, ActionMode::Coup);
            break;
        }

        case ActionMode::Realign: {
            const auto& graph = adjacency();
            for (const auto target : action.targets) {
                const auto ussr_inf = next.influence_of(Side::USSR, target);
                const auto us_inf = next.influence_of(Side::US, target);
                auto count_adj = [&](Side player) {
                    int total = 0;
                    for (const auto neighbor : graph[target]) {
                        if (neighbor == kUsaAnchorId || neighbor == kUssrAnchorId) {
                            continue;
                        }
                        if (controls_country(player, neighbor, next)) {
                            ++total;
                        }
                    }
                    return total;
                };
                const auto ussr_anchor = std::find(graph[target].begin(), graph[target].end(), kUssrAnchorId) != graph[target].end() ? 1 : 0;
                const auto us_anchor = std::find(graph[target].begin(), graph[target].end(), kUsaAnchorId) != graph[target].end() ? 1 : 0;
                const auto [ussr_total, us_total] = realign_result(
                    ussr_inf,
                    us_inf,
                    count_adj(Side::USSR) + ussr_anchor,
                    count_adj(Side::US) + us_anchor,
                    rng
                );
                if (ussr_total > us_total) {
                    next.set_influence(Side::US, target, std::max(0, next.influence_of(Side::US, target) - (ussr_total - us_total)));
                } else if (us_total > ussr_total) {
                    next.set_influence(Side::USSR, target, std::max(0, next.influence_of(Side::USSR, target) - (us_total - ussr_total)));
                }
            }
            handle_card_played(next, action.card_id, side, ActionMode::Realign);
            break;
        }

        case ActionMode::Space: {
            const auto current_level = next.space[to_index(side)];
            if (space_result(current_level, rng)) {
                const auto new_level = current_level + 1;
                next.space[to_index(side)] = new_level;
                if (new_level == 4 && !next.space_level4_first.has_value()) {
                    next.space_level4_first = side;
                }
                if (new_level == 6 && !next.space_level6_first.has_value()) {
                    next.space_level6_first = side;
                }
                static constexpr std::array<std::pair<int, int>, 9> kSpaceVp = {{
                    {0, 0}, {2, 0}, {0, 0}, {2, 0}, {0, 0}, {3, 1}, {0, 0}, {4, 2}, {2, 0},
                }};
                const auto [first_vp, second_vp] = kSpaceVp[new_level];
                const auto opponent_level = next.space[to_index(other_side(side))];
                const auto vp = opponent_level < new_level ? first_vp : second_vp;
                next.vp += side == Side::USSR ? vp : -vp;
            }
            next.space_attempts[to_index(side)] += 1;
            handle_card_played(next, action.card_id, side, ActionMode::Space);
            break;
        }

        case ActionMode::Event: {
            auto [event_pub, over, winner] = apply_event(pub, action, side, rng);
            return {event_pub, over, winner};
        }
    }

    const auto [over, winner] = check_vp_win(next);
    return {next, over, winner};
}

std::tuple<bool, std::optional<Side>> check_vp_win(const PublicState& pub) {
    if (pub.vp >= 20) {
        return {true, Side::USSR};
    }
    if (pub.vp <= -20) {
        return {true, Side::US};
    }
    if (pub.defcon <= 1) {
        return {true, other_side(pub.phasing)};
    }
    return {false, std::nullopt};
}

}  // namespace ts
