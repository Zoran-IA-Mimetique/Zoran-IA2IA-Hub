# Analyse performance (exemple)

- p95 = 180ms @50 users → conforme à l’objectif (<200ms)
- Dégradation gracieuse au‑delà (cf. plan de bench)
- Actions : activer CDN/edge pour `/feeds/*` si charge >100 users
