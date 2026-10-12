# Changelog

## 0.3.0 — 2026-10-12
Prepared for publishing on GitHub as `elmiller9/systems-explainer`.
- The repository is now a marketplace (`elmiller9`) with the plugin in `plugins/systems-explainer/`. Only that folder is installed, so local source analyses and test pages can't be shipped by mistake.
- MIT license. Personal details removed from the manifests and docs; author and owner are the GitHub account.
- `update-playbook` saves new analyses outside the plugin folder.
- README rewritten for public install from GitHub, with a separate local-development section.

## 0.2.2 — 2026-10-12
- Installed and verified with Claude Code 2.1.296 (VS Code extension's bundled CLI): `plugin validate` passes, the plugin is enabled at user scope and read in place, and all three skills load from another folder with their paths filled in.
- Added a marketplace description (cleared the validator warning). Rewrote the README install section for the VS Code extension, which has no `/plugin` command: bundled CLI, a hand-edited settings method, verification, troubleshooting and uninstall.
- `.gitignore`: `sources/` is now local-only (third-party transcripts and private research), except `sources/README.md`. Also ignores Python caches, virtualenvs, local Claude settings, screenshots, and editor and OS files.
- `sources/README.md` explains the folder and keeps the analysis prompt, so the README no longer points at an ignored file.

## 0.2.1 — 2026-10-12
Pre-production review.
- **Skills resolve their files from any project.** The three `SKILL.md` files now point at `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_SKILL_DIR}` (substituted by Claude Code when a plugin skill loads) instead of paths relative to the skill folder, which only worked when the current directory happened to be inside the plugin.
- New `scripts/check_page.py`: one command for the mechanical pre-handover checks on a generated page (placeholders, token block, literal colors, external requests, inline-script parse, title). Both skills and both checklists call it; the old instruction to run `sync_tokens.py --check` after building a page checked the templates, not the page.
- `scripts/sync_tokens.py` accepts page paths, so a page can be checked or re-synced after a token change. The example page gained `TOKENS:BEGIN/END` markers and is in sync (it had the pre-0.2.0 palette without ochre and the semantic roles).
- `marketplace.json`: plugin source is `.`, the documented form for a plugin at the marketplace root. README explains in-place loading (`/reload-plugins`, no reinstall) and `claude plugin validate .`.
- Playbook consistency: `visual-language.md` §2 lists ochre, grid-dot, on-accent and the semantic aliases and says tokens come from `shared/tokens.css`; `method.md` §4 uses the same 1366×670 viewport figure as everything else.
- Reference template and R5 explorer: the detail panel is a `div` holding `dl`s (a heading inside `dl` is invalid HTML). Blueprint template: the theme toggle no longer throws if its button is removed.

## 0.2.0 — 2026-10-12
Two companion versions sharing one palette, prompted by comparing the plugin's explainer with a plain reference-style page for the same research.
- New `reference-guide` skill (the detailed version): method, source-to-component mapping, checklist, template with a contents rail and generic switch, filter and explorer hooks, and component library R1–R15.
- `shared/tokens.css` is the single source for color and type. `scripts/sync_tokens.py` copies it into both templates. Added semantic roles (ok, gap, ai, human) and an ochre token for human decisions.
- `shared/versions.md`: how to choose a version, plus the both-mode workflow (one fact inventory, reference first, cross-links, consistency check).
- `blueprint-explainer`: version choice, both mode, a companion link to the reference in the final zone, and a 1366×670 viewport rule.
- `update-playbook` routes new learning to the right version, or to the shared tokens.
- Reference template fixes found in testing: `[hidden]` now wins over component `display` rules, and component grid children can shrink so wide tables don't stretch the page.

## 0.1.1 — 2026-10-12
Lessons from the first real test (a dense reference architecture on threat-informed defense):
- Template: added a compact mode for short laptop viewports (`max-height: 820px`). The number sits beside the title and type and padding tighten. A 1366×768 screen only leaves about 670 px of viewport.
- Template: zone diagrams auto-fit their viewBox to the drawn content, so labels in split zones stay legible.
- Playbook: visual-language and checklist now say to measure against a 1366×670 viewport and check the rendered label size.

## 0.1.0 — 2026-10-12
- First version of the playbook, distilled from four explainer-video analyses (kept locally, not published).
- `blueprint-explainer` skill: four narrative arcs (pieces, loop, build order, taxonomy), a table of 17 rhetorical devices, a metaphor dictionary, and a desktop-first template with a minimap rail, keyboard stepping, draw-in and pop-in motion, and dark mode.
- Component library: 13 SVG diagrams and 8 HTML mock-ups.
- `update-playbook` skill for folding in new sources and corrections.
- Example page: `examples/systems-explainer-tour.html`.
