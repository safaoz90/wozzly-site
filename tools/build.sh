#!/bin/sh
# Makes the site: the help pages (tools/pages.py), and the legal pages, app-ads.txt and photo credits copied from the
# old site (safaoz90.github.io, whose tools/legal.py writes them). Run it after changing either, then commit and push.
set -e
cd "$(dirname "$0")/.."
OLD=../safaoz90.github.io
python3 tools/pages.py
for f in privacy terms cozy-privacy cozy-terms antfarm-privacy antfarm-terms messenger-privacy messenger-terms cozy-credits; do
  # (Aha's legal pages link "Support" to the old home page: here that's aha.html)
  sed 's|href="index.html">Support|href="aha.html">Support|' "$OLD/$f.html" > "$f.html"
done
cp "$OLD/legal.css" "$OLD/app-ads.txt" "$OLD/icon.svg" "$OLD/cozy-icon.png" "$OLD/antfarm-icon.png" "$OLD/messenger-icon.png" .
echo "built"
