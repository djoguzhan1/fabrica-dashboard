#!/bin/bash
# Run structural precheck then score. Proposal count omitted (defaults to early-send prior).
set -euo pipefail
BUDGET="${1:?budget}"
shift
POST="${POST_FILE:-/tmp/job_post.txt}"
python3 "$(dirname "$0")/go_precheck.py" --budget "$BUDGET" "$@" --description-file "$POST"
python3 "$(dirname "$0")/go_score.py" --budget "$BUDGET" --verified --proposals 3 \
  --boost-top4 --prework strong --scope-clear --demo-match exact "$@"
