"""Pre-handover checks for a generated explainer or reference page.

Usage:
    python scripts/check_page.py <page.html> [more.html ...]

Checks (each prints PASS or FAIL, exit 1 if any fail):
  placeholders   no "{{" left in the file
  tokens         the TOKENS block matches shared/tokens.css, and any MOTION-CSS / MOTION-JS
                 blocks match shared/motion.css / motion.js (skipped where markers are absent)
  colors         no literal hex colors outside the shared blocks (SVG, CSS and inline styles must use tokens)
  external       the only external URLs are the Google Fonts stylesheet and preconnects; no <img> or external <script>
  script         every inline <script> parses (needs node on PATH; skipped otherwise)
  title          <title> is 2–4 words and <meta name="description"> is present and non-empty
"""
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED = {
    "TOKENS": ROOT / "shared" / "tokens.css",
    "MOTION-CSS": ROOT / "shared" / "motion.css",
    "MOTION-JS": ROOT / "shared" / "motion.js",
}
ALLOWED_HOSTS = ("https://fonts.googleapis.com", "https://fonts.gstatic.com")


def block_rx(name: str) -> re.Pattern:
    return re.compile(r"/\* " + re.escape(name) + r":BEGIN[^*]*\*/\n(.*?)\n/\* " + re.escape(name) + r":END \*/", re.S)


def report(name: str, ok: bool, detail: str = "") -> bool:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{(': ' + detail) if detail else ''}")
    return ok


def check(path: pathlib.Path) -> bool:
    html = path.read_text(encoding="utf-8")
    print(path)
    results = []

    # placeholders
    hits = [i + 1 for i, line in enumerate(html.splitlines()) if "{{" in line]
    results.append(report("placeholders", not hits, f"lines {hits[:8]}" if hits else ""))

    # shared blocks
    found, stale = [], []
    for name, src in SHARED.items():
        m = block_rx(name).search(html)
        if not m:
            continue
        found.append(name)
        if m.group(1).strip() != src.read_text(encoding="utf-8").strip():
            stale.append(name)
    if found:
        results.append(report("tokens", not stale,
                              f"stale: {', '.join(stale)} (run sync_tokens.py on this page)" if stale else ", ".join(found)))
    else:
        print("  SKIP  tokens: no shared-block markers (page predates them)")

    # literal colors outside the shared blocks
    body = html
    for name in SHARED:
        body = block_rx(name).sub("", body)
    body = re.sub(r":root[^{]*\{[^}]*\}", "", body)  # legacy pages define tokens without markers
    hexes = sorted({h.group(0) for h in re.finditer(r"#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b(?![\w-])", body)})
    hexes = [h for h in hexes if not re.fullmatch(r"#[a-z][\w-]*", h)]  # id references like #ah are not colors
    results.append(report("colors", not hexes, ", ".join(hexes[:8]) if hexes else ""))

    # external requests
    urls = re.findall(r"""(?:href|src)=["'](https?://[^"']+)""", html)
    bad = [u for u in urls if not u.startswith(ALLOWED_HOSTS)]
    imgs = re.findall(r"<img\b", html, re.I)
    results.append(report("external", not bad and not imgs, "; ".join(bad[:4] + (["<img> present"] if imgs else []))))

    # inline script parses
    scripts = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.S | re.I)
    node = shutil.which("node")
    if node and scripts:
        failures = []
        for i, src in enumerate(scripts, 1):
            # encoding="utf-8": the default on Windows is cp1252, which can't encode characters
            # like "↓" and kills the stdin writer, leaving node waiting forever.
            try:
                proc = subprocess.run([node, "-e", "new Function(require('fs').readFileSync(0,'utf8'))"],
                                      input=src, text=True, encoding="utf-8", capture_output=True, timeout=30)
            except subprocess.TimeoutExpired:
                failures.append(f"#{i}: node timed out")
                continue
            if proc.returncode:
                failures.append(f"#{i}: {proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else 'parse error'}")
        results.append(report("script", not failures, "; ".join(failures)))
    else:
        print("  SKIP  script: node not on PATH" if scripts else "  SKIP  script: no inline script")

    # title + description
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    words = len(t.group(1).split()) if t else 0
    d = re.search(r"""<meta\s+name=["']description["']\s+content=["']([^"']*)["']""", html)
    ok_title = 2 <= words <= 4
    ok_desc = bool(d and d.group(1).strip())
    results.append(report("title", ok_title and ok_desc,
                          "" if ok_title and ok_desc else f"title has {words} words; description {'present' if ok_desc else 'missing'}"))

    return all(results)


def main() -> int:
    paths = [pathlib.Path(a) for a in sys.argv[1:]]
    if not paths:
        print(__doc__)
        return 2
    ok = all([check(p) for p in paths])
    print("ALL PASS" if ok else "FAILURES — fix the items above before handing over")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
