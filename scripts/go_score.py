#!/usr/bin/env python3
"""Estimate hire probability for one Upwork job before spending Connects.

Usage (answer from the job page; omit what you don't know):
  python3 scripts/go_score.py --age 12 --proposals 4 --budget 120 --verified \
      --interviewing 0 --invites 0 --client-hires 0 --hires-new-freelancers \
      --scope-clear --demo-match exact --prework strong --invite

Prints the funnel estimate and a SNIPER / GO / SKIP decision.
Weights are priors; recalibrate them from the proposal log every 10 sends.
"""
import argparse

SNIPER_MIN = 0.25
GO_MIN = 0.10


def clamp(x, lo=0.02, hi=0.95):
    return max(lo, min(hi, x))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--age", type=float, default=30, help="job age in minutes")
    ap.add_argument("--proposals", type=int, default=3,
                    help="at send time (early push); not used for SNIPER/GO band")
    ap.add_argument("--budget", type=float, default=100)
    ap.add_argument("--verified", action="store_true", help="payment verified")
    ap.add_argument("--interviewing", type=int, default=0)
    ap.add_argument("--invites", type=int, default=0)
    ap.add_argument("--client-hires", type=int, default=0)
    ap.add_argument("--client-hire-rate", type=float, default=None, help="0-100")
    ap.add_argument("--hires-new-freelancers", action="store_true", help="history shows low-review hires")
    ap.add_argument("--scope-clear", action="store_true")
    ap.add_argument("--demo-match", choices=["exact", "close", "none"], default="close")
    ap.add_argument("--prework", choices=["strong", "light", "none"], default="light")
    ap.add_argument("--boost-top4", action="store_true", help="B4+1 fits under the cap")
    ap.add_argument("--invite", action="store_true", help="client invited us")
    ap.add_argument("--reviews", type=int, default=0, help="our public reviews")
    ap.add_argument("--client-spent", type=float, default=0, help="client lifetime spend USD")
    ap.add_argument("--chat-ready", action="store_true", help="§23 reply templates prepped for this thread")
    a = ap.parse_args()

    if not a.verified:
        print("SKIP: payment not verified")
        return
    if a.budget < 50:
        print("SKIP: budget below $50")
        return

    vel = a.proposals / max(a.age, 5.0)  # only for bot-wave penalty, not band label

    # open rate
    o = 0.35
    if a.invite:
        o = 0.90
    else:
        o += 0.20 if a.boost_top4 else 0.0
        o += 0.15 if a.age <= 15 else (0.05 if a.age <= 45 else -0.15)
        # Proposal count spikes after the early window; K1/K2 already SKIP bots/crowds.
        if vel > 1.0:
            o -= 0.25
        elif a.proposals >= 20:
            o -= 0.15
        o += {"strong": 0.10, "light": 0.03, "none": -0.10}[a.prework]
        o -= 0.25 if a.interviewing >= 2 else (0.10 if a.interviewing == 1 else 0.0)
        o -= 0.15 if a.invites >= 5 else 0.0
    o = clamp(o)

    # opened -> reply
    r = 0.25
    r += {"exact": 0.15, "close": 0.05, "none": -0.10}[a.demo_match]
    r += {"strong": 0.12, "light": 0.03, "none": -0.10}[a.prework]
    r += 0.08 if a.scope_clear else -0.05
    r += 0.15 if a.invite else 0.0
    r = clamp(r)

    # reply -> hire
    h = 0.45
    h += 0.08 if a.hires_new_freelancers else 0.0
    h += 0.06 if a.client_hires == 0 else 0.0
    if a.client_hire_rate is not None and a.client_hire_rate < 30 and a.client_hires >= 5:
        h -= 0.20
    h += min(a.reviews, 5) * 0.03
    h += 0.10 if a.invite else 0.0
    if a.client_hire_rate is not None and a.client_hire_rate >= 70 and a.client_spent >= 100:
        h += 0.05
    if a.chat_ready:
        h += 0.04
    h = clamp(h)

    p = o * r * h
    decision = "SNIPER" if p >= SNIPER_MIN else ("GO" if p >= GO_MIN else "SKIP")
    # Band label: package + activity + boost — not raw proposal count (§5.4 K1/K2, §20.1).
    band = "davet" if a.invite else None
    if band is None:
        if (
            a.boost_top4
            and a.prework == "strong"
            and a.demo_match in ("exact", "close")
            and a.scope_clear
            and a.interviewing == 0
            and a.invites < 5
        ):
            band = "tam-paket"
        elif a.prework == "none" or a.demo_match == "none" or a.interviewing >= 2:
            band = "risk"
        else:
            band = "standart"
    print(f"open {o:.0%} x reply {r:.0%} x hire {h:.0%} = {p:.1%}  ->  {decision}  band={band}")


if __name__ == "__main__":
    main()
