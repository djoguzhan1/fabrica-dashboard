#!/usr/bin/env bash
# Publishes the portfolio to https://djoguzhan1.github.io/oguzehan-salatan/
# Run once on your machine (GitHub CLI logged in: gh auth login).
set -euo pipefail

REPO="djoguzhan1/oguzehan-salatan"
SRC="$(cd "$(dirname "$0")/../web-dev-portfolio" && pwd)"
WORKDIR="${TMPDIR:-/tmp}/oguzehan-salatan-publish"
SITE="https://djoguzhan1.github.io/oguzehan-salatan/"

echo "→ Source: $SRC"

if ! gh auth status >/dev/null 2>&1; then
  echo "Run: gh auth login"
  exit 1
fi

if gh repo view "$REPO" >/dev/null 2>&1; then
  echo "→ Repo exists: $REPO"
  rm -rf "$WORKDIR"
  gh repo clone "$REPO" "$WORKDIR"
else
  echo "→ Creating public repo $REPO"
  mkdir -p "$WORKDIR"
  gh repo create "$REPO" --public --description "Portfolio and live demo sites"
  gh repo clone "$REPO" "$WORKDIR"
fi

rsync -a --delete \
  --exclude PUBLISH.md \
  --exclude SETUP-LIVE.md \
  "$SRC/" "$WORKDIR/"

cd "$WORKDIR"
git add -A
if git diff --staged --quiet; then
  echo "→ No file changes to push."
else
  git commit -m "Publish portfolio hub and live demos"
fi
git push origin master 2>/dev/null || git push origin main

echo "→ Enabling GitHub Pages (master / root) if needed…"
gh api "repos/$REPO/pages" -X POST \
  -f build_type=legacy \
  -f "source[branch]=$(git symbolic-ref --short HEAD)" \
  -f "source[path]=/" 2>/dev/null || true

echo ""
echo "Done. Wait 1–2 minutes, then open:"
echo "  $SITE"
echo "  ${SITE}demos/hvac-landing/"
echo "  ${SITE}demos/plumbing-landing/"
