from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from guardrails import validate_output
from ingestion import create_vector_db
from rag_pipeline import create_rag_chain
from retriever import get_retriever


PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATIC_DIR = PROJECT_ROOT / "static"

app = FastAPI(title="Om Singh Bisen Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

rag_chain = None


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


def get_rag_chain():
    global rag_chain
    if rag_chain is None:
        create_vector_db()
        retriever = get_retriever()
        rag_chain = create_rag_chain(retriever)

    return rag_chain


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    question = request.question.strip()
    if not question:
        return ChatResponse(answer="Ask me something about Om's skills, projects, education, or career profile.")

    result = get_rag_chain()(question)
    validated = validate_output(result["result"], result["source_documents"])
    return ChatResponse(answer=validated.answer)


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
