import argparse
from orchestrator import Orchestrator
from memory import FractalMemory
from ethicchain_policy_check import policy_guard

def demo():
    mem = FractalMemory()
    orch = Orchestrator(memory=mem)
    msgs = [
        {"id":"m1","role":"system","content":"Init ΔM11.3"},
        {"id":"m2","role":"agent","content":"Hello from agent A"},
        {"id":"m3","role":"agent","content":"Ack from agent B"}
    ]
    for m in msgs:
        orch.process(m)
    print("✓ Demo complete:", orch.report())

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()
    policy_guard()
    if args.demo:
        demo()
    else:
        print("Use --demo to run the quick demo.")
