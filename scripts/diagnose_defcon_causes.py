"""Diagnose nuclear war causes in current heuristic — fast multiprocessed version."""
import multiprocessing as mp
from collections import Counter


def _run_game(seed: int) -> dict:
    from tsrl.policies.minimal_hybrid import choose_minimal_hybrid, MinimalHybridParams
    from tsrl.engine.game_loop import run_game_cb

    params = MinimalHybridParams()
    last_ussr: dict = {}
    last_us: dict = {}

    def ussr_policy(pub, hand, holds_china):
        action = choose_minimal_hybrid(pub, hand, holds_china, params)
        last_ussr.update(defcon=pub.defcon, action=action)
        return action

    def us_policy(pub, hand, holds_china):
        action = choose_minimal_hybrid(pub, hand, holds_china, params)
        last_us.update(defcon=pub.defcon, action=action)
        return action

    result = run_game_cb(ussr_policy=ussr_policy, us_policy=us_policy, seed=seed)

    causes = []
    if result.end_reason == "defcon1":
        for side_name, last in [("USSR", last_ussr), ("US", last_us)]:
            if last.get("defcon") == 2 and last.get("action"):
                a = last["action"]
                mode_name = a.mode.name if hasattr(a.mode, "name") else str(a.mode)
                causes.append(f"{side_name}:def=2 card={a.card_id} mode={mode_name}")

    return {"end_reason": result.end_reason, "causes": causes}


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-games", type=int, default=400)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    seeds = list(range(args.seed, args.seed + args.n_games))
    print(f"Running {args.n_games} games on {args.workers} workers...")

    ctx = mp.get_context("spawn")
    with ctx.Pool(processes=args.workers) as pool:
        results = pool.map(_run_game, seeds)

    war_causes: Counter = Counter()
    nuclear_wars = sum(1 for r in results if r["end_reason"] == "defcon1")
    for r in results:
        for c in r["causes"]:
            war_causes[c] += 1

    print(f"\nNuclear wars: {nuclear_wars}/{args.n_games} = {nuclear_wars/args.n_games:.1%}")
    print("\nTop causes (last action at DEFCON=2 before death):")
    for cause, count in war_causes.most_common(25):
        print(f"  {count:3d}x  {cause}")


if __name__ == "__main__":
    main()
