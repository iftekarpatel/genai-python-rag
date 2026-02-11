from rag.vector_store import VectorStore


class SemanticSearch:
    def __init__(self):
        self.vector_store = VectorStore()

    def search(self, query):
        results = self.vector_store.search(query)
        documents = results["documents"][0]
        return documents