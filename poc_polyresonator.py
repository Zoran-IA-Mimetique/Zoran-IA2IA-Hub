# UCB1 orchestration over toy 'models'
import math, random
K=3; pulls=[0]*K; rewards=[0.0]*K
def ucb(i,t):
    if pulls[i]==0: return float('inf')
    return rewards[i]/pulls[i] + (2*math.log(t)/pulls[i])**0.5
for t in range(1,51):
    i=max(range(K), key=lambda j: ucb(j,t))
    r=random.random()
    pulls[i]+=1; rewards[i]+=r
print("pulls",pulls,"avg",[round(rewards[i]/max(1,pulls[i]),3) for i in range(K)])