"""
Data loading and cleaning utilities.
Safe date parsing and helper functions for reading JungleCart CSV files.
"""

from pathlib import Path
import pandas as pd

def read_csv_safe_dates(path: Path) -> pd.DataFrame:
    """
    Read a CSV file and automatically convert any date-like columns.
    This avoids 'Missing column provided to parse_dates' errors.
    """
    df = pd.read_csv(path)
    if df.empty:
        return df

    # detect date-like columns
    preferred = {"order_date","payment_date","refund_date","return_date","created_at","order_ts"}
    heuristic = {c for c in df.columns if any(k in c.lower() for k in ["date","time","timestamp","created_at","ts"])}
    candidates = list((preferred | heuristic) & set(df.columns))

    for c in candidates:
        df[c] = pd.to_datetime(df[c], errors="coerce")
    return df