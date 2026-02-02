#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re


def inline_katex_css(root: pathlib.Path) -> None:
    katex_css_path = pathlib.Path("assets/katex/katex.min.css")
    style_path = root / "style.css"
    if not katex_css_path.exists() or not style_path.exists():
        return

    katex_css = katex_css_path.read_text()
    katex_css = katex_css.replace("fonts-subset/", "/assets/katex/fonts-subset/")
    katex_css = katex_css.replace("fonts/", "/assets/katex/fonts/")
    # Preserve existing sidenote counter while keeping KaTeX counters.
    katex_css = katex_css.replace(
        "body{counter-reset:katexEqnNo mmlEqnNo}",
        "body{counter-reset:sidenote-counter katexEqnNo mmlEqnNo}",
    )

    style = style_path.read_text()
    style_path.write_text(style + "\n/* Inline KaTeX */\n" + katex_css)


def inject_preloads(root: pathlib.Path) -> None:
    critical_css = """
    @font-face{font-family:Literata;src:url("/fonts/Literata-Regular.woff2") format("woff2");font-style:normal;font-weight:400;font-display:swap;}
    @font-face{font-family:Literata;src:url("/fonts/Literata-Italic.woff2") format("woff2");font-style:italic;font-weight:400;font-display:swap;}
    :root{--font-serif:Literata,Georgia,serif;--bg:#000;--fg:#fff;--rule:rgba(255,255,255,0.25);--max-width:1400px;--main-col:55%;}
    @media (prefers-color-scheme: light){:root{--bg:#fff;--fg:#111;--rule:rgba(0,0,0,0.2);}}
    html{font-size:15px;}
    body{width:87.5%;max-width:var(--max-width);margin:0 auto;padding-left:12.5%;font-family:var(--font-serif);background:var(--bg);color:var(--fg);counter-reset:sidenote-counter;}
    article{padding:5rem 0;}
    section{padding:1rem 0;counter-reset:md-h1;position:relative;}
    p,dl,ol,ul{font-size:1.4rem;line-height:2rem;}
    p{margin:1.4rem 0;}
    a:link,a:visited{color:inherit;text-underline-offset:0.1em;text-decoration-thickness:0.05em;}
    h1{font-weight:400;margin:4rem 0 1.5rem;font-size:3.2rem;line-height:1;}
    h2{font-style:italic;font-weight:400;margin:2.1rem 0 1.4rem;font-size:2.2rem;line-height:1;}
    p.subtitle{display:block;font-style:italic;margin:1rem 0;font-size:1.8rem;line-height:1;}
    figure{max-width:var(--main-col);margin:0 0 3em 0;}
    img{max-width:100%;}
    figcaption{float:right;clear:right;margin:0;font-size:1.1rem;line-height:1.6;position:relative;max-width:40%;}
    """

    woff_preloads = [
        '<link rel="preload" href="/fonts/Literata-Regular.woff2" as="font" type="font/woff2" crossorigin>',
        '<link rel="preload" href="/fonts/Literata-Italic.woff2" as="font" type="font/woff2" crossorigin>',
    ]
    style_preload = '<link rel="preload" href="/style.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">'
    style_fallback = '<noscript><link rel="stylesheet" href="/style.css"></noscript>'
    icon_link = '<link rel="icon" href="/favicon.ico" sizes="any">'
    critical_style = f"<style>{critical_css}</style>"
    inject_block = "".join(woff_preloads + [style_preload, style_fallback, icon_link, critical_style])
    meta_pattern = re.compile(r'(<meta content="width=device-width,initial-scale=1" name=viewport>)')

    for html in root.rglob("*.html"):
        text = html.read_text()
        # Remove any existing font/style preloads or stylesheet links (ttf/woff2/katex/css).
        text = re.sub(r'<link[^>]+href=[^>]+\.(ttf|woff2)[^>]*>', "", text)
        text = re.sub(r'<link[^>]+katex\.min\.css[^>]*>', "", text)
        text = re.sub(r'<link[^>]+href=[^>]*style\.css[^>]*>', "", text)
        # Inject our canonical preloads + async style + icon + critical CSS after viewport meta.
        text = meta_pattern.sub(lambda m: m.group(1) + inject_block, text, count=1)
        html.write_text(text)


def main() -> None:
    root = pathlib.Path("public")
    inline_katex_css(root)
    inject_preloads(root)


if __name__ == "__main__":
    main()
