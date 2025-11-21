import pandas as pd
import config

def load_data():
    if not config.BILLBOARD_CLEAN.exists():
        print("missing billboard")
        return None, None
    if not config.SPOTIFY_CLEAN.exists():
        print("missing spotify")
        return None, None

    b = pd.read_csv(config.BILLBOARD_CLEAN)
    s = pd.read_csv(config.SPOTIFY_CLEAN)
    return b, s

def exact(b, s):
    if "song_id" not in b.columns or "song_id" not in s.columns:
        print("missing song_id")
        return None
    m = b.merge(s, on="song_id", how="inner")
    return m

def integrate(b, s):
    m = exact(b, s)
    return m

def save(df):
    df.to_csv(config.INTEGRATED_DATA, index=False)
    print("saved")

def main():
    b, s = load_data()
    if b is None:
        return
    out = integrate(b, s)
    if out is not None:
        save(out)
    else:
        print("no matches")

if __name__ == "__main__":
    main()
