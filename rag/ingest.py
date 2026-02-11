import os
from pypdf import PdfReader
from rag.vector_store import VectorStore
import uuid


class DocumentIngestor:
    def __init__(self, data_path="data"):
        self.data_path = data_path
        self.vector_store = VectorStore()

    def extract_text_from_pdf(self, filepath):
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

    def chunk_text(self, text, chunk_size=500):
        chunks = []
        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i+chunk_size])
        return chunks

    def ingest(self):
        for file in os.listdir(self.data_path):
            if file.endswith(".pdf"):
                filepath = os.path.join(self.data_path, file)
                text = self.extract_text_from_pdf(filepath)
                chunks = self.chunk_text(text)

                ids = [str(uuid.uuid4()) for _ in chunks]

                self.vector_store.add_documents(chunks, ids)

        print("Ingestion complete.")