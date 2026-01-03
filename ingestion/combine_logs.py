import pandas as pd
from windows_security_parser import parse_security_log
from powershell_parser import parse_powershell_log

def combine():
    sec = parse_security_log("C:/SentinelAI/data/windows_logs/security.csv")
    ps = parse_powershell_log("C:/SentinelAI/data/windows_logs/powershell.csv")

    # Normalize columns
    sec["encoded_command"] = 0
    sec["script_block"] = 0

    ps["failed_count"] = 0
    ps["hour"] = pd.to_datetime(ps["TimeCreated"]).dt.hour
    ps["event_type"] = "PowerShell Activity"

    combined = pd.concat([sec, ps], ignore_index=True).fillna(0)
    combined.to_csv("C:/SentinelAI/data/combined_logs.csv", index=False)

    return combined

if __name__ == "__main__":
    df = combine()
    print(df.head())
