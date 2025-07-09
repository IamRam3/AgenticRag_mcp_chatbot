# agents/retrieval_agent.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from core.mcp import MCPMessage, MCPBus

class RetrievalAgent:
    def __init__(self, bus: MCPBus):
        self.name = "RetrievalAgent"
        self.bus = bus
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.text_chunks = []

    def store_chunks(self, chunks: list):
        self.text_chunks = chunks
        embeddings = self.model.encode(chunks)
        self.index.add(np.array(embeddings, dtype=np.float32))

    def receive_message(self, message):
        if message.type == "PARSED_CHUNKS":
            chunks = message.payload["chunks"]
            self.store_chunks(chunks)

    def retrieve(self, query: str, top_k=5, trace_id=""): 
        query_vec = self.model.encode([query])
        D, I = self.index.search(np.array(query_vec, dtype=np.float32), top_k)
        top_chunks = [self.text_chunks[i] for i in I[0] if i < len(self.text_chunks)]

        message = MCPMessage(
            sender=self.name,
            receiver="LLMResponseAgent",
            type="RETRIEVAL_RESULT",
            trace_id=trace_id,
            payload={"retrieved_context": top_chunks, "query": query}
        )
        self.bus.send_message(message)
