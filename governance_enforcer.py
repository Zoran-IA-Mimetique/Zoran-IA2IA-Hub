# Enforcer minimal: vérifie présence tests et absence de secrets (démo)
import os, re, json, pathlib, sys
def at_least_one_test():
    return any(p.endswith('_test.py') or p.startswith('test_') for p in os.listdir('.'))
def no_secret_patterns():
    pat = re.compile(r'(AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA|EC) PRIVATE KEY-----)')
    for p in os.listdir('.'):
        if not os.path.isfile(p): continue
        try:
            if pat.search(pathlib.Path(p).read_text(encoding='utf-8', errors='ignore')):
                return False
        except Exception:
            pass
    return True
def main():
    res = {
        'has_test': at_least_one_test(),
        'no_secrets': no_secret_patterns()
    }
    ok = all(res.values())
    print(json.dumps({'ok': ok, 'details': res}))
    sys.exit(0 if ok else 1)
if __name__=='__main__': main()
