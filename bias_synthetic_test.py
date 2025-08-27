# Test biais synthétique (démo naïf)
import random, json
def run(n=1000):
    a=sum(random.random()<0.55 for _ in range(n))
    b=n-a
    return {'groupA':a, 'groupB':b, 'delta': (a-b)/n}
if __name__=='__main__':
    print(json.dumps(run()))
