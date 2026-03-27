---
name: Superpower adjacency and influence/coup legality
description: "Adjacent to a Superpower" means either superpower for both players -- Cuba accessible to USSR, North Korea accessible to US from game start
type: reference
---

# Superpower Adjacency and Influence/Coup Accessibility

## Rule (GMT Deluxe Edition, section 4.1)

> "A player may place Influence markers in any country that already contains one or more of their Influence markers, or in any country that is adjacent to a country that already contains one or more of their Influence markers. **Superpowers are considered countries for this purpose.**"

The rule says "adjacent to a Superpower" -- NOT "adjacent to your own Superpower."
Both superpower nodes (USA id=81, USSR id=82) are valid adjacency anchors for **both** players.

## Confirmed rulings

- USSR can place influence in / coup Cuba (id=36) from turn 1 with zero prior foothold. Cuba is adjacent to USA (id=81).
- US can place influence in / coup North Korea (id=23) from turn 1 with zero prior foothold. NK is adjacent to USSR (id=82).
- The coup rule uses the same accessibility test as influence placement.
- Superpower nodes are adjacency anchors only. Players cannot place influence ON them or coup IN them.

## Legality function formula

```
accessible(player, country) = (
    country has player_influence > 0
    OR any neighbor of country has player_influence > 0
    OR country is adjacent to USA node (id=81)   -- both players
    OR country is adjacent to USSR node (id=82)  -- both players
)
```

## Confirmed in adjacency.csv

- 36,81  # Cuba -- USA  (line 92)
- 23,82  # North Korea -- USSR  (line 71)

Full USA adjacency list (id=81): Canada(2), Cuba(36), Japan(22), Mexico(42), Philippines(78), South Korea(25)
Full USSR adjacency list (id=82): Afghanistan(20), Finland(6), North Korea(23), Poland(12), Romania(13)

## Important edge case

Region-restriction card text ("place influence only in Europe") overrides superpower adjacency connectivity.
Superpower adjacency relaxes the connectivity requirement only; it never overrides explicit card-text region restrictions.

## Recommended regression test IDs

R-ADJ-01 through R-ADJ-10 -- see rules-lawyer answer 2026-03-26.
Key: accessible(USSR, Cuba)=True, accessible(US, NK)=True, superpower nodes themselves are illegal targets.
