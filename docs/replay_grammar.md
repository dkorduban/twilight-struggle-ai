# Twilight Struggle Replay Grammar

**Status:** Draft – to be validated against actual replay logs.

This document specifies the expected format for Twilight Struggle replay log files
and the normalized event grammar produced by the parser.

---

## 1. Source log format

Twilight Struggle online servers (e.g., ACTS/Wargame Room) produce turn-by-turn
text logs.  The exact format varies by platform.  This section documents the
subset we target first.

### 1.1 File structure

```
GAME_ID: <id>
PLAYERS: <ussr_player> vs <us_player>
DATE: <YYYY-MM-DD>
<turn-block>*
FINAL SCORE: ...
```

### 1.2 Turn block

```
--- TURN <n> ---
  HEADLINE:
    <ussr_player> plays <card>
    <us_player> plays <card>
  AR1:
    <phasing_player> plays <card> [for ops | event | space]
    ...
  AR2: ...
  ...
  END OF TURN <n>
```

### 1.3 Card play line patterns

The grammar below uses regex-like notation.  `<CARD>` matches a canonical card
name (see `data/spec/cards.csv`).  `<COUNTRY>` matches a canonical country name.

```
# Play for ops
<player> plays <CARD> for ops

# Play event
<player> plays <CARD> (event)

# Headline
<player> headlines <CARD>

# Space race
<player> plays <CARD> for space

# Coup
<player> coups <COUNTRY> with <N> ops  ->  roll: <D> -> result: +<N> / -<N>

# Realignment
<player> realigns <COUNTRY>  ->  roll: <D> vs <D>  ->  result: ...

# Influence
<player> places <N> influence in <COUNTRY> [(<CARD>)]
<player> removes <N> influence from <COUNTRY>

# Forced discard
<player> is forced to discard <CARD>

# Reveal hand
<player>'s hand is revealed: <CARD>, <CARD>, ...

# Transfer / give card
<player> passes <CARD> to <opponent>

# Reshuffle
Discard pile reshuffled into draw pile

# End of turn held cards
<player> holds into next turn: <CARD> [, <CARD>]*
```

---

## 2. Normalized event grammar

Each line in a replay is parsed into a `ReplayEvent` (see `python/tsrl/schemas.py`).

### 2.1 Event kinds

| EventKind | Source pattern | Notes |
|-----------|---------------|-------|
| `GAME_START` | File header | turn=0, ar=0 |
| `TURN_START` | `--- TURN N ---` | |
| `HEADLINE_PHASE_START` | `HEADLINE:` | |
| `ACTION_ROUND_START` | `ARN:` | |
| `TURN_END` | `END OF TURN N` | |
| `GAME_END` | `FINAL SCORE:` | |
| `HEADLINE` | `<player> headlines <CARD>` | |
| `PLAY` | `<player> plays <CARD> ...` | card_id set |
| `FORCED_DISCARD` | `forced to discard <CARD>` | |
| `REVEAL_HAND` | `hand is revealed: ...` | aux_card_ids |
| `TRANSFER` | `passes <CARD> to ...` | |
| `DRAW` | implicit at turn start / reshuffle | hand_size reconstructed |
| `DISCARD` | when card goes to discard | |
| `REMOVE` | starred event resolves | |
| `RESHUFFLE` | `Discard pile reshuffled` | |
| `END_TURN_HELD` | `holds into next turn: ...` | aux_card_ids |
| `COUP` | `coups <COUNTRY>` | country_id, amount=net |
| `REALIGN` | `realigns <COUNTRY>` | |
| `PLACE_INFLUENCE` | `places N influence in <COUNTRY>` | |
| `REMOVE_INFLUENCE` | `removes N influence from <COUNTRY>` | |
| `SPACE_RACE` | `plays <CARD> for space` | |
| `SCORING` | scoring card played | |
| `DEFCON_CHANGE` | DEFCON marker moves | amount = new_value |
| `VP_CHANGE` | VP marker moves | amount = delta (+ = USSR) |
| `MILOPS_CHANGE` | mil ops track moves | |
| `CHINA_CARD_PASS` | China Card passed | phasing = new holder |
| `UNKNOWN` | no pattern matched | raw_line preserved |

### 2.2 Unknown line handling

Lines that do not match any known pattern **must not be silently dropped**.
They are emitted as `UNKNOWN` events with `raw_line` preserved.  The parser
tracks `unknown_line_count` and `line_parse_coverage` per game.

---

## 3. Hand knowledge derivation rules

The `HandKnowledge` reducer updates the support mask on each event:

### 3.1 `known_in_hand` additions
- After `DRAW`: add drawn cards if visible
- After `REVEAL_HAND`: add all revealed cards to `known_in_hand`
- After `END_TURN_HELD`: add held cards
- After `TRANSFER` (receiving): add transferred card

### 3.2 `known_not_in_hand` additions
- After `PLAY` / `HEADLINE`: card leaves hand
- After `FORCED_DISCARD`: card leaves hand
- After `DISCARD`: card goes to discard (not in hand)
- After `REMOVE`: card removed from game
- After `TRANSFER` (sending): card leaves hand

### 3.3 `possible_hidden` (support mask) maintenance
- Initialized to all cards not in `removed` and not in `known_not_in_hand`
- On each `known_not_in_hand` addition: remove from `possible_hidden`
- On `RESHUFFLE`: `possible_hidden` is recomputed from scratch
- **Invariant**: no card actually in the actor's hand may ever appear in
  `known_not_in_hand` (false_exclusion_rate == 0)

### 3.4 Hand size accounting
- At turn start: hand_size = HAND_SIZE_EARLY (turns 1-3) or HAND_SIZE_LATE (turns 4-10)
- China Card does NOT count toward hand_size
- Each PLAY / HEADLINE decrements hand_size
- Each DRAW increments hand_size
- Each FORCED_DISCARD decrements hand_size

---

## 4. Parser correctness requirements

- `line_parse_coverage` ≥ 95% on golden corpus before proceeding
- `unknown_line_count` tracked per game
- All events must be emitted in order; no reordering
- `state_hash` must be deterministic: same replay → same hash
- Hand size must balance to zero at end of each turn

---

## 5. Golden corpus

See `data/raw_logs/` for curated regression games.

Each golden log must have an associated expected output in
`data/raw_logs/<game_id>_expected.json` containing:
- Final VP
- Final DEFCON
- State hash at turn-end for each turn
- Card counts per era

---

## 6. Open questions

- [ ] Exact format variation between ACTS and Wargame Room logs
- [ ] How are simultaneous events (headline resolution) ordered?
- [ ] Format for die-roll lines (coup/realignment outcomes)
- [ ] How is the "Held scoring card" warning logged, if at all?
- [ ] China Card play line format (it has no event text)
