import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from openai import APIConnectionError, AuthenticationError, NotFoundError, OpenAIError


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

PROMPT = ChatPromptTemplate.from_template(
    """You are Om Singh Bisen's personal RAG career assistant.

Your job:
- Answer using Om's retrieved personal context: resume, skills, projects, education, and achievements.
- Personalize every answer to Om's actual background.
- When giving advice, connect it to evidence from the context.
- If the question asks for missing skills or next steps, recommend practical additions.
- Do not invent facts about Om that are not in the context.
- Keep the answer direct, useful, and structured.

Context:
{context}

Question:
{question}
"""
)


def _format_docs(docs):
    formatted_docs = []
    for index, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "personal data")
        formatted_docs.append(f"[Source {index}: {source}]\n{doc.page_content}")

    return "\n\n".join(formatted_docs)


def _local_answer(query, docs):
    context = _format_docs(docs)
    query_lower = query.lower()

    if "skill" in query_lower or "learn" in query_lower:
        return (
            "Based on your personal data, you already have a good base in Python, "
            "RAG, LangChain, scikit-learn, NLP, Django, React, REST APIs, SQL, Git, Linux, "
            "and core CS subjects.\n\n"
            "For AI roles, your next best skills are:\n"
            "1. Deep learning with PyTorch or TensorFlow.\n"
            "2. LLM application development: agents, evaluation, tool calling, and prompt testing.\n"
            "3. Vector databases and retrieval evaluation beyond basic RAG.\n"
            "4. MLOps basics: model serving, monitoring, Docker, and deployment.\n"
            "5. Stronger math for ML: linear algebra, probability, and optimization.\n\n"
            "A strong next project would be an end-to-end LLM app with evaluation, authentication, "
            "deployment, and clear metrics, because it connects well with your AI Career Digital Twin "
            "and full-stack background."
        )

    if "project" in query_lower:
        return (
            "Your strongest existing projects for AI/full-stack roles are:\n"
            "1. AI Career Digital Twin: this is the most directly relevant AI project because it uses "
            "LangChain, RAG, LLMs, intent classification, retrieval, guardrails, and confidence scoring.\n"
            "2. Raspberry Pi System Monitoring Dashboard: this shows Python, Django, Linux, system metrics, "
            "real-time monitoring, and practical engineering depth.\n\n"
            "To make your portfolio stronger, upgrade the AI Career Digital Twin with resume upload, "
            "source citations, RAG evaluation, deployment, and a clean architecture diagram. That will "
            "make it feel like a complete AI engineering project rather than only a demo."
        )

    return (
        "Based on your personal data, you are positioned well for AI/ML engineering and full-stack AI roles. "
        "You have Python, RAG, LangChain, scikit-learn, Django, React, SQL, and strong core CS foundations, "
        "plus projects that show applied AI and web engineering.\n\n"
        "Best next steps:\n"
        "1. Deepen one AI specialization: LLM apps/RAG, ML systems, or data science.\n"
        "2. Add one production-grade project with deployment, metrics, and a clean README.\n"
        "3. Prepare project stories around problem, architecture, tradeoffs, and measurable impact.\n"
        "4. Keep DSA sharp for interviews while building stronger ML fundamentals.\n\n"
        f"Profile context used:\n{context}"
    )


def _error_answer(error, docs):
    if isinstance(error, AuthenticationError):
        reason = "The OpenAI API key was rejected. Check that the key is active and has API access."
    elif isinstance(error, APIConnectionError):
        reason = "The app could not connect to the OpenAI API from this environment."
    elif isinstance(error, NotFoundError):
        reason = "The selected OpenAI model is not available for this API key."
    else:
        reason = "The OpenAI request failed."

    return f"{reason}\n\nUsing local career guidance instead:\n\n"


class RetrievalQACompat:
    def __init__(self, retriever):
        self.retriever = retriever
        self.chain = None

    def _get_chain(self):
        if self.chain is None:
            llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0, timeout=8)
            self.chain = PROMPT | llm | StrOutputParser()

        return self.chain

    def __call__(self, query):
        docs = self.retriever.invoke(query)
        try:
            answer = self._get_chain().invoke({
                "context": _format_docs(docs),
                "question": query,
            })
        except OpenAIError as error:
            answer = _error_answer(error, docs) + _local_answer(query, docs)

        return {
            "result": answer,
            "source_documents": docs,
        }


def create_rag_chain(retriever):
    return RetrievalQACompat(retriever)
