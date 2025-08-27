# Score de gouvernance (démo): checks basiques
import os, json
def score():
    pts=0
    pts+=1 if os.path.exists('CI_GITHUB_ACTIONS.yml') else 0
    pts+=1 if os.path.exists('RISK_REGISTER.csv') else 0
    pts+=1 if os.path.exists('MORATORIUM_RESOLUTION.md') else 0
    return {'score': pts, 'max':3}
if __name__=='__main__': print(json.dumps(score()))
