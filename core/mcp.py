# core/mcp.py

from dataclasses import dataclass
from typing import Dict

@dataclass
class MCPMessage:
    sender: str
    receiver: str
    type: str
    trace_id: str
    payload: Dict

class MCPBus:
    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent):
        self.agents[name] = agent

    def send_message(self, message: MCPMessage):
        receiver = self.agents.get(message.receiver)
        if receiver:
            receiver.receive_message(message)
        else:
            print(f"[MCPBus] No such receiver: {message.receiver}")
