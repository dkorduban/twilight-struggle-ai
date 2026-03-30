"""Trace exactly why US picks Brush War/Che COUP at DEFCON=2."""
import tsrl.policies.minimal_hybrid as mh
from tsrl.policies.minimal_hybrid import MinimalHybridParams, _is_suicidal_action, _defcon_safety_penalty, _score_action, _action_sort_key, _scored_candidate_actions, _make_decision_context
from tsrl.engine.game_loop import run_game_cb
from tsrl.schemas import ActionMode, Side

TARGET_CARDS = frozenset({39, 83})
params = MinimalHybridParams()
found = 0

_original_choose = mh.choose_minimal_hybrid

def tracing_choose(pub, hand, holds_china, params=None, side=None):
    global found
    if params is None:
        params = MinimalHybridParams()

    # Detect who we are by checking calls
    result = _original_choose(pub, hand, holds_china, params=params)

    if (result and result.card_id in TARGET_CARDS
            and result.mode == ActionMode.COUP
            and pub.defcon <= 2
            and found < 3):
        found += 1
        # Determine which side we are
        # Try to figure out side from pub state
        from tsrl.schemas import Side as S
        for side_try in [S.US, S.USSR]:
            ctx = _make_decision_context(pub, side_try, params)
            candidates = _scored_candidate_actions(hand, holds_china, ctx)

            _held_us_defcon = hand & mh._US_DEFCON_LOWERING_CARDS
            grain_sales_suicidal = pub.defcon <= 2 and 53 in hand

            scored = []
            for action, cached_score in candidates:
                score = cached_score if cached_score is not None else _score_action(ctx, action)
                card = ctx.card_cache[action.card_id]
                score += _defcon_safety_penalty(ctx, action, card)
                scored.append((action, score))

            safe = [
                (a, s) for a, s in scored
                if not _is_suicidal_action(a, ctx.card_cache[a.card_id], pub, side_try)
                and not (grain_sales_suicidal and a.card_id == 68)
            ]

            # Check if our result is in safe
            in_safe = any(a.card_id == result.card_id and a.mode == result.mode and a.targets == result.targets for a, _ in safe)
            if in_safe or not safe:
                print(f"\n=== Brush War/Che COUP chosen (found #{found}) side={side_try.name} DEFCON={pub.defcon} ===")
                print(f"  Hand: {sorted(hand)}")
                print(f"  Chosen: card={result.card_id} mode={result.mode.name} targets={result.targets}")
                print(f"  Safe pool ({len(safe)} actions):")
                for a, s in sorted(safe, key=lambda x: -x[1])[:15]:
                    mode_name = a.mode.name if hasattr(a.mode, 'name') else str(a.mode)
                    mark = "<-- CHOSEN" if (a.card_id == result.card_id and a.mode == result.mode) else ""
                    print(f"    card={a.card_id} mode={mode_name} tgts={a.targets} score={s:.1f} {mark}")
                break

    return result

mh.choose_minimal_hybrid = tracing_choose

for seed in range(200):
    result = run_game_cb(
        ussr_policy=lambda pub, hand, hc: mh.choose_minimal_hybrid(pub, hand, hc),
        us_policy=lambda pub, hand, hc: mh.choose_minimal_hybrid(pub, hand, hc),
        seed=seed,
    )

print(f"\nTotal traced: {found}")
