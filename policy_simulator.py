# Simulateur de politique (démo): applique règles simples à un texte
import sys, json, pathlib, re
RULES={'no_hype': r'(révolutionnaire|ultime|imparable)'}
def main():
    p=sys.argv[1] if len(sys.argv)>1 else None
    if not p: return print(json.dumps({'error':'path'}))
    t=pathlib.Path(p).read_text(encoding='utf-8', errors='ignore').lower()
    res={k: bool(re.search(v,t)) for k,v in RULES.items()}
    print(json.dumps({'violations': res}))
if __name__=='__main__': main()
