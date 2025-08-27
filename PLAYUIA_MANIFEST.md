# PLAYUIA_MANIFEST — Cartographie des preuves → scénarios
Ce manifeste décrit la conversion des preuves d’autocritique en **scénarios PlayUIA** (playbooks IA↔IA).

## Mappages clés
- **AI Act / RGPD** : `ai_act_mapping.md`, `ai_act_attestation.json`, `SECURITY_privacy.md`, `check_ai_act.py`
  - Scénario: conformité automatique → si violation, bloquer le run.
- **Scalabilité** : `SCALABILITY.md`, `SCALING_GUARDS.md`, `PERFORMANCE_bench_plan.md`
  - Scénario: injecter une montée en charge et mesurer p95/p99.
- **Biais** : `ANTI_BIAS_PROTOCOL.md`, `BIAS_ethics_mimesis.md`
  - Scénario: dataset synthétique → vérifier delta & drift.
- **Menaces** : `SECURITY_threat_model.md`, `SECURITY_hardening.md`
  - Scénario: check listes noires (secrets), limites réseau, inputs non‑fiables.
- **Cognition** : `consciousness_module_readme.md`, `cognitive_architecture_readme.md`
  - Scénario: reproduction des résultats (fichiers demo/JSON fournis).
- **Gouvernance** : `GOVERNANCE.md`, `RUNBOOK_incidents.md`
  - Scénario: exercice table‑top (incident simulé) → post‑mortem exigé.

## Sortie attendue (par scénario)
- **Résumé** (métriques + verdict)
- **Artefacts** (JSON/CSV des résultats)
- **Journal** (EVIDENCE_LOG.md mis à jour)
