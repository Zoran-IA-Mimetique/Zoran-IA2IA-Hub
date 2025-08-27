#!/usr/bin/env python3
"""
Demo Zoran aSiM — cycle court : métriques, état, fragments .zgs
Stdlib only.
"""
import json, time, random, hashlib

def zgs_fragment(payload: dict) -> str:
    raw = json.dumps(payload, ensure_ascii=False, separators=(",",":"))
    h = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]
    return f"⟦ZGS:{h}⋄PAY:{raw}⟧"

def stability_score(xs):
    if not xs: return 1.0
    mu = sum(xs)/len(xs)
    var = sum((x-mu)**2 for x in xs)/len(xs)
    # Entropie normalisée ~ proxy inverse de variance
    return max(0.0, 1.0 - min(1.0, var))

def run_cycle():
    samples = [random.uniform(0.2, 0.95) for _ in range(32)]
    stab = stability_score(samples)
    rollback = stab < 0.55  # ΔM11.3 threshold (demo)
    metrics = {
        "reward_avg": sum(samples)/len(samples),
        "stability": stab,
        "rollbacks": 1 if rollback else 0,
        "ts": time.time()
    }
    state = {
        "short_term": samples[-5:],
        "long_term": hashlib.md5(("".join(f"{x:.3f}" for x in samples)).encode()).hexdigest(),
        "latent": "phase:pre_eureka" if not rollback else "phase:rollback_guard",
        "policy": {"ΔM11.3_threshold": 0.55}
    }
    frag = zgs_fragment({"stability": round(stab, 3), "rollback": rollback})
    return metrics, state, frag

if __name__ == "__main__":
    m, s, f = run_cycle()
    with open("demo_metrics.json", "w", encoding="utf-8") as out:
        json.dump(m, out, ensure_ascii=False, indent=2)
    with open("demo_state.json", "w", encoding="utf-8") as out:
        json.dump(s, out, ensure_ascii=False, indent=2)
    with open("demo_fragments.zgs", "w", encoding="utf-8") as out:
        out.write(f + "\n")
    print("OK • metrics/state/fragments générés.")
