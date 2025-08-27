# Simulation scalabilité (démo)
import time, random, json
def simulate(n=5000):
    t0=time.time()
    for _ in range(n): time.sleep(random.random()/10000)
    dt=time.time()-t0
    return {'n': n, 'approx_p95_ms': round((dt/n)*1000*3,3)}
if __name__=='__main__': print(json.dumps(simulate()))
