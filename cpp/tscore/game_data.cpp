// Parsing and caching of canonical card/country specification tables.

#include "game_data.hpp"

#include <algorithm>
#include <cctype>
#include <charconv>
#include <fstream>
#include <mutex>
#include <sstream>
#include <stdexcept>

namespace ts {
namespace {

// Spec CSVs are simple enough that a tiny splitter is easier to audit than
// pulling in a full CSV dependency.
std::string trim(std::string value) {
    auto not_space = [](unsigned char ch) { return !std::isspace(ch); };
    value.erase(value.begin(), std::find_if(value.begin(), value.end(), not_space));
    value.erase(std::find_if(value.rbegin(), value.rend(), not_space).base(), value.end());
    return value;
}

std::vector<std::string> split_csv_row(const std::string& line) {
    std::vector<std::string> out;
    std::string current;
    std::stringstream ss(line);
    while (std::getline(ss, current, ',')) {
        out.push_back(trim(current));
    }
    return out;
}

int parse_int(std::string_view text, int fallback = 0) {
    int value = fallback;
    const auto* begin = text.data();
    const auto* end = begin + text.size();
    const auto result = std::from_chars(begin, end, value);
    if (result.ec != std::errc{}) {
        return fallback;
    }
    return value;
}

bool parse_bool(std::string_view text) {
    return text == "true" || text == "True" || text == "1" || text == "yes";
}

Side parse_side(std::string_view text) {
    if (text == "USSR") {
        return Side::USSR;
    }
    if (text == "US") {
        return Side::US;
    }
    return Side::Neutral;
}

Era parse_era(std::string_view text) {
    if (text == "Mid") {
        return Era::Mid;
    }
    if (text == "Late") {
        return Era::Late;
    }
    return Era::Early;
}

Region parse_region(std::string_view text) {
    if (text == "Asia") {
        return Region::Asia;
    }
    if (text == "MiddleEast") {
        return Region::MiddleEast;
    }
    if (text == "CentralAmerica") {
        return Region::CentralAmerica;
    }
    if (text == "SouthAmerica") {
        return Region::SouthAmerica;
    }
    if (text == "Africa") {
        return Region::Africa;
    }
    if (text == "SoutheastAsia") {
        return Region::SoutheastAsia;
    }
    return Region::Europe;
}

SpecTables load_specs() {
    SpecTables tables;

    {
        std::ifstream input(spec_dir() / "cards.csv");
        if (!input) {
            throw std::runtime_error("failed to open data/spec/cards.csv");
        }
        std::string line;
        while (std::getline(input, line)) {
            line = trim(line);
            if (line.empty() || line[0] == '#') {
                continue;
            }
            if (line.starts_with("card_id")) {
                continue;
            }
            const auto comment = line.find('#');
            if (comment != std::string::npos) {
                line = trim(line.substr(0, comment));
            }
            if (line.empty()) {
                continue;
            }
            const auto row = split_csv_row(line);
            if (row.size() < 7) {
                continue;
            }

            CardSpec spec;
            spec.card_id = static_cast<CardId>(parse_int(row[0]));
            spec.name = row[1];
            spec.side = parse_side(row[2]);
            spec.ops = parse_int(row[3]);
            spec.era = parse_era(row[4]);
            spec.starred = parse_bool(row[5]);
            spec.is_scoring = parse_bool(row[6]);
            spec.must_be_played_by_era_end = row.size() > 7 ? !row[7].empty() : spec.is_scoring;

            tables.cards[spec.card_id] = spec;
            tables.all_card_ids.push_back(spec.card_id);
        }
    }

    {
        std::ifstream input(spec_dir() / "countries.csv");
        if (!input) {
            throw std::runtime_error("failed to open data/spec/countries.csv");
        }
        std::string line;
        while (std::getline(input, line)) {
            line = trim(line);
            if (line.empty() || line[0] == '#') {
                continue;
            }
            if (line.starts_with("country_id")) {
                continue;
            }
            const auto comment = line.find('#');
            if (comment != std::string::npos) {
                line = trim(line.substr(0, comment));
            }
            if (line.empty()) {
                continue;
            }
            const auto row = split_csv_row(line);
            if (row.size() < 7) {
                continue;
            }

            CountrySpec spec;
            spec.country_id = static_cast<CountryId>(parse_int(row[0]));
            spec.name = row[1];
            spec.region = parse_region(row[2]);
            spec.stability = parse_int(row[3]);
            spec.is_battleground = parse_bool(row[4]);
            spec.us_start = parse_int(row[5]);
            spec.ussr_start = parse_int(row[6]);

            tables.countries[spec.country_id] = spec;
            tables.all_country_ids.push_back(spec.country_id);
        }
    }

    std::sort(tables.all_card_ids.begin(), tables.all_card_ids.end());
    std::sort(tables.all_country_ids.begin(), tables.all_country_ids.end());
    return tables;
}

}  // namespace

std::filesystem::path repo_root() {
    return std::filesystem::path(__FILE__).parent_path().parent_path().parent_path();
}

std::filesystem::path spec_dir() {
    return repo_root() / "data" / "spec";
}

const SpecTables& specs() {
    static std::once_flag once;
    static SpecTables cached;
    std::call_once(once, [] { cached = load_specs(); });
    return cached;
}

const CardSpec& card_spec(CardId card_id) {
    const auto& item = specs().cards[card_id];
    if (!item.has_value()) {
        throw std::out_of_range("unknown card id");
    }
    return *item;
}

bool has_card_spec(CardId card_id) {
    return specs().cards[card_id].has_value();
}

const CountrySpec& country_spec(CountryId country_id) {
    const auto& item = specs().countries[country_id];
    if (!item.has_value()) {
        throw std::out_of_range("unknown country id");
    }
    return *item;
}

bool has_country_spec(CountryId country_id) {
    return specs().countries[country_id].has_value();
}

const std::vector<CardId>& all_card_ids() {
    return specs().all_card_ids;
}

const std::vector<CountryId>& all_country_ids() {
    return specs().all_country_ids;
}

}  // namespace ts
