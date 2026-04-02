"""Minimal stdlib HTTP server for TorchScript policy inference.

Usage:
    uv run python scripts/play_server.py --model path/to/model.pt --port 8000
"""
from __future__ import annotations

import argparse
import json
import os
import resource
import sys
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

import torch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

from tsrl.engine.legal_actions import accessible_countries, effective_ops, legal_modes
from tsrl.engine.legal_actions import load_adjacency
from tsrl.etl.dataset import _card_mask
from tsrl.schemas import ActionMode, PublicState, Side

_BYTES_PER_GB = 1024 * 1024 * 1024
_MEMORY_LIMIT_BYTES = _BYTES_PER_GB
_NUM_COUNTRIES = 86
_CARD_MASK_LEN = 112
_CHINA_CARD_ID = 6


def _set_memory_limit(limit_bytes: int) -> None:
    try:
        for rlimit in (resource.RLIMIT_AS, resource.RLIMIT_DATA):
            soft, hard = resource.getrlimit(rlimit)
            new_limit = limit_bytes if hard < 0 else min(limit_bytes, hard)
            resource.setrlimit(rlimit, (new_limit, hard))
    except Exception:
        pass


def _parse_side(value: Any) -> Side:
    if isinstance(value, str):
        normalized = value.strip().upper()
        if normalized == "USSR":
            return Side.USSR
        if normalized == "US":
            return Side.US
    if value in (0, 1):
        return Side(int(value))
    raise ValueError("phasing must be 0/1 or USSR/US")


def _parse_int_list(name: str, value: Any, *, expected_len: int | None = None) -> list[int]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a list")
    try:
        parsed = [int(item) for item in value]
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must contain integers") from exc
    if expected_len is not None and len(parsed) != expected_len:
        raise ValueError(f"{name} must have length {expected_len}")
    return parsed


def _build_public_state(payload: dict[str, Any]) -> tuple[PublicState, frozenset[int], bool, int]:
    required = {
        "turn",
        "ar",
        "phasing",
        "vp",
        "defcon",
        "ussr_influence",
        "us_influence",
        "hand",
        "opp_hand_size",
    }
    missing = sorted(required - payload.keys())
    if missing:
        raise ValueError(f"missing fields: {', '.join(missing)}")

    side = _parse_side(payload["phasing"])
    hand = frozenset(_parse_int_list("hand", payload["hand"]))
    holds_china = _CHINA_CARD_ID in hand
    opp = Side.US if side == Side.USSR else Side.USSR

    pub = PublicState(
        turn=int(payload["turn"]),
        ar=int(payload["ar"]),
        phasing=side,
        vp=int(payload["vp"]),
        defcon=int(payload["defcon"]),
        china_held_by=side if holds_china else opp,
        china_playable=holds_china,
    )

    ussr_influence = _parse_int_list(
        "ussr_influence", payload["ussr_influence"], expected_len=_NUM_COUNTRIES
    )
    us_influence = _parse_int_list(
        "us_influence", payload["us_influence"], expected_len=_NUM_COUNTRIES
    )
    for cid, amount in enumerate(ussr_influence):
        if amount:
            pub.influence[Side.USSR, cid] = int(amount)
    for cid, amount in enumerate(us_influence):
        if amount:
            pub.influence[Side.US, cid] = int(amount)

    opp_hand_size = int(payload["opp_hand_size"])
    return pub, hand, holds_china, opp_hand_size


def _build_model_inputs(
    pub: PublicState,
    hand: frozenset[int],
    holds_china: bool,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    hand_mask = _card_mask(hand)
    influence = torch.tensor(
        list(pub.influence._data[:_NUM_COUNTRIES]) + list(pub.influence._data[_NUM_COUNTRIES:]),
        dtype=torch.float32,
    ).unsqueeze(0)
    cards = torch.tensor(
        hand_mask + hand_mask + ([0] * _CARD_MASK_LEN) + ([0] * _CARD_MASK_LEN),
        dtype=torch.float32,
    ).unsqueeze(0)
    scalars = torch.tensor(
        [
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
            float(int(pub.phasing)),
        ],
        dtype=torch.float32,
    ).unsqueeze(0)
    return influence, cards, scalars


def _extract_output_tensor(outputs: Any, key: str, index: int) -> torch.Tensor:
    if isinstance(outputs, dict) and key in outputs:
        tensor = outputs[key]
    elif isinstance(outputs, (tuple, list)) and len(outputs) > index:
        tensor = outputs[index]
    else:
        raise ValueError(f"model output missing {key}")
    if not isinstance(tensor, torch.Tensor):
        raise ValueError(f"model output {key} is not a tensor")
    if tensor.ndim != 2 or tensor.shape[0] != 1:
        raise ValueError(f"model output {key} must have shape (1, N)")
    return tensor[0]


def _ranked_targets(country_logits: torch.Tensor, accessible: list[int], count: int) -> list[int]:
    ranked = sorted(accessible, key=lambda cid: (-float(country_logits[cid].item()), cid))
    if not ranked or count <= 0:
        return []
    if count <= len(ranked):
        return ranked[:count]
    return ranked + [ranked[0]] * (count - len(ranked))


def _decode_action(
    outputs: Any,
    pub: PublicState,
    hand: frozenset[int],
    holds_china: bool,
    adj: dict[int, frozenset[int]],
) -> dict[str, Any]:
    del holds_china  # encoded into the feature tensor already

    playable = sorted(cid for cid in hand if 1 <= cid <= 111)
    if not playable:
        raise ValueError("hand must contain at least one playable card id")

    card_logits = _extract_output_tensor(outputs, "card_logits", 0)
    masked_card_logits = torch.full_like(card_logits, float("-inf"))
    for card_id in playable:
        masked_card_logits[card_id - 1] = card_logits[card_id - 1]
    card_id = int(torch.argmax(masked_card_logits).item()) + 1

    mode_logits = _extract_output_tensor(outputs, "mode_logits", 1)
    legal = sorted(legal_modes(card_id, pub, pub.phasing, adj=adj), key=int)
    if not legal:
        legal = [ActionMode(i) for i in range(mode_logits.shape[0])]
    masked_mode_logits = torch.full_like(mode_logits, float("-inf"))
    for mode in legal:
        masked_mode_logits[int(mode)] = mode_logits[int(mode)]
    mode = ActionMode(int(torch.argmax(masked_mode_logits).item()))

    if mode in (ActionMode.EVENT, ActionMode.SPACE):
        targets: list[int] = []
    else:
        country_logits = _extract_output_tensor(outputs, "country_logits", 2)
        accessible = sorted(accessible_countries(pub.phasing, pub, adj, mode=mode))
        if mode == ActionMode.COUP:
            targets = _ranked_targets(country_logits, accessible, 1)
        else:
            ops = effective_ops(card_id, pub, pub.phasing)
            targets = _ranked_targets(country_logits, accessible, ops)

    return {
        "card_id": card_id,
        "mode": mode.name.lower(),
        "targets": targets,
    }


class _Handler(BaseHTTPRequestHandler):
    model: torch.jit.ScriptModule
    adjacency: dict[int, frozenset[int]]

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _write_json(self, status: HTTPStatus, payload: dict[str, Any]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path != "/health":
            self._write_json(HTTPStatus.NOT_FOUND, {"error": "not found"})
            return
        self._write_json(HTTPStatus.OK, {"status": "ok"})

    def do_POST(self) -> None:
        if self.path != "/action":
            self._write_json(HTTPStatus.NOT_FOUND, {"error": "not found"})
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._write_json(HTTPStatus.BAD_REQUEST, {"error": "invalid content length"})
            return

        try:
            body = self.rfile.read(content_length)
            payload = json.loads(body.decode("utf-8"))
            if not isinstance(payload, dict):
                raise ValueError("request body must be a JSON object")
            pub, hand, holds_china, _opp_hand_size = _build_public_state(payload)
            influence, cards, scalars = _build_model_inputs(pub, hand, holds_china)
            with torch.inference_mode():
                outputs = self.model(influence, cards, scalars)
            action = _decode_action(outputs, pub, hand, holds_china, self.adjacency)
        except json.JSONDecodeError:
            self._write_json(HTTPStatus.BAD_REQUEST, {"error": "invalid json"})
            return
        except ValueError as exc:
            self._write_json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
            return
        except Exception as exc:
            self._write_json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})
            return

        self._write_json(HTTPStatus.OK, action)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Minimal TorchScript play server.")
    parser.add_argument("--model", required=True, help="Path to a TorchScript model")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    _set_memory_limit(_MEMORY_LIMIT_BYTES)
    torch.set_num_threads(1)
    try:
        torch.set_num_interop_threads(1)
    except RuntimeError:
        pass

    model = torch.jit.load(args.model, map_location="cpu")
    model.eval()
    adjacency = load_adjacency()

    class Handler(_Handler):
        pass

    Handler.model = model
    Handler.adjacency = adjacency

    server = ThreadingHTTPServer(("0.0.0.0", args.port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
