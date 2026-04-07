#!/usr/bin/env python3
"""Analyze 51 human Twilight Struggle games from tsreplayer logs."""

import csv
import glob
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_LOGS = ROOT / "data" / "raw_logs"
SPEC = ROOT / "data" / "spec"

# ── Load spec data ──────────────────────────────────────────────────────
def load_cards():
    """card_name -> {id, side, ops, era}"""
    cards = {}
    with open(SPEC / "cards.csv") as f:
        lines = [l for l in f if not l.startswith("#")]
    for row in csv.DictReader(lines):
        cards[row["name"]] = {
            "id": int(row["card_id"]),
            "side": row["side"],
            "ops": int(row["ops"]),
            "era": row["era"],
        }
    # Add common aliases
    aliases = {
        "Mideast Scoring": "Middle East Scoring",
        "Alliance For Progress*": "Alliance for Progress",
        "Alliance For Progress": "Alliance for Progress",
        "Zaire": "Congo/Zaire",
        "\"We Will Bury You\"*": "We Will Bury You",
        "\"We Will Bury You\"": "We Will Bury You",
        "How I Learned To Stop Worrying*": "How I Learned to Stop Worrying",
        "How I Learned To Stop Worrying": "How I Learned to Stop Worrying",
        "Lonely Hearts Club Band*": "Lonely Hearts Club Band",
        "Lonely Hearts Club Band": "Lonely Hearts Club Band",
    }
    for alias, canonical in aliases.items():
        if canonical in cards and alias not in cards:
            cards[alias] = cards[canonical]
    return cards

def load_countries():
    """country_name -> {id, region, stability, is_bg}"""
    countries = {}
    with open(SPEC / "countries.csv") as f:
        lines = [l for l in f if not l.startswith("#")]
    for row in csv.DictReader(lines):
        if int(row["stability"]) == 0:
            continue  # skip anchor entries
        countries[row["name"]] = {
            "id": int(row["country_id"]),
            "region": row["region"],
            "stability": int(row["stability"]),
            "is_bg": row["is_battleground"].lower() == "true",
        }
    # Add aliases
    aliases = {
        "Zaire": "Congo/Zaire",
        "Congo": "Congo/Zaire",
    }
    for alias, canonical in aliases.items():
        if canonical in countries and alias not in countries:
            countries[alias] = countries[canonical]
    return countries


CARDS = load_cards()
COUNTRIES = load_countries()


def war_phase(turn):
    if turn <= 3:
        return "Early"
    elif turn <= 7:
        return "Mid"
    else:
        return "Late"


# ── Parse one game ──────────────────────────────────────────────────────

# Regex for action round headers
AR_RE = re.compile(
    r"Turn (\d+), (USSR|US) AR(\d+): (.+?):"
    r"\s*(Place Influence|Coup|Realignment|Space Race|Event)"
    r"(?:\s*\((\d+) Ops\))?(?::\s*(.*))?$"
)

# Simpler: just match "Turn X, Side ARY: CardName: ..." and then look for mode on same or next lines
AR_HEADER_RE = re.compile(r"Turn (\d+), (USSR|US) AR(\d+): (.+)")

HEADLINE_RE = re.compile(r"Turn (\d+), Headline Phase: (.+?) & (.+?):")
HEADLINE_WHO_RE = re.compile(r"(USSR|US) Headlines (.+)")

INF_RE = re.compile(r"(USSR|US) \+(\d+) in (.+?) \[")
COUP_TARGET_RE = re.compile(r"Target: (.+)")
SPACE_RE = re.compile(r"Space Race \((\d+) Ops\)")
PLACE_INF_RE = re.compile(r"Place Influence \((\d+) Ops\)")
COUP_OPS_RE = re.compile(r"Coup \((\d+) Ops\)")
REALIGN_OPS_RE = re.compile(r"Realignment \((\d+) Ops\)")
EVENT_RE = re.compile(r"Event: (.+)")
TRAP_RE = re.compile(r"(USSR|US) discards (.+)")
SCORING_RE = re.compile(r"(Asia|Europe|Middle East|Mideast|Central America|South America|Southeast Asia|Africa) Scoring")


def classify_card_side(card_name):
    """Return the card's side from spec."""
    clean = card_name.rstrip("*").strip()
    for name in [card_name, clean, card_name + "*", clean + "*"]:
        if name in CARDS:
            return CARDS[name]["side"]
    return None


def get_card_ops(card_name):
    clean = card_name.rstrip("*").strip()
    for name in [card_name, clean, card_name + "*", clean + "*"]:
        if name in CARDS:
            return CARDS[name]["ops"]
    return None


def get_card_era(card_name):
    clean = card_name.rstrip("*").strip()
    for name in [card_name, clean, card_name + "*", clean + "*"]:
        if name in CARDS:
            return CARDS[name]["era"]
    return None


def get_country_info(name):
    """Return country info dict or None."""
    name = name.strip()
    for n in [name, name.replace("Congo/Zaire", "Congo/Zaire")]:
        if n in COUNTRIES:
            return COUNTRIES[n]
    # Try fuzzy
    for k, v in COUNTRIES.items():
        if k.lower() == name.lower():
            return v
    return None


def parse_game(filepath):
    """Parse a single game log, return list of action records."""
    with open(filepath) as f:
        lines = f.readlines()

    actions = []
    headlines = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # ── Headlines ──
        hm = HEADLINE_RE.match(line)
        if hm:
            turn = int(hm.group(1))
            # Look for "USSR Headlines X" and "US Headlines Y" in next lines
            j = i + 1
            while j < min(i + 15, len(lines)):
                wm = HEADLINE_WHO_RE.match(lines[j].strip())
                if wm:
                    side = wm.group(1)
                    card = wm.group(2).strip()
                    headlines.append({
                        "turn": turn,
                        "phase": war_phase(turn),
                        "side": side,
                        "card": card,
                        "card_side": classify_card_side(card),
                    })
                j += 1
            i += 1
            continue

        # ── Action Rounds ──
        am = AR_HEADER_RE.match(line)
        if am:
            turn = int(am.group(1))
            side = am.group(2)
            ar_num = int(am.group(3))
            rest = am.group(4).strip()

            # rest is like "CardName: Mode (N Ops):" or "CardName: Event: EventName"
            # Split on first ":"
            card_and_mode = rest
            card_name = None
            mode = None
            ops_used = None

            # Try to extract card name (everything before first mode keyword)
            # Modes appear as: "Place Influence (N Ops)", "Coup (N Ops)", "Realignment (N Ops)", "Space Race (N Ops)", "Event: X"
            mode_match = re.search(
                r"(Place Influence|Coup|Realignment|Space Race|Event)\s*(?:\((\d+) Ops\))?",
                rest
            )

            if mode_match:
                mode_start = mode_match.start()
                # Card name is everything before the mode, minus trailing ": "
                card_name = rest[:mode_start].rstrip(": ").strip()
                mode = mode_match.group(1)
                if mode_match.group(2):
                    ops_used = int(mode_match.group(2))
            else:
                # No mode found on header line — might be trap/discard or weird format
                # Card name is up to first ":"
                parts = rest.split(":", 1)
                card_name = parts[0].strip()
                # Look at subsequent lines for mode
                j = i + 1
                while j < min(i + 10, len(lines)):
                    subline = lines[j].strip()
                    mm2 = re.search(
                        r"(Place Influence|Coup|Realignment|Space Race)\s*\((\d+) Ops\)",
                        subline
                    )
                    if mm2:
                        mode = mm2.group(1)
                        ops_used = int(mm2.group(2))
                        break
                    if subline.startswith("Event:"):
                        mode = "Event"
                        break
                    # Trap/discard lines for Quagmire/Bear Trap
                    if "discards" in subline and ("Trap" in lines[j+1] if j+1 < len(lines) else False):
                        mode = "Trap_Discard"
                        break
                    if re.match(r"Turn \d+", subline):
                        break
                    j += 1

            # Special: handle "Trap Roll" / Quagmire/Bear Trap discard
            # Check subsequent lines for trap
            if mode is None:
                j = i + 1
                while j < min(i + 5, len(lines)):
                    sl = lines[j].strip()
                    if "Trap Roll" in sl or "discards" in sl.lower():
                        mode = "Trap_Discard"
                        break
                    if re.match(r"Turn \d+", sl):
                        break
                    j += 1

            # Collect influence targets for Place Influence
            inf_targets = []
            coup_target = None
            coup_region = None
            coup_stability = None
            coup_is_bg = None

            if mode == "Place Influence":
                j = i + 1
                while j < len(lines):
                    sl = lines[j].strip()
                    im = INF_RE.match(sl)
                    if im:
                        inf_side = im.group(1)
                        amount = int(im.group(2))
                        country = im.group(3).strip()
                        inf_targets.append((country, amount))
                        j += 1
                        continue
                    # Could also have opponent event firing influence after ops
                    if sl == "" or sl.startswith("Event:") or sl.startswith("Turn ") or sl.startswith("*RESHUFFLE*"):
                        break
                    # Skip non-influence lines (e.g., event text)
                    if re.match(r"(USSR|US) ", sl) and not re.search(r"\+\d", sl):
                        break
                    j += 1

            if mode == "Coup":
                j = i + 1
                while j < min(i + 8, len(lines)):
                    sl = lines[j].strip()
                    tm = COUP_TARGET_RE.match(sl)
                    if tm:
                        coup_target = tm.group(1).strip()
                        ci = get_country_info(coup_target)
                        if ci:
                            coup_region = ci["region"]
                            coup_stability = ci["stability"]
                            coup_is_bg = ci["is_bg"]
                        break
                    j += 1

            # Also check for mode in subsequent lines if it was an Event + ops action
            # e.g., "Event: CIA Created*" followed by "Place Influence (1 Ops):" — that's the event giving ops
            # But the primary mode for the card play is what's on the AR header line

            # Determine if event was also fired (opponent card triggers event)
            event_also_fired = False
            if mode in ("Place Influence", "Coup", "Realignment", "Space Race"):
                # Check subsequent lines for "Event: X" which means opponent's event fired
                j = i + 1
                while j < min(i + 30, len(lines)):
                    sl = lines[j].strip()
                    if re.match(r"Turn \d+", sl):
                        break
                    if sl.startswith("Event:"):
                        event_also_fired = True
                        break
                    j += 1

            # For scoring cards, classify as Event
            if card_name and ("Scoring" in card_name):
                mode = "Event"

            action = {
                "turn": turn,
                "phase": war_phase(turn),
                "side": side,
                "ar": ar_num,
                "card": card_name,
                "card_side": classify_card_side(card_name),
                "card_ops": get_card_ops(card_name),
                "mode": mode,
                "ops_used": ops_used,
                "inf_targets": inf_targets,
                "coup_target": coup_target,
                "coup_region": coup_region,
                "coup_stability": coup_stability,
                "coup_is_bg": coup_is_bg,
                "event_also_fired": event_also_fired,
            }
            actions.append(action)

        i += 1

    # Second pass: look for coup/realign/influence that come from event resolution
    # (after "Event: X" lines within an action round)
    # We already captured the primary action — the sub-actions from events are not separate plays

    return actions, headlines


def compute_allocation_shape(inf_targets):
    """Given list of (country, amount), return sorted tuple of amounts descending."""
    if not inf_targets:
        return ()
    amounts = sorted([a for _, a in inf_targets], reverse=True)
    return tuple(amounts)


# ── Main analysis ───────────────────────────────────────────────────────
def main():
    log_files = sorted(glob.glob(str(RAW_LOGS / "tsreplayer_*.txt")))
    print(f"Found {len(log_files)} game files")

    all_actions = []
    all_headlines = []
    game_count = 0

    for fp in log_files:
        try:
            actions, headlines = parse_game(fp)
            all_actions.extend(actions)
            all_headlines.extend(headlines)
            game_count += 1
        except Exception as e:
            print(f"  ERROR parsing {os.path.basename(fp)}: {e}")

    print(f"Parsed {game_count} games, {len(all_actions)} action rounds, {len(all_headlines)} headlines")

    # Count modes
    mode_counts = Counter(a["mode"] for a in all_actions)
    print(f"\nMode distribution: {dict(mode_counts)}")
    unknown_count = sum(1 for a in all_actions if a["mode"] is None)
    print(f"Unknown/unclassified: {unknown_count} ({100*unknown_count/len(all_actions):.1f}%)")

    # ── A. Mode distribution by side and phase ──────────────────────────
    mode_by_side_phase = defaultdict(lambda: Counter())
    for a in all_actions:
        if a["mode"] is None:
            continue
        key = (a["side"], a["phase"])
        mode_by_side_phase[key][a["mode"]] += 1

    # ── B. Influence allocation shapes ──────────────────────────────────
    alloc_by_ops = defaultdict(lambda: Counter())
    for a in all_actions:
        if a["mode"] != "Place Influence":
            continue
        if not a["inf_targets"]:
            continue
        shape = compute_allocation_shape(a["inf_targets"])
        total_ops = sum(shape)
        alloc_by_ops[total_ops][shape] += 1

    # ── C. Coup stats ───────────────────────────────────────────────────
    coups = [a for a in all_actions if a["mode"] == "Coup"]
    coup_by_region = Counter(a["coup_region"] for a in coups if a["coup_region"])
    coup_by_phase = Counter(a["phase"] for a in coups)
    coup_by_stability = Counter(a["coup_stability"] for a in coups if a["coup_stability"])
    coup_bg = Counter(a["coup_is_bg"] for a in coups if a["coup_is_bg"] is not None)

    # ── D. Regional focus ───────────────────────────────────────────────
    region_by_side_phase = defaultdict(lambda: Counter())
    for a in all_actions:
        if a["mode"] != "Place Influence":
            continue
        for country, amount in a["inf_targets"]:
            ci = get_country_info(country)
            if ci:
                region_by_side_phase[(a["side"], a["phase"])][ci["region"]] += amount

    # ── E. Headline patterns ────────────────────────────────────────────
    headline_by_side = defaultdict(lambda: Counter())
    headline_opp_card = defaultdict(int)
    headline_total = defaultdict(int)
    for h in all_headlines:
        headline_by_side[h["side"]][h["card"]] += 1
        headline_total[h["side"]] += 1
        # Check if headlining opponent's card
        cs = h["card_side"]
        if cs:
            if (h["side"] == "USSR" and cs == "US") or (h["side"] == "US" and cs == "USSR"):
                headline_opp_card[h["side"]] += 1

    # ── F. Card event firing rate ───────────────────────────────────────
    # For own-side cards: how often event vs ops?
    # For opponent-side cards: how often event vs ops?
    event_rate = defaultdict(lambda: {"event": 0, "ops": 0, "total": 0})
    for a in all_actions:
        if a["mode"] is None or a["mode"] == "Trap_Discard":
            continue
        cs = a["card_side"]
        side = a["side"]
        if cs is None:
            continue
        if cs == "Neutral":
            key = (side, "Neutral")
        elif cs == side:
            key = (side, "Own")
        else:
            key = (side, "Opponent")

        event_rate[key]["total"] += 1
        if a["mode"] == "Event":
            event_rate[key]["event"] += 1
        else:
            event_rate[key]["ops"] += 1

    # ── G. Space race ───────────────────────────────────────────────────
    space_by_side_phase = defaultdict(int)
    total_by_side_phase = defaultdict(int)
    space_card_ops = Counter()
    for a in all_actions:
        if a["mode"] is None:
            continue
        total_by_side_phase[(a["side"], a["phase"])] += 1
        if a["mode"] == "Space Race":
            space_by_side_phase[(a["side"], a["phase"])] += 1
            ops = a["card_ops"]
            if ops:
                space_card_ops[ops] += 1

    # ── Overall mode percentages ────────────────────────────────────────
    total_classified = sum(1 for a in all_actions if a["mode"] and a["mode"] != "Trap_Discard")

    # ── Generate report ─────────────────────────────────────────────────
    report = []
    report.append("# Human Game Statistics: 51 Twilight Struggle Games\n")
    report.append(f"**Games analyzed:** {game_count}")
    report.append(f"**Total action rounds:** {len(all_actions)}")
    report.append(f"**Total headlines:** {len(all_headlines)}")
    report.append(f"**Unclassified actions:** {unknown_count} ({100*unknown_count/len(all_actions):.1f}%)")
    report.append(f"**Classification rate:** {100*(1-unknown_count/len(all_actions)):.1f}%\n")

    # A. Mode distribution
    report.append("## A. Mode Distribution\n")
    report.append("### Overall\n")
    modes = ["Event", "Place Influence", "Coup", "Realignment", "Space Race", "Trap_Discard"]
    overall_mode = Counter()
    for a in all_actions:
        if a["mode"]:
            overall_mode[a["mode"]] += 1
    total_known = sum(overall_mode.values())
    report.append("| Mode | Count | % |")
    report.append("|------|------:|--:|")
    for m in modes:
        c = overall_mode.get(m, 0)
        report.append(f"| {m} | {c} | {100*c/total_known:.1f}% |")
    report.append("")

    report.append("### By Side\n")
    report.append("| Side | Event | Influence | Coup | Realign | Space | Trap |")
    report.append("|------|------:|----------:|-----:|--------:|------:|-----:|")
    for side in ["USSR", "US"]:
        total_side = sum(1 for a in all_actions if a["side"] == side and a["mode"])
        row = [side]
        for m in modes:
            c = sum(1 for a in all_actions if a["side"] == side and a["mode"] == m)
            row.append(f"{100*c/total_side:.1f}%")
        report.append("| " + " | ".join(row) + " |")
    report.append("")

    report.append("### By Side and War Phase\n")
    report.append("| Side | Phase | Event | Influence | Coup | Realign | Space | N |")
    report.append("|------|-------|------:|----------:|-----:|--------:|------:|--:|")
    for side in ["USSR", "US"]:
        for phase in ["Early", "Mid", "Late"]:
            key = (side, phase)
            mc = mode_by_side_phase[key]
            total = sum(mc.values())
            if total == 0:
                continue
            row = [side, phase]
            for m in ["Event", "Place Influence", "Coup", "Realignment", "Space Race"]:
                c = mc.get(m, 0)
                row.append(f"{100*c/total:.1f}%")
            row.append(str(total))
            report.append("| " + " | ".join(row) + " |")
    report.append("")

    # B. Allocation shapes
    report.append("## B. Influence Allocation Shapes\n")
    report.append("Distribution of how ops are spread across countries when placing influence.\n")
    for ops_count in sorted(alloc_by_ops.keys()):
        shapes = alloc_by_ops[ops_count]
        total = sum(shapes.values())
        report.append(f"### {ops_count} Ops Placed\n")
        report.append(f"N = {total}\n")
        report.append("| Shape | Count | % |")
        report.append("|-------|------:|--:|")
        for shape, count in shapes.most_common(15):
            report.append(f"| {shape} | {count} | {100*count/total:.1f}% |")
        report.append("")

    # C. Coup distribution
    report.append("## C. Coup Target Distribution\n")
    report.append(f"Total coups: {len(coups)}\n")

    report.append("### By Region\n")
    report.append("| Region | Count | % |")
    report.append("|--------|------:|--:|")
    for region, count in coup_by_region.most_common():
        report.append(f"| {region} | {count} | {100*count/len(coups):.1f}% |")
    report.append("")

    report.append("### By War Phase\n")
    report.append("| Phase | Count | % |")
    report.append("|-------|------:|--:|")
    for phase in ["Early", "Mid", "Late"]:
        c = coup_by_phase.get(phase, 0)
        report.append(f"| {phase} | {c} | {100*c/len(coups):.1f}% |")
    report.append("")

    report.append("### By Target Stability\n")
    report.append("| Stability | Count | % |")
    report.append("|-----------|------:|--:|")
    for stab in sorted(coup_by_stability.keys()):
        c = coup_by_stability[stab]
        report.append(f"| {stab} | {c} | {100*c/len(coups):.1f}% |")
    report.append("")

    report.append("### Battleground vs Non-Battleground\n")
    bg_count = coup_bg.get(True, 0)
    nbg_count = coup_bg.get(False, 0)
    bg_total = bg_count + nbg_count
    report.append(f"| Type | Count | % |")
    report.append(f"|------|------:|--:|")
    report.append(f"| Battleground | {bg_count} | {100*bg_count/bg_total:.1f}% |")
    report.append(f"| Non-BG | {nbg_count} | {100*nbg_count/bg_total:.1f}% |")
    report.append("")

    # Coups by side
    report.append("### Coups by Side\n")
    report.append("| Side | Count | % of side actions |")
    report.append("|------|------:|------------------:|")
    for side in ["USSR", "US"]:
        c = sum(1 for a in coups if a["side"] == side)
        total_side = sum(1 for a in all_actions if a["side"] == side and a["mode"])
        report.append(f"| {side} | {c} | {100*c/total_side:.1f}% |")
    report.append("")

    # D. Regional focus
    report.append("## D. Regional Focus by Phase (Influence Ops)\n")
    report.append("Shows total influence points placed per region.\n")
    for side in ["USSR", "US"]:
        report.append(f"### {side}\n")
        report.append("| Phase | Top Regions (inf placed) |")
        report.append("|-------|------------------------|")
        for phase in ["Early", "Mid", "Late"]:
            key = (side, phase)
            rc = region_by_side_phase[key]
            total = sum(rc.values())
            if total == 0:
                continue
            top3 = rc.most_common(5)
            desc = ", ".join(f"{r}: {c} ({100*c/total:.0f}%)" for r, c in top3)
            report.append(f"| {phase} | {desc} |")
        report.append("")

    # E. Headlines
    report.append("## E. Headline Patterns\n")
    for side in ["USSR", "US"]:
        report.append(f"### {side} Top Headlines\n")
        report.append("| Card | Count |")
        report.append("|------|------:|")
        for card, count in headline_by_side[side].most_common(15):
            report.append(f"| {card} | {count} |")
        total = headline_total[side]
        opp = headline_opp_card[side]
        report.append(f"\nOpponent's card headlined: {opp}/{total} ({100*opp/total:.1f}%)\n")

    # F. Event firing rate
    report.append("## F. Card Event Firing Rate\n")
    report.append("For each player: how often do they fire the event vs use for ops, by card ownership.\n")
    report.append("| Player | Card Owner | Event% | Ops% | N |")
    report.append("|--------|-----------|-------:|-----:|--:|")
    for side in ["USSR", "US"]:
        for owner in ["Own", "Opponent", "Neutral"]:
            key = (side, owner)
            d = event_rate.get(key, {"event": 0, "ops": 0, "total": 0})
            if d["total"] == 0:
                continue
            ep = 100 * d["event"] / d["total"]
            op = 100 * d["ops"] / d["total"]
            report.append(f"| {side} | {owner} | {ep:.1f}% | {op:.1f}% | {d['total']} |")
    report.append("")

    # G. Space race
    report.append("## G. Space Race Usage\n")
    report.append("### By Side and Phase\n")
    report.append("| Side | Phase | Space% | N (total) |")
    report.append("|------|-------|-------:|----------:|")
    for side in ["USSR", "US"]:
        for phase in ["Early", "Mid", "Late"]:
            key = (side, phase)
            s = space_by_side_phase[key]
            t = total_by_side_phase[key]
            if t == 0:
                continue
            report.append(f"| {side} | {phase} | {100*s/t:.1f}% | {t} |")
    report.append("")

    report.append("### Card Ops Values Spaced\n")
    report.append("| Ops | Count | % |")
    report.append("|-----|------:|--:|")
    total_sp = sum(space_card_ops.values())
    for ops in sorted(space_card_ops.keys()):
        c = space_card_ops[ops]
        report.append(f"| {ops} | {c} | {100*c/total_sp:.1f}% |")
    report.append("")

    # ── Key Findings ────────────────────────────────────────────────────
    report.append("## Key Findings\n")

    # Calculate overall percentages
    total_all = sum(overall_mode.values())
    inf_pct = 100 * overall_mode.get("Place Influence", 0) / total_all
    coup_pct = 100 * overall_mode.get("Coup", 0) / total_all
    event_pct = 100 * overall_mode.get("Event", 0) / total_all
    realign_pct = 100 * overall_mode.get("Realignment", 0) / total_all
    space_pct = 100 * overall_mode.get("Space Race", 0) / total_all

    report.append(f"1. **Mode balance:** Humans play Influence {inf_pct:.1f}%, Event {event_pct:.1f}%, "
                  f"Coup {coup_pct:.1f}%, Realignment {realign_pct:.1f}%, Space {space_pct:.1f}%")
    report.append(f"   - Our model over-coups at ~39% vs human {coup_pct:.1f}%")
    report.append(f"   - Humans event much more ({event_pct:.1f}%) than a coup-heavy model would suggest")
    report.append("")

    # Coup region distribution
    report.append("2. **Coup targets:** Humans mostly coup in:")
    for region, count in coup_by_region.most_common(3):
        report.append(f"   - {region}: {100*count/len(coups):.1f}%")
    report.append("")

    # Allocation shapes
    report.append("3. **Influence allocation:** Humans spread influence rather than stacking:")
    for ops_count in [2, 3, 4]:
        shapes = alloc_by_ops.get(ops_count, Counter())
        total = sum(shapes.values())
        if total == 0:
            continue
        top = shapes.most_common(1)[0]
        report.append(f"   - {ops_count} ops: most common shape {top[0]} = {100*top[1]/total:.1f}%")
    report.append("")

    report.append("4. **Europe in Early War:** Humans place influence in Europe during Early War:")
    for side in ["USSR", "US"]:
        key = (side, "Early")
        rc = region_by_side_phase[key]
        total = sum(rc.values())
        eu = rc.get("Europe", 0)
        if total > 0:
            report.append(f"   - {side}: {eu} inf ({100*eu/total:.0f}% of Early War influence)")
    report.append("")

    report.append("## Implications for Training\n")
    report.append("1. **Coup penalty/reward shaping:** Model over-coups at 39% vs human ~{:.0f}%. "
                  "Consider adding coup frequency as an auxiliary loss or reward penalty.".format(coup_pct))
    report.append("2. **Event firing:** Humans fire events much more often. The model should learn "
                  "when events are strategically valuable, not just default to ops.")
    report.append("3. **Europe focus:** If the model ignores Europe in Early War, it diverges "
                  "from human strategy. Europe scoring dominance is critical in competitive play.")
    report.append("4. **Influence spreading:** Humans often split influence across 2-3 countries "
                  "rather than stacking all ops in one. This diversification reduces risk.")
    report.append("5. **Space race as dump:** Humans space ~{:.0f}% of actions — a meaningful "
                  "escape valve for opponent cards. Model should learn this pattern.".format(space_pct))
    report.append("")

    # Write report
    out_path = ROOT / "results" / "human_game_stats.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.write("\n".join(report))

    print(f"\nReport written to {out_path}")
    print(f"Classification rate: {100*(1-unknown_count/len(all_actions)):.1f}%")


if __name__ == "__main__":
    main()
