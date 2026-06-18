# Multi-Agent Research System 🔬

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![LangChain](https://img.shields.io/badge/LangChain-Agentic-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen)

An AI-powered research assistant that automates information gathering, content extraction, report generation, and quality evaluation through a multi-agent pipeline.

Built with **LangChain**, **Groq**, **Tavily**, and **Streamlit**.

---

## Overview

This project orchestrates specialized LLM agents to perform research tasks sequentially. Given a topic, the system searches the web, extracts relevant information, generates a structured report, and evaluates the quality of the generated output.

### Pipeline Components

* **Search Tool** — Retrieves relevant information using Tavily.
* **Reader Agent** — Extracts and analyzes content from web pages.
* **Writer Agent** — Produces a structured research report.
* **Critic Agent** — Evaluates the report and provides feedback with a quality score.

---

## Architecture

```text
                    ┌──────────────┐
                    │ User Topic   │
                    └──────┬───────┘
                           │
                           ▼
                ┌────────────────────┐
                │   Tavily Search     │
                │       Tool          │
                └─────────┬───────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    Reader Agent    │
                │ Content Extraction │
                │ Information Parsing│
                └─────────┬───────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    Writer Agent    │
                │ Report Generation  │
                └─────────┬───────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    Critic Agent    │
                │ Quality Evaluation │
                │ Feedback & Scoring │
                └────────────────────┘
```

---

## Features

* Multi-agent research pipeline
* Real-time web search with Tavily
* Web content extraction using BeautifulSoup4 and Trafilatura
* AI-generated research reports
* Automated report evaluation and scoring
* Interactive Streamlit interface
* Fast inference powered by Groq

---

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
└── src
    ├── agents
    │   ├── agents.py
    │   └── __init__.py
    ├── pipeline
    │   ├── pipeline.py
    │   └── __init__.py
    └── tools
        ├── tools.py
        └── __init__.py
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/abhi6174/Multiagentic-research-system.git

cd Multiagentic-research-system
```

### Create a Conda Environment

```bash
conda create -n research python=3.11 -y

conda activate research
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Example Usage

```python
from src.pipeline.pipeline import run_research_pipeline

topic = "Artificial Intelligence in Healthcare"

results = run_research_pipeline(topic)

print(results["report"])
print(results["Evaluation"])
```

---

## Workflow

```text
Input Topic
     │
     ▼
Web Search
     │
     ▼
Content Extraction
     │
     ▼
Report Generation
     │
     ▼
Quality Evaluation
     │
     ▼
Final Output
```

---

## Tech Stack

| Category           | Technologies                |
| ------------------ | --------------------------- |
| LLM Framework      | LangChain                   |
| LLM Provider       | Groq                        |
| Search             | Tavily                      |
| Content Extraction | BeautifulSoup4, Trafilatura |
| Frontend           | Streamlit                   |
| Environment        | python-dotenv               |
| Utilities          | Requests, Rich              |

---

## Roadmap

* [ ] Parallel agent execution
* [ ] Source citation support
* [ ] PDF and Markdown export
* [ ] Iterative report refinement
* [ ] Multi-LLM support
* [ ] Long-term memory integration

---

## License

This project is licensed under the **Apache License 2.0**.

See the `LICENSE` file for details.

---

## Acknowledgements

* LangChain
* Groq
* Tavily
* Streamlit
* BeautifulSoup4
* Trafilatura

---

⭐ If you found this project useful, consider giving it a star.
