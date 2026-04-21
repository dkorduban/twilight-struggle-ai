#include <catch2/catch_test_macros.hpp>

#include <algorithm>
#include <array>
#include <bitset>
#include <cstdint>
#include <iomanip>
#include <optional>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

#include "game_data.hpp"
#include "game_loop.hpp"
#include "game_state.hpp"
#include "hand_ops.hpp"
#include "legal_actions.hpp"
#include "scoring.hpp"
#include "step.hpp"
#include "types.hpp"

using namespace ts;

namespace {

constexpr int kMidWarTurnForTest = 4;
constexpr int kLateWarTurnForTest = 8;
constexpr int kMaxTurnsForTest = 10;
constexpr int kSpaceShuttleArsForTest = 8;

enum class ExecutionPath {
    LegacyPolicyCallback,
    SubframePolicy,
};

struct TraceEntry {
    int turn = 0;
    int ar = 0;
    Side side = Side::Neutral;
    ActionEncoding action;
    uint64_t state_hash = 0;
};

struct GameRun {
    GameResult result;
    std::vector<TraceEntry> trace;
};

void hash_byte(uint64_t& hash, uint8_t value) {
    hash ^= value;
    hash *= 1099511628211ULL;
}

void hash_u64(uint64_t& hash, uint64_t value) {
    for (int shift = 0; shift < 64; shift += 8) {
        hash_byte(hash, static_cast<uint8_t>((value >> shift) & 0xffU));
    }
}

void hash_i64(uint64_t& hash, int64_t value) {
    hash_u64(hash, static_cast<uint64_t>(value));
}

void hash_bool(uint64_t& hash, bool value) {
    hash_byte(hash, value ? 1U : 0U);
}

void hash_side(uint64_t& hash, Side side) {
    hash_i64(hash, static_cast<int>(side));
}

void hash_region(uint64_t& hash, Region region) {
    hash_i64(hash, static_cast<int>(region));
}

template <size_t N>
void hash_bitset(uint64_t& hash, const std::bitset<N>& bits) {
    for (size_t idx = 0; idx < N; ++idx) {
        hash_bool(hash, bits.test(idx));
    }
}

void hash_optional_side(uint64_t& hash, const std::optional<Side>& side) {
    hash_bool(hash, side.has_value());
    if (side.has_value()) {
        hash_side(hash, *side);
    }
}

void hash_optional_region(uint64_t& hash, const std::optional<Region>& region) {
    hash_bool(hash, region.has_value());
    if (region.has_value()) {
        hash_region(hash, *region);
    }
}

uint64_t per_ar_state_hash(const GameState& gs) {
    const auto& pub = gs.pub;
    uint64_t hash = 14695981039346656037ULL;

    hash_i64(hash, pub.turn);
    hash_i64(hash, pub.ar);
    hash_side(hash, pub.phasing);
    hash_i64(hash, pub.vp);
    hash_i64(hash, pub.defcon);
    for (const auto value : pub.milops) hash_i64(hash, value);
    for (const auto value : pub.space) hash_i64(hash, value);
    hash_side(hash, pub.china_held_by);
    hash_bool(hash, pub.china_playable);
    for (int side = 0; side < 2; ++side) {
        for (int country = 0; country < kCountrySlots; ++country) {
            hash_i64(hash, pub.influence[static_cast<size_t>(side)][static_cast<size_t>(country)]);
        }
    }
    hash_bitset(hash, pub.discard);
    hash_bitset(hash, pub.removed);
    for (const auto value : pub.space_attempts) hash_i64(hash, value);
    hash_optional_side(hash, pub.space_level4_first);
    hash_optional_side(hash, pub.space_level6_first);

    hash_bool(hash, pub.warsaw_pact_played);
    hash_bool(hash, pub.marshall_plan_played);
    hash_bool(hash, pub.truman_doctrine_played);
    hash_bool(hash, pub.john_paul_ii_played);
    hash_bool(hash, pub.nato_active);
    hash_bool(hash, pub.de_gaulle_active);
    hash_bool(hash, pub.willy_brandt_active);
    hash_bool(hash, pub.us_japan_pact_active);
    hash_bool(hash, pub.nuclear_subs_active);
    hash_bool(hash, pub.norad_active);
    hash_bool(hash, pub.shuttle_diplomacy_active);
    hash_bool(hash, pub.flower_power_active);
    hash_bool(hash, pub.flower_power_cancelled);
    hash_bool(hash, pub.salt_active);
    hash_bool(hash, pub.opec_cancelled);
    hash_bool(hash, pub.awacs_active);
    hash_bool(hash, pub.north_sea_oil_extra_ar);
    hash_i64(hash, pub.glasnost_free_ops);
    hash_bool(hash, pub.formosan_active);
    hash_bool(hash, pub.cuban_missile_crisis_active);
    hash_bool(hash, pub.vietnam_revolts_active);
    hash_bool(hash, pub.bear_trap_active);
    hash_bool(hash, pub.quagmire_active);
    hash_bool(hash, pub.iran_hostage_crisis_active);
    hash_i64(hash, pub.handicap_ussr);
    hash_i64(hash, pub.handicap_us);
    for (const auto value : pub.ops_modifier) hash_i64(hash, value);
    hash_optional_region(hash, pub.chernobyl_blocked_region);
    hash_optional_side(hash, pub.latam_coup_bonus);
    hash_i64(hash, pub.state_hash);

    return hash;
}

std::string side_to_string(Side side) {
    switch (side) {
        case Side::USSR: return "USSR";
        case Side::US: return "US";
        case Side::Neutral: return "Neutral";
    }
    return "?";
}

std::string winner_to_string(const std::optional<Side>& winner) {
    return winner.has_value() ? side_to_string(*winner) : "draw";
}

std::string mode_to_string(ActionMode mode) {
    switch (mode) {
        case ActionMode::Influence: return "Influence";
        case ActionMode::Coup: return "Coup";
        case ActionMode::Realign: return "Realign";
        case ActionMode::Space: return "Space";
        case ActionMode::Event: return "Event";
        case ActionMode::EventFirst: return "EventFirst";
    }
    return "?";
}

std::string action_to_string(const ActionEncoding& action) {
    std::ostringstream out;
    out << "card=" << static_cast<int>(action.card_id)
        << " mode=" << mode_to_string(action.mode)
        << " targets=[";
    for (size_t idx = 0; idx < action.targets.size(); ++idx) {
        if (idx != 0) out << ",";
        out << static_cast<int>(action.targets[idx]);
    }
    out << "]";
    return out.str();
}

std::string hash_to_string(uint64_t hash) {
    std::ostringstream out;
    out << "0x" << std::hex << std::setw(16) << std::setfill('0') << hash;
    return out.str();
}

void sync_china_for_test(GameState& gs) {
    gs.ussr_holds_china = gs.pub.china_held_by == Side::USSR;
    gs.us_holds_china = gs.pub.china_held_by == Side::US;
}

bool has_eligible_opponent_card_for_test(const CardSet& hand, Side side) {
    const auto opponent = other_side(side);
    for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
        if (!hand.test(static_cast<size_t>(card_id)) || card_id == kChinaCardId) {
            continue;
        }
        const auto& spec = card_spec(static_cast<CardId>(card_id));
        if (spec.side == opponent && !spec.is_scoring) {
            return true;
        }
    }
    return false;
}

std::vector<CountryId> sorted_countries(std::vector<CountryId> countries) {
    std::sort(countries.begin(), countries.end());
    countries.erase(std::unique(countries.begin(), countries.end()), countries.end());
    return countries;
}

bool first_budget_targets_impl(
    const std::vector<CountryId>& countries,
    const std::vector<int>& costs,
    int remaining,
    int start_index,
    std::vector<CountryId>& current
) {
    if (remaining == 0) {
        return true;
    }
    for (int idx = start_index; idx < static_cast<int>(countries.size()); ++idx) {
        if (costs[static_cast<size_t>(idx)] > remaining) {
            continue;
        }
        current.push_back(countries[static_cast<size_t>(idx)]);
        if (first_budget_targets_impl(countries, costs, remaining - costs[static_cast<size_t>(idx)], idx, current)) {
            return true;
        }
        current.pop_back();
    }
    return false;
}

std::optional<std::vector<CountryId>> first_budget_targets(
    std::vector<CountryId> countries,
    const PublicState& pub,
    Side side,
    int budget
) {
    countries = sorted_countries(std::move(countries));
    std::vector<int> costs;
    costs.reserve(countries.size());
    const auto opponent = other_side(side);
    for (const auto country : countries) {
        costs.push_back(controls_country(opponent, country, pub) ? 2 : 1);
    }

    std::vector<CountryId> targets;
    if (first_budget_targets_impl(countries, costs, budget, 0, targets)) {
        return targets;
    }
    return std::nullopt;
}

std::optional<ActionEncoding> first_legal_action(
    const PublicState& pub,
    const CardSet& hand,
    Side side,
    bool holds_china
) {
    auto cards = legal_cards(hand, pub, side, holds_china);
    std::sort(cards.begin(), cards.end());

    for (const auto card_id : cards) {
        auto modes = legal_modes(card_id, pub, side);
        if (card_id == 32 && !has_eligible_opponent_card_for_test(hand, side)) {
            modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        }
        std::sort(modes.begin(), modes.end(), [](ActionMode lhs, ActionMode rhs) {
            return static_cast<int>(lhs) < static_cast<int>(rhs);
        });

        for (const auto mode : modes) {
            if (mode == ActionMode::Event || mode == ActionMode::EventFirst || mode == ActionMode::Space) {
                return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}};
            }

            auto countries = sorted_countries(legal_countries(card_id, mode, pub, side));
            if (countries.empty()) {
                continue;
            }

            if (mode == ActionMode::Coup) {
                return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {countries.front()}};
            }

            auto targets = first_budget_targets(countries, pub, side, effective_ops(card_id, pub, side));
            if (targets.has_value()) {
                return ActionEncoding{.card_id = card_id, .mode = mode, .targets = *targets};
            }

            if (pub.vietnam_revolts_active && side == Side::USSR) {
                auto sea_countries = countries;
                sea_countries.erase(
                    std::remove_if(
                        sea_countries.begin(),
                        sea_countries.end(),
                        [](CountryId country) { return country_spec(country).region != Region::SoutheastAsia; }
                    ),
                    sea_countries.end()
                );
                targets = first_budget_targets(sea_countries, pub, side, effective_ops(card_id, pub, side) + 1);
                if (targets.has_value()) {
                    return ActionEncoding{.card_id = card_id, .mode = mode, .targets = *targets};
                }
            }

            if (card_id == kChinaCardId) {
                auto asia_countries = countries;
                asia_countries.erase(
                    std::remove_if(
                        asia_countries.begin(),
                        asia_countries.end(),
                        [](CountryId country) { return country_spec(country).region != Region::Asia; }
                    ),
                    asia_countries.end()
                );
                targets = first_budget_targets(asia_countries, pub, side, effective_ops(card_id, pub, side) + 1);
                if (targets.has_value()) {
                    return ActionEncoding{.card_id = card_id, .mode = mode, .targets = *targets};
                }
            }
        }
    }

    return std::nullopt;
}

PolicyCallbackFn deterministic_policy_callback() {
    return [](const PublicState&, const EventDecision& decision) -> int {
        REQUIRE(decision.n_options > 0);
        if (decision.kind == DecisionKind::SmallChoice) {
            return 0;
        }

        int best_index = 0;
        int best_id = decision.eligible_ids[0];
        for (int idx = 1; idx < decision.n_options; ++idx) {
            if (decision.eligible_ids[idx] < best_id) {
                best_id = decision.eligible_ids[idx];
                best_index = idx;
            }
        }
        return best_index;
    };
}

template <size_t N>
int first_set_bit(const std::bitset<N>& bits, int start, const char* label) {
    for (int idx = start; idx < static_cast<int>(N); ++idx) {
        if (bits.test(static_cast<size_t>(idx))) {
            return idx;
        }
    }
    FAIL(std::string("empty DecisionFrame mask for ") + label);
    return 0;
}

FrameAction deterministic_frame_action(const DecisionFrame& frame) {
    switch (frame.kind) {
        case FrameKind::SmallChoice:
        case FrameKind::CancelChoice:
        case FrameKind::DeferredOps:
            REQUIRE(frame.eligible_n > 0);
            return FrameAction{.option_index = 0};

        case FrameKind::CountryPick:
        case FrameKind::FreeOpsInfluence:
        case FrameKind::NoradInfluence:
        case FrameKind::SetupPlacement:
            return FrameAction{
                .country_id = static_cast<CountryId>(first_set_bit(frame.eligible_countries, 0, "eligible_countries")),
            };

        case FrameKind::CardSelect:
        case FrameKind::ForcedDiscard:
            return FrameAction{
                .card_id = static_cast<CardId>(first_set_bit(frame.eligible_cards, 1, "eligible_cards")),
            };

        case FrameKind::TopLevelAR:
        case FrameKind::Headline:
            FAIL("unsupported pending DecisionFrame kind in frame parity test");
            return FrameAction{};
    }

    FAIL("unknown pending DecisionFrame kind in frame parity test");
    return FrameAction{};
}

SubframePolicyFn deterministic_subframe_policy() {
    return [](const GameState&, const DecisionFrame& frame) {
        return deterministic_frame_action(frame);
    };
}

std::string end_reason_for_test(const GameState& gs, std::optional<Side> winner, CardId card_id = 0) {
    const auto& pub = gs.pub;
    if (pub.defcon <= 1) {
        return "defcon1";
    }
    if (card_id == 105) {
        return "wargames";
    }
    if (winner.has_value()) {
        return gs.scoring_auto_win ? "europe_control" : "vp_threshold";
    }
    return "vp_threshold";
}

std::optional<GameResult> end_of_turn_for_test(GameState& gs, int turn) {
    gs.phase = GamePhase::Cleanup;

    const auto defcon = gs.pub.defcon;
    for (const auto side : {Side::USSR, Side::US}) {
        const auto shortfall = std::max(0, defcon - gs.pub.milops[to_index(side)]);
        if (shortfall == 0) {
            continue;
        }
        if (side == Side::USSR) {
            gs.pub.vp -= shortfall;
        } else {
            gs.pub.vp += shortfall;
        }
    }

    auto [over, winner] = check_vp_win(gs.pub);
    if (over) {
        return GameResult{.winner = winner, .final_vp = gs.pub.vp, .end_turn = gs.pub.turn, .end_reason = "vp"};
    }

    gs.pub.defcon = std::min(5, gs.pub.defcon + 1);
    gs.pub.milops = {0, 0};
    gs.pub.space_attempts = {0, 0};
    gs.pub.ops_modifier = {0, 0};
    gs.pub.vietnam_revolts_active = false;
    gs.pub.north_sea_oil_extra_ar = false;
    gs.pub.glasnost_free_ops = 0;
    gs.pub.cuban_missile_crisis_active = false;
    gs.pub.chernobyl_blocked_region.reset();
    gs.pub.latam_coup_bonus.reset();

    if (turn == kMaxTurnsForTest) {
        auto final = apply_final_scoring(gs.pub);
        gs.pub.vp += final.vp_delta;
        if (final.game_over) {
            return GameResult{
                .winner = final.winner,
                .final_vp = gs.pub.vp,
                .end_turn = turn,
                .end_reason = "europe_control",
            };
        }
        std::tie(over, winner) = check_vp_win(gs.pub);
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = turn,
                .end_reason = "vp_threshold",
            };
        }
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
            if (!gs.hands[to_index(side)].test(static_cast<size_t>(card_id))) {
                continue;
            }
            if (card_spec(static_cast<CardId>(card_id)).is_scoring) {
                return GameResult{
                    .winner = other_side(side),
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = "scoring_card_held",
                };
            }
        }
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
            if (gs.hands[to_index(side)].test(static_cast<size_t>(card_id))) {
                gs.pub.discard.set(static_cast<size_t>(card_id));
            }
        }
        gs.hands[to_index(side)].reset();
    }

    return std::nullopt;
}

void run_deterministic_setup(GameState& gs) {
    gs.phase = GamePhase::Setup;
    for (const auto side : {Side::USSR, Side::US}) {
        gs.pub.phasing = side;
        const auto side_idx = to_index(side);
        const auto target = side == Side::USSR
            ? *std::min_element(kSetupEasternBlocIds.begin(), kSetupEasternBlocIds.end())
            : *std::min_element(kSetupWesternEuropeIds.begin(), kSetupWesternEuropeIds.end());
        while (gs.setup_influence_remaining[static_cast<size_t>(side_idx)] > 0) {
            gs.pub.set_influence(side, target, gs.pub.influence_of(side, target) + 1);
            --gs.setup_influence_remaining[static_cast<size_t>(side_idx)];
        }
    }
    gs.phase = GamePhase::Headline;
}

std::tuple<bool, std::optional<Side>> apply_top_level_for_test(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    ExecutionPath path,
    const PolicyCallbackFn& policy_cb,
    const SubframePolicyFn& sub_policy
) {
    if (path == ExecutionPath::LegacyPolicyCallback) {
        auto [new_pub, over, winner] = apply_action_live(gs, action, side, rng, &policy_cb, false, nullptr);
        (void)new_pub;
        return {over, winner};
    }

    auto result = engine_step_toplevel(gs, action, side, rng);
    int subframe_steps = 0;
    for (auto frame = engine_peek(gs); frame.has_value(); frame = engine_peek(gs)) {
        REQUIRE(subframe_steps < 512);
        result = engine_step_subframe(gs, sub_policy(gs, *frame), rng);
        ++subframe_steps;
    }
    return {result.game_over || gs.game_over, result.winner.has_value() ? result.winner : gs.winner};
}

std::tuple<bool, std::optional<Side>> apply_headline_for_test(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    ExecutionPath path,
    const PolicyCallbackFn& policy_cb,
    const SubframePolicyFn& sub_policy
) {
    if (path == ExecutionPath::LegacyPolicyCallback) {
        auto [new_pub, over, winner] = apply_headline_event_with_hands(gs, action, side, rng, &policy_cb, nullptr);
        (void)new_pub;
        return {over, winner};
    }

    gs.frame_stack.clear();
    const auto previous_frame_stack_mode = gs.frame_stack_mode;
    gs.frame_stack_mode = true;
    auto [new_pub, over, winner] = apply_headline_event_with_hands(gs, action, side, rng, nullptr, &gs.frame_stack);
    gs.frame_stack_mode = previous_frame_stack_mode;
    (void)new_pub;

    StepResult result{
        .pushed_subframe = !gs.frame_stack.empty(),
        .side_changed = false,
        .game_over = over,
        .winner = winner,
    };
    int subframe_steps = 0;
    for (auto frame = engine_peek(gs); frame.has_value(); frame = engine_peek(gs)) {
        REQUIRE(subframe_steps < 512);
        result = engine_step_subframe(gs, sub_policy(gs, *frame), rng);
        ++subframe_steps;
    }
    return {result.game_over || gs.game_over, result.winner.has_value() ? result.winner : gs.winner};
}

std::optional<GameResult> resolve_pre_action_hooks_for_test(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn& policy_cb
) {
    if (auto cmc_result = resolve_cuban_missile_crisis_cancel_live(gs, side, rng, &policy_cb); cmc_result.has_value()) {
        auto& [new_pub, over, winner] = *cmc_result;
        (void)new_pub;
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = end_reason_for_test(gs, winner),
            };
        }
        return std::nullopt;
    }

    if (auto trap_result = resolve_trap_ar_live(gs, side, rng, &policy_cb); trap_result.has_value()) {
        auto& [new_pub, over, winner] = *trap_result;
        (void)new_pub;
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = end_reason_for_test(gs, winner),
            };
        }
        return std::nullopt;
    }

    return std::nullopt;
}

void record_trace(GameRun& run, const GameState& gs, Side side, const ActionEncoding& action) {
    run.trace.push_back(TraceEntry{
        .turn = gs.pub.turn,
        .ar = gs.pub.ar,
        .side = side,
        .action = action,
        .state_hash = per_ar_state_hash(gs),
    });
}

std::optional<GameResult> run_headline_phase_for_test(
    GameState& gs,
    Pcg64Rng& rng,
    ExecutionPath path,
    const PolicyCallbackFn& policy_cb,
    const SubframePolicyFn& sub_policy,
    GameRun& run
) {
    gs.phase = GamePhase::Headline;
    gs.pub.ar = 0;

    struct PendingHeadline {
        Side side = Side::USSR;
        ActionEncoding action;
    };

    std::array<std::optional<PendingHeadline>, 2> chosen = {};
    for (const auto side : {Side::USSR, Side::US}) {
        gs.pub.phasing = side;
        const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
        auto headline_pub = gs.pub;
        headline_pub.ar = 0;
        auto cards = legal_cards(gs.hands[to_index(side)], headline_pub, side, holds_china);
        cards.erase(std::remove(cards.begin(), cards.end(), kChinaCardId), cards.end());
        std::sort(cards.begin(), cards.end());
        if (cards.empty()) {
            continue;
        }
        ActionEncoding action{.card_id = cards.front(), .mode = ActionMode::Event, .targets = {}};
        gs.hands[to_index(side)].reset(action.card_id);
        chosen[to_index(side)] = PendingHeadline{.side = side, .action = action};
    }

    std::vector<PendingHeadline> ordered;
    for (const auto side : {Side::USSR, Side::US}) {
        if (chosen[to_index(side)].has_value()) {
            ordered.push_back(*chosen[to_index(side)]);
        }
    }

    if (chosen[to_index(Side::US)].has_value() && chosen[to_index(Side::US)]->action.card_id == 108) {
        if (chosen[to_index(Side::USSR)].has_value()) {
            gs.pub.discard.set(chosen[to_index(Side::USSR)]->action.card_id);
            ordered.erase(
                std::remove_if(
                    ordered.begin(),
                    ordered.end(),
                    [](const PendingHeadline& pending) { return pending.side == Side::USSR; }
                ),
                ordered.end()
            );
        }
    }

    std::sort(ordered.begin(), ordered.end(), [](const auto& lhs, const auto& rhs) {
        const auto lhs_ops = card_spec(lhs.action.card_id).ops;
        const auto rhs_ops = card_spec(rhs.action.card_id).ops;
        if (lhs_ops != rhs_ops) {
            return lhs_ops > rhs_ops;
        }
        return static_cast<int>(lhs.side) < static_cast<int>(rhs.side);
    });

    for (const auto& pending : ordered) {
        gs.pub.phasing = pending.side;
        auto [over, winner] = apply_headline_for_test(gs, pending.action, pending.side, rng, path, policy_cb, sub_policy);
        sync_china_for_test(gs);
        record_trace(run, gs, pending.side, pending.action);
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = end_reason_for_test(gs, winner, pending.action.card_id),
            };
        }
    }

    return std::nullopt;
}

std::optional<GameResult> run_one_action_slot_for_test(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    ExecutionPath path,
    const PolicyCallbackFn& policy_cb,
    const SubframePolicyFn& sub_policy,
    GameRun& run
) {
    gs.pub.phasing = side;
    if (auto result = resolve_pre_action_hooks_for_test(gs, side, rng, policy_cb); result.has_value()) {
        record_trace(run, gs, side, ActionEncoding{});
        return result;
    }

    const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
    auto& hand = gs.hands[to_index(side)];
    auto action = first_legal_action(gs.pub, hand, side, holds_china);
    if (!action.has_value()) {
        record_trace(run, gs, side, ActionEncoding{});
        return std::nullopt;
    }

    hand.reset(action->card_id);
    auto [over, winner] = apply_top_level_for_test(gs, *action, side, rng, path, policy_cb, sub_policy);
    sync_china_for_test(gs);
    record_trace(run, gs, side, *action);
    if (over) {
        return GameResult{
            .winner = winner,
            .final_vp = gs.pub.vp,
            .end_turn = gs.pub.turn,
            .end_reason = end_reason_for_test(gs, winner, action->card_id),
        };
    }

    if (side == Side::USSR && gs.pub.norad_active && gs.pub.defcon == 2) {
        if (auto norad = resolve_norad_live(gs, rng, &policy_cb); norad.has_value()) {
            auto& [norad_pub, norad_over, norad_winner] = *norad;
            (void)norad_pub;
            if (norad_over) {
                return GameResult{
                    .winner = norad_winner,
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = end_reason_for_test(gs, norad_winner),
                };
            }
        }
    }

    return std::nullopt;
}

std::optional<GameResult> run_action_rounds_for_test(
    GameState& gs,
    Pcg64Rng& rng,
    int total_ars,
    ExecutionPath path,
    const PolicyCallbackFn& policy_cb,
    const SubframePolicyFn& sub_policy,
    GameRun& run
) {
    gs.phase = GamePhase::ActionRound;
    for (int ar = 1; ar <= kSpaceShuttleArsForTest; ++ar) {
        gs.pub.ar = ar;
        for (const auto side : {Side::USSR, Side::US}) {
            if (ar > total_ars && gs.pub.space[to_index(side)] < kSpaceShuttleArsForTest) {
                continue;
            }
            if (auto result = run_one_action_slot_for_test(gs, side, rng, path, policy_cb, sub_policy, run); result.has_value()) {
                return result;
            }
        }
    }
    return std::nullopt;
}

std::optional<GameResult> run_extra_action_round_for_test(
    GameState& gs,
    Pcg64Rng& rng,
    ExecutionPath path,
    const PolicyCallbackFn& policy_cb,
    const SubframePolicyFn& sub_policy,
    GameRun& run
) {
    gs.pub.ar = std::max(gs.pub.ar, ars_for_turn(gs.pub.turn)) + 1;
    return run_one_action_slot_for_test(gs, Side::US, rng, path, policy_cb, sub_policy, run);
}

GameRun play_with_path(uint32_t seed, ExecutionPath path) {
    GameRun run;
    auto gs = reset_game(seed);
    Pcg64Rng rng(seed);
    const auto policy_cb = deterministic_policy_callback();
    const auto sub_policy = deterministic_subframe_policy();

    run_deterministic_setup(gs);

    for (int turn = 1; turn <= kMaxTurnsForTest; ++turn) {
        gs.pub.turn = turn;
        if (turn == kMidWarTurnForTest) {
            advance_to_mid_war(gs, rng);
        } else if (turn == kLateWarTurnForTest) {
            advance_to_late_war(gs, rng);
        }

        deal_cards(gs, Side::USSR, rng);
        deal_cards(gs, Side::US, rng);

        if (auto result = run_headline_phase_for_test(gs, rng, path, policy_cb, sub_policy, run); result.has_value()) {
            run.result = *result;
            return run;
        }
        if (auto result = run_action_rounds_for_test(gs, rng, ars_for_turn(turn), path, policy_cb, sub_policy, run); result.has_value()) {
            run.result = *result;
            return run;
        }
        if (gs.pub.north_sea_oil_extra_ar) {
            gs.pub.north_sea_oil_extra_ar = false;
            if (auto result = run_extra_action_round_for_test(gs, rng, path, policy_cb, sub_policy, run); result.has_value()) {
                run.result = *result;
                return run;
            }
        }
        if (gs.pub.glasnost_free_ops > 0) {
            resolve_glasnost_free_ops_live(gs.pub, rng, &policy_cb);
        }
        if (auto result = end_of_turn_for_test(gs, turn); result.has_value()) {
            run.result = *result;
            return run;
        }
    }

    if (gs.pub.vp < 0) {
        run.result = GameResult{.winner = Side::US, .final_vp = gs.pub.vp, .end_turn = kMaxTurnsForTest, .end_reason = "turn_limit"};
        return run;
    }
    run.result = GameResult{.winner = Side::USSR, .final_vp = gs.pub.vp, .end_turn = kMaxTurnsForTest, .end_reason = "turn_limit"};
    return run;
}

GameRun play_with_policy_cb_trace(uint32_t seed) {
    return play_with_path(seed, ExecutionPath::LegacyPolicyCallback);
}

GameRun play_with_sub_policy_trace(uint32_t seed) {
    return play_with_path(seed, ExecutionPath::SubframePolicy);
}

GameResult play_with_policy_cb(uint32_t seed) {
    return play_with_policy_cb_trace(seed).result;
}

GameResult play_with_sub_policy(uint32_t seed) {
    return play_with_sub_policy_trace(seed).result;
}

void assert_game_result_equal(uint32_t seed, const GameResult& legacy, const GameResult& subframe) {
    INFO("seed=" << seed
        << " legacy_winner=" << winner_to_string(legacy.winner)
        << " subframe_winner=" << winner_to_string(subframe.winner));
    REQUIRE(legacy.winner == subframe.winner);
    INFO("seed=" << seed << " legacy_final_vp=" << legacy.final_vp << " subframe_final_vp=" << subframe.final_vp);
    REQUIRE(legacy.final_vp == subframe.final_vp);
    INFO("seed=" << seed << " legacy_end_turn=" << legacy.end_turn << " subframe_end_turn=" << subframe.end_turn);
    REQUIRE(legacy.end_turn == subframe.end_turn);
    INFO("seed=" << seed << " legacy_end_reason=" << legacy.end_reason << " subframe_end_reason=" << subframe.end_reason);
    REQUIRE(legacy.end_reason == subframe.end_reason);
}

void assert_trace_equal(uint32_t seed, const GameRun& legacy, const GameRun& subframe) {
    INFO("seed=" << seed << " legacy_trace_size=" << legacy.trace.size() << " subframe_trace_size=" << subframe.trace.size());

    const auto shared_size = std::min(legacy.trace.size(), subframe.trace.size());
    for (size_t idx = 0; idx < shared_size; ++idx) {
        const auto& lhs = legacy.trace[idx];
        const auto& rhs = subframe.trace[idx];
        std::string previous = "none";
        if (idx > 0) {
            const auto& prev_lhs = legacy.trace[idx - 1];
            const auto& prev_rhs = subframe.trace[idx - 1];
            std::ostringstream prev_out;
            prev_out
                << "legacy_prev=t" << prev_lhs.turn << "/AR" << prev_lhs.ar << "/" << side_to_string(prev_lhs.side)
                << " {" << action_to_string(prev_lhs.action) << "}"
                << " subframe_prev=t" << prev_rhs.turn << "/AR" << prev_rhs.ar << "/" << side_to_string(prev_rhs.side)
                << " {" << action_to_string(prev_rhs.action) << "}";
            previous = prev_out.str();
        }
        INFO("seed=" << seed
            << " ar_index=" << idx
            << " legacy_slot=t" << lhs.turn << "/AR" << lhs.ar << "/" << side_to_string(lhs.side)
            << " subframe_slot=t" << rhs.turn << "/AR" << rhs.ar << "/" << side_to_string(rhs.side)
            << " legacy_hash=" << hash_to_string(lhs.state_hash)
            << " subframe_hash=" << hash_to_string(rhs.state_hash)
            << " legacy_action={" << action_to_string(lhs.action) << "}"
            << " subframe_action={" << action_to_string(rhs.action) << "}"
            << " previous=" << previous);
        REQUIRE(lhs.turn == rhs.turn);
        REQUIRE(lhs.ar == rhs.ar);
        REQUIRE(lhs.side == rhs.side);
        REQUIRE(lhs.action == rhs.action);
        REQUIRE(lhs.state_hash == rhs.state_hash);
    }

    REQUIRE(legacy.trace.size() == subframe.trace.size());
}

struct FrameParityTest {
    static void assert_seed(uint32_t seed) {
        const auto legacy = play_with_policy_cb_trace(seed);
        const auto subframe = play_with_sub_policy_trace(seed);
        assert_trace_equal(seed, legacy, subframe);
        assert_game_result_equal(seed, legacy.result, subframe.result);
    }
};

struct FrameParityScript {
    std::vector<int> top_level_indices;
    std::vector<int> subframe_indices;
    std::vector<FrameAction> subframe_actions;
};

struct FrameParityHarnessRun {
    GameResult result;
    std::vector<TraceEntry> trace;
    FrameParityScript script;
};

struct FrameParityReplayCursor {
    size_t top_level = 0;
    size_t subframe = 0;
};

int first_frame_order_callback_index(const EventDecision& decision) {
    REQUIRE(decision.n_options > 0);
    if (decision.kind == DecisionKind::SmallChoice) {
        return 0;
    }

    int callback_index = 0;
    int best_id = decision.eligible_ids[0];
    for (int idx = 1; idx < decision.n_options; ++idx) {
        if (decision.eligible_ids[idx] < best_id) {
            best_id = decision.eligible_ids[idx];
            callback_index = idx;
        }
    }
    return callback_index;
}

PolicyCallbackFn first_legal_policy_callback() {
    return [](const PublicState&, const EventDecision& decision) -> int {
        return first_frame_order_callback_index(decision);
    };
}

struct FirstLegalPolicy {
    std::optional<ActionEncoding> operator()(
        const PublicState& pub,
        const CardSet& hand,
        bool holds_china
    ) const {
        return first_legal_action(pub, hand, pub.phasing, holds_china);
    }
};

int nth_set_bit_or_fail(const std::bitset<kCountrySlots>& bits, int action_index, const char* label) {
    REQUIRE(action_index >= 0);
    int seen = 0;
    for (int idx = 0; idx < static_cast<int>(bits.size()); ++idx) {
        if (!bits.test(static_cast<size_t>(idx))) {
            continue;
        }
        if (seen == action_index) {
            return idx;
        }
        ++seen;
    }
    FAIL(std::string("DecisionFrame action index out of range for ") + label);
    return 0;
}

int nth_card_bit_or_fail(const CardSet& bits, int action_index, const char* label) {
    REQUIRE(action_index >= 0);
    int seen = 0;
    for (int idx = 1; idx < static_cast<int>(bits.size()); ++idx) {
        if (!bits.test(static_cast<size_t>(idx))) {
            continue;
        }
        if (seen == action_index) {
            return idx;
        }
        ++seen;
    }
    FAIL(std::string("DecisionFrame action index out of range for ") + label);
    return 0;
}

FrameAction frame_action_at_index(const DecisionFrame& frame, int action_index) {
    switch (frame.kind) {
        case FrameKind::SmallChoice:
        case FrameKind::CancelChoice:
        case FrameKind::DeferredOps:
            REQUIRE(action_index >= 0);
            REQUIRE(action_index < frame.eligible_n);
            return FrameAction{.option_index = action_index};

        case FrameKind::CountryPick:
        case FrameKind::FreeOpsInfluence:
        case FrameKind::NoradInfluence:
        case FrameKind::SetupPlacement:
            return FrameAction{
                .country_id = static_cast<CountryId>(
                    nth_set_bit_or_fail(frame.eligible_countries, action_index, "eligible_countries")
                ),
            };

        case FrameKind::CardSelect:
        case FrameKind::ForcedDiscard:
            return FrameAction{
                .card_id = static_cast<CardId>(
                    nth_card_bit_or_fail(frame.eligible_cards, action_index, "eligible_cards")
                ),
            };

        case FrameKind::TopLevelAR:
        case FrameKind::Headline:
            FAIL("unsupported pending DecisionFrame kind in FrameParityHarness");
            return FrameAction{};
    }

    FAIL("unknown pending DecisionFrame kind in FrameParityHarness");
    return FrameAction{};
}

std::optional<ActionEncoding> choose_harness_action(
    const GameState& gs,
    Side side,
    int action_index
) {
    REQUIRE(action_index == 0);
    const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
    return FirstLegalPolicy{}(gs.pub, gs.hands[to_index(side)], holds_china);
}

std::optional<ActionEncoding> choose_harness_headline_action(
    const GameState& gs,
    Side side,
    int action_index
) {
    REQUIRE(action_index == 0);
    const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
    auto cards = legal_cards(gs.hands[to_index(side)], gs.pub, side, holds_china);
    cards.erase(std::remove(cards.begin(), cards.end(), kChinaCardId), cards.end());
    std::sort(cards.begin(), cards.end());
    if (cards.empty()) {
        return std::nullopt;
    }
    return ActionEncoding{.card_id = cards.front(), .mode = ActionMode::Event, .targets = {}};
}

std::tuple<bool, std::optional<Side>> apply_harness_policy_callback_action(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    FrameParityScript& script
) {
    std::vector<DecisionFrame> frames;
    const auto policy_cb = first_legal_policy_callback();
    auto [new_pub, over, winner] = apply_action_live(gs, action, side, rng, &policy_cb, false, &frames);
    (void)new_pub;
    for (const auto& frame : frames) {
        script.subframe_indices.push_back(0);
        script.subframe_actions.push_back(frame_action_at_index(frame, 0));
    }
    return {over, winner};
}

std::tuple<bool, std::optional<Side>> apply_harness_frame_stack_action(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const FrameParityScript& script,
    FrameParityReplayCursor& cursor
) {
    auto result = engine_step_toplevel(gs, action, side, rng);
    int subframe_steps = 0;
    while (auto frame = engine_peek(gs)) {
        REQUIRE(subframe_steps < 512);
        const auto action_index = cursor.subframe < script.subframe_indices.size()
            ? script.subframe_indices[cursor.subframe]
            : 0;
        const auto frame_action = cursor.subframe < script.subframe_actions.size()
            ? script.subframe_actions[cursor.subframe]
            : frame_action_at_index(*frame, action_index);
        ++cursor.subframe;
        result = engine_step_subframe(gs, frame_action, rng);
        ++subframe_steps;
    }
    return {result.game_over || gs.game_over, result.winner.has_value() ? result.winner : gs.winner};
}

std::tuple<bool, std::optional<Side>> apply_harness_action(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    bool frame_stack_path,
    FrameParityScript& script,
    FrameParityReplayCursor& cursor
) {
    if (!frame_stack_path) {
        return apply_harness_policy_callback_action(gs, action, side, rng, script);
    }
    return apply_harness_frame_stack_action(gs, action, side, rng, script, cursor);
}

std::tuple<bool, std::optional<Side>> apply_harness_policy_callback_headline(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    FrameParityScript& script
) {
    std::vector<DecisionFrame> frames;
    const auto policy_cb = first_legal_policy_callback();
    auto [new_pub, over, winner] = apply_headline_event_with_hands(gs, action, side, rng, &policy_cb, &frames);
    (void)new_pub;
    for (const auto& frame : frames) {
        script.subframe_indices.push_back(0);
        script.subframe_actions.push_back(frame_action_at_index(frame, 0));
    }
    return {over, winner};
}

std::tuple<bool, std::optional<Side>> apply_harness_frame_stack_headline(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const FrameParityScript& script,
    FrameParityReplayCursor& cursor
) {
    gs.frame_stack.clear();
    const auto previous_frame_stack_mode = gs.frame_stack_mode;
    gs.frame_stack_mode = true;
    auto [new_pub, over, winner] = apply_headline_event_with_hands(gs, action, side, rng, nullptr, &gs.frame_stack);
    gs.frame_stack_mode = previous_frame_stack_mode;
    (void)new_pub;

    StepResult result{
        .pushed_subframe = !gs.frame_stack.empty(),
        .side_changed = false,
        .game_over = over,
        .winner = winner,
    };
    int subframe_steps = 0;
    while (auto frame = engine_peek(gs)) {
        REQUIRE(subframe_steps < 512);
        const auto action_index = cursor.subframe < script.subframe_indices.size()
            ? script.subframe_indices[cursor.subframe]
            : 0;
        const auto frame_action = cursor.subframe < script.subframe_actions.size()
            ? script.subframe_actions[cursor.subframe]
            : frame_action_at_index(*frame, action_index);
        ++cursor.subframe;
        result = engine_step_subframe(gs, frame_action, rng);
        ++subframe_steps;
    }
    return {result.game_over || gs.game_over, result.winner.has_value() ? result.winner : gs.winner};
}

std::tuple<bool, std::optional<Side>> apply_harness_headline(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    bool frame_stack_path,
    FrameParityScript& script,
    FrameParityReplayCursor& cursor
) {
    if (!frame_stack_path) {
        return apply_harness_policy_callback_headline(gs, action, side, rng, script);
    }
    return apply_harness_frame_stack_headline(gs, action, side, rng, script, cursor);
}

void record_harness_trace(
    FrameParityHarnessRun& run,
    const GameState& gs,
    Side side,
    const ActionEncoding& action
) {
    run.trace.push_back(TraceEntry{
        .turn = gs.pub.turn,
        .ar = gs.pub.ar,
        .side = side,
        .action = action,
        .state_hash = per_ar_state_hash(gs),
    });
}

std::optional<GameResult> run_harness_headline_phase(
    GameState& gs,
    Pcg64Rng& rng,
    bool frame_stack_path,
    FrameParityHarnessRun& run,
    FrameParityReplayCursor& cursor
) {
    gs.phase = GamePhase::Headline;
    gs.pub.ar = 0;

    struct PendingHeadline {
        Side side = Side::USSR;
        ActionEncoding action;
    };

    std::array<std::optional<PendingHeadline>, 2> chosen = {};
    for (const auto side : {Side::USSR, Side::US}) {
        gs.pub.phasing = side;
        const int action_index = frame_stack_path
            ? run.script.top_level_indices.at(cursor.top_level++)
            : 0;
        if (!frame_stack_path) {
            run.script.top_level_indices.push_back(action_index);
        }
        auto action = choose_harness_headline_action(gs, side, action_index);
        if (!action.has_value()) {
            continue;
        }
        gs.hands[to_index(side)].reset(action->card_id);
        chosen[to_index(side)] = PendingHeadline{.side = side, .action = *action};
    }

    std::vector<PendingHeadline> ordered;
    for (const auto side : {Side::USSR, Side::US}) {
        if (chosen[to_index(side)].has_value()) {
            ordered.push_back(*chosen[to_index(side)]);
        }
    }

    if (chosen[to_index(Side::US)].has_value() && chosen[to_index(Side::US)]->action.card_id == 108) {
        if (chosen[to_index(Side::USSR)].has_value()) {
            gs.pub.discard.set(chosen[to_index(Side::USSR)]->action.card_id);
            ordered.erase(
                std::remove_if(
                    ordered.begin(),
                    ordered.end(),
                    [](const PendingHeadline& pending) { return pending.side == Side::USSR; }
                ),
                ordered.end()
            );
        }
    }

    std::sort(ordered.begin(), ordered.end(), [](const auto& lhs, const auto& rhs) {
        const auto lhs_ops = card_spec(lhs.action.card_id).ops;
        const auto rhs_ops = card_spec(rhs.action.card_id).ops;
        if (lhs_ops != rhs_ops) {
            return lhs_ops > rhs_ops;
        }
        return static_cast<int>(lhs.side) < static_cast<int>(rhs.side);
    });

    for (const auto& pending : ordered) {
        gs.pub.phasing = pending.side;
        auto [over, winner] = apply_harness_headline(
            gs,
            pending.action,
            pending.side,
            rng,
            frame_stack_path,
            run.script,
            cursor
        );
        sync_china_for_test(gs);
        record_harness_trace(run, gs, pending.side, pending.action);
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = end_reason_for_test(gs, winner, pending.action.card_id),
            };
        }
    }

    return std::nullopt;
}

std::optional<GameResult> run_harness_action_slot(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    bool frame_stack_path,
    FrameParityHarnessRun& run,
    FrameParityReplayCursor& cursor
) {
    gs.pub.phasing = side;
    const int action_index = frame_stack_path
        ? run.script.top_level_indices.at(cursor.top_level++)
        : 0;
    auto action = choose_harness_action(gs, side, action_index);
    if (!frame_stack_path) {
        run.script.top_level_indices.push_back(action_index);
    }
    if (!action.has_value()) {
        record_harness_trace(run, gs, side, ActionEncoding{});
        return std::nullopt;
    }

    gs.hands[to_index(side)].reset(action->card_id);
    auto [over, winner] = apply_harness_action(
        gs,
        *action,
        side,
        rng,
        frame_stack_path,
        run.script,
        cursor
    );
    sync_china_for_test(gs);
    record_harness_trace(run, gs, side, *action);
    if (over) {
        return GameResult{
            .winner = winner,
            .final_vp = gs.pub.vp,
            .end_turn = gs.pub.turn,
            .end_reason = end_reason_for_test(gs, winner, action->card_id),
        };
    }
    return std::nullopt;
}

std::optional<GameResult> run_harness_action_rounds(
    GameState& gs,
    Pcg64Rng& rng,
    bool frame_stack_path,
    FrameParityHarnessRun& run,
    FrameParityReplayCursor& cursor
) {
    gs.phase = GamePhase::ActionRound;
    for (int ar = 1; ar <= ars_for_turn(gs.pub.turn); ++ar) {
        gs.pub.ar = ar;
        for (const auto side : {Side::USSR, Side::US}) {
            if (auto result = run_harness_action_slot(gs, side, rng, frame_stack_path, run, cursor);
                result.has_value()) {
                return result;
            }
        }
    }
    return std::nullopt;
}

FrameParityHarnessRun run_frame_parity_harness(
    uint32_t seed,
    bool frame_stack_path,
    const FrameParityScript* replay_script = nullptr
) {
    FrameParityHarnessRun run;
    if (replay_script != nullptr) {
        run.script = *replay_script;
    }
    FrameParityReplayCursor cursor;
    auto gs = reset_game(seed);
    Pcg64Rng rng(seed);
    run_deterministic_setup(gs);

    constexpr int kHarnessTurns = 3;
    for (int turn = 1; turn <= kHarnessTurns; ++turn) {
        gs.pub.turn = turn;
        deal_cards(gs, Side::USSR, rng);
        deal_cards(gs, Side::US, rng);

        if (auto result = run_harness_headline_phase(gs, rng, frame_stack_path, run, cursor);
            result.has_value()) {
            run.result = *result;
            return run;
        }
        if (auto result = run_harness_action_rounds(gs, rng, frame_stack_path, run, cursor);
            result.has_value()) {
            run.result = *result;
            return run;
        }
        if (auto result = end_of_turn_for_test(gs, turn); result.has_value()) {
            run.result = *result;
            return run;
        }
    }

    run.result = GameResult{
        .winner = gs.pub.vp >= 0 ? Side::USSR : Side::US,
        .final_vp = gs.pub.vp,
        .end_turn = kHarnessTurns,
        .end_reason = "harness_turn_limit",
    };
    if (frame_stack_path) {
        REQUIRE(cursor.top_level == run.script.top_level_indices.size());
    }
    return run;
}

}  // namespace

TEST_CASE("FrameParityHarness", "[frame_parity]") {
    constexpr uint32_t kSeed = 12345;

    const auto policy_callback = run_frame_parity_harness(kSeed, false);
    const auto frame_stack = run_frame_parity_harness(kSeed, true, &policy_callback.script);

    const GameRun policy_trace{
        .result = policy_callback.result,
        .trace = policy_callback.trace,
    };
    const GameRun frame_trace{
        .result = frame_stack.result,
        .trace = frame_stack.trace,
    };
    assert_trace_equal(kSeed, policy_trace, frame_trace);
    assert_game_result_equal(kSeed, policy_callback.result, frame_stack.result);
}

TEST_CASE("frame_parity FrameParity SingleGame_Seed0", "[frame_parity]") {
    FrameParityTest::assert_seed(0);
}

TEST_CASE("frame_parity FrameParity Seeds0To49", "[frame_parity]") {
    for (uint32_t seed = 0; seed < 50; ++seed) {
        DYNAMIC_SECTION("seed " << seed) {
            FrameParityTest::assert_seed(seed);
        }
    }
}

TEST_CASE("frame_parity DISABLED_FrameParity Bulk500Seeds", "[frame_parity][.]") {
    for (uint32_t seed = 0; seed < 500; ++seed) {
        DYNAMIC_SECTION("seed " << seed) {
            FrameParityTest::assert_seed(seed);
        }
    }
}
