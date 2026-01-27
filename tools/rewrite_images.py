#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import mimetypes
import subprocess
from functools import lru_cache
from pathlib import Path, PurePosixPath

import brotli
from bs4 import BeautifulSoup, Doctype  # type: ignore

DEFAULT_SIZES = "(max-width: 900px) 90vw, 800px"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rewrite <img> tags to responsive <picture> blocks.",
    )
    parser.add_argument(
        "--html-dir",
        default="public",
        help="Directory containing generated HTML files.",
    )
    parser.add_argument(
        "--assets-dir",
        default="assets",
        help="Directory containing site assets (for image variants).",
    )
    return parser.parse_args()


@lru_cache(maxsize=None)
def image_dimensions(path: Path) -> tuple[int, int] | None:
    if not path.exists():
        return None
    try:
        result = subprocess.run(
            ["identify", "-format", "%w %h", str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    parts = result.stdout.strip().split()
    if len(parts) != 2:
        return None
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None


def guess_width(path: Path) -> int:
    dims = image_dimensions(path)
    if dims:
        return dims[0]
    # Fallback based on filename hint
    name = path.name
    if "-800" in name:
        return 800
    return 1400


def resolve_asset(src: str, assets_root: Path) -> tuple[Path, str] | None:
    if (
        src.startswith("data:")
        or src.startswith("http://")
        or src.startswith("https://")
    ):
        return None
    clean_src = src.split("?")[0].split("#")[0]
    parsed = PurePosixPath(clean_src)
    if "assets" not in parsed.parts:
        return None
    idx = parsed.parts.index("assets")
    rel = PurePosixPath(*parsed.parts[idx + 1 :])
    if not rel.parts or rel.parts[0] != "img":
        return None

    asset_path = assets_root / rel
    prefix_path = parsed.parent.as_posix()
    prefix = f"{prefix_path}/" if prefix_path not in {"", "."} else ""
    return asset_path, prefix


def collect_variants(asset_path: Path) -> dict[str, Path]:
    stem = asset_path.stem
    ext = asset_path.suffix
    directory = asset_path.parent

    variants: dict[str, Path] = {}

    webp_hi = directory / f"{stem}.webp"
    webp_lo = directory / f"{stem}-800.webp"
    if webp_hi.exists():
        variants["webp_hi"] = webp_hi
    if webp_lo.exists():
        variants["webp_lo"] = webp_lo

    fallback_hi = asset_path if asset_path.exists() else None
    fallback_lo = None

    same_ext_lo = directory / f"{stem}-800{ext}"
    jpg_lo = directory / f"{stem}-800.jpg"
    for candidate in (same_ext_lo, jpg_lo):
        if candidate.exists():
            fallback_lo = candidate
            break

    if fallback_hi:
        variants["fallback_hi"] = fallback_hi
    if fallback_lo:
        variants["fallback_lo"] = fallback_lo

    return variants


def srcset(prefix: str, entries: list[Path]) -> str:
    parts: list[str] = []
    for path in entries:
        width = guess_width(path)
        parts.append(f"{prefix}{path.name} {width}w")
    return ", ".join(parts)


def mime_for(path: Path | None) -> str | None:
    if path is None:
        return None
    mime, _ = mimetypes.guess_type(path.name)
    return mime


def build_picture(
    soup: BeautifulSoup, img_tag, prefix: str, variants: dict[str, Path], is_first: bool
) -> BeautifulSoup:
    sizes = DEFAULT_SIZES
    picture = soup.new_tag("picture")

    webp_entries = [p for p in (variants.get("webp_lo"), variants.get("webp_hi")) if p]
    if webp_entries:
        source_webp = soup.new_tag(
            "source",
            srcset=srcset(prefix, webp_entries),
            type="image/webp",
            sizes=sizes,
        )
        picture.append(source_webp)

    fallback_entries = [
        p for p in (variants.get("fallback_lo"), variants.get("fallback_hi")) if p
    ]
    if fallback_entries:
        fallback_type = None
        suffixes = {p.suffix for p in fallback_entries}
        if len(suffixes) == 1:
            fallback_type = mime_for(fallback_entries[0])
        source_attrs = {
            "srcset": srcset(prefix, fallback_entries),
            "sizes": sizes,
        }
        if fallback_type:
            source_attrs["type"] = fallback_type
        picture.append(soup.new_tag("source", **source_attrs))

    img_attrs = {
        k: v for k, v in img_tag.attrs.items() if k not in {"src", "srcset", "sizes"}
    }
    if variants.get("fallback_hi"):
        img_attrs["src"] = prefix + variants["fallback_hi"].name
    else:
        img_attrs["src"] = img_tag.get("src", "")

    if fallback_entries:
        img_attrs["srcset"] = srcset(prefix, fallback_entries)
        img_attrs["sizes"] = sizes

    if "decoding" not in img_attrs:
        img_attrs["decoding"] = "async"

    if (
        not is_first
        and "loading" not in img_attrs
        and img_attrs.get("fetchpriority") != "high"
    ):
        img_attrs["loading"] = "lazy"
    elif is_first and "fetchpriority" not in img_attrs:
        img_attrs["fetchpriority"] = "high"

    dims = (
        image_dimensions(variants.get("fallback_hi"))
        if variants.get("fallback_hi")
        else None
    )
    if dims:
        img_attrs.setdefault("width", str(dims[0]))
        img_attrs.setdefault("height", str(dims[1]))

    picture.append(soup.new_tag("img", **img_attrs))
    return picture


def rewrite_file(html_path: Path, assets_root: Path) -> bool:
    html_text = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html_text, "html.parser")

    changed = False
    # Normalise doctype to avoid odd serialisation (e.g. "<!DOCTYPE tml>").
    doctypes = [node for node in soup.contents if isinstance(node, Doctype)]
    doctype_changed = False
    if doctypes:
        if doctypes[0].string.lower() != "html":  # type: ignore[union-attr]
            doctypes[0].replace_with(Doctype("html"))
            doctype_changed = True
    else:
        soup.insert(0, Doctype("html"))
        doctype_changed = True

    first_asset_img_seen = False

    for img in soup.find_all("img"):
        if img.parent and img.parent.name == "picture":
            continue
        src = img.get("src")
        if not src:
            continue
        resolved = resolve_asset(src, assets_root)
        if not resolved:
            continue
        asset_path, prefix = resolved
        variants = collect_variants(asset_path)
        if not variants:
            continue

        picture = build_picture(
            soup, img, prefix, variants, is_first=not first_asset_img_seen
        )
        first_asset_img_seen = True
        img.replace_with(picture)
        changed = True

    if changed or doctype_changed:
        html_bytes = soup.encode("utf-8")
        html_path.write_bytes(html_bytes)

        gz_path = html_path.with_suffix(html_path.suffix + ".gz")
        with gzip.open(gz_path, "wb", compresslevel=9) as fh:
            fh.write(html_bytes)

        br_path = html_path.with_suffix(html_path.suffix + ".br")
        br_path.write_bytes(brotli.compress(html_bytes, quality=11))

    return changed


def main() -> None:
    args = parse_args()
    html_root = Path(args.html_dir)
    assets_root = Path(args.assets_dir)

    html_files = sorted(html_root.rglob("*.html"))
    any_changed = False
    for html_file in html_files:
        if rewrite_file(html_file, assets_root):
            print(f"rewrote {html_file}")
            any_changed = True

    if not any_changed:
        print("rewrite_images: no eligible images found; nothing changed.")


if __name__ == "__main__":
    main()
