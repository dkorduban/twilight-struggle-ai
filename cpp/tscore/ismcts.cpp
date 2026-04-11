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

#include "game_data.hpp"
#include "game_loop.hpp"
#include "human_openings.hpp"
#include "nn_features.hpp"
#include "policies.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts {
namespace {

constexpr int kMidWarTurn = 4;
constexpr int kLateWarTurn = 8;
constexpr int kMaxTurns = 10;
constexpr int kSpaceShuttleArs = 8;
constexpr int kVirtualLossWeight = 1;
constexpr int kMaxCardLogits = 112;
constexpr int kMaxModeLogits = 8;
constexpr int kMaxCountryLogits = 86;
constexpr int kMaxStrategies = 8;
constexpr std::array<int, 13> kDefconLoweringCards = {
    4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105,
};

struct ModeDraft {
    ActionMode mode = ActionMode::Influence;
    std::vector<ActionEncoding> edges;
};

struct CardDraft {
    CardId card_id = 0;
    std::vector<ModeDraft> modes;
};

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
    GameState sim_state;
    bool is_root_expansion = false;
};

struct DeterminizationSlot {
    GameState root_state;
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

int count_hand_excluding_china(const CardSet& hand) {
    auto count = static_cast<int>(hand.count());
    if (hand.test(kChinaCardId)) {
        --count;
    }
    return count;
}

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

[[nodiscard]] bool is_defcon_lowering_card(CardId card_id) {
    return std::find(kDefconLoweringCards.begin(), kDefconLoweringCards.end(), static_cast<int>(card_id)) !=
        kDefconLoweringCards.end();
}

[[nodiscard]] bool is_card_blocked_by_defcon(const PublicState& pub, Side side, CardId card_id) {
    if (!is_defcon_lowering_card(card_id)) {
        return false;
    }

    const auto& card_info = card_spec(card_id);
    const bool is_opponent_card = (card_info.side != side && card_info.side != Side::Neutral);
    const bool is_neutral_card = (card_info.side == Side::Neutral);
    if (is_opponent_card) {
        if (pub.defcon <= 2) {
            return true;
        }
        if (pub.defcon == 3 && pub.ar == 0) {
            return true;
        }
    }
    if (is_neutral_card && pub.ar == 0 && pub.defcon <= 3) {
        return true;
    }
    return false;
}

[[nodiscard]] double winner_value(std::optional<Side> winner) {
    if (winner == Side::USSR) {
        return 1.0;
    }
    if (winner == Side::US) {
        return -1.0;
    }
    return 0.0;
}

[[nodiscard]] double calibrate_value(double raw_value, const MctsConfig& config) {
    if (config.calib_a == 1.0f && config.calib_b == 0.0f) {
        return raw_value;
    }
    const auto logit = static_cast<double>(config.calib_a) * raw_value + static_cast<double>(config.calib_b);
    const auto probability = 1.0 / (1.0 + std::exp(-logit));
    return 2.0 * probability - 1.0;
}

[[nodiscard]] bool holds_china_for(const GameState& state, Side side) {
    return side == Side::USSR ? state.ussr_holds_china : state.us_holds_china;
}

void sync_china_flags(GameState& state) {
    state.ussr_holds_china = state.pub.china_held_by == Side::USSR;
    state.us_holds_china = state.pub.china_held_by == Side::US;
}


/// Compute softmax in-place over buf[0..n), writing probabilities back into buf.
inline void softmax_inplace(float* buf, int n) {
    float max_val = -std::numeric_limits<float>::infinity();
    for (int i = 0; i < n; ++i) {
        if (buf[i] > max_val) max_val = buf[i];
    }
    float sum = 0.0f;
    for (int i = 0; i < n; ++i) {
        buf[i] = std::exp(buf[i] - max_val);
        sum += buf[i];
    }
    if (sum > 0.0f) {
        const float inv_sum = 1.0f / sum;
        for (int i = 0; i < n; ++i) {
            buf[i] *= inv_sum;
        }
    }
}

void apply_tree_action(GameState& state, const ActionEncoding& action, Pcg64Rng& rng) {
    const auto side = state.pub.phasing;
    auto& hand = state.hands[to_index(side)];
    if (hand.test(action.card_id)) {
        hand.reset(action.card_id);
    }

    auto [new_pub, over, winner] = apply_action_live(state, action, side, rng);
    (void)new_pub;
    sync_china_flags(state);
    state.game_over = over;
    state.winner = winner;
    state.current_side = over ? side : other_side(side);
    if (!over) {
        state.pub.phasing = other_side(side);
    }
}

double rollout_value(const GameState& state, const MctsConfig& config, Pcg64Rng& rng) {
    (void)config.rollout_depth_limit;
    const PolicyFn heuristic = [](const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& local_rng) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, local_rng);
    };
    const auto result = play_game_from_mid_state_fn(state, heuristic, heuristic, rng.next_u32());
    return winner_value(result.winner);
}


double evaluate_leaf_value_raw(
    const GameState& state,
    const float* value_ptr,
    int value_stride,
    int batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto value = static_cast<double>(value_ptr[batch_index * value_stride]);
    value = calibrate_value(value, config);
    if (!config.use_rollout_backup) {
        return value;
    }
    const auto rollout = rollout_value(state, config, rng);
    return static_cast<double>(config.value_weight) * value +
        static_cast<double>(1.0f - config.value_weight) * rollout;
}

// Precomputed accessible countries for all three action modes — avoids repeated BFS.
struct AccessibleCache {
    std::vector<CountryId> influence;
    std::vector<CountryId> coup;
    std::vector<CountryId> realign;
    bool can_space = false;
    int space_ops_min = 2;

    static AccessibleCache build(Side side, const PublicState& pub) {
        AccessibleCache cache;

        // Compute BFS-based accessibility ONCE
        auto base_inf = accessible_countries(side, pub, ActionMode::Influence);
        auto base_coup = accessible_countries(side, pub, ActionMode::Coup);

        // Filter influence for Chernobyl
        if (side == Side::USSR && pub.chernobyl_blocked_region.has_value()) {
            const auto blocked = *pub.chernobyl_blocked_region;
            base_inf.erase(
                std::remove_if(base_inf.begin(), base_inf.end(),
                    [blocked](CountryId cid) { return country_spec(cid).region == blocked; }),
                base_inf.end()
            );
        }
        cache.influence = std::move(base_inf);

        // Filter coup/realign for DEFCON, NATO, Japan pact
        auto filter_military = [&](std::vector<CountryId>& countries) {
            countries.erase(
                std::remove_if(countries.begin(), countries.end(),
                    [&](CountryId cid) {
                        if (cid == kUsaAnchorId || cid == kUssrAnchorId) return true;
                        constexpr std::array<int, 7> kDefconRegionThreshold = {4, 3, 2, 1, 1, 1, 3};
                        const auto threshold = kDefconRegionThreshold[static_cast<size_t>(country_spec(cid).region)];
                        if (pub.defcon <= threshold) return true;
                        if (side == Side::USSR) {
                            if (pub.nato_active) {
                                constexpr std::array<CountryId, 12> kNatoWe = {1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18};
                                bool in_nato = std::find(kNatoWe.begin(), kNatoWe.end(), cid) != kNatoWe.end();
                                if (in_nato) {
                                    bool exempted = (cid == 7 && pub.de_gaulle_active) || (cid == 18 && pub.willy_brandt_active);
                                    if (!exempted && controls_country(Side::US, cid, pub)) return true;
                                }
                            }
                            if (pub.us_japan_pact_active && cid == 22) return true;
                        }
                        return false;
                    }),
                countries.end()
            );
        };
        filter_military(base_coup);
        cache.coup = std::move(base_coup);
        // Realign uses same base accessibility as coup
        cache.realign = cache.coup;  // copy — realign has same restrictions

        // Space eligibility
        const auto level = pub.space[to_index(side)];
        const auto opp_level = pub.space[to_index(other_side(side))];
        const auto max_space = (level >= 2 && opp_level < 2) ? 2 : 1;
        cache.can_space = (level < 8 && pub.space_attempts[to_index(side)] < max_space);
        constexpr std::array<int, 8> kSpaceOpsMin = {2, 2, 2, 2, 3, 3, 3, 4};
        cache.space_ops_min = kSpaceOpsMin[static_cast<size_t>(std::min(level, 7))];

        return cache;
    }
};

bool nato_prerequisite_met_inline(const PublicState& pub) {
    return pub.warsaw_pact_played || pub.marshall_plan_played || pub.truman_doctrine_played;
}

struct DraftsResult {
    std::vector<CardDraft> drafts;
    AccessibleCache cache;
};

DraftsResult collect_card_drafts(const GameState& state) {
    const auto side = state.pub.phasing;
    const auto holds_china = holds_china_for(state, side);
    const auto& pub = state.pub;
    auto cache = AccessibleCache::build(side, pub);

    std::vector<CardDraft> cards;
    cards.reserve(10);

    for (const auto card_id : legal_cards(state.hands[to_index(side)], pub, side, holds_china)) {
        if (is_card_blocked_by_defcon(pub, side, card_id)) {
            continue;
        }

        const auto& spec = card_spec(card_id);
        CardDraft card{.card_id = card_id, .modes = {}};

        // Inline legal_modes logic using cached accessibility
        auto try_add_mode = [&](ActionMode mode, const std::vector<CountryId>& countries) {
            if (countries.empty()) return;
            if (mode == ActionMode::Coup && pub.defcon <= 2) return;
            if (pub.cuban_missile_crisis_active && mode == ActionMode::Coup) return;

            ModeDraft mode_draft{.mode = mode, .edges = {}};
            mode_draft.edges.reserve(countries.size());
            for (const auto country : countries) {
                if (!has_country_spec(country)) continue;
                mode_draft.edges.push_back(ActionEncoding{
                    .card_id = card_id,
                    .mode = mode,
                    .targets = {country},
                });
            }
            if (!mode_draft.edges.empty()) {
                card.modes.push_back(std::move(mode_draft));
            }
        };

        if (spec.ops > 0) {
            // Influence — no per-country targets in tree, just one edge
            if (!cache.influence.empty()) {
                card.modes.push_back(ModeDraft{
                    .mode = ActionMode::Influence,
                    .edges = {ActionEncoding{.card_id = card_id, .mode = ActionMode::Influence, .targets = {}}},
                });
            }

            try_add_mode(ActionMode::Coup, cache.coup);
            try_add_mode(ActionMode::Realign, cache.realign);

            // Space
            if (cache.can_space && spec.ops >= cache.space_ops_min) {
                bool blocked = (pub.bear_trap_active && side == Side::USSR && !spec.is_scoring) ||
                               (pub.quagmire_active && side == Side::US && !spec.is_scoring);
                if (!blocked) {
                    card.modes.push_back(ModeDraft{
                        .mode = ActionMode::Space,
                        .edges = {ActionEncoding{.card_id = card_id, .mode = ActionMode::Space, .targets = {}}},
                    });
                }
            }
        }

        // Event
        bool event_ok = true;
        if (card_id == 21 && !nato_prerequisite_met_inline(pub)) event_ok = false;
        if (pub.defcon <= 2 && is_defcon_lowering_card(card_id)) event_ok = false;
        if (pub.bear_trap_active && side == Side::USSR && !spec.is_scoring) event_ok = false;
        if (pub.quagmire_active && side == Side::US && !spec.is_scoring) event_ok = false;
        if (card_id == 103 && pub.defcon != 2) event_ok = false;
        if (event_ok) {
            card.modes.push_back(ModeDraft{
                .mode = ActionMode::Event,
                .edges = {ActionEncoding{.card_id = card_id, .mode = ActionMode::Event, .targets = {}}},
            });
        }

        if (!card.modes.empty()) {
            cards.push_back(std::move(card));
        }
    }

    return DraftsResult{.drafts = std::move(cards), .cache = std::move(cache)};
}

std::optional<ExpansionResult> expand_without_model(const GameState& state, Pcg64Rng& rng) {
    auto node = std::make_unique<MctsNode>();
    node->side_to_move = state.pub.phasing;

    if (state.game_over) {
        node->is_terminal = true;
        const auto terminal_value = winner_value(state.winner);
        node->terminal_value = terminal_value;
        return ExpansionResult{.node = std::move(node), .leaf_value = terminal_value};
    }

    const auto [drafts, _cache] = collect_card_drafts(state);
    if (!drafts.empty()) {
        return std::nullopt;
    }

    if (auto fallback = choose_action(
            PolicyKind::MinimalHybrid,
            state.pub,
            state.hands[to_index(state.pub.phasing)],
            holds_china_for(state, state.pub.phasing),
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
    const GameState& state,
    const RawBatchOutputs& raw,
    int batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto node = std::make_unique<MctsNode>();
    node->side_to_move = state.pub.phasing;
    node->edges.reserve(64);
    node->children.reserve(64);
    node->applied_actions.reserve(64);

    auto [drafts, cache] = collect_card_drafts(state);
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
        const double card_prob = (cidx >= 0 && cidx < n_card) ? static_cast<double>(masked_card[cidx]) : 0.0;

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
                    const auto ops = effective_ops(edge.card_id, state.pub, state.pub.phasing);
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
                state.pub,
                state.hands[to_index(state.pub.phasing)],
                holds_china_for(state, state.pub.phasing),
                rng
            );
            fallback.has_value()) {
            node->edges.push_back(MctsEdge{.action = *fallback, .prior = 1.0f});
            node->children.emplace_back(nullptr);
            node->applied_actions.push_back(*fallback);
            return ExpansionResult{
                .node = std::move(node),
                .leaf_value = evaluate_leaf_value_raw(state, raw.value, raw.value_stride, batch_index, config, rng),
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
        .leaf_value = evaluate_leaf_value_raw(state, raw.value, raw.value_stride, batch_index, config, rng),
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
    pend.sim_state = clone_game_state(det.root_state);

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
    if (card_id == 103) {
        return "wargames";
    }
    if (winner.has_value()) {
        return "europe_control";
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
    if (slot.game_state.pub.glasnost_extra_ar) {
        slot.game_state.pub.glasnost_extra_ar = false;
        slot.stage = IsmctsGameStage::ExtraActionRoundUSSR;
        return;
    }
    slot.stage = IsmctsGameStage::Cleanup;
}

void move_to_followup_stage_after_extra(IsmctsGameSlot& slot, Side side) {
    if (side == Side::US && slot.game_state.pub.glasnost_extra_ar) {
        slot.game_state.pub.glasnost_extra_ar = false;
        slot.stage = IsmctsGameStage::ExtraActionRoundUSSR;
        return;
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

    // Mask illegal cards (DEFCON-lowering safety included).
    auto masked_card = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto card_id : playable) {
        if (is_card_blocked_by_defcon(pub, side, card_id)) {
            continue;
        }
        const auto idx = static_cast<int64_t>(card_id - 1);
        masked_card.index_put_({idx}, card_logits.index({idx}));
    }

    // If all playable cards were masked, fall back.
    const bool all_masked = (masked_card.max().item<float>() == -std::numeric_limits<float>::infinity());
    if (all_masked) {
        return heuristic_fallback();
    }

    const auto card_id = static_cast<CardId>(masked_card.argmax().item<int64_t>() + 1);

    // Mode selection.
    auto modes = legal_modes(card_id, pub, side);
    if (modes.empty()) {
        return heuristic_fallback();
    }

    auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
    for (const auto m : modes) {
        const auto idx = static_cast<int64_t>(static_cast<int>(m));
        masked_mode.index_put_({idx}, mode_logits.index({idx}));
    }
    // DEFCON safety: forbid coup/event for DEFCON-lowering cards at DEFCON<=2.
    if (pub.defcon <= 2) {
        for (auto mode_val : {ActionMode::Coup, ActionMode::Event}) {
            if (is_defcon_lowering_card(card_id)) {
                const auto idx = static_cast<int64_t>(static_cast<int>(mode_val));
                masked_mode.index_put_({idx}, -std::numeric_limits<float>::infinity());
            }
        }
    }
    // Re-check after filtering.
    const bool mode_all_masked = (masked_mode.max().item<float>() == -std::numeric_limits<float>::infinity());
    if (mode_all_masked) {
        return heuristic_fallback();
    }
    const auto mode = static_cast<ActionMode>(masked_mode.argmax().item<int64_t>());

    // Country / target selection.
    ActionEncoding action{.card_id = card_id, .mode = mode, .targets = {}};

    if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
        auto accessible = accessible_countries(side, pub, mode);
        if (accessible.empty()) {
            return heuristic_fallback();
        }
        // Filter forbidden targets (DEFCON, NATO, etc.) using the cache logic.
        const auto& cache = AccessibleCache::build(side, pub);
        const auto& valid = (mode == ActionMode::Coup) ? cache.coup : cache.realign;
        if (valid.empty()) {
            return heuristic_fallback();
        }
        // Pick highest logit among accessible countries.
        const auto country_logits = outputs.country_logits.defined()
            ? outputs.country_logits.index({bi})
            : torch::zeros(kMaxCountryLogits);
        CountryId best_country = valid[0];
        float best_val = -std::numeric_limits<float>::infinity();
        for (const auto cid : valid) {
            const float v = country_logits.index({static_cast<int64_t>(cid)}).item<float>();
            if (v > best_val) {
                best_val = v;
                best_country = cid;
            }
        }
        action.targets.push_back(best_country);
    } else if (mode == ActionMode::Influence || mode == ActionMode::Space) {
        const auto& cache = AccessibleCache::build(side, pub);
        if (mode == ActionMode::Space) {
            // Space: pick best country (though usually irrelevant for space).
            if (!cache.influence.empty()) {
                action.targets.push_back(cache.influence[0]);
            }
        } else {
            const auto ops = effective_ops(card_id, pub, side);
            const auto& accessible = cache.influence;
            if (accessible.empty()) {
                return heuristic_fallback();
            }
            const auto country_logits = outputs.country_logits.defined()
                ? outputs.country_logits.index({bi})
                : torch::zeros(kMaxCountryLogits);
            // Allocate ops proportional to logits (deterministic, like greedy_action_from_outputs).
            std::vector<float> vals;
            vals.reserve(accessible.size());
            float max_v = -std::numeric_limits<float>::infinity();
            for (const auto cid : accessible) {
                const float v = country_logits.index({static_cast<int64_t>(cid)}).item<float>();
                vals.push_back(v);
                if (v > max_v) max_v = v;
            }
            // Softmax.
            float sum_exp = 0.0f;
            for (auto& v : vals) {
                v = std::exp(v - max_v);
                sum_exp += v;
            }
            for (auto& v : vals) {
                v /= sum_exp;
            }
            // Floor allocation.
            std::vector<int> alloc(accessible.size(), 0);
            float rem = static_cast<float>(ops);
            for (size_t i = 0; i < accessible.size(); ++i) {
                alloc[i] = static_cast<int>(std::floor(vals[i] * static_cast<float>(ops)));
                rem -= static_cast<float>(alloc[i]);
            }
            // Distribute remaining ops by largest fractional.
            int rem_int = static_cast<int>(std::round(rem));
            if (rem_int > 0) {
                std::vector<std::pair<float, size_t>> fractional;
                for (size_t i = 0; i < accessible.size(); ++i) {
                    const float frac = vals[i] * static_cast<float>(ops) - static_cast<float>(alloc[i]);
                    fractional.emplace_back(-frac, i);  // negate for ascending sort = descending frac
                }
                std::sort(fractional.begin(), fractional.end());
                for (int k = 0; k < rem_int && k < static_cast<int>(fractional.size()); ++k) {
                    alloc[fractional[static_cast<size_t>(k)].second] += 1;
                }
            }
            for (size_t i = 0; i < accessible.size(); ++i) {
                for (int k = 0; k < alloc[i]; ++k) {
                    action.targets.push_back(accessible[i]);
                }
            }
        }
    }
    // Event mode: no targets needed.

    if (action.targets.empty() && mode != ActionMode::Event && mode != ActionMode::Space) {
        return heuristic_fallback();
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
    while (slot.active && !slot.game_done && !slot.decision.has_value()) {
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
    const auto opp_hand_size = count_hand_excluding_china(slot.game_state.hands[to_index(other_side(acting_side))]);

    slot.dets.clear();
    slot.dets.reserve(static_cast<size_t>(config.n_determinizations));
    for (int i = 0; i < config.n_determinizations; ++i) {
        Pcg64Rng local_rng(slot.rng.next_u64());
        auto determinized = sample_determinization(slot.game_state, acting_side, opp_hand_size, local_rng);
        DeterminizationSlot det;
        det.root_state = std::move(determinized);
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
        state.pub,
        state.hands[to_index(state.pub.phasing)],
        holds_china_for(state, state.pub.phasing),
        state.pub.phasing
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
    int opp_hand_size,
    Pcg64Rng& rng
) {
    if (!is_player_side(acting_side)) {
        throw std::invalid_argument("acting_side must be USSR or US");
    }
    if (opp_hand_size < 0) {
        throw std::invalid_argument("opp_hand_size must be non-negative");
    }

    auto determinized = clone_game_state(gs);
    const auto opponent = other_side(acting_side);
    auto& opponent_hand = determinized.hands[to_index(opponent)];
    const auto known_opp_count = count_hand_excluding_china(opponent_hand);
    if (known_opp_count > opp_hand_size) {
        throw std::invalid_argument("known opponent hand exceeds opp_hand_size");
    }

    auto hidden_pool = determinized.deck;
    hidden_pool.erase(
        std::remove(hidden_pool.begin(), hidden_pool.end(), kChinaCardId),
        hidden_pool.end()
    );
    shuffle_with_numpy_rng(std::span<CardId>(hidden_pool.begin(), hidden_pool.end()), rng);

    const auto hidden_needed = opp_hand_size - known_opp_count;
    if (hidden_needed > static_cast<int>(hidden_pool.size())) {
        throw std::invalid_argument("not enough hidden cards to fill opponent hand");
    }

    for (int i = 0; i < hidden_needed; ++i) {
        opponent_hand.set(hidden_pool[static_cast<size_t>(i)]);
    }
    determinized.deck.assign(hidden_pool.begin() + hidden_needed, hidden_pool.end());
    return determinized;
}

IsmctsResult ismcts_search(
    const GameState& partial_state,
    Side acting_side,
    int opp_hand_size,
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
        auto determinized = sample_determinization(partial_state, acting_side, opp_hand_size, local_rng);
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
            const auto opp_idx = to_index(other_side(acting));
            auto opp_hand_size = static_cast<int>(gs.hands[opp_idx].count());
            if (gs.hands[opp_idx].test(kChinaCardId)) {
                --opp_hand_size;
            }
            auto result = ismcts_search(gs, acting, opp_hand_size, model, config, local_rng);
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
                        pend.sim_state = clone_game_state(det.root_state);
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
                        pend.sim_state = clone_game_state(det.root_state);
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
