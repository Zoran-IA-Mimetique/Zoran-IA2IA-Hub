# stdlib-only demo of fractal memory layers
import json, time
mem = {"short": [], "long": [], "latent": {}, "parasitic": []}
for i in range(5):
    mem["short"].append({"t": time.time(), "v": i})
mem["long"] = mem["short"][:]
mem["latent"]["hint"] = "pre_eureka"
mem["parasitic"].append("ext://signal:demo")
print(json.dumps(mem, ensure_ascii=False))