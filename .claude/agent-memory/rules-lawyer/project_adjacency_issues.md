---
name: adjacency.csv known issues and decisions
description: Confirmed bugs and verified adjacency facts for data/spec/adjacency.csv, including missing inter-region edges
type: project
---

# adjacency.csv Known Issues

## France -- Algeria missing (CRITICAL -- affects legality)
The official GMT Deluxe Edition board shows a direct connection between France (Europe, id=7)
and Algeria (Africa, id=56). This edge is NOT in adjacency.csv.

- **Missing edge:** 7,56  # France -- Algeria
- **Why:** France had colonial Algeria. The board explicitly shows this line as one of three
  Europe-Africa cross-region connections (the others being Spain/Portugal--Morocco and the
  Libya--Tunisia/Algeria MiddleEast-Africa connections).
- **How to apply:** Add `7,56  # France -- Algeria` to adjacency.csv. Update the total count
  from 138 to 139. Any coup/realignment legality check from France or from Algeria depends
  on this edge being present.

## Complete cross-region edge inventory (verified)
All cross-region connections that should be present:
- 7,56   France (Europe) -- Algeria (Africa)              [MISSING -- add this]
- 14,65  Spain/Portugal (Europe) -- Morocco (Africa)      [present]
- 16,35  Turkey (Europe) -- Syria (MiddleEast)            [present]
- 26,72  Egypt (MiddleEast) -- Sudan (Africa)             [present]
- 33,56  Libya (MiddleEast) -- Algeria (Africa)           [present]
- 33,73  Libya (MiddleEast) -- Tunisia (Africa)           [present]

## Verified-absent connections (common misconceptions)
- Libya -- Sudan: NOT adjacent. Egypt connects to Sudan, not Libya.
- Nigeria -- Algeria: NOT adjacent. Saharan States sits between them.
- Cuba -- Dominican Republic: NOT adjacent. Haiti is in between.
- Cuba -- Mexico: NOT adjacent. Cuba connects only to Haiti and USA.
- Angola -- Namibia/Zambia: Those are not separate board spaces; absorbed into SE African States.
- South Africa -- Mozambique: NOT adjacent. Routes go through Botswana, Zimbabwe, or SE African States.

## Starting influence -- resolved uncertainties (Deluxe Edition, ITS)
All UNCERTAIN flags in countries.csv are now resolved:
- Italy US start: 0 (confirmed correct for ITS/Deluxe)
- UK US start: 5 (confirmed Deluxe Edition; original was 4)
- Hungary USSR start: 1 (confirmed)
- Yugoslavia: 0/0 (confirmed)
- Saudi Arabia: 0/0 (confirmed)
- Gulf States: 0/0 (confirmed)
- Pakistan: 0/0 (confirmed)
- Costa Rica stability: 3 (confirmed)
- Panama US start: 1 (confirmed)
- Uruguay stability: 2 (confirmed)

USSR total starting influence = 19:
  Czechoslovakia=3, East Germany=3, Finland=1, France=1, Hungary=1, Poland=4,
  Romania=3, North Korea=3, Syria=1, Iraq=1, Vietnam=1

US total starting influence = 20:
  Canada=2, UK=5, West Germany=4, Turkey=1, Israel=1, Iran=1, Japan=1,
  South Korea=1, Philippines=1, Panama=1, South Africa=1
