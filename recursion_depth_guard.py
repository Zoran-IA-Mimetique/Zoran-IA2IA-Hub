# Garde récursion simple (démo): coupe au-delà d'une profondeur
import sys, json
def safe_recurse(depth, limit=10):
    if depth>limit: return {'ok': False, 'reason':'limit_exceeded'}
    return {'ok': True, 'depth': depth}
if __name__=='__main__':
    d=int(sys.argv[1]) if len(sys.argv)>1 else 0
    print(json.dumps(safe_recurse(d)))
