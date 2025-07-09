# agents/response_agent.py

import groq
from core.mcp import MCPMessage, MCPBus

class LLMResponseAgent:
    def __init__(self, bus: MCPBus, groq_api_key: str):
        self.name = "LLMResponseAgent"
        self.bus = bus
        self.client = groq.Groq(api_key=groq_api_key)
    
    def receive_message(self, message):
        if message.type == "RETRIEVAL_RESULT":
            query = message.payload["query"]
            chunks = message.payload["retrieved_context"]
            self.generate_response(query, chunks, message.trace_id)


    def generate_response(self, query: str, context_chunks: list, trace_id: str):
        context = "\n".join(context_chunks)
        prompt = f"Answer the following question using the context below:\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"

        response = self.client.chat.completions.create(
            model="llama3-8b-8192",  # or llama3-70b-8192
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        final_answer = response.choices[0].message.content.strip()

        message = MCPMessage(
            sender=self.name,
            receiver="CoordinatorAgent",
            type="LLM_RESPONSE",
            trace_id=trace_id,
            payload={"answer": final_answer, "sources": context_chunks}
        )
        self.bus.send_message(message)
