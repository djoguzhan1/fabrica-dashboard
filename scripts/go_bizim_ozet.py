#!/usr/bin/env python3
"""Bizim sistem başarı özeti — Ek B / proposal_log.tsv (Insights gerçeği)."""
import argparse
import sys
from pathlib import Path

TARGETS = {
    "open_rate": 0.50,
    "reply_rate": 0.35,
    "hire_rate_given_reply": 0.45,
    "go_to_hire": 0.12,
}


def parse_tsv(path: Path):
    lines = [
        l
        for l in path.read_text(encoding="utf-8").splitlines()
        if l.strip() and not l.strip().startswith("#")
    ]
    if not lines:
        return []
    header = [h.strip() for h in lines[0].split("\t")]
    rows = []
    for line in lines[1:]:
        cols = line.split("\t")
        if len(cols) < len(header):
            cols += [""] * (len(header) - len(cols))
        rows.append(dict(zip(header, cols)))
    return rows


def truthy(val: str) -> bool:
    v = (val or "").strip().lower()
    return v in ("1", "yes", "y", "true", "evet", "açıldı", "opened")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("log", nargs="?", default="docs/proposal_log.tsv")
    ap.add_argument("--last", type=int, default=0, help="only last N GO sends")
    a = ap.parse_args()
    path = Path(a.log)
    if not path.is_file():
        print("Log yok:", path)
        print("Hedefler (bizim plan):", TARGETS)
        sys.exit(0)

    rows = parse_tsv(path)
    sends = [r for r in rows if (r.get("decision") or "").upper() in ("GO", "SNIPER", "GÖNDER", "SEND")]
    sends = [r for r in sends if (r.get("tier") or "").strip()]
    if a.last and len(sends) > a.last:
        sends = sends[-a.last :]

    n = len(sends)
    if n == 0:
        print("Henüz tier işaretli GO satırı yok. Gönderimde proposal_log.tsv doldur.")
        print("Hedefler:", TARGETS)
        sys.exit(0)

    opened = sum(1 for r in sends if truthy(r.get("opened_24h", "")))
    replied = sum(1 for r in sends if truthy(r.get("replied", "")))
    hired = sum(1 for r in sends if truthy(r.get("hired", "")))

    open_rate = opened / n
    reply_rate = replied / opened if opened else 0.0
    hire_given_reply = hired / replied if replied else 0.0
    go_hire = hired / n

    print("=== Bizim sistem (gerçek log) ===")
    print(f"GO gönderim (tier dolu): {n}")
    print(f"Açılma: {opened}/{n} = {open_rate:.1%}  (hedef ≥{TARGETS['open_rate']:.0%})")
    if opened:
        print(f"Cevap:  {replied}/{opened} = {reply_rate:.1%}  (hedef ≥{TARGETS['reply_rate']:.0%})")
    if replied:
        print(f"İşe alım (cevap sonrası): {hired}/{replied} = {hire_given_reply:.1%}")
    print(f"GO → işe alım: {hired}/{n} = {go_hire:.1%}  (hedef ≥{TARGETS['go_to_hire']:.0%})")

    by_tier = {}
    for r in sends:
        t = r.get("tier") or "?"
        by_tier.setdefault(t, {"n": 0, "h": 0})
        by_tier[t]["n"] += 1
        if truthy(r.get("hired", "")):
            by_tier[t]["h"] += 1
    print("\nPaket bazlı işe alım:")
    for t, v in sorted(by_tier.items()):
        print(f"  {t}: {v['h']}/{v['n']}")

    loss = {}
    for r in sends:
        if truthy(r.get("hired", "")):
            continue
        stage = (r.get("loss_stage") or "unknown").strip() or "unknown"
        loss[stage] = loss.get(stage, 0) + 1
    if loss:
        print("\nKayıp aşaması (işe alınmayanlar):")
        for k, v in sorted(loss.items(), key=lambda x: -x[1]):
            print(f"  {k}: {v}")

    print("\nNot: go_score P = iç EV tahmini; başarı yalnızca Insights + bu log.")


if __name__ == "__main__":
    main()
