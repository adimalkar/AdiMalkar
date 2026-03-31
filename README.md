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
| **Agentic AI Policy Navigator** | Multi-agent system using LangGraph, FastAPI, and Pinecone to navigate policy frameworks, resolve compliance conflicts, and generate impact assessments via specialized RAG pipelines. |
| **AI DOM-Autofill Extension** | Browser extension that bypasses ATS security limitations through recursive Shadow DOM traversal, React/Vue native setter bypass, and async form observation via `MutationObserver`. |
| **Alpha-Aware Hierarchical RL** | Training autonomous trading agents within the ABIDES limit order book simulator to study market microstructures and regime classification. |
| **Neural Data Compression** | Researching lossy and lossless compression architectures for high-fidelity images and video. |

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
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
      <img src="https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white" alt="Spark"/>
      <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux"/>
    </td>
  </tr>
</table>

<br>

## Highlights

### 🏆 FraudSight AI — *Hackathon Winner*
Won a hackathon by building something I hadn't seen done before: a Vision-Critic pipeline where four separate models act as a "jury" for insurance fraud detection. The idea was to completely separate the visual forensic analysis (extracting and examining keyframes with OpenCV) from the logical deduction step, so neither could contaminate the other's judgment. Each model votes independently, and the system only flags fraud when there's consensus. It was a wild 48 hours but the approach held up under the judges' stress-testing.

### ⚡ Real-Time Speech-to-Speech Translation
This one started as a class project and turned into something I'm genuinely proud of. I built a concurrent translation pipeline using a producer-consumer threaded architecture — Whisper handles the speech recognition, MarianMT does translation, and Meta's MMS-TTS generates the output speech. The hardest part wasn't any single model; it was getting them to pipeline together without blowing up latency. Ended up hitting `<3ms` frame latency on the Voice Activity Detection stage using Silero VAD, and the full pipeline runs at ~2.8s depth. Also had to build custom hallucination filters because Whisper likes to make things up when it hears silence.

### 🔍 Financial Data Integrity Analysis
I ran a quantitative backtest comparing Yahoo Finance data against CRSP (the gold standard in academic finance) because I kept seeing people build trading strategies on free API data without questioning it. Turns out, survivorship bias in free data sources creates a **41.5% variance** in annualized returns compared to clean institutional data. That's not a rounding error — it's the difference between a strategy that looks profitable and one that isn't. Published the methodology and findings to help other researchers avoid the same trap.

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
    <img src="https://github-profile-trophy-kannan.vercel.app/?username=adimalkar&theme=darkhub&no-frame=true&no-bg=true&column=-1&margin-w=15&margin-h=15&rank=-?" alt="trophy" />
  </a>
</p>

<p align="center">
  <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=adimalkar&layout=compact&theme=transparent&hide_border=true&title_color=1F6FEB&text_color=777777&langs_count=6" height="180" alt="Top Langs" /><img src="https://streak-stats.demolab.com/?user=adimalkar&theme=transparent&hide_border=true&title_color=1F6FEB&text_color=777777&sideNums=777777&sideLabels=777777&ring=1F6FEB&currStreakLabel=1F6FEB&hide_current_streak=true&hide_longest_streak=true&card_width=250" height="180" alt="Total Contributions" />
</p>

<br>

<div align="center">
  <i>"In God we trust, all others must bring data." — W. Edwards Deming</i>
  <br><br>
  <a href="https://www.adityamalkar.com"><b>adityamalkar.com</b></a>
</div>
