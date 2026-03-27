"""Tests for the game data loader (cards, countries, adjacency)."""
import pytest
from tsrl.etl.game_data import (
    card_name_index,
    country_name_index,
    initial_influence,
    load_cards,
    load_countries,
)
from tsrl.schemas import Era, Side


def test_cards_load():
    cards = load_cards()
    assert len(cards) > 100, f"Expected ~108+ cards, got {len(cards)}"


def test_cards_all_have_valid_ops():
    for cid, c in load_cards().items():
        assert 0 <= c.ops <= 4, f"Card {cid} ({c.name}) has invalid ops {c.ops}"


def test_scoring_cards_have_zero_ops():
    for cid, c in load_cards().items():
        if c.is_scoring:
            assert c.ops == 0, f"Scoring card {cid} ({c.name}) should have ops=0"


def test_cards_known_early_war():
    """Spot-check a few well-known Early War cards."""
    cards = load_cards()
    names = {c.name.lower() for c in cards.values()}
    # These are in every standard TS deck:
    for expected in ["asia scoring", "europe scoring", "middle east scoring"]:
        assert expected in names, f"Missing scoring card: {expected}"


def test_cards_have_expected_sides():
    cards = load_cards()
    us_count = sum(1 for c in cards.values() if c.side == Side.US)
    ussr_count = sum(1 for c in cards.values() if c.side == Side.USSR)
    neutral_count = sum(1 for c in cards.values() if c.side == Side.NEUTRAL)
    # Rough counts: ~45 US, ~45 USSR, ~20 neutral (scoring + special)
    assert us_count > 30, f"Too few US cards: {us_count}"
    assert ussr_count > 30, f"Too few USSR cards: {ussr_count}"
    assert neutral_count >= 3, f"Too few neutral/scoring cards: {neutral_count}"


def test_countries_load():
    countries = load_countries()
    assert len(countries) > 50, f"Expected 50+ countries, got {len(countries)}"


def test_battleground_countries_exist():
    countries = load_countries()
    battlegrounds = [c for c in countries.values() if c.is_battleground]
    # TS has ~22 battleground countries
    assert len(battlegrounds) >= 20, f"Too few battlegrounds: {len(battlegrounds)}"


def test_stability_range():
    for cid, c in load_countries().items():
        if c.stability == 0:
            # Superpower anchor entries (USA/USSR) have stability=0 by design.
            continue
        assert 1 <= c.stability <= 5, f"Country {cid} ({c.name}) has invalid stability {c.stability}"


def test_initial_influence_us_west_germany():
    """West Germany starts with 4 US influence."""
    countries = load_countries()
    inf = initial_influence()
    wg = next((c for c in countries.values() if "west germany" in c.name.lower()), None)
    if wg:
        assert inf.get((Side.US, wg.country_id), 0) == 4, "West Germany should start with 4 US influence"


def test_initial_influence_ussr_poland():
    """Poland starts with 4 USSR influence."""
    countries = load_countries()
    inf = initial_influence()
    poland = next((c for c in countries.values() if "poland" in c.name.lower()), None)
    if poland:
        assert inf.get((Side.USSR, poland.country_id), 0) == 4, "Poland should start with 4 USSR influence"


def test_card_name_index_is_lowercase():
    idx = card_name_index()
    for k in idx:
        assert k == k.lower()


def test_country_name_index():
    idx = country_name_index()
    assert len(idx) > 50
