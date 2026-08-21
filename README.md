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
| **[Termnova](https://github.com/adimalkar/termnova)** | Production-grade AI contract intelligence platform with hybrid RAG, LangGraph multi-agent workflows, OpenTelemetry tracing, and hallucination guardrails. |
| **[Alpha-Aware Hierarchical RL](https://github.com/adimalkar/alpha-aware-hrl)** | Autonomous trading agents in ABIDES limit order book simulations studying market microstructures and regime classification. |
| **[Supplier Intelligence Platform](https://github.com/adimalkar/supplier-intelligence-platform)** | Multi-source B2B intelligence engine extracting supplier risk signals, financial health indicators, and market trends. |
| **[AI DOM-Autofill Extension](https://github.com/adimalkar/Autofill-Extension)** | Browser automation engine bypassing ATS limitations via recursive Shadow DOM traversal and React synthetic event dispatcher overrides. |

<br>

## Tech Stack

<table>
  <tr>
    <td><b>Languages</b></td>
    <td>
      <img src="https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54" alt="Python"/>
      <img src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white" alt="SQL"/>
      <img src="https://img.shields.io/badge/JavaScript-323330?style=flat-square&logo=javascript&logoColor=F7DF1E" alt="JavaScript"/>
      <img src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white" alt="R"/>
    </td>
  </tr>
  <tr>
    <td><b>ML & AI</b></td>
    <td>
      <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
      <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
      <img src="https://img.shields.io/badge/LangChain-121212?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain"/>
      <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
      <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV"/>
    </td>
  </tr>
  <tr>
    <td><b>Infrastructure</b></td>
    <td>
      <img src="https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazon-aws&logoColor=white" alt="AWS"/>
      <img src="https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="GCP"/>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
      <img src="https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white" alt="Spark"/>
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
  <img src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs?username=adimalkar&layout=compact&theme=tokyonight&hide_border=true&hide=Jupyter%20Notebook&langs_count=8" height="195" alt="Most Used Languages" />&nbsp;&nbsp;
  <img src="https://github-readme-streak-stats-eight.vercel.app/?user=adimalkar&theme=tokyonight&hide_border=true" height="195" alt="Contribution Streak" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=adimalkar&theme=react-dark&hide_border=true&area=true" width="100%" alt="Aditya's GitHub Activity Graph" />
</p>

<br>

<div align="center">
  <i>"In God we trust, all others must bring data." — W. Edwards Deming</i>
  <br><br>
  <a href="https://www.adityamalkar.com"><b>adityamalkar.com</b></a>
</div>