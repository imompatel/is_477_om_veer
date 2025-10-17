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


5. Plan

6. Timeline

7. Constraints

8. Gaps
