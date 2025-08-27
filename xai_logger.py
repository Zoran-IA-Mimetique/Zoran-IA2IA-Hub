# Journalisation XAI minimale (démo)
import json, time, hashlib

def log_decision(actor, inputs, output, reason):
    rec = {
        'ts': time.time(),
        'actor': actor,
        'input_hash': hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest(),
        'output_hash': hashlib.sha256(json.dumps(output, sort_keys=True).encode()).hexdigest(),
        'reason': reason
    }
    print(json.dumps(rec))

if __name__=='__main__':
    log_decision('zoran', {'q':'test'}, {'a':'ok'}, 'rule:test')
