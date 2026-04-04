// Determinized information-set MCTS built by sampling hidden opponent hands
// and reusing the native full-state MCTS implementation.

#include "ismcts.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
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

struct DeterminizationSlot {
    GameState root_state;
    GameState sim_state;
    std::unique_ptr<MctsNode> root;
    std::vector<std::pair<MctsNode*, int>> path;
    int sims_completed = 0;
    bool pending_expansion = false;
    bool pending_root_expansion = false;
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
    bool is_root_expansion = false;
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

torch::Tensor tensor_at(const torch::Tensor& tensor, int64_t index) {
    return tensor.index({index});
}

int argmax_index(const torch::Tensor& tensor) {
    return tensor.argmax(/*dim=*/0).item<int>();
}

std::vector<CountryId> accessible_countries_filtered(const PublicState& pub, Side side, CardId card_id, ActionMode mode) {
    auto accessible = legal_countries(card_id, mode, pub, side);
    accessible.erase(
        std::remove_if(accessible.begin(), accessible.end(), [](CountryId cid) { return !has_country_spec(cid); }),
        accessible.end()
    );
    return accessible;
}

ActionEncoding build_action_from_country_logits(
    CardId card_id,
    ActionMode mode,
    const torch::Tensor& country_logits,
    const PublicState& pub,
    Side side,
    const torch::Tensor& strategy_logits,
    const torch::Tensor& country_strategy_logits
) {
    const auto accessible = accessible_countries_filtered(pub, side, card_id, mode);
    if (accessible.empty()) {
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {}};
    }

    auto source_logits = country_logits;
    if (strategy_logits.defined() && country_strategy_logits.defined()) {
        const auto strategy_index = strategy_logits.argmax(/*dim=*/0).item<int64_t>();
        source_logits = country_strategy_logits.index({strategy_index});
    }

    auto masked = torch::full_like(source_logits, -std::numeric_limits<float>::infinity());
    for (const auto cid : accessible) {
        const auto index = static_cast<int64_t>(cid);
        masked.index_put_({index}, tensor_at(source_logits, index));
    }
    const auto probs = torch::softmax(masked, 0);

    if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
        const auto target = static_cast<CountryId>(argmax_index(probs));
        return ActionEncoding{.card_id = card_id, .mode = mode, .targets = {target}};
    }

    const auto ops = effective_ops(card_id, pub, side);
    const auto accessible_indices = torch::tensor(
        std::vector<int64_t>(accessible.begin(), accessible.end()),
        torch::TensorOptions().dtype(torch::kInt64)
    );
    auto accessible_probs = probs.index({accessible_indices});
    auto alloc = accessible_probs * static_cast<double>(ops);
    auto floor_alloc = torch::floor(alloc).to(torch::kInt64);
    auto remainder = ops - static_cast<int>(floor_alloc.sum().item<int64_t>());
    if (remainder > 0) {
        auto fractional = alloc - floor_alloc.to(torch::kFloat32);
        std::vector<std::pair<float, CountryId>> order;
        order.reserve(accessible.size());
        for (size_t i = 0; i < accessible.size(); ++i) {
            const auto index = static_cast<int64_t>(i);
            order.emplace_back(-tensor_at(fractional, index).item<float>(), accessible[i]);
        }
        std::sort(order.begin(), order.end());
        for (int i = 0; i < remainder && i < static_cast<int>(order.size()); ++i) {
            const auto target = order[static_cast<size_t>(i)].second;
            const auto pos = static_cast<long long>(
                std::find(accessible.begin(), accessible.end(), target) - accessible.begin()
            );
            const auto pos64 = static_cast<int64_t>(pos);
            floor_alloc.index_put_({pos64}, tensor_at(floor_alloc, pos64).item<int64_t>() + 1);
        }
    }

    ActionEncoding action{.card_id = card_id, .mode = mode, .targets = {}};
    for (size_t i = 0; i < accessible.size(); ++i) {
        const auto index = static_cast<int64_t>(i);
        const auto count = tensor_at(floor_alloc, index).item<int64_t>();
        for (int64_t j = 0; j < count; ++j) {
            action.targets.push_back(accessible[i]);
        }
    }
    return action;
}

ActionEncoding fallback_resolved_action(const ActionEncoding& action, const PublicState& pub, Side side) {
    const auto accessible = accessible_countries_filtered(pub, side, action.card_id, action.mode);
    if (accessible.empty()) {
        return action;
    }

    if (action.mode == ActionMode::Coup || action.mode == ActionMode::Realign) {
        return ActionEncoding{.card_id = action.card_id, .mode = action.mode, .targets = {accessible.front()}};
    }

    ActionEncoding resolved{.card_id = action.card_id, .mode = action.mode, .targets = {}};
    const auto ops = effective_ops(action.card_id, pub, side);
    resolved.targets.assign(static_cast<size_t>(ops), accessible.front());
    return resolved;
}

ActionEncoding resolve_edge_action(
    const ActionEncoding& action,
    const PublicState& pub,
    Side side,
    const torch::Tensor& country_logits,
    const torch::Tensor& strategy_logits,
    const torch::Tensor& country_strategy_logits
) {
    if (action.mode != ActionMode::Influence) {
        return action;
    }
    if (country_logits.defined()) {
        auto resolved = build_action_from_country_logits(
            action.card_id,
            action.mode,
            country_logits,
            pub,
            side,
            strategy_logits,
            country_strategy_logits
        );
        if (!resolved.targets.empty()) {
            return resolved;
        }
    }
    return fallback_resolved_action(action, pub, side);
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

double evaluate_leaf_value(
    const GameState& state,
    const torch::Tensor& value_tensor,
    int64_t batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto value = value_tensor.index({batch_index, 0}).item<double>();
    value = calibrate_value(value, config);
    if (!config.use_rollout_backup) {
        return value;
    }
    const auto rollout = rollout_value(state, config, rng);
    return static_cast<double>(config.value_weight) * value +
        static_cast<double>(1.0f - config.value_weight) * rollout;
}

std::vector<CardDraft> collect_card_drafts(const GameState& state) {
    const auto side = state.pub.phasing;
    const auto holds_china = holds_china_for(state, side);
    std::vector<CardDraft> cards;

    for (const auto card_id : legal_cards(state.hands[to_index(side)], state.pub, side, holds_china)) {
        if (is_card_blocked_by_defcon(state.pub, side, card_id)) {
            continue;
        }

        CardDraft card{.card_id = card_id, .modes = {}};
        for (const auto mode : legal_modes(card_id, state.pub, side)) {
            if (mode == ActionMode::Coup && state.pub.defcon <= 2) {
                continue;
            }
            if (mode == ActionMode::Event && state.pub.defcon <= 2 && is_defcon_lowering_card(card_id)) {
                continue;
            }

            ModeDraft mode_draft{.mode = mode, .edges = {}};
            if (mode == ActionMode::Event || mode == ActionMode::Space || mode == ActionMode::Influence) {
                mode_draft.edges.push_back(ActionEncoding{
                    .card_id = card_id,
                    .mode = mode,
                    .targets = {},
                });
            } else {
                auto countries = legal_countries(card_id, mode, state.pub, side);
                countries.erase(
                    std::remove_if(countries.begin(), countries.end(), [](CountryId cid) { return !has_country_spec(cid); }),
                    countries.end()
                );
                for (const auto country : countries) {
                    mode_draft.edges.push_back(ActionEncoding{
                        .card_id = card_id,
                        .mode = mode,
                        .targets = {country},
                    });
                }
            }

            if (!mode_draft.edges.empty()) {
                card.modes.push_back(std::move(mode_draft));
            }
        }

        if (!card.modes.empty()) {
            cards.push_back(std::move(card));
        }
    }

    return cards;
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

    const auto drafts = collect_card_drafts(state);
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

ExpansionResult expand_from_outputs(
    const GameState& state,
    const nn::BatchOutputs& outputs,
    int64_t batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto node = std::make_unique<MctsNode>();
    node->side_to_move = state.pub.phasing;

    const auto drafts = collect_card_drafts(state);
    const auto card_logits = outputs.card_logits.index({batch_index});
    const auto mode_logits = outputs.mode_logits.index({batch_index});
    const auto country_logits = outputs.country_logits.defined() ? outputs.country_logits.index({batch_index}) : torch::Tensor{};
    const auto strategy_logits = outputs.strategy_logits.defined() ? outputs.strategy_logits.index({batch_index}) : torch::Tensor{};
    const auto country_strategy_logits = outputs.country_strategy_logits.defined()
        ? outputs.country_strategy_logits.index({batch_index})
        : torch::Tensor{};

    auto masked_card = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto& card : drafts) {
        masked_card.index_put_({static_cast<int64_t>(card.card_id - 1)}, tensor_at(card_logits, card.card_id - 1));
    }
    const auto card_probs = torch::softmax(masked_card, 0);

    double total_prior = 0.0;
    for (const auto& card : drafts) {
        auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto& mode : card.modes) {
            masked_mode.index_put_({static_cast<int64_t>(mode.mode)}, tensor_at(mode_logits, static_cast<int>(mode.mode)));
        }
        const auto mode_probs = torch::softmax(masked_mode, 0);
        const auto card_prob = tensor_at(card_probs, card.card_id - 1).item<double>();

        for (const auto& mode : card.modes) {
            const auto mode_prob = tensor_at(mode_probs, static_cast<int>(mode.mode)).item<double>();
            if ((mode.mode == ActionMode::Coup || mode.mode == ActionMode::Realign) && country_logits.defined()) {
                auto masked_country = torch::full_like(country_logits, -std::numeric_limits<float>::infinity());
                for (const auto& edge : mode.edges) {
                    const auto country = edge.targets.front();
                    masked_country.index_put_({static_cast<int64_t>(country)}, tensor_at(country_logits, country));
                }
                const auto country_probs = torch::softmax(masked_country, 0);
                for (const auto& edge : mode.edges) {
                    const auto country = edge.targets.front();
                    const auto prior = card_prob * mode_prob * tensor_at(country_probs, country).item<double>();
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
                node->applied_actions.push_back(resolve_edge_action(
                    edge,
                    state.pub,
                    state.pub.phasing,
                    country_logits,
                    strategy_logits,
                    country_strategy_logits
                ));
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
                .leaf_value = evaluate_leaf_value(state, outputs.value, batch_index, config, rng),
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
        .leaf_value = evaluate_leaf_value(state, outputs.value, batch_index, config, rng),
    };
}

void backpropagate(DeterminizationSlot& det, double leaf_value) {
    for (auto it = det.path.rbegin(); it != det.path.rend(); ++it) {
        auto* ancestor = it->first;
        auto& edge = ancestor->edges[static_cast<size_t>(it->second)];
        edge.virtual_loss = std::max(0, edge.virtual_loss - kVirtualLossWeight);
        edge.visit_count += 1;
        edge.total_value += leaf_value;
        ancestor->total_visits += 1;
    }
    det.path.clear();
}

SelectionResult select_to_leaf(DeterminizationSlot& det, const MctsConfig& config) {
    det.path.clear();
    det.pending_expansion = false;
    det.pending_root_expansion = false;
    det.sim_state = clone_game_state(det.root_state);

    MctsNode* node = det.root.get();
    while (node != nullptr && !node->is_terminal && !node->edges.empty()) {
        const auto edge_index = node->select_edge(config.c_puct);
        if (edge_index < 0) {
            break;
        }

        auto& edge = node->edges[static_cast<size_t>(edge_index)];
        edge.virtual_loss += kVirtualLossWeight;
        det.path.emplace_back(node, edge_index);
        apply_tree_action(det.sim_state, node->applied_actions[static_cast<size_t>(edge_index)], det.rng);
        if (node->children[static_cast<size_t>(edge_index)] == nullptr) {
            if (auto immediate = expand_without_model(det.sim_state, det.rng); immediate.has_value()) {
                node->children[static_cast<size_t>(edge_index)] = std::move(immediate->node);
                return SelectionResult{.needs_batch = false, .leaf_value = immediate->leaf_value};
            }
            det.pending_expansion = true;
            return SelectionResult{.needs_batch = true};
        }
        node = node->children[static_cast<size_t>(edge_index)].get();
    }

    if (node != nullptr && node->is_terminal) {
        return SelectionResult{.needs_batch = false, .leaf_value = node->terminal_value};
    }
    return SelectionResult{.needs_batch = false, .leaf_value = 0.0};
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

std::string end_reason(const PublicState& pub, std::optional<Side> winner) {
    if (pub.defcon <= 1) {
        return "defcon1";
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

void advance_until_search_or_done(IsmctsGameSlot& slot, Side learned_side) {
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
                    resolve_heuristic_decision(slot);
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
                    resolve_heuristic_decision(slot);
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
                    resolve_heuristic_decision(slot);
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
        det.sim_state = det.root_state;
        det.rng = std::move(local_rng);
        slot.dets.push_back(std::move(det));
    }
    slot.search_active = true;
}

bool determinization_complete(const DeterminizationSlot& det, int sims_target) {
    return det.root != nullptr && det.sims_completed >= sims_target;
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
    DeterminizationSlot& det,
    const GameState& state,
    bool is_root_expansion
) {
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
        .is_root_expansion = is_root_expansion,
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
    shuffle_with_numpy_rng(hidden_pool, rng);

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

    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(pool_size * config.n_determinizations, device);
    std::vector<BatchEntry> batch_entries;
    batch_entries.reserve(static_cast<size_t>(pool_size * config.n_determinizations));

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
                advance_until_search_or_done(slot, learned_side);
                if (slot.game_done || !slot.decision.has_value()) {
                    continue;
                }
                start_search(slot, config);
            }

            for (auto& det : slot.dets) {
                if (determinization_complete(det, config.mcts_config.n_simulations)) {
                    continue;
                }

                if (det.root == nullptr) {
                    if (auto immediate = expand_without_model(det.root_state, det.rng); immediate.has_value()) {
                        det.root = std::move(immediate->node);
                        apply_root_dirichlet_noise(*det.root, config.mcts_config, det.rng);
                    } else {
                        det.pending_expansion = true;
                        det.pending_root_expansion = true;
                        queue_batch_item(batch_inputs, batch_entries, slot, det, det.root_state, true);
                    }
                    continue;
                }

                if (det.sims_completed >= config.mcts_config.n_simulations) {
                    continue;
                }

                const auto selection = select_to_leaf(det, config.mcts_config);
                if (selection.needs_batch) {
                    queue_batch_item(batch_inputs, batch_entries, slot, det, det.sim_state, false);
                    continue;
                }

                backpropagate(det, selection.leaf_value);
                det.sims_completed += 1;
            }
        }

        if (!batch_entries.empty()) {
            const auto outputs = nn::forward_model_batched(model, batch_inputs);
            for (size_t i = 0; i < batch_entries.size(); ++i) {
                auto& entry = batch_entries[i];
                const auto batch_index = static_cast<int64_t>(i);
                if (entry.is_root_expansion) {
                    auto expansion = expand_from_outputs(
                        entry.det->root_state,
                        outputs,
                        batch_index,
                        config.mcts_config,
                        entry.det->rng
                    );
                    entry.det->root = std::move(expansion.node);
                    apply_root_dirichlet_noise(*entry.det->root, config.mcts_config, entry.det->rng);
                    entry.det->pending_expansion = false;
                    entry.det->pending_root_expansion = false;
                    continue;
                }

                auto expansion = expand_from_outputs(
                    entry.det->sim_state,
                    outputs,
                    batch_index,
                    config.mcts_config,
                    entry.det->rng
                );
                auto& [parent, edge_index] = entry.det->path.back();
                parent->children[static_cast<size_t>(edge_index)] = std::move(expansion.node);
                entry.det->pending_expansion = false;
                backpropagate(*entry.det, expansion.leaf_value);
                entry.det->sims_completed += 1;
            }
        }

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
    }

    return results;
}

}  // namespace ts

#endif
