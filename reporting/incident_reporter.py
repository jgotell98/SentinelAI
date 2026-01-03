import pandas as pd
from datetime import datetime
import uuid

RULES_PATH = "C:/SentinelAI/data/rule_alerts.csv"
ML_PATH = "C:/SentinelAI/data/alerts.csv"
REPORT_PATH = "C:/SentinelAI/data/incident_report.txt"

MITRE_MAP = {
    "Multiple Failed Logons": "T1110 – Brute Force",
    "After-Hours Failed Login": "T1078 – Valid Accounts",
    "Encoded PowerShell Command": "T1059 – Command-Line Interface"
}

def load_alerts():
    try:
        rules = pd.read_csv(RULES_PATH)
    except:
        rules = pd.DataFrame()

    try:
        ml = pd.read_csv(ML_PATH)
    except:
        ml = pd.DataFrame()

    return rules, ml

def determine_severity(rules, ml):
    if not rules.empty:
        return "HIGH"
    if not ml.empty:
        return "MEDIUM"
    return "LOW"

def generate_summary(rules, ml):
    summary = []

    if not rules.empty:
        for _, row in rules.iterrows():
            summary.append(
                f"- Rule Triggered: {row['rule']} "
                f"(Count: {row['count']}, MITRE: {row['mitre']})"
            )

    if not ml.empty:
        summary.append(
            f"- ML Anomaly Detection flagged {len(ml)} suspicious events"
        )

    return "\n".join(summary) if summary else "No malicious activity detected."

def generate_recommendations(severity):
    if severity == "HIGH":
        return [
            "Reset affected user credentials",
            "Review authentication logs for lateral movement",
            "Enable or enforce MFA",
            "Investigate PowerShell execution activity"
        ]
    if severity == "MEDIUM":
        return [
            "Monitor affected accounts",
            "Review recent login activity",
            "Tune detection thresholds"
        ]
    return ["No immediate action required"]

def generate_report():
    rules, ml = load_alerts()
    severity = determine_severity(rules, ml)

    report = f"""
==============================
 SentinelAI Incident Report
==============================

Incident ID: {uuid.uuid4()}
Generated At: {datetime.now()}
Affected System: Windows Endpoint VM
Severity: {severity}

--- Summary ---
{generate_summary(rules, ml)}

--- MITRE ATT&CK Techniques ---
"""
    techniques = set()

    if not rules.empty:
        for _, row in rules.iterrows():
            techniques.add(MITRE_MAP.get(row["rule"], row["mitre"]))

    for tech in techniques:
        report += f"- {tech}\n"

    report += "\n--- Recommended Actions ---\n"
    for action in generate_recommendations(severity):
        report += f"- {action}\n"

    with open(REPORT_PATH, "w") as f:
        f.write(report)

    return report

if __name__ == "__main__":
    print(generate_report())
