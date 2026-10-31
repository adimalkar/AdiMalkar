<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&center=true&vCenter=true&multiline=true&width=700&height=80&lines=%3E_+Aditya+Malkar;Data+Scientist+%7C+ML+Engineer" alt="Typing SVG" />
</h1>

<p align="center">
  <em>Building autonomous AI systems &amp; high-performance data pipelines.</em>
</p>

<p align="center">
  <a href="https://www.adityamalkar.com"><img src="https://img.shields.io/badge/Portfolio-1F6FEB?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"/></a>&nbsp;
  <a href="https://www.linkedin.com/in/aditya-malkar-694490253/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>&nbsp;
  <a href="mailto:amalkar@stevens.edu"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
</p>

<br>

## About Me

I'm Aditya — a Data Scientist and ML Engineer currently finishing my **M.S. in Data Science at Stevens Institute of Technology** in Hoboken, NJ. I got into this field because I genuinely enjoy the process of taking messy, real-world problems and turning them into something a model can reason about.

Most of my work revolves around **LLM-driven autonomous systems** and **scalable data pipelines**. I've built things like multi-agent RAG systems that orchestrate specialized LLM workers, browser extensions that have to fight through Shadow DOM and framework-level restrictions to automate form filling, and speech-to-speech translation pipelines where every millisecond of latency matters. I care a lot about writing code that actually ships — not just notebooks that run once.

Outside of the typical ML stack, I spend time thinking about **AI safety and alignment**. I find the challenge of getting deterministic, trustworthy behavior out of probabilistic models genuinely interesting, not just as an academic question but as something that matters the moment you put a model in front of real users. I'm also an **AWS Certified AI Practitioner** and **ML Engineer**, which keeps me grounded in how these systems run at scale in production.

<br>

## Currently Building

| Project | Description |
|:--------|:------------|
| **[Termnova](https://github.com/adimalkar/termnova)** · [*live demo*](https://termnova.onrender.com) | Production-grade AI contract intelligence platform with hybrid RAG (dense vector + BM25 reranking), LangGraph multi-agent orchestration, OpenTelemetry distributed tracing, Celery async queues, and hallucination guardrails. |
| **[Cadence](https://github.com/adimalkar/cadence-ci)** | Open-source CI intelligence for GitHub Actions — analyzes build history over the plain GitHub API, quantifies wasted runtime and dollar costs, and automatically opens the PR that fixes it with zero configuration. |
| **[Multimodal Fraud Detector](https://github.com/adimalkar/multimodal-fraud-detector)** · [*live demo*](https://frontend-adimalkars-projects.vercel.app) | Multi-agent AI pipeline detecting generative-AI fraud in insurance claims across images, PDFs, and video. Employs a "Jury System" of Qwen-VL forensic vision analysis paired with DeepSeek-R1 / Qwen / GLM critic agents with majority voting. |
| **[QuantServe](https://github.com/adimalkar/quantserve)** | Hardware-aware LLM deployment optimizer & inference systems engine — surrogate latency/VRAM models predicting TTFT and TPOT, custom Triton fused W4A16 dequant kernels, and automated Docker / Kubernetes manifest export. |
| **[Supplier Intelligence Platform](https://github.com/adimalkar/supplier-intelligence-platform)** | Real-time supplier intelligence & quality monitoring engine — agentic AI root-cause analysis, edge computer vision defect detection (YOLOv8), and distributed Kafka/Airflow data streaming pipelines. |

<br>

## Open Source Contributions

<!-- START_SECTION:contributions -->
**18 merged pull requests in 7 projects**, plus 13 in review — fixes and features in ML infrastructure, compilers, agent frameworks, and evaluation tooling.

| Project | Stars | Merged | What I fixed |
|:--------|------:|:-------|:-------------|
| **[kornia](https://github.com/kornia/kornia)** | 11.5k | [10 PRs](https://github.com/pulls?q=is%3Apr+author%3Aadimalkar+-user%3Aadimalkar+-user%3Ahiringfleet+is%3Amerged+repo%3Akornia%2Fkornia) | Revived LoFTR CPU accuracy tests; fixed PatchMix bounding boxes, `same_on_batch` pairing and input-rank errors across augmentations. |
| **[great_expectations](https://github.com/fivetran/great_expectations)** | 11.9k | [#12254](https://github.com/fivetran/great_expectations/pull/12254) · [#12173](https://github.com/fivetran/great_expectations/pull/12173) | Resolved 36 mypy errors across 8 excluded integration test modules; serialized infinite `Decimal`s instead of raising. |
| **[sqlfluff](https://github.com/sqlfluff/sqlfluff)** | 10k | [#8420](https://github.com/sqlfluff/sqlfluff/pull/8420) · [#8411](https://github.com/sqlfluff/sqlfluff/pull/8411) | Added full AST grammar for Snowflake `CREATE/ALTER/DROP ALERT` DDL; fixed reflow alignment for leading-comma T-SQL. |
| **[Arize Phoenix](https://github.com/Arize-ai/phoenix)** | 12.1k | [#15683](https://github.com/Arize-ai/phoenix/pull/15683) | Fixed playground/evaluator clients silently dropping Anthropic & Bedrock tool-`choice` and `strict` configurations prior to dispatch. |
| **[Microsoft PyRIT](https://github.com/microsoft/PyRIT)** | 4.7k | [#3051](https://github.com/microsoft/PyRIT/pull/3051) | Let the PUZZLED keyword masker select words with non-ASCII letters. |
| **[MLC-AI xgrammar](https://github.com/mlc-ai/xgrammar)** | 2k | [#929](https://github.com/mlc-ai/xgrammar/pull/929) | Resolved JSON Schema references through array indices for grammar-guided LLM structured output generation. |
| **[NVIDIA numba-cuda-mlir](https://github.com/NVIDIA/numba-cuda-mlir)** | 74 | [#307](https://github.com/NVIDIA/numba-cuda-mlir/pull/307) | Fixed float-to-bool conversion in the MLIR lowering by comparing against zero instead of truncating. |

<details>
<summary><b>In review (13)</b>: hermes-agent, browser-use, vLLM, CrewAI, …</summary>

| Project | Stars | Pull request |
|:--------|------:|:-------------|
| **[hermes-agent](https://github.com/NousResearch/hermes-agent)** | 259k | [#132669](https://github.com/NousResearch/hermes-agent/pull/132669) Show saved working directories in session lists |
| **[browser-use](https://github.com/browser-use/browser-use)** | 120k | [#6023](https://github.com/browser-use/browser-use/pull/6023) Accept X \| None annotations on special action params |
| **[vLLM](https://github.com/vllm-project/vllm)** | 96k | [#58879](https://github.com/vllm-project/vllm/pull/58879) Use original context length for mRoPE YaRN correction range |
| **[CrewAI](https://github.com/crewAIInc/crewAI)** | 60.4k | [#7742](https://github.com/crewAIInc/crewAI/pull/7742) Fail when expected metric has no score |
| **[Stanford DSPy](https://github.com/stanfordnlp/dspy)** | 38.9k | [#10275](https://github.com/stanfordnlp/dspy/pull/10275) Reject reserved `trajectory` output name in ReAct (follow-up to #9852) |
| **[Microsoft ONNX Runtime](https://github.com/microsoft/onnxruntime)** | 22.2k | [#32703](https://github.com/microsoft/onnxruntime/pull/32703) Reconnect the producer edge when DivMulFusion substitutes the Mul's input |
| **[Arize Phoenix](https://github.com/Arize-ai/phoenix)** | 12.1k | [#16118](https://github.com/Arize-ai/phoenix/pull/16118) Expose per-span cost scalars in trace and session filters |
| **[great_expectations](https://github.com/fivetran/great_expectations)** | 11.9k | [#12255](https://github.com/fivetran/great_expectations/pull/12255) Count rows with NULLs as unexpected on SQL in four pair and multicolumn Expectations |
| **[MLC-AI xgrammar](https://github.com/mlc-ai/xgrammar)** | 2k | [#1008](https://github.com/mlc-ai/xgrammar/pull/1008) Ignore a string pattern whose regex syntax is not supported |
| **[MLC-AI xgrammar](https://github.com/mlc-ai/xgrammar)** | 2k | [#969](https://github.com/mlc-ai/xgrammar/pull/969) Warn when a string schema uses a format that is not built in |
| **[NVIDIA numba-cuda-mlir](https://github.com/NVIDIA/numba-cuda-mlir)** | 74 | [#421](https://github.com/NVIDIA/numba-cuda-mlir/pull/421) Lower NumPy scalars read through module attributes |
| **[NVIDIA numba-cuda-mlir](https://github.com/NVIDIA/numba-cuda-mlir)** | 74 | [#420](https://github.com/NVIDIA/numba-cuda-mlir/pull/420) Lower cuda.lanemask_lt() by reading the %lanemask_lt special register |
| **[NVIDIA numba-cuda-mlir](https://github.com/NVIDIA/numba-cuda-mlir)** | 74 | [#374](https://github.com/NVIDIA/numba-cuda-mlir/pull/374) Lower integer constants of 2\*\*63 or more as their two's complement |

</details>

<p align="center"><a href="https://github.com/pulls?q=is%3Apr+author%3Aadimalkar+-user%3Aadimalkar+-user%3Ahiringfleet+is%3Amerged"><img src="https://img.shields.io/badge/GitHub-All_18_merged_open_source_PRs-238636?style=for-the-badge&logo=github&logoColor=white" alt="All merged open source PRs" /></a></p>
<!-- END_SECTION:contributions -->

<br>

## Tech Stack

<table>
  <tr>
    <td><b>Languages</b></td>
    <td>
      <img src="https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54" alt="Python"/>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
      <img src="https://img.shields.io/badge/JavaScript-323330?style=flat-square&logo=javascript&logoColor=F7DF1E" alt="JavaScript"/>
      <img src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white" alt="SQL"/>
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5"/>
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3"/>
      <img src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white" alt="R"/>
    </td>
  </tr>
  <tr>
    <td><b>ML & AI</b></td>
    <td>
      <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
      <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
      <img src="https://img.shields.io/badge/LangChain-121212?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain"/>
      <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face"/>
      <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
      <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV"/>
      <img src="https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white" alt="Spark"/>
    </td>
  </tr>
  <tr>
    <td><b>Frameworks</b></td>
    <td>
      <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React"/>
      <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js"/>
      <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js"/>
      <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
    </td>
  </tr>
  <tr>
    <td><b>Data</b></td>
    <td>
      <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis"/>
      <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB"/>
      <img src="https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white" alt="Celery"/>
    </td>
  </tr>
  <tr>
    <td><b>Infrastructure</b></td>
    <td>
      <img src="https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazon-aws&logoColor=white" alt="AWS"/>
      <img src="https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="GCP"/>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
      <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes"/>
      <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions"/>
      <img src="https://img.shields.io/badge/OpenTelemetry-F54C00?style=flat-square&logo=opentelemetry&logoColor=white" alt="OpenTelemetry"/>
      <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux"/>
    </td>
  </tr>
</table>

<br>

## Highlights

### 📄 Termnova — *AI Contract Intelligence Platform*
Engineered an enterprise-grade contract analysis platform utilizing **LangGraph multi-agent orchestration** and **Hybrid RAG** (dense vector embeddings combined with sparse BM25 reranking). Implemented asynchronous ingestion queues with Celery, end-to-end distributed tracing via **OpenTelemetry**, and strict quantitative RAG evaluation metrics (`faithfulness`, `context precision`, `hallucination scoring`) to audit complex legal agreements with deterministic precision.

### 🏆 Multimodal Fraud Detector (FraudSight AI) — *Hackathon Winner*
Won 1st place in a Databricks Hackathon by designing a **Vision-Critic multi-model jury architecture** for insurance claim fraud detection. Visual forensic analysis (OpenCV keyframe extraction and metadata artifact detection) was strictly decoupled from logical LLM deduction to eliminate decision contamination. Built weighted heuristic risk-scoring models that evaluate cross-modal signals across video, images, and transaction metadata.

### ⚡ Low-Latency Real-Time Speech-to-Speech Translation
Architected a concurrent, low-latency audio translation pipeline using a producer-consumer threaded design across **Whisper (ASR)**, **MarianMT (Neural Translation)**, and **Meta MMS (TTS)**. Achieved `<3ms` Voice Activity Detection latency with Silero VAD, sub-3s end-to-end latency, and dynamic gain-normalization filters to eliminate background static.

### 🔬 Distributed Medical Vision (`Diabetic Retinopathy Classification`)
Developed a distributed medical computer vision pipeline on **Google Cloud Platform (GCP)** leveraging **PySpark and Spark ML** for large-scale fundus image preprocessing. Applied PyTorch deep neural networks with custom **CLAHE (Contrast Limited Adaptive Histogram Equalization)** contrast-enhancement algorithms to classify diabetic retinopathy severity while preserving critical microvascular pathology.

<br>

## Certifications

<p align="center">
  <a href="https://www.credly.com/badges/4918c215-64ad-4064-9876-4b8a22908df0/public_url"><img src="https://images.credly.com/size/340x340/images/4d4693bb-530e-4bca-9327-de07f3aa2348/image.png" alt="AWS Certified AI Practitioner" width="150"/></a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.credly.com/badges/2fa341b2-fd74-44e7-a3e6-779b30db9992/public_url"><img src="https://images.credly.com/size/340x340/images/1a634b4e-3d6b-4a74-b118-c0dcb429e8d2/image.png" alt="AWS Certified ML Engineer – Associate" width="150"/></a>
</p>

<br>

## GitHub Analytics

<p align="center">
  <a href="https://github.com/ryo-ma/github-profile-trophy">
    <img src="https://github-trophies.devomb.com/?username=adimalkar&theme=darkhub&no-frame=true&no-bg=true&column=-1&margin-w=15&margin-h=15&rank=-?" alt="trophy" />
  </a>
</p>

<p align="center">
  <img src="top-langs.svg" height="195" alt="Most Used Languages" />&nbsp;&nbsp;
  <img src="https://github-readme-streak-stats-eight.vercel.app/?user=adimalkar&theme=tokyonight&hide_border=true" height="195" alt="Contribution Streak" />
</p>

<p align="center">
  <img src="https://gh-readme-activity-graph.vercel.app/graph?username=adimalkar&theme=react-dark&hide_border=true&area=true" width="100%" alt="Aditya's GitHub Activity Graph" />
</p>

<br>

<div align="center">
  <i>"In God we trust, all others must bring data." — W. Edwards Deming</i>
  <br><br>
  <a href="https://www.adityamalkar.com"><b>adityamalkar.com</b></a>
</div>