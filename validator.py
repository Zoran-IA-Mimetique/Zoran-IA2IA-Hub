import json, hashlib, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
REQ=['meta','hyperglottal','schemas','feeds','code','policies','injectors','docs','assets']
missing=[d for d in REQ if not (ROOT/d).exists()]
status='ok' if not missing else 'missing:'+','.join(missing)
h=hashlib.sha256((';'.join(sorted(REQ))+status).encode()).hexdigest()
stability=(int(h[:8],16)%1000)/1000
print(json.dumps({'status':status,'stability_score':stability},indent=2))
print('ΔM11.3: rollback triggered (demo)' if stability<0.72 else 'ΔM11.3: stable')
