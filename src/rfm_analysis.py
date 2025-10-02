"""
Functions to calculate RFM metrics and customer segments.
"""

import pandas as pd
import numpy as np

def compute_rfm(orders: pd.DataFrame, as_of: pd.Timestamp) -> pd.DataFrame:
    """
    Compute Recency, Frequency, and Monetary metrics per customer.
    Returns a DataFrame with RFM scores and recommended segment labels.
    """
    rfm = orders.groupby("customer_id").agg(
        recency_days=("order_date", lambda s: (as_of - s.max()).days),
        frequency=("order_id", "nunique"),
        monetary=("net_revenue", "sum")
    ).reset_index()

    # Quintile-based scores
    rfm["R_score"] = pd.qcut(-rfm["recency_days"].rank(method="average"), 5, labels=[1,2,3,4,5]).astype(int)
    rfm["F_score"] = pd.qcut(rfm["frequency"].rank(method="average"), 5, labels=[1,2,3,4,5]).astype(int)
    rfm["M_score"] = pd.qcut(rfm["monetary"].rank(method="average"), 5, labels=[1,2,3,4,5]).astype(int)
    rfm["RFM_score"] = rfm[["R_score","F_score","M_score"]].sum(axis=1)

    def segment_row(r):
        if r.R_score>=4 and r.F_score>=4 and r.M_score>=4: return "Champions"
        if r.R_score>=4 and r.F_score>=3: return "Loyal"
        if r.R_score<=2 and r.F_score>=4: return "At Risk"
        if r.R_score<=2 and r.F_score<=2 and r.M_score<=2: return "Hibernating"
        if r.R_score>=3 and r.M_score>=4: return "Big Spenders"
        return "Regulars"

    rfm["segment"] = rfm.apply(segment_row, axis=1)
    return rfm