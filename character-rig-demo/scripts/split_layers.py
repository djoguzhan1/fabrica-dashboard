#!/usr/bin/env python3
"""Split a single character illustration into rig layers (normalized polygons)."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "source.jpg"
OUT = ROOT / "assets" / "layers"

# Normalized polygons for 720x1280 — forest night, standing full-body (user asset only).
# Each layer: one polygon or a list of polygons (for disjoint background strips).
LayerPolys = list[tuple[float, float]] | list[list[tuple[float, float]]]

LAYER_DEFS: dict[str, LayerPolys] = {
    # Forest + ground (frame strips; character filled by layers above)
    "background": [
        [(0, 0), (1, 0), (1, 0.1), (0, 0.1)],
        [(0, 0.56), (1, 0.56), (1, 1), (0, 1)],
        [(0, 0), (0.16, 0), (0.16, 1), (0, 1)],
        [(0.84, 0), (1, 0), (1, 1), (0.84, 1)],
    ],
    # Long green hair (behind body; sways with head)
    "hair_back": [
        (0.04, 0.08),
        (0.96, 0.08),
        (0.99, 0.8),
        (0.01, 0.8),
    ],
    # Torso + arms behind back
    "torso": [
        (0.2, 0.23),
        (0.8, 0.23),
        (0.84, 0.5),
        (0.16, 0.5),
    ],
    # Legs, stockings, feet
    "legs": [
        (0.14, 0.46),
        (0.86, 0.46),
        (0.93, 1),
        (0.07, 1),
    ],
    # Face + hat crown (bells separate)
    "head": [
        (0.2, 0.015),
        (0.8, 0.015),
        (0.82, 0.245),
        (0.18, 0.245),
    ],
    "bell_left": [
        (0.01, 0.02),
        (0.19, 0.02),
        (0.21, 0.19),
        (0.03, 0.21),
    ],
    "bell_right": [
        (0.81, 0.02),
        (0.99, 0.02),
        (0.97, 0.21),
        (0.79, 0.19),
    ],
}


def _normalize_polys(points: LayerPolys) -> list[list[tuple[float, float]]]:
    if not points:
        return []
    if isinstance(points[0], tuple):
        return [points]  # type: ignore[list-item]
    return points  # type: ignore[return-value]


def poly_mask(size: tuple[int, int], polys: list[list[tuple[float, float]]]) -> Image.Image:
    w, h = size
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    for points in polys:
        px = [(x * w, y * h) for x, y in points]
        draw.polygon(px, fill=255)
    return mask


def polygon_centroid(points: list[tuple[float, float]]) -> tuple[float, float]:
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    return cx, cy


def layer_centroid(polys: list[list[tuple[float, float]]]) -> tuple[float, float]:
    if len(polys) == 1:
        return polygon_centroid(polys[0])
    # Weighted by bounding-box area (rough pivot for multi-strip background)
    total = 0.0
    sx = sy = 0.0
    for points in polys:
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        area = (max(xs) - min(xs)) * (max(ys) - min(ys))
        cx, cy = polygon_centroid(points)
        total += area
        sx += cx * area
        sy += cy * area
    return sx / total, sy / total


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
    meta: dict[str, dict] = {"size": list(base.size), "layers": {}}

    for name, raw in LAYER_DEFS.items():
        polys = _normalize_polys(raw)
        mask = poly_mask(base.size, polys)
        layer = extract_layer(base, mask)
        path = OUT / f"{name}.png"
        layer.save(path)
        cx, cy = layer_centroid(polys)
        meta["layers"][name] = {
            "file": f"layers/{name}.png",
            "pivot": [cx, cy],
            "z": list(LAYER_DEFS.keys()).index(name),
        }

    base.save(OUT / "_full.png")

    preview = base.copy()
    draw = ImageDraw.Draw(preview)
    w, h = base.size
    for name, raw in LAYER_DEFS.items():
        for points in _normalize_polys(raw):
            px = [(x * w, y * h) for x, y in points]
            draw.polygon(px, outline=(255, 64, 64, 200), width=2)
            draw.text(px[0], name, fill=(255, 255, 0, 255))

    preview.save(OUT / "_mask_preview.png")
    (OUT / "manifest.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Wrote {len(LAYER_DEFS)} layers to {OUT} ({base.size[0]}x{base.size[1]})")


if __name__ == "__main__":
    main()
