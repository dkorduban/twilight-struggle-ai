from __future__ import annotations

from .config import HeuristicConfig
from .tscore_experimental import get_tscore_experimental


def play_selfplay_game(seed: int | None = 12345, config: HeuristicConfig | None = None) -> dict:
    module = get_tscore_experimental()
    return module.play_selfplay_game(seed=seed, config={} if config is None else config.__dict__)
