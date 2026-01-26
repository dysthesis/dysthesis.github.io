#!/usr/bin/env bash
# Optimize raster images in-place for web delivery.
#  - Downscales anything wider than 1400px.
#  - Re-encodes JPEG/PNG with sane quality and stripping metadata.
#  - Stops if ImageMagick (convert) is unavailable.

set -euo pipefail

if ! command -v convert >/dev/null 2>&1; then
  echo "optimize-images: ImageMagick 'convert' is required but not found in PATH." >&2
  exit 1
fi

shopt -s nullglob
for img in "$@"; do
  if [[ -d "$img" ]]; then
    # Recurse into directory
    "$0" "$img"/*
    continue
  fi

  case "${img,,}" in
    *.jpg|*.jpeg|*.png)
      tmp="$(mktemp)"
      # Downscale (only if >1400px wide), strip metadata, set progressive JPEG,
      # control quality/size.
      convert "$img" \
        -resize '1400x1400>' \
        -strip \
        -interlace Plane \
        -sampling-factor 4:2:0 \
        -quality 82 \
        -define jpeg:extent=900kb \
        "$tmp"
      mv "$tmp" "$img"
      echo "optimized $img"
      ;;
    *)
      ;;
  esac
done
