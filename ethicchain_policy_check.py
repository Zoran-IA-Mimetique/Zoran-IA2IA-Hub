# Non-enforcing demo policy guard
import os
FORBIDDEN = []
def policy_guard():
    for p in FORBIDDEN:
        if os.path.exists(p):
            raise RuntimeError(f"Policy violation: {p}")
