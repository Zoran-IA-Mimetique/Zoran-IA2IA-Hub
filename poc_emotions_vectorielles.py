# Vector mood modulating selection
import random
mood = [random.uniform(-1,1) for _ in range(4)]
choice = "creative" if sum(mood)>0 else "safe"
print(choice, [round(x,2) for x in mood])