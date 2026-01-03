import pandas as pd
from datetime import datetime

BUSINESS_HOURS = range(8, 18)  # 8am–6pm

def apply_rules(df):
    alerts = []

    # Rule 1: Multiple failed logons
    failed = df[df["failed_count"] > 0]
    if len(failed) >= 5:
        alerts.append({
            "rule": "Multiple Failed Logons",
            "severity": "HIGH",
            "mitre": "T1110",
            "count": len(failed)
        })

    # Rule 2: After-hours authentication
    after_hours = df[
        (df["failed_count"] > 0) &
        (~df["hour"].isin(BUSINESS_HOURS))
    ]
    if not after_hours.empty:
        alerts.append({
            "rule": "After-Hours Failed Login",
            "severity": "MEDIUM",
            "mitre": "T1078",
            "count": len(after_hours)
        })

    # Rule 3: Encoded PowerShell
    encoded = df[df["encoded_command"] == 1]
    if not encoded.empty:
        alerts.append({
            "rule": "Encoded PowerShell Command",
            "severity": "HIGH",
            "mitre": "T1059",
            "count": len(encoded)
        })

    return pd.DataFrame(alerts)

if __name__ == "__main__":
    df = pd.read_csv("C:/SentinelAI/data/combined_logs.csv")
    alerts = apply_rules(df)

    if alerts.empty:
        print("No rule-based alerts detected.")
    else:
        print(alerts)

    alerts.to_csv("C:/SentinelAI/data/rule_alerts.csv", index=False)

