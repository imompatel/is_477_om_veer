
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
CLEANED_DATA_DIR = DATA_DIR / "cleaned"
INTEGRATED_DATA_DIR = DATA_DIR / "integrated"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
CLEANED_DATA_DIR.mkdir(parents=True, exist_ok=True)
INTEGRATED_DATA_DIR.mkdir(parents=True, exist_ok=True)

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

BILLBOARD_DATASET_URL = "https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs"

BILLBOARD_RAW = RAW_DATA_DIR / "billboard_hot_100.csv"
SPOTIFY_RAW = RAW_DATA_DIR / "spotify_features.csv"
BILLBOARD_CLEAN = CLEANED_DATA_DIR / "billboard_cleaned.csv"
SPOTIFY_CLEAN = CLEANED_DATA_DIR / "spotify_cleaned.csv"
INTEGRATED_DATA = INTEGRATED_DATA_DIR / "integrated_billboard_spotify.csv"

SPOTIFY_API_RATE_LIMIT = 30  # requests per minute
FUZZY_MATCH_THRESHOLD = 85  # for string matching (0-100)
