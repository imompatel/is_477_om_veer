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

This project explores the question of what makes a song successful on the Billboard Hot 100 chart by examining musical characteristics available through Spotify’s audio feature dataset. The motivation behind the project comes from both a curiosity about the factors that shape music popularity and a desire to apply data curation and analysis techniques to a large real-world dataset. The Billboard Hot 100 is considered one of the most influential music charts in the world, and understanding the attributes that distinguish hit songs can offer insight into how musical tastes, production styles, and industry influence evolve over time. While the music industry often relies on intuition, marketing strategies, and cultural awareness to predict success, the growing availability of quantitative musical features—especially through streaming platforms—opens the door for data-driven analysis.

The central research question guiding this project is: **Which Spotify audio features are most strongly associated with whether a song reaches the Top 10 on the Billboard Hot 100?** From this question, several secondary questions naturally emerge: How do musical features differ between highly successful songs and those that chart but never break into the Top 10? Can machine learning models use these audio features to predict chart success? And to what extent do these features help explain trends in music popularity?

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

## **Descriptive Comparisons**

Across the integrated dataset, Top 10 songs displayed significantly different distributions for several Spotify audio features:

- **Danceability:** Top 10 songs were, on average, 0.015 points more danceable. This aligns with modern popular music’s emphasis on rhythm and groove.  
- **Loudness:** Top 10 songs were about 0.8 dB louder on average, suggesting more energetic production.  
- **Valence:** Higher valence (+0.02) indicates that hit songs tend to sound “happier” or more positive.  
- **Acousticness:** Lower acousticness (–0.03) suggests hit songs skew toward electronic, pop, and hip-hop production styles.  
- **Energy:** Although the mean difference was small (+0.008), it suggests a subtle trend toward more intense tracks.  

These findings are visually represented through boxplots (`feature_distributions.png`) and a correlation heatmap (`correlation_heatmap.png`), showing relationships among the features.

---

## **Correlation Insights**

Some notable correlation patterns include:

- **Energy ↔ Loudness:** Strong positive correlation, consistent with music production practices.  
- **Energy ↔ Acousticness:** Strong negative correlation, indicating that more acoustic tracks tend to be less energetic.  
- **Valence ↔ Danceability:** Moderate positive correlation, suggesting happier tracks often feel more danceable.  

While none of these relationships are surprising, they validate the structure of the Spotify audio feature space and help explain model behavior.

---

## **Machine Learning Results**

Two models were used:

### **Random Forest Classifier**
- Accuracy: ~70%  
- Excellent performance on the majority class (non–Top 10 songs)  
- Feature importance ranking:  
  1. Danceability  
  2. Speechiness  
  3. Valence  
  4. Loudness  
  5. Acousticness  

The model struggled with recall for rare Top 10 hits, which is expected due to class imbalance.

### **Logistic Regression**
- Accuracy: ~63%  
- More interpretable but less accurate  
- Coefficients confirmed the directionality of descriptive findings  

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
