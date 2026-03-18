# 🤖 AI Career Digital Twin 2025

An intelligent, personalized AI career assistant built using **LangChain, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs)** to deliver grounded, context-aware career guidance.

---

## 🚀 Overview

AI Career Digital Twin simulates a **personal career mentor** by leveraging your own data (resume, skills, projects) and combining it with modern AI techniques like **RAG pipelines and intent classification**.

Unlike generic chatbots, this system provides **fact-based, explainable responses** with reduced hallucination.

---

## ✨ Key Features

* 🔍 **RAG Pipeline**
  Retrieves relevant information from structured documents to ensure grounded responses

* 🧠 **Intent Classification**
  Supports multiple query types:

  * Career Planning
  * Skill Matching
  * Project Recommendations

* 📄 **Semantic Search (Vector DB)**
  Uses embeddings + similarity search for accurate document retrieval

* 🛡️ **AI Guardrails**

  * Structured output validation (Pydantic)
  * Confidence scoring system

* 💬 **ChatGPT-like UI (Streamlit)**
  Interactive chat interface with session-based memory

* 📊 **Explainability**
  Displays retrieved source documents for transparency

---

## 🏗️ Tech Stack

| Category      | Technology           |
| ------------- | -------------------- |
| Language      | Python               |
| LLM Framework | LangChain            |
| Vector DB     | ChromaDB             |
| Embeddings    | OpenAI / HuggingFace |
| UI            | Streamlit            |
| Validation    | Pydantic             |

---

## 📁 Project Structure

```
ai-career-digital-twin/
│
├── data/
│   ├── resume.txt
│   ├── skills.txt
│   ├── projects.txt
│
├── src/
│   ├── app.py              # Streamlit UI
│   ├── ingestion.py       # Data loading & chunking
│   ├── retriever.py       # Vector retrieval
│   ├── classifier.py      # Intent classification
│   ├── rag_pipeline.py    # RAG logic
│   ├── guardrails.py      # Validation & scoring
│   ├── main.py            # CLI interface
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-career-digital-twin.git
cd ai-career-digital-twin
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run the Application

```bash
streamlit run src/app.py
```

---

## 💡 Example Queries

* “What skills should I learn for AI roles?”
* “Suggest projects for machine learning”
* “How can I transition to data science?”

---

## 🧠 System Architecture

```
User Query
   ↓
Intent Classifier
   ↓
Retriever (Vector Database)
   ↓
RAG Pipeline (LangChain)
   ↓
LLM Response Generation
   ↓
Output Validation + Confidence Score
```

---

## 📊 Key Achievements

* Reduced hallucination using **grounded RAG responses**
* Processed **100+ document chunks**
* Designed **multi-stage retrieval pipeline**
* Implemented **production-ready guardrails**

---

## 🔮 Future Improvements

* 📄 Resume PDF upload & parsing
* 🧠 Conversational memory (context-aware chat)
* ⚡ FastAPI backend deployment
* 🐳 Docker containerization
* ☁️ Cloud deployment (AWS / Render)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

