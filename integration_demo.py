import subprocess, sys, pathlib

def test_end_to_end():
    ROOT = pathlib.Path(__file__).resolve().parents[1]
    out = subprocess.check_output([sys.executable, str(ROOT/'code'/'validator.py')])
    assert b'stability_score' in out
