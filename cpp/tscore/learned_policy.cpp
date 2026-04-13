// TorchScript model loading and native action selection for learned-policy
// matchups and collection.

#include "learned_policy.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <limits>
#include <stdexcept>
#include <tuple>

#include <torch/torch.h>

#include "card_properties.hpp"
#include "game_data.hpp"
#include "nn_features.hpp"
#include "policies.hpp"

namespace ts {
namespace {

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

    auto ops = effective_ops(card_id, pub, side);
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

}  // namespace

TorchScriptPolicy::TorchScriptPolicy(std::string model_path, bool use_country_head)
    : model_path_(std::move(model_path)),
      use_country_head_(use_country_head),
      module_(torch::jit::load(model_path_)) {
    module_.eval();
}

void TorchScriptPolicy::set_exploration_rate(float exploration_rate) {
    if (exploration_rate < 0.0f || exploration_rate > 1.0f) {
        throw std::invalid_argument("exploration_rate must be in [0, 1]");
    }
    exploration_rate_ = exploration_rate;
}

std::optional<ActionEncoding> TorchScriptPolicy::choose_action(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    Pcg64Rng& rng
) {
    const auto side = pub.phasing;
    auto playable = legal_cards(hand, pub, side, holds_china);
    if (playable.empty()) {
        return std::nullopt;
    }
    if (exploration_rate_ > 0.0f && rng.bernoulli(static_cast<double>(exploration_rate_))) {
        auto legal_actions = enumerate_actions(hand, pub, side, holds_china);
        if (legal_actions.empty()) {
            return std::nullopt;
        }
        return legal_actions[rng.choice_index(legal_actions.size())];
    }

    const auto outputs = nn::forward_model(module_, pub, hand, holds_china, side);
    const auto card_logits = get_tensor(outputs, "card_logits").index({0});
    const auto mode_logits = get_tensor(outputs, "mode_logits").index({0});
    const auto country_logits_raw = get_tensor(outputs, "country_logits", false);
    const auto strategy_logits_raw = get_tensor(outputs, "strategy_logits", false);
    const auto country_strategy_logits_raw = get_tensor(outputs, "country_strategy_logits", false);

    // Cards whose event drops DEFCON or triggers a coup as part of the effect.
    // Canonical list in cpp/tscore/card_properties.hpp.
    using tscore::kDefconLoweringCards;

    auto masked_card = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto card_id : playable) {
        // DEFCON safety at card-selection level: opponent-owned danger cards cannot be
        // played safely because their event fires automatically (regardless of selected
        // mode), dropping DEFCON by 1.
        //
        // At DEFCON 2: any ops mode or Event with an opponent danger card = instant loss.
        //
        // At DEFCON 3 during headline (ar=0): the opponent's headline may fire first
        // and drop DEFCON to 2; if our headline then fires a DEFCON-lowering event, it
        // drops to 1 = nuclear war.  Block opponent danger cards in headline at DEFCON 3.
        const bool in_danger_list = std::find(
            kDefconLoweringCards.begin(), kDefconLoweringCards.end(),
            static_cast<int>(card_id)
        ) != kDefconLoweringCards.end();
        if (in_danger_list) {
            const auto& card_info = card_spec(card_id);
            const bool is_opponent_card = (card_info.side != side && card_info.side != Side::Neutral);
            const bool is_neutral_card = (card_info.side == Side::Neutral);
            if (is_opponent_card) {
                // Opponent danger card: event fires for any ops mode → always unsafe at DEFCON 2.
                if (pub.defcon <= 2) {
                    continue;  // leave as -inf
                }
                // Headline at DEFCON 3: opponent headline may fire first → DEFCON 2
                // → our event fires at DEFCON 2 → DEFCON-1.
                if (pub.defcon == 3 && pub.ar == 0) {
                    continue;  // leave as -inf
                }
            }
            if (is_neutral_card && pub.ar == 0) {
                // Neutral danger card played as headline Event at DEFCON 2 can lower
                // DEFCON to 1.  Also block at DEFCON 3 headline since the opponent's
                // headline may fire first and drop DEFCON to 2.
                if (pub.defcon <= 3) {
                    continue;  // leave as -inf
                }
            }
        }
        const auto index = static_cast<int64_t>(card_id - 1);
        masked_card.index_put_({index}, tensor_at(card_logits, index));
    }
    // If all cards were masked (e.g. full hand is opponent danger cards at DEFCON 2),
    // delegate to MinimalHybrid which has its own DEFCON safety logic.
    // Do NOT restore opponent danger cards — that would allow DEFCON-lowering events.
    {
        auto all_masked = true;
        for (const auto card_id : playable) {
            const auto index = static_cast<int64_t>(card_id - 1);
            if (tensor_at(masked_card, index).item<float>() > -std::numeric_limits<float>::infinity()) {
                all_masked = false;
                break;
            }
        }
        if (all_masked) {
            return ts::choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
        }
    }
    auto sampled_card_id = static_cast<CardId>(masked_card.argmax(/*dim=*/0).item<int64_t>() + 1);

    auto modes = legal_modes(sampled_card_id, pub, side);
    if (modes.empty()) {
        return std::nullopt;
    }
    auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
    for (const auto mode : modes) {
        const auto index = static_cast<int64_t>(static_cast<int>(mode));
        masked_mode.index_put_({index}, tensor_at(mode_logits, index));
    }
    auto mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());

    // DEFCON safety: never coup at DEFCON 2 (drops to 1 = instant loss).
    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return std::nullopt;
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto legal_mode : modes) {
            const auto index = static_cast<int64_t>(static_cast<int>(legal_mode));
            masked_mode.index_put_({index}, tensor_at(mode_logits, index));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    // DEFCON safety: never fire an event that lowers DEFCON or triggers a coup
    // when DEFCON is already at 2 — that would drop to 1 and trigger nuclear war.
    // kDefconLoweringCards is defined above in the card-selection block.
    const bool is_defcon_lowering = pub.defcon <= 2 &&
        mode == ActionMode::Event &&
        std::find(kDefconLoweringCards.begin(), kDefconLoweringCards.end(), static_cast<int>(sampled_card_id))
            != kDefconLoweringCards.end();
    if (is_defcon_lowering) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        if (modes.empty()) {
            return std::nullopt;
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto legal_mode : modes) {
            const auto index = static_cast<int64_t>(static_cast<int>(legal_mode));
            masked_mode.index_put_({index}, tensor_at(mode_logits, index));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    // Re-apply coup guard: the event guard above may have changed mode to Coup.
    // Any coup at DEFCON 2 drops DEFCON to 1 (instant loss for phasing player).
    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return std::nullopt;
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto legal_mode : modes) {
            const auto index = static_cast<int64_t>(static_cast<int>(legal_mode));
            masked_mode.index_put_({index}, tensor_at(mode_logits, index));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    // Belt-and-suspenders DEFCON safety gate (covers all modes).
    // Playing an opponent-owned danger card via ops (Influence/Coup/Realign/Space)
    // fires the event automatically, potentially dropping DEFCON.
    if (pub.defcon <= 2) {
        const bool in_danger = std::find(
            kDefconLoweringCards.begin(), kDefconLoweringCards.end(),
            static_cast<int>(sampled_card_id)
        ) != kDefconLoweringCards.end();
        if (in_danger) {
            const auto& ci = card_spec(sampled_card_id);
            const bool event_fires_for_any_mode = (ci.side != side && ci.side != Side::Neutral);
            const bool event_fires_for_event_space =
                (mode == ActionMode::Event) ||
                (mode == ActionMode::Space && event_fires_for_any_mode);
            if (event_fires_for_any_mode || event_fires_for_event_space) {
                return ts::choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
            }
        }
    }

    if (mode == ActionMode::Event || mode == ActionMode::Space) {
        return ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {}};
    }

    if (use_country_head_ && country_logits_raw.defined()) {
        const auto country_logits = country_logits_raw.index({0});
        const auto strategy_logits = strategy_logits_raw.defined() ? strategy_logits_raw.index({0}) : torch::Tensor{};
        const auto country_strategy_logits = country_strategy_logits_raw.defined() ? country_strategy_logits_raw.index({0}) : torch::Tensor{};
        auto action = build_action_from_country_logits(
            sampled_card_id,
            mode,
            country_logits,
            pub,
            side,
            strategy_logits,
            country_strategy_logits
        );
        if (!action.targets.empty()) {
            return action;
        }
    }

    // Fallback: no country head or it returned no targets. Sample countries
    // randomly for the already DEFCON-safe (sampled_card_id, mode) pair instead
    // of calling sample_action(), which would pick an entirely new action and
    // could violate the DEFCON guards applied above.
    {
        const auto accessible = accessible_countries_filtered(pub, side, sampled_card_id, mode);
        if (!accessible.empty()) {
            if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
                const auto target = accessible[rng.choice_index(accessible.size())];
                return ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {target}};
            }
            // Influence: distribute ops uniformly at random.
            const auto ops = effective_ops(sampled_card_id, pub, side);
            ActionEncoding action{.card_id = sampled_card_id, .mode = mode, .targets = {}};
            for (int i = 0; i < ops; ++i) {
                action.targets.push_back(accessible[rng.choice_index(accessible.size())]);
            }
            return action;
        }
    }
    // Ultimate fallback: model produced no valid target countries for the chosen card+mode.
    // Use the heuristic (DEFCON-safe) instead of pure random, which could violate DEFCON safety.
    return ts::choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng);
}

}  // namespace ts

#endif
