import pandas as pd
import sys
from pathlib import Path
import config

def load_spotify_data(filepath):
    print("loading spotify data")
    return pd.read_csv(filepath)

def clean_spotify(df):
    print("cleaning spotify data")
    return df

def save_cleaned(df, out):
    df.to_csv(out, index=False)

def main():
    if not config.SPOTIFY_RAW.exists():
        print("no raw spotify file")
        sys.exit(1)
    df = load_spotify_data(config.SPOTIFY_RAW)
    df_clean = clean_spotify(df)
    save_cleaned(df_clean, config.SPOTIFY_CLEAN)

if __name__ == "__main__":
    main()
