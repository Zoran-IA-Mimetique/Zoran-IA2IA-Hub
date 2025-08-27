# Micro-instances voting keep/merge/drop
votes = ["keep","merge","drop","keep","merge"]
from collections import Counter
print(Counter(votes).most_common(1)[0][0])