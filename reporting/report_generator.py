# reporting/report_generator.py
from datetime import datetime

def generate_report(incident):
    return f"""
Incident Report
---------------
Time: {datetime.now()}
Severity: HIGH
MITRE ATT&CK: T1110 (Brute Force)

Summary:
Suspicious authentication behavior detected involving multiple failed login attempts.

Recommendation:
- Lock affected account
- Review source IP
- Enable MFA
"""

if __name__ == "__main__":
    print(generate_report({}))
