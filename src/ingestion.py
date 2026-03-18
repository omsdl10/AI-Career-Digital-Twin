from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def load_and_split(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)

def create_vector_db():
    files = ["data/resume.txt", "data/skills.txt", "data/projects.txt"]

    all_docs = []
    for file in files:
        all_docs.extend(load_and_split(file))

    db = Chroma.from_documents(
        all_docs,
        embedding=OpenAIEmbeddings(),
        persist_directory="db"
    )

    db.persist()
    return db