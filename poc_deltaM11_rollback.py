# ΔM11.3 rollback guard (toy proxy)
import random, sys
samples = [random.random() for _ in range(16)]
stability = 1 - min(1.0, (max(samples)-min(samples)))
if stability < 0.55:
    print("ROLLBACK")
    sys.exit(1)
print("STABLE")