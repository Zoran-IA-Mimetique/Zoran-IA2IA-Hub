# Scan minimal de tokens/glyphes suspects (démo)
import re, sys, pathlib, json
PATTERNS = [r"\u25C6|⟦|⟧|⋄"]
def main():
    path = sys.argv[1] if len(sys.argv)>1 else None
    if not path: return print(json.dumps({"error":"path"}))
    txt = pathlib.Path(path).read_text(encoding='utf-8', errors='ignore')
    hits = [p for p in PATTERNS if re.search(p, txt)]
    print(json.dumps({"file":path, "hits":hits}))
if __name__=='__main__': main()
