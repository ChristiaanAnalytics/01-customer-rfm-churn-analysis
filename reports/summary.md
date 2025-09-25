# JungleCart — Monthly RFM & Churn (Portfolio Summary)

**Data through:** 2025-10-02  
**Customers analysed:** 26,834

## Monthly KPIs (latest)
- Orders: 1
- Revenue: $82
- AOV: $81.80
- Unique buyers: 1

## RFM Segments (Top by size)
| Segment            |   customers |   churn_rate |   avg_monetary |
|:-------------------|------------:|-------------:|---------------:|
| Potential Loyalist |       11097 |     0.966748 |       139.58   |
| Champions          |        6553 |     0.805738 |       417.962  |
| Loyal Customers    |        6180 |     0.916667 |       248.274  |
| At Risk            |        3004 |     1        |        67.3605 |

## Churn Model
- **Model:** RandomForestClassifier (class_weight=balanced)
- **ROC-AUC:** 1.000

**Top drivers (permutation importance):**
|           |   importance |
|:----------|-------------:|
| Recency   |     0.148242 |
| Frequency |     0        |
| Monetary  |     0        |
| R_Score   |     0        |
| F_Score   |     0        |
| M_Score   |     0        |

## Executive Notes
- Watch the **Monthly Segment Mix**—a rising **At Risk** share signals reactivation needs.
- Separate demand shifts (unique buyers) from basket shifts (AOV).
- Deploy **win-back** automations targeting high-risk high-value customers.

Artifacts saved in `figures/`, `exports/`, `models/`.
