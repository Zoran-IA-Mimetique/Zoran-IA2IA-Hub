# Latent ingestion + recall
latent = {"keys":["ethic","memory","resonance"]}
query = "memoire"
hit = any(query in k for k in latent["keys"])
print("WAKE" if hit else "SLEEP")