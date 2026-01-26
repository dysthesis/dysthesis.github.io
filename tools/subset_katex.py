#!/usr/bin/env python3
"""
Subset KaTeX webfonts to only the glyphs actually used across generated pages.

Inputs:
  - public/ (HTML output from ssg)
  - assets/katex/fonts/*.woff2 (upstream KaTeX fonts)

Outputs:
  - assets/katex/fonts-subset/*.woff2 (subsetted)
  - assets/katex/katex.min.css rewritten to point at fonts-subset for the
    subsetted faces (others remain untouched).
"""
from __future__ import annotations

import subprocess
from pathlib import Path

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise SystemExit("BeautifulSoup4 is required; add it to the build inputs.") from exc


PUBLIC_DIR = Path("public")
KATEX_CSS = Path("assets/katex/katex.min.css")
FONT_DIR = Path("assets/katex/fonts")
SUBSET_DIR = Path("assets/katex/fonts-subset")

# Minimal set of KaTeX fonts worth subsetting; others are rarely used.
SUBSET_FACES = [
    "KaTeX_Main-Regular",
    "KaTeX_Math-Italic",
    "KaTeX_AMS-Regular",
]

# Baseline glyphs to avoid missing common punctuation.
BASELINE = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    " +-*/=()[]{}<>,.;:'\"!?#$%&|_^\\`~"
)


def collect_glyphs() -> str:
    chars: set[str] = set(BASELINE)
    for html_path in PUBLIC_DIR.rglob("*.html"):
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
        for el in soup.select(".katex"):
            chars.update(el.get_text())
    return "".join(sorted(chars))


def subset_font(face: str, glyphs: str) -> None:
    src = FONT_DIR / f"{face}.woff2"
    dst = SUBSET_DIR / f"{face}.woff2"
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pyftsubset",
        str(src),
        "--text=" + glyphs,
        "--flavor=woff2",
        "--layout-features=*",
        "--output-file=" + str(dst),
    ]
    subprocess.run(cmd, check=True)


def rewrite_css(glyph_faces: list[str]) -> None:
    css = KATEX_CSS.read_text(encoding="utf-8")
    for face in glyph_faces:
        css = css.replace(f"fonts/{face}.woff2", f"fonts-subset/{face}.woff2")
    KATEX_CSS.write_text(css, encoding="utf-8")


def main() -> None:
    glyphs = collect_glyphs()
    for face in SUBSET_FACES:
        subset_font(face, glyphs)
    rewrite_css(SUBSET_FACES)


if __name__ == "__main__":
    main()
