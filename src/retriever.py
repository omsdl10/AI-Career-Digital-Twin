from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from ingestion import load_documents


class LocalDocumentRetriever:
    def __init__(self, documents, k=5):
        self.documents = documents
        self.k = k
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(
            doc.page_content for doc in documents
        )

    def invoke(self, query):
        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix).ravel()
        ranked_indexes = scores.argsort()[::-1][:self.k]

        ranked_docs = []
        for index in ranked_indexes:
            doc = self.documents[index]
            doc.metadata["score"] = float(scores[index])
            ranked_docs.append(doc)

        return ranked_docs


def get_retriever():
    return LocalDocumentRetriever(load_documents(), k=5)
