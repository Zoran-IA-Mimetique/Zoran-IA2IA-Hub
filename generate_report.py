import json, csv, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
sota = list(csv.DictReader((ROOT/'evaluations'/'sota_matrix.csv').read_text(encoding='utf-8').splitlines(), delimiter=';'))
claims = json.loads((ROOT/'claims'/'evidence_map.json').read_text(encoding='utf-8'))
report = {"sota":sota,"evidence":claims}
print(json.dumps(report, indent=2, ensure_ascii=False))
