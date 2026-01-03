# ingestion/linux_parser.py
import pandas as pd
import re

def parse_auth_log(file_path):
    rows = []
    with open(file_path, "r") as f:
        for line in f:
            if "sshd" in line:
                rows.append({
                    "raw": line,
                    "failed": "Failed password" in line,
                    "timestamp": line[:15]
                })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = parse_auth_log("../data/linux_logs/auth.log")
    print(df.head())
