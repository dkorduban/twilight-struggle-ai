// Tests for accessible_countries() in adjacency.cpp.
//
// Country ID reference (from data/spec/adjacency.csv and countries.csv):
//   USSR anchor (id=82) neighbors: Afghanistan(20), Finland(6), North Korea(23), Poland(12), Romania(13)
//   USA  anchor (id=81) neighbors: Canada(2), Cuba(36), Japan(22), Mexico(42), Philippines(78), South Korea(25)
//
// Map countries used in tests:
//   Canada=2, Czechoslovakia=3, Finland=6, Hungary=9, Poland=12, Romania=13,
//   Afghanistan=20, Japan=22, North Korea=23, South Korea=25, Cuba=36,
//   Mexico=42, Philippines=78, Bulgaria=83
//
// Adjacencies relevant to 1-hop tests:
//   Poland(12) neighbors include: Czechoslovakia(3), East Germany(4), Austria(0), Romania(13),
//                                   West Germany(18), USSR-anchor(82)
//   Czechoslovakia(3) neighbors include: Austria(0), East Germany(4), Hungary(9), Poland(12),
//                                        West Germany(18)
//   Hungary(9) neighbors include: Austria(0), Czechoslovakia(3), Romania(13), Yugoslavia(19)

#include <algorithm>
#include <catch2/catch_test_macros.hpp>
#include <vector>

#include "adjacency.hpp"
#include "public_state.hpp"
#include "types.hpp"

using namespace ts;

namespace {

bool contains(const std::vector<CountryId>& v, CountryId cid) {
    return std::find(v.begin(), v.end(), cid) != v.end();
}

// Convenience: total number of real map countries (excludes anchors).
// We derive this at runtime from the accessible set for Coup on an empty board,
// which should equal all map countries.
int total_map_countries() {
    PublicState empty;
    auto all = accessible_countries(Side::USSR, empty, ActionMode::Coup);
    return static_cast<int>(all.size());
}

}  // namespace

// ---------------------------------------------------------------------------
// Test 1: Influence, empty board — accessible from own anchor neighbors only.
// ---------------------------------------------------------------------------

TEST_CASE("accessible_countries Influence USSR empty board: anchor neighbors only", "[adjacency]") {
    PublicState empty;
    auto acc = accessible_countries(Side::USSR, empty, ActionMode::Influence);

    // USSR anchor (82) neighbors: Afghanistan(20), Finland(6), North Korea(23), Poland(12), Romania(13)
    REQUIRE(contains(acc, 20));   // Afghanistan
    REQUIRE(contains(acc, 6));    // Finland
    REQUIRE(contains(acc, 23));   // North Korea
    REQUIRE(contains(acc, 12));   // Poland
    REQUIRE(contains(acc, 13));   // Romania

    // NOT accessible: Czechoslovakia(3) — adjacent to Poland, but 2 hops from USSR anchor
    REQUIRE_FALSE(contains(acc, 3));

    // NOT accessible: Canada(2) — adjacent to US anchor, not USSR anchor
    REQUIRE_FALSE(contains(acc, 2));

    // NOT accessible: Cuba(36) — adjacent to US anchor
    REQUIRE_FALSE(contains(acc, 36));

    // NOT accessible: Japan(22) — adjacent to US anchor
    REQUIRE_FALSE(contains(acc, 22));
}

// ---------------------------------------------------------------------------
// Test 2: Influence, USSR has influence in Poland — 1-hop, no transitive chain.
// ---------------------------------------------------------------------------

TEST_CASE("accessible_countries Influence USSR in Poland: 1-hop only, no transitive chaining", "[adjacency]") {
    PublicState pub;
    pub.influence[static_cast<int>(Side::USSR)][12] = 1;  // Poland = 12

    auto acc = accessible_countries(Side::USSR, pub, ActionMode::Influence);

    // Poland itself must be accessible
    REQUIRE(contains(acc, 12));   // Poland

    // 1-hop neighbors of Poland that are not anchors must be accessible.
    // Poland's neighbors: Czechoslovakia(3), East Germany(4/id from csv), Austria(0),
    //                     Romania(13), West Germany(18), USSR-anchor(82 excluded)
    REQUIRE(contains(acc, 3));    // Czechoslovakia (adjacent to Poland)

    // USSR anchor neighbors still accessible
    REQUIRE(contains(acc, 6));    // Finland (USSR anchor neighbor)
    REQUIRE(contains(acc, 20));   // Afghanistan (USSR anchor neighbor)

    // NOT accessible: Hungary(9) — adjacent to Czechoslovakia, but 2 hops from Poland
    // (unless Hungary is directly adjacent to Poland — let's verify it is NOT)
    // Hungary's neighbors: Austria, Czechoslovakia, Romania, Yugoslavia; NOT Poland directly.
    REQUIRE_FALSE(contains(acc, 9));

    // NOT accessible: Canada(2) — US anchor neighbor
    REQUIRE_FALSE(contains(acc, 2));

    // NOT accessible: Japan(22) — US anchor neighbor
    REQUIRE_FALSE(contains(acc, 22));
}

// ---------------------------------------------------------------------------
// Test 3: Coup — returns all map countries (unrestricted).
// ---------------------------------------------------------------------------

TEST_CASE("accessible_countries Coup: returns all map countries", "[adjacency]") {
    PublicState empty;
    auto acc = accessible_countries(Side::USSR, empty, ActionMode::Coup);

    // Must be non-empty
    REQUIRE(acc.size() > 0);

    // Must include countries with no USSR presence anywhere near them
    REQUIRE(contains(acc, 36));   // Cuba (US anchor neighbor; USSR has no presence)
    REQUIRE(contains(acc, 2));    // Canada (US anchor neighbor)
    REQUIRE(contains(acc, 22));   // Japan
    REQUIRE(contains(acc, 6));    // Finland
    REQUIRE(contains(acc, 12));   // Poland

    // Must be the full map (no country excluded due to adjacency)
    // Venezuela is deep in South America with no USSR presence on empty board
    // We confirm the set is large (>= 68 countries)
    REQUIRE(static_cast<int>(acc.size()) >= 68);
}

// ---------------------------------------------------------------------------
// Test 4: Realignment — same unrestricted scope as Coup.
// ---------------------------------------------------------------------------

TEST_CASE("accessible_countries Realign: returns all map countries", "[adjacency]") {
    PublicState empty;
    auto acc_realign = accessible_countries(Side::USSR, empty, ActionMode::Realign);
    auto acc_coup    = accessible_countries(Side::USSR, empty, ActionMode::Coup);

    // Realign and Coup accessible sets must be identical in size and content
    REQUIRE(acc_realign.size() == acc_coup.size());

    for (CountryId cid : acc_coup) {
        REQUIRE(contains(acc_realign, cid));
    }
}

// ---------------------------------------------------------------------------
// Test 5: US side empty board — can access US anchor neighbors, not USSR ones.
// ---------------------------------------------------------------------------

TEST_CASE("accessible_countries Influence US empty board: own anchor only", "[adjacency]") {
    PublicState empty;
    auto acc = accessible_countries(Side::US, empty, ActionMode::Influence);

    // US anchor (81) neighbors: Canada(2), Cuba(36), Japan(22), Mexico(42), Philippines(78), South Korea(25)
    REQUIRE(contains(acc, 2));    // Canada
    REQUIRE(contains(acc, 36));   // Cuba
    REQUIRE(contains(acc, 22));   // Japan
    REQUIRE(contains(acc, 42));   // Mexico
    REQUIRE(contains(acc, 78));   // Philippines
    REQUIRE(contains(acc, 25));   // South Korea

    // NOT accessible: USSR anchor neighbors
    REQUIRE_FALSE(contains(acc, 6));    // Finland (USSR anchor neighbor)
    REQUIRE_FALSE(contains(acc, 12));   // Poland (USSR anchor neighbor)
    REQUIRE_FALSE(contains(acc, 20));   // Afghanistan (USSR anchor neighbor)
    REQUIRE_FALSE(contains(acc, 23));   // North Korea (USSR anchor neighbor)
    REQUIRE_FALSE(contains(acc, 13));   // Romania (USSR anchor neighbor)
}
