# Content Brief Template

Fill this in before writing any HTML. Keep it in your working notes, not on the page. If a field can't be filled, the explainer isn't ready yet: ask the user, or go read the sources.

```yaml
topic:            # what system is being explained, in plain words
audience:         # who reads this and what they already know (e.g. "small-business owner, no coding")
the_promise:      # one sentence: what the reader can do/understand after reading
arc:              # A N-pieces | B anti-pattern→loop | C build-order | D taxonomy (see method.md §3)
count:            # N (3–5) and the noun: "four pieces", "three layers", "five types"
hook:
  device:         # big-promise | negation | if-I-started-over
  line:           # the opening sentence (≤ 20 words)
  zone01_diagram: # the overview diagram that will return at the end
vocabulary:       # optional: 2–3 terms people confuse, with a one-line definition each
anti_pattern:     # optional: the naive approach + a dated mini-story ending in a cost
parts:            # one entry per counted item
  - name:
    one_liner:    # what it is, ≤ 15 words
    metaphor:     # object from visual-language.md §5 (or a new one, which you then add there)
    concrete:     # one real configuration/example/number
    feeds:        # what it connects to (systems = parts + connections)
    aphorism:     # ≤ 12 words, original
the_hard_part:    # "the part people get wrong" + the step-by-step fix
design_rule:      # optional: the one rule that makes it all hold together
copyable_asset:   # exact prompt / command / setting / template the reader can use today
synthesis:        # one realistic request traced through every part to one output
guardrails:       # optional: 2–4 rules about where humans stay in control
scoreboard:       # optional: one metric that tells you it's working
caveat:           # the honest cost
close:            # recap line + "start with piece 1" (no sales pitch)
zones:            # final ordered list: "01 TITLE (layout, weight)" …
```

## Zone script format

Write each zone like this before building it:

```
## 04 PIECE TWO: THE PANTRY        [split | standard]
LEDE: Everything the kitchen knows, written down where any cook can find it.
POINTS:
- Raw deliveries go on one shelf, untouched.
- Prepped ingredients get labeled and dated.
- A card on the door says what's where.
DIAGRAM: shelf of labeled jars; the index card on the door is highlighted in the accent color.
APHORISM: "If it isn't labeled, it isn't in stock."
```
