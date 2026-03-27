"""Tests for the replay log parser.

Validates patterns against real TSEspionage/ACTS log format.
Golden-log integration tests live in test_parser_golden.py.
"""
import pytest
from tsrl.etl.parser import ParseResult, parse_replay
from tsrl.schemas import EventKind, Side


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def events_of(result: ParseResult, kind: EventKind):
    return [e for e in result.events if e.kind == kind]


def parse(text: str) -> ParseResult:
    return parse_replay(text)


# ---------------------------------------------------------------------------
# SETUP block
# ---------------------------------------------------------------------------


def test_setup_emits_game_start():
    r = parse("SETUP: : brown_town will play as USSR.")
    assert events_of(r, EventKind.GAME_START)


def test_setup_us_player_not_unknown():
    r = parse("SETUP: : brown_town will play as USSR.\nLogarius will play as USA.")
    assert r.unknown_line_count == 0


def test_setup_info_lines_not_unknown():
    lines = "\n".join([
        "SETUP: : player1 will play as USSR.",
        "player2 will play as USA.",
        "Handicap influence: US +2",
        "Scenario: Standard",
        "Optional Cards Added",
        "Time per Player: 1 Hour",
        "player1 bids 0 Influence for USSR",
    ])
    r = parse(lines)
    assert r.unknown_line_count == 0


def test_setup_influence_emits_place_influence():
    r = parse("SETUP: : p1 will play as USSR.\nUSSR +4 in Poland [0][4]")
    infl = events_of(r, EventKind.PLACE_INFLUENCE)
    assert len(infl) == 1
    assert infl[0].phasing == Side.USSR
    assert infl[0].amount == 4
    assert infl[0].turn == 0   # setup: turn=0


def test_setup_us_influence():
    r = parse("SETUP: : p1 will play as USSR.\nUS +3 in West Germany [3][0]")
    infl = events_of(r, EventKind.PLACE_INFLUENCE)
    assert infl[0].phasing == Side.US
    assert infl[0].amount == 3


# ---------------------------------------------------------------------------
# Headline phase
# ---------------------------------------------------------------------------


def test_headline_phase_emits_headline_phase_start():
    r = parse("Turn 1, Headline Phase: Vietnam Revolts* & Marshall Plan*: DEFCON improves to 3")
    evs = events_of(r, EventKind.HEADLINE_PHASE_START)
    assert len(evs) == 1
    assert evs[0].turn == 1


def test_headline_phase_inline_defcon():
    r = parse("Turn 1, Headline Phase: Asia Scoring & Olympic Games: DEFCON improves to 3")
    defcon_evs = events_of(r, EventKind.DEFCON_CHANGE)
    assert len(defcon_evs) == 1
    assert defcon_evs[0].amount == 3


def test_headline_phase_inline_ussr_headlines():
    r = parse(
        "Turn 1, Headline Phase: Captured Nazi Scientist* & Containment*: "
        "USSR Headlines Captured Nazi Scientist*"
    )
    h = events_of(r, EventKind.HEADLINE)
    assert len(h) == 1
    assert h[0].phasing == Side.USSR


def test_headline_phase_no_inline():
    # Some logs have no inline text
    r = parse("Turn 1, Headline Phase: Vietnam Revolts* & Marshall Plan*:")
    assert events_of(r, EventKind.HEADLINE_PHASE_START)
    assert r.unknown_line_count == 0


def test_ussr_headlines_subline():
    r = parse(
        "Turn 1, Headline Phase: Asia Scoring & Olympic Games:\n"
        "USSR Headlines Asia Scoring"
    )
    h = events_of(r, EventKind.HEADLINE)
    ussr_h = [e for e in h if e.phasing == Side.USSR]
    assert ussr_h


def test_us_headlines_subline():
    r = parse(
        "Turn 1, Headline Phase: Asia Scoring & Olympic Games:\n"
        "US Headlines Olympic Games"
    )
    h = events_of(r, EventKind.HEADLINE)
    us_h = [e for e in h if e.phasing == Side.US]
    assert us_h


def test_headline_ar_is_zero():
    r = parse(
        "Turn 2, Headline Phase: Red Scare/Purge & Defectors:\n"
        "USSR Headlines Red Scare/Purge"
    )
    h = events_of(r, EventKind.HEADLINE)
    assert h[0].ar == 0


# ---------------------------------------------------------------------------
# Action rounds
# ---------------------------------------------------------------------------


def test_action_round_emits_ar_start():
    r = parse("Turn 1, USSR AR1: East European Unrest: Place Influence (3 Ops):")
    evs = events_of(r, EventKind.ACTION_ROUND_START)
    assert len(evs) == 1
    assert evs[0].turn == 1
    assert evs[0].ar == 1
    assert evs[0].phasing == Side.USSR


def test_action_round_us_phasing():
    r = parse("Turn 1, US AR1: NORAD*: Coup (4 Ops):")
    evs = events_of(r, EventKind.ACTION_ROUND_START)
    assert evs[0].phasing == Side.US


def test_action_round_context_propagates():
    text = "\n".join([
        "Turn 3, USSR AR2: Nasser*: Event: Nasser*",
        "USSR +2 in Egypt [2][2]",
    ])
    r = parse(text)
    infl = events_of(r, EventKind.PLACE_INFLUENCE)
    assert infl[0].turn == 3
    assert infl[0].ar == 2


def test_action_round_inline_event_announce_not_unknown():
    r = parse("Turn 1, USSR AR1: Duck and Cover: Event: Duck and Cover")
    assert r.unknown_line_count == 0


def test_action_round_empty_action_not_unknown():
    # "Turn 2, US AR6: : " — player passes or no action
    r = parse("Turn 2, US AR6: : ")
    assert r.unknown_line_count == 0
    evs = events_of(r, EventKind.ACTION_ROUND_START)
    assert evs[0].phasing == Side.US
    assert evs[0].ar == 6


def test_action_round_inline_trap_discard():
    # "Turn 7, USSR AR1: Containment*: USSR discards Containment*"
    r = parse("Turn 7, USSR AR1: Containment*: USSR discards Containment*")
    fd = events_of(r, EventKind.FORCED_DISCARD)
    assert len(fd) == 1
    assert fd[0].phasing == Side.USSR


def test_action_round_inline_card_expired():
    r = parse("Turn 5, US AR2: The China Card: Formosan Resolution* is no longer in play.")
    exp = events_of(r, EventKind.CARD_EXPIRED)
    assert len(exp) == 1


# ---------------------------------------------------------------------------
# Cleanup
# ---------------------------------------------------------------------------


def test_cleanup_emits_turn_end():
    r = parse("Turn 5, Cleanup: : Vietnam Revolts* is no longer in play.")
    evs = events_of(r, EventKind.TURN_END)
    assert len(evs) == 1
    assert evs[0].turn == 5


def test_cleanup_inline_card_expired():
    r = parse("Turn 5, Cleanup: : Vietnam Revolts* is no longer in play.")
    exp = events_of(r, EventKind.CARD_EXPIRED)
    assert len(exp) == 1


def test_cleanup_inline_vp():
    r = parse("Turn 9, Cleanup: : USSR gains 2 VP. Score is USSR 10.")
    vp = events_of(r, EventKind.VP_CHANGE)
    assert len(vp) == 1
    assert vp[0].amount == 2  # USSR gains → positive


def test_cleanup_hand_limit_discard():
    r = parse(
        "Turn 5, Cleanup: : \n"
        "USSR discards Panama Canal Returned*"
    )
    fd = events_of(r, EventKind.FORCED_DISCARD)
    assert len(fd) == 1
    assert fd[0].phasing == Side.USSR


def test_cleanup_empty_not_unknown():
    r = parse("Turn 9, Cleanup: : ")
    assert r.unknown_line_count == 0


# ---------------------------------------------------------------------------
# Game end
# ---------------------------------------------------------------------------


def test_game_end_emits_game_end():
    r = parse(": : US gains 26 VP. Score is US 38.")
    evs = events_of(r, EventKind.GAME_END)
    assert len(evs) == 1


def test_game_end_also_has_vp():
    r = parse(": : US gains 26 VP. Score is US 38.")
    vp = events_of(r, EventKind.VP_CHANGE)
    assert len(vp) == 1
    assert vp[0].amount == -26  # US gains → negative convention


# ---------------------------------------------------------------------------
# Influence sub-lines
# ---------------------------------------------------------------------------


def test_influence_positive():
    r = parse("Turn 1, USSR AR1: Test: Place Influence (3 Ops):\nUSSR +3 in Thailand [0][3]")
    infl = events_of(r, EventKind.PLACE_INFLUENCE)
    assert infl[0].amount == 3
    assert infl[0].phasing == Side.USSR


def test_influence_negative():
    r = parse(
        "Turn 1, USSR AR3: Socialist Governments: Coup (3 Ops):\n"
        "US -2 in Iran [0][0]"
    )
    rm = events_of(r, EventKind.REMOVE_INFLUENCE)
    assert len(rm) == 1
    assert rm[0].amount == 2
    assert rm[0].phasing == Side.US


# ---------------------------------------------------------------------------
# DEFCON
# ---------------------------------------------------------------------------


def test_defcon_degrades():
    r = parse(
        "Turn 1, USSR AR3: Socialist Governments: Coup (3 Ops):\n"
        "DEFCON degrades to 4"
    )
    dc = events_of(r, EventKind.DEFCON_CHANGE)
    assert dc[0].amount == 4


def test_defcon_improves():
    r = parse("Turn 2, Headline Phase: Asia Scoring & Olympic Games: DEFCON improves to 5")
    dc = events_of(r, EventKind.DEFCON_CHANGE)
    assert dc[0].amount == 5


# ---------------------------------------------------------------------------
# VP
# ---------------------------------------------------------------------------


def test_vp_ussr_gains():
    r = parse(
        "Turn 1, USSR AR5: Captured Nazi Scientist*: Event: Captured Nazi Scientist*\n"
        "USSR gains 2 VP. Score is USSR 2."
    )
    vp = events_of(r, EventKind.VP_CHANGE)
    assert vp[0].amount == 2   # positive = USSR advantage


def test_vp_us_gains():
    r = parse(
        "Turn 1, US AR5: Decolonization: Space Race (2 Ops):\n"
        "US gains 1 VP. Score is USSR 1."
    )
    vp = events_of(r, EventKind.VP_CHANGE)
    assert vp[0].amount == -1  # negative = US advantage


def test_no_vp_not_unknown():
    r = parse(
        "Turn 1, US AR3: Asia Scoring: Event: Asia Scoring\n"
        "No VP awarded. Score is US 3."
    )
    assert r.unknown_line_count == 0
    vp = events_of(r, EventKind.VP_CHANGE)
    assert len(vp) == 0   # "No VP awarded" emits nothing


# ---------------------------------------------------------------------------
# MilOps
# ---------------------------------------------------------------------------


def test_milops_ussr():
    r = parse(
        "Turn 1, USSR AR1: Warsaw Pact Formed*: Coup (3 Ops):\n"
        "USSR Military Ops to 3"
    )
    mo = events_of(r, EventKind.MILOPS_CHANGE)
    assert mo[0].phasing == Side.USSR
    assert mo[0].amount == 3


def test_milops_us():
    r = parse(
        "Turn 1, US AR1: NORAD*: Coup (3 Ops):\n"
        "US Military Ops to 3"
    )
    mo = events_of(r, EventKind.MILOPS_CHANGE)
    assert mo[0].phasing == Side.US
    assert mo[0].amount == 3


# ---------------------------------------------------------------------------
# Space Race
# ---------------------------------------------------------------------------


def test_space_advance():
    r = parse(
        "Turn 1, US AR5: Decolonization: Space Race (2 Ops):\n"
        "US advances to 1 in the Space Race."
    )
    sp = events_of(r, EventKind.SPACE_RACE)
    assert sp[0].phasing == Side.US
    assert sp[0].amount == 1


# ---------------------------------------------------------------------------
# Card state events
# ---------------------------------------------------------------------------


def test_card_in_play():
    r = parse(
        "Turn 1, Headline Phase: Vietnam Revolts* & Marshall Plan*:\n"
        "Event: Marshall Plan*\n"
        "Marshall Plan* is now in play."
    )
    evs = events_of(r, EventKind.CARD_IN_PLAY)
    assert len(evs) == 1


def test_card_expired():
    r = parse("Turn 5, Cleanup: : Vietnam Revolts* is no longer in play.")
    evs = events_of(r, EventKind.CARD_EXPIRED)
    assert len(evs) == 1


# ---------------------------------------------------------------------------
# Card movement
# ---------------------------------------------------------------------------


def test_forced_discard_standalone():
    # "US discards Decolonization"  (e.g. from Blockade)
    r = parse(
        "Turn 1, US AR3: Blockade*: Event: Blockade*\n"
        "US discards Decolonization"
    )
    fd = events_of(r, EventKind.FORCED_DISCARD)
    assert len(fd) == 1
    assert fd[0].phasing == Side.US


def test_reveal_hand():
    r = parse(
        "Turn 1, USSR AR6: CIA Created*: Event: CIA Created*\n"
        "USSR reveals De Gaulle Leads France*"
    )
    rv = events_of(r, EventKind.REVEAL_HAND)
    assert len(rv) == 1
    assert rv[0].phasing == Side.USSR


def test_reveal_from_hand_variant():
    r = parse(
        "Turn 5, Headline Phase: Grain Sales To Soviets & Willy Brandt*:\n"
        "Event: Grain Sales To Soviets\n"
        "USSR reveals Central America Scoring from hand"
    )
    rv = events_of(r, EventKind.REVEAL_HAND)
    assert rv[0].phasing == Side.USSR


def test_transfer():
    r = parse("US returns Central America Scoring to USSR")
    tr = events_of(r, EventKind.TRANSFER)
    assert len(tr) == 1
    assert tr[0].phasing == Side.US  # US is the sender


def test_un_intervention_opponent_card():
    # "USSR plays Bear Trap*" means USSR (via UN Intervention) uses a US card.
    # Bear Trap* leaves the US hand.
    r = parse(
        "Turn 4, USSR AR2: UN Intervention: Event: UN Intervention\n"
        "USSR plays Bear Trap*"
    )
    fd = events_of(r, EventKind.FORCED_DISCARD)
    assert len(fd) == 1
    assert fd[0].phasing == Side.US  # card leaves US hand


# ---------------------------------------------------------------------------
# Reshuffle
# ---------------------------------------------------------------------------


def test_reshuffle():
    r = parse(
        "Turn 3, Headline Phase: Red Scare/Purge & Olympic Games: DEFCON improves to 3\n"
        "*RESHUFFLE*"
    )
    evs = events_of(r, EventKind.RESHUFFLE)
    assert len(evs) == 1


# ---------------------------------------------------------------------------
# Informational sub-lines (must not appear as unknown)
# ---------------------------------------------------------------------------


def test_coup_info_not_unknown():
    lines = "\n".join([
        "Turn 1, USSR AR1: Warsaw Pact Formed*: Coup (3 Ops):",
        "Target: Iran",
        "SUCCESS: 3 [ + 3 - 2x2 = 2 ]",
        "US -1 in Iran [0][0]",
        "USSR +1 in Iran [0][1]",
        "USSR Military Ops to 3",
        "DEFCON degrades to 4",
    ])
    r = parse(lines)
    assert r.unknown_line_count == 0


def test_space_race_info_not_unknown():
    lines = "\n".join([
        "Turn 1, US AR5: Decolonization: Space Race (2 Ops):",
        "Die roll: 1 -- Success! (Needed 3 or less)",
        "US advances to 1 in the Space Race.",
        "US gains 1 VP. Score is USSR 1.",
    ])
    r = parse(lines)
    assert r.unknown_line_count == 0


def test_realignment_info_not_unknown():
    lines = "\n".join([
        "Turn 4, USSR AR4: Indo-Pakistani War: Realignment (2 Ops):",
        "Target: Panama",
        "USSR rolls 6",
        "US rolls 2 (+1) = 3",
        "US -2 in Panama [0][0]",
    ])
    r = parse(lines)
    assert r.unknown_line_count == 0


def test_war_result_not_unknown():
    lines = "\n".join([
        "Turn 2, USSR AR2: Indo-Pakistani War: Event: Indo-Pakistani War",
        "War in Pakistan",
        "DEFEAT: 1 < 4",
        "USSR Military Ops to 5",
    ])
    r = parse(lines)
    assert r.unknown_line_count == 0


def test_trap_roll_not_unknown():
    r = parse("Trap Roll: 3 <= 4 -- Trap Escaped")
    assert r.unknown_line_count == 0


def test_olympics_not_unknown():
    r = parse("USSR chooses to participate in the Olympics")
    assert r.unknown_line_count == 0


def test_no_cards_to_reveal_not_unknown():
    r = parse("US has no cards to reveal")
    assert r.unknown_line_count == 0


# ---------------------------------------------------------------------------
# Unknown line handling (invariant: never silently dropped)
# ---------------------------------------------------------------------------


def test_unknown_lines_not_dropped():
    r = parse("Turn 1, USSR AR1: Test: Place Influence (1 Ops):\nsome completely unknown line")
    unknown_evs = [e for e in r.events if e.kind == EventKind.UNKNOWN]
    assert len(unknown_evs) == 1
    assert "some completely unknown line" in unknown_evs[0].raw_line


def test_unknown_lines_tracked_in_result():
    r = parse("unknown line 1\nunknown line 2")
    assert r.unknown_line_count == 2
    assert len(r.unknown_lines) == 2


def test_coverage_all_known():
    text = "\n".join([
        "SETUP: : p1 will play as USSR.",
        "p2 will play as USA.",
        "USSR +4 in Poland [0][4]",
        "Turn 1, Headline Phase: Asia Scoring & Olympic Games:",
        "USSR Headlines Asia Scoring",
        "US Headlines Olympic Games",
        "Turn 1, USSR AR1: COMECON*: Place Influence (3 Ops):",
        "USSR Military Ops to 3",
        "Turn 1, Cleanup: : ",
    ])
    r = parse(text)
    assert r.line_parse_coverage == 1.0


def test_empty_replay():
    r = parse("")
    assert r.events == []
    assert r.unknown_line_count == 0
    assert r.line_parse_coverage == 1.0


# ---------------------------------------------------------------------------
# Multi-turn context propagation
# ---------------------------------------------------------------------------


def test_turn_propagates_across_lines():
    text = "\n".join([
        "Turn 3, USSR AR2: Nasser*: Event: Nasser*",
        "USSR +2 in Egypt [2][2]",
        "US -1 in Egypt [1][2]",
    ])
    r = parse(text)
    infl = events_of(r, EventKind.PLACE_INFLUENCE) + events_of(r, EventKind.REMOVE_INFLUENCE)
    for e in infl:
        assert e.turn == 3
        assert e.ar == 2


def test_phasing_changes_between_ars():
    text = "\n".join([
        "Turn 1, USSR AR1: COMECON*: Place Influence (3 Ops):",
        "USSR +3 in Thailand [0][3]",
        "Turn 1, US AR1: Duck and Cover: Place Influence (3 Ops):",
        "US +3 in France [3][0]",
    ])
    r = parse(text)
    ar_evs = events_of(r, EventKind.ACTION_ROUND_START)
    assert ar_evs[0].phasing == Side.USSR
    assert ar_evs[1].phasing == Side.US


# ---------------------------------------------------------------------------
# Nixon Plays The China Card event emission
# ---------------------------------------------------------------------------


def test_nixon_event_emits_china_card_pass():
    """When Nixon fires as an EVENT, parser must emit CHINA_CARD_PASS(phasing=US).

    Regression: "Event: Nixon Plays The China Card*" was parsed as an INFO line
    (no events emitted), so china_held_by was never updated after Nixon fired.
    """
    text = "\n".join([
        "Turn 7, US AR7: Nixon Plays The China Card*: Event: Nixon Plays The China Card*",
    ])
    r = parse(text)
    china_passes = events_of(r, EventKind.CHINA_CARD_PASS)
    assert len(china_passes) == 1, (
        f"Expected 1 CHINA_CARD_PASS event, got {len(china_passes)}: {china_passes}"
    )
    assert china_passes[0].phasing == Side.US, (
        "Nixon event should give China Card to US"
    )
