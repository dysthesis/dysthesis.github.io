#!/usr/bin/env bash
set -euo pipefail

out_dir=${1:-${out:-}}
if [ -z "${out_dir}" ]; then
  echo "Usage: $0 <out>" >&2
  exit 1
fi

mkdir -p "${out_dir}"
cp -r public/* "${out_dir}/"
cp -r fonts "${out_dir}/fonts"
cp -r assets "${out_dir}/assets"

# Ensure favicon is available at the root for automatic browser fetches.
if [ -f assets/favicon.ico ]; then
  cp assets/favicon.ico "${out_dir}/favicon.ico"
fi
if [ -f assets/favicon.svg ]; then
  cp assets/favicon.svg "${out_dir}/favicon.svg"
fi
