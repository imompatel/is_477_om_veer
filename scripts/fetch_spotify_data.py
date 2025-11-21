import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import config

def init_client():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=config.SPOTIFY_CLIENT_ID,
        client_secret=config.SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-read-private"
    ))
    return sp

def search(sp, song, artist):
    q = f"track:{song} artist:{artist}"
    r = sp.search(q=q, type="track", limit=1)
    if r["tracks"]["items"]:
        t = r["tracks"]["items"][0]
        return t["id"]
    return None

def audio(sp, tid):
    f = sp.audio_features([tid])
    if f and f[0]:
        return f[0]
    return None

def fetch(input_file, output_file, sample=None):
    sp = init_client()
    df = pd.read_csv(input_file)

    if "song" in df.columns:
        s_col = "song"
    elif "Song" in df.columns:
        s_col = "Song"
    else:
        print("missing song col")
        return

    if "artist" in df.columns:
        a_col = "artist"
    elif "Artist" in df.columns:
        a_col = "Artist"
    else:
        print("missing artist col")
        return

    u = df.drop_duplicates(subset=[s_col, a_col])
    if sample:
        u = u.sample(sample)

    out = []
    for _, row in u.iterrows():
        sid = search(sp, row[s_col], row[a_col])
        if sid:
            feat = audio(sp, sid)
            if feat:
                out.append({
                    "song": row[s_col],
                    "artist": row[a_col],
                    "spotify_id": sid,
                    "danceability": feat["danceability"],
                    "energy": feat["energy"],
                    "speechiness": feat["speechiness"],
                    "acousticness": feat["acousticness"],
                    "instrumentalness": feat["instrumentalness"],
                    "liveness": feat["liveness"],
                    "valence": feat["valence"],
                    "tempo": feat["tempo"]
                })
        time.sleep(0.3)

    if out:
        pd.DataFrame(out).to_csv(output_file, index=False)
        print("saved")
    else:
        print("no data")

def main():
    fetch(config.BILLBOARD_CLEAN, config.SPOTIFY_RAW, sample=50)

if __name__ == "__main__":
    main()
