# The Method: Explaining a System So It Sticks

This is the teaching approach behind every blueprint explainer. It comes from studying short explainer videos that make complicated systems feel obvious. The format here is a page instead of a video, and there's no on-screen character or sales pitch. What carries over is the *thinking*.

---

## 1. Core principles

1. **A system is parts plus the connections between them.** Never explain a part without saying what feeds it and what it feeds. The arrows matter as much as the boxes.
2. **Count it before you explain it.** Say how many pieces there are before showing any of them ("It's four pieces."). The count gives the reader a container to put each piece in, and it lets them know where they are in the explanation.
3. **One zone, one idea.** Each numbered zone teaches exactly one thing. It has one diagram and one sentence worth remembering. If a zone needs two diagrams, it's really two zones.
4. **Every abstract noun gets a physical object.** "Permissions" are a door with a lock. "A knowledge base" is a shelf of labeled jars. "Compression" is a stack of pages being squeezed. If you can't draw it as an object, you haven't understood it well enough yet.
5. **Structure beats prose.** Short declarative sentences go next to a diagram. Don't write paragraphs that explain what the diagram already shows.
6. **Calm authority, no hype.** The tone is a senior practitioner walking a colleague through the plant floor. Leave out exclamation marks, "game-changing" and "revolutionary".
7. **Proof, then instruction.** Ground each claim in something concrete (a number, a case, a real configuration), then tell the reader what to do. Use first person for proof ("In my setup…") and second person for instruction ("You connect…").
8. **Close the loop.** The last zone brings back the opening diagram, now fully labeled and understood. The reader sees the whole system they just learned.

---

## 2. Rhetorical devices (the toolkit)

Use the ones the topic calls for. Every explainer needs at least: **the hook, the count, one aphorism per zone, and the loop-back**.

| Device | What it does | Pattern | Original example |
|---|---|---|---|
| **Big-promise hook** | Gives the payoff in one sentence | "[Small input] now does [large output]. It's [N] pieces." | "A three-person kitchen can serve two hundred covers a night. It runs on four pieces." |
| **Negation hook** | Takes something away to make the real thing stand out | "The secret isn't X. It isn't Y. It's Z." | "Good onboarding isn't the docs. It isn't the buddy. It's the first ticket." |
| **"If I started over" hook** | Offers to save the reader your mistakes | "If I rebuilt [X] from zero, here's the order I'd build it in." | "If I set up a home network from scratch today, I'd build it in three layers." |
| **The count** | Gives the reader a container for what follows | State N up front, number every zone, and repeat N in the recap. | "Three parts. Count them with me." |
| **Vocabulary check** | Untangles terms people confuse, before the framework | "Before the [N], three words you have to keep apart: A, B, C." | "Backup, sync and archive are three different things." |
| **Anti-pattern story** | Shows the cost of the naive approach | A dated, specific sequence of how it went wrong, ending in a number. | "Monday: one wrong price in the sheet. Thursday: forty invoices. Two weeks to reconcile." |
| **"The part people get wrong"** | Slows down at the hardest step | Flag it, then walk through it step by step. | "Here's where most setups break." |
| **The design rule** | The one rule that makes the whole stack work | "Here's the rule that makes it all hold together: …" | "Recipes point at the pantry; they never keep their own copy of the ingredients." |
| **Aphorism** | One quotable line that sums up the zone | A contrast or parallel structure in 12 words or fewer. | "A backup you've never restored is a hope." |
| **The copyable asset** | Something concrete to use today | An exact prompt, setting, template or command shown in a mock UI. | A terminal box with the exact command. |
| **Synthesis ("make it real")** | Proves the parts work together | One realistic request, with a line drawn from *every* numbered part to the output. | One customer order traced through all four stations. |
| **The detail that breaks most setups** | Adds depth once the main framework is clear | A nuance or caveat after the framework. | "Long lists don't stay whole; here's what gets dropped." |
| **Guardrails** | Shows where human control stays | 2–4 boxes, each a rule with a lock or checkmark icon. | "Money moves need a human approval, every time." |
| **Scoreboard** | One number that tells you it's working | "How do you know it works? One question: …" | "Does the same mistake happen twice?" |
| **The honest caveat** | Earns trust by naming the cost | "This isn't zero work. Here's what it costs." | "You still taste every sauce for the first month." |
| **Lifestyle payoff** | Shows what your day looks like once it runs | Show the human's remaining role, often as a small UI. | A review queue with Approve / Edit / Skip. |
| **Loop-back** | Ends on the opening picture, completed | Repeat the zone-01 diagram, fully labeled. | The same flowchart, now with every box understood. |

### Writing aphorisms
- Use contrast: "X is a lesson; Y is a disaster." Or redefinition: "A skill that only works once is a note."
- Use parallel structure: "Users try it. Operators run on it."
- Use concrete nouns and keep it to 12 words or fewer, with no hedging.
- Each one should still make sense if the reader remembers *only* that line from the zone.

---

## 3. Narrative arcs

Pick **one** arc per explainer. The arc decides the order of the zones; the devices fill them in. Most explainers run **8–14 zones**.

### Arc A: The N-Pieces Stack
*Use when:* the system has 3–5 parallel components that each add a capability. ("What you need to run X.")
1. Big-promise hook, and the system shown as one diagram (the parts unlabeled or lightly labeled).
2. Piece 1 … Piece N: one zone each. Each gets an object metaphor and one concrete configuration ("I allowed read and send, and left delete off").
3. The part people get wrong: usually the piece that needs a procedure, given 2 zones.
4. Results: one dense flowchart of everything the assembled system now does.
5. Guardrails / supervision: where the human stays in control, plus a gauge showing how much runs on its own.
6. Loop-back: the opening diagram, now fully labeled.

### Arc B: Anti-Pattern → Loop
*Use when:* the topic is a process or cycle that most people do naively or not at all. ("How to make X improve over time.")
1. Value hook plus a single proof point (a number).
2. The warning: why the obvious approach fails, told as an anti-pattern story on a timeline.
3. Reframe: "The goal isn't X. It's Y."
4. The loop: one overview zone showing the full cycle, then one zone per step (N = 3–5).
5. The detail that breaks most setups (and its fix).
6. Routing / where the lesson lands: a branching diagram, with the wrong branch grayed out.
7. Guardrails.
8. Scoreboard: one metric.
9. Honest caveat, then loop-back.

### Arc C: Build Order (Layers)
*Use when:* the components depend on each other and order matters. ("Build it in this order.")
1. "If I started over" hook, plus receipts (what it runs today).
2. The stack: N numbered shelves stacked bottom-up, with an upward arrow.
3. Layer 1 … Layer N: one zone each, and each says what it feeds next.
4. The design rule: slow down, give it 2 zones, and draw the reference lines.
5. Flywheel: the whole stack in cross-section, with lines showing how one change spreads through every layer.
6. Lifestyle payoff: what the human does now.
7. Recap: the numbered layers in one row, then loop-back.

### Arc D: Taxonomy (Types of X)
*Use when:* people treat something as one thing when it's really several distinct kinds. ("The N types of X.")
1. Negation hook, then "with it vs without it" side by side.
2. Roadmap: N placeholder boxes, "It's N, not one."
3. Vocabulary check: three confused terms, with a mini flow that connects them.
4. Type 1 … Type N: one zone each (definition, object metaphor, example, and how it fails). Save the most neglected type for last, as "the one almost nobody builds".
5. Synthesis: one real request, with a colored line from each type to the parts of the output it shaped.
6. Technical caveat: a short bonus that compares two ways of doing the hard part.
7. Recap: "N types. Say them with me." Then loop-back.

### Choosing
- Parallel capabilities → **A**. A cycle or habit → **B**. Dependencies or order → **C**. Kinds or categories → **D**.
- If two arcs fit, choose the one whose zone 01 diagram you can draw most clearly.

---

## 4. Pacing on the page

The videos ran 3–7 minutes. A page has no clock, so pace with **zone weight** instead:
- **Light zone:** a 1–2 sentence lede plus a diagram. Use it for the hook, simple pieces, and the loop-back.
- **Standard zone:** a lede, 2–4 short points, a diagram and an aphorism. This is most zones.
- **Heavy zone:** the "part people get wrong" or the design rule. Split it into two consecutive zones rather than making one zone dense.
- Give the most time to the hardest step, not the most impressive one.
- Zone text must fit beside its diagram in a 1366×670 viewport (a 1366×768 laptop after browser toolbars) without scrolling inside the zone. If it doesn't fit, cut words or split the zone.

---

## 5. What to leave out
- No presenter avatar or mascot, and no "I" persona beyond short proof statements.
- No sales pitch, pricing or "join my community" ending. Finish with a recap, the loop-back and "start with piece 1".
- Don't use another creator's phrasing, names or branding. Write original aphorisms and examples for every topic.
