# Methodology — Customer RFM & Churn Analysis

## 1. Objective
To provide a **portfolio-grade, end-to-end example** of how a data-science consultant would:
* segment an e-commerce customer base using **RFM analysis**,
* identify and predict **customer churn**, and
* estimate **Customer Lifetime Value (CLV)**.

The goal is to demonstrate a complete consulting workflow, from raw transactional data to actionable business insights.

---

## 2. Data
**Source:** Synthetic “JungleCart” e-commerce dataset (Jan 2018 – Sept 2025) generated in the preceding repository.

**Main tables:**
* `customers.csv` – customer master data.
* `orders.csv`, `order_items.csv` – transactional sales records.
* `products.csv` – product hierarchy (category/subcategory).
* `payments.csv`, `returns.csv`, `refunds.csv` – financial adjustments.

The dataset deliberately contains **messy real-world quirks** (e.g., missing values, returns, refunds) to replicate a true consulting scenario.

---

## 3. Data Preparation
1. **Safe ingestion:** Custom loader automatically detects and parses date-like columns to avoid errors from missing column names.
2. **Revenue calculation:**  
   * Primary source: `order_items` × `unit_price`.
   * Fallback: `payments` table when item-level price data is missing.
   * Returns and refunds are subtracted to create **net revenue**.
3. **Filtering:** Orders are restricted to completed/paid/shipped statuses where available.

---

## 4. RFM Analysis
* **Recency:** Days since the most recent purchase (relative to the dataset’s latest order date).
* **Frequency:** Count of unique orders per customer.
* **Monetary:** Total net revenue generated per customer.

**Scoring:** Each metric is converted into quintiles (1–5).  
*Higher score = better metric.*  
* `R_score` uses inverted recency (more recent = higher score).  
* `F_score` and `M_score` use direct ranking.

**Segmentation:**  
Rules-based mapping creates interpretable groups:
* Champions, Loyal, Big Spenders, At Risk, Hibernating, Regulars.

---

## 5. Dynamic Churn Labelling
A **variable churn horizon** reflects differences in buying behaviour:
* High-frequency or high-category-diversity customers: **90 days**.
* Average customers: **120 days**.
* Low-frequency customers: **180 days**.

A customer is labelled **churned** if their days since last purchase exceed their personal horizon.

---

## 6. Survival Analysis (Optional)
If `lifelines` is available, a **Kaplan–Meier survival curve** estimates the probability that a customer remains active over time.

---

## 7. Predictive Churn Model
* **Features:** RFM metrics, category richness, tenure, order velocity, average order value.
* **Model:** Logistic regression with isotonic calibration (`CalibratedClassifierCV`) to produce well-calibrated probabilities.
* **Evaluation:** ROC-AUC, Average Precision, and Brier score.  
  Decile lift plots show how churn rate increases with predicted risk.

The model produces a **churn probability per customer** for marketing automation.

---

## 8. Customer Lifetime Value (CLV)
Two approaches:
1. **Probabilistic (preferred):** BG/NBD + Gamma-Gamma models (`lifetimes` package) estimate 6-month purchase frequency and spend.
2. **Heuristic fallback:** Velocity of orders × average order value.

Outputs a **6-month CLV estimate per customer**.

---

## 9. Deliverables
All artefacts are exported to `/outputs/`:
* `customer_master_rfm_churn_clv.csv` – consolidated table of RFM, churn probabilities and CLV.
* Intermediate CSVs and all figures (segment distributions, churn rate charts, survival curves, risk-decile lift plots).

---

## 10. Assumptions & Limitations
* Synthetic data approximates real e-commerce patterns but does not represent an actual business.
* Churn horizon thresholds (90/120/180 days) are heuristics for demonstration; a real engagement would validate these using historical retention curves.
* CLV modelling assumes stationarity of purchasing behaviour within the forecast window.

---

## 11. Next Steps
This customer-centric analysis feeds directly into **Repo 02: Revenue Trend Forecasting**, where churn-adjusted forecasts of revenue and seasonality will inform:
* inventory planning,
* marketing budget allocation, and
* strategic growth scenarios.