# The Reference Method: A Detailed Guide You Can Work From

The reference guide is the **detailed companion** to the blueprint explainer. The explainer teaches the argument, one idea per screen. The reference preserves what the source says, so the people who build, review or audit the system can look things up, compare options and check details.

| | Blueprint explainer | Reference guide |
|---|---|---|
| Job | Teach and persuade | Look up and work from |
| Reader | Someone new to the topic, or a decision-maker | Someone building, reviewing or auditing it |
| Coverage | About 10–15 ideas, chosen for the arc | Nearly all of the source, sections kept |
| Order | Narrative arc (hook → count → loop-back) | The source's own section order |
| Reading | One full screen per zone, keyboard stepping | Scroll and skim, contents rail, filters and toggles |
| Visuals | A drawn object metaphor for every idea | Tables, explorers, ladders, timelines, code |
| Voice | Short rules and aphorisms | Precise and plain, in the source's own terms |
| Shared | Tokens, fonts, semantic colors, and an honest record of data conflicts | (same) |

---

## 1. Principles

1. **Completeness over selection.** Every section of the source appears, in order, with its own number. Cover at least 90% of its substantive content (decisions, tables, interfaces, lists, phases, open questions). Leave out only repetition and boilerplate.
2. **Keep the source's terms.** Use its entity names, IDs, versions, units and figures exactly. Don't round numbers, rename concepts or invent examples the source doesn't give.
3. **Summary before detail.** Each section opens with a plain-language claim as its `h2`, then 2–4 sentences of context, then the detailed component.
4. **Tabular content becomes interactive, not longer.** If the source has a long table, a family of interfaces or a set of scenarios, make it a switcher, filter or explorer so the reader can narrow it down. The content still lives in the markup.
5. **Color has meaning.** Semantic chips (ok, gap, ai, human) carry classification consistently across the whole page. The terracotta accent marks a key row, the active item or the one figure that matters.
6. **Flag what's wrong in the source.** If two figures contradict each other, or a claim has no support, say so plainly in the footer, and in the section when it matters. Pick one figure, and say which and why.
7. **Calm, plain prose.** Short declarative sentences in the active voice. No hype, no aphorisms (those belong to the explainer) and no presenter persona.
8. **Complete without script.** All content is visible in the HTML. Script only adds the contents rail, switching, filtering and the theme toggle. Hidden tab panels are the only content not visible at rest.

---

## 2. Mapping source content to components

| Source content | Component (see `assets/components.html`) |
|---|---|
| Core decisions, principles, "things to build" | R1 decision cards |
| Any table | R2 data table (`.is-key` on the row that matters) |
| Several related tables, or interfaces/contracts of one family | R3 switcher (+ R12 code) |
| Steps or items with a classification (deterministic / AI / human…) | R4 filtered classified table |
| Architecture diagram, module list, system map | R5 explorer (lanes + detail panel) |
| Named pipeline or loop | R6 steps |
| Outcome taxonomy, maturity levels, severity scale | R7 ladder (`.rung--trap` for misleading categories) |
| "X goes to Y" rules, ownership, routing | R8 routes |
| Swap-out or "what if" scenarios | R9 scenario selector |
| Roadmap, phases, history | R10 timeline (`.phase--key` for where to start) |
| Rules, warnings, caveats, decisions for humans | R11 callouts |
| Interfaces, schemas, commands | R12 code |
| Composite definitions plus examples | R13 tuple + variants |
| Open questions, assumptions | R14 open questions |
| Risk or status registers | R15 status table |
| The single most important figure | Hero key figure with a unit grid |

Mermaid or diagram code in the source turns into an R5 explorer or R6 steps. Don't paste the diagram source itself.

---

## 3. Page structure

1. **Hero:** an eyebrow (document type and context), the subject's name as `h1`, a 2–3 sentence thesis, the companion link (both mode), the theme toggle, and the key figure if the source has one.
2. **Contents rail:** built automatically from the sections, using the source's own numbering.
3. **Sections:** one per source section, in source order. Each has an eyebrow (`N · Source section name`), an `h2` stating the section's claim in plain words, short prose, then components. Long source sections can contain several components. Combine source sections only when one is a stub.
4. **Footer:** the source title, an evidence-quality note, and any data conflicts.

Aim for 8–16 sections. If the source has more, group its smallest neighboring sections under one heading and keep their numbers in the eyebrow (e.g. `12–13 · …`).
