from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def get_retriever():
    db = Chroma(
        persist_directory="db",
        embedding_function=OpenAIEmbeddings()
    )

    return db.as_retriever(search_kwargs={"k": 3})