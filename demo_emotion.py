
import sys, json
EMOTIONS = {"joie":["heureux","content","satisfait"],
            "colere":["fâché","enerve","colere","énervé"],
            "tristesse":["triste","déprimé","malheureux"]}
text = " ".join(sys.argv[1:]) if len(sys.argv)>1 else "Je suis très heureux aujourd'hui"
scores = {emo: sum(word in text.lower() for word in words) for emo, words in EMOTIONS.items()}
pred = max(scores, key=scores.get)
print(json.dumps({"text":text,"scores":scores,"prediction":pred}, indent=2, ensure_ascii=False))
