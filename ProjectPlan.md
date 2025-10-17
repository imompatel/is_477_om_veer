1. Overview

The goal of this project is to analyze the evolution of popular music and determine what makes a song a Billboard Hot 100 hit. By combining data from two sources — the Billboard Hot 100 Historical Dataset and Spotify's Web API audio features — we can determine how musical attributes such as tempo, danceability, and energy contribute to chart success.

By combining decades' worth of Billboard chart behavior with quantitative audio features from Spotify, this project will seek to identify patterns that explain why some songs become commercially successful while others do not. Additionally, it will examine whether and to what extent these "hit song" characteristics have changed since the 1960s to the current streaming era.

The project will cover the entire data lifecycle, from acquisition through cleaning, integration, and quality checking to reproducible analysis. The final deliverables are an integrated dataset, statistical findings, and visualizations that are clear evidence of popular music evolution.

2. Research Questions

A.)What specific musical attributes (such as danceability, energy, tempo, and valence) are most strongly associated with higher chart performance on the Billboard Hot 100?

B.)How have these key musical features evolved across decades (1960s–2020s)?

C.)Are there measurable differences between “hit” songs in the pre-streaming era and the modern digital/streaming era?

D.)Is there a relationship between a song’s audio profile and its longevity on the charts (measured by weeks on the chart)?

3. Team Responsibilities

Om - Data Inegration and Analysis Lead

  -Acquire Billboard and Spotify Datasets
  
  -Write Python Scripts for cleaning, merging, and enriching datasets
  
  -Ensure reproducibility, workflow automation, and documentation
  
Veer - Documentation and Visualization Lead

  -Develop visualizations (time trends, correlations, and decade comparisons)
  
  -Manage project documentation
  
  -Create and format visual deliverables for presentation and submission

4. Data Sources

Billboard Hot 100 Historical Dataset

Source: Kaggle – “Billboard Hot 100 & More”

License: Creative Commons BY-NC-SA 4.0 (non-commercial use permitted)

Coverage: 1963 – Present (updated weekly)

Format: Comma-separated values (CSV)

Key Fields: date, title, artist, rank, last_week, peak_pos, weeks_on_chart, image_url

The Billboard dataset represents the dependent variable in our analysis—the measurable indicator of success. It captures the performance of thousands of songs over six decades, providing a context for comparing changes in musical trends.


Spotify Web API Audio Features

Source: Spotify Developer Web API

Access: Client Credentials Flow 

Format: JSON responses converted to tabular form

Selected Attributes:

danceability – suitability for dancing (0–1)

energy – intensity and activity (0–1)

tempo – beats per minute

valence – musical positivity (0–1)

acousticness, speechiness, instrumentalness, liveness – compositional traits

popularity – Spotify’s engagement score

more variables to test out if needed.

Spotify provides a unique quantitative representation of sound, enabling objective comparison of musical styles across time. This will be used to identify the driving factors of success, whether it be a song's danceability, the time, or even the tempo. This will be used to find the accurate correlation for all the questions we have.

6. Timeline
- The following is our projected timeline:

**Week 1:** We'll work on extracting the Spotify API and converting the data into a dataframe into what variables we would require, as mentioned above. Then we will match the Billboard entries to Spotify tracks using artist and title fuzzy matching.
  
**Week 2 (Oct 27 - Nov 3):** Clean the data sets by removing duplicates and/or missing values. making sure that our table is in a unified table with one row per song containing both chart and audio metrics

**Week 3 (Nov 3 - Nov 10):** perform various statistical measures to understand the data size, variability, and an overall summary. Vizualize long-term trends across the decades using lineplots and heatmaps. Finally, looking at the correlation between certain attributes and billboard ranks.

**Week 4 (Nov 10 - Nov 17):** Work on the intermediate report, highlighting the project's direction, goal and insights gained so far. Working on modelling, such as regression (multiple and logistic) and maybe random forests to get different accuracies and better understanding.

**Week 5 (Nov 17- Nov 24):** Create a clear and concise visualization using matplotlib and seaborn to show the musical evolution. Also finalizing the documentation and preparing the repository for submission.

**Week 6 (Nov 24 - Dec 1):** Go to Office hours and go through our project and see if we missed any aspect, and how we can maybe improve our model. Compile findings and push all material to GitHub.
  
7. Constraints
Some constraints we expect to run into are as follows:
- **API Rate Limits:** Spotify's Web API has request limits (typically 100 calls/minute), which may slow data collection for large data sets.
- **Licensing Restriction:** The Billboard dataset is under non-commercial terms, so we have to make sure that we aren't using/giving this data to give to a third party.
- **Data matching Limitation:** Song title/artist mismatch between Billboard and Spotify may lead to missing records.
- **Resources:** Handling large datasets and processing extensive audio feature data may demand more efficient Python optimization.

8. Gaps
- **Incomplete data between data sets:** Some Billboard records lack exact release dates or artist IDs needed for accurate Spotify lookups.
- **Model Selection:** Still don't have a clear idea of which model to use to perform the necessary prediction, so we will have to first have to conduct our initial exploratory.
- **Streaming Era:** learning and defining the transition between the "pre-streaming" and post-streaming era is necessary, so maybe creating a cutoff year that accurately represents that can be looked into.
