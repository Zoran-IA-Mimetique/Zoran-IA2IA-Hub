import hashlib, time

class FractalMemory:
    def __init__(self):
        self.state = {}
    def checkpoint(self, key: str) -> str:
        h = hashlib.sha256(f"{key}:{int(time.time())}".encode()).hexdigest()[:12]
        self.state[key] = h
        return h
