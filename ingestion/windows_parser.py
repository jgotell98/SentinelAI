# ingestion/windows_parser.py
import pandas as pd

def parse_windows_log(file_path):
    df = pd.read_csv(file_path)
    df["is_failed"] = df["EventID"] == 4625
    return df[["TimeCreated", "EventID", "is_failed"]]

if __name__ == "__main__":
    df = parse_windows_log("../data/windows_logs/security.csv")
    print(df.head())
