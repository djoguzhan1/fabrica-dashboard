"""Build WordPress Playground blueprints from the static landing demos.

Each demo's <body> is split into one Custom HTML block per top-level section,
so the page stays editable section-by-section in the WordPress editor.
Run from the repo root: python3 wordpress-demos/build.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
BRANCH = "cursor/upwork-job-alerts-fc98"
RAW = f"https://raw.githubusercontent.com/djoguzhan1/fabrica-dashboard/{BRANCH}/wordpress-demos/"
ASSETS = "https://djoguzhan1.github.io/web-dev-portfolio/demos/"

DEMOS = {
    "hvac-landing": {"title": "CoolAir HVAC", "site": "CoolAir HVAC · Dallas–Fort Worth"},
    "plumbing-landing": {"title": "ProFix Plumbing", "site": "ProFix Plumbing"},
}

SECTION_START = re.compile(r"^(  <(?!/)(?!main\b)[a-z]|    <section\b)")


def body_blocks(slug: str) -> str:
    html = (ROOT / "web-dev-portfolio/demos" / slug / "index.html").read_text()
    body = html.split("<body>", 1)[1].rsplit("</body>", 1)[0]
    body = re.sub(r'\s*<script src="main\.js" defer></script>', "", body)
    # Each block must hold balanced HTML, so <main> cannot span blocks; the skip link target moves to the first section.
    body = body.replace('  <main id="main">', "").replace("  </main>", "")
    body = body.replace('<section class="hero"', '<section id="main" class="hero"', 1)
    body = re.sub(r'((?:src|srcset|href)=")img/', rf"\g<1>{ASSETS}{slug}/img/", body)
    body = re.sub(r"(,\s*)img/", rf"\g<1>{ASSETS}{slug}/img/", body)
    body = body.replace('href="../../index.html"', 'href="https://djoguzhan1.github.io/web-dev-portfolio/"')
    body = re.sub(
        r"Demo website · (.+?) is a fictional company built to show what your site could look like\.",
        r"WordPress demo · \1 is a fictional company. This page runs on WordPress; every section is an editable block.",
        body,
    )

    chunks, current = [], []
    for line in body.splitlines():
        if SECTION_START.match(line) and current and any(l.strip() for l in current):
            chunks.append("\n".join(current))
            current = []
        current.append(line)
    chunks.append("\n".join(current))

    return "\n\n".join(
        f"<!-- wp:html -->\n{c.strip()}\n<!-- /wp:html -->" for c in chunks if c.strip()
    )


def blueprint(slug: str, meta: dict) -> dict:
    php = f"""<?php
require '/wordpress/wp-load.php';
$id = wp_insert_post( array(
	'post_type'    => 'page',
	'post_status'  => 'publish',
	'post_author'  => 1,
	'post_title'   => {json.dumps(meta["title"], ensure_ascii=False)},
	'post_content' => wp_slash( file_get_contents( '/wordpress/wp-content/demo-content.html' ) ),
) );
update_post_meta( $id, '_demo_landing', {json.dumps(slug)} );
update_option( 'show_on_front', 'page' );
update_option( 'page_on_front', $id );
update_option( 'blogname', {json.dumps(meta["site"], ensure_ascii=False)} );
"""
    return {
        "$schema": "https://playground.wordpress.net/blueprint-schema.json",
        "landingPage": "/",
        "preferredVersions": {"php": "8.2", "wp": "latest"},
        "features": {"networking": True},
        "steps": [
            {"step": "login"},
            {"step": "mkdir", "path": "/wordpress/wp-content/mu-plugins/demo-landing"},
            {"step": "writeFile", "path": "/wordpress/wp-content/mu-plugins/demo-landing.php",
             "data": {"resource": "url", "url": RAW + "demo-landing.php"}},
            {"step": "writeFile", "path": "/wordpress/wp-content/mu-plugins/demo-landing/template.php",
             "data": {"resource": "url", "url": RAW + "template.php"}},
            {"step": "writeFile", "path": "/wordpress/wp-content/demo-content.html",
             "data": {"resource": "url", "url": RAW + f"content-{slug}.html"}},
            {"step": "runPHP", "code": php},
        ],
    }


for slug, meta in DEMOS.items():
    (OUT / f"content-{slug}.html").write_text(body_blocks(slug) + "\n")
    (OUT / f"blueprint-{slug}.json").write_text(json.dumps(blueprint(slug, meta), indent=2, ensure_ascii=False) + "\n")
    print(slug, "ok")
