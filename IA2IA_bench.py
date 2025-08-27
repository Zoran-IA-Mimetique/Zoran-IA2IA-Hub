# Minimal interop bench: validates schema presence and runs a tiny pipeline
import json, time, random, pathlib
from orchestrator import Orchestrator
from memory import FractalMemory

def run():
    mem = FractalMemory()
    orch = Orchestrator(memory=mem)
    ds = pathlib.Path("datasets/ia2ia_messages.jsonl").read_text(encoding="utf-8").splitlines()
    ok = 0
    t0 = time.time()
    for line in ds:
        msg = json.loads(line)
        try:
            orch.process(msg)
            ok += 1
        except AssertionError:
            pass
    dt = time.time() - t0
    print({"parsed": ok, "latency_s": round(dt, 6)})

if __name__ == "__main__":
    run()
