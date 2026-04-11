Q: let's say I want to avoid AR first, and use factorized heads + score[c, k] influence head; some qq: 1. how do I implement Vietnam/Chinma (region-restricted +1 ops bonus): if its boolean choice before placement, that's extra inference hop? because it changes scores naturally (and adds mask), depending on +1 (AFAIU). 2. give me minimal but exact set of heads + context features (like "in Fidel firstcoup") that will cover all possible card /eve/nt/ decision making interactionns in TS
A:
Yes. For a non-AR v1, I would change the factorization to:

`card -> use -> scope -> typed-args`

not `card -> mode -> countries`.

That matches the rules better: all actions from a card must finish before the next Action Round starts, the phasing player stays fixed through the round, opponent events triggered by Ops are implemented by the opponent, and realignment lets you choose the next target after seeing the previous roll. That structure is much easier to model as a sequence of typed engine nodes than as one giant flat action. ([GMT Games][1])

## 1) China / Vietnam without an extra policy hop

I would make **scope** an explicit factor under “use this card for Ops.”

For the rules:

* The China Card gets **+1 Ops** only if **all** its Ops are spent in **Asia**, and Asia includes Southeast Asia. ([GMT Games][1])
* Vietnam Revolts gives the USSR **+1 Ops** on a card only if **all** its Ops are spent in **Southeast Asia** for the rest of the turn. ([Twilight Strategy][2])
* Ops modifiers stack in aggregate and can modify the China Card. ([GMT Games][1])

So the legal `scope` values are engine-generated:

* `normal`
* `asia_only` — legal when using China for Ops
* `seasia_only` — legal when Vietnam bonus is active for the USSR
* if both apply, `seasia_only` implies both bonuses, because Southeast Asia is inside Asia. ([GMT Games][1])

I would **not** make that a second policy call. Do one trunk pass, then score all legal scopes in parallel. For each legal scope, the engine computes:

* the effective ops count `B(scope)`
* the legal country mask / region mask
* the legal submodes under that scope

Then the same head is conditioned on `scope` and `B(scope)`:

[
score[c,k \mid scope] = f(h_c,; e_k,; e_{scope},; e_{B})
]

and you decode separately per scope. For placement, that is DP on the scope-specific mask and budget. For coup, it is a single target under the scope mask. For realignment, it is repeated single-target decisions under the scope mask. This is one more **factor** in the action, not another inference hop. ([GMT Games][1])

A practical shortcut is to treat scope as just another small masked choice:

* `use = event / space / ops`
* if `use = ops`, choose `scope`
* then choose the mode-specific arguments

That gives you the right semantics without needing internal AR.

## 2) Minimal exact head set

If the engine emits **typed decision nodes**, you do **not** need a separate “family head” at all. The engine already knows what kind of node it is asking the policy to solve.

For standard TS, I would use **4 head families**:

### A. `CardHead`

Choose **one visible card** from a masked candidate set.

This single head covers:

* normal Action Round hand choice
* headline choice
* mandatory discards such as Blockade, Quagmire, Bear Trap, Latin American Debt Crisis
* choosing a discard-pile card for SALT or Star Wars
* choosing a revealed opponent-hand card for Aldrich Ames
* tie-break card choice in Missile Envy
* choosing the paired card for UN Intervention. ([Twilight Strategy][2])

So I would not make separate “hand head” and “discard head.” Use one `CardHead` with zone tags and a legal mask.

### B. `SmallChoiceHead`

One masked head for all finite small choices.

This covers:

* root use choice: `event / ops / space`
* opponent-event timing: `event_before_ops / event_after_ops`
* China/Vietnam `scope`
* Olympics `participate / boycott`
* Summit and How I Learned DEFCON choice
* Chernobyl region choice
* Wargames invoke-or-not
* Warsaw Pact add-vs-remove
* South African Unrest branch
* India-vs-Pakistan and Iran-vs-Iraq war-side choices. ([GMT Games][1])

So this is the generic “small enum” head.

### C. `CountryAllocHead(score[c,k])`

One generic masked **country/count** head.

Use it in three ways:

* **true allocations**: influence add/remove/move with caps and costs
  Examples: Suez Crisis, Socialist Governments, Marshall Plan, Decolonization, Liberation Theology, Voice of America, The Reformer. ([Twilight Strategy][2])

* **choose N countries** with cap 1, where `k ∈ {0,1}`
  Examples: Comecon, Marshall Plan, Decolonization, Muslim Revolution, Pershing II. ([Twilight Strategy][2])

* **single-country target** by setting total = 1
  Examples: coup target, Brush War target, Truman Doctrine target, Junta follow-up target, Ortega free coup target. ([Twilight Strategy][2])

Two important exactness notes:

* **Realignment should not be one-shot DP.** The rules explicitly let the player resolve each realignment roll before declaring the next target, and the same country may be targeted more than once. So for exact TS play, realignment should be modeled as repeated `CountryAllocHead(total=1)` continuation nodes, one roll at a time. ([GMT Games][1])
* **De-Stalinization should be two sequential nodes.** First a remove-allocation node, then the engine updates control, then a place-allocation node with `required_total = moved_amount` and the new legal destination mask. That is exact and still does not require internal AR. ([Twilight Strategy][2])

### D. `CardSubsetHead`

A subset head for “choose any subset of visible cards.”

In the standard card set, the clearest case is Ask Not, which lets the US discard up to its entire hand before drawing replacements. ([Twilight Strategy][2])

I would keep this head separate because it is the one place where “pick one card” is not enough.

### Not a head: chance

Dice rolls and forced random card draws/discards stay in the engine as chance nodes: war cards, Summit, Five Year Plan, Grain Sales, Terrorism, and so on. ([Twilight Strategy][2])

## 3) Minimal exact context features

The exactness comes more from the **node context** than from having lots of heads.

I would split the context into three layers.

### Board / global state

Per-country tokens:

* USSR influence
* US influence
* control status
* stability
* battleground flag
* region bits
* adjacency/superpower adjacency features

Global scalars:

* turn
* Action Round index
* phasing player
* decision owner
* DEFCON
* VP
* MilOps
* Space Race positions
* China owner / face-up state. ([GMT Games][1])

### Active-effect bitset

Keep a bitset or small embedding bag of all currently active persistent / turn-long effects, because the rules and card texts create ongoing legality and value changes:

* underlined permanent events stay active
* Ops modifiers stack and affect later cards, including China
* many events change later legality or scoring windows. ([GMT Games][1])

This is where cards like NATO, Formosan Resolution, Vietnam Revolts, Containment, Brezhnev Doctrine, Red Scare/Purge, Cuban Missile Crisis, Nuclear Subs, Flower Power, The Reformer, Willy Brandt, Chernobyl, Camp David, AWACS, North Sea Oil, Iran-Contra, Latin American Death Squads, Shuttle Diplomacy, and similar ongoing effects belong. ([Twilight Strategy][2])

### Resolution-frame context

This is the key part. Do **not** hardcode booleans like “in_X_first_coup.”

Use a generic frame:

* `source_card_id`
* `step_id`
* `decision_kind`
  (`CARD`, `SMALL_CHOICE`, `COUNTRY_ALLOC`, `CARD_SUBSET`)
* `phase`
  (`headline`, `main_ar`, `forced_discard`, `response`, `free_ops_continuation`, etc.)
* `visible_card_set` with zone tags
* `legal_small_choice_mask`
* `country_mask`
* `cap[c]`
* `cost_curve[c][k]`
* `required_total`, `min_total`, `max_total`
* `linked_total_from_previous_step`
* `effective_ops`
* `legal_scope_mask`
* `allowed_ops_modes`
* `event_before_after_flag` when relevant

That frame is what makes the 4 heads exact.

Example:

* Ortega continuation node = `decision_kind=COUNTRY_ALLOC`, `step_id=FREE_COUP`, `required_total=1`, `country_mask=adjacent_to_nicaragua`, `effective_ops=2`. ([Twilight Strategy][2])
* Chernobyl node = `decision_kind=SMALL_CHOICE`, `step_id=CHOOSE_REGION`, legal options = regions. ([Twilight Strategy][2])
* SALT node = `decision_kind=CARD`, visible set = discard pile, mask = non-scoring only. ([Twilight Strategy][2])
* De-Stalinization place node = `decision_kind=COUNTRY_ALLOC`, `step_id=PLACE_AFTER_REMOVE`, `linked_total=moved_amount`, mask = current non-US-controlled countries, caps = 2 per country. ([Twilight Strategy][2])

## 4) The pragmatic recommendation

For your non-AR first pass, I would implement exactly this:

* `CardHead`
* `SmallChoiceHead`
* `CountryAllocHead(score[c,k])`
* `CardSubsetHead`

plus an engine resolution stack that emits typed nodes with the frame above.

That is small, exact for standard TS, and it handles China/Vietnam cleanly by inserting `scope` as a masked small choice or by evaluating all legal scopes in parallel from one trunk pass. It also avoids forcing you into internal AR before you actually need it.

[1]: https://www.gmtgames.com/living_rules/TS_Rules_Deluxe.pdf "https://www.gmtgames.com/living_rules/TS_Rules_Deluxe.pdf"
[2]: https://twilightstrategy.com/card-list/ "https://twilightstrategy.com/card-list/"
