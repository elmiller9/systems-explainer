"""Copy the shared blocks into every template (and any page you name).

Shared blocks (source file -> marker name in templates/pages):
    shared/tokens.css  -> /* TOKENS:BEGIN ... */      ... /* TOKENS:END */
    shared/motion.css  -> /* MOTION-CSS:BEGIN ... */  ... /* MOTION-CSS:END */
    shared/motion.js   -> /* MOTION-JS:BEGIN ... */   ... /* MOTION-JS:END */

TOKENS is required. The MOTION blocks are synced wherever their markers exist.

Usage (from anywhere; paths are resolved from this script's location):
    python scripts/sync_tokens.py                    # write both templates
    python scripts/sync_tokens.py --check            # exit 1 if any template is out of sync
    python scripts/sync_tokens.py --check page.html  # also check a generated page
    python scripts/sync_tokens.py page.html          # bring a generated page up to date
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOCKS = {
    "TOKENS": ROOT / "shared" / "tokens.css",
    "MOTION-CSS": ROOT / "shared" / "motion.css",
    "MOTION-JS": ROOT / "shared" / "motion.js",
}
REQUIRED = {"TOKENS"}
TEMPLATES = [
    ROOT / "skills" / "blueprint-explainer" / "assets" / "template.html",
    ROOT / "skills" / "reference-guide" / "assets" / "template.html",
]


def pattern(name: str) -> re.Pattern:
    return re.compile(r"(/\* " + re.escape(name) + r":BEGIN[^*]*\*/\n).*?(\n/\* " + re.escape(name) + r":END \*/)", re.S)


def sync(path: pathlib.Path, check: bool) -> bool:
    """Return True when the file is (or now is) in sync."""
    html = original = path.read_text(encoding="utf-8")
    ok = True
    for name, src in BLOCKS.items():
        rx = pattern(name)
        if not rx.search(html):
            if name in REQUIRED:
                print(f"MISSING {name} MARKERS: {path}")
                ok = False
            continue
        content = src.read_text(encoding="utf-8").strip()
        html = rx.sub(lambda m: m.group(1) + content + m.group(2), html)
    if not ok:
        return False
    if html == original:
        print(f"in sync: {path}")
        return True
    if check:
        print(f"OUT OF SYNC: {path}")
        return False
    path.write_text(html, encoding="utf-8")
    print(f"synced: {path}")
    return True


def main() -> int:
    args = sys.argv[1:]
    check = "--check" in args
    extra = [pathlib.Path(a).resolve() for a in args if a != "--check"]
    ok = all([sync(p, check) for p in TEMPLATES + extra])
    if not ok:
        print("out of sync — run: python scripts/sync_tokens.py [page.html]")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
