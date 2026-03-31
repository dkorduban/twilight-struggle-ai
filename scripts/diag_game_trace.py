"""Step 5: Side-by-side game trace — compare two checkpoints on same seeds vs heuristic.

Plays N fixed-seed games with each checkpoint and prints per-game results.

Usage:
    uv run python scripts/diag_game_trace.py \
        --ckpt-a data/checkpoints/retrain_v23/baseline_best.pt \
        --ckpt-b data/checkpoints/retrain_v24/baseline_best.pt \
        --n-games 20 --seed 12345
"""
from __future__ import annotations
import argparse, sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

import torch

from tsrl.engine.game_loop import play_game, make_random_policy
from tsrl.engine.game_state import GameState, reset
from tsrl.policies.learned_policy import make_learned_policy
from tsrl.policies.minimal_hybrid import make_minimal_hybrid_policy
from tsrl.schemas import Side


def load_policy(ckpt_path: str, device):
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    from tsrl.policies.model import TSBaselineModel
    hidden_dim = ckpt.get("args", {}).get("hidden_dim", 256)
    model = TSBaselineModel(hidden_dim=hidden_dim, dropout=0.0).to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()
    ep = ckpt.get("epoch", "?")
    val_loss = ckpt.get("val_metrics", {}).get("loss", float("nan"))
    print(f"  Loaded {ckpt_path}  ep={ep}  val_loss={val_loss:.4f}")
    return make_learned_policy(ckpt_path, device)


def run_games(policy, label: str, n_games: int, seed: int) -> dict:
    heuristic = make_minimal_hybrid_policy()
    wins = draws = losses = 0
    end_turns = []
    end_reasons = []
    rng = random.Random(seed)

    for i in range(n_games):
        game_seed = rng.randint(0, 2**31)
        # Alternate sides
        if i % 2 == 0:
            ussr_policy, us_policy = policy, heuristic
            learned_side = Side.USSR
        else:
            ussr_policy, us_policy = heuristic, policy
            learned_side = Side.US

        result = play_game(ussr_policy, us_policy, seed=game_seed)

        if result.winner == learned_side:
            wins += 1
            outcome = "W"
        elif result.winner is None:
            draws += 1
            outcome = "D"
        else:
            losses += 1
            outcome = "L"

        end_turns.append(result.end_turn)
        end_reasons.append(result.end_reason or "?")

        if i < 10 or outcome == "W":
            print(f"  [{label}] game {i+1:3d}  {outcome}  turn={result.end_turn}  "
                  f"reason={result.end_reason}  vp={result.final_vp:+d}  "
                  f"learned={'USSR' if learned_side==Side.USSR else 'US'}")

    decisive = wins + losses
    wr = wins / decisive if decisive else 0.0
    avg_turn = sum(end_turns) / len(end_turns)
    reason_counts = {}
    for r in end_reasons:
        reason_counts[r] = reason_counts.get(r, 0) + 1

    print(f"\n  [{label}] SUMMARY: {wins}W/{draws}D/{losses}L  "
          f"win_rate={100*wr:.1f}%  avg_end_turn={avg_turn:.1f}  "
          f"reasons={reason_counts}")
    return {"wins": wins, "draws": draws, "losses": losses, "win_rate": wr,
            "avg_turn": avg_turn, "reasons": reason_counts}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt-a", required=True)
    ap.add_argument("--ckpt-b", required=True)
    ap.add_argument("--n-games", type=int, default=20)
    ap.add_argument("--seed",    type=int, default=12345)
    args = ap.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    print("Loading checkpoints...")
    pol_a = load_policy(args.ckpt_a, device)
    pol_b = load_policy(args.ckpt_b, device)

    print(f"\n{'='*60}")
    print(f"Checkpoint A: {args.ckpt_a}")
    res_a = run_games(pol_a, "A", args.n_games, args.seed)

    print(f"\n{'='*60}")
    print(f"Checkpoint B: {args.ckpt_b}")
    res_b = run_games(pol_b, "B", args.n_games, args.seed)

    print(f"\n{'='*60}")
    print(f"COMPARISON (same {args.n_games} games, seed={args.seed})")
    print(f"  A (v23): {res_a['win_rate']*100:.1f}%  avg_turn={res_a['avg_turn']:.1f}  {res_a['reasons']}")
    print(f"  B (v24): {res_b['win_rate']*100:.1f}%  avg_turn={res_b['avg_turn']:.1f}  {res_b['reasons']}")


if __name__ == "__main__":
    main()
