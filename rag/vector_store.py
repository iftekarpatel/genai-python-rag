import chromadb
from chromadb.utils.embedding_functions import EmbeddingFunction
from openai import OpenAI
from config import GITHUB_TOKEN, GITHUB_ENDPOINT


class GitHubEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.client = OpenAI(
            api_key=GITHUB_TOKEN,
            base_url=GITHUB_ENDPOINT
        )

    def __call__(self, texts):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        return [item.embedding for item in response.data]

    def name(self) -> str:
        return "github_openai_embedding"


class VectorStore:
    def __init__(self):
        self.client = chromadb.Client(
            settings=chromadb.Settings(
                persist_directory="./vector_db",
                is_persistent=True
            )
        )

        self.embedding_function = GitHubEmbeddingFunction()

        self.collection = self.client.get_or_create_collection(
            name="rag_docs",
            embedding_function=self.embedding_function
        )

    def add_documents(self, documents, ids):
        self.collection.add(
            documents=documents,
            ids=ids
        )

    def search(self, query, k=3):
        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )
        return results