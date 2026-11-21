
# Analytical Guardrails

- Validate schema, uniqueness, ranges and nulls before calculating KPIs.
- Never treat synthetic findings as claims about a real company or person.
- Aggregate small cohorts; do not expose row-level data in production dashboards.
- Separate correlation from causation and label modeled or forecast values.
- Reconcile every segment total to the portfolio total before publication.
- Version metric definitions; do not silently change KPI denominators.
- Apply least-privilege access to production data and never commit credentials.
- Use human review for high-impact employment, health, lending or fraud decisions.
