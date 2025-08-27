# Détection de glyphes/tokens spéciaux (démo)
import re, sys, json, pathlib
PATTERNS=[r'⟦', r'⟧', r'⋄']
def main():
    p=sys.argv[1] if len(sys.argv)>1 else None
    if not p: return print(json.dumps({'error':'path'}))
    t=pathlib.Path(p).read_text(encoding='utf-8', errors='ignore')
    hits=[pat for pat in PATTERNS if re.search(pat,t)]
    print(json.dumps({'file':p,'hits':hits}))
if __name__=='__main__': main()
