# -*- coding: utf-8 -*-
import html

W, H = 1000, 392
TOTAL = 16000.0
BAR = 40
X = 34
FS = 16
LH = 28
CW = FS * 0.601  # monospace advance width

C = dict(bg="#0B0E14", chrome="#12161F", edge="#1F2733",
         prompt="#00E58A", cmd="#E6EDF3", dim="#7D8590",
         out="#C9D1D9", cyan="#56D4FF", amber="#FFB86C", mag="#C792EA")

# (kind, y, segments[(text,color,weight)], start_ms, dur_ms)
L = []
def line(y, segs, s, d): L.append((y, segs, s, d))

y0 = BAR + 40
line(y0,        [("$ ", C["prompt"], 700), ("whoami", C["cmd"], 500)], 200, 620)
line(y0+LH,     [("Harshal Andhale", C["cyan"], 700), ("  ·  ", C["dim"], 400), ("AI Engineer", C["out"], 500)], 950, 640)
line(y0+LH*2.4, [("$ ", C["prompt"], 700), ("cat ./focus.md", C["cmd"], 500)], 1750, 780)
line(y0+LH*3.4, [("LLM Post-Training", C["amber"], 600), (" (SFT · DPO)  ·  ", C["dim"], 400), ("Agentic Systems", C["amber"], 600), ("  ·  ", C["dim"], 400), ("RAG at Scale", C["amber"], 600)], 2700, 1150)
line(y0+LH*4.8, [("$ ", C["prompt"], 700), ("ls ./shipped/", C["cmd"], 500)], 4000, 700)
line(y0+LH*5.8, [("PRISM/   AEGIS/   Axiom/   Groundwork/   CampusLens/", C["mag"], 500)], 4850, 950)
line(y0+LH*7.2, [("$ ", C["prompt"], 700), ("./status --now", C["cmd"], 500)], 5950, 760)
line(y0+LH*8.2, [("▸ ", C["prompt"], 700), ("SWE Intern @ Funlingo", C["out"], 500), ("     ▸ ", C["prompt"], 700), ("AI Engineer Intern @ SGRAMX", C["out"], 500)], 6850, 1250)

CUR_Y = y0 + LH*9.6
CUR_SHOW = 8300

def pct(ms): return round(ms / TOTAL * 100, 3)

css, body = [], []
css.append("text{font-family:ui-monospace,'SF Mono',SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono',monospace;font-size:%dpx;white-space:pre}" % FS)

for i, (y, segs, s, d) in enumerate(L):
    n = sum(len(t) for t, _, _ in segs)
    w = int(n * CW) + 6
    css.append("@keyframes t%d{0%%,%s%%{width:0}%s%%,100%%{width:%dpx}}" % (i, pct(s), pct(s+d), w))
    css.append("#c%d rect{animation:t%d %.0fms steps(%d,end) infinite}" % (i, i, TOTAL, max(n,1)))
    body.append('<clipPath id="c%d"><rect x="%d" y="%d" width="0" height="%d"/></clipPath>' % (i, X, y-FS, LH))
    ts, cx = [], X
    for t, col, fw in segs:
        ts.append('<tspan x="%.1f" fill="%s" font-weight="%d">%s</tspan>' % (cx, col, fw, html.escape(t)))
        cx += len(t) * CW
    body.append('<text y="%d" clip-path="url(#c%d)">%s</text>' % (y, i, "".join(ts)))

css.append("@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}")
css.append("@keyframes cur{0%%,%s%%{opacity:0}%s%%,100%%{opacity:1}}" % (pct(CUR_SHOW), pct(CUR_SHOW+1)))
css.append("#cur{animation:blink 1.06s steps(1,end) infinite,cur %.0fms linear infinite}" % TOTAL)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Harshal Andhale — AI Engineer. LLM post-training, agentic systems, RAG at scale.">
<style>{"".join(css)}</style>
<defs>
<linearGradient id="glow" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#00E58A"/><stop offset=".5" stop-color="#56D4FF"/><stop offset="1" stop-color="#C792EA"/>
</linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#161C28"/><stop offset="1" stop-color="#0B0E14"/>
</linearGradient>
</defs>
<rect width="{W}" height="{H}" rx="12" fill="{C['bg']}" stroke="{C['edge']}"/>
<path d="M12 0h{W-24}a12 12 0 0 1 12 12v{BAR-12}H0V12A12 12 0 0 1 12 0z" fill="url(#fade)"/>
<rect y="{BAR-1}" width="{W}" height="1" fill="{C['edge']}"/>
<circle cx="26" cy="{BAR//2}" r="6" fill="#FF5F57"/><circle cx="48" cy="{BAR//2}" r="6" fill="#FEBC2E"/><circle cx="70" cy="{BAR//2}" r="6" fill="#28C840"/>
<text x="{W//2}" y="{BAR//2+5}" text-anchor="middle" fill="{C['dim']}" font-size="13">harshal@github ─ ~/portfolio ─ zsh</text>
{chr(10).join(body)}
<text y="{CUR_Y}"><tspan x="{X}" fill="{C['prompt']}" font-weight="700">$ </tspan></text>
<rect id="cur" x="{X + 2*CW:.0f}" y="{CUR_Y-FS+2}" width="{CW:.0f}" height="{FS}" fill="{C['prompt']}"/>
<rect x="0" y="{H-3}" width="{W}" height="3" fill="url(#glow)" opacity=".9"/>
</svg>'''
open("terminal.svg","w",encoding="utf-8").write(svg)
print("wrote", len(svg), "bytes")
