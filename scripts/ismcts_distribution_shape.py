#!/usr/bin/env python3
"""ISMCTS-vs-NN distribution-shape diagnostic.

At each mined root state, run ISMCTS and compare the NN policy prior to the
ISMCTS visit-count distribution. The binding `tscore.ismcts_search_from_state`
returns per-edge `prior` (NN softmax over legal actions at the root) and
`visits` (ISMCTS visit count), so one call gives both distributions.

Reports per state:
  nn_top1 / mcts_top1     top action by each policy (card_id, mode, visits)
  top1_match              whether argmax(prior) == argmax(visits) at edge level
  card_top1_match         whether argmax by card aggregate matches
  nn_entropy, mcts_entropy
  kl_nn_to_mcts           KL(prior || visits/N)
  js_div                  Jensen-Shannon (symmetric, bounded [0,1])
  q_gap                   q(mcts_argmax) - q(nn_argmax) from ISMCTS estimates
  spearman_rho            rank correlation (top-K by prior vs top-K by visits)

Aggregate means + histograms at the end.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, "build-ninja/bindings")
import tscore  # noqa: E402

DEFAULT_POSITIONS = Path("data/teacher_targets/v84/hard_positions_top1000.jsonl")
DEFAULT_MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"


def safe_log(p: float) -> float:
    return math.log(p) if p > 1e-12 else math.log(1e-12)


def entropy(probs: list[float]) -> float:
    s = sum(probs)
    if s <= 0:
        return 0.0
    return -sum((p / s) * safe_log(p / s) for p in probs if p > 0)


def kl(p: list[float], q: list[float]) -> float:
    sp, sq = sum(p), sum(q)
    if sp <= 0 or sq <= 0:
        return float("nan")
    out = 0.0
    for pi, qi in zip(p, q):
        pn = pi / sp
        if pn <= 0:
            continue
        qn = qi / sq
        out += pn * (safe_log(pn) - safe_log(qn))
    return out


def js_divergence(p: list[float], q: list[float]) -> float:
    sp, sq = sum(p), sum(q)
    if sp <= 0 or sq <= 0:
        return float("nan")
    pn = [x / sp for x in p]
    qn = [x / sq for x in q]
    m = [0.5 * (a + b) for a, b in zip(pn, qn)]
    return 0.5 * (kl(pn, m) + kl(qn, m)) / math.log(2)


def spearman(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 2:
        return float("nan")

    def rank(vs: list[float]) -> list[float]:
        idx = sorted(range(len(vs)), key=lambda i: vs[i])
        r = [0.0] * len(vs)
        i = 0
        while i < len(vs):
            j = i
            while j + 1 < len(vs) and vs[idx[j + 1]] == vs[idx[i]]:
                j += 1
            avg = 0.5 * (i + j) + 1
            for k in range(i, j + 1):
                r[idx[k]] = avg
            i = j + 1
        return r

    rx, ry = rank(xs), rank(ys)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    dy = math.sqrt(sum((b - my) ** 2 for b in ry))
    return num / (dx * dy) if dx > 0 and dy > 0 else float("nan")


def analyze_state(edges: list[dict]) -> dict:
    if not edges:
        return {}

    priors = [e["prior"] for e in edges]
    visits = [e["visits"] for e in edges]
    qs = [e["mean_value"] for e in edges]
    total_v = sum(visits)

    nn_argmax = max(range(len(edges)), key=lambda i: priors[i])
    mcts_argmax = max(range(len(edges)), key=lambda i: visits[i])

    # Card-level aggregates (collapse modes/targets per card_id)
    by_card_prior: dict[int, float] = {}
    by_card_visits: dict[int, int] = {}
    for e in edges:
        cid = e["card_id"]
        by_card_prior[cid] = by_card_prior.get(cid, 0.0) + e["prior"]
        by_card_visits[cid] = by_card_visits.get(cid, 0) + e["visits"]
    nn_card = max(by_card_prior, key=by_card_prior.get)
    mcts_card = max(by_card_visits, key=by_card_visits.get)

    nn_e = edges[nn_argmax]
    mcts_e = edges[mcts_argmax]

    return {
        "n_edges": len(edges),
        "nn_top1": {
            "card_id": nn_e["card_id"],
            "mode": nn_e["mode"],
            "prior": nn_e["prior"],
            "visits": nn_e["visits"],
            "q": nn_e["mean_value"],
        },
        "mcts_top1": {
            "card_id": mcts_e["card_id"],
            "mode": mcts_e["mode"],
            "prior": mcts_e["prior"],
            "visits": mcts_e["visits"],
            "q": mcts_e["mean_value"],
        },
        "edge_top1_match": nn_argmax == mcts_argmax,
        "card_top1_match": nn_card == mcts_card,
        "nn_entropy": entropy(priors),
        "mcts_entropy": entropy([max(v, 0) for v in visits]),
        "max_prior": max(priors),
        "visit_concentration": (max(visits) / total_v) if total_v > 0 else 0.0,
        "kl_nn_to_mcts": kl(priors, [v + 1e-6 for v in visits]),
        "js_div": js_divergence(priors, [v + 1e-6 for v in visits]),
        "q_gap": mcts_e["mean_value"] - nn_e["mean_value"],
        "spearman_rho": spearman(priors, [float(v) for v in visits]),
        "total_visits": total_v,
    }


def fmt_pct(xs: list[bool]) -> str:
    if not xs:
        return "n/a"
    return f"{100.0 * sum(xs) / len(xs):5.1f}%"


def fmt_mean(xs: list[float]) -> str:
    xs = [x for x in xs if x is not None and not math.isnan(x)]
    if not xs:
        return "n/a"
    return f"{sum(xs) / len(xs):+.3f}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--positions", type=Path, default=DEFAULT_POSITIONS)
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--n-states", type=int, default=50)
    p.add_argument("--n-det", type=int, default=4)
    p.add_argument("--n-sim", type=int, default=50)
    p.add_argument("--pool", type=int, default=16)
    p.add_argument("--pend", type=int, default=8)
    p.add_argument("--seed-base", type=int, default=91000)
    p.add_argument("--out", type=Path, default=Path("results/ismcts_fix/distribution_shape.jsonl"))
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args()

    positions: list[dict] = []
    with args.positions.open() as f:
        for line in f:
            positions.append(json.loads(line))
            if len(positions) >= args.n_states:
                break

    print(
        f"Loaded {len(positions)} positions from {args.positions}\n"
        f"Model: {args.model}\n"
        f"Config: n_det={args.n_det} n_sim={args.n_sim} pool={args.pool} pend={args.pend}\n",
        flush=True,
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    records = []
    wall_total = 0.0

    header = (
        f"{'idx':>3} {'turn':>4} {'ar':>2} {'ph':>2} "
        f"{'NN_card/m':>10} {'NN_pri':>7} "
        f"{'MC_card/m':>10} {'MC_vis':>7} "
        f"{'match':>5} {'H_nn':>5} {'H_mc':>5} "
        f"{'JS':>5} {'KL':>6} {'qgap':>6} {'rho':>5}"
    )
    print(header)
    print("-" * len(header))

    with args.out.open("w") as out_f:
        for i, pos in enumerate(positions):
            sd = pos["state_dict"]
            t0 = time.perf_counter()
            try:
                r = tscore.ismcts_search_from_state(
                    state_dict=sd,
                    model_path=args.model,
                    n_determinizations=args.n_det,
                    n_simulations=args.n_sim,
                    max_pending_per_det=args.pend,
                    c_puct=1.5,
                    seed=args.seed_base + i,
                )
            except Exception as e:
                print(f"{i:>3} ERROR: {e!r}", flush=True)
                continue
            elapsed = time.perf_counter() - t0
            wall_total += elapsed

            a = analyze_state(r["edges"])
            if not a:
                continue
            rec = {
                "idx": i,
                "turn": sd["turn"],
                "ar": sd["ar"],
                "phasing": sd["phasing"],
                "elapsed_s": elapsed,
                "root_value": r["root_value"],
                **a,
            }
            records.append(rec)
            out_f.write(json.dumps(rec) + "\n")
            out_f.flush()

            print(
                f"{i:>3} {sd['turn']:>4} {sd['ar']:>2} {sd['phasing']:>2} "
                f"{a['nn_top1']['card_id']:3d}/{a['nn_top1']['mode']:1d}    "
                f"{a['nn_top1']['prior']:6.3f}  "
                f"{a['mcts_top1']['card_id']:3d}/{a['mcts_top1']['mode']:1d}    "
                f"{a['mcts_top1']['visits']:6d}  "
                f"{'YES' if a['edge_top1_match'] else 'no':>5} "
                f"{a['nn_entropy']:5.2f} {a['mcts_entropy']:5.2f} "
                f"{a['js_div']:5.3f} {a['kl_nn_to_mcts']:6.3f} "
                f"{a['q_gap']:+6.3f} {a['spearman_rho']:+5.2f}",
                flush=True,
            )

    if not records:
        print("No records — aborting aggregate.")
        return

    edge_matches = [r["edge_top1_match"] for r in records]
    card_matches = [r["card_top1_match"] for r in records]
    js = [r["js_div"] for r in records]
    kl_vals = [r["kl_nn_to_mcts"] for r in records]
    h_nn = [r["nn_entropy"] for r in records]
    h_mc = [r["mcts_entropy"] for r in records]
    q_gaps = [r["q_gap"] for r in records]
    rhos = [r["spearman_rho"] for r in records]
    vis_conc = [r["visit_concentration"] for r in records]
    max_prior = [r["max_prior"] for r in records]

    # q_gap buckets: search found better, same, worse
    q_better = sum(1 for q in q_gaps if q > 0.01)
    q_same = sum(1 for q in q_gaps if abs(q) <= 0.01)
    q_worse = sum(1 for q in q_gaps if q < -0.01)

    # Top card disagreement histogram: what does MCTS pick when NN is wrong?
    disagreements = [
        (r["nn_top1"]["card_id"], r["mcts_top1"]["card_id"])
        for r in records
        if not r["edge_top1_match"]
    ]

    print()
    print("=" * 60)
    print("AGGREGATE")
    print("=" * 60)
    print(f"N states:                {len(records)}")
    print(f"Wall time:               {wall_total:.1f}s ({wall_total/len(records):.2f}s/state)")
    print(f"Edge top-1 match:        {fmt_pct(edge_matches)}  ({sum(edge_matches)}/{len(records)})")
    print(f"Card top-1 match:        {fmt_pct(card_matches)}  ({sum(card_matches)}/{len(records)})")
    print(f"Mean NN entropy:         {fmt_mean(h_nn)}")
    print(f"Mean ISMCTS entropy:     {fmt_mean(h_mc)}")
    print(f"Mean max(prior):         {fmt_mean(max_prior)}")
    print(f"Mean visit concentration:{fmt_mean(vis_conc)}")
    print(f"Mean JS(NN||ISMCTS):     {fmt_mean(js)}")
    print(f"Mean KL(NN||ISMCTS):     {fmt_mean(kl_vals)}")
    print(f"Mean Spearman rho:       {fmt_mean(rhos)}")
    print()
    print(f"q_gap = Q(ISMCTS_argmax) − Q(NN_argmax), from ISMCTS value estimates")
    print(f"  search found better (>+0.01): {q_better}/{len(records)}  ({100*q_better/len(records):.0f}%)")
    print(f"  tie (|gap|≤0.01):             {q_same}/{len(records)}")
    print(f"  search found worse (<−0.01):  {q_worse}/{len(records)}  ({100*q_worse/len(records):.0f}%)")
    print(f"  mean q_gap:                   {fmt_mean(q_gaps)}")

    if disagreements:
        print()
        print(f"Top disagreements (NN card → MCTS card), {len(disagreements)} total:")
        counter = Counter(disagreements)
        for (nn_c, mc_c), n in counter.most_common(10):
            print(f"  card {nn_c:3d} → card {mc_c:3d}: {n}")

    print()
    print(f"Per-state records saved to {args.out}")


if __name__ == "__main__":
    main()
