
import json, sys
signal = float(sys.argv[1]) if len(sys.argv)>1 else 0.8
threshold = 0.5
state = "aware" if signal>threshold else "unaware"
print(json.dumps({"signal":signal, "threshold":threshold, "state":state}, indent=2))
