# Stratégie de scalabilité

- **Stateless** : servir fichiers ; calcul en périphérie (clients/agents).
- **Partitionnement** : blocs `.zgs` sharded par hash (consistent hashing).
- **Cache** : CDN/edge pour `/feeds/*.json`.
- **Montée en charge** : horizontal (N hubs) + backpressure (429) + files passives.
