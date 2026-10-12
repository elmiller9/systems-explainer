---
name: blueprint-explainer
description: Builds the educational version, a single-page, laptop-screen explainer that teaches any system, process or concept "blueprint style". It uses numbered zones, a count stated up front, physical-object diagrams, one-line rules and a closing loop-back, in a retro-instruction-manual look (cream, charcoal, terracotta). Use when the user asks to explain, break down, give an overview of, or teach how something works as a page, explainer, one-pager, infographic or "systems view". It works for AI, business operations, engineering or any other domain. Its detailed companion is the reference-guide skill; use both when the user wants an educational and a detailed version.
---

# Blueprint Explainer

Turn a topic into a self-contained HTML page that teaches it as a **system**: the parts, the connections between them, and why the whole thing works. The page is designed for **laptop and desktop screens** (landscape, 1280–1920 px). It's one continuous canvas of full-screen numbered zones, with a minimap rail and keyboard stepping.

It is the **educational** version. Its detailed companion is the `reference-guide` skill. Both share the palette in `${CLAUDE_PLUGIN_ROOT}/shared/tokens.css`.

## Where the files are
This skill's folder is `${CLAUDE_SKILL_DIR}` and the plugin root is `${CLAUDE_PLUGIN_ROOT}`. Those are absolute paths, substituted when the skill loads. Use them in every file read and command below; the current working directory is the user's project, not the plugin.

## Before you start: read the playbook
- `${CLAUDE_PLUGIN_ROOT}/shared/versions.md`: which version to build, and the **both mode** workflow. **Always read it.** If the request doesn't say which version, ask once (educational, detailed, or both).
- `${CLAUDE_PLUGIN_ROOT}/shared/motion.md`: the motion grammar (M1–M6), its test and its budget. Read it before adding any motion; motion is optional and must pass the test.
- `${CLAUDE_SKILL_DIR}/references/method.md`: the principles, the rhetorical devices and the four narrative arcs. **Always read it.**
- `${CLAUDE_SKILL_DIR}/references/visual-language.md`: layout, color tokens, type, the metaphor dictionary and the diagram and motion rules. **Always read it.**
- `${CLAUDE_SKILL_DIR}/references/content-brief.md`: the brief and zone-script format.
- `${CLAUDE_SKILL_DIR}/references/quality-checklist.md`: the pre-handover checks.
- `${CLAUDE_SKILL_DIR}/assets/template.html`: the page skeleton. Copy it and never edit it in place.
- `${CLAUDE_SKILL_DIR}/assets/components.html`: the diagram and UI snippet library (S1–S13 SVG, H1–H8 HTML).

## Workflow

1. **Brief.** Get the topic, audience and source material from the request, files or links. Read any sources fully. If the audience or the goal is genuinely unclear, ask at most two questions. Otherwise fill in the brief from `content-brief.md` in your own notes and keep going.
2. **Choose the arc and the count.** Pick one arc (A pieces · B loop · C build order · D taxonomy) using the "Choosing" rules in `method.md`. Settle the count (3–5) and its noun before writing anything else.
3. **Script every zone** in the zone-script format: number, title, layout (split / flip / wide / statement), lede, points, diagram (named from the metaphor dictionary or a component ID), and an original aphorism. Make sure the arc's required beats are present: the hook, the count, the hard part, the copyable asset, the synthesis, the caveat and the loop-back. Aim for 8–14 zones. End with a recap and "start with piece one", never with a pitch.
4. **Build.** Copy `${CLAUDE_SKILL_DIR}/assets/template.html` to the output path. Replace the sample zones with your scripted zones, composing diagrams from `components.html` and adjusting the coordinates to the content. Put page-specific CSS only in section 8 of the template, using tokens only. Replace every `{{…}}` placeholder. Leave the `TOKENS:BEGIN … TOKENS:END` block exactly as copied.
   - Output path: the one the user gives, otherwise `./explainers/<topic-slug>.html` in the current working directory. In both mode, use `<slug>-explainer.html` beside `<slug>-reference.html`.
   - Both mode: work from the fact inventory already built for the reference (same thesis, figures and terms), and end the final zone's text with `<a class="companion-link" href="<slug>-reference.html">Go deeper: the full reference →</a>`.
5. **Check.** Go through `${CLAUDE_SKILL_DIR}/references/quality-checklist.md` item by item and fix any failures. Then:
   - Run `python ${CLAUDE_PLUGIN_ROOT}/scripts/check_page.py <file>`. It checks placeholders, the token block, literal colors, external requests, the inline script and the title. Every line must say PASS.
   - Look at the page at about 1366×670, the viewport a 1366×768 laptop actually shows: every zone should fit on one screen and every diagram should be legible. Use a browser tool if one is available. Otherwise take a headless screenshot, for example on Windows `& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --window-size=1366,670 --screenshot=<png> "file:///<file>"` (Chrome takes the same flags), and read the image. If you can, also check dark mode and a narrow window.
6. **Hand over.** Give the file path in one line, the arc and count used in one line, and offer once to publish it as a private claude.ai Artifact. If the user accepts, load the `artifact-design` skill and publish the file (icon: `diagram`).
7. **Learn.** When the user corrects the result, fix the page, then ask: *"Does this correction belong in the playbook?"* If it's a general rule rather than a one-off, add it to the right reference file under `${CLAUDE_SKILL_DIR}/references/` (a new metaphor goes in `visual-language.md` §5, a new device or arc goes in `method.md`, a new check goes in `quality-checklist.md`) and add a line to `${CLAUDE_PLUGIN_ROOT}/CHANGELOG.md`.

## Non-negotiables
- One idea per zone, and every abstract concept is drawn as a physical object.
- Laptop-first: every zone fits in a 1366×670 viewport (a 1366×768 laptop after browser toolbars) without scrolling inside the zone. If it doesn't fit, cut text or split the zone.
- The page is flat and uses only the shared tokens (synced from `shared/tokens.css`, never edited in the template or the page): no gradients, no blur, no pure black and no hex colors inside the SVG.
- The single HTML file is self-contained (Google Fonts is the only external request), with inline SVG and no images.
- Wording is original. Don't reproduce source transcripts or another creator's phrases, names, branding, characters or sales calls to action. Source material is for facts and structure only.
- No presenter character or persona. The voice is calm, second-person instruction with brief first-person proof only where the user supplies real proof.
