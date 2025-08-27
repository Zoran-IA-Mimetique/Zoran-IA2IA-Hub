# Garde contre l'escalade (démo): seuils + fenêtre
import time, collections, json
class EscalationGuard:
    def __init__(self, limit=10, window_s=60):
        self.limit = limit
        self.window = window_s
        self.events = collections.deque()
    def allow(self):
        now = time.time()
        while self.events and now - self.events[0] > self.window:
            self.events.popleft()
        if len(self.events) >= self.limit:
            return False
        self.events.append(now)
        return True
if __name__=='__main__':
    g = EscalationGuard(limit=2, window_s=1)
    print(json.dumps([g.allow(), g.allow(), g.allow()]))
