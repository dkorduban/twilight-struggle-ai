---
name: Regional scoring VP tables and rules
description: Exact Presence/Domination/Control VP amounts for all 7 regions, control condition, SE Asia special format, Europe auto-win, China Card bonus, VP sign convention
type: reference
---

# Twilight Struggle Regional Scoring Rules (Deluxe Edition / ITS)

## Control condition
`own_influence >= opponent_influence + stability`
The >= form is correct. > form is wrong.

## VP sign convention
Positive VP = US lead. Scoring VPs are signed deltas: +N means US gains N, -N means USSR gains N.

## Tier determination (standard regions)
- CONTROL: own side controls ALL battleground countries in region
- DOMINATION: controls more BGs than opponent AND controls at least 1 non-battleground country
- PRESENCE: controls at least 1 country in the region (BG or non-BG)
- NONE: controls 0 countries

Winner (higher tier) scores; loser scores nothing.
Tie at same tier = 0 VP, no one scores.

## VP tables

### Europe (7 BGs: East Germany, France, Italy, Poland, Turkey, UK, West Germany)
| Tier       | US VP | USSR VP |
|------------|-------|---------|
| Presence   |   +1  |    -1   |
| Domination |   +3  |    -3   |
| Control    | AUTOMATIC WIN | AUTOMATIC WIN |

Europe Control is the only region where Control = instant game win (not just VP).

### Asia (5 BGs: India, Japan, North Korea, Pakistan, South Korea)
| Tier       | US VP | USSR VP |
|------------|-------|---------|
| Presence   |   +3  |    -3   |
| Domination |   +7  |    -7   |
| Control    |   +9  |    -9   |

China Card bonus: +1 VP to the side holding the China Card when Asia Scoring resolves. Unconditional (does not depend on who won the scoring). Stacks on top of main scoring.

SE Asia countries (Burma, Indonesia/Malaysia, Laos/Cambodia, Philippines, Thailand, Vietnam) do NOT count for Asia Scoring.

### Middle East (6 BGs: Egypt, Iran, Iraq, Israel, Libya, Saudi Arabia)
| Tier       | US VP | USSR VP |
|------------|-------|---------|
| Presence   |   +3  |    -3   |
| Domination |   +5  |    -5   |
| Control    |   +7  |    -7   |

### Central America (2 BGs: Cuba, Panama)
| Tier       | US VP | USSR VP |
|------------|-------|---------|
| Presence   |   +1  |    -1   |
| Domination |   +3  |    -3   |
| Control    |   +5  |    -5   |

### South America (4 BGs: Argentina, Brazil, Chile, Venezuela)
| Tier       | US VP | USSR VP |
|------------|-------|---------|
| Presence   |   +2  |    -2   |
| Domination |   +4  |    -4   |
| Control    |   +6  |    -6   |

### Africa (6 BGs: Algeria, Angola, Ethiopia, Morocco, Nigeria, South Africa)
| Tier       | US VP | USSR VP |
|------------|-------|---------|
| Presence   |   +1  |    -1   |
| Domination |   +4  |    -4   |
| Control    |   +6  |    -6   |

Congo/Zaire is NOT a battleground.
Libya is Middle East only; does not appear in Africa scoring.

### Southeast Asia -- SPECIAL FORMAT (not Presence/Domination/Control)
1 VP per controlled country. Thailand counts as 2 VP (only exception).
Both sides can score simultaneously (unique to SE Asia).

Countries: Burma (1 VP), Indonesia/Malaysia (1 VP), Laos/Cambodia (1 VP),
           Philippines (1 VP), Thailand (2 VP), Vietnam (1 VP).
Maximum one-side total: 7 VP.

## No "+1 per extra BG" bonus
There is no additional bonus VP for controlling more battlegrounds than opponent beyond the tier VP amounts. The only bonus mechanic is the Asia China Card +1 VP.

## Open ambiguity
1. Domination non-BG condition: "controls" vs "has any influence in" a non-BG country. ITS standard: must CONTROL (own >= opp + stab) at least 1 non-BG. Verify.
2. Africa Congo/Zaire battleground status: marked non-BG in countries.csv; confirm with physical board.
3. SE Asia Philippines: 1 VP despite being a battleground. Thailand-only double-VP. Confirm Thailand exception is not extended to other BGs.
