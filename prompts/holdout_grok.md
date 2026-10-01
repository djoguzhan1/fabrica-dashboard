# Holdout judge (grok-4.7-low) — calibration only

Blind: you see letter + card + prework summary, NOT other judges' scores.

Question: "If you were this client, would you hire without a call? yes/no"
Then: "One sentence: what feels fake or off-scope?"

If verdict disagrees with outcome after 10 live sends, weights in go_score.py get adjusted (§12).

Output: `{"hire":"yes|no","off_scope":true|false,"verdict":"PASS|FAIL"}`
