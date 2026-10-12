"""Copy shared/tokens.css into every template (and any page you name) between the TOKENS markers.

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
TOKENS = (ROOT / "shared" / "tokens.css").read_text(encoding="utf-8").strip()
TEMPLATES = [
    ROOT / "skills" / "blueprint-explainer" / "assets" / "template.html",
    ROOT / "skills" / "reference-guide" / "assets" / "template.html",
]
BLOCK = re.compile(r"(/\* TOKENS:BEGIN[^*]*\*/\n).*?(\n/\* TOKENS:END \*/)", re.S)


def sync(path: pathlib.Path, check: bool) -> bool:
    """Return True when the file is (or now is) in sync."""
    html = path.read_text(encoding="utf-8")
    if not BLOCK.search(html):
        print(f"MISSING MARKERS: {path}")
        return False
    updated = BLOCK.sub(lambda m: m.group(1) + TOKENS + m.group(2), html)
    if updated == html:
        print(f"in sync: {path}")
        return True
    if check:
        print(f"OUT OF SYNC: {path}")
        return False
    path.write_text(updated, encoding="utf-8")
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
