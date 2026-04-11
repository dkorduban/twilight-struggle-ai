# Opus Analysis: Bipartite Elo Design for Per-Side Ratings
Date: 2026-04-10
Question: Is the per-side Elo (elo_ussr, elo_us) implementation mathematically correct? The user argues each checkpoint is 2 players in a bipartite graph requiring a single anchor.

## Executive Summary

The user's bipartite-graph argument is theoretically valid for a *joint* model that estimates both USSR-strength and US-strength simultaneously from a single likelihood, but the current implementation sidesteps the bipartite issue by using a simpler and defensible approach: it runs three independent BayesElo fits (combined, USSR-only, US-only), each treating model checkpoints as symmetric players within their respective pools. This approach is mathematically self-consistent within each pool and produces correct *relative* orderings per side, but it has a meaningful flaw: the three pools share the same anchor value (v12=2001), which makes the absolute Elo numbers directly comparable across pools when they should not be. The correct minimal fix is either (a) not comparing USSR Elo and US Elo numbers directly, or (b) switching to a proper bipartite 2N-node model with a single anchor.

## Findings

### 1. What the current code does

In `scripts/run_elo_tournament.py` (lines 303-332, 496-508):

- `_ussr_matches(matches)` extracts a match list where `wins_a` = model_a's wins when playing USSR, and `wins_b` = model_b's wins when playing USSR. Each matchup contributes at most `half` games (since each model plays USSR in half the games).
- `_us_matches(matches)` does the same for US-side wins.
- Each filtered list is passed to an **independent** `bayeselo_fit()` call with the same anchor (v12) and same anchor_elo (2001.0).

The `bayeselo_fit()` solver (lines 69-120) is a standard iterative MM/Newton BayesElo solver. It treats all input players as symmetric, computes log-odds ratings, anchors one player, and converts to Elo scale.

### 2. Is the current approach wrong?

**Within each pool, the relative ratings are correct.** When we filter to USSR-only results and fit BayesElo, we are asking: "If model A and model B each played USSR against various opponents in half their games, who wins more as USSR?" The MM solver correctly finds the maximum-likelihood ratings for this question. The relative ordering (v22_ussr > v19_ussr > v14_ussr > ...) is valid.

**The problem is cross-pool comparability.** By anchoring both the USSR pool and the US pool at v12=2001, the implementation implicitly asserts that v12's USSR-strength equals v12's US-strength. This is an unjustified assumption. Looking at the data, v12 happens to be roughly symmetric (its combined Elo is the anchor), but other models are not: v25 has elo_ussr=1869 vs elo_us=1733, a 136-point gap. This gap is real and meaningful, but the absolute values (1869 and 1733) are only comparable to each other **if** the anchor model's true USSR and US strengths happen to be equal.

### 3. The bipartite graph argument in detail

The user argues that each checkpoint is really 2 "players" (one USSR, one US), and these form a bipartite graph where USSR-players only face US-players. This is correct in the following sense:

- In the raw game data, model_A_as_USSR plays against model_B_as_US, and vice versa.
- A match between model_A_USSR and model_B_US is an observation that constrains the *difference* between A's USSR rating and B's US rating.
- A fully joint model would have 2N rating parameters (N models x 2 sides) and a single likelihood function over all games.

In such a bipartite model:
- Only ONE anchor is needed (e.g., v12_USSR = 2001).
- v12_US would be a *free* parameter estimated from data, not forced to 2001.
- The resulting ratings would be directly comparable: you could say "v25_USSR (1850) is stronger than v25_US (1720)" with proper calibration.

### 4. Is the current approach "wrong" or just "limited"?

It is **limited but not catastrophically wrong**. Here is why:

**What it gets right:**
- Relative ordering within USSR pool: correct.
- Relative ordering within US pool: correct.
- Combined Elo: correct (uses all data).
- The per-side ratings are useful for detecting asymmetric models (v24, v25 have large USSR-US gaps).

**What it gets subtly wrong:**
- The *magnitude* of the USSR-US gap for each model is distorted by the anchor assumption. If v12's true USSR-strength is actually 20 Elo higher than its US-strength, then ALL USSR ratings are inflated by ~20 and all US ratings are deflated by ~20 relative to the truth.
- The current CIs are not computed for per-side ratings (the code only computes `bayeselo_ci95` for the combined ratings).
- With only half the games per side, per-side fits have higher variance.

**When it fails:**
- If someone computes `elo_ussr - elo_us` for a model and interprets this as the model's true USSR-US asymmetry, it will be off by a constant bias (the anchor model's unknown asymmetry).
- The autonomous log already uses these numbers directly: "v24peak=1809 (USSR=1855, US=1706)" — the gap of 149 is only correct up to the anchor's unknown bias.

### 5. The correct bipartite formulation

The mathematically correct joint model:

**Parameters:** For N models, define 2N ratings: r_{i,USSR} and r_{i,US} for i = 1..N.

**Likelihood:** For a game where model_i plays USSR and model_j plays US:
```
P(i wins) = sigmoid(r_{i,USSR} - r_{j,US})
```

**Anchor:** Fix exactly one parameter, e.g., r_{anchor,USSR} = 2001.

**Solver:** Same MM/Newton iteration but over 2N parameters. The bipartite structure means each game connects one USSR-node to one US-node. The graph is connected as long as the combined match graph is connected (which round-robin guarantees).

**Result:** All 2N ratings are on a single scale. You can directly compare r_{i,USSR} vs r_{i,US} for any model.

### 6. Sample size considerations

With the current data (8 models, round-robin, 400 games/match = 200/side):
- Combined pool: 28 matchups x 400 games = 11,200 observations for 8 parameters.
- Per-side pool (current): 28 matchups x 200 games = 5,600 observations for 8 parameters.
- Bipartite joint: 28 matchups x 200 x 2 game-types = 11,200 observations for 16 parameters.

The bipartite model uses the same total data but estimates twice as many parameters, so per-parameter precision is comparable to the current per-side fits. No data is wasted.

### 7. Does TrueSkill or WHR handle bipartite structure better?

**TrueSkill** (Microsoft): Designed for team games. Each "team" could be (model, side), making this a 1v1 between team={model_i, USSR} and team={model_j, US}. TrueSkill naturally handles this as each (model, side) pair gets its own mu and sigma. This is equivalent to the bipartite BayesElo formulation above but with Bayesian posterior updates. TrueSkill would work well here but is overkill for a round-robin tournament with known matchups.

**WHR (Whole History Rating):** Designed for time-varying ratings. Treats each player as having a rating that varies over time. Could model (model, side) as separate players. Useful if we want to track how a model's per-side strength changes across training, but unnecessary for a static snapshot tournament.

**BayesElo with 2N nodes** is the simplest correct solution. It requires no new dependencies, no new solver — just changing the input encoding. The existing `bayeselo_fit()` function works unmodified.

### 8. What the minimum fix looks like

The fix is straightforward. Instead of:
```python
ussr_mlist = _ussr_matches(matches)    # model names as players
elos_ussr = bayeselo_fit(ussr_mlist, anchor="v12", anchor_elo=2001)
```

Do:
```python
bipartite_matches = _bipartite_matches(matches)  # players are "v12_USSR", "v12_US", etc.
elos_bipartite = bayeselo_fit(bipartite_matches, anchor="v12_USSR", anchor_elo=2001)
# Then extract: elos_ussr[m] = elos_bipartite[f"{m}_USSR"]
#               elos_us[m]   = elos_bipartite[f"{m}_US"]
```

Where `_bipartite_matches` converts each match into a `MatchResult` with `player_a = f"{m.player_a}_USSR"`, `player_b = f"{m.player_b}_US"` for the first half (where A played USSR), and the reverse for the second half.

This is ~20 lines of code change. The solver, CI computation, and output format all work as-is.

## Conclusions

1. **The user's bipartite-graph argument is mathematically correct.** Each checkpoint is two distinct "players" (one per side), and in the raw game data, USSR-players only face US-players. A proper joint model should have 2N nodes and a single anchor.

2. **The current implementation is not a joint bipartite fit.** It runs three independent BayesElo fits: one combined (ignoring side), one USSR-only, one US-only. Each pool independently anchors v12 at 2001.

3. **The current per-side relative orderings are correct.** Within the USSR pool or within the US pool, the relative ratings are maximum-likelihood estimates and are valid for ranking models by per-side strength.

4. **The current per-side absolute numbers are biased by a shared constant.** The bias equals the unknown asymmetry of the anchor model (v12). If v12's true USSR-strength differs from its US-strength by X Elo, then all USSR ratings are off by +X/2 and all US ratings are off by -X/2 (approximately). This means the USSR-US gap for any model is correct *up to a constant*.

5. **The practical impact is moderate.** For the primary use case (detecting asymmetric models like v24/v25), the relative ordering and approximate gap magnitudes are correct. The bug matters most when comparing absolute numbers across pools (e.g., "v25's USSR Elo is higher than v8's combined Elo").

6. **A bipartite 2N-node BayesElo is the correct and minimal fix.** It requires ~20 lines of code change, no new dependencies, and makes all 2N ratings directly comparable on a single scale.

## Recommendations

1. **Implement bipartite BayesElo with 2N nodes.** Add a `_bipartite_matches()` function that creates `MatchResult` entries with `"{model}_USSR"` and `"{model}_US"` as player names. Feed these to the existing `bayeselo_fit()` with a single anchor (e.g., `v12_USSR=2001`). Extract per-side ratings from the result. This is ~20 lines of change.

2. **Keep the combined Elo as-is.** The combined fit (aggregating both sides) is correct and useful as the primary ranking metric. It answers "which model is strongest overall?" The bipartite fit answers "which model is strongest as USSR?" and "which model is strongest as US?" separately.

3. **Do not anchor v12_US at 2001.** Let it float. The data will determine v12's USS-US asymmetry. The only fixed anchor should be v12_USSR=2001 (or whichever model/side you choose).

4. **Add a "side_gap" field to the output.** For each model, compute `elo_ussr - elo_us` from the bipartite fit. This directly measures the model's side asymmetry on a calibrated scale.

5. **Do not switch to TrueSkill or WHR.** BayesElo with 2N nodes is sufficient, simpler, and already implemented (modulo the input encoding). TrueSkill/WHR add complexity without meaningful benefit for a static round-robin tournament.

6. **Re-run the tournament after the fix.** The relative orderings will likely stay the same, but the absolute per-side numbers and gap magnitudes may shift. This will give a more accurate picture of v24/v25's true asymmetry.

## Open Questions

1. **What is v12's true side asymmetry?** The current data anchors v12 as perfectly symmetric (both sides at 2001). The bipartite fit will reveal whether v12 is actually slightly stronger as USSR or US. This shifts all interpretations of per-side gaps for other models.

2. **Should the anchor be the heuristic instead?** The heuristic player is deterministic and always available. Anchoring `heuristic_USSR` at a fixed value might be more stable across tournament reruns as new models are added. However, heuristic is the weakest player, so it has the least data connectivity — v12 is a better choice for statistical reasons.

3. **How much do the per-side CIs widen in the bipartite model?** With 2N parameters and the same data, individual CIs will be wider. Worth computing to understand how much precision we lose.

4. **Should draws be modeled?** The current solver treats each match as W/L only (draws are implicitly split). BayesElo can incorporate a draw model (elo parameter + draw probability), but with low draw rates (~2-4%), the impact is negligible.
