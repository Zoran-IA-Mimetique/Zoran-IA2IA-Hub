# Zoran IA↔IA Hub — Ready Pack (v1.0.0)

Badges: ![MIT](https://img.shields.io/badge/license-MIT-green) ![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)

> Pack « prêt production » corrigeant 13 points critiques : licence, conformité RGPD/AI Act, interop, CI/CD, scalabilité, démo Docker, gouvernance, schémas normalisés.

## Démarrage rapide
```bash
python main.py --demo
pytest -q
python loadtest.py --messages 1000 --concurrency 200
docker compose up
```

## Structure clé
- `main.py` • `orchestrator.py` • `memory.py` • `ethicchain_policy_check.py`
- `datasets/` • `benchmark/` • `results/` • `configs/`
- `schemas/` • `openapi.yaml`
- Docker: `Dockerfile` • `docker-compose.yml`
- CI: `.github/workflows/ci.yml`
- Conformité: `compliance/` • `SECURITYPRIVACY.md`
- Gouvernance: `GOVERNANCE.md` • `CONTRIBUTING.md`

## Contact
- MIT • © 2025 Frédéric Tabary • contact: tabary01@gmail.com
