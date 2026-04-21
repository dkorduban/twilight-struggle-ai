# Twilight Struggle Scoring Rules (§10)

## 10.0 SCORING AND VICTORY

The object of the game is to score Victory Points (VPs). Regional Victory Points are scored through geographic Influence over the six Regions. VPs can also be received through the play of certain Events. Each region has its own 'scoring card'. Playing a scoring card causes Victory Points to be scored, based on how much influence each superpower has in that region at the time the card is played.

**PLAY NOTE:** Trying to play scoring cards to coincide with your superpower's peak influence in a region is often a crucial factor in winning the game.

## 10.1 SCORING

### 10.1.1 SCORING TIER DEFINITIONS

The following terms are used during Regional Scoring:

**Presence:** A superpower has Presence in a Region if it Controls at least one country in that Region.

**Domination:** A superpower achieves Domination of a Region if it Controls more countries in that Region than its opponent, and it Controls more Battleground countries in that Region than its opponent. A superpower must Control at least one non-Battleground and one Battleground country in a Region in order to achieve Domination of that Region.

**Control:** A superpower has Control of a Region if it Controls more countries in that Region than its opponent, and Controls all of the Battleground countries in that Region.

### 10.1.2 REGIONAL SCORING FORMULA

Players score additional points during Regional Scoring, as follows:

- **+1 VP per country** they Control in the scoring region that is adjacent to the enemy superpower
- **+1 VP per Battleground country** that they Control in the scoring region.
- **Tier bonuses** (region-specific; VP table transcribed from the TS Deluxe rulebook scoring panel):

| Region         | Presence | Domination | Control  |
|----------------|----------|------------|----------|
| Europe         | 3        | 7          | GAME WIN |
| Asia           | 3        | 7          | 9        |
| Middle East    | 3        | 5          | 7        |
| Central America| 1        | 3          | 5        |
| South America  | 2        | 5          | 6        |
| Africa         | 1        | 4          | 6        |

**Authoritative source:** `cpp/tscore/scoring.cpp` `kRegionVp` array. A prior version of this doc showed Europe as `1/3/GAME WIN` with a bogus "verified empirically" note — that was an LLM-authored transcription error that silently contradicted the engine for weeks. If you change this table, also edit `scoring.cpp` in the same commit.

Victory points are then cumulated for both players, and the net difference between the two scores is marked on the Victory Point Track.

**EXAMPLE:** The USSR plays the Central American Scoring card. The USSR controls Cuba, Haiti and the Dominican Republic. The United States controls Guatemala, and has 1 point of influence in Panama. The USSR player would therefore get points for Dominating Central America (3 VPs) + 1 VP for control of a battleground country (Cuba). +1 VP for Cuba's being adjacent to your opponent's home nation for a total of 5 VPs. The United States would receive 1 VP for presence in Central America since he controls Guatemala. Since the United States only has 1 Influence point in Panama, he does not control it, and therefore controls no battleground countries. That is why the USSR player scores Dominance points. He controls more battleground countries (Cuba) and more countries overall. He also meets the "at least one non-battleground country" test through control of either Haiti or the Dominican Republic. Having calculated relative victory points, 5 VPs for the USSR, and 1 VP for the US, you subtract the US VPs from the Soviets, and move the VP point track a net 4 spaces toward Soviet victory.

### 10.1.3 EVENT-BASED SCORING

Playing certain card Events may result in Victory Points being scored.

### 10.1.4 MILITARY OPERATIONS PENALTY

Victory Points may be scored due to your opponent's failure to perform the number of required military operations during the turn (8.2).

### 10.1.5 SCORING CARD HOLDING RESTRICTIONS

A player may not be forced to Hold a Scoring Card through the effects of an Event(s).

## 10.2 THE VICTORY POINT TRACK

### 10.2.1 TRACK RANGE AND STARTING POSITION

The Victory Point Track shows a range of scoring possibilities from US-20 (US automatic victory) to USSR-20 (USSR automatic victory). At the start of the game, place the VP marker in the center of the chart, on the box marked At Start. This box represents zero points, or total equilibrium of the two sides. This box should be counted as a space when players' scores are adjusted.

**EXAMPLE:** If the scoring marker is on the USSR-1 box, and the US player scores 2 VPs, the marker should move 2 spaces to the US-1 box.

### 10.2.2 GAINING VICTORY POINTS

Wherever a card states that the player 'gains' a Victory Point, this means that the VP marker is moved that many spaces in that player's favor, i.e., if the VP marker is on the 0 space (US winning) and the USSR player gains 2 VP, the marker is moved to the 8 space on the VP track.

### 10.2.3 SIMULTANEOUS SCORING BY BOTH PLAYERS

If both players earn Victory Points from the same card or Event play, apply only the difference in Victory Points awarded.

## 10.3 VICTORY

### 10.3.1 AUTOMATIC VICTORY

There are several ways to achieve an automatic victory in Twilight Struggle:

- **20 VP Threshold:** The instant one player reaches a score of 20 VP, the game is over and that player is the winner. **NOTE:** All VP awards (for both players) that are scored during an event or scoring card must be applied prior to determining automatic victory.

- **Europe Control:** If either side Controls Europe, that side wins when the Europe Scoring card is played.

- **Nuclear War:** A player may also win the instant his opponent causes the DEFCON level to reach 1.

### 10.3.2 END GAME VICTORY (FINAL SCORING)

If neither side has achieved victory of any kind by the end of turn 10, then every Region is scored as if its regional scoring card had just been played (these new VPs are added to the current score). **Southeast Asia is not scored separately: it is included in the Asia scoring calculations.** Every Region's score must be calculated before final victory is determined. Reaching 20 VPs does not result in Automatic Victory during scoring at the end of turn 10; however, Control of Europe does grant automatic victory to the controlling player, regardless of scoring elsewhere.

Once all regions have been scored, victory goes to the player who has accrued most VPs. If the VP marker is on a positive number, the US wins; if the VP marker is on a negative number, the USSR wins. If the VP marker is on zero, the game ends in a draw.

## ADJACENCY BONUS DETAILS

The adjacency bonus applies to **all controlled countries** (BG and non-BG) adjacent to the enemy superpower:
- +1 VP per country (BG **or** non-BG) the scoring player controls that is adjacent to the enemy superpower
- This is the literal reading of §10.1.2: "+ VP per country they Control in the scoring region that is adjacent to the enemy superpower"
- The rulebook makes no BG-only restriction for the adjacency bonus; the BG-only restriction is only for the separate BG bonus

**NOTE:** A previous version of this doc erroneously stated adjacency bonus was BG-only.
That claim was wrong — see §10.1.2 text above which says "country", not "Battleground country".
The rule says: "+VP per **Battleground country** they Control" (BG bonus) AND
"+VP per **country** they Control adjacent to enemy superpower" (adjacency bonus — any country).

## CHINA CARD BONUS IN ASIA SCORING

When Asia is scored (including at end-game final scoring), the holder of the China Card receives +1 VP. This is separate from the card's operations bonus:
- **Scoring bonus:** +1 VP to whoever holds the China Card when Asia is scored
- **Operations bonus:** +1 ops when the card is played and all ops are spent in Asia

Both bonuses are independent. The scoring bonus is implemented in scoring.py (china_card_vp_delta) and applied in apply_scoring_card / score_asia_final.

## SOUTHEAST ASIA SPECIAL RULE

### 7.2 SOUTHEAST ASIA SCORING CARD

The Southeast Asia Scoring card has an **asterisk following the Event title, and is the only scoring card removed after play.** This means when the Southeast Asia Scoring card is played as an event, it is permanently removed from the game and not shuffled back into the deck.

### 10.3.2 SOUTHEAST ASIA IN FINAL SCORING

During final scoring at the end of turn 10, Southeast Asia is **not scored separately**: it is included in the Asia scoring calculations. This means a single Asia scoring calculation at the end of the game covers both Asia and Southeast Asia as one region.

## FORMOSAN RESOLUTION EVENT RULES

Card 35: Formosan Resolution (US, 2 ops, Early War, starred).

Effect: Taiwan is treated as a battleground country for Asia scoring purposes while US controls it. Cancelled if USSR plays the China Card for its event.

**Implementation status:** Taiwan is not yet in countries.csv as a board country. The `formosan_active` flag is set when the card fires, but scoring.py does not yet use it. Adding Taiwan as a country (stability=3, SoutheastAsia, non-BG by default) is required to fully implement this.

## SHUTTLE DIPLOMACY (Historical Reference)

Shuttle Diplomacy (1973) was personalized diplomacy using advances in transportation and communications, a hallmark of Henry Kissinger's term as Secretary of State. It was utilized to broker a cease-fire between Israel and Egypt after the Yom Kippur War. By acting as personal go-between for the Egyptians and Israelis, Kissinger maintained the pivotal role in discussions and minimized Soviet influence over the negotiation process.

*Note: The specific game effects of Shuttle Diplomacy on scoring should be verified in the card text itself, as the rulebook contains historical background but game mechanics are found on individual event cards.*

## SCORING SUMMARY CHECKLIST

For each regional scoring card played:

1. Determine which player has Presence (≥1 country controlled)
2. Check for Control (all BGs + more countries) → region-specific VP (see table above)
3. If no Control, check for Domination (more BGs + more countries, at least 1 BG + 1 non-BG) → region-specific VP
4. If no Domination, award Presence → region-specific VP
5. Add +1 VP per controlled country adjacent to enemy superpower
6. Add +1 VP per controlled battleground country
7. Calculate net VP difference and move VP marker
8. At end-game, score all regions (including Southeast Asia within Asia scoring)
