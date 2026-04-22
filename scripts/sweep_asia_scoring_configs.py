"""Offline config sweep for Asia card-1 SCORING_VP_MISMATCH residuals.

Reads results/validator_violations.jsonl (full state snapshots per violation),
recomputes expected VP under 8 config toggles, and reports residual count + delta
histogram per config.

Config toggles (3 independent bits, 2^3 = 8 configs):
    sk_is_bg      : True  = South Korea (id=25) is a battleground (current spec)
                    False = South Korea is non-BG (hypothesis)
    sk_usa_adj    : True  = South Korea adjacent to USA anchor (current adjacency.csv)
                    False = no SK-USA adjacency
    phi_usa_adj   : True  = Philippines (id=78) adjacent to USA anchor (current)
                    False = no PHI-USA adjacency

China card bonus is NOT toggled here (holder info not in snapshot). This script
only explores BG/adjacency toggles. It operates on expected_vp from the log as
ground truth.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

REPO = Path(__file__).parent.parent
VIOLATIONS = REPO / "results/validator_violations.jsonl"
COUNTRIES = REPO / "data/spec/countries.csv"
ADJACENCY = REPO / "data/spec/adjacency.csv"

USA_ID = 81
USSR_ID = 82

ASIA_NAMES = {
    "Afghanistan", "India", "Japan", "North Korea", "Pakistan", "South Korea",
    "Burma", "Indonesia", "Laos/Cambodia", "Philippines", "Thailand", "Vietnam",
    "Malaysia", "Taiwan",
}

ASIA_VP = (3, 7, 9)  # Presence, Domination, Control


def load_countries() -> dict[str, dict]:
    """name -> {id, stability, is_battleground}."""
    out = {}
    with open(COUNTRIES) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            if line.startswith("country_id"):
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 5:
                continue
            cid = int(parts[0])
            name = parts[1]
            stability = int(parts[3])
            is_bg = parts[4].lower() == "true"
            out[name] = {"id": cid, "stability": stability, "is_battleground": is_bg}
    return out


def load_adjacency_to_usa() -> set[str]:
    """Return set of country names adjacent to USA anchor (id=81)."""
    usa_adj = set()
    # Map id -> name for USA-adjacent rows
    id_to_name = {}
    with open(COUNTRIES) as f:
        for line in f:
            if line.startswith("#") or not line.strip() or line.startswith("country_id"):
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 2:
                continue
            id_to_name[int(parts[0])] = parts[1]

    with open(ADJACENCY) as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#") or s.startswith("country_a"):
                continue
            payload = s.split("#")[0].strip()
            parts = payload.split(",")
            try:
                a, b = int(parts[0]), int(parts[1])
            except (ValueError, IndexError):
                continue
            if a == USA_ID and b in id_to_name:
                usa_adj.add(id_to_name[b])
            elif b == USA_ID and a in id_to_name:
                usa_adj.add(id_to_name[a])
    return usa_adj


def compute_control(
    influence_us: dict[str, int],
    influence_ussr: dict[str, int],
    countries: dict[str, dict],
    asia_countries: list[str],
) -> tuple[set[str], set[str]]:
    """Apply stability rule: own_inf >= opp_inf + stability ⇒ control."""
    ctrl_us, ctrl_ussr = set(), set()
    for name in asia_countries:
        stab = countries[name]["stability"]
        us_inf = influence_us.get(name, 0)
        ussr_inf = influence_ussr.get(name, 0)
        if us_inf >= ussr_inf + stab:
            ctrl_us.add(name)
        elif ussr_inf >= us_inf + stab:
            ctrl_ussr.add(name)
    return ctrl_us, ctrl_ussr


def compute_tier_vp(
    ctrl_us: set[str],
    ctrl_ussr: set[str],
    bg_set: set[str],
) -> tuple[int, int]:
    """Return (us_base_vp, ussr_base_vp)."""
    bg_us = ctrl_us & bg_set
    bg_ussr = ctrl_ussr & bg_set
    non_bg_us = ctrl_us - bg_set
    non_bg_ussr = ctrl_ussr - bg_set
    total_bgs = len(bg_set)

    def tier(own, opp, own_bg, opp_bg, own_non_bg):
        if not own:
            return 0  # no presence
        has_all_bg = len(own_bg) == total_bgs
        more_countries = len(own) > len(opp)
        more_bg = len(own_bg) > len(opp_bg)
        if has_all_bg and more_countries:
            return ASIA_VP[2]  # Control
        if more_countries and more_bg and own_bg and own_non_bg:
            return ASIA_VP[1]  # Domination
        return ASIA_VP[0]  # Presence

    us_base = tier(ctrl_us, ctrl_ussr, bg_us, bg_ussr, non_bg_us)
    ussr_base = tier(ctrl_ussr, ctrl_us, bg_ussr, bg_us, non_bg_ussr)
    return us_base, ussr_base


def recompute_expected(
    violation: dict,
    countries: dict[str, dict],
    usa_adj: set[str],
    config: dict,
) -> int:
    """Return predicted VP delta (USSR - US, positive = USSR gains)."""
    # Apply BG toggle
    bg_set = {name for name, info in countries.items()
              if name in ASIA_NAMES and info["is_battleground"]}
    if not config["sk_is_bg"]:
        bg_set.discard("South Korea")

    # Apply adjacency toggle
    adj_set = set(usa_adj)
    if not config["sk_usa_adj"]:
        adj_set.discard("South Korea")
    if not config["phi_usa_adj"]:
        adj_set.discard("Philippines")

    # Asia countries in play
    asia_countries = [n for n in ASIA_NAMES if n in countries]

    ctrl_us, ctrl_ussr = compute_control(
        violation["us_influence_by_country"],
        violation["ussr_influence_by_country"],
        countries,
        asia_countries,
    )

    us_base, ussr_base = compute_tier_vp(ctrl_us, ctrl_ussr, bg_set)

    # BG bonus: +1 per BG controlled
    us_bg = len(ctrl_us & bg_set)
    ussr_bg = len(ctrl_ussr & bg_set)

    # Adjacency bonus: +1 per controlled country adjacent to enemy superpower.
    # Enemy of US = USSR, enemy of USSR = US. adj_set = USA-adjacent.
    # US countries adj to USSR: not available here (USSR-adj not toggled in our hypotheses)
    # Using only USA adjacency toggles:
    us_adj_bonus = 0  # USSR adj not changing under our hypotheses; assume no residual impact
    ussr_adj_bonus = len(ctrl_ussr & adj_set)

    us_vp = us_base + us_bg + us_adj_bonus
    ussr_vp = ussr_base + ussr_bg + ussr_adj_bonus

    return ussr_vp - us_vp


def main() -> None:
    countries = load_countries()
    usa_adj = load_adjacency_to_usa()

    print(f"USA-adjacent countries (from adjacency.csv): {sorted(usa_adj)}")
    print(f"Asia BGs in current spec: {sorted(n for n in ASIA_NAMES if n in countries and countries[n]['is_battleground'])}")

    violations = []
    with open(VIOLATIONS) as f:
        for line in f:
            d = json.loads(line)
            if d.get("region") == "Asia" and d.get("card_id") == 1:
                violations.append(d)
    print(f"\nAsia card-1 violations: {len(violations)}\n")

    # 8 configs
    configs = []
    for sk_bg in (True, False):
        for sk_adj in (True, False):
            for phi_adj in (True, False):
                configs.append({
                    "sk_is_bg": sk_bg,
                    "sk_usa_adj": sk_adj,
                    "phi_usa_adj": phi_adj,
                })

    for cfg in configs:
        label = f"sk_bg={int(cfg['sk_is_bg'])} sk_adj={int(cfg['sk_usa_adj'])} phi_adj={int(cfg['phi_usa_adj'])}"
        # Predicted delta (USSR - US) under this config vs log's expected_vp.
        # log_signed: if side="USSR", log_signed = expected_vp; if "US", log_signed = -expected_vp.
        # For each violation we try three china-holder hypotheses (none/US/USSR) and count
        # the case as solved if ANY hypothesis zeroes the residual.
        residuals_no_china = []
        solvable_by_china = {"none": 0, "us": 0, "ussr": 0, "any": 0, "unsolved": 0}
        for v in violations:
            pred = recompute_expected(v, countries, usa_adj, cfg)
            log_signed = v["expected_vp"] if v["side"] == "USSR" else -v["expected_vp"]
            r_none = pred - log_signed
            # china=US → -1 to (USSR-US); china=USSR → +1 to (USSR-US)
            r_us = (pred - 1) - log_signed
            r_ussr = (pred + 1) - log_signed
            residuals_no_china.append(r_none)
            if r_none == 0:
                solvable_by_china["none"] += 1
                solvable_by_china["any"] += 1
            elif r_us == 0:
                solvable_by_china["us"] += 1
                solvable_by_china["any"] += 1
            elif r_ussr == 0:
                solvable_by_china["ussr"] += 1
                solvable_by_china["any"] += 1
            else:
                solvable_by_china["unsolved"] += 1
        hist = sorted(Counter(residuals_no_china).items())
        print(f"{label}: no_china_zero={solvable_by_china['none']}/71  "
              f"china_us_fixes={solvable_by_china['us']}  china_ussr_fixes={solvable_by_china['ussr']}  "
              f"any={solvable_by_china['any']}/71  unsolved={solvable_by_china['unsolved']}")


if __name__ == "__main__":
    main()
