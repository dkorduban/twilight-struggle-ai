#pragma once

#include <cstdint>

// ---------------------------------------------------------------------------
// Fundamental enums and type aliases for the Twilight Struggle core engine.
//
// Conventions:
//   - All enums are uint8_t to keep arrays compact.
//   - Side and Superpower are distinct: Side includes Neutral (used for
//     countries / scoring), Superpower does not (used for phasing player,
//     influence arrays, etc.).
//   - CardId and CountryId are plain uint8_t aliases; zero is not a valid
//     card or country in the canonical encoding (reserved / sentinel).
// ---------------------------------------------------------------------------

namespace ts {

enum class Side : uint8_t {
    USSR    = 0,
    US      = 1,
    Neutral = 2,
};

// Superpower is used wherever Neutral is not a legal value (phasing player,
// array indexing, etc.).
enum class Superpower : uint8_t {
    USSR = 0,
    US   = 1,
};

enum class Era : uint8_t {
    Early = 0,  // turns 1-3
    Mid   = 1,  // turns 4-6
    Late  = 2,  // turns 7-10
};

enum class Region : uint8_t {
    Europe          = 0,
    Asia            = 1,
    MiddleEast      = 2,
    CentralAmerica  = 3,
    SouthAmerica    = 4,
    Africa          = 5,
    SoutheastAsia   = 6,
};

// ---------------------------------------------------------------------------
// Primitive type aliases
// ---------------------------------------------------------------------------

using CardId    = uint8_t;
using CountryId = uint8_t;
using Ops       = uint8_t;
using Influence = int8_t;   // signed: negative never occurs on-board but
                             // arithmetic intermediates may go negative.

// ---------------------------------------------------------------------------
// Well-known constants
// ---------------------------------------------------------------------------

// Placeholder CardId for the China Card. The canonical id will be pinned once
// cards.csv is finalised; every caller should use this constant, not the
// literal, so that a single change propagates everywhere.
static constexpr CardId CHINA_CARD = 6;

// Maximum number of card slots in any bitset. 110 covers all TS card ids with
// room for a few reserved values.
static constexpr int MAX_CARDS     = 110;

// Maximum number of country slots.
static constexpr int MAX_COUNTRIES = 100;

// Hand sizes per the ITS / competitive rules.
// The China Card does NOT count toward hand size; it is tracked separately.
static constexpr int HAND_SIZE_EARLY = 8;  // turns 1-3
static constexpr int HAND_SIZE_LATE  = 9;  // turns 4-10

} // namespace ts
