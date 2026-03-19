from ingestion import create_vector_db
from retriever import get_retriever
from classifier import classify_intent
from rag_pipeline import create_rag_chain
from guardrails import validate_output

def run():
    print("Initializing AI Career Digital Twin...")

    create_vector_db()
    retriever = get_retriever()
    rag_chain = create_rag_chain(retriever)

    while True:
        query = input("\nAsk your career assistant: ")

        intent = classify_intent(query)
        print(f"[Intent]: {intent}")

        result = rag_chain(query)

        answer = result["result"]
        sources = result["source_documents"]

        validated = validate_output(answer, sources)

        print("\nAnswer:", validated.answer)
        print("Confidence:", validated.confidence)

if __name__ == "__main__":
    run()