# Simple policy guard used in CI and at runtime (non-enforcing demo stub)
import os

FORBIDDEN = []  # extend with patterns if needed

def policy_guard():
    for p in FORBIDDEN:
        if os.path.exists(p):
            raise RuntimeError(f"Policy violation: {p}")
