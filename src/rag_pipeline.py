from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def create_rag_chain(retriever):
    llm = ChatOpenAI(model="gpt-4", temperature=0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain