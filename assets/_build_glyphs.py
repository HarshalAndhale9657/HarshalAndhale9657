# -*- coding: utf-8 -*-
"""
Builds assets/fonts/glyphs.json — a glyph atlas (outlines + advances + pair
kerning) for every face the profile SVGs use.

Why: an SVG shown through <img> on GitHub can't load web fonts, so <text>
falls back to whatever the viewer has installed and the design drifts per
machine. Every string in these SVGs is therefore drawn as outlines. Building
the atlas needs fonttools + uharfbuzz once; everything downstream
(_design.py, _render.py, and the nightly _stats_generator.py in CI) only needs
the stdlib and this JSON.

Fonts (SIL OFL 1.1, licences alongside): Instrument Serif, Geist, Geist Mono.

    pip install fonttools uharfbuzz
    python assets/_build_glyphs.py <dir-with-ttfs>
"""
import io, json, os, sys

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

SRC = sys.argv[1] if len(sys.argv) > 1 else "."
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "glyphs.json")

FACES = {
    "serif":    ("instrumentserif__InstrumentSerif-Regular.ttf", None),
    "serif-it": ("instrumentserif__InstrumentSerif-Italic.ttf", None),
    "sans":     ("geist__Geist[wght].ttf", 400),
    "sans-md":  ("geist__Geist[wght].ttf", 500),
    "sans-sb":  ("geist__Geist[wght].ttf", 600),
    "mono":     ("geistmono__GeistMono[wght].ttf", 400),
    "mono-md":  ("geistmono__GeistMono[wght].ttf", 500),
}

CHARS = "".join(chr(c) for c in range(32, 127)) + "·—–−→↗×₹•’‘“”…✓≈≥≤←↓↑é§"


def load(fn, wght):
    f = TTFont(os.path.join(SRC, fn))
    if wght is not None and "fvar" in f:
        f = instantiateVariableFont(f, {"wght": wght})
    buf = io.BytesIO()
    f.save(buf)
    data = buf.getvalue()
    return TTFont(io.BytesIO(data)), data


def shape(hbfont, text):
    b = hb.Buffer()
    b.add_str(text)
    b.guess_segment_properties()
    hb.shape(hbfont, b, {"kern": True, "liga": False, "calt": False})
    return b.glyph_infos, b.glyph_positions


def num(v):
    v = round(v, 1)
    return str(int(v)) if v == int(v) else str(v)


atlas = {}
for name, (fn, wght) in FACES.items():
    tt, data = load(fn, wght)
    upm = tt["head"].unitsPerEm
    k = 1000.0 / upm
    cmap = tt.getBestCmap()
    gs = tt.getGlyphSet()
    hbfont = hb.Font(hb.Face(data))
    os2 = tt["OS/2"]

    glyphs, missing = {}, []
    for ch in CHARS:
        gname = cmap.get(ord(ch))
        if gname is None:
            missing.append(ch)
            continue
        pen = SVGPathPen(gs, ntos=num)
        gs[gname].draw(TransformPen(pen, (k, 0, 0, -k, 0, 0)))   # y-down, 1000 upm
        glyphs[ch] = [round(gs[gname].width * k, 1), pen.getCommands()]

    have = [c for c in glyphs if c != " "]
    kern = {}
    for a in have:
        for b in have:
            _, pos = shape(hbfont, a + b)
            d = round(pos[0].x_advance * k - glyphs[a][0], 1)
            if abs(d) >= 1:
                kern[a + b] = d

    atlas[name] = dict(
        asc=round(os2.sTypoAscender * k), desc=round(os2.sTypoDescender * k),
        cap=round(getattr(os2, "sCapHeight", 700) * k), xh=round(getattr(os2, "sxHeight", 500) * k),
        glyphs=glyphs, kern=kern)
    print(f"{name:9s} upm={upm} glyphs={len(glyphs)} kern={len(kern)} missing={''.join(missing)!r}")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(atlas, fh, ensure_ascii=False, separators=(",", ":"))
print(f"wrote {OUT}  {os.path.getsize(OUT) / 1024:.0f} KB")
