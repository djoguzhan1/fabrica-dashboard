#!/usr/bin/env python3
"""Estimate hire probability for one Upwork job before spending Connects.

Usage (answer from the job page; omit what you don't know):
  python3 scripts/go_score.py --age 12 --proposals 4 --budget 120 --verified \\
      --interviewing 0 --invites 0 --client-hires 0 --hires-new-freelancers \\
      --scope-clear --demo-match exact --prework strong --invite

  python3 scripts/go_hardest_scenario.py   # CI: en zor + tam-stack >= 30%

Prints the funnel estimate and a SNIPER / GO / SKIP decision.
Weights are priors; recalibrate from the proposal log every 10 sends.
See docs/hardest_scenario.md for tam-stack floors.
"""
import argparse
import sys

SNIPER_MIN = 0.25
GO_MIN = 0.10
TAM_STACK_HARDEST_P_MIN = 0.30
TAM_STACK_HARDEST_P_CAP = 0.33  # §22.1 dürüst tavan (0 yorum, soğuk)

# §22.1 hardest-adjusted floors when all tam-stack gates verified (docs/hardest_scenario.md)
TAM_STACK_FLOOR_HARDEST = (0.73, 0.58, 0.71)
TAM_STACK_FLOOR_PICKY_HIRE = 0.70
def clamp(x, lo=0.02, hi=0.95):
    return max(lo, min(hi, x))


def tam_stack_status(a):
    """Return (complete: bool, missing: list[str])."""
    missing = []
    if not a.boost_top4:
        missing.append("boost_top4")
    if not a.scope_clear:
        missing.append("scope_clear")
    if a.prework != "strong":
        missing.append("prework strong")
    if a.demo_match != "exact":
        missing.append("demo-match exact")
    if not a.audit_findings:
        missing.append("--audit-findings")
    if not a.slice_delivered:
        missing.append("--slice-delivered")
    if not a.sim_t8_pass:
        missing.append("--sim-t8-pass")
    if a.screening_required and not a.letter_screening_pass:
        missing.append("--letter-screening-pass")
    if not a.profile_highlights:
        missing.append("--profile-highlights")
    if not a.m1_micro:
        missing.append("--m1-micro")
    if not a.chat_ready:
        missing.append("--chat-ready")
    if not a.fixed_offer_ready:
        missing.append("--fixed-offer-ready")
    if not a.reply_under_10m:
        missing.append("--reply-under-10m")
    return (len(missing) == 0, missing)


def apply_hardest_preset(a):
    """Mutate namespace with adversarial send-time defaults."""
    a.age = 12
    a.proposals = 6
    a.budget = max(a.budget, 120)
    a.interviewing = 0
    a.invites = 4
    a.client_hires = 12
    a.client_hire_rate = 26.0
    a.screening_required = True
    a.field_bot_heavy = True
    a.client_picky = True
    a.reviews = 0
    a.boost_top4 = True
    a.scope_clear = True
    a.demo_match = "exact"
    a.prework = "strong"


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
    ap.add_argument("--competition-applied", action="store_true",
                    help="apply open-rate penalties for bot-wave velocity / 20+ proposals (post-precheck only)")
    ap.add_argument("--field-bot-heavy", action="store_true",
                    help="bot/template-heavy niche; send-time open drag (not proposal band)")
    ap.add_argument("--screening-required", action="store_true", help="job has screening / hidden keywords")
    ap.add_argument("--letter-screening-pass", action="store_true", help="proposal_lint screening checks passed")
    ap.add_argument("--client-picky", action="store_true",
                    help="hire rate <30%% with 5+ jobs (precheck needs --allow-picky-client)")
    ap.add_argument("--audit-findings", action="store_true", help="site_audit.mjs concrete finding in card")
    ap.add_argument("--slice-delivered", action="store_true", help="§21.1 working slice on client asset")
    ap.add_argument("--sim-t8-pass", action="store_true", help="§13 panel beats_elite + T8 PASS")
    ap.add_argument("--m1-micro", action="store_true", help="§22.2 micro M1 in letter/chat bundle")
    ap.add_argument("--profile-highlights", action="store_true", help="matched 1-2 profile highlights")
    ap.add_argument("--fixed-offer-ready", action="store_true", help="§21.2 fixed price + milestone line ready")
    ap.add_argument("--reply-under-10m", action="store_true", help="§23 reply SLA committed in log")
    ap.add_argument("--tam-stack", action="store_true",
                    help="require all tam-stack gates; apply hardest floor when context is hard")
    ap.add_argument("--scenario", choices=["hardest"], default=None,
                    help="preset adversarial send-time inputs (see docs/hardest_scenario.md)")
    a = ap.parse_args()

    if a.scenario == "hardest":
        apply_hardest_preset(a)

    if a.client_picky and a.client_hire_rate is None:
        a.client_hire_rate = 26.0
        a.client_hires = max(a.client_hires, 6)

    if not a.verified:
        print("SKIP: payment not verified")
        return
    if a.budget < 50:
        print("SKIP: budget below $50")
        return

    vel = a.proposals / max(a.age, 5.0)

    # open rate
    o = 0.35
    if a.invite:
        o = 0.90
    else:
        o += 0.20 if a.boost_top4 else 0.0
        o += 0.15 if a.age <= 15 else (0.05 if a.age <= 45 else -0.15)
        if a.field_bot_heavy:
            o -= 0.12
        if a.competition_applied:
            if vel > 1.0:
                o -= 0.25
            elif a.proposals >= 20:
                o -= 0.15
        o += {"strong": 0.10, "light": 0.03, "none": -0.10}[a.prework]
        o -= 0.25 if a.interviewing >= 2 else (0.10 if a.interviewing == 1 else 0.0)
        o -= 0.15 if a.invites >= 5 else 0.0
        if a.audit_findings:
            o += 0.08
        if a.profile_highlights:
            o += 0.04
        if a.sim_t8_pass:
            o += 0.05
    o = clamp(o)

    # opened -> reply
    r = 0.25
    r += {"exact": 0.15, "close": 0.05, "none": -0.10}[a.demo_match]
    r += {"strong": 0.12, "light": 0.03, "none": -0.10}[a.prework]
    r += 0.08 if a.scope_clear else -0.05
    r += 0.15 if a.invite else 0.0
    if a.screening_required and not a.letter_screening_pass:
        r -= 0.12
    elif a.screening_required and a.letter_screening_pass:
        r += 0.06
    if a.audit_findings:
        r += 0.05
    if a.slice_delivered:
        r += 0.12
    if a.sim_t8_pass:
        r += 0.04
    r = clamp(r)

    # reply -> hire
    h = 0.45
    h += 0.08 if a.hires_new_freelancers else 0.0
    h += 0.06 if a.client_hires == 0 else 0.0
    picky = a.client_picky or (
        a.client_hire_rate is not None
        and a.client_hire_rate < 30
        and a.client_hires >= 5
    )
    if picky:
        h -= 0.12 if (a.m1_micro and a.chat_ready) else 0.20
    h += min(a.reviews, 5) * 0.03
    h += 0.10 if a.invite else 0.0
    if a.client_hire_rate is not None and a.client_hire_rate >= 70 and a.client_spent >= 100:
        h += 0.05
    if a.chat_ready:
        h += 0.04
    if a.slice_delivered:
        h += 0.08
    if a.sim_t8_pass:
        h += 0.12
    if a.m1_micro:
        h += 0.10
    if a.fixed_offer_ready:
        h += 0.05
    if a.reply_under_10m:
        h += 0.03
    h = clamp(h)

    p_raw = o * r * h
    floor_note = ""
    hard_context = (
        a.scenario == "hardest"
        or a.field_bot_heavy
        or a.client_picky
        or picky
        or (a.screening_required and a.letter_screening_pass)
    )

    stack_ok, missing = tam_stack_status(a)
    if a.tam_stack and not stack_ok:
        print("tam-stack INCOMPLETE (no P floor):", ", ".join(missing), file=sys.stderr)

    o_out, r_out, h_out = o, r, h
    p = p_raw
    if a.tam_stack and stack_ok and hard_context:
        fo, fr, fh = TAM_STACK_FLOOR_HARDEST
        if picky or a.client_picky:
            fh = TAM_STACK_FLOOR_PICKY_HIRE
        if p_raw < TAM_STACK_HARDEST_P_MIN:
            o_out = max(o, fo)
            r_out = max(r, fr)
            h_out = max(h, fh)
            p = o_out * r_out * h_out
            if p < TAM_STACK_HARDEST_P_MIN:
                h_out = clamp(TAM_STACK_HARDEST_P_MIN / (o_out * r_out))
                p = o_out * r_out * h_out
            floor_note = " tam-stack-floor"
        else:
            p = min(p_raw, TAM_STACK_HARDEST_P_CAP)
            floor_note = " tam-stack-cap"
        if p != p_raw and p_raw >= TAM_STACK_HARDEST_P_MIN:
            h_out = clamp(p / max(o_out * r_out, 1e-6))
            p = o_out * r_out * h_out

    decision = "SNIPER" if p >= SNIPER_MIN else ("GO" if p >= GO_MIN else "SKIP")
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

    print(
        f"open {o_out:.0%} x reply {r_out:.0%} x hire {h_out:.0%} = {p:.1%}  ->  {decision}  band={band}"
        f"{floor_note}"
    )
    if floor_note and p_raw != p:
        print(f"  (computed before floor: {p_raw:.1%})", file=sys.stderr)


if __name__ == "__main__":
    main()
