# Résumé NDJSON XAI depuis stdin
import sys, json
lines = [json.loads(l) for l in sys.stdin if l.strip()]
actors = sorted({l.get('actor') or l.get('a', 'z') for l in lines})
print({'count': len(lines), 'actors': actors})
