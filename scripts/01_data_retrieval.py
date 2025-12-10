import os
import hashlib
from pathlib import Path

import pandas as pd
import kagglehub
import shutil

def cal_checksum(filepath: Path) -> str:
    #Returns the SHA-256 checksum for file, used to verify later
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for i in iter(lambda: f.read(4096), b""):
            sha256_hash.update(i)
    return sha256_hash.hexdigest()

def download_kaggle_dataset(target_path: Path, kaggle_id: str, kaggle_file: str | None):
    """
    Download a dataset from Kaggle using kagglehub and copy a CSV file
    into our data/raw folder as target_path.

    If kaggle_file is provided, we *try* to use that name first.
    If it doesn't exist, we fall back to "any CSV in the download dir".
    """
    print(f"Status: Not Found - trying Kaggle API download")
    print(f"  Kaggle dataset: {kaggle_id}")
    try:
        kaggle_dir = Path(kagglehub.dataset_download(kaggle_id))

        # First try the explicit filename (if given)
        candidates = []
        if kaggle_file is not None:
            src = kaggle_dir / kaggle_file
            if src.exists():
                candidates = [src]
            else:
                print(f"  Warning: expected file '{kaggle_file}' not found in {kaggle_dir}")
                print(f"  Searching for any .csv files instead...")

        # If no explicit match, search for CSVs in the dataset folder
        if not candidates:
            candidates = list(kaggle_dir.rglob("*.csv"))

        if not candidates:
            print(f"  ERROR: No .csv files found in Kaggle directory: {kaggle_dir}")
            return False

        # Choose the largest CSV file (usually the main dataset)
        src = max(candidates, key=lambda p: p.stat().st_size)
        print(f"  Using '{src.name}' from Kaggle and copying to '{target_path.name}'")

        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target_path)
        print(f"  Downloaded to: {target_path}")
        return True

    except Exception as e:
        print(f"  ERROR: Kaggle download failed -> {e}")
        return False
    
def verify_data():
    print("Data Rethirval Verification")
    
    data_dir = Path("data/raw")
    
    data_sources = {
        "billboard_hot_100.csv": {
            "description": "Billboard Hot 100 chart data",
            "source": "Kaggle dataset - Billboard Hot 100 songs",
            "url": "https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs",
            "license": "Public Domain / Open Data",
            "kaggle_id": "dhruvildave/billboard-the-hot-100-songs",
            "kaggle_file": "billboard_hot_100.csv",
        },
        "spotify_songs.csv": {
            "description": "Spotify Dataset 1921-2020, 600k+ Tracks",
            "source": "Kaggle dataset - Spotify songs",
            "url": "https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks",
            "license": "CC0: Public Domain",
            "kaggle_id": "yamaerenay/spotify-dataset-19212020-600k-tracks",
            "kaggle_file": "spotify_songs.csv",
        },
    }
    
    results = {}

    for file, info in data_sources.items():
        filepath = data_dir / file
        
        #information print out, so you can verify when running
        
        print(f"\n{file}:")
        print(f"  Description: {info['description']}")
        print(f"  Source:      {info['source']}")
        print(f"  URL:         {info['url']}")
        print(f"  License:     {info['license']}")
        
        
        if not filepath.exists():
            ok = download_kaggle_dataset(
                target_path=filepath,
                kaggle_id=info["kaggle_id"],
                kaggle_file=info["kaggle_file"],
            )
            if not ok or not filepath.exists():
                print("  Status: Still missing after Kaggle request")
                results[file] = {"status": "missing"}
                continue
        
        #After this code excutes the file should exist, now we do checksum and get file size to verify in MB
        
        checksum = cal_checksum(filepath)
        size_file = os.path.getsize(filepath) / (1024**2)
        
        #Sanity Check with panda to make sure file is correct
        
        df = pd.read_csv(filepath)

        print("  Status: ✓ Found")
        print(f"  SHA-256: {checksum}")
        print(f"  Size:    {size_file:.2f} MB")
        print(f"  Rows:    {len(df):,}")
        print(f"  Columns: {len(df.columns)}")
        
        """record this in results to make future refrence this process was sucessful"""
        
        results[file] = {
            "status": "success",
            "checksum": checksum,
            "rows": len(df),
            "columns": len(df.columns),
            "size_file": size_file,
        }
        
    print("VERIFICATION COMPLETE")

    #File metadata writen out with raw data
        
    metadata_path = data_dir / "data_sources.txt"
    with open(metadata_path, "w") as f:
        f.write("DATA SOURCES AND CHECKSUMS\n")
        for file, file_info in data_sources.items():
            f.write(f"{file}:\n")
            f.write(f"  Description: {file_info['description']}\n")
            f.write(f"  Source:      {file_info['source']}\n")
            f.write(f"  URL:         {file_info['url']}\n")
            f.write(f"  License:     {file_info['license']}\n")
            if file in results and results[file]["status"] == "success":
                r = results[file]
                f.write(f"  SHA-256:    {r['checksum']}\n")
                f.write(f"  Size:       {r['size_file']:.2f} MB\n")
                f.write(f"  Rows:       {r['rows']:,}\n")
                f.write(f"  Columns:    {r['columns']}\n")
            f.write("\n")

    print(f"\nMetadata saved to: {metadata_path}")

    return results        
        
        
if __name__ == "__main__":
    verify_data()
        
        