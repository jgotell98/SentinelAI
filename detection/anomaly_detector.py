import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

df = pd.read_csv("C:/SentinelAI/data/combined_logs.csv")

features = df[["hour", "failed_count", "encoded_command", "script_block"]]

MODEL_PATH = "C:/SentinelAI/models/isolation_forest.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(features)

df["anomaly"] = model.fit_predict(features)

alerts = df[df["anomaly"] == -1]
print("Anomalies detected:")
print(alerts.head())

alerts.to_csv("C:/SentinelAI/data/alerts.csv", index=False)
