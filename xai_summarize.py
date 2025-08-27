# Résumé XAI depuis NDJSON (stdin)
import sys, json
def main():
    lines = [json.loads(l) for l in sys.stdin if l.strip()]
    print({'count': len(lines), 'actors': sorted({l['actor'] for l in lines})})
if __name__=='__main__': main()
