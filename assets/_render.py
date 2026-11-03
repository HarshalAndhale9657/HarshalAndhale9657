# -*- coding: utf-8 -*-
"""
Renders every static SVG on the profile, in assets/dark/ and assets/light/.
GitHub picks the variant matching the viewer's theme via <picture>.

Edit the content blocks below, then:   python assets/_render.py
(The nightly activity panel is _stats_generator.py; it shares _design.py.)
"""
from _design import ATLAS, Canvas, measure, wrap, f

W = 1000          # full-width panels; README scales them to the column
CARD_W = 500      # project cards sit two to a row


# ════════════════════════════════════════════════════════════════════════════
#  CONTENT
# ════════════════════════════════════════════════════════════════════════════

METRICS = [
    ("20K+", "Active users", "on the extension I ship"),
    ("4", "Industry internships", "AI · ML · Software"),
    ("Winner", "DEVCLASH 2026", "National-level hackathon"),
    ("Top 2%", "NPTEL · LLMs", "IIT Delhi · AIR under 100"),
    ("Top 600", "Amazon ML Challenge", "of 1 lakh+ teams"),
]

PRINCIPLES = [
    ("Prove it, don't claim it.",
     "A.E.G.I.S. won't open a pull request until it has executed the exploit it reports. "
     "Unproven findings are discarded, never surfaced."),
    ("Optimise the real cost.",
     "Axiom is scored in rupees, not AUC. Blocking every COD order turns out worse than "
     "doing nothing, so the threshold is set by cost."),
    ("Know when to abstain.",
     "Groundwork answers only from what it actually read. A calibrated “not found” "
     "beats a fluent invention."),
    ("Publish the negative result.",
     "P.R.I.S.M. v1 benchmarked as near-noise. I shipped the diagnostic, rebuilt it around "
     "source attribution and marked the old claims superseded."),
]

EXPERIENCE = [
    dict(org="Funlingo", role="Software Engineer Intern", when="Aug 2026 — Now",
         where="Remote", current=True,
         desc="Ship features end to end in a React Chrome extension used by 20K+ language "
              "learners: dual-language subtitle sync, instant lookups, phrase detection, TTS and "
              "Japanese word segmentation across 8 platforms including Netflix, Crunchyroll, "
              "Hotstar, HBO Max and Apple TV+. Built the serverless plans and billing layer on "
              "AWS Lambda with Stripe and Razorpay.",
         tags=["React", "JavaScript", "Chrome extensions", "AWS Lambda", "Stripe", "Razorpay"]),
    dict(org="SGRAMX", role="AI Engineer Intern", when="Jul 2026 — Now",
         where="Remote · Pune", current=True,
         desc="AI workflows for PharmX: evaluating, scoring and prioritising drug molecules, "
              "turning multi-stakeholder criteria into structured, explainable rankings.",
         tags=["Applied AI", "Scoring pipelines", "Drug discovery"]),
    dict(org="Ethara AI", role="LLM Post-Training Intern", when="Feb — May 2026",
         where="Remote · Gurugram",
         desc="Post-trained domain-specific LLMs with SFT and DPO, raising reliability and "
              "output quality through data curation, prompt optimisation and systematic evaluation.",
         tags=["SFT", "DPO", "Data curation", "Evaluation"]),
    dict(org="Labmentix", role="ML Engineer Intern", when="Dec 2025 — Feb 2026",
         where="Remote · Bengaluru",
         desc="ML pipelines for tourism behaviour analysis (regression, classification, feature "
              "engineering), plus collaborative and content-based recommenders shipped in Streamlit.",
         tags=["scikit-learn", "Recommenders", "Streamlit"]),
]
EDUCATION = dict(org="D. Y. Patil Institute of Technology", role="B.E. Computer Science",
                 when="2024 — 2028", where="Pune", note="CGPA 8.93 / 10")

WORK = [
    dict(key="aegis", name="A.E.G.I.S.", cat="Autonomous security", live=True,
         desc="Red-team agent that finds a vulnerability, executes the exploit to prove it's "
              "real, patches it and opens the pull request — no human in the loop.",
         proof="Fail-closed gates · Petri-net control · W3C traces",
         stack=["Python", "FastAPI", "LLM agents", "Redis", "OpenTelemetry"]),
    dict(key="prism", name="P.R.I.S.M.", cat="Forensic NLP", live=True,
         desc="Catches stitched plagiarism — verbatim, paraphrased and translated — and "
              "attributes every span to the source it was taken from.",
         proof="Precision 1.00 · Recall 0.86 · FPR 0.00",
         stack=["FastAPI", "spaCy", "HDBSCAN", "OpenAlex", "GPT-4o"]),
    dict(key="axiom", name="Axiom", cat="Risk ML · Razorpay Buildathon",
         desc="COD/RTO fraud risk manager optimised for rupees, not AUC: calibrated LightGBM, "
              "SHAP reasons and a bounded Gemini agent behind an audit trail.",
         proof="₹49,254 per 1k orders · −24% vs approve-all",
         stack=["LightGBM", "SHAP", "Gemini", "FastAPI", "Next.js"]),
    dict(key="groundwork", name="Groundwork", cat="Agentic AI · Research",
         desc="Local-first browser agent built on calibrated grounding: act only on what's on "
              "the page, answer only from what was read, abstain otherwise.",
         proof="Risk-gated actions · on-device · own refusal benchmark",
         stack=["Chrome MV3", "Transformers.js", "PGlite", "QLoRA", "Ollama"]),
    dict(key="incidentforge", name="IncidentForge", cat="RL environments · Meta × PyTorch",
         desc="OpenEnv reinforcement-learning environment that trains LLMs to work as SREs, "
              "diagnosing and remediating incidents across simulated microservices.",
         proof="Custom action space · shaped rewards · curriculum",
         stack=["Python", "OpenEnv", "PyTorch", "Reinforcement learning"]),
    dict(key="reconciliation", name="Reconciliation Engine", cat="Distributed systems",
         desc="Event-driven ledger reconciliation for out-of-order, delayed records from "
              "mismatched sources, designed for replay and audit.",
         proof="Ingest once · stream events · reconcile deterministically",
         stack=["TypeScript", "Kafka", "PostgreSQL", "Docker"]),
]

RECOGNITION = [
    ("Winner", "DEVCLASH 2026", "National-level hackathon · Open Track"),
    ("Top 2%", "NPTEL · Introduction to LLMs", "IIT Delhi · All-India Rank under 100"),
    ("#600", "Amazon ML Challenge", "Among 1 lakh+ competing teams"),
    ("Selected", "AI Research Intern", "IIT Roorkee"),
    ("$750", "Prototype Development Grant", "La Trobe University, Australia"),
    ("Top 5%", "NPTEL · Introduction to ML", "IIT Madras"),
    ("Finalist", "IBM · Meta × PyTorch · AMD", "National hackathons"),
    ("Lead", "Technical Lead", "Computer Society of India · DYPIT"),
]
ALSO = ("Also: Machine Learning Specialization and PyTorch for Deep Learning (DeepLearning.AI) · "
        "RAG Bootcamp with LangChain, LangGraph and LangSmith · 300+ DSA problems solved")

TOOLKIT = [
    ("Modeling", ["PyTorch", "Transformers", "PEFT", "SFT", "DPO", "QLoRA", "scikit-learn",
                  "LightGBM", "SHAP"]),
    ("LLM systems", ["LangChain", "LangGraph", "RAG", "Agents", "Evals", "OpenAI", "Claude",
                     "Gemini", "Ollama"]),
    ("Data & retrieval", ["PostgreSQL", "pgvector", "MongoDB", "Pinecone", "FAISS", "ChromaDB",
                          "Neo4j", "Redis", "Kafka"]),
    ("Backend", ["Python", "FastAPI", "Node.js", "Express", "Flask", "Java", "SQL", "REST"]),
    ("Frontend", ["React", "Next.js", "TypeScript", "Three.js", "Tailwind", "Chrome extensions"]),
    ("Infra & MLOps", ["Docker", "Kubernetes", "AWS Lambda", "GitHub Actions", "MLflow",
                       "OpenTelemetry"]),
]

# Causal attention map in the hero: rows are query tokens, columns keys.
TOKENS = ["<s>", "build", "AI", "that", "has", "to", "be", "right"]
ATTN = {(1, 0): .5, (1, 1): .62, (2, 1): .55, (3, 2): .78, (3, 1): .28, (4, 2): .7,
        (4, 3): .34, (5, 4): .66, (6, 5): .6, (6, 4): .36, (7, 2): .92, (7, 1): .56,
        (7, 6): .4, (7, 7): .46}

LINKEDIN = ("M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 "
            "2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 "
            "4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-"
            "2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h"
            "3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h"
            "20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z")


# ════════════════════════════════════════════════════════════════════════════
#  COMPONENTS
# ════════════════════════════════════════════════════════════════════════════

def cap(face, size):
    return ATLAS[face]["cap"] * size / 1000.0


def header(cv, idx, title, caption=None):
    cv.text(0, 41, idx, "mono-md", 12.5, "accent", track=1.2)
    cv.text(38, 42, title, "serif", 40, "text")
    if caption:
        cv.text(cv.w, 41, caption, "mono", 11.5, "text3", track=1.6, anchor="end", upper=True)
    cv.hline(0, cv.w, 62, "line2")
    return 62


def hero(theme):
    H = 508
    cv = Canvas(W, H, theme, "Harshal Andhale — AI Engineer. LLM post-training, agentic systems "
                "and retrieval. Software Engineer at Funlingo, AI Engineer at SGRAMX. 20K+ users, "
                "4 internships, DEVCLASH 2026 winner, NPTEL LLMs top 2%, Amazon ML Challenge top 600.")
    t = cv.t
    cv.defs += [
        '<pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">'
        '<circle cx="1.5" cy="1.5" r="1.1" fill="%s"/></pattern>' % t["line2"],
        '<radialGradient id="dm" cx=".8" cy=".36" r=".5"><stop offset="0" stop-color="#fff"/>'
        '<stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>',
        '<mask id="m"><rect width="%d" height="%d" fill="url(#dm)"/></mask>' % (W, H),
        '<radialGradient id="glow" cx=".82" cy=".28" r=".5"><stop offset="0" stop-color="%s" '
        'stop-opacity="%s"/><stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient>'
        % (t["accent"], t["glow_op"], t["accent"]),
        '<linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="%s" stop-opacity="0"/>'
        '<stop offset=".5" stop-color="%s"/><stop offset="1" stop-color="%s" stop-opacity="0"/>'
        '</linearGradient>' % (t["accent"], t["accent"], t["accent"]),
    ]
    cv.frame(16, "bg", "line")
    box = '<rect x=".5" y=".5" width="%d" height="%d" rx="16" fill="%s"%s/>'
    cv.add(box % (W - 1, H - 1, "url(#glow)", ""))
    cv.add(box % (W - 1, H - 1, "url(#dots)", ' mask="url(#m)" opacity="%s"' % t["grid_op"]))
    cv.add('<rect x="120" y="0" width="%d" height="1" fill="url(#edge)" opacity=".7"/>' % (W - 240))

    X = 56
    # eyebrow
    cv.runs(X, 80, [("AI ENGINEER", "mono-md", 12, "accent", 2.2),
                    ("   /   ", "mono", 12, "text3"),
                    ("LLM POST-TRAINING · AGENTIC SYSTEMS · RAG", "mono", 12, "text3", 1.8)])
    # name
    cv.runs(X - 3, 174, [("Harshal ", "serif", 94, "text"), ("Andhale", "serif-it", 94, "text")])
    # thesis
    cv.para(X, 224, "I build AI systems that have to be right: post-trained models, agents that "
            "prove their work, and retrieval that knows when to abstain.",
            "sans", 19.5, maxw=548, lh=30, fill="text2", max_lines=3)

    # now
    ny = 330
    cv.add('<circle class="halo" cx="%s" cy="%s" r="4" fill="%s"/>' % (X + 4, ny - 4.5, t["live"]))
    cv.circle(X + 4, ny - 4.5, 4, "live")
    x = X + 18
    x += cv.text(x, ny, "NOW", "mono-md", 11.5, "live", track=1.6) + 14
    x += cv.text(x, ny, "Software Engineer", "sans-md", 15, "text") + 6
    x += cv.text(x, ny, "@ Funlingo", "sans", 15, "text2") + 16
    x += cv.text(x, ny, "/", "sans", 15, "line2") + 16
    x += cv.text(x, ny, "AI Engineer", "sans-md", 15, "text") + 6
    cv.text(x, ny, "@ SGRAMX", "sans", 15, "text2")

    # attention map
    n, cell, pitch = len(TOKENS), 23, 29
    gx, gy = W - 56 - (n * pitch - (pitch - cell)), 70
    for i, tok in enumerate(TOKENS):
        cy = gy + i * pitch + cell / 2
        cv.text(gx - 12, cy + cap("mono", 11.5) / 2, tok, "mono", 11.5, "text3", anchor="end")
        row = []
        for j in range(n):
            x0, y0 = gx + j * pitch, gy + i * pitch
            if j > i:
                cv.rect(x0 + .5, y0 + .5, cell - 1, cell - 1, 4, "none", "line", 1)
                continue
            w = ATTN.get((i, j), 1.0 if (i, j) == (0, 0) else (.42 if j == 0 else .07))
            row.append('<rect x="%s" y="%s" width="%d" height="%d" rx="4" fill="%s" opacity="%s"/>'
                       % (f(x0), f(y0), cell, cell, t["accent"], f(.1 + .9 * w)))
        cv.add('<g class="r" style="animation-delay:%ss">%s</g>' % (f(i * .55), "".join(row)))
    cv.text(W - 56, gy + n * pitch + 22, "CAUSAL ATTENTION · L12 · H7", "mono", 10.5, "text3",
            track=1.6, anchor="end")

    # metrics band
    by = 372
    cv.hline(1, W - 1, by, "line")
    colw = (W - 2 * X) / len(METRICS)
    for i, (num, l1, l2) in enumerate(METRICS):
        x = X + i * colw
        if i:
            cv.vline(x - 22, by + 1, H - 1, "line")
        cv.text(x, by + 56, num, "serif", 38, "text")
        cv.text(x, by + 82, l1, "sans-md", 13.5, "text")
        cv.text(x, by + 102, l2, "sans", 12.5, "text3")

    cv.css += [
        "@keyframes gen{0%{opacity:0}6%{opacity:1}80%{opacity:1}94%,100%{opacity:.18}}",
        ".r{animation:gen 9s cubic-bezier(.2,.7,.2,1) infinite both}",
        "@keyframes halo{0%{opacity:.55;transform:scale(1)}100%{opacity:0;transform:scale(3.2)}}",
        ".halo{transform-box:fill-box;transform-origin:center;animation:halo 2.4s ease-out infinite}",
        "@media (prefers-reduced-motion:reduce){.r{animation:none!important;opacity:1}"
        ".halo{animation:none!important;opacity:0}}",
    ]
    return cv


def button(theme, kind):
    label = {"linkedin": "LinkedIn", "email": "Email", "repos": "Repositories"}[kind]
    tw = measure(label, "sans-md", 15)
    aw = measure("↗", "sans", 15)
    w, h = int(18 + 16 + 10 + tw + 10 + aw + 18), 44
    cv = Canvas(w, h, theme, label)
    t = cv.t
    cv.rect(.5, .5, w - 1, h - 1, h / 2 - .5, "surface", "line2")
    ix, iy = 18, (h - 16) / 2
    if kind == "linkedin":
        cv.add('<path transform="translate(%s %s) scale(%s)" fill="%s" d="%s"/>'
               % (ix, f(iy), f(16 / 24, 4), t["text"], LINKEDIN))
    elif kind == "email":
        cv.add('<g transform="translate(%s %s)" fill="none" stroke="%s" stroke-width="1.6" '
               'stroke-linejoin="round"><rect x=".8" y="2.3" width="14.4" height="11.4" rx="2"/>'
               '<path d="M1.6 3.6 8 8.6l6.4-5"/></g>' % (ix, f(iy), t["text"]))
    else:
        cv.add('<g transform="translate(%s %s)" fill="%s">%s</g>' % (ix, f(iy), t["text"], "".join(
            '<rect x="%s" y="%s" width="6.6" height="6.6" rx="1.6"/>' % (a, b)
            for a in (.8, 8.6) for b in (.8, 8.6))))
    base = h / 2 + cap("sans-md", 15) / 2
    x = ix + 16 + 10
    cv.text(x, base, label, "sans-md", 15, "text")
    cv.text(x + tw + 10, base, "↗", "sans", 15, "text3")
    return cv


def principles(theme):
    cv = Canvas(W, 10, theme, "How I work: " + " ".join(p[0] for p in PRINCIPLES))
    y0 = header(cv, "01", "How I work", "Principles, with receipts")
    cw, pad = W / 2, 40
    top = y0
    for r in range(2):
        hmax = 0
        for c in range(2):
            title, body = PRINCIPLES[r * 2 + c]
            x = c * cw + (pad if c else 0)
            y = top + 44
            cv.text(x, y, ["I", "II", "III", "IV"][r * 2 + c], "mono-md", 12, "accent", track=1.4)
            cv.text(x, y + 38, title, "serif", 28, "text")
            last, _ = cv.para(x, y + 72, body, "sans", 15.5, maxw=cw - pad - 8, lh=24, fill="text2")
            hmax = max(hmax, last - top + 34)
        if r == 0:
            cv.hline(0, W, top + hmax, "line")
        top += hmax
    cv.vline(cw, y0 + 1, top, "line")
    cv.h = int(top + 8)
    return cv


def experience(theme):
    cv = Canvas(W, 10, theme, "Experience: " + "; ".join(
        "%s, %s (%s)" % (e["role"], e["org"], e["when"]) for e in EXPERIENCE))
    t = cv.t
    y0 = header(cv, "02", "Experience", "Four internships · two current")
    MX, CX = 180, 212
    maxw = W - CX
    y = y0 + 58
    marks = []
    for e in EXPERIENCE + [None]:
        edu = e is None
        if edu:
            e = EDUCATION
            y += 4
        cv.text(0, y, e["when"], "mono-md", 11.5, "text2", track=.9, upper=True)
        cv.text(0, y + 21, e["where"], "mono", 11.5, "text3", track=.4)
        marks.append((y - 5, e.get("current", False), edu))
        ow = cv.text(CX, y + 3, e["org"], "serif", 30 if not edu else 26, "text")
        cv.text(CX + ow + 14, y + 2, e["role"], "sans", 15.5, "text2")
        if e.get("current"):
            pw = measure("CURRENT", "mono-md", 10.5, 1.4) + 20
            cv.rect(W - pw - .5, y - 16.5, pw, 22, 11, "none", "accent", 1, ' opacity=".55"')
            cv.text(W - pw + 10, y - 5.5 + cap("mono-md", 10.5) / 2, "CURRENT", "mono-md", 10.5,
                    "accent", track=1.4)
        if edu:
            cv.text(CX, y + 32, e["note"], "mono", 12, "text3", track=.4)
            y += 40
            break
        last, _ = cv.para(CX, y + 36, e["desc"], "sans", 16, maxw=maxw - 20, lh=25, fill="text2")
        ty, tx = last + 20, CX
        for tag in e["tags"]:
            tx += cv.pill(tx, ty, tag, "mono", 11.5, "text3", "line2", h=24, padx=10, track=.2) + 8
        y = ty + 24 + 52
    # timeline
    cv.vline(MX, marks[0][0], marks[-1][0], "line2")
    for my, cur, edu in marks:
        if edu:
            cv.add('<rect x="%s" y="%s" width="9" height="9" transform="rotate(45 %s %s)" '
                   'fill="%s" stroke="%s"/>' % (f(MX + .5 - 4.5), f(my - 4.5), f(MX + .5), f(my),
                                                t["bg"], t["text3"]))
        elif cur:
            cv.circle(MX + .5, my, 9, "accent", extra=' opacity=".18"')
            cv.circle(MX + .5, my, 4.5, "accent")
        else:
            cv.circle(MX + .5, my, 4.5, "bg", "text3", 1.4)
    cv.h = int(y + 6)
    return cv


def work_header(theme):
    cv = Canvas(W, 72, theme, "Selected work")
    header(cv, "03", "Selected work", "Flagship projects")
    return cv


def card(theme, i, p):
    H = 300
    cv = Canvas(CARD_W, H, theme, "%s — %s %s" % (p["name"], p["desc"], p["proof"]))
    t = cv.t
    cv.frame(14, "surface", "line")
    P = 28
    x = P
    x += cv.text(x, 46, "%02d" % (i + 1), "mono-md", 11.5, "accent", track=1.4)
    x += cv.text(x, 46, "  /  ", "mono", 11.5, "line2")
    cv.text(x, 46, p["cat"], "mono", 11.5, "text3", track=1.4, upper=True)
    if p.get("live"):
        lw = measure("LIVE", "mono-md", 10.5, 1.4)
        pw = lw + 34
        px = CARD_W - P - pw
        cv.rect(px, 29, pw, 23, 11.5, "none", "live", 1, ' opacity=".5"')
        cv.circle(px + 13, 40.5, 3.2, "live")
        cv.text(px + 23, 40.5 + cap("mono-md", 10.5) / 2, "LIVE", "mono-md", 10.5, "live", track=1.4)
    cv.text(P - 1, 104, p["name"], "serif", 38, "text")
    cv.para(P, 140, p["desc"], "sans", 15.5, maxw=CARD_W - 2 * P - 4, lh=23.5, fill="text2",
            max_lines=3)
    cv.text(P, 226, p["proof"], "mono-md", 12, "accent", track=.2)
    cv.hline(P, CARD_W - P, 246, "line")
    stack, sep = list(p["stack"]), "  ·  "
    while measure(sep.join(stack), "mono", 12) > CARD_W - 2 * P:
        stack.pop()
    cv.text(P, 274, sep.join(stack), "mono", 12, "text3")
    return cv


def recognition(theme):
    cv = Canvas(W, 10, theme, "Recognition: " + "; ".join("%s — %s, %s" % r for r in RECOGNITION))
    y0 = header(cv, "04", "Recognition", "Awards · rankings · grants")
    cw, gap, rh = (W - 48) / 2, 48, 78
    for k, (big, title, sub) in enumerate(RECOGNITION):
        c, r = k % 2, k // 2
        x = c * (cw + gap)
        top = y0 + r * rh
        cv.text(x, top + 50, big, "serif", 30, "accent")
        cv.text(x + 128, top + 40, title, "sans-md", 16, "text")
        cv.text(x + 128, top + 62, sub, "sans", 14, "text3")
        cv.hline(x, x + cw, top + rh, "line")
    y = y0 + 4 * rh + 40
    last, _ = cv.para(0, y, ALSO, "sans", 14, maxw=W, lh=22, fill="text3")
    cv.h = int(last + 12)
    return cv


def toolkit(theme):
    cv = Canvas(W, 10, theme, "Toolkit: " + "; ".join("%s: %s" % (k, ", ".join(v)) for k, v in TOOLKIT))
    y = header(cv, "05", "Toolkit", "What I reach for")
    LX, maxw, size, sep = 210, W - 210, 16.5, "   ·   "
    for k, items in TOOLKIT:
        lines, cur = [], []
        for it in items:
            if cur and measure(sep.join(cur + [it]), "sans", size) > maxw:
                lines.append(cur)
                cur = []
            cur.append(it)
        lines.append(cur)
        base = y + 40
        cv.text(0, base, k, "mono-md", 11.5, "text3", track=1.6, upper=True)
        for li, ln in enumerate(lines):
            x = LX
            for j, it in enumerate(ln):
                if j:
                    x += cv.text(x, base + li * 28, sep, "sans", size, "line2")
                x += cv.text(x, base + li * 28, it, "sans", size, "text")
        y = base + (len(lines) - 1) * 28 + 22
        cv.hline(0, W, y, "line")
    cv.h = int(y + 4)
    return cv


def footer(theme):
    H = 196
    cv = Canvas(W, H, theme, "If being wrong is expensive, let's talk. Open to AI/ML engineering "
                "roles, research collaborations and serious open source.")
    cv.hline(W / 2 - 24, W / 2 + 24, 6, "accent")
    cv.runs(W / 2, 82, [("If being wrong is expensive, ", "serif", 44, "text"),
                        ("let’s talk.", "serif-it", 44, "accent")], anchor="middle")
    cv.text(W / 2, 122, "Open to AI/ML engineering roles, research collaborations and serious "
            "open source.", "sans", 16.5, "text2", anchor="middle")
    cv.text(W / 2, 160, "HARSHALANDHALE9@GMAIL.COM   ·   PUNE, INDIA   ·   IST, UTC+5:30", "mono",
            11.5, "text3", track=1.4, anchor="middle")
    return cv


# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    out = []
    for th in ("dark", "light"):
        out.append(hero(th).save("hero.svg"))
        for k in ("linkedin", "email", "repos"):
            out.append(button(th, k).save("btn-%s.svg" % k))
        out.append(principles(th).save("principles.svg"))
        out.append(experience(th).save("experience.svg"))
        out.append(work_header(th).save("work.svg"))
        for i, p in enumerate(WORK):
            out.append(card(th, i, p).save("card-%s.svg" % p["key"]))
        out.append(recognition(th).save("recognition.svg"))
        out.append(toolkit(th).save("toolkit.svg"))
        out.append(footer(th).save("footer.svg"))
    import os
    tot = sum(os.path.getsize(p) for p in out)
    print("wrote %d SVGs, %.0f KB total" % (len(out), tot / 1024))
