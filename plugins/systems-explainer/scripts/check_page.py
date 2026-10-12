"""Pre-handover checks for a generated explainer or reference page.

Usage:
    python scripts/check_page.py <page.html> [more.html ...]

Checks (each prints PASS or FAIL, exit 1 if any fail):
  placeholders   no "{{" left in the file
  tokens         the TOKENS:BEGIN/END block matches shared/tokens.css (skipped if the page has no markers)
  colors         no literal hex colors outside the token block (SVG, CSS and inline styles must use tokens)
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
TOKENS = (ROOT / "shared" / "tokens.css").read_text(encoding="utf-8").strip()
BLOCK = re.compile(r"/\* TOKENS:BEGIN[^*]*\*/\n(.*?)\n/\* TOKENS:END \*/", re.S)
ALLOWED_HOSTS = ("https://fonts.googleapis.com", "https://fonts.gstatic.com")


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

    # tokens
    m = BLOCK.search(html)
    if m:
        results.append(report("tokens", m.group(1).strip() == TOKENS, "" if m.group(1).strip() == TOKENS else "run sync_tokens.py on this page"))
    else:
        print("  SKIP  tokens: no TOKENS markers (page predates them)")

    # literal colors outside the token block
    body = BLOCK.sub("", html)
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
    scripts = [s for s in re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.S | re.I)]
    node = shutil.which("node")
    if node and scripts:
        failures = []
        for i, src in enumerate(scripts, 1):
            proc = subprocess.run([node, "-e", "new Function(require('fs').readFileSync(0,'utf8'))"], input=src, text=True, capture_output=True)
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
    results.append(report("title", ok_title and ok_desc, "" if ok_title and ok_desc else f"title has {words} words; description {'present' if ok_desc else 'missing'}"))

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
