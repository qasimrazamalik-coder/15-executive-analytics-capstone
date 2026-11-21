
# Data Dictionary

| Field | Type | Definition | Rule |
|---|---|---|---|
| record_id | string | Stable record identifier | Unique, non-null |
| date | date | Observation date | ISO 8601 |
| business_unit | category | Primary analytical segment | Controlled vocabulary |
| volume | integer | Activity volume | >= 0 |
| revenue | decimal | Gross revenue | >= 0 |
| cost | decimal | Direct/allocated cost | >= 0 |
| quality_score | decimal | Normalized operational quality | 0–100 |
| risk_flag | integer | Observed risk indicator | 0 or 1 |

Derived fields: `margin = revenue - cost`; `margin_pct = margin / revenue`; `risk_rate = mean(risk_flag)`.
