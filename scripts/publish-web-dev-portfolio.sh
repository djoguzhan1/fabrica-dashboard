#!/usr/bin/env bash
# Updates https://djoguzhan1.github.io/web-dev-portfolio/ (existing repo, no 404 path).
set -euo pipefail

REPO="djoguzhan1/web-dev-portfolio"
SRC="$(cd "$(dirname "$0")/../web-dev-portfolio" && pwd)"
WORKDIR="${TMPDIR:-/tmp}/web-dev-portfolio-publish"

echo "→ Source: $SRC"
gh auth status >/dev/null 2>&1 || { echo "Run: gh auth login"; exit 1; }

rm -rf "$WORKDIR"
gh repo clone "$REPO" "$WORKDIR"
rsync -a --delete --exclude PUBLISH.md --exclude SETUP-LIVE.md "$SRC/" "$WORKDIR/"
cd "$WORKDIR"
git add -A
git diff --staged --quiet && echo "→ No changes." || git commit -m "Publish rebuilt portfolio and demos"
git push origin master

echo "Live in 1–2 min:"
echo "  https://djoguzhan1.github.io/web-dev-portfolio/"
echo "  https://djoguzhan1.github.io/web-dev-portfolio/demos/hvac-landing/"
echo "  https://djoguzhan1.github.io/web-dev-portfolio/demos/plumbing-landing/"
