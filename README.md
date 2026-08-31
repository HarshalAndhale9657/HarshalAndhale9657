<div align="center">

<img src="assets/terminal.svg" alt="Harshal Andhale — AI Engineer. LLM post-training, agentic systems, RAG at scale." width="100%"/>

<a href="https://www.linkedin.com/in/harshal-andhale/"><img src="https://img.shields.io/badge/LinkedIn-0B0E14?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzU2RDRGRiI+PHBhdGggZD0iTTIwLjQ0NyAyMC40NTJoLTMuNTU0di01LjU2OWMwLTEuMzI4LS4wMjctMy4wMzctMS44NTItMy4wMzctMS44NTMgMC0yLjEzNiAxLjQ0NS0yLjEzNiAyLjkzOXY1LjY2N0g5LjM1MVY5aDMuNDE0djEuNTYxaC4wNDZjLjQ3Ny0uOSAxLjYzNy0xLjg1IDMuMzctMS44NSAzLjYwMSAwIDQuMjY3IDIuMzcgNC4yNjcgNS40NTV2Ni4yODZ6TTUuMzM3IDcuNDMzYy0xLjE0NCAwLTIuMDYzLS45MjYtMi4wNjMtMi4wNjUgMC0xLjEzOC45Mi0yLjA2MyAyLjA2My0yLjA2MyAxLjE0IDAgMi4wNjQuOTI1IDIuMDY0IDIuMDYzIDAgMS4xMzktLjkyNSAyLjA2NS0yLjA2NCAyLjA2NXptMS43ODIgMTMuMDE5SDMuNTU1VjloMy41NjR2MTEuNDUyek0yMi4yMjUgMEgxLjc3MUMuNzkyIDAgMCAuNzc0IDAgMS43Mjl2MjAuNTQyQzAgMjMuMjI3Ljc5MiAyNCAxLjc3MSAyNGgyMC40NTFDMjMuMiAyNCAyNCAyMy4yMjcgMjQgMjIuMjcxVjEuNzI5QzI0IC43NzQgMjMuMiAwIDIyLjIyNSAweiIvPjwvc3ZnPg==" height="26" alt="LinkedIn"/></a> <a href="mailto:harshalandhale9@gmail.com"><img src="https://img.shields.io/badge/Email-0B0E14?style=flat-square&logo=gmail&logoColor=FFB86C" height="26" alt="Email"/></a> <a href="https://github.com/HarshalAndhale9657?tab=repositories"><img src="https://img.shields.io/badge/Repositories-0B0E14?style=flat-square&logo=github&logoColor=C792EA" height="26" alt="Repositories"/></a> <img src="https://img.shields.io/badge/Pune,_India-0B0E14?style=flat-square&logo=googlemaps&logoColor=00E58A" height="26" alt="Pune, India"/>

</div>

<br/>

<h3><code>harshal@github:~$ cat ./about.md</code></h3>

I build AI systems that have to survive contact with reality — where a hallucinated answer, an uncalibrated score, or an unverified patch is an actual failure, not a demo bug.

That constraint shapes everything I ship. **A.E.G.I.S.** refuses to open a pull request until it has *executed* the exploit it claims to have found. **Axiom** reports a rupee cost curve instead of a flattering AUC. **Groundwork** is built around calibrated abstention — a model that says *"not found in your history"* rather than inventing one. **P.R.I.S.M.** published a diagnostic showing its own v1 engine was near-noise, then rebuilt it and measured the replacement honestly.

Currently interning across two teams while finishing my CS degree — shipping a Chrome extension to **10K+ users** at Funlingo, and building AI workflows for pharmaceutical molecule prioritisation at SGRAMX.

```
Focus     LLM post-training (SFT · DPO) · agentic systems · RAG at scale · applied ML
Education B.E. Computer Science, Dr. D. Y. Patil Institute of Technology  ·  2024 – 2028
Open to   ML/AI engineering roles · research collaborations · open source
```

<br/>

<h3><code>harshal@github:~$ ./experience --list</code></h3>

<table>
<tr><td width="32%"><b>Software Engineer Intern</b><br/><sub>Funlingo · Remote</sub></td>
<td width="18%"><sub><code>Aug 2026 — present</code></sub></td>
<td>React Chrome extension serving <b>10K+ users</b> across <b>8 streaming platforms</b>. Also drives Next.js web + SEO work.</td></tr>

<tr><td><b>AI Engineer Intern</b><br/><sub>SGRAMX · Remote / Pune</sub></td>
<td><sub><code>Jul 2026 — present</code></sub></td>
<td>AI workflows for <b>PharmX</b> — drug-molecule evaluation, scoring and prioritisation, with multi-stakeholder criteria producing structured rankings.</td></tr>

<tr><td><b>LLM Post-Training Intern</b><br/><sub>Ethara AI · Remote / Gurugram</sub></td>
<td><sub><code>Feb 2026 — May 2026</code></sub></td>
<td><b>SFT and DPO</b> post-training for domain-specific models. Lifted reliability and output quality through data curation, prompt optimisation and evaluation.</td></tr>

<tr><td><b>ML Engineer Intern</b><br/><sub>Labmentix · Remote / Bengaluru</sub></td>
<td><sub><code>Dec 2025 — Feb 2026</code></sub></td>
<td>ML pipelines for tourism behaviour analysis; collaborative + content-based recommenders shipped through Streamlit.</td></tr>
</table>

<br/>

<h3><code>harshal@github:~$ ls ./flagship/</code></h3>

<table>
<tr>
<td width="50%" valign="top">

#### 🛡️ [A.E.G.I.S.](https://github.com/HarshalAndhale9657/ANVIL) · [live ↗](https://aegis-frontend-azure.vercel.app)

`Python` `FastAPI` `Colored Petri Nets` `LLM Agents` `OpenTelemetry`

An autonomous red-team engine that finds a vulnerability, **executes the exploit to prove it's real**, patches it, and opens the PR — with no human in the loop.

The interesting part is the failure handling. A **Colored Petri Net** governs execution, so the agent routes deterministically instead of death-spiralling on retries. Verification gates are **fail-closed**: unproven findings are discarded, not reported. Every decision is traced end-to-end via W3C distributed tracing, so the run is auditable rather than a black box.

</td>
<td width="50%" valign="top">

#### 🔬 [P.R.I.S.M.](https://github.com/HarshalAndhale9657/P.R.I.S.M) · [live ↗](https://p-r-i-s-m-psi.vercel.app/)

`Python` `FastAPI` `spaCy` `HDBSCAN` `OpenAlex` `GPT-4o`

Originality checker that catches **stitched plagiarism** — verbatim, paraphrased *and translated* — then attributes each span to its actual source.

**Precision 1.00 · Recall 0.86 · FPR 0.00** <sub>(controlled set, `eval_matcher.py`)</sub>

It's also the project I'm most willing to defend. v1 was stylometric; I benchmarked it, found the detection was **near-noise**, published the diagnostic in-repo, and rebuilt it around source attribution. The old claims are marked superseded rather than quietly deleted.

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 📊 [Axiom](https://github.com/HarshalAndhale9657/Axiom)

`LightGBM` `SHAP` `Gemini` `FastAPI` `Next.js`

RTO/COD fraud risk manager built for the **Razorpay AI Buildathon**. Blocking a good customer costs ~13× the fraud you prevent, so the headline metric is **rupees, not AUC**:

| Policy | ₹ / 1k orders |
|---|---:|
| Approve everything | ₹64,795 |
| Naive "block all COD" | ₹71,776 |
| **Axiom @ τ\*** | **₹49,254** |

Block-all-COD is *worse than doing nothing* — that result **is** the false-positive-cost argument. PR-AUC **0.51** at 0.17 prevalence, Brier **0.108**, ROC-AUC 0.80 — deliberately not a fake 0.99. Leakage-safe by construction, with a guard test that fails if any feature can see its own label.

</td>
<td width="50%" valign="top">

#### 🧠 [Groundwork](https://github.com/HarshalAndhale9657/LocalOS)

`Chrome MV3` `WXT` `Transformers.js` `PGlite` `QLoRA` `Ollama`

A local-first agentic browser assistant, and the research project behind my thesis on **calibrated grounding**: act only on what's on the page, answer only from what was actually read, and *abstain* otherwise.

Runs the full loop — observe (CDP a11y snapshot) → decide → risk-gate → confirm → act → re-observe — behind a SAFE/CAUTION/UNSAFE confirmation gate. Retrieval is cosine + time-decay + MMR + negative rejection over an in-browser Postgres. Ships with **Personal-Memory-RGB**, a purpose-built benchmark for refusal metrics. Nothing leaves the device.

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🏛️ [CampusLens](https://github.com/HarshalAndhale9657/Campus-Lens) · [live ↗](https://campus-lens-delta.vercel.app/)

`React Three Fiber` `WebGL` `FastAPI` `Socket.IO` `RAG`

A real-time **3D digital twin** of a university campus. Rooms glow green when free, a live density heatmap flags overcrowding, and a RAG chatbot answers *"where is this professor teaching right now?"*

Built so the simulation engine can be swapped for real IoT sensors without touching the frontend.

</td>
<td width="50%" valign="top">

#### 💰 [Reconciliation Engine](https://github.com/HarshalAndhale9657/Reconcillation-Engine)

`TypeScript` `Kafka` `PostgreSQL` `Docker` `Microservices`

Event-driven financial reconciliation for ledger systems that receive **out-of-order and delayed** records from mismatched sources.

Kafka streaming, isolated ingestion and reconciliation services, deterministic matching, durable state in Postgres — built for replay and auditability. *Ingest once. Stream events. Reconcile deterministically.*

</td>
</tr>
</table>

<details>
<summary><b><code>harshal@github:~$ ls ./flagship/ --all</code></b> &nbsp;— five more worth opening</summary>

<br/>

| Project | What it is |
|---|---|
| 🔥 [**IncidentForge**](https://github.com/HarshalAndhale9657/OpenEnv) | An **OpenEnv RL environment** that trains LLMs to act as SREs — diagnosing and remediating incidents in simulated microservice infrastructure. Custom action and observation spaces, reward design, curriculum learning, baseline scores. Built for the **Meta × PyTorch** hackathon. |
| 🧠 [**Second Brain**](https://github.com/HarshalAndhale9657/SecondBrain) | Chrome extension running a complete RAG pipeline **entirely in-browser** — Transformers.js embeddings over **PGlite + pgvector** (WebAssembly Postgres) with HNSW indexing. Ask questions about anything you've read; nothing is uploaded. |
| 🎨 [**VEKTOR Studio**](https://github.com/HarshalAndhale9657/VEKTOR) | A production web studio site — full JSON-LD `ProfessionalService` schema, OG and Twitter cards, sitemap, hardened API routes. Real client-facing work, not a template. |
| 🏥 [**MediSense AI**](https://github.com/HarshalAndhale9657/MediSense-AI) | Multimodal health assistant on GPT-4o Vision — decodes medical reports, checks drug interactions, analyses skin conditions, serves first-aid guidance. |
| 🛢️ [**LeakSense**](https://github.com/HarshalAndhale9657/LeakSense-Dashboard) | IoT multi-gas leak detection. ESP32 → serial → SQLite → Flask/Socket.IO at 1 Hz, with auto-reconnect, an offline watchdog, and a simulator mode so it demos with no hardware attached. Runs unchanged on a laptop or a Raspberry Pi 4. |

</details>

<br/>

<h3><code>harshal@github:~$ ./metrics --render</code></h3>

<div align="center">

<img src="assets/metrics-overview.svg" width="49%" alt="GitHub overview and commit calendar"/> <img src="assets/metrics-languages.svg" width="49%" alt="Language breakdown"/>

<img src="assets/metrics-habits.svg" width="49%" alt="Coding habits"/>

<sub>Rendered nightly by <a href="https://github.com/lowlighter/metrics">lowlighter/metrics</a> and committed into this repo — no third-party rate limits, no broken images.</sub>

</div>

<br/>

<h3><code>harshal@github:~$ cat ./stack.txt</code></h3>

<table>
<tr><td><b>AI / ML</b></td><td>
<img src="https://img.shields.io/badge/PyTorch-0B0E14?style=flat-square&logo=pytorch&logoColor=EE4C2C" alt="PyTorch"/>
<img src="https://img.shields.io/badge/Transformers-0B0E14?style=flat-square&logo=huggingface&logoColor=FFD21E" alt="Transformers"/>
<img src="https://img.shields.io/badge/PEFT_·_SFT_·_DPO-0B0E14?style=flat-square&logo=huggingface&logoColor=FFD21E" alt="PEFT SFT DPO"/>
<img src="https://img.shields.io/badge/scikit--learn-0B0E14?style=flat-square&logo=scikitlearn&logoColor=F7931E" alt="scikit-learn"/>
<img src="https://img.shields.io/badge/LightGBM-0B0E14?style=flat-square" alt="LightGBM"/>
<img src="https://img.shields.io/badge/SHAP-0B0E14?style=flat-square" alt="SHAP"/>
<img src="https://img.shields.io/badge/MLflow-0B0E14?style=flat-square&logo=mlflow&logoColor=0194E2" alt="MLflow"/>
</td></tr>

<tr><td><b>LLM / Agents</b></td><td>
<img src="https://img.shields.io/badge/LangChain-0B0E14?style=flat-square&logo=langchain&logoColor=1C3C3C" alt="LangChain"/>
<img src="https://img.shields.io/badge/LangGraph-0B0E14?style=flat-square&logo=langgraph&logoColor=56D4FF" alt="LangGraph"/>
<img src="https://img.shields.io/badge/OpenAI-0B0E14?style=flat-square" alt="OpenAI"/>
<img src="https://img.shields.io/badge/Claude-0B0E14?style=flat-square&logo=anthropic&logoColor=D97757" alt="Claude"/>
<img src="https://img.shields.io/badge/Gemini-0B0E14?style=flat-square&logo=googlegemini&logoColor=8E75B2" alt="Gemini"/>
<img src="https://img.shields.io/badge/Ollama-0B0E14?style=flat-square&logo=ollama&logoColor=FFFFFF" alt="Ollama"/>
<img src="https://img.shields.io/badge/RAG-0B0E14?style=flat-square" alt="RAG"/>
</td></tr>

<tr><td><b>Data / Vector</b></td><td>
<img src="https://img.shields.io/badge/PostgreSQL-0B0E14?style=flat-square&logo=postgresql&logoColor=4169E1" alt="PostgreSQL"/>
<img src="https://img.shields.io/badge/MongoDB-0B0E14?style=flat-square&logo=mongodb&logoColor=47A248" alt="MongoDB"/>
<img src="https://img.shields.io/badge/pgvector-0B0E14?style=flat-square&logo=postgresql&logoColor=4169E1" alt="pgvector"/>
<img src="https://img.shields.io/badge/Pinecone-0B0E14?style=flat-square" alt="Pinecone"/>
<img src="https://img.shields.io/badge/FAISS-0B0E14?style=flat-square&logo=meta&logoColor=0467DF" alt="FAISS"/>
<img src="https://img.shields.io/badge/ChromaDB-0B0E14?style=flat-square" alt="ChromaDB"/>
<img src="https://img.shields.io/badge/Neo4j-0B0E14?style=flat-square&logo=neo4j&logoColor=4581C3" alt="Neo4j"/>
<img src="https://img.shields.io/badge/Kafka-0B0E14?style=flat-square&logo=apachekafka&logoColor=FFFFFF" alt="Kafka"/>
</td></tr>

<tr><td><b>Backend</b></td><td>
<img src="https://img.shields.io/badge/Python-0B0E14?style=flat-square&logo=python&logoColor=3776AB" alt="Python"/>
<img src="https://img.shields.io/badge/FastAPI-0B0E14?style=flat-square&logo=fastapi&logoColor=009688" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Node.js-0B0E14?style=flat-square&logo=nodedotjs&logoColor=339933" alt="Node.js"/>
<img src="https://img.shields.io/badge/Express-0B0E14?style=flat-square&logo=express&logoColor=FFFFFF" alt="Express"/>
<img src="https://img.shields.io/badge/Flask-0B0E14?style=flat-square&logo=flask&logoColor=FFFFFF" alt="Flask"/>
<img src="https://img.shields.io/badge/Java-0B0E14?style=flat-square&logo=openjdk&logoColor=FFFFFF" alt="Java"/>
</td></tr>

<tr><td><b>Frontend</b></td><td>
<img src="https://img.shields.io/badge/React-0B0E14?style=flat-square&logo=react&logoColor=61DAFB" alt="React"/>
<img src="https://img.shields.io/badge/Next.js-0B0E14?style=flat-square&logo=nextdotjs&logoColor=FFFFFF" alt="Next.js"/>
<img src="https://img.shields.io/badge/TypeScript-0B0E14?style=flat-square&logo=typescript&logoColor=3178C6" alt="TypeScript"/>
<img src="https://img.shields.io/badge/Three.js-0B0E14?style=flat-square&logo=threedotjs&logoColor=FFFFFF" alt="Three.js"/>
<img src="https://img.shields.io/badge/Tailwind-0B0E14?style=flat-square&logo=tailwindcss&logoColor=06B6D4" alt="Tailwind"/>
</td></tr>

<tr><td><b>Infra</b></td><td>
<img src="https://img.shields.io/badge/Docker-0B0E14?style=flat-square&logo=docker&logoColor=2496ED" alt="Docker"/>
<img src="https://img.shields.io/badge/Kubernetes-0B0E14?style=flat-square&logo=kubernetes&logoColor=326CE5" alt="Kubernetes"/>
<img src="https://img.shields.io/badge/OpenTelemetry-0B0E14?style=flat-square&logo=opentelemetry&logoColor=FFFFFF" alt="OpenTelemetry"/>
<img src="https://img.shields.io/badge/Redis-0B0E14?style=flat-square&logo=redis&logoColor=FF4438" alt="Redis"/>
<img src="https://img.shields.io/badge/GitHub_Actions-0B0E14?style=flat-square&logo=githubactions&logoColor=2088FF" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/AWS-0B0E14?style=flat-square" alt="AWS"/>
</td></tr>
</table>

<br/>

<h3><code>harshal@github:~$ ./achievements --verify</code></h3>

```
[✓] NPTEL · Introduction to Large Language Models — IIT Delhi
    Top 2% nationally · All India Rank under 100

[✓] DEVCLASH 2026 — Winner
    Pune's largest inter-collegiate hackathon · 50+ colleges

[✓] $750 Prototype Development Grant — La Trobe University, Australia

[✓] NPTEL · Introduction to Machine Learning — IIT Madras · Top 5%

[✓] Technical Lead — Computer Society of India (CSI), DYPIT chapter

[✓] Meta × PyTorch Hackathon — IncidentForge (OpenEnv RL environment)

[✓] 300+ DSA problems — LeetCode · GeeksforGeeks

[✓] Machine Learning Specialization · PyTorch for Deep Learning — DeepLearning.AI
```

<br/>

<h3><code>harshal@github:~$ ./connect --now</code></h3>

<div align="center">

<a href="https://www.linkedin.com/in/harshal-andhale/"><img src="https://img.shields.io/badge/LinkedIn-0B0E14?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzU2RDRGRiI+PHBhdGggZD0iTTIwLjQ0NyAyMC40NTJoLTMuNTU0di01LjU2OWMwLTEuMzI4LS4wMjctMy4wMzctMS44NTItMy4wMzctMS44NTMgMC0yLjEzNiAxLjQ0NS0yLjEzNiAyLjkzOXY1LjY2N0g5LjM1MVY5aDMuNDE0djEuNTYxaC4wNDZjLjQ3Ny0uOSAxLjYzNy0xLjg1IDMuMzctMS44NSAzLjYwMSAwIDQuMjY3IDIuMzcgNC4yNjcgNS40NTV2Ni4yODZ6TTUuMzM3IDcuNDMzYy0xLjE0NCAwLTIuMDYzLS45MjYtMi4wNjMtMi4wNjUgMC0xLjEzOC45Mi0yLjA2MyAyLjA2My0yLjA2MyAxLjE0IDAgMi4wNjQuOTI1IDIuMDY0IDIuMDYzIDAgMS4xMzktLjkyNSAyLjA2NS0yLjA2NCAyLjA2NXptMS43ODIgMTMuMDE5SDMuNTU1VjloMy41NjR2MTEuNDUyek0yMi4yMjUgMEgxLjc3MUMuNzkyIDAgMCAuNzc0IDAgMS43Mjl2MjAuNTQyQzAgMjMuMjI3Ljc5MiAyNCAxLjc3MSAyNGgyMC40NTFDMjMuMiAyNCAyNCAyMy4yMjcgMjQgMjIuMjcxVjEuNzI5QzI0IC43NzQgMjMuMiAwIDIyLjIyNSAweiIvPjwvc3ZnPg==" height="34" alt="LinkedIn"/></a> &nbsp; <a href="mailto:harshalandhale9@gmail.com"><img src="https://img.shields.io/badge/harshalandhale9@gmail.com-0B0E14?style=for-the-badge&logo=gmail&logoColor=FFB86C" height="34" alt="Email"/></a>

<br/>

<sub><i>Open to ML/AI engineering roles, research collaborations, and open-source work.<br/>If you're building something where being wrong is expensive — I'd like to hear about it.</i></sub>

<br/><br/>

<img src="https://raw.githubusercontent.com/HarshalAndhale9657/HarshalAndhale9657/output/github-contribution-grid-snake-dark.svg" alt="Contribution snake" width="100%"/>

</div>
