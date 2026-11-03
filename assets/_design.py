# -*- coding: utf-8 -*-
"""
Shared design system for every profile SVG: palette (light + dark), type
scale, and an outline typesetter backed by fonts/glyphs.json.

Text is never emitted as <text>. Each glyph is defined once in <defs> (in
1000-unit font space) and placed with <use>, so the typography is identical on
every machine and a card weighs a few KB. Stdlib only — runs in CI as-is.
"""
import html, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "fonts", "glyphs.json"), encoding="utf-8") as _fh:
    ATLAS = json.load(_fh)

FALLBACK = {"serif": ["sans"], "serif-it": ["sans"], "sans-md": ["sans"],
            "sans-sb": ["sans"], "mono-md": ["mono", "sans"], "mono": ["sans"], "sans": ["mono"]}

# One accent, used sparingly. Neutrals lean cool so the panels sit cleanly on
# GitHub's own #0D1117 / #FFFFFF page backgrounds.
THEMES = {
    "dark": dict(
        bg="#0A0C10", surface="#0E1116", raised="#13171E",
        line="#1D222B", line2="#2A313C",
        text="#ECEEF1", text2="#A3ABB7", text3="#6D7684",
        accent="#E6B566", accent2="#F3D49B", live="#3FD68F",
        ramp=["#161B22", "#3A2E17", "#6E5221", "#B28637", "#E6B566"],
        grid_op=0.55, glow_op=0.16,
    ),
    "light": dict(
        bg="#FBFBFA", surface="#FFFFFF", raised="#F5F5F3",
        line="#E7E7E3", line2="#D6D6D0",
        text="#111318", text2="#4A515C", text3="#8A919C",
        accent="#9A6410", accent2="#7A4E0A", live="#16834F",
        ramp=["#EEEEEA", "#F2E2C2", "#E1C185", "#C4913A", "#9A6410"],
        grid_op=0.9, glow_op=0.10,
    ),
}


def f(v, nd=2):
    """Compact number for attributes."""
    v = round(float(v), nd)
    return str(int(v)) if v == int(v) else ("%.*f" % (nd, v)).rstrip("0").rstrip(".")


def esc(s):
    return html.escape(str(s), quote=True)


def _glyph(face, ch):
    g = ATLAS[face]["glyphs"]
    if ch in g:
        return face, g[ch]
    for fb in FALLBACK.get(face, []):
        if ch in ATLAS[fb]["glyphs"]:
            return fb, ATLAS[fb]["glyphs"][ch]
    raise KeyError("no glyph for %r in %s" % (ch, face))


def layout(s, face, size, track=0.0):
    """Shape a single-face run. Returns ([(face, ch, x_units)], width_px)."""
    k = 1000.0 / size
    tu = track * k
    kern = ATLAS[face]["kern"]
    x, out, prev = 0.0, [], None
    for ch in s:
        gf, (adv, d) = _glyph(face, ch)
        if prev is not None:
            x += kern.get(prev + ch, 0)
        if d:
            out.append((gf, ch, x))
        x += adv + tu
        prev = ch
    if s:
        x -= tu
    return out, x * size / 1000.0


def measure(s, face, size, track=0.0):
    return layout(s, face, size, track)[1]


def wrap(s, face, size, maxw, track=0.0):
    lines, cur = [], ""
    for word in s.split(" "):
        trial = word if not cur else cur + " " + word
        if measure(trial, face, size, track) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


class Canvas:
    def __init__(self, w, h, theme, label=""):
        self.w, self.h, self.theme, self.label = w, h, theme, label
        self.t = THEMES[theme]
        self.used, self.defs, self.els, self.css = set(), [], [], []

    def c(self, key):
        return self.t.get(key, key)

    def add(self, s):
        self.els.append(s)

    # ── type ────────────────────────────────────────────────────────────────
    def text(self, x, y, s, face="sans", size=16, fill="text", track=0.0,
             anchor="start", upper=False, opacity=None, extra=""):
        if upper:
            s = s.upper()
        gl, w = layout(s, face, size, track)
        if anchor == "end":
            x -= w
        elif anchor == "middle":
            x -= w / 2
        self.used.update((gf, ch) for gf, ch, _ in gl)
        uses = "".join('<use href="#%s" x="%d"/>' % (gid(gf, ch), round(gx)) for gf, ch, gx in gl)
        op = ' opacity="%s"' % f(opacity) if opacity is not None else ""
        self.add('<g transform="translate(%s %s) scale(%s)" fill="%s"%s%s>%s</g>'
                 % (f(x), f(y), f(size / 1000.0, 5), self.c(fill), op, extra, uses))
        return w

    def runs(self, x, y, parts, anchor="start"):
        """parts: [(text, face, size, fill[, track])] laid out inline on one baseline."""
        widths = [measure(p[0], p[1], p[2], p[4] if len(p) > 4 else 0) for p in parts]
        total = sum(widths)
        if anchor == "end":
            x -= total
        elif anchor == "middle":
            x -= total / 2
        for p, w in zip(parts, widths):
            self.text(x, y, p[0], p[1], p[2], p[3], p[4] if len(p) > 4 else 0)
            x += w
        return total

    def para(self, x, y, s, face="sans", size=16, maxw=400, lh=None, fill="text2", max_lines=None):
        lh = lh or size * 1.5
        lines = wrap(s, face, size, maxw)
        if max_lines and len(lines) > max_lines:
            raise ValueError("paragraph overflows %d lines: %r" % (max_lines, s[:60]))
        for i, ln in enumerate(lines):
            self.text(x, y + i * lh, ln, face, size, fill)
        return y + (len(lines) - 1) * lh, len(lines)

    # ── shapes ──────────────────────────────────────────────────────────────
    def rect(self, x, y, w, h, rx=0, fill="none", stroke=None, sw=1, extra=""):
        s = ' stroke="%s" stroke-width="%s"' % (self.c(stroke), f(sw)) if stroke else ""
        self.add('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s"%s%s/>'
                 % (f(x), f(y), f(w), f(h), f(rx), self.c(fill), s, extra))

    def hline(self, x1, x2, y, stroke="line", sw=1, extra=""):
        self.add('<path d="M%s %sH%s" stroke="%s" stroke-width="%s"%s/>'
                 % (f(x1), f(y + 0.5), f(x2), self.c(stroke), f(sw), extra))

    def vline(self, x, y1, y2, stroke="line", sw=1, extra=""):
        self.add('<path d="M%s %sV%s" stroke="%s" stroke-width="%s"%s/>'
                 % (f(x + 0.5), f(y1), f(y2), self.c(stroke), f(sw), extra))

    def circle(self, cx, cy, r, fill="accent", stroke=None, sw=1, extra=""):
        s = ' stroke="%s" stroke-width="%s"' % (self.c(stroke), f(sw)) if stroke else ""
        self.add('<circle cx="%s" cy="%s" r="%s" fill="%s"%s%s/>'
                 % (f(cx), f(cy), f(r), self.c(fill), s, extra))

    def pill(self, x, y, label, face="mono", size=12, fill="text3", stroke="line2",
             bg="none", padx=10, h=26, track=0.4, upper=False, anchor="start"):
        s = label.upper() if upper else label
        w = measure(s, face, size, track) + padx * 2
        if anchor == "end":
            x -= w
        self.rect(x, y, w, h, h / 2, bg, stroke)
        cap = ATLAS[face]["cap"] * size / 1000.0
        self.text(x + padx, y + h / 2 + cap / 2, s, face, size, fill, track)
        return w

    def frame(self, rx=14, fill="surface", stroke="line"):
        self.rect(0.5, 0.5, self.w - 1, self.h - 1, rx, fill, stroke)

    # ── output ──────────────────────────────────────────────────────────────
    def render(self):
        glyph_defs = "".join('<path id="%s" d="%s"/>' % (gid(face, ch), _glyph(face, ch)[1][1])
                             for face, ch in sorted(self.used))
        css = ("<style>%s</style>" % "".join(self.css)) if self.css else ""
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
                'role="img" aria-label="%s" fill="none">%s<defs>%s%s</defs>%s</svg>'
                % (self.w, self.h, self.w, self.h, esc(self.label), css, glyph_defs,
                   "".join(self.defs), "\n".join(self.els)))

    def save(self, name):
        path = os.path.join(HERE, self.theme, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(self.render())
        return path


def gid(face, ch):
    return "%s%x" % (face.replace("-", ""), ord(ch))
