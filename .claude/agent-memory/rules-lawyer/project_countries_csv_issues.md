---
name: countries.csv known issues and decisions
description: Confirmed bugs, FIXMEs, and data decisions in data/spec/countries.csv that affect scoring and engine correctness
type: project
---

# countries.csv Known Issues

## Libya duplicate (CRITICAL -- affects scoring)
countries.csv has Libya in BOTH MiddleEast (id=33) AND Africa (id=64).
Libya is a Middle East country ONLY. The Africa entry (id=64) is wrong.
The CSV itself flags this as FIXME with a note to reassign id=64.
- Middle East scoring: use id=33 (Libya, MiddleEast, stab=2, BG=true). Correct.
- Africa scoring: id=64 must NOT be Libya. The comment suggests reassigning to Ivory Coast or another country. Resolve before implementing scoring.
- **Why:** Physical TS board -- Libya is geographically/thematically Middle East. Africa has no Libya country space.
- **How to apply:** Scoring function must treat Africa battleground list as: Algeria, Angola, Ethiopia, Morocco, Nigeria, South Africa (6 BGs). Do not include any Libya entry in Africa.

## Bulgaria late addition (id=83)
Bulgaria was omitted from the Europe id block (0-19) and added at id=83.
It is a valid Europe non-battleground country (stab=3, adjacent to Romania/Yugoslavia/Turkey/Greece).
- **CRITICAL BUG:** Bulgaria USSR start influence is 0 in the CSV but should be 3.
- **How to apply:** Europe scoring must include id=83 in the Europe country set. Any loop over "Europe countries" that stops at id=19 will miss Bulgaria. Set ussr_start_influence=3.

## Thailand double-VP in SE Asia Scoring
Thailand (id=79) has is_battleground=true. This correctly governs Coup/DEFCON rules.
The 2 VP value in Southeast Asia Scoring comes from the card text, NOT from the battleground flag.
- **How to apply:** SE Asia scoring function must hard-code Thailand = 2 VP. Do not derive double-VP from is_battleground=true, or it would incorrectly apply to Philippines and Vietnam (also battlegrounds).

## Superpower homeland anchors (ids 81=USA, 82=USSR)
These are adjacency-only entries with region=Europe (arbitrary). They must be excluded from all scoring, coup, realignment, and influence placement logic.
- **How to apply:** Scoring functions should filter by country_id < 81, or explicitly exclude ids 81 and 82.

## CONFIRMED SETUP BUGS (verified 2026-03-26 against Deluxe Edition rules)

### Iraq USSR start influence: 1 (WRONG) -- should be 3
Iraq (id=29) is MiddleEast, stability=3, battleground=true. USSR starts with 3 influence, not 1.
- **Why:** The CSV likely carried over a transcription error. Iraq USSR=3 is a well-known setup value.
- **How to apply:** Set iraq.ussr_start_influence=3. Affects all ME opening legality and ME scoring from turn 1.

### Yugoslavia USSR start influence: 0 (WRONG) -- should be 1
Yugoslavia (id=19) is Europe, stability=3, non-battleground. USSR starts with 1 influence.
- **Why:** Missed in initial transcription. Yugoslavia borders Italy, Austria, Greece, Bulgaria, Romania, Hungary.
- **How to apply:** Set yugoslavia.ussr_start_influence=1. Affects Europe connectivity and early-game coups.

### Australia: MISSING ENTIRELY
Australia does not exist in the CSV. It is a Deluxe Edition country (not in original printing).
- Region: Asia, stability=4, is_battleground=false, us_start_influence=4, ussr_start_influence=0
- Adjacent to: Indonesia/Malaysia (and possibly Philippines -- verify against physical board)
- **Why:** Deluxe Edition added Australia. It is adjacent to Indonesia/Malaysia (SE Asia battleground), making it a significant US foothold.
- **How to apply:** Add Australia to CSV with a new id (suggest id=84 or reassign id=64 after Libya fix). Add adjacency entry.

### Taiwan: MISSING ENTIRELY
Taiwan does not exist in the CSV.
- Region: Asia, stability=3, is_battleground=false, us_start_influence=1, ussr_start_influence=0
- Adjacent to: Japan and Philippines (verify South Korea adjacency against physical board)
- **Why:** Missed in initial population.
- **How to apply:** Add Taiwan to CSV. Add adjacency entry.

## Setup values CONFIRMED CORRECT (previously uncertain, now resolved)
- Japan US=1 (not 4): Japan starts with US 1. The stab=4 may have caused confusion.
- South Africa US=1: Correct.
- Panama US=1: Correct.
- Hungary USSR=1: Correct.
- UK US=5: Correct for Deluxe Ed (original was 4).

## Setup uncertainties still open
- Italy US start influence: 0 in CSV. Most likely correct. Verify against physical board.
- Greece: 0/0 in CSV. No contradicting evidence. Low priority.
- Benelux: 0/0 in CSV. No contradicting evidence. Low priority.
- Saudi Arabia: 0/0 in CSV. Flagged UNCERTAIN. Verify.
- Costa Rica stability: 3 in CSV. Flagged UNCERTAIN.
- Australia adjacency: confirmed adjacent to Indonesia/Malaysia; Philippines connection uncertain.
- Taiwan adjacency: adjacent to Japan and Philippines; South Korea adjacency uncertain.
