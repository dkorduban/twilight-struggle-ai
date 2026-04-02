#!/usr/bin/env python3
"""
Extract opening influence placements from human game logs.

Parses SETUP sections from 52 TSReplayer log files and extracts the free
placements (excluding fixed setup influence) for both USSR and US.

Output: cpp/tscore/human_openings.hpp
"""

import re
from pathlib import Path
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Dict, List, Tuple

# Country name to ID mapping (from countries.csv)
COUNTRY_NAME_TO_ID = {
    # Europe
    "Austria": 0,
    "Benelux": 1,
    "Canada": 2,
    "Czechoslovakia": 3,
    "Denmark": 4,
    "East Germany": 5,
    "Finland": 6,
    "France": 7,
    "Greece": 8,
    "Hungary": 9,
    "Italy": 10,
    "Norway": 11,
    "Poland": 12,
    "Romania": 13,
    "Spain/Portugal": 14,
    "Sweden": 15,
    "Turkey": 16,
    "UK": 17,
    "West Germany": 18,
    "Yugoslavia": 19,
    # Asia
    "Afghanistan": 20,
    "India": 21,
    "Japan": 22,
    "North Korea": 23,
    "Pakistan": 24,
    "South Korea": 25,
    # Middle East
    "Egypt": 26,
    "Gulf States": 27,
    "Iran": 28,
    "Iraq": 29,
    "Israel": 30,
    "Jordan": 31,
    "Lebanon": 32,
    "Libya": 33,
    "Saudi Arabia": 34,
    "Syria": 35,
    # Central America
    "Cuba": 36,
    "Dominican Republic": 37,
    "El Salvador": 38,
    "Guatemala": 39,
    "Haiti": 40,
    "Honduras": 41,
    "Mexico": 42,
    "Nicaragua": 43,
    "Panama": 44,
    "Costa Rica": 45,
    # South America
    "Argentina": 46,
    "Bolivia": 47,
    "Brazil": 48,
    "Chile": 49,
    "Colombia": 50,
    "Ecuador": 51,
    "Paraguay": 52,
    "Peru": 53,
    "Uruguay": 54,
    "Venezuela": 55,
    # Africa
    "Algeria": 56,
    "Angola": 57,
    "Botswana": 58,
    "Cameroon": 59,
    "Congo/Zaire": 60,
    "Ethiopia": 61,
    "Ivory Coast": 62,
    "Kenya": 63,
    "Morocco": 65,
    "Mozambique": 66,
    "Nigeria": 67,
    "Saharan States": 68,
    "SE African States": 69,
    "Somalia": 70,
    "South Africa": 71,
    "Sudan": 72,
    "Tunisia": 73,
    "Zimbabwe": 74,
    # Southeast Asia
    "Burma": 75,
    "Indonesia": 76,
    "Laos/Cambodia": 77,
    "Philippines": 78,
    "Thailand": 79,
    "Vietnam": 80,
    # Superpowers and special
    "USA": 81,
    "USSR": 82,
    "Bulgaria": 83,
    "Malaysia": 84,
    "Taiwan": 85,
}

# Fixed setup influence by country (from countries.csv)
# These amounts are always in place at game start
FIXED_USSR_INFLUENCE = {
    5: 3,    # East Germany
    6: 1,    # Finland
    23: 3,   # North Korea
    29: 1,   # Iraq
    35: 1,   # Syria
}

FIXED_US_INFLUENCE = {
    2: 2,    # Canada
    10: 1,   # Italy (uncertain in CSV, set to 1 per human logs analysis)
    17: 5,   # UK
    22: 1,   # Japan
    25: 1,   # South Korea
    28: 1,   # Iran
    30: 1,   # Israel
    44: 1,   # Panama
    71: 1,   # South Africa
    78: 1,   # Philippines
}

# Valid free-placement regions
# Note: Austria (0) appears in some human games, treating it as valid.
# Also including all official targets per rules.
VALID_USSR_FREE_TARGETS = {0, 3, 5, 9, 12, 13, 19, 83}  # Eastern Europe (including Austria)
VALID_US_FREE_TARGETS = {1, 2, 4, 7, 8, 10, 11, 14, 15, 16, 17, 18}  # Western Europe


@dataclass
class SetupPlacement:
    country_id: int
    amount: int

    def __hash__(self):
        return hash((self.country_id, self.amount))

    def __eq__(self, other):
        return self.country_id == other.country_id and self.amount == other.amount


@dataclass
class Opening:
    placements: Tuple[SetupPlacement, ...]

    def __hash__(self):
        return hash(self.placements)

    def __eq__(self, other):
        return self.placements == other.placements

    @property
    def total_influence(self):
        return sum(p.amount for p in self.placements)


def parse_setup_section(lines: List[str]) -> Tuple[Opening, Opening]:
    """
    Parse the SETUP section of a game log.
    Returns (ussr_opening, us_opening).

    Note: US typically has 7 free placements in Western Europe, plus a 2-point
    bid that can go anywhere (e.g., Iran). This function extracts only the free
    placements in valid regions, excluding bid influence.
    """
    setup_lines = []
    handicap = 0

    for line in lines:
        if "Turn 1" in line:
            break
        # Extract handicap if present
        if "Handicap influence" in line:
            match = re.search(r"US \+(\d+)", line)
            if match:
                handicap = int(match.group(1))
        if re.match(r"(USSR|US)\s+\+", line):
            setup_lines.append(line)

    ussr_placements = {}
    us_placements = {}

    for line in setup_lines:
        # Format: "USSR +4 in Poland [0][4]"
        match = re.match(
            r"(USSR|US)\s+\+(\d+)\s+in\s+(.+?)\s+\[(\d+)\]\[(\d+)\]", line
        )
        if not match:
            print(f"WARNING: Could not parse setup line: {line}")
            continue

        side, amount, country_name, us_val, ussr_val = match.groups()
        amount = int(amount)
        us_val = int(us_val)
        ussr_val = int(ussr_val)

        if country_name not in COUNTRY_NAME_TO_ID:
            print(f"WARNING: Unknown country '{country_name}' in line: {line}")
            continue

        country_id = COUNTRY_NAME_TO_ID[country_name]

        if side == "USSR":
            ussr_placements[country_id] = ussr_val
        else:  # US
            us_placements[country_id] = us_val

    # Compute free placements by subtracting fixed influence
    ussr_free = []
    for country_id, total_ussr in ussr_placements.items():
        fixed = FIXED_USSR_INFLUENCE.get(country_id, 0)
        free = total_ussr - fixed
        if free > 0:
            # Note: only include placements in valid targets
            if country_id in VALID_USSR_FREE_TARGETS:
                ussr_free.append(SetupPlacement(country_id, free))

    # For US: subtract both fixed influence AND bid influence.
    # The bid is typically placed in non-WE countries (like Iran).
    # Extract only free placements in valid Western Europe targets.
    us_free = []
    for country_id, total_us in us_placements.items():
        fixed = FIXED_US_INFLUENCE.get(country_id, 0)
        free = total_us - fixed

        # If this country is NOT a valid free target (WE country),
        # then all the influence here is bid influence — skip it.
        if country_id not in VALID_US_FREE_TARGETS:
            continue

        if free > 0:
            us_free.append(SetupPlacement(country_id, free))

    # Sort for consistency
    ussr_free.sort(key=lambda p: p.country_id)
    us_free.sort(key=lambda p: p.country_id)

    return Opening(tuple(ussr_free)), Opening(tuple(us_free))


def main():
    logs_dir = Path("/home/dkord/code/twilight-struggle-ai/data/raw_logs")
    log_files = sorted(logs_dir.glob("*.txt"))

    print(f"Found {len(log_files)} log files")

    ussr_openings: List[Opening] = []
    us_openings: List[Opening] = []

    for log_file in log_files:
        try:
            with open(log_file) as f:
                lines = f.readlines()
            ussr_opening, us_opening = parse_setup_section(lines)
            ussr_openings.append(ussr_opening)
            us_openings.append(us_opening)
        except Exception as e:
            print(f"ERROR parsing {log_file}: {e}")

    # Analyze openings
    ussr_counter = Counter(ussr_openings)
    us_counter = Counter(us_openings)

    print("\n" + "=" * 80)
    print("USSR OPENINGS")
    print("=" * 80)
    print(f"Unique configurations: {len(ussr_counter)}")
    print()

    for opening, count in ussr_counter.most_common():
        total = opening.total_influence
        status = "OK" if total == 6 else f"ERROR (total={total})"
        print(f"Count: {count:2d}  Total: {total}  {status}")
        for p in opening.placements:
            country_names = [k for k, v in COUNTRY_NAME_TO_ID.items() if v == p.country_id]
            country_name = country_names[0] if country_names else f"ID{p.country_id}"
            print(f"          {country_name:20s} (id={p.country_id:2d}): +{p.amount}")
        print()

    print("=" * 80)
    print("US OPENINGS")
    print("=" * 80)
    print(f"Unique configurations: {len(us_counter)}")
    print()

    for opening, count in us_counter.most_common():
        total = opening.total_influence
        status = "OK" if total == 7 else f"ERROR (total={total})"
        print(f"Count: {count:2d}  Total: {total}  {status}")
        for p in opening.placements:
            country_names = [k for k, v in COUNTRY_NAME_TO_ID.items() if v == p.country_id]
            country_name = country_names[0] if country_names else f"ID{p.country_id}"
            print(f"          {country_name:20s} (id={p.country_id:2d}): +{p.amount}")
        print()

    # Generate C++ header
    generate_cpp_header(ussr_counter, us_counter)


def generate_cpp_header(ussr_counter: Counter, us_counter: Counter):
    """Generate cpp/tscore/human_openings.hpp"""

    ussr_sorted = sorted(ussr_counter.items(), key=lambda x: -x[1])
    us_sorted = sorted(us_counter.items(), key=lambda x: -x[1])

    cpp_code = """#pragma once

#include "types.hpp"

#include <array>
#include <span>

namespace ts {

// Setup placement for a single country during opening phase.
struct SetupPlacement {
    CountryId country;
    int amount;
};

// One complete opening configuration (sorted by country ID for determinism).
// Padded with {0, 0} sentinels to fixed length.
struct SetupOpening {
    std::array<SetupPlacement, 6> placements;  // max 6 free placements per side
    int count;  // actual number of valid entries
};

// Extracted from 52 human TSReplayer game logs.
// Each entry represents an actual opening configuration played by humans.

"""

    cpp_code += f"inline constexpr std::array<SetupOpening, {len(ussr_sorted)}> kHumanUSSROpenings = {{\n"
    for opening, count in ussr_sorted:
        placements_str = _format_placements(opening.placements)
        cpp_code += f"    // Played {count} time(s)\n"
        cpp_code += f"    SetupOpening{{\n"
        cpp_code += placements_str
        cpp_code += f"{len(opening.placements)},  // count\n"
        cpp_code += f"    }},\n"
    cpp_code += "};\n\n"

    cpp_code += f"inline constexpr std::array<SetupOpening, {len(us_sorted)}> kHumanUSOpenings = {{\n"
    for opening, count in us_sorted:
        placements_str = _format_placements(opening.placements)
        cpp_code += f"    // Played {count} time(s)\n"
        cpp_code += f"    SetupOpening{{\n"
        cpp_code += placements_str
        cpp_code += f"{len(opening.placements)},  // count\n"
        cpp_code += f"    }},\n"
    cpp_code += "};\n\n"

    cpp_code += "}  // namespace ts\n"

    output_path = Path("/home/dkord/code/twilight-struggle-ai/cpp/tscore/human_openings.hpp")
    output_path.write_text(cpp_code)
    print(f"\nWrote {output_path}")


def _format_placements(placements: Tuple[SetupPlacement, ...]) -> str:
    """Format placements array for C++ output."""
    lines = "        .placements = {\n"
    for p in placements:
        lines += f"            SetupPlacement{{{p.country_id}, {p.amount}}},\n"
    # Pad with sentinels
    for _ in range(6 - len(placements)):
        lines += f"            SetupPlacement{{0, 0}},\n"
    lines += "        },\n"
    lines += "        .count = "
    return lines


if __name__ == "__main__":
    main()
