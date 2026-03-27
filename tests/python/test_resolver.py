"""Tests for the name-to-ID resolver pass."""
import pytest
from tsrl.etl.game_data import load_cards, load_countries
from tsrl.etl.resolver import (
    _norm_card,
    _norm_country,
    build_indexes,
    resolve_names,
)
from tsrl.schemas import EventKind, ReplayEvent, Side


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------


def test_norm_card_strips_star():
    assert _norm_card("Marshall Plan*") == "marshall plan"


def test_norm_card_strips_quotes():
    assert _norm_card('"Lone Gunman"') == "lone gunman"


def test_norm_card_strips_star_and_quotes():
    assert _norm_card('"Lone Gunman"*') == "lone gunman"


def test_norm_card_replaces_hyphen():
    assert _norm_card("KAL-007") == "kal 007"


def test_norm_card_lowercases():
    assert _norm_card("Duck and Cover") == "duck and cover"


def test_norm_country_lowercases():
    assert _norm_country("West Germany") == "west germany"


# ---------------------------------------------------------------------------
# Index building
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def indexes():
    cards = load_cards()
    countries = load_countries()
    return build_indexes(cards, countries)


def test_card_index_has_china_card(indexes):
    card_idx, _ = indexes
    assert card_idx.get("china card") == 6


def test_card_index_alias_the_china_card(indexes):
    card_idx, _ = indexes
    assert card_idx.get("the china card") == 6


def test_card_index_alias_mideast_scoring(indexes):
    card_idx, _ = indexes
    assert card_idx.get("mideast scoring") == 3


def test_card_index_alias_voice_of_america(indexes):
    card_idx, _ = indexes
    assert card_idx.get("the voice of america") == 75


def test_card_index_alias_ask_not(indexes):
    card_idx, _ = indexes
    # Log emits: "Ask Not What Your Country..."*
    assert card_idx.get("ask not what your country...") == 78


def test_card_index_alias_one_small_step(indexes):
    card_idx, _ = indexes
    assert card_idx.get("one small step...") == 81


def test_card_index_kal_hyphen(indexes):
    """'Soviets Shoot Down KAL-007' should resolve via hyphen→space normalization."""
    card_idx, _ = indexes
    norm = _norm_card("Soviets Shoot Down KAL-007")
    assert card_idx.get(norm) == 92


def test_card_index_promo_lone_gunman(indexes):
    card_idx, _ = indexes
    assert card_idx.get("lone gunman") == 109


def test_card_index_promo_colonial_rear_guards(indexes):
    card_idx, _ = indexes
    assert card_idx.get("colonial rear guards") == 110


def test_card_index_promo_panama_canal_returned(indexes):
    card_idx, _ = indexes
    assert card_idx.get("panama canal returned") == 111


def test_country_index_alias_zaire(indexes):
    _, country_idx = indexes
    assert country_idx.get("zaire") == 60


def test_country_index_alias_congo(indexes):
    _, country_idx = indexes
    assert country_idx.get("congo") == 60


def test_country_index_alias_indonesia(indexes):
    _, country_idx = indexes
    assert country_idx.get("indonesia") == 76


def test_country_index_alias_malaysia(indexes):
    # Malaysia is now a separate country from Indonesia (id=84 in countries.csv).
    _, country_idx = indexes
    assert country_idx.get("malaysia") == 84


def test_country_index_bulgaria(indexes):
    _, country_idx = indexes
    assert country_idx.get("bulgaria") == 83


# ---------------------------------------------------------------------------
# resolve_names
# ---------------------------------------------------------------------------


def _ev(kind, card_name=None, country_name=None):
    return ReplayEvent(
        kind=kind, turn=1, ar=1, phasing=Side.USSR,
        card_name=card_name, country_name=country_name,
    )


def test_resolve_names_fills_card_id():
    cards = load_cards()
    countries = load_countries()
    evs = [_ev(EventKind.PLAY, card_name="Marshall Plan")]
    result = resolve_names(evs, cards, countries, warn_unresolved=False)
    assert result[0].card_id is not None


def test_resolve_names_fills_country_id():
    cards = load_cards()
    countries = load_countries()
    evs = [_ev(EventKind.PLACE_INFLUENCE, country_name="West Germany")]
    result = resolve_names(evs, cards, countries, warn_unresolved=False)
    assert result[0].country_id == 18


def test_resolve_names_alias_the_china_card():
    cards = load_cards()
    countries = load_countries()
    evs = [_ev(EventKind.PLAY, card_name="The China Card")]
    result = resolve_names(evs, cards, countries, warn_unresolved=False)
    assert result[0].card_id == 6


def test_resolve_names_alias_zaire():
    cards = load_cards()
    countries = load_countries()
    evs = [_ev(EventKind.PLACE_INFLUENCE, country_name="Zaire")]
    result = resolve_names(evs, cards, countries, warn_unresolved=False)
    assert result[0].country_id == 60


def test_resolve_names_quoted_lone_gunman():
    cards = load_cards()
    countries = load_countries()
    evs = [_ev(EventKind.PLAY, card_name='"Lone Gunman"*')]
    result = resolve_names(evs, cards, countries, warn_unresolved=False)
    assert result[0].card_id == 109


def test_resolve_names_skips_already_resolved():
    """Events with card_id already set are not overwritten."""
    cards = load_cards()
    countries = load_countries()
    ev = ReplayEvent(
        kind=EventKind.PLAY, turn=1, ar=1, phasing=Side.USSR,
        card_id=99, card_name="Marshall Plan",
    )
    result = resolve_names([ev], cards, countries, warn_unresolved=False)
    assert result[0].card_id == 99


def test_resolve_names_warns_on_unknown(recwarn):
    cards = load_cards()
    countries = load_countries()
    evs = [_ev(EventKind.PLAY, card_name="NONEXISTENT CARD XYZ")]
    resolve_names(evs, cards, countries, warn_unresolved=True)
    assert any("NONEXISTENT CARD XYZ" in str(w.message) for w in recwarn.list)


def test_resolve_names_no_warn_when_disabled():
    import warnings
    cards = load_cards()
    countries = load_countries()
    evs = [_ev(EventKind.PLAY, card_name="NONEXISTENT CARD XYZ")]
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        resolve_names(evs, cards, countries, warn_unresolved=False)  # must not raise
