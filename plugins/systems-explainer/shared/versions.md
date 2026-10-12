# Choosing a Version, and Building Both

The plugin makes two companion pages from the same source. They share colors, fonts and semantic meaning, and differ in purpose, layout, content and voice.

| Version | Skill | Use it when the reader needs to… |
|---|---|---|
| **Educational**: blueprint explainer | `blueprint-explainer` | understand the idea and buy into it: onboarding, leadership briefings, persuasion |
| **Detailed**: reference guide | `reference-guide` | work from the material: build, review, audit, compare options |
| **Both** | either skill, in both mode | reach both audiences. The explainer is the front door, and the reference is the manual behind it. |

## If the request doesn't say which
Ask one question with three options (educational, detailed, or both) and recommend **both** for dense technical sources. Skip the question when the wording makes it obvious: "teach / explain / overview / one-pager" means educational, and "reference / detailed / everything in it / for the engineers" means detailed.

## Both mode workflow
1. **Read the source once, and build one fact inventory** (in your working notes, not on the page):
   - Every section with its number and title.
   - Every figure, ID, version and name, as written.
   - Every table, list, interface, scenario and phase.
   - The thesis in one sentence.
   - **Conflicts:** contradictory figures and unsupported claims, and which figure both pages will use.
2. **Build the reference guide first** from the inventory (`reference-guide` skill). It forces full coverage and catches conflicts early.
3. **Build the explainer** from the same inventory (`blueprint-explainer` skill). Select the arc and the 10–15 ideas from material already checked.
4. **Cross-link them.**
   - Name the files `<slug>-explainer.html` and `<slug>-reference.html` in the same folder.
   - The reference hero has `Start with the visual explainer →` linking to the explainer.
   - The explainer's final zone ends with a `Go deeper: the full reference →` link (class `companion-link`, see the explainer template).
5. **Check consistency.** The thesis, the count, key figures and terms must match across both pages. If the explainer simplifies a term, the reference uses the full term and introduces the simple one once.

## Publishing both
Local relative links work as-is. If both are published as claude.ai Artifacts, publish the reference first, then replace the explainer's companion link with the reference's Artifact URL (and vice versa), and republish both.
