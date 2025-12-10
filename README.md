# What Makes Songs Chart on the Billboard Hot 100?

## Contributors  
- Om Patel - ompatel2@illinois.edu
- Veer Jain - Veerj2@illinois.edu
---

## Metadata (DataCite-Compatible)

- **Title:** What Makes Songs Chart on Billboard Hot 100?
- **Creator:** Om Patel, Veer Jain (University of Illinois Urbana-Champaign)
- **Description:** A data science analysis integrating Spotify audio features with Billboard chart history to identify predictors of Top 10 chart success.
- **Version:** 1.0 (December 2025)
- **Keywords:** music analytics, Spotify audio features, Billboard Hot 100, machine learning, data integration, feature importance, predictive modeling
- **License:** MIT License (code), CC0/Public Domain (data)
- **Related Identifiers:**  
  - Billboard Dataset — https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs  
  - Spotify Dataset — https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks
  
# Summary  

This project explores the question of what makes a song successful on the Billboard Hot 100 chart by looking at characteristics available through Spotify’s audio feature dataset. The motivation behind the project comes from both a curiosity about the factors that shape music popularity and common interest to learn the factors that make certain songs more trending. The Billboard Hot 100 is considered one of the most influential music charts in the world, and understanding the attributes that distinguish hit songs can offer insight into how musical tastes, production styles, and industry influence evolve over time. While factors like marketing, sponsorship and brand deals are factors that heavily influence the top songs of today's world there are still a lot of quantiative and qualitative factors we could look at to understand how music has evolved and also maybe what new artists could focus on.

The central research question guiding this project is: **Which Spotify audio features are most strongly associated with whether a song reaches the Top 10 on the Billboard Hot 100?** From this question, several secondary questions naturally emerge: How do musical features differ between highly successful songs and those that chart but never break into the Top 10? Are machine learning models able to determine if a song is able to do better than the rest just relying on data and if so which model is the most accurate and apporopriate?

To answer these questions, the project integrates two large datasets: a Kaggle compilation of Billboard Hot 100 chart data from 1958–2020 (doi: https://doi.org/10.34740/kaggle/ds/1211465) , and a Kaggle dataset of Spotify audio features covering over 600,000 tracks originally collected through the Spotify Web API (https://developer.spotify.com/documentation/web-api/reference/get-audio-features, ). After extensive preprocessing, text normalization, integration, and cleaning, the resulting dataset includes over 220,000 matched Billboard–Spotify entries. These matched entries capture both chart performance and measurable musical attributes such as danceability, energy, loudness, valence (positivity), acousticness, and speechiness.

The results of this study show that there is a correlation between chart success and specific Spotify audio features.  Specifically, danceability, loudness, valence, and speechiness consistently show up as characteristics that set the Top 10 songs apart from the rest of the charting dataset.  Both machine learning techniques and visual analysis support these patterns.  Feature importance scores closely matched the observed descriptive differences, and a Random Forest classifier trained on the cleaned dataset predicted whether a song would make it into the Top 10 with about 70% accuracy.  Given the complexity of elements outside the purview of audio features, such as artist reputation, marketing campaigns, cultural timing, and industry support, the outcome is significant even though predictive accuracy is far from perfect.
At the same time, the project findings also emphasize the limitations of relying solely on audio features. The low recall for the Top 10 class and the modest effect sizes for many features highlight that musical characteristics cannot fully explain hit-making. Chart success is a multifaceted phenomenon, and while certain musical patterns are visible, they likely operate alongside non-musical forces. This observation reinforces why thoughtful data curation—including clarifying the limits of data sources—is essential.

Finally, the project demonstrates the importance of careful metadata documentation, ethical considerations, workflow transparency, and reproducibility. By documenting each step of the data lifecycle—from acquisition to analysis—the project ensures that others can understand, critique, and reproduce the work. This commitment to transparency aligns with the FAIR principles and with the expectations of rigorous data management practices.

Overall, the project provides meaningful insight into how quantifiable musical features align with chart performance while illustrating the strengths and challenges of data-driven research in cultural domains.

---

# Data Profile  

This project uses two primary datasets: a Billboard Hot 100 chart dataset and a Spotify audio feature dataset. Both were sourced through Kaggle, but each originates from a fundamentally different creator and comes with unique ethical and legal considerations. This section describes each dataset in detail, including provenance, structure, licensing implications, and limitations.

## **Dataset 1: Billboard Hot 100 Chart History**

The first dataset contains weekly Billboard Hot 100 chart entries from 1958 through 2020. The dataset is publicly available on Kaggle but is derived from Billboard’s own published charts. We treat Billboard as the original creator of the data and Kaggle as a secondary distributor. Because Billboard content is copyrighted, and because the data is aggregated from chart listings rather than directly provided through a public API, the project does not redistribute the dataset. Instead, users must download the CSV directly from Kaggle, ensuring compliance with licensing and fair use.

The Billboard dataset includes approximately 350,000 rows, each representing a single chart appearance of a song during a particular week. Key fields include:

- `date`: the chart week  
- `song`: song title  
- `artist`: performing artist  
- `rank`: chart rank from 1 to 100  
- `peak_position`: highest rank the song achieved  
- `weeks_on_chart`: number of weeks the song has appeared  

From a data curation standpoint, this dataset is relatively clean but includes variability in artist naming conventions, featuring attributions (e.g., “feat.”), capitalization, and punctuation. These inconsistencies become critical during integration with Spotify data, requiring robust string processing and normalization.

### Ethical & Legal Considerations  
Although the data is publicly viewable on Billboard’s website, redistribution is restricted. For this reason:

- The dataset is **not included in the GitHub repository**.  
- Instructions are provided to download it directly from Kaggle.  
- Billboard is cited as the authoritative source of the underlying content.  

The dataset does not contain personal user data, minimizing privacy concerns. Instead, it captures cultural artifacts (song charts) that fall under fair use for analysis when appropriately cited and not redistributed in raw form.

---

## **Dataset 2: Spotify Audio Features**

The second dataset contains audio feature metadata for over 600,000 tracks spanning nearly a century of music. Although hosted on Kaggle, the data originates from the **Spotify Web API**, which allows developers to retrieve descriptive musical attributes for individual tracks. These include both numeric and categorical fields, most notably:

- `danceability`  
- `energy`  
- `loudness`  
- `speechiness`  
- `acousticness`  
- `instrumentalness`  
- `liveness`  
- `valence`  
- `tempo`  
- `duration_ms`  

Spotify describes these features as computationally derived characteristics meant to quantify musical qualities such as rhythmic stability, harmonic content, dynamic intensity, and mood. This dataset does not include any user behavior or streaming data, and thus carries minimal privacy risk.

### Provenance and API Considerations  

Before selecting the Kaggle dataset, the project attempted to reproduce the data directly using Spotify’s Web API. However, several challenges made this impractical:

1. The API is not designed for bulk historical scraping of hundreds of thousands of tracks.  
2. Rate limits severely restrict throughput.  
3. Some endpoints used by the Kaggle dataset’s original creator are no longer supported or require authentication scopes not available for academic scraping.  
4. Spotify's terms of use prohibit large-scale redistribution of raw API responses.  

For these reasons, the Kaggle dataset was selected as a preserved snapshot suitable for analysis, and Spotify is cited as the original upstream provider.

### Ethical & Legal Constraints  

Spotify’s data:

- Is licensed for non-commercial analysis but **cannot be redistributed** in raw form.  
- Contains only track-level metadata, not copyrighted audio or user-level data.  
- Requires attribution to Spotify as the source of the features.  

As with the Billboard dataset, the raw Spotify CSV is not included in the repo and must be downloaded manually.

---

## **Integrated Dataset**

After cleaning and matching song titles and artist names, the integrated dataset contains:

- **223,185 rows** of matched Billboard–Spotify entries  
- **63.7% match rate**  
- Combined metadata and audio features  
- Derived labels such as `reached_top_10` and `reached_top_1`

The integration process required a custom normalization function to remove punctuation, standardize case, reduce spacing inconsistencies, and handle featuring attributions.

This dataset serves as the foundation for quality assessment, cleaning, and analysis.

---

# Data Quality  

Ensuring data quality is a central component of this project, especially because the dataset is assembled from two different sources with differing levels of structure and consistency. The data quality assessment aimed to evaluate completeness, accuracy, validity, consistency, and outlier behavior using both automated profiling and manual inspection.

## **Completeness**

Completeness refers to whether all required variables contain meaningful values. For this project, we defined “critical variables” as song title, artist name, chart date, chart rank, and all Spotify audio features used in modeling. During profiling, we found:

- Billboard data had no missing values in rank or date fields.  
- Spotify data had occasional missing or null values in auxiliary metadata (e.g., key, mode), but **none** in core audio features.  
- After integration, missing values existed only when a Billboard song failed to match a Spotify entry, but unmatched rows were excluded from the modeling dataset.

As a result, the final cleaned dataset is **100% complete** for all fields used in analysis.

---

## **Validity**

Validity checks ensure variables fall within expected domain ranges. The following checks were performed:

- **Rank values** confirmed to be integers between 1 and 100.  
- **Normalized Spotify features** verified to be within [0, 1].  
- **Loudness** values fell within realistic musical production ranges (approximately −60 dB to 0 dB).  
- **Tempo** values were largely between 60–200 BPM; extreme values were evaluated separately.  
- **Duration** values were non-negative and within typical ranges for commercial songs.  

Invalid entries were rare and primarily caused by formatting errors such as stray characters (“-”) or missing numeric codes. These were corrected when possible or removed during cleaning.

---

## **Consistency**

Consistency examines whether the dataset behaves logically according to expectations. We found:

- **232 exact duplicates** in Spotify-derived rows, likely due to redundant Kaggle entries. These were removed.  
- Billboard songs appeared multiple times across weeks, which is expected behavior; these were retained.  
- No contradictions were found between peak position and weekly ranks.

Additionally, the normalized representation of song and artist names required careful consistency checks. Without normalization, matches between Billboard and Spotify entries would fail; with normalization, match rates improved substantially.

---

## **Outliers**

Outlier analysis used the Interquartile Range (IQR) method to identify extreme values in tempo, loudness, duration, and several Spotify features. Key findings:

- Tempo values below 50 BPM and above 230 BPM were flagged as outliers but not necessarily invalid (e.g., ambient tracks vs. electronic tracks).  
- Loudness had a long left tail as expected for dynamic recordings.  
- Duration outliers likely represented extended mixes or short skits.  

Rather than discarding these observations, the project applied **capping at the 1st and 99th percentiles** to retain structure while reducing the effect of extreme values.

---

## **Overall Quality Assessment**

After applying the quality assessment and cleaning procedures, the final dataset can be considered:

- **Complete**  
- **Valid**  
- **Consistent**  
- **Free from problematic outliers** (via capping)  
- **Well-documented** through logs and scripts  

This solid foundation ensures that subsequent analyses reflect underlying patterns rather than noise or artifact.

---

# Findings  

The analysis revealed several meaningful patterns in how audio features relate to Billboard Hot 100 success. Using both descriptive statistics and machine learning models, the project uncovered consistent differences between songs that reached the Top 10 and those that did not.

**Descriptive Comparisons**

Across the integrated dataset, Top 10 songs showed meaningful differences in several Spotify audio features and engineered combinations:

- **Tempo:** Top 10 songs are on average about **2 BPM slower** (–2.04 difference), suggesting that many hits sit slightly below the tempo of non–Top 10 songs.
- **Loudness:** Top 10 songs are about **0.34 dB louder**, pointing to somewhat more polished or aggressive production, though the gap is modest.
- **Energy × Loudness (`energy_loudness`):** This interaction term is **higher for Top 10 songs** (+0.22), capturing that successful tracks tend to combine moderately high energy with higher loudness.
- **Danceability:** Top 10 songs are about **0.03 points more danceable**, reinforcing that rhythm and groove are important for mainstream success.
- **Energy × Danceability (`energy_danceability`):** Also higher for Top 10 songs (+0.018), indicating that hits often balance movement (danceability) with some energetic intensity.
- **Valence:** A small positive difference (+0.0095) suggests Top 10 songs sound **slightly “happier” or more positive** on average.
- **Instrumentalness:** Lower for Top 10 songs (–0.009), consistent with the idea that hits are **more vocal-driven** and less purely instrumental.
- **Energy:** Interestingly, raw energy is **slightly lower** for Top 10 songs (–0.006), implying that extremely high-energy tracks are not strictly necessary for success.
- **Positive Energy (`positive_energy`) & Vocal Prominence (`vocal_prominence`):** Both are slightly higher for Top 10 songs, meaning successful tracks tend to pair moderate energy with positive mood and clear vocals.
- **Tempo Normalized (`tempo_normalized`):** Negative difference (–0.034) again highlights that Top 10 songs lean a bit **below the 120 BPM “reference” tempo**.

These patterns are visualized using boxplots (`feature_distributions.png`) and a correlation heatmap (`correlation_heatmap.png`), which jointly illustrate how Top 10 and non–Top 10 songs differ across both raw and engineered features.

---

## **Correlation Insights**

Some big correlation patterns include:

- **Energy ↔ Loudness:** Strong positive correlation, reflecting standard production practice where more energetic tracks are typically mixed louder.
- **Energy ↔ Acousticness:** Strong negative correlation, indicating that highly acoustic tracks tend to be less energetic, while dense electronic/pop productions are more energetic.
- **Valence ↔ Danceability:** Moderate positive correlation, suggesting that tracks that feel “happier” also tend to be more danceable.

These relationships confirm that the engineered features (e.g., `energy_loudness`, `energy_danceability`, `positive_energy`) are built on meaningful underlying structure in the audio feature space and help explain why they show up as important in the Random Forest and Gradient Boosting models.

---

## **Machine Learning Results**

We evaluated three models to predict whether a song reaches the Top 10 based on its audio features.

### **Random Forest Classifier**

- **Accuracy:** 0.8196  
- **ROC–AUC:** 0.8998  
- Trained on a class-balanced version of the data (using SMOTE), the Random Forest performs best overall, especially at separating Top 10 from non–Top 10 songs.  
- **Top features (by importance):**
  1. **Danceability** (0.1003)
  2. **Energy × Loudness** (`energy_loudness`, 0.0777)
  3. **Acousticness** (0.0756)
  4. **Energy × Danceability** (`energy_danceability`, 0.0755)
  5. **Energy** (0.0731)

These results suggest that not just raw energy and loudness, but their *interaction* with rhythm (danceability) and acoustic profile are strong drivers of chart success.

---

### **Gradient Boosting Classifier**

- **Accuracy:** 0.7534  
- **ROC–AUC:** 0.8372  
- Gradient Boosting also performs well, but slightly below the Random Forest. It confirms similar patterns: songs that combine higher danceability, loudness/energy, and specific vocal characteristics tend to be more successful.  

This model provides an additional, more sequential (stage-wise) perspective on how features contribute to hit potential.

---

### **Logistic Regression**

- **Accuracy:** 0.5565  
- **ROC–AUC:** 0.5872  
- Logistic Regression is less accurate than the tree-based models, but it is **more interpretable**.  
- Key coefficient patterns:
  - **Positive** for `energy_danceability` and `loudness` (these increase the log-odds of reaching Top 10)
  - **Negative** for `energy` and `energy_loudness` (very high energy/loudness combinations may hurt rather than help)
  - Smaller effects for `speechiness`, `vocal_prominence`, and `tempo`-related features

Overall, Logistic Regression confirms the general direction of the descriptive findings but struggles to capture the nonlinear relationships that Random Forest and Gradient Boosting handle more effectively.

---

## **Interpretation**

The results indicate that while Spotify audio features capture meaningful musical attributes associated with chart success, they are insufficient for highly accurate prediction. The modest accuracy reflects the complex, multifaceted nature of hit-making—where marketing, cultural timing, and artist popularity likely dominate musical structure.

---


# Future Work  

While the project successfully demonstrates how audio features correlate with chart performance, it also exposes limitations and opportunities for more comprehensive analysis.

## **1. Improving Record Linkage**

Record linkage proved to be one of the most challenging aspects. Normalization of song and artist names can only capture so much. Future efforts could incorporate:

- Fuzzy matching algorithms (e.g., Jaro-Winkler distance)  
- MusicBrainz or ISRC identifiers to link tracks across datasets  
- Probabilistic linkage frameworks  

Using external identifiers would dramatically increase match accuracy and reduce loss during integration.

---

## **2. Addressing Class Imbalance**

Top 10 songs make up a small proportion of all charting entries. This imbalance limits model performance. To address this:

- Oversampling strategies such as SMOTE could create synthetic examples.  
- Undersampling the majority class might reduce bias but risks losing information.  
- Cost-sensitive modeling would penalize misclassification of the minority class.  

Any of these approaches could help future models place more emphasis on correctly identifying hit songs.

---

## **3. Incorporating Additional Data Sources**

Audio features alone cannot capture the full picture of chart success. Future analyses could include:

- **Streaming volume** or velocity data  
- **Social media metrics** such as TikTok or Twitter trends  
- **Radio airplay statistics**  
- **Artist-level variables**, including career length, prior hits, and label affiliation  
- **Genre classification**, which may explain many audio feature patterns  

The integration of multiple signals could dramatically improve predictive accuracy.

---

## **4. Temporal and Genre-Aware Modeling**

Musical trends change over time. A model trained on data spanning 1958–2020 implicitly assumes feature relevance is constant across decades, which is unrealistic. To address this:

- Build decade-specific models  
- Examine concept drift in features  
- Analyze subgenres or stylistic families  

Such approaches would help clarify how musical preferences evolve and which features remain consistently predictive.

---

## **5. Exploring More Advanced Models**

While the Random Forest model provided meaningful insight, more powerful models could reveal deeper patterns:

- XGBoost or LightGBM for gradient boosting  
- Neural networks for nonlinear interactions  
- Calibrated probability models for better interpretability  

Each method brings trade-offs, but exploring alternatives would strengthen conclusions.

---

## **6. Enhancing Reproducibility**

Although the current project includes a Snakemake workflow and a unified run script, further steps could increase reproducibility:

- Packaging the environment with Docker  
- Using data versioning tools such as DVC  
- Publishing a persistent identifier through Zenodo  

These additions would align the project even more closely with FAIR principles.

---

## **7. Extending Data Curation Documentation**

Future versions of this project could include:

- Schema.org metadata  
- DataCite-style descriptive metadata  
- More detailed cleaning provenance in JSON or YAML format  
- Automated metadata extraction for each pipeline step  

Such improvements would help others understand the lineage and transformation of the dataset more transparently.

---

## **Conclusion**

This project demonstrates how audio features provide partial but meaningful insight into what differentiates hit songs from others. While predictive accuracy remains moderate, the patterns uncovered—especially around danceability, loudness, valence, and acousticness—illustrate the relationship between musical structure and popular appeal. Future expansions of data sources, modeling techniques, and reproducibility practices offer clear pathways to deepen the analysis and enhance the robustness of the results.

---

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software as long as the original license is included.

---
## Authors

- **Om Patel** — University of Illinois Urbana-Champaign  
  - ORCID: https://orcid.org/0009-0005-4376-3934  

- **Veer Jain** — University of Illinois Urbana-Champaign
  - ORCID: https://orcid.org/0009-0008-3927-7409

MIT License

Copyright (c) 2025 Om Patel and Veer Jain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      
copies of the Software, and to permit persons to whom the Software is          
furnished to do so, subject to the following conditions:                       

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.                                 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.

# References  

1. Dave, D. (2021). *Billboard “The Hot 100” Songs* [Dataset]. Kaggle.  
2. Ay, Y. E. (2020). *Spotify Dataset 1921–2020, 600k+ Tracks* [Dataset]. Kaggle.  
3. Billboard. *Billboard Hot 100 Chart*. https://www.billboard.com/charts/hot-100/  
4. Spotify for Developers. *Web API Reference*. https://developer.spotify.com/documentation/web-api/  
5. McKinney, W. (2010). *Data Structures for Statistical Computing in Python*. SciPy Conference.  
6. Hunter, J. D. (2007). *Matplotlib: A 2D Graphics Environment*.  
7. Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*.  
8. Köster, J., & Rahmann, S. (2012). *Snakemake: A Scalable Bioinformatics Workflow Engine*.
