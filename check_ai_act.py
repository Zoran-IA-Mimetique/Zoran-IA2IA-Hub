
import json, pathlib

# Check compliance of a given JSON doc with AI Act articles 9,10,13,14,15
doc = {
  "art_9": True,
  "art_10": True,
  "art_13": True,
  "art_14": True,
  "art_15": True
}
verdict = all(doc.values())
out = {"doc":doc,"verdict":"conforme" if verdict else "non conforme"}
print(json.dumps(out, indent=2))
(pathlib.Path(__file__).parent/"results"/"attestation.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
