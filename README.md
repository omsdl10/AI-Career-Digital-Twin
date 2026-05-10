# AI Career Digital Twin 2025

An animated AI/ML portfolio website with an embedded personal RAG chatbot. The assistant answers questions using verified details from Om Singh Bisen's resume, skills, projects, education, and achievements.

---

## 🚀 Overview

AI Career Digital Twin simulates a **personal career mentor** by leveraging structured personal data and combining it with modern AI techniques like **retrieval-augmented generation, local document retrieval, and grounded response generation**.

Unlike generic chatbots, this system provides **profile-aware responses** grounded in project and resume context. The website also acts as a polished portfolio for AI/ML engineering roles.

---

## ✨ Key Features

* **RAG Pipeline**
  Retrieves relevant information from structured documents to ensure grounded responses

* **Animated Portfolio Website**
  Custom FastAPI-served HTML/CSS/JS portfolio inspired by bold editorial design

* **Personal Chatbot**
  Answers questions about skills, projects, education, resume fit, and interview profile

* **Local Retrieval**
  Uses TF-IDF similarity search over personal text data for retrieval

* **AI Guardrails**

  * Structured output validation (Pydantic)
  * Confidence scoring system

* **FastAPI Backend**
  Provides the website and `/api/chat` endpoint

---

## 🏗️ Tech Stack

| Category      | Technology           |
| ------------- | -------------------- |
| Language      | Python               |
| LLM Framework | LangChain            |
| Retrieval     | scikit-learn TF-IDF  |
| LLM Provider  | OpenAI               |
| Backend       | FastAPI / Uvicorn    |
| Frontend      | HTML, CSS, JavaScript |
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
│   ├── app.py              # FastAPI backend and API routes
│   ├── ingestion.py       # Data loading & chunking
│   ├── retriever.py       # Local document retrieval
│   ├── classifier.py      # Intent classification
│   ├── rag_pipeline.py    # RAG logic
│   ├── guardrails.py      # Validation & scoring
│   ├── main.py            # CLI interface
│
├── static/
│   ├── index.html         # Animated portfolio page
│   ├── styles.css         # Visual design and animations
│   ├── script.js          # Chat UI and neural canvas animation
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/omsdl10/AI-Career-Digital-Twin.git
cd AI-Career-Digital-Twin
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
cd src
uvicorn app:app --host 127.0.0.1 --port 8501
```

Open `http://127.0.0.1:8501` in your browser.

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
FastAPI /api/chat
   ↓
Local Retriever
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
