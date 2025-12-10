# Data Dictionary

## Integrated Dataset

This document describes the structure and content of the integrated dataset combining Billboard Hot 100 chart data with Spotify song features.

### Dataset Overview

- **Files**: 
  - `data/processed/integrated_data.csv` (after integration)
  - `data/processed/cleaned_data.csv` (after cleaning)
- **Description**: Integrated dataset of Billboard Hot 100 songs with Spotify audio features
- **Time Period**: 1958-2020
- **Record Type**: Song chart entry
- **Total Records**: ~223,185 (after integration)
- **Match Rate**: ~63.7% of Billboard songs matched with Spotify data

---

## Column Descriptions

### Billboard Chart Data

| Column | Type | Description | Values/Range | Notes |
|--------|------|-------------|--------------|-------|
| `Date` | datetime | Date of chart entry | 1958-08-06 to 2020-12-31 | Week of chart appearance |
| `Song` | string | Song title | Text | Normalized for matching |
| `Artist` | string | Artist name | Text | May include featured artists |
| `Rank` | integer | Chart position for this week | 1-100 | Lower is better |
| `Last Week` | integer | Previous week's chart position | 0-100 or null | 0 indicates new entry |
| `Peak Position` | integer | Highest position achieved | 1-100 | Across all weeks |
| `Weeks in Charts` | integer | Number of weeks on chart | 1+ | Cumulative count |

**Source**: Billboard Hot 100 Charts  
**Original Dataset**: dhruvildave/billboard-the-hot-100-songs (Kaggle)  
**License**: Public Domain / Open Data

---

### Spotify Audio Features

#### Track Metadata

| Column | Type | Description | Values/Range | Notes |
|--------|------|-------------|--------------|-------|
| `duration_ms` | integer | Track duration in milliseconds | Positive integer | Typical: 180,000-300,000 ms |
| `release_date` | string | Release date | Date string | Format varies by source |
| `year` | integer | Release year | 1921-2020 | May differ from chart date |
| `popularity` | integer | Spotify popularity score | 0-100 | Higher = more popular |
| `explicit` | integer | Contains explicit content | 0 or 1 | 1 = explicit |

#### Musical Features (Normalized 0.0-1.0)

| Column | Type | Description | Values/Range | Interpretation |
|--------|------|-------------|--------------|----------------|
| `acousticness` | float | Confidence of acoustic sound | 0.0-1.0 | 1.0 = highly acoustic |
| `danceability` | float | Suitability for dancing | 0.0-1.0 | Based on tempo, rhythm, beat |
| `energy` | float | Intensity and activity | 0.0-1.0 | Fast, loud, noisy = high |
| `instrumentalness` | float | Predicts no vocals | 0.0-1.0 | >0.5 likely instrumental |
| `liveness` | float | Presence of live audience | 0.0-1.0 | >0.8 likely live |
| `speechiness` | float | Presence of spoken words | 0.0-1.0 | >0.66 likely speech/podcast |
| `valence` | float | Musical positiveness | 0.0-1.0 | High = happy, Low = sad |

#### Musical Properties (Non-normalized)

| Column | Type | Description | Values/Range | Notes |
|--------|------|-------------|--------------|-------|
| `loudness` | float | Overall loudness | -60 to 0 dB | Typical: -15 to -5 dB |
| `tempo` | float | Estimated tempo | 0-250 BPM | Typical: 60-200 BPM |
| `mode` | integer | Musical mode | 0 or 1 | 0 = minor, 1 = major |
| `key` | integer | Pitch class | 0-11 | 0=C, 1=C#/Db, 2=D, etc. |

**Source**: Spotify Web API  
**Original Dataset**: yamaerenay/spotify-dataset-19212020-600k-tracks (Kaggle)  
**License**: CC0: Public Domain

---

### Derived Variables (Analysis)

| Column | Type | Description | Values/Range | Purpose |
|--------|------|-------------|--------------|---------|
| `reached_top_10` | integer | Binary: reached top 10 | 0 or 1 | Target variable for ML |
| `reached_top_1` | integer | Binary: reached #1 | 0 or 1 | Alternative target |

---

### Engineered Features (Created During Analysis)

| Column | Type | Description | Formula | Purpose |
|--------|------|-------------|---------|---------|
| `energy_loudness` | float | Energy-loudness interaction | `energy × loudness` | Intensity measure |
| `energy_danceability` | float | Energy-dance interaction | `energy × danceability` | Upbeat factor |
| `positive_energy` | float | Happy energetic songs | `valence × energy` | Mood indicator |
| `vocal_prominence` | float | Vocal presence | `speechiness × (1 - instrumentalness)` | Vocal strength |
| `tempo_normalized` | float | Normalized tempo | `(tempo - 120) / 60` | Tempo relative to average |

---

## Detailed Feature Definitions

### Spotify Audio Feature Explanations

**Acousticness** (0.0-1.0)  
A confidence measure of whether the track is acoustic. 1.0 represents high confidence the track is acoustic (no electric instruments).
- **Low (0.0-0.3)**: Electronic, synthesized
- **Medium (0.3-0.7)**: Mixed acoustic/electric
- **High (0.7-1.0)**: Primarily acoustic instruments

**Danceability** (0.0-1.0)  
How suitable a track is for dancing based on tempo, rhythm stability, beat strength, and regularity. Combines multiple musical elements.
- **Low (0.0-0.4)**: Irregular rhythm, slow
- **Medium (0.4-0.7)**: Moderate danceability
- **High (0.7-1.0)**: Strong, regular beat

**Energy** (0.0-1.0)  
Perceptual measure of intensity and activity. Energetic tracks feel fast, loud, and noisy. Represents dynamic range, perceived loudness, timbre, onset rate, and general entropy.
- **Low (0.0-0.4)**: Calm, soft
- **Medium (0.4-0.7)**: Moderate intensity
- **High (0.7-1.0)**: Fast, loud, intense

**Instrumentalness** (0.0-1.0)  
Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental. Rap or spoken word tracks are clearly "vocal".
- **<0.5**: Contains significant vocals
- **>0.5**: Likely instrumental
- **>0.8**: Very likely no vocals

**Liveness** (0.0-1.0)  
Detects the presence of an audience in the recording. Higher values represent increased probability that the track was performed live.
- **<0.8**: Studio recording
- **>0.8**: Likely live performance

**Loudness** (-60 to 0 dB)  
Overall loudness in decibels (dB). Averaged across the entire track. Useful for comparing relative loudness of tracks.
- **Quiet**: < -15 dB
- **Average**: -10 to -5 dB
- **Loud**: > -5 dB

**Speechiness** (0.0-1.0)  
Detects the presence of spoken words.
- **<0.33**: Music (minimal speech)
- **0.33-0.66**: May contain both music and speech (e.g., rap)
- **>0.66**: Probably made entirely of spoken words (podcast, audiobook)

**Tempo** (BPM)  
Overall estimated tempo in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece.
- **Slow**: < 90 BPM
- **Moderate**: 90-120 BPM
- **Fast**: > 120 BPM

**Valence** (0.0-1.0)  
Musical positiveness conveyed by a track. Tracks with high valence sound more positive (happy, cheerful, euphoric), while tracks with low valence sound more negative (sad, depressed, angry).
- **Negative**: 0.0-0.4 (sad, angry)
- **Neutral**: 0.4-0.6
- **Positive**: 0.6-1.0 (happy, cheerful)

**Mode** (0 or 1)  
Modality (major or minor) of a track. Type of scale from which melodic content is derived.
- **0**: Minor (often sounds sad)
- **1**: Major (often sounds happy)

**Key** (0-11)  
The key the track is in using standard Pitch Class notation.
- **0**: C
- **1**: C♯/D♭
- **2**: D
- **3**: D♯/E♭
- **4**: E
- **5**: F
- **6**: F♯/G♭
- **7**: G
- **8**: G♯/A♭
- **9**: A
- **10**: A♯/B♭
- **11**: B

---

## Data Quality Notes

### Completeness
- **Critical variables**: 100% complete after cleaning (Song, Artist, Rank, audio features)
- **Optional variables**: Some missing values in `Last Week` (new entries), filled with 0

### Data Cleaning Applied
1. **Missing Values**: Dropped rows with missing critical features; filled non-critical with median
2. **Duplicates**: Removed 232+ duplicate entries
3. **Outliers**: Capped tempo, loudness, and duration at 1st and 99th percentiles
4. **Range Validation**: Ensured all bounded features (0-1) are within valid ranges
5. **Type Conversion**: Standardized integer and float types

### Match Process
Songs matched between datasets using:
- Normalized song titles (lowercase, removed punctuation)
- Normalized artist names (lowercase, removed punctuation)
- Combined match key: `song_clean + '_' + artist_clean`

**Limitations**:
- Not all Billboard songs have Spotify matches (~36% unmatched), Not all songs are uploaded to Spotify
- Multiple versions of same song may exist
- Artist name variations can prevent matches
- Older songs less likely to have Spotify data

---

## Data Files

### Raw Data
- `data/raw/billboard_hot_100.csv` - Billboard chart data (330,087 entries)
- `data/raw/spotify_songs.csv` - Spotify audio features (586,672 tracks)
- `data/raw/data_sources.txt` - Metadata and checksums

### Processed Data
- `data/processed/integrated_data.csv` - Merged Billboard + Spotify (~223,185 entries)
- `data/processed/cleaned_data.csv` - Final cleaned dataset
- `data/processed/integration_summary.txt` - Integration statistics
- `data/processed/quality_report.txt` - Data quality assessment
- `data/processed/cleaning_log.txt` - Cleaning operations log

### Analysis Results
- `results/analysis_results.txt` - Model performance and findings
- `results/figures/*.png` - Visualizations

---

## Usage Examples

### Loading Data
```python
import pandas as pd

# Load cleaned dataset
df = pd.read_csv('data/processed/cleaned_data.csv')

# Parse date column
df['Date'] = pd.to_datetime(df['Date'])

# Display summary
print(df.info())
print(df.describe())
```

### Accessing Specific Features
```python
# Get all audio features
audio_features = ['danceability', 'energy', 'loudness', 'speechiness',
                  'acousticness', 'instrumentalness', 'liveness', 
                  'valence', 'tempo']

X = df[audio_features]
y = df['reached_top_10']
```

---