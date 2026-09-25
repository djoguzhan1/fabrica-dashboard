#!/usr/bin/env bash
# Updates https://djoguzhan1.github.io/web-dev-portfolio/ (site files only; keeps docs/, fiverr-screenshots/, etc.)
set -euo pipefail

REPO="djoguzhan1/web-dev-portfolio"
SRC="$(cd "$(dirname "$0")/../web-dev-portfolio" && pwd)"
WORKDIR="${TMPDIR:-/tmp}/web-dev-portfolio-publish-$$"

SITE_PATHS=(
  index.html
  styles.css
  links.json
  LIVE-LINKS.md
  .nojekyll
  img
  fonts
  demos
  upwork-screenshots
)

echo "→ Source: $SRC"
gh auth status >/dev/null 2>&1 || { echo "Run: gh auth login"; exit 1; }

rm -rf "$WORKDIR"
gh repo clone "$REPO" "$WORKDIR"
cd "$WORKDIR"

for path in "${SITE_PATHS[@]}"; do
  if [ -e "$SRC/$path" ]; then
    rm -rf "$path"
    cp -a "$SRC/$path" "$path"
  fi
done

touch .nojekyll
git add "${SITE_PATHS[@]}" .nojekyll 2>/dev/null || true
git add -u
if git diff --staged --quiet; then
  echo "→ No changes."
else
  git commit -m "Publish rebuilt portfolio and demos (site paths only)"
  git push origin master
fi

echo "Live in 1–2 min:"
echo "  https://djoguzhan1.github.io/web-dev-portfolio/"
echo "  https://djoguzhan1.github.io/web-dev-portfolio/demos/hvac-landing/"
echo "  https://djoguzhan1.github.io/web-dev-portfolio/demos/plumbing-landing/"
