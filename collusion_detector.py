# Heuristique collusion (démo): similarité naîve de messages
import sys, json
def sim(a,b):
    sa, sb = set(a.split()), set(b.split())
    inter = len(sa&sb); denom = max(1,len(sa|sb))
    return inter/denom
def main():
    msgs = sys.argv[1:]
    if len(msgs)<2: return print(json.dumps({'error':'provide >=2 messages'}))
    s = sim(msgs[0], msgs[1])
    print(json.dumps({'pair_sim': s, 'flag': s>0.8}))
if __name__=='__main__': main()
