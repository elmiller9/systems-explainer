# Motion Grammar

**The rule: motion answers the reader's question. It never plays at the reader.**

That rule comes from a side-by-side review (2026-10-12) of static and motion builds of a dense reference architecture, explainer and reference:

| Pattern | Kind | Verdict |
|---|---|---|
| M3 State ("simulate a run" buttons on the outcome taxonomy) | Reader-driven | **Very useful in both page types.** Picking a case and seeing which outcome it produces taught the traps faster than reading. |
| M4 Trace (hover or select a module, see its connections) | Reader-driven | **Useful, once it explains itself.** Lighting items with no reason given was confusing, and selecting must visibly change something. Lit items now carry IN/OUT relation labels, and a status line narrates the selection. |
| M6 Count (number counts up) | Autoplay | Not noticed. No difference from static. |
| M2 Build (zone reveals in steps) | Autoplay | Not noticed. No difference from static. |
| M1 Flow (dot travels a pipeline) | Autoplay | Not useful. On a finished loop diagram it **hurt the aesthetic**. |
| M5 Sequence (stations highlight in turn) | Autoplay | Not useful: things lit up, but they weren't clickable and nothing changed. |

Both page types share this grammar and one runtime: `shared/motion.css` + `shared/motion.js`, synced into both templates by `scripts/sync_tokens.py`.

---

## Tier 1: use these (reader-driven)

### M3 State: "simulate a case"
Use it when the reader is likely to ask *"what happens if…?"* and the answer is one or more items in a set: outcome taxonomies, routing (gap type → owner), permission scenarios, failure modes.

- 3–5 cases, named the way a practitioner would say them ("Log source down", "Rule suppressed"), plus "All".
- Each case lights the item(s) it produces, dims the rest, and shows a one-sentence `data-say` explaining *why* that outcome results, including the check or trap it implies.
- Explainer: put it on the zone that teaches the hard part. Reference: put it on taxonomy and scenario tables.

```html
<div data-states>
  <div class="m-states" role="group" aria-label="Simulate a run">
    <button type="button" data-set-state="all" aria-pressed="true">All outcomes</button>
    <button type="button" data-set-state="outage">Log source down</button>
  </div>
  … <div class="rung" data-when="outage">…</div> …
  <p class="m-say" data-say="outage" hidden>Why this outcome, and the check that catches it.</p>
</div>
```

### M4 Trace: "what does this touch?"
Use it on architecture maps and module explorers, where the reader asks *"what does this part connect to?"*

**Required, or don't use it:**
1. **Every lit item says why.** It needs a `data-rel` label from the traced node's point of view: `IN · <what it sends>` or `OUT · <what it receives>`. Lighting without a reason reads as random.
2. **A status line** (`[data-trace-status]`) narrates what is shown: "Selected: Validation orchestration · 3 direct connections. IN = sends something to it · OUT = receives something from it."
3. **Selecting changes something visible.** Use `data-trace-pressed` so a click pins the trace, marks the item SELECTED and updates the status. The detail panel also lists the same connections in plain text, so it works without script too.
4. Only real, source-backed connections. Never infer edges the source doesn't describe.

```html
<div data-explorer data-trace-scope data-trace-pressed>
  <p class="m-trace-status" data-trace-status>Hover or select a module to see what it connects to.</p>
  <button class="item" data-key="val" data-node="val"
          data-links="cov corr emu"
          data-rel="cov:IN · coverage gaps; corr:OUT · emulation runs">Validation orchestration</button>
  …
  <dl class="detail" data-panel="val">… <div class="full"><dt>Connections</dt><dd>IN from Coverage mapping: coverage gaps · OUT to …</dd></div></dl>
</div>
```

## Tier 2: off by default (autoplay)

M1 Flow, M2 Build, M5 Sequence and M6 Count stay in the runtime but **are not used unless the user explicitly asks for them**. If they are requested, they must also:
- be triggered or replayable by the reader, and change something meaningful when triggered;
- never run on a finished overview or loop-back diagram (that hurt the aesthetic);
- never highlight items the reader can't act on.

Markup for Tier 2 is in each skill's `components.html`, marked "on request only".

## Rules for all motion

1. **Complete at rest.** Without script, or with `prefers-reduced-motion`, everything shows in its final state and nothing is dimmed. Interactive patterns still work. They just don't animate.
2. **Reader in control.** Buttons and focusable items. Everything works by keyboard.
3. **Explain every highlight.** Lit means "related", and the page always says how (a `data-say` sentence or a `data-rel` label).
4. **One accent.** Lit uses `--accent`, and dimming uses opacity (0.28). No new colors, glow, blur or bounce.
5. **Budget.** Explainer: Tier 1 on at most 2–3 zones, and only where a "what if" or "what does it touch" question is real. Reference: at most 3 uses, on taxonomies, scenarios and architecture. Never on plain tables, filters or switchers (they're already interactive).
6. **No motion in an explainer's zone 01 or a reference's hero.**
