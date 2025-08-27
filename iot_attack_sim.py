
import random, json, pathlib

# Simulate IoT devices under attack, rollback ΔM11.3 if instability triggered
devices = [{"id":i,"status":"ok"} for i in range(10)]
attacks = 0
for d in devices:
    if random.random()<0.3:
        d["status"] = "compromised"
        attacks+=1

instability = attacks/len(devices)
rollback_triggered = instability>0.25

out = {"devices":devices,"instability":instability,"rollback_delta_m11_3":rollback_triggered}
print(json.dumps(out, indent=2))
(pathlib.Path(__file__).parent/"results"/"report.md").write_text(json.dumps(out, indent=2), encoding="utf-8")
