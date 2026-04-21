"""
Region scoring for Twilight Struggle.

Scoring rules (GMT Deluxe Edition §10.1):

Control condition (§2.1.7):
  own_influence >= opponent_influence + country_stability

Tier determination (§10.1.1):
  CONTROL    : controls ALL battlegrounds AND more total countries than opponent
  DOMINATION : more total countries than opponent AND more battlegrounds than opponent
               AND controls >=1 non-BG AND >=1 BG country
  PRESENCE   : controls >= 1 country (battleground or not)
  NONE       : controls 0 countries

Scoring formula (§10.1.2) — BOTH sides score independently, net is the VP delta:
  side_VP = tier_base_VP
           + 1 per Battleground country controlled in region
           + 1 per country controlled adjacent to the ENEMY superpower

  vp_delta = USSR_VP - US_VP  (positive = USSR gains, negative = US gains)

VP base amounts:
  Region           Presence  Domination  Control
  Europe           3         7           GAME WIN
  Asia             3         7           9
  Middle East      3         5           7
  Central America  1         3           5
  South America    2         5           6
  Africa           1         4           6

Asia scoring also awards +1 VP to whoever holds the China Card. Asia scoring
includes Southeast Asia countries; Southeast Asia Scoring (card #41) is a
separate overlapping scoring card with special per-country rules.

Southeast Asia scoring (card #41 text):
  Each controlled country: 1 VP; Thailand: 2 VP.  No §10.1.2 BG/adj bonuses.

Notes:
  - Country id=64 (erroneous Libya/Africa duplicate) is excluded.
  - Superpower anchors (id=81, 82) are excluded from scoring but ARE used for
    adjacency checks (§10.1.2 "adjacent to enemy superpower").
  - Congo/Zaire (id=60) IS a battleground (TS Deluxe has 5 Africa BGs).
"""
from __future__ import annotations

from ._deprecation import warn_engine_deprecated

warn_engine_deprecated(__name__)

from collections import defaultdict
from dataclasses import dataclass
from enum import IntEnum, auto

from tsrl.etl.game_data import CountrySpec, load_adjacency, load_countries
from tsrl.schemas import PublicState, Region, Side

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_EXCLUDED_IDS: frozenset[int] = frozenset({
    64,  # erroneous Libya/Africa duplicate; Libya is Middle East (id=33)
    81,  # USA superpower anchor — excluded from country lists but used in adjacency
    82,  # USSR superpower anchor — excluded from country lists but used in adjacency
})

# Superpower IDs for adjacency bonus (§10.1.2 "adjacent to enemy superpower").
_USA_ID: int = 81
_USSR_ID: int = 82
_TAIWAN_ID: int = 85

# Special VP value meaning "Europe Control → immediate game win".
GAME_WIN_EUROPE: int = 9999

# VP tables: (presence_vp, domination_vp, control_vp)
# Positive = USSR gain, negative = US gain applied by caller.
_REGION_VP: dict[Region, tuple[int, int, int]] = {
    Region.EUROPE:          (3, 7, GAME_WIN_EUROPE),
    Region.ASIA:            (3, 7, 9),
    Region.MIDDLE_EAST:     (3, 5, 7),
    Region.CENTRAL_AMERICA: (1, 3, 5),
    Region.SOUTH_AMERICA:   (2, 5, 6),
    Region.AFRICA:          (1, 4, 6),
    # SOUTHEAST_ASIA handled separately
}

# Southeast Asia VP per country (card text, ITS rules).
# Thailand = 2 VP (from Southeast Asia Scoring card text; not derived from is_battleground).
# Indonesia and Malaysia are SEPARATE countries in the TSEspionage mod (each 1 VP).
# Coup logs confirm: Indonesia stab=1, Malaysia stab=2.
_SE_ASIA_COUNTRY_VP: dict[int, int] = {
    75: 1,  # Burma
    76: 1,  # Indonesia (stab=1)
    77: 1,  # Laos/Cambodia
    78: 1,  # Philippines
    79: 2,  # Thailand (2 VP per card text)
    80: 1,  # Vietnam
    84: 1,  # Malaysia (stab=2, non-battleground)
}


# ---------------------------------------------------------------------------
# Tier enum
# ---------------------------------------------------------------------------


class Tier(IntEnum):
    NONE       = 0
    PRESENCE   = 1
    DOMINATION = 2
    CONTROL    = 3


# ---------------------------------------------------------------------------
# Country and adjacency helpers
# ---------------------------------------------------------------------------

_COUNTRY_CACHE: dict[int, CountrySpec] | None = None
_ADJ_CACHE: dict[int, frozenset[int]] | None = None


def _countries() -> dict[int, CountrySpec]:
    global _COUNTRY_CACHE
    if _COUNTRY_CACHE is None:
        _COUNTRY_CACHE = load_countries()
    return _COUNTRY_CACHE


def _adj_map() -> dict[int, frozenset[int]]:
    """Return adjacency as {country_id: frozenset of neighbor_ids}."""
    global _ADJ_CACHE
    if _ADJ_CACHE is None:
        raw: frozenset[tuple[int, int]] = load_adjacency()
        tmp: dict[int, set[int]] = defaultdict(set)
        for a, b in raw:
            tmp[a].add(b)
            tmp[b].add(a)
        _ADJ_CACHE = {k: frozenset(v) for k, v in tmp.items()}
    return _ADJ_CACHE


def _is_scoring_battleground(
    country_id: int,
    pub: PublicState,
    countries: dict[int, CountrySpec],
) -> bool:
    """Return whether a country counts as a battleground for scoring."""
    return countries[country_id].is_battleground or (
        country_id == _TAIWAN_ID and pub.formosan_active
    )


def _controls(side: Side, country_id: int, pub: PublicState) -> bool:
    """True iff side controls the country.

    Control: own_influence >= opponent_influence + country_stability.
    """
    opp = Side.US if side == Side.USSR else Side.USSR
    own = pub.influence.get((side, country_id), 0)
    opp_inf = pub.influence.get((opp, country_id), 0)
    stability = _countries()[country_id].stability
    return own >= opp_inf + stability


# ---------------------------------------------------------------------------
# Scoring functions
# ---------------------------------------------------------------------------


@dataclass
class ScoringResult:
    """Result of scoring one region card."""
    vp_delta: int   # positive = USSR gains, negative = US gains
    game_over: bool = False
    winner: Side | None = None
    clear_shuttle: bool = False  # True if Shuttle Diplomacy (74) was consumed


def score_region(region: Region, pub: PublicState) -> ScoringResult:
    """Compute VP change for a standard region scoring card.

    Implements §10.1 bilateral scoring:
      - Both sides independently earn: tier_base + BG_bonus + adj_enemy_superpower_bonus
      - vp_delta = USSR_total - US_total

    For Southeast Asia, delegates to score_southeast_asia().
    """
    if region == Region.SOUTHEAST_ASIA:
        return score_southeast_asia(pub)

    countries = _countries()
    adj = _adj_map()
    vp_table = _REGION_VP.get(region)
    if vp_table is None:
        return ScoringResult(vp_delta=0)

    presence_vp, domination_vp, control_vp = vp_table

    # Gather countries in this scoring region (superpowers excluded from country
    # lists). Asia Scoring includes the Southeast Asia subset; the dedicated
    # Southeast Asia card uses score_southeast_asia() above instead.
    region_ids = [
        cid for cid, spec in countries.items()
        if (
            spec.region == region
            or (region == Region.ASIA and spec.region == Region.SOUTHEAST_ASIA)
        )
        and cid not in _EXCLUDED_IDS
    ]
    battleground_ids = [
        cid for cid in region_ids
        if _is_scoring_battleground(cid, pub, countries)
    ]
    total_bgs = len(battleground_ids)

    # Shuttle Diplomacy (74): when active, exclude the highest-stability BG from
    # Asia or Middle East scoring for BOTH sides (competitive / ITS ruling).
    # The excluded BG is removed from BOTH battleground_ids AND region_ids so it
    # does not contribute to tier totals as a non-BG country either.
    # The flag is cleared by apply_scoring_card after one Asia or ME scoring card.
    shuttle_used = False
    if pub.shuttle_diplomacy_active and region in (Region.ASIA, Region.MIDDLE_EAST):
        if battleground_ids:
            top_bg = max(battleground_ids, key=lambda cid: countries[cid].stability)
            battleground_ids = [cid for cid in battleground_ids if cid != top_bg]
            region_ids = [cid for cid in region_ids if cid != top_bg]
            total_bgs -= 1
            shuttle_used = True

    # Pre-compute control counts for both sides (used in tier and scoring).
    def _counts(side: Side) -> tuple[int, int, int]:
        """Return (bgs_controlled, non_bgs_controlled, total_controlled)."""
        bgs = sum(1 for cid in battleground_ids if _controls(side, cid, pub))
        non_bgs = sum(
            1 for cid in region_ids
            if cid not in battleground_ids and _controls(side, cid, pub)
        )
        return bgs, non_bgs, bgs + non_bgs

    ussr_bgs, ussr_non_bgs, ussr_total = _counts(Side.USSR)
    us_bgs, us_non_bgs, us_total = _counts(Side.US)

    def _tier(bgs: int, non_bgs: int, total: int, opp_bgs: int, opp_total: int) -> Tier:
        """Determine scoring tier per §10.1.1."""
        # Control: all BGs + more total countries than opponent.
        if total_bgs > 0 and bgs == total_bgs and total > opp_total:
            return Tier.CONTROL
        # Domination: more total, more BGs, ≥1 non-BG, ≥1 BG.
        if total > opp_total and bgs > opp_bgs and non_bgs >= 1 and bgs >= 1:
            return Tier.DOMINATION
        # Presence: any country controlled.
        if total >= 1:
            return Tier.PRESENCE
        return Tier.NONE

    ussr_tier = _tier(ussr_bgs, ussr_non_bgs, ussr_total, us_bgs, us_total)
    us_tier   = _tier(us_bgs,   us_non_bgs,   us_total,   ussr_bgs, ussr_total)

    # Europe Control = immediate game win for whichever side achieves it.
    if control_vp == GAME_WIN_EUROPE:
        if ussr_tier == Tier.CONTROL:
            return ScoringResult(vp_delta=0, game_over=True, winner=Side.USSR)
        if us_tier == Tier.CONTROL:
            return ScoringResult(vp_delta=0, game_over=True, winner=Side.US)

    def _side_score(side: Side, tier: Tier, bgs_ctrl: int) -> int:
        """Compute one side's total VP contribution (§10.1.2)."""
        if tier == Tier.NONE:
            return 0
        base = (0, presence_vp, domination_vp, control_vp)[tier]

        # +1 per BG country controlled in this region.
        bg_bonus = bgs_ctrl

        # +1 per country (BG or non-BG) controlled that is adjacent to the ENEMY
        # superpower (§10.1.2).
        # Note: the log tsreplayer_14 T5 AR3 was previously thought to show BG-only
        # behavior (Mexico adj USA, no adj bonus), but the actual reason the engine
        # computed Presence(1)+BG(2)+adj(1)=4 (not Domination+BG+adj) was that
        # USSR controlled only BG countries (non_bgs=0), failing the domination
        # threshold.  The adj bonus for Mexico (BG, adj USA) was correctly applied.
        enemy_sp = _USSR_ID if side == Side.US else _USA_ID
        enemy_neighbors = adj.get(enemy_sp, frozenset())
        adj_bonus = sum(
            1 for cid in region_ids
            if cid in enemy_neighbors and _controls(side, cid, pub)
        )

        return base + bg_bonus + adj_bonus

    ussr_vp = _side_score(Side.USSR, ussr_tier, ussr_bgs)
    us_vp   = _side_score(Side.US,   us_tier,   us_bgs)

    return ScoringResult(vp_delta=ussr_vp - us_vp, clear_shuttle=shuttle_used)


def score_southeast_asia(pub: PublicState) -> ScoringResult:
    """Compute VP change for Southeast Asia Scoring.

    Card text (card #41): each controlled country scores 1 VP for its controller;
    Thailand scores 2 VP.  No additional BG or adjacency bonuses apply —
    §10.1.2 bonuses are defined only for the six standard regional scoring cards.

    Implementation:
      - VP per country from _SE_ASIA_COUNTRY_VP (Thailand=2, others=1).
      - Both sides score simultaneously; vp_delta = USSR_total - US_total.

    Empirically verified: tsreplayer_16 T7 AR3 — US controls all 6 SE Asia
    countries (Thailand=2, others 5×1 = 5), net = 7 VP for US.  Adding BG bonuses
    would give 11 VP, which contradicts the log.
    """
    vp_delta = 0

    for country_id, base_vp in _SE_ASIA_COUNTRY_VP.items():
        for side, sign in ((Side.USSR, +1), (Side.US, -1)):
            if _controls(side, country_id, pub):
                vp_delta += sign * base_vp

    return ScoringResult(vp_delta=vp_delta)


def score_asia_final(pub: PublicState) -> ScoringResult:
    """Asia scoring for end-of-Turn-10 final scoring (§10.3.2).

    SE Asia countries are included in the Asia country pool (not scored
    separately at end-game).  The standard Tier+BG+adjacency formula applies;
    the per-country SE Asia card VP (Thailand=2 etc.) does NOT apply here.

    China Card bonus (+1 to holder) is applied as in the mid-game Asia card.
    """
    countries = _countries()
    adj = _adj_map()

    # Combined country pool: all Asia AND SoutheastAsia countries.
    region_ids = [
        cid for cid, spec in countries.items()
        if spec.region in (Region.ASIA, Region.SOUTHEAST_ASIA)
        and cid not in _EXCLUDED_IDS
    ]
    battleground_ids = [
        cid for cid in region_ids
        if _is_scoring_battleground(cid, pub, countries)
    ]
    total_bgs = len(battleground_ids)

    # Shuttle Diplomacy (74): exclude highest-stability Asia BG if still active.
    shuttle_used = False
    if pub.shuttle_diplomacy_active:
        if battleground_ids:
            top_bg = max(battleground_ids, key=lambda cid: countries[cid].stability)
            battleground_ids = [cid for cid in battleground_ids if cid != top_bg]
            total_bgs -= 1
            shuttle_used = True

    def _counts(side: Side) -> tuple[int, int, int]:
        bgs = sum(1 for cid in battleground_ids if _controls(side, cid, pub))
        non_bgs = sum(
            1 for cid in region_ids
            if cid not in battleground_ids and _controls(side, cid, pub)
        )
        return bgs, non_bgs, bgs + non_bgs

    ussr_bgs, ussr_non_bgs, ussr_total = _counts(Side.USSR)
    us_bgs, us_non_bgs, us_total = _counts(Side.US)

    def _tier(bgs: int, non_bgs: int, total: int, opp_bgs: int, opp_total: int) -> Tier:
        if total_bgs > 0 and bgs == total_bgs and total > opp_total:
            return Tier.CONTROL
        if total > opp_total and bgs > opp_bgs and non_bgs >= 1 and bgs >= 1:
            return Tier.DOMINATION
        if total >= 1:
            return Tier.PRESENCE
        return Tier.NONE

    ussr_tier = _tier(ussr_bgs, ussr_non_bgs, ussr_total, us_bgs, us_total)
    us_tier   = _tier(us_bgs,   us_non_bgs,   us_total,   ussr_bgs, ussr_total)

    presence_vp, domination_vp, control_vp = _REGION_VP[Region.ASIA]

    def _side_score(side: Side, tier: Tier, bgs_ctrl: int) -> int:
        if tier == Tier.NONE:
            return 0
        base = (0, presence_vp, domination_vp, control_vp)[tier]
        bg_bonus = bgs_ctrl
        enemy_sp = _USSR_ID if side == Side.US else _USA_ID
        enemy_neighbors = adj.get(enemy_sp, frozenset())
        adj_bonus = sum(
            1 for cid in region_ids
            if cid in enemy_neighbors and _controls(side, cid, pub)
        )
        return base + bg_bonus + adj_bonus

    ussr_vp = _side_score(Side.USSR, ussr_tier, ussr_bgs)
    us_vp   = _side_score(Side.US,   us_tier,   us_bgs)
    vp_delta = ussr_vp - us_vp + score_asia_china_bonus(pub)
    return ScoringResult(vp_delta=vp_delta, clear_shuttle=shuttle_used)


def score_asia_china_bonus(pub: PublicState) -> int:
    """Return ±1 VP bonus for the China Card holder at Asia Scoring.

    +1 = USSR holds China Card (USSR gains 1 VP).
    -1 = US holds China Card (US gains 1 VP).
    """
    if pub.china_held_by == Side.USSR:
        return +1
    return -1


# ---------------------------------------------------------------------------
# Scoring card dispatch
# ---------------------------------------------------------------------------

# Maps scoring card_id → (region, include_china_bonus)
_SCORING_CARD_REGION: dict[int, tuple[Region, bool]] = {
    1:  (Region.ASIA,            False),   # Asia Scoring (Early War)
    2:  (Region.EUROPE,          False),   # Europe Scoring
    3:  (Region.MIDDLE_EAST,     False),   # Middle East Scoring
    40: (Region.CENTRAL_AMERICA, False),   # Central America Scoring
    41: (Region.SOUTHEAST_ASIA,  False),   # Southeast Asia Scoring
    80: (Region.AFRICA,          False),   # Africa Scoring
    82: (Region.SOUTH_AMERICA,   False),   # South America Scoring
}

# Asia Scoring (id=1) and Southeast Asia (id=41) both award China Card bonus.
_CHINA_BONUS_CARDS: frozenset[int] = frozenset({1})


def apply_final_scoring(pub: PublicState) -> ScoringResult:
    """Apply all-region final scoring at end of Turn 10 (§10.3.2).

    Scores Europe, Asia (including SE Asia), Middle East, Central America,
    South America, and Africa in that order.  Stops and returns game_over=True
    if Europe Control is achieved (§10.3.2: "Control of Europe does grant
    automatic victory").

    China Card bonus is included in the Asia total.

    Returns a ScoringResult with the cumulative vp_delta across all regions.
    """
    regions = [
        Region.EUROPE,
        Region.ASIA,   # uses score_asia_final (includes SE Asia)
        Region.MIDDLE_EAST,
        Region.CENTRAL_AMERICA,
        Region.SOUTH_AMERICA,
        Region.AFRICA,
    ]

    total_vp = 0
    for region in regions:
        if region == Region.ASIA:
            result = score_asia_final(pub)
        else:
            result = score_region(region, pub)

        total_vp += result.vp_delta
        if result.clear_shuttle:
            pub.shuttle_diplomacy_active = False

        if result.game_over:
            # Europe control: immediate win regardless of other scores.
            return ScoringResult(
                vp_delta=total_vp,
                game_over=True,
                winner=result.winner,
            )

    return ScoringResult(vp_delta=total_vp)


def apply_scoring_card(card_id: int, pub: PublicState) -> ScoringResult:
    """Apply the scoring event for a scoring card, returning the VP result.

    result.clear_shuttle is True when Shuttle Diplomacy (74) was consumed.
    The caller must set pub.shuttle_diplomacy_active = False in that case.
    """
    if card_id not in _SCORING_CARD_REGION:
        raise ValueError(f"Card {card_id} is not a scoring card")

    region, _ = _SCORING_CARD_REGION[card_id]
    result = score_region(region, pub)

    if card_id in _CHINA_BONUS_CARDS and not result.game_over:
        result = ScoringResult(
            vp_delta=result.vp_delta + score_asia_china_bonus(pub),
            game_over=result.game_over,
            winner=result.winner,
            clear_shuttle=result.clear_shuttle,
        )
    return result
