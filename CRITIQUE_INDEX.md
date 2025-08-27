# Index des preuves d’autocritique — Zoran-IA2IA-Hub
_Date_: 2025-08-27

Ce hub intègre volontairement des **fichiers critiques et auto-critiques**. Ils ne sont **pas** des failles, mais des **preuves publiques** de transparence et de robustesse (PlayUIA).

## 1) Gouvernance / Processus (preuves d’auto-contrôle)
- `GOVERNANCE.md` — règles, responsabilités, décisions.
- `CODE_OF_CONDUCT.md` — cadre de conduite communautaire.
- `CONTRIBUTING.md` — exigences de contributions (tests, revues).
- `MAINTAINERS.md` — responsables identifiés.
- `ROADMAP.md`, `ROADMAP_SMART.md` — objectifs et jalons.
- `RUNBOOK_incidents.md` — gestion d’incidents & post-mortems.
- `COMMUNITY.md`, `COMMUNITY_PLAN.md`, `COMMUNITY_CONTRIBUTION.md` — dispositifs ouverts.
- `FILE_INDEX.md`, `INDEX.md` — traçabilité des artefacts.
- `OFFICIAL_RESPONSE.md` — réponses publiques consolidées.

## 2) Sécurité / Conformité (preuves d’auditabilité)
- `SECURITY.md`, `SECURITY_hardening.md`, `SECURITY_threat_model.md` — durcissement & menaces.
- `SECURITY_privacy.md` — vie privée & minimisation.
- `ai_act_mapping.md`, `ai_act_attestation.json`, `check_ai_act.py` — AI Act : mappages & vérifs.
- `SLO_SLA.md` — engagements de service.
- `RISK_REGISTER.md` — registre des risques.
- `ANTI_BIAS_PROTOCOL.md`, `BIAS_ethics_mimesis.md` — politiques anti-biais.
- `OPEN_SOURCE_ATTESTATION.json`, `CITATION.cff` — attestations publiques.
- `LICENSE` + `LICENSE_EXPLAINED.md` — cadre légal (MIT + explications).

## 3) Architecture / Scalabilité (preuves techniques)
- `ARCHITECTURE.md`, `architecture_overview.md`, `architecture_detailed.md`, `ARCH_DECENTRALIZED.md` — descriptions complètes.
- `arch_schema.json`, `IA_AXE_schema.json`, `IA_AXE_spec.md`, `OTOKEN_schema.json`, `OTOKEN_spec.md`, `absorption_dose.schema.json` — schémas.
- `SCALABILITY.md`, `SCALABILITY_strategy.md`, `SCALING_GUARDS.md` — performances & gardes.
- `PERFORMANCE_bench_plan.md`, `BENCHMARKS.md`, `bench_nlu.json`, `bench_pid.json`, `bench_planner.json` — plans & données de bench.
- `core.py`, `__init__.py` — noyau exécutable (stdlib only).
- `api_reference.md`, `applications_catalog.md`, `autoscale_policy.yaml`, `api_rate_limit.json` — intégration & politiques.

## 4) Cognition / Modules (preuves expérimentales)
- `consciousness_module_readme.md`, `consciousness_results_demo.json` — conscience (démo).
- `cognitive_architecture_readme.md`, `cognitive_architecture_schema.json`, `cognitive_architecture_plan.json` — architecture cognitive.
- `MODEL_COLLAPSE_MONITOR.md` — dérives & effondrement de modèle.
- `algorithms_explained.md`, `analysis_report.md`, `ablation_plan.md` — analyses & ablations.

## 5) Communauté / Transparence (preuves externes)
- `COMMUNITY_SHOWCASE.md`, `COMMUNITY_CHAT.md`, `COMMUNITY_FEEDBACK.md` — échanges & réutilisations.
- `WHITEPAPER.md` — récit technique.
- `MILESTONES.json`, `EVIDENCE_LOG.md`, `adoption_tracking.json` — journalisation & adoption.
- `PILOTS.md` — pilotes & retours.

---

### Lecture guidée (PlayUIA)
1. **Lire** les fichiers de cette liste comme des **preuves d’autocritique**.
2. **Relier** chaque classe de preuve à un **risque** dans `RISK_REGISTER.md`.
3. **Tester** les garde-fous décrits (ex. SCALING_GUARDS) avec les plans de bench (`PERFORMANCE_bench_plan.md`, `BENCHMARKS.md`).

> Cette page **requalifie** l’ensemble des documents critiques : ils sont publiés **volontairement** pour maximiser auditabilité, falsifiabilité et robustesse inter‑IA (IA↔IA).
