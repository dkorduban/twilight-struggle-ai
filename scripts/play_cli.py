#!/usr/bin/env python3
"""Interactive one-side Twilight Struggle play assistant."""

from __future__ import annotations

import argparse
import difflib
import json
import math
import secrets
import shlex
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

from tsrl.engine.game_loop import _MAX_TURNS, _run_game_gen
from tsrl.engine.game_state import GamePhase, reset
from tsrl.engine.legal_actions import (
    effective_ops,
    enumerate_actions,
    legal_cards,
    legal_countries,
    legal_modes,
)
from tsrl.engine.rng import make_rng
from tsrl.etl.dataset import _card_mask, _influence_array
from tsrl.etl.game_data import CardSpec, CountrySpec, load_cards, load_countries
from tsrl.schemas import ActionEncoding, ActionMode, PublicState, Region, Side

CARDS: dict[int, CardSpec] = load_cards()
COUNTRIES: dict[int, CountrySpec] = load_countries()
EXCLUDED_BOARD_IDS = {64, 81, 82}

MODE_ALIASES = {
    "event": ActionMode.EVENT,
    "e": ActionMode.EVENT,
    "influence": ActionMode.INFLUENCE,
    "i": ActionMode.INFLUENCE,
    "inf": ActionMode.INFLUENCE,
    "coup": ActionMode.COUP,
    "c": ActionMode.COUP,
    "realign": ActionMode.REALIGN,
    "r": ActionMode.REALIGN,
    "space": ActionMode.SPACE,
    "s": ActionMode.SPACE,
}

COMMAND_HELP = {
    "/help": "show this help",
    "/board": "show region control summary",
    "/status": "alias for /board",
    "/hand": "show your current hand",
    "/hand set Card1 Card2..": "set your full hand (external mode)",
    "/hand add Card1 Card2..": "add cards to hand (external mode)",
    "/hand remove Card1 Card2..": "remove cards from hand (external mode)",
    "/draw Card1 Card2..": "alias for /hand add (external mode)",
    "/place ussr|us Country [=N]": "set influence to N (external mode)",
    "/add ussr|us Country [N]": "add N influence (default: 1) (external mode)",
    "/legal": "show your legal actions",
    "/suggest": "re-show model suggestions",
    "/s": "alias for /suggest",
    "/undo": "undo the last applied action",
    "/save [file]": "save the game to JSON",
    "/load [file]": "load a saved game",
    "/quit": "exit",
    "/q": "alias for /quit",
}

REGION_ORDER = [
    Region.EUROPE,
    Region.ASIA,
    Region.MIDDLE_EAST,
    Region.AFRICA,
    Region.CENTRAL_AMERICA,
    Region.SOUTH_AMERICA,
    Region.SOUTHEAST_ASIA,
]

REGION_LABELS = {
    Region.EUROPE: "Europe",
    Region.ASIA: "Asia",
    Region.MIDDLE_EAST: "Middle East",
    Region.AFRICA: "Africa",
    Region.CENTRAL_AMERICA: "Central America",
    Region.SOUTH_AMERICA: "South America",
    Region.SOUTHEAST_ASIA: "SE Asia",
}


def normalize_name(text: str) -> str:
    return "".join(ch for ch in text.lower() if ch.isalnum())


def side_name(side: Side) -> str:
    return "USSR" if side == Side.USSR else "US"


def mode_name(mode: ActionMode) -> str:
    return mode.name.lower()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def vp_text(vp: int) -> str:
    if vp > 0:
        return f"+{vp} USSR"
    if vp < 0:
        return f"+{-vp} US"
    return "0"


def parse_side(value: str) -> Side:
    lowered = value.strip().lower()
    if lowered == "ussr":
        return Side.USSR
    if lowered == "us":
        return Side.US
    raise argparse.ArgumentTypeError("side must be 'ussr' or 'us'")


def action_to_dict(action: ActionEncoding) -> dict[str, Any]:
    return {
        "card_id": int(action.card_id),
        "mode": mode_name(action.mode),
        "targets": [int(target) for target in action.targets],
    }


def action_from_dict(payload: dict[str, Any]) -> ActionEncoding:
    mode_value = payload["mode"]
    if isinstance(mode_value, str):
        mode = MODE_ALIASES[mode_value.lower()]
    else:
        mode = ActionMode(int(mode_value))
    return ActionEncoding(
        card_id=int(payload["card_id"]),
        mode=mode,
        targets=tuple(int(target) for target in payload.get("targets", [])),
    )


def _entity_variants(name: str) -> set[str]:
    parts = [normalize_name(part) for part in name.replace("/", " ").replace("-", " ").split()]
    parts = [part for part in parts if part]
    variants = {normalize_name(name)}
    variants.update(parts)
    for idx in range(len(parts) - 1):
        variants.add(parts[idx] + parts[idx + 1])
    if name.lower().startswith("west "):
        variants.add("w" + normalize_name(name[5:]))
    if name.lower().startswith("east "):
        variants.add("e" + normalize_name(name[5:]))
    if name.lower().startswith("south "):
        variants.add("s" + normalize_name(name[6:]))
    if name.lower().startswith("north "):
        variants.add("n" + normalize_name(name[6:]))
    return {variant for variant in variants if variant}


CARD_VARIANTS = {card_id: _entity_variants(spec.name) for card_id, spec in CARDS.items()}
COUNTRY_VARIANTS = {
    country_id: _entity_variants(spec.name) for country_id, spec in COUNTRIES.items()
}


class ActionParseError(ValueError):
    pass


class JsonlLogger:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, event_type: str, **payload: Any) -> None:
        row = {"ts": utc_now(), "type": event_type, **payload}
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(row, sort_keys=True) + "\n")


@dataclass
class RequestView:
    side: Side
    pub: PublicState
    hand: frozenset[int]
    holds_china: bool


class PlaySession:
    def __init__(self, seed: int, human_side: Side, checkpoint: str, *, external: bool = False) -> None:
        self.master_seed = int(seed)
        self.human_side = human_side
        self.checkpoint = checkpoint
        self.external = external
        # In external mode, user-specified hand (not engine-dealt).
        self._external_hand: set[int] = set()
        self.history: list[dict[str, Any]] = []
        self.result = None
        self.req = None
        self.gs = None
        self._rebuild([])

    @property
    def opponent_side(self) -> Side:
        return Side.US if self.human_side == Side.USSR else Side.USSR

    def _derive_seeds(self) -> tuple[int, int]:
        sequence = np.random.SeedSequence(self.master_seed)
        deck_seed, rng_seed = sequence.generate_state(2, dtype=np.uint32)
        return int(deck_seed), int(rng_seed)

    def _apply_history_entry(self, entry: dict[str, Any], game_gen) -> None:
        """Apply one history entry: either a hand override or an action."""
        if entry.get("type") == "hand_set":
            cards = frozenset(int(c) for c in entry["cards"])
            self._external_hand = set(cards)
            # Patch engine hand to match user-specified hand
            self.gs.hands[self.human_side] = cards - {6}  # China tracked separately
            return
        # Action entry — inject card into hand if needed (external mode)
        action = action_from_dict(entry["parsed"])
        if self.external and action.card_id != 6:
            side = Side.USSR if entry.get("side", "") == "ussr" else Side.US
            if action.card_id not in self.gs.hands[side]:
                self.gs.hands[side] = self.gs.hands[side] | {action.card_id}

    def _rebuild(self, history: list[dict[str, Any]]) -> None:
        deck_seed, rng_seed = self._derive_seeds()
        gs = reset(seed=deck_seed)
        rng = make_rng(rng_seed)
        game_gen = _run_game_gen(gs, rng, _MAX_TURNS)
        self.gs = gs
        self._external_hand = set()
        result = None
        try:
            req = next(game_gen)
        except StopIteration as exc:
            req = None
            result = exc.value
        for entry in history:
            if req is None:
                raise RuntimeError("history continues after game over")
            if entry.get("type") == "hand_set":
                self._apply_history_entry(entry, game_gen)
                continue
            self._apply_history_entry(entry, game_gen)
            try:
                req = game_gen.send(action_from_dict(entry["parsed"]))
            except StopIteration as exc:
                req = None
                result = exc.value
        self.req = req
        self.result = result
        self._gen = game_gen
        self.history = list(history)

    def rebuild_from_save(self, payload: dict[str, Any]) -> None:
        self.master_seed = int(payload["seed"])
        self.human_side = parse_side(payload["human_side"])
        self.checkpoint = str(payload["checkpoint"])
        self.external = bool(payload.get("external", False))
        self._rebuild(list(payload.get("history", [])))

    def save_payload(self) -> dict[str, Any]:
        return {
            "version": 2,
            "seed": self.master_seed,
            "human_side": self.human_side.name.lower(),
            "checkpoint": self.checkpoint,
            "external": self.external,
            "history": self.history,
        }

    def set_hand(self, card_ids: list[int]) -> None:
        """Set the human player's hand (external mode). Records in history for undo."""
        self._external_hand = set(card_ids)
        engine_cards = frozenset(c for c in card_ids if c != 6)
        self.gs.hands[self.human_side] = engine_cards
        self.history.append({"type": "hand_set", "cards": card_ids})

    def apply(self, raw_text: str, action: ActionEncoding) -> None:
        if self.req is None:
            raise RuntimeError("game is already over")
        side = self.req.side
        # In external mode, inject card into hand if engine doesn't have it
        if self.external and action.card_id != 6:
            if action.card_id not in self.gs.hands[side]:
                self.gs.hands[side] = self.gs.hands[side] | {action.card_id}
        self.history.append(
            {
                "side": side_name(side).lower(),
                "raw": raw_text,
                "parsed": action_to_dict(action),
            }
        )
        try:
            self.req = self._gen.send(action)
        except StopIteration as exc:
            self.req = None
            self.result = exc.value
        # In external mode, after opponent plays, remove card from their hand tracking
        if self.external and side == self.human_side:
            self._external_hand.discard(action.card_id)

    def undo(self) -> bool:
        if not self.history:
            return False
        self._rebuild(self.history[:-1])
        return True

    def full_hand(self, side: Side, *, legal_only: bool = False) -> frozenset[int]:
        if self.external and side == self.human_side:
            return frozenset(self._external_hand)
        hand = set(self.gs.hands[side])
        if self.gs.pub.china_held_by == side and (self.gs.pub.china_playable or not legal_only):
            hand.add(6)
        return frozenset(hand)

    def current(self) -> RequestView | None:
        if self.req is None:
            return None
        if self.external and self.req.side == self.human_side:
            hand = frozenset(self._external_hand)
        else:
            hand = set(self.req.hand)
            if self.gs.phase != GamePhase.HEADLINE and self.req.holds_china:
                hand.add(6)
            hand = frozenset(hand)
        return RequestView(
            side=self.req.side,
            pub=self.req.pub,
            hand=hand,
            holds_china=self.req.holds_china,
        )


class ModelAdapter:
    def __init__(self, checkpoint_path: str) -> None:
        import torch

        self.torch = torch
        self.path = str(Path(checkpoint_path))
        self.kind = "torchscript"
        self.scalar_dim: int | None = None
        try:
            self.model = torch.jit.load(self.path, map_location="cpu")
            self.model.eval()
        except Exception:
            self.kind = "raw"
            self.model = self._load_raw_checkpoint(self.path)
            self.scalar_dim = 32

    def _load_raw_checkpoint(self, checkpoint_path: str):
        import torch
        from tsrl.policies.model import (
            TSBaselineModel,
            TSCardEmbedModel,
            TSControlFeatGNNModel,
            TSControlFeatGNNSideModel,
            TSControlFeatModel,
            TSCountryAttnModel,
            TSCountryAttnSideModel,
            TSCountryEmbedModel,
            TSDirectCountryModel,
            TSFullEmbedModel,
            TSMarginalValueModel,
        )

        registry = {
            "baseline": TSBaselineModel,
            "card_embed": TSCardEmbedModel,
            "country_embed": TSCountryEmbedModel,
            "full_embed": TSFullEmbedModel,
            "country_attn": TSCountryAttnModel,
            "country_attn_side": TSCountryAttnSideModel,
            "direct_country": TSDirectCountryModel,
            "marginal_value": TSMarginalValueModel,
            "control_feat": TSControlFeatModel,
            "control_feat_gnn": TSControlFeatGNNModel,
            "control_feat_gnn_side": TSControlFeatGNNSideModel,
        }

        checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
        state_dict = checkpoint.get("model_state_dict", checkpoint)
        args = checkpoint.get("args", {})
        hidden_dim = args.get("hidden_dim", 256)
        dropout = args.get("dropout", 0.1)
        num_strategies = args.get("num_strategies", 4)
        model_type = args.get("model_type", "baseline")
        model_cls = registry.get(model_type, TSBaselineModel)
        if model_cls in (TSControlFeatGNNModel,) and num_strategies != 4:
            model = model_cls(hidden_dim=hidden_dim, dropout=dropout, num_strategies=num_strategies)
        else:
            model = model_cls(hidden_dim=hidden_dim, dropout=dropout)

        filtered: dict[str, Any] = {}
        model_state = model.state_dict()
        for key, value in state_dict.items():
            if key not in model_state:
                continue
            if value.shape == model_state[key].shape:
                filtered[key] = value
                continue
            if value.dim() == 2 and model_state[key].dim() == 2 and value.shape[0] == model_state[key].shape[0]:
                new_weight = model_state[key].clone()
                new_weight[:, : value.shape[1]] = value
                filtered[key] = new_weight
        model.load_state_dict(filtered, strict=False)
        model.eval()
        return model

    def _build_scalars(self, pub: PublicState, holds_china: bool, side: Side, scalar_dim: int) -> list[float]:
        values = [
            pub.vp / 20.0,
            (pub.defcon - 1) / 4.0,
            pub.milops[Side.USSR] / 6.0,
            pub.milops[Side.US] / 6.0,
            pub.space[Side.USSR] / 9.0,
            pub.space[Side.US] / 9.0,
            float(int(pub.china_held_by)),
            float(holds_china),
            pub.turn / 10.0,
            pub.ar / 8.0,
            float(int(side)),
            float(pub.bear_trap_active),
            float(pub.quagmire_active),
            float(pub.cuban_missile_crisis_active),
            float(pub.iran_hostage_crisis_active),
            float(pub.norad_active),
            float(pub.shuttle_diplomacy_active),
            float(pub.salt_active),
            float(pub.flower_power_active),
            float(pub.flower_power_cancelled),
            float(pub.vietnam_revolts_active),
            float(pub.north_sea_oil_extra_ar),
            float(pub.glasnost_extra_ar),
            float(pub.nato_active),
            float(pub.de_gaulle_active),
            float(pub.nuclear_subs_active),
            float(pub.formosan_active),
            float(pub.awacs_active),
            float(pub.chernobyl_blocked_region is not None),
            (
                float(int(pub.chernobyl_blocked_region)) / 6.0
                if pub.chernobyl_blocked_region is not None
                else 0.0
            ),
            pub.ops_modifier[Side.USSR] / 3.0,
            pub.ops_modifier[Side.US] / 3.0,
        ]
        return values[:scalar_dim]

    def _build_inputs(self, pub: PublicState, hand: frozenset[int], holds_china: bool, side: Side, scalar_dim: int):
        torch = self.torch
        influence = torch.tensor(
            _influence_array(pub, Side.USSR) + _influence_array(pub, Side.US),
            dtype=torch.float32,
        ).unsqueeze(0)
        hand_mask = _card_mask(hand)
        cards = torch.tensor(
            hand_mask + hand_mask + _card_mask(pub.discard) + _card_mask(pub.removed),
            dtype=torch.float32,
        ).unsqueeze(0)
        scalars = torch.tensor(
            self._build_scalars(pub, holds_china, side, scalar_dim),
            dtype=torch.float32,
        ).unsqueeze(0)
        return influence, cards, scalars

    def forward(self, pub: PublicState, hand: frozenset[int], holds_china: bool, side: Side) -> dict[str, Any]:
        torch = self.torch
        tried: list[int] = []
        for scalar_dim in ([self.scalar_dim] if self.scalar_dim is not None else [11, 32]):
            if scalar_dim is None:
                continue
            tried.append(scalar_dim)
            influence, cards, scalars = self._build_inputs(pub, hand, holds_china, side, scalar_dim)
            try:
                with torch.inference_mode():
                    outputs = self.model(influence, cards, scalars)
                if self.scalar_dim is None:
                    self.scalar_dim = scalar_dim
                return outputs
            except RuntimeError:
                continue
        raise RuntimeError(f"model forward failed for scalar dims {tried}")


def _controls(side: Side, country_id: int, pub: PublicState) -> bool:
    opponent = Side.US if side == Side.USSR else Side.USSR
    own = pub.influence.get((side, country_id), 0)
    opp = pub.influence.get((opponent, country_id), 0)
    return own >= opp + COUNTRIES[country_id].stability


def _region_tier(region: Region, pub: PublicState, side: Side) -> str:
    if region == Region.SOUTHEAST_ASIA:
        return "Special"
    countries = [cid for cid, spec in COUNTRIES.items() if spec.region == region and cid not in EXCLUDED_BOARD_IDS]
    battlegrounds = [
        cid
        for cid in countries
        if COUNTRIES[cid].is_battleground or (cid == 85 and pub.formosan_active)
    ]
    opponent = Side.US if side == Side.USSR else Side.USSR
    own_bg = sum(1 for cid in battlegrounds if _controls(side, cid, pub))
    opp_bg = sum(1 for cid in battlegrounds if _controls(opponent, cid, pub))
    own_total = sum(1 for cid in countries if _controls(side, cid, pub))
    opp_total = sum(1 for cid in countries if _controls(opponent, cid, pub))
    own_non_bg = own_total - own_bg
    if battlegrounds and own_bg == len(battlegrounds) and own_total > opp_total:
        return "Control"
    if own_total > opp_total and own_bg > opp_bg and own_bg >= 1 and own_non_bg >= 1:
        return "Domination"
    if own_total >= 1:
        return "Presence"
    return "-"


def region_summary_lines(pub: PublicState) -> list[str]:
    lines: list[str] = []
    for region in REGION_ORDER:
        countries = [
            cid for cid, spec in COUNTRIES.items() if spec.region == region and cid not in EXCLUDED_BOARD_IDS
        ]
        total = len(countries)
        ussr_total = sum(1 for cid in countries if _controls(Side.USSR, cid, pub))
        us_total = sum(1 for cid in countries if _controls(Side.US, cid, pub))
        lines.append(
            f"{REGION_LABELS[region]:<15} USSR {ussr_total}/{total}  US {us_total}/{total}  "
            f"({_region_tier(region, pub, Side.USSR)}/{_region_tier(region, pub, Side.US)})"
        )
    return lines


def format_card(card_id: int, viewer_side: Side) -> str:
    spec = CARDS[card_id]
    suffix = ""
    if spec.side not in (viewer_side, Side.NEUTRAL):
        suffix = "*"
    return f"{spec.name}({spec.ops}{suffix})"


def format_hand(session: PlaySession) -> str:
    hand = sorted(session.full_hand(session.human_side, legal_only=False))
    return "[" + ", ".join(format_card(card_id, session.human_side) for card_id in hand) + "]"


def format_targets(targets: tuple[int, ...]) -> str:
    if not targets:
        return ""
    counts = Counter(targets)
    ordered: list[int] = []
    for target in targets:
        if target not in ordered:
            ordered.append(target)
    chunks = []
    for target in ordered:
        name = COUNTRIES[target].name
        count = counts[target]
        chunks.append(f"{name} x{count}" if count > 1 else name)
    return " " + ", ".join(chunks)


def format_action(action: ActionEncoding) -> str:
    return f"{CARDS[action.card_id].name} {action.mode.name.title()}{format_targets(action.targets)}"


def state_header(session: PlaySession, req: RequestView) -> list[str]:
    pub = req.pub
    if session.gs.phase == GamePhase.HEADLINE or pub.ar == 0:
        title = f"Turn {pub.turn}, Headline Phase ({side_name(req.side)})"
    else:
        title = f"Turn {pub.turn}, AR {pub.ar} ({side_name(req.side)})"
    status = (
        f"DEFCON: {pub.defcon} | VP: {vp_text(pub.vp)} | "
        f"MilOps: USSR={pub.milops[0]} US={pub.milops[1]} | "
        f"Space: USSR={pub.space[0]} US={pub.space[1]}"
    )
    lines = [title, status]
    if req.side == session.human_side:
        lines.append(f"Hand: {format_hand(session)}")
    return lines


def _match_entity(query: str, variants: dict[int, set[str]], names: dict[int, str], allowed: set[int]) -> int:
    stripped = query.strip()
    if not stripped:
        raise ActionParseError("missing name")
    if stripped.startswith("#"):
        stripped = stripped[1:]
    if stripped.isdigit():
        entity_id = int(stripped)
        if entity_id in allowed:
            return entity_id
        raise ActionParseError(f"unknown id: {entity_id}")

    needle = normalize_name(stripped)
    if not needle:
        raise ActionParseError(f"could not understand '{query}'")

    exact = [entity_id for entity_id in sorted(allowed) if needle in variants[entity_id]]
    if len(exact) == 1:
        return exact[0]
    if len(exact) > 1:
        raise ActionParseError("ambiguous match: " + ", ".join(names[item] for item in exact[:5]))

    partial = [
        entity_id
        for entity_id in sorted(allowed)
        if any(needle in variant or variant.startswith(needle) for variant in variants[entity_id])
    ]
    if len(partial) == 1:
        return partial[0]
    if len(partial) > 1:
        raise ActionParseError("ambiguous match: " + ", ".join(names[item] for item in partial[:5]))

    suggestions = difflib.get_close_matches(
        needle,
        [normalize_name(names[item]) for item in sorted(allowed)],
        n=3,
        cutoff=0.55,
    )
    if suggestions:
        hint = ", ".join(
            names[item]
            for item in sorted(allowed)
            if normalize_name(names[item]) in suggestions
        )
        raise ActionParseError(f"unknown name '{query}'. Close matches: {hint}")
    raise ActionParseError(f"unknown name '{query}'")


def resolve_card(query: str, allowed_cards: set[int]) -> int:
    names = {card_id: spec.name for card_id, spec in CARDS.items()}
    return _match_entity(query, CARD_VARIANTS, names, allowed_cards)


def resolve_country_tokens(tokens: list[str], allowed_countries: set[int] | None = None) -> list[int]:
    names = {country_id: spec.name for country_id, spec in COUNTRIES.items()}
    allowed = allowed_countries or set(COUNTRIES)
    resolved: list[int] = []
    index = 0
    while index < len(tokens):
        match = None
        for stop in range(len(tokens), index, -1):
            chunk = " ".join(tokens[index:stop])
            try:
                country_id = _match_entity(chunk, COUNTRY_VARIANTS, names, allowed)
            except ActionParseError:
                continue
            match = (country_id, stop)
            break
        if match is None:
            raise ActionParseError(f"could not understand country near '{' '.join(tokens[index:])}'")
        resolved.append(match[0])
        index = match[1]
    return resolved


def parse_action_text(session: PlaySession, text: str) -> ActionEncoding:
    req = session.current()
    if req is None:
        raise ActionParseError("game is over")

    tokens = text.strip().split()
    if not tokens:
        raise ActionParseError("empty input")

    legal_hand = req.hand
    # In external mode, relax validation: opponent can play any card, human plays from external hand
    if session.external:
        if req.side != session.human_side:
            # Opponent move — accept any card
            legal_playable = set(CARDS)
            visible_catalog = set(CARDS)
        else:
            # Human move — use external hand if set
            if session._external_hand:
                legal_hand = frozenset(session._external_hand)
            legal_playable = legal_cards(legal_hand, req.pub, req.side, holds_china=req.holds_china)
            visible_catalog = set(legal_hand)
    else:
        legal_playable = legal_cards(legal_hand, req.pub, req.side, holds_china=req.holds_china)
        visible_catalog = set(legal_hand) if req.side == session.human_side else set(CARDS)

    phase_is_headline = session.gs.phase == GamePhase.HEADLINE or req.pub.ar == 0
    mode_index = next((idx for idx, token in enumerate(tokens) if token.lower() in MODE_ALIASES), None)
    if phase_is_headline and mode_index is None:
        card_text = " ".join(tokens)
        mode = ActionMode.EVENT
        target_tokens: list[str] = []
    else:
        if mode_index is None:
            card_text = " ".join(tokens)
            try:
                candidate_card = resolve_card(card_text, visible_catalog)
            except ActionParseError as exc:
                raise ActionParseError(str(exc)) from exc
            legal_for_card = sorted(legal_modes(candidate_card, req.pub, req.side), key=int)
            if len(legal_for_card) != 1:
                modes = ", ".join(mode_name(item) for item in legal_for_card)
                raise ActionParseError(f"missing mode. Legal modes for {CARDS[candidate_card].name}: {modes}")
            mode = legal_for_card[0]
            target_tokens = []
            card_text = CARDS[candidate_card].name
        else:
            card_text = " ".join(tokens[:mode_index])
            mode = MODE_ALIASES[tokens[mode_index].lower()]
            target_tokens = tokens[mode_index + 1 :]

    if not card_text:
        raise ActionParseError("missing card name")
    card_id = resolve_card(card_text, visible_catalog)
    if card_id not in legal_playable:
        if req.side == session.human_side:
            raise ActionParseError(f"{CARDS[card_id].name} is not playable from your current hand")
        raise ActionParseError(f"{CARDS[card_id].name} is not currently playable for the opponent")

    legal_mode_set = legal_modes(card_id, req.pub, req.side)
    if phase_is_headline:
        legal_mode_set = {ActionMode.EVENT}
    if mode not in legal_mode_set:
        modes = ", ".join(mode_name(item) for item in sorted(legal_mode_set, key=int))
        raise ActionParseError(f"illegal mode for {CARDS[card_id].name}. Legal modes: {modes}")

    if mode in (ActionMode.EVENT, ActionMode.SPACE):
        if target_tokens:
            raise ActionParseError(f"{mode_name(mode)} does not take country targets")
        return ActionEncoding(card_id=card_id, mode=mode, targets=())

    targets = resolve_country_tokens(target_tokens)
    allowed_countries = set(legal_countries(card_id, mode, req.pub, req.side))
    illegal_targets = [COUNTRIES[target].name for target in targets if target not in allowed_countries]
    if illegal_targets:
        raise ActionParseError(
            "illegal target(s): " + ", ".join(illegal_targets)
        )

    if mode == ActionMode.COUP:
        if len(targets) != 1:
            raise ActionParseError("coup requires exactly one target country")
        return ActionEncoding(card_id=card_id, mode=mode, targets=tuple(targets))

    base_ops = effective_ops(card_id, req.pub, req.side)
    legal_lengths = {base_ops}
    if card_id == 6:
        asia_only = {
            country_id
            for country_id in allowed_countries
            if COUNTRIES[country_id].region == Region.ASIA
        }
        if asia_only:
            legal_lengths.add(base_ops + 1)
            if len(targets) == base_ops + 1 and any(target not in asia_only for target in targets):
                raise ActionParseError("China Card 5-op bonus requires all targets to be in Asia")
    if len(targets) not in legal_lengths:
        lengths = ", ".join(str(item) for item in sorted(legal_lengths))
        raise ActionParseError(f"{mode_name(mode)} requires {lengths} target(s)")
    return ActionEncoding(card_id=card_id, mode=mode, targets=tuple(targets))


def command_path(session: PlaySession, explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    log_stem = Path(session.checkpoint).stem.replace(".pt", "")
    return Path(f"{log_stem}_play_state.json").resolve()


def show_help() -> None:
    print("Commands:")
    for command, description in COMMAND_HELP.items():
        print(f"  {command:<14} {description}")


def show_board(session: PlaySession) -> None:
    for line in region_summary_lines(session.gs.pub):
        print(line)


def show_hand(session: PlaySession) -> None:
    print(format_hand(session))


def show_legal(session: PlaySession) -> None:
    req = session.current()
    if req is None:
        print("Game is over.")
        return
    if req.side != session.human_side:
        print("Legal actions are hidden during the opponent turn.")
        return
    actions = enumerate_actions(req.hand, req.pub, req.side, holds_china=req.holds_china)
    print(f"{len(actions)} legal actions:")
    for action in actions:
        print(f"  {format_action(action)}")


def _masked_softmax(logits, allowed_indices: list[int]):
    torch = __import__("torch")
    masked = torch.full_like(logits, float("-inf"))
    masked[allowed_indices] = logits[allowed_indices]
    return torch.softmax(masked, dim=0)


def _country_probs(country_tensor, allowed: list[int]):
    torch = __import__("torch")
    probs = torch.zeros(86, dtype=torch.float32)
    if country_tensor is None:
        if allowed:
            probs[allowed] = 1.0 / len(allowed)
        return probs
    source = country_tensor.detach().cpu().to(torch.float32).flatten()
    probs[: min(86, source.shape[0])] = source[: min(86, source.shape[0])]
    total = float(probs[allowed].sum().item()) if allowed else 0.0
    if total <= 0.0:
        if allowed:
            probs[allowed] = 1.0 / len(allowed)
        return probs
    masked = torch.zeros_like(probs)
    masked[allowed] = probs[allowed] / total
    return masked


def rank_suggestions(model: ModelAdapter, session: PlaySession, top_k: int) -> tuple[list[dict[str, Any]], float]:
    req = session.current()
    if req is None:
        return [], 0.0
    outputs = model.forward(req.pub, req.hand, req.holds_china, req.side)
    card_logits = outputs["card_logits"][0].detach().cpu()
    mode_logits = outputs["mode_logits"][0].detach().cpu()
    country_logits = outputs.get("country_logits")
    if country_logits is not None:
        country_logits = country_logits[0]
    value = float(outputs["value"][0, 0].item())

    actions = enumerate_actions(req.hand, req.pub, req.side, holds_china=req.holds_china)
    playable = sorted(legal_cards(req.hand, req.pub, req.side, holds_china=req.holds_china))
    card_probs = _masked_softmax(card_logits, [card_id - 1 for card_id in playable])

    mode_cache: dict[int, Any] = {}
    country_cache: dict[tuple[int, ActionMode], Any] = {}
    scored: list[tuple[float, ActionEncoding]] = []
    for action in actions:
        if action.card_id not in mode_cache:
            legal = sorted(legal_modes(action.card_id, req.pub, req.side), key=int)
            mode_cache[action.card_id] = _masked_softmax(mode_logits, [int(mode) for mode in legal])
        log_score = math.log(float(card_probs[action.card_id - 1].item()) + 1e-30)
        log_score += math.log(float(mode_cache[action.card_id][int(action.mode)].item()) + 1e-30)
        if action.mode not in (ActionMode.EVENT, ActionMode.SPACE):
            cache_key = (action.card_id, action.mode)
            if cache_key not in country_cache:
                legal = sorted(legal_countries(action.card_id, action.mode, req.pub, req.side))
                country_cache[cache_key] = _country_probs(country_logits, legal)
            for target in action.targets:
                log_score += math.log(float(country_cache[cache_key][target].item()) + 1e-30)
        scored.append((log_score, action))

    if not scored:
        return [], value
    max_log = max(item[0] for item in scored)
    weights = [math.exp(item[0] - max_log) for item in scored]
    total = sum(weights)
    ranked: list[dict[str, Any]] = []
    for (log_score, action), weight in sorted(
        zip(scored, weights, strict=True),
        key=lambda item: item[0][0],
        reverse=True,
    )[:top_k]:
        ranked.append(
            {
                "card_id": action.card_id,
                "mode": int(action.mode),
                "targets": list(action.targets),
                "prob": weight / total,
                "text": format_action(action),
            }
        )
    return ranked, value


def save_session(path: Path, session: PlaySession) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(session.save_payload(), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_session(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def print_suggestions(model: ModelAdapter, session: PlaySession, logger: JsonlLogger, top_k: int) -> None:
    req = session.current()
    if req is None or req.side != session.human_side:
        print("Suggestions are only available on your turn.")
        return
    ranked, value = rank_suggestions(model, session, top_k)
    if not ranked:
        print("No suggestions available.")
        return
    summary = ", ".join(f"{item['text']} ({item['prob'] * 100:.1f}%)" for item in ranked)
    print(f"Model suggests: {summary}")
    logger.log("model_suggestion", top_k=ranked, value=value)


def log_state(logger: JsonlLogger, session: PlaySession) -> None:
    req = session.current()
    if req is None:
        return
    phase = "headline" if session.gs.phase == GamePhase.HEADLINE or req.pub.ar == 0 else "action_round"
    logger.log(
        "state",
        turn=req.pub.turn,
        ar=req.pub.ar,
        phase=phase,
        side=side_name(req.side).lower(),
        defcon=req.pub.defcon,
        vp=req.pub.vp,
        milops=list(req.pub.milops),
        space=list(req.pub.space),
        hand=sorted(session.full_hand(session.human_side, legal_only=False)),
    )


def prompt_label(session: PlaySession, req: RequestView) -> str:
    if req.side == session.human_side:
        return "> Enter your headline: " if session.gs.phase == GamePhase.HEADLINE or req.pub.ar == 0 else "> Enter your action: "
    return "> Enter opponent headline: " if session.gs.phase == GamePhase.HEADLINE or req.pub.ar == 0 else "> Enter opponent action: "


def handle_command(
    raw_text: str,
    session: PlaySession,
    model: ModelAdapter,
    logger: JsonlLogger,
    top_k: int,
) -> bool:
    parts = shlex.split(raw_text)
    command = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else None
    logger.log("command", raw=raw_text)
    if command == "/help":
        show_help()
        return True
    if command in {"/board", "/status"}:
        show_board(session)
        return True
    if command == "/hand":
        if arg and len(parts) > 2 and arg.lower() in ("set", "add", "remove"):
            if not session.external:
                print("Hand override only available in --external mode.")
                return True
            subcommand = arg.lower()
            card_tokens = parts[2:]
            try:
                card_ids = [resolve_card(t, set(CARDS)) for t in card_tokens]
            except ActionParseError as exc:
                print(str(exc))
                return True
            if subcommand == "set":
                session.set_hand(card_ids)
                names = [CARDS[c].name for c in card_ids]
                print(f"Hand set: {', '.join(names)}")
                logger.log("hand_set", cards=card_ids)
            elif subcommand == "add":
                existing = list(session._external_hand)
                session.set_hand(existing + card_ids)
                names = [CARDS[c].name for c in card_ids]
                print(f"Added: {', '.join(names)}")
                print(f"Hand now: {format_hand(session)}")
                logger.log("hand_add", cards=card_ids)
            elif subcommand == "remove":
                existing = set(session._external_hand)
                removed = []
                for cid in card_ids:
                    if cid in existing:
                        existing.discard(cid)
                        removed.append(cid)
                    else:
                        print(f"  {CARDS[cid].name} not in hand, skipping")
                session.set_hand(list(existing))
                if removed:
                    names = [CARDS[c].name for c in removed]
                    print(f"Removed: {', '.join(names)}")
                print(f"Hand now: {format_hand(session)}")
                logger.log("hand_remove", cards=removed)
            return True
        show_hand(session)
        return True
    if command == "/draw":
        # Alias for /hand add
        if not session.external:
            print("/draw only available in --external mode.")
            return True
        if len(parts) < 2:
            print("Usage: /draw Card1 Card2 ...")
            return True
        card_tokens = parts[1:]
        try:
            card_ids = [resolve_card(t, set(CARDS)) for t in card_tokens]
        except ActionParseError as exc:
            print(str(exc))
            return True
        existing = list(session._external_hand)
        session.set_hand(existing + card_ids)
        names = [CARDS[c].name for c in card_ids]
        print(f"Drew: {', '.join(names)}")
        print(f"Hand now: {format_hand(session)}")
        logger.log("hand_add", cards=card_ids)
        return True
    if command in ("/place", "/add"):
        if not session.external:
            print(f"{command} only available in --external mode.")
            return True
        if len(parts) < 3:
            if command == "/place":
                print("Usage: /place ussr|us Country N  (set influence to N)")
            else:
                print("Usage: /add ussr|us Country [N]  (add N influence, default 1)")
            return True
        side_str = parts[1].lower()
        if side_str not in ("ussr", "us"):
            print(f"Unknown side '{parts[1]}'. Use 'ussr' or 'us'.")
            return True
        place_side = Side.USSR if side_str == "ussr" else Side.US
        # Last token might be a number (amount)
        amount_str = parts[-1]
        if amount_str.isdigit() or (amount_str.startswith("-") and amount_str[1:].isdigit()):
            amount = int(amount_str)
            country_tokens = parts[2:-1]
        else:
            amount = 1 if command == "/add" else None
            country_tokens = parts[2:]
        if command == "/place" and amount is None:
            print("Usage: /place ussr|us Country N  (N is required)")
            return True
        if not country_tokens:
            print("Missing country name.")
            return True
        try:
            country_ids = resolve_country_tokens(country_tokens)
        except ActionParseError as exc:
            print(str(exc))
            return True
        absolute = command == "/place"
        for cid in country_ids:
            if absolute:
                session.gs.pub.influence[(place_side, cid)] = max(0, amount)
            else:
                current = session.gs.pub.influence.get((place_side, cid), 0)
                session.gs.pub.influence[(place_side, cid)] = max(0, current + amount)
            new_val = session.gs.pub.influence.get((place_side, cid), 0)
            print(f"  {side_str.upper()} in {COUNTRIES[cid].name}: {new_val}")
        logger.log(command.lstrip("/"), side=side_str, countries=[cid for cid in country_ids], amount=amount, absolute=absolute)
        return True
    if command == "/legal":
        show_legal(session)
        return True
    if command in {"/suggest", "/s"}:
        print_suggestions(model, session, logger, top_k)
        return True
    if command == "/undo":
        if not session.undo():
            print("Nothing to undo.")
            return True
        print("Undid the last action.")
        log_state(logger, session)
        return True
    if command == "/save":
        path = command_path(session, arg)
        save_session(path, session)
        print(f"Saved to {path}")
        logger.log("save", path=str(path))
        return True
    if command == "/load":
        path = command_path(session, arg)
        payload = load_session(path)
        prior_checkpoint = session.checkpoint
        session.rebuild_from_save(payload)
        if session.checkpoint != prior_checkpoint:
            model.__init__(session.checkpoint)
        print(f"Loaded {path}")
        log_state(logger, session)
        return True
    if command in {"/quit", "/q"}:
        raise SystemExit(0)
    print(f"Unknown command: {command}")
    return True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI play assistant for one-side Twilight Struggle play.")
    parser.add_argument("--checkpoint", required=True, help="TorchScript or raw model checkpoint path")
    parser.add_argument("--side", required=True, type=parse_side, help="Human side: ussr or us")
    parser.add_argument("--log-file", default=None, help="JSONL log path")
    parser.add_argument("--seed", type=int, default=None, help="Deterministic master seed")
    parser.add_argument("--top-k", type=int, default=5, help="Suggestion count to show")
    parser.add_argument("--external", action="store_true",
                        help="External game mode: you enter your own draws and opponent moves. "
                             "Use /hand set ... and /draw ... to manage your hand.")
    return parser


def default_log_path() -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return Path(f"ts_play_{stamp}.jsonl").resolve()


def make_completer(session: PlaySession):
    from prompt_toolkit.completion import Completer, Completion

    command_words = sorted(COMMAND_HELP)

    class SessionCompleter(Completer):
        def get_completions(self, document, complete_event):
            req = session.current()
            if req is None:
                return
            text = document.text_before_cursor
            stripped = text.lstrip()
            current = document.get_word_before_cursor(WORD=True)
            if stripped.startswith("/"):
                for command in command_words:
                    if command.startswith(stripped):
                        yield Completion(command, start_position=-len(current))
                return

            if req.side == session.human_side:
                card_ids = sorted(req.hand)
            else:
                card_ids = sorted(CARDS)
            card_names = [CARDS[card_id].name for card_id in card_ids]

            tokens = text.strip().split()
            if not tokens:
                for name in card_names:
                    yield Completion(name, start_position=0)
                return

            mode_index = next((idx for idx, token in enumerate(tokens) if token.lower() in MODE_ALIASES), None)
            if mode_index is not None:
                card_text = " ".join(tokens[:mode_index]) if tokens[:mode_index] else ""
                try:
                    card_id = resolve_card(card_text, set(card_ids))
                except ActionParseError:
                    return
                for country_id in sorted(legal_countries(card_id, MODE_ALIASES[tokens[mode_index].lower()], req.pub, req.side)):
                    name = COUNTRIES[country_id].name
                    if normalize_name(current) in normalize_name(name):
                        yield Completion(name, start_position=-len(current))
                return

            probe_tokens = tokens[:-1] if current else tokens
            if probe_tokens:
                probe_text = " ".join(probe_tokens)
                try:
                    card_id = resolve_card(probe_text, set(card_ids))
                except ActionParseError:
                    card_id = None
                if card_id is not None:
                    for mode in sorted(legal_modes(card_id, req.pub, req.side), key=int):
                        name = mode_name(mode)
                        if normalize_name(current) in normalize_name(name):
                            yield Completion(name, start_position=-len(current))
                    return

            for name in card_names:
                if normalize_name(current) in normalize_name(name):
                    yield Completion(name, start_position=-len(current))

    return SessionCompleter()


def run_cli(args: argparse.Namespace) -> int:
    try:
        from prompt_toolkit import PromptSession
    except ImportError as exc:
        raise RuntimeError("prompt_toolkit is required; run `uv sync` first") from exc

    seed = args.seed if args.seed is not None else secrets.randbits(32)
    log_file = Path(args.log_file).expanduser().resolve() if args.log_file else default_log_path()
    logger = JsonlLogger(log_file)
    session = PlaySession(seed=seed, human_side=args.side, checkpoint=args.checkpoint, external=args.external)
    model = ModelAdapter(args.checkpoint)

    logger.log(
        "game_start",
        side=side_name(session.human_side).lower(),
        model=session.checkpoint,
        seed=seed,
    )

    print(f"Welcome to TS Play Assistant. You are playing {side_name(session.human_side)}.")
    if session.external:
        print("EXTERNAL MODE: Enter your draws with /hand set or /draw. Enter opponent moves directly.")
    print(f"Model: {Path(session.checkpoint).name}")
    print(f"Log: {log_file}")
    print("Type /help for commands.")

    prompt_session = PromptSession()
    completer = make_completer(session)

    while True:
        req = session.current()
        if req is None:
            winner = "Draw" if session.result.winner is None else side_name(session.result.winner)
            print(
                f"Game over. Winner: {winner} | VP: {vp_text(session.result.final_vp)} | "
                f"Reason: {session.result.end_reason}"
            )
            logger.log(
                "game_end",
                winner=winner.lower(),
                final_vp=session.result.final_vp,
                end_turn=session.result.end_turn,
                end_reason=session.result.end_reason,
            )
            return 0

        for line in state_header(session, req):
            print(line)
        log_state(logger, session)
        if session.external and req.side == session.human_side and not session._external_hand:
            print(">>> Hand not set. Use /hand set Card1 Card2... before playing.")
        if req.side == session.human_side:
            print_suggestions(model, session, logger, args.top_k)

        try:
            raw = prompt_session.prompt(prompt_label(session, req), completer=completer, complete_while_typing=False)
        except (EOFError, KeyboardInterrupt):
            print()
            logger.log("command", raw="/quit")
            return 0

        if not raw.strip():
            continue
        if raw.lstrip().startswith("/"):
            try:
                handle_command(raw.strip(), session, model, logger, args.top_k)
            except SystemExit:
                return 0
            except Exception as exc:
                print(str(exc))
                logger.log("error", message=str(exc), raw_input=raw)
            continue

        try:
            action = parse_action_text(session, raw)
            parsed = action_to_dict(action)
            logger.log(
                "user_input" if req.side == session.human_side else "opponent_input",
                raw=raw,
                parsed=parsed,
            )
            session.apply(raw, action)
            print(f"Applied: {format_action(action)}")
            logger.log(
                "action_applied",
                side=side_name(req.side).lower(),
                card_id=action.card_id,
                mode=mode_name(action.mode),
                targets=list(action.targets),
                vp_after=session.gs.pub.vp,
                defcon_after=session.gs.pub.defcon,
                turn_after=session.gs.pub.turn,
                ar_after=session.gs.pub.ar,
            )
            completer = make_completer(session)
        except ActionParseError as exc:
            print(str(exc))
            logger.log("error", message=str(exc), raw_input=raw)
        except Exception as exc:
            print(f"Unexpected error: {exc}")
            logger.log("error", message=str(exc), raw_input=raw)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return run_cli(args)


if __name__ == "__main__":
    raise SystemExit(main())
