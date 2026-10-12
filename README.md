# systems-explainer

A Claude Code plugin that turns any topic or source document into single-page web apps, in two companion versions that share one palette:

- **Educational: blueprint explainer.** A laptop-screen canvas of full-screen numbered zones with a minimap rail and keyboard stepping. It teaches the topic as a *system* (the parts, the connections, why the whole works) using object diagrams and one-line rules.
- **Detailed: reference guide.** An interactive reference that keeps nearly all of a source document in its own section order. It has a contents rail, tables, switchable views, filters, an architecture explorer, taxonomies, scenarios and a roadmap.
- **Both.** Built from one reading of the source and linked to each other. The explainer is the front door, and the reference is the manual behind it.

Pages are self-contained HTML files with light and dark themes. Optional, reader-driven motion ("simulate a case" buttons that show which outcome a scenario produces, and architecture maps that light up what a part connects to and why) follows a small motion grammar. Every page reads completely without it, and with reduced motion. Open them in a browser, or publish them wherever you host static pages.

See [`examples/systems-explainer-tour.html`](examples/systems-explainer-tour.html) for a finished explainer: a tour of this plugin, built with this plugin. Download it and open it in a browser.

---

## Install

### In Claude Code (terminal)

```
/plugin marketplace add elmiller9/systems-explainer
/plugin install systems-explainer@elmiller9
```

### In the VS Code extension

`/plugin` (singular) isn't available in the extension. Type **`/plugins`** (plural) to open **Manage plugins**:

1. On the **Marketplaces** tab, add `elmiller9/systems-explainer`.
2. On the **Plugins** tab, find `systems-explainer` and choose **Install for you**.
3. Start a new conversation, or run `/reload-plugins`.

### With the CLI

```
claude plugin marketplace add elmiller9/systems-explainer
claude plugin install systems-explainer@elmiller9
```

On Windows, the VS Code extension ships with the CLI even when `claude` isn't on your PATH:

```powershell
$claude = Get-ChildItem "$env:USERPROFILE\.vscode\extensions\anthropic.claude-code-*\resources\native-binary\claude.exe" |
          Sort-Object LastWriteTime | Select-Object -Last 1 -ExpandProperty FullName
& $claude plugin marketplace add elmiller9/systems-explainer
& $claude plugin install systems-explainer@elmiller9
```

### With settings

Add these keys to `~/.claude/settings.json`, merging with what's already there, then start a new conversation:

```json
{
  "extraKnownMarketplaces": {
    "elmiller9": { "source": { "source": "github", "repo": "elmiller9/systems-explainer" } }
  },
  "enabledPlugins": { "systems-explainer@elmiller9": true }
}
```

### Check that it worked

`claude plugin list` shows `systems-explainer@elmiller9` as enabled. In a new conversation, three skills appear: `systems-explainer:blueprint-explainer`, `systems-explainer:reference-guide` and `systems-explainer:update-playbook`.

To update later, run `/plugin marketplace update elmiller9` (or `claude plugin marketplace update elmiller9`). To remove the plugin, run `claude plugin uninstall systems-explainer@elmiller9`.

---

## Use

| Skill | Call it with | What it does |
|---|---|---|
| `blueprint-explainer` | `/systems-explainer:blueprint-explainer <topic>, for <audience>`, or "explain X as a blueprint page" | The educational version. It picks a narrative arc and a count, scripts every zone, builds the page from a template, checks it, and offers to publish it. |
| `reference-guide` | `/systems-explainer:reference-guide <source file>`, or "make a detailed reference of X" | The detailed version. It keeps the source's order and terms, covers nearly everything, turns tables into interactive views, and flags contradictions it finds in the source. |
| `update-playbook` | `/systems-explainer:update-playbook <path to an analysis or notes>` | Folds new patterns, or your corrections, into the right playbook (see [Development](#development)). |

To get **both**, ask for them together, for example "make the explainer and the reference for `research.md`". You get `<slug>-explainer.html` and `<slug>-reference.html`, linked to each other. If you don't say which version you want, the skill asks.

Pages are written to `./explainers/` in your current project unless you give a path.

---

## How it works

The educational version follows a teaching method built from studying short explainer videos that make complicated systems easy to follow:
- State the count up front ("it's four pieces").
- Give one idea per screen, and draw every abstract concept as a physical object (doors for access, shelves for layers).
- Slow down at the part people get wrong, and give one quotable rule per zone.
- End on the opening diagram, now complete.

The detailed version keeps the substance of the source, then makes it navigable.

Both versions share one set of design tokens (warm paper, charcoal ink, a terracotta accent) and the same semantic colors: verified, gap, AI-assisted and human decision.

## Repository layout

```
.claude-plugin/marketplace.json     the "elmiller9" marketplace (lists the plugin below)
plugins/systems-explainer/          the plugin; the only folder that gets installed
  .claude-plugin/plugin.json
  skills/blueprint-explainer/       educational version: method, visual language, template, 13 SVG + 8 HTML components
  skills/reference-guide/           detailed version: method, template, components R1–R15
  skills/update-playbook/           the improvement loop
  shared/tokens.css                 the one palette + type for both versions
  shared/versions.md                choosing a version; the both-mode workflow
  shared/motion.md                  the motion grammar (M1–M6): when motion earns its place
  shared/motion.css, motion.js      the motion runtime, synced into both templates
  scripts/sync_tokens.py            copies shared tokens into the templates (--check to verify)
  scripts/check_page.py             pre-handover checks for a generated page
  CHANGELOG.md
examples/                           finished example pages (not installed)
sources/                            your local source analyses (git-ignored except its README)
LICENSE
```

---

## Development

To change the plugin, work from a clone and install it from the local folder. A local marketplace is read in place, so edits apply at the next conversation or after `/reload-plugins`, with no reinstall.

```
git clone https://github.com/elmiller9/systems-explainer.git
claude plugin marketplace add ./systems-explainer
claude plugin install systems-explainer@elmiller9
claude plugin validate ./systems-explainer
```

If you already installed the GitHub version, remove it first (`claude plugin marketplace remove elmiller9`), since both use the marketplace name `elmiller9`.

**Changing the palette.** Edit `plugins/systems-explainer/shared/tokens.css`, then run:

```
python plugins/systems-explainer/scripts/sync_tokens.py
python plugins/systems-explainer/scripts/sync_tokens.py examples/systems-explainer-tour.html
```

Never edit the `TOKENS:BEGIN … TOKENS:END` blocks in the templates or pages directly.

**Checking a page.** Run `python plugins/systems-explainer/scripts/check_page.py <page>.html`. Every line should say PASS. To see a real laptop viewport (1366×768 leaves about 670 px of page), take a headless screenshot: `msedge --headless=new --window-size=1366,670 --screenshot=out.png file:///<path>` (Chrome takes the same flags).

**Growing the playbook.**
1. Analyze an explainer you admire. [`sources/README.md`](sources/README.md) has a prompt for breaking down a video.
2. Save the analysis in `sources/` and run `update-playbook` on it. It describes patterns in its own words and never copies the source.
3. When you correct a generated page, say whether the correction is a general rule. If it is, it goes into the playbook.

`sources/` stays out of git (except its README), so third-party transcripts and private material are never published, and the plugin never depends on them.

## License

[MIT](LICENSE)
