from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DATA_FILES = ["resume.txt", "skills.txt", "projects.txt"]


def load_and_split(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120
    )

    chunks = splitter.split_documents(documents)
    for chunk in chunks:
        chunk.metadata["source"] = Path(file_path).name

    return chunks


def create_vector_db():
    return load_documents()


def load_documents():
    all_docs = []
    for file in DATA_FILES:
        all_docs.extend(load_and_split(DATA_DIR / file))

    return all_docs
