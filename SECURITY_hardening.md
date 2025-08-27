# Hardening sécurité

- **Surface minimale** : stdlib only, pas d’API mutables.
- **Validation entrées** : schémas JSON pour manifestes/verdicts/doses.
- **Rate limiting** (côté reverse proxy) et cache en lecture.
- **Journalisation** : événements critiques + claims→evidence.
- **Rollback ΔM11.3** si divergence d’état.
- **Zero‑trust** : aucune clé ici ; secrets hors dépôt.
