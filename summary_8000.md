# Zoran IA↔IA Hub — Pack « Ready » (Compliance • Interop • CI • Demo)

Ce pack corrige 13 points critiques identifiés : licence, conformité RGPD/AI Act, interopérabilité IA↔IA, équilibre code/doc, onboarding,
gouvernance, scalabilité, CI/CD, communauté, schémas, positionnement, surcharge documentaire et démos partielles.

## Ce qui change concrètement
- **Licence OSI** : MIT au cœur, **ETHICAL_ADDENDUM.md** séparé (non contraignant).
- **Conformité** : matrices AI Act + RGPD (DPIA template, ROPA), ISO 42001 mapping, LEGAL_DISCLAIMER clair.
- **Interop IA↔IA** : schémas JSON Schema + JSON‑LD, OpenAPI 3.1, dataset `datasets/ia2ia_messages.jsonl`, bench `benchmark/IA2IA_bench.py`.
- **Code opérationnel** : `main.py`, `orchestrator.py`, `memory.py`, `ethicchain_policy_check.py` (ΔM11.3), `loadtest.py` (async).
- **CI/CD** : `.github/workflows/ci.yml` (pytest, flake8, bandit, docker build; artefacts de couverture).
- **Scalabilité** : scénarios `configs/bench_scenarios.yaml`, résultats `results/` + script de charge.
- **Démos clés en main** : `Dockerfile`, `docker-compose.yml`, `examples/run_demo.sh`.
- **Gouvernance & communauté** : `GOVERNANCE.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, templates d’issues/PR, `ROADMAP.md`.
- **Docs allégées** : `docs/INDEX.md` (table des matières compacte), `README.md` unique, `SUMMARY.md` minimal.
- **Positionnement** : `SCIENTIFIC_POSITIONING.md` factuel, `EVIDENCE_PLAN.md` pour validation empirique.

## Comment démarrer (3 minutes)
```bash
# 1) Demo locale (Python 3.11+)
python main.py --demo

# 2) Tests + charge
pytest -q
python loadtest.py --messages 1000 --concurrency 200

# 3) Docker
docker build -t zoran/ia2ia:ready .
docker compose up
```

## Bench d’interopérabilité
- **But** : évaluer la clarté du protocole IA↔IA et la stabilité ΔM11.3.
- **Mesures** : taux de parsing (JSON Schema), latence P95, cohérence, taux de rollback, idempotence.
- **Reproductible** : `benchmark/IA2IA_bench.py` + `datasets/` + `results/` fournis.

## Schémas normalisés
- `schemas/ia2ia-message.schema.json` (JSON Schema 2020-12) + `schemas/context.jsonld` (JSON‑LD).
- `openapi.yaml` (3.1) pour exposition REST minimale.

## Gouvernance & sécurité
- **GOVERNANCE.md** clarifie rôles et décisions.
- **CONTRIBUTING.md** impose tests, lint, et passage `ethicchain_policy_check.py` en CI.
- **SECURITYPRIVACY.md** explique le périmètre sécurité, divulgation responsable et données personnelles.

## Limites & prochaines étapes
- Pas de certification externe (prévue via `compliance/externals/README.md`).
- Résultats de charge fournis à titre indicatif (simulation locale).
- Ouverture à contributions : implémentations multi‑langages, plus de datasets et cas réels.
