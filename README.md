# SentinelAI – AI-Assisted Cybersecurity Defense Platform

SentinelAI is a Windows-focused, AI-assisted cybersecurity defense system designed to simulate how modern SOC, SIEM, and XDR platforms detect, correlate, and respond to security threats.

The system combines **rule-based detection**, **machine learning anomaly detection**, **MITRE ATT&CK mapping**, **automated incident reporting**, and a **human-in-the-loop learning pipeline** to improve detection accuracy over time.

---

## 🎯 Project Objectives

- Detect suspicious authentication and PowerShell activity on Windows endpoints
- Combine deterministic (rules) and probabilistic (ML) detection techniques
- Correlate alerts to reduce false positives
- Automatically generate SOC-style incident reports
- Safely retrain models using analyst-reviewed feedback

---

## 🧱 System Architecture

[ Windows Event Logs ]
|
v
[ Log Ingestion ]
|
v
[ Feature Extraction ]
|
v
[ Detection Engine ]
| |
[ Rules ] [ ML (Isolation Forest) ]
|
v
[ Alert Correlation ]
|
v
[ Incident Reporting ]
|
v
[ Analyst Feedback ]
|
v
[ Controlled Model Retraining ]



---

## 🛠️ Technology Stack

- **Language:** Python
- **OS:** Windows 10 Enterprise (VM)
- **Logging:** Windows Security & PowerShell Operational Logs
- **ML:** Scikit-learn (Isolation Forest)
- **Security Framework:** MITRE ATT&CK
- **Automation:** PowerShell + Python
- **Version Control:** GitHub

---

## 🔍 Detection Capabilities

### Rule-Based Detection
- Multiple failed login attempts (Brute Force – T1110)
- After-hours authentication attempts (Valid Accounts – T1078)
- Encoded PowerShell commands (Command-Line Interface – T1059)

### Machine Learning Detection
- Unsupervised anomaly detection using Isolation Forest
- Identifies abnormal login timing, frequency, and command execution patterns

### Alert Correlation
- Rule-based alerts take precedence
- ML alerts raise severity when correlated
- Final severity assigned: LOW / MEDIUM / HIGH

---

## 🧠 Learning From Missed Attacks

SentinelAI uses a **human-in-the-loop learning model**:

1. Analyst reviews suspicious activity
2. Events are labeled as malicious
3. Feedback is stored separately
4. Model is retrained with approved data
5. Detection improves without risk of model poisoning

This approach mirrors real-world SOC and AI governance practices.

---

## 📄 Automated Incident Reporting

The system generates incident reports containing:
- Incident ID
- Detection timestamp
- Severity level
- Summary of detected activity
- MITRE ATT&CK techniques
- Recommended remediation actions

Reports are generated automatically in text format for analyst review.

---

## 📸 Screenshots & Evidence

Include screenshots of:
- Windows Event Viewer showing Event ID 4625
- PowerShell Operational logs with EncodedCommand
- Python detection output
- Generated incident report

---

## 🚀 Future Enhancements

- Elastic SIEM integration
- Real-time log ingestion
- Web dashboard (FastAPI)
- Dockerized deployment
- Cloud log ingestion (Azure/AWS)

---

## 👤 Author

Jaquavious Gotell  
Cybersecurity & Software Engineering Portfolio Project
