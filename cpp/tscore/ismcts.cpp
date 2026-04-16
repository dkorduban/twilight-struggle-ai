// Determinized information-set MCTS built by sampling hidden opponent hands
// and reusing the native full-state MCTS implementation.

#include "ismcts.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <limits>
#include <memory>
#include <optional>
#include <string>
#include <stdexcept>
#include <tuple>
#include <utility>
#include <vector>

#include <torch/torch.h>

#include "decode_helpers.hpp"
#include "game_data.hpp"
#include "game_loop.hpp"
#include "human_openings.hpp"
#include "nn_features.hpp"
#include "policies.hpp"
#include "rule_queries.hpp"
#include "search_common.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts {
namespace {

// Forward declaration — defined later in this file.
std::optional<GameResult> finish_turn(GameState& gs, int turn);

constexpr int kMidWarTurn = 4;
constexpr int kLateWarTurn = 8;
constexpr int kMaxTurns = 10;
// kSpaceShuttleArs is in search_common.hpp
constexpr int kVirtualLossWeight = 1;
constexpr int kMaxCardLogits = 112;
constexpr int kMaxModeLogits = 8;
constexpr int kMaxCountryLogits = 86;
constexpr int kMaxStrategies = 8;

struct ExpansionResult {
    std::unique_ptr<MctsNode> node;
    double leaf_value = 0.0;
};

struct SelectionResult {
    bool needs_batch = false;
    double leaf_value = 0.0;
};

struct AggregatedEdgeState {
    MctsEdge edge;
    int occurrences = 0;
};

struct PendingExpansion {
    std::vector<std::pair<MctsNode*, int>> path;
    struct TreeState {
        GameState game_state;
        bool in_extra_round = false;
    } sim_state;
    bool is_root_expansion = false;
};

struct DeterminizationSlot {
    PendingExpansion::TreeState root_state;
    std::unique_ptr<MctsNode> root;
    std::vector<PendingExpansion> pending;
    int sims_completed = 0;
    Pcg64Rng rng;
};

enum class IsmctsGameStage : uint8_t {
    TurnSetup = 0,
    HeadlineChoiceUSSR = 1,
    HeadlineChoiceUS = 2,
    HeadlineResolve = 3,
    ActionRound = 4,
    ExtraActionRoundUS = 5,
    ExtraActionRoundUSSR = 6,
    Cleanup = 7,
    Finished = 8,
};

struct PendingDecision {
    int turn = 0;
    int ar = 0;
    Side side = Side::USSR;
    bool holds_china = false;
    bool is_headline = false;
    PublicState pub_snapshot;
    CardSet hand_snapshot;
};

struct PendingHeadlineChoice {
    Side side = Side::USSR;
    bool holds_china = false;
    CardSet hand_snapshot;
    ActionEncoding action;
};

struct IsmctsGameSlot {
    GameState game_state;
    std::vector<DeterminizationSlot> dets;
    bool search_active = false;
    bool game_done = false;
    bool emitted = false;
    bool active = false;
    GameResult result;
    int game_index = 0;
    Pcg64Rng rng;

    int turn = 1;
    int total_ars = 0;
    int current_ar = 0;
    Side current_side = Side::USSR;
    IsmctsGameStage stage = IsmctsGameStage::TurnSetup;
    std::array<std::optional<PendingHeadlineChoice>, 2> pending_headlines = {};
    std::vector<PendingHeadlineChoice> headline_order;
    size_t headline_order_index = 0;
    std::optional<PendingDecision> decision;
};

struct BatchEntry {
    IsmctsGameSlot* game = nullptr;
    DeterminizationSlot* det = nullptr;
    size_t pending_index = 0;
};

bool action_less(const ActionEncoding& lhs, const ActionEncoding& rhs) {
    if (lhs.card_id != rhs.card_id) {
        return lhs.card_id < rhs.card_id;
    }
    if (lhs.mode != rhs.mode) {
        return static_cast<int>(lhs.mode) < static_cast<int>(rhs.mode);
    }
    return lhs.targets < rhs.targets;
}

bool aggregated_edge_better(const MctsEdge& lhs, const MctsEdge& rhs) {
    if (lhs.visit_count != rhs.visit_count) {
        return lhs.visit_count > rhs.visit_count;
    }
    if (lhs.prior != rhs.prior) {
        return lhs.prior > rhs.prior;
    }
    return action_less(lhs.action, rhs.action);
}

using TreeState = PendingExpansion::TreeState;

void mark_tree_game_done(TreeState& state, std::optional<Side> winner, Side side) {
    state.game_state.game_over = true;
    state.game_state.winner = winner;
    state.game_state.current_side = side;
    state.in_extra_round = false;
}

void advance_tree_action_pair(Side& current_side, int& current_ar) {
    if (current_side == Side::USSR) {
        current_side = Side::US;
    } else {
        current_side = Side::USSR;
        current_ar += 1;
    }
}

void start_tree_next_turn(TreeState& state, Pcg64Rng& rng) {
    auto& game = state.game_state;
    state.in_extra_round = false;
    game.phase = GamePhase::Headline;
    game.current_side = Side::USSR;
    game.headline_card = {0, 0};
    game.ar_index = 1;
    game.ars_taken = {0, 0};

    game.pub.turn += 1;
    if (game.pub.turn == kMidWarTurn) {
        advance_to_mid_war(game, rng);
    } else if (game.pub.turn == kLateWarTurn) {
        advance_to_late_war(game, rng);
    }
    deal_cards(game, Side::USSR, rng);
    deal_cards(game, Side::US, rng);
    game.pub.ar = 0;
    game.pub.phasing = Side::USSR;
}

void advance_tree_post_round_to_decision_or_done(TreeState& state, Pcg64Rng& rng);

void advance_tree_action_round_to_decision_or_done(TreeState& state, Side current_side, int current_ar, Pcg64Rng& rng) {
    auto& game = state.game_state;
    state.in_extra_round = false;
    game.phase = GamePhase::ActionRound;

    while (!game.game_over) {
        if (current_ar > kSpaceShuttleArs) {
            advance_tree_post_round_to_decision_or_done(state, rng);
            return;
        }

        if (current_ar > ars_for_turn(game.pub.turn) &&
            game.pub.space[to_index(current_side)] < kSpaceShuttleArs) {
            advance_tree_action_pair(current_side, current_ar);
            continue;
        }

        game.pub.ar = current_ar;
        game.pub.phasing = current_side;
        game.current_side = current_side;

        if (auto cmc_result = resolve_cuban_missile_crisis_cancel_live(game, current_side, rng);
            cmc_result.has_value()) {
            auto& [new_pub, over, winner] = *cmc_result;
            (void)new_pub;
            sync_china_flags(game);
            if (over) {
                mark_tree_game_done(state, winner, current_side);
                return;
            }
            advance_tree_action_pair(current_side, current_ar);
            continue;
        }

        if (auto trap_result = resolve_trap_ar_live(game, current_side, rng); trap_result.has_value()) {
            auto& [new_pub, over, winner] = *trap_result;
            (void)new_pub;
            sync_china_flags(game);
            if (over) {
                mark_tree_game_done(state, winner, current_side);
                return;
            }
            advance_tree_action_pair(current_side, current_ar);
            continue;
        }

        const auto holds_china = holds_china_for(game, current_side);
        if (!has_legal_action(game.hands[to_index(current_side)], game.pub, current_side, holds_china)) {
            advance_tree_action_pair(current_side, current_ar);
            continue;
        }

        return;
    }
}

void advance_tree_extra_round_to_decision_or_done(TreeState& state, Pcg64Rng& rng) {
    auto& game = state.game_state;
    state.in_extra_round = true;
    game.phase = GamePhase::ActionRound;
    game.current_side = Side::US;
    game.pub.ar = std::max(game.pub.ar, ars_for_turn(game.pub.turn)) + 1;
    game.pub.phasing = Side::US;

    if (auto cmc_result = resolve_cuban_missile_crisis_cancel_live(game, Side::US, rng); cmc_result.has_value()) {
        auto& [new_pub, over, winner] = *cmc_result;
        (void)new_pub;
        sync_china_flags(game);
        if (over) {
            mark_tree_game_done(state, winner, Side::US);
            return;
        }
    } else if (game.hands[to_index(Side::US)].none()) {
        // No extra-round decision; fall through to cleanup.
    } else if (auto trap_result = resolve_trap_ar_live(game, Side::US, rng); trap_result.has_value()) {
        auto& [new_pub, over, winner] = *trap_result;
        (void)new_pub;
        sync_china_flags(game);
        if (over) {
            mark_tree_game_done(state, winner, Side::US);
            return;
        }
    } else {
        const auto holds_china = holds_china_for(game, Side::US);
        if (has_legal_action(game.hands[to_index(Side::US)], game.pub, Side::US, holds_china)) {
            return;
        }
    }

    state.in_extra_round = false;
    if (game.pub.glasnost_free_ops > 0) {
        resolve_glasnost_free_ops_live(game.pub, rng);
    }
    if (auto result = finish_turn(game, game.pub.turn); result.has_value()) {
        mark_tree_game_done(state, result->winner, Side::US);
        return;
    }
    start_tree_next_turn(state, rng);
}

void advance_tree_post_round_to_decision_or_done(TreeState& state, Pcg64Rng& rng) {
    auto& game = state.game_state;
    state.in_extra_round = false;
    if (game.pub.north_sea_oil_extra_ar) {
        game.pub.north_sea_oil_extra_ar = false;
        advance_tree_extra_round_to_decision_or_done(state, rng);
        return;
    }
    if (game.pub.glasnost_free_ops > 0) {
        resolve_glasnost_free_ops_live(game.pub, rng);
    }
    if (auto result = finish_turn(game, game.pub.turn); result.has_value()) {
        mark_tree_game_done(state, result->winner, game.current_side);
        return;
    }
    start_tree_next_turn(state, rng);
}

void resolve_tree_headlines_and_advance(TreeState& state, Pcg64Rng& rng) {
    auto& game = state.game_state;
    std::vector<std::pair<Side, CardId>> ordered;
    for (const auto side : {Side::USSR, Side::US}) {
        const auto card_id = game.headline_card[to_index(side)];
        if (card_id != 0) {
            ordered.emplace_back(side, card_id);
        }
    }

    if (game.headline_card[to_index(Side::US)] == 108 && game.headline_card[to_index(Side::USSR)] != 0) {
        game.pub.discard.set(game.headline_card[to_index(Side::USSR)]);
        ordered.erase(
            std::remove_if(
                ordered.begin(),
                ordered.end(),
                [](const auto& pending) { return pending.first == Side::USSR; }
            ),
            ordered.end()
        );
    }

    std::sort(ordered.begin(), ordered.end(), [](const auto& lhs, const auto& rhs) {
        const auto lhs_ops = card_spec(lhs.second).ops;
        const auto rhs_ops = card_spec(rhs.second).ops;
        if (lhs_ops != rhs_ops) {
            return lhs_ops > rhs_ops;
        }
        return static_cast<int>(lhs.first) > static_cast<int>(rhs.first);
    });

    for (const auto& [side, card_id] : ordered) {
        game.pub.phasing = side;
        game.pub.ar = 0;
        const ActionEncoding headline{
            .card_id = card_id,
            .mode = ActionMode::Event,
            .targets = {},
        };
        auto [new_pub, over, winner] = apply_action_live(game, headline, side, rng);
        (void)new_pub;
        sync_china_flags(game);
        if (over) {
            mark_tree_game_done(state, winner, side);
            return;
        }
    }

    game.headline_card = {0, 0};
    advance_tree_action_round_to_decision_or_done(state, Side::USSR, 1, rng);
}

void apply_tree_action(TreeState& state, const ActionEncoding& action, Pcg64Rng& rng) {
    auto& game = state.game_state;
    const auto side = game.pub.phasing;
    auto& hand = game.hands[to_index(side)];
    if (hand.test(action.card_id)) {
        hand.reset(action.card_id);
    }

    if (game.phase == GamePhase::Headline) {
        game.headline_card[to_index(side)] = action.card_id;
        state.in_extra_round = false;
        if (game.headline_card[to_index(other_side(side))] == 0) {
            game.pub.ar = 0;
            game.pub.phasing = other_side(side);
            game.current_side = other_side(side);
            return;
        }
        resolve_tree_headlines_and_advance(state, rng);
        return;
    }

    const bool was_extra_round = state.in_extra_round;
    auto [new_pub, over, winner] = apply_action_live(game, action, side, rng);
    (void)new_pub;
    sync_china_flags(game);
    game.game_over = over;
    game.winner = winner;

    if (over) {
        game.current_side = side;
        state.in_extra_round = false;
        return;
    }

    if (side == Side::USSR && game.pub.norad_active && game.pub.defcon == 2) {
        if (auto norad = resolve_norad_live(game, rng); norad.has_value()) {
            auto& [norad_pub, norad_over, norad_winner] = *norad;
            (void)norad_pub;
            sync_china_flags(game);
            if (norad_over) {
                mark_tree_game_done(state, norad_winner, side);
                return;
            }
        }
    }

    if (was_extra_round) {
        state.in_extra_round = false;
        if (side == Side::US && game.pub.glasnost_free_ops > 0) {
            resolve_glasnost_free_ops_live(game.pub, rng);
        }
        if (auto result = finish_turn(game, game.pub.turn); result.has_value()) {
            mark_tree_game_done(state, result->winner, side);
            return;
        }
        start_tree_next_turn(state, rng);
        return;
    }

    advance_tree_action_round_to_decision_or_done(state, other_side(side), game.pub.ar, rng);
}
// count_scoring_cards, remaining_action_decisions_for_side, scoring_card_prior_multiplier
// are now in search_common.hpp.

DraftsResult collect_card_drafts(const TreeState& state) {
    const auto& game = state.game_state;
    const auto side = game.pub.phasing;
    const auto holds_china = holds_china_for(game, side);
    const auto& pub = game.pub;
    auto cache = AccessibleCache::build(side, pub);

    if (game.phase == GamePhase::Headline) {
        auto cards = collect_event_only_card_drafts(
            game.hands[to_index(side)],
            pub,
            side,
            holds_china,
            [&](CardId card_id) {
                const auto modes = legal_modes(card_id, pub, side);
                return std::find(modes.begin(), modes.end(), ActionMode::Event) != modes.end();
            }
        );
        return DraftsResult{.drafts = std::move(cards), .cache = std::move(cache)};
    }

    // Only force scoring when every remaining decision slot must be spent on
    // a scoring card to avoid the cleanup loss. This preserves any genuine
    // setup ARs instead of forcing immediate play as soon as a scoring card is held.
    if (must_play_scoring_card(game, side)) {
        // Return only the scoring card(s) as Event actions.
        auto cards = collect_event_only_card_drafts(
            game.hands[to_index(side)],
            pub,
            side,
            holds_china,
            [](CardId card_id) { return card_spec(card_id).is_scoring; }
        );
        if (!cards.empty()) {
            return DraftsResult{.drafts = std::move(cards), .cache = std::move(cache)};
        }
        // Fallthrough: no scoring cards are actually legal (shouldn't happen); run normal drafts.
    }

    auto cards = collect_drafts_from_legal_cards(
        game.hands[to_index(side)],
        pub,
        side,
        holds_china,
        [&](CardDraft& card, CardId card_id) {
            const auto& spec = card_spec(card_id);
            const auto legal = legal_modes(card_id, pub, side);
            const auto has_mode = [&](ActionMode mode) {
                return std::find(legal.begin(), legal.end(), mode) != legal.end();
            };

            if (spec.ops > 0) {
                if (has_mode(ActionMode::Influence) && !cache.influence.empty()) {
                    append_single_edge_mode_draft(card, card_id, ActionMode::Influence);
                    if (has_mode(ActionMode::EventFirst)) {
                        append_single_edge_mode_draft(card, card_id, ActionMode::EventFirst);
                    }
                }

                if (has_mode(ActionMode::Coup)) {
                    append_country_target_mode_draft(card, card_id, ActionMode::Coup, cache.coup);
                }
                if (has_mode(ActionMode::Realign)) {
                    append_country_target_mode_draft(card, card_id, ActionMode::Realign, cache.realign);
                }

                if (has_mode(ActionMode::Space) && cache.can_space && spec.ops >= cache.space_ops_min) {
                    append_single_edge_mode_draft(card, card_id, ActionMode::Space);
                }
            }

            if (has_mode(ActionMode::Event)) {
                append_single_edge_mode_draft(card, card_id, ActionMode::Event);
            }
        }
    );

    return DraftsResult{.drafts = std::move(cards), .cache = std::move(cache)};
}

std::optional<ExpansionResult> expand_without_model(const TreeState& state, Pcg64Rng& rng) {
    auto node = std::make_unique<MctsNode>();
    node->side_to_move = state.game_state.pub.phasing;

    if (state.game_state.game_over) {
        node->is_terminal = true;
        const auto terminal_value = winner_value(state.game_state.winner);
        node->terminal_value = terminal_value;
        return ExpansionResult{.node = std::move(node), .leaf_value = terminal_value};
    }

    const auto [drafts, _cache] = collect_card_drafts(state);
    if (!drafts.empty()) {
        return std::nullopt;
    }

    if (auto fallback = choose_action(
            PolicyKind::MinimalHybrid,
            state.game_state.pub,
            state.game_state.hands[to_index(state.game_state.pub.phasing)],
            holds_china_for(state.game_state, state.game_state.pub.phasing),
            rng
        );
        fallback.has_value()) {
        node->edges.push_back(MctsEdge{.action = *fallback, .prior = 1.0f});
        node->children.emplace_back(nullptr);
        node->applied_actions.push_back(*fallback);
        return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
    }

    node->is_terminal = true;
    return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
}

// Pre-extracted raw pointers from batch outputs for zero-copy per-item access.
struct RawBatchOutputs {
    const float* card_logits = nullptr;  // [batch, n_card]
    int n_card = 0;
    int card_stride = 0;

    const float* mode_logits = nullptr;  // [batch, n_mode]
    int n_mode = 0;
    int mode_stride = 0;

    const float* country_logits = nullptr;  // [batch, n_country]
    int n_country = 0;
    int country_stride = 0;

    const float* strategy_logits = nullptr;  // [batch, n_strategy]
    int n_strategy = 0;
    int strategy_stride = 0;

    const float* country_strategy_logits = nullptr;  // [batch, n_strat, n_country]
    int cs_n_strategies = 0;
    int cs_n_countries = 0;
    int cs_batch_stride = 0;  // stride between batch items

    const float* value = nullptr;  // [batch, 1]
    int value_stride = 0;

    static RawBatchOutputs extract(const nn::BatchOutputs& outputs) {
        RawBatchOutputs raw;
        auto cont_card = outputs.card_logits.contiguous();
        raw.card_logits = cont_card.data_ptr<float>();
        raw.n_card = std::min(static_cast<int>(cont_card.size(1)), kMaxCardLogits);
        raw.card_stride = static_cast<int>(cont_card.stride(0));

        auto cont_mode = outputs.mode_logits.contiguous();
        raw.mode_logits = cont_mode.data_ptr<float>();
        raw.n_mode = std::min(static_cast<int>(cont_mode.size(1)), kMaxModeLogits);
        raw.mode_stride = static_cast<int>(cont_mode.stride(0));

        if (outputs.country_logits.defined()) {
            auto cont = outputs.country_logits.contiguous();
            raw.country_logits = cont.data_ptr<float>();
            raw.n_country = std::min(static_cast<int>(cont.size(1)), kMaxCountryLogits);
            raw.country_stride = static_cast<int>(cont.stride(0));
        }
        if (outputs.strategy_logits.defined()) {
            auto cont = outputs.strategy_logits.contiguous();
            raw.strategy_logits = cont.data_ptr<float>();
            raw.n_strategy = std::min(static_cast<int>(cont.size(1)), kMaxStrategies);
            raw.strategy_stride = static_cast<int>(cont.stride(0));
        }
        if (outputs.country_strategy_logits.defined()) {
            auto cont = outputs.country_strategy_logits.contiguous();
            raw.country_strategy_logits = cont.data_ptr<float>();
            raw.cs_n_strategies = static_cast<int>(cont.size(1));
            raw.cs_n_countries = static_cast<int>(cont.size(2));
            raw.cs_batch_stride = static_cast<int>(cont.stride(0));
        }
        auto cont_val = outputs.value.contiguous();
        raw.value = cont_val.data_ptr<float>();
        raw.value_stride = static_cast<int>(cont_val.stride(0));

        return raw;
    }
};

ExpansionResult expand_from_raw(
    const TreeState& state,
    const RawBatchOutputs& raw,
    int batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto node = std::make_unique<MctsNode>();
    node->side_to_move = state.game_state.pub.phasing;
    node->edges.reserve(64);
    node->children.reserve(64);
    node->applied_actions.reserve(64);

    auto [drafts, cache] = collect_card_drafts(state);
    const int scoring_cards = count_scoring_cards(state.game_state.hands[to_index(state.game_state.pub.phasing)]);
    const double scoring_prior_boost =
        scoring_card_prior_multiplier(state.game_state, state.game_state.pub.phasing, scoring_cards);
    // --- Copy this item's logits to stack arrays ---
    float card_logits_arr[kMaxCardLogits];
    float mode_logits_arr[kMaxModeLogits];
    float country_logits_arr[kMaxCountryLogits];

    const int n_card = raw.n_card;
    std::memcpy(card_logits_arr, raw.card_logits + batch_index * raw.card_stride,
                static_cast<size_t>(n_card) * sizeof(float));

    const int n_mode = raw.n_mode;
    std::memcpy(mode_logits_arr, raw.mode_logits + batch_index * raw.mode_stride,
                static_cast<size_t>(n_mode) * sizeof(float));

    const float* country_logits_ptr = nullptr;
    int n_country = 0;

    // Prefer strategy-selected raw logits over pre-mixed country_logits (which
    // are already probabilities — applying softmax again would double-softmax).
    if (raw.strategy_logits != nullptr && raw.country_strategy_logits != nullptr &&
        raw.cs_n_countries > 0 && raw.cs_n_strategies > 0) {
        const float* sl = raw.strategy_logits + batch_index * raw.strategy_stride;
        int best_strat = 0;
        float best_val = sl[0];
        for (int s = 1; s < raw.n_strategy; ++s) {
            if (sl[s] > best_val) { best_val = sl[s]; best_strat = s; }
        }
        n_country = std::min(raw.cs_n_countries, kMaxCountryLogits);
        const float* cs_row = raw.country_strategy_logits +
            batch_index * raw.cs_batch_stride +
            best_strat * raw.cs_n_countries;
        std::memcpy(country_logits_arr, cs_row, static_cast<size_t>(n_country) * sizeof(float));
        country_logits_ptr = country_logits_arr;
    } else if (raw.country_logits != nullptr) {
        n_country = raw.n_country;
        std::memcpy(country_logits_arr, raw.country_logits + batch_index * raw.country_stride,
                    static_cast<size_t>(n_country) * sizeof(float));
        country_logits_ptr = country_logits_arr;
    }

    // --- Masked card softmax using raw arrays ---
    float masked_card[kMaxCardLogits];
    std::fill(masked_card, masked_card + n_card, -std::numeric_limits<float>::infinity());
    for (const auto& card : drafts) {
        const int idx = static_cast<int>(card.card_id) - 1;
        if (idx >= 0 && idx < n_card) {
            masked_card[idx] = card_logits_arr[idx];
        }
    }
    softmax_inplace(masked_card, n_card);

    // --- Build edges with raw float math ---
    double total_prior = 0.0;
    for (const auto& card : drafts) {
        float masked_mode[kMaxModeLogits];
        std::fill(masked_mode, masked_mode + n_mode, -std::numeric_limits<float>::infinity());
        for (const auto& mode : card.modes) {
            const int midx = static_cast<int>(mode.mode);
            if (midx < n_mode) {
                masked_mode[midx] = mode_logits_arr[midx];
            }
        }
        softmax_inplace(masked_mode, n_mode);

        const int cidx = static_cast<int>(card.card_id) - 1;
        double card_prob = (cidx >= 0 && cidx < n_card) ? static_cast<double>(masked_card[cidx]) : 0.0;
        if (card_spec(card.card_id).is_scoring) {
            card_prob *= scoring_prior_boost;
        }

        for (const auto& mode : card.modes) {
            const int midx = static_cast<int>(mode.mode);
            const double mode_prob = (midx < n_mode) ? static_cast<double>(masked_mode[midx]) : 0.0;

            if ((mode.mode == ActionMode::Coup || mode.mode == ActionMode::Realign) &&
                country_logits_ptr != nullptr) {
                float masked_country[kMaxCountryLogits];
                std::fill(masked_country, masked_country + n_country, -std::numeric_limits<float>::infinity());
                for (const auto& edge : mode.edges) {
                    const int ci = static_cast<int>(edge.targets.front());
                    if (ci < n_country) {
                        masked_country[ci] = country_logits_arr[ci];
                    }
                }
                softmax_inplace(masked_country, n_country);

                for (const auto& edge : mode.edges) {
                    const int ci = static_cast<int>(edge.targets.front());
                    const double country_prob = (ci < n_country) ? static_cast<double>(masked_country[ci]) : 0.0;
                    const auto prior = card_prob * mode_prob * country_prob;
                    node->edges.push_back(MctsEdge{
                        .action = edge,
                        .prior = static_cast<float>(prior),
                    });
                    node->children.emplace_back(nullptr);
                    node->applied_actions.push_back(edge);
                    total_prior += prior;
                }
                continue;
            }

            const auto per_edge_prior = card_prob * mode_prob;
            for (const auto& edge : mode.edges) {
                node->edges.push_back(MctsEdge{
                    .action = edge,
                    .prior = static_cast<float>(per_edge_prior),
                });
                node->children.emplace_back(nullptr);
                // Resolve influence allocation using cached accessible countries
                if (edge.mode == ActionMode::Influence && country_logits_ptr != nullptr && !cache.influence.empty()) {
                    const auto ops = effective_ops(edge.card_id, state.game_state.pub, state.game_state.pub.phasing);
                    float masked[kMaxCountryLogits];
                    std::fill(masked, masked + n_country, -std::numeric_limits<float>::infinity());
                    for (const auto cid : cache.influence) {
                        const int idx = static_cast<int>(cid);
                        if (idx < n_country) masked[idx] = country_logits_arr[idx];
                    }
                    softmax_inplace(masked, n_country);
                    // Proportional allocation
                    const int n_acc = static_cast<int>(cache.influence.size());
                    int alloc_i[kMaxCountryLogits];
                    int floor_sum = 0;
                    float alloc_f[kMaxCountryLogits];
                    for (int i = 0; i < n_acc; ++i) {
                        float p = masked[static_cast<int>(cache.influence[static_cast<size_t>(i)])];
                        alloc_f[i] = p * static_cast<float>(ops);
                        alloc_i[i] = static_cast<int>(std::floor(alloc_f[i]));
                        floor_sum += alloc_i[i];
                    }
                    int remainder = ops - floor_sum;
                    if (remainder > 0) {
                        std::pair<float, int> order[kMaxCountryLogits];
                        for (int i = 0; i < n_acc; ++i) {
                            order[i] = {-(alloc_f[i] - static_cast<float>(alloc_i[i])), i};
                        }
                        std::sort(order, order + n_acc);
                        for (int i = 0; i < remainder && i < n_acc; ++i) alloc_i[order[i].second] += 1;
                    }
                    ActionEncoding resolved{.card_id = edge.card_id, .mode = edge.mode, .targets = {}};
                    for (int i = 0; i < n_acc; ++i) {
                        for (int j = 0; j < alloc_i[i]; ++j) {
                            resolved.targets.push_back(cache.influence[static_cast<size_t>(i)]);
                        }
                    }
                    node->applied_actions.push_back(std::move(resolved));
                } else {
                    node->applied_actions.push_back(edge);
                }
                total_prior += per_edge_prior;
            }
        }
    }

    if (node->edges.empty()) {
        if (auto fallback = choose_action(
                PolicyKind::MinimalHybrid,
                state.game_state.pub,
                state.game_state.hands[to_index(state.game_state.pub.phasing)],
                holds_china_for(state.game_state, state.game_state.pub.phasing),
                rng
            );
            fallback.has_value()) {
            node->edges.push_back(MctsEdge{.action = *fallback, .prior = 1.0f});
            node->children.emplace_back(nullptr);
            node->applied_actions.push_back(*fallback);
            return ExpansionResult{
                .node = std::move(node),
                .leaf_value = evaluate_leaf_value_raw(state.game_state, raw.value, raw.value_stride, batch_index, config, rng),
            };
        }

        node->is_terminal = true;
        return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
    }

    if (total_prior > 0.0) {
        for (auto& edge : node->edges) {
            edge.prior = static_cast<float>(edge.prior / total_prior);
        }
    } else {
        const auto uniform = 1.0f / static_cast<float>(node->edges.size());
        for (auto& edge : node->edges) {
            edge.prior = uniform;
        }
    }

    return ExpansionResult{
        .node = std::move(node),
        .leaf_value = evaluate_leaf_value_raw(state.game_state, raw.value, raw.value_stride, batch_index, config, rng),
    };
}

void backpropagate_path(std::vector<std::pair<MctsNode*, int>>& path, double leaf_value) {
    for (auto it = path.rbegin(); it != path.rend(); ++it) {
        auto* ancestor = it->first;
        auto& edge = ancestor->edges[static_cast<size_t>(it->second)];
        edge.virtual_loss = std::max(0, edge.virtual_loss - kVirtualLossWeight);
        edge.visit_count += 1;
        edge.total_value += leaf_value;
        ancestor->total_visits += 1;
    }
    path.clear();
}

SelectionResult select_to_leaf(DeterminizationSlot& det, const MctsConfig& config) {
    PendingExpansion pend;
    pend.sim_state.game_state = clone_game_state(det.root_state.game_state);
    pend.sim_state.in_extra_round = det.root_state.in_extra_round;

    MctsNode* node = det.root.get();
    while (node != nullptr && !node->is_terminal && !node->edges.empty()) {
        const auto edge_index = node->select_edge(config.c_puct);
        if (edge_index < 0) {
            break;
        }

        auto& edge = node->edges[static_cast<size_t>(edge_index)];
        edge.virtual_loss += kVirtualLossWeight;
        pend.path.emplace_back(node, edge_index);
        apply_tree_action(pend.sim_state, node->applied_actions[static_cast<size_t>(edge_index)], det.rng);
        if (node->children[static_cast<size_t>(edge_index)] == nullptr) {
            if (auto immediate = expand_without_model(pend.sim_state, det.rng); immediate.has_value()) {
                node->children[static_cast<size_t>(edge_index)] = std::move(immediate->node);
                backpropagate_path(pend.path, immediate->leaf_value);
                return SelectionResult{.needs_batch = false, .leaf_value = immediate->leaf_value};
            }
            det.pending.push_back(std::move(pend));
            return SelectionResult{.needs_batch = true};
        }
        node = node->children[static_cast<size_t>(edge_index)].get();
    }

    double value = 0.0;
    if (node != nullptr && node->is_terminal) {
        value = node->terminal_value;
    }
    backpropagate_path(pend.path, value);
    return SelectionResult{.needs_batch = false, .leaf_value = value};
}

double mean_root_value(const MctsNode& root) {
    if (root.is_terminal) {
        return root.terminal_value;
    }
    if (root.total_visits == 0) {
        return 0.0;
    }

    double total = 0.0;
    for (const auto& edge : root.edges) {
        total += edge.total_value;
    }
    return total / static_cast<double>(root.total_visits);
}

void run_setup_influence_heuristic(GameState& gs, Pcg64Rng& rng) {
    for (const auto side : {Side::USSR, Side::US}) {
        const SetupOpening* opening = (side == Side::USSR)
            ? choose_random_opening(kHumanUSSROpenings.data(),
                                    static_cast<int>(kHumanUSSROpenings.size()), rng)
            : choose_random_opening(kHumanUSOpeningsBid2.data(),
                                    static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
        if (opening == nullptr) {
            continue;
        }
        for (int i = 0; i < opening->count; ++i) {
            const auto country = opening->placements[i].country;
            const auto amount = opening->placements[i].amount;
            gs.pub.set_influence(
                side,
                country,
                gs.pub.influence_of(side, country) + amount
            );
        }
    }
    gs.setup_influence_remaining = {0, 0};
    gs.phase = GamePhase::Headline;
}

std::string end_reason(const PublicState& pub, std::optional<Side> winner, int card_id = -1) {
    if (pub.defcon <= 1) {
        return "defcon1";
    }
    if (card_id == kWargamesCardId) {
        return "wargames";
    }
    if (winner.has_value()) {
        return std::abs(pub.vp) >= 20 ? "vp_threshold" : "europe_control";
    }
    return "vp_threshold";
}

std::optional<GameResult> finish_turn(GameState& gs, int turn) {
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

void reset_search(IsmctsGameSlot& slot) {
    slot.search_active = false;
    slot.dets.clear();
}

void mark_game_done(IsmctsGameSlot& slot, GameResult result) {
    slot.result = std::move(result);
    slot.game_done = true;
    slot.stage = IsmctsGameStage::Finished;
    slot.decision.reset();
    reset_search(slot);
}

void initialize_game_slot(IsmctsGameSlot& slot, int game_index, uint32_t base_seed) {
    const auto seed = base_seed + static_cast<uint32_t>(game_index);
    slot = IsmctsGameSlot{};
    slot.active = true;
    slot.game_index = game_index;
    slot.game_state = reset_game(seed);
    slot.rng = Pcg64Rng(seed);
    run_setup_influence_heuristic(slot.game_state, slot.rng);
    slot.turn = 1;
    slot.stage = IsmctsGameStage::TurnSetup;
}

void advance_after_action_pair(IsmctsGameSlot& slot) {
    if (slot.current_side == Side::USSR) {
        slot.current_side = Side::US;
    } else {
        slot.current_side = Side::USSR;
        slot.current_ar += 1;
    }
}

void move_to_post_round_stage(IsmctsGameSlot& slot) {
    if (slot.game_state.pub.north_sea_oil_extra_ar) {
        slot.game_state.pub.north_sea_oil_extra_ar = false;
        slot.stage = IsmctsGameStage::ExtraActionRoundUS;
        return;
    }
    if (slot.game_state.pub.glasnost_free_ops > 0) {
        resolve_glasnost_free_ops_live(slot.game_state.pub, slot.rng);
    }
    slot.stage = IsmctsGameStage::Cleanup;
}

void move_to_followup_stage_after_extra(IsmctsGameSlot& slot, Side side) {
    if (side == Side::US && slot.game_state.pub.glasnost_free_ops > 0) {
        resolve_glasnost_free_ops_live(slot.game_state.pub, slot.rng);
    }
    slot.stage = IsmctsGameStage::Cleanup;
}

void queue_decision(IsmctsGameSlot& slot, Side side, int ar, bool is_headline) {
    slot.game_state.pub.phasing = side;
    slot.game_state.pub.ar = ar;
    slot.decision = PendingDecision{
        .turn = slot.game_state.pub.turn,
        .ar = ar,
        .side = side,
        .holds_china = holds_china_for(slot.game_state, side),
        .is_headline = is_headline,
        .pub_snapshot = slot.game_state.pub,
        .hand_snapshot = slot.game_state.hands[to_index(side)],
    };
    reset_search(slot);
}

void finalize_headline_choices(IsmctsGameSlot& slot) {
    slot.headline_order.clear();
    for (const auto side : {Side::USSR, Side::US}) {
        if (slot.pending_headlines[to_index(side)].has_value()) {
            slot.headline_order.push_back(*slot.pending_headlines[to_index(side)]);
        }
    }

    if (slot.pending_headlines[to_index(Side::US)].has_value() &&
        slot.pending_headlines[to_index(Side::US)]->action.card_id == 108 &&
        slot.pending_headlines[to_index(Side::USSR)].has_value()) {
        slot.game_state.pub.discard.set(slot.pending_headlines[to_index(Side::USSR)]->action.card_id);
        slot.headline_order.erase(
            std::remove_if(
                slot.headline_order.begin(),
                slot.headline_order.end(),
                [](const PendingHeadlineChoice& pending) { return pending.side == Side::USSR; }
            ),
            slot.headline_order.end()
        );
    }

    std::sort(slot.headline_order.begin(), slot.headline_order.end(), [](const auto& lhs, const auto& rhs) {
        const auto lhs_ops = card_spec(lhs.action.card_id).ops;
        const auto rhs_ops = card_spec(rhs.action.card_id).ops;
        if (lhs_ops != rhs_ops) {
            return lhs_ops > rhs_ops;
        }
        return static_cast<int>(lhs.side) > static_cast<int>(rhs.side);
    });

    slot.headline_order_index = 0;
    slot.stage = IsmctsGameStage::HeadlineResolve;
}

void commit_selected_action(IsmctsGameSlot& slot, ActionEncoding action) {
    if (!slot.decision.has_value()) {
        return;
    }

    if (action.card_id == 0) {
        action = choose_action(
            PolicyKind::MinimalHybrid,
            slot.decision->pub_snapshot,
            slot.decision->hand_snapshot,
            slot.decision->holds_china,
            slot.rng
        ).value_or(ActionEncoding{});
    }
    if (action.card_id == 0) {
        throw std::runtime_error("ISMCTS benchmark could not resolve an action");
    }

    const auto decision = *slot.decision;
    slot.decision.reset();
    reset_search(slot);

    if (decision.is_headline) {
        action.mode = ActionMode::Event;
        action.targets.clear();
        auto& hand = slot.game_state.hands[to_index(decision.side)];
        if (hand.test(action.card_id)) {
            hand.reset(action.card_id);
        }
        slot.pending_headlines[to_index(decision.side)] = PendingHeadlineChoice{
            .side = decision.side,
            .holds_china = decision.holds_china,
            .hand_snapshot = decision.hand_snapshot,
            .action = action,
        };
        if (decision.side == Side::USSR) {
            slot.stage = IsmctsGameStage::HeadlineChoiceUS;
        } else {
            finalize_headline_choices(slot);
        }
        return;
    }

    auto& hand = slot.game_state.hands[to_index(decision.side)];
    if (hand.test(action.card_id)) {
        hand.reset(action.card_id);
    }

    auto [new_pub, over, winner] = apply_action_live(slot.game_state, action, decision.side, slot.rng);
    (void)new_pub;
    sync_china_flags(slot.game_state);

    if (over) {
        mark_game_done(slot, GameResult{
            .winner = winner,
            .final_vp = slot.game_state.pub.vp,
            .end_turn = slot.game_state.pub.turn,
            .end_reason = end_reason(slot.game_state.pub, winner),
        });
        return;
    }

    if (decision.side == Side::USSR && slot.game_state.pub.norad_active && slot.game_state.pub.defcon == 2) {
        if (auto norad = resolve_norad_live(slot.game_state, slot.rng); norad.has_value()) {
            auto& [norad_pub, norad_over, norad_winner] = *norad;
            (void)norad_pub;
            if (norad_over) {
                mark_game_done(slot, GameResult{
                    .winner = norad_winner,
                    .final_vp = slot.game_state.pub.vp,
                    .end_turn = slot.game_state.pub.turn,
                    .end_reason = end_reason(slot.game_state.pub, norad_winner),
                });
                return;
            }
        }
    }

    if (slot.stage == IsmctsGameStage::ActionRound) {
        advance_after_action_pair(slot);
        return;
    }
    if (slot.stage == IsmctsGameStage::ExtraActionRoundUS ||
        slot.stage == IsmctsGameStage::ExtraActionRoundUSSR) {
        move_to_followup_stage_after_extra(slot, decision.side);
    }
}

void resolve_heuristic_decision(IsmctsGameSlot& slot) {
    if (!slot.decision.has_value()) {
        return;
    }
    auto action = choose_action(
        PolicyKind::MinimalHybrid,
        slot.decision->pub_snapshot,
        slot.decision->hand_snapshot,
        slot.decision->holds_china,
        slot.rng
    ).value_or(ActionEncoding{});
    commit_selected_action(slot, action);
}

/// Select a greedy (argmax) action from model logits for a single state.
/// Uses batch-1 inference: fill one slot, run forward, pick best legal action.
ActionEncoding greedy_action_from_model(
    torch::jit::script::Module& model,
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    Side side,
    Pcg64Rng& rng,
    torch::Device device
) {
    // Heuristic fallback used when model output is degenerate.
    const auto heuristic_fallback = [&]() -> ActionEncoding {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
            .value_or(ActionEncoding{});
    };

    auto playable = legal_cards(hand, pub, side, holds_china);
    if (playable.empty()) {
        return heuristic_fallback();
    }

    // Batch-1 forward pass.
    nn::BatchInputs inputs;
    inputs.allocate(1, device);
    inputs.fill_slot(0, pub, hand, holds_china, side);
    inputs.filled = 1;
    const auto outputs = nn::forward_model_batched(model, inputs);
    constexpr int64_t bi = 0;

    const auto card_logits = outputs.card_logits.index({bi});
    const auto mode_logits = outputs.mode_logits.index({bi});
    const auto country_logits_raw = outputs.country_logits.defined()
        ? outputs.country_logits.index({bi})
        : torch::Tensor{};
    const auto marginal_logits_raw = outputs.marginal_logits.defined()
        ? outputs.marginal_logits.index({bi})
        : torch::Tensor{};
    const auto strategy_logits_raw = outputs.strategy_logits.defined()
        ? outputs.strategy_logits.index({bi})
        : torch::Tensor{};
    const auto country_strategy_logits_raw = outputs.country_strategy_logits.defined()
        ? outputs.country_strategy_logits.index({bi})
        : torch::Tensor{};

    auto decode_pub = pub;
    decode_pub.phasing = side;
    auto action = decode::choose_greedy_action_from_outputs(
        decode_pub,
        hand,
        holds_china,
        /*use_country_head=*/true,
        card_logits,
        mode_logits,
        country_logits_raw,
        strategy_logits_raw,
        country_strategy_logits_raw,
        rng,
        heuristic_fallback,
        heuristic_fallback,
        marginal_logits_raw
    );

    if (action.mode == ActionMode::Space && action.targets.empty()) {
        const auto& cache = AccessibleCache::build(side, pub);
        if (!cache.influence.empty()) {
            action.targets.push_back(cache.influence.front());
        }
    }

    return action;
}

void resolve_model_decision(
    IsmctsGameSlot& slot,
    torch::jit::script::Module& model,
    torch::Device device
) {
    if (!slot.decision.has_value()) {
        return;
    }
    const auto& dec = *slot.decision;
    // Set phasing so greedy_action_from_model reads the correct side.
    slot.game_state.pub.phasing = dec.side;
    auto action = greedy_action_from_model(
        model,
        dec.pub_snapshot,
        dec.hand_snapshot,
        dec.holds_china,
        dec.side,
        slot.rng,
        device
    );
    commit_selected_action(slot, action);
}

// Resolve an opponent decision using either heuristic or model policy.
// When opponent_model is non-null, use greedy model inference; otherwise use heuristic.
void resolve_opponent_decision(
    IsmctsGameSlot& slot,
    torch::jit::script::Module* opponent_model,
    torch::Device device
) {
    if (opponent_model != nullptr) {
        resolve_model_decision(slot, *opponent_model, device);
    } else {
        resolve_heuristic_decision(slot);
    }
}

void advance_until_search_or_done(
    IsmctsGameSlot& slot,
    Side learned_side,
    torch::jit::script::Module* opponent_model = nullptr,
    torch::Device device = torch::kCPU
) {
    constexpr int kMaxAdvanceSteps = 50000;  // well above any legitimate 10-turn game
    int guard_steps = 0;
    while (slot.active && !slot.game_done && !slot.decision.has_value()) {
        if (++guard_steps > kMaxAdvanceSteps) {
            // Infinite loop detected — force game to end as a draw.
            // This is a fatal engine bug; log and terminate gracefully.
            std::fprintf(stderr,
                "[ISMCTS] advance_until_search_or_done: exceeded %d steps "
                "(turn=%d ar=%d stage=%d) — forcing game end to avoid hang\n",
                kMaxAdvanceSteps,
                slot.game_state.pub.turn,
                slot.game_state.pub.ar,
                static_cast<int>(slot.stage));
            mark_game_done(slot, GameResult{
                .winner = std::nullopt,
                .final_vp = slot.game_state.pub.vp,
                .end_turn = slot.game_state.pub.turn,
                .end_reason = "loop_guard",
            });
            break;
        }
        switch (slot.stage) {
            case IsmctsGameStage::TurnSetup: {
                slot.game_state.pub.turn = slot.turn;
                if (slot.turn == kMidWarTurn) {
                    advance_to_mid_war(slot.game_state, slot.rng);
                } else if (slot.turn == kLateWarTurn) {
                    advance_to_late_war(slot.game_state, slot.rng);
                }
                deal_cards(slot.game_state, Side::USSR, slot.rng);
                deal_cards(slot.game_state, Side::US, slot.rng);
                slot.pending_headlines = {};
                slot.headline_order.clear();
                slot.headline_order_index = 0;
                slot.total_ars = ars_for_turn(slot.turn);
                slot.current_ar = 1;
                slot.current_side = Side::USSR;
                slot.stage = IsmctsGameStage::HeadlineChoiceUSSR;
                break;
            }

            case IsmctsGameStage::HeadlineChoiceUSSR:
            case IsmctsGameStage::HeadlineChoiceUS: {
                const auto side = slot.stage == IsmctsGameStage::HeadlineChoiceUSSR ? Side::USSR : Side::US;
                const auto holds_china = holds_china_for(slot.game_state, side);
                if (!has_legal_action(slot.game_state.hands[to_index(side)], slot.game_state.pub, side, holds_china)) {
                    if (side == Side::USSR) {
                        slot.stage = IsmctsGameStage::HeadlineChoiceUS;
                    } else {
                        finalize_headline_choices(slot);
                    }
                    break;
                }
                slot.game_state.phase = GamePhase::Headline;
                queue_decision(slot, side, /*ar=*/0, /*is_headline=*/true);
                if (side != learned_side) {
                    resolve_opponent_decision(slot, opponent_model, device);
                }
                break;
            }

            case IsmctsGameStage::HeadlineResolve: {
                if (slot.headline_order_index >= slot.headline_order.size()) {
                    slot.stage = IsmctsGameStage::ActionRound;
                    break;
                }

                const auto pending = slot.headline_order[slot.headline_order_index++];
                auto [new_pub, over, winner] = apply_action_live(slot.game_state, pending.action, pending.side, slot.rng);
                (void)new_pub;
                sync_china_flags(slot.game_state);
                if (over) {
                    mark_game_done(slot, GameResult{
                        .winner = winner,
                        .final_vp = slot.game_state.pub.vp,
                        .end_turn = slot.game_state.pub.turn,
                        .end_reason = end_reason(slot.game_state.pub, winner),
                    });
                }
                break;
            }

            case IsmctsGameStage::ActionRound: {
                if (slot.current_ar > kSpaceShuttleArs) {
                    move_to_post_round_stage(slot);
                    break;
                }

                const auto side = slot.current_side;
                if (slot.current_ar > slot.total_ars && slot.game_state.pub.space[to_index(side)] < kSpaceShuttleArs) {
                    advance_after_action_pair(slot);
                    break;
                }

                slot.game_state.phase = GamePhase::ActionRound;
                slot.game_state.pub.ar = slot.current_ar;
                slot.game_state.pub.phasing = side;
                if (
                    auto cmc_result = resolve_cuban_missile_crisis_cancel_live(slot.game_state, side, slot.rng);
                    cmc_result.has_value()
                ) {
                    auto& [new_pub, over, winner] = *cmc_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.game_state.pub.vp,
                            .end_turn = slot.game_state.pub.turn,
                            .end_reason = end_reason(slot.game_state.pub, winner),
                        });
                        break;
                    }
                    advance_after_action_pair(slot);
                    break;
                }
                if (auto trap_result = resolve_trap_ar_live(slot.game_state, side, slot.rng); trap_result.has_value()) {
                    auto& [new_pub, over, winner] = *trap_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.game_state.pub.vp,
                            .end_turn = slot.game_state.pub.turn,
                            .end_reason = end_reason(slot.game_state.pub, winner),
                        });
                        break;
                    }
                    advance_after_action_pair(slot);
                    break;
                }

                const auto holds_china = holds_china_for(slot.game_state, side);
                if (!has_legal_action(slot.game_state.hands[to_index(side)], slot.game_state.pub, side, holds_china)) {
                    advance_after_action_pair(slot);
                    break;
                }
                queue_decision(slot, side, slot.current_ar, /*is_headline=*/false);
                if (side != learned_side) {
                    resolve_opponent_decision(slot, opponent_model, device);
                }
                break;
            }

            case IsmctsGameStage::ExtraActionRoundUS:
            case IsmctsGameStage::ExtraActionRoundUSSR: {
                const auto side = slot.stage == IsmctsGameStage::ExtraActionRoundUS ? Side::US : Side::USSR;
                slot.game_state.pub.ar = std::max(slot.game_state.pub.ar, ars_for_turn(slot.game_state.pub.turn)) + 1;
                slot.game_state.pub.phasing = side;
                auto& hand = slot.game_state.hands[to_index(side)];
                if (
                    auto cmc_result = resolve_cuban_missile_crisis_cancel_live(slot.game_state, side, slot.rng);
                    cmc_result.has_value()
                ) {
                    auto& [new_pub, over, winner] = *cmc_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.game_state.pub.vp,
                            .end_turn = slot.game_state.pub.turn,
                            .end_reason = end_reason(slot.game_state.pub, winner),
                        });
                        break;
                    }
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }
                if (hand.none()) {
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }
                if (auto trap_result = resolve_trap_ar_live(slot.game_state, side, slot.rng); trap_result.has_value()) {
                    auto& [new_pub, over, winner] = *trap_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.game_state.pub.vp,
                            .end_turn = slot.game_state.pub.turn,
                            .end_reason = end_reason(slot.game_state.pub, winner),
                        });
                        break;
                    }
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }

                const auto holds_china = holds_china_for(slot.game_state, side);
                if (!has_legal_action(hand, slot.game_state.pub, side, holds_china)) {
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }
                queue_decision(slot, side, slot.game_state.pub.ar, /*is_headline=*/false);
                if (side != learned_side) {
                    resolve_opponent_decision(slot, opponent_model, device);
                }
                break;
            }

            case IsmctsGameStage::Cleanup: {
                if (auto result = finish_turn(slot.game_state, slot.turn); result.has_value()) {
                    mark_game_done(slot, *result);
                    break;
                }
                if (slot.turn >= kMaxTurns) {
                    std::optional<Side> winner;
                    if (slot.game_state.pub.vp > 0) {
                        winner = Side::USSR;
                    } else if (slot.game_state.pub.vp < 0) {
                        winner = Side::US;
                    }
                    mark_game_done(slot, GameResult{
                        .winner = winner,
                        .final_vp = slot.game_state.pub.vp,
                        .end_turn = kMaxTurns,
                        .end_reason = "turn_limit",
                    });
                    break;
                }
                slot.turn += 1;
                slot.stage = IsmctsGameStage::TurnSetup;
                break;
            }

            case IsmctsGameStage::Finished:
                slot.game_done = true;
                break;
        }
    }
}

void start_search(IsmctsGameSlot& slot, const IsmctsConfig& config) {
    if (!slot.decision.has_value()) {
        return;
    }

    const auto acting_side = slot.decision->side;
    const auto obs = make_observation(slot.game_state, acting_side);

    slot.dets.clear();
    slot.dets.reserve(static_cast<size_t>(config.n_determinizations));
    for (int i = 0; i < config.n_determinizations; ++i) {
        Pcg64Rng local_rng(slot.rng.next_u64());
        auto determinized = determinize(obs, local_rng);
        DeterminizationSlot det;
        det.root_state.game_state = std::move(determinized);
        det.root_state.in_extra_round = slot.stage == IsmctsGameStage::ExtraActionRoundUS ||
                                        slot.stage == IsmctsGameStage::ExtraActionRoundUSSR;
        for (const auto side : {Side::USSR, Side::US}) {
            if (slot.pending_headlines[to_index(side)].has_value()) {
                det.root_state.game_state.headline_card[to_index(side)] =
                    slot.pending_headlines[to_index(side)]->action.card_id;
            }
        }
        det.rng = std::move(local_rng);
        slot.dets.push_back(std::move(det));
    }
    slot.search_active = true;
}

bool determinization_complete(const DeterminizationSlot& det, int sims_target) {
    return det.root != nullptr && det.sims_completed >= sims_target && det.pending.empty();
}

int sims_budget(const DeterminizationSlot& det, int sims_target, int max_pending) {
    if (det.root == nullptr && det.pending.empty()) return 1;  // root expansion
    if (det.root == nullptr) return 0;  // root pending
    int in_flight = static_cast<int>(det.pending.size());
    int remaining = sims_target - det.sims_completed - in_flight;
    int slot_capacity = max_pending - in_flight;
    return std::max(0, std::min(remaining, slot_capacity));
}

bool search_complete(const IsmctsGameSlot& slot, int sims_target) {
    if (!slot.search_active || slot.dets.empty()) {
        return false;
    }
    return std::all_of(slot.dets.begin(), slot.dets.end(), [sims_target](const DeterminizationSlot& det) {
        return determinization_complete(det, sims_target);
    });
}

IsmctsResult aggregate_result(const IsmctsGameSlot& slot, const IsmctsConfig& config) {
    std::vector<AggregatedEdgeState> aggregated;
    aggregated.reserve(32);
    double total_root_value = 0.0;

    for (const auto& det : slot.dets) {
        if (det.root == nullptr) {
            continue;
        }
        total_root_value += mean_root_value(*det.root);
        for (size_t edge_index = 0; edge_index < det.root->edges.size(); ++edge_index) {
            const auto resolved_action = edge_index < det.root->applied_actions.size()
                ? det.root->applied_actions[edge_index]
                : det.root->edges[edge_index].action;
            const auto& edge = det.root->edges[edge_index];
            const auto found = std::find_if(
                aggregated.begin(),
                aggregated.end(),
                [&resolved_action](const AggregatedEdgeState& state) { return state.edge.action == resolved_action; }
            );
            if (found == aggregated.end()) {
                aggregated.push_back(AggregatedEdgeState{
                    .edge = MctsEdge{
                        .action = resolved_action,
                        .prior = edge.prior,
                        .visit_count = edge.visit_count,
                        .virtual_loss = 0,
                        .total_value = edge.total_value,
                    },
                    .occurrences = 1,
                });
                continue;
            }

            found->edge.prior += edge.prior;
            found->edge.visit_count += edge.visit_count;
            found->edge.total_value += edge.total_value;
            found->occurrences += 1;
        }
    }

    IsmctsResult result;
    result.total_determinizations = config.n_determinizations;
    if (!slot.dets.empty()) {
        result.mean_root_value = total_root_value / static_cast<double>(slot.dets.size());
    }
    result.aggregated_edges.reserve(aggregated.size());

    for (auto& state : aggregated) {
        if (state.occurrences > 0) {
            state.edge.prior /= static_cast<float>(state.occurrences);
        }
        result.aggregated_edges.push_back(std::move(state.edge));
    }

    std::sort(
        result.aggregated_edges.begin(),
        result.aggregated_edges.end(),
        [](const MctsEdge& lhs, const MctsEdge& rhs) { return aggregated_edge_better(lhs, rhs); }
    );

    if (!result.aggregated_edges.empty()) {
        result.best_action = result.aggregated_edges.front().action;
    }
    return result;
}

void queue_batch_item(
    nn::BatchInputs& batch_inputs,
    std::vector<BatchEntry>& batch_entries,
    IsmctsGameSlot& game_slot,
    DeterminizationSlot& det
) {
    // The last pending expansion is the one we just added
    const auto pending_index = det.pending.size() - 1;
    const auto& state = det.pending[pending_index].sim_state;
    const auto batch_index = batch_inputs.filled;
    batch_inputs.fill_slot(
        batch_index,
        state.game_state.pub,
        state.game_state.hands[to_index(state.game_state.pub.phasing)],
        holds_china_for(state.game_state, state.game_state.pub.phasing),
        state.game_state.pub.phasing
    );
    batch_entries.push_back(BatchEntry{
        .game = &game_slot,
        .det = &det,
        .pending_index = pending_index,
    });
}

}  // namespace

GameState sample_determinization(
    const GameState& gs,
    Side acting_side,
    [[maybe_unused]] int opp_hand_size,  // derived from oracle gs via make_observation
    Pcg64Rng& rng
) {
    return determinize(make_observation(gs, acting_side), rng);
}

IsmctsResult ismcts_search(
    const Observation& obs,
    torch::jit::script::Module& model,
    const IsmctsConfig& config,
    Pcg64Rng& rng
) {
    if (config.n_determinizations <= 0) {
        throw std::invalid_argument("n_determinizations must be positive");
    }

    std::vector<AggregatedEdgeState> aggregated;
    aggregated.reserve(32);
    double total_root_value = 0.0;

    for (int i = 0; i < config.n_determinizations; ++i) {
        Pcg64Rng local_rng(rng.next_u64());
        auto determinized = determinize(obs, local_rng);
        const auto result = mcts_search(determinized, model, config.mcts_config, local_rng);
        total_root_value += result.root_value;

        for (const auto& edge : result.root_edges) {
            const auto found = std::find_if(
                aggregated.begin(),
                aggregated.end(),
                [&edge](const AggregatedEdgeState& state) { return state.edge.action == edge.action; }
            );
            if (found == aggregated.end()) {
                aggregated.push_back(AggregatedEdgeState{
                    .edge = MctsEdge{
                        .action = edge.action,
                        .prior = edge.prior,
                        .visit_count = edge.visit_count,
                        .virtual_loss = 0,
                        .total_value = edge.total_value,
                    },
                    .occurrences = 1,
                });
                continue;
            }

            found->edge.prior += edge.prior;
            found->edge.visit_count += edge.visit_count;
            found->edge.total_value += edge.total_value;
            found->occurrences += 1;
        }
    }

    IsmctsResult ismcts_result;
    ismcts_result.total_determinizations = config.n_determinizations;
    ismcts_result.mean_root_value = total_root_value / static_cast<double>(config.n_determinizations);
    ismcts_result.aggregated_edges.reserve(aggregated.size());

    for (auto& state : aggregated) {
        if (state.occurrences > 0) {
            state.edge.prior /= static_cast<float>(state.occurrences);
        }
        ismcts_result.aggregated_edges.push_back(std::move(state.edge));
    }

    std::sort(
        ismcts_result.aggregated_edges.begin(),
        ismcts_result.aggregated_edges.end(),
        [](const MctsEdge& lhs, const MctsEdge& rhs) { return aggregated_edge_better(lhs, rhs); }
    );

    if (!ismcts_result.aggregated_edges.empty()) {
        ismcts_result.best_action = ismcts_result.aggregated_edges.front().action;
    }
    return ismcts_result;
}

std::vector<GameResult> play_ismcts_matchup(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    const IsmctsConfig& config,
    uint32_t base_seed
) {
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(std::max(0, n_games)));

    for (int i = 0; i < n_games; ++i) {
        const auto seed = base_seed + static_cast<uint32_t>(i);
        auto gs = reset_game(seed);
        Pcg64Rng rng(seed);

        for (const auto side : {Side::USSR, Side::US}) {
            const SetupOpening* opening = (side == Side::USSR)
                ? choose_random_opening(kHumanUSSROpenings.data(),
                                        static_cast<int>(kHumanUSSROpenings.size()), rng)
                : choose_random_opening(kHumanUSOpeningsBid2.data(),
                                        static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
            if (opening == nullptr) {
                continue;
            }
            for (int j = 0; j < opening->count; ++j) {
                gs.pub.set_influence(side, opening->placements[j].country,
                    gs.pub.influence_of(side, opening->placements[j].country) + opening->placements[j].amount);
            }
        }
        gs.setup_influence_remaining = {0, 0};
        gs.phase = GamePhase::Headline;

        const PolicyFn ismcts_fn = [&gs, &model, &config](
            const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& local_rng
        ) -> std::optional<ActionEncoding> {
            const auto acting = pub.phasing;
            const auto obs = make_observation(gs, acting);
            auto result = ismcts_search(obs, model, config, local_rng);
            return result.best_action;
        };

        const PolicyFn heuristic_fn = [](
            const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& local_rng
        ) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, local_rng);
        };

        GameLoopConfig loop_config;
        loop_config.skip_setup_influence = true;

        const auto& ussr_fn = (learned_side == Side::USSR) ? ismcts_fn : heuristic_fn;
        const auto& us_fn = (learned_side == Side::US) ? ismcts_fn : heuristic_fn;

        auto traced = play_game_traced_from_state_ref_with_rng(gs, ussr_fn, us_fn, rng, loop_config);
        results.push_back(std::move(traced.result));
    }
    return results;
}

std::vector<GameResult> play_ismcts_matchup_pooled(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    const IsmctsConfig& config,
    int pool_size,
    uint32_t base_seed,
    torch::Device device
) {
    if (n_games <= 0) {
        return {};
    }
    if (!is_player_side(learned_side)) {
        throw std::invalid_argument("learned_side must be USSR or US");
    }
    if (config.n_determinizations <= 0) {
        throw std::invalid_argument("n_determinizations must be positive");
    }
    if (pool_size <= 0) {
        throw std::invalid_argument("pool_size must be positive");
    }

    std::vector<IsmctsGameSlot> pool(static_cast<size_t>(pool_size));
    int games_started = 0;
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(n_games));

    const int max_pending = config.max_pending_per_det;
    const int max_batch = pool_size * config.n_determinizations * max_pending;
    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(max_batch, device);
    std::vector<BatchEntry> batch_entries;
    batch_entries.reserve(static_cast<size_t>(max_batch));

    using Clock = std::chrono::high_resolution_clock;
    double t_advance = 0, t_select = 0, t_nn = 0, t_expand = 0, t_apply = 0;
    int n_batches = 0, total_batch_items = 0;

    while (static_cast<int>(results.size()) < n_games) {
        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                results.push_back(slot.result);
                slot.emitted = true;
                slot.active = false;
            }
            if (!slot.active && games_started < n_games) {
                initialize_game_slot(slot, games_started, base_seed);
                games_started += 1;
            }
        }

        batch_inputs.reset();
        batch_entries.clear();

        for (auto& slot : pool) {
            if (!slot.active || slot.game_done) {
                continue;
            }

            if (!slot.search_active) {
                auto t0 = Clock::now();
                advance_until_search_or_done(slot, learned_side);
                t_advance += std::chrono::duration<double>(Clock::now() - t0).count();
                if (slot.game_done || !slot.decision.has_value()) {
                    continue;
                }
                start_search(slot, config);
            }

            auto t0s = Clock::now();
            for (auto& det : slot.dets) {
                if (determinization_complete(det, config.mcts_config.n_simulations)) {
                    continue;
                }

                // Root expansion: create a PendingExpansion for the root state
                if (det.root == nullptr && det.pending.empty()) {
                    if (auto immediate = expand_without_model(det.root_state, det.rng); immediate.has_value()) {
                        det.root = std::move(immediate->node);
                        apply_root_dirichlet_noise(*det.root, config.mcts_config, det.rng);
                    } else {
                        PendingExpansion pend;
                        pend.sim_state.game_state = clone_game_state(det.root_state.game_state);
                        pend.sim_state.in_extra_round = det.root_state.in_extra_round;
                        pend.is_root_expansion = true;
                        det.pending.push_back(std::move(pend));
                        queue_batch_item(batch_inputs, batch_entries, slot, det);
                    }
                    continue;
                }
                if (det.root == nullptr) {
                    continue;  // root expansion pending
                }

                // Select multiple leaves per det (up to max_pending)
                for (;;) {
                    const int budget = sims_budget(det, config.mcts_config.n_simulations, max_pending);
                    if (budget <= 0) break;
                    const auto selection = select_to_leaf(det, config.mcts_config);
                    if (selection.needs_batch) {
                        queue_batch_item(batch_inputs, batch_entries, slot, det);
                    } else {
                        det.sims_completed += 1;
                    }
                }
            }
            t_select += std::chrono::duration<double>(Clock::now() - t0s).count();
        }

        if (!batch_entries.empty()) {
            n_batches += 1;
            total_batch_items += static_cast<int>(batch_entries.size());
            auto t0n = Clock::now();
            const auto outputs = nn::forward_model_batched(model, batch_inputs);
            t_nn += std::chrono::duration<double>(Clock::now() - t0n).count();
            auto t0e = Clock::now();
            const auto raw = RawBatchOutputs::extract(outputs);
            for (size_t i = 0; i < batch_entries.size(); ++i) {
                auto& entry = batch_entries[i];
                const auto batch_index = static_cast<int>(i);
                auto& pend = entry.det->pending[entry.pending_index];
                if (pend.is_root_expansion) {
                    auto expansion = expand_from_raw(
                        pend.sim_state,
                        raw,
                        batch_index,
                        config.mcts_config,
                        entry.det->rng
                    );
                    entry.det->root = std::move(expansion.node);
                    apply_root_dirichlet_noise(*entry.det->root, config.mcts_config, entry.det->rng);
                } else {
                    auto expansion = expand_from_raw(
                        pend.sim_state,
                        raw,
                        batch_index,
                        config.mcts_config,
                        entry.det->rng
                    );
                    auto& [parent, edge_index] = pend.path.back();
                    parent->children[static_cast<size_t>(edge_index)] = std::move(expansion.node);
                    backpropagate_path(pend.path, expansion.leaf_value);
                    entry.det->sims_completed += 1;
                }
            }
            // Clear all processed pending expansions
            for (auto& slot : pool) {
                for (auto& det : slot.dets) {
                    det.pending.clear();
                }
            }
            t_expand += std::chrono::duration<double>(Clock::now() - t0e).count();
        }

        auto t0a = Clock::now();
        for (auto& slot : pool) {
            if (!search_complete(slot, config.mcts_config.n_simulations)) {
                continue;
            }

            auto result = aggregate_result(slot, config);
            auto action = result.best_action;
            if (action.card_id == 0 && slot.decision.has_value()) {
                action = choose_action(
                    PolicyKind::MinimalHybrid,
                    slot.decision->pub_snapshot,
                    slot.decision->hand_snapshot,
                    slot.decision->holds_china,
                    slot.rng
                ).value_or(ActionEncoding{});
            }
            commit_selected_action(slot, action);
        }
        t_apply += std::chrono::duration<double>(Clock::now() - t0a).count();
    }

    const double total = t_advance + t_select + t_nn + t_expand + t_apply;
    fprintf(stderr, "[ISMCTS profile] advance=%.3fs select=%.3fs nn=%.3fs expand=%.3fs apply=%.3fs total=%.3fs\n",
            t_advance, t_select, t_nn, t_expand, t_apply, total);
    fprintf(stderr, "[ISMCTS profile] batches=%d items=%d avg_batch=%.1f\n",
            n_batches, total_batch_items, n_batches > 0 ? double(total_batch_items) / n_batches : 0.0);

    return results;
}

std::vector<GameResult> play_ismcts_vs_model_pooled(
    int n_games,
    torch::jit::script::Module& search_model,
    torch::jit::script::Module& opponent_model,
    Side search_side,
    const IsmctsConfig& config,
    int pool_size,
    uint32_t base_seed,
    torch::Device device
) {
    if (n_games <= 0) {
        return {};
    }
    if (!is_player_side(search_side)) {
        throw std::invalid_argument("search_side must be USSR or US");
    }
    if (config.n_determinizations <= 0) {
        throw std::invalid_argument("n_determinizations must be positive");
    }
    if (pool_size <= 0) {
        throw std::invalid_argument("pool_size must be positive");
    }

    std::vector<IsmctsGameSlot> pool(static_cast<size_t>(pool_size));
    int games_started = 0;
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(n_games));

    const int max_pending = config.max_pending_per_det;
    const int max_batch = pool_size * config.n_determinizations * max_pending;
    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(max_batch, device);
    std::vector<BatchEntry> batch_entries;
    batch_entries.reserve(static_cast<size_t>(max_batch));

    using Clock = std::chrono::high_resolution_clock;
    double t_advance = 0, t_select = 0, t_nn = 0, t_expand = 0, t_apply = 0;
    int n_batches = 0, total_batch_items = 0;

    while (static_cast<int>(results.size()) < n_games) {
        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                results.push_back(slot.result);
                slot.emitted = true;
                slot.active = false;
            }
            if (!slot.active && games_started < n_games) {
                initialize_game_slot(slot, games_started, base_seed);
                games_started += 1;
            }
        }

        batch_inputs.reset();
        batch_entries.clear();

        for (auto& slot : pool) {
            if (!slot.active || slot.game_done) {
                continue;
            }

            if (!slot.search_active) {
                auto t0 = Clock::now();
                advance_until_search_or_done(slot, search_side, &opponent_model, device);
                t_advance += std::chrono::duration<double>(Clock::now() - t0).count();
                if (slot.game_done || !slot.decision.has_value()) {
                    continue;
                }
                start_search(slot, config);
            }

            auto t0s = Clock::now();
            for (auto& det : slot.dets) {
                if (determinization_complete(det, config.mcts_config.n_simulations)) {
                    continue;
                }

                if (det.root == nullptr && det.pending.empty()) {
                    if (auto immediate = expand_without_model(det.root_state, det.rng); immediate.has_value()) {
                        det.root = std::move(immediate->node);
                        apply_root_dirichlet_noise(*det.root, config.mcts_config, det.rng);
                    } else {
                        PendingExpansion pend;
                        pend.sim_state.game_state = clone_game_state(det.root_state.game_state);
                        pend.sim_state.in_extra_round = det.root_state.in_extra_round;
                        pend.is_root_expansion = true;
                        det.pending.push_back(std::move(pend));
                        queue_batch_item(batch_inputs, batch_entries, slot, det);
                    }
                    continue;
                }
                if (det.root == nullptr) {
                    continue;
                }

                for (;;) {
                    const int budget = sims_budget(det, config.mcts_config.n_simulations, max_pending);
                    if (budget <= 0) break;
                    const auto selection = select_to_leaf(det, config.mcts_config);
                    if (selection.needs_batch) {
                        queue_batch_item(batch_inputs, batch_entries, slot, det);
                    } else {
                        det.sims_completed += 1;
                    }
                }
            }
            t_select += std::chrono::duration<double>(Clock::now() - t0s).count();
        }

        if (!batch_entries.empty()) {
            n_batches += 1;
            total_batch_items += static_cast<int>(batch_entries.size());
            auto t0n = Clock::now();
            const auto outputs = nn::forward_model_batched(search_model, batch_inputs);
            t_nn += std::chrono::duration<double>(Clock::now() - t0n).count();
            auto t0e = Clock::now();
            const auto raw = RawBatchOutputs::extract(outputs);
            for (size_t i = 0; i < batch_entries.size(); ++i) {
                auto& entry = batch_entries[i];
                const auto batch_index = static_cast<int>(i);
                auto& pend = entry.det->pending[entry.pending_index];
                if (pend.is_root_expansion) {
                    auto expansion = expand_from_raw(
                        pend.sim_state,
                        raw,
                        batch_index,
                        config.mcts_config,
                        entry.det->rng
                    );
                    entry.det->root = std::move(expansion.node);
                    apply_root_dirichlet_noise(*entry.det->root, config.mcts_config, entry.det->rng);
                } else {
                    auto expansion = expand_from_raw(
                        pend.sim_state,
                        raw,
                        batch_index,
                        config.mcts_config,
                        entry.det->rng
                    );
                    auto& [parent, edge_index] = pend.path.back();
                    parent->children[static_cast<size_t>(edge_index)] = std::move(expansion.node);
                    backpropagate_path(pend.path, expansion.leaf_value);
                    entry.det->sims_completed += 1;
                }
            }
            for (auto& slot : pool) {
                for (auto& det : slot.dets) {
                    det.pending.clear();
                }
            }
            t_expand += std::chrono::duration<double>(Clock::now() - t0e).count();
        }

        auto t0a = Clock::now();
        for (auto& slot : pool) {
            if (!search_complete(slot, config.mcts_config.n_simulations)) {
                continue;
            }

            auto result = aggregate_result(slot, config);
            auto action = result.best_action;
            if (action.card_id == 0 && slot.decision.has_value()) {
                action = choose_action(
                    PolicyKind::MinimalHybrid,
                    slot.decision->pub_snapshot,
                    slot.decision->hand_snapshot,
                    slot.decision->holds_china,
                    slot.rng
                ).value_or(ActionEncoding{});
            }
            commit_selected_action(slot, action);
        }
        t_apply += std::chrono::duration<double>(Clock::now() - t0a).count();
    }

    const double total = t_advance + t_select + t_nn + t_expand + t_apply;
    fprintf(stderr, "[ISMCTS vs model profile] advance=%.3fs select=%.3fs nn=%.3fs expand=%.3fs apply=%.3fs total=%.3fs\n",
            t_advance, t_select, t_nn, t_expand, t_apply, total);
    fprintf(stderr, "[ISMCTS vs model profile] batches=%d items=%d avg_batch=%.1f\n",
            n_batches, total_batch_items, n_batches > 0 ? double(total_batch_items) / n_batches : 0.0);

    return results;
}

}  // namespace ts

#endif
