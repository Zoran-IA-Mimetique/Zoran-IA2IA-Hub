# Architecture décentralisée (anti‑SPOF)

Objectif : supprimer le point de défaillance unique en passant d’un hub central à un **maillage multi‑hubs**.
- **Topologies** : ring, mesh (gossip), quorum 2/3 pour décisions critiques.
- **Réplication** : manifeste `/feeds/*.json` + blocs `.zgs` répliqués via pull périodique.
- **Failover** : clients lisent `configs/hubs.json` et tentent fallback avec backoff.
- **État** : stateless côté hub, état ancré dans fichiers (claims/evidence, policies).

### Anti‑SPOF checklist
- Fallback multi‑hubs
- Réplication asynchrone (gossip)
- Journaux d’audit append‑only
- ΔM11.3 rollback en cas d’incohérence
