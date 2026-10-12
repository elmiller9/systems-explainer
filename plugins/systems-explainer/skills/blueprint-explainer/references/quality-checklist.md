# Quality Checklist

Run through this before handing over an explainer. Fix anything that fails; don't just report it.

## Thinking
- [ ] The count is stated in zone 01, every counted item has its own numbered zone, and the recap repeats the count.
- [ ] Each part says what feeds it or what it feeds. The page explains connections, not just a list.
- [ ] Each zone teaches exactly one idea.
- [ ] Every abstract concept has a physical object in its diagram.
- [ ] The hardest step gets the most space (two zones if needed).
- [ ] There's a synthesis or flywheel zone that shows all the parts working together on one real example.
- [ ] The last zone brings back the zone-01 diagram, completed.

## Writing
- [ ] The hook line is 20 words or fewer and states the payoff or the negation.
- [ ] Each zone has at most one aphorism, it's 12 words or fewer, and it's original. Nothing is copied from source material.
- [ ] The text is short and declarative: a lede of 2 sentences or fewer and 4 points or fewer, each 20 words or fewer.
- [ ] There's no hype vocabulary, no exclamation marks, no presenter persona and no sales pitch.
- [ ] There's at least one copyable asset (an exact prompt, command, setting or template).
- [ ] There's an honest caveat somewhere.

## Visual
- [ ] Only the template tokens are used. There are no hex colors inside SVGs, no pure black, no gradients and no blurred shadows. `check_page.py` passes (placeholders, tokens, colors, external requests, script, title).
- [ ] The accent color marks one thing per zone.
- [ ] Each diagram has 9 nodes or fewer and SVG text is 13 units or larger. Lines are orthogonal and nodes are aligned.
- [ ] Layouts vary: split zones flip occasionally, with 1–2 wide zones and at most 2 statement zones.
- [ ] Color is never the only signal; every colored line or tag also has a text label.

## Screen & interaction
- [ ] Every zone's text and diagram fit a **1366×670 viewport** (a 1366×768 laptop after browser toolbars) without scrolling inside the zone. Measure it; don't eyeball it.
- [ ] Diagram labels render at about 10 px or more on a 1366 laptop. Split-zone diagrams are the usual offenders, so check a screenshot.
- [ ] At 1920×1080, the diagrams use the width, without big empty gutters or tiny diagrams.
- [ ] The minimap rail lists every zone and highlights the current one, and clicking an item jumps to that zone.
- [ ] Arrow keys, PageUp/PageDown, Space and Home/End step through zones.
- [ ] Draw-in and pop-in animations fire when a zone enters view, and with reduced motion everything is visible immediately.
- [ ] Below 900 px it stacks into one column with a 16 px gutter and no horizontal scroll.
- [ ] Dark mode (system setting) reads well.
- [ ] It's a single self-contained file: the only external resource is the Google Fonts stylesheet. No other network requests or images (SVG is inline).
- [ ] The `<title>` is a 2–4 word name, and the `<meta name="description">` holds the promise.
