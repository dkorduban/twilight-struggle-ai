#include <catch2/catch_test_macros.hpp>

#include <algorithm>
#include <array>
#include <limits>
#include <optional>
#include <vector>

#include <torch/torch.h>

#include "decode_helpers.hpp"
#include "game_state.hpp"
#include "policies.hpp"

using namespace ts;

namespace {

torch::Tensor legacy_tensor_at(const torch::Tensor& tensor, int64_t index) {
    return tensor.index({index});
}

int legacy_argmax_index(const torch::Tensor& tensor) {
    return tensor.argmax(/*dim=*/0).item<int>();
}

bool legacy_is_defcon_lowering_card(CardId card_id) {
    static constexpr std::array<int, 13> kDefconLoweringCards = {
        4, 11, 13, 20, 24, 39, 48, 49, 50, 53, 83, 92, 105,
    };
    return std::find(kDefconLoweringCards.begin(), kDefconLoweringCards.end(), static_cast<int>(card_id)) !=
        kDefconLoweringCards.end();
}

std::vector<CountryId> legacy_accessible_countries_filtered(
    const PublicState& pub,
    Side side,
    CardId card_id,
    ActionMode mode
) {
    auto accessible = legal_countries(card_id, mode, pub, side);
    accessible.erase(
        std::remove_if(accessible.begin(), accessible.end(), [](CountryId cid) { return !has_country_spec(cid); }),
        accessible.end()
    );
    return accessible;
}

ActionEncoding legacy_build_action_from_country_logits(
    CardId card_id,
    ActionMode mode,
    const torch::Tensor& country_logits,
    const PublicState& pub,
    Side side,
    const torch::Tensor& strategy_logits,
    const torch::Tensor& country_strategy_logits
) {
    const auto accessible = legacy_accessible_countries_filtered(pub, side, card_id, mode);
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
        masked.index_put_({index}, legacy_tensor_at(source_logits, index));
    }
    const auto probs = torch::softmax(masked, 0);

    if (mode == ActionMode::Coup || mode == ActionMode::Realign) {
        const auto target = static_cast<CountryId>(legacy_argmax_index(probs));
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
            order.emplace_back(-legacy_tensor_at(fractional, index).item<float>(), accessible[i]);
        }
        std::sort(order.begin(), order.end());
        for (int i = 0; i < remainder && i < static_cast<int>(order.size()); ++i) {
            const auto target = order[static_cast<size_t>(i)].second;
            const auto pos = static_cast<long long>(
                std::find(accessible.begin(), accessible.end(), target) - accessible.begin()
            );
            const auto pos64 = static_cast<int64_t>(pos);
            floor_alloc.index_put_({pos64}, legacy_tensor_at(floor_alloc, pos64).item<int64_t>() + 1);
        }
    }

    ActionEncoding action{.card_id = card_id, .mode = mode, .targets = {}};
    for (size_t i = 0; i < accessible.size(); ++i) {
        const auto index = static_cast<int64_t>(i);
        const auto count = legacy_tensor_at(floor_alloc, index).item<int64_t>();
        for (int64_t j = 0; j < count; ++j) {
            action.targets.push_back(accessible[i]);
        }
    }
    return action;
}

ActionEncoding legacy_greedy_decode(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    const torch::Tensor& card_logits,
    const torch::Tensor& mode_logits,
    const torch::Tensor& country_logits_raw,
    const torch::Tensor& strategy_logits_raw,
    const torch::Tensor& country_strategy_logits_raw,
    Pcg64Rng& rng
) {
    const auto side = pub.phasing;

    auto playable = legal_cards(hand, pub, side, holds_china);
    if (playable.empty()) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
            .value_or(ActionEncoding{});
    }

    auto masked_card = torch::full_like(card_logits, -std::numeric_limits<float>::infinity());
    for (const auto card_id : playable) {
        if (legacy_is_defcon_lowering_card(card_id)) {
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
        masked_card.index_put_({index}, legacy_tensor_at(card_logits, index));
    }

    bool all_masked = true;
    for (const auto card_id : playable) {
        const auto index = static_cast<int64_t>(card_id - 1);
        if (legacy_tensor_at(masked_card, index).item<float>() > -std::numeric_limits<float>::infinity()) {
            all_masked = false;
            break;
        }
    }
    if (all_masked) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
            .value_or(ActionEncoding{});
    }

    const auto sampled_card_id = static_cast<CardId>(masked_card.argmax(/*dim=*/0).item<int64_t>() + 1);

    auto modes = legal_modes(sampled_card_id, pub, side);
    if (modes.empty()) {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
            .value_or(ActionEncoding{});
    }

    auto masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
    for (const auto mode : modes) {
        const auto index = static_cast<int64_t>(static_cast<int>(mode));
        masked_mode.index_put_({index}, legacy_tensor_at(mode_logits, index));
    }
    auto mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());

    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto legal_mode : modes) {
            const auto index = static_cast<int64_t>(static_cast<int>(legal_mode));
            masked_mode.index_put_({index}, legacy_tensor_at(mode_logits, index));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    if (pub.defcon <= 2 && mode == ActionMode::Event && legacy_is_defcon_lowering_card(sampled_card_id)) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Event), modes.end());
        if (modes.empty()) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto legal_mode : modes) {
            const auto index = static_cast<int64_t>(static_cast<int>(legal_mode));
            masked_mode.index_put_({index}, legacy_tensor_at(mode_logits, index));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    if (mode == ActionMode::Coup && pub.defcon <= 2) {
        modes.erase(std::remove(modes.begin(), modes.end(), ActionMode::Coup), modes.end());
        if (modes.empty()) {
            return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
                .value_or(ActionEncoding{});
        }
        masked_mode = torch::full_like(mode_logits, -std::numeric_limits<float>::infinity());
        for (const auto legal_mode : modes) {
            const auto index = static_cast<int64_t>(static_cast<int>(legal_mode));
            masked_mode.index_put_({index}, legacy_tensor_at(mode_logits, index));
        }
        mode = static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
    }

    if (pub.defcon <= 2 && legacy_is_defcon_lowering_card(sampled_card_id)) {
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

    if (mode == ActionMode::Event || mode == ActionMode::Space) {
        return ActionEncoding{.card_id = sampled_card_id, .mode = mode, .targets = {}};
    }

    if (country_logits_raw.defined()) {
        auto action = legacy_build_action_from_country_logits(
            sampled_card_id,
            mode,
            country_logits_raw,
            pub,
            side,
            strategy_logits_raw,
            country_strategy_logits_raw
        );
        if (!action.targets.empty()) {
            return action;
        }
    }

    const auto accessible = legacy_accessible_countries_filtered(pub, side, sampled_card_id, mode);
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

ActionEncoding helper_greedy_decode(
    const PublicState& pub,
    const CardSet& hand,
    bool holds_china,
    bool use_country_head,
    const torch::Tensor& card_logits,
    const torch::Tensor& mode_logits,
    const torch::Tensor& country_logits_raw,
    const torch::Tensor& strategy_logits_raw,
    const torch::Tensor& country_strategy_logits_raw,
    Pcg64Rng& rng
) {
    auto heuristic_fallback = [&]() {
        return choose_action(PolicyKind::MinimalHybrid, pub, hand, holds_china, rng)
            .value_or(ActionEncoding{});
    };

    return decode::choose_action_from_outputs(
        pub,
        hand,
        holds_china,
        use_country_head,
        card_logits,
        mode_logits,
        country_logits_raw,
        strategy_logits_raw,
        country_strategy_logits_raw,
        rng,
        [](const torch::Tensor& masked_card) -> CardId {
            return static_cast<CardId>(masked_card.argmax(/*dim=*/0).item<int64_t>() + 1);
        },
        [](const torch::Tensor& masked_mode) -> ActionMode {
            return static_cast<ActionMode>(masked_mode.argmax(/*dim=*/0).item<int64_t>());
        },
        heuristic_fallback,
        heuristic_fallback
    );
}

torch::Tensor make_card_logits(CardId preferred_card) {
    auto logits = torch::full(
        {kMaxCardId},
        -10.0f,
        torch::TensorOptions().dtype(torch::kFloat32)
    );
    logits.index_put_({static_cast<int64_t>(preferred_card - 1)}, 10.0f);
    return logits;
}

torch::Tensor make_mode_logits(ActionMode best_mode, std::optional<ActionMode> second_mode = std::nullopt) {
    auto logits = torch::full({5}, -10.0f, torch::TensorOptions().dtype(torch::kFloat32));
    logits.index_put_({static_cast<int64_t>(static_cast<int>(best_mode))}, 10.0f);
    if (second_mode.has_value()) {
        logits.index_put_({static_cast<int64_t>(static_cast<int>(*second_mode))}, 5.0f);
    }
    return logits;
}

torch::Tensor make_country_logits(CountryId preferred_country) {
    auto logits = torch::full(
        {kCountrySlots},
        -10.0f,
        torch::TensorOptions().dtype(torch::kFloat32)
    );
    logits.index_put_({static_cast<int64_t>(preferred_country)}, 10.0f);
    return logits;
}

}  // namespace

TEST_CASE("decode helper matches legacy greedy decode on fixed positions", "[decode_helpers]") {
    SECTION("country head influence allocation") {
        const auto state = reset_game(7);
        auto pub = state.pub;
        pub.phasing = Side::USSR;
        pub.ar = 1;

        CardSet hand;
        hand.set(30);  // Decolonization
        const auto accessible = legacy_accessible_countries_filtered(pub, Side::USSR, 30, ActionMode::Influence);
        REQUIRE(!accessible.empty());

        const auto card_logits = make_card_logits(30);
        const auto mode_logits = make_mode_logits(ActionMode::Influence);
        const auto country_logits = make_country_logits(accessible.front());

        Pcg64Rng legacy_rng(101);
        Pcg64Rng helper_rng(101);
        const auto legacy = legacy_greedy_decode(
            pub, hand, false, card_logits, mode_logits, country_logits, torch::Tensor{}, torch::Tensor{}, legacy_rng);
        const auto helper = helper_greedy_decode(
            pub, hand, false, true, card_logits, mode_logits, country_logits, torch::Tensor{}, torch::Tensor{}, helper_rng);

        REQUIRE(helper == legacy);
        REQUIRE(helper.mode == ActionMode::Influence);
        REQUIRE_FALSE(helper.targets.empty());
    }

    SECTION("danger card event is filtered at DEFCON 2") {
        const auto state = reset_game(11);
        auto pub = state.pub;
        pub.phasing = Side::USSR;
        pub.defcon = 2;
        pub.ar = 1;

        CardSet hand;
        hand.set(53);  // We Will Bury You
        const auto accessible = legacy_accessible_countries_filtered(pub, Side::USSR, 53, ActionMode::Influence);
        REQUIRE(!accessible.empty());

        const auto card_logits = make_card_logits(53);
        const auto mode_logits = make_mode_logits(ActionMode::Event, ActionMode::Influence);
        const auto country_logits = make_country_logits(accessible.front());

        Pcg64Rng legacy_rng(202);
        Pcg64Rng helper_rng(202);
        const auto legacy = legacy_greedy_decode(
            pub, hand, false, card_logits, mode_logits, country_logits, torch::Tensor{}, torch::Tensor{}, legacy_rng);
        const auto helper = helper_greedy_decode(
            pub, hand, false, true, card_logits, mode_logits, country_logits, torch::Tensor{}, torch::Tensor{}, helper_rng);

        REQUIRE(helper == legacy);
        REQUIRE(helper.mode != ActionMode::Event);
    }

    SECTION("all masked cards fall back to heuristic") {
        const auto state = reset_game(19);
        auto pub = state.pub;
        pub.phasing = Side::USSR;
        pub.defcon = 2;
        pub.ar = 1;

        CardSet hand;
        hand.set(4);  // Duck and Cover as opponent danger card

        const auto card_logits = make_card_logits(4);
        const auto mode_logits = make_mode_logits(ActionMode::Event, ActionMode::Influence);

        Pcg64Rng legacy_rng(303);
        Pcg64Rng helper_rng(303);
        const auto legacy = legacy_greedy_decode(
            pub, hand, false, card_logits, mode_logits, torch::Tensor{}, torch::Tensor{}, torch::Tensor{}, legacy_rng);
        const auto helper = helper_greedy_decode(
            pub, hand, false, false, card_logits, mode_logits, torch::Tensor{}, torch::Tensor{}, torch::Tensor{}, helper_rng);

        REQUIRE(helper == legacy);
        REQUIRE(helper.card_id != 0);
    }

    SECTION("random target fallback stays identical without country head") {
        const auto state = reset_game(23);
        auto pub = state.pub;
        pub.phasing = Side::USSR;
        pub.ar = 1;

        CardSet hand;
        hand.set(30);  // Decolonization
        const auto accessible = legacy_accessible_countries_filtered(pub, Side::USSR, 30, ActionMode::Influence);
        REQUIRE(accessible.size() >= 2);

        const auto card_logits = make_card_logits(30);
        const auto mode_logits = make_mode_logits(ActionMode::Influence);

        Pcg64Rng legacy_rng(404);
        Pcg64Rng helper_rng(404);
        const auto legacy = legacy_greedy_decode(
            pub, hand, false, card_logits, mode_logits, torch::Tensor{}, torch::Tensor{}, torch::Tensor{}, legacy_rng);
        const auto helper = helper_greedy_decode(
            pub, hand, false, false, card_logits, mode_logits, torch::Tensor{}, torch::Tensor{}, torch::Tensor{}, helper_rng);

        REQUIRE(helper == legacy);
        REQUIRE(helper.mode == ActionMode::Influence);
        REQUIRE_FALSE(helper.targets.empty());
    }
}
