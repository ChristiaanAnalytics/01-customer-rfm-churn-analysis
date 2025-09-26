# JungleCart — Repo 01: Customer RFM & Churn Analysis

## 📌 Overview
This repository is the **first stage** of the JungleCart analytics portfolio.  
It demonstrates how a data-driven e-commerce company can:
* segment customers using **RFM (Recency, Frequency, Monetary) analysis**, and
* predict and monitor **customer churn**.

The work simulates a real consulting engagement: from raw transactional data to executive insights and actionable KPIs.

---

## 🎯 Objectives
* Build a **robust data-processing pipeline** that copes with messy, real-world e-commerce data.
* Identify customer segments (Champions, Loyal, At Risk, etc.) to guide marketing strategy.
* Estimate **churn probability** for every customer using a **calibrated logistic model**.
* Provide **6-month Customer Lifetime Value (CLV)** estimates with a probabilistic BG/NBD + Gamma–Gamma model (and a heuristic fallback).
* Export ready-to-use artefacts (CSV tables and figures) for later repositories.

---

## 🗂 Project Structure

01-customer-rfm-churn-analysis/
├─ README.md
├─ LICENSE
├─ requirements.txt
├─ environment.yml
├─ .gitattributes
├─ .gitignore
├─ data/
│   ├─ raw/
│   │   ├─ customers.csv
│   │   ├─ orders.csv
│   │   ├─ order_items.csv
│   │   ├─ payments.csv
│   │   ├─ returns.csv
│   │   ├─ refunds.csv
│   │   └─ products.csv
│   └─ processed/
├─ notebooks/
│   └─ 01_customer_rfm_churn_analysis.ipynb
├─ src/
│   ├─ __init__.py
│   ├─ data_loading.py
│   ├─ rfm_analysis.py
│   ├─ churn_model.py
│   └─ visualization.py
├─ assets/
│   ├─ junglecart_logo.png
│   ├─ colour_palette.md
│   └─ diagrams/
│       ├─ rfm_framework.png
│       └─ churn_workflow.svg
├─ outputs/
│   ├─ figures/
│   │   ├─ rfm_segments_counts.png
│   │   ├─ rfm_scatter_recency_monetary.png
│   │   ├─ churn_rate_by_segment.png
│   │   ├─ km_overall.png
│   │   └─ risk_deciles.png
│   ├─ customers_rfm.csv
│   ├─ customers_rfm_churn_labels.csv
│   ├─ customers_churn_scores.csv
│   ├─ customers_clv_6m.csv
│   └─ customer_master_rfm_churn_clv.csv
└─ docs/
    ├─ methodology.md
    ├─ key_findings.md
    └─ next_steps.md

Key configuration files:
* **.gitattributes** – enables Git LFS for large artefacts (figures, CSVs).
* **.gitignore** – excludes caches, logs and local environment files.

---

## 🔑 Key Findings
* **Balanced Customer Segments**: Champions and Loyal customers form a strong revenue core, while At Risk and Hibernating groups highlight clear win-back opportunities.
* **Dynamic Churn Insights**: Applying a 90/120/180-day churn horizon yields a realistic overall churn rate and exposes customers with **low purchase frequency or category diversity** as the highest-risk group.
* **Predictive Modelling**: The calibrated logistic model achieves high AUC and precision, enabling **top-decile targeting** for retention campaigns.
* **Customer Lifetime Value**: Six-month CLV estimates identify the most valuable customers and guide marketing investment.

---

## 📊 Exports
All key artefacts are saved to `outputs/`:
* `customer_master_rfm_churn_clv.csv` – single table combining RFM, churn probability and 6-month CLV.
* Segment-level CSVs and figures:
  * `customers_rfm.csv`
  * `customers_churn_scores.csv`
  * Figures such as `rfm_segments_counts.png`, `churn_rate_by_segment.png`, `risk_deciles.png`.

These files are intended to feed the next stage of the portfolio.

---

## ▶️ Reproduce the Analysis
1. **Clone** this repository.
2. **Create environment**:
   ```bash
   conda env create -f environment.yml
   conda activate junglecart

or

pip install -r requirements.txt

	3.	Run the notebook in notebooks/01_customer_rfm_churn_analysis.ipynb.

Git LFS is required for large figures and CSV outputs:

git lfs install


⸻

🚀 Next Step: Repo 02 — Revenue Trend Forecasting

With a clear picture of who the customers are and who is at risk of churn,
the next repository forecasts future revenue using time-series models (e.g. SARIMAX, Prophet).
This connects churn risk to financial impact, enabling better inventory planning and marketing-budget allocation.

⸻

📜 License

This project is released under the MIT License.
Feel free to fork or adapt for your own analytical portfolio.

