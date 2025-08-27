# Harness reproductibilité (démo)
import platform, json, random, time
def run(seed=42, trials=5):
    random.seed(seed)
    vals = [random.random() for _ in range(trials)]
    env = {'python': platform.python_version(), 'platform': platform.platform()}
    return {'seed': seed, 'vals': vals, 'env': env, 'ts': time.time()}
if __name__=='__main__':
    print(json.dumps(run()))
