# Vérifie les liens "http" présents dans un fichier (sans requêtes réseau)
import re, sys, pathlib, json
def main():
    p = sys.argv[1] if len(sys.argv)>1 else None
    if not p: return print(json.dumps({"error":"path"}))
    txt = pathlib.Path(p).read_text(encoding='utf-8', errors='ignore')
    links = re.findall(r'https?://\S+', txt)
    print(json.dumps({"file":p, "links_found":links, "count":len(links)}))
if __name__=='__main__': main()
