# agents/coordinator_agent.py

from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.response_agent import LLMResponseAgent
from core.mcp import MCPBus
import os

class CoordinatorAgent:
    def __init__(self):
        self.bus = MCPBus()
        self.ingestion_agent = IngestionAgent(self.bus)
        self.retrieval_agent = RetrievalAgent(self.bus)
        self.response_agent = LLMResponseAgent(self.bus, groq_api_key = os.getenv("GROQ_API_KEY"))
        self.trace_id = "session-1"

    def launch(self):
        self.bus.register_agent("IngestionAgent", self.ingestion_agent)
        self.bus.register_agent("RetrievalAgent", self.retrieval_agent)
        self.bus.register_agent("LLMResponseAgent", self.response_agent)
        self.bus.register_agent("CoordinatorAgent", self)

    def handle_file_upload(self, file_paths: list):
        self.ingestion_agent.ingest_files(file_paths, self.trace_id)

    def handle_question(self, question: str):
        self.retrieval_agent.retrieve(query=question, trace_id=self.trace_id)

    def receive_message(self, message):
        if message.type == "LLM_RESPONSE":
            self.last_answer = message.payload

    def get_last_answer(self):
        return getattr(self, "last_answer", None)
