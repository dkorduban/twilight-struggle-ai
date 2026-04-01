// Access to canonical card and country spec tables loaded from `data/spec`.

#pragma once

#include <array>
#include <filesystem>
#include <string>
#include <vector>

#include "types.hpp"

namespace ts {

struct SpecTables {
    std::array<std::optional<CardSpec>, kCardSlots> cards;
    std::array<std::optional<CountrySpec>, kCountrySlots> countries;
    std::vector<CardId> all_card_ids;
    std::vector<CountryId> all_country_ids;
};

// Shared read-only spec accessors used throughout the native runtime.
const SpecTables& specs();
const CardSpec& card_spec(CardId card_id);
bool has_card_spec(CardId card_id);
const CountrySpec& country_spec(CountryId country_id);
bool has_country_spec(CountryId country_id);
const std::vector<CardId>& all_card_ids();
const std::vector<CountryId>& all_country_ids();
std::filesystem::path repo_root();
std::filesystem::path spec_dir();

}  // namespace ts
