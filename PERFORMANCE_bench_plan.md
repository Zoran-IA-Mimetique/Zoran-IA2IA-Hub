# Plan de bench de performance

- **Objectifs** : p95 < 200ms jusqu’à 100 agents ; dégradation gracieuse au‑delà.
- **Outillage** : Python stdlib (threading + urllib), pas de dépendances.
- **Méthode** :
  1) Lancer `code/serve.py` du dépôt principal.
  2) Exécuter `code/perf/load_sim.py` (cf. ci‑joint) sur 10/50/100 utilisateurs.
  3) Générer `performance/results.json` et vérifier SLO dans `SLO_SLA.md`.
