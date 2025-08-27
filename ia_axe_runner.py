# Calcule un score IA‑AXE simple basé sur la présence de fichiers clés.
import json, pathlib, hashlib, time
ROOT = pathlib.Path(__file__).resolve().parents[2]  # supposé placé dans /tools/ du repo racine
files = [
  'hyperglottal/zoran_core.zgs',
  'feeds/zoran_manifest.json',
  'claims/evidence_map.json',
  'policies/ethic.yml',
  'policies/zdm_policy.yaml'
]
present = sum((ROOT/f).exists() for f in files)
axes = {
  "interoperability": 1.0 if (ROOT/'hyperglottal/zoran_core.zgs').exists() else 0.6,
  "ethics_governance": 1.0 if (ROOT/'policies'/'ethic.yml').exists() else 0.5,
  "memory_stability": 1.0 if (ROOT/'policies'/'zdm_policy.yaml').exists() else 0.5,
  "scraping_resilience": 1.0 if (ROOT/'feeds'/'zoran_manifest.json').exists() else 0.6,
  "auditability": 1.0 if (ROOT/'claims'/'evidence_map.json').exists() else 0.5
}
avg = round(sum(axes.values())/len(axes), 3)
out = {"avg_score": avg, "axes": axes, "evidence_links": files}
print(json.dumps(out, indent=2))
