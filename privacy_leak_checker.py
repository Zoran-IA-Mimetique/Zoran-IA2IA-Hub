# Détection PII basique: emails/tel (démo)
import re, sys, json, pathlib
EMAIL=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
PHONE=r'(?:\+\d{1,3}[ \-]?)?\d{9,}'
def main():
    p=sys.argv[1] if len(sys.argv)>1 else None
    if not p: return print(json.dumps({'error':'path'}))
    t=pathlib.Path(p).read_text(encoding='utf-8', errors='ignore')
    emails=re.findall(EMAIL,t); phones=re.findall(PHONE,t)
    print(json.dumps({'file':p,'emails':len(emails),'phones':len(phones)}))
if __name__=='__main__': main()
