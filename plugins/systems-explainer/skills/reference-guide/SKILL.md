---
name: reference-guide
description: Builds the detailed companion to a blueprint explainer. It's a single-page interactive reference that keeps nearly all of a source document (architecture, research report, specification, runbook) in its own section order, with a contents rail, data tables, switchable views, filterable classified lists, an architecture explorer, taxonomies, scenario selectors and a roadmap timeline. It uses the same palette and type as the explainer. Use when the user wants a detailed, reference, deep-dive or "everything in it" page for engineers, reviewers or auditors, or asks for both the educational and the detailed version.
---

# Reference Guide

Turn a dense source into a self-contained HTML reference that people can **work from**: look things up, compare options, filter, and check exact figures. It's the detailed companion to the `blueprint-explainer` page. It has the same colors, fonts and semantic meanings, and a different layout, density and voice.

## Where the files are
This skill's folder is `${CLAUDE_SKILL_DIR}` and the plugin root is `${CLAUDE_PLUGIN_ROOT}`. Those are absolute paths, substituted when the skill loads. Use them in every file read and command below; the current working directory is the user's project, not the plugin.

## Before you start
- `${CLAUDE_PLUGIN_ROOT}/shared/versions.md`: which version to build, and the **both mode** workflow. **Always read it.** If the request doesn't say which version, ask once (educational, detailed, or both).
- `${CLAUDE_SKILL_DIR}/references/method.md`: principles, the source-to-component mapping and page structure. **Always read it.**
- `${CLAUDE_SKILL_DIR}/references/quality-checklist.md`: the pre-handover checks.
- `${CLAUDE_SKILL_DIR}/assets/template.html`: the page skeleton with the shared tokens and generic script. Copy it and never edit it in place.
- `${CLAUDE_SKILL_DIR}/assets/components.html`: snippets R1–R15.

## Workflow
1. **Read the whole source** and build the fact inventory described in `shared/versions.md`: sections, figures, tables, interfaces, scenarios, phases, the thesis, and **conflicts**.
2. **Plan the sections.** Keep one section per source section, in order, and pick components for each using the mapping table in `method.md`. Write a plain-language claim for each `h2`.
3. **Build.** Copy `${CLAUDE_SKILL_DIR}/assets/template.html` to the output path and fill the hero, sections and footer from the components. Keep all content in the markup. Put page-specific CSS only in section 7, using tokens only. Replace every `{{…}}`. Leave the `TOKENS:BEGIN … TOKENS:END` block exactly as copied.
   - Output path: the user's choice, otherwise `./explainers/<slug>-reference.html` in the current working directory (with `<slug>-explainer.html` for the companion in both mode).
   - Without a companion, remove the companion link from the hero.
4. **Check.** Go through `${CLAUDE_SKILL_DIR}/references/quality-checklist.md`. Run `python ${CLAUDE_PLUGIN_ROOT}/scripts/check_page.py <file>` (placeholders, token block, literal colors, external requests, inline script, title) and make every line PASS. Spot-check five figures against the source. Take one look at the rendered page (a browser tool if available, otherwise one headless screenshot: on Windows `& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --window-size=1366,670 --screenshot=<png> "file:///<file>"`), fix what it shows, and don't loop.
5. **Hand over.** Give the path, the section count, any data conflicts found, and offer once to publish it as a private claude.ai Artifact. If the user accepts, load `artifact-design` and publish (icon: `book`).
6. **Both mode.** Then build the explainer with the `blueprint-explainer` skill from the same inventory, and cross-link the two as described in `shared/versions.md`.
7. **Learn.** When the user corrects a reference page, ask whether the correction belongs in the playbook. If it does, update `${CLAUDE_SKILL_DIR}/references/method.md`, `${CLAUDE_SKILL_DIR}/assets/components.html` or the checklist, and log it in `${CLAUDE_PLUGIN_ROOT}/CHANGELOG.md`.

## Non-negotiables
- Source order, source numbering and source terms. Never invent figures, examples or vendors.
- Name contradictions in the source openly. Never quietly pick one.
- Use the same tokens as the explainer, synced from `shared/tokens.css`. Never use literal colors.
- The page is complete without script. Every table scrolls inside its own container, and nothing makes the page scroll sideways at 400 px.
- Plain, active prose. No aphorisms, presenter persona or sales pitch.
