# -*- coding: utf-8 -*-
"""
Generates assets/{dark,light}/stats.svg — the activity panel — from the GitHub
GraphQL API. Runs nightly in CI (.github/workflows/metrics.yml).

Why hand-rolled instead of a stats service: those render their own theme,
publish every zero-valued field they know about, rate-limit into broken
images, and can't be told that most of this account's bytes are Jupyter
notebook *output* rather than code. This draws only real numbers, in the same
design system as the rest of the profile (_design.py; stdlib only).

Run:  GH_TOKEN=<pat> python assets/_stats_generator.py
"""
import collections, datetime, json, os, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _design import ATLAS, Canvas, measure, f  # noqa: E402

USER = "HarshalAndhale9657"
SINCE = datetime.date(2024, 9, 1)
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    sys.exit("GH_TOKEN not set")

# Notebook bytes are mostly embedded PNG output, and markup/config languages
# inflate a "what do you write" bar; both are excluded and the panel says so.
EXCLUDE = {"Jupyter Notebook", "HTML", "CSS", "SCSS", "TeX", "PowerShell", "EJS", "Batchfile",
           "Shell", "Dockerfile", "Makefile", "Roff", "MDX"}

Q = """
query($login:String!,$from:DateTime!,$to:DateTime!){
  user(login:$login){
    pullRequests{totalCount}
    contributionsCollection(from:$from,to:$to){
      contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}
    }
    repositories(first:100,ownerAffiliations:OWNER,isFork:false){
      totalCount
      nodes{languages(first:12,orderBy:{field:SIZE,direction:DESC}){edges{size node{name}}}}
    }
  }
}"""


def gql(frm, to):
    body = json.dumps({"query": Q, "variables": {"login": USER, "from": frm, "to": to}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Authorization": "bearer " + TOKEN, "Content-Type": "application/json",
        "User-Agent": "profile-stats"})
    r = json.loads(urllib.request.urlopen(req, timeout=45).read())
    if "errors" in r:
        sys.exit("GraphQL: " + json.dumps(r["errors"])[:400])
    return r["data"]["user"]


# ── gather ──────────────────────────────────────────────────────────────────
today = datetime.date.today()
windows, cur = [], SINCE
while cur <= today:
    nxt = min(cur.replace(year=cur.year + 1), today + datetime.timedelta(days=1))
    windows.append((cur.isoformat() + "T00:00:00Z", nxt.isoformat() + "T00:00:00Z"))
    cur = nxt

total, days, last = 0, {}, None
for frm, to in windows:
    u = gql(frm, to)
    cal = u["contributionsCollection"]["contributionCalendar"]
    total += cal["totalContributions"]
    for w in cal["weeks"]:
        for d in w["contributionDays"]:
            days[d["date"]] = d["contributionCount"]
    last = u

repos = last["repositories"]["totalCount"]
prs = last["pullRequests"]["totalCount"]
lang = collections.Counter()
for n in last["repositories"]["nodes"]:
    for e in n["languages"]["edges"]:
        if e["node"]["name"] not in EXCLUDE:
            lang[e["node"]["name"]] += e["size"]

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
peak = max(days.values()) if days else 0
active = sum(1 for v in days.values() if v > 0)

# last 53 weeks, Sunday-first columns
end = today + datetime.timedelta(days=(5 - today.weekday()) % 7)          # next Saturday
start = end - datetime.timedelta(weeks=53) + datetime.timedelta(days=1)
weeks, d = [], start
while d <= end:
    weeks.append([(d + datetime.timedelta(days=k)) for k in range(7)])
    d += datetime.timedelta(days=7)

year_vals = sorted(v for k, v in days.items() if v and k >= str(start))


def level(v):
    """Quartiles of this account's own non-zero days, so the ramp reads the same in quiet years."""
    if not v:
        return 0
    if not year_vals:
        return 1
    q = [year_vals[int(len(year_vals) * p)] for p in (.25, .5, .75)]
    return 1 + sum(v > x for x in q)


top = [(n, v) for n, v in lang.most_common(6) if v / max(sum(lang.values()), 1) >= .01][:5]
ltot = sum(v for _, v in top) or 1


# ── draw ────────────────────────────────────────────────────────────────────
def panel(theme):
    W = 1000
    cv = Canvas(W, 10, theme, "GitHub activity for %s: %d contributions since %d, %d pull requests, "
                "%d repositories, %d active days." % (USER, total, SINCE.year, prs, repos, active))
    t = cv.t
    cv.text(0, 41, "06", "mono-md", 12.5, "accent", track=1.2)
    cv.text(38, 42, "Activity", "serif", 40, "text")
    cv.text(W, 41, "Updated nightly · %s" % today.strftime("%d %b %Y"), "mono", 11.5, "text3",
            track=1.6, anchor="end", upper=True)
    cv.hline(0, W, 62, "line2")

    # headline numbers
    y = 62
    tiles = [("%s" % format(total, ","), "Contributions since %d" % SINCE.year),
             ("%d" % prs, "Pull requests"), ("%d" % repos, "Repositories"),
             ("%d" % active, "Active days")]
    cw = W / 4
    for i, (n, lab) in enumerate(tiles):
        x = i * cw + (28 if i else 0)
        if i:
            cv.vline(i * cw, y + 1, y + 112, "line")
        cv.text(x, y + 66, n, "serif", 48, "text")
        cv.text(x, y + 94, lab, "mono", 11.5, "text3", track=1.4, upper=True)
    y += 112
    cv.hline(0, W, y, "line")

    # contribution calendar
    gap = 4.0
    pitch = (W + gap) / len(weeks)
    cell = pitch - gap
    y += 44
    seen = set()
    for i, col in enumerate(weeks):
        m = col[0]
        if m.day <= 7 and m.month not in seen and i < len(weeks) - 2:
            seen.add(m.month)
            cv.text(i * pitch, y, m.strftime("%b"), "mono", 11, "text3", track=.6, upper=True)
    y += 14
    ramp = t["ramp"]
    for i, col in enumerate(weeks):
        for j, dt in enumerate(col):
            if dt > today:
                continue
            v = days.get(str(dt), 0)
            cv.add('<rect x="%s" y="%s" width="%s" height="%s" rx="3" fill="%s"><title>%s · %d</title></rect>'
                   % (f(i * pitch), f(y + j * pitch), f(cell), f(cell), ramp[level(v)], dt, v))
    y += 7 * pitch - gap + 30
    facts = "Current streak %dd   ·   Longest %dd   ·   Peak day %d" % (streak, best, peak)
    cv.text(0, y, facts, "mono", 11.5, "text3", track=1.2, upper=True)
    lx = W - 5 * 17 - measure("MORE", "mono", 11, 1) - 8
    cv.text(lx - 10, y, "LESS", "mono", 11, "text3", track=1, anchor="end")
    for k in range(5):
        cv.rect(lx + k * 17, y - 10.5, 12, 12, 2.5, ramp[k])
    cv.text(lx + 5 * 17 + 4, y, "MORE", "mono", 11, "text3", track=1)

    # languages
    y += 30
    cv.hline(0, W, y, "line")
    y += 44
    cv.text(0, y, "Languages", "mono-md", 11.5, "text3", track=1.6, upper=True)
    cv.text(W, y, "Source only", "mono", 11.5, "text3", track=1.6, upper=True, anchor="end")
    y += 20
    shades = [1, .72, .5, .32, .2]
    cv.defs.append('<clipPath id="lb"><rect x="0" y="%s" width="%d" height="8" rx="4"/></clipPath>' % (f(y), W))
    x = 0
    for k, (n, v) in enumerate(top):
        w = W * v / ltot
        cv.add('<rect x="%s" y="%s" width="%s" height="8" fill="%s" opacity="%s" clip-path="url(#lb)"/>'
               % (f(x), f(y), f(w + .5), t["accent"], f(shades[k])))
        x += w
    y += 38
    x = 0
    for k, (n, v) in enumerate(top):
        cv.rect(x, y - 10, 10, 10, 2.5, "accent", extra=' opacity="%s"' % f(shades[k]))
        x += 18
        x += cv.text(x, y, n, "sans-md", 14.5, "text") + 8
        x += cv.text(x, y, "%.1f%%" % (v / ltot * 100), "mono", 12.5, "text3") + 34
    y += 30
    cv.text(0, y, "Jupyter notebooks and markup are excluded: notebook bytes are mostly embedded "
            "output, not authored code.", "sans", 13, "text3")
    cv.h = int(y + 12)
    return cv


for th in ("dark", "light"):
    path = panel(th).save("stats.svg")
    print("wrote", path)
print("  contributions %d | PRs %d | repos %d | active %d | streak %d | best %d | peak %d"
      % (total, prs, repos, active, streak, best, peak))
print("  langs " + ", ".join("%s %.1f%%" % (n, v / ltot * 100) for n, v in top))
