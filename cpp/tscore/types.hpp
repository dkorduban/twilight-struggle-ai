// Shared native engine enums, aliases, and fixed-size container definitions.

#pragma once

#include <array>
#include <bitset>
#include <cstddef>
#include <cstdint>
#include <optional>
#include <span>
#include <string>
#include <string_view>
#include <vector>

namespace ts {

enum class Side : uint8_t {
    USSR = 0,
    US = 1,
    Neutral = 2,
};

enum class ActionMode : uint8_t {
    Influence = 0,
    Coup = 1,
    Realign = 2,
    Space = 3,
    Event = 4,
};

enum class Era : uint8_t {
    Early = 0,
    Mid = 1,
    Late = 2,
};

enum class Region : uint8_t {
    Europe = 0,
    Asia = 1,
    MiddleEast = 2,
    CentralAmerica = 3,
    SouthAmerica = 4,
    Africa = 5,
    SoutheastAsia = 6,
};

enum class GamePhase : uint8_t {
    Setup = 0,
    Headline = 1,
    ActionRound = 2,
    Cleanup = 3,
    GameOver = 4,
};

using CardId = uint8_t;
using CountryId = uint8_t;

inline constexpr CardId kChinaCardId = 6;
inline constexpr int kMaxCardId = 111;
inline constexpr int kCardSlots = kMaxCardId + 1;  // index 0 unused
inline constexpr int kMaxCountryId = 85;
inline constexpr int kCountrySlots = kMaxCountryId + 1;  // ids 0..85
inline constexpr int kHandSizeEarly = 8;
inline constexpr int kHandSizeLate = 9;
inline constexpr CountryId kUsaAnchorId = 81;
inline constexpr CountryId kUssrAnchorId = 82;
inline constexpr CountryId kTaiwanId = 85;
inline constexpr CardId CHINA_CARD = kChinaCardId;
inline constexpr int MAX_CARDS = kCardSlots;
inline constexpr int MAX_COUNTRIES = kCountrySlots;
inline constexpr int HAND_SIZE_EARLY = kHandSizeEarly;
inline constexpr int HAND_SIZE_LATE = kHandSizeLate;

using CardSet = std::bitset<kCardSlots>;
using InfluenceBlock = std::array<int16_t, kCountrySlots>;

inline constexpr int to_index(Side side) {
    return static_cast<int>(side);
}

inline constexpr Side other_side(Side side) {
    return side == Side::USSR ? Side::US : Side::USSR;
}

inline constexpr bool is_player_side(Side side) {
    return side == Side::USSR || side == Side::US;
}

struct ActionEncoding {
    CardId card_id = 0;
    ActionMode mode = ActionMode::Influence;
    std::vector<CountryId> targets;

    [[nodiscard]] bool operator==(const ActionEncoding& other) const = default;
};

struct CardSpec {
    CardId card_id = 0;
    std::string name;
    Side side = Side::Neutral;
    int ops = 0;
    Era era = Era::Early;
    bool starred = false;
    bool is_scoring = false;
    bool must_be_played_by_era_end = false;
};

struct CountrySpec {
    CountryId country_id = 0;
    std::string name;
    Region region = Region::Europe;
    int stability = 0;
    bool is_battleground = false;
    int us_start = 0;
    int ussr_start = 0;
};

struct ScoringResult {
    int vp_delta = 0;
    bool game_over = false;
    std::optional<Side> winner;
    bool clear_shuttle = false;
};

struct GameResult {
    std::optional<Side> winner;
    int final_vp = 0;
    int end_turn = 0;
    std::string end_reason;
};

struct MatchSummary {
    int games = 0;
    int ussr_wins = 0;
    int us_wins = 0;
    int draws = 0;
    int defcon1 = 0;
    int turn_limit = 0;
    int scoring_card_held = 0;
    int vp_threshold = 0;
    double avg_turn = 0.0;
    double avg_final_vp = 0.0;
};

struct DecisionRequest {
    Side side = Side::USSR;
    bool holds_china = false;
};

template <typename Container>
inline std::vector<int> sorted_set_bits(const Container& bits, int start = 0) {
    std::vector<int> result;
    for (int i = start; i < static_cast<int>(bits.size()); ++i) {
        if (bits.test(static_cast<size_t>(i))) {
            result.push_back(i);
        }
    }
    return result;
}

}  // namespace ts
