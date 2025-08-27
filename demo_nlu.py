
import sys, json, re
text = " ".join(sys.argv[1:]) if len(sys.argv)>1 else "bonjour, comment ça va ?"
intents = {
    "greet": ["bonjour","salut","hello"],
    "ask_status": ["comment","ça","va","ca va"],
    "bye": ["au revoir","bye","ciao"]
}
scores = {k: sum(1 for w in v if re.search(r"\b"+re.escape(w)+r"\b", text.lower())) for k,v in intents.items()}
intent = max(scores, key=scores.get)
print(json.dumps({"text":text,"scores":scores,"intent":intent}, indent=2, ensure_ascii=False))
