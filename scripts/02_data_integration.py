import pandas as pd
import re
from pathlib import Path

def clean_string(s):
    """Cleaning the strings to all match"""
    
    if pd.isna(s):
        return ""
    # Changing Strings to all be or have lowercase, remove special characters, extra spaces
    s = str(s).lower()
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def integrate_data():
    
    """Intergrate the Billboard and Spotify dataset into our coding pipelines"""
    
    print("Data Intergration")
    
    #Load in the Datasets into Pandas
    
    billboard_df = pd.read_csv("data/raw/billboard_hot_100.csv")
    spotify_df = pd.read_csv("data/raw/spotify_songs.csv")
    
    print("\nLoading Datasets")
    print(f"Billboard records: {len(billboard_df):,}")
    print(f"Spotify records: {len(spotify_df):,}")
    
    #Clean both datasets to work
    
    print("\nCleaning datasets")

    def get_col(df, candidates, friendly_name):
        """
        Helper that picks the first column name from `candidates`
        that actually exists in df.columns.
        """
        for c in candidates:
            if c in df.columns:
                return c
        raise KeyError(
            f"Could not find a column for {friendly_name}. "
            f"Tried: {candidates}. Available columns: {list(df.columns)}"
        )

    # Billboard: find song + artist columns, regardless of exact casing/name
    billboard_song_col = get_col(
        billboard_df,
        ["Song", "song", "title", "Track Name", "track_name"],
        "Billboard song",
    )
    billboard_artist_col = get_col(
        billboard_df,
        ["Artist", "artist", "Artist(s)", "artist_name"],
        "Billboard artist",
    )

    billboard_df["song_clean"] = billboard_df[billboard_song_col].apply(clean_string)
    billboard_df["artist_clean"] = billboard_df[billboard_artist_col].apply(clean_string)

    # Spotify: name is consistent
    spotify_df["name_clean"] = spotify_df["name"].apply(clean_string)

    artists_clean = []
    for artist in spotify_df["artists"]:
        raw = str(artist)
        raw = raw.replace("[", "").replace("]", "").replace("'", "")
        artists_clean.append(clean_string(raw))

    spotify_df["artists_clean"] = artists_clean

    print("\nDatasets Cleaned")
    
    #Create key matching for datasets, used to help match object between both datasets after cleaning reformattation
    billboard_df['match_key'] = billboard_df['song_clean'] + '_' + billboard_df['artist_clean']
    spotify_df['match_key'] = spotify_df['name_clean'] + '_' + spotify_df['artists_clean']

    #Merge Datasets together
    
    print("\nMerging Datasets")
    merged_df = billboard_df.merge(
        spotify_df,
        on='match_key',
        how='inner'
    )
    #Print out the merge stats, since not every song on Spotify has Charted on Billboards thus some records won't be shared between each dataset
    print(f"Total matched records: {len(merged_df):,}")
    print(f"Match rate of datasets: {len(merged_df)/len(billboard_df)*100:.2f}% ")
    
    
    # Filtering out unnecessary columns between new merged dataset
    # Kaggle's Billboard chart file uses lowercase / hyphenated names
    billboard_keep_map = {
        "date": "Date",
        "song": "Song",
        "artist": "Artist",
        "rank": "Rank",
        "last-week": "Last Week",
        "peak-rank": "Peak Position",
        "weeks-on-board": "Weeks in Charts",
    }

    # Spotify feature columns we care about
    spotify_keep = [
        "duration_ms", "release_date", "year",
        "acousticness", "danceability", "energy", "instrumentalness",
        "liveness", "loudness", "speechiness", "tempo", "valence",
        "mode", "key", "popularity", "explicit",
    ]

    print("\nFiltering out unnecessary variables from new Merged Dataset")

    # Build list (not set!) of columns to keep
    keep_cols = list(billboard_keep_map.keys()) + spotify_keep

    # Optional: sanity check / warning if something is missing
    missing = [c for c in keep_cols if c not in merged_df.columns]
    if missing:
        print("  Warning: the following expected columns are missing in merged_df:")
        for m in missing:
            print(f"    - {m}")
        # Keep only the columns that actually exist
        keep_cols = [c for c in keep_cols if c in merged_df.columns]

    integrated_df = merged_df[keep_cols].copy()

    # Rename Billboard columns to nicer names
    integrated_df = integrated_df.rename(columns=billboard_keep_map)

    # Convert Date column to datetime
    integrated_df["Date"] = pd.to_datetime(integrated_df["Date"])

    # Creating Binary Targets for overall song performance
    integrated_df["reached_top_10"] = (integrated_df["Peak Position"] <= 10).astype(int)
    integrated_df["reached_top_1"] = (integrated_df["Peak Position"] == 1).astype(int)
    
    #Sorting the Dataset with data
    integrated_df = integrated_df.sort_values('Date')

    #Save new updated Integrated Dataset, al
    output_path = Path("data/processed/integrated_data.csv")
    integrated_df.to_csv(output_path, index=False)
    #Final information of Where Integrated dataset is saved to and Statsical inforamtion of Integrated Dataset
    print(f"\nIntegrated data saved to: {output_path}")
    print(f"Final dataset shape: {integrated_df.shape}")
    print(f"Columns: {list(integrated_df.columns)}")
    
    #Creating a Text File highlighting details and summarizing infromation of new Dataset we created for any inquires
    txt_path = Path("data/processed/integration_summary.txt")
    
    with open(txt_path, 'w') as f:
        f.write("Data Integration Summary\n")
        
        f.write(f"Billboard records: {len(billboard_df):,}\n")
        f.write(f"Spotify records: {len(spotify_df):,}\n")
        f.write(f"Matched records: {len(merged_df):,}\n")
        f.write(f"Match rate: {len(merged_df)/len(billboard_df)*100:.2f}%\n")
        f.write(f"\nFinal dataset shape: {integrated_df.shape}\n")
        f.write(f"\nColumns in integrated dataset:\n")
        for col in integrated_df.columns:
            f.write(f"  - {col}\n")
        f.write(f"\nTarget variables created:\n")
        f.write(f"  - reached_top_10: {integrated_df['reached_top_10'].sum():,} songs\n")
        f.write(f"  - reached_top_1: {integrated_df['reached_top_1'].sum():,} songs\n")

    print(f"Integration summary saved to: {txt_path}")

    return integrated_df

if __name__ == "__main__":
    integrate_data()