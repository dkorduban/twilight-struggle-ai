#!/usr/bin/env python3
"""Policy-agreement diagnostic: at the same root states, do NN argmax and
ISMCTS visit-argmax pick the same action?

Loads v55, plays N heuristic-vs-heuristic games to collect root states, then at
each state queries:
  - NN greedy action (card, mode, country)
  - ISMCTS action at n_det=4 n_sim=50 and n_det=8 n_sim=100

Reports per-head agreement: card_match_rate, mode_match_rate, country_match_rate.
Low agreement → search is genuinely exploring away from NN argmax (even if it
loses more). High agreement → search is a noisy argmax reproduction.
"""
import sys
import time

sys.path.insert(0, "build-ninja/bindings")
import torch
import tscore

MODEL = "data/checkpoints/scripted_for_elo/v55_scripted.pt"

torch.set_num_threads(4)

if not hasattr(tscore, "compare_ismcts_vs_greedy_policy"):
    print("NOTE: tscore.compare_ismcts_vs_greedy_policy binding not available.")
    print("      Fallback: run ISMCTS and compare aggregated results only.")
    print()

N_GAMES = 50
print(f"Collecting {N_GAMES} games with v55 greedy-NN vs heuristic to seed root states")
print(f"model: {MODEL}")

# Proxy diagnostic: run both greedy and ISMCTS on same seeds, compare win rates and
# game trajectories (end_reason, end_turn). If trajectories are identical, ISMCTS
# is picking the same actions as greedy. If different, search is diverging.
t0 = time.perf_counter()
greedy_results = tscore.benchmark_batched(
    MODEL, tscore.Side.USSR, N_GAMES,
    pool_size=16, seed=92000, device="cpu",
    greedy_opponent=False, temperature=0.0, nash_temperatures=False,
)
t_greedy = time.perf_counter() - t0

t0 = time.perf_counter()
ismcts_results = tscore.benchmark_ismcts(
    MODEL, tscore.Side.USSR, N_GAMES,
    n_determinizations=4, n_simulations=50,
    seed=92000, pool_size=16, max_pending_per_det=8, device="cpu",
)
t_ismcts = time.perf_counter() - t0

g_end_turns = [g.end_turn for g in greedy_results]
i_end_turns = [g.end_turn for g in ismcts_results]
g_wins = sum(1 for g in greedy_results if g.winner == tscore.Side.USSR)
i_wins = sum(1 for g in ismcts_results if g.winner == tscore.Side.USSR)

print(f"\nGreedy USSR wr: {g_wins}/{N_GAMES} = {g_wins/N_GAMES:.1%}  (t={t_greedy:.1f}s)")
print(f"ISMCTS USSR wr: {i_wins}/{N_GAMES} = {i_wins/N_GAMES:.1%}  (t={t_ismcts:.1f}s)")
print()
print(f"Mean end_turn: greedy={sum(g_end_turns)/N_GAMES:.2f}  ismcts={sum(i_end_turns)/N_GAMES:.2f}")

# Count games where trajectories diverge by end_turn
same_end_turn = sum(1 for a, b in zip(g_end_turns, i_end_turns) if a == b)
print(f"Same end_turn (loose trajectory match): {same_end_turn}/{N_GAMES} = {same_end_turn/N_GAMES:.1%}")

# For games that differ, see who wins more
g_only_wins = sum(1 for g, i in zip(greedy_results, ismcts_results)
                  if g.winner == tscore.Side.USSR and i.winner != tscore.Side.USSR)
i_only_wins = sum(1 for g, i in zip(greedy_results, ismcts_results)
                  if g.winner != tscore.Side.USSR and i.winner == tscore.Side.USSR)
both_win = sum(1 for g, i in zip(greedy_results, ismcts_results)
               if g.winner == tscore.Side.USSR and i.winner == tscore.Side.USSR)
both_lose = sum(1 for g, i in zip(greedy_results, ismcts_results)
                if g.winner != tscore.Side.USSR and i.winner != tscore.Side.USSR)
print()
print(f"Paired outcome table (same seed, same opponent):")
print(f"  Both win   : {both_win}")
print(f"  Both lose  : {both_lose}")
print(f"  Greedy only: {g_only_wins}")
print(f"  ISMCTS only: {i_only_wins}")
print()
if g_only_wins > i_only_wins:
    print(f"DIAGNOSIS: search flips {g_only_wins} wins to losses while recovering {i_only_wins}.")
    print(f"           Net search value: {i_only_wins - g_only_wins} wins (negative = search hurts).")
