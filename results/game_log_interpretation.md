# How to Read the Heuristic Game Trace

The trace in `sample_heuristic_game.txt` records every **decision point** the engine
asks a player to make. Each line represents one atomic action the policy chose.

## Line format

```
AR{n} {side} {card_name}  {mode}  -> {targets}  [VP/DEFCON changes]
```

## Understanding the fields

### Card + Mode = what the player chose to do

- **Event**: Play the card for its event text effect
- **Influence**: Play the card for operations points, placing influence on the map
- **Coup**: Play the card for operations points, attempting a coup in a target country
- **Realignment**: Play the card for operations points, attempting realignment rolls
- **Space Race**: Discard the card to advance on the space race track
- **Discard**: Forced discard (e.g., from Bear Trap, Quagmire, or held-event resolution)

### Targets = where influence was placed

The `targets` list shows **countries that received influence** from the operations
points of the card play. This is straightforward for Influence mode but can be
confusing for Events.

## Key interpretation rules

### 1. Event cards also generate ops for the opponent

When USSR plays a US-associated card (or vice versa), **both** the event AND the ops
happen. The trace records the **player's ops placement choice** in the targets field,
not the event effect. The event effect happens automatically in the engine.

**Example from the game:**
```
AR1 USSR East European Unrest    Event    -> Nicaragua  [DEFCON 5->4]
```
- Card 28 (East European Unrest) is a **US event** (removes USSR influence from E.Europe)
- USSR played it — so the event fires (removing USSR influence) AND USSR gets to use
  the ops points
- The targets show where USSR placed influence with the ops (Nicaragua)
- The DEFCON drop is from the ops being used as influence in a battleground
- **Read as**: "USSR played East European Unrest. The US event fired (removing USSR
  influence from Eastern Europe). Then USSR used the 3 ops to place influence in
  Nicaragua."

### 2. Scoring cards show influence placement, not the scoring

**Example:**
```
AR6 USSR SE Asia Scoring         Influence  -> E.Germany, Mexico, Honduras
```
- This does NOT mean "SE Asia Scoring placed influence in E.Germany"
- Scoring cards are 0-ops cards. The trace shows the **next action** after scoring
  resolved, which happens to be an influence placement recorded under the same AR
- **Read as**: "USSR played SE Asia Scoring (scored the region), then placed influence
  in E.Germany, Mexico, Honduras with a subsequent card/ops"

Actually, looking more carefully: scoring cards have 0 ops, so this is likely a trace
artifact where the scoring card and the following ops action share the same AR number.

### 3. Multi-step events show only the final ops allocation

Cards like De-Stalinization, Puppet Governments, or COMECON involve multiple engine
steps (choose countries, place/remove influence). The trace captures only the
**player's top-level action** — the card choice, mode, and the resulting country
targets.

**Example:**
```
AR3 USSR COMECON                 Event    -> Indonesia  [DEFCON 4->3]
```
- COMECON's event places 1 influence in each of 4 non-US-controlled E.European countries
- But the trace shows "Indonesia" as the target — this is likely the ops allocation
  (COMECON is a USSR event played by USSR, so the event fires AND the ops are available)
- The DEFCON change confirms ops were used (battleground coup or similar)

### 4. Headline phase

```
Headline: USSR=Fidel  US=Suez Crisis
```
- Both sides simultaneously reveal their headline card
- Events resolve in order (USSR first if same priority)
- No ops are generated during headline — pure event effects

### 5. VP is positive = USSR-favored, negative = US-favored

VP is always from USSR's perspective:
- `VP=+20` means USSR is 20 VP ahead
- `VP=-5` means US is 5 VP ahead
- USSR instant-wins at VP >= +20, US instant-wins at VP <= -20

### 6. DEFCON changes

- DEFCON starts at 5 (peace) and can drop to 1 (nuclear war = instant loss)
- Coups in battleground countries lower DEFCON by 1
- Some events raise or lower DEFCON
- DEFCON is reset to minimum of (current, 5) at the start of each turn... actually
  it raises by 1 per turn (max 5) at turn start

## Common confusing patterns

| What you see | What actually happened |
|---|---|
| `{Event card} Influence -> {countries}` | Card was played for ops, not event |
| `{Opponent's event} Event -> {countries}` | Event fired (opponent benefits), then player placed ops |
| `{Scoring card} Influence -> {countries}` | Scoring resolved, then next ops action in same AR |
| `[DEFCON 3->2]` on an Influence action | Coup in a battleground country, not influence |
| No target listed for Event | Pure event with no ops allocation needed |

## Limitations of this trace format

1. **Event effects are implicit** — you only see the ops placement, not what the event
   did to the board. To see event effects, you'd need the full pub_snapshot diffs.
2. **Country names may not be 100% accurate** — the mapping from country IDs to names
   is approximate and may have off-by-one errors for some regions.
3. **Sub-decisions within events** (e.g., which countries to target with Realignment
   rolls) are not shown separately — only the top-level card+mode+targets.
4. **China Card** usage is recorded as a normal card play but the "face down" status
   isn't shown explicitly.
