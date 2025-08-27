# Détection simple de secrets
import re, sys, pathlib, json
SUSPECT = [r'AKIA[0-9A-Z]{16}', r'-----BEGIN (?:RSA|EC) PRIVATE KEY-----']
def main():
    p = sys.argv[1] if len(sys.argv)>1 else None
    if not p: return print(json.dumps({"error":"path"}))
    txt = pathlib.Path(p).read_text(encoding='utf-8', errors='ignore')
    hits = [pat for pat in SUSPECT if re.search(pat, txt)]
    print(json.dumps({"file":p, "hits":hits}))
if __name__=='__main__': main()
