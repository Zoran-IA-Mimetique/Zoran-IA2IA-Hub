import subprocess, sys, pathlib
def test_validator_runs():
    ROOT = pathlib.Path(__file__).resolve().parents[1]
    out = subprocess.check_output([sys.executable, str(ROOT/'lib'/'core.py')])
