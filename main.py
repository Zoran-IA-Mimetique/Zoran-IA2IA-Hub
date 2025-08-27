import json, pathlib
print(json.loads((pathlib.Path(__file__).resolve().parents[1]/'feeds'/'zoran_manifest.json').read_text(encoding='utf-8')))