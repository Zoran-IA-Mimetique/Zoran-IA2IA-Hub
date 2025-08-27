# Simulation: vérifie la présence des fichiers clés et "score" la couverture.
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
required = [
  'hyperglottal/zoran_core.zgs',
  'feeds/zoran_manifest.json',
  'claims/evidence_map.json',
  'evaluations/scoring_rules.yaml'
]
coverage = sum((ROOT/p).exists() for p in required)/len(required)
print(json.dumps({"absorption_coverage": coverage}, indent=2))
