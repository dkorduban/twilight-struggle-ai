// Region scoring and final-scoring helpers for the native engine.

#pragma once

#include "public_state.hpp"

namespace ts {

enum class Tier : uint8_t {
    None = 0,
    Presence = 1,
    Domination = 2,
    Control = 3,
};

ScoringResult score_region(Region region, const PublicState& pub);
ScoringResult score_southeast_asia(const PublicState& pub);
ScoringResult score_asia_final(const PublicState& pub);
int score_asia_china_bonus(const PublicState& pub);
ScoringResult apply_scoring_card(CardId card_id, const PublicState& pub);
ScoringResult apply_final_scoring(PublicState pub);
bool controls_country(Side side, CountryId country_id, const PublicState& pub);

}  // namespace ts
