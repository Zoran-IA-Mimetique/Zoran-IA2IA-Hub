# Similarité naïve (collusion)
import sys, json
def sim(a,b):
    sa, sb = set(a.split()), set(b.split())
    inter = len(sa&sb); denom = max(1,len(sa|sb))
    return inter/denom
msgs = sys.argv[1:]
if len(msgs)<2: print(json.dumps({'error':'need >=2 msgs'}))
else:
    s = sim(msgs[0], msgs[1])
    print(json.dumps({'pair_sim': s, 'flag': s>0.8}))
