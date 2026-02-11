from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from rag.chat_service import RAGChatService
from rag.ingest import DocumentIngestor

app = FastAPI()
rag_service = RAGChatService()

# Ingest on startup
@app.on_event("startup")
def startup_event():
    ingestor = DocumentIngestor()
    ingestor.ingest()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>Python RAG Chat</h2>
    <form action="/ask" method="get">
        <input name="q" style="width:300px"/>
        <button type="submit">Ask</button>
    </form>
    """


@app.get("/ask")
def ask(q: str):
    answer = rag_service.ask(q)
    return {"answer": answer}