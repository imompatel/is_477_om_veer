import pandas as pd
from pathlib import Path
import hashlib
import config

def checksum(file):
    h = hashlib.sha256()
    with open(file, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            h.update(block)
    return h.hexdigest()

def load_billboard():
    if config.BILLBOARD_RAW.exists():
        print("billboard file found")
        df = pd.read_csv(config.BILLBOARD_RAW)
        print(len(df))
        print(list(df.columns))
        return df
    else:
        print("missing billboard file")
        return None

def save_checksum():
    c = checksum(config.BILLBOARD_RAW)
    out = config.BILLBOARD_RAW.parent / "billboard_hot_100.csv.sha256"
    with open(out, "w") as f:
        f.write(c)
    print("checksum saved")

def main():
    df = load_billboard()
    if df is None:
        return
    save_checksum()
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        print(df["Date"].min(), df["Date"].max())

if __name__ == "__main__":
    main()
