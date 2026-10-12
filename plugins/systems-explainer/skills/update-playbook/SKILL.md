---
name: update-playbook
description: Folds new learning into the systems-explainer playbooks (the educational blueprint explainer and the detailed reference guide). Use when the user provides a new analysis of an explainer video, article, reference page or documentation site (a file, a URL they've analyzed, or pasted notes), or a batch of corrections, and wants the useful patterns (narrative arcs, rhetorical devices, metaphors, diagram components, visual rules, checks) merged into the right playbook. Also use when they say "add this to the playbook", "learn from this analysis" or "update the explainer skill".
---

# Update the Playbook

Both page types (the educational explainer and the detailed reference) should get better each time the plugin is fed a new source. This skill turns a new analysis into precise edits to the playbook, without bloating it or copying anyone's content.

## Where the files are
The plugin root is `${CLAUDE_PLUGIN_ROOT}` (an absolute path, substituted when the skill loads). Every path below is relative to it. When the plugin is loaded in place from a local marketplace, that root *is* the source repository, so edits persist and take effect after `/reload-plugins`. If the root is a copy inside the plugin cache instead, edit the source repository the user points you to, not the cache.

**Educational version (blueprint explainer)**
- `skills/blueprint-explainer/references/method.md`: principles, devices table, arcs
- `skills/blueprint-explainer/references/visual-language.md`: layout, type, metaphor dictionary §5, diagram rules §6, motion §7
- `skills/blueprint-explainer/references/quality-checklist.md`
- `skills/blueprint-explainer/assets/components.html`: new reusable diagrams (plus CSS in `template.html` §5b if needed)

**Detailed version (reference guide)**
- `skills/reference-guide/references/method.md`: principles, the source-to-component mapping, page structure
- `skills/reference-guide/references/quality-checklist.md`
- `skills/reference-guide/assets/components.html` (plus CSS in its `template.html` §5)

**Shared**
- `shared/tokens.css`: colors and fonts for **both** versions. After editing it, run `python ${CLAUDE_PLUGIN_ROOT}/scripts/sync_tokens.py`. Never edit the TOKENS blocks inside the templates.
- `shared/versions.md`: when to build which version, and the both-mode workflow
- `scripts/check_page.py`: the pre-handover page checks. A new mechanical check goes here; a judgment check goes in a checklist.
- `CHANGELOG.md` and `.claude-plugin/plugin.json` (version)

## Workflow

1. **Ingest.** Read the new material in full. If it's a new source analysis, save a copy in a `sources/` folder **outside the plugin**, never under `${CLAUDE_PLUGIN_ROOT}`. In the systems-explainer repository that's the top-level `sources/` (two levels above the plugin root). Anywhere else, use `sources/` in the user's current project. Give it a descriptive name (e.g. `sources/2026-10-channel-topic.md`), unless it's already there. That folder is git-ignored (third-party transcripts stay local), so the playbook must never depend on a file in it.
2. **Read the current playbook** (the files above for the version or versions affected) so you know what already exists.
3. **Decide which version each candidate serves.** A teaching move (hook, metaphor, arc) goes to the explainer. A way of presenting detail (table pattern, explorer, filter) goes to the reference. Color and type go to `shared/tokens.css`.
4. **Extract candidates** into these buckets. For each, note the evidence (which source, which section):
   - **Arc**: a zone sequence not covered by arcs A–D.
   - **Device**: a rhetorical move not in the devices table.
   - **Metaphor**: a concept → object mapping not in §5.
   - **Component**: a diagram shape worth making reusable.
   - **Visual rule**: a palette, type, layout or motion rule that differs from or sharpens the current one.
   - **Check**: something that should be verified before handover.
5. **Filter hard.** Keep a candidate only if it's (a) genuinely new or meaningfully sharper than what's there, (b) reusable across topics, and (c) compatible with the laptop-first, flat, no-persona, no-pitch rules. Drop anything tied to one creator's branding, characters, catchphrases or sales funnel. If a new source *conflicts* with the current playbook, don't overwrite silently; list the conflict for the user.
6. **Write in our own words.** Describe each pattern abstractly, and give each one an **original** example. Never paste transcript lines, aphorisms or titles from the source into the playbook.
7. **Show the diff plan** to the user as a short list ("method.md: +1 device 'X'; visual-language.md: +2 metaphors; checklist: +1 check; conflicts: …") and apply it once they agree. For small additions (3 items or fewer, no conflicts) just apply them and report afterwards.
8. **Apply the edits** surgically, matching each file's existing format (table rows, numbered arcs, checklist boxes). New components must follow the rules at the top of `components.html` and use only token classes.
9. **Version and log.** Bump `version` in `.claude-plugin/plugin.json`: patch for wording or checks, minor for a new arc, component or metaphor batch. Add a dated entry at the top of `CHANGELOG.md` listing what changed and from which source.
10. **Sanity check.** Run `python ${CLAUDE_PLUGIN_ROOT}/scripts/sync_tokens.py --check`. If a component or template CSS changed, build a quick throwaway page from the template using the new pieces, run `check_page.py` on it, open it to confirm it renders in light and dark, then delete it.

## Corrections as input
When the input is a set of user corrections from real explainers (not a source analysis), treat each one as a candidate **check** or **rule**. Corrections that apply everywhere belong in the playbook. One-off taste calls for a single page don't.
