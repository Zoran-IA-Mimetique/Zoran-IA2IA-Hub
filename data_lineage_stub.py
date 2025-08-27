# Traçabilité simple: enchaîne opérations et hachages (démo)
import json, hashlib
def step(prev_hash, payload):
    h=hashlib.sha256((prev_hash or '').encode()+json.dumps(payload, sort_keys=True).encode()).hexdigest()
    return h
if __name__=='__main__':
    h=None
    for i in range(3):
        h=step(h, {'i':i})
    print(json.dumps({'final_hash':h}))
