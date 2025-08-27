# Purge mémoire TTL (démo)
import time, json
class Mem:
    def __init__(self, ttl=60):
        self.ttl=ttl; self.s={}
    def set(self,k,v): self.s[k]=(v,time.time())
    def get(self,k):
        v=self.s.get(k); 
        if not v: return None
        val,ts=v
        if time.time()-ts>self.ttl:
            self.s[k]=('[REDACTED]',ts); return None
        return val
    def purge(self):
        now=time.time()
        for k,(v,ts) in list(self.s.items()):
            if now-ts>self.ttl: self.s[k]=('[REDACTED]',ts)
if __name__=='__main__':
    m=Mem(ttl=1); m.set('x','y'); time.sleep(1.1); m.purge(); print(json.dumps(m.s))
