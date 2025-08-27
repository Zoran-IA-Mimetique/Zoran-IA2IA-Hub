# Détection simple de secrets (démo)
import re, sys, pathlib, json
SUSPECT = [r'AKIA[0-9A-Z]{16}', r'-----BEGIN (?:RSA|EC) PRIVATE KEY-----']
def main():
    path = sys.argv[1] if len(sys.argv)>1 else None
    if not path: return print('{"error":"path"}')
    txt = pathlib.Path(path).read_text(encoding='utf-8', errors='ignore')
    hits = [p for p in SUSPECT if re.search(p, txt)]
    print(json.dumps({"file":path, "hits":hits}))
if __name__=='__main__': main()
