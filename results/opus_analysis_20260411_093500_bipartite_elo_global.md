---
# Opus Analysis: Bipartite Elo in Global Tournament
Date: 2026-04-11T09:35:00Z
Question: How to get reasonable bipartite (per-side) Elo ratings in the global Elo tournament, similar to what confirmation tournaments produce?

## Executive Summary

The extreme bipartite Elo values in the global tournament (e.g. elo_ussr=7908, elo_us=-12186 for v55) are caused by a **Newton-step solver divergence** in `bayeselo_fit()` when applied to the bipartite graph structure. In bipartite graphs (USSR-nodes only play US-nodes), the systematic USSR side advantage pushes ratings apart, making the predicted win probability approach 0 or 1 for many matchups. This causes the diagonal Hessian approximation (p\*(1-p)) to approach zero, making Newton step sizes explode. The fix is straightforward: replace the Newton-step solver with the standard **Minorization-Maximization (MM) algorithm** for the bipartite fit, which is guaranteed to converge for connected Bradley-Terry graphs. Verified on the full 34-model global dataset: MM produces reasonable values (e.g. v55 USSR=2117, US=2065, gap=+53).

## Findings

### 1. How the global Elo tournament computes bipartite per-side Elo

In `scripts/run_elo_tournament.py`:
- `_bipartite_matches()` (line 305-336) constructs a 2N-node bipartite match list: each model `X` becomes `X_USSR` and `X_US`.
- Each original match generates two sub-matches: `{a}_USSR vs {b}_US` and `{b}_USSR vs {a}_US`.
- A single anchor (`v14_USSR = 2015`) is used for the full bipartite fit.
- The same `bayeselo_fit()` function (Newton-step MM solver, lines 69-121) is used for both combined and bipartite ratings.

### 2. How confirmation tournaments compute per-side Elo

`scripts/ppo_confirm_best.py` delegates to `scripts/run_elo_tournament.py` with the same `bayeselo_fit()` solver. The confirmation tournament uses the **identical code path**. The reason confirmation per-side Elo values appear reasonable (e.g. v14 USSR=2015, US=1985) is that:
- Confirmation tournaments have fewer models (7 candidates + 4 fixtures = 11 total = 22 bipartite nodes)
- The candidates are close in strength (from the same PPO run)
- With 200 games/side and models close in strength, the predicted win probabilities stay away from 0/1
- The Newton solver converges before diverging because it only needs small steps

With the full global tournament (34 models = 68 bipartite nodes, spanning heuristic to v55), the strength range is much larger. Heuristic_US wins only 3-5% of games against most model_USSR nodes, pushing predicted p_win to extreme values where the solver destabilizes.

### 3. Root cause: Newton solver instability on bipartite graphs

The `bayeselo_fit()` solver uses a diagonal Newton step in log-odds space:

```
grad = actual_wins - expected_wins
hess_diag = sum(n_games * p_win * (1 - p_win))  # for all opponents
new_rating = old_rating + grad / hess_diag
```

In a bipartite graph where USSR systematically beats US:
1. Ratings spread: all USSR nodes go up, all US nodes go down
2. As ratings spread, p_win for USSR-vs-US matchups approaches 1.0
3. The Hessian term `p*(1-p)` approaches 0, making `hess_diag` tiny
4. Newton step = `grad / tiny_number` = huge overshoot
5. The solver oscillates and diverges, producing values like +7908 / -12186

This is a well-known failure mode of diagonal Newton methods on bipartite structures. The off-diagonal Hessian terms (which couple USSR and US nodes) are completely ignored by the diagonal approximation.

### 4. Verified fix: MM algorithm

The standard Minorization-Maximization (MM) algorithm for Bradley-Terry models works in "strength" space (gamma = exp(rating)) with the update:

```
gamma_new[i] = total_wins[i] / sum_over_opponents(n_games_ij / (gamma[i] + gamma[j]))
```

This is provably convergent for any connected comparison graph (Hunter 2004). Tested on the full 34-model global dataset:

| Model     | elo_ussr (MM) | elo_us (MM) | gap  |
|-----------|---------------|-------------|------|
| v55       | 2117          | 2065        | +53  |
| v46       | 2119          | 2033        | +87  |
| v22       | 2095          | 2030        | +65  |
| v14       | 2015          | 1939        | +76  |
| heuristic | 1763          | 1601        | +162 |

All values are in a reasonable range. The USSR-US gap is 50-180 Elo, consistent with the known game asymmetry (USSR ~62% WR overall).

### 5. Confirmation tournaments: lucky convergence, not correct algorithm

The confirmation tournaments get reasonable values by accident -- the Newton solver happens to converge when models are close in strength. If a confirmation tournament included a very weak model (e.g. an early iteration with <10% WR), the same divergence would occur. The fix should be applied to both code paths (they share the same solver).

## Conclusions

1. The extreme bipartite Elo values (elo_ussr=7908, elo_us=-12186) are caused by Newton-step solver divergence in `bayeselo_fit()` when applied to bipartite graphs with large strength differences.
2. The diagonal Hessian approximation becomes degenerate when p_win approaches 0 or 1, which is inevitable in bipartite graphs with systematic side advantages.
3. Confirmation tournaments work by luck (small strength range), not by correctness.
4. The standard MM (Minorization-Maximization) algorithm is the correct solver for Bradley-Terry models on arbitrary connected graphs, including bipartite ones. It is provably convergent.
5. Replacing the solver for the bipartite fit produces reasonable values that are directly comparable to combined Elo (e.g. v55 combined=2124, USSR=2117, US=2065).
6. The combined (non-bipartite) Elo fit is unaffected -- the Newton solver works fine there because each player has opponents on both sides of the strength spectrum.

## Recommendations

1. **Add an MM solver function** (`bayeselo_fit_mm`) to `scripts/run_elo_tournament.py` that uses the standard MM update in gamma-space. Keep the existing Newton solver for the combined fit where it works well.

2. **Use MM for the bipartite fit only**: Change the bipartite fitting section (around line 540) to call `bayeselo_fit_mm` instead of `bayeselo_fit`. This is a ~30-line change.

3. **Implementation sketch** for `bayeselo_fit_mm`:
   ```python
   def bayeselo_fit_mm(matches, anchor, anchor_elo=1500.0, max_iter=5000, tol=1e-10):
       players = sorted({m.player_a for m in matches} | {m.player_b for m in matches})
       idx = {p: i for i, p in enumerate(players)}
       n = len(players)
       gamma = [1.0] * n
       for _ in range(max_iter):
           new_gamma = gamma[:]
           for i, p in enumerate(players):
               if p == anchor:
                   continue
               wins_i = sum(m.wins_a for m in matches if m.player_a == p) + \
                        sum(m.wins_b for m in matches if m.player_b == p)
               if wins_i == 0:
                   new_gamma[i] = 1e-10
                   continue
               denom = sum(
                   m.games / (gamma[i] + gamma[idx[m.player_b if m.player_a == p else m.player_a]])
                   for m in matches if m.player_a == p or m.player_b == p
               )
               if denom > 1e-15:
                   new_gamma[i] = wins_i / denom
           scale = 1.0 / new_gamma[idx[anchor]]
           new_gamma = [g * scale for g in new_gamma]
           delta = max(abs(math.log(max(new_gamma[i], 1e-300)) - math.log(max(gamma[i], 1e-300))) for i in range(n))
           gamma = new_gamma
           if delta < tol:
               break
       elo_scale = 400.0 / math.log(10.0)
       return {p: anchor_elo + math.log(max(gamma[idx[p]], 1e-300)) * elo_scale for p in players}
   ```

4. **Re-run the global tournament** after the fix: `uv run python scripts/run_elo_tournament.py --resume-from results/elo_full_ladder.json ...` (no new matches needed, just re-fits ratings from cached match results).

5. **Optional improvement**: Also switch the combined fit to MM for consistency and robustness, though it is not required since the Newton solver works correctly for the non-bipartite case.

## Open Questions

1. Should the `bayeselo_ci95` function also be updated? The current Fisher-information CI is based on the Newton Hessian and may also be inaccurate for bipartite fits. For now, CIs on per-side Elo can be deferred -- the point estimates are the priority.

2. The bipartite RMSE in confirmation tournaments is often >= combined RMSE, suggesting that per-side Elo does not improve prediction. This may be because all models share similar USSR/US asymmetry (they are all trained the same way). The per-side Elo is still useful for monitoring whether a model is disproportionately strong/weak on one side.
---
