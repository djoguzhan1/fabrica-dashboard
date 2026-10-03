#!/usr/bin/env python3
"""Split a single character illustration into rig layers (normalized polygons)."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "source.jpg"
OUT = ROOT / "assets" / "layers"

# User forest JPG, arms at sides (720x1280).
LayerPolys = list[tuple[float, float]] | list[list[tuple[float, float]]]

LAYER_DEFS: dict[str, LayerPolys] = {
    "background": [
        [(0, 0), (1, 0), (1, 0.09), (0, 0.09)],
        [(0, 0.56), (1, 0.56), (1, 1), (0, 1)],
        [(0, 0.09), (0.05, 0.09), (0.05, 0.56), (0, 0.56)],
        [(0.95, 0.09), (1, 0.09), (1, 0.56), (0.95, 0.56)],
    ],
    "hair_back": [
        (0.04, 0.08),
        (0.96, 0.08),
        (0.99, 0.82),
        (0.01, 0.82),
    ],
    # Screen-left arm (character right)
    "arm_l_upper": [
        (0.0, 0.245),
        (0.155, 0.245),
        (0.17, 0.385),
        (0.02, 0.395),
    ],
    "arm_l_lower": [
        (0.02, 0.37),
        (0.175, 0.37),
        (0.19, 0.535),
        (0.04, 0.545),
    ],
    # Screen-right arm (character left)
    "arm_r_upper": [
        (0.845, 0.245),
        (1.0, 0.245),
        (0.98, 0.395),
        (0.83, 0.385),
    ],
    "arm_r_lower": [
        (0.825, 0.37),
        (0.98, 0.37),
        (0.96, 0.545),
        (0.81, 0.535),
    ],
    "torso": [
        (0.2, 0.23),
        (0.8, 0.23),
        (0.84, 0.5),
        (0.16, 0.5),
    ],
    "legs": [
        (0.14, 0.46),
        (0.86, 0.46),
        (0.93, 1),
        (0.07, 1),
    ],
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

# Joint pivots (normalized); limbs use these instead of polygon centroid.
PIVOT_OVERRIDES: dict[str, tuple[float, float]] = {
    "arm_l_upper": (0.12, 0.26),
    "arm_l_lower": (0.11, 0.39),
    "arm_r_upper": (0.88, 0.26),
    "arm_r_lower": (0.89, 0.39),
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
        if name in PIVOT_OVERRIDES:
            cx, cy = PIVOT_OVERRIDES[name]
        else:
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
        if name in PIVOT_OVERRIDES:
            px, py = PIVOT_OVERRIDES[name]
            draw.ellipse((px * w - 4, py * h - 4, px * w + 4, py * h + 4), fill=(0, 255, 128, 255))

    preview.save(OUT / "_mask_preview.png")
    (OUT / "manifest.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Wrote {len(LAYER_DEFS)} layers to {OUT} ({base.size[0]}x{base.size[1]})")


if __name__ == "__main__":
    main()
