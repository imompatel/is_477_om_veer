

import pandas as pd
import numpy as np
import sys
from pathlib import Path
import config

def load_billboard_data(filepath):
    print(f"Loading data from: {filepath}")
    df = pd.read_csv(filepath, low_memory=False)
    print(f"✓ Loaded {len(df):,} rows, {len(df.columns)} columns")
    return df

def profile_data(df, stage="Initial"):
    print(f"\n{'=' * 70}")
    print(f"{stage} Data Profile")
    print('=' * 70)
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print(f"\nColumn data types:")
    print(df.dtypes)

    print(f"\nMissing values:")
    missing = df.isnull().sum()
    if missing.any():
        for col, count in missing[missing > 0].items():
            print(f"  {col}: {count:,} ({count/len(df)*100:.2f}%)")
    else:
        print("  None")

    print(f"\nDuplicate rows: {df.duplicated().sum():,}")

def normalize_text(text):
    if pd.isna(text):
        return text
    text = str(text).strip()
    text = ' '.join(text.split())  
    return text

def clean_billboard_data(df):
   
    print("\n" + "=" * 70)
    print("CLEANING OPERATIONS")
    print("=" * 70 + "\n")

    df_clean = df.copy()
    initial_rows = len(df_clean)

    print("Step 1: Column standardization")

    case_mapping = {}
    for col in df_clean.columns:
        lower_col = col.lower().replace(' ', '_')
        if lower_col != col:
            case_mapping[col] = lower_col

    if case_mapping:
        df_clean.rename(columns=case_mapping, inplace=True)
        print(f"  ✓ Normalized column names to lowercase")
        for old, new in case_mapping.items():
            print(f"    - '{old}' → '{new}'")

    column_mapping = {
        'chart_date': 'date',
        'chart-date': 'date',
        'song-name': 'song',
        'artist-name': 'artist',
        'peak-rank': 'peak_position',
        'peak_position': 'peak_position',
        'weeks-on-board': 'weeks_on_chart',
        'weeks_in_charts': 'weeks_on_chart',
        'last-week': 'last_week',
        'last_week': 'last_week',
        'this-week': 'current_rank',
        'rank': 'current_rank',
        'image_url': 'image_url' 
    }

    for old_col, new_col in column_mapping.items():
        if old_col in df_clean.columns and old_col != new_col:
            df_clean.rename(columns={old_col: new_col}, inplace=True)
            print(f"  ✓ Renamed '{old_col}' to '{new_col}'")

    print("\nStep 2: Date standardization")
    date_col = None
    for col in ['date', 'chart_date', 'week']:
        if col in df_clean.columns:
            date_col = col
            break

    if date_col:
        df_clean[date_col] = pd.to_datetime(df_clean[date_col], errors='coerce')
        invalid_dates = df_clean[date_col].isna().sum()
        if invalid_dates > 0:
            print(f"  ⚠ Found {invalid_dates} invalid dates - removing rows")
            df_clean = df_clean.dropna(subset=[date_col])
        print(f"  ✓ Date range: {df_clean[date_col].min()} to {df_clean[date_col].max()}")
    else:
        print("  ⚠ No date column found!")

    print("\nStep 3: Text normalization")
    if 'song' in df_clean.columns:
        df_clean['song'] = df_clean['song'].apply(normalize_text)
        print("  ✓ Normalized song names")

    if 'artist' in df_clean.columns:
        df_clean['artist'] = df_clean['artist'].apply(normalize_text)
        df_clean['artist'] = df_clean['artist'].str.replace(' Featuring ', ' feat. ', case=False)
        df_clean['artist'] = df_clean['artist'].str.replace(' ft. ', ' feat. ', case=False)
        df_clean['artist'] = df_clean['artist'].str.replace(' ft ', ' feat. ', case=False)

    critical_columns = ['song', 'artist']
    available_critical = [col for col in critical_columns if col in df_clean.columns]

    if available_critical:
        before = len(df_clean)
        df_clean = df_clean.dropna(subset=available_critical)
        removed = before - len(df_clean)
        if removed > 0:
            print(f"  ✓ Removed {removed:,} rows with missing song/artist")
        else:
            print("  ✓ No rows with missing song/artist")

    before = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    removed = before - len(df_clean)

    if 'song' in df_clean.columns and 'artist' in df_clean.columns:
        df_clean['song_id'] = (
            df_clean['song'].str.lower().str.replace('[^a-z0-9]', '', regex=True) +
            '_' +
            df_clean['artist'].str.lower().str.replace('[^a-z0-9]', '', regex=True)
        )

    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if col in ['current_rank', 'peak_position', 'last_week']:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
          

    return df_clean

def save_cleaned_data(df, output_file):
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    

def main():


    if not config.BILLBOARD_RAW.exists():
        
        sys.exit(1)

    df_raw = load_billboard_data(config.BILLBOARD_RAW)

    profile_data(df_raw, stage="Initial")

    df_clean = clean_billboard_data(df_raw)

    profile_data(df_clean, stage="Cleaned")

    save_cleaned_data(df_clean, config.BILLBOARD_CLEAN)

    print("\n" + "=" * 70)
    print("✓ Billboard data cleaning completed successfully!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
