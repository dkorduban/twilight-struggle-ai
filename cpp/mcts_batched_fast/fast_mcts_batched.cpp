// Single-thread benchmark-oriented replica of the batched full-information MCTS loop.

#include "fast_mcts_batched.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <condition_variable>
#include <cstdint>
#include <cstring>
#include <limits>
#include <memory>
#include <mutex>
#include <optional>
#include <stdexcept>
#include <thread>
#include <utility>
#include <vector>

#include <torch/torch.h>

#include "game_data.hpp"
#include "game_loop.hpp"
#include "human_openings.hpp"
#include "mcts_batched.hpp"
#include "nn_features.hpp"
#include "policies.hpp"
#include "scoring.hpp"
#include "step.hpp"

namespace ts::fastmcts {
namespace {

constexpr int kMidWarTurn = 4;
constexpr int kLateWarTurn = 8;
constexpr int kMaxTurns = 10;
constexpr int kSpaceShuttleArs = 8;
constexpr int kMaxCardLogits = 112;
constexpr int kMaxModeLogits = 8;
constexpr int kMaxCountryLogits = 86;
constexpr int kMaxStrategies = 8;
constexpr bool kValidateCompactTree = false;
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
    std::unique_ptr<struct FastNode> node;
    double leaf_value = 0.0;
};

struct SelectionResult {
    bool needs_batch = false;
    double leaf_value = 0.0;
};

struct FastPendingDecision {
    int turn = 0;
    int ar = 0;
    int move_number = 0;
    Side side = Side::USSR;
    bool holds_china = false;
    bool is_headline = false;
};

struct FastPendingHeadlineChoice {
    Side side = Side::USSR;
    bool holds_china = false;
    ActionEncoding action;
};

struct FastPendingExpansion {
    std::vector<std::pair<struct FastNode*, int>> path;
    GameState sim_state;
    bool is_root_expansion = false;
};

struct FastGameSlot {
    GameState root_state;
    std::unique_ptr<struct FastNode> root;
    std::vector<FastPendingExpansion> pending;
    int sims_completed = 0;
    int sims_target = 0;
    bool move_done = false;
    bool game_done = false;
    bool emitted = false;
    bool active = false;
    Pcg64Rng rng;

    GameResult result;

    BatchedGameStage stage = BatchedGameStage::TurnSetup;
    int turn = 1;
    int total_ars = 0;
    int current_ar = 0;
    int decisions_started = 0;
    Side current_side = Side::USSR;
    std::array<std::optional<FastPendingHeadlineChoice>, 2> pending_headlines = {};
    std::vector<FastPendingHeadlineChoice> headline_order;
    size_t headline_order_index = 0;
    std::optional<FastPendingDecision> decision;
};

struct BatchEntry {
    FastGameSlot* slot = nullptr;
    size_t pending_index = 0;
    int batch_index = 0;
};

struct FastEdge {
    CardId card_id = 0;
    ActionMode mode = ActionMode::Influence;
    CountryId country = 0;
    int target_offset = 0;
    int target_count = 0;
    float prior = 0.0f;
    int visit_count = 0;
    int virtual_loss = 0;
    double total_value = 0.0;
};

struct FastNode {
    std::vector<FastEdge> edges;
    std::vector<std::unique_ptr<FastNode>> children;
    std::vector<CountryId> resolved_targets;
    int total_visits = 0;
    bool is_terminal = false;
    double terminal_value = 0.0;
    Side side_to_move = Side::USSR;
    std::unique_ptr<GameState> cached_state;
};

[[noreturn]] void throw_compact_node_error(
    const char* context,
    const FastNode& node,
    size_t edge_index,
    const FastEdge& edge
) {
    throw std::runtime_error(
        std::string(context) +
        " edge_index=" + std::to_string(edge_index) +
        " mode=" + std::to_string(static_cast<int>(edge.mode)) +
        " card=" + std::to_string(static_cast<int>(edge.card_id)) +
        " country=" + std::to_string(static_cast<int>(edge.country)) +
        " target_offset=" + std::to_string(edge.target_offset) +
        " target_count=" + std::to_string(edge.target_count) +
        " edge_count=" + std::to_string(node.edges.size()) +
        " child_count=" + std::to_string(node.children.size()) +
        " resolved_targets=" + std::to_string(node.resolved_targets.size())
    );
}

[[maybe_unused]] void validate_compact_node(const FastNode& node, const char* context) {
    if (node.edges.size() != node.children.size()) {
        throw std::runtime_error(
            std::string(context) +
            " mismatched edge/child counts edge_count=" + std::to_string(node.edges.size()) +
            " child_count=" + std::to_string(node.children.size())
        );
    }

    for (size_t edge_index = 0; edge_index < node.edges.size(); ++edge_index) {
        const auto& edge = node.edges[edge_index];
        if (edge.mode == ActionMode::Influence) {
            if (edge.country != 0) {
                throw_compact_node_error(context, node, edge_index, edge);
            }
            if (edge.target_count < 0 || edge.target_offset < 0) {
                throw_compact_node_error(context, node, edge_index, edge);
            }
            if (static_cast<size_t>(edge.target_offset + edge.target_count) > node.resolved_targets.size()) {
                throw_compact_node_error(context, node, edge_index, edge);
            }
            continue;
        }

        if (edge.target_count != 0) {
            throw_compact_node_error(context, node, edge_index, edge);
        }
        if ((edge.mode == ActionMode::Coup || edge.mode == ActionMode::Realign) && edge.country == 0) {
            throw_compact_node_error(context, node, edge_index, edge);
        }
        if ((edge.mode == ActionMode::Event || edge.mode == ActionMode::Space) && edge.country != 0) {
            throw_compact_node_error(context, node, edge_index, edge);
        }
    }
}

torch::Tensor get_tensor(const c10::impl::GenericDict& dict, const char* key, bool required = true) {
    const auto key_value = c10::IValue(std::string(key));
    if (!dict.contains(key_value)) {
        if (required) {
            throw std::runtime_error(std::string("missing model output key: ") + key);
        }
        return {};
    }
    return dict.at(key_value).toTensor();
}

nn::BatchOutputs forward_model_batched_local(torch::jit::script::Module& model, const nn::BatchInputs& inputs) {
    if (inputs.filled <= 0) {
        throw std::invalid_argument("batched forward requires at least one filled slot");
    }

    const auto dev = inputs.device;
    auto influence = inputs.influence.narrow(0, 0, inputs.filled);
    auto cards = inputs.cards.narrow(0, 0, inputs.filled);
    auto scalars = inputs.scalars.narrow(0, 0, inputs.filled);
    if (dev.type() != torch::kCPU) {
        influence = influence.to(dev);
        cards = cards.to(dev);
        scalars = scalars.to(dev);
    }

    std::vector<torch::jit::IValue> model_inputs;
    model_inputs.emplace_back(influence);
    model_inputs.emplace_back(cards);
    model_inputs.emplace_back(scalars);

    c10::InferenceMode guard;
    const auto outputs = model.forward(model_inputs).toGenericDict();

    auto to_cpu_contiguous = [](torch::Tensor tensor) -> torch::Tensor {
        if (!tensor.defined()) {
            return tensor;
        }
        if (!tensor.device().is_cpu()) {
            tensor = tensor.to(torch::kCPU);
        }
        return tensor.contiguous();
    };

    return nn::BatchOutputs{
        .card_logits = to_cpu_contiguous(get_tensor(outputs, "card_logits")),
        .mode_logits = to_cpu_contiguous(get_tensor(outputs, "mode_logits")),
        .country_logits = to_cpu_contiguous(get_tensor(outputs, "country_logits", false)),
        .strategy_logits = to_cpu_contiguous(get_tensor(outputs, "strategy_logits", false)),
        .country_strategy_logits = to_cpu_contiguous(get_tensor(outputs, "country_strategy_logits", false)),
        .value = to_cpu_contiguous(get_tensor(outputs, "value")),
    };
}

class ForwardWorker {
public:
    explicit ForwardWorker(bool enabled) : enabled_(enabled) {
        if (enabled_) {
            worker_ = std::thread([this] { worker_loop(); });
        }
    }

    ~ForwardWorker() {
        if (!enabled_) {
            return;
        }
        {
            std::unique_lock<std::mutex> lock(mu_);
            stop_ = true;
        }
        cv_job_.notify_one();
        worker_.join();
    }

    nn::BatchOutputs run(torch::jit::script::Module& model, const nn::BatchInputs& inputs) {
        if (!enabled_) {
            return forward_model_batched_local(model, inputs);
        }

        std::unique_lock<std::mutex> lock(mu_);
        cv_done_.wait(lock, [this] { return !has_job_; });
        model_ = &model;
        inputs_ = &inputs;
        done_ = false;
        has_job_ = true;
        cv_job_.notify_one();
        cv_done_.wait(lock, [this] { return done_; });
        return std::move(outputs_);
    }

private:
    void worker_loop() {
        for (;;) {
            torch::jit::script::Module* model = nullptr;
            const nn::BatchInputs* inputs = nullptr;
            {
                std::unique_lock<std::mutex> lock(mu_);
                cv_job_.wait(lock, [this] { return stop_ || has_job_; });
                if (stop_) {
                    return;
                }
                model = model_;
                inputs = inputs_;
            }

            auto outputs = forward_model_batched_local(*model, *inputs);

            {
                std::unique_lock<std::mutex> lock(mu_);
                outputs_ = std::move(outputs);
                has_job_ = false;
                done_ = true;
            }
            cv_done_.notify_one();
        }
    }

    bool enabled_ = false;
    bool stop_ = false;
    bool has_job_ = false;
    bool done_ = false;
    torch::jit::script::Module* model_ = nullptr;
    const nn::BatchInputs* inputs_ = nullptr;
    nn::BatchOutputs outputs_;
    std::mutex mu_;
    std::condition_variable cv_job_;
    std::condition_variable cv_done_;
    std::thread worker_;
};

inline void softmax_inplace(float* buf, int n) {
    float max_val = -std::numeric_limits<float>::infinity();
    for (int i = 0; i < n; ++i) {
        if (buf[i] > max_val) {
            max_val = buf[i];
        }
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

struct AccessibleCache {
    std::vector<CountryId> influence;
    std::vector<CountryId> coup;
    std::vector<CountryId> realign;
    bool can_space = false;
    int space_ops_min = 2;

    static AccessibleCache build(Side side, const PublicState& pub) {
        AccessibleCache cache;

        auto base_inf = accessible_countries(side, pub, ActionMode::Influence);
        auto base_coup = accessible_countries(side, pub, ActionMode::Coup);

        auto filter_valid = [](std::vector<CountryId>& countries) {
            countries.erase(
                std::remove_if(
                    countries.begin(),
                    countries.end(),
                    [](CountryId cid) {
                        return cid == 0 || cid == kUsaAnchorId || cid == kUssrAnchorId || !has_country_spec(cid);
                    }
                ),
                countries.end()
            );
        };
        filter_valid(base_inf);
        filter_valid(base_coup);

        if (side == Side::USSR && pub.chernobyl_blocked_region.has_value()) {
            const auto blocked = *pub.chernobyl_blocked_region;
            base_inf.erase(
                std::remove_if(
                    base_inf.begin(),
                    base_inf.end(),
                    [blocked](CountryId cid) { return country_spec(cid).region == blocked; }
                ),
                base_inf.end()
            );
        }
        cache.influence = std::move(base_inf);

        auto filter_military = [&](std::vector<CountryId>& countries) {
            countries.erase(
                std::remove_if(
                    countries.begin(),
                    countries.end(),
                    [&](CountryId cid) {
                        if (cid == kUsaAnchorId || cid == kUssrAnchorId) {
                            return true;
                        }
                        constexpr std::array<int, 7> kDefconRegionThreshold = {4, 3, 2, 1, 1, 1, 3};
                        const auto threshold = kDefconRegionThreshold[static_cast<size_t>(country_spec(cid).region)];
                        if (pub.defcon <= threshold) {
                            return true;
                        }
                        if (side == Side::USSR) {
                            if (pub.nato_active) {
                                constexpr std::array<CountryId, 12> kNatoWe = {1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18};
                                const bool in_nato =
                                    std::find(kNatoWe.begin(), kNatoWe.end(), cid) != kNatoWe.end();
                                if (in_nato) {
                                    const bool exempted =
                                        (cid == 7 && pub.de_gaulle_active) || (cid == 18 && pub.willy_brandt_active);
                                    if (!exempted && controls_country(Side::US, cid, pub)) {
                                        return true;
                                    }
                                }
                            }
                            if (pub.us_japan_pact_active && cid == 22) {
                                return true;
                            }
                        }
                        return false;
                    }
                ),
                countries.end()
            );
        };
        filter_military(base_coup);
        filter_valid(base_coup);
        cache.coup = std::move(base_coup);
        cache.realign = cache.coup;

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

struct LegalCardInfo {
    CardId card_id = 0;
    int ops = 0;
    bool has_influence = false;
    bool has_coup = false;
    bool has_realign = false;
    bool has_space = false;
    bool has_event = false;
};

struct CompactLegalCardsResult {
    std::vector<LegalCardInfo> cards;
    AccessibleCache cache;
};

DraftsResult collect_card_drafts_cached(const GameState& state) {
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

        auto try_add_mode = [&](ActionMode mode, const std::vector<CountryId>& countries) {
            if (countries.empty()) {
                return;
            }
            if (mode == ActionMode::Coup && pub.defcon <= 2) {
                return;
            }
            if (pub.cuban_missile_crisis_active && mode == ActionMode::Coup) {
                return;
            }

            ModeDraft mode_draft{.mode = mode, .edges = {}};
            mode_draft.edges.reserve(countries.size());
            for (const auto country : countries) {
                if (!has_country_spec(country)) {
                    continue;
                }
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
            if (!cache.influence.empty()) {
                card.modes.push_back(ModeDraft{
                    .mode = ActionMode::Influence,
                    .edges = {ActionEncoding{.card_id = card_id, .mode = ActionMode::Influence, .targets = {}}},
                });
            }

            try_add_mode(ActionMode::Coup, cache.coup);
            try_add_mode(ActionMode::Realign, cache.realign);

            if (cache.can_space && spec.ops >= cache.space_ops_min) {
                const bool blocked =
                    (pub.bear_trap_active && side == Side::USSR && !spec.is_scoring) ||
                    (pub.quagmire_active && side == Side::US && !spec.is_scoring);
                if (!blocked) {
                    card.modes.push_back(ModeDraft{
                        .mode = ActionMode::Space,
                        .edges = {ActionEncoding{.card_id = card_id, .mode = ActionMode::Space, .targets = {}}},
                    });
                }
            }
        }

        bool event_ok = true;
        if (card_id == 21 && !nato_prerequisite_met_inline(pub)) {
            event_ok = false;
        }
        if (pub.defcon <= 2 && is_defcon_lowering_card(card_id)) {
            event_ok = false;
        }
        if (pub.bear_trap_active && side == Side::USSR && !spec.is_scoring) {
            event_ok = false;
        }
        if (pub.quagmire_active && side == Side::US && !spec.is_scoring) {
            event_ok = false;
        }
        if (card_id == 103 && pub.defcon != 2) {
            event_ok = false;
        }
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

CompactLegalCardsResult collect_compact_legal_cards(const GameState& state) {
    const auto side = state.pub.phasing;
    const auto holds_china = holds_china_for(state, side);
    const auto& pub = state.pub;
    auto cache = AccessibleCache::build(side, pub);

    std::vector<LegalCardInfo> cards;
    cards.reserve(10);

    for (const auto card_id : legal_cards(state.hands[to_index(side)], pub, side, holds_china)) {
        if (is_card_blocked_by_defcon(pub, side, card_id)) {
            continue;
        }

        const auto& spec = card_spec(card_id);
        const int ops = effective_ops(card_id, pub, side);
        const bool trapped = (pub.bear_trap_active && side == Side::USSR && !spec.is_scoring) ||
            (pub.quagmire_active && side == Side::US && !spec.is_scoring);

        LegalCardInfo card{
            .card_id = card_id,
            .ops = ops,
            .has_influence = spec.ops > 0 && !cache.influence.empty(),
            .has_coup = spec.ops > 0 && !cache.coup.empty() && pub.defcon > 2 && !pub.cuban_missile_crisis_active,
            .has_realign = spec.ops > 0 && !cache.realign.empty(),
            .has_space = spec.ops > 0 && cache.can_space && spec.ops >= cache.space_ops_min && !trapped,
            .has_event = false,
        };

        bool event_ok = true;
        if (card_id == 21 && !nato_prerequisite_met_inline(pub)) {
            event_ok = false;
        }
        if (pub.defcon <= 2 && is_defcon_lowering_card(card_id)) {
            event_ok = false;
        }
        if (trapped) {
            event_ok = false;
        }
        if (card_id == 103 && pub.defcon != 2) {
            event_ok = false;
        }
        card.has_event = event_ok;

        if (card.has_influence || card.has_coup || card.has_realign || card.has_space || card.has_event) {
            cards.push_back(card);
        }
    }

    return CompactLegalCardsResult{
        .cards = std::move(cards),
        .cache = std::move(cache),
    };
}

int exact_edge_count(const CompactLegalCardsResult& legal) {
    int total = 0;
    for (const auto& card : legal.cards) {
        total += card.has_influence ? 1 : 0;
        total += card.has_coup ? static_cast<int>(legal.cache.coup.size()) : 0;
        total += card.has_realign ? static_cast<int>(legal.cache.realign.size()) : 0;
        total += card.has_space ? 1 : 0;
        total += card.has_event ? 1 : 0;
    }
    return total;
}

bool has_any_model_action_cached_exact(const GameState& state) {
    const auto side = state.pub.phasing;
    const auto holds_china = holds_china_for(state, side);
    const auto& pub = state.pub;
    auto cache = AccessibleCache::build(side, pub);
    const auto& hand = state.hands[to_index(side)];

    for (int raw_card_id = 1; raw_card_id <= kMaxCardId; ++raw_card_id) {
        if (!hand.test(raw_card_id)) {
            continue;
        }
        const auto card_id = static_cast<CardId>(raw_card_id);
        if (card_id == kChinaCardId && !holds_china) {
            continue;
        }
        if (is_card_blocked_by_defcon(pub, side, card_id)) {
            continue;
        }

        const auto& spec = card_spec(card_id);
        if (spec.ops > 0) {
            if (!cache.influence.empty()) {
                return true;
            }
            if (!cache.coup.empty() && pub.defcon > 2 && !pub.cuban_missile_crisis_active) {
                return true;
            }
            if (!cache.realign.empty()) {
                return true;
            }
            const bool trapped = (pub.bear_trap_active && side == Side::USSR && !spec.is_scoring) ||
                (pub.quagmire_active && side == Side::US && !spec.is_scoring);
            if (cache.can_space && spec.ops >= cache.space_ops_min && !trapped) {
                return true;
            }
        }

        bool event_ok = true;
        if (card_id == 21 && !nato_prerequisite_met_inline(pub)) {
            event_ok = false;
        }
        if (pub.defcon <= 2 && is_defcon_lowering_card(card_id)) {
            event_ok = false;
        }
        if ((pub.bear_trap_active && side == Side::USSR && !spec.is_scoring) ||
            (pub.quagmire_active && side == Side::US && !spec.is_scoring)) {
            event_ok = false;
        }
        if (card_id == 103 && pub.defcon != 2) {
            event_ok = false;
        }
        if (event_ok) {
            return true;
        }
    }

    return false;
}

inline void softmax_compact_inplace(float* values, int n) {
    if (n <= 0) {
        return;
    }
    float max_val = values[0];
    for (int i = 1; i < n; ++i) {
        if (values[i] > max_val) {
            max_val = values[i];
        }
    }
    float sum = 0.0f;
    for (int i = 0; i < n; ++i) {
        values[i] = std::exp(values[i] - max_val);
        sum += values[i];
    }
    if (sum > 0.0f) {
        const float inv_sum = 1.0f / sum;
        for (int i = 0; i < n; ++i) {
            values[i] *= inv_sum;
        }
    }
}

int softmax_country_logits_for_accessible(
    const std::vector<CountryId>& accessible,
    const float* country_logits,
    int n_country,
    float* out_probs
) {
    int count = 0;
    for (const auto cid : accessible) {
        const int idx = static_cast<int>(cid);
        if (idx >= 0 && idx < n_country) {
            out_probs[count++] = country_logits[idx];
        }
    }
    softmax_compact_inplace(out_probs, count);
    return count;
}

ActionEncoding build_influence_action_from_probs(CardId card_id, int ops, const std::vector<CountryId>& accessible, const float* influence_probs) {
    ActionEncoding resolved{
        .card_id = card_id,
        .mode = ActionMode::Influence,
        .targets = {},
    };
    if (accessible.empty() || ops <= 0) {
        return resolved;
    }

    const int n_acc = static_cast<int>(accessible.size());
    int alloc_i[kMaxCountryLogits];
    int floor_sum = 0;
    float alloc_f[kMaxCountryLogits];
    for (int i = 0; i < n_acc; ++i) {
        alloc_f[i] = influence_probs[i] * static_cast<float>(ops);
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
        for (int i = 0; i < remainder && i < n_acc; ++i) {
            alloc_i[order[i].second] += 1;
        }
    }

    resolved.targets.reserve(static_cast<size_t>(ops));
    for (int i = 0; i < n_acc; ++i) {
        for (int j = 0; j < alloc_i[i]; ++j) {
            resolved.targets.push_back(accessible[static_cast<size_t>(i)]);
        }
    }
    return resolved;
}

ActionEncoding materialize_action(const FastNode& node, size_t edge_index) {
    const auto& edge = node.edges[edge_index];
    ActionEncoding action{
        .card_id = edge.card_id,
        .mode = edge.mode,
        .targets = {},
    };
    if (edge.mode == ActionMode::Influence && edge.target_count > 0) {
        if (static_cast<size_t>(edge.target_offset + edge.target_count) > node.resolved_targets.size()) {
            throw_compact_node_error("materialize_action influence range", node, edge_index, edge);
        }
        action.targets.reserve(static_cast<size_t>(edge.target_count));
        for (int i = 0; i < edge.target_count; ++i) {
            action.targets.push_back(node.resolved_targets[static_cast<size_t>(edge.target_offset + i)]);
        }
    } else if ((edge.mode == ActionMode::Coup || edge.mode == ActionMode::Realign) && edge.country != 0) {
        action.targets.push_back(edge.country);
    } else if (edge.mode == ActionMode::Coup || edge.mode == ActionMode::Realign) {
        throw_compact_node_error("materialize_action military edge missing target", node, edge_index, edge);
    }
    return action;
}

void append_compact_edge(FastNode& node, const ActionEncoding& action, float prior, const char* context) {
    int target_offset = 0;
    int target_count = 0;
    CountryId country = 0;
    if (action.mode == ActionMode::Influence && !action.targets.empty()) {
        target_offset = static_cast<int>(node.resolved_targets.size());
        target_count = static_cast<int>(action.targets.size());
        node.resolved_targets.insert(node.resolved_targets.end(), action.targets.begin(), action.targets.end());
    } else if ((action.mode == ActionMode::Coup || action.mode == ActionMode::Realign) && !action.targets.empty()) {
        country = action.targets.front();
    } else if (action.mode == ActionMode::Coup || action.mode == ActionMode::Realign) {
        throw std::runtime_error(
            std::string(context) +
            " append_compact_edge received military action without target card=" +
            std::to_string(static_cast<int>(action.card_id)) +
            " mode=" + std::to_string(static_cast<int>(action.mode))
        );
    }
    node.edges.push_back(FastEdge{
        .card_id = action.card_id,
        .mode = action.mode,
        .country = country,
        .target_offset = target_offset,
        .target_count = target_count,
        .prior = prior,
    });
    node.children.emplace_back(nullptr);
    if constexpr (kValidateCompactTree) {
        validate_compact_node(node, context);
    }
}

void apply_root_dirichlet_noise_fast(FastNode& root, const MctsConfig& config, Pcg64Rng& rng) {
    if (config.dir_epsilon <= 0.0f || config.dir_alpha <= 0.0f || root.edges.empty()) {
        return;
    }

    std::vector<double> noise(root.edges.size(), 0.0);
    std::gamma_distribution<double> gamma(static_cast<double>(config.dir_alpha), 1.0);

    double total_noise = 0.0;
    for (auto& sample : noise) {
        sample = gamma(rng);
        total_noise += sample;
    }
    if (total_noise <= 0.0) {
        const auto uniform = 1.0 / static_cast<double>(noise.size());
        std::fill(noise.begin(), noise.end(), uniform);
    } else {
        for (auto& sample : noise) {
            sample /= total_noise;
        }
    }

    const auto epsilon = static_cast<double>(config.dir_epsilon);
    const auto keep = 1.0 - epsilon;
    for (size_t i = 0; i < root.edges.size(); ++i) {
        root.edges[i].prior = static_cast<float>(keep * static_cast<double>(root.edges[i].prior) + epsilon * noise[i]);
    }
}

struct RawBatchOutputs {
    torch::Tensor card_logits_tensor;
    const float* card_logits = nullptr;
    int n_card = 0;
    int card_stride = 0;

    torch::Tensor mode_logits_tensor;
    const float* mode_logits = nullptr;
    int n_mode = 0;
    int mode_stride = 0;

    torch::Tensor country_logits_tensor;
    const float* country_logits = nullptr;
    int n_country = 0;
    int country_stride = 0;

    torch::Tensor strategy_logits_tensor;
    const float* strategy_logits = nullptr;
    int n_strategy = 0;
    int strategy_stride = 0;

    torch::Tensor country_strategy_logits_tensor;
    const float* country_strategy_logits = nullptr;
    int cs_n_strategies = 0;
    int cs_n_countries = 0;
    int cs_batch_stride = 0;

    torch::Tensor value_tensor;
    const float* value = nullptr;
    int value_stride = 0;

    static RawBatchOutputs extract(const nn::BatchOutputs& outputs) {
        RawBatchOutputs raw;
        raw.card_logits_tensor = outputs.card_logits.contiguous();
        raw.card_logits = raw.card_logits_tensor.data_ptr<float>();
        raw.n_card = std::min(static_cast<int>(raw.card_logits_tensor.size(1)), kMaxCardLogits);
        raw.card_stride = static_cast<int>(raw.card_logits_tensor.stride(0));

        raw.mode_logits_tensor = outputs.mode_logits.contiguous();
        raw.mode_logits = raw.mode_logits_tensor.data_ptr<float>();
        raw.n_mode = std::min(static_cast<int>(raw.mode_logits_tensor.size(1)), kMaxModeLogits);
        raw.mode_stride = static_cast<int>(raw.mode_logits_tensor.stride(0));

        if (outputs.country_logits.defined()) {
            raw.country_logits_tensor = outputs.country_logits.contiguous();
            raw.country_logits = raw.country_logits_tensor.data_ptr<float>();
            raw.n_country = std::min(static_cast<int>(raw.country_logits_tensor.size(1)), kMaxCountryLogits);
            raw.country_stride = static_cast<int>(raw.country_logits_tensor.stride(0));
        }
        if (outputs.strategy_logits.defined()) {
            raw.strategy_logits_tensor = outputs.strategy_logits.contiguous();
            raw.strategy_logits = raw.strategy_logits_tensor.data_ptr<float>();
            raw.n_strategy = std::min(static_cast<int>(raw.strategy_logits_tensor.size(1)), kMaxStrategies);
            raw.strategy_stride = static_cast<int>(raw.strategy_logits_tensor.stride(0));
        }
        if (outputs.country_strategy_logits.defined()) {
            raw.country_strategy_logits_tensor = outputs.country_strategy_logits.contiguous();
            raw.country_strategy_logits = raw.country_strategy_logits_tensor.data_ptr<float>();
            raw.cs_n_strategies = static_cast<int>(raw.country_strategy_logits_tensor.size(1));
            raw.cs_n_countries = static_cast<int>(raw.country_strategy_logits_tensor.size(2));
            raw.cs_batch_stride = static_cast<int>(raw.country_strategy_logits_tensor.stride(0));
        }
        raw.value_tensor = outputs.value.contiguous();
        raw.value = raw.value_tensor.data_ptr<float>();
        raw.value_stride = static_cast<int>(raw.value_tensor.stride(0));
        return raw;
    }
};

[[maybe_unused]] ExpansionResult expand_from_raw(
    const GameState& state,
    const RawBatchOutputs& raw,
    int batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto node = std::make_unique<FastNode>();
    node->side_to_move = state.pub.phasing;
    node->edges.reserve(64);
    node->children.reserve(64);

    auto [drafts, cache] = collect_card_drafts_cached(state);

    float card_logits_arr[kMaxCardLogits];
    float mode_logits_arr[kMaxModeLogits];
    float country_logits_arr[kMaxCountryLogits];

    const int n_card = raw.n_card;
    std::memcpy(
        card_logits_arr,
        raw.card_logits + batch_index * raw.card_stride,
        static_cast<size_t>(n_card) * sizeof(float)
    );

    const int n_mode = raw.n_mode;
    std::memcpy(
        mode_logits_arr,
        raw.mode_logits + batch_index * raw.mode_stride,
        static_cast<size_t>(n_mode) * sizeof(float)
    );

    const float* country_logits_ptr = nullptr;
    int n_country = 0;

    if (raw.strategy_logits != nullptr && raw.country_strategy_logits != nullptr &&
        raw.cs_n_countries > 0 && raw.cs_n_strategies > 0) {
        const float* strategies = raw.strategy_logits + batch_index * raw.strategy_stride;
        int best_strategy = 0;
        float best_value = strategies[0];
        for (int i = 1; i < raw.n_strategy; ++i) {
            if (strategies[i] > best_value) {
                best_value = strategies[i];
                best_strategy = i;
            }
        }
        n_country = std::min(raw.cs_n_countries, kMaxCountryLogits);
        const float* row = raw.country_strategy_logits +
            batch_index * raw.cs_batch_stride +
            best_strategy * raw.cs_n_countries;
        std::memcpy(country_logits_arr, row, static_cast<size_t>(n_country) * sizeof(float));
        country_logits_ptr = country_logits_arr;
    } else if (raw.country_logits != nullptr) {
        n_country = raw.n_country;
        std::memcpy(
            country_logits_arr,
            raw.country_logits + batch_index * raw.country_stride,
            static_cast<size_t>(n_country) * sizeof(float)
        );
        country_logits_ptr = country_logits_arr;
    }

    float masked_card[kMaxCardLogits];
    std::fill(masked_card, masked_card + n_card, -std::numeric_limits<float>::infinity());
    for (const auto& card : drafts) {
        const int idx = static_cast<int>(card.card_id) - 1;
        if (idx >= 0 && idx < n_card) {
            masked_card[idx] = card_logits_arr[idx];
        }
    }
    softmax_inplace(masked_card, n_card);

    double total_prior = 0.0;
    for (const auto& card : drafts) {
        float masked_mode[kMaxModeLogits];
        std::fill(masked_mode, masked_mode + n_mode, -std::numeric_limits<float>::infinity());
        for (const auto& mode : card.modes) {
            const int idx = static_cast<int>(mode.mode);
            if (idx < n_mode) {
                masked_mode[idx] = mode_logits_arr[idx];
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
                    append_compact_edge(*node, edge, static_cast<float>(prior), "expand_from_raw military-softmax");
                    total_prior += prior;
                }
                continue;
            }

            const auto per_edge_prior = card_prob * mode_prob;
            for (const auto& edge : mode.edges) {
                if (edge.mode == ActionMode::Influence && country_logits_ptr != nullptr && !cache.influence.empty()) {
                    const auto ops = effective_ops(edge.card_id, state.pub, state.pub.phasing);
                    float masked[kMaxCountryLogits];
                    std::fill(masked, masked + n_country, -std::numeric_limits<float>::infinity());
                    for (const auto cid : cache.influence) {
                        const int idx = static_cast<int>(cid);
                        if (idx < n_country) {
                            masked[idx] = country_logits_arr[idx];
                        }
                    }
                    softmax_inplace(masked, n_country);

                    const int n_acc = static_cast<int>(cache.influence.size());
                    int alloc_i[kMaxCountryLogits];
                    int floor_sum = 0;
                    float alloc_f[kMaxCountryLogits];
                    for (int i = 0; i < n_acc; ++i) {
                        const float p = masked[static_cast<int>(cache.influence[static_cast<size_t>(i)])];
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
                        for (int i = 0; i < remainder && i < n_acc; ++i) {
                            alloc_i[order[i].second] += 1;
                        }
                    }
                    ActionEncoding resolved{.card_id = edge.card_id, .mode = edge.mode, .targets = {}};
                    for (int i = 0; i < n_acc; ++i) {
                        for (int j = 0; j < alloc_i[i]; ++j) {
                            resolved.targets.push_back(cache.influence[static_cast<size_t>(i)]);
                        }
                    }
                    append_compact_edge(*node, resolved, static_cast<float>(per_edge_prior), "expand_from_raw influence-resolved");
                } else {
                    append_compact_edge(*node, edge, static_cast<float>(per_edge_prior), "expand_from_raw generic");
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
            append_compact_edge(*node, *fallback, 1.0f, "expand_from_raw fallback");
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

ExpansionResult expand_from_raw_flat(
    const GameState& state,
    const RawBatchOutputs& raw,
    int batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    auto legal = collect_compact_legal_cards(state);
    const auto& cards = legal.cards;
    const auto& cache = legal.cache;

    auto node = std::make_unique<FastNode>();
    node->side_to_move = state.pub.phasing;
    const int reserved_edges = exact_edge_count(legal);
    node->edges.reserve(static_cast<size_t>(std::max(1, reserved_edges)));
    node->children.reserve(static_cast<size_t>(std::max(1, reserved_edges)));
    node->resolved_targets.reserve(static_cast<size_t>(std::max(8, reserved_edges * 2)));

    const float* card_logits = raw.card_logits + batch_index * raw.card_stride;
    const int n_card = raw.n_card;
    const float* mode_logits = raw.mode_logits + batch_index * raw.mode_stride;
    const int n_mode = raw.n_mode;

    const float* country_logits_ptr = nullptr;
    int n_country = 0;

    if (raw.strategy_logits != nullptr && raw.country_strategy_logits != nullptr &&
        raw.cs_n_countries > 0 && raw.cs_n_strategies > 0) {
        const float* strategies = raw.strategy_logits + batch_index * raw.strategy_stride;
        int best_strategy = 0;
        float best_value = strategies[0];
        for (int i = 1; i < raw.n_strategy; ++i) {
            if (strategies[i] > best_value) {
                best_value = strategies[i];
                best_strategy = i;
            }
        }
        n_country = std::min(raw.cs_n_countries, kMaxCountryLogits);
        country_logits_ptr = raw.country_strategy_logits +
            batch_index * raw.cs_batch_stride +
            best_strategy * raw.cs_n_countries;
    } else if (raw.country_logits != nullptr) {
        n_country = raw.n_country;
        country_logits_ptr = raw.country_logits + batch_index * raw.country_stride;
    }

    float card_probs[kMaxCardLogits];
    int card_prob_count = 0;
    for (const auto& card : cards) {
        const int idx = static_cast<int>(card.card_id) - 1;
        if (idx >= 0 && idx < n_card) {
            card_probs[card_prob_count++] = card_logits[idx];
        }
    }
    softmax_compact_inplace(card_probs, card_prob_count);

    float influence_probs[kMaxCountryLogits];
    int influence_prob_count = 0;
    float military_probs[kMaxCountryLogits];
    int military_prob_count = 0;
    if (country_logits_ptr != nullptr) {
        if (!cache.influence.empty()) {
            influence_prob_count =
                softmax_country_logits_for_accessible(cache.influence, country_logits_ptr, n_country, influence_probs);
        }
        if (!cache.coup.empty()) {
            military_prob_count =
                softmax_country_logits_for_accessible(cache.coup, country_logits_ptr, n_country, military_probs);
        }
    }

    double total_prior = 0.0;
    for (int card_idx = 0; card_idx < static_cast<int>(cards.size()); ++card_idx) {
        const auto& card = cards[static_cast<size_t>(card_idx)];
        ActionMode mode_order[5];
        float mode_probs[5];
        int mode_count = 0;
        if (card.has_influence) {
            mode_order[mode_count] = ActionMode::Influence;
            mode_probs[mode_count++] = static_cast<int>(ActionMode::Influence) < n_mode
                ? mode_logits[static_cast<int>(ActionMode::Influence)]
                : -std::numeric_limits<float>::infinity();
        }
        if (card.has_coup) {
            mode_order[mode_count] = ActionMode::Coup;
            mode_probs[mode_count++] = static_cast<int>(ActionMode::Coup) < n_mode
                ? mode_logits[static_cast<int>(ActionMode::Coup)]
                : -std::numeric_limits<float>::infinity();
        }
        if (card.has_realign) {
            mode_order[mode_count] = ActionMode::Realign;
            mode_probs[mode_count++] = static_cast<int>(ActionMode::Realign) < n_mode
                ? mode_logits[static_cast<int>(ActionMode::Realign)]
                : -std::numeric_limits<float>::infinity();
        }
        if (card.has_space) {
            mode_order[mode_count] = ActionMode::Space;
            mode_probs[mode_count++] = static_cast<int>(ActionMode::Space) < n_mode
                ? mode_logits[static_cast<int>(ActionMode::Space)]
                : -std::numeric_limits<float>::infinity();
        }
        if (card.has_event) {
            mode_order[mode_count] = ActionMode::Event;
            mode_probs[mode_count++] = static_cast<int>(ActionMode::Event) < n_mode
                ? mode_logits[static_cast<int>(ActionMode::Event)]
                : -std::numeric_limits<float>::infinity();
        }
        if (mode_count <= 0) {
            continue;
        }
        softmax_compact_inplace(mode_probs, mode_count);

        const double card_prob = static_cast<double>(card_probs[card_idx]);

        for (int mode_idx = 0; mode_idx < mode_count; ++mode_idx) {
            const auto mode = mode_order[mode_idx];
            const double mode_prob = static_cast<double>(mode_probs[mode_idx]);

            if ((mode == ActionMode::Coup || mode == ActionMode::Realign)) {
                const auto& military_targets = mode == ActionMode::Coup ? cache.coup : cache.realign;
                if (military_prob_count == static_cast<int>(military_targets.size())) {
                    for (int i = 0; i < military_prob_count; ++i) {
                        ActionEncoding edge{
                            .card_id = card.card_id,
                            .mode = mode,
                            .targets = {military_targets[static_cast<size_t>(i)]},
                        };
                        const auto prior = card_prob * mode_prob * static_cast<double>(military_probs[i]);
                        append_compact_edge(*node, edge, static_cast<float>(prior), "expand_from_raw_flat military-softmax");
                        total_prior += prior;
                    }
                    continue;
                }

                const auto per_edge_prior = card_prob * mode_prob;
                for (const auto country : military_targets) {
                    ActionEncoding edge{
                        .card_id = card.card_id,
                        .mode = mode,
                        .targets = {country},
                    };
                    append_compact_edge(*node, edge, static_cast<float>(per_edge_prior), "expand_from_raw_flat military-uniform");
                    total_prior += per_edge_prior;
                }
                continue;
            }

            const auto per_edge_prior = card_prob * mode_prob;
            ActionEncoding edge{
                .card_id = card.card_id,
                .mode = mode,
                .targets = {},
            };
            if (mode == ActionMode::Influence &&
                influence_prob_count == static_cast<int>(cache.influence.size()) &&
                !cache.influence.empty()) {
                append_compact_edge(
                    *node,
                    build_influence_action_from_probs(card.card_id, card.ops, cache.influence, influence_probs),
                    static_cast<float>(per_edge_prior),
                    "expand_from_raw_flat influence-resolved"
                );
            } else {
                append_compact_edge(*node, edge, static_cast<float>(per_edge_prior), "expand_from_raw_flat generic");
            }
            total_prior += per_edge_prior;
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
            append_compact_edge(*node, *fallback, 1.0f, "expand_from_raw_flat fallback");
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

[[maybe_unused]] std::vector<CardDraft> collect_card_drafts(const GameState& state) {
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
                    std::remove_if(
                        countries.begin(),
                        countries.end(),
                        [](CountryId cid) { return !has_country_spec(cid); }
                    ),
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
    auto node = std::make_unique<FastNode>();
    node->side_to_move = state.pub.phasing;

    if (state.game_over) {
        node->is_terminal = true;
        const auto terminal_value = winner_value(state.winner);
        node->terminal_value = terminal_value;
        return ExpansionResult{.node = std::move(node), .leaf_value = terminal_value};
    }

    if (has_any_model_action_cached_exact(state)) {
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
        append_compact_edge(*node, *fallback, 1.0f, "expand_without_model fallback");
        return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
    }

    node->is_terminal = true;
    return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
}

int best_root_edge_index(const FastNode& root) {
    if (root.edges.empty()) {
        return -1;
    }

    int best_index = 0;
    for (size_t i = 1; i < root.edges.size(); ++i) {
        const auto& current = root.edges[i];
        const auto& best = root.edges[static_cast<size_t>(best_index)];
        if (current.visit_count > best.visit_count) {
            best_index = static_cast<int>(i);
            continue;
        }
        if (current.visit_count == best.visit_count && current.prior > best.prior) {
            best_index = static_cast<int>(i);
        }
    }
    return best_index;
}

int select_edge_fast(const FastNode& node, float c_puct) {
    if (node.edges.empty()) {
        return -1;
    }

    constexpr double kVirtualLossPenalty = 1.0;
    int pending_visits = 0;
    for (const auto& edge : node.edges) {
        pending_visits += edge.virtual_loss;
    }

    const auto parent_visits = std::sqrt(static_cast<double>(std::max(1, node.total_visits + pending_visits)));
    int best_index = 0;
    double best_score = -std::numeric_limits<double>::infinity();
    const bool invert_q = (node.side_to_move == Side::US);
    for (size_t i = 0; i < node.edges.size(); ++i) {
        const auto& edge = node.edges[i];
        const auto effective_visits = edge.visit_count + edge.virtual_loss;
        const auto virtual_loss_term = static_cast<double>(edge.virtual_loss) * kVirtualLossPenalty;
        const auto effective_total_value = edge.total_value + (invert_q ? virtual_loss_term : -virtual_loss_term);
        auto q = effective_visits > 0 ? effective_total_value / static_cast<double>(effective_visits) : 0.0;
        if (invert_q) {
            q = -q;
        }
        const auto u = static_cast<double>(c_puct) * static_cast<double>(edge.prior) * parent_visits /
            static_cast<double>(1 + effective_visits);
        const auto score = q + u;
        if (score > best_score) {
            best_score = score;
            best_index = static_cast<int>(i);
        }
    }
    return best_index;
}

[[nodiscard]] float effective_temperature(const FastPendingDecision& decision, const BenchConfig& config) {
    if (config.temperature <= 0.0f) {
        return 0.0f;
    }
    float base = 0.0f;
    if (decision.move_number <= 10) {
        base = 1.0f;
    } else if (decision.move_number <= 30) {
        base = 0.5f;
    }
    return config.temperature * base;
}

std::optional<int> sample_edge_by_visit_counts(
    const FastNode& root,
    float temperature,
    Pcg64Rng& rng
) {
    if (temperature <= 0.0f || root.edges.empty()) {
        return std::nullopt;
    }

    std::vector<std::pair<size_t, double>> scaled_log_weights;
    scaled_log_weights.reserve(root.edges.size());
    double max_scaled_log_weight = -std::numeric_limits<double>::infinity();
    for (size_t i = 0; i < root.edges.size(); ++i) {
        const auto visits = root.edges[i].visit_count;
        if (visits <= 0) {
            continue;
        }
        const auto scaled_log_weight = std::log(static_cast<double>(visits)) / static_cast<double>(temperature);
        scaled_log_weights.emplace_back(i, scaled_log_weight);
        max_scaled_log_weight = std::max(max_scaled_log_weight, scaled_log_weight);
    }

    if (scaled_log_weights.empty()) {
        return std::nullopt;
    }

    std::vector<std::pair<size_t, double>> weights;
    weights.reserve(scaled_log_weights.size());
    double total_weight = 0.0;
    for (const auto& [edge_index, scaled_log_weight] : scaled_log_weights) {
        const auto weight = std::exp(scaled_log_weight - max_scaled_log_weight);
        if (!(weight > 0.0) || !std::isfinite(weight)) {
            continue;
        }
        total_weight += weight;
        weights.emplace_back(edge_index, total_weight);
    }

    if (!(total_weight > 0.0)) {
        return std::nullopt;
    }

    const auto draw = rng.random_double() * total_weight;
    for (const auto& [edge_index, cumulative_weight] : weights) {
        if (draw < cumulative_weight) {
            return static_cast<int>(edge_index);
        }
    }
    return static_cast<int>(weights.back().first);
}

void backpropagate_path(FastPendingExpansion& pending, double leaf_value, int virtual_loss_weight) {
    for (auto it = pending.path.rbegin(); it != pending.path.rend(); ++it) {
        auto* ancestor = it->first;
        auto& edge = ancestor->edges[static_cast<size_t>(it->second)];
        edge.virtual_loss = std::max(0, edge.virtual_loss - virtual_loss_weight);
        edge.visit_count += 1;
        edge.total_value += leaf_value;
        ancestor->total_visits += 1;
    }
    pending.path.clear();
}

int sims_budget(const FastGameSlot& slot, int max_pending) {
    if (slot.root == nullptr && slot.pending.empty()) {
        return 1;
    }
    if (slot.root == nullptr) {
        return 0;
    }
    const int in_flight = static_cast<int>(slot.pending.size());
    const int remaining = slot.sims_target - slot.sims_completed - in_flight;
    const int slot_capacity = max_pending - in_flight;
    return std::max(0, std::min(remaining, slot_capacity));
}

SelectionResult select_to_leaf(FastGameSlot& slot, const BenchConfig& config) {
    FastPendingExpansion pending;

    FastNode* node = slot.root.get();
    const GameState* best_cached = &slot.root_state;
    size_t best_cached_depth = 0;

    while (node != nullptr && !node->is_terminal && !node->edges.empty()) {
        const auto edge_index = select_edge_fast(*node, config.mcts.c_puct);
        if (edge_index < 0) {
            break;
        }

        auto& edge = node->edges[static_cast<size_t>(edge_index)];
        edge.virtual_loss += config.virtual_loss_weight;
        pending.path.emplace_back(node, edge_index);

        const bool is_leaf = (node->children[static_cast<size_t>(edge_index)] == nullptr);
        if (!is_leaf) {
            auto* child = node->children[static_cast<size_t>(edge_index)].get();
            if (child->cached_state) {
                best_cached = child->cached_state.get();
                best_cached_depth = pending.path.size();
            }
            node = child;
        } else {
            node = nullptr;
        }
    }

    pending.sim_state = clone_game_state(*best_cached);
    for (size_t i = best_cached_depth; i < pending.path.size(); ++i) {
        auto [path_node, path_edge_index] = pending.path[i];
        apply_tree_action(
            pending.sim_state,
            materialize_action(*path_node, static_cast<size_t>(path_edge_index)),
            slot.rng
        );
    }

    if (!pending.path.empty()) {
        auto [last_node, last_edge_index] = pending.path.back();
        if (last_node->children[static_cast<size_t>(last_edge_index)] == nullptr) {
            if (auto immediate = expand_without_model(pending.sim_state, slot.rng); immediate.has_value()) {
                last_node->children[static_cast<size_t>(last_edge_index)] = std::move(immediate->node);
                backpropagate_path(pending, immediate->leaf_value, config.virtual_loss_weight);
                return SelectionResult{.needs_batch = false, .leaf_value = immediate->leaf_value};
            }
            slot.pending.push_back(std::move(pending));
            return SelectionResult{.needs_batch = true};
        }
        node = last_node->children[static_cast<size_t>(last_edge_index)].get();
    } else {
        node = slot.root.get();
    }

    const double value = (node != nullptr && node->is_terminal) ? node->terminal_value : 0.0;
    backpropagate_path(pending, value, config.virtual_loss_weight);
    return SelectionResult{.needs_batch = false, .leaf_value = value};
}

void run_setup_influence_heuristic(GameState& state, Pcg64Rng& rng) {
    for (const auto side : {Side::USSR, Side::US}) {
        const SetupOpening* opening = (side == Side::USSR)
            ? choose_random_opening(kHumanUSSROpenings.data(), static_cast<int>(kHumanUSSROpenings.size()), rng)
            : choose_random_opening(kHumanUSOpeningsBid2.data(), static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
        if (opening == nullptr) {
            continue;
        }
        for (int i = 0; i < opening->count; ++i) {
            const auto country = opening->placements[i].country;
            const auto amount = opening->placements[i].amount;
            state.pub.set_influence(side, country, state.pub.influence_of(side, country) + amount);
        }
    }
    state.setup_influence_remaining = {0, 0};
    state.phase = GamePhase::Headline;
}

void initialize_slot(FastGameSlot& slot, int game_index, uint32_t base_seed, const BenchConfig& config) {
    const auto seed = base_seed + static_cast<uint32_t>(game_index);
    slot = FastGameSlot{};
    slot.active = true;
    slot.root_state = reset_game(seed);
    slot.rng = Pcg64Rng(seed);
    run_setup_influence_heuristic(slot.root_state, slot.rng);
    slot.turn = 1;
    slot.stage = BatchedGameStage::TurnSetup;
    slot.sims_target = config.mcts.n_simulations;
    slot.pending.reserve(static_cast<size_t>(std::max(1, config.max_pending)));
    slot.headline_order.reserve(2);
}

void reset_move_search(FastGameSlot& slot, const BenchConfig& config) {
    slot.root.reset();
    slot.pending.clear();
    slot.sims_completed = 0;
    slot.sims_target = config.mcts.n_simulations;
    slot.move_done = false;
}

void mark_game_done(FastGameSlot& slot, GameResult result) {
    slot.result = std::move(result);
    slot.game_done = true;
    slot.stage = BatchedGameStage::Finished;
    slot.move_done = false;
    slot.pending.clear();
    slot.decision.reset();
    slot.root.reset();
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

std::optional<GameResult> finish_turn(GameState& state, int turn) {
    state.phase = GamePhase::Cleanup;

    const auto defcon = state.pub.defcon;
    for (const auto side : {Side::USSR, Side::US}) {
        const auto shortfall = std::max(0, defcon - state.pub.milops[to_index(side)]);
        if (shortfall == 0) {
            continue;
        }
        if (side == Side::USSR) {
            state.pub.vp -= shortfall;
        } else {
            state.pub.vp += shortfall;
        }
    }

    auto [over, winner] = check_vp_win(state.pub);
    if (over) {
        return GameResult{
            .winner = winner,
            .final_vp = state.pub.vp,
            .end_turn = state.pub.turn,
            .end_reason = "vp",
        };
    }

    state.pub.defcon = std::min(5, state.pub.defcon + 1);
    state.pub.milops = {0, 0};
    state.pub.space_attempts = {0, 0};
    state.pub.ops_modifier = {0, 0};
    state.pub.vietnam_revolts_active = false;
    state.pub.north_sea_oil_extra_ar = false;
    state.pub.glasnost_extra_ar = false;
    state.pub.chernobyl_blocked_region.reset();
    state.pub.latam_coup_bonus.reset();

    if (turn == kMaxTurns) {
        auto final = apply_final_scoring(state.pub);
        state.pub.vp += final.vp_delta;
        if (final.game_over) {
            return GameResult{
                .winner = final.winner,
                .final_vp = state.pub.vp,
                .end_turn = turn,
                .end_reason = "europe_control",
            };
        }
        std::tie(over, winner) = check_vp_win(state.pub);
        if (over) {
            return GameResult{
                .winner = winner,
                .final_vp = state.pub.vp,
                .end_turn = turn,
                .end_reason = "vp_threshold",
            };
        }
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
            if (!state.hands[to_index(side)].test(card_id)) {
                continue;
            }
            if (card_spec(static_cast<CardId>(card_id)).is_scoring) {
                return GameResult{
                    .winner = other_side(side),
                    .final_vp = state.pub.vp,
                    .end_turn = state.pub.turn,
                    .end_reason = "scoring_card_held",
                };
            }
        }
    }

    for (const auto side : {Side::USSR, Side::US}) {
        for (int card_id = 1; card_id <= kMaxCardId; ++card_id) {
            if (state.hands[to_index(side)].test(card_id)) {
                state.pub.discard.set(card_id);
            }
        }
        state.hands[to_index(side)].reset();
    }

    return std::nullopt;
}

void advance_after_action_pair(FastGameSlot& slot) {
    if (slot.current_side == Side::USSR) {
        slot.current_side = Side::US;
    } else {
        slot.current_side = Side::USSR;
        slot.current_ar += 1;
    }
}

void move_to_post_round_stage(FastGameSlot& slot) {
    if (slot.root_state.pub.north_sea_oil_extra_ar) {
        slot.root_state.pub.north_sea_oil_extra_ar = false;
        slot.stage = BatchedGameStage::ExtraActionRoundUS;
        return;
    }
    if (slot.root_state.pub.glasnost_extra_ar) {
        slot.root_state.pub.glasnost_extra_ar = false;
        slot.stage = BatchedGameStage::ExtraActionRoundUSSR;
        return;
    }
    slot.stage = BatchedGameStage::Cleanup;
}

void move_to_followup_stage_after_extra(FastGameSlot& slot, Side side) {
    if (side == Side::US && slot.root_state.pub.glasnost_extra_ar) {
        slot.root_state.pub.glasnost_extra_ar = false;
        slot.stage = BatchedGameStage::ExtraActionRoundUSSR;
        return;
    }
    slot.stage = BatchedGameStage::Cleanup;
}

void queue_decision(FastGameSlot& slot, Side side, int ar, bool is_headline, const BenchConfig& config) {
    slot.root_state.pub.phasing = side;
    slot.root_state.pub.ar = ar;
    slot.decision = FastPendingDecision{
        .turn = slot.root_state.pub.turn,
        .ar = ar,
        .move_number = slot.decisions_started + 1,
        .side = side,
        .holds_china = holds_china_for(slot.root_state, side),
        .is_headline = is_headline,
    };
    slot.decisions_started += 1;
    reset_move_search(slot, config);
}

void finalize_headline_choices(FastGameSlot& slot) {
    slot.headline_order.clear();
    for (const auto side : {Side::USSR, Side::US}) {
        if (slot.pending_headlines[to_index(side)].has_value()) {
            slot.headline_order.push_back(*slot.pending_headlines[to_index(side)]);
        }
    }

    if (slot.pending_headlines[to_index(Side::US)].has_value() &&
        slot.pending_headlines[to_index(Side::US)]->action.card_id == 108 &&
        slot.pending_headlines[to_index(Side::USSR)].has_value()) {
        slot.root_state.pub.discard.set(slot.pending_headlines[to_index(Side::USSR)]->action.card_id);
        slot.headline_order.erase(
            std::remove_if(
                slot.headline_order.begin(),
                slot.headline_order.end(),
                [](const FastPendingHeadlineChoice& pending) { return pending.side == Side::USSR; }
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
    slot.stage = BatchedGameStage::HeadlineResolve;
}

void advance_until_decision(FastGameSlot& slot, const BenchConfig& config) {
    while (slot.active && !slot.game_done && !slot.move_done && !slot.decision.has_value()) {
        switch (slot.stage) {
            case BatchedGameStage::TurnSetup: {
                slot.root_state.pub.turn = slot.turn;
                if (slot.turn == kMidWarTurn) {
                    advance_to_mid_war(slot.root_state, slot.rng);
                } else if (slot.turn == kLateWarTurn) {
                    advance_to_late_war(slot.root_state, slot.rng);
                }
                deal_cards(slot.root_state, Side::USSR, slot.rng);
                deal_cards(slot.root_state, Side::US, slot.rng);
                slot.pending_headlines = {};
                slot.headline_order.clear();
                slot.headline_order_index = 0;
                slot.total_ars = ars_for_turn(slot.turn);
                slot.current_ar = 1;
                slot.current_side = Side::USSR;
                slot.stage = BatchedGameStage::HeadlineChoiceUSSR;
                break;
            }

            case BatchedGameStage::HeadlineChoiceUSSR:
            case BatchedGameStage::HeadlineChoiceUS: {
                const auto side = slot.stage == BatchedGameStage::HeadlineChoiceUSSR ? Side::USSR : Side::US;
                const auto holds_china = holds_china_for(slot.root_state, side);
                if (!has_legal_action(slot.root_state.hands[to_index(side)], slot.root_state.pub, side, holds_china)) {
                    if (side == Side::USSR) {
                        slot.stage = BatchedGameStage::HeadlineChoiceUS;
                    } else {
                        finalize_headline_choices(slot);
                    }
                    break;
                }
                slot.root_state.phase = GamePhase::Headline;
                queue_decision(slot, side, 0, true, config);
                break;
            }

            case BatchedGameStage::HeadlineResolve: {
                if (slot.headline_order_index >= slot.headline_order.size()) {
                    slot.stage = BatchedGameStage::ActionRound;
                    break;
                }

                const auto pending = slot.headline_order[slot.headline_order_index++];
                auto [new_pub, over, winner] = apply_action_live(slot.root_state, pending.action, pending.side, slot.rng);
                (void)new_pub;
                sync_china_flags(slot.root_state);
                if (over) {
                    mark_game_done(slot, GameResult{
                        .winner = winner,
                        .final_vp = slot.root_state.pub.vp,
                        .end_turn = slot.root_state.pub.turn,
                        .end_reason = end_reason(slot.root_state.pub, winner),
                    });
                }
                break;
            }

            case BatchedGameStage::ActionRound: {
                if (slot.current_ar > kSpaceShuttleArs) {
                    move_to_post_round_stage(slot);
                    break;
                }

                const auto side = slot.current_side;
                if (slot.current_ar > slot.total_ars && slot.root_state.pub.space[to_index(side)] < kSpaceShuttleArs) {
                    advance_after_action_pair(slot);
                    break;
                }

                slot.root_state.phase = GamePhase::ActionRound;
                slot.root_state.pub.ar = slot.current_ar;
                slot.root_state.pub.phasing = side;
                if (auto trap_result = resolve_trap_ar_live(slot.root_state, side, slot.rng); trap_result.has_value()) {
                    auto& [new_pub, over, winner] = *trap_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.root_state.pub.vp,
                            .end_turn = slot.root_state.pub.turn,
                            .end_reason = end_reason(slot.root_state.pub, winner),
                        });
                        break;
                    }
                    advance_after_action_pair(slot);
                    break;
                }

                const auto holds_china = holds_china_for(slot.root_state, side);
                if (!has_legal_action(slot.root_state.hands[to_index(side)], slot.root_state.pub, side, holds_china)) {
                    advance_after_action_pair(slot);
                    break;
                }
                queue_decision(slot, side, slot.current_ar, false, config);
                break;
            }

            case BatchedGameStage::ExtraActionRoundUS:
            case BatchedGameStage::ExtraActionRoundUSSR: {
                const auto side = slot.stage == BatchedGameStage::ExtraActionRoundUS ? Side::US : Side::USSR;
                slot.root_state.pub.ar = std::max(slot.root_state.pub.ar, ars_for_turn(slot.root_state.pub.turn)) + 1;
                slot.root_state.pub.phasing = side;
                auto& hand = slot.root_state.hands[to_index(side)];
                if (hand.none()) {
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }
                if (auto trap_result = resolve_trap_ar_live(slot.root_state, side, slot.rng); trap_result.has_value()) {
                    auto& [new_pub, over, winner] = *trap_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.root_state.pub.vp,
                            .end_turn = slot.root_state.pub.turn,
                            .end_reason = end_reason(slot.root_state.pub, winner),
                        });
                        break;
                    }
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }

                const auto holds_china = holds_china_for(slot.root_state, side);
                if (!has_legal_action(hand, slot.root_state.pub, side, holds_china)) {
                    move_to_followup_stage_after_extra(slot, side);
                    break;
                }
                queue_decision(slot, side, slot.root_state.pub.ar, false, config);
                break;
            }

            case BatchedGameStage::Cleanup: {
                if (auto result = finish_turn(slot.root_state, slot.turn); result.has_value()) {
                    mark_game_done(slot, *result);
                    break;
                }
                if (slot.turn >= kMaxTurns) {
                    std::optional<Side> winner;
                    if (slot.root_state.pub.vp > 0) {
                        winner = Side::USSR;
                    } else if (slot.root_state.pub.vp < 0) {
                        winner = Side::US;
                    }
                    mark_game_done(slot, GameResult{
                        .winner = winner,
                        .final_vp = slot.root_state.pub.vp,
                        .end_turn = kMaxTurns,
                        .end_reason = "turn_limit",
                    });
                    break;
                }
                slot.turn += 1;
                slot.stage = BatchedGameStage::TurnSetup;
                break;
            }

            case BatchedGameStage::Finished:
                slot.game_done = true;
                break;
        }
    }
}

void commit_best_action(FastGameSlot& slot, const BenchConfig& config, BenchResult& metrics) {
    if (!slot.move_done || !slot.decision.has_value()) {
        return;
    }

    const auto decision = *slot.decision;

    ActionEncoding action{};
    int best_index = -1;
    if (slot.root != nullptr) {
        best_index = best_root_edge_index(*slot.root);
        if (best_index >= 0) {
            action = materialize_action(*slot.root, static_cast<size_t>(best_index));
        }
    }

    if (config.epsilon_greedy > 0.0f && slot.root != nullptr && !slot.root->edges.empty() &&
        slot.rng.random_double() < static_cast<double>(config.epsilon_greedy)) {
        best_index = static_cast<int>(slot.rng.choice_index(slot.root->edges.size()));
        action = materialize_action(*slot.root, static_cast<size_t>(best_index));
    } else if (slot.root != nullptr && action.card_id != 0) {
        const auto temp = effective_temperature(decision, config);
        if (const auto sampled = sample_edge_by_visit_counts(*slot.root, temp, slot.rng); sampled.has_value()) {
            best_index = *sampled;
            action = materialize_action(*slot.root, static_cast<size_t>(*sampled));
        }
    }

    if (action.card_id == 0) {
        action = choose_action(
            PolicyKind::MinimalHybrid,
            slot.root_state.pub,
            slot.root_state.hands[to_index(decision.side)],
            decision.holds_china,
            slot.rng
        ).value_or(ActionEncoding{});
    }
    if (action.card_id == 0) {
        throw std::runtime_error("fast batched MCTS could not resolve an action");
    }

    if (slot.sims_target > 0) {
        metrics.total_simulations += slot.sims_completed;
        metrics.mcts_decisions += 1;
    }

    slot.decision.reset();
    slot.root.reset();
    slot.pending.clear();
    slot.move_done = false;

    if (decision.is_headline) {
        action.mode = ActionMode::Event;
        action.targets.clear();
        auto& hand = slot.root_state.hands[to_index(decision.side)];
        if (hand.test(action.card_id)) {
            hand.reset(action.card_id);
        }
        slot.pending_headlines[to_index(decision.side)] = FastPendingHeadlineChoice{
            .side = decision.side,
            .holds_china = decision.holds_china,
            .action = action,
        };
        if (decision.side == Side::USSR) {
            slot.stage = BatchedGameStage::HeadlineChoiceUS;
        } else {
            finalize_headline_choices(slot);
        }
        return;
    }

    auto& hand = slot.root_state.hands[to_index(decision.side)];
    if (hand.test(action.card_id)) {
        hand.reset(action.card_id);
    }

    auto [new_pub, over, winner] = apply_action_live(slot.root_state, action, decision.side, slot.rng);
    (void)new_pub;
    sync_china_flags(slot.root_state);

    if (over) {
        mark_game_done(slot, GameResult{
            .winner = winner,
            .final_vp = slot.root_state.pub.vp,
            .end_turn = slot.root_state.pub.turn,
            .end_reason = end_reason(slot.root_state.pub, winner),
        });
        return;
    }

    if (decision.side == Side::USSR && slot.root_state.pub.norad_active && slot.root_state.pub.defcon == 2) {
        if (auto norad = resolve_norad_live(slot.root_state, slot.rng); norad.has_value()) {
            auto& [norad_pub, norad_over, norad_winner] = *norad;
            (void)norad_pub;
            if (norad_over) {
                mark_game_done(slot, GameResult{
                    .winner = norad_winner,
                    .final_vp = slot.root_state.pub.vp,
                    .end_turn = slot.root_state.pub.turn,
                    .end_reason = end_reason(slot.root_state.pub, norad_winner),
                });
                return;
            }
        }
    }

    if (slot.stage == BatchedGameStage::ActionRound) {
        advance_after_action_pair(slot);
        return;
    }
    if (slot.stage == BatchedGameStage::ExtraActionRoundUS || slot.stage == BatchedGameStage::ExtraActionRoundUSSR) {
        move_to_followup_stage_after_extra(slot, decision.side);
        return;
    }

    reset_move_search(slot, config);
}

}  // namespace

BenchResult benchmark_mcts_fast(
    int n_games,
    torch::jit::script::Module& model,
    const BenchConfig& config,
    uint32_t base_seed,
    torch::Device device
) {
    if (n_games <= 0) {
        throw std::invalid_argument("n_games must be positive");
    }
    if (config.pool_size <= 0) {
        throw std::invalid_argument("pool_size must be positive");
    }
    if (config.max_pending <= 0) {
        throw std::invalid_argument("max_pending must be positive");
    }
    if (config.virtual_loss_weight <= 0) {
        throw std::invalid_argument("virtual_loss_weight must be positive");
    }
    if (config.mcts.n_simulations < 0) {
        throw std::invalid_argument("n_simulations must be non-negative");
    }

    BenchResult result;
    result.n_games = n_games;
    result.pool_size = config.pool_size;
    result.n_simulations = config.mcts.n_simulations;

    std::vector<FastGameSlot> pool(static_cast<size_t>(config.pool_size));
    int games_started = 0;
    int games_emitted = 0;

    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(config.pool_size * config.max_pending, device);
    std::vector<BatchEntry> batch_entries;
    batch_entries.reserve(static_cast<size_t>(config.pool_size) * static_cast<size_t>(config.max_pending));
    ForwardWorker forward_worker(config.use_forward_worker);

    using Clock = std::chrono::high_resolution_clock;
    const auto t_start = Clock::now();

    while (games_emitted < n_games) {
        auto t0_adv = Clock::now();
        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                if (!config.learned_side.has_value()) {
                    if (slot.result.winner == Side::USSR) {
                        result.wins += 1;
                    } else if (slot.result.winner == Side::US) {
                        result.losses += 1;
                    } else {
                        result.draws += 1;
                    }
                } else if (slot.result.winner == *config.learned_side) {
                    result.wins += 1;
                } else if (slot.result.winner.has_value()) {
                    result.losses += 1;
                } else {
                    result.draws += 1;
                }
                slot.emitted = true;
                slot.active = false;
                games_emitted += 1;
            }
            if (!slot.active && games_started < n_games) {
                initialize_slot(slot, games_started, base_seed, config);
                games_started += 1;
            }
        }
        result.t_advance += std::chrono::duration<double>(Clock::now() - t0_adv).count();

        batch_inputs.reset();
        batch_entries.clear();

        auto t0_sel = Clock::now();
        for (auto& slot : pool) {
            if (!slot.active) {
                continue;
            }

            if (slot.move_done) {
                continue;
            }

            advance_until_decision(slot, config);
            if (slot.game_done || !slot.decision.has_value()) {
                continue;
            }

            if (config.learned_side.has_value() && slot.decision->side != *config.learned_side) {
                if (config.greedy_nn_opponent) {
                    slot.sims_target = 0;
                    slot.sims_completed = 0;
                } else {
                    slot.sims_target = 0;
                    slot.sims_completed = 0;
                    slot.move_done = true;
                    continue;
                }
            }

            if (slot.root == nullptr) {
                if (!slot.pending.empty()) {
                    continue;
                }
                if (auto immediate = expand_without_model(slot.root_state, slot.rng); immediate.has_value()) {
                    slot.root = std::move(immediate->node);
                } else {
                    FastPendingExpansion pending;
                    pending.sim_state = clone_game_state(slot.root_state);
                    pending.is_root_expansion = true;
                    slot.pending.push_back(std::move(pending));
                    const int batch_index = batch_inputs.filled;
                    batch_inputs.fill_slot(
                        batch_index,
                        slot.root_state.pub,
                        slot.root_state.hands[to_index(slot.root_state.pub.phasing)],
                        holds_china_for(slot.root_state, slot.root_state.pub.phasing),
                        slot.root_state.pub.phasing
                    );
                    batch_entries.push_back(BatchEntry{
                        .slot = &slot,
                        .pending_index = slot.pending.size() - 1,
                        .batch_index = batch_index,
                    });
                    continue;
                }
            }

            if (slot.sims_completed >= slot.sims_target && slot.pending.empty()) {
                slot.move_done = true;
                continue;
            }

            for (;;) {
                const int budget = sims_budget(slot, config.max_pending);
                if (budget <= 0) {
                    break;
                }
                const auto selection = select_to_leaf(slot, config);
                if (selection.needs_batch) {
                    auto& pending = slot.pending.back();
                    const int batch_index = batch_inputs.filled;
                    batch_inputs.fill_slot(
                        batch_index,
                        pending.sim_state.pub,
                        pending.sim_state.hands[to_index(pending.sim_state.pub.phasing)],
                        holds_china_for(pending.sim_state, pending.sim_state.pub.phasing),
                        pending.sim_state.pub.phasing
                    );
                    batch_entries.push_back(BatchEntry{
                        .slot = &slot,
                        .pending_index = slot.pending.size() - 1,
                        .batch_index = batch_index,
                    });
                } else {
                    slot.sims_completed += 1;
                    if (slot.sims_completed >= slot.sims_target && slot.pending.empty()) {
                        slot.move_done = true;
                        break;
                    }
                }
            }
        }
        result.t_select += std::chrono::duration<double>(Clock::now() - t0_sel).count();

        if (!batch_entries.empty()) {
            result.n_batches += 1;
            result.total_batch_items += static_cast<int64_t>(batch_entries.size());

            auto t0_nn = Clock::now();
            const auto outputs = forward_worker.run(model, batch_inputs);
            result.t_nn += std::chrono::duration<double>(Clock::now() - t0_nn).count();

            auto t0_exp = Clock::now();
            const auto raw = RawBatchOutputs::extract(outputs);
            std::vector<FastGameSlot*> touched_slots;
            touched_slots.reserve(batch_entries.size());
            FastGameSlot* last_touched = nullptr;

            for (const auto& entry : batch_entries) {
                if (entry.slot != last_touched) {
                    touched_slots.push_back(entry.slot);
                    last_touched = entry.slot;
                }
                auto& pending = entry.slot->pending[entry.pending_index];
                if (pending.is_root_expansion) {
                    auto expansion = expand_from_raw_flat(
                        pending.sim_state,
                        raw,
                        entry.batch_index,
                        config.mcts,
                        entry.slot->rng
                    );
                    entry.slot->root = std::move(expansion.node);
                        apply_root_dirichlet_noise_fast(*entry.slot->root, config.mcts, entry.slot->rng);
                    if (entry.slot->sims_target == 0) {
                        entry.slot->move_done = true;
                    }
                } else {
                    auto expansion = expand_from_raw_flat(
                        pending.sim_state,
                        raw,
                        entry.batch_index,
                        config.mcts,
                        entry.slot->rng
                    );
                    auto& [parent, edge_index] = pending.path.back();
                    if (parent->total_visits >= config.cache_visit_threshold) {
                        expansion.node->cached_state = std::make_unique<GameState>(pending.sim_state);
                    }
                    parent->children[static_cast<size_t>(edge_index)] = std::move(expansion.node);
                    backpropagate_path(pending, expansion.leaf_value, config.virtual_loss_weight);
                    entry.slot->sims_completed += 1;
                }
            }

            for (auto* slot : touched_slots) {
                slot->pending.clear();
                if (slot->sims_completed >= slot->sims_target && slot->pending.empty()) {
                    slot->move_done = true;
                }
            }
            result.t_expand += std::chrono::duration<double>(Clock::now() - t0_exp).count();
        }

        auto t0_commit = Clock::now();
        for (auto& slot : pool) {
            if (slot.active && slot.move_done) {
                commit_best_action(slot, config, result);
            }
        }
        result.t_commit += std::chrono::duration<double>(Clock::now() - t0_commit).count();
    }

    result.elapsed_s = std::chrono::duration<double>(Clock::now() - t_start).count();
    result.avg_batch = result.n_batches > 0
        ? static_cast<double>(result.total_batch_items) / static_cast<double>(result.n_batches)
        : 0.0;
    result.sims_per_s = result.elapsed_s > 0.0
        ? static_cast<double>(result.total_simulations) / result.elapsed_s
        : 0.0;
    return result;
}

}  // namespace ts::fastmcts

#endif
