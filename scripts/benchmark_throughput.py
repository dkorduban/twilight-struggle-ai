"""Throughput benchmark for model inference and MCTS modes.

Measures:
  1. Model forward-pass throughput (inference, various batch sizes)
  2. Training step throughput (forward + backward, batch_size=1024)
  3. Plain vectorized collection throughput (N games, batched inference)
  4. Interleaved MCTS throughput (N games, n_sim simulations per move)

Usage:
    uv run python scripts/benchmark_throughput.py
    uv run python scripts/benchmark_throughput.py --checkpoint data/checkpoints/retrain_v20/baseline_best.pt
    uv run python scripts/benchmark_throughput.py --n-games 30 --n-sim 20 --secs 10
"""
from __future__ import annotations

import argparse
import os
import random
import sys
import time
from typing import Callable

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

import torch
import torch.nn as nn

from tsrl.engine.game_state import reset
from tsrl.engine.mcts import interleaved_uct_mcts
from tsrl.engine.vec_runner import run_games_vectorized
from tsrl.policies.learned_policy import _extract_features
from tsrl.policies.model import (
    CARD_DIM, CARD_HIDDEN, INFLUENCE_DIM, INFLUENCE_HIDDEN,
    NUM_CARDS, NUM_COUNTRIES, NUM_MODES, NUM_PLAYABLE_CARDS, NUM_STRATEGIES,
    SCALAR_DIM, SCALAR_HIDDEN, TRUNK_HIDDEN, TSBaselineModel,
)
from tsrl.schemas import ActionEncoding, ActionMode, Side


# ---------------------------------------------------------------------------
# Old (flat-MLP) architecture — for throughput comparison
# ---------------------------------------------------------------------------

class _OldTrunkModel(nn.Module):
    """Pre-residual flat-MLP trunk — mirrors the v20 training architecture."""

    def __init__(self, hidden_dim: int = TRUNK_HIDDEN) -> None:
        super().__init__()
        trunk_in = INFLUENCE_HIDDEN + CARD_HIDDEN + SCALAR_HIDDEN  # 320
        self.influence_encoder = nn.Linear(INFLUENCE_DIM, INFLUENCE_HIDDEN)
        self.card_encoder = nn.Linear(CARD_DIM, CARD_HIDDEN)
        self.scalar_encoder = nn.Linear(SCALAR_DIM, SCALAR_HIDDEN)
        self.trunk = nn.Sequential(
            nn.Linear(trunk_in, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
        )
        self.card_head = nn.Linear(hidden_dim, NUM_PLAYABLE_CARDS)
        self.mode_head = nn.Linear(hidden_dim, NUM_MODES)
        self.strategy_heads = nn.Linear(hidden_dim, NUM_STRATEGIES * NUM_COUNTRIES)
        self.strategy_mixer = nn.Linear(hidden_dim, NUM_STRATEGIES)
        self.value_head = nn.Linear(hidden_dim, 1)

    def forward(self, influence, cards, scalars):
        h = torch.relu(self.influence_encoder(influence))
        c = torch.relu(self.card_encoder(cards))
        s = torch.relu(self.scalar_encoder(scalars))
        hidden = self.trunk(torch.cat([h, c, s], dim=-1))
        country_strategy_logits = self.strategy_heads(hidden).view(
            hidden.shape[0], NUM_STRATEGIES, NUM_COUNTRIES
        )
        strategy_logits = self.strategy_mixer(hidden)
        mixing = torch.softmax(strategy_logits, dim=1).unsqueeze(2)
        country_logits = (mixing * torch.softmax(country_strategy_logits, dim=2)).sum(dim=1)
        return {
            "card_logits": self.card_head(hidden),
            "mode_logits": self.mode_head(hidden),
            "country_logits": country_logits,
            "country_strategy_logits": country_strategy_logits,
            "strategy_logits": strategy_logits,
            "value": torch.tanh(self.value_head(hidden)),
        }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_random_batch(batch_size: int, device: torch.device):
    influence = torch.randn(batch_size, INFLUENCE_DIM, device=device)
    cards = torch.randint(0, 2, (batch_size, CARD_DIM), device=device).float()
    scalars = torch.rand(batch_size, SCALAR_DIM, device=device)
    return influence, cards, scalars


def _timed(fn: Callable, secs: float) -> tuple[int, float]:
    """Run fn() repeatedly for at least `secs` seconds. Return (calls, total_time)."""
    calls = 0
    t0 = time.perf_counter()
    while True:
        fn()
        calls += 1
        elapsed = time.perf_counter() - t0
        if elapsed >= secs:
            return calls, elapsed


def _fmt(n: float, unit: str = "") -> str:
    if n >= 1e6:
        return f"{n/1e6:.2f}M{unit}"
    if n >= 1e3:
        return f"{n/1e3:.1f}k{unit}"
    return f"{n:.1f}{unit}"


# ---------------------------------------------------------------------------
# 1. Model forward-pass throughput
# ---------------------------------------------------------------------------

def bench_inference(model: nn.Module, device: torch.device, secs: float = 5.0):
    print("\n── Model inference throughput ──────────────────────────────────────")
    model.eval()
    header = f"{'batch':>8}  {'samples/s':>12}  {'ms/sample':>10}  {'ms/batch':>10}"
    print(header)
    print("-" * len(header))

    for batch_size in [1, 4, 16, 64, 256, 1024]:
        inf, crd, scl = _make_random_batch(batch_size, device)
        def _fwd():
            with torch.no_grad():
                model(inf, crd, scl)
        if device.type == "cuda":
            torch.cuda.synchronize()
        calls, elapsed = _timed(_fwd, secs)
        if device.type == "cuda":
            torch.cuda.synchronize()
        samples = calls * batch_size
        samples_per_sec = samples / elapsed
        ms_per_sample = elapsed / samples * 1000
        ms_per_batch = elapsed / calls * 1000
        print(f"{batch_size:>8}  {_fmt(samples_per_sec):>12}  {ms_per_sample:>10.4f}  {ms_per_batch:>10.2f}")


# ---------------------------------------------------------------------------
# 2. Training step throughput
# ---------------------------------------------------------------------------

def bench_training(model: nn.Module, device: torch.device, secs: float = 5.0):
    print("\n── Training step throughput (fwd + bwd) ────────────────────────────")
    model.train()
    opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
    header = f"{'batch':>8}  {'samples/s':>12}  {'ms/step':>10}"
    print(header)
    print("-" * len(header))

    for batch_size in [256, 512, 1024, 2048]:
        inf, crd, scl = _make_random_batch(batch_size, device)
        card_tgt = torch.zeros(batch_size, dtype=torch.long, device=device)
        mode_tgt = torch.zeros(batch_size, dtype=torch.long, device=device)
        value_tgt = torch.zeros(batch_size, 1, device=device)
        country_tgt = torch.zeros(batch_size, 86, device=device)
        country_tgt[:, 0] = 1.0

        def _step():
            opt.zero_grad(set_to_none=True)
            out = model(inf, crd, scl)
            log_p = torch.log_softmax(out["country_logits"], dim=1)
            loss = (
                nn.functional.cross_entropy(out["card_logits"], card_tgt)
                + nn.functional.cross_entropy(out["mode_logits"], mode_tgt)
                + nn.functional.mse_loss(out["value"], value_tgt)
                - (country_tgt * log_p).sum(dim=1).mean()
            )
            loss.backward()
            opt.step()

        if device.type == "cuda":
            torch.cuda.synchronize()
        calls, elapsed = _timed(_step, secs)
        if device.type == "cuda":
            torch.cuda.synchronize()
        samples_per_sec = calls * batch_size / elapsed
        ms_per_step = elapsed / calls * 1000
        print(f"{batch_size:>8}  {_fmt(samples_per_sec):>12}  {ms_per_step:>10.2f}")

    model.eval()


# ---------------------------------------------------------------------------
# 3. Vectorized game collection throughput (plain batched inference)
# ---------------------------------------------------------------------------

def bench_plain_vectorized(
    model: nn.Module,
    device: torch.device,
    n_games: int,
    n_trials: int = 3,
):
    print(f"\n── Plain vectorized collection ({n_games} games) ───────────────────────")
    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency, sample_action
    from tsrl.policies.minimal_hybrid import choose_minimal_hybrid

    adj = load_adjacency()
    model.eval()

    def learned_infer_fn(requests, game_states):
        if not requests:
            return []
        inf_list, crd_list, scl_list = [], [], []
        for req in requests:
            inf, crd, scl = _extract_features(req.pub, req.hand, req.holds_china, req.side)
            inf_list.append(inf)
            crd_list.append(crd)
            scl_list.append(scl)
        with torch.no_grad():
            out = model(
                torch.cat(inf_list).to(device),
                torch.cat(crd_list).to(device),
                torch.cat(scl_list).to(device),
            )
        actions = []
        for i, req in enumerate(requests):
            card_logits = out["card_logits"][i].cpu()
            legal_c = legal_cards(req.hand, req.pub, req.side, holds_china=req.holds_china)
            if not legal_c:
                actions.append(sample_action(req.hand, req.pub, req.side, holds_china=req.holds_china, rng=random.Random(i)))
                continue
            mask = torch.full((card_logits.shape[0],), float("-inf"))
            for cid in legal_c:
                if 1 <= cid <= card_logits.shape[0]:
                    mask[cid - 1] = 0.0
            card_id = int((card_logits + mask).argmax()) + 1
            legal_m = list(legal_modes(card_id, req.pub, req.side, adj=adj))
            mode = legal_m[0] if legal_m else ActionMode.EVENT
            actions.append(ActionEncoding(card_id=card_id, mode=mode, targets=()))
        return actions

    def heuristic_fn(req):
        a = choose_minimal_hybrid(req.pub, req.hand, req.holds_china)
        if a is None:
            a = sample_action(req.hand, req.pub, req.side, holds_china=req.holds_china, rng=random.Random())
        return a

    times = []
    for trial in range(n_trials):
        t0 = time.perf_counter()
        run_games_vectorized(
            n_games=n_games,
            make_game_fn=lambda: reset(seed=random.randint(0, 2**32)),
            learned_side_fn=lambda idx: Side.USSR if idx % 2 == 0 else Side.US,
            learned_infer_fn=learned_infer_fn,
            heuristic_fn=heuristic_fn,
            seed_base=trial * 1000,
        )
        times.append(time.perf_counter() - t0)

    best = min(times)
    avg = sum(times) / len(times)
    print(f"  {n_games} games: best={best:.2f}s  avg={avg:.2f}s  "
          f"=> {n_games/best:.1f} games/s  ({n_games/best*60:.0f} games/min)")


# ---------------------------------------------------------------------------
# 4. Interleaved MCTS throughput
# ---------------------------------------------------------------------------

def bench_interleaved_mcts(
    model: nn.Module,
    device: torch.device,
    n_games: int,
    n_sim: int,
    n_candidates: int,
    n_trials: int = 2,
):
    print(f"\n── Interleaved MCTS ({n_games} games, n_sim={n_sim}, n_cand={n_candidates}) ──────────────")
    from tsrl.engine.legal_actions import legal_cards, legal_modes, load_adjacency, sample_action
    from tsrl.engine.mcts import _holds_china as _mcts_holds_china, _sample_candidates
    from tsrl.policies.minimal_hybrid import _DEFCON_LOWERING_CARDS, choose_minimal_hybrid
    from tsrl.policies.learned_policy import _build_action_from_country_logits, _build_random_targets

    adj = load_adjacency()
    model.eval()
    expected_influence_dim = INFLUENCE_DIM

    def batch_value_fn(game_states_leaf):
        if not game_states_leaf:
            return []
        inf_list, crd_list, scl_list = [], [], []
        for gs in game_states_leaf:
            side = gs.pub.phasing
            holds_c = _mcts_holds_china(gs, side)
            inf, crd, scl = _extract_features(gs.pub, gs.hands[side], holds_c, side)
            inf_list.append(inf.to(device))
            crd_list.append(crd.to(device))
            scl_list.append(scl.to(device))
        with torch.no_grad():
            out = model(torch.cat(inf_list), torch.cat(crd_list), torch.cat(scl_list))
        return out["value"].squeeze(-1).cpu().tolist()

    def candidate_fn(gs, side, holds_china, n, *, rng=None):
        _rng = rng or random.Random()
        if n_candidates <= 0:
            return _sample_candidates(gs, side, holds_china, n, _rng)
        playable = sorted(legal_cards(gs.hands[side], gs.pub, side, holds_china=holds_china))
        if not playable:
            return []
        inf, crd, scl = _extract_features(gs.pub, gs.hands[side], holds_china, side)
        with torch.no_grad():
            out = model(inf.to(device), crd.to(device), scl.to(device))
        card_probs = torch.softmax(out["card_logits"][0], dim=0)
        mode_probs = torch.softmax(out["mode_logits"][0], dim=0)
        cl = out.get("country_logits")
        cl = cl[0] if cl is not None else None
        scored = []
        for card_id in playable:
            cs = float(card_probs[card_id - 1].item())
            for mode in sorted(legal_modes(card_id, gs.pub, side, adj=adj), key=int):
                if mode == ActionMode.COUP and gs.pub.defcon <= 2:
                    continue
                if mode == ActionMode.EVENT and gs.pub.defcon <= 2 and card_id in _DEFCON_LOWERING_CARDS:
                    continue
                scored.append((card_id, mode, cs * float(mode_probs[int(mode)].item())))
        if not scored:
            return _sample_candidates(gs, side, holds_china, n, _rng)
        scored.sort(key=lambda x: (-x[2], x[0], int(x[1])))
        actions = []
        for card_id, mode, _ in scored[:max(1, n)]:
            if mode in (ActionMode.SPACE, ActionMode.EVENT):
                a = ActionEncoding(card_id=card_id, mode=mode, targets=())
            else:
                a = _build_action_from_country_logits(card_id, mode, cl, gs.pub, side, adj, _rng)
                if a is None:
                    a = _build_random_targets(card_id, mode, gs.pub, side, adj, _rng)
            if a is not None:
                actions.append(a)
        return actions or _sample_candidates(gs, side, holds_china, 1, _rng)

    def mcts_infer_fn(requests, game_states):
        results = interleaved_uct_mcts(
            game_states, n_sim, batch_value_fn,
            candidate_fn=candidate_fn, rng=random.Random(42),
        )
        out = []
        for action, req in zip(results, requests):
            if action is None:
                action = sample_action(req.hand, req.pub, req.side,
                                       holds_china=req.holds_china, rng=random.Random())
            out.append(action)
        return out

    def heuristic_fn(req):
        a = choose_minimal_hybrid(req.pub, req.hand, req.holds_china)
        if a is None:
            a = sample_action(req.hand, req.pub, req.side,
                              holds_china=req.holds_china, rng=random.Random())
        return a

    times = []
    for trial in range(n_trials):
        t0 = time.perf_counter()
        run_games_vectorized(
            n_games=n_games,
            make_game_fn=lambda: reset(seed=random.randint(0, 2**32)),
            learned_side_fn=lambda idx: Side.USSR if idx % 2 == 0 else Side.US,
            learned_infer_fn=mcts_infer_fn,
            heuristic_fn=heuristic_fn,
            seed_base=trial * 1000,
        )
        times.append(time.perf_counter() - t0)

    best = min(times)
    avg = sum(times) / len(times)
    print(f"  {n_games} games: best={best:.2f}s  avg={avg:.2f}s  "
          f"=> {n_games/best:.1f} games/s  ({n_games/best*60:.0f} games/min)")
    print(f"  (estimate for 2000 games: {2000/n_games*best/60:.1f} min)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _build_model(arch: str, hidden_dim: int, checkpoint: str | None) -> nn.Module:
    if arch == "old":
        model = _OldTrunkModel(hidden_dim=hidden_dim)
        if checkpoint and os.path.exists(checkpoint):
            ckpt = torch.load(checkpoint, map_location="cpu", weights_only=False)
            sd = ckpt.get("model_state_dict", ckpt)
            model.load_state_dict(sd, strict=False)
            print(f"  [old arch] loaded checkpoint: {checkpoint}")
        else:
            print(f"  [old arch] untrained, hidden_dim={hidden_dim}")
    else:
        model = TSBaselineModel(hidden_dim=hidden_dim)
        if checkpoint and os.path.exists(checkpoint):
            ckpt = torch.load(checkpoint, map_location="cpu", weights_only=False)
            sd = ckpt.get("model_state_dict", ckpt)
            model.load_state_dict(sd, strict=False)
            print(f"  [new arch] loaded checkpoint: {checkpoint}")
        else:
            print(f"  [new arch] untrained, hidden_dim={hidden_dim}")
    total_params = sum(p.numel() for p in model.parameters())
    print(f"  Parameters: {total_params:,}")
    return model


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", default=None,
                        help="Checkpoint to load (for --arch old, use a v19/v20 .pt)")
    parser.add_argument("--hidden-dim", type=int, default=256)
    parser.add_argument("--arch", choices=["new", "old", "both"], default="both",
                        help="Which architecture to benchmark (new=residual, old=flat-MLP, both)")
    parser.add_argument("--n-games", type=int, default=20)
    parser.add_argument("--n-sim", type=int, default=20)
    parser.add_argument("--n-candidates", type=int, default=8)
    parser.add_argument("--secs", type=float, default=5.0,
                        help="Seconds to run each micro-benchmark")
    parser.add_argument("--skip-training", action="store_true")
    parser.add_argument("--skip-games", action="store_true")
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    archs_to_bench = ["old", "new"] if args.arch == "both" else [args.arch]

    # For game collection, use the new arch model (or old if explicitly requested).
    game_model = None

    for arch in archs_to_bench:
        ckpt = args.checkpoint
        # For "both", use the v20 checkpoint for old arch (it's trained with old arch).
        if args.arch == "both" and arch == "old" and not ckpt:
            ckpt = "data/checkpoints/retrain_v20/baseline_best.pt"
        print(f"\n{'='*60}")
        print(f"Architecture: {arch.upper()}")
        model = _build_model(arch, args.hidden_dim, ckpt)
        model = model.to(device)

        bench_inference(model, device, secs=args.secs)
        if not args.skip_training:
            bench_training(model, device, secs=args.secs)

        if arch in ("new", archs_to_bench[-1]):
            game_model = model

    if not args.skip_games and game_model is not None:
        bench_plain_vectorized(game_model, device, n_games=args.n_games)

        for n_sim in [args.n_sim]:
            bench_interleaved_mcts(
                game_model, device,
                n_games=args.n_games,
                n_sim=n_sim,
                n_candidates=args.n_candidates,
            )


if __name__ == "__main__":
    main()
