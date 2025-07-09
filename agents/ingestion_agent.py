# agents/ingestion_agent.py

import os
from core.utils import parse_file
from core.mcp import MCPMessage, MCPBus

class IngestionAgent:
    def __init__(self, bus: MCPBus):
        self.name = "IngestionAgent"
        self.bus = bus

    def ingest_files(self, file_paths: list, trace_id: str):
        all_chunks = []
        for path in file_paths:
            ext = os.path.splitext(path)[1].lower()
            chunks = parse_file(path, ext)
            all_chunks.extend(chunks)

        message = MCPMessage(
            sender=self.name,
            receiver="RetrievalAgent",
            type="PARSED_CHUNKS",
            trace_id=trace_id,
            payload={"chunks": all_chunks}
        )
        self.bus.send_message(message)
