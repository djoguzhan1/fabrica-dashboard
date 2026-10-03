#!/usr/bin/env python3
"""Split a single character illustration into rig layers (normalized polygons)."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "source.jpg"
OUT = ROOT / "assets" / "layers"
# Normalized polygon points (x, y) in 0..1, tuned for 816x1264 source pose.
LAYER_DEFS: dict[str, list[tuple[float, float]]] = {
    # Bed / room (static back)
    "background": [
        (0, 0),
        (1, 0),
        (1, 0.42),
        (0.72, 0.38),
        (0.28, 0.38),
        (0, 0.42),
    ],
    # Hair mass behind head & shoulders
    "hair_back": [
        (0.18, 0.12),
        (0.82, 0.12),
        (0.88, 0.55),
        (0.12, 0.55),
    ],
    # Torso + arms (mostly hidden; moves as one block for breathing)
    "torso": [
        (0.22, 0.38),
        (0.78, 0.38),
        (0.85, 0.72),
        (0.15, 0.72),
    ],
    # Legs / knees (foreground)
    "legs": [
        (0.12, 0.48),
        (0.88, 0.48),
        (0.95, 1),
        (0.05, 1),
    ],
    # Head + face (rotates slightly)
    "head": [
        (0.28, 0.02),
        (0.72, 0.02),
        (0.78, 0.34),
        (0.22, 0.34),
    ],
    # Jester hat bells (secondary motion)
    "bell_left": [
        (0.05, 0.02),
        (0.22, 0.02),
        (0.24, 0.18),
        (0.06, 0.2),
    ],
    "bell_right": [
        (0.78, 0.02),
        (0.95, 0.02),
        (0.94, 0.2),
        (0.76, 0.18),
    ],
}


def poly_mask(size: tuple[int, int], points: list[tuple[float, float]]) -> Image.Image:
    w, h = size
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    px = [(x * w, y * h) for x, y in points]
    draw.polygon(px, fill=255)
    return mask


def extract_layer(base: Image.Image, mask: Image.Image) -> Image.Image:
    rgba = base.convert("RGBA")
    out = Image.new("RGBA", base.size, (0, 0, 0, 0))
    out.paste(rgba, mask=mask)
    return out


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Missing source: {SRC}")

    base = Image.open(SRC).convert("RGBA")
    OUT.mkdir(parents=True, exist_ok=True)
    meta: dict[str, dict] = {"size": base.size, "layers": {}}

    for name, points in LAYER_DEFS.items():
        mask = poly_mask(base.size, points)
        layer = extract_layer(base, mask)
        path = OUT / f"{name}.png"
        layer.save(path)
        # Pivot: polygon centroid (normalized)
        cx = sum(p[0] for p in points) / len(points)
        cy = sum(p[1] for p in points) / len(points)
        meta["layers"][name] = {
            "file": f"layers/{name}.png",
            "pivot": [cx, cy],
            "z": list(LAYER_DEFS.keys()).index(name),
        }

    # Full reference for alignment checks
    base.save(OUT / "_full.png")

    preview = base.copy()
    draw = ImageDraw.Draw(preview)
    w, h = base.size
    for name, points in LAYER_DEFS.items():
        px = [(x * w, y * h) for x, y in points]
        draw.polygon(px, outline=(255, 64, 64, 200), width=2)
        draw.text(px[0], name, fill=(255, 255, 0, 255))

    preview.save(OUT / "_mask_preview.png")
    (OUT / "manifest.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Wrote {len(LAYER_DEFS)} layers to {OUT}")


if __name__ == "__main__":
    main()
