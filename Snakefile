"""
Snakemake Workflow for Billboard Hot 100 Analysis
This workflow automates the entire data pipeline from acquisition to analysis.
"""

# Final targets for a full end-to-end run
rule all:
    input:
        "data/raw/data_sources.txt",
        "data/processed/integrated_data.csv",
        "data/processed/quality_report.txt",
        "data/processed/cleaned_data.csv",
        "results/analysis_results.txt",
        "results/figures/feature_distributions.png",
        "results/figures/correlation_heatmap.png",
        "results/figures/feature_importance_diff.png",
        "results/figures/rf_feature_importance.png",
        "results/figures/confusion_matrices.png"


# Step 1: Data acquisition and verification
rule data_acquisition:
    input:
        #none because data is getting fetched from the Kaggle API
    output:
        "data/raw/billboard_hot_100.csv",
        "data/raw/spotify_songs.csv",
        "data/raw/data_sources.txt"
    shell:
        "python scripts/01_data_retrieval.py"


# Step 2: Data integration
rule data_integration:
    input:
        "data/raw/billboard_hot_100.csv",
        "data/raw/spotify_songs.csv",
        "data/raw/data_sources.txt"
    output:
        "data/processed/integrated_data.csv",
        "data/processed/integration_summary.txt"
    shell:
        "python scripts/02_data_integration.py"


# Step 3: Data quality assessment
rule data_quality:
    input:
        "data/processed/integrated_data.csv"
    output:
        "data/processed/quality_report.txt"
    shell:
        "python scripts/03_data_quality.py"


# Step 4: Data cleaning
rule data_cleaning:
    input:
        "data/processed/integrated_data.csv",
        "data/processed/quality_report.txt"
    output:
        "data/processed/cleaned_data.csv",
        "data/processed/cleaning_log.txt"
    shell:
        "python scripts/04_data_cleaning.py"


# Step 5: Analysis and visualization
rule analysis:
    input:
        "data/processed/cleaned_data.csv"
    output:
        "results/analysis_results.txt",
        "results/figures/feature_distributions.png",
        "results/figures/correlation_heatmap.png",
        "results/figures/feature_importance_diff.png",
        "results/figures/rf_feature_importance.png",
        "results/figures/confusion_matrices.png"
    shell:
        "python scripts/05_data_analysis.py"