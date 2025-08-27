# Heuristique lock-in: répétitions de mots au-delà d'un seuil (démo)
import sys, json, pathlib, collections
def main():
    p=sys.argv[1] if len(sys.argv)>1 else None
    if not p: return print(json.dumps({'error':'path'}))
    t=pathlib.Path(p).read_text(encoding='utf-8', errors='ignore').lower().split()
    cnt=collections.Counter(t); over={k:v for k,v in cnt.items() if v>20}
    print(json.dumps({'overused_tokens': over, 'unique': len(cnt)}))
if __name__=='__main__': main()
