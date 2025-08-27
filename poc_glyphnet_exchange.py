# Glyphic encode: compact + checksum
import hashlib, json
payload = {"m":"hello","t":1}
raw = json.dumps(payload,separators=(",",":"))
h = hashlib.md5(raw.encode()).hexdigest()[:6]
print(f"⟦GXY:{h}⋄{raw}⟧")