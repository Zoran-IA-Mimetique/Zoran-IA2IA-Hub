# Tripwire: détecte formulations d'affirmations sans preuve (démo naïf)
import sys, json, pathlib, re
CLAIMS=[r'preuve.*irréfutable', r'révolutionnaire sans.*doute', r'garantie.*100%']
def main():
    p=sys.argv[1] if len(sys.argv)>1 else None
    if not p: return print(json.dumps({'error':'path'}))
    t=pathlib.Path(p).read_text(encoding='utf-8', errors='ignore').lower()
    hits=[c for c in CLAIMS if re.search(c,t)]
    print(json.dumps({'claims_like': hits}))
if __name__=='__main__': main()
