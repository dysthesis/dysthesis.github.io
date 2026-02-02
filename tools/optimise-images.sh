#!/usr/bin/env bash
# Optimize raster images in-place for web delivery.
#  - Downscales anything wider than 1400px.
#  - Emits responsive 800w variants (JPEG + WebP) and a 1400w WebP.
#  - Re-encodes JPEG/PNG with sane quality and stripping metadata.
#  - Stops if ImageMagick (convert) is unavailable.

set -euo pipefail

if ! command -v convert >/dev/null 2>&1; then
  echo "optimize-images: ImageMagick 'convert' is required but not found in PATH." >&2
  exit 1
fi

shopt -s nullglob
for img in "$@"; do
  if [[ -d $img ]]; then
    # Recurse into directory
    "$0" "$img"/*
    continue
  fi

  case "${img,,}" in
  *.jpg | *.jpeg | *.png)
    base="${img%.*}"
    tmp="$(mktemp)"
    # Primary: downscale to <=1400px wide, strip metadata, progressive JPEG,
    # cap quality/size to keep LCP image fast.
    convert "$img" \
      -resize '1400x1400>' \
      -strip \
      -interlace Plane \
      -sampling-factor 4:2:0 \
      -quality 82 \
      -define jpeg:extent=900kb \
      "$tmp"
    mv "$tmp" "$img"

    # High-res WebP (<=1400px).
    convert "$img" \
      -resize '1400x1400>' \
      -strip \
      -quality 82 \
      "${base}.webp"

    # 800px responsive pair (WebP + JPEG fallback).
    convert "$img" \
      -resize '800x800>' \
      -strip \
      -interlace Plane \
      -sampling-factor 4:2:0 \
      -quality 82 \
      -define jpeg:extent=500kb \
      "${base}-800.jpg"

    convert "$img" \
      -resize '800x800>' \
      -strip \
      -quality 80 \
      "${base}-800.webp"

    echo "optimized $img -> ${base}.webp (+ 800px variants)"
    ;;
  *) ;;
  esac
done
