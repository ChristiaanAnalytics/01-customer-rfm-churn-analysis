# Key Findings — Customer RFM & Churn Analysis

## Customer Segmentation
* **Champions & Loyal Customers** form a strong core of JungleCart’s revenue.  
  They purchase frequently and recently, making them ideal for early product launches and premium upsells.
* **Big Spenders** show high monetary value but lower recent activity.  
  They represent an opportunity for **high-margin re-engagement campaigns**.
* **At Risk & Hibernating** segments highlight customers whose activity has lapsed and who are most likely to leave without intervention.

## Churn Insights
* Using a **dynamic churn horizon** (90/120/180 days) reveals a realistic overall churn rate.
* Customers with **low category diversity** and **low order frequency** show the highest churn risk.
* The **calibrated logistic churn model** delivers strong predictive performance (high AUC and precision), allowing precise targeting of retention budgets.

## Customer Lifetime Value (CLV)
* Six-month CLV estimates, derived from BG/NBD + Gamma-Gamma modelling (with a heuristic fallback), quantify the **future revenue potential** of each customer.
* CLV combined with churn probability identifies **high-value / high-risk customers**—a priority for retention.

## Strategic Takeaways
* Focus **retention spend** where **churn probability is high and CLV is significant** (e.g. Big Spenders and At Risk segments).
* Maintain and reward Champions and Loyal customers to protect the revenue base.
* Track the exported churn-probability scores weekly as an **early-warning KPI**.