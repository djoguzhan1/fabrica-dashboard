#!/usr/bin/env python3
import subprocess
import sys

import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(budget, title, desc, extra=()):
    p = subprocess.run(
        [sys.executable, f"{ROOT}/scripts/go_precheck.py", "--budget", str(budget),
         "--payment-verified", "--title", title, *extra],
        input=desc,
        capture_output=True,
        text=True,
    )
    return p.returncode, p.stdout + p.stderr


def test_rag_skip():
    code, out = run(100, "Fix RAG", "LangChain Pinecone vector database retrieval")
    assert code == 1 and "arena outside" in out


def test_ongoing_skip():
    code, out = run(50, "Figma", "figma to html landing", ["--ongoing"])
    assert code == 1 and "ongoing" in out


def test_wp_go():
    code, out = run(120, "Elementor fix", "Fix mobile menu on WordPress Elementor site /contact")
    assert code == 0 and "GO" in out


def test_picky_skip_without_flag():
    code, out = run(
        120, "Elementor", "Fix Elementor mobile",
        ["--client-hire-rate", "25", "--client-hires", "8"],
    )
    assert code == 1 and "hire rate <30%" in out


def test_picky_warn_with_allow():
    code, out = run(
        120, "Elementor", "Fix Elementor mobile",
        ["--client-hire-rate", "25", "--client-hires", "8", "--allow-picky-client",
         "--age-minutes", "12", "--proposals", "6"],
    )
    assert code == 0 and "picky client" in out


def test_k1_skip():
    code, out = run(
        120, "Elementor", "Fix Elementor",
        ["--age-minutes", "70", "--proposals", "12"],
    )
    assert code == 1 and "K1" in out


if __name__ == "__main__":
    test_rag_skip()
    test_ongoing_skip()
    test_wp_go()
    test_picky_skip_without_flag()
    test_picky_warn_with_allow()
    test_k1_skip()
    print("ok")
