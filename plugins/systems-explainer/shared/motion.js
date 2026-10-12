/* ============================================================
   SHARED MOTION RUNTIME — systems-explainer plugin (see shared/motion.md)
   Synced into both templates by scripts/sync_tokens.py. Edit here only.
   Hooks: M1 .m-token[data-flow]  M2 [data-step]  M3 [data-states]
          M4 [data-trace-scope]   M5 [data-sequence]  M6 [data-count]
   ============================================================ */
(() => {
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) root.classList.add('motion-on');
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const watch = (el, enter, leave, threshold = 0.45) => {
    const io = new IntersectionObserver(es => es.forEach(e => (e.isIntersecting ? enter() : leave && leave())), { threshold });
    io.observe(el);
  };

  // ---- M6 Count: markup holds the final value; count up once on first view ----
  $$('[data-count]').forEach(el => {
    const final = el.textContent.trim();
    const n = parseFloat(final.replace(/,/g, ''));
    if (reduce || Number.isNaN(n)) return;
    const dec = (final.split('.')[1] || '').length;
    let done = false;
    watch(el, () => {
      if (done) return; done = true;
      const t0 = performance.now(), D = 900;
      const tick = t => {
        const p = Math.min(1, (t - t0) / D);
        el.textContent = p < 1 ? (n * (1 - Math.pow(1 - p, 3))).toFixed(dec) : final;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    }, null, 0.6);
  });

  // ---- M1 Flow: a token travels a guide path; stations flash as it passes ----
  $$('.m-token[data-flow]').forEach(tok => {
    const path = document.querySelector(tok.dataset.flow);
    const svg = tok.ownerSVGElement;
    if (!path || !svg || !path.getTotalLength) return;
    const L = path.getTotalLength();
    const dur = (parseFloat(tok.dataset.dur) || 3) * 1000;
    const rounds = parseInt(tok.dataset.rounds, 10) || 2;
    const hits = (tok.dataset.hits || '').split(';').map(s => s.trim()).filter(Boolean)
      .map(s => { const [f, sel] = s.split(/\s+/); return { f: parseFloat(f), el: document.querySelector(sel) }; })
      .filter(h => h.el && !Number.isNaN(h.f)).sort((a, b) => a.f - b.f);
    const place = d => { const p = path.getPointAtLength(d); tok.setAttribute('cx', p.x); tok.setAttribute('cy', p.y); };
    const flash = el => { el.classList.add('is-hit'); setTimeout(() => el.classList.remove('is-hit'), 700); };
    let raf = 0, timer = 0, running = false;
    place(0);
    const stop = () => { running = false; cancelAnimationFrame(raf); clearTimeout(timer); tok.classList.remove('is-running'); };
    const run = () => {
      if (reduce || running) return;
      running = true; tok.classList.add('is-running');
      let r = 0;
      const once = () => {
        const t0 = performance.now(); let next = 0;
        const tick = t => {
          if (!running) return;
          const p = Math.min(1, (t - t0) / dur);
          place(L * p);
          while (next < hits.length && p >= hits[next].f) flash(hits[next++].el);
          if (p < 1) raf = requestAnimationFrame(tick);
          else if (++r < rounds) timer = setTimeout(once, 700);
          else stop();
        };
        raf = requestAnimationFrame(tick);
      };
      once();
    };
    svg.setAttribute('data-flow-figure', '');
    svg.addEventListener('click', () => { stop(); run(); });
    watch(svg, run, stop);
  });

  // ---- M5 Sequence: stations take turns being active, for a set number of rounds ----
  $$('[data-sequence]').forEach(box => {
    const items = $$('[data-seq-item]', box);
    const ms = parseInt(box.dataset.seqMs, 10) || 800;
    const rounds = parseInt(box.dataset.rounds, 10) || 2;
    let timer = 0, running = false;
    const clear = () => items.forEach(i => i.classList.remove('is-active'));
    const stop = () => { running = false; clearTimeout(timer); clear(); };
    const run = () => {
      if (reduce || running || !items.length) return;
      running = true; let k = 0;
      const step = () => {
        clear();
        if (!running || k >= items.length * rounds) { running = false; return; }
        items[k % items.length].classList.add('is-active'); k++;
        timer = setTimeout(step, ms);
      };
      step();
    };
    box.addEventListener('click', e => { if (!e.target.closest('button, a')) { stop(); run(); } });
    watch(box, run, stop);
  });

  // ---- M3 State: pick an input; matching items light, others dim ----
  $$('[data-states]').forEach(box => {
    const btns = $$('[data-set-state]', box), items = $$('[data-when]', box), says = $$('[data-say]', box);
    const set = s => {
      btns.forEach(b => b.setAttribute('aria-pressed', b.dataset.setState === s ? 'true' : 'false'));
      items.forEach(i => {
        const on = i.dataset.when.split(/\s+/).includes(s);
        i.classList.toggle('is-lit', s !== 'all' && on);
        i.classList.toggle('is-dim', s !== 'all' && !on);
      });
      says.forEach(p => { p.hidden = p.dataset.say !== s; });
    };
    btns.forEach(b => b.addEventListener('click', () => set(b.dataset.setState)));
    const first = btns.find(b => b.getAttribute('aria-pressed') === 'true') || btns[0];
    if (first) set(first.dataset.setState);
  });

  // ---- M4 Trace: hover/focus a node to light everything linked to it, and say WHY ----
  // data-rel="k1:IN · reason; k2:OUT · reason" on a linked element = the label it shows while k1/k2 is traced.
  // [data-trace-status] inside the scope narrates what is selected or hovered.
  $$('[data-trace-scope]').forEach(scope => {
    const nodes = $$('[data-node]', scope);
    const all = [...new Set([...nodes, ...$$('[data-links]', scope)])];
    const status = scope.querySelector('[data-trace-status]');
    const idle = status ? status.textContent : '';
    const nameOf = k => { const n = nodes.find(x => x.dataset.node === k); return n ? (n.dataset.label || n.firstChild.textContent.trim()) : k; };
    const relOf = (el, k) => {
      const hit = (el.dataset.rel || '').split(';').map(s => s.trim()).find(s => s.startsWith(k + ':'));
      return hit ? hit.slice(k.length + 1).trim() : '';
    };
    const chip = el => el.querySelector(':scope > .m-rel') || el.appendChild(Object.assign(document.createElement('span'), { className: 'm-rel' }));
    const on = (k, pinned) => {
      let count = 0;
      all.forEach(el => {
        const self = el.dataset.node === k;
        const hit = self || (el.dataset.links || '').split(/\s+/).includes(k);
        el.classList.toggle('is-lit', hit);
        el.classList.toggle('is-dim', !hit);
        el.classList.toggle('is-origin', self);
        if (el.dataset.rel !== undefined || self) {
          const text = self ? (pinned ? 'SELECTED' : 'THIS MODULE') : (hit ? relOf(el, k) : '');
          if (text || el.querySelector(':scope > .m-rel')) chip(el).textContent = text;
        }
        if (hit && !self) count++;
      });
      if (status) status.textContent = `${pinned ? 'Selected' : 'Showing'}: ${nameOf(k)} · ${count} direct connection${count === 1 ? '' : 's'}. IN = sends something to it · OUT = receives something from it.`;
    };
    const rest = () => {
      const pressed = nodes.find(n => n.getAttribute('aria-pressed') === 'true');
      if (pressed && scope.hasAttribute('data-trace-pressed')) on(pressed.dataset.node, true);
      else {
        all.forEach(el => { el.classList.remove('is-lit', 'is-dim', 'is-origin'); const c = el.querySelector(':scope > .m-rel'); if (c) c.textContent = ''; });
        if (status) status.textContent = idle;
      }
    };
    nodes.forEach(n => {
      if (!n.hasAttribute('tabindex') && !/^(BUTTON|A)$/.test(n.tagName)) n.setAttribute('tabindex', '0');
      n.addEventListener('mouseenter', () => on(n.dataset.node, false));
      n.addEventListener('focus', () => on(n.dataset.node, n.getAttribute('aria-pressed') === 'true'));
      n.addEventListener('mouseleave', rest);
      n.addEventListener('blur', rest);
      n.addEventListener('click', () => setTimeout(rest, 0));
    });
    rest();
  });

  // ---- M2 Build (explainer zones): narrated steps; ↓/Space reveals before moving on ----
  if (!reduce) {
    const builds = $$('.zone').filter(z => z.querySelector('[data-step]')).map(z => {
      const nums = [...new Set($$('[data-step]', z).map(s => parseInt(s.dataset.step, 10)))].sort((a, b) => a - b);
      const b = { z, groups: nums.map(n => $$(`[data-step="${n}"]`, z)), shown: 0, timer: 0, ms: parseInt(z.dataset.stepMs, 10) || 900 };
      b.hint = z.querySelector('.m-steps-hint');
      return b;
    });
    const label = b => { if (b.hint) b.hint.textContent = b.shown < b.groups.length ? `↓ next step · ${b.shown}/${b.groups.length}` : `${b.groups.length}/${b.groups.length} · ↓ next zone`; };
    const reveal = b => {
      if (b.shown >= b.groups.length) return false;
      b.groups[b.shown++].forEach(el => el.classList.add('is-shown'));
      label(b); return true;
    };
    const auto = b => { clearTimeout(b.timer); if (b.shown < b.groups.length) b.timer = setTimeout(() => { reveal(b); auto(b); }, b.ms); };
    builds.forEach(b => { label(b); watch(b.z, () => { if (!b.shown) { b.timer = setTimeout(() => { reveal(b); auto(b); }, 500); } else auto(b); }, () => clearTimeout(b.timer), 0.5); });
    const current = () => {
      let best = null, bd = Infinity;
      $$('.zone').forEach(z => { const d = Math.abs(z.getBoundingClientRect().top); if (d < bd) { bd = d; best = z; } });
      return builds.find(b => b.z === best);
    };
    addEventListener('keydown', e => {
      if (e.altKey || e.ctrlKey || e.metaKey || e.target.closest('input, textarea, select, button, [contenteditable]')) return;
      const next = ['ArrowDown', 'ArrowRight', 'PageDown'].includes(e.key) || (e.key === ' ' && !e.shiftKey);
      if (!next) return;
      const b = current();
      if (b && reveal(b)) { e.preventDefault(); e.stopImmediatePropagation(); auto(b); }
    }, true);
  }
})();
