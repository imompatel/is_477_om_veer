# 1. Updates
## Data Acquisition (Completed)
data/raw/billboard_hot_100.csv

scripts/fetch_spotify_data.py

### Update:
* Retrieved Billboard dataset (1963–2022) from Kaggle under CC license.
* Pulled Spotify audio features for Top 100 songs (2000–2022) using the Web API.

## Data Cleaning (In progress)
data/cleaned/billboard_cleaned.csv

### Update:
* Cleaned the Billboard dataset, but we are planning to segment the data more based on time, specifically from 2000 to 2022 to match our Spotify data

## Attributes to perform analysis:
### Update:
* Initial plan included ~10 Spotify features, but missing/inconsistent values made the scope too large.
So we decided the following:
  * Quantitative attribute: Danceability (candidate)
  * Qualitative attribute: Genre
#### This reduced noise and made analysis reproducible and manageable.

### Overall Updates:

We identified the Billboard HOT 100 & more Kaggle dataset, which has an open and public License through Creative Commons and has a DOI citation as well. Hence, we decided to go with that dataset, which included data from 1963 - 2022. We are using this data to find attributes like Danceability, Tempo, Time, Genre etc., through which we want to compare to Spotify's API to retrieve its top 100 songs from 2000 - 2025 and see how music has changed over time and what attributes correlate with higher chart performance. <br> <br> While that was the original plan was to test danceability, energy, tempo, valence, acousticness, speechiness, instrumentalness, liveness (compositional traits)
and popularity, as we started pulling data, we realized that there is a lot of data and attributes that would need to be cleaned up, and that would make our data almost impossible to use. Hence, we are now deciding to go with one quantitative data attribute (like danceability or time) and a qualitative data attribute (like genre).

# 2. Updated Timeline
### Week 1 (Completed):
Selected Billboard & Spotify datasets, realized original scope was too large → narrowed to 1 quantitative attribute (danceability) and 1 qualitative attribute (genre)
and retrieved initial Spotify + Billboard data

### Week 2 (Nov 18–Nov 24) In Progress: 
Clean both datasets (remove duplicates, fix titles/artists, standardize genres). Choose the final two attributes and begin merging Billboard and Spotify using fuzzy matching

### Week 3 (Nov 24–Dec 1) Not Started: 
Finish dataset merge and run basic descriptive statistics. Create simple visuals (histograms, line charts, bar charts) and also work on storage and organization strategy

### Week 4 (Dec 1–Dec 7) Not Started: 
Analyze relationships between attributes and chart rank and work on an automated end-to-end workflow while making sure all the content is reproducible enough,
Lastly, go through the checklist and main requirements and make sure everything is cleaned and ready to submit
