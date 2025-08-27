# Scan minimal de tokens/glyphes suspects (pattern générique, non-invasif)
import re, sys, pathlib, json

PATTERNS = [r"\u25C6|⟦|⟧|⋄"]  # exemples génériques
def scan_text(text):
    found = []
    for p in PATTERNS:
        if re.search(p, text):
            found.append(p)
    return found

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    if path and pathlib.Path(path).exists():
        txt = pathlib.Path(path).read_text(encoding='utf-8', errors='ignore')
        print(json.dumps({"file": path, "matches": scan_text(txt)}))
    else:
        print(json.dumps({"error":"provide a file path"}))

if __name__ == '__main__':
    main()
