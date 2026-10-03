#!/bin/bash
# Append one line to proposal log (Ek B). Create file if missing.
# Usage: ./scripts/log_proposal.sh "2026-10-01,GO,120,WP-fix,tam-paket,27,opened,..."
LOG="${PROPOSAL_LOG:-docs/proposal-log.csv}"
HEADER="date,decision,budget,arena,band,boost_b4,boost_status,opened,replied,hired,primary_note,b4_at_skip"
if [[ ! -f "$LOG" ]]; then
  echo "$HEADER" > "$LOG"
fi
echo "$1" >> "$LOG"
