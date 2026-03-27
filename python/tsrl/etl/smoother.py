"""
Offline actor-hand smoother.

Produces OfflineLabels for each decision point in a replay by using
the FULL replay (past + future observations) to reconstruct actor hands
as precisely as possible.

Strict separation rule:
  - OfflineLabels are ONLY for supervised training targets.
  - They must NEVER be passed to reduce_public(), reduce_hand(), or any
    online/self-play code path.

Algorithm (single-pass forward + backward reconciliation):
  1. Forward pass: run the causal HandKnowledge reducer (reduce_hand)
     to accumulate what we knew about each hand at each step.
  2. Backward pass: walk the event list in reverse and propagate
     future-visible card observations back to earlier steps.
  3. For each decision point, combine forward and backward knowledge
     to produce the best possible actor-hand reconstruction.

Label quality tags:
  EXACT     – every card in hand was directly observed (reveal_hand or
               end_turn_held at this exact step).
  INFERRED  – all cards provably in hand from causal + future evidence;
               no ambiguity remains.
  AMBIGUOUS – some cards must be among a known set but the exact assignment
              is uncertain (set size > 1 per slot).
  UNKNOWN   – insufficient evidence to reconstruct any portion of hand.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

from tsrl.etl.reducer import (
    HAND_SIZE_EARLY,
    HAND_SIZE_LATE,
    reduce_hand,
    reduce_public,
)
from tsrl.schemas import (
    EventKind,
    HandKnowledge,
    LabelQuality,
    OfflineLabels,
    PublicState,
    ReplayEvent,
    Side,
)


# ---------------------------------------------------------------------------
# Internal snapshot (per-step state for the backward pass)
# ---------------------------------------------------------------------------


@dataclass
class _StepSnapshot:
    """State at a single replay step, used during smoothing."""

    event: ReplayEvent
    pub: PublicState
    ussr_hand: HandKnowledge
    us_hand: HandKnowledge

    # Backward-propagated: cards known in hand from future evidence only.
    backward_known_in: dict[Side, frozenset[int]] = field(
        default_factory=lambda: {Side.USSR: frozenset(), Side.US: frozenset()}
    )

    # Intra-turn propagation: backward knowledge carried forward within the
    # turn, with played cards subtracted.  Populated by _intra_turn_propagation.
    propagated_known_in: dict[Side, frozenset[int]] = field(
        default_factory=lambda: {Side.USSR: frozenset(), Side.US: frozenset()}
    )
    # True iff the propagated set for each side was seeded from a complete
    # backward snapshot at the start of this turn (size == expected hand size).
    seed_complete_in: dict[Side, bool] = field(
        default_factory=lambda: {Side.USSR: False, Side.US: False}
    )
    # Expected hand size at this step = initial_size - plays_so_far_this_turn.
    # Populated by _intra_turn_propagation.
    expected_size_in: dict[Side, int] = field(
        default_factory=lambda: {Side.USSR: 0, Side.US: 0}
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def smooth_game(
    events: list[ReplayEvent],
    all_card_ids: frozenset[int],
    *,
    decision_kinds: frozenset[EventKind] = frozenset({
        EventKind.PLAY,
        EventKind.HEADLINE,
    }),
) -> list[OfflineLabels]:
    """Produce offline-smoothed labels for every decision point in a game.

    Args:
        events: Ordered events from parse_replay().
        all_card_ids: All valid card ids (excl. China Card).
        decision_kinds: EventKinds that count as decision points where we
            want actor-hand labels. Defaults to PLAY / HEADLINE / SPACE_RACE.

    Returns:
        One OfflineLabels per event in ``events`` whose kind is in
        ``decision_kinds``. Steps are in replay order.
    """
    snapshots = _forward_pass(events, all_card_ids)
    _backward_pass(snapshots)
    _intra_turn_propagation(snapshots)
    return _build_labels(snapshots, all_card_ids, decision_kinds)


# ---------------------------------------------------------------------------
# Forward pass
# ---------------------------------------------------------------------------


def _forward_pass(
    events: list[ReplayEvent],
    all_card_ids: frozenset[int],
) -> list[_StepSnapshot]:
    """Run the causal reducer forward and collect per-step snapshots."""
    pub = PublicState()
    ussr_hand = HandKnowledge(observer=Side.USSR, possible_hidden=all_card_ids)
    us_hand = HandKnowledge(observer=Side.US, possible_hidden=all_card_ids)
    snapshots: list[_StepSnapshot] = []

    for event in events:
        prev_pub = pub
        pub = reduce_public(pub, event)
        ussr_hand = reduce_hand(ussr_hand, event, all_card_ids, prev_pub)
        us_hand = reduce_hand(us_hand, event, all_card_ids, prev_pub)
        snapshots.append(_StepSnapshot(
            event=event,
            pub=pub,
            ussr_hand=ussr_hand,
            us_hand=us_hand,
        ))

    return snapshots


# ---------------------------------------------------------------------------
# Backward pass
# ---------------------------------------------------------------------------


def _backward_pass(snapshots: list[_StepSnapshot]) -> None:
    """Walk snapshots in reverse, propagating future card observations back.

    Mutates snapshots[i].backward_known_in in place.

    Key rules:
    - PLAY / HEADLINE: card was in the actor's hand at this step and at all
      earlier steps within the same turn → add to backward set.
    - FORCED_DISCARD: card was in the holder's hand before being discarded
      → add to that side's backward set.
    - HEADLINE_PHASE_START: turn boundary.  TSEspionage logs carry no DRAW
      events, so we cannot trace cards back across a refill.  Clear both sets
      (END_TURN_HELD events encountered later in the backward walk will
      re-add cards explicitly held across the boundary).
    - RESHUFFLE: same conservative clear as HEADLINE_PHASE_START.
    - REVEAL_HAND / END_TURN_HELD: explicit forward-observed evidence; add.
    - DISCARD / REMOVE: card leaves the game permanently; stop propagating.
    """
    backward_ussr: set[int] = set()
    backward_us: set[int] = set()

    for snap in reversed(snapshots):
        ev = snap.event
        card_id = ev.card_id

        # --- Update backward sets from this event ---

        if ev.kind == EventKind.HEADLINE_PHASE_START:
            # Turn boundary: hands are refilled from the deck.  Without explicit
            # DRAW events we cannot know which cards crossed this boundary.
            backward_ussr.clear()
            backward_us.clear()

        elif ev.kind == EventKind.REVEAL_HAND:
            target = ev.phasing
            if target == Side.USSR:
                backward_ussr.update(ev.aux_card_ids)
                if card_id is not None:
                    backward_ussr.add(card_id)
            elif target == Side.US:
                backward_us.update(ev.aux_card_ids)
                if card_id is not None:
                    backward_us.add(card_id)

        elif ev.kind == EventKind.END_TURN_HELD:
            # Explicitly held across turn boundary — propagate back past the
            # HEADLINE_PHASE_START clear that will be encountered next.
            target = ev.phasing
            if target == Side.USSR:
                backward_ussr.update(ev.aux_card_ids)
            elif target == Side.US:
                backward_us.update(ev.aux_card_ids)

        elif ev.kind in (EventKind.PLAY, EventKind.HEADLINE):
            # Going backward: the card was in the actor's hand at this step.
            # Add it so all earlier steps in the same turn see it as held.
            if card_id is not None:
                if ev.phasing == Side.USSR:
                    backward_ussr.add(card_id)
                elif ev.phasing == Side.US:
                    backward_us.add(card_id)

        elif ev.kind == EventKind.FORCED_DISCARD:
            # Card was in the holder's hand before being discarded.
            if card_id is not None:
                if ev.phasing == Side.USSR:
                    backward_ussr.add(card_id)
                elif ev.phasing == Side.US:
                    backward_us.add(card_id)

        elif ev.kind in (EventKind.DISCARD, EventKind.REMOVE):
            # Card removed from game permanently; stop propagating.
            if card_id is not None:
                backward_ussr.discard(card_id)
                backward_us.discard(card_id)

        elif ev.kind == EventKind.RESHUFFLE:
            # Deck reshuffled: cannot trace hand contents across this point.
            backward_ussr.clear()
            backward_us.clear()

        # --- Store snapshot of backward knowledge at this step ---
        snap.backward_known_in[Side.USSR] = frozenset(backward_ussr)
        snap.backward_known_in[Side.US] = frozenset(backward_us)


# ---------------------------------------------------------------------------
# Intra-turn propagation (third pass)
# ---------------------------------------------------------------------------


def _intra_turn_propagation(snapshots: list[_StepSnapshot]) -> None:
    """Forward sweep: carry backward-established hand knowledge through a turn.

    Once we observe N cards in backward_known_in for a side (the peak
    backward snapshot for the turn — typically the headline step where all
    this-turn plays are visible), we track those cards forward, removing each
    card as it is played or discarded.  This upgrades later ARs from AMBIGUOUS
    (only 1-2 cards known from backward) to INFERRED (full remaining hand known).

    Also records seed_complete_in[side]: True iff the seed that was established
    for this side at turn start was a complete hand (size == expected hand size).

    Mutates snapshots[i].propagated_known_in and .seed_complete_in in place.
    """
    running: dict[Side, frozenset[int]] = {Side.USSR: frozenset(), Side.US: frozenset()}
    seed_complete: dict[Side, bool] = {Side.USSR: False, Side.US: False}
    plays_so_far: dict[Side, int] = {Side.USSR: 0, Side.US: 0}
    current_turn: int = -1
    initial_size: int = HAND_SIZE_EARLY

    for snap in snapshots:
        ev = snap.event

        # New turn: reset running sets, seed flags, and play counters.
        if ev.turn != current_turn:
            current_turn = ev.turn
            running = {Side.USSR: frozenset(), Side.US: frozenset()}
            seed_complete = {Side.USSR: False, Side.US: False}
            plays_so_far = {Side.USSR: 0, Side.US: 0}
            initial_size = HAND_SIZE_EARLY if current_turn <= 3 else HAND_SIZE_LATE

        # Absorb backward knowledge if it expands what we're tracking.
        for side in (Side.USSR, Side.US):
            b = snap.backward_known_in[side]
            if len(b) > len(running[side]):
                running[side] = b
                if len(b) >= initial_size:
                    seed_complete[side] = True

        # Record propagated state BEFORE removing the played card.
        # (The label represents what was in hand when the decision was made.)
        snap.propagated_known_in = {
            Side.USSR: frozenset(running[Side.USSR]),
            Side.US: frozenset(running[Side.US]),
        }
        snap.seed_complete_in = dict(seed_complete)
        snap.expected_size_in = {
            side: max(0, initial_size - plays_so_far[side])
            for side in (Side.USSR, Side.US)
        }

        # Remove the played/discarded card from running and increment play count.
        if ev.kind in (EventKind.PLAY, EventKind.HEADLINE, EventKind.FORCED_DISCARD):
            actor = ev.phasing
            if actor in (Side.USSR, Side.US):
                plays_so_far[actor] += 1
                if ev.card_id is not None:
                    running[actor] = running[actor] - {ev.card_id}


# ---------------------------------------------------------------------------
# Label construction
# ---------------------------------------------------------------------------


def _build_labels(
    snapshots: list[_StepSnapshot],
    all_card_ids: frozenset[int],
    decision_kinds: frozenset[EventKind],
) -> list[OfflineLabels]:
    """Combine forward and backward knowledge into OfflineLabels."""
    labels: list[OfflineLabels] = []

    for snap in snapshots:
        if snap.event.kind not in decision_kinds:
            continue

        actor = snap.event.phasing
        if actor not in (Side.USSR, Side.US):
            continue

        hand_knowledge = snap.ussr_hand if actor == Side.USSR else snap.us_hand

        # Best estimate of actor's hand: union of causal forward knowledge,
        # raw backward knowledge, and intra-turn propagated knowledge.
        forward_known = hand_knowledge.known_in_hand
        backward_known = snap.backward_known_in.get(actor, frozenset())
        propagated_known = snap.propagated_known_in.get(actor, frozenset())
        combined_known = forward_known | propagated_known

        # Opponent's support mask: possible_hidden from the opponent's perspective.
        opponent = Side.US if actor == Side.USSR else Side.USSR
        opp_knowledge = snap.us_hand if actor == Side.USSR else snap.ussr_hand
        opponent_possible = opp_knowledge.possible_hidden

        # Assign quality tags per card.
        # EXACT   = in both forward (causal) and backward evidence
        # INFERRED = in forward or propagated (but not both causal sources)
        card_quality: dict[int, LabelQuality] = {}
        for cid in combined_known:
            if cid in forward_known and cid in backward_known:
                card_quality[cid] = LabelQuality.EXACT
            else:
                card_quality[cid] = LabelQuality.INFERRED

        # Expected hand size at this decision step.
        # If the intra-turn propagation was seeded from a complete backward
        # snapshot, len(propagated_known) IS the true remaining hand size.
        # Otherwise fall back to the turn-based constant (conservative).
        if snap.seed_complete_in.get(actor, False) and propagated_known:
            # Seed was complete → propagated exactly tracks remaining hand size.
            expected_hand_size = len(propagated_known)
        elif hand_knowledge.hand_size > 0:
            expected_hand_size = hand_knowledge.hand_size
        else:
            # Fall back to initial_size - plays_so_far (computed in third pass).
            expected_hand_size = snap.expected_size_in.get(actor, 0) or (
                HAND_SIZE_EARLY if snap.event.turn <= 3 else HAND_SIZE_LATE
            )

        step_quality = _aggregate_quality(card_quality, expected_hand_size, combined_known)

        labels.append(OfflineLabels(
            turn=snap.event.turn,
            ar=snap.event.ar,
            phasing=actor,
            actor_hand=combined_known,
            card_quality=card_quality,
            step_quality=step_quality,
            opponent_possible=opponent_possible,
        ))

    return labels


def _aggregate_quality(
    card_quality: dict[int, LabelQuality],
    hand_size: int,
    known_cards: frozenset[int],
) -> LabelQuality:
    """Compute overall step quality from per-card tags."""
    if not card_quality:
        return LabelQuality.UNKNOWN
    # If we know fewer cards than hand_size, there are unobserved cards.
    if len(known_cards) < hand_size:
        return LabelQuality.AMBIGUOUS
    worst = max(card_quality.values())
    return LabelQuality(worst)


# ---------------------------------------------------------------------------
# Convenience metrics
# ---------------------------------------------------------------------------


@dataclass
class SmootherMetrics:
    """Aggregate quality metrics across all labels in a game."""

    total: int = 0
    exact: int = 0
    inferred: int = 0
    ambiguous: int = 0
    unknown: int = 0
    false_exclusion_violations: int = 0  # must stay 0

    @property
    def exact_rate(self) -> float:
        return self.exact / self.total if self.total else 0.0

    @property
    def partial_rate(self) -> float:
        return (self.exact + self.inferred) / self.total if self.total else 0.0

    @property
    def false_exclusion_rate(self) -> float:
        return self.false_exclusion_violations / self.total if self.total else 0.0


def compute_metrics(
    labels: list[OfflineLabels],
    ground_truth_hands: dict[tuple[int, int, Side], frozenset[int]] | None = None,
) -> SmootherMetrics:
    """Compute smoother quality metrics.

    Args:
        labels: Output of smooth_game().
        ground_truth_hands: Optional oracle. Maps (turn, ar, actor) →
            true hand at that step. Used to check false_exclusion_rate.
            If None, false_exclusion_violations is not checked.
    """
    m = SmootherMetrics(total=len(labels))
    for label in labels:
        q = label.step_quality
        if q == LabelQuality.EXACT:
            m.exact += 1
        elif q == LabelQuality.INFERRED:
            m.inferred += 1
        elif q == LabelQuality.AMBIGUOUS:
            m.ambiguous += 1
        else:
            m.unknown += 1

        if ground_truth_hands is not None:
            key = (label.turn, label.ar, label.phasing)
            true_hand = ground_truth_hands.get(key, frozenset())
            # False exclusion: a card actually in hand was excluded from actor_hand.
            excluded = true_hand - label.actor_hand
            if excluded:
                m.false_exclusion_violations += len(excluded)

    return m
