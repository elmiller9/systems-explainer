# Reference Guide Quality Checklist

Run through this before handing the page over. Fix anything that fails; don't just report it.

## Coverage and accuracy
- [ ] Every source section appears, in order, with its source number in the eyebrow and the contents rail.
- [ ] At least 90% of substantive content is present: decisions, every table, interfaces, lists, phases, open questions.
- [ ] Figures, IDs, versions and names match the source exactly. Spot-check five.
- [ ] Contradictions or unsupported claims in the source are named in the footer, with the figure the page uses.
- [ ] Nothing is invented: examples, numbers and vendor names all come from the source.

## Structure and writing
- [ ] Each section has a plain-language claim as its `h2`, then short context, then detail.
- [ ] Long tabular content uses a switcher, filter or explorer rather than one very long table.
- [ ] Semantic chips are consistent everywhere (ok, gap, ai, human) and never decorative.
- [ ] Prose is plain and active, with no aphorisms, hype or em-dash asides.

## Visual and interaction
- [ ] Only template tokens are used, with no literal colors. `check_page.py` passes on the page (placeholders, tokens, colors, external requests, script, title).
- [ ] Every table sits in `.table-wrap`. At about 400 px wide nothing makes the page scroll sideways.
- [ ] The contents rail highlights the current section and its links jump correctly.
- [ ] Every switcher, explorer and filter works, and each one starts in a sensible default state.
- [ ] Both themes read well. The theme toggle works.
- [ ] In both mode, the companion link points to the explainer's file name, and the explainer's last zone links back.
