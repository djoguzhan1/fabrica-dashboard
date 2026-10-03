#!/usr/bin/env python3
"""Expected net USD per proposal from go_score-style inputs.

Usage:
  python3 scripts/estimate_ev.py --budget 120 --p 0.30 --connects-submit 8 --boost-bid 27
"""
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, required=True)
    ap.add_argument("--p", type=float, required=True, help="hire probability 0-1")
    ap.add_argument("--connects-submit", type=int, default=8)
    ap.add_argument("--boost-bid", type=int, default=0)
    ap.add_argument("--connect-price", type=float, default=0.15)
    ap.add_argument("--fee", type=float, default=0.10, help="Upwork fee fraction")
    a = ap.parse_args()

    net_job = a.budget * (1 - a.fee)
    connect_cost = (a.connects_submit + a.boost_bid) * a.connect_price
    ev = a.p * net_job - connect_cost
    print(f"net_if_hired=${net_job:.2f} connect_cost=${connect_cost:.2f} P={a.p:.1%} EV=${ev:.2f}")

    if connect_cost > a.budget * 0.15:
        print("WARN: connect spend > 15% of budget (§6)")


if __name__ == "__main__":
    main()
