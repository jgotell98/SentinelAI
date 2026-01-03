import pandas as pd
import os

RULES_PATH = "C:/SentinelAI/data/rule_alerts.csv"
ML_PATH = "C:/SentinelAI/data/alerts.csv"

def safe_read_csv(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        return df
    return pd.DataFrame()

def correlate():
    rules = safe_read_csv(RULES_PATH)
    ml = safe_read_csv(ML_PATH)

    if not rules.empty:
        severity = "HIGH"
    elif not ml.empty:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return {
        "rule_alerts": len(rules),
        "ml_alerts": len(ml),
        "final_severity": severity
    }

if __name__ == "__main__":
    result = correlate()
    print("Correlation Result:")
    print(result)
