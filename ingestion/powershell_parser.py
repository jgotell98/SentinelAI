import pandas as pd

def parse_powershell_log(path):
    df = pd.read_csv(path)

    df["encoded_command"] = df["Message"].str.contains("EncodedCommand", na=False)
    df["script_block"] = df["Id"].isin([4103, 4104])

    return df[["TimeCreated", "Id", "encoded_command", "script_block"]]

if __name__ == "__main__":
    df = parse_powershell_log("C:/SentinelAI/data/windows_logs/powershell.csv")
    print(df[df["encoded_command"]].head())
