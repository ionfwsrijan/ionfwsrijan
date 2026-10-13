<div align="center">

<img src="assets/banner.svg" alt="Srijan Jaiswal: Generative AI, Applied ML, Security Engineering" width="100%">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-srijancodes-0A66C2?style=flat-square&logo=linkedin&logoColor=white&labelColor=111827)](https://linkedin.com/in/srijancodes)
[![Portfolio](https://img.shields.io/badge/Website-srijanbuilds.dev-2563eb?style=flat-square&logo=googlechrome&logoColor=white&labelColor=111827)](https://srijanbuilds.dev/)
[![Email](https://img.shields.io/badge/Email-jaiswalsrijan505-EA4335?style=flat-square&logo=gmail&logoColor=white&labelColor=111827)](mailto:jaiswalsrijan505@gmail.com)

![Samsung R&D](https://img.shields.io/badge/Samsung%20R%26D%20Bangalore-Research%20Intern-2563eb?style=flat-square&labelColor=111827)
![GSSoC](https://img.shields.io/badge/GSSoC-%231%20Contributor-2563eb?style=flat-square&labelColor=111827)
![SSoC](https://img.shields.io/badge/SSoC-Project%20Admin-2563eb?style=flat-square&labelColor=111827)

</div>

---

## About

I build AI systems that hold up outside a notebook: retrieval pipelines that cite their sources, models that explain their predictions, and scanners that find what is broken and propose the fix. Most of my work sits where machine learning meets security and infrastructure.

At Samsung R&D Institute Bangalore I work on applied ML and Generative AI research alongside senior research engineers, covering model development, experimentation and evaluation across deep learning, NLP and LLM-based systems.

**Open source**

- Ranked #1 overall among contributors at GirlScript Summer of Code
- Project Admin at Social Summer of Code: mentoring contributors, reviewing PRs, triaging issues
- Authored LangChain integration examples and RAG utilities used by 20+ developers

---

## Selected Work

### [PatchPilot](https://github.com/ionfwsrijan/PatchPilot)

*Automated code security triage: scan, fix, verify and export compliance evidence. Runs entirely locally.*

```mermaid
flowchart LR
    A["Repo or ZIP"] --> B["Semgrep · OSV-Scanner · Gitleaks"]
    B --> C["Triage and ranking"]
    C --> D["Proposed fixes"]
    D --> E["Verify"]
    E --> F["Evidence pack"]
```

![Review time](https://img.shields.io/badge/review%20time-~60%25%20less-2563eb?style=flat-square&labelColor=111827)
![Scale](https://img.shields.io/badge/scanned-500%2B%20files-2563eb?style=flat-square&labelColor=111827)
![Latency](https://img.shields.io/badge/inference-%3C150%20ms-2563eb?style=flat-square&labelColor=111827)

<details>
<summary>Under the hood</summary>

- Runs SAST, dependency and secret scanners in parallel against a ZIP upload or a GitHub repo
- LLM-assisted remediation with sub-150ms inference, followed by a verification pass that re-runs the checks
- ML layer for severity ranking, finding deduplication, false-positive filtering and fix-success prediction; local LLM patch generation via Ollama
- Exports a compliance evidence pack with audit artifacts and diffs
- Open source, with outside contributors

`Python` `FastAPI` `React` `Vite` `Tailwind` `Docker` `Semgrep` `OSV-Scanner` `Gitleaks`

</details>

### [Skewline](https://github.com/ionfwsrijan/Skewline)

*Research-grade limit-order-book simulator for benchmarking market making strategies under realistic microstructure constraints.*

```mermaid
flowchart LR
    A["Price process"] --> B["Order flow"]
    B --> C["Latency queue"]
    C --> D["Limit order book"]
    D --> E["Agent quotes"]
    E --> F["Risk manager"]
    D --> G["Metrics and live dashboard"]
```

![Strategies](https://img.shields.io/badge/strategies-7-2563eb?style=flat-square&labelColor=111827)
![Tests](https://img.shields.io/badge/tests-28%2B-2563eb?style=flat-square&labelColor=111827)
![Validation](https://img.shields.io/badge/validated%20on-real%20Binance%20trades-2563eb?style=flat-square&labelColor=111827)

<details>
<summary>Under the hood</summary>

- Benchmarks Avellaneda-Stoikov, GLFT, flow imbalance, tabular RL, DQN and multi-asset hedging under stochastic latency, adverse selection and partial fills
- Full-stack FastAPI and React dashboard with real-time WebSocket streaming
- Backtested against real Binance BTC, ETH and SOL trade data using KS-test distribution comparison
- 28+ automated tests, CI and Docker deployment

`Python` `FastAPI` `React` `NumPy` `WebSocket` `Docker`

</details>

### [Driftmark](https://github.com/ionfwsrijan/Driftmark)

*End-to-end churn prediction with explanations and monitoring built in.*

```mermaid
flowchart LR
    A["Raw data"] --> B["Snapshots and 30-day churn labels"]
    B --> C["Tabular · NLP · Sequence models"]
    C --> D["Calibrated stacker"]
    D --> E["Reason codes and campaign export"]
    E --> F["FastAPI and drift report"]
```

![Accuracy](https://img.shields.io/badge/accuracy-85%25-2563eb?style=flat-square&labelColor=111827)
![F1](https://img.shields.io/badge/F1-0.78-2563eb?style=flat-square&labelColor=111827)
![Records](https://img.shields.io/badge/records-10K%2B-2563eb?style=flat-square&labelColor=111827)

<details>
<summary>Under the hood</summary>

- Tabular (LightGBM), NLP and sequence models ensembled into a time-aware, calibrated stacker
- SHAP-based reason codes and automated CRM campaign exports
- FastAPI batch-scoring API with PSI-based drift monitoring

`Python` `LightGBM` `XGBoost` `SHAP` `FastAPI` `Poetry`

</details>

### [Lexivault](https://github.com/ionfwsrijan/Lexivault)

*RAG-based document Q&A with citations, built to be measured.*

```mermaid
flowchart LR
    A["Ingest PDF · DOCX · TXT · MD · URL"] --> B["Chunk and embed"]
    B --> C[("ChromaDB")]
    C --> D["MMR retrieval and rerank"]
    D --> E["LLM answer"]
    E --> F["Citations and streaming"]
```

![Relevance](https://img.shields.io/badge/relevance-0.909%20mean-2563eb?style=flat-square&labelColor=111827)
![Retrieval](https://img.shields.io/badge/retrieval-MMR%20%2B%20cross--encoder-2563eb?style=flat-square&labelColor=111827)

<details>
<summary>Under the hood</summary>

- 90%+ answer relevance on an evaluation set
- Multi-format ingestion, SSE streaming and chunk-level citations
- Feedback loop, drift monitoring, evaluation and benchmark scripts
- CI/CD with Docker and GitHub Actions

`Python` `LangChain` `ChromaDB` `FastAPI` `OpenAI` `Docker` `GitHub Actions`

</details>

---

## Stack

**Languages**
&nbsp;![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)

**ML and Generative AI**
&nbsp;![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)

**Backend and Infrastructure**
&nbsp;![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

**Frontend**
&nbsp;![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)

**Security Tooling**
&nbsp;![Semgrep](https://img.shields.io/badge/Semgrep-SAST-1B2A49?style=flat-square)
![OSV-Scanner](https://img.shields.io/badge/OSV--Scanner-SCA-4285F4?style=flat-square)
![Gitleaks](https://img.shields.io/badge/Gitleaks-Secrets-DC2626?style=flat-square)

---

## Activity

<div align="center"> <img src="https://github-statspro.vercel.app/api/stats/ionfwsrijan?theme=dark&design=compact" alt="Contribution activity" width="98%"> </div>

---

<div align="center">

*Building AI systems that don't just predict. They protect, explain and scale.*

[jaiswalsrijan505@gmail.com](mailto:jaiswalsrijan505@gmail.com)

</div>
