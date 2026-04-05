// Wavefront-batched MCTS collection over a pool of concurrent games.

#include "mcts_batched.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <array>
#include <atomic>
#include <condition_variable>
#include <functional>
#include <mutex>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <limits>
#include <map>
#include <sstream>
#include <stdexcept>
#include <thread>
#include <utility>
#include <vector>

#include <torch/torch.h>

#include "game_data.hpp"
#include "human_openings.hpp"
#include "mcts.hpp"
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
constexpr std::array<int, 13> kDefconLoweringCards = {
    4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105,
};

constexpr int kMaxCardLogits = 112;
constexpr int kMaxModeLogits = 8;
constexpr int kMaxCountryLogits = 86;
constexpr int kMaxStrategies = 8;

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

// Simple thread pool that persists across iterations to avoid launch overhead.
class SlotThreadPool {
public:
    explicit SlotThreadPool(int n_threads)
        : n_threads_(std::max(1, n_threads)), done_(false), task_(nullptr) {
        if (n_threads_ <= 1) return;
        workers_.reserve(static_cast<size_t>(n_threads_));
        for (int t = 0; t < n_threads_; ++t) {
            workers_.emplace_back([this, t] { worker_loop(t); });
        }
    }

    ~SlotThreadPool() {
        {
            std::unique_lock<std::mutex> lock(mu_);
            done_ = true;
        }
        cv_start_.notify_all();
        for (auto& w : workers_) w.join();
    }

    template<typename Fn>
    void run(int n_items, Fn&& fn) {
        if (n_threads_ <= 1 || n_items <= 1) {
            for (int i = 0; i < n_items; ++i) fn(i);
            return;
        }
        n_items_ = n_items;
        remaining_.store(n_threads_, std::memory_order_release);
        // Type-erase the lambda
        auto wrapper = [&fn, this](int tid) {
            const int chunk = (n_items_ + n_threads_ - 1) / n_threads_;
            const int lo = tid * chunk;
            const int hi = std::min(lo + chunk, n_items_);
            for (int i = lo; i < hi; ++i) fn(i);
        };
        std::function<void(int)> task_fn = wrapper;
        {
            std::unique_lock<std::mutex> lock(mu_);
            task_ = &task_fn;
            generation_++;
        }
        cv_start_.notify_all();
        // Wait for all workers to finish
        {
            std::unique_lock<std::mutex> lock(mu_);
            cv_done_.wait(lock, [this] { return remaining_.load(std::memory_order_acquire) == 0; });
            task_ = nullptr;
        }
    }

    SlotThreadPool(const SlotThreadPool&) = delete;
    SlotThreadPool& operator=(const SlotThreadPool&) = delete;

private:
    void worker_loop(int tid) {
        uint64_t my_gen = 0;
        for (;;) {
            std::unique_lock<std::mutex> lock(mu_);
            cv_start_.wait(lock, [this, my_gen] { return done_ || generation_ > my_gen; });
            if (done_) return;
            my_gen = generation_;
            auto* fn = task_;
            lock.unlock();

            if (fn) (*fn)(tid);

            if (remaining_.fetch_sub(1, std::memory_order_acq_rel) == 1) {
                cv_done_.notify_one();
            }
        }
    }

    int n_threads_;
    int n_items_ = 0;
    bool done_;
    uint64_t generation_ = 0;
    std::function<void(int)>* task_;
    std::atomic<int> remaining_{0};
    std::mutex mu_;
    std::condition_variable cv_start_;
    std::condition_variable cv_done_;
    std::vector<std::thread> workers_;
};

template<typename Fn>
void parallel_for_slots(int n_slots, Fn&& fn) {
    const int n_threads = std::min(n_slots, static_cast<int>(std::thread::hardware_concurrency()));
    if (n_threads <= 1) {
        for (int i = 0; i < n_slots; ++i) {
            fn(i);
        }
        return;
    }

    std::vector<std::thread> threads;
    threads.reserve(static_cast<size_t>(n_threads));
    const int chunk = (n_slots + n_threads - 1) / n_threads;
    for (int t = 0; t < n_threads; ++t) {
        const int lo = t * chunk;
        const int hi = std::min(lo + chunk, n_slots);
        if (lo >= hi) {
            break;
        }
        threads.emplace_back([&fn, lo, hi] {
            for (int i = lo; i < hi; ++i) {
                fn(i);
            }
        });
    }
    for (auto& thread : threads) {
        thread.join();
    }
}

struct AggregatedVisitCount {
    CardId card_id = 0;
    ActionMode mode = ActionMode::Influence;
    int visits = 0;
};

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

// Expand sub-phase accumulators (for profiling)
static thread_local double g_expand_drafts = 0, g_expand_edges = 0, g_expand_alloc = 0;
static thread_local int g_expand_count = 0;

ExpansionResult expand_from_raw(
    const GameState& state,
    const RawBatchOutputs& raw,
    int batch_index,
    const MctsConfig& config,
    Pcg64Rng& rng
) {
    using XClock = std::chrono::high_resolution_clock;
    auto xt0 = XClock::now();

    auto node = std::make_unique<MctsNode>();
    node->side_to_move = state.pub.phasing;
    node->edges.reserve(64);
    node->children.reserve(64);
    node->applied_actions.reserve(64);

    g_expand_alloc += std::chrono::duration<double>(XClock::now() - xt0).count();
    auto xt1 = XClock::now();

    auto [drafts, cache] = collect_card_drafts_cached(state);

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

    if (raw.country_logits != nullptr) {
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

    g_expand_edges += std::chrono::duration<double>(XClock::now() - xt2).count();
    ++g_expand_count;

    return ExpansionResult{
        .node = std::move(node),
        .leaf_value = evaluate_leaf_value_raw(state, raw.value, raw.value_stride, batch_index, config, rng),
    };
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

// expand_from_outputs removed — replaced by expand_from_raw for performance

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

int best_root_edge_index(const MctsNode& root) {
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

SearchResult build_search_result(const GameSlot& slot) {
    SearchResult result;
    result.total_simulations = slot.sims_completed;
    if (slot.root == nullptr) {
        return result;
    }

    result.root_edges = slot.root->edges;
    result.root_value = mean_root_value(*slot.root);
    const auto best_index = best_root_edge_index(*slot.root);
    if (best_index >= 0) {
        result.best_action = slot.root->applied_actions[static_cast<size_t>(best_index)];
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

void backpropagate_path(std::vector<std::pair<MctsNode*, int>>& path, double leaf_value, int vl_weight) {
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
std::atomic<int64_t> g_cache_hits{0};           // selections where best_cached_depth > 0

SelectionResult select_to_leaf(GameSlot& slot, const BatchedMctsConfig& config) {
    PendingExpansion pend;

    // Phase 1: Walk down the tree selecting edges, deferring state simulation.
    // Track the deepest node with a cached state so we can clone from there.
    MctsNode* node = slot.root.get();
    const GameState* best_cached = &slot.root_state;
    size_t best_cached_depth = 0;  // path index after which best_cached is valid

    // Collect path first without applying actions.
    while (node != nullptr && !node->is_terminal && !node->edges.empty()) {
        const auto edge_index = node->select_edge(config.mcts.c_puct);
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
    if (best_cached_depth > 0) g_cache_hits.fetch_add(1, std::memory_order_relaxed);

    // Phase 2: Clone from the deepest cached state and apply only remaining actions.
    pend.sim_state = clone_game_state(*best_cached);
    for (size_t i = best_cached_depth; i < pend.path.size(); ++i) {
        auto [path_node, path_edge_index] = pend.path[i];
        apply_tree_action(pend.sim_state,
                          path_node->applied_actions[static_cast<size_t>(path_edge_index)],
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

std::string game_id_for(uint32_t base_seed, int game_index) {
    std::ostringstream out;
    out << "mcts_" << base_seed << "_";
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
    slot.root_state = reset_game(seed);
    slot.rng = Pcg64Rng(seed);
    // Run setup influence placement before MCTS begins.
    run_setup_influence_heuristic(slot.root_state, slot.rng);
    slot.game_id = game_id_for(base_seed, game_index);
    slot.turn = 1;
    slot.stage = BatchedGameStage::TurnSetup;
    slot.sims_target = config.mcts.n_simulations;
}

void reset_move_search(GameSlot& slot, const BatchedMctsConfig& config) {
    slot.root.reset();
    slot.pending.clear();
    slot.sims_completed = 0;
    slot.sims_target = config.mcts.n_simulations;
    slot.move_done = false;
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
    if (slot.root_state.pub.glasnost_extra_ar) {
        slot.root_state.pub.glasnost_extra_ar = false;
        slot.stage = BatchedGameStage::ExtraActionRoundUSSR;
        return;
    }
    slot.stage = BatchedGameStage::Cleanup;
}

void move_to_followup_stage_after_extra(GameSlot& slot, Side side) {
    if (side == Side::US && slot.root_state.pub.glasnost_extra_ar) {
        slot.root_state.pub.glasnost_extra_ar = false;
        slot.stage = BatchedGameStage::ExtraActionRoundUSSR;
        return;
    }
    slot.stage = BatchedGameStage::Cleanup;
}

void queue_decision(GameSlot& slot, Side side, int ar, bool is_headline, const BatchedMctsConfig& config) {
    slot.root_state.pub.phasing = side;
    slot.root_state.pub.ar = ar;
    slot.decision = PendingDecision{
        .turn = slot.root_state.pub.turn,
        .ar = ar,
        .move_number = slot.decisions_started + 1,
        .side = side,
        .holds_china = holds_china_for(slot.root_state, side),
        .is_headline = is_headline,
        .pub_snapshot = slot.root_state.pub,
        .hand_snapshot = slot.root_state.hands[to_index(side)],
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
                queue_decision(slot, side, slot.current_ar, /*is_headline=*/false, config);
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

void commit_best_action(GameSlot& slot, const BatchedMctsConfig& config) {
    if (!slot.move_done || !slot.decision.has_value()) {
        return;
    }

    const auto search = build_search_result(slot);
    auto action = search.best_action;

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
        const float temp = effective_temperature(*slot.decision, config);
        if (const auto sampled = sample_action_by_visit_counts(search, temp, slot.rng); sampled.has_value()) {
            action = *sampled;
        }
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
            .search = search,
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
    auto [new_pub, over, winner] = apply_action_live(slot.root_state, action, decision.side, slot.rng);
    (void)new_pub;
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
    std::ostream& out_stream
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

    // Reset cache profiling counters.
    g_cache_selections.store(0);
    g_cache_hits.store(0);
    g_cache_total_depth.store(0);
    g_cache_saved_depth.store(0);

    struct BatchEntry {
        GameSlot* slot = nullptr;
        size_t pending_index = 0;
        int batch_index = 0;
    };

    struct SlotBatchInfo {
        std::vector<std::pair<int, size_t>> entries;
    };

    std::vector<GameSlot> pool(static_cast<size_t>(config.pool_size));
    std::vector<SlotBatchInfo> slot_infos(pool.size());
    int games_started = 0;
    int games_emitted = 0;

    const int max_pending = std::max(1, config.max_pending);
    nn::BatchInputs batch_inputs;
    batch_inputs.allocate(config.pool_size * max_pending);
    std::vector<BatchEntry> batch_entries;
    batch_entries.reserve(static_cast<size_t>(config.pool_size) * static_cast<size_t>(max_pending));

    const int hw_threads = static_cast<int>(std::thread::hardware_concurrency());
    const int n_threads = std::min(config.pool_size, hw_threads);
    SlotThreadPool thread_pool(n_threads);
    // Limit PyTorch intra-op threads to avoid contention with our thread pool.
    // Empirically, 2 PyTorch threads is optimal when CPU threads handle select/expand.
    if (n_threads > 2) {
        at::set_num_threads(2);
    }

    using Clock = std::chrono::high_resolution_clock;
    double t_advance = 0, t_select = 0, t_nn = 0, t_expand = 0;
    int n_batches = 0, total_batch_items = 0;
    int debug_iters = 0;

    while (games_emitted < n_games) {
        batch_inputs.reset();
        batch_entries.clear();
        ++debug_iters;

        auto t0_adv = Clock::now();
        for (auto& slot : pool) {
            if (slot.active && slot.game_done && !slot.emitted) {
                write_game_rows(slot, out_stream);
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

        auto t0_sel = Clock::now();
        std::atomic<int> batch_count{0};
        thread_pool.run(static_cast<int>(pool.size()), [&](int slot_idx) {
            auto& slot = pool[static_cast<size_t>(slot_idx)];
            auto& info = slot_infos[static_cast<size_t>(slot_idx)];
            info.entries.clear();

            if (!slot.active) {
                return;
            }

            if (slot.move_done) {
                commit_best_action(slot, config);
            }
            advance_until_decision(slot, config);
            if (slot.game_done || !slot.decision.has_value()) {
                return;
            }

            // If learned_side is set and this decision is for the opponent,
            // use heuristic immediately — no MCTS search needed.
            if (config.learned_side.has_value() &&
                slot.decision->side != *config.learned_side) {
                // Force immediate heuristic commit by setting sims_target=0.
                slot.sims_target = 0;
                slot.sims_completed = 0;
                slot.move_done = true;
                return;
            }

            if (slot.root == nullptr) {
                if (!slot.pending.empty()) {
                    return;
                }
                if (auto immediate = expand_without_model(slot.root_state, slot.rng); immediate.has_value()) {
                    slot.root = std::move(immediate->node);
                } else {
                    PendingExpansion pend;
                    pend.sim_state = clone_game_state(slot.root_state);
                    pend.is_root_expansion = true;
                    slot.pending.push_back(std::move(pend));
                    const int bi = batch_count.fetch_add(1, std::memory_order_relaxed);
                    batch_inputs.fill_slot(bi,
                        slot.root_state.pub,
                        slot.root_state.hands[to_index(slot.root_state.pub.phasing)],
                        holds_china_for(slot.root_state, slot.root_state.pub.phasing),
                        slot.root_state.pub.phasing);
                    info.entries.emplace_back(bi, slot.pending.size() - 1);
                    return;
                }
            }

            if (slot.sims_completed >= slot.sims_target && slot.pending.empty()) {
                slot.move_done = true;
                return;
            }

            for (;;) {
                const int budget = sims_budget(slot, max_pending);
                if (budget <= 0) {
                    break;
                }
                const auto selection = select_to_leaf(slot, config);
                if (selection.needs_batch) {
                    auto& pend = slot.pending.back();
                    const int bi = batch_count.fetch_add(1, std::memory_order_relaxed);
                    batch_inputs.fill_slot(bi,
                        pend.sim_state.pub,
                        pend.sim_state.hands[to_index(pend.sim_state.pub.phasing)],
                        holds_china_for(pend.sim_state, pend.sim_state.pub.phasing),
                        pend.sim_state.pub.phasing);
                    info.entries.emplace_back(bi, slot.pending.size() - 1);
                } else {
                    slot.sims_completed += 1;
                    if (slot.sims_completed >= slot.sims_target && slot.pending.empty()) {
                        slot.move_done = true;
                        break;
                    }
                }
            }
        });
        t_select += std::chrono::duration<double>(Clock::now() - t0_sel).count();

        batch_inputs.filled = batch_count.load(std::memory_order_relaxed);
        for (size_t slot_idx = 0; slot_idx < pool.size(); ++slot_idx) {
            for (const auto& [batch_index, pending_index] : slot_infos[slot_idx].entries) {
                batch_entries.push_back(BatchEntry{&pool[slot_idx], pending_index, batch_index});
            }
        }

        if (!batch_entries.empty()) {
            auto t0_nn = Clock::now();
            const auto outputs = nn::forward_model_batched(model, batch_inputs);
            const auto raw = RawBatchOutputs::extract(outputs);
            t_nn += std::chrono::duration<double>(Clock::now() - t0_nn).count();
            n_batches += 1;
            total_batch_items += static_cast<int>(batch_entries.size());

            auto t0_exp = Clock::now();
            thread_pool.run(static_cast<int>(pool.size()), [&](int slot_idx) {
                auto& slot = pool[static_cast<size_t>(slot_idx)];
                auto& info = slot_infos[static_cast<size_t>(slot_idx)];
                if (!slot.active) {
                    return;
                }
                for (const auto& [batch_index, pending_index] : info.entries) {
                    auto& pend = slot.pending[pending_index];
                    if (pend.is_root_expansion) {
                        auto expansion = expand_from_raw(pend.sim_state, raw, batch_index, config.mcts, slot.rng);
                        slot.root = std::move(expansion.node);
                        apply_root_dirichlet_noise(*slot.root, config.mcts, slot.rng);
                        if (slot.sims_target == 0) {
                            slot.move_done = true;
                        }
                    } else {
                        auto expansion = expand_from_raw(pend.sim_state, raw, batch_index, config.mcts, slot.rng);
                        auto& [parent, edge_index] = pend.path.back();
                        // Cache the game state at newly expanded nodes whose parent is
                        // frequently visited. This lets select_to_leaf skip prefix actions.
                        if (parent->total_visits >= kCacheVisitThreshold) {
                            expansion.node->cached_state =
                                std::make_unique<GameState>(pend.sim_state);
                        }
                        parent->children[static_cast<size_t>(edge_index)] = std::move(expansion.node);
                        backpropagate_path(pend.path, expansion.leaf_value, config.virtual_loss_weight);
                        slot.sims_completed += 1;
                    }
                }
                slot.pending.clear();
                if (slot.sims_completed >= slot.sims_target && slot.pending.empty()) {
                    slot.move_done = true;
                }
            });
            t_expand += std::chrono::duration<double>(Clock::now() - t0_exp).count();
        }
    }

    const double total = t_advance + t_select + t_nn + t_expand;
    fprintf(stderr, "[MCTS profile] advance=%.3fs select=%.3fs nn=%.3fs expand=%.3fs total=%.3fs\n",
            t_advance, t_select, t_nn, t_expand, total);
    fprintf(stderr, "[MCTS profile] batches=%d items=%d avg_batch=%.1f iters=%d\n",
            n_batches, total_batch_items, n_batches > 0 ? double(total_batch_items) / n_batches : 0.0, debug_iters);
    fprintf(stderr, "[MCTS expand] alloc=%.3fs drafts=%.3fs edges=%.3fs count=%d\n",
            g_expand_alloc, g_expand_drafts, g_expand_edges, g_expand_count);
    const auto cs = g_cache_selections.load();
    const auto ch = g_cache_hits.load();
    const auto cd = g_cache_total_depth.load();
    const auto csd = g_cache_saved_depth.load();
    if (cs > 0) {
        fprintf(stderr, "[MCTS cache] selections=%lld hits=%lld (%.1f%%) avg_depth=%.2f avg_saved=%.2f save_ratio=%.1f%%\n",
                (long long)cs, (long long)ch,
                100.0 * ch / cs,
                (double)cd / cs,
                (double)csd / cs,
                cd > 0 ? 100.0 * csd / cd : 0.0);
    }
}

// ---------------------------------------------------------------------------
// Greedy batched benchmark: same GameSlot/advance_until_decision machinery
// as MCTS collection, but uses a single argmax decode instead of tree search.
// ---------------------------------------------------------------------------

namespace {

// Exact mirror of TorchScriptPolicy::choose_action logic from learned_policy.cpp,
// but reads from BatchOutputs instead of calling forward_model individually.
ActionEncoding greedy_action_from_outputs(
    const GameState& state,
    const nn::BatchOutputs& outputs,
    int64_t batch_index,
    Pcg64Rng& rng
) {
    const auto& pub = state.pub;
    const auto side = pub.phasing;
    const auto holds_china = holds_china_for(state, side);
    const auto& hand = state.hands[to_index(side)];

    auto playable = legal_cards(hand, pub, side, holds_china);
    if (playable.empty()) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
            .value_or(ActionEncoding{});
    }

    const auto card_logits = outputs.card_logits.index({batch_index});
    const auto mode_logits = outputs.mode_logits.index({batch_index});
    const auto country_logits_raw = outputs.country_logits.defined()
        ? outputs.country_logits.index({batch_index}) : torch::Tensor{};
    const auto strategy_logits_raw = outputs.strategy_logits.defined()
        ? outputs.strategy_logits.index({batch_index}) : torch::Tensor{};
    const auto country_strategy_logits_raw = outputs.country_strategy_logits.defined()
        ? outputs.country_strategy_logits.index({batch_index}) : torch::Tensor{};

    // ── Card selection with DEFCON safety (mirrors learned_policy.cpp) ──
    auto masked_card = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto card_id : playable) {
        if (is_defcon_lowering_card(card_id)) {
            const auto& ci = card_spec(card_id);
            const bool is_opp = (ci.side != side && ci.side != Side::Neutral);
            const bool is_neutral = (ci.side == Side::Neutral);
            if (is_opp) {
                if (pub.defcon <= 2) continue;
                if (pub.defcon == 3 && pub.ar == 0) continue;
            }
            if (is_neutral && pub.ar == 0 && pub.defcon <= 3) continue;
        }
        const auto index = static_cast<int64_t>(card_id - 1);
        masked_card.index_put_({index}, tensor_at(card_logits, index));
    }

    // If all masked, fall back to heuristic.
    {
        bool all_masked = true;
        for (const auto card_id : playable) {
            const auto index = static_cast<int64_t>(card_id - 1);
            if (tensor_at(masked_card, index).item<float>() > -std::numeric_limits<float>::infinity()) {
                all_masked = false;
                break;
            }
        }
        if (all_masked) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
    }

    auto sampled_card_id = static_cast<CardId>(masked_card.argmax(/*dim=*/0).item<int64_t>() + 1);

    // ── Mode selection (mirrors learned_policy.cpp) ──
    auto modes = legal_modes(sampled_card_id, pub, side);
    if (modes.empty()) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
            .value_or(ActionEncoding{});
    }

    auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
    for (const auto m : modes) {
        const auto index = static_cast<int64_t>(static_cast<int>(m));
        masked_mode.index_put_({index}, tensor_at(mode_logits, index));
    }
    auto mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());

    // DEFCON safety: no coup at DEFCON ≤ 2.
    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto m : modes) {
            masked_mode.index_put_({static_cast<int64_t>(static_cast<int>(m))}, tensor_at(mode_logits, static_cast<int>(m)));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    // DEFCON safety: no event for DEFCON-lowering cards at DEFCON ≤ 2.
    if (pub.defcon <= 2 && mode == ActionMode::Event && is_defcon_lowering_card(sampled_card_id)) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        if (modes.empty()) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto m : modes) {
            masked_mode.index_put_({static_cast<int64_t>(static_cast<int>(m))}, tensor_at(mode_logits, static_cast<int>(m)));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    // Re-apply coup guard after event guard may have changed mode.
    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto m : modes) {
            masked_mode.index_put_({static_cast<int64_t>(static_cast<int>(m))}, tensor_at(mode_logits, static_cast<int>(m)));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    // Belt-and-suspenders DEFCON safety gate.
    if (pub.defcon <= 2 && is_defcon_lowering_card(sampled_card_id)) {
        const auto& ci = card_spec(sampled_card_id);
        const bool event_fires_for_any_mode = (ci.side != side && ci.side != Side::Neutral);
        const bool event_fires_for_event_space =
            (mode == ActionMode::Event) ||
            (mode == ActionMode::Space && event_fires_for_any_mode);
        if (event_fires_for_any_mode || event_fires_for_event_space) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
    }

    // ── Target selection ──
    if (mode == ActionMode::Event || mode == ActionMode::Space) {
        return ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {}};
    }

    if (country_logits_raw.defined()) {
        auto action = build_action_from_country_logits(
            sampled_card_id, mode, country_logits_raw,
            pub, side, strategy_logits_raw, country_strategy_logits_raw);
        if (!action.targets.empty()) {
            return action;
        }
    }

    // Fallback: random target selection (mirrors learned_policy.cpp).
    const auto accessible = accessible_countries_filtered(pub, side, sampled_card_id, mode);
    if (!accessible.empty()) {
        if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
            const auto target = accessible[rng.choice_index(accessible.size())];
            return ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {target}};
        }
        const auto ops = effective_ops(sampled_card_id, pub, side);
        ActionEncoding action{.card_id = sampled_card_id, .mode = mode, .targets = {}};
        for (int i = 0; i < ops; ++i) {
            action.targets.push_back(accessible[rng.choice_index(accessible.size())]);
        }
        return action;
    }

    return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
        .value_or(ActionEncoding{});
}

void commit_greedy_action(GameSlot& slot, const ActionEncoding& action) {
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

    auto [new_pub, over, winner] = apply_action_live(slot.root_state, resolved, decision.side, slot.rng);
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
}

}  // anonymous namespace

std::vector<GameResult> benchmark_games_batched(
    int n_games,
    torch::jit::script::Module& model,
    Side learned_side,
    int pool_size,
    uint32_t base_seed,
    torch::Device device
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
                batch_inputs.fill_slot(
                    batch_idx,
                    slot.root_state.pub,
                    slot.root_state.hands[to_index(decision_side)],
                    slot.decision->holds_china,
                    decision_side
                );
                batch_entries.push_back(BatchEntry{&slot, true});
            } else {
                // Heuristic side: resolve immediately.
                auto heuristic_action = choose_action(
                    PolicyKind::MinimalHybrid,
                    slot.decision->pub_snapshot,
                    slot.decision->hand_snapshot,
                    slot.decision->holds_china,
                    slot.rng
                ).value_or(ActionEncoding{});
                commit_greedy_action(slot, heuristic_action);
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
                auto action = greedy_action_from_outputs(
                    entry.slot->root_state,
                    outputs,
                    static_cast<int64_t>(batch_idx),
                    entry.slot->rng
                );
                commit_greedy_action(*entry.slot, action);
                batch_idx += 1;
            }
        }
    }

    return results;
}

}  // namespace ts

#endif
