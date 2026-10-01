#!/usr/bin/env python3
"""Suggest send window in client local business hours (09:00–11:30)."""
import argparse
from datetime import datetime, timezone, timedelta

# UTC offsets (simplified; no DST — log warns)
OFFSETS = {
    "US": -5, "USA": -5, "UNITED STATES": -5,
    "UK": 0, "GB": 0, "UNITED KINGDOM": 0,
    "DE": 1, "GERMANY": 1,
    "AU": 10, "AUSTRALIA": 10,
    "CA": -5, "CANADA": -5,
    "TR": 3, "TURKEY": 3,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", default="US")
    ap.add_argument("--now-utc", default=None, help="ISO UTC for tests")
    a = ap.parse_args()
    key = a.country.upper().strip()
    off = OFFSETS.get(key, 0)
    now = datetime.now(timezone.utc)
    if a.now_utc:
        now = datetime.fromisoformat(a.now_utc.replace("Z", "+00:00"))
    local = now + timedelta(hours=off)
    start = local.replace(hour=9, minute=0, second=0, microsecond=0)
    end = local.replace(hour=11, minute=30, second=0, microsecond=0)
    in_window = start <= local <= end
    print(f"client_local={local.strftime('%Y-%m-%d %H:%M')} offset_utc={off:+d}")
    print(f"window=09:00-11:30 local in_window={in_window}")
    if not in_window:
        if local < start:
            wait = start - local
        else:
            wait = (start + timedelta(days=1)) - local
        print(f"suggest_wait={wait}")


if __name__ == "__main__":
    main()
