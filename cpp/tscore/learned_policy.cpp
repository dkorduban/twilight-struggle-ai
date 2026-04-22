// TorchScript model loading and native action selection for learned-policy
// matchups and collection.

#include "learned_policy.hpp"

#if defined(TS_BUILD_TORCH_RUNTIME)

#include <algorithm>
#include <limits>
#include <stdexcept>
#include <tuple>

#include <torch/torch.h>

#include "decode_helpers.hpp"
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

    GameState gs;
    gs.pub = pub;
    const auto outputs = nn::forward_model(module_, gs, hand, holds_china, side);
    const auto card_logits = get_tensor(outputs, "card_logits").index({0});
    const auto mode_logits = get_tensor(outputs, "mode_logits").index({0});
    const auto country_logits_raw = get_tensor(outputs, "country_logits", false);
    const auto marginal_logits_raw = get_tensor(outputs, "marginal_logits", false);
    const auto strategy_logits_raw = get_tensor(outputs, "strategy_logits", false);
    const auto country_strategy_logits_raw = get_tensor(outputs, "country_strategy_logits", false);
    const auto country_logits = country_logits_raw.defined() ? country_logits_raw.index({0}) : torch::Tensor{};
    const auto marginal_logits = (marginal_logits_raw.defined() && marginal_logits_raw.numel() > 0)
        ? marginal_logits_raw.index({0})
        : torch::Tensor{};
    const auto strategy_logits = strategy_logits_raw.defined() ? strategy_logits_raw.index({0}) : torch::Tensor{};
    const auto country_strategy_logits = country_strategy_logits_raw.defined()
        ? country_strategy_logits_raw.index({0}) : torch::Tensor{};

    return decode::choose_action_from_outputs(
        pub,
        hand,
        holds_china,
        use_country_head_,
        card_logits,
        mode_logits,
        country_logits,
        strategy_logits,
        country_strategy_logits,
        rng,
        [](const torch::Tensor& masked_card) -> CardId {
            return static_cast<CardId>(masked_card.argmax(/*dim=*/0).item<int64_t>() + 1);
        },
        [](const torch::Tensor& masked_mode) -> ActionMode {
            return static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
        },
        [&]() { return ts::choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng); },
        []() -> std::optional<ActionEncoding> { return std::nullopt; },
        marginal_logits
    );
}

int TorchScriptPolicy::choose_event_decision(
    const PublicState& pub,
    const EventDecision& decision,
    Pcg64Rng& rng
) {
    const auto n_options = std::clamp(decision.n_options, 0, EventDecision::kMaxEligible);
    if (n_options <= 1) {
        return 0;
    }
    if (exploration_rate_ > 0.0f && rng.bernoulli(static_cast<double>(exploration_rate_))) {
        return static_cast<int>(rng.choice_index(static_cast<size_t>(n_options)));
    }

    const auto side = is_player_side(decision.acting_side) ? decision.acting_side : pub.phasing;
    const auto holds_china = pub.china_held_by == side;

    GameState gs;
    gs.pub = pub;
    gs.frame_stack_mode = true;

    DecisionFrame frame;
    frame.source_card = decision.source_card;
    frame.acting_side = side;
    frame.eligible_n = static_cast<uint8_t>(n_options);

    CardSet hand;
    switch (decision.kind) {
        case DecisionKind::SmallChoice:
            frame.kind = FrameKind::SmallChoice;
            break;
        case DecisionKind::CountrySelect:
            frame.kind = FrameKind::CountryPick;
            for (int option = 0; option < n_options; ++option) {
                const auto country_id = decision.eligible_ids[option];
                if (country_id >= 0 && country_id < kCountrySlots) {
                    frame.eligible_countries.set(static_cast<size_t>(country_id));
                }
            }
            break;
        case DecisionKind::CardSelect:
            frame.kind = FrameKind::CardSelect;
            for (int option = 0; option < n_options; ++option) {
                const auto card_id = decision.eligible_ids[option];
                if (card_id >= 0 && card_id < kCardSlots) {
                    frame.eligible_cards.set(static_cast<size_t>(card_id));
                    hand.set(static_cast<size_t>(card_id));
                }
            }
            break;
    }
    gs.frame_stack.push_back(frame);

    const auto outputs = nn::forward_model(module_, gs, hand, holds_china, side);
    const auto card_logits = get_tensor(outputs, "card_logits").index({0});
    const auto country_logits_raw = get_tensor(outputs, "country_logits", false);
    const auto small_choice_logits_raw = get_tensor(outputs, "small_choice_logits", false);
    const auto country_logits = country_logits_raw.defined() ? country_logits_raw.index({0}) : torch::Tensor{};
    const auto small_choice_logits = small_choice_logits_raw.defined()
        ? small_choice_logits_raw.index({0})
        : torch::Tensor{};

    auto score_option = [&](int option) -> double {
        if (decision.kind == DecisionKind::SmallChoice) {
            if (small_choice_logits.defined() && option < small_choice_logits.size(0)) {
                return small_choice_logits.index({option}).item<double>();
            }
            return 0.0;
        }
        if (decision.kind == DecisionKind::CardSelect) {
            const auto card_id = decision.eligible_ids[option];
            const auto logit_index = card_id - 1;
            if (logit_index >= 0 && logit_index < card_logits.size(0)) {
                return card_logits.index({logit_index}).item<double>();
            }
            return -std::numeric_limits<double>::infinity();
        }

        const auto country_id = decision.eligible_ids[option];
        if (country_logits.defined() && country_id >= 0 && country_id < country_logits.size(0)) {
            return country_logits.index({country_id}).item<double>();
        }
        return -std::numeric_limits<double>::infinity();
    };

    int best_option = 0;
    auto best_score = score_option(0);
    for (int option = 1; option < n_options; ++option) {
        const auto score = score_option(option);
        if (score > best_score) {
            best_score = score;
            best_option = option;
        }
    }
    return best_option;
}

}  // namespace ts

#endif
