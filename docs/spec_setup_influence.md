# Spec: Setup Influence Placement Phase

## Context

Per TS Deluxe Edition rules §3.0:

**USSR places 15 total influence:**
- Fixed: 1 Syria, 1 Iraq, 3 North Korea, 3 East Germany, 1 Finland = 9
- Free: **6 anywhere in Eastern Europe** (player's choice, after seeing hand)

**US places 25 total influence:**
- Fixed: 2 Canada, 1 Iran, 1 Israel, 1 Japan, 4 Australia, 1 Philippines,
  1 South Korea, 1 Panama, 1 South Africa, 5 UK = 18
- Free: **7 anywhere in Western Europe** (player's choice, after seeing hand)

Players see their opening hand BEFORE placing influence (§3.1).

**Currently:** The engine skips free placement entirely. All games start from
identical board positions, missing a critical strategic dimension.

## Valid countries for free placement

**Eastern Europe** (USSR free placement targets):
- Czechoslovakia (3), East Germany (5), Hungary (9), Poland (12),
  Romania (13), Yugoslavia (19), Bulgaria (83)
- Austria (0) and Finland (6) are geographically Eastern but the standard
  TS community consensus is they are NOT valid for USSR setup placement.
- Matches existing `kEasternBlocIds` in step.cpp.

**Western Europe** (US free placement targets):
- Benelux (1), Canada (2), Denmark (4), France (7), Greece (8),
  Italy (10), Norway (11), Spain/Portugal (14), Sweden (15),
  Turkey (16), UK (17), West Germany (18)
- Matches existing `kWesternEuropeIds` in step.cpp.

## Missing country: Australia

The rules list "4 in Australia" as fixed US influence. Our countries.csv
has no Australia entry. Australia is adjacent to SE Asian countries on the
board. Need to add:
- Australia, SoutheastAsia (or a special anchor), stability=4, non-BG,
  us_start=4, ussr_start=0
- Add adjacency: Australia ↔ Indonesia (76), possibly others

**Defer Australia to a separate change** — it requires adjacency.csv and
country ID assignment. The setup phase can work without it.

## Bid/handicap influence (separate from free placement)

Per the example game in the rules (p.14): "These [bid] points may only be
placed in countries eligible for US Influence during the game setup." This
means bid influence can go to ANY country that has fixed US starting
influence (Iran, Israel, Japan, etc.) OR Western Europe — wider than the
free 7 which is Western Europe only.

This is modeled separately via `handicap_ussr` / `handicap_us` in
PublicState and is orthogonal to the free placement phase.

## Implementation plan

### Change 1: Add setup phase to game loop

In `game_state.cpp::reset_game_impl()`, after setting fixed influence and
dealing hands, set `phase = GamePhase::SetupInfluence` instead of
`GamePhase::Headline`.

Add new `GamePhase::SetupInfluence` enum value (or reuse `Setup`).

### Change 2: Setup influence as action decisions

Model setup placement as a sequence of influence placement actions:
- USSR places 6 points (one at a time or all at once)
- US places 7 points (one at a time or all at once)

Simplest encoding: use existing `ActionMode::PlaceInfluence` with a
constraint that target must be in the valid region. Each action places
1 influence point. USSR gets 6 actions, US gets 7 actions.

### Change 3: Legal action generation for setup

In the legal action generator, when `phase == GamePhase::SetupInfluence`:
- If phasing side is USSR: return all Eastern Europe country IDs
- If phasing side is US: return all Western Europe country IDs
- Card ID can be 0 or a sentinel (no card played during setup)

### Change 4: Game loop integration

In `play_turn()` / batched MCTS `advance_game()`:
- Before turn 1 headline, run setup phase
- USSR does 6 placement actions, then US does 7

### Change 5: Heuristic policy for setup

Add a `choose_setup_action()` to heuristic policy:
- USSR default: Poland 4, East Germany 1 (total=4), Yugoslavia 1
- US default: West Germany 4, Italy 2, France 1
- With some randomization for diversity

### Change 6: Learned policy for setup

The model already has a country target head. Setup placement is just
a special case of PlaceInfluence where the legal targets are restricted.
No model architecture change needed — just legal action masking.

## Build sequence

1. Add Eastern/Western Europe constants to a shared header
2. Add setup phase to game state + game loop (non-batched first)
3. Add heuristic policy for setup
4. Test with non-batched game loop
5. Add setup phase to batched MCTS
6. Collect new data with setup phase active
7. Retrain — model learns opening theory from data

## Risk

This changes the game state for ALL self-play and benchmarks.
Historical comparisons become invalid (different starting positions).
The first few generations after this change may have lower win rates
as the model learns setup placement, but long-term this is strictly
better — it adds a strategic dimension that was missing.
