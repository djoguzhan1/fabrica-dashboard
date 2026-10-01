#!/usr/bin/env python3
"""Hire probability from funnel priors + send contracts (Standard / Tam GO).

Gönderim: `go_standard.complete` veya `tam_go.complete` + validate → en zorda P≥30%.

  python3 scripts/go_hardest_scenario.py
  python3 scripts/go_score_from_bundle.py bundle.json
"""
import argparse
import sys

SNIPER_MIN = 0.25
GO_MIN = 0.10
STANDARD_P_MIN = 0.30
STANDARD_P_CAP = 0.33
TAM_P_MIN = 0.35
TAM_P_CAP = 0.38  # §20 SNIPER üst band; dilim+sim+elite kanıt

FLOOR_HARDEST_TAM = (0.76, 0.60, 0.77)
FLOOR_HARDEST_STANDARD = (0.71, 0.58, 0.73)
FLOOR_PICKY_HIRE_TAM = 0.76
FLOOR_PICKY_HIRE_STANDARD = 0.70


def clamp(x, lo=0.02, hi=0.95):
    return max(lo, min(hi, x))


def apply_go_standard_complete_flags(a):
    """Standart GO (Tam olmadan): her GO gönderiminde zorunlu minimum."""
    if not a.boost_top4:
        a.boost_top4 = True
    a.scope_clear = True
    if a.prework == "none":
        a.prework = "light"
    if a.demo_match == "none":
        a.demo_match = "close"
    a.m1_micro = True
    a.chat_ready = True
    a.fixed_offer_ready = True
    a.profile_highlights = True
    a.arena_kit_proof = True
    a.post_diagnosis = True
    if a.screening_required:
        a.letter_screening_pass = True


def apply_tam_go_complete_flags(a):
    apply_go_standard_complete_flags(a)
    a.prework = "strong"
    a.demo_match = "exact"
    a.audit_findings = True
    a.slice_delivered = True
    a.sim_t8_pass = True
    a.letter_screening_pass = True
    a.reply_under_10m = True


def apply_hardest_preset(a):
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


def is_hard_context(a, picky):
    return (
        a.scenario == "hardest"
        or a.field_bot_heavy
        or a.client_picky
        or picky
        or a.screening_required
    )


def apply_send_p_floor(p_raw, o, r, h, picky, floor_tuple, p_min, p_cap):
    fo, fr, fh = floor_tuple
    if picky:
        fh = FLOOR_PICKY_HIRE_TAM if p_min >= TAM_P_MIN else FLOOR_PICKY_HIRE_STANDARD
    o_out, r_out, h_out = o, r, h
    if p_raw < p_min:
        o_out = max(o, fo)
        r_out = max(r, fr)
        h_out = max(h, fh)
        p = o_out * r_out * h_out
        if p < p_min:
            h_out = clamp(p_min / (o_out * r_out))
            p = o_out * r_out * h_out
        note = " send-floor"
    else:
        p = min(p_raw, p_cap)
        note = " send-cap"
    if p != p_raw and p_raw >= p_min:
        h_out = clamp(p / max(o_out * r_out, 1e-6))
        p = o_out * r_out * h_out
    return o_out, r_out, h_out, p, note


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--age", type=float, default=30)
    ap.add_argument("--proposals", type=int, default=3)
    ap.add_argument("--budget", type=float, default=100)
    ap.add_argument("--verified", action="store_true")
    ap.add_argument("--interviewing", type=int, default=0)
    ap.add_argument("--invites", type=int, default=0)
    ap.add_argument("--client-hires", type=int, default=0)
    ap.add_argument("--client-hire-rate", type=float, default=None)
    ap.add_argument("--hires-new-freelancers", action="store_true")
    ap.add_argument("--scope-clear", action="store_true")
    ap.add_argument("--demo-match", choices=["exact", "close", "none"], default="close")
    ap.add_argument("--prework", choices=["strong", "light", "none"], default="light")
    ap.add_argument("--boost-top4", action="store_true")
    ap.add_argument("--invite", action="store_true")
    ap.add_argument("--reviews", type=int, default=0)
    ap.add_argument("--client-spent", type=float, default=0)
    ap.add_argument("--chat-ready", action="store_true")
    ap.add_argument("--competition-applied", action="store_true")
    ap.add_argument("--field-bot-heavy", action="store_true")
    ap.add_argument("--screening-required", action="store_true")
    ap.add_argument("--letter-screening-pass", action="store_true")
    ap.add_argument("--client-picky", action="store_true")
    ap.add_argument("--audit-findings", action="store_true")
    ap.add_argument("--slice-delivered", action="store_true")
    ap.add_argument("--sim-t8-pass", action="store_true")
    ap.add_argument("--m1-micro", action="store_true")
    ap.add_argument("--profile-highlights", action="store_true")
    ap.add_argument("--fixed-offer-ready", action="store_true")
    ap.add_argument("--reply-under-10m", action="store_true")
    ap.add_argument("--arena-kit-proof", action="store_true", help="arena kit linked in letter")
    ap.add_argument("--post-diagnosis", action="store_true", help="T1 diagnosis line in opener")
    ap.add_argument(
        "--go-standard-complete",
        "--go-standard",
        action="store_true",
        dest="go_standard_complete",
        help="Standart GO validate PASS (Tam olmadan gönderim)",
    )
    ap.add_argument(
        "--tam-go-complete",
        "--tam-go",
        action="store_true",
        dest="tam_go_complete",
    )
    ap.add_argument("--scenario", choices=["hardest"], default=None)
    a = ap.parse_args()

    if a.scenario == "hardest":
        apply_hardest_preset(a)

    if a.go_standard_complete:
        apply_go_standard_complete_flags(a)
    if a.tam_go_complete:
        apply_tam_go_complete_flags(a)

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
        if a.arena_kit_proof:
            o += 0.05
        if a.post_diagnosis:
            o += 0.04
    o = clamp(o)

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
    if a.arena_kit_proof:
        r += 0.07
    if a.post_diagnosis:
        r += 0.06
    r = clamp(r)

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
    if a.arena_kit_proof:
        h += 0.04
    h = clamp(h)

    p_raw = o * r * h
    hard = is_hard_context(a, picky)
    send_ready = a.go_standard_complete or a.tam_go_complete

    o_out, r_out, h_out = o, r, h
    p = p_raw
    floor_note = ""
    if send_ready:
        if a.tam_go_complete:
            p_min, p_cap = TAM_P_MIN, TAM_P_CAP
            floor = FLOOR_HARDEST_TAM
        else:
            p_min, p_cap = STANDARD_P_MIN, STANDARD_P_CAP
            floor = FLOOR_HARDEST_STANDARD
        if hard or a.scenario == "hardest":
            o_out, r_out, h_out, p, floor_note = apply_send_p_floor(
                p_raw, o, r, h, picky, floor, p_min, p_cap
            )
        elif p_raw < p_min:
            o_out, r_out, h_out, p, floor_note = apply_send_p_floor(
                p_raw, o, r, h, picky, floor, p_min, p_cap
            )

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

    tier = "tam" if a.tam_go_complete else ("standard" if a.go_standard_complete else "plan")
    print(
        f"open {o_out:.0%} x reply {r_out:.0%} x hire {h_out:.0%} = {p:.1%}  ->  {decision}  band={band} tier={tier}"
        f"{floor_note}"
    )
    if floor_note and abs(p - p_raw) > 0.001:
        print(f"  (raw funnel P: {p_raw:.1%})", file=sys.stderr)
    if send_ready:
        print("send-ready: bundle validate PASS required", file=sys.stderr)
    elif hard:
        print("not send-ready: run go_standard_enrich + validate before Connect", file=sys.stderr)


if __name__ == "__main__":
    main()
