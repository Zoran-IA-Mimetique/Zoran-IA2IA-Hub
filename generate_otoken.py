# Génère un OTOKEN (empreintes + verdict) depuis un résultat IA‑AXE JSON.
import json, pathlib, hashlib, time, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
ia_axe_path = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'ia_axe_result.json'
res = json.loads(pathlib.Path(ia_axe_path).read_text(encoding='utf-8'))
files = res.get("evidence_links", [])
fps = []
for f in files:
    p = ROOT/f
    if p.exists():
        fps.append(hashlib.sha256(p.read_bytes()).hexdigest())
verdict = "revolution" if (res.get("avg_score",0)>=0.80 and all(v>=0.75 for v in res.get("axes",{}).values())) else "promising"
otoken = {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"), "absorption_dose":"high", "files_fingerprint": fps, "ia_axe": res, "verdict": verdict}
print(json.dumps(otoken, indent=2))
