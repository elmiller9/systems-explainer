# Visual Language: Retro Instruction Manual × System Blueprint

Calm, flat and structural. It should feel like a well-made equipment manual crossed with an engineer's whiteboard, and never like a neon tech landing page.

---

## 1. Canvas & layout (desktop-first)

- **Target screens:** laptop and desktop, 1280–1920 px wide. Design at 1440×900, and check at 1366×768 and 1920×1080.
- **Real viewport height is smaller than the screen.** A 1366×768 laptop leaves about **650–670 px** of viewport once the browser's toolbars are counted. The template has a compact mode for `max-height: 820px` (number beside the title, tighter type and padding). Still, measure each zone against a 670 px viewport, not 768.
- **The canvas** is one continuous page split into full-viewport **zones** (`min-height: 100vh`), with gentle scroll-snap so each zone settles like a camera stop.
- **Zone composition (default "split"):**
  - Left column, about 38%: zone number, title, lede, points, aphorism.
  - Right column, about 62%: one large diagram in inline SVG with a wide viewBox (960×540 by default).
  - Alternate it with `zone--flip` (diagram left, text right) every few zones to vary the rhythm. Don't alternate every zone.
- **Other zone layouts:**
  - `zone--wide`: the title runs across the top and the diagram spans full width underneath. Use it for big flowcharts, timelines, synthesis and the loop-back.
  - `zone--statement`: one large aphorism or count ("IT'S FOUR.") centered, with a small diagram or none. Use it at most twice per page.
- **Minimap rail:** a fixed left rail (about 220 px) lists every zone as `01 TITLE`. The current zone is highlighted in the accent color with a filled marker. Clicking an item scrolls to it. The rail shows the whole system at all times.
- **Keyboard:** ↓ / → / PageDown / Space go to the next zone, ↑ / ← / PageUp / Shift+Space go to the previous one, and Home / End jump to the first or last.
- **Progress:** a thin accent bar along the top edge shows scroll progress.
- **Narrow fallback (< 900 px):** the rail turns into a compact top strip, the zones stack text above diagram, there's a 16 px side gutter, and nothing scrolls horizontally. It's acceptable rather than optimized, since laptops are the target.

---

## 2. Color tokens

The tokens live in `shared/tokens.css` at the plugin root and are copied into the template between the `TOKENS:BEGIN … TOKENS:END` markers by `scripts/sync_tokens.py`. Edit the shared file, never the block in the template or in a page. Light and dark values are both defined there.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#F3EBE0` | `#1D1A17` | page background (warm cream / warm charcoal) |
| `--card` | `#FFFDF8` | `#272320` | UI boxes and diagram node fill |
| `--ink` | `#222222` | `#EDE4D6` | text, lines, borders (**never pure black**) |
| `--ink-soft` | `#5B5550` | `#B3A898` | secondary text, captions |
| `--rule` | `#CFC4B4` | `#4A433C` | faint guides, dotted alignment lines, grid |
| `--accent` | `#C55A44` | `#E07A62` | terracotta: zone numbers, key line, highlight, the one thing to notice |
| `--accent-2` | `#D97746` | `#EB9563` | burnt orange: a second series |
| `--accent-3` | `#8C3B2D` | `#C9705E` | deep brick: a third series |
| `--olive` | `#6F7F4E` | `#9DB07A` | "good / allowed / works" |
| `--slate` | `#4E6A80` | `#8FB0C8` | neutral system element, a fourth series |
| `--ochre` | `#9A6A12` | `#E0B04A` | human decision / judgment |
| `--muted-fill` | `#E8DFD2` | `#332E29` | grayed-out "wrong path" fill |
| `--grid-dot` | `#E2D7C6` | `#2B2723` | the blueprint dot grid on the page background |
| `--on-accent` | `#FFFDF8` | `#1D1A17` | text on accent fills |

Semantic aliases also exist and mean the same thing on both page types: `--ok` (olive: verified, allowed), `--gap` (accent: gap, risk, forbidden), `--ai` (slate: AI-assisted) and `--human` (ochre: human decision), each with a pale `--tint-*` for fills. Use them when a diagram shows a status rather than a series.

**Rules**
- There's one accent per idea. In any zone, terracotta marks **the one thing the reader must notice**. Everything else is ink.
- Pale tag fills (pale red, green, blue at about 20% strength) are only for distinguishing categories, such as the columns of a file tree.
- When several series need colors (like the synthesis lines), use accent → accent-2 → accent-3 → slate, and always add text labels too. Color is never the only signal.

---

## 3. Typography

Load these from Google Fonts. The template already links them.

| Role | Font | Fallback | Style |
|---|---|---|---|
| Zone numbers, titles, statements | **Bebas Neue** | Anton, "Arial Narrow", sans-serif | ALL CAPS, tight leading (0.95), huge numbers |
| Labels, UI text, code, captions | **Space Mono** | "Courier Prime", ui-monospace, monospace | ALL CAPS for labels with +0.06em tracking; sentence case for body inside mock UIs |
| Body copy (lede, points) | **IBM Plex Sans** | system-ui, sans-serif | sentence case, 18–20 px on desktop, line-height 1.5 |

**Scale (desktop):** zone number 96–128 px in the accent color, zone title 56–72 px, lede 20 px, points 18 px, labels 12–13 px mono caps. Use `clamp()` so it scales down gracefully.

---

## 4. Shape & surface rules

- **Flat only.** No gradients, glows, blur or glassmorphism.
- **Borders:** 2.5–3 px `--ink` on cards and nodes. Use 2 px for secondary elements.
- **Corners:** 6–10 px radius on UI boxes, full pill shape on tags, and square corners on "paper" objects like checklists and index cards.
- **Shadows:** solid offset block shadows only (`box-shadow: 5px 5px 0 var(--ink)`), never blurred.
- **Lines:** uniform stroke width (3 px main, 2 px secondary), with round caps and simple arrowheads. Dashed lines mean "boundary / container / optional / references" and solid lines mean "flows into".
- **Section divider:** a thick 3 px rule under each zone header.
- **Background texture:** optional faint dot grid in `--rule` at low opacity, to suggest blueprint paper.

---

## 5. Metaphor dictionary (concept → object)

Find the concept, then draw the object. Add new rows as topics demand; this table is meant to grow.

| Concept | Object to draw | Notes |
|---|---|---|
| Integration / connection / access to a tool | **Door** with a knob and a label pinned on it | Permissions go on a checklist taped to the door. Read-only is a padlock badge. |
| Permissions / scopes | **Checklist card** with ✓ and ✗ items | Put the forbidden item in the accent color with ✗. |
| Knowledge base / reference data | **Shelf** of labeled jars or books, or a **library** | "Search by meaning" is a lens over the shelf. |
| Organized repository | **Folder split into 3 zones**: raw → organized → index | Draw lines from the raw files to the organized nodes. |
| Index / table of contents | **Short bulleted card** at the folder's front | "Read first" badge. |
| Procedure / recipe / SOP | **Notepad or recipe card**: needs / steps / checks | A three-column card layout. |
| Correction / revision | **Pencil striking through** text and rewriting it | Strike-through in the accent color. |
| Memory that persists | **Index card** or **labeled file** (`memory.md`) | Dashed lines drop from it to the places that read it. |
| Temporary / volatile state | Items **dropping into a dark "GONE" box** | Good for anything that evaporates. |
| Compression / summarization | **Stack of pages squeezed** into one sheet | "10 notes → 1 rule". |
| Layers / dependencies | **Isometric shelves** stacked bottom-up and numbered | Add an upward arrow for the build order. |
| Decision / filter / rule | **Logic gate**: a diamond with a question in it | "Yes" passes through, "No" gets grayed out. |
| Routing / choosing a path | **Branching track**, with the wrong branch grayed and the right one in the accent color | |
| Process over time / incident | **Horizontal timeline** with dated nodes | The bad outcome node gets the accent color. |
| Cycle / loop / flywheel | **Circle of numbered stations** with arrows | 3–5 stations. |
| Many outputs from one source | **Bracket `}` fanning out** to stacked boxes | Use it for the hook diagram. |
| Autonomy level / trust | **Gauge** with a needle, plus a **rubber stamp** for the number | |
| Human approval / oversight | **Review queue** UI: Approve / Edit / Skip | |
| Comparison | **Two side-by-side cards** ("without" / "with"), one grayed out | |
| Confused vocabulary | **Three identical cards in a row** on a dotted baseline | Each has an icon, a term, a one-line definition and a tiny footer. |
| Exact instruction / asset | **Terminal or chat mock** showing the exact text | Monospace with a `>` prompt. |
| Real-world proof | **File tree** with named files and sizes | Pale tag headers for each owner. |
| Growth vs stagnation | **Line chart**: a flat line next to a compounding curve | Two labeled lines and no axes clutter. |
| Synthesis | **One request at the top**, **one output at the bottom**, and **colored lines from each part** to the bit of the output it shaped | A legend of tags on the left. |

---

## 6. Diagram construction rules

- **Inline SVG**, `viewBox="0 0 960 540"` (16:9) by default, or `0 0 960 400` for strips. Use `width: 100%` with no fixed height.
- Style everything through CSS classes that read the tokens (`.d-node`, `.d-line`, `.d-accent`, `.d-label`…) so dark mode works automatically. **Never hard-code hex values inside the SVG.**
- Text in SVG uses the mono label font, ALL CAPS, at 13–16 px in viewBox units.
- **Mind the rendered size, not the viewBox size.** In a split zone on a 1366 laptop the diagram column is about 600 px wide, so a 960-wide viewBox renders at about 0.63×, which turns 13-unit text into roughly 8 px. The template's script **auto-fits each figure's viewBox to its drawn content** after fonts load (opt out with `data-fit="off"`), so leftover margins don't shrink the labels. For split-zone diagrams, keep the drawn content compact (about 760 units wide or less) and prefer regular `d-label` over `d-label--sm` for anything the reader must read.
- Lay out on an implied 8-column grid inside the viewBox, align nodes and keep equal gaps. Lines turn at right angles (orthogonal routing) unless the diagram is a loop.
- A diagram should mostly make sense with the zone text hidden. Labels carry the meaning.
- Keep it to 9 nodes per diagram at most. If you need more, split it across zones or use `zone--wide`.

---

## 7. Motion rules

- **Draw-in:** lines and paths with class `draw` animate their stroke from start to end when the zone enters the viewport (about 0.9 s, ease-out). The template handles this with `pathLength="1"` plus a dash offset.
- **Pop-in:** nodes and cards with class `pop` scale from 0.85 to 1 and fade in (0.35 s), staggered with `style="--i:N"`.
- **Stamp:** a single element with class `stamp` drops and rotates slightly. Use it once per page at most.
- **Explanatory motion (M1–M6)** goes beyond these entrances: flows, narrated builds, state toggles, traces, sequences and counts. It is governed by `shared/motion.md` (the test, the budget and the markup). The runtime ships in the template's MOTION blocks.
- No motion blur, parallax, horizontal camera moves or continuous looping animation; flows and sequences run a set number of rounds, then stop.
- Under `prefers-reduced-motion: reduce`, everything appears immediately in its final state.
