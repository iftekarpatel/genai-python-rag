from ai_client import AIClient
from rag.semantic_search import SemanticSearch


class RAGChatService:
    def __init__(self):
        self.ai = AIClient()
        self.search = SemanticSearch()

    def ask(self, user_query):
        retrieved_docs = self.search.search(user_query)

        context = "\n\n".join(retrieved_docs)

        system_prompt = f"""
You are an assistant who answers questions only from provided context.

Context:
{context}

If answer not found, use your existing knowledge.
"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]

        response = self.ai.chat(messages)

        return response.choices[0].message.content