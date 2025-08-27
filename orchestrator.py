from typing import Dict, List
from memory import FractalMemory

class Orchestrator:
    def __init__(self, memory: FractalMemory):
        self.memory = memory
        self.processed: List[Dict] = []

    def process(self, msg: Dict):
        assert {"id","role","content"} <= msg.keys(), "Invalid IA2IA message"
        msg = dict(msg)
        msg["checkpoint"] = self.memory.checkpoint(msg["id"])
        self.processed.append(msg)
        return msg

    def report(self) -> Dict:
        return {"count": len(self.processed), "last_checkpoint": self.processed[-1]["checkpoint"] if self.processed else None}
