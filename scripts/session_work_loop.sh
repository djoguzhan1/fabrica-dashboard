#!/bin/bash
# Background validation loop for long strengthen sessions.
START="${SESSION_START:-$(date +%s)}"
END=$((START + 1800))
LOG="${SESSION_LOG:-docs/session-strengthen.log}"
mkdir -p "$(dirname "$LOG")"
echo "session start=$START end=$END" >> "$LOG"
while (( $(date +%s) < END )); do
  TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  if python3 tests/test_go_precheck.py && python3 tests/test_go_score.py && python3 tests/test_proposal_lint.py; then
    echo "$TS tests=PASS elapsed=$(( $(date +%s) - START ))s" >> "$LOG"
  else
    echo "$TS tests=FAIL elapsed=$(( $(date +%s) - START ))s" >> "$LOG"
  fi
  sleep 300
done
echo "session complete elapsed=$(( $(date +%s) - START ))s" >> "$LOG"
