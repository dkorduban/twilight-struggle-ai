#pragma once

#include <bitset>
#include <functional>
#include <optional>

#include "types.hpp"

namespace ts {

struct GameState;

enum class FrameKind : uint8_t {
    TopLevelAR = 0,
    SmallChoice = 1,
    CountryPick = 2,
    CardSelect = 3,
    ForcedDiscard = 4,
    CancelChoice = 5,
    FreeOpsInfluence = 6,
    NoradInfluence = 7,
    DeferredOps = 8,
    SetupPlacement = 9,
    Headline = 10,
};

struct DecisionFrame {
    FrameKind kind = FrameKind::TopLevelAR;
    Side acting_side = Side::USSR;
    CardId source_card = 0;
    uint8_t step_index = 0;
    uint8_t total_steps = 1;
    int16_t budget_remaining = -1;
    uint8_t stack_depth = 0;
    CardId parent_card = 0;
    CardSet eligible_cards;
    std::bitset<kCountrySlots> eligible_countries;
    uint8_t eligible_n = 0;
    uint16_t criteria_bits = 0;
};

// Thin action for one frame. Fill the relevant field for the frame kind:
// SmallChoice/CancelChoice/DeferredOps: option_index
// CountryPick/FreeOpsInfluence/NoradInfluence: country_id
// CardSelect/ForcedDiscard: card_id
struct FrameAction {
    int option_index = 0;
    CardId card_id = 0;
    CountryId country_id = 0;
};

struct StepResult {
    bool pushed_subframe = false;
    bool side_changed = false;
    bool game_over = false;
    std::optional<Side> winner;
};

using SubframePolicyFn = std::function<FrameAction(const GameState&, const DecisionFrame&)>;

}  // namespace ts
