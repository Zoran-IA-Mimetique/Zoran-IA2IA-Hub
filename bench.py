# Bench jouet: latence de décisions
import time, json, random
def decide(x):
    time.sleep(random.random()/1000)
    return x*2
def bench(n=1000):
    t0=time.time()
    for i in range(n): decide(i)
    dt=time.time()-t0
    return {'n':n,'latency_p95_ms_approx': round((dt/n)*1000*3,3)}
if __name__=='__main__':
    print(json.dumps(bench()))
