# Démo purge mémoire: TTL + redaction (jouet pédagogique)
import time, json

class SymbolicMemory:
    def __init__(self, ttl_seconds=60):
        self.ttl = ttl_seconds
        self.store = {}  # key -> (value, ts)
    def set(self, key, value):
        self.store[key] = (value, time.time())
    def get(self, key):
        v = self.store.get(key); 
        if not v: return None
        value, ts = v
        if time.time()-ts > self.ttl:
            # TTL expiré — redaction
            self.store[key] = ('[REDACTED]', ts)
            return None
        return value
    def purge_all_expired(self):
        now = time.time()
        for k,(v,ts) in list(self.store.items()):
            if now-ts > self.ttl:
                self.store[k] = ('[REDACTED]', ts)

if __name__=='__main__':
    m = SymbolicMemory(ttl_seconds=1)
    m.set('secret','data')
    time.sleep(1.2)
    m.purge_all_expired()
    print(json.dumps(m.store))
