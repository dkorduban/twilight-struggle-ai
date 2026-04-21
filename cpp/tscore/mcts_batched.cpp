// Wavefront-batched MCTS collection over a pool of concurrent games.

#include "mcts_batched.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <atomic>
#include <barrier>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <limits>
#include <map>
#include <cstdlib>
#include <sstream>
#include <stdexcept>
#include <thread>
#include <utility>
#include <vector>

#include <torch/torch.h>

#include "decode_helpers.hpp"
#include "game_data.hpp"
#include "game_loop.hpp"
#include "human_openings.hpp"
#include "mcts.hpp"
#include "nn_features.hpp"
#include "policies.hpp"
#include "policy_callback.hpp"
#include "rule_queries.hpp"
#include "scoring.hpp"
#include "search_common.hpp"
#include "step.hpp"

namespace ts {
namespace {

constexpr int kMidWarTurn = 4;
constexpr int kLateWarTurn = 8;
constexpr int kMaxTurns = 10;
// kSpaceShuttleArs is in search_common.hpp
constexpr int kMaxCardLogits = 112;
constexpr int kMaxModeLogits = 8;
constexpr int kMaxCountryLogits = 86;
constexpr int kMaxStrategies = 8;

// ---------------------------------------------------------------------------
// Compact tree storage (FastNode / FastEdge)
// FastEdge avoids per-edge ActionEncoding heap allocation by storing influence
// targets in a flat resolved_targets array on the node, indexed by offset/count.
// ---------------------------------------------------------------------------

struct FastEdge {
    CardId card_id = 0;
    ActionMode mode = ActionMode::Influence;
    CountryId country = static_cast<CountryId>(kMaxCountryLogits);  // for Coup/Realign; kMaxCountryLogits = no target
    int target_offset = 0;          // index into FastNode::resolved_targets
    int target_count = 0;           // number of influence targets
    float prior = 0.0f;
    int visit_count = 0;
    int virtual_loss = 0;
    double total_value = 0.0;
};

struct FastNode {
    std::vector<FastEdge> edges;
    std::vector<std::unique_ptr<FastNode>> children;
    std::vector<CountryId> resolved_targets;  // flat influence target storage
    int total_visits = 0;
    bool is_terminal = false;
    double terminal_value = 0.0;
    Side side_to_move = Side::USSR;
    std::unique_ptr<GameState> cached_state;
};

// Reconstruct a full ActionEncoding from a compact FastEdge.
ActionEncoding materialize_action(const FastNode& node, size_t edge_index) {
    const auto& edge = node.edges[edge_index];
    ActionEncoding action{edge.card_id, edge.mode, {}};
    if (edge.mode == ActionMode::Influence && edge.target_count > 0) {
        action.targets.reserve(static_cast<size_t>(edge.target_count));
        for (int i = 0; i < edge.target_count; ++i) {
            action.targets.push_back(
                node.resolved_targets[static_cast<size_t>(edge.target_offset + i)]);
        }
    } else if ((edge.mode == ActionMode::Coup || edge.mode == ActionMode::Realign) &&
               edge.country < static_cast<CountryId>(kMaxCountryLogits)) {
        action.targets.push_back(edge.country);
    }
    return action;
}

// Append an edge to a FastNode, storing influence targets in resolved_targets.
void append_compact_edge(FastNode& node, const ActionEncoding& action, float prior) {
    int target_offset = 0;
    int target_count = 0;
    CountryId country = static_cast<CountryId>(kMaxCountryLogits);
    if (action.mode == ActionMode::Influence && !action.targets.empty()) {
        target_offset = static_cast<int>(node.resolved_targets.size());
        target_count = static_cast<int>(action.targets.size());
        node.resolved_targets.insert(
            node.resolved_targets.end(), action.targets.begin(), action.targets.end());
    } else if ((action.mode == ActionMode::Coup || action.mode == ActionMode::Realign) &&
               !action.targets.empty()) {
        country = action.targets.front();
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
}

void sort_edges_by_prior_desc(FastNode& node) {
    if (node.edges.size() < 2) {
        return;
    }

    std::vector<size_t> order(node.edges.size(), 0);
    for (size_t i = 0; i < order.size(); ++i) {
        order[i] = i;
    }
    std::stable_sort(order.begin(), order.end(),
        [&node](size_t lhs, size_t rhs) {
            return node.edges[lhs].prior > node.edges[rhs].prior;
        });

    std::vector<FastEdge> sorted_edges;
    sorted_edges.reserve(node.edges.size());
    std::vector<std::unique_ptr<FastNode>> sorted_children;
    sorted_children.reserve(node.children.size());
    for (const size_t index : order) {
        sorted_edges.push_back(std::move(node.edges[index]));
        sorted_children.push_back(std::move(node.children[index]));
    }

    node.edges = std::move(sorted_edges);
    node.children = std::move(sorted_children);
}

void renormalize_edge_priors(FastNode& node) {
    if (node.edges.empty()) {
        return;
    }

    float sum = 0.0f;
    for (const auto& edge : node.edges) {
        sum += edge.prior;
    }
    if (sum > 0.0f) {
        const float inv_sum = 1.0f / sum;
        for (auto& edge : node.edges) {
            edge.prior *= inv_sum;
        }
        return;
    }

    const auto uniform = 1.0f / static_cast<float>(node.edges.size());
    for (auto& edge : node.edges) {
        edge.prior = uniform;
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
        root.edges[i].prior = static_cast<float>(
            keep * static_cast<double>(root.edges[i].prior) + epsilon * noise[i]);
    }
    sort_edges_by_prior_desc(root);
}

// ---------------------------------------------------------------------------
// Internal game pool types (not part of public API)
// ---------------------------------------------------------------------------

struct PendingExpansion {
    std::vector<std::pair<FastNode*, int>> path;
    GameState sim_state;
    bool is_root_expansion = false;
};

struct GameSlot {
    GameState root_state;
    std::unique_ptr<FastNode> root;
    std::vector<PendingExpansion> pending;
    bool record_history = true;
    int sims_completed = 0;
    int sims_target = 0;
    bool move_done = false;
    bool game_done = false;
    bool emitted = false;
    bool active = false;
    Pcg64Rng rng;

    int game_index = -1;
    std::string game_id;
    std::vector<StepTrace> traces;
    std::vector<SearchResult> search_results;
    GameResult result;

    BatchedGameStage stage = BatchedGameStage::TurnSetup;
    int turn = 1;
    int total_ars = 0;
    int current_ar = 0;
    int decisions_started = 0;
    Side current_side = Side::USSR;
    std::array<std::optional<PendingHeadlineChoice>, 2> pending_headlines = {};
    std::vector<PendingHeadlineChoice> headline_order;
    size_t headline_order_index = 0;
    std::optional<PendingDecision> decision;
    // Saved RNG state before MCTS search starts, used in heuristic_teacher_mode to
    // restore the game RNG so heuristic move selection is identical to pure heuristic.
    std::optional<Pcg64Rng> rng_before_mcts;
    // Per-game heuristic temperature (0 = deterministic argmax).
    float heuristic_temperature = 0.0f;
};

struct ExpansionResult {
    std::unique_ptr<FastNode> node;
    double leaf_value = 0.0;
};

struct SelectionResult {
    bool needs_batch = false;
    double leaf_value = 0.0;
};

class PhaseBarrier {
public:
    explicit PhaseBarrier(int n_threads)
        : barrier_(std::max(1, n_threads)) {}

    void wait() {
        barrier_.arrive_and_wait();
    }

private:
    std::barrier<> barrier_;
};

struct CommitPolicyTrace;

PolicyCallbackFn make_commit_policy_callback(
    torch::jit::script::Module& model,
    torch::Device device,
    GameSlot& slot,
    const ActionEncoding& action,
    const torch::Tensor& small_choice_logits,
    CommitPolicyTrace* trace
);

Observation pending_observation(const PendingDecision& decision) {
    Observation obs;
    obs.pub = decision.pub_snapshot;
    obs.own_hand = decision.hand_snapshot;
    obs.holds_china = decision.holds_china;
    // PendingDecision snapshots do not retain opponent hand size; the batched
    // read-only helpers below only consume the actor-visible fields.
    obs.opp_hand_size = 0;
    obs.acting_side = decision.side;
    return obs;
}

DecisionFrame frame_context_from_event_decision(const EventDecision& decision) {
    DecisionFrame frame;
    frame.source_card = decision.source_card;
    frame.acting_side = decision.acting_side;
    frame.eligible_n = static_cast<uint8_t>(std::min(decision.n_options, 255));
    switch (decision.kind) {
        case DecisionKind::SmallChoice:
            frame.kind = FrameKind::SmallChoice;
            break;
        case DecisionKind::CountrySelect:
            frame.kind = FrameKind::CountryPick;
            for (int i = 0; i < decision.n_options; ++i) {
                frame.eligible_countries.set(static_cast<size_t>(decision.eligible_ids[i]));
            }
            break;
        case DecisionKind::CardSelect:
            frame.kind = FrameKind::CardSelect;
            for (int i = 0; i < decision.n_options; ++i) {
                frame.eligible_cards.set(static_cast<size_t>(decision.eligible_ids[i]));
            }
            break;
    }
    return frame;
}

// Write a single batch slot without touching any shared counters.
// Each thread writes to its own disjoint slice of the batch buffer.
void fill_batch_slot_no_count(nn::BatchInputs& batch_inputs, int idx, const Observation& obs) {
    batch_inputs.fill_slot_no_count(idx, obs);
}

void compact_batch_tensor_rows(torch::Tensor& tensor, int src_row, int dst_row, int count) {
    if (count <= 0 || src_row == dst_row) {
        return;
    }
    const auto row_width = static_cast<size_t>(tensor.size(1));
    float* data = tensor.data_ptr<float>();
    std::memmove(
        data + (static_cast<size_t>(dst_row) * row_width),
        data + (static_cast<size_t>(src_row) * row_width),
        static_cast<size_t>(count) * row_width * sizeof(float)
    );
}

void compact_batch_inputs(nn::BatchInputs& batch_inputs, int src_row, int dst_row, int count) {
    compact_batch_tensor_rows(batch_inputs.influence, src_row, dst_row, count);
    compact_batch_tensor_rows(batch_inputs.cards, src_row, dst_row, count);
    compact_batch_tensor_rows(batch_inputs.scalars, src_row, dst_row, count);
}

struct AggregatedVisitCount {
    CardId card_id = 0;
    ActionMode mode = ActionMode::Influence;
    int visits = 0;
};

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

DraftsResult collect_card_drafts_cached(const Observation& obs) {
    const auto side = obs.acting_side;
    const auto& pub = obs.pub;
    auto cache = AccessibleCache::build(side, pub);

    auto cards = collect_drafts_from_legal_cards(
        obs.own_hand,
        pub,
        side,
        obs.holds_china,
        [&](CardDraft& card, CardId card_id) {
            const auto& spec = card_spec(card_id);

            if (spec.ops > 0) {
                if (!cache.influence.empty()) {
                    append_single_edge_mode_draft(card, card_id, ActionMode::Influence);
                }

                if (pub.defcon > 2) {
                    append_country_target_mode_draft(card, card_id, ActionMode::Coup, cache.coup);
                }
                append_country_target_mode_draft(card, card_id, ActionMode::Realign, cache.realign);

                if (cache.can_space && spec.ops >= cache.space_ops_min) {
                    if (!is_trap_blocked(pub, side, card_id)) {
                        append_single_edge_mode_draft(card, card_id, ActionMode::Space);
                    }
                }
            }

            if (is_event_play_allowed(pub, side, card_id)) {
                append_single_edge_mode_draft(card, card_id, ActionMode::Event);
            }
        }
    );

    return DraftsResult{.drafts = std::move(cards), .cache = std::move(cache)};
}

// ---------------------------------------------------------------------------
// Compact legal card representation — boolean mode flags, no ActionEncoding
// allocations. Used by expand_from_raw_fast for the default K=1 path.
// ---------------------------------------------------------------------------

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

CompactLegalCardsResult collect_compact_legal_cards(const Observation& obs) {
    const auto side = obs.acting_side;
    const auto& pub = obs.pub;
    auto cache = AccessibleCache::build(side, pub);

    std::vector<LegalCardInfo> cards;
    cards.reserve(10);

    for (const auto card_id : legal_cards(obs.own_hand, pub, side, obs.holds_china)) {
        if (is_card_blocked_by_defcon(pub, side, card_id)) {
            continue;
        }

        const auto& spec = card_spec(card_id);
        const int ops = effective_ops(card_id, pub, side);
        const bool trapped = is_trap_blocked(pub, side, card_id);

        LegalCardInfo card{
            .card_id = card_id,
            .ops = ops,
            .has_influence = spec.ops > 0 && !cache.influence.empty(),
            .has_coup = spec.ops > 0 && !cache.coup.empty() && pub.defcon > 2,
            .has_realign = spec.ops > 0 && !cache.realign.empty(),
            .has_space = spec.ops > 0 && cache.can_space && spec.ops >= cache.space_ops_min && !trapped,
            .has_event = false,
        };

        card.has_event = is_event_play_allowed(pub, side, card_id);

        if (card.has_influence || card.has_coup || card.has_realign || card.has_space || card.has_event) {
            cards.push_back(card);
        }
    }

    return CompactLegalCardsResult{.cards = std::move(cards), .cache = std::move(cache)};
}

// Pre-counts exact number of edges for a given compact legal set so the node's
// edge/child/resolved_targets vectors can be reserved precisely (no reallocations).
int exact_edge_count(const CompactLegalCardsResult& legal) {
    const int coup_count = static_cast<int>(legal.cache.coup.size());
    int total = 0;
    for (const auto& card : legal.cards) {
        total += card.has_influence ? 1 : 0;
        total += card.has_coup ? coup_count : 0;
        total += card.has_realign ? coup_count : 0;  // realign uses same country set as coup
        total += card.has_space ? 1 : 0;
        total += card.has_event ? 1 : 0;
    }
    return total;
}

// Pre-extracted raw pointers from batch outputs for zero-copy per-item access.
struct RawBatchOutputs {
    // Storage tensors keep the contiguous data alive across barriers.
    torch::Tensor card_logits_storage;
    const float* card_logits = nullptr;  // [batch, n_card]
    int n_card = 0;
    int card_stride = 0;

    torch::Tensor mode_logits_storage;
    const float* mode_logits = nullptr;  // [batch, n_mode]
    int n_mode = 0;
    int mode_stride = 0;

    torch::Tensor country_logits_storage;
    const float* country_logits = nullptr;  // [batch, n_country]
    int n_country = 0;
    int country_stride = 0;

    torch::Tensor strategy_logits_storage;
    const float* strategy_logits = nullptr;  // [batch, n_strategy]
    int n_strategy = 0;
    int strategy_stride = 0;

    torch::Tensor country_strategy_logits_storage;
    const float* country_strategy_logits = nullptr;  // [batch, n_strat, n_country]
    int cs_n_strategies = 0;
    int cs_n_countries = 0;
    int cs_batch_stride = 0;  // stride between batch items

    torch::Tensor value_storage;
    const float* value = nullptr;  // [batch, 1]
    int value_stride = 0;

    static RawBatchOutputs extract(const nn::BatchOutputs& outputs) {
        RawBatchOutputs raw;
        raw.card_logits_storage = outputs.card_logits.contiguous();
        raw.card_logits = raw.card_logits_storage.data_ptr<float>();
        raw.n_card = std::min(static_cast<int>(raw.card_logits_storage.size(1)), kMaxCardLogits);
        raw.card_stride = static_cast<int>(raw.card_logits_storage.stride(0));

        raw.mode_logits_storage = outputs.mode_logits.contiguous();
        raw.mode_logits = raw.mode_logits_storage.data_ptr<float>();
        raw.n_mode = std::min(static_cast<int>(raw.mode_logits_storage.size(1)), kMaxModeLogits);
        raw.mode_stride = static_cast<int>(raw.mode_logits_storage.stride(0));

        if (outputs.country_logits.defined()) {
            raw.country_logits_storage = outputs.country_logits.contiguous();
            raw.country_logits = raw.country_logits_storage.data_ptr<float>();
            raw.n_country = std::min(static_cast<int>(raw.country_logits_storage.size(1)), kMaxCountryLogits);
            raw.country_stride = static_cast<int>(raw.country_logits_storage.stride(0));
        }
        if (outputs.strategy_logits.defined()) {
            raw.strategy_logits_storage = outputs.strategy_logits.contiguous();
            raw.strategy_logits = raw.strategy_logits_storage.data_ptr<float>();
            raw.n_strategy = std::min(static_cast<int>(raw.strategy_logits_storage.size(1)), kMaxStrategies);
            raw.strategy_stride = static_cast<int>(raw.strategy_logits_storage.stride(0));
        }
        if (outputs.country_strategy_logits.defined()) {
            raw.country_strategy_logits_storage = outputs.country_strategy_logits.contiguous();
            raw.country_strategy_logits = raw.country_strategy_logits_storage.data_ptr<float>();
            raw.cs_n_strategies = static_cast<int>(raw.country_strategy_logits_storage.size(1));
            raw.cs_n_countries = static_cast<int>(raw.country_strategy_logits_storage.size(2));
            raw.cs_batch_stride = static_cast<int>(raw.country_strategy_logits_storage.stride(0));
        }
        raw.value_storage = outputs.value.contiguous();
        raw.value = raw.value_storage.data_ptr<float>();
        raw.value_stride = static_cast<int>(raw.value_storage.stride(0));

        return raw;
    }
};

// ---------------------------------------------------------------------------
// K-sample influence allocation helpers
// ---------------------------------------------------------------------------

// Zobrist hash table for order-invariant deduplication of influence allocations.
// hash(allocation) = sum over all placed ops of kInfluenceZobrist[country_id].
// Initialized from a fixed seed unrelated to the game RNG.
static const std::array<uint64_t, 86> kInfluenceZobrist = []() {
    std::array<uint64_t, 86> table{};
    Pcg64Rng zobrist_rng(0xDEADBEEF42ULL);
    for (int i = 0; i < 86; ++i) {
        table[static_cast<size_t>(i)] = zobrist_rng.next_u64();
    }
    return table;
}();

struct AllocationResult {
    std::vector<CountryId> targets;
    uint64_t hash;
};

// Proportional allocation: floor(p * ops) for each country, then distribute
// remainder by largest fractional part. Targets sorted by country id.
AllocationResult proportional_allocation(
    const float* probs,              // softmaxed country probs, indexed by CountryId
    const std::vector<CountryId>& accessible,
    int ops,
    int /*n_country*/
) {
    const int n_acc = static_cast<int>(accessible.size());
    int alloc_i[kMaxCountryLogits] = {};
    float alloc_f[kMaxCountryLogits] = {};
    int floor_sum = 0;
    for (int i = 0; i < n_acc; ++i) {
        float p = probs[static_cast<int>(accessible[static_cast<size_t>(i)])];
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
    // Build targets sorted by country id, compute Zobrist hash
    uint64_t hash = 0;
    std::vector<CountryId> targets;
    targets.reserve(static_cast<size_t>(ops));
    for (int i = 0; i < n_acc; ++i) {
        if (alloc_i[i] > 0) {
            const CountryId cid = accessible[static_cast<size_t>(i)];
            const int cid_int = static_cast<int>(cid);
            for (int j = 0; j < alloc_i[i]; ++j) {
                targets.push_back(cid);
            }
            hash += static_cast<uint64_t>(alloc_i[i]) *
                    kInfluenceZobrist[static_cast<size_t>(cid_int)];
        }
    }
    // targets already in country-id order since we iterate accessible in order
    return AllocationResult{std::move(targets), hash};
}

// Compact variant of proportional_allocation: probs[i] is the softmaxed probability
// for accessible[i] (position-indexed, not CountryId-indexed). Only returns targets;
// hash is not needed for the non-K-sample path.
std::vector<CountryId> proportional_allocation_compact(
    const float* compact_probs,
    const std::vector<CountryId>& accessible,
    int ops
) {
    const int n_acc = static_cast<int>(accessible.size());
    int alloc_i[kMaxCountryLogits] = {};
    float alloc_f[kMaxCountryLogits] = {};
    int floor_sum = 0;
    for (int i = 0; i < n_acc; ++i) {
        alloc_f[i] = compact_probs[i] * static_cast<float>(ops);
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
    std::vector<CountryId> targets;
    targets.reserve(static_cast<size_t>(ops));
    for (int i = 0; i < n_acc; ++i) {
        for (int j = 0; j < alloc_i[i]; ++j) {
            targets.push_back(accessible[static_cast<size_t>(i)]);
        }
    }
    return targets;
}

// Categorical sample: draw from discrete distribution with given probs (must sum to 1).
int categorical_sample(const float* probs, int n, Pcg64Rng& rng) {
    const double u = static_cast<double>(rng.next_u32()) / 4294967296.0;
    double cum = 0.0;
    for (int i = 0; i < n - 1; ++i) {
        cum += static_cast<double>(probs[i]);
        if (u < cum) return i;
    }
    return n - 1;
}

// Multinomial sample: draw ops samples from temperature-scaled distribution.
// temperature > 0; probs[c] = softmaxed probability for accessible countries.
AllocationResult multinomial_sample(
    const float* probs,                       // softmaxed probs indexed by CountryId
    const std::vector<CountryId>& accessible,
    int ops,
    int /*n_country*/,
    float temperature,
    Pcg64Rng& rng
) {
    const int n_acc = static_cast<int>(accessible.size());
    // Temperature-scale probs and renormalize
    float scaled[kMaxCountryLogits] = {};
    float total = 0.0f;
    const float inv_T = 1.0f / temperature;
    for (int i = 0; i < n_acc; ++i) {
        float p = probs[static_cast<int>(accessible[static_cast<size_t>(i)])];
        float sp = (p > 0.0f) ? std::pow(p, inv_T) : 0.0f;
        scaled[i] = sp;
        total += sp;
    }
    if (total > 0.0f) {
        for (int i = 0; i < n_acc; ++i) scaled[i] /= total;
    } else {
        const float unif = 1.0f / static_cast<float>(n_acc);
        for (int i = 0; i < n_acc; ++i) scaled[i] = unif;
    }
    // Build CDF and sample ops times
    int counts[kMaxCountryLogits] = {};
    for (int op = 0; op < ops; ++op) {
        const double u = static_cast<double>(rng.next_u32()) / 4294967296.0;
        double cum = 0.0;
        int chosen = n_acc - 1;
        for (int i = 0; i < n_acc - 1; ++i) {
            cum += static_cast<double>(scaled[i]);
            if (u < cum) { chosen = i; break; }
        }
        counts[chosen]++;
    }
    // Build targets sorted by country id, compute Zobrist hash
    uint64_t hash = 0;
    std::vector<CountryId> targets;
    targets.reserve(static_cast<size_t>(ops));
    for (int i = 0; i < n_acc; ++i) {
        if (counts[i] > 0) {
            const CountryId cid = accessible[static_cast<size_t>(i)];
            const int cid_int = static_cast<int>(cid);
            for (int j = 0; j < counts[i]; ++j) {
                targets.push_back(cid);
            }
            hash += static_cast<uint64_t>(counts[i]) *
                    kInfluenceZobrist[static_cast<size_t>(cid_int)];
        }
    }
    return AllocationResult{std::move(targets), hash};
}

// Multinomial probability: ops! / prod(count_i!) * prod(p_i^count_i)
// computed in log-space. p_i from RAW (unscaled) country_probs.
double multinomial_probability(
    const std::vector<CountryId>& targets,
    const float* strategy_probs,   // softmaxed probs indexed by CountryId
    const std::vector<CountryId>& accessible,
    int ops,
    int /*n_country*/
) {
    // Lookup table for log(k!) for k = 0..ops (max ops = 5 → 120)
    static const double log_factorial[6] = {
        0.0,                    // 0!
        0.0,                    // 1!
        0.6931471805599453,     // 2!
        1.791759469228327,      // 3!
        3.1780538303479458,     // 4!
        4.787491742782046       // 5!
    };

    // Count ops per accessible country
    const int n_acc = static_cast<int>(accessible.size());
    int counts[kMaxCountryLogits] = {};
    for (const auto& cid : targets) {
        // Find index in accessible
        for (int i = 0; i < n_acc; ++i) {
            if (accessible[static_cast<size_t>(i)] == cid) {
                counts[i]++;
                break;
            }
        }
    }

    // Re-normalize strategy_probs over accessible countries
    float acc_probs[kMaxCountryLogits] = {};
    float acc_total = 0.0f;
    for (int i = 0; i < n_acc; ++i) {
        float p = strategy_probs[static_cast<int>(accessible[static_cast<size_t>(i)])];
        acc_probs[i] = p;
        acc_total += p;
    }
    if (acc_total > 0.0f) {
        for (int i = 0; i < n_acc; ++i) acc_probs[i] /= acc_total;
    }

    // log density = log(ops!) - sum(log(count_i!)) + sum(count_i * log(p_i))
    const int bounded_ops = std::min(ops, 5);
    double log_density = log_factorial[bounded_ops];
    for (int i = 0; i < n_acc; ++i) {
        if (counts[i] > 0) {
            const int bk = std::min(counts[i], 5);
            log_density -= log_factorial[bk];
            if (acc_probs[i] > 0.0f) {
                log_density += static_cast<double>(counts[i]) *
                               std::log(static_cast<double>(acc_probs[i]));
            } else {
                return 0.0;  // zero probability placement
            }
        }
    }
    return std::exp(log_density);
}

// ---------------------------------------------------------------------------
// Expand sub-phase accumulators (for profiling)
// ---------------------------------------------------------------------------
static thread_local double g_expand_drafts = 0, g_expand_edges = 0, g_expand_alloc = 0;
static thread_local int g_expand_count = 0;
static thread_local int g_expand_total_edges = 0;  // total edges created across all expansions
static thread_local double g_ksample_time = 0;
static thread_local int g_ksample_count = 0;
static thread_local int g_ksample_edges_total = 0;
// Mode composition counters
static thread_local int g_mode_influence = 0;
static thread_local int g_mode_coup = 0;
static thread_local int g_mode_realign = 0;
static thread_local int g_mode_space = 0;
static thread_local int g_mode_event = 0;
static thread_local int g_mode_other = 0;

// Edge utilization: per-node fraction of edges with visits > 0
// We bin into 10 buckets: [0%, 10%), [10%, 20%), ..., [90%, 100%], plus a 100% exact bucket.
static thread_local int g_edge_util_histogram[11] = {};  // [0..9] = 0-90%, [10] = 100%
static thread_local int g_edge_util_nodes = 0;

void collect_tree_edge_utilization(const FastNode* node) {
    if (!node || node->edges.empty()) return;
    int visited = 0;
    for (const auto& e : node->edges) {
        if (e.visit_count > 0) ++visited;
    }
    const double frac = static_cast<double>(visited) / static_cast<double>(node->edges.size());
    int bucket = static_cast<int>(frac * 10.0);
    if (bucket >= 11) bucket = 10;
    if (visited == static_cast<int>(node->edges.size())) bucket = 10;  // 100% exact
    g_edge_util_histogram[bucket]++;
    g_edge_util_nodes++;
    // Recurse into children
    for (const auto& child : node->children) {
        if (child) collect_tree_edge_utilization(child.get());
    }
}

ExpansionResult expand_from_raw(
    const GameState& state,
    const RawBatchOutputs& raw,
    int batch_index,
    const BatchedMctsConfig& config,
    Pcg64Rng& rng
) {
    using XClock = std::chrono::high_resolution_clock;
    auto xt0 = XClock::now();

    auto node = std::make_unique<FastNode>();
    node->side_to_move = state.pub.phasing;
    node->edges.reserve(64);
    node->children.reserve(64);
    node->resolved_targets.reserve(128);

    g_expand_alloc += std::chrono::duration<double>(XClock::now() - xt0).count();
    auto xt1 = XClock::now();

    const auto obs = make_observation(state, state.pub.phasing);
    auto [drafts, cache] = collect_card_drafts_cached(obs);

    g_expand_drafts += std::chrono::duration<double>(XClock::now() - xt1).count();
    auto xt2 = XClock::now();
    (void)xt2;  // used at function end
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
        // Pick best strategy via argmax
        const float* sl = raw.strategy_logits + batch_index * raw.strategy_stride;
        int best_strat = 0;
        float best_val = sl[0];
        for (int s = 1; s < raw.n_strategy; ++s) {
            if (sl[s] > best_val) { best_val = sl[s]; best_strat = s; }
        }
        // Copy that strategy's country logits (raw logits, not probabilities)
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

    // Apply per-head prior temperature scaling to logits before softmax.
    // T<1 sharpens, T>1 flattens, 1.0 = identity.
    if (config.prior_t_card != 1.0f && config.prior_t_card > 0.0f) {
        const float inv_t = 1.0f / config.prior_t_card;
        for (int i = 0; i < n_card; ++i) card_logits_arr[i] *= inv_t;
    }
    if (config.prior_t_mode != 1.0f && config.prior_t_mode > 0.0f) {
        const float inv_t = 1.0f / config.prior_t_mode;
        for (int i = 0; i < n_mode; ++i) mode_logits_arr[i] *= inv_t;
    }
    if (country_logits_ptr != nullptr && config.prior_t_country != 1.0f && config.prior_t_country > 0.0f) {
        const float inv_t = 1.0f / config.prior_t_country;
        for (int i = 0; i < n_country; ++i) country_logits_arr[i] *= inv_t;
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
    const bool use_ksample = country_logits_ptr != nullptr &&
        !cache.influence.empty() &&
        (config.influence_samples > 1 ||
         config.influence_t_strategy > 0.0f ||
         config.influence_t_country > 0.0f);

    int ksample_effective_n_strat = 0;
    float ksample_country_probs_all[kMaxStrategies][kMaxCountryLogits] = {};
    float ksample_strategy_logits_buf[kMaxStrategies] = {};
    float ksample_strategy_probs[kMaxStrategies] = {};
    if (use_ksample) {
        const int n_strat = (raw.strategy_logits != nullptr &&
                             raw.country_strategy_logits != nullptr &&
                             raw.cs_n_strategies > 0)
                            ? std::min(raw.cs_n_strategies, kMaxStrategies)
                            : 0;

        if (n_strat > 0) {
            for (int s = 0; s < n_strat; ++s) {
                const float* cs_row = raw.country_strategy_logits +
                    batch_index * raw.cs_batch_stride +
                    s * raw.cs_n_countries;
                float masked[kMaxCountryLogits];
                std::fill(masked, masked + n_country, -std::numeric_limits<float>::infinity());
                for (const auto cid : cache.influence) {
                    const int idx = static_cast<int>(cid);
                    if (idx < n_country && idx < raw.cs_n_countries) {
                        masked[idx] = cs_row[idx];
                    }
                }
                softmax_inplace(masked, n_country);
                std::memcpy(ksample_country_probs_all[s], masked,
                            static_cast<size_t>(n_country) * sizeof(float));
            }
        } else {
            float masked[kMaxCountryLogits];
            std::fill(masked, masked + n_country, -std::numeric_limits<float>::infinity());
            for (const auto cid : cache.influence) {
                const int idx = static_cast<int>(cid);
                if (idx < n_country) {
                    masked[idx] = country_logits_arr[idx];
                }
            }
            softmax_inplace(masked, n_country);
            std::memcpy(ksample_country_probs_all[0], masked,
                        static_cast<size_t>(n_country) * sizeof(float));
        }

        ksample_effective_n_strat = (n_strat > 0) ? n_strat : 1;
        if (raw.strategy_logits != nullptr && n_strat > 0) {
            std::memcpy(ksample_strategy_logits_buf,
                        raw.strategy_logits + batch_index * raw.strategy_stride,
                        static_cast<size_t>(ksample_effective_n_strat) * sizeof(float));
        }
        std::memcpy(ksample_strategy_probs, ksample_strategy_logits_buf,
                    static_cast<size_t>(ksample_effective_n_strat) * sizeof(float));
        softmax_inplace(ksample_strategy_probs, ksample_effective_n_strat);
    }

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
                    append_compact_edge(*node, edge, static_cast<float>(prior));
                    total_prior += prior;
                }
                continue;
            }

            const auto per_edge_prior = card_prob * mode_prob;
            for (const auto& edge : mode.edges) {
                // Resolve influence allocation using cached accessible countries
                if (edge.mode == ActionMode::Influence && country_logits_ptr != nullptr && !cache.influence.empty()) {
                    const auto ops = effective_ops(edge.card_id, state.pub, state.pub.phasing);

                    // Guard: use new K-sample path only when knobs are non-default.
                    // At T_s=0, T_c=0, K=1: skip entirely → bit-identical to old code.
                    if (use_ksample) {

                        // --- K-sample influence allocation path ---
                        auto ks_t0 = std::chrono::high_resolution_clock::now();
                        const size_t edges_before = node->edges.size();
                        // Bootstrap local RNG: main RNG advances by exactly 1 regardless of K.
                        Pcg64Rng local_rng(rng.next_u64());

                        const float T_s = config.influence_t_strategy;
                        const float T_c = config.influence_t_country;
                        const bool prop_first = config.influence_proportional_first;
                        const int K = config.influence_samples;

                        // Track which strategies have produced a proportional allocation
                        bool strategy_has_proportional[kMaxStrategies] = {};

                        // Helper: pick a strategy index
                        auto pick_strategy = [&]() -> int {
                            if (T_s == 0.0f) {
                                // argmax
                                int best = 0;
                                for (int s = 1; s < ksample_effective_n_strat; ++s) {
                                    if (ksample_strategy_logits_buf[s] > ksample_strategy_logits_buf[best]) best = s;
                                }
                                return best;
                            }
                            float temp_logits[kMaxStrategies];
                            for (int s = 0; s < ksample_effective_n_strat; ++s) {
                                temp_logits[s] = ksample_strategy_logits_buf[s] / T_s;
                            }
                            softmax_inplace(temp_logits, ksample_effective_n_strat);
                            return categorical_sample(temp_logits, ksample_effective_n_strat, local_rng);
                        };

                        // Helper: generate one allocation for a given strategy
                        auto make_allocation = [&](int strat) -> AllocationResult {
                            bool use_proportional = (T_c == 0.0f) ||
                                                    (prop_first && !strategy_has_proportional[strat]);
                            if (use_proportional) {
                                strategy_has_proportional[strat] = true;
                                return proportional_allocation(
                                    ksample_country_probs_all[strat], cache.influence, ops, n_country);
                            }
                            return multinomial_sample(
                                ksample_country_probs_all[strat], cache.influence, ops, n_country, T_c, local_rng);
                        };

                        // Helper: compute model density for placement (marginalize over strategies)
                        auto compute_density = [&](const std::vector<CountryId>& tgts) -> double {
                            double density = 0.0;
                            for (int s = 0; s < ksample_effective_n_strat; ++s) {
                                density += static_cast<double>(ksample_strategy_probs[s]) *
                                    multinomial_probability(tgts, ksample_country_probs_all[s],
                                                           cache.influence, ops, n_country);
                            }
                            return density;
                        };

                        // --- Generate K allocations with dedup ---
                        struct InfluenceAlloc {
                            ActionEncoding action;
                            double density;
                            uint64_t hash;
                        };
                        std::vector<InfluenceAlloc> allocations;
                        allocations.reserve(static_cast<size_t>(K));

                        auto try_add = [&](AllocationResult&& ar) -> bool {
                            for (const auto& alloc : allocations) {
                                if (alloc.hash == ar.hash) {
                                    return false;
                                }
                            }
                            double dens = compute_density(ar.targets);
                            ActionEncoding act{edge.card_id, ActionMode::Influence, std::move(ar.targets)};
                            allocations.push_back(InfluenceAlloc{std::move(act), dens, ar.hash});
                            return true;
                        };

                        if (T_s == 0.0f && T_c == 0.0f) {
                            // All-deterministic fast path:
                            // Edge 0: argmax strategy proportional
                            int best_s = pick_strategy();
                            try_add(make_allocation(best_s));

                            // Per-strategy proportional for remaining strategies
                            for (int s = 0; s < ksample_effective_n_strat &&
                                 static_cast<int>(allocations.size()) < K; ++s) {
                                if (s == best_s) continue;
                                try_add(make_allocation(s));
                            }

                            // Fill remainder with T_c=1.0 multinomial
                            const int max_retries = 3 * K;
                            int retries = 0;
                            while (static_cast<int>(allocations.size()) < K && retries++ < max_retries) {
                                float uniform_logits[kMaxStrategies];
                                std::memcpy(uniform_logits, ksample_strategy_logits_buf,
                                            static_cast<size_t>(ksample_effective_n_strat) * sizeof(float));
                                softmax_inplace(uniform_logits, ksample_effective_n_strat);
                                int s = categorical_sample(uniform_logits, ksample_effective_n_strat, local_rng);
                                auto ar = multinomial_sample(ksample_country_probs_all[s], cache.influence,
                                                             ops, n_country, 1.0f, local_rng);
                                try_add(std::move(ar));
                            }
                        } else {
                            // General path (at least one T > 0)
                            const int max_retries = 3 * K;
                            int retries = 0;
                            while (static_cast<int>(allocations.size()) < K && retries++ < max_retries) {
                                int s = pick_strategy();
                                auto ar = make_allocation(s);
                                try_add(std::move(ar));
                            }
                        }

                        // Fallback: if no allocations generated, use single proportional
                        if (allocations.empty()) {
                            int best_s = 0;
                            for (int s = 1; s < ksample_effective_n_strat; ++s) {
                                if (ksample_strategy_logits_buf[s] > ksample_strategy_logits_buf[best_s]) best_s = s;
                            }
                            auto ar = proportional_allocation(
                                ksample_country_probs_all[best_s], cache.influence, ops, n_country);
                            double dens = compute_density(ar.targets);
                            ActionEncoding act{edge.card_id, ActionMode::Influence, std::move(ar.targets)};
                            allocations.push_back(InfluenceAlloc{std::move(act), dens, ar.hash});
                        }

                        // Normalize densities and add edges
                        double density_sum = 0.0;
                        for (const auto& alloc : allocations) density_sum += alloc.density;

                        const double influence_total_prior = card_prob * mode_prob;
                        for (auto& alloc : allocations) {
                            double norm_prior = (density_sum > 0.0)
                                ? influence_total_prior * alloc.density / density_sum
                                : influence_total_prior / static_cast<double>(allocations.size());

                            // Use alloc.action (resolved targets), not the template edge.
                            append_compact_edge(*node, alloc.action, static_cast<float>(norm_prior));
                            total_prior += norm_prior;
                        }

                        g_ksample_time += std::chrono::duration<double>(
                            std::chrono::high_resolution_clock::now() - ks_t0).count();
                        g_ksample_count++;
                        g_ksample_edges_total += static_cast<int>(node->edges.size() - edges_before);

                    } else {
                        // --- Original single-allocation path (bit-identical at defaults) ---
                        float masked[kMaxCountryLogits];
                        std::fill(masked, masked + n_country, -std::numeric_limits<float>::infinity());
                        for (const auto cid : cache.influence) {
                            const int idx = static_cast<int>(cid);
                            if (idx < n_country) masked[idx] = country_logits_arr[idx];
                        }
                        softmax_inplace(masked, n_country);
                        auto resolved = proportional_allocation(masked, cache.influence, ops, n_country);
                        ActionEncoding act{edge.card_id, edge.mode, std::move(resolved.targets)};
                        append_compact_edge(*node, act, static_cast<float>(per_edge_prior));
                        total_prior += per_edge_prior;
                    }
                } else {
                    // Non-influence edge (or no country logits)
                    append_compact_edge(*node, edge, static_cast<float>(per_edge_prior));
                    total_prior += per_edge_prior;
                }
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
            append_compact_edge(*node, *fallback, 1.0f);
            return ExpansionResult{
                .node = std::move(node),
                .leaf_value = evaluate_leaf_value_raw(state, raw.value, raw.value_stride, batch_index, config.mcts, rng),
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

    g_expand_edges += std::chrono::duration<double>(XClock::now() - xt2).count();
    ++g_expand_count;
    g_expand_total_edges += static_cast<int>(node->edges.size());
    // Count mode composition
    for (const auto& e : node->edges) {
        switch (e.mode) {
            case ActionMode::Influence: ++g_mode_influence; break;
            case ActionMode::Coup:      ++g_mode_coup; break;
            case ActionMode::Realign: ++g_mode_realign; break;
            case ActionMode::Space:     ++g_mode_space; break;
            case ActionMode::Event:     ++g_mode_event; break;
            default:                    ++g_mode_other; break;
        }
    }

    return ExpansionResult{
        .node = std::move(node),
        .leaf_value = evaluate_leaf_value_raw(state, raw.value, raw.value_stride, batch_index, config.mcts, rng),
    };
}

// Fast expansion path using compact legal card representation.
// Avoids per-card/per-mode ActionEncoding vector allocations and uses compact
// softmax (only over legal items). Falls back to expand_from_raw for K-sample.
ExpansionResult expand_from_raw_fast(
    const GameState& state,
    const RawBatchOutputs& raw,
    int batch_index,
    const BatchedMctsConfig& config,
    Pcg64Rng& rng
) {
    // K-sample path is complex — fall back to full draft expansion for it.
    if (config.influence_samples > 1 ||
        config.influence_t_strategy > 0.0f ||
        config.influence_t_country > 0.0f) {
        return expand_from_raw(state, raw, batch_index, config, rng);
    }

    // --- Compact legal card collection (no per-mode ActionEncoding vectors) ---
    auto legal = collect_compact_legal_cards(make_observation(state, state.pub.phasing));
    const auto& cards = legal.cards;
    const auto& cache = legal.cache;

    // --- Allocate node with exact capacity (no reallocations) ---
    auto node = std::make_unique<FastNode>();
    node->side_to_move = state.pub.phasing;
    const int reserved = exact_edge_count(legal);
    node->edges.reserve(static_cast<size_t>(std::max(1, reserved)));
    node->children.reserve(static_cast<size_t>(std::max(1, reserved)));
    node->resolved_targets.reserve(static_cast<size_t>(std::max(8, reserved * 2)));

    // --- Resolve logit pointers (no memcpy — point directly into batch output) ---
    const float* card_logits = raw.card_logits + batch_index * raw.card_stride;
    const int n_card = raw.n_card;
    const float* mode_logits_ptr = raw.mode_logits + batch_index * raw.mode_stride;
    const int n_mode = raw.n_mode;

    const float* country_logits_ptr = nullptr;
    int n_country = 0;
    if (raw.strategy_logits != nullptr && raw.country_strategy_logits != nullptr &&
        raw.cs_n_countries > 0 && raw.cs_n_strategies > 0) {
        const float* sl = raw.strategy_logits + batch_index * raw.strategy_stride;
        int best_strat = 0;
        float best_val = sl[0];
        for (int s = 1; s < raw.n_strategy; ++s) {
            if (sl[s] > best_val) { best_val = sl[s]; best_strat = s; }
        }
        n_country = std::min(raw.cs_n_countries, kMaxCountryLogits);
        country_logits_ptr = raw.country_strategy_logits +
            batch_index * raw.cs_batch_stride + best_strat * raw.cs_n_countries;
    } else if (raw.country_logits != nullptr) {
        n_country = raw.n_country;
        country_logits_ptr = raw.country_logits + batch_index * raw.country_stride;
    }

    // --- Compact card softmax (only over legal cards, not full 112-element array) ---
    float card_probs[kMaxCardLogits];
    const int n_legal_cards = static_cast<int>(cards.size());
    for (int ci = 0; ci < n_legal_cards; ++ci) {
        const int idx = static_cast<int>(cards[static_cast<size_t>(ci)].card_id) - 1;
        card_probs[ci] = (idx >= 0 && idx < n_card) ? card_logits[idx] : 0.0f;
    }
    softmax_inplace(card_probs, n_legal_cards);

    // --- Pre-compute country softmax ONCE outside card loop ---
    // influence_probs[i] = softmax probability for cache.influence[i]
    // military_probs[i]  = softmax probability for cache.coup[i] (same set as realign)
    float influence_probs[kMaxCountryLogits];
    int inf_count = 0;
    float military_probs[kMaxCountryLogits];
    int mil_count = 0;
    if (country_logits_ptr != nullptr) {
        for (const auto cid : cache.influence) {
            const int idx = static_cast<int>(cid);
            influence_probs[inf_count++] = (idx < n_country) ? country_logits_ptr[idx] : 0.0f;
        }
        softmax_inplace(influence_probs, inf_count);

        for (const auto cid : cache.coup) {
            const int idx = static_cast<int>(cid);
            military_probs[mil_count++] = (idx < n_country) ? country_logits_ptr[idx] : 0.0f;
        }
        softmax_inplace(military_probs, mil_count);
    }

    double total_prior = 0.0;
    for (int ci = 0; ci < n_legal_cards; ++ci) {
        const auto& card = cards[static_cast<size_t>(ci)];
        const double card_prob = static_cast<double>(card_probs[ci]);

        // --- Compact mode softmax (only over legal modes for this card) ---
        ActionMode mode_order[5];
        float mode_prob_arr[5];
        int mode_count = 0;

        if (card.has_influence) {
            mode_order[mode_count] = ActionMode::Influence;
            const int midx = static_cast<int>(ActionMode::Influence);
            mode_prob_arr[mode_count++] = (midx < n_mode) ? mode_logits_ptr[midx] : 0.0f;
        }
        if (card.has_coup) {
            mode_order[mode_count] = ActionMode::Coup;
            const int midx = static_cast<int>(ActionMode::Coup);
            mode_prob_arr[mode_count++] = (midx < n_mode) ? mode_logits_ptr[midx] : 0.0f;
        }
        if (card.has_realign) {
            mode_order[mode_count] = ActionMode::Realign;
            const int midx = static_cast<int>(ActionMode::Realign);
            mode_prob_arr[mode_count++] = (midx < n_mode) ? mode_logits_ptr[midx] : 0.0f;
        }
        if (card.has_space) {
            mode_order[mode_count] = ActionMode::Space;
            const int midx = static_cast<int>(ActionMode::Space);
            mode_prob_arr[mode_count++] = (midx < n_mode) ? mode_logits_ptr[midx] : 0.0f;
        }
        if (card.has_event) {
            mode_order[mode_count] = ActionMode::Event;
            const int midx = static_cast<int>(ActionMode::Event);
            mode_prob_arr[mode_count++] = (midx < n_mode) ? mode_logits_ptr[midx] : 0.0f;
        }
        if (mode_count <= 0) continue;
        softmax_inplace(mode_prob_arr, mode_count);

        for (int mi = 0; mi < mode_count; ++mi) {
            const auto mode = mode_order[mi];
            const double mode_prob = static_cast<double>(mode_prob_arr[mi]);
            const double per_edge_prior = card_prob * mode_prob;

            if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
                const auto& military_targets =
                    (mode == ActionMode::Coup) ? cache.coup : cache.realign;

                if (country_logits_ptr != nullptr &&
                    mil_count == static_cast<int>(military_targets.size()) &&
                    mil_count > 0) {
                    // Softmax already computed once outside card loop
                    for (int i = 0; i < mil_count; ++i) {
                        const ActionEncoding edge{
                            .card_id = card.card_id,
                            .mode = mode,
                            .targets = {military_targets[static_cast<size_t>(i)]},
                        };
                        const double prior = per_edge_prior * static_cast<double>(military_probs[i]);
                        append_compact_edge(*node, edge, static_cast<float>(prior));
                        total_prior += prior;
                    }
                } else {
                    for (const auto country : military_targets) {
                        const ActionEncoding edge{
                            .card_id = card.card_id,
                            .mode = mode,
                            .targets = {country},
                        };
                        append_compact_edge(*node, edge, static_cast<float>(per_edge_prior));
                        total_prior += per_edge_prior;
                    }
                }
                continue;
            }

            if (mode == ActionMode::Influence) {
                if (country_logits_ptr != nullptr && !cache.influence.empty() &&
                    inf_count == static_cast<int>(cache.influence.size())) {
                    auto resolved = proportional_allocation_compact(
                        influence_probs, cache.influence, card.ops);
                    ActionEncoding act{card.card_id, ActionMode::Influence, std::move(resolved)};
                    append_compact_edge(*node, act, static_cast<float>(per_edge_prior));
                } else {
                    const ActionEncoding edge_tpl{
                        .card_id = card.card_id, .mode = ActionMode::Influence, .targets = {}};
                    append_compact_edge(*node, edge_tpl, static_cast<float>(per_edge_prior));
                }
                total_prior += per_edge_prior;
                continue;
            }

            // Space / Event
            {
                const ActionEncoding edge{.card_id = card.card_id, .mode = mode, .targets = {}};
                append_compact_edge(*node, edge, static_cast<float>(per_edge_prior));
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
            append_compact_edge(*node, *fallback, 1.0f);
            return ExpansionResult{
                .node = std::move(node),
                .leaf_value = evaluate_leaf_value_raw(state, raw.value, raw.value_stride, batch_index, config.mcts, rng),
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

    sort_edges_by_prior_desc(*node);

    // --- Edge pruning: drop low-prior edges to reduce tree width ---
    if (config.min_prior_threshold > 0.0f && node->edges.size() > 1) {
        // Find edges to keep (prior >= threshold)
        std::vector<size_t> keep_indices;
        keep_indices.reserve(node->edges.size());
        for (size_t i = 0; i < node->edges.size(); ++i) {
            if (node->edges[i].prior >= config.min_prior_threshold) {
                keep_indices.push_back(i);
            }
        }
        // Keep at least 1 edge (the best one)
        if (keep_indices.empty()) {
            keep_indices.push_back(0);
        }
        if (keep_indices.size() < node->edges.size()) {
            // Compact edges and children in-place
            for (size_t dst = 0; dst < keep_indices.size(); ++dst) {
                const size_t src = keep_indices[dst];
                if (dst != src) {
                    node->edges[dst] = std::move(node->edges[src]);
                    node->children[dst] = std::move(node->children[src]);
                }
            }
            node->edges.resize(keep_indices.size());
            node->children.resize(keep_indices.size());
            // Note: resolved_targets may have dangling entries but they're only
            // accessed via edge.target_offset/target_count which remain valid.

            renormalize_edge_priors(*node);
        }
    }

    if (config.top_k_actions > 0 &&
        static_cast<int>(node->edges.size()) > config.top_k_actions) {
        const auto limit = static_cast<size_t>(config.top_k_actions);
        node->edges.resize(limit);
        node->children.resize(limit);
        renormalize_edge_priors(*node);
    }

    // Maintain profiling counters
    ++g_expand_count;
    g_expand_total_edges += static_cast<int>(node->edges.size());
    for (const auto& e : node->edges) {
        switch (e.mode) {
            case ActionMode::Influence: ++g_mode_influence; break;
            case ActionMode::Coup:      ++g_mode_coup; break;
            case ActionMode::Realign:   ++g_mode_realign; break;
            case ActionMode::Space:     ++g_mode_space; break;
            case ActionMode::Event:     ++g_mode_event; break;
            default:                    ++g_mode_other; break;
        }
    }

    return ExpansionResult{
        .node = std::move(node),
        .leaf_value = evaluate_leaf_value_raw(state, raw.value, raw.value_stride, batch_index, config.mcts, rng),
    };
}

// Zero-allocation predicate: does this state have any legal action that would be
// handled by the NN model?  Equivalent to `!collect_card_drafts(state).empty()`
// but short-circuits on the first hit and allocates nothing.
bool has_any_model_action_cached_exact(const Observation& obs) {
    const auto side = obs.acting_side;
    const auto& pub = obs.pub;
    auto cache = AccessibleCache::build(side, pub);
    const auto& hand = obs.own_hand;

    for (int raw_card_id = 1; raw_card_id <= kMaxCardId; ++raw_card_id) {
        if (!hand.test(raw_card_id)) {
            continue;
        }
        const auto card_id = static_cast<CardId>(raw_card_id);
        if (card_id == kChinaCardId && !obs.holds_china) {
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
            if (!cache.coup.empty() && pub.defcon > 2) {
                return true;
            }
            if (!cache.realign.empty()) {
                return true;
            }
            if (cache.can_space && spec.ops >= cache.space_ops_min && !is_trap_blocked(pub, side, card_id)) {
                return true;
            }
        }

        if (is_event_play_allowed(pub, side, card_id)) {
            return true;
        }
    }

    return false;
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

    const auto obs = make_observation(state, state.pub.phasing);
    if (has_any_model_action_cached_exact(obs)) {
        return std::nullopt;
    }

    if (auto fallback = choose_action(
            PolicyKind::MinimalHybrid,
            obs.pub,
            obs.own_hand,
            obs.holds_china,
            rng
        );
        fallback.has_value()) {
        append_compact_edge(*node, *fallback, 1.0f);
        return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
    }

    node->is_terminal = true;
    return ExpansionResult{.node = std::move(node), .leaf_value = 0.0};
}

// expand_from_outputs removed — replaced by expand_from_raw for performance

double mean_root_value(const FastNode& root) {
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

// Convert FastEdge → MctsEdge (materializing the action from compact storage).
MctsEdge to_mcts_edge(const FastNode& node, size_t edge_index) {
    const auto& fe = node.edges[edge_index];
    MctsEdge me;
    me.action = materialize_action(node, edge_index);
    me.prior = fe.prior;
    me.visit_count = fe.visit_count;
    me.virtual_loss = fe.virtual_loss;
    me.total_value = fe.total_value;
    return me;
}

SearchResult build_search_result(const GameSlot& slot, bool include_root_edges) {
    SearchResult result;
    result.total_simulations = slot.sims_completed;
    if (slot.root == nullptr) {
        return result;
    }

    if (include_root_edges) {
        result.root_edges.reserve(slot.root->edges.size());
        for (size_t i = 0; i < slot.root->edges.size(); ++i) {
            result.root_edges.push_back(to_mcts_edge(*slot.root, i));
        }
    }
    result.root_value = mean_root_value(*slot.root);
    const auto best_index = best_root_edge_index(*slot.root);
    if (best_index >= 0) {
        result.best_action = materialize_action(*slot.root, static_cast<size_t>(best_index));
    }
    return result;
}

// Returns the effective sampling temperature for a given move number.
// If config.temperature == 0, always returns 0 (greedy).
// Otherwise config.temperature is treated as a scale multiplier applied to
// the piecewise schedule:
//   move <= 10  -> 1.0 (full stochasticity, early game)
//   move <= 30  -> 0.5 (moderate exploration, mid game)
//   move > 30   -> 0.0 (greedy, late game)
[[nodiscard]] float effective_temperature(const PendingDecision& decision, const BatchedMctsConfig& config) {
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

std::optional<ActionEncoding> sample_action_by_visit_counts(
    const SearchResult& search,
    float temperature,
    Pcg64Rng& rng
) {
    if (temperature <= 0.0f || search.root_edges.empty()) {
        return std::nullopt;
    }

    std::vector<std::pair<size_t, double>> scaled_log_weights;
    scaled_log_weights.reserve(search.root_edges.size());
    double max_scaled_log_weight = -std::numeric_limits<double>::infinity();
    for (size_t i = 0; i < search.root_edges.size(); ++i) {
        const auto visits = search.root_edges[i].visit_count;
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
            return search.root_edges[edge_index].action;
        }
    }

    return search.root_edges[weights.back().first].action;
}

void backpropagate_path(std::vector<std::pair<FastNode*, int>>& path, double leaf_value, int vl_weight) {
    for (auto it = path.rbegin(); it != path.rend(); ++it) {
        auto* ancestor = it->first;
        auto& edge = ancestor->edges[static_cast<size_t>(it->second)];
        edge.virtual_loss = std::max(0, edge.virtual_loss - vl_weight);
        edge.visit_count += 1;
        edge.total_value += leaf_value;
        ancestor->total_visits += 1;
    }
    path.clear();
}

// Returns how many new simulations this slot can start in the current iteration.
int sims_budget(const GameSlot& slot, int max_pending) {
    if (slot.root == nullptr && slot.pending.empty()) return 1;  // need root expansion
    if (slot.root == nullptr) return 0;                           // root expansion pending
    const int in_flight = static_cast<int>(slot.pending.size());
    const int remaining = slot.sims_target - slot.sims_completed - in_flight;
    const int slot_capacity = max_pending - in_flight;
    return std::max(0, std::min(remaining, slot_capacity));
}

// Minimum visit count before caching a node's state. Avoids caching rarely-visited
// nodes that would waste memory without saving much work.
constexpr int kCacheVisitThreshold = 0;

// Profiling counters for cache effectiveness.
std::atomic<int64_t> g_cache_total_depth{0};    // sum of path.size() across selections
std::atomic<int64_t> g_cache_saved_depth{0};    // sum of best_cached_depth (actions skipped)
std::atomic<int64_t> g_cache_selections{0};     // number of selections
std::atomic<int64_t> g_cache_max_depth{0};      // max path.size() seen
std::atomic<int64_t> g_cache_hits{0};           // selections where best_cached_depth > 0

// Inline PUCT edge selection over FastNode edges.
inline int select_edge_fast(const FastNode& node, float c_puct, int n_active = -1) {
    if (node.edges.empty()) {
        return -1;
    }
    const size_t active_edges = n_active > 0
        ? std::min(node.edges.size(), static_cast<size_t>(n_active))
        : node.edges.size();
    if (active_edges == 0) {
        return -1;
    }

    int pending_visits = 0;
    for (size_t i = 0; i < active_edges; ++i) {
        pending_visits += node.edges[i].virtual_loss;
    }

    const auto parent_visits = std::sqrt(static_cast<double>(std::max(1, node.total_visits + pending_visits)));
    const bool invert_q = (node.side_to_move == Side::US);
    int best_index = 0;
    double best_score = -std::numeric_limits<double>::infinity();
    for (size_t i = 0; i < active_edges; ++i) {
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

SelectionResult select_to_leaf(GameSlot& slot, const BatchedMctsConfig& config) {
    PendingExpansion pend;

    // Phase 1: Walk down the tree selecting edges, deferring state simulation.
    // Track the deepest node with a cached state so we can clone from there.
    FastNode* node = slot.root.get();
    const GameState* best_cached = &slot.root_state;
    size_t best_cached_depth = 0;  // path index after which best_cached is valid

    // Collect path first without applying actions.
    while (node != nullptr && !node->is_terminal && !node->edges.empty()) {
        int n_active = -1;
        if (config.pw_c > 0.0f && !node->edges.empty()) {
            const auto n = static_cast<double>(std::max(1, node->total_visits));
            n_active = std::min(
                static_cast<int>(node->edges.size()),
                std::max(1, static_cast<int>(std::ceil(
                    static_cast<double>(config.pw_c) *
                    std::pow(n, static_cast<double>(config.pw_alpha))
                )))
            );
        }
        const auto edge_index = select_edge_fast(*node, config.mcts.c_puct, n_active);
        if (edge_index < 0) break;

        auto& edge = node->edges[static_cast<size_t>(edge_index)];
        edge.virtual_loss += config.virtual_loss_weight;
        pend.path.emplace_back(node, edge_index);

        const bool is_leaf = (node->children[static_cast<size_t>(edge_index)] == nullptr);
        if (!is_leaf) {
            auto* child = node->children[static_cast<size_t>(edge_index)].get();
            if (child->cached_state) {
                best_cached = child->cached_state.get();
                best_cached_depth = pend.path.size();  // after this edge
            }
            node = child;
        } else {
            node = nullptr;  // will handle leaf below
        }
    }

    // Profile cache effectiveness.
    g_cache_selections.fetch_add(1, std::memory_order_relaxed);
    g_cache_total_depth.fetch_add(static_cast<int64_t>(pend.path.size()), std::memory_order_relaxed);
    g_cache_saved_depth.fetch_add(static_cast<int64_t>(best_cached_depth), std::memory_order_relaxed);
    {   // Update max depth (relaxed atomic max)
        int64_t d = static_cast<int64_t>(pend.path.size());
        int64_t cur = g_cache_max_depth.load(std::memory_order_relaxed);
        while (d > cur && !g_cache_max_depth.compare_exchange_weak(cur, d, std::memory_order_relaxed));
    }
    if (best_cached_depth > 0) g_cache_hits.fetch_add(1, std::memory_order_relaxed);

    // Phase 2: Clone from the deepest cached state and apply only remaining actions.
    pend.sim_state = clone_game_state(*best_cached);
    for (size_t i = best_cached_depth; i < pend.path.size(); ++i) {
        auto [path_node, path_edge_index] = pend.path[i];
        apply_tree_action(pend.sim_state,
                          materialize_action(*path_node, static_cast<size_t>(path_edge_index)),
                          slot.rng);
    }

    // Phase 3: Check if we stopped at a leaf (unexpanded child) or internal/terminal.
    if (!pend.path.empty()) {
        auto [last_node, last_edge_idx] = pend.path.back();
        if (last_node->children[static_cast<size_t>(last_edge_idx)] == nullptr) {
            // Leaf — try immediate expansion or queue for batch NN.
            if (auto immediate = expand_without_model(pend.sim_state, slot.rng);
                immediate.has_value()) {
                last_node->children[static_cast<size_t>(last_edge_idx)] =
                    std::move(immediate->node);
                backpropagate_path(pend.path, immediate->leaf_value,
                                   config.virtual_loss_weight);
                return SelectionResult{.needs_batch = false,
                                       .leaf_value = immediate->leaf_value};
            }
            slot.pending.push_back(std::move(pend));
            return SelectionResult{.needs_batch = true};
        }
        // Fell through: ended at an expanded internal node (terminal or no edges).
        node = last_node->children[static_cast<size_t>(last_edge_idx)].get();
    } else {
        node = slot.root.get();
    }

    double value = (node != nullptr && node->is_terminal) ? node->terminal_value : 0.0;
    backpropagate_path(pend.path, value, config.virtual_loss_weight);
    return SelectionResult{.needs_batch = false, .leaf_value = value};
}

std::string game_id_for(const std::string& prefix, uint32_t base_seed, int game_index) {
    std::ostringstream out;
    out << prefix << "_" << base_seed << "_";
    if (game_index < 10) {
        out << "000";
    } else if (game_index < 100) {
        out << "00";
    } else if (game_index < 1000) {
        out << "0";
    }
    out << game_index;
    return out.str();
}

// Run setup influence placement (TS Deluxe §3.0), sampling from human game corpus.
// USSR places 6 in EE, US places 9 (7 WE + 2 bid) as atomic openings.
void run_setup_influence_heuristic(GameState& gs, Pcg64Rng& rng) {
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
}

void initialize_slot(GameSlot& slot, int game_index, uint32_t base_seed, const BatchedMctsConfig& config) {
    const auto seed = base_seed + static_cast<uint32_t>(game_index);
    slot = GameSlot{};
    slot.active = true;
    slot.game_index = game_index;
    slot.record_history = config.record_rows;
    slot.root_state = reset_game(seed);
    slot.rng = Pcg64Rng(seed);
    // Run setup influence placement before MCTS begins.
    run_setup_influence_heuristic(slot.root_state, slot.rng);
    slot.game_id = game_id_for(config.game_id_prefix, base_seed, game_index);
    slot.turn = 1;
    slot.stage = BatchedGameStage::TurnSetup;
    slot.sims_target = config.mcts.n_simulations;

    // Derive per-game Nash temperature from this game's own seed so that
    // game i always gets the same temperature regardless of batch size.
    if (config.nash_temperatures && config.learned_side.has_value()) {
        Pcg64Rng nash_rng(seed + 999999U);
        const auto opponent = other_side(*config.learned_side);
        slot.heuristic_temperature = (opponent == Side::USSR)
            ? sample_nash_temperature(kNashUSSRTemps.data(),
                  static_cast<int>(kNashUSSRTemps.size()), nash_rng)
            : sample_nash_temperature(kNashUSTemps.data(),
                  static_cast<int>(kNashUSTemps.size()), nash_rng);
    }
}

void reset_move_search(GameSlot& slot, const BatchedMctsConfig& config) {
    slot.root.reset();
    slot.pending.clear();
    slot.sims_completed = 0;
    slot.sims_target = config.mcts.n_simulations;
    slot.move_done = false;
    // In heuristic_teacher_mode, save the RNG state before MCTS begins so we can
    // restore it in commit_best_action and keep game trajectories identical to a
    // pure heuristic run (same seed).
    if (config.heuristic_teacher_mode) {
        slot.rng_before_mcts = slot.rng;
    }
}

void mark_game_done(GameSlot& slot, GameResult result) {
    slot.result = std::move(result);
    slot.game_done = true;
    slot.stage = BatchedGameStage::Finished;
    slot.move_done = false;
    slot.pending.clear();
    slot.decision.reset();
    slot.root.reset();
}

std::string end_reason(const GameState& gs, std::optional<Side> winner, int card_id = -1) {
    const auto& pub = gs.pub;
    if (pub.defcon <= 1) {
        return "defcon1";
    }
    if (card_id == kWargamesCardId) {
        return "wargames";
    }
    if (winner.has_value()) {
        return gs.scoring_auto_win ? "europe_control" : "vp_threshold";
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

void advance_after_action_pair(GameSlot& slot) {
    if (slot.current_side == Side::USSR) {
        slot.current_side = Side::US;
    } else {
        slot.current_side = Side::USSR;
        slot.current_ar += 1;
    }
}

void move_to_post_round_stage(GameSlot& slot) {
    if (slot.root_state.pub.north_sea_oil_extra_ar) {
        slot.root_state.pub.north_sea_oil_extra_ar = false;
        slot.stage = BatchedGameStage::ExtraActionRoundUS;
        return;
    }
    if (slot.root_state.pub.glasnost_free_ops > 0) {
        resolve_glasnost_free_ops_live(slot.root_state.pub, slot.rng);
    }
    slot.stage = BatchedGameStage::Cleanup;
}

void move_to_followup_stage_after_extra(GameSlot& slot, Side side) {
    if (side == Side::US && slot.root_state.pub.glasnost_free_ops > 0) {
        resolve_glasnost_free_ops_live(slot.root_state.pub, slot.rng);
    }
    slot.stage = BatchedGameStage::Cleanup;
}

void queue_decision(GameSlot& slot, Side side, int ar, bool is_headline, const BatchedMctsConfig& config) {
    slot.root_state.pub.phasing = side;
    slot.root_state.pub.ar = ar;
    const auto obs = make_observation(slot.root_state, side);
    slot.decision = PendingDecision{
        .turn = slot.root_state.pub.turn,
        .ar = ar,
        .move_number = slot.decisions_started + 1,
        .side = side,
        .holds_china = obs.holds_china,
        .is_headline = is_headline,
        .pub_snapshot = obs.pub,
        .hand_snapshot = obs.own_hand,
    };
    slot.decisions_started += 1;
    reset_move_search(slot, config);
}

void finalize_headline_choices(GameSlot& slot) {
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
    slot.stage = BatchedGameStage::HeadlineResolve;
}

void advance_until_decision(GameSlot& slot, const BatchedMctsConfig& config) {
    int transitions = 0;
    while (slot.active && !slot.game_done && !slot.move_done && !slot.decision.has_value()) {
        if (++transitions > 1024) {
            throw std::runtime_error("advance_until_decision exceeded transition guard");
        }
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
                queue_decision(slot, side, /*ar=*/0, /*is_headline=*/true, config);
                break;
            }

            case BatchedGameStage::HeadlineResolve: {
                if (slot.headline_order_index >= slot.headline_order.size()) {
                    slot.stage = BatchedGameStage::ActionRound;
                    break;
                }

                const auto pending = slot.headline_order[slot.headline_order_index++];
                const auto pub_snapshot = slot.root_state.pub;
                const auto vp_before = slot.root_state.pub.vp;
                const auto defcon_before = slot.root_state.pub.defcon;
                auto [new_pub, over, winner] = apply_action_live(slot.root_state, pending.action, pending.side, slot.rng);
                (void)new_pub;
                if (slot.record_history) {
                    // Full-info MCTS: OK to access both hands (self-play only).
                    slot.traces.push_back(StepTrace{
                        .turn = slot.root_state.pub.turn,
                        .ar = 0,
                        .side = pending.side,
                        .holds_china = pending.holds_china,
                        .pub_snapshot = pub_snapshot,
                        .hand_snapshot = pending.hand_snapshot,
                        .action = pending.action,
                        .vp_before = vp_before,
                        .vp_after = slot.root_state.pub.vp,
                        .defcon_before = defcon_before,
                        .defcon_after = slot.root_state.pub.defcon,
                        .opp_hand_snapshot = slot.root_state.hands[to_index(pending.side == Side::USSR ? Side::US : Side::USSR)],
                        .deck_snapshot = slot.root_state.deck,
                        .ussr_holds_china_snapshot = slot.root_state.ussr_holds_china,
                        .us_holds_china_snapshot = slot.root_state.us_holds_china,
                    });
                    slot.search_results.push_back(pending.search);
                }
                sync_china_flags(slot.root_state);
                if (over) {
                    mark_game_done(slot, GameResult{
                        .winner = winner,
                        .final_vp = slot.root_state.pub.vp,
                        .end_turn = slot.root_state.pub.turn,
                        .end_reason = end_reason(slot.root_state, winner, pending.action.card_id),
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
                if (
                    auto cmc_result = resolve_cuban_missile_crisis_cancel_live(slot.root_state, side, slot.rng);
                    cmc_result.has_value()
                ) {
                    auto& [new_pub, over, winner] = *cmc_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.root_state.pub.vp,
                            .end_turn = slot.root_state.pub.turn,
                            .end_reason = end_reason(slot.root_state, winner),
                        });
                        break;
                    }
                    advance_after_action_pair(slot);
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
                            .end_reason = end_reason(slot.root_state, winner),
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
                queue_decision(slot, side, slot.current_ar, /*is_headline=*/false, config);
                break;
            }

            case BatchedGameStage::ExtraActionRoundUS:
            case BatchedGameStage::ExtraActionRoundUSSR: {
                const auto side = slot.stage == BatchedGameStage::ExtraActionRoundUS ? Side::US : Side::USSR;
                slot.root_state.pub.ar = std::max(slot.root_state.pub.ar, ars_for_turn(slot.root_state.pub.turn)) + 1;
                slot.root_state.pub.phasing = side;
                auto& hand = slot.root_state.hands[to_index(side)];
                if (
                    auto cmc_result = resolve_cuban_missile_crisis_cancel_live(slot.root_state, side, slot.rng);
                    cmc_result.has_value()
                ) {
                    auto& [new_pub, over, winner] = *cmc_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.root_state.pub.vp,
                            .end_turn = slot.root_state.pub.turn,
                            .end_reason = end_reason(slot.root_state, winner),
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
                if (auto trap_result = resolve_trap_ar_live(slot.root_state, side, slot.rng); trap_result.has_value()) {
                    auto& [new_pub, over, winner] = *trap_result;
                    (void)new_pub;
                    if (over) {
                        mark_game_done(slot, GameResult{
                            .winner = winner,
                            .final_vp = slot.root_state.pub.vp,
                            .end_turn = slot.root_state.pub.turn,
                            .end_reason = end_reason(slot.root_state, winner),
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
                queue_decision(slot, side, slot.root_state.pub.ar, /*is_headline=*/false, config);
                break;
            }

            case BatchedGameStage::Cleanup: {
                if (auto result = finish_turn(slot.root_state, slot.turn); result.has_value()) {
                    mark_game_done(slot, *result);
                    break;
                }
                // Turn limit: sequential game loop stops at kMaxTurns and
                // resolves winner by VP.  Mirror that here.
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

void commit_best_action(
    GameSlot& slot,
    const BatchedMctsConfig& config,
    torch::jit::script::Module& model
) {
    if (!slot.move_done || !slot.decision.has_value()) {
        return;
    }

    // Collect edge utilization stats before tree is consumed (optional).
    if (config.verbose_tree_stats && slot.root) {
        collect_tree_edge_utilization(slot.root.get());
    }

    const float temp = effective_temperature(*slot.decision, config);
    const bool need_root_edges = slot.record_history
        || config.epsilon_greedy > 0.0f
        || temp > 0.0f;
    const auto search = build_search_result(slot, need_root_edges);
    ActionEncoding action;

    if (config.heuristic_teacher_mode) {
        // Restore the RNG to its pre-MCTS state so heuristic move selection produces
        // the same game trajectory as a pure heuristic run with the same seed.
        if (slot.rng_before_mcts.has_value()) {
            slot.rng = *slot.rng_before_mcts;
            slot.rng_before_mcts.reset();
        }
        // Use MinimalHybrid for the actual game move; MCTS visit counts are kept as
        // teacher targets only.
        action = choose_action(
            PolicyKind::MinimalHybrid,
            slot.decision->pub_snapshot,
            slot.decision->hand_snapshot,
            slot.decision->holds_china,
            slot.rng
        ).value_or(ActionEncoding{});
    } else {
        action = search.best_action;

        // Epsilon-greedy: with probability epsilon_greedy, pick a uniformly random
        // legal action from the root edges instead of the MCTS-recommended action.
        const bool do_epsilon = config.epsilon_greedy > 0.0f
            && !search.root_edges.empty()
            && slot.rng.random_double() < static_cast<double>(config.epsilon_greedy);
        if (do_epsilon) {
            const auto idx = slot.rng.choice_index(search.root_edges.size());
            action = search.root_edges[idx].action;
        } else if (action.card_id != 0) {
            // Temperature-based sampling with piecewise schedule.
            if (const auto sampled = sample_action_by_visit_counts(search, temp, slot.rng); sampled.has_value()) {
                action = *sampled;
            }
        }
        if (action.card_id == 0) {
            if (slot.heuristic_temperature > 0.0f) {
                action = choose_minimal_hybrid_sampled(
                    slot.decision->pub_snapshot,
                    slot.decision->hand_snapshot,
                    slot.decision->holds_china,
                    slot.heuristic_temperature,
                    slot.rng
                ).value_or(ActionEncoding{});
            } else {
                action = choose_action(
                    PolicyKind::MinimalHybrid,
                    slot.decision->pub_snapshot,
                    slot.decision->hand_snapshot,
                    slot.decision->holds_china,
                    slot.rng
                ).value_or(ActionEncoding{});
            }
        }
    }
    if (action.card_id == 0) {
        throw std::runtime_error("batched MCTS could not resolve an action");
    }

    const auto decision = *slot.decision;
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
        slot.pending_headlines[to_index(decision.side)] = PendingHeadlineChoice{
            .side = decision.side,
            .holds_china = decision.holds_china,
            .hand_snapshot = decision.hand_snapshot,
            .action = action,
            .search = slot.record_history ? search : SearchResult{},
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

    const auto vp_before = slot.root_state.pub.vp;
    const auto defcon_before = slot.root_state.pub.defcon;
    PolicyCallbackFn policy_cb;
    const PolicyCallbackFn* cb_ptr = nullptr;
    if (action.mode == ActionMode::EventFirst) {
        policy_cb = make_commit_policy_callback(
            model,
            config.device,
            slot,
            action,
            torch::Tensor{},
            /*trace=*/nullptr
        );
        cb_ptr = &policy_cb;
    }
    auto [new_pub, over, winner] = apply_action_live(slot.root_state, action, decision.side, slot.rng, cb_ptr);
    (void)new_pub;
    if (slot.record_history) {
        // Full-info MCTS: OK to access both hands (self-play only).
        slot.traces.push_back(StepTrace{
            .turn = decision.turn,
            .ar = decision.ar,
            .side = decision.side,
            .holds_china = decision.holds_china,
            .pub_snapshot = decision.pub_snapshot,
            .hand_snapshot = decision.hand_snapshot,
            .action = action,
            .vp_before = vp_before,
            .vp_after = slot.root_state.pub.vp,
            .defcon_before = defcon_before,
            .defcon_after = slot.root_state.pub.defcon,
            .opp_hand_snapshot = slot.root_state.hands[to_index(decision.side == Side::USSR ? Side::US : Side::USSR)],
            .deck_snapshot = slot.root_state.deck,
            .ussr_holds_china_snapshot = slot.root_state.ussr_holds_china,
            .us_holds_china_snapshot = slot.root_state.us_holds_china,
        });
        slot.search_results.push_back(search);
    }
    sync_china_flags(slot.root_state);

    if (over) {
        mark_game_done(slot, GameResult{
            .winner = winner,
            .final_vp = slot.root_state.pub.vp,
            .end_turn = slot.root_state.pub.turn,
            .end_reason = end_reason(slot.root_state, winner, action.card_id),
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
                    .end_reason = end_reason(slot.root_state, norad_winner),
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

const char* game_result_str(const std::optional<Side>& winner) {
    if (!winner.has_value()) {
        return "draw";
    }
    return *winner == Side::USSR ? "ussr_win" : "us_win";
}

int winner_side_int(const std::optional<Side>& winner) {
    if (!winner.has_value()) {
        return 0;
    }
    return *winner == Side::USSR ? 1 : -1;
}

std::string targets_csv(const std::vector<CountryId>& targets) {
    std::ostringstream out;
    for (size_t i = 0; i < targets.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << static_cast<int>(targets[i]);
    }
    return out.str();
}

void write_int_array(std::ostream& out, const std::vector<int>& values) {
    out << "[";
    for (size_t i = 0; i < values.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << values[i];
    }
    out << "]";
}

std::vector<int> card_mask(const CardSet& cards) {
    std::vector<int> mask(ts::kCardSlots, 0);
    for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
        if (cards.test(card_id)) {
            mask[static_cast<size_t>(card_id)] = 1;
        }
    }
    return mask;
}

std::vector<int> influence_array(const PublicState& pub, Side side) {
    std::vector<int> values(ts::kCountrySlots, 0);
    for (int country_id = 0; country_id <= ts::kMaxCountryId; ++country_id) {
        values[static_cast<size_t>(country_id)] = pub.influence_of(side, static_cast<CountryId>(country_id));
    }
    return values;
}

std::vector<AggregatedVisitCount> aggregate_visit_counts(const SearchResult& result) {
    std::map<std::pair<int, int>, int> counts;
    for (const auto& edge : result.root_edges) {
        counts[{static_cast<int>(edge.action.card_id), static_cast<int>(edge.action.mode)}] += edge.visit_count;
    }

    std::vector<AggregatedVisitCount> aggregated;
    aggregated.reserve(counts.size());
    for (const auto& [key, visits] : counts) {
        aggregated.push_back(AggregatedVisitCount{
            .card_id = static_cast<CardId>(key.first),
            .mode = static_cast<ActionMode>(key.second),
            .visits = visits,
        });
    }
    std::sort(aggregated.begin(), aggregated.end(), [](const auto& lhs, const auto& rhs) {
        if (lhs.visits != rhs.visits) {
            return lhs.visits > rhs.visits;
        }
        if (lhs.card_id != rhs.card_id) {
            return lhs.card_id < rhs.card_id;
        }
        return static_cast<int>(lhs.mode) < static_cast<int>(rhs.mode);
    });
    return aggregated;
}

void write_visit_counts_json(std::ostream& out, const SearchResult& result) {
    const auto aggregated = aggregate_visit_counts(result);
    out << "[";
    for (size_t i = 0; i < aggregated.size(); ++i) {
        if (i > 0) {
            out << ",";
        }
        out << "{\"card_id\":" << static_cast<int>(aggregated[i].card_id)
            << ",\"mode\":" << static_cast<int>(aggregated[i].mode)
            << ",\"visits\":" << aggregated[i].visits
            << "}";
    }
    out << "]";
}

void write_game_rows(const GameSlot& slot, std::ostream& out) {
    for (size_t step_idx = 0; step_idx < slot.traces.size(); ++step_idx) {
        const auto& step = slot.traces[step_idx];
        const auto& pub = step.pub_snapshot;
        const auto& search = slot.search_results[step_idx];

        auto actor_hand_mask = card_mask(step.hand_snapshot);
        std::vector<int> card_quality(ts::kCardSlots, 3);
        for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
            if (step.hand_snapshot.test(card_id)) {
                card_quality[static_cast<size_t>(card_id)] = 0;
            }
        }
        auto discard_mask = card_mask(pub.discard);
        auto removed_mask = card_mask(pub.removed);
        auto actor_known_not_in = card_mask(pub.discard | pub.removed);
        auto opp_known_in = std::vector<int>(ts::kCardSlots, 0);
        auto opp_known_not_in = card_mask(step.hand_snapshot | pub.discard | pub.removed);
        auto opp_possible = std::vector<int>(ts::kCardSlots, 0);
        auto lbl_opponent_possible = std::vector<int>(ts::kCardSlots, 0);
        int actor_hand_size = 0;
        for (int card_id = 1; card_id <= ts::kMaxCardId; ++card_id) {
            if (step.hand_snapshot.test(card_id) && card_id != ts::kChinaCardId) {
                ++actor_hand_size;
            }
        }

        out
            << "{\"game_id\":\"" << slot.game_id << "\""
            << ",\"step_idx\":" << step_idx
            << ",\"turn\":" << pub.turn
            << ",\"ar\":" << pub.ar
            << ",\"phasing\":" << static_cast<int>(step.side)
            << ",\"action_kind\":-1"
            << ",\"card_id\":" << static_cast<int>(step.action.card_id)
            << ",\"country_id\":" << (step.action.targets.empty() ? -1 : static_cast<int>(step.action.targets.front()))
            << ",\"action_card_id\":" << static_cast<int>(step.action.card_id)
            << ",\"action_mode\":" << static_cast<int>(step.action.mode)
            << ",\"action_targets\":\"" << targets_csv(step.action.targets) << "\""
            << ",\"vp\":" << pub.vp
            << ",\"defcon\":" << pub.defcon
            << ",\"milops_ussr\":" << pub.milops[to_index(Side::USSR)]
            << ",\"milops_us\":" << pub.milops[to_index(Side::US)]
            << ",\"space_ussr\":" << pub.space[to_index(Side::USSR)]
            << ",\"space_us\":" << pub.space[to_index(Side::US)]
            << ",\"china_held_by\":" << static_cast<int>(pub.china_held_by)
            << ",\"china_playable\":" << (pub.china_playable ? "true" : "false")
            << ",\"ussr_influence\":";
        write_int_array(out, influence_array(pub, Side::USSR));
        out << ",\"us_influence\":";
        write_int_array(out, influence_array(pub, Side::US));
        out << ",\"discard_mask\":";
        write_int_array(out, discard_mask);
        out << ",\"removed_mask\":";
        write_int_array(out, removed_mask);
        out << ",\"actor_known_in\":";
        write_int_array(out, actor_hand_mask);
        out << ",\"actor_known_not_in\":";
        write_int_array(out, actor_known_not_in);
        out << ",\"actor_possible\":";
        write_int_array(out, actor_hand_mask);
        out << ",\"actor_hand_size\":" << actor_hand_size
            << ",\"actor_holds_china\":" << (step.holds_china ? "true" : "false")
            << ",\"opp_known_in\":";
        write_int_array(out, opp_known_in);
        out << ",\"opp_known_not_in\":";
        write_int_array(out, opp_known_not_in);
        out << ",\"opp_possible\":";
        write_int_array(out, opp_possible);
        out << ",\"opp_hand_size\":0"
            << ",\"opp_holds_china\":" << ((pub.china_held_by != Side::Neutral && !step.holds_china) ? "true" : "false")
            << ",\"lbl_actor_hand\":";
        write_int_array(out, actor_hand_mask);
        out << ",\"lbl_step_quality\":0"
            << ",\"lbl_card_quality\":";
        write_int_array(out, card_quality);
        out << ",\"lbl_opponent_possible\":";
        write_int_array(out, lbl_opponent_possible);
        out << ",\"mcts_visit_counts\":";
        write_visit_counts_json(out, search);
        out << ",\"mcts_root_value\":" << search.root_value
            << ",\"mcts_n_sim\":" << search.total_simulations
            << ",\"game_result\":\"" << game_result_str(slot.result.winner) << "\""
            << ",\"winner_side\":" << winner_side_int(slot.result.winner)
            << ",\"final_vp\":" << slot.result.final_vp
            << ",\"end_turn\":" << slot.result.end_turn
            << ",\"end_reason\":\"" << slot.result.end_reason << "\"}\n";
    }
}

}  // namespace

void collect_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    const BatchedMctsConfig& config,
    uint32_t base_seed,
    std::ostream& out_stream,
    std::vector<GameResult>* out_results
) {
    if (n_games <= 0) {
        throw std::invalid_argument("n_games must be positive");
    }
    if (config.pool_size <= 0) {
        throw std::invalid_argument("pool_size must be positive");
    }
    if (config.virtual_loss_weight <= 0) {
        throw std::invalid_argument("virtual_loss_weight must be positive");
    }
    if (config.mcts.n_simulations < 0) {
        throw std::invalid_argument("n_simulations must be non-negative");
    }
    if (config.n_mcts_threads < 0) {
        throw std::invalid_argument("n_mcts_threads must be non-negative");
    }
    if (config.torch_intra_threads < 0) {
        throw std::invalid_argument("torch_intra_threads must be non-negative");
    }
    if (config.torch_interop_threads < 0) {
        throw std::invalid_argument("torch_interop_threads must be non-negative");
    }

    // Reset cache profiling counters.
    g_cache_selections.store(0);
    g_cache_hits.store(0);
    g_cache_total_depth.store(0);
    g_cache_saved_depth.store(0);
    g_cache_max_depth.store(0);
    // Reset expand/K-sample profiling counters.
    g_expand_total_edges = 0;
    g_ksample_time = 0;
    g_ksample_count = 0;
    g_ksample_edges_total = 0;
    g_mode_influence = g_mode_coup = g_mode_realign = g_mode_space = g_mode_event = g_mode_other = 0;
    std::fill(std::begin(g_edge_util_histogram), std::end(g_edge_util_histogram), 0);
    g_edge_util_nodes = 0;

    struct BatchEntry {
        GameSlot* slot = nullptr;
        size_t pending_index = 0;
        int batch_index = 0;
    };

    struct ThreadBatchState {
        int slot_begin = 0;
        int slot_end = 0;
        int batch_base = 0;  // start index in batch_inputs for this thread
        int filled = 0;      // how many batch items this thread filled
        int compacted_offset = 0;  // offset after compaction by thread 0
        std::vector<BatchEntry> entries;
    };

    std::vector<GameSlot> pool(static_cast<size_t>(config.pool_size));
    int games_started = 0;
    int games_emitted = 0;

    const int max_pending = std::max(1, config.max_pending);
    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(config.pool_size * max_pending, config.device);

    // Thread count: configurable or auto.
    const int hw_threads = static_cast<int>(std::thread::hardware_concurrency());
    const int requested_threads = config.n_mcts_threads > 0
        ? config.n_mcts_threads
        : std::min(config.pool_size, std::max(1, hw_threads));
    const int n_threads = std::max(1, std::min(config.pool_size, requested_threads));

    // Configure PyTorch threading separately from MCTS threads.
    if (config.torch_intra_threads > 0) {
        at::set_num_threads(config.torch_intra_threads);
    } else if (n_threads > 2) {
        at::set_num_threads(4);
    }
    if (config.torch_interop_threads > 0) {
        try {
            at::set_num_interop_threads(config.torch_interop_threads);
        } catch (...) {
            // Already set by a previous call — ignore.
        }
    } else if (n_threads > 2) {
        try {
            at::set_num_interop_threads(1);
        } catch (...) {}
    }

    // Partition game slots evenly across threads. Each thread owns a contiguous
    // slice of the pool and a corresponding disjoint slice of batch_inputs.
    std::vector<ThreadBatchState> thread_states(static_cast<size_t>(n_threads));
    {
        const int base_slots = config.pool_size / n_threads;
        const int extra_slots = config.pool_size % n_threads;
        int slot_cursor = 0;
        for (int tid = 0; tid < n_threads; ++tid) {
            const int slot_count = base_slots + (tid < extra_slots ? 1 : 0);
            auto& ts = thread_states[static_cast<size_t>(tid)];
            ts.slot_begin = slot_cursor;
            ts.slot_end = slot_cursor + slot_count;
            ts.batch_base = slot_cursor * max_pending;
            ts.entries.reserve(static_cast<size_t>(slot_count) * static_cast<size_t>(max_pending));
            slot_cursor += slot_count;
        }
    }

    using Clock = std::chrono::high_resolution_clock;
    double t_advance = 0, t_commit = 0, t_select = 0, t_nn = 0, t_expand = 0;
    int n_batches = 0, total_batch_items = 0;
    int debug_iters = 0;
    PhaseBarrier barrier(n_threads);
    std::atomic<bool> stop_requested{false};
    int compacted_batch_size = 0;
    RawBatchOutputs raw_outputs;
    const bool progress_debug = std::getenv("TS_MCTS_PROGRESS") != nullptr;
    auto last_progress = Clock::now();

    auto worker_loop = [&](int tid) {
        auto& thread_state = thread_states[static_cast<size_t>(tid)];
        for (;;) {
            // ── Phase 1: Emit completed games + start new ones (thread 0 only) ──
            if (tid == 0) {
                batch_inputs.filled = 0;
                compacted_batch_size = 0;
                raw_outputs = RawBatchOutputs{};

                auto t0_adv = Clock::now();
                for (auto& slot : pool) {
                    if (slot.active && slot.game_done && !slot.emitted) {
                        if (slot.record_history) {
                            write_game_rows(slot, out_stream);
                        }
                        if (out_results) {
                            out_results->push_back(slot.result);
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
                t_advance += std::chrono::duration<double>(Clock::now() - t0_adv).count();

                stop_requested.store(games_emitted >= n_games, std::memory_order_release);
                if (!stop_requested.load(std::memory_order_acquire)) {
                    ++debug_iters;
                }
            }

            barrier.wait();  // ── Barrier 1: all threads see updated pool ──
            if (stop_requested.load(std::memory_order_acquire)) {
                break;
            }

            // ── Phase 2: Select (each thread processes its own partition) ──
            const auto t0_sel = tid == 0 ? Clock::now() : Clock::time_point{};
            thread_state.filled = 0;
            thread_state.entries.clear();

            for (int slot_idx = thread_state.slot_begin; slot_idx < thread_state.slot_end; ++slot_idx) {
                auto& slot = pool[static_cast<size_t>(slot_idx)];

                if (!slot.active) {
                    continue;
                }

                if (slot.move_done) {
                    const auto t0_commit = tid == 0 ? Clock::now() : Clock::time_point{};
                    commit_best_action(slot, config, model);
                    if (tid == 0) {
                        t_commit += std::chrono::duration<double>(Clock::now() - t0_commit).count();
                    }
                }
                advance_until_decision(slot, config);
                if (slot.game_done || !slot.decision.has_value()) {
                    continue;
                }

                // Opponent handling: heuristic fallback or greedy NN.
                if (config.learned_side.has_value() &&
                    slot.decision->side != *config.learned_side) {
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
                        PendingExpansion pend;
                        pend.sim_state = clone_game_state(slot.root_state);
                        pend.is_root_expansion = true;
                        slot.pending.push_back(std::move(pend));
                        const int bi = thread_state.batch_base + thread_state.filled;
                        fill_batch_slot_no_count(
                            batch_inputs,
                            bi,
                            make_observation(slot.root_state, slot.root_state.pub.phasing)
                        );
                        thread_state.entries.push_back(BatchEntry{
                            .slot = &slot,
                            .pending_index = slot.pending.size() - 1,
                            .batch_index = bi,
                        });
                        thread_state.filled += 1;
                        continue;
                    }
                }

                if (slot.sims_completed >= slot.sims_target && slot.pending.empty()) {
                    slot.move_done = true;
                    continue;
                }

                for (;;) {
                    const int budget = sims_budget(slot, max_pending);
                    if (budget <= 0) {
                        break;
                    }
                    const auto selection = select_to_leaf(slot, config);
                    if (selection.needs_batch) {
                        auto& pend = slot.pending.back();
                        const int bi = thread_state.batch_base + thread_state.filled;
                        fill_batch_slot_no_count(
                            batch_inputs,
                            bi,
                            make_observation(pend.sim_state, pend.sim_state.pub.phasing)
                        );
                        thread_state.entries.push_back(BatchEntry{
                            .slot = &slot,
                            .pending_index = slot.pending.size() - 1,
                            .batch_index = bi,
                        });
                        thread_state.filled += 1;
                    } else {
                        slot.sims_completed += 1;
                        if (slot.sims_completed >= slot.sims_target && slot.pending.empty()) {
                            slot.move_done = true;
                            break;
                        }
                    }
                }
            }

            barrier.wait();  // ── Barrier 2: all threads done selecting ──

            // ── Phase 3: Compact + NN forward (thread 0 only) ──
            if (tid == 0) {
                t_select += std::chrono::duration<double>(Clock::now() - t0_sel).count();

                auto t0_nn = Clock::now();
                int total = 0;
                for (auto& ts : thread_states) {
                    ts.compacted_offset = total;
                    total += ts.filled;
                }
                compacted_batch_size = total;
                batch_inputs.filled = total;

                if (total > 0) {
                    // Compact disjoint thread slices into contiguous block.
                    for (auto& ts : thread_states) {
                        const int src = ts.batch_base;
                        const int dst = ts.compacted_offset;
                        if (ts.filled > 0 && src != dst) {
                            compact_batch_inputs(batch_inputs, src, dst, ts.filled);
                        }
                        // Remap batch indices to compacted positions.
                        for (auto& entry : ts.entries) {
                            entry.batch_index = dst + (entry.batch_index - src);
                        }
                    }
                    raw_outputs = RawBatchOutputs::extract(
                        nn::forward_model_batched(model, batch_inputs));
                    n_batches += 1;
                    total_batch_items += total;
                }
                t_nn += std::chrono::duration<double>(Clock::now() - t0_nn).count();
            }

            barrier.wait();  // ── Barrier 3: NN results ready ──

            // ── Phase 4: Expand (each thread processes its own entries) ──
            const auto t0_exp = tid == 0 ? Clock::now() : Clock::time_point{};
            if (compacted_batch_size > 0) {
                for (const auto& entry : thread_state.entries) {
                    auto& slot = *entry.slot;
                    auto& pend = slot.pending[entry.pending_index];
                    if (pend.is_root_expansion) {
                        auto expansion = expand_from_raw_fast(
                            pend.sim_state, raw_outputs, entry.batch_index,
                            config, slot.rng);
                        slot.root = std::move(expansion.node);
                        apply_root_dirichlet_noise_fast(*slot.root, config.mcts, slot.rng);
                        if (slot.sims_target == 0) {
                            slot.move_done = true;
                        }
                    } else {
                        auto expansion = expand_from_raw_fast(
                            pend.sim_state, raw_outputs, entry.batch_index,
                            config, slot.rng);
                        auto& [parent, edge_index] = pend.path.back();
                        if (parent->total_visits >= kCacheVisitThreshold) {
                            expansion.node->cached_state =
                                std::make_unique<GameState>(pend.sim_state);
                        }
                        parent->children[static_cast<size_t>(edge_index)] =
                            std::move(expansion.node);
                        backpropagate_path(pend.path, expansion.leaf_value,
                            config.virtual_loss_weight);
                        slot.sims_completed += 1;
                    }
                }
            }

            for (int slot_idx = thread_state.slot_begin; slot_idx < thread_state.slot_end; ++slot_idx) {
                auto& slot = pool[static_cast<size_t>(slot_idx)];
                if (!slot.active) {
                    continue;
                }
                slot.pending.clear();
                if (slot.sims_completed >= slot.sims_target && slot.pending.empty()) {
                    slot.move_done = true;
                }
            }

            barrier.wait();  // ── Barrier 4: all threads done expanding ──
            if (tid == 0) {
                t_expand += std::chrono::duration<double>(Clock::now() - t0_exp).count();
                if (progress_debug) {
                    const auto now = Clock::now();
                    const auto since_last = std::chrono::duration<double>(now - last_progress).count();
                    if (since_last >= 5.0) {
                        fprintf(stderr,
                                "[MCTS progress] iters=%d emitted=%d/%d commit=%.3fs select=%.3fs nn=%.3fs expand=%.3fs batches=%d items=%d\n",
                                debug_iters, games_emitted, n_games,
                                t_commit, t_select, t_nn, t_expand,
                                n_batches, total_batch_items);
                        last_progress = now;
                    }
                }
            }
        }
    };

    // Launch worker threads. Thread 0 runs on the calling thread.
    std::vector<std::thread> workers;
    workers.reserve(static_cast<size_t>(std::max(0, n_threads - 1)));
    for (int tid = 1; tid < n_threads; ++tid) {
        workers.emplace_back(worker_loop, tid);
    }
    worker_loop(0);
    for (auto& worker : workers) {
        worker.join();
    }

    const double total = t_advance + t_commit + t_select + t_nn + t_expand;
    fprintf(stderr, "[MCTS profile] threads=%d advance=%.3fs commit=%.3fs select=%.3fs nn=%.3fs expand=%.3fs total=%.3fs\n",
            n_threads, t_advance, t_commit, t_select, t_nn, t_expand, total);
    fprintf(stderr, "[MCTS profile] batches=%d items=%d avg_batch=%.1f iters=%d\n",
            n_batches, total_batch_items, n_batches > 0 ? double(total_batch_items) / n_batches : 0.0, debug_iters);
    fprintf(stderr, "[MCTS expand] alloc=%.3fs drafts=%.3fs edges=%.3fs count=%d total_edges=%d avg=%.1f\n",
            g_expand_alloc, g_expand_drafts, g_expand_edges, g_expand_count,
            g_expand_total_edges,
            g_expand_count > 0 ? static_cast<double>(g_expand_total_edges) / g_expand_count : 0.0);
    {
        const int total_mode = g_mode_influence + g_mode_coup + g_mode_realign + g_mode_space + g_mode_event + g_mode_other;
        if (total_mode > 0) {
            fprintf(stderr, "[MCTS modes] inf=%d(%.0f%%) coup=%d(%.0f%%) realign=%d(%.0f%%) space=%d(%.0f%%) event=%d(%.0f%%) other=%d\n",
                    g_mode_influence, 100.0 * g_mode_influence / total_mode,
                    g_mode_coup, 100.0 * g_mode_coup / total_mode,
                    g_mode_realign, 100.0 * g_mode_realign / total_mode,
                    g_mode_space, 100.0 * g_mode_space / total_mode,
                    g_mode_event, 100.0 * g_mode_event / total_mode,
                    g_mode_other);
        }
    }
    if (g_ksample_count > 0) {
        fprintf(stderr, "[MCTS K-sample] calls=%d edges=%d avg_edges=%.1f time=%.3fs avg=%.1fus\n",
                g_ksample_count, g_ksample_edges_total,
                static_cast<double>(g_ksample_edges_total) / g_ksample_count,
                g_ksample_time,
                g_ksample_time / g_ksample_count * 1e6);
    }
    const auto cs = g_cache_selections.load();
    const auto ch = g_cache_hits.load();
    const auto cd = g_cache_total_depth.load();
    const auto csd = g_cache_saved_depth.load();
    if (cs > 0) {
        const auto md = g_cache_max_depth.load();
        fprintf(stderr, "[MCTS cache] selections=%lld hits=%lld (%.1f%%) avg_depth=%.2f max_depth=%lld avg_saved=%.2f save_ratio=%.1f%%\n",
                (long long)cs, (long long)ch,
                100.0 * ch / cs,
                (double)cd / cs,
                (long long)md,
                (double)csd / cs,
                cd > 0 ? 100.0 * csd / cd : 0.0);
    }
    if (g_edge_util_nodes > 0) {
        fprintf(stderr, "[MCTS edge-util] nodes=%d histogram(%%edges_visited):", g_edge_util_nodes);
        for (int i = 0; i <= 10; ++i) {
            if (g_edge_util_histogram[i] > 0) {
                if (i < 10)
                    fprintf(stderr, " %d-%d%%=%d", i*10, (i+1)*10, g_edge_util_histogram[i]);
                else
                    fprintf(stderr, " 100%%=%d", g_edge_util_histogram[i]);
            }
        }
        fprintf(stderr, "\n");
    }
}

// ---------------------------------------------------------------------------
// Greedy batched benchmark: same GameSlot/advance_until_decision machinery
// as MCTS collection, but uses a single argmax decode instead of tree search.
// ---------------------------------------------------------------------------

namespace {

// Greedy decode shares TorchScriptPolicy::choose_action semantics via
// decode_helpers.hpp, while rollout decode below keeps the same mask/log-prob
// bookkeeping around that shared logic.
// Sample from logits using temperature. T=0 → argmax, T>0 → softmax sampling.
CardId sample_from_masked_logits(torch::Tensor masked, float temperature, Pcg64Rng& rng) {
    if (temperature <= 0.0f) {
        return static_cast<CardId>(masked.argmax(0).item<int64_t>() + 1);
    }
    auto scaled = masked / temperature;
    auto probs = torch::softmax(scaled, 0);
    auto sampled_idx = torch::multinomial(probs, 1).item<int64_t>();
    return static_cast<CardId>(sampled_idx + 1);
}

void populate_rollout_features(
    RolloutStep& step,
    const nn::BatchInputs& inputs,
    int64_t batch_index
) {
    step.influence = inputs.influence.index({batch_index}).cpu().clone();
    step.cards = inputs.cards.index({batch_index}).cpu().clone();
    step.scalars = inputs.scalars.index({batch_index}).cpu().clone();
}

std::pair<ActionEncoding, RolloutStep> rollout_action_from_outputs(
    const Observation& obs,
    const nn::BatchInputs& inputs,
    const nn::BatchOutputs& outputs,
    int64_t batch_index,
    Pcg64Rng& rng,
    float temperature,
    int game_index,
    torch::Device input_device
) {
    (void)input_device;

    const auto& pub = obs.pub;
    const auto side = obs.acting_side;
    const auto& hand = obs.own_hand;

    RolloutStep step;
    step.value = outputs.value.index({batch_index, 0}).item<float>();
    step.side_int = to_index(side);
    step.game_index = game_index;

    auto heuristic_fallback = [&]() -> std::pair<ActionEncoding, RolloutStep> {
        auto action = choose_action(PolicyKind::MinimalHybrid, pub, hand, obs.holds_china, rng)
            .value_or(ActionEncoding{});
        step.card_idx = -1;
        step.mode_idx = -1;
        return {action, std::move(step)};
    };

    const auto card_logits = outputs.card_logits.index({batch_index});
    const auto mode_logits = outputs.mode_logits.index({batch_index});
    const auto country_logits_raw = outputs.country_logits.defined()
        ? outputs.country_logits.index({batch_index}) : torch::Tensor{};
    auto decoded = decode::choose_action_from_outputs_with_logprobs(
        pub,
        hand,
        obs.holds_china,
        card_logits,
        mode_logits,
        country_logits_raw,
        temperature
    );

    step.card_mask = decoded.trace.card_mask;
    step.mode_mask = decoded.trace.mode_mask;
    step.country_mask = decoded.trace.country_mask;
    step.card_idx = decoded.trace.card_idx;
    step.mode_idx = decoded.trace.mode_idx;
    step.country_targets = std::move(decoded.trace.country_targets);

    if (decoded.should_populate_rollout_features) {
        populate_rollout_features(step, inputs, batch_index);
    }
    if (decoded.needs_fallback) {
        return heuristic_fallback();
    }

    step.log_prob =
        decoded.log_probs.card_lp + decoded.log_probs.mode_lp + decoded.log_probs.country_lp;
    return {std::move(decoded.action), std::move(step)};
}

ActionEncoding greedy_action_from_outputs(
    const Observation& obs,
    const nn::BatchOutputs& outputs,
    int64_t batch_index,
    Pcg64Rng& rng,
    float temperature = 0.0f
) {
    const auto& pub = obs.pub;
    const auto& hand = obs.own_hand;

    const auto card_logits = outputs.card_logits.index({batch_index});
    const auto mode_logits = outputs.mode_logits.index({batch_index});
    const auto country_logits_raw = outputs.country_logits.defined()
        ? outputs.country_logits.index({batch_index}) : torch::Tensor{};
    const auto marginal_logits_raw = outputs.marginal_logits.defined()
        ? outputs.marginal_logits.index({batch_index}) : torch::Tensor{};
    const auto strategy_logits_raw = outputs.strategy_logits.defined()
        ? outputs.strategy_logits.index({batch_index}) : torch::Tensor{};
    const auto country_strategy_logits_raw = outputs.country_strategy_logits.defined()
        ? outputs.country_strategy_logits.index({batch_index}) : torch::Tensor{};

    auto heuristic_fallback = [&]() {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, obs.holds_china, rng)
            .value_or(ActionEncoding{});
    };

    return decode::choose_action_from_outputs(
        pub,
        hand,
        obs.holds_china,
        /*use_country_head=*/true,
        card_logits,
        mode_logits,
        country_logits_raw,
        strategy_logits_raw,
        country_strategy_logits_raw,
        rng,
        [&](const torch::Tensor& masked_card) -> CardId {
            return sample_from_masked_logits(masked_card, temperature, rng);
        },
        [&](const torch::Tensor& masked_mode) -> ActionMode {
            if (temperature <= 0.0f) {
                return static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
            }
            auto scaled = masked_mode / temperature;
            auto probs = torch::softmax(scaled, 0);
            return static_cast<ActionMode>(torch::multinomial(probs, 1).item<int64_t>());
        },
        heuristic_fallback,
        heuristic_fallback,
        marginal_logits_raw
    );
}

struct CommitPolicyTrace {
    int small_choice_target = -1;
    int small_choice_n_options = 0;
    float small_choice_logprob = 0.0f;
    bool deferred_country_used = false;
    torch::Tensor deferred_country_mask;
    std::vector<int> deferred_country_targets;
    float deferred_country_logprob = 0.0f;
};

std::vector<ActionEncoding> enumerate_deferred_event_first_actions(
    const PublicState& pub,
    CardId source_card,
    Side side
) {
    CardSet hand;
    hand.set(static_cast<int>(source_card));

    std::vector<ActionEncoding> ops_actions;
    for (const auto& candidate : enumerate_actions(hand, pub, side, /*holds_china=*/false)) {
        if (
            candidate.card_id == source_card &&
            candidate.mode != ActionMode::EventFirst &&
            candidate.mode != ActionMode::Event &&
            candidate.mode != ActionMode::Space
        ) {
            ops_actions.push_back(candidate);
        }
    }
    return ops_actions;
}

torch::Tensor build_country_mask_for_action(
    const PublicState& pub,
    Side side,
    CardId card_id,
    ActionMode mode
) {
    const auto bool_opts = torch::TensorOptions().dtype(torch::kBool);
    auto mask = torch::zeros({kCountrySlots}, bool_opts);
    for (const auto cid : accessible_countries_filtered(pub, side, card_id, mode)) {
        mask.index_put_({static_cast<int64_t>(cid)}, true);
    }
    return mask;
}

float compute_country_logprob_for_action(
    const PublicState& pub,
    Side side,
    const ActionEncoding& action,
    const torch::Tensor& country_logits
) {
    if (
        !country_logits.defined() ||
        action.targets.empty() ||
        action.mode == ActionMode::Event ||
        action.mode == ActionMode::Space ||
        action.mode == ActionMode::EventFirst
    ) {
        return 0.0f;
    }

    auto masked_probs = torch::zeros_like(country_logits);
    for (const auto cid : accessible_countries_filtered(pub, side, action.card_id, action.mode)) {
        const auto index = static_cast<int64_t>(cid);
        masked_probs.index_put_({index}, decode::tensor_at(country_logits, index));
    }

    const auto normalized_probs = masked_probs / (masked_probs.sum() + 1e-10f);
    const auto country_log_probs = torch::log(normalized_probs + 1e-10f);

    float country_lp = 0.0f;
    for (const auto target : action.targets) {
        country_lp += country_log_probs.index({static_cast<int64_t>(target)}).item<float>();
    }
    return country_lp;
}

bool is_deferred_event_first_choice(const ActionEncoding& top_level_action, const EventDecision& decision) {
    if (
        top_level_action.mode != ActionMode::EventFirst ||
        decision.kind != DecisionKind::SmallChoice ||
        decision.source_card != top_level_action.card_id ||
        decision.n_options <= 0
    ) {
        return false;
    }
    for (int option = 0; option < decision.n_options; ++option) {
        if (decision.eligible_ids[option] != option) {
            return false;
        }
    }
    return true;
}

std::optional<int> choose_deferred_event_first_index(
    const PublicState& pub,
    const EventDecision& decision,
    const torch::Tensor& country_logits,
    CommitPolicyTrace* trace
) {
    auto ops_actions = enumerate_deferred_event_first_actions(pub, decision.source_card, decision.acting_side);
    if (ops_actions.empty()) {
        return std::nullopt;
    }

    if (!country_logits.defined() || country_logits.size(0) <= 0) {
        return std::nullopt;
    }

    float best_score = -std::numeric_limits<float>::infinity();
    std::optional<int> best_choice;
    const ActionEncoding* best_action = nullptr;

    for (int option = 0; option < decision.n_options; ++option) {
        const auto action_index = decision.eligible_ids[option];
        if (action_index < 0 || action_index >= static_cast<int>(ops_actions.size())) {
            continue;
        }
        const auto& candidate = ops_actions[static_cast<size_t>(action_index)];
        const auto score = compute_country_logprob_for_action(pub, decision.acting_side, candidate, country_logits);
        if (!best_choice.has_value() || score > best_score) {
            best_score = score;
            best_choice = option;
            best_action = &candidate;
        }
    }

    if (!best_choice.has_value() || best_action == nullptr) {
        return std::nullopt;
    }

    if (trace != nullptr) {
        trace->deferred_country_used = true;
        trace->deferred_country_mask =
            build_country_mask_for_action(pub, decision.acting_side, best_action->card_id, best_action->mode);
        trace->deferred_country_targets.clear();
        trace->deferred_country_targets.reserve(best_action->targets.size());
        for (const auto target : best_action->targets) {
            trace->deferred_country_targets.push_back(static_cast<int>(target));
        }
        trace->deferred_country_logprob = best_score;
    }

    return best_choice;
}

std::optional<int> argmax_eligible_logit_index(
    const EventDecision& decision,
    const torch::Tensor& logits
) {
    if (!logits.defined() || logits.dim() != 1 || logits.size(0) <= 0 || decision.n_options <= 0) {
        return std::nullopt;
    }

    const auto n_logits = static_cast<int>(logits.size(0));
    float best_score = -std::numeric_limits<float>::infinity();
    std::optional<int> best_choice;
    for (int option = 0; option < decision.n_options; ++option) {
        const auto eligible_id = decision.eligible_ids[option];
        if (eligible_id < 0 || eligible_id >= n_logits) {
            continue;
        }
        const auto score = decode::tensor_at(logits, eligible_id).item<float>();
        if (!best_choice.has_value() || score > best_score) {
            best_score = score;
            best_choice = option;
        }
    }
    return best_choice;
}

PolicyCallbackFn make_commit_policy_callback(
    torch::jit::script::Module& model,
    torch::Device device,
    GameSlot& slot,
    const ActionEncoding& action,
    const torch::Tensor& small_choice_logits,
    CommitPolicyTrace* trace
) {
    return [&model, device, &slot, action, small_choice_logits, trace](
        const PublicState& pub,
        const EventDecision& decision
    ) -> int {
        if (decision.n_options <= 0) {
            return 0;
        }

        std::optional<nn::BatchOutputs> callback_outputs;
        auto ensure_callback_outputs = [&]() -> const nn::BatchOutputs* {
            if (!callback_outputs.has_value()) {
                auto obs = make_observation(slot.root_state, decision.acting_side);
                obs.pub = pub;
                auto frame_context = slot.root_state;
                frame_context.pub = pub;
                frame_context.frame_stack_mode = true;
                frame_context.frame_stack.clear();
                frame_context.frame_stack.push_back(frame_context_from_event_decision(decision));

                nn::BatchInputs callback_inputs;
                callback_inputs.allocate(1, device);
                callback_inputs.fill_slot(0, frame_context, obs.own_hand, obs.holds_china, obs.acting_side);
                callback_outputs = nn::forward_model_batched(model, callback_inputs);
            }
            return &*callback_outputs;
        };

        if (decision.kind == DecisionKind::SmallChoice) {
            if (is_deferred_event_first_choice(action, decision)) {
                const auto* outputs = ensure_callback_outputs();
                if (outputs != nullptr &&
                    outputs->country_logits.defined() &&
                    outputs->country_logits.size(0) > 0) {
                    if (auto choice = choose_deferred_event_first_index(
                            pub,
                            decision,
                            outputs->country_logits.index({0}),
                            trace
                        );
                        choice.has_value()) {
                        return *choice;
                    }
                }
                return 0;
            }

            if (!small_choice_logits.defined() || decision.n_options <= 1) {
                return 0;
            }

            auto masked = small_choice_logits.slice(/*dim=*/0, /*start=*/0, /*end=*/decision.n_options);
            auto log_probs = torch::log_softmax(masked, /*dim=*/0);
            const auto choice = static_cast<int>(masked.argmax(0).item<int64_t>());
            if (trace != nullptr) {
                trace->small_choice_target = choice;
                trace->small_choice_n_options = decision.n_options;
                trace->small_choice_logprob = log_probs[choice].item<float>();
            }
            return choice;
        }

        if (decision.n_options <= 1) {
            return 0;
        }

        if (decision.kind == DecisionKind::CountrySelect) {
            const auto* outputs = ensure_callback_outputs();
            if (outputs == nullptr ||
                !outputs->country_logits.defined() ||
                outputs->country_logits.size(0) <= 0) {
                return 0;
            }
            if (auto choice = argmax_eligible_logit_index(
                    decision,
                    outputs->country_logits.index({0})
                );
                choice.has_value()) {
                return std::clamp(*choice, 0, decision.n_options - 1);
            }
            return 0;
        }

        if (decision.kind == DecisionKind::CardSelect) {
            const auto* outputs = ensure_callback_outputs();
            if (outputs == nullptr ||
                !outputs->card_logits.defined() ||
                outputs->card_logits.size(0) <= 0) {
                return 0;
            }
            if (auto choice = argmax_eligible_logit_index(
                    decision,
                    outputs->card_logits.index({0})
                );
                choice.has_value()) {
                return std::clamp(*choice, 0, decision.n_options - 1);
            }
            return 0;
        }

        return 0;
    };
}

void commit_greedy_action(GameSlot& slot, const ActionEncoding& action, const PolicyCallbackFn* policy_cb = nullptr) {
    if (!slot.decision.has_value()) {
        return;
    }

    auto resolved = action;
    if (resolved.card_id == 0) {
        resolved = choose_action(
            PolicyKind::MinimalHybrid,
            slot.decision->pub_snapshot,
            slot.decision->hand_snapshot,
            slot.decision->holds_china,
            slot.rng
        ).value_or(ActionEncoding{});
    }
    if (resolved.card_id == 0) {
        throw std::runtime_error("greedy benchmark could not resolve an action");
    }

    const auto decision = *slot.decision;
    slot.decision.reset();
    slot.root.reset();
    slot.pending.clear();
    slot.move_done = false;

    if (decision.is_headline) {
        resolved.mode = ActionMode::Event;
        resolved.targets.clear();
        auto& hand = slot.root_state.hands[to_index(decision.side)];
        if (hand.test(resolved.card_id)) {
            hand.reset(resolved.card_id);
        }
        // Greedy benchmark doesn't need real SearchResult, use empty.
        slot.pending_headlines[to_index(decision.side)] = PendingHeadlineChoice{
            .side = decision.side,
            .holds_china = decision.holds_china,
            .hand_snapshot = decision.hand_snapshot,
            .action = resolved,
            .search = SearchResult{},
        };
        if (decision.side == Side::USSR) {
            slot.stage = BatchedGameStage::HeadlineChoiceUS;
        } else {
            finalize_headline_choices(slot);
        }
        return;
    }

    auto& hand = slot.root_state.hands[to_index(decision.side)];
    if (hand.test(resolved.card_id)) {
        hand.reset(resolved.card_id);
    }

    auto [new_pub, over, winner] = apply_action_live(slot.root_state, resolved, decision.side, slot.rng, policy_cb);
    (void)new_pub;
    sync_china_flags(slot.root_state);

    if (over) {
        mark_game_done(slot, GameResult{
            .winner = winner,
            .final_vp = slot.root_state.pub.vp,
            .end_turn = slot.root_state.pub.turn,
            .end_reason = end_reason(slot.root_state, winner, resolved.card_id),
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
                    .end_reason = end_reason(slot.root_state, norad_winner),
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
}

}  // anonymous namespace

std::vector<GameResult> benchmark_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int pool_size,
    uint32_t base_seed,
    torch::Device device,
    bool greedy_opponent,
    float temperature,
    bool nash_temperatures
) {
    if (n_games <= 0) {
        return {};
    }
    if (pool_size <= 0) {
        pool_size = std::min(n_games, 64);
    }

    // Use a minimal MCTS config just for GameSlot initialization.
    BatchedMctsConfig config;
    config.pool_size = pool_size;
    config.mcts.n_simulations = 0;  // No tree search.
    config.learned_side = learned_side;
    config.nash_temperatures = nash_temperatures;
    config.record_rows = false;

    std::vector<GameSlot> pool(static_cast<size_t>(pool_size));
    int games_started = 0;
    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(n_games));

    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(pool_size, device);

    // Track which batch slot corresponds to which GameSlot, and whether
    // the learned side needs NN inference for that decision.
    struct BatchEntry {
        GameSlot* slot = nullptr;
        bool needs_nn = false;  // true = learned side, false = heuristic side
    };
    std::vector<BatchEntry> batch_entries;
    batch_entries.reserve(static_cast<size_t>(pool_size));

    while (static_cast<int>(results.size()) < n_games) {
        batch_inputs.reset();
        batch_entries.clear();

        // Collect completed games, start new ones.
        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                results.push_back(slot.result);
                slot.emitted = true;
                slot.active = false;
            }
            if (!slot.active && games_started < n_games) {
                initialize_slot(slot, games_started, base_seed, config);
                games_started += 1;
            }
        }

        // Advance each active game until it needs a decision.
        for (auto& slot : pool) {
            if (!slot.active || slot.game_done) {
                continue;
            }

            if (slot.move_done) {
                // Previous action was resolved; commit it.
                // (should not happen in greedy mode, but handle anyway)
            }

            advance_until_decision(slot, config);
            if (slot.game_done || !slot.decision.has_value()) {
                continue;
            }

            const auto decision_side = slot.decision->side;
            const bool is_learned = (decision_side == learned_side);

            if (is_learned) {
                // Queue for batched NN inference.
                const auto batch_idx = batch_inputs.filled;
                batch_inputs.fill_slot(batch_idx, pending_observation(*slot.decision));
                batch_entries.push_back(BatchEntry{&slot, true});
            } else if (greedy_opponent) {
                // Opponent also uses NN (greedy argmax) — for MCTS-vs-greedy comparison.
                const auto batch_idx = batch_inputs.filled;
                batch_inputs.fill_slot(batch_idx, pending_observation(*slot.decision));
                batch_entries.push_back(BatchEntry{&slot, true});
            } else {
                // Heuristic side: resolve with optional temperature.
                std::optional<ActionEncoding> heuristic_action;
                if (slot.heuristic_temperature > 0.0f) {
                    heuristic_action = choose_minimal_hybrid_sampled(
                        slot.decision->pub_snapshot,
                        slot.decision->hand_snapshot,
                        slot.decision->holds_china,
                        slot.heuristic_temperature,
                        slot.rng
                    );
                } else {
                    heuristic_action = choose_action(
                        PolicyKind::MinimalHybrid,
                        slot.decision->pub_snapshot,
                        slot.decision->hand_snapshot,
                        slot.decision->holds_china,
                        slot.rng
                    );
                }
                commit_greedy_action(slot, heuristic_action.value_or(ActionEncoding{}));
            }
        }

        // Run batched NN inference for all learned-side decisions.
        if (!batch_entries.empty()) {
            const auto outputs = nn::forward_model_batched(model, batch_inputs);
            int batch_idx = 0;
            for (auto& entry : batch_entries) {
                if (!entry.needs_nn) {
                    continue;
                }
                const auto obs = pending_observation(*entry.slot->decision);
                auto action = greedy_action_from_outputs(
                    obs,
                    outputs,
                    static_cast<int64_t>(batch_idx),
                    entry.slot->rng,
                    temperature
                );
                const auto small_choice_logits =
                    outputs.small_choice_logits.defined() && outputs.small_choice_logits.size(0) > batch_idx
                        ? outputs.small_choice_logits[batch_idx]
                        : torch::Tensor{};
                const auto needs_callback =
                    action.mode == ActionMode::EventFirst || small_choice_logits.defined();
                PolicyCallbackFn policy_cb;
                const PolicyCallbackFn* cb_ptr = nullptr;
                if (needs_callback) {
                    policy_cb = make_commit_policy_callback(
                        model,
                        device,
                        *entry.slot,
                        action,
                        small_choice_logits,
                        /*trace=*/nullptr
                    );
                    cb_ptr = &policy_cb;
                }
                commit_greedy_action(*entry.slot, action, cb_ptr);
                batch_idx += 1;
            }
        }
    }

    return results;
}

std::vector<GameResult> benchmark_model_vs_model_batched(
    int n_games,
    torch::jit::script::Module& model_a,
    torch::jit::script::Module& model_b,
    int pool_size,
    uint32_t base_seed,
    torch::Device device,
    float temperature,
    bool nash_temperatures
) {
    if (n_games <= 0) {
        return {};
    }
    // n_games must be even — split into first half (a=USSR) and second half (a=US).
    const int half = n_games / 2;
    const int total = half * 2;

    if (pool_size <= 0) {
        pool_size = std::min(total, 64);
    }

    // game_index [0, half) => model_a plays USSR, model_b plays US
    // game_index [half, total) => model_a plays US,  model_b plays USSR
    auto a_is_ussr = [&](int game_index) -> bool {
        return game_index < half;
    };

    BatchedMctsConfig config;
    config.pool_size = pool_size;
    config.mcts.n_simulations = 0;
    config.learned_side = std::nullopt;  // Both sides use NN.
    config.nash_temperatures = false;    // No heuristic opponent.
    config.record_rows = false;

    std::vector<GameSlot> pool(static_cast<size_t>(pool_size));
    int games_started = 0;
    // Maintain ordered results — allocate slots for all games upfront.
    std::vector<GameResult> results(static_cast<size_t>(total));
    std::vector<bool> result_filled(static_cast<size_t>(total), false);
    int games_finished = 0;

    // Two separate batch input buffers — one per model.
    nn::BatchInputs batch_a, batch_b;
    batch_a.allocate(pool_size, device);
    batch_b.allocate(pool_size, device);

    struct BatchEntry {
        GameSlot* slot = nullptr;
        bool is_model_a = false;
    };
    std::vector<BatchEntry> entries_a, entries_b;
    entries_a.reserve(static_cast<size_t>(pool_size));
    entries_b.reserve(static_cast<size_t>(pool_size));

    while (games_finished < total) {
        batch_a.reset();
        batch_b.reset();
        entries_a.clear();
        entries_b.clear();

        // Collect completed games, start new ones.
        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                const int gi = slot.game_index;
                results[static_cast<size_t>(gi)] = slot.result;
                result_filled[static_cast<size_t>(gi)] = true;
                slot.emitted = true;
                slot.active = false;
                games_finished += 1;
            }
            if (!slot.active && games_started < total) {
                initialize_slot(slot, games_started, base_seed, config);
                games_started += 1;
            }
        }

        // Advance each active game until it needs a decision.
        for (auto& slot : pool) {
            if (!slot.active || slot.game_done) {
                continue;
            }

            advance_until_decision(slot, config);
            if (slot.game_done || !slot.decision.has_value()) {
                continue;
            }

            const auto decision_side = slot.decision->side;
            // Which model acts for this decision?
            // If a_is_ussr(game_index): model_a=USSR, so model_a acts when side==USSR.
            // If !a_is_ussr(game_index): model_a=US, so model_a acts when side==US.
            const bool a_acts = (a_is_ussr(slot.game_index))
                                    ? (decision_side == Side::USSR)
                                    : (decision_side == Side::US);

            if (a_acts) {
                const auto batch_idx = batch_a.filled;
                batch_a.fill_slot(batch_idx, pending_observation(*slot.decision));
                entries_a.push_back(BatchEntry{&slot, true});
            } else {
                const auto batch_idx = batch_b.filled;
                batch_b.fill_slot(batch_idx, pending_observation(*slot.decision));
                entries_b.push_back(BatchEntry{&slot, false});
            }
        }

        // Run batched NN inference for model_a decisions.
        if (!entries_a.empty()) {
            const auto outputs = nn::forward_model_batched(model_a, batch_a);
            int batch_idx = 0;
            for (auto& entry : entries_a) {
                const auto obs = pending_observation(*entry.slot->decision);
                auto action = greedy_action_from_outputs(
                    obs,
                    outputs,
                    static_cast<int64_t>(batch_idx),
                    entry.slot->rng,
                    temperature
                );
                const auto small_choice_logits =
                    outputs.small_choice_logits.defined() && outputs.small_choice_logits.size(0) > batch_idx
                        ? outputs.small_choice_logits[batch_idx]
                        : torch::Tensor{};
                const auto needs_callback =
                    action.mode == ActionMode::EventFirst || small_choice_logits.defined();
                PolicyCallbackFn policy_cb;
                const PolicyCallbackFn* cb_ptr = nullptr;
                if (needs_callback) {
                    policy_cb = make_commit_policy_callback(
                        model_a,
                        device,
                        *entry.slot,
                        action,
                        small_choice_logits,
                        /*trace=*/nullptr
                    );
                    cb_ptr = &policy_cb;
                }
                commit_greedy_action(*entry.slot, action, cb_ptr);
                batch_idx += 1;
            }
        }

        // Run batched NN inference for model_b decisions.
        if (!entries_b.empty()) {
            const auto outputs = nn::forward_model_batched(model_b, batch_b);
            int batch_idx = 0;
            for (auto& entry : entries_b) {
                const auto obs = pending_observation(*entry.slot->decision);
                auto action = greedy_action_from_outputs(
                    obs,
                    outputs,
                    static_cast<int64_t>(batch_idx),
                    entry.slot->rng,
                    temperature
                );
                const auto small_choice_logits =
                    outputs.small_choice_logits.defined() && outputs.small_choice_logits.size(0) > batch_idx
                        ? outputs.small_choice_logits[batch_idx]
                        : torch::Tensor{};
                const auto needs_callback =
                    action.mode == ActionMode::EventFirst || small_choice_logits.defined();
                PolicyCallbackFn policy_cb;
                const PolicyCallbackFn* cb_ptr = nullptr;
                if (needs_callback) {
                    policy_cb = make_commit_policy_callback(
                        model_b,
                        device,
                        *entry.slot,
                        action,
                        small_choice_logits,
                        /*trace=*/nullptr
                    );
                    cb_ptr = &policy_cb;
                }
                commit_greedy_action(*entry.slot, action, cb_ptr);
                batch_idx += 1;
            }
        }
    }

    return results;
}

RolloutResult rollout_model_vs_model_batched(
    int n_games,
    torch::jit::script::Module& model_a,
    torch::jit::script::Module& model_b,
    int pool_size,
    uint32_t base_seed,
    torch::Device device,
    float temperature,
    bool nash_temperatures,
    float dir_alpha,
    float dir_epsilon,
    Side learned_side
) {
    if (n_games <= 0) {
        return {};
    }
    if (temperature <= 0.0f) {
        throw std::invalid_argument("rollout_model_vs_model_batched requires temperature > 0");
    }
    if (pool_size <= 0) {
        pool_size = std::min(n_games, 64);
    }

    // learned_side=Neutral: alternate sides (first half USSR, second half US).
    // learned_side=USSR: model_a always plays USSR.
    // learned_side=US:   model_a always plays US.
    const int half = n_games / 2;
    auto a_is_ussr = [&](int game_index) -> bool {
        if (learned_side == Side::USSR) return true;
        if (learned_side == Side::US)   return false;
        return game_index < half;  // Neutral: alternate
    };

    BatchedMctsConfig config;
    config.pool_size = pool_size;
    config.mcts.n_simulations = 0;
    config.nash_temperatures = nash_temperatures;
    config.record_rows = false;
    config.mcts.dir_alpha = dir_alpha;
    config.mcts.dir_epsilon = dir_epsilon;

    std::vector<GameSlot> pool(static_cast<size_t>(pool_size));
    int games_started = 0;
    int games_finished = 0;
    std::vector<std::optional<GameResult>> ordered_results(static_cast<size_t>(n_games));
    std::vector<std::vector<RolloutStep>> steps_by_game(static_cast<size_t>(n_games));

    // Separate batch buffers: model_a batch (steps recorded) and model_b batch (greedy only).
    nn::BatchInputs batch_a;
    batch_a.allocate(pool_size, device);
    nn::BatchInputs batch_b;
    batch_b.allocate(pool_size, device);

    struct BatchEntry {
        GameSlot* slot = nullptr;
        int game_index = -1;
    };
    std::vector<BatchEntry> entries_a;
    std::vector<BatchEntry> entries_b;
    entries_a.reserve(static_cast<size_t>(pool_size));
    entries_b.reserve(static_cast<size_t>(pool_size));

    while (games_finished < n_games) {
        batch_a.reset();
        batch_b.reset();
        entries_a.clear();
        entries_b.clear();

        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                ordered_results[static_cast<size_t>(slot.game_index)] = slot.result;
                slot.emitted = true;
                slot.active = false;
                games_finished += 1;
            }
            if (!slot.active && games_started < n_games) {
                initialize_slot(slot, games_started, base_seed, config);
                games_started += 1;
            }
        }

        for (auto& slot : pool) {
            if (!slot.active || slot.game_done) {
                continue;
            }

            advance_until_decision(slot, config);
            if (slot.game_done || !slot.decision.has_value()) {
                continue;
            }

            const auto decision_side = slot.decision->side;
            // Determine whether model_a is acting this decision.
            const bool a_acts =
                a_is_ussr(slot.game_index)
                    ? (decision_side == Side::USSR)
                    : (decision_side == Side::US);

            if (a_acts) {
                batch_a.fill_slot(batch_a.filled, pending_observation(*slot.decision));
                entries_a.push_back(BatchEntry{&slot, slot.game_index});
            } else {
                batch_b.fill_slot(batch_b.filled, pending_observation(*slot.decision));
                entries_b.push_back(BatchEntry{&slot, slot.game_index});
            }
        }

        // model_a batch: rollout_action_from_outputs records steps.
        if (!entries_a.empty()) {
            const auto outputs_a = nn::forward_model_batched(model_a, batch_a);
            for (int batch_idx = 0; batch_idx < static_cast<int>(entries_a.size()); ++batch_idx) {
                auto& entry = entries_a[static_cast<size_t>(batch_idx)];
                const auto obs = pending_observation(*entry.slot->decision);
                auto [action, step] = rollout_action_from_outputs(
                    obs,
                    batch_a,
                    outputs_a,
                    static_cast<int64_t>(batch_idx),
                    entry.slot->rng,
                    temperature,
                    entry.game_index,
                    device
                );
                if (step.card_idx >= 0) {
                    // Populate raw game state for future re-encoding.
                    const auto& pub = entry.slot->root_state.pub;
                    step.raw_turn   = pub.turn;
                    step.raw_ar     = pub.ar;
                    step.raw_defcon = pub.defcon;
                    step.raw_vp     = pub.vp;
                    step.raw_milops = {pub.milops[0], pub.milops[1]};
                    step.raw_space  = {pub.space[0], pub.space[1]};
                    for (int c = 0; c < kCountrySlots; ++c) {
                        step.raw_ussr_influence[static_cast<size_t>(c)] = pub.influence[0][c];
                        step.raw_us_influence[static_cast<size_t>(c)]   = pub.influence[1][c];
                    }
                    const auto& hand =
                        entry.slot->root_state.hands[to_index(entry.slot->decision->side)];
                    step.hand_card_ids.clear();
                    for (int card = 1; card <= kMaxCardId; ++card) {
                        if (hand.test(static_cast<size_t>(card))) {
                            step.hand_card_ids.push_back(card);
                        }
                    }
                    steps_by_game[static_cast<size_t>(entry.game_index)].push_back(std::move(step));
                }
                const auto original_country_logprob =
                    outputs_a.country_logits.defined() && outputs_a.country_logits.size(0) > batch_idx
                        ? compute_country_logprob_for_action(
                              obs.pub,
                              obs.acting_side,
                              action,
                              outputs_a.country_logits.index({static_cast<int64_t>(batch_idx)})
                          )
                        : 0.0f;
                CommitPolicyTrace trace;
                const auto small_choice_logits =
                    outputs_a.small_choice_logits.defined() && outputs_a.small_choice_logits.size(0) > batch_idx
                        ? outputs_a.small_choice_logits[batch_idx]
                        : torch::Tensor{};
                const auto needs_callback =
                    action.mode == ActionMode::EventFirst || small_choice_logits.defined();
                PolicyCallbackFn policy_cb;
                const PolicyCallbackFn* cb_ptr = nullptr;
                if (needs_callback) {
                    policy_cb = make_commit_policy_callback(
                        model_a,
                        device,
                        *entry.slot,
                        action,
                        small_choice_logits,
                        &trace
                    );
                    cb_ptr = &policy_cb;
                }
                commit_greedy_action(*entry.slot, action, cb_ptr);
                if (trace.small_choice_target >= 0 && step.card_idx >= 0) {
                    auto& game_steps = steps_by_game[static_cast<size_t>(entry.game_index)];
                    if (!game_steps.empty()) {
                        game_steps.back().small_choice_target = trace.small_choice_target;
                        game_steps.back().small_choice_n_options = trace.small_choice_n_options;
                        game_steps.back().small_choice_logprob = trace.small_choice_logprob;
                    }
                }
                if (trace.deferred_country_used && step.card_idx >= 0) {
                    auto& game_steps = steps_by_game[static_cast<size_t>(entry.game_index)];
                    if (!game_steps.empty()) {
                        game_steps.back().country_mask = trace.deferred_country_mask;
                        game_steps.back().country_targets = trace.deferred_country_targets;
                        game_steps.back().log_prob +=
                            trace.deferred_country_logprob - original_country_logprob;
                    }
                }
            }
        }

        // model_b batch: greedy_action_from_outputs, no step recording.
        if (!entries_b.empty()) {
            const auto outputs_b = nn::forward_model_batched(model_b, batch_b);
            for (int batch_idx = 0; batch_idx < static_cast<int>(entries_b.size()); ++batch_idx) {
                auto& entry = entries_b[static_cast<size_t>(batch_idx)];
                const auto obs = pending_observation(*entry.slot->decision);
                auto action = greedy_action_from_outputs(
                    obs,
                    outputs_b,
                    static_cast<int64_t>(batch_idx),
                    entry.slot->rng,
                    temperature
                );
                const auto small_choice_logits =
                    outputs_b.small_choice_logits.defined() && outputs_b.small_choice_logits.size(0) > batch_idx
                        ? outputs_b.small_choice_logits[batch_idx]
                        : torch::Tensor{};
                const auto needs_callback =
                    action.mode == ActionMode::EventFirst || small_choice_logits.defined();
                PolicyCallbackFn policy_cb;
                const PolicyCallbackFn* cb_ptr = nullptr;
                if (needs_callback) {
                    policy_cb = make_commit_policy_callback(
                        model_b,
                        device,
                        *entry.slot,
                        action,
                        small_choice_logits,
                        /*trace=*/nullptr
                    );
                    cb_ptr = &policy_cb;
                }
                commit_greedy_action(*entry.slot, action, cb_ptr);
            }
        }
    }

    RolloutResult result;
    result.results.reserve(static_cast<size_t>(n_games));
    result.game_boundaries.reserve(static_cast<size_t>(n_games));

    size_t total_steps = 0;
    for (const auto& game_steps : steps_by_game) {
        total_steps += game_steps.size();
    }
    result.steps.reserve(total_steps);

    int offset = 0;
    for (int game_index = 0; game_index < n_games; ++game_index) {
        result.game_boundaries.push_back(offset);
        const auto& maybe_result = ordered_results[static_cast<size_t>(game_index)];
        if (!maybe_result.has_value()) {
            throw std::runtime_error("rollout_model_vs_model_batched missing ordered game result");
        }
        result.results.push_back(*maybe_result);

        auto& game_steps = steps_by_game[static_cast<size_t>(game_index)];
        offset += static_cast<int>(game_steps.size());
        for (auto& step : game_steps) {
            result.steps.push_back(std::move(step));
        }
    }

    return result;
}

RolloutResult rollout_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int pool_size,
    uint32_t base_seed,
    torch::Device device,
    float temperature,
    bool nash_temperatures,
    float dir_alpha,
    float dir_epsilon
) {
    if (n_games <= 0) {
        return {};
    }
    if (temperature <= 0.0f) {
        throw std::invalid_argument("rollout_games_batched requires temperature > 0");
    }
    if (pool_size <= 0) {
        pool_size = std::min(n_games, 64);
    }

    BatchedMctsConfig config;
    config.pool_size = pool_size;
    config.mcts.n_simulations = 0;
    config.learned_side = learned_side;
    config.nash_temperatures = nash_temperatures;
    config.record_rows = false;
    config.mcts.dir_alpha = dir_alpha;
    config.mcts.dir_epsilon = dir_epsilon;

    std::vector<GameSlot> pool(static_cast<size_t>(pool_size));
    int games_started = 0;
    int games_finished = 0;
    std::vector<std::optional<GameResult>> ordered_results(static_cast<size_t>(n_games));
    std::vector<std::vector<RolloutStep>> steps_by_game(static_cast<size_t>(n_games));

    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(pool_size, device);

    std::vector<GameSlot*> batch_slots;
    batch_slots.reserve(static_cast<size_t>(pool_size));

    while (games_finished < n_games) {
        batch_inputs.reset();
        batch_slots.clear();

        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                ordered_results[static_cast<size_t>(slot.game_index)] = slot.result;
                slot.emitted = true;
                slot.active = false;
                games_finished += 1;
            }
            if (!slot.active && games_started < n_games) {
                initialize_slot(slot, games_started, base_seed, config);
                games_started += 1;
            }
        }

        for (auto& slot : pool) {
            if (!slot.active || slot.game_done) {
                continue;
            }

            advance_until_decision(slot, config);
            if (slot.game_done || !slot.decision.has_value()) {
                continue;
            }

            const auto decision_side = slot.decision->side;
            if (decision_side == learned_side) {
                const auto batch_idx = batch_inputs.filled;
                batch_inputs.fill_slot(batch_idx, pending_observation(*slot.decision));
                batch_slots.push_back(&slot);
            } else {
                std::optional<ActionEncoding> heuristic_action;
                if (slot.heuristic_temperature > 0.0f) {
                    heuristic_action = choose_minimal_hybrid_sampled(
                        slot.decision->pub_snapshot,
                        slot.decision->hand_snapshot,
                        slot.decision->holds_china,
                        slot.heuristic_temperature,
                        slot.rng
                    );
                } else {
                    heuristic_action = choose_action(
                        PolicyKind::MinimalHybrid,
                        slot.decision->pub_snapshot,
                        slot.decision->hand_snapshot,
                        slot.decision->holds_china,
                        slot.rng
                    );
                }
                commit_greedy_action(slot, heuristic_action.value_or(ActionEncoding{}));
            }
        }

        if (!batch_slots.empty()) {
            const auto outputs = nn::forward_model_batched(model, batch_inputs);
            for (int batch_idx = 0; batch_idx < static_cast<int>(batch_slots.size()); ++batch_idx) {
                auto* slot = batch_slots[static_cast<size_t>(batch_idx)];
                const auto obs = pending_observation(*slot->decision);
                auto [action, step] = rollout_action_from_outputs(
                    obs,
                    batch_inputs,
                    outputs,
                    static_cast<int64_t>(batch_idx),
                    slot->rng,
                    temperature,
                    slot->game_index,
                    device
                );
                if (step.card_idx >= 0) {
                    // Populate raw game state for future re-encoding.
                    const auto& pub = slot->root_state.pub;
                    step.raw_turn   = pub.turn;
                    step.raw_ar     = pub.ar;
                    step.raw_defcon = pub.defcon;
                    step.raw_vp     = pub.vp;
                    step.raw_milops = {pub.milops[0], pub.milops[1]};
                    step.raw_space  = {pub.space[0], pub.space[1]};
                    for (int c = 0; c < kCountrySlots; ++c) {
                        step.raw_ussr_influence[static_cast<size_t>(c)] = pub.influence[0][c];
                        step.raw_us_influence[static_cast<size_t>(c)]   = pub.influence[1][c];
                    }
                    const auto& hand =
                        slot->root_state.hands[to_index(slot->decision->side)];
                    step.hand_card_ids.clear();
                    for (int card = 1; card <= kMaxCardId; ++card) {
                        if (hand.test(static_cast<size_t>(card))) {
                            step.hand_card_ids.push_back(card);
                        }
                    }
                    steps_by_game[static_cast<size_t>(slot->game_index)].push_back(std::move(step));
                }
                const auto original_country_logprob =
                    outputs.country_logits.defined() && outputs.country_logits.size(0) > batch_idx
                        ? compute_country_logprob_for_action(
                              obs.pub,
                              obs.acting_side,
                              action,
                              outputs.country_logits.index({static_cast<int64_t>(batch_idx)})
                          )
                        : 0.0f;
                CommitPolicyTrace trace;
                const auto small_choice_logits =
                    outputs.small_choice_logits.defined() && outputs.small_choice_logits.size(0) > batch_idx
                        ? outputs.small_choice_logits[batch_idx]
                        : torch::Tensor{};
                const auto needs_callback =
                    action.mode == ActionMode::EventFirst || small_choice_logits.defined();
                PolicyCallbackFn policy_cb;
                const PolicyCallbackFn* cb_ptr = nullptr;
                if (needs_callback) {
                    policy_cb = make_commit_policy_callback(
                        model,
                        device,
                        *slot,
                        action,
                        small_choice_logits,
                        &trace
                    );
                    cb_ptr = &policy_cb;
                }
                commit_greedy_action(*slot, action, cb_ptr);
                if (trace.small_choice_target >= 0 && step.card_idx >= 0) {
                    auto& game_steps = steps_by_game[static_cast<size_t>(slot->game_index)];
                    if (!game_steps.empty()) {
                        game_steps.back().small_choice_target = trace.small_choice_target;
                        game_steps.back().small_choice_n_options = trace.small_choice_n_options;
                        game_steps.back().small_choice_logprob = trace.small_choice_logprob;
                    }
                }
                if (trace.deferred_country_used && step.card_idx >= 0) {
                    auto& game_steps = steps_by_game[static_cast<size_t>(slot->game_index)];
                    if (!game_steps.empty()) {
                        game_steps.back().country_mask = trace.deferred_country_mask;
                        game_steps.back().country_targets = trace.deferred_country_targets;
                        game_steps.back().log_prob +=
                            trace.deferred_country_logprob - original_country_logprob;
                    }
                }
            }
        }
    }

    RolloutResult result;
    result.results.reserve(static_cast<size_t>(n_games));
    result.game_boundaries.reserve(static_cast<size_t>(n_games));

    size_t total_steps = 0;
    for (const auto& game_steps : steps_by_game) {
        total_steps += game_steps.size();
    }
    result.steps.reserve(total_steps);

    int offset = 0;
    for (int game_index = 0; game_index < n_games; ++game_index) {
        result.game_boundaries.push_back(offset);
        const auto& maybe_result = ordered_results[static_cast<size_t>(game_index)];
        if (!maybe_result.has_value()) {
            throw std::runtime_error("rollout_games_batched missing ordered game result");
        }
        result.results.push_back(*maybe_result);

        auto& game_steps = steps_by_game[static_cast<size_t>(game_index)];
        offset += static_cast<int>(game_steps.size());
        for (auto& step : game_steps) {
            result.steps.push_back(std::move(step));
        }
    }

    return result;
}

RolloutResult rollout_self_play_batched(
    int n_games,
    torch::jit::script::Module& model,
    int pool_size,
    uint32_t base_seed,
    torch::Device device,
    float temperature,
    bool nash_temperatures
) {
    if (n_games <= 0) {
        return {};
    }
    if (temperature <= 0.0f) {
        throw std::invalid_argument("rollout_self_play_batched requires temperature > 0");
    }
    if (pool_size <= 0) {
        pool_size = std::min(n_games, 64);
    }

    BatchedMctsConfig config;
    config.pool_size = pool_size;
    config.mcts.n_simulations = 0;
    config.nash_temperatures = nash_temperatures;
    config.record_rows = false;

    std::vector<GameSlot> pool(static_cast<size_t>(pool_size));
    int games_started = 0;
    int games_finished = 0;
    std::vector<std::optional<GameResult>> ordered_results(static_cast<size_t>(n_games));
    std::vector<std::vector<RolloutStep>> steps_by_game(static_cast<size_t>(n_games));

    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(pool_size, device);

    std::vector<GameSlot*> batch_slots;
    batch_slots.reserve(static_cast<size_t>(pool_size));

    while (games_finished < n_games) {
        batch_inputs.reset();
        batch_slots.clear();

        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                ordered_results[static_cast<size_t>(slot.game_index)] = slot.result;
                slot.emitted = true;
                slot.active = false;
                games_finished += 1;
            }
            if (!slot.active && games_started < n_games) {
                initialize_slot(slot, games_started, base_seed, config);
                games_started += 1;
            }
        }

        for (auto& slot : pool) {
            if (!slot.active || slot.game_done) {
                continue;
            }

            advance_until_decision(slot, config);
            if (slot.game_done || !slot.decision.has_value()) {
                continue;
            }

            const auto batch_idx = batch_inputs.filled;
            batch_inputs.fill_slot(batch_idx, pending_observation(*slot.decision));
            batch_slots.push_back(&slot);
        }

        if (!batch_slots.empty()) {
            const auto outputs = nn::forward_model_batched(model, batch_inputs);
            for (int batch_idx = 0; batch_idx < static_cast<int>(batch_slots.size()); ++batch_idx) {
                auto* slot = batch_slots[static_cast<size_t>(batch_idx)];
                const auto obs = pending_observation(*slot->decision);
                auto [action, step] = rollout_action_from_outputs(
                    obs,
                    batch_inputs,
                    outputs,
                    static_cast<int64_t>(batch_idx),
                    slot->rng,
                    temperature,
                    slot->game_index,
                    device
                );
                if (step.card_idx >= 0) {
                    // Populate raw game state for future re-encoding.
                    const auto& pub = slot->root_state.pub;
                    step.raw_turn   = pub.turn;
                    step.raw_ar     = pub.ar;
                    step.raw_defcon = pub.defcon;
                    step.raw_vp     = pub.vp;
                    step.raw_milops = {pub.milops[0], pub.milops[1]};
                    step.raw_space  = {pub.space[0], pub.space[1]};
                    for (int c = 0; c < kCountrySlots; ++c) {
                        step.raw_ussr_influence[static_cast<size_t>(c)] = pub.influence[0][c];
                        step.raw_us_influence[static_cast<size_t>(c)]   = pub.influence[1][c];
                    }
                    const auto& hand =
                        slot->root_state.hands[to_index(slot->decision->side)];
                    step.hand_card_ids.clear();
                    for (int card = 1; card <= kMaxCardId; ++card) {
                        if (hand.test(static_cast<size_t>(card))) {
                            step.hand_card_ids.push_back(card);
                        }
                    }
                    steps_by_game[static_cast<size_t>(slot->game_index)].push_back(std::move(step));
                }
                const auto original_country_logprob =
                    outputs.country_logits.defined() && outputs.country_logits.size(0) > batch_idx
                        ? compute_country_logprob_for_action(
                              obs.pub,
                              obs.acting_side,
                              action,
                              outputs.country_logits.index({static_cast<int64_t>(batch_idx)})
                          )
                        : 0.0f;
                CommitPolicyTrace trace;
                const auto small_choice_logits =
                    outputs.small_choice_logits.defined() && outputs.small_choice_logits.size(0) > batch_idx
                        ? outputs.small_choice_logits[batch_idx]
                        : torch::Tensor{};
                const auto needs_callback =
                    action.mode == ActionMode::EventFirst || small_choice_logits.defined();
                PolicyCallbackFn policy_cb;
                const PolicyCallbackFn* cb_ptr = nullptr;
                if (needs_callback) {
                    policy_cb = make_commit_policy_callback(
                        model,
                        device,
                        *slot,
                        action,
                        small_choice_logits,
                        &trace
                    );
                    cb_ptr = &policy_cb;
                }
                commit_greedy_action(*slot, action, cb_ptr);
                if (trace.small_choice_target >= 0 && step.card_idx >= 0) {
                    auto& game_steps = steps_by_game[static_cast<size_t>(slot->game_index)];
                    if (!game_steps.empty()) {
                        game_steps.back().small_choice_target = trace.small_choice_target;
                        game_steps.back().small_choice_n_options = trace.small_choice_n_options;
                        game_steps.back().small_choice_logprob = trace.small_choice_logprob;
                    }
                }
                if (trace.deferred_country_used && step.card_idx >= 0) {
                    auto& game_steps = steps_by_game[static_cast<size_t>(slot->game_index)];
                    if (!game_steps.empty()) {
                        game_steps.back().country_mask = trace.deferred_country_mask;
                        game_steps.back().country_targets = trace.deferred_country_targets;
                        game_steps.back().log_prob +=
                            trace.deferred_country_logprob - original_country_logprob;
                    }
                }
            }
        }
    }

    RolloutResult result;
    result.results.reserve(static_cast<size_t>(n_games));
    result.game_boundaries.reserve(static_cast<size_t>(n_games));

    size_t total_steps = 0;
    for (const auto& game_steps : steps_by_game) {
        total_steps += game_steps.size();
    }
    result.steps.reserve(total_steps);

    int offset = 0;
    for (int game_index = 0; game_index < n_games; ++game_index) {
        result.game_boundaries.push_back(offset);
        const auto& maybe_result = ordered_results[static_cast<size_t>(game_index)];
        if (!maybe_result.has_value()) {
            throw std::runtime_error("rollout_self_play_batched missing ordered game result");
        }
        result.results.push_back(*maybe_result);

        auto& game_steps = steps_by_game[static_cast<size_t>(game_index)];
        offset += static_cast<int>(game_steps.size());
        for (auto& step : game_steps) {
            result.steps.push_back(std::move(step));
        }
    }

    return result;
}

std::vector<GameResult> benchmark_mcts_vs_greedy(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int n_simulations,
    int pool_size,
    uint32_t base_seed,
    torch::Device device
) {
    return benchmark_mcts(n_games, model, learned_side, n_simulations,
                          pool_size, base_seed, device, /*greedy_nn_opponent=*/true);
}

std::vector<GameResult> benchmark_mcts(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int n_simulations,
    int pool_size,
    uint32_t base_seed,
    torch::Device device,
    bool greedy_nn_opponent,
    bool nash_temperatures,
    int n_mcts_threads,
    int torch_intra_threads,
    int torch_interop_threads,
    int influence_samples,
    float influence_t_strategy,
    float influence_t_country,
    bool influence_proportional_first,
    float min_prior_threshold,
    int top_k_actions,
    float pw_c,
    float pw_alpha,
    float prior_t_card,
    float prior_t_mode,
    float prior_t_country
) {
    BatchedMctsConfig config;
    const bool benchmark_k_sample_mode = influence_samples > 1;
    config.mcts.n_simulations = n_simulations;
    config.pool_size = pool_size;
    config.learned_side = learned_side;
    config.greedy_nn_opponent = greedy_nn_opponent;
    config.nash_temperatures = nash_temperatures;
    config.device = device;
    config.n_mcts_threads = (benchmark_k_sample_mode && n_mcts_threads == 0) ? 1 : n_mcts_threads;
    config.torch_intra_threads = (benchmark_k_sample_mode && torch_intra_threads == 0) ? 1 : torch_intra_threads;
    config.torch_interop_threads = (benchmark_k_sample_mode && torch_interop_threads == 0) ? 1 : torch_interop_threads;
    config.influence_samples = influence_samples;
    config.influence_t_strategy = influence_t_strategy;
    config.influence_t_country = influence_t_country;
    config.influence_proportional_first = influence_proportional_first;
    config.min_prior_threshold = min_prior_threshold;
    config.top_k_actions = top_k_actions;
    config.pw_c = pw_c;
    config.pw_alpha = pw_alpha;
    config.prior_t_card = prior_t_card;
    config.prior_t_mode = prior_t_mode;
    config.prior_t_country = prior_t_country;
    config.verbose_tree_stats = false;
    config.record_rows = false;
    // max_pending=64 maximises NN batch size (vs the old default of 8).
    // The fast-replica README validated that 64–96 gives 4–5× throughput over 8
    // with no change in MCTS correctness (it is a pure batching knob).
    config.max_pending = 64;
    config.virtual_loss_weight = 3;
    config.temperature = 0.0f;
    config.mcts.dir_alpha = 0.3f;
    config.mcts.dir_epsilon = 0.25f;

    std::vector<GameResult> results;
    results.reserve(static_cast<size_t>(n_games));

    // Use a null output stream — we only want game results, not JSONL.
    std::ostringstream null_stream;
    collect_games_batched(n_games, model, config, base_seed, null_stream, &results);
    return results;
}

}  // namespace ts

#endif
