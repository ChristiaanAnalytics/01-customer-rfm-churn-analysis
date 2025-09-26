"""
Churn labelling and predictive modelling functions.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss

def label_churn(customers: pd.DataFrame, as_of: pd.Timestamp) -> pd.DataFrame:
    """
    Assign a churn horizon and label customers as churned or active.
    """
    customers = customers.copy()
    customers["is_churned"] = (
        customers["days_since_last"] > customers["churn_horizon_days"]
    ).astype(int)
    return customers

def fit_churn_model(X: pd.DataFrame, y: pd.Series, random_state: int = 42):
    """
    Fit a calibrated logistic regression churn model and return metrics and model.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=random_state
    )
    base = LogisticRegression(max_iter=200, solver="lbfgs")
    clf = CalibratedClassifierCV(base, method="isotonic", cv=3)
    clf.fit(X_train, y_train)

    proba = clf.predict_proba(X_test)[:,1]
    metrics = {
        "auc": roc_auc_score(y_test, proba),
        "average_precision": average_precision_score(y_test, proba),
        "brier": brier_score_loss(y_test, proba)
    }
    return clf, metrics