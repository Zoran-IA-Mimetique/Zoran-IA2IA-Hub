# PROBLEMS_FIXED.md — Trace de résolution (13/13)

1. **Licence éthique non standardisée** → `LICENSE` (MIT) + `ETHICAL_ADDENDUM.md` (non contraignant).
2. **RGPD / AI Act non auditables** → `compliance/AI_ACT_MATRIX.csv`, `RGPD_DPIA_TEMPLATE.md`, `ROPA.md`, `ISO_42001_MAP.md`, `LEGAL_DISCLAIMER.md`.
3. **Interop IA↔IA sans preuves** → `datasets/ia2ia_messages.jsonl`, `benchmark/IA2IA_bench.py`, `results/baseline.csv`.
4. **Équilibre code/doc** → Code exécutable (`main.py`, `orchestrator.py`, `memory.py`) + docs réduites.
5. **Courbe d’apprentissage** → `README.md` concis, `docs/INDEX.md`, `examples/run_demo.sh`.
6. **Gouvernance floue** → `GOVERNANCE.md`, `CONTRIBUTING.md`, `MAINTAINERS.yaml`, templates issues/PR.
7. **Scalabilité non validée** → `loadtest.py`, `configs/bench_scenarios.yaml`, `results/loadtest_1k.csv`.
8. **CI insuffisante** → `.github/workflows/ci.yml`, `tests/test_basic.py`, `coverage_report.md` (artefact).
9. **Adoption limitée** → `ROADMAP.md`, `SUPPORT.md`, `DISCUSSIONS.md`, `CHANGELOG.md`.
10. **Schémas partiels** → `schemas/ia2ia-message.schema.json`, `schemas/context.jsonld`, `openapi.yaml`.
11. **Positionnement radical** → `SCIENTIFIC_POSITIONING.md`, `EVIDENCE_PLAN.md` (neutres et falsifiables).
12. **Surcharge documentaire** → `docs/INDEX.md` (TOC), `SUMMARY.md`, fusion des README.
13. **Démos partielles** → `Dockerfile`, `docker-compose.yml`, `examples/run_demo.sh` clé en main.
