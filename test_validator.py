import subprocess, sys, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2]
out=subprocess.check_output([sys.executable,str(ROOT/'code'/'validator.py')])
assert b'stability_score' in out
