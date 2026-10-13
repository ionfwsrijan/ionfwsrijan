<div align="center">

# Srijan Jaiswal

**Generative AI · Applied ML · Security Engineering**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/srijancodes)
[![Website](https://img.shields.io/badge/Website-111827?style=flat-square&logo=googlechrome&logoColor=white)](https://srijanbuilds.dev/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:jaiswalsrijan505@gmail.com)

</div>

```text
~ $ whoami
srijan jaiswal. builds LLM systems, ML pipelines and security tooling.

~ $ now
Research Intern, AI/ML @ Samsung R&D Institute Bangalore
```

---

## About

I build AI systems that hold up outside a notebook: retrieval pipelines that cite their sources, models that explain their predictions, and scanners that find what is broken and propose the fix. Most of my work sits where machine learning meets security and infrastructure.

At Samsung R&D Institute Bangalore I work on applied ML and Generative AI research with senior research engineers, covering model development, experimentation and evaluation across deep learning, NLP and LLM-based systems.

Outside of work I contribute to open source. I ranked #1 overall among contributors at GirlScript Summer of Code, served as a project admin at Social Summer of Code (mentoring contributors, reviewing PRs and triaging issues), and authored LangChain integration examples and RAG utilities used by 20+ developers.

---

## Selected Work

### [PatchPilot](https://github.com/ionfwsrijan/PatchPilot)
Automated code security triage: scan, fix, verify and export compliance evidence, all running locally.

- Runs Semgrep (SAST), OSV-Scanner (dependencies) and Gitleaks (secrets) in parallel against a ZIP or GitHub repo
- Cut manual review time by about 60% across codebases of 500+ files
- LLM-assisted remediation with inference latency under 150ms, followed by a verification pass and a downloadable evidence pack
- ML layer for severity ranking, finding deduplication, false-positive filtering and fix-success prediction; local LLM patch generation via Ollama
- Open source, with outside contributors

`Python` `FastAPI` `React` `Vite` `Tailwind` `Docker` `Semgrep` `OSV-Scanner` `Gitleaks`

### [Skewline](https://github.com/ionfwsrijan/Skewline)
Research-grade limit-order-book simulator for benchmarking market making strategies under realistic microstructure constraints.

- Benchmarks 7 quoting strategies (Avellaneda-Stoikov, GLFT, flow imbalance, tabular RL, DQN and multi-asset hedging) under stochastic latency, adverse selection and partial fills
- Full-stack FastAPI and React dashboard with real-time WebSocket streaming
- Validated against real Binance BTC, ETH and SOL trade data using KS-test distribution comparison
- 28+ automated tests, CI and Docker deployment

`Python` `FastAPI` `React` `NumPy` `WebSocket` `Docker`

### [Driftmark](https://github.com/ionfwsrijan/Driftmark)
End-to-end churn prediction with explanations and monitoring built in.

- Tabular (LightGBM), NLP and sequence models ensembled into a time-aware, calibrated stacker
- 85% accuracy (F1 0.78) across 10K+ customer records
- SHAP-based reason codes and automated CRM campaign exports
- FastAPI batch-scoring API with PSI-based drift monitoring

`Python` `LightGBM` `XGBoost` `SHAP` `FastAPI` `Poetry`

### [Lexivault](https://github.com/ionfwsrijan/Lexivault)
RAG-based document Q&A with citations, built to be measured.

- 0.909 mean answer relevance on an evaluation set (90%+)
- ChromaDB vector store, MMR retrieval and cross-encoder reranking
- Ingests PDF, DOCX, TXT, Markdown and URLs; streams answers over SSE with chunk-level citations
- Feedback loop, drift monitoring, evaluation and benchmark scripts; Docker and GitHub Actions CI/CD

`Python` `LangChain` `ChromaDB` `FastAPI` `OpenAI` `Docker` `GitHub Actions`

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

<div align="center">

<a href="https://github.com/ionfwsrijan">
  <img height="170" alt="GitHub stats" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=ionfwsrijan&theme=github_dark" />
</a>
<a href="https://github.com/ionfwsrijan">
  <img height="170" alt="Most used languages in commits" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=ionfwsrijan&theme=github_dark" />
</a>

</div>

---

<div align="center">

*Building AI systems that don't just predict. They protect, explain and scale.*

[jaiswalsrijan505@gmail.com](mailto:jaiswalsrijan505@gmail.com)

</div>
