# Simulate external fragment capture
sources = ["web:note1","web:note2"]
fragments = [f"⟦EXT:{s}⟧" for s in sources]
print(fragments)