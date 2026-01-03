import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

BASE_DATA_PATH = "C:/SentinelAI/data/combined_logs.csv"
FEEDBACK_PATH = "C:/SentinelAI/data/feedback/analyst_feedback.csv"
MODEL_PATH = "C:/SentinelAI/models/isolation_forest.pkl"

os.makedirs("C:/SentinelAI/models", exist_ok=True)

def retrain():
    base_df = pd.read_csv(BASE_DATA_PATH)
    feedback_df = pd.read_csv(FEEDBACK_PATH)

    # Only use malicious feedback
    feedback_df = feedback_df[feedback_df["label"] == "malicious"]

    training_df = pd.concat([base_df, feedback_df], ignore_index=True)

    features = training_df[["hour", "failed_count", "encoded_command", "script_block"]]

    model = IsolationForest(
        contamination=0.15,  # Adjusted after feedback
        random_state=42
    )

    model.fit(features)
    joblib.dump(model, MODEL_PATH)

    print("Model retrained using analyst feedback.")
    print(f"Training samples: {len(training_df)}")

if __name__ == "__main__":
    retrain()
