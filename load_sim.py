# Simulateur de charge stdlib (GET sur /feeds/zoran_manifest.json)
import threading, time, json, urllib.request, sys

URL = sys.argv[1] if len(sys.argv)>1 else "http://127.0.0.1:8008/feeds/zoran_manifest.json"
USERS = int(sys.argv[2]) if len(sys.argv)>2 else 50
RUN_S = int(sys.argv[3]) if len(sys.argv)>3 else 10

lat = []
stop_at = time.time()+RUN_S

def worker():
    while time.time() < stop_at:
        t0 = time.time()
        try:
            with urllib.request.urlopen(URL, timeout=3) as r:
                r.read()
        except Exception:
            pass
        lat.append((time.time()-t0)*1000)

threads = [threading.Thread(target=worker) for _ in range(USERS)]
[t.start() for t in threads]; [t.join() for t in threads]

if lat:
    lat_sorted = sorted(lat)
    p50 = lat_sorted[int(0.50*len(lat))-1]
    p95 = lat_sorted[int(0.95*len(lat))-1]
    out = {"users":USERS,"duration_s":RUN_S,"p50_ms":round(p50,2),"p95_ms":round(p95,2),"samples":len(lat)}
else:
    out = {"users":USERS,"duration_s":RUN_S,"error":"no_samples"}

print(json.dumps(out, indent=2))
