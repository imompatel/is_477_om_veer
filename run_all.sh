#!/bin/bash

echo "Running Billboard-Spotify pipeline"

python scripts/fetch_billboard_data.py
python scripts/clean_billboard.py
python scripts/fetch_spotify_data.py
python scripts/clean_spotify.py
python scripts/integrate_datasets.py

echo "Done"
