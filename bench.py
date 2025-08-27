# Minimal interop bench
import json, time, pathlib
from orchestrator import Orchestrator
from memory import FractalMemory

def run():
    mem = FractalMemory()
    orch = Orchestrator(memory=mem)
    lines = pathlib.Path("ia2ia_messages.jsonl").read_text(encoding="utf-8").splitlines()
    ok, t0 = 0, time.time()
    for line in lines:
        msg = json.loads(line)
        try:
            orch.process(msg); ok += 1
        except AssertionError:
            pass
    dt = time.time() - t0
    print({"parsed": ok, "latency_s": round(dt, 6)})

if __name__ == "__main__":
    run()
