#!/usr/bin/env bash
set -euo pipefail

./tools/optimise-images.sh assets/img

# Subset and compress fonts to WOFF2 for shipping.
mkdir -p fonts-woff2
subset_range='U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2013-2014,U+2018-201A,U+201C-201E,U+2022,U+2026,U+2039-203A'

# Serif text faces
for font in fonts/Literata-Regular.ttf fonts/Literata-Italic.ttf; do
  base=$(basename "$font" .ttf)
  pyftsubset "$font" \
    --unicodes="$subset_range" \
    --flavor=woff2 \
    --layout-features='*' \
    --output-file="fonts-woff2/${base}.woff2"
done

# Monospace faces
for font in fonts/JetBrainsCustom-*.ttf; do
  base=$(basename "$font" .ttf)
  pyftsubset "$font" \
    --unicodes="$subset_range,U+2190-21FF" \
    --flavor=woff2 \
    --layout-features='*' \
    --output-file="fonts-woff2/${base}.woff2"
done

rm -rf fonts
mv fonts-woff2 fonts

if [ -f assets/favicon.svg ]; then
  magick convert assets/favicon.svg -define icon:auto-resize=64,32,16 assets/favicon.ico
fi

# Generate site
ssg

# Rewrite image tags to responsive <picture> blocks with srcsets.
python ./tools/rewrite_images.py

# Subset KaTeX fonts to only used glyphs and rewrite KaTeX CSS.
python ./tools/subset_katex.py

# Inline critical CSS and rewrite HTML asset links.
python ./tools/postprocess_html.py
