// Determinized information-set MCTS built by sampling hidden opponent hands
// and reusing the native full-state MCTS implementation.

#include "ismcts.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <stdexcept>
#include <utility>

#include "game_loop.hpp"
#include "human_openings.hpp"
#include "policies.hpp"

namespace ts {
namespace {

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

struct AggregatedEdgeState {
    MctsEdge edge;
    int occurrences = 0;
};

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

        // Atomic setup: place from opening tables with +2 bid.
        for (const auto side : {Side::USSR, Side::US}) {
            const SetupOpening* opening = (side == Side::USSR)
                ? choose_random_opening(kHumanUSSROpenings.data(),
                                        static_cast<int>(kHumanUSSROpenings.size()), rng)
                : choose_random_opening(kHumanUSOpeningsBid2.data(),
                                        static_cast<int>(kHumanUSOpeningsBid2.size()), rng);
            if (opening == nullptr) continue;
            for (int j = 0; j < opening->count; ++j) {
                gs.pub.set_influence(side, opening->placements[j].country,
                    gs.pub.influence_of(side, opening->placements[j].country) + opening->placements[j].amount);
            }
        }
        gs.setup_influence_remaining = {0, 0};
        gs.phase = GamePhase::Headline;

        // ISMCTS policy for learned side: captures &gs to access full state.
        const PolicyFn ismcts_fn = [&gs, &model, &config](
            const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng
        ) -> std::optional<ActionEncoding> {
            const auto acting = pub.phasing;
            const auto opp_idx = to_index(other_side(acting));
            auto opp_hand_size = static_cast<int>(gs.hands[opp_idx].count());
            if (gs.hands[opp_idx].test(kChinaCardId)) {
                --opp_hand_size;
            }
            auto result = ismcts_search(gs, acting, opp_hand_size, model, config, rng);
            return result.best_action;
        };

        const PolicyFn heuristic_fn = [](
            const PublicState& pub, const CardSet& hand, bool holds_china, Pcg64Rng& rng
        ) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
        };

        GameLoopConfig loop_config;
        loop_config.skip_setup_influence = true;  // already done above

        const auto& ussr_fn = (learned_side == Side::USSR) ? ismcts_fn : heuristic_fn;
        const auto& us_fn = (learned_side == Side::US) ? ismcts_fn : heuristic_fn;

        auto traced = play_game_traced_from_state_ref_with_rng(gs, ussr_fn, us_fn, rng, loop_config);
        results.push_back(std::move(traced.result));
    }
    return results;
}

}  // namespace ts

#endif
