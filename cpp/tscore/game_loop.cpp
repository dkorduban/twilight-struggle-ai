#include "game_loop.hpp"

#include <algorithm>

#include "game_data.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts {
namespace {

constexpr int kMidWarTurn = 4;
constexpr int kLateWarTurn = 8;
constexpr int kMaxTurns = 10;

struct PendingHeadline {
    Side side = Side::USSR;
    bool holds_china = false;
    CardSet hand_snapshot;
    ActionEncoding action;
};

void sync_china(GameState& gs) {
    gs.ussr_holds_china = gs.pub.china_held_by == Side::USSR;
    gs.us_holds_china = gs.pub.china_held_by == Side::US;
}

std::string end_reason(const PublicState& pub, std::optional<Side> winner) {
    if (pub.defcon <= 1) {
        return "defcon1";
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
    std::mt19937& rng,
    std::vector<StepTrace>* trace_steps
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
        auto action = (side == Side::USSR ? ussr_policy : us_policy)(
            headline_pub,
            gs.hands[to_index(side)],
            holds_china,
            rng
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

    std::sort(ordered.begin(), ordered.end(), [](const auto& lhs, const auto& rhs) {
        const auto lhs_ops = card_spec(lhs.action.card_id).ops;
        const auto rhs_ops = card_spec(rhs.action.card_id).ops;
        if (lhs_ops != rhs_ops) {
            return lhs_ops > rhs_ops;
        }
        return lhs.side == Side::US;
    });

    for (const auto& pending : ordered) {
        const auto side = pending.side;
        const auto& action = pending.action;
        const auto pub_snapshot = gs.pub;
        const auto vp_before = gs.pub.vp;
        const auto defcon_before = gs.pub.defcon;
        auto [new_pub, over, winner] = apply_action(gs.pub, action, side, rng);
        gs.pub = std::move(new_pub);
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
    }

    return std::nullopt;
}

std::optional<GameResult> run_action_rounds(
    GameState& gs,
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    std::mt19937& rng,
    int total_ars,
    std::vector<StepTrace>* trace_steps
) {
    gs.phase = GamePhase::ActionRound;
    for (int ar = 1; ar <= total_ars; ++ar) {
        gs.pub.ar = ar;
        for (const auto side : {Side::USSR, Side::US}) {
            gs.pub.phasing = side;
            const auto holds_china = side == Side::USSR ? gs.ussr_holds_china : gs.us_holds_china;
            auto& hand = gs.hands[to_index(side)];
            if (!has_legal_action(hand, gs.pub, side, holds_china)) {
                continue;
            }
            auto action = (side == Side::USSR ? ussr_policy : us_policy)(
                gs.pub,
                hand,
                holds_china,
                rng
            );
            if (!action.has_value()) {
                continue;
            }
            const auto pub_snapshot = gs.pub;
            const auto hand_snapshot = hand;
            if (hand.test(action->card_id)) {
                hand.reset(action->card_id);
            }
            const auto vp_before = gs.pub.vp;
            const auto defcon_before = gs.pub.defcon;
            auto [new_pub, over, winner] = apply_action(gs.pub, *action, side, rng);
            gs.pub = std::move(new_pub);
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
    gs.pub.glasnost_extra_ar = false;
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

GameResult play_game_fn(const PolicyFn& ussr_policy, const PolicyFn& us_policy, std::optional<uint32_t> seed) {
    return play_game_traced_fn(ussr_policy, us_policy, seed).result;
}

TracedGame play_game_traced_fn(const PolicyFn& ussr_policy, const PolicyFn& us_policy, std::optional<uint32_t> seed) {
    std::mt19937 rng(seed.value_or(std::random_device{}()));
    auto gs = reset_game(static_cast<uint32_t>(rng()));
    TracedGame traced;

    for (int turn = 1; turn <= kMaxTurns; ++turn) {
        gs.pub.turn = turn;
        if (turn == kMidWarTurn) {
            advance_to_mid_war(gs, rng);
        } else if (turn == kLateWarTurn) {
            advance_to_late_war(gs, rng);
        }

        deal_cards(gs, Side::USSR, rng);
        deal_cards(gs, Side::US, rng);

        if (auto result = run_headline_phase(gs, ussr_policy, us_policy, rng, &traced.steps); result.has_value()) {
            traced.result = *result;
            return traced;
        }
        if (auto result = run_action_rounds(gs, ussr_policy, us_policy, rng, ars_for_turn(turn), &traced.steps); result.has_value()) {
            traced.result = *result;
            return traced;
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
    traced.result = GameResult{.winner = std::nullopt, .final_vp = gs.pub.vp, .end_turn = kMaxTurns, .end_reason = "turn_limit"};
    return traced;
}

GameResult play_game(PolicyKind ussr_policy, PolicyKind us_policy, std::optional<uint32_t> seed) {
    const PolicyFn ussr_fn = [ussr_policy](const PublicState& pub, const CardSet& hand, bool holds_china, std::mt19937& rng) {
        return choose_action(ussr_policy, pub, hand, holds_china, rng);
    };
    const PolicyFn us_fn = [us_policy](const PublicState& pub, const CardSet& hand, bool holds_china, std::mt19937& rng) {
        return choose_action(us_policy, pub, hand, holds_china, rng);
    };
    return play_game_fn(ussr_fn, us_fn, seed);
}

GameResult play_random_game(std::optional<uint32_t> seed) {
    return play_game(PolicyKind::Random, PolicyKind::Random, seed);
}

std::vector<GameResult> play_matchup(
    PolicyKind ussr_policy,
    PolicyKind us_policy,
    int game_count,
    std::optional<uint32_t> seed
) {
    const PolicyFn ussr_fn = [ussr_policy](const PublicState& pub, const CardSet& hand, bool holds_china, std::mt19937& rng) {
        return choose_action(ussr_policy, pub, hand, holds_china, rng);
    };
    const PolicyFn us_fn = [us_policy](const PublicState& pub, const CardSet& hand, bool holds_china, std::mt19937& rng) {
        return choose_action(us_policy, pub, hand, holds_china, rng);
    };
    return play_matchup_fn(ussr_fn, us_fn, game_count, seed);
}

std::vector<GameResult> play_matchup_fn(
    const PolicyFn& ussr_policy,
    const PolicyFn& us_policy,
    int game_count,
    std::optional<uint32_t> seed
) {
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(std::max(0, game_count)));
    const auto base_seed = seed.value_or(std::random_device{}());
    for (int game_index = 0; game_index < game_count; ++game_index) {
        results.push_back(play_game_fn(ussr_policy, us_policy, base_seed + static_cast<uint32_t>(game_index)));
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
        }
    }

    if (!results.empty()) {
        summary.avg_turn = static_cast<double>(total_turns) / static_cast<double>(results.size());
        summary.avg_final_vp = static_cast<double>(total_vp) / static_cast<double>(results.size());
    }
    return summary;
}

}  // namespace ts
