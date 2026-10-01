#!/bin/bash
# Run structural precheck then score. Proposal count omitted (defaults to early-send prior).
set -euo pipefail
BUDGET="${1:?budget}"
shift
POST="${POST_FILE:-/tmp/job_post.txt}"
PRECHECK="$(dirname "$0")/go_precheck.py"
SCORE="$(dirname "$0")/go_score.py"
python3 "$PRECHECK" --budget "$BUDGET" "$@" --description-file "$POST"
# proposals=3 = early notification prior; not used for band label
python3 "$SCORE" --budget "$BUDGET" --verified --proposals 3 \
  --boost-top4 --prework strong --scope-clear --demo-match exact "$@"
