# Zoran IA↔IA Hub — Flat Pack (v1.0.0)
- 100% sans dossiers (zip à plat). À déposer tel quel à la racine d’un dépôt.
- Déplacez **CI_GITHUB_ACTIONS.yml** vers `.github/workflows/ci.yml` après import.
- Démarrage: `python main.py --demo` puis `pytest -q` et `python loadtest.py --messages 1000 --concurrency 200`.
