# -*- coding: utf-8 -*-
"""
Generates assets/stats.svg — a bespoke, terminal-themed GitHub stats panel.

Why hand-rolled instead of a stats service: the popular generators render a
light-themed card, publish every zero-valued field they know about, and can't
be told that 83% of this account's bytes are Jupyter notebook *output* rather
than code. This queries the GraphQL API directly and draws only what's true
and worth showing.

Run:  GH_TOKEN=<pat> python assets/_stats_generator.py
"""
import json, os, sys, urllib.request, datetime, collections

USER = "HarshalAndhale9657"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stats.svg")
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    sys.exit("GH_TOKEN not set")

# Notebooks are ~83% of raw bytes here but that is embedded PNG output, not
# authored code; markup/config languages likewise inflate a "what do you write"
# bar. Excluded, and the SVG says so.
EXCLUDE = {"Jupyter Notebook", "HTML", "CSS", "SCSS", "TeX", "PowerShell",
           "EJS", "Batchfile", "Shell", "Dockerfile", "Makefile", "Roff", "MDX"}

Q = """
query($login:String!,$from:DateTime!,$to:DateTime!){
  user(login:$login){
    followers{totalCount}
    contributionsCollection(from:$from,to:$to){
      totalCommitContributions restrictedContributionsCount
      totalPullRequestContributions
      totalRepositoriesWithContributedCommits
      contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}
    }
    repositories(first:100,ownerAffiliations:OWNER,isFork:false){
      totalCount
      nodes{stargazerCount forkCount
        languages(first:12,orderBy:{field:SIZE,direction:DESC}){edges{size node{name color}}}}
    }
  }
}"""


def gql(frm, to):
    body = json.dumps({"query": Q, "variables": {"login": USER, "from": frm, "to": to}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body,
                                 headers={"Authorization": "bearer " + TOKEN,
                                          "Content-Type": "application/json",
                                          "User-Agent": USER})
    r = json.loads(urllib.request.urlopen(req, timeout=45).read())
    if "errors" in r:
        sys.exit("GraphQL: " + json.dumps(r["errors"])[:400])
    return r["data"]["user"]


# ── gather ──────────────────────────────────────────────────────────────────
today = datetime.date.today()
windows, cur = [], datetime.date(2024, 9, 1)
while cur < today:
    nxt = min(cur.replace(year=cur.year + 1), today + datetime.timedelta(days=1))
    windows.append((cur.isoformat() + "T00:00:00Z", nxt.isoformat() + "T00:00:00Z"))
    cur = nxt

commits = prs = 0
days, last = {}, None
for frm, to in windows:
    u = gql(frm, to)
    c = u["contributionsCollection"]
    commits += c["totalCommitContributions"] + c["restrictedContributionsCount"]
    prs += c["totalPullRequestContributions"]
    for w in c["contributionCalendar"]["weeks"]:
        for d in w["contributionDays"]:
            days[d["date"]] = d["contributionCount"]
    last = u

repos = last["repositories"]
stars = sum(n["stargazerCount"] for n in repos["nodes"])
forks = sum(n["forkCount"] for n in repos["nodes"])
followers = last["followers"]["totalCount"]
contributed = last["contributionsCollection"]["totalRepositoriesWithContributedCommits"]

lang, colors = collections.Counter(), {}
for n in repos["nodes"]:
    for e in n["languages"]["edges"]:
        nm = e["node"]["name"]
        if nm in EXCLUDE:
            continue
        lang[nm] += e["size"]
        colors[nm] = e["node"]["color"] or "#8B949E"

# streaks
best = run = 0
for d in sorted(days):
    run = run + 1 if days[d] > 0 else 0
    best = max(best, run)
streak, probe = 0, today
if days.get(str(today), 0) == 0:
    probe = today - datetime.timedelta(days=1)
while days.get(str(probe), 0) > 0:
    streak += 1
    probe -= datetime.timedelta(days=1)
busiest = max(days.values()) if days else 0
active = sum(1 for v in days.values() if v > 0)

# ── layout ──────────────────────────────────────────────────────────────────
W, BAR, X, FS, CW = 1000, 40, 34, 16, 16 * 0.601
C = dict(bg="#0B0E14", edge="#1F2733", prompt="#00E58A", cmd="#E6EDF3",
         dim="#7D8590", cyan="#56D4FF", amber="#FFB86C", mag="#C792EA")
RAMP = ["#161B22", "#0C3A2A", "#00754A", "#00A768", "#00E58A"]

CELL, GAP = 13, 3
PITCH = CELL + GAP

# last 53 weeks, weeks start Sunday
end = today - datetime.timedelta(days=(today.weekday() + 1) % 7) + datetime.timedelta(days=6)
start = end - datetime.timedelta(weeks=52, days=6)
weeks = []
d = start
while d <= end:
    col = []
    for _ in range(7):
        col.append((d, days.get(str(d))))
        d += datetime.timedelta(days=1)
    weeks.append(col)
NW = len(weeks)
HM_W = NW * PITCH - GAP


def lvl(v):
    if v is None or v == 0:
        return 0
    if v >= 10: return 4
    if v >= 5:  return 3
    if v >= 3:  return 2
    return 1


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, segs, size=FS, anchor="start"):
    t = "".join('<tspan fill="%s" font-weight="%d">%s</tspan>' % (c, w, esc(s)) for s, c, w in segs)
    return '<text x="%.1f" y="%.1f" font-size="%d" text-anchor="%s">%s</text>' % (x, y, size, anchor, t)


b = []
y = BAR + 38
b.append(txt(X, y, [("$ ", C["prompt"], 700), ("gh stats --all-time", C["cmd"], 500)]))

# ── stat tiles: four numbers that are all non-zero and all mean something ──
y += 30
tiles = [(f"{commits:,}", "commits", C["cyan"]), (f"{stars}", "stars earned", C["amber"]),
         (f"{repos['totalCount']}", "repositories", C["mag"]), (f"{active}", "active days", C["prompt"])]
tw = (W - 2 * X) / 4
for i, (n, lab, col) in enumerate(tiles):
    cx = X + i * tw
    b.append('<rect x="%.1f" y="%.1f" width="%.1f" height="62" rx="6" fill="#0E141D" stroke="%s"/>'
             % (cx, y, tw - 12, C["edge"]))
    b.append(txt(cx + 16, y + 32, [(n, col, 700)], size=27))
    b.append(txt(cx + 16, y + 50, [(lab, C["dim"], 400)], size=12))

# ── contribution heatmap ──
y += 62 + 34
b.append(txt(X, y, [("$ ", C["prompt"], 700), ("gh contributions --graph", C["cmd"], 500)]))
y += 26
seen = set()
for i, col in enumerate(weeks):
    m = col[0][0]
    if m.month not in seen and m.day <= 7:
        seen.add(m.month)
        b.append(txt(X + i * PITCH, y, [(m.strftime("%b"), C["dim"], 400)], size=11))
y += 8
for i, col in enumerate(weeks):
    for j, (dt, v) in enumerate(col):
        if dt > today:
            continue
        b.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="2.5" fill="%s"><title>%s: %s</title></rect>'
                 % (X + i * PITCH, y + j * PITCH, CELL, CELL, RAMP[lvl(v)], dt, (v or 0)))
y += 7 * PITCH + 20

# legend + streak facts on one line
b.append(txt(X, y, [(f"{streak}d current streak", C["cmd"], 600), ("   ·   ", C["dim"], 400),
                    (f"{best}d best streak", C["cmd"], 600), ("   ·   ", C["dim"], 400),
                    (f"{busiest} commits in a day", C["cmd"], 600)], size=13))
lx = W - X - 5 * (CELL + 2) - 62
b.append(txt(lx - 8, y, [("less", C["dim"], 400)], size=11, anchor="end"))
for k in range(5):
    b.append('<rect x="%.1f" y="%.1f" width="11" height="11" rx="2.5" fill="%s"/>' % (lx + k * 14, y - 9, RAMP[k]))
b.append(txt(lx + 5 * 14 + 2, y, [("more", C["dim"], 400)], size=11))

# ── languages ──
y += 38
b.append(txt(X, y, [("$ ", C["prompt"], 700), ("gh languages --source-only", C["cmd"], 500)]))
y += 22
top = [(n, v) for n, v in lang.most_common(6) if v / max(sum(lang.values()), 1) >= 0.01][:5]
tot = sum(v for _, v in top) or 1
BW = W - 2 * X
b.append('<clipPath id="lb"><rect x="%d" y="%.1f" width="%d" height="14" rx="7"/></clipPath>' % (X, y, BW))
cx = X
for nm, v in top:
    w = BW * v / tot
    b.append('<rect x="%.2f" y="%.1f" width="%.2f" height="14" fill="%s" clip-path="url(#lb)"><title>%s %.1f%%</title></rect>'
             % (cx, y, w + .6, colors[nm], nm, v / tot * 100))
    cx += w
y += 34
cx = X
for nm, v in top:
    b.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (cx + 5, y - 5, colors[nm]))
    b.append(txt(cx + 17, y, [(nm, C["cmd"], 500), ("  %.1f%%" % (v / tot * 100), C["dim"], 400)], size=13))
    cx += 17 + (len(nm) + 7) * 13 * 0.601 + 26
y += 22
b.append(txt(X, y, [("source code only — Jupyter notebooks and markup excluded, since notebook bytes are mostly embedded output", C["dim"], 400)], size=11))

H = int(y + 30)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="GitHub statistics for {USER}: {commits} commits, {stars} stars, {repos['totalCount']} repositories.">
<style>text{{font-family:ui-monospace,'SF Mono',SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono',monospace;white-space:pre}}</style>
<defs>
<linearGradient id="glow" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#00E58A"/><stop offset=".5" stop-color="#56D4FF"/><stop offset="1" stop-color="#C792EA"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#161C28"/><stop offset="1" stop-color="#0B0E14"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" rx="12" fill="{C['bg']}" stroke="{C['edge']}"/>
<path d="M12 0h{W-24}a12 12 0 0 1 12 12v{BAR-12}H0V12A12 12 0 0 1 12 0z" fill="url(#fade)"/>
<rect y="{BAR-1}" width="{W}" height="1" fill="{C['edge']}"/>
<circle cx="26" cy="{BAR//2}" r="6" fill="#FF5F57"/><circle cx="48" cy="{BAR//2}" r="6" fill="#FEBC2E"/><circle cx="70" cy="{BAR//2}" r="6" fill="#28C840"/>
<text x="{W//2}" y="{BAR//2+5}" text-anchor="middle" fill="{C['dim']}" font-size="13" font-family="ui-monospace,Menlo,Consolas,monospace">harshal@github ─ ~/metrics ─ zsh</text>
{chr(10).join(b)}
<rect x="0" y="{H-3}" width="{W}" height="3" fill="url(#glow)" opacity=".9"/>
</svg>'''

open(OUT, "w", encoding="utf-8").write(svg)
print(f"wrote {OUT}  ({W}x{H})")
print(f"  commits {commits} | stars {stars} | repos {repos['totalCount']} | contributed {contributed}")
print(f"  streak {streak}d | best {best}d | active {active} | busiest {busiest}")
print("  langs " + ", ".join(f"{n} {v/tot*100:.1f}%" for n, v in top))
