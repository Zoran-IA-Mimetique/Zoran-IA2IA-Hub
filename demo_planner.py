
import json
G = {"A":["B","C"],"B":["D"],"C":["E"],"D":["F"],"E":["F"],"F":[]}
start, goal = "A","F"
from collections import deque
q = deque([[start]])
seen = set([start])
found = []
while q:
    path = q.popleft()
    if path[-1]==goal:
        found = path; break
    for n in G[path[-1]]:
        if n not in seen:
            seen.add(n); q.append(path+[n])
print(json.dumps({"plan":found}, indent=2))
