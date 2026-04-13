# Golden Replay Fixtures

This directory holds JSON fixtures for deterministic C++ replay and event-gap
regression tests.

## Format

Each fixture is a single JSON object:

```json
{
  "name": "gap003_space_suppression",
  "gap_id": "GAP-003",
  "description": "Spacing an opponent card must not fire the opponent event",
  "setup": {
    "turn": 1,
    "defcon": 5,
    "ar": 1,
    "ussr_hand": [11],
    "us_hand": [12],
    "influence": {}
  },
  "actions": [
    {
      "side": "US",
      "card_id": 11,
      "mode": "Space",
      "note": "US spaces USSR card 11 (Korean War)"
    }
  ],
  "assertions": [
    {
      "field": "milops_ussr",
      "op": "eq",
      "value": 0,
      "note": "Korean War event did NOT fire (would give 2 milops)"
    }
  ]
}
```

## Field Notes

- `name`: Stable fixture identifier. Use a gap-oriented name when possible.
- `gap_id`: Tracking ID for the known engine gap or regression.
- `description`: Human-readable expectation for the scenario.
- `setup`: Minimal state required before replaying scripted actions.
- `setup.turn`, `setup.defcon`, `setup.ar`: Public round metadata.
- `setup.ussr_hand`, `setup.us_hand`: Explicit card IDs in each hand.
- `setup.influence`: Optional sparse influence map keyed by country name or ID,
  depending on the eventual C++ fixture loader contract.
- `actions`: Ordered scripted actions to apply after setup.
- `actions[].side`: `"USSR"` or `"US"`.
- `actions[].card_id`: Card played for this step.
- `actions[].mode`: Action mode such as `"Event"`, `"Space"`, `"Influence"`,
  `"Coup"`, or `"Realign"`.
- `actions[].note`: Free-form explanation for maintainers.
- `assertions`: Post-condition checks after all scripted actions resolve.
- `assertions[].field`: Engine field or derived metric to inspect.
- `assertions[].op`: Comparison operator. Start with simple operators such as
  `eq`, `ne`, `lt`, `le`, `gt`, `ge`.
- `assertions[].value`: Expected scalar value for the assertion.
- `assertions[].note`: Why the assertion matters for the referenced gap.

## Conventions

- Keep fixtures small and single-purpose.
- Prefer one gap per fixture.
- Encode only the state needed to reproduce the regression.
- Leave raw logs and card specs unchanged; fixtures are test inputs, not source data.
