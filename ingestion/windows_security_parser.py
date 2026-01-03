import pandas as pd

SECURITY_EVENTS = {
    4624: "Successful Logon",
    4625: "Failed Logon",
    4634: "Logoff",
    4740: "Account Lockout"
}

def parse_security_log(path):
    df = pd.read_csv(path)

    df["event_type"] = df["Id"].map(SECURITY_EVENTS)
    df["is_failed"] = df["Id"] == 4625
    df["is_success"] = df["Id"] == 4624
    df["hour"] = pd.to_datetime(df["TimeCreated"]).dt.hour

    # Feature: brute-force indicator
    df["failed_count"] = df["is_failed"].astype(int)

    return df[["TimeCreated", "Id", "event_type", "hour", "failed_count"]]

if __name__ == "__main__":
    df = parse_security_log("C:/SentinelAI/data/windows_logs/security.csv")
    print(df.head())
