// Native whole-game loop implementation, including headline handling, extra
// ARs, trap/NORAD hooks, and traced execution for parity work.

#include "game_loop.hpp"

#include <algorithm>
#include <array>
#include <cstdio>
#include <cstdlib>
#include <string>

#include "adjacency.hpp"
#include "dice.hpp"
#include "hand_ops.hpp"
#include "human_openings.hpp"

#include "game_data.hpp"
#include "legal_actions.hpp"
#include "rule_queries.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts {
namespace {

constexpr int kMidWarTurn = 4;
constexpr int kLateWarTurn = 8;
constexpr int kMaxTurns = 10;
constexpr int kSpaceShuttleArs = 8;

struct PendingHeadline {
    Side side = Side::USSR;
    bool holds_china = false;
    CardSet hand_snapshot;
    ActionEncoding action;
};

// Keep China-card ownership booleans synchronized with the public-state owner.
void sync_china(GameState& gs) {
    gs.ussr_holds_china = gs.pub.china_held_by == Side::USSR;
    gs.us_holds_china = gs.pub.china_held_by == Side::US;
}

float normalized_exploration_rate(const GameLoopConfig& config) {
    return std::clamp(config.exploration_rate, 0.0f, 1.0f);
}

std::optional<ActionEncoding> choose_headline_action_with_config(
    const PolicyFn& policy,
    const PublicState& pub,
    const CardSet& hand,
    Side side,
    bool holds_china,
    Pcg64Rng& rng,
    const GameLoopConfig& config
) {
    const auto exploration_rate = normalized_exploration_rate(config);
    if (exploration_rate > 0.0f && rng.bernoulli(static_cast<double>(exploration_rate))) {
        auto cards = legal_cards(hand, pub, side, holds_china);
        cards.erase(std::remove(cards.begin(), cards.end(), kChinaCardId), cards.end());
        if (cards.empty()) {
            return std::nullopt;
        }
        return ActionEncoding{
            .card_id = cards[rng.choice_index(cards.size())],
            .mode = ActionMode::Event,
            .targets = {},
        };
    }
    return policy(pub, hand, holds_china, rng);
}

std::optional<ActionEncoding> choose_action_with_config(
    const PolicyFn& policy,
    const PublicState& pub,
    const CardSet& hand,
    Side side,
    bool holds_china,
    Pcg64Rng& rng,
    const GameLoopConfig& config
) {
    const auto exploration_rate = normalized_exploration_rate(config);
    if (exploration_rate > 0.0f && rng.bernoulli(static_cast<double>(exploration_rate))) {
        auto actions = enumerate_actions(hand, pub, side, holds_china);
        if (!actions.empty()) {
            return actions[rng.choice_index(actions.size())];
        }
    }
    return policy(pub, hand, holds_china, rng);
}

std::vector<CountryId> filtered_influence_targets(const PublicState& pub, Side side) {
    auto accessible = accessible_countries(side, pub, ActionMode::Influence);
    accessible.erase(
        std::remove_if(
            accessible.begin(),
            accessible.end(),
            [&](CountryId cid) { return is_chernobyl_blocked(pub, side, cid); }
        ),
        accessible.end()
    );
    return accessible;
}

void apply_influence_budget_impl(
    PublicState& pub,
    Side side,
    int ops_budget,
    CardId context_card_id,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
) {
    const auto opponent = other_side(side);
    while (ops_budget > 0) {
        auto accessible = filtered_influence_targets(pub, side);
        accessible.erase(
            std::remove_if(
                accessible.begin(),
                accessible.end(),
                [&](CountryId cid) { return (controls_country(opponent, cid, pub) ? 2 : 1) > ops_budget; }
            ),
            accessible.end()
        );
        if (accessible.empty()) {
            return;
        }

        const auto target = choose_country(pub, context_card_id, side, accessible, rng, policy_cb);
        const auto cost = controls_country(opponent, target, pub) ? 2 : 1;
        if (cost > ops_budget) {
            return;
        }
        pub.set_influence(side, target, pub.influence_of(side, target) + 1);
        ops_budget -= cost;
    }
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_norad(
    GameState& gs,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb = nullptr
) {
    std::vector<CountryId> eligible;
    for (const auto cid : all_country_ids()) {
        if (gs.pub.influence_of(Side::US, cid) > 0) {
            eligible.push_back(cid);
        }
    }
    if (eligible.empty()) {
        return std::nullopt;
    }
    const auto target = choose_country(gs.pub, 106, Side::US, eligible, rng, policy_cb);
    gs.pub.set_influence(Side::US, target, gs.pub.influence_of(Side::US, target) + 1);
    const auto [over, winner] = check_vp_win(gs.pub);
    return std::tuple{gs.pub, over, winner};
}

std::string end_reason(const PublicState& pub, std::optional<Side> winner, int card_id = -1) {
    if (pub.defcon <= 1) {
        return "defcon1";
    }
    if (card_id == kWargamesCardId) {
        return "wargames";
    }
    if (winner.has_value()) {
        return "europe_control";
    }
    return "vp_threshold";
}

std::optional<GameResult> run_headline_phase(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    gs.phase = GamePhase::Headline;
    gs.pub.ar = 0;

    std::array<std::optional<PendingHeadline>, 2> chosen = {};
    for (const auto side : {Side::USSR, Side::US}) {
        gs.pub.phasing = side;
        const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
        const auto hand_snapshot = gs.hands[to_index(side)];
        auto headline_pub = gs.pub;
        headline_pub.ar = 0;
        auto action = choose_headline_action_with_config(
            side == Side::USSR ? ussr_policy : us_policy,
            headline_pub,
            gs.hands[to_index(side)],
            side,
            holds_china,
            rng,
            config
        );
        if (!action.has_value()) {
            continue;
        }
        action->mode = ActionMode::Event;
        action->targets.clear();
        if (gs.hands[to_index(side)].test(action->card_id)) {
            gs.hands[to_index(side)].reset(action->card_id);
        }
        chosen[to_index(side)] = PendingHeadline{
            .side = side,
            .holds_china = holds_china,
            .hand_snapshot = hand_snapshot,
            .action = *action,
        };
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
        // USSR (side=0) resolves first on headline tiebreak per official TS rules.
        return static_cast<int>(lhs.side) < static_cast<int>(rhs.side);
    });

    for (const auto& pending : ordered) {
        const auto side = pending.side;
        const auto& action = pending.action;
        const auto pub_snapshot = gs.pub;
        const auto deck_snapshot = gs.deck;
        const auto ussr_holds_china_snap = gs.ussr_holds_china;
        const auto us_holds_china_snap = gs.us_holds_china;
        const auto opp = side == Side::USSR ? Side::US : Side::USSR;
        const CardSet opp_hand_snap = chosen[to_index(opp)].has_value()
            ? chosen[to_index(opp)]->hand_snapshot
            : gs.hands[to_index(opp)];
        const auto vp_before = gs.pub.vp;
        const auto defcon_before = gs.pub.defcon;
        gs.pub.phasing = side;
        auto [new_pub, over, winner] = apply_action_with_hands(gs, action, side, rng);
        if (trace_steps != nullptr) {
            trace_steps->push_back(StepTrace{
                .turn = gs.pub.turn,
                .ar = 0,
                .side = side,
                .holds_china = pending.holds_china,
                .pub_snapshot = pub_snapshot,
                .hand_snapshot = pending.hand_snapshot,
                .action = action,
                .vp_before = vp_before,
                .vp_after = gs.pub.vp,
                .defcon_before = defcon_before,
                .defcon_after = gs.pub.defcon,
                .opp_hand_snapshot = opp_hand_snap,
                .deck_snapshot = deck_snapshot,
                .ussr_holds_china_snapshot = ussr_holds_china_snap,
                .us_holds_china_snapshot = us_holds_china_snap,
            });
        }
        sync_china(gs);
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = end_reason(gs.pub, winner, action.card_id),
            };
        }
    }

    return std::nullopt;
}

std::optional<GameResult> run_action_rounds(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    int total_ars,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    gs.phase = GamePhase::ActionRound;
    for (int ar = 1; ar <= kSpaceShuttleArs; ++ar) {
        gs.pub.ar = ar;
        for (const auto side : {Side::USSR, Side::US}) {
            if (ar > total_ars && gs.pub.space[to_index(side)] < kSpaceShuttleArs) {
                continue;
            }
            gs.pub.phasing = side;
            const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
            auto& hand = gs.hands[to_index(side)];
            if (auto cmc_result = resolve_cuban_missile_crisis_cancel(gs, side, rng); cmc_result.has_value()) {
                auto& [new_pub, over, winner] = *cmc_result;
                (void)new_pub;
                if (over) {
                    return GameResult{
                        .winner = winner,
                        .final_vp = gs.pub.vp,
                        .end_turn = gs.pub.turn,
                        .end_reason = end_reason(gs.pub, winner),
                    };
                }
                continue;
            }
            if (auto trap_result = resolve_trap_ar(gs, side, rng); trap_result.has_value()) {
                auto& [new_pub, over, winner] = *trap_result;
                (void)new_pub;
                if (over) {
                    return GameResult{
                        .winner = winner,
                        .final_vp = gs.pub.vp,
                        .end_turn = gs.pub.turn,
                        .end_reason = end_reason(gs.pub, winner),
                    };
                }
                continue;
            }
            if (!has_legal_action(hand, gs.pub, side, holds_china)) {
                continue;
            }
            auto action = choose_action_with_config(
                side == Side::USSR ? ussr_policy : us_policy,
                gs.pub,
                hand,
                side,
                holds_china,
                rng,
                config
            );
            if (!action.has_value()) {
                continue;
            }
            const auto pub_snapshot = gs.pub;
            const auto hand_snapshot = hand;
            const auto deck_snapshot_ar = gs.deck;
            const auto ussr_holds_china_snap_ar = gs.ussr_holds_china;
            const auto us_holds_china_snap_ar = gs.us_holds_china;
            const auto opp_ar = side == Side::USSR ? Side::US : Side::USSR;
            const CardSet opp_hand_snap_ar = gs.hands[to_index(opp_ar)];
            if (hand.test(action->card_id)) {
                hand.reset(action->card_id);
            }
            const auto vp_before = gs.pub.vp;
            const auto defcon_before = gs.pub.defcon;
            auto [new_pub, over, winner] = apply_action_with_hands(gs, *action, side, rng);
            if (trace_steps != nullptr) {
                trace_steps->push_back(StepTrace{
                    .turn = gs.pub.turn,
                    .ar = ar,
                    .side = side,
                    .holds_china = holds_china,
                    .pub_snapshot = pub_snapshot,
                    .hand_snapshot = hand_snapshot,
                    .action = *action,
                    .vp_before = vp_before,
                    .vp_after = gs.pub.vp,
                    .defcon_before = defcon_before,
                    .defcon_after = gs.pub.defcon,
                    .opp_hand_snapshot = opp_hand_snap_ar,
                    .deck_snapshot = deck_snapshot_ar,
                    .ussr_holds_china_snapshot = ussr_holds_china_snap_ar,
                    .us_holds_china_snapshot = us_holds_china_snap_ar,
                });
            }
            sync_china(gs);
            if (over) {
                return GameResult{
                    .winner = winner,
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = end_reason(gs.pub, winner, action->card_id),
                };
            }
            if (side == Side::USSR && gs.pub.norad_active && gs.pub.defcon == 2) {
                if (auto norad = resolve_norad(gs, rng); norad.has_value()) {
                    auto& [norad_pub, norad_over, norad_winner] = *norad;
                    (void)norad_pub;
                    if (norad_over) {
                        return GameResult{
                            .winner = norad_winner,
                            .final_vp = gs.pub.vp,
                            .end_turn = gs.pub.turn,
                            .end_reason = end_reason(gs.pub, norad_winner),
                        };
                    }
                }
            }
        }
    }
    return std::nullopt;
}

std::optional<GameResult> run_extra_action_round(
    GameState& gs,
    Side side,
    const PolicyFn& policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    gs.pub.ar = std::max(gs.pub.ar, ars_for_turn(gs.pub.turn)) + 1;
    gs.pub.phasing = side;
    const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
    auto& hand = gs.hands[to_index(side)];
    if (auto cmc_result = resolve_cuban_missile_crisis_cancel(gs, side, rng); cmc_result.has_value()) {
        auto& [new_pub, over, winner] = *cmc_result;
        (void)new_pub;
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = end_reason(gs.pub, winner),
            };
        }
        return std::nullopt;
    }
    if (hand.none()) {
        return std::nullopt;
    }
    if (auto trap_result = resolve_trap_ar(gs, side, rng); trap_result.has_value()) {
        auto& [new_pub, over, winner] = *trap_result;
        (void)new_pub;
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = gs.pub.vp,
                .end_turn = gs.pub.turn,
                .end_reason = end_reason(gs.pub, winner),
            };
        }
        return std::nullopt;
    }
    if (!has_legal_action(hand, gs.pub, side, holds_china)) {
        return std::nullopt;
    }
    auto action = choose_action_with_config(policy, gs.pub, hand, side, holds_china, rng, config);
    if (!action.has_value()) {
        return std::nullopt;
    }
    const auto pub_snapshot = gs.pub;
    const auto hand_snapshot = hand;
    const auto deck_snapshot_extra = gs.deck;
    const auto ussr_holds_china_snap_extra = gs.ussr_holds_china;
    const auto us_holds_china_snap_extra = gs.us_holds_china;
    const auto opp_extra = side == Side::USSR ? Side::US : Side::USSR;
    const CardSet opp_hand_snap_extra = gs.hands[to_index(opp_extra)];
    if (hand.test(action->card_id)) {
        hand.reset(action->card_id);
    }
    const auto vp_before = gs.pub.vp;
    const auto defcon_before = gs.pub.defcon;
    auto [new_pub, over, winner] = apply_action_with_hands(gs, *action, side, rng);
    if (trace_steps != nullptr) {
        trace_steps->push_back(StepTrace{
            .turn = gs.pub.turn,
            .ar = gs.pub.ar,
            .side = side,
            .holds_china = holds_china,
            .pub_snapshot = pub_snapshot,
            .hand_snapshot = hand_snapshot,
            .action = *action,
            .vp_before = vp_before,
            .vp_after = gs.pub.vp,
            .defcon_before = defcon_before,
            .defcon_after = gs.pub.defcon,
            .opp_hand_snapshot = opp_hand_snap_extra,
            .deck_snapshot = deck_snapshot_extra,
            .ussr_holds_china_snapshot = ussr_holds_china_snap_extra,
            .us_holds_china_snapshot = us_holds_china_snap_extra,
        });
    }
    sync_china(gs);
    if (over) {
        return GameResult{
            .winner = winner,
            .final_vp = gs.pub.vp,
            .end_turn = gs.pub.turn,
            .end_reason = end_reason(gs.pub, winner),
        };
    }
    if (side == Side::USSR && gs.pub.norad_active && gs.pub.defcon == 2) {
        if (auto norad = resolve_norad(gs, rng); norad.has_value()) {
            auto& [norad_pub, norad_over, norad_winner] = *norad;
            (void)norad_pub;
            if (norad_over) {
                return GameResult{
                    .winner = norad_winner,
                    .final_vp = gs.pub.vp,
                    .end_turn = gs.pub.turn,
                    .end_reason = end_reason(gs.pub, norad_winner),
                };
            }
        }
    }
    return std::nullopt;
}

std::optional<GameResult> end_of_turn(GameState& gs, int turn) {
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
        return GameResult{
            .winner = winner,
            .final_vp = gs.pub.vp,
            .end_turn = gs.pub.turn,
            .end_reason = "vp",
        };
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

    if (turn == kMaxTurns) {
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
            if (!gs.hands[to_index(side)].test(card_id)) {
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
            if (gs.hands[to_index(side)].test(card_id)) {
                gs.pub.discard.set(card_id);
            }
        }
        gs.hands[to_index(side)].reset();
    }

    return std::nullopt;
}

}  // namespace

void resolve_glasnost_free_ops_live(
    PublicState& pub,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    if (pub.glasnost_free_ops <= 0) {
        return;
    }
    const auto ops = pub.glasnost_free_ops;
    pub.glasnost_free_ops = 0;
    apply_influence_budget_impl(pub, Side::USSR, ops, static_cast<CardId>(93), rng, policy_cb);
}

// Convert old-style EventDecision to DecisionFrame for SubframePolicyFn callers.
static DecisionFrame event_decision_to_frame(const EventDecision& ed) {
    DecisionFrame f;
    f.source_card = ed.source_card;
    f.acting_side = ed.acting_side;
    f.eligible_n = static_cast<uint8_t>(ed.n_options);
    switch (ed.kind) {
        case DecisionKind::SmallChoice:
            f.kind = FrameKind::SmallChoice;
            break;
        case DecisionKind::CountrySelect:
            f.kind = FrameKind::CountryPick;
            for (int i = 0; i < ed.n_options; ++i)
                f.eligible_countries.set(static_cast<size_t>(ed.eligible_ids[i]));
            break;
        case DecisionKind::CardSelect:
            f.kind = FrameKind::CardSelect;
            for (int i = 0; i < ed.n_options; ++i)
                f.eligible_cards.set(static_cast<CardId>(ed.eligible_ids[i]));
            break;
    }
    return f;
}

// Convert FrameAction back to the int index expected by PolicyCallbackFn.
static int frame_action_to_index(const FrameAction& fa, const EventDecision& ed) {
    switch (ed.kind) {
        case DecisionKind::SmallChoice:
            return fa.option_index;
        case DecisionKind::CountrySelect:
            for (int i = 0; i < ed.n_options; ++i)
                if (ed.eligible_ids[i] == static_cast<int>(fa.country_id)) return i;
            return 0;
        case DecisionKind::CardSelect:
            for (int i = 0; i < ed.n_options; ++i)
                if (ed.eligible_ids[i] == static_cast<int>(fa.card_id)) return i;
            return 0;
    }
    return 0;
}

std::optional<DecisionFrame> engine_peek(const GameState& gs) {
    if (!gs.frame_stack.empty()) {
        return gs.frame_stack.back();
    }
    return std::nullopt;
}

StepResult engine_step_toplevel(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const SubframePolicyFn& sub_policy
) {
    gs.frame_stack.clear();
    const PolicyCallbackFn* cb_ptr = nullptr;
    PolicyCallbackFn adapter;
    if (sub_policy) {
        adapter = [&](const PublicState&, const EventDecision& ed) -> int {
            DecisionFrame frame = event_decision_to_frame(ed);
            FrameAction fa = sub_policy(gs, frame);
            return frame_action_to_index(fa, ed);
        };
        cb_ptr = &adapter;
    }
    gs.frame_stack_mode = !sub_policy;
    auto [new_pub, over, winner] = apply_action_live(gs, action, side, rng, cb_ptr, false, &gs.frame_stack);
    gs.frame_stack_mode = false;
    (void)new_pub;
    return StepResult{
        .pushed_subframe = !gs.frame_stack.empty(),
        .side_changed = !over,
        .game_over = over,
        .winner = winner,
    };
}

namespace {

constexpr CountryId kFrameFranceId = 7;
constexpr CountryId kFrameUkId = 17;
constexpr CountryId kFrameIsraelId = 30;
constexpr CountryId kFrameLebanonId = 32;
constexpr CountryId kFrameSouthAfricaId = 71;

uint8_t frame_count(size_t value) {
    return static_cast<uint8_t>(std::min<size_t>(value, 255));
}

void add_frame_influence(PublicState& pub, Side side, CountryId country_id, int delta) {
    pub.set_influence(side, country_id, std::max(0, pub.influence_of(side, country_id) + delta));
}

uint16_t aldrich_ames_region_key(CountryId country_id) {
    const auto region = country_spec(country_id).region;
    if (region == Region::CentralAmerica) {
        return 0;
    }
    if (region == Region::SouthAmerica) {
        return 1;
    }
    return 2;
}

void mark_frame_event_played(PublicState& pub, CardId card_id, Side side) {
    if (pub.discard.test(card_id) || pub.removed.test(card_id)) {
        return;
    }
    if (card_id == kChinaCardId) {
        pub.china_held_by = other_side(side);
        pub.china_playable = false;
        return;
    }
    if (card_spec(card_id).starred) {
        pub.removed.set(card_id);
    } else {
        pub.discard.set(card_id);
    }
}

std::bitset<kCountrySlots> country_bits(std::span<const CountryId> countries) {
    std::bitset<kCountrySlots> bits;
    for (const auto cid : countries) {
        bits.set(static_cast<size_t>(cid));
    }
    return bits;
}

void push_country_frame(
    GameState& gs,
    CardId source_card,
    Side acting_side,
    const std::bitset<kCountrySlots>& eligible,
    int step_index,
    int total_steps,
    uint16_t criteria_bits = 0
) {
    if (eligible.none()) {
        return;
    }
    DecisionFrame frame;
    frame.kind = FrameKind::CountryPick;
    frame.source_card = source_card;
    frame.acting_side = acting_side;
    frame.step_index = frame_count(static_cast<size_t>(std::max(0, step_index)));
    frame.total_steps = frame_count(static_cast<size_t>(std::max(1, total_steps)));
    frame.stack_depth = frame_count(gs.frame_stack.size());
    frame.eligible_countries = eligible;
    frame.eligible_n = frame_count(eligible.count());
    frame.criteria_bits = criteria_bits;
    gs.frame_stack.push_back(frame);
}

void push_card_frame(
    GameState& gs,
    CardId source_card,
    Side acting_side,
    const CardSet& eligible,
    int step_index,
    int total_steps,
    uint16_t criteria_bits = 0
) {
    if (eligible.none()) {
        return;
    }
    DecisionFrame frame;
    frame.kind = FrameKind::CardSelect;
    frame.source_card = source_card;
    frame.acting_side = acting_side;
    frame.step_index = frame_count(static_cast<size_t>(std::max(0, step_index)));
    frame.total_steps = frame_count(static_cast<size_t>(std::max(1, total_steps)));
    frame.stack_depth = frame_count(gs.frame_stack.size());
    frame.eligible_cards = eligible;
    frame.eligible_n = frame_count(eligible.count());
    frame.criteria_bits = criteria_bits;
    gs.frame_stack.push_back(frame);
}

void finish_frame_event(GameState& gs, CardId card_id, Side acting_side) {
    mark_frame_event_played(gs.pub, card_id, acting_side);
    const auto [over, winner] = check_vp_win(gs.pub);
    gs.game_over = over;
    gs.winner = winner;
}

void discard_frame_card(PublicState& pub, CardId card_id) {
    if (card_spec(card_id).starred) {
        pub.removed.set(card_id);
    } else {
        pub.discard.set(card_id);
    }
}

void discard_frame_hand_card(GameState& gs, Side side, CardId card_id) {
    gs.hands[to_index(side)].reset(card_id);
    discard_frame_card(gs.pub, card_id);
}

void tag_new_frames_with_parent(GameState& gs, size_t first_new_frame, CardId parent_card) {
    for (size_t idx = first_new_frame; idx < gs.frame_stack.size(); ++idx) {
        gs.frame_stack[idx].parent_card = parent_card;
    }
}

void complete_parent_frame_if_ready(GameState& gs, const DecisionFrame& frame) {
    if (frame.parent_card == 0 || gs.game_over) {
        return;
    }
    if (gs.frame_stack.empty()) {
        finish_frame_event(gs, frame.parent_card, frame.acting_side);
    } else if (gs.frame_stack.back().parent_card == 0) {
        gs.frame_stack.back().parent_card = frame.parent_card;
    }
}

PolicyCallbackFn frame_first_legal_policy_callback() {
    return [](const PublicState&, const EventDecision& decision) -> int {
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

std::optional<CardId> draw_one_frame(GameState& gs, Pcg64Rng& rng) {
    if (gs.deck.empty()) {
        std::vector<CardId> reshuffled;
        for (int raw = 1; raw <= kMaxCardId; ++raw) {
            const auto candidate = static_cast<CardId>(raw);
            if (gs.pub.discard.test(candidate) && !gs.pub.removed.test(candidate)) {
                reshuffled.push_back(candidate);
            }
        }
        if (reshuffled.empty()) {
            return std::nullopt;
        }
        shuffle_with_numpy_rng(reshuffled, rng);
        gs.deck = std::move(reshuffled);
        gs.pub.discard.reset();
    }
    if (gs.deck.empty()) {
        return std::nullopt;
    }
    const auto card = gs.deck.back();
    gs.deck.pop_back();
    return card;
}

void resolve_frame_selected_event(
    GameState& gs,
    CardId selected_card,
    CardId parent_card,
    Side event_side,
    Side parent_side,
    Pcg64Rng& rng
) {
    const auto stack_before = gs.frame_stack.size();
    const ActionEncoding action{
        .card_id = selected_card,
        .mode = ActionMode::Event,
        .targets = {},
    };
    const auto previous_frame_stack_mode = gs.frame_stack_mode;
    gs.frame_stack_mode = true;
    auto [event_pub, over, winner] =
        apply_action_live(gs, action, event_side, rng, nullptr, false, &gs.frame_stack);
    gs.frame_stack_mode = previous_frame_stack_mode;
    (void)event_pub;
    if (over) {
        mark_frame_event_played(gs.pub, parent_card, parent_side);
        gs.game_over = true;
        gs.winner = winner;
        return;
    }
    if (gs.frame_stack.size() > stack_before) {
        tag_new_frames_with_parent(gs, stack_before, parent_card);
        return;
    }
    finish_frame_event(gs, parent_card, parent_side);
}

void resume_card_5(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CardSelect ||
        action.card_id == 0 ||
        !frame.eligible_cards.test(action.card_id)) {
        return;
    }

    gs.hands[to_index(Side::USSR)].reset(action.card_id);
    discard_frame_card(gs.pub, action.card_id);

    if (card_spec(action.card_id).is_scoring) {
        auto result = apply_scoring_card(action.card_id, gs.pub);
        gs.pub.vp += result.vp_delta;
        if (result.clear_shuttle) {
            gs.pub.shuttle_diplomacy_active = false;
        }
        if (result.game_over) {
            mark_frame_event_played(gs.pub, frame.source_card, frame.acting_side);
            gs.game_over = true;
            gs.winner = result.winner;
            return;
        }
    } else if (card_spec(action.card_id).side == Side::US) {
        resolve_frame_selected_event(gs, action.card_id, frame.source_card, Side::US, frame.acting_side, rng);
        return;
    }

    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_socialist_governments(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }

    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::USSR, action.country_id, 1);
    }

    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = std::max<int>(1, frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        push_country_frame(
            gs,
            frame.source_card,
            frame.acting_side,
            next_eligible,
            next_step,
            total_steps
        );
        if (!gs.frame_stack.empty()) {
            return;
        }
    }

    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_68(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CardSelect ||
        action.card_id == 0 ||
        !frame.eligible_cards.test(action.card_id)) {
        return;
    }

    gs.hands[to_index(Side::USSR)].reset(action.card_id);
    const auto policy_cb = frame_first_legal_policy_callback();
    apply_ops_randomly_impl(
        gs.pub,
        Side::US,
        effective_ops(action.card_id, gs.pub, Side::US),
        frame.source_card,
        rng,
        &policy_cb,
        nullptr
    );
    gs.hands[to_index(Side::USSR)].set(action.card_id);
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_88(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CardSelect ||
        action.card_id == 0 ||
        !frame.eligible_cards.test(action.card_id)) {
        return;
    }

    gs.pub.discard.reset(action.card_id);
    resolve_frame_selected_event(gs, action.card_id, frame.source_card, frame.acting_side, frame.acting_side, rng);
}

void resume_card_101(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CardSelect ||
        action.card_id == 0 ||
        !frame.eligible_cards.test(action.card_id)) {
        return;
    }

    discard_frame_hand_card(gs, Side::US, action.card_id);
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_102(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::US, action.country_id, -1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        if (next_eligible.any()) {
            push_country_frame(gs, frame.source_card, frame.acting_side, next_eligible, next_step, total_steps);
            if (!gs.frame_stack.empty()) {
                return;
            }
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_105(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        apply_war_card(gs.pub, frame.acting_side, action.country_id, 2, 2, rng);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_10(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CardSelect) {
        return;
    }
    if (frame.eligible_cards.test(static_cast<size_t>(action.card_id))) {
        discard_frame_hand_card(gs, Side::US, action.card_id);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_26(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::US, action.country_id, 1);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_46(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CardSelect) {
        return;
    }
    if (frame.eligible_cards.test(static_cast<size_t>(action.card_id))) {
        gs.pub.discard.reset(action.card_id);
        gs.hands[to_index(frame.acting_side)].set(action.card_id);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_52(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CardSelect) {
        return;
    }
    if (frame.eligible_cards.test(static_cast<size_t>(action.card_id))) {
        const auto opponent = other_side(frame.acting_side);
        gs.hands[to_index(opponent)].reset(action.card_id);
        const auto policy_cb = frame_first_legal_policy_callback();
        apply_ops_randomly_impl(
            gs.pub,
            frame.acting_side,
            effective_ops(action.card_id, gs.pub, frame.acting_side),
            frame.source_card,
            rng,
            &policy_cb,
            nullptr
        );
        gs.hands[to_index(opponent)].set(action.card_id);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_14(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::USSR, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        push_country_frame(gs, frame.source_card, frame.acting_side, next_eligible, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_19(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        gs.pub.set_influence(Side::USSR, action.country_id, 0);
    }
    gs.pub.truman_doctrine_played = true;
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_24(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        apply_war_card(gs.pub, frame.acting_side, action.country_id, 2, 2, rng);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_20(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind == FrameKind::SmallChoice) {
        if (action.option_index == 0) {
            gs.pub.defcon = std::max(1, gs.pub.defcon - 1);
            const auto card_player = other_side(frame.acting_side);
            auto accessible = accessible_countries(card_player, gs.pub, ActionMode::Influence);
            if (!accessible.empty()) {
                std::bitset<kCountrySlots> eligible;
                for (const auto cid : accessible) {
                    eligible.set(static_cast<size_t>(cid));
                }
                push_country_frame(gs, frame.source_card, card_player, eligible, 0, 4);
            }
            if (gs.frame_stack.empty()) {
                finish_frame_event(gs, frame.source_card, frame.acting_side);
            }
        } else {
            const auto card_player = other_side(frame.acting_side);
            const auto opponent = frame.acting_side;
            auto my_roll = roll_d6(rng);
            auto opp_roll = roll_d6(rng);
            while (my_roll == opp_roll) {
                my_roll = roll_d6(rng);
                opp_roll = roll_d6(rng);
            }
            const auto winner = my_roll > opp_roll ? card_player : opponent;
            if (winner == Side::USSR) {
                gs.pub.vp += 2;
            } else {
                gs.pub.vp -= 2;
            }
            finish_frame_event(gs, frame.source_card, frame.acting_side);
        }
        return;
    }
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, frame.acting_side, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        push_country_frame(gs, frame.source_card, frame.acting_side, frame.eligible_countries, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_23(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::US, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = std::max<int>(1, frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        push_country_frame(gs, frame.source_card, frame.acting_side, next_eligible, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    gs.pub.marshall_plan_played = true;
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_29(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    const int amount = (gs.pub.turn >= 8) ? 2 : 1;
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::USSR, action.country_id, -amount);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = std::max<int>(1, frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        push_country_frame(gs, frame.source_card, frame.acting_side, next_eligible, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_30(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::USSR, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        push_country_frame(gs, frame.source_card, frame.acting_side, frame.eligible_countries, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_32(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CardSelect ||
        action.card_id == 0 ||
        !frame.eligible_cards.test(action.card_id)) {
        return;
    }

    const auto ops = effective_ops(action.card_id, gs.pub, frame.acting_side);
    discard_frame_hand_card(gs, frame.acting_side, action.card_id);
    const auto policy_cb = frame_first_legal_policy_callback();
    apply_ops_randomly_impl(
        gs.pub,
        frame.acting_side,
        ops,
        frame.source_card,
        rng,
        &policy_cb,
        nullptr
    );
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_37(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::US, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        push_country_frame(gs, frame.source_card, frame.acting_side, frame.eligible_countries, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_39(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        apply_war_card(gs.pub, frame.acting_side, action.country_id, 3, 3, rng);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_48(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::SmallChoice) {
        return;
    }
    const auto winner = frame.acting_side;
    const auto defcon_delta = action.option_index == 0 ? -1 : 1;
    gs.pub.defcon = std::clamp(gs.pub.defcon + defcon_delta, 1, 5);
    if (winner == Side::USSR) {
        gs.pub.vp += 2;
    } else {
        gs.pub.vp -= 2;
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_49(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::SmallChoice) {
        return;
    }
    gs.pub.defcon = std::clamp(action.option_index + 2, 2, 5);
    gs.pub.milops[to_index(frame.acting_side)] = 5;
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_59(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        gs.pub.set_influence(Side::US, action.country_id, 0);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = std::max<int>(1, frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        push_country_frame(gs, frame.source_card, frame.acting_side, next_eligible, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_60(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, frame.acting_side, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        push_country_frame(gs, frame.source_card, frame.acting_side, frame.eligible_countries, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_67(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::US, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = std::max<int>(1, frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        push_country_frame(gs, frame.source_card, frame.acting_side, next_eligible, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_71(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::US, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        push_country_frame(gs, frame.source_card, frame.acting_side, frame.eligible_countries, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_75(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::USSR, action.country_id, -1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = std::max<int>(1, frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        push_country_frame(gs, frame.source_card, frame.acting_side, next_eligible, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_77(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, frame.acting_side, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        push_country_frame(gs, frame.source_card, frame.acting_side, frame.eligible_countries, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_78(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind == FrameKind::SmallChoice) {
        const auto discard_count = std::clamp(action.option_index, 0, std::max(0, static_cast<int>(frame.eligible_n) - 1));
        if (discard_count <= 0) {
            finish_frame_event(gs, frame.source_card, frame.acting_side);
            return;
        }

        std::vector<CardId> discardable;
        for (int raw = 1; raw <= kMaxCardId; ++raw) {
            const auto candidate = static_cast<CardId>(raw);
            if (
                gs.hands[to_index(Side::US)].test(candidate) &&
                candidate != kChinaCardId &&
                !card_spec(candidate).is_scoring
            ) {
                discardable.push_back(candidate);
            }
        }
        if (discardable.size() > 4) {
            discardable.resize(4);
        }
        CardSet eligible;
        for (const auto card_id : discardable) {
            eligible.set(card_id);
        }
        push_card_frame(gs, frame.source_card, frame.acting_side, eligible, 0, discard_count, discard_count);
        if (!gs.frame_stack.empty()) {
            return;
        }
        finish_frame_event(gs, frame.source_card, frame.acting_side);
        return;
    }

    if (frame.kind != FrameKind::CardSelect) {
        return;
    }
    if (frame.eligible_cards.test(action.card_id)) {
        discard_frame_hand_card(gs, Side::US, action.card_id);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        auto reduced = frame.eligible_cards;
        reduced.reset(action.card_id);
        if (reduced.any()) {
            push_card_frame(gs, frame.source_card, frame.acting_side, reduced, next_step, total_steps, frame.criteria_bits);
            if (!gs.frame_stack.empty()) {
                return;
            }
        }
    }
    for (int i = 0; i < total_steps; ++i) {
        if (const auto drawn = draw_one_frame(gs, rng); drawn.has_value()) {
            gs.hands[to_index(Side::US)].set(*drawn);
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_83(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (!frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        finish_frame_event(gs, frame.source_card, frame.acting_side);
        return;
    }

    if (frame.step_index == 0) {
        const auto first_region = aldrich_ames_region_key(action.country_id);
        apply_free_coup(gs.pub, Side::USSR, action.country_id, 3, rng, false);

        std::bitset<kCountrySlots> second_eligible;
        for (const auto cid : all_country_ids()) {
            if (frame.eligible_countries.test(static_cast<size_t>(cid)) &&
                aldrich_ames_region_key(cid) != first_region) {
                second_eligible.set(static_cast<size_t>(cid));
            }
        }
        if (second_eligible.any()) {
            const auto total_steps = static_cast<int>(frame.total_steps);
            push_country_frame(
                gs,
                frame.source_card,
                frame.acting_side,
                second_eligible,
                1,
                total_steps,
                first_region
            );
            if (!gs.frame_stack.empty()) {
                return;
            }
        }
    } else {
        apply_free_coup(gs.pub, Side::USSR, action.country_id, 3, rng, false);
    }

    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_warsaw_pact(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    constexpr uint16_t kAddInfluenceChoice = 1;

    if (frame.kind == FrameKind::SmallChoice) {
        if (action.option_index <= 0) {
            std::bitset<kCountrySlots> eligible;
            for (const auto cid : kSetupEasternBlocIds) {
                if (gs.pub.influence_of(Side::US, cid) > 0) {
                    eligible.set(static_cast<size_t>(cid));
                }
            }
            if (eligible.none()) {
                gs.pub.warsaw_pact_played = true;
                finish_frame_event(gs, frame.source_card, frame.acting_side);
                return;
            }
            push_country_frame(
                gs,
                frame.source_card,
                frame.acting_side,
                eligible,
                0,
                std::min<int>(4, static_cast<int>(eligible.count()))
            );
            return;
        }

        push_country_frame(
            gs,
            frame.source_card,
            frame.acting_side,
            country_bits(kSetupEasternBlocIds),
            0,
            5,
            kAddInfluenceChoice
        );
        return;
    }

    if (frame.kind != FrameKind::CountryPick) {
        return;
    }

    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        if ((frame.criteria_bits & kAddInfluenceChoice) != 0) {
            add_frame_influence(gs.pub, Side::USSR, action.country_id, 1);
        } else {
            gs.pub.set_influence(Side::US, action.country_id, 0);
        }
    }

    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = std::max<int>(1, frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        if ((frame.criteria_bits & kAddInfluenceChoice) == 0) {
            next_eligible.reset(static_cast<size_t>(action.country_id));
        }
        push_country_frame(
            gs,
            frame.source_card,
            frame.acting_side,
            next_eligible,
            next_step,
            total_steps,
            frame.criteria_bits
        );
        if (!gs.frame_stack.empty()) {
            return;
        }
    }

    gs.pub.warsaw_pact_played = true;
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_suez_crisis(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }

    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::US, action.country_id, -2);
    }

    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = std::max<int>(1, frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        push_country_frame(
            gs,
            frame.source_card,
            frame.acting_side,
            next_eligible,
            next_step,
            total_steps
        );
        if (!gs.frame_stack.empty()) {
            return;
        }
    }

    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_south_african_unrest(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind == FrameKind::CountryPick &&
        frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::USSR, action.country_id, 2);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_liberation_theology(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }

    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::USSR, action.country_id, 1);
    }

    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = std::max<int>(1, frame.total_steps);
    if (next_step < total_steps) {
        push_country_frame(
            gs,
            frame.source_card,
            frame.acting_side,
            frame.eligible_countries,
            next_step,
            total_steps
        );
        return;
    }

    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_33(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    const bool is_src_pick = (frame.step_index % 2 == 0);
    const auto total_steps = static_cast<int>(frame.total_steps);
    const auto next_step = static_cast<int>(frame.step_index) + 1;

    if (is_src_pick) {
        if (!frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
            finish_frame_event(gs, frame.source_card, frame.acting_side);
            return;
        }
        // Build destinations: countries not US-controlled
        std::bitset<kCountrySlots> dst_eligible;
        for (const auto cid : all_country_ids()) {
            if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                continue;
            }
            if (!controls_country(Side::US, cid, gs.pub)) {
                dst_eligible.set(static_cast<size_t>(cid));
            }
        }
        if (dst_eligible.any() && next_step < total_steps) {
            push_country_frame(
                gs, frame.source_card, frame.acting_side, dst_eligible, next_step, total_steps,
                static_cast<uint16_t>(action.country_id)
            );
            if (!gs.frame_stack.empty()) {
                return;
            }
        }
        finish_frame_event(gs, frame.source_card, frame.acting_side);
    } else {
        // Dst pick: apply -1 to source, +1 to destination
        const auto src_cid = static_cast<CountryId>(frame.criteria_bits);
        if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
            add_frame_influence(gs.pub, Side::USSR, src_cid, -1);
            add_frame_influence(gs.pub, Side::USSR, action.country_id, 1);
        }
        if (next_step < total_steps) {
            // Rebuild available sources from current state
            std::bitset<kCountrySlots> src_eligible;
            for (const auto cid : all_country_ids()) {
                if (cid == 64 || cid == kUsaAnchorId || cid == kUssrAnchorId) {
                    continue;
                }
                if (gs.pub.influence_of(Side::USSR, cid) > 0) {
                    src_eligible.set(static_cast<size_t>(cid));
                }
            }
            if (src_eligible.any()) {
                push_country_frame(gs, frame.source_card, frame.acting_side, src_eligible, next_step, total_steps, 0);
                if (!gs.frame_stack.empty()) {
                    return;
                }
            }
        }
        finish_frame_event(gs, frame.source_card, frame.acting_side);
    }
}

void resume_card_50(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (frame.step_index == 0) {
        if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
            add_frame_influence(gs.pub, frame.acting_side, action.country_id, 2);
        }
        if (next_step < total_steps) {
            push_country_frame(gs, frame.source_card, frame.acting_side, frame.eligible_countries, next_step, total_steps);
            if (!gs.frame_stack.empty()) {
                return;
            }
        }
    } else {
        if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
            apply_free_coup(gs.pub, frame.acting_side, action.country_id, 2, rng, false);
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_91(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    gs.pub.set_influence(Side::US, kFrameLebanonId, 0);
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::US, action.country_id, -1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        auto next_eligible = frame.eligible_countries;
        next_eligible.reset(static_cast<size_t>(action.country_id));
        if (next_eligible.any()) {
            push_country_frame(gs, frame.source_card, frame.acting_side, next_eligible, next_step, total_steps);
            if (!gs.frame_stack.empty()) {
                return;
            }
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_90(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::USSR, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        push_country_frame(gs, frame.source_card, frame.acting_side, frame.eligible_countries, next_step, total_steps);
        if (!gs.frame_stack.empty()) {
            return;
        }
    }
    gs.pub.defcon = std::min(5, gs.pub.defcon + 1);
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_94(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        apply_free_coup(gs.pub, Side::USSR, action.country_id, 2, rng, false);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_36(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CountryPick) {
        return;
    }
    if (frame.eligible_countries.test(static_cast<size_t>(action.country_id))) {
        add_frame_influence(gs.pub, Side::USSR, action.country_id, 1);
    }
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        // Recompute regions from current hand state (US scoring cards don't change during event)
        std::vector<Region> regions;
        auto maybe_add = [&](CardId scoring_card, Region region) {
            if (gs.hands[to_index(Side::US)].test(scoring_card)) {
                regions.push_back(region);
            }
        };
        maybe_add(1, Region::Asia);
        maybe_add(2, Region::Europe);
        maybe_add(3, Region::MiddleEast);
        maybe_add(40, Region::CentralAmerica);
        maybe_add(41, Region::SoutheastAsia);
        maybe_add(80, Region::Africa);
        maybe_add(82, Region::SouthAmerica);
        std::sort(regions.begin(), regions.end(), [](Region lhs, Region rhs) {
            return static_cast<int>(lhs) < static_cast<int>(rhs);
        });
        regions.erase(std::unique(regions.begin(), regions.end()), regions.end());
        if (next_step < static_cast<int>(regions.size())) {
            const auto next_region = regions[static_cast<size_t>(next_step)];
            std::bitset<kCountrySlots> eligible;
            for (const auto cid : all_country_ids()) {
                if (cid != 64 && cid != kUsaAnchorId && cid != kUssrAnchorId &&
                    country_spec(cid).region == next_region) {
                    eligible.set(static_cast<size_t>(cid));
                }
            }
            if (eligible.any()) {
                push_country_frame(gs, frame.source_card, frame.acting_side, eligible, next_step, total_steps);
                if (!gs.frame_stack.empty()) {
                    return;
                }
            }
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_95(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CardSelect ||
        action.card_id == 0 ||
        !frame.eligible_cards.test(action.card_id)) {
        finish_frame_event(gs, frame.source_card, frame.acting_side);
        return;
    }
    const auto opponent = other_side(frame.acting_side);
    discard_frame_hand_card(gs, opponent, action.card_id);
    const auto next_step = static_cast<int>(frame.step_index) + 1;
    const auto total_steps = static_cast<int>(frame.total_steps);
    if (next_step < total_steps) {
        auto reduced = frame.eligible_cards;
        reduced.reset(action.card_id);
        if (reduced.any()) {
            push_card_frame(gs, frame.source_card, frame.acting_side, reduced, next_step, total_steps);
            if (!gs.frame_stack.empty()) {
                return;
            }
        }
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_97(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::SmallChoice) {
        return;
    }
    static constexpr std::array<Region, 6> kRegions = {
        Region::Europe,
        Region::Asia,
        Region::MiddleEast,
        Region::CentralAmerica,
        Region::SouthAmerica,
        Region::Africa,
    };
    const auto idx = std::clamp(action.option_index, 0, 5);
    gs.pub.chernobyl_blocked_region = kRegions[static_cast<size_t>(idx)];
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_98(GameState& gs, const DecisionFrame& frame, const FrameAction& action) {
    if (frame.kind != FrameKind::CardSelect ||
        action.card_id == 0 ||
        !frame.eligible_cards.test(action.card_id)) {
        finish_frame_event(gs, frame.source_card, frame.acting_side);
        return;
    }
    if (frame.step_index == 0) {
        // Push step-1 frame with criteria_bits = first chosen card
        auto reduced = frame.eligible_cards;
        reduced.reset(action.card_id);
        const auto total_steps = static_cast<int>(frame.total_steps);
        if (reduced.any()) {
            push_card_frame(gs, frame.source_card, frame.acting_side, reduced, 1, total_steps,
                            static_cast<uint16_t>(action.card_id));
            if (!gs.frame_stack.empty()) {
                return;
            }
        } else {
            discard_frame_hand_card(gs, Side::US, action.card_id);
        }
    } else {
        const auto first = static_cast<CardId>(frame.criteria_bits);
        discard_frame_hand_card(gs, Side::US, first);
        discard_frame_hand_card(gs, Side::US, action.card_id);
    }
    finish_frame_event(gs, frame.source_card, frame.acting_side);
}

void resume_card_subframe(GameState& gs, const DecisionFrame& frame, const FrameAction& action, Pcg64Rng& rng) {
    switch (frame.source_card) {
        case 5:
            resume_card_5(gs, frame, action, rng);
            break;
        case 7:
            resume_socialist_governments(gs, frame, action);
            break;
        case 10:
            resume_card_10(gs, frame, action);
            break;
        case 33:
            resume_card_33(gs, frame, action);
            break;
        case 36:
            resume_card_36(gs, frame, action);
            break;
        case 14:
            resume_card_14(gs, frame, action);
            break;
        case 16:
            resume_warsaw_pact(gs, frame, action);
            break;
        case 19:
            resume_card_19(gs, frame, action);
            break;
        case 20:
            resume_card_20(gs, frame, action, rng);
            break;
        case 23:
            resume_card_23(gs, frame, action);
            break;
        case 24:
            resume_card_24(gs, frame, action, rng);
            break;
        case 26:
            resume_card_26(gs, frame, action);
            break;
        case 28:
            resume_suez_crisis(gs, frame, action);
            break;
        case 29:
            resume_card_29(gs, frame, action);
            break;
        case 30:
            resume_card_30(gs, frame, action);
            break;
        case 32:
            resume_card_32(gs, frame, action, rng);
            break;
        case 37:
            resume_card_37(gs, frame, action);
            break;
        case 39:
            resume_card_39(gs, frame, action, rng);
            break;
        case 46:
            resume_card_46(gs, frame, action);
            break;
        case 48:
            resume_card_48(gs, frame, action);
            break;
        case 49:
            resume_card_49(gs, frame, action);
            break;
        case 50:
            resume_card_50(gs, frame, action, rng);
            break;
        case 52:
            resume_card_52(gs, frame, action, rng);
            break;
        case 56:
            resume_south_african_unrest(gs, frame, action);
            break;
        case 59:
            resume_card_59(gs, frame, action);
            break;
        case 60:
            resume_card_60(gs, frame, action);
            break;
        case 67:
            resume_card_67(gs, frame, action);
            break;
        case 71:
            resume_card_71(gs, frame, action);
            break;
        case 76:
            resume_liberation_theology(gs, frame, action);
            break;
        case 75:
            resume_card_75(gs, frame, action);
            break;
        case 77:
            resume_card_77(gs, frame, action);
            break;
        case 78:
            resume_card_78(gs, frame, action, rng);
            break;
        case 83:
            resume_card_83(gs, frame, action, rng);
            break;
        case 68:
            resume_card_68(gs, frame, action, rng);
            break;
        case 88:
            resume_card_88(gs, frame, action, rng);
            break;
        case 90:
            resume_card_90(gs, frame, action);
            break;
        case 91:
            resume_card_91(gs, frame, action);
            break;
        case 94:
            resume_card_94(gs, frame, action, rng);
            break;
        case 95:
            resume_card_95(gs, frame, action);
            break;
        case 97:
            resume_card_97(gs, frame, action);
            break;
        case 98:
            resume_card_98(gs, frame, action);
            break;
        case 101:
            resume_card_101(gs, frame, action);
            break;
        case 102:
            resume_card_102(gs, frame, action);
            break;
        case 105:
            resume_card_105(gs, frame, action, rng);
            break;
        default:
            break;
    }
}

}  // namespace

StepResult engine_step_subframe(GameState& gs, const FrameAction& action, Pcg64Rng& rng) {
    if (gs.frame_stack.empty()) {
        return StepResult{
            .pushed_subframe = false,
            .side_changed = false,
            .game_over = gs.game_over,
            .winner = gs.winner,
        };
    }
    const auto frame = gs.frame_stack.back();
    gs.frame_stack.pop_back();
    resume_card_subframe(gs, frame, action, rng);
    complete_parent_frame_if_ready(gs, frame);
    return StepResult{
        .pushed_subframe = !gs.frame_stack.empty(),
        .side_changed = false,
        .game_over = gs.game_over,
        .winner = gs.winner,
    };
}

namespace {

bool action_log_enabled() {
    static const bool enabled = (std::getenv("TS_ACTION_LOG") != nullptr);
    return enabled;
}

const char* mode_name(ActionMode m) {
    switch (m) {
        case ActionMode::Event:      return "Event";
        case ActionMode::Coup:       return "Coup";
        case ActionMode::Realign:    return "Realign";
        case ActionMode::Influence:  return "Infl";
        case ActionMode::Space:      return "Space";
        default:                     return "?";
    }
}

}  // namespace

std::tuple<PublicState, bool, std::optional<Side>> apply_action_live(
    GameState& gs,
    const ActionEncoding& action,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb,
    bool log_real_move,
    std::vector<DecisionFrame>* frame_log
) {
    const int defcon_before = gs.pub.defcon;
    const int vp_before = gs.pub.vp;
    const int turn_before = gs.pub.turn;
    const int ar_before = gs.pub.ar;
    auto result = apply_action_with_hands(gs, action, side, rng, policy_cb, frame_log);
    if (log_real_move && action_log_enabled()) {
        const auto& card = card_spec(action.card_id);
        std::string targets_str;
        for (size_t i = 0; i < action.targets.size(); ++i) {
            if (i > 0) targets_str += ",";
            targets_str += std::to_string(static_cast<int>(action.targets[i]));
        }
        const auto over = std::get<1>(result);
        const auto winner = std::get<2>(result);
        std::fprintf(stderr,
            "[APPLY] t%d/AR%d %s card=%d(%s) mode=%s targets=[%s] "
            "defcon=%d->%d vp=%+d->%+d%s\n",
            turn_before, ar_before,
            (side == Side::USSR ? "USSR" : "US"),
            static_cast<int>(action.card_id), card.name.c_str(),
            mode_name(action.mode), targets_str.c_str(),
            defcon_before, gs.pub.defcon,
            vp_before, gs.pub.vp,
            over ? (winner.has_value()
                    ? (*winner == Side::USSR ? " GAME_OVER winner=USSR" : " GAME_OVER winner=US")
                    : " GAME_OVER winner=DRAW") : "");
    }
    return result;
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_trap_ar_live(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    return resolve_trap_ar(gs, side, rng, policy_cb);
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_cuban_missile_crisis_cancel_live(
    GameState& gs,
    Side side,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    return resolve_cuban_missile_crisis_cancel(gs, side, rng, policy_cb);
}

std::optional<std::tuple<PublicState, bool, std::optional<Side>>> resolve_norad_live(
    GameState& gs,
    Pcg64Rng& rng,
    const PolicyCallbackFn* policy_cb
) {
    return resolve_norad(gs, rng, policy_cb);
}

std::optional<GameResult> run_extra_action_round_live(
    GameState& gs,
    Side side,
    const PolicyFn& policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    return run_extra_action_round(gs, side, policy, rng, trace_steps, config);
}

std::optional<GameResult> run_headline_phase_live(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    return run_headline_phase(gs, ussr_policy, us_policy, rng, trace_steps, config);
}

std::optional<GameResult> run_action_rounds_live(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    int total_ars,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    return run_action_rounds(gs, ussr_policy, us_policy, rng, total_ars, trace_steps, config);
}

// --- Setup influence placement phase (TS Deluxe §3.0) ---
// USSR places 6 in Eastern Europe, then US places 7 in Western Europe.
// Both players have seen their opening hands before placing.
void run_setup_phase(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    std::vector<StepTrace>* trace_steps,
    const GameLoopConfig& config
) {
    gs.phase = GamePhase::Setup;

    // Sample opening from human game corpus, weighted by historical frequency.
    for (const auto side : {Side::USSR, Side::US}) {
        gs.pub.phasing = side;
        const int side_idx = to_index(side);
        const auto valid_targets = [&]() -> std::vector<CountryId> {
            if (side == Side::USSR) {
                return {kSetupEasternBlocIds.begin(), kSetupEasternBlocIds.end()};
            } else {
                return {kSetupWesternEuropeIds.begin(), kSetupWesternEuropeIds.end()};
            }
        }();

        // Sample an opening weighted by human frequency.
        // All human games used +2 bid, so US openings are always 9-influence atomic units
        // (including Iran+1 bid placement). kHumanUSOpeningsBid2 is the only US table.
        const SetupOpening* opening;
        if (side == Side::USSR) {
            opening = choose_random_opening(kHumanUSSROpenings.data(),
                                            static_cast<int>(kHumanUSSROpenings.size()), rng);
        } else {
            opening = choose_random_opening(kHumanUSOpeningsBid2.data(),
                                            static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
        }

        std::vector<CountryId> heuristic_sequence;
        if (opening != nullptr) {
            for (int i = 0; i < opening->count; ++i) {
                for (int j = 0; j < opening->placements[i].amount; ++j) {
                    heuristic_sequence.push_back(opening->placements[i].country);
                }
            }
        }

        int heuristic_idx = 0;
        while (gs.setup_influence_remaining[side_idx] > 0) {
            const bool holds_china = (side == Side::USSR) ? gs.ussr_holds_china : gs.us_holds_china;
            const auto pub_snapshot = gs.pub;
            const auto hand_snapshot = gs.hands[side_idx];

            // Ask policy for placement (learned model will return meaningful targets)
            auto action_opt = (side == Side::USSR ? ussr_policy : us_policy)(
                gs.pub, gs.hands[side_idx], holds_china, rng
            );

            // Check if policy returned a valid setup target
            CountryId target = 0;
            bool valid_from_policy = false;
            if (action_opt.has_value() && !action_opt->targets.empty()) {
                const auto t = static_cast<CountryId>(action_opt->targets[0]);
                if (std::find(valid_targets.begin(), valid_targets.end(), t) != valid_targets.end()) {
                    target = t;
                    valid_from_policy = true;
                }
            }

            // Fallback: use heuristic plan
            if (!valid_from_policy) {
                if (heuristic_idx < static_cast<int>(heuristic_sequence.size())) {
                    target = heuristic_sequence[heuristic_idx++];
                } else {
                    target = valid_targets[rng.choice_index(valid_targets.size())];
                }
            }

            // Place 1 influence
            gs.pub.set_influence(side, target, gs.pub.influence_of(side, target) + 1);
            gs.setup_influence_remaining[side_idx] -= 1;

            // Record trace step for training data
            if (trace_steps) {
                ActionEncoding setup_action;
                setup_action.card_id = 0;  // no card during setup
                setup_action.mode = ActionMode::Influence;
                setup_action.targets = {target};
                trace_steps->push_back(StepTrace{
                    .turn = 0,
                    .ar = 0,
                    .side = side,
                    .holds_china = holds_china,
                    .pub_snapshot = pub_snapshot,
                    .hand_snapshot = hand_snapshot,
                    .action = setup_action,
                    .vp_before = gs.pub.vp,
                    .vp_after = gs.pub.vp,
                    .defcon_before = gs.pub.defcon,
                    .defcon_after = gs.pub.defcon,
                    .opp_hand_snapshot = {},
                    .deck_snapshot = {},
                    .ussr_holds_china_snapshot = false,
                    .us_holds_china_snapshot = false,
                });
            }
        }
    }

    // Transition to headline phase
    gs.phase = GamePhase::Headline;
}

TracedGame play_game_traced_from_state_ref_with_rng(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    const GameLoopConfig& config
) {
    TracedGame traced;

    // Apply competitive bid: US gets extra free influence in Western Europe.
    // Standard online TS bid is +2 for US.
    if (config.us_bid_extra > 0) {
        gs.setup_influence_remaining[to_index(Side::US)] += config.us_bid_extra;
    }

    // Run setup phase if game hasn't started yet (fresh game state)
    if (gs.phase == GamePhase::Setup && gs.setup_influence_remaining[0] > 0) {
        if (config.skip_setup_influence) {
            // Skip free placement, go directly to headline.
            gs.setup_influence_remaining = {0, 0};
            gs.phase = GamePhase::Headline;
        } else if (config.use_atomic_setup) {
            // Atomic setup: place from opening tables in one shot, no policy
            // callbacks.  Consumes exactly 2 RNG calls (one per side for
            // choose_random_opening), matching the batched path in
            // mcts_batched.cpp::run_setup_influence_heuristic.
            for (const auto side : {Side::USSR, Side::US}) {
                const SetupOpening* opening = (side == Side::USSR)
                    ? choose_random_opening(kHumanUSSROpenings.data(),
                                            static_cast<int>(kHumanUSSROpenings.size()), rng)
                    : choose_random_opening(kHumanUSOpeningsBid2.data(),
                                            static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
                if (opening == nullptr) continue;
                for (int i = 0; i < opening->count; ++i) {
                    const auto country = opening->placements[i].country;
                    const auto amount = opening->placements[i].amount;
                    gs.pub.set_influence(side, country,
                        gs.pub.influence_of(side, country) + amount);
                }
            }
            gs.setup_influence_remaining = {0, 0};
            gs.phase = GamePhase::Headline;
        } else {
            run_setup_phase(gs, ussr_policy, us_policy, rng, &traced.steps, config);
        }
    }

    for (int turn = 1; turn <= kMaxTurns; ++turn) {
        gs.pub.turn = turn;
        if (turn == kMidWarTurn) {
            advance_to_mid_war(gs, rng);
        } else if (turn == kLateWarTurn) {
            advance_to_late_war(gs, rng);
        }

        deal_cards(gs, Side::USSR, rng);
        deal_cards(gs, Side::US, rng);

        if (auto result = run_headline_phase(gs, ussr_policy, us_policy, rng, &traced.steps, config); result.has_value()) {
            traced.result = *result;
            return traced;
        }
        if (auto result = run_action_rounds(gs, ussr_policy, us_policy, rng, ars_for_turn(turn), &traced.steps, config); result.has_value()) {
            traced.result = *result;
            return traced;
        }
        if (gs.pub.north_sea_oil_extra_ar) {
            gs.pub.north_sea_oil_extra_ar = false;
            if (auto result = run_extra_action_round(gs, Side::US, us_policy, rng, &traced.steps, config); result.has_value()) {
                traced.result = *result;
                return traced;
            }
        }
        if (gs.pub.glasnost_free_ops > 0) {
            resolve_glasnost_free_ops_live(gs.pub, rng);
        }
        if (auto result = end_of_turn(gs, turn); result.has_value()) {
            traced.result = *result;
            return traced;
        }
    }

    if (gs.pub.vp > 0) {
        traced.result = GameResult{.winner = Side::USSR, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
        return traced;
    }
    if (gs.pub.vp < 0) {
        traced.result = GameResult{.winner = Side::US, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
        return traced;
    }
    // Tie at VP=0: USSR wins per rules
    traced.result = GameResult{.winner = Side::USSR, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
    return traced;
}

TracedGame play_game_traced_from_state_with_rng(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    Pcg64Rng& rng,
    const GameLoopConfig& config
) {
    return play_game_traced_from_state_ref_with_rng(gs, ussr_policy, us_policy, rng, config);
}

GameResult play_game_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    return play_game_traced_fn(ussr_policy, us_policy, seed, config).result;
}

GameResult play_game_from_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    return play_game_traced_from_state_fn(std::move(gs), ussr_policy, us_policy, seed, config).result;
}

TracedGame play_game_traced_from_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    Pcg64Rng rng(seed.value_or(std::random_device{}()));
    return play_game_traced_from_state_with_rng(std::move(gs), ussr_policy, us_policy, rng, config);
}

GameResult play_game_from_mid_state_fn(
    GameState gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    Pcg64Rng rng(seed.value_or(std::random_device{}()));
    const int start_turn = std::max(1, gs.pub.turn);

    // For the first turn we are continuing mid-turn: skip era advancement and
    // card dealing (the caller has already set up hands and deck).  For all
    // subsequent turns we run the normal turn sequence including dealing.
    for (int turn = start_turn; turn <= kMaxTurns; ++turn) {
        gs.pub.turn = turn;

        if (turn == start_turn) {
            // Continuing mid-game: skip era advancement and card dealing.
            // We run the headline phase and action rounds from whatever the
            // current phase is.  Simplest: always run headline then action
            // rounds; the caller should set gs.phase = Headline or ActionRound
            // appropriately.  If mid-action-round, we still re-run the full
            // round count; this is a slight over-estimate but acceptable for
            // rollouts.
        } else {
            // Normal turn setup.
            if (turn == kMidWarTurn) {
                advance_to_mid_war(gs, rng);
            } else if (turn == kLateWarTurn) {
                advance_to_late_war(gs, rng);
            }
            deal_cards(gs, Side::USSR, rng);
            deal_cards(gs, Side::US, rng);
        }

        if (auto result = run_headline_phase(gs, ussr_policy, us_policy, rng, nullptr, config); result.has_value()) {
            return *result;
        }
        if (auto result = run_action_rounds(gs, ussr_policy, us_policy, rng, ars_for_turn(turn), nullptr, config); result.has_value()) {
            return *result;
        }
        if (gs.pub.north_sea_oil_extra_ar) {
            gs.pub.north_sea_oil_extra_ar = false;
            if (auto result = run_extra_action_round(gs, Side::US, us_policy, rng, nullptr, config); result.has_value()) {
                return *result;
            }
        }
        if (gs.pub.glasnost_free_ops > 0) {
            resolve_glasnost_free_ops_live(gs.pub, rng);
        }
        if (auto result = end_of_turn(gs, turn); result.has_value()) {
            return *result;
        }
    }

    if (gs.pub.vp > 0) {
        return GameResult{.winner = Side::USSR, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
    }
    if (gs.pub.vp < 0) {
        return GameResult{.winner = Side::US, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
    }
    // Tie at VP=0: USSR wins per rules
    return GameResult{.winner = Side::USSR, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
}

TracedGame play_game_traced_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    auto gs = reset_game(seed);
    Pcg64Rng runtime_rng(seed.value_or(std::random_device{}()));
    return play_game_traced_from_state_with_rng(std::move(gs), ussr_policy, us_policy, runtime_rng, config);
}

TracedGame play_game_traced_from_seed_words_fn(
    std::array<uint64_t, 4> words,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    auto gs = reset_game_from_seed_words(words);
    Pcg64Rng runtime_rng(seed.value_or(std::random_device{}()));
    return play_game_traced_from_state_with_rng(std::move(gs), ussr_policy, us_policy, runtime_rng, config);
}

GameResult play_game(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    const PolicyFn ussr_fn = [ussr_policy](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng) {
        return choose_action(ussr_policy, pub, hand, holds_china, rng);
    };
    const PolicyFn us_fn = [us_policy](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng) {
        return choose_action(us_policy, pub, hand, holds_china, rng);
    };
    return play_game_fn(ussr_fn, us_fn, seed, config);
}

GameResult play_random_game(std::optional<uint32_t> seed, const GameLoopConfig& config) {
    return play_game(PolicyKind::Random, PolicyKind::Random, seed, config);
}

std::vector<GameResult> play_matchup(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    int game_count,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    const PolicyFn ussr_fn = [ussr_policy](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng) {
        return choose_action(ussr_policy, pub, hand, holds_china, rng);
    };
    const PolicyFn us_fn = [us_policy](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng) {
        return choose_action(us_policy, pub, hand, holds_china, rng);
    };
    return play_matchup_fn(ussr_fn, us_fn, game_count, seed, config);
}

std::vector<GameResult> play_matchup_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    int game_count,
    std::optional<uint32_t> seed,
    const GameLoopConfig& config
) {
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(std::max(0, game_count)));
    const auto base_seed = seed.value_or(std::random_device{}());
    for (int game_index = 0; game_index < game_count; ++game_index) {
        results.push_back(play_game_fn(ussr_policy, us_policy, base_seed + static_cast<uint32_t>(game_index), config));
    }
    return results;
}

MatchSummary summarize_results(std::span<const GameResult> results) {
    MatchSummary summary;
    summary.games = static_cast<int>(results.size());
    long long total_turns = 0;
    long long total_vp = 0;

    for (const auto& result : results) {
        total_turns += result.end_turn;
        total_vp += result.final_vp;

        if (!result.winner.has_value()) {
            ++summary.draws;
        } else if (*result.winner == Side::USSR) {
            ++summary.ussr_wins;
        } else if (*result.winner == Side::US) {
            ++summary.us_wins;
        }

        if (result.end_reason == "defcon1") {
            ++summary.defcon1;
        } else if (result.end_reason == "turn_limit") {
            ++summary.turn_limit;
        } else if (result.end_reason == "scoring_card_held") {
            ++summary.scoring_card_held;
        } else if (result.end_reason == "vp_threshold" || result.end_reason == "vp") {
            ++summary.vp_threshold;
        } else if (result.end_reason == "wargames") {
            ++summary.wargames;
        } else if (result.end_reason == "europe_control") {
            ++summary.europe_control;
        }
    }

    if (!results.empty()) {
        summary.avg_turn = static_cast<double>(total_turns) / static_cast<double>(results.size());
        summary.avg_final_vp = static_cast<double>(total_vp) / static_cast<double>(results.size());
    }
    return summary;
}

}  // namespace ts
