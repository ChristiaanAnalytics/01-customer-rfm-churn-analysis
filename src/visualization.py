"""
Reusable plotting utilities for RFM and churn analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_segment_counts(df: pd.DataFrame, segment_col: str = "segment"):
    """
    Bar chart of customers by RFM segment.
    """
    plt.figure(figsize=(10,5))
    sns.countplot(data=df, x=segment_col, order=df[segment_col].value_counts().index)
    plt.xticks(rotation=20, ha="right")
    plt.title("Customers by RFM Segment")
    plt.tight_layout()

def plot_churn_rate_by_segment(df: pd.DataFrame, segment_col: str = "segment", churn_col: str = "is_churned"):
    """
    Bar chart of churn rate by segment.
    """
    churn_by_seg = df.groupby(segment_col)[churn_col].mean().sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    sns.barplot(x=churn_by_seg.index, y=churn_by_seg.values)
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Churn rate")
    plt.title("Churn rate by RFM segment")
    plt.tight_layout()