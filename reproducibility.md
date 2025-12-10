# Reproducibility Guide

This document provides step-by-step instructions to reproduce the analysis results for the Billboard Hot 100 & Spotify project.

---

## Prerequisites

- **Python 3.8+** installed
- **Git** installed
- **Kaggle account** (free account at https://www.kaggle.com)
- **Minimum 4GB RAM** and **500MB free disk space**

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/imompatel/is_477_om_veer
cd IS_477_Project
```

### 2. Create and Activate Virtual Environment - Not Required but can be helpful

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Kaggle API

**Step 1:** Create a Kaggle account at https://www.kaggle.com (if you don't have one)

**Step 2:** Get your API Token
- Go to your Kaggle account settings: https://www.kaggle.com/settings
- Scroll down to the **API section**
- Click **"Generate New Token"**
- A popup will appear showing your API token (e.g., `KGAT_...`)
- **IMPORTANT:** Copy this token immediately - you won't be able to see it again!

**Step 3:** Set up the API token on your system

**macOS/Linux:**
```bash
# Create the kaggle directory
mkdir -p ~/.kaggle

# Set the token as an environment variable
export KAGGLE_API_TOKEN="KGAT_YOUR_TOKEN_HERE"

# To make it permanent, add to your shell config file:
echo 'export KAGGLE_API_TOKEN="KGAT_YOUR_TOKEN_HERE"' >> ~/.bashrc  # or ~/.zshrc
source ~/.bashrc  # or source ~/.zshrc
```

**Windows (Command Prompt):**
```bash
# Create the kaggle directory
mkdir %USERPROFILE%\.kaggle

# Set environment variable (temporary - for current session)
set KAGGLE_API_TOKEN=KGAT_YOUR_TOKEN_HERE

# To make it permanent, use System Environment Variables:
# 1. Search for "Environment Variables" in Windows
# 2. Click "Environment Variables"
# 3. Under "User variables", click "New"
# 4. Variable name: KAGGLE_API_TOKEN
# 5. Variable value: KGAT_YOUR_TOKEN_HERE
```

**Windows (PowerShell):**
```powershell
# Create the kaggle directory
New-Item -ItemType Directory -Force -Path $env:USERPROFILE\.kaggle

# Set environment variable (temporary)
$env:KAGGLE_API_TOKEN = "KGAT_YOUR_TOKEN_HERE"

# To make it permanent:
[System.Environment]::SetEnvironmentVariable('KAGGLE_API_TOKEN', 'KGAT_YOUR_TOKEN_HERE', 'User')
```

**Alternative: Create kaggle.json manually (if preferred)**
```bash
# Create the directory
mkdir -p ~/.kaggle  # macOS/Linux
mkdir %USERPROFILE%\.kaggle  # Windows

# Create kaggle.json with your token
# Replace YOUR_TOKEN with your actual API token from Kaggle
echo '{"username":"your_username","key":"KGAT_YOUR_TOKEN_HERE"}' > ~/.kaggle/kaggle.json

# Set proper permissions (macOS/Linux only)
chmod 600 ~/.kaggle/kaggle.json
```

**Verify setup:**
```bash
# Check if environment variable is set
echo $KAGGLE_API_TOKEN  # macOS/Linux
echo %KAGGLE_API_TOKEN%  # Windows CMD
echo $env:KAGGLE_API_TOKEN  # Windows PowerShell

# Or verify the kagglehub library can authenticate
python -c "import kagglehub; print('Kaggle API configured successfully!')"
```

---

## Data Access

### Automatic Data Download (Recommended)

The project **automatically downloads data from Kaggle** when you run the pipeline. No manual download is required!

**Data Sources (downloaded automatically):**
- **Billboard Hot 100:** dhruvildave/billboard-the-hot-100-songs
- **Spotify Tracks:** yamaerenay/spotify-dataset-19212020-600k-tracks

The `01_data_retrieval.py` script uses the `kagglehub` library to:
1. Download datasets from Kaggle
2. Verify file integrity with SHA-256 checksums
3. Save metadata about the downloads

### Pre-processed Results (Optional - Available on Box)

If you want to skip data download/processing and just verify final results:

**Box Folder:** [INSERT YOUR BOX LINK HERE]

**Available Files:**
```
processed_data/
├── integrated_data.csv          (~25 MB)
├── cleaned_data.csv              (~24 MB)
├── integration_summary.txt
├── quality_report.txt
└── cleaning_log.txt

results/
├── analysis_results.txt
└── figures/
    ├── feature_distributions.png
    ├── correlation_heatmap.png
    ├── feature_importance_diff.png
    ├── rf_feature_importance.png
    └── confusion_matrices.png
```

**To use pre-processed data:**
1. Download `processed_data.zip` from Box
2. Extract to `data/processed/` in your project directory
3. Download `results.zip` from Box (optional, to compare outputs)
4. Extract to `results/` in your project directory
5. Skip to "Analysis Only" section below

---

## Running the Analysis

### Complete Pipeline (Full Reproduction)

Run the entire workflow from raw data download to final analysis:

```bash
./run_all.sh
```

Or use Snakemake directly:

```bash
snakemake --cores 1
```

**This will execute:**
1. **Data Acquisition** - Download from Kaggle via API, verify checksums
2. **Data Integration** - Merge Billboard + Spotify datasets
3. **Quality Assessment** - Check completeness, validity, outliers
4. **Data Cleaning** - Handle missing values, duplicates, outliers
5. **Analysis** - Generate visualizations and machine learning models

**Expected Runtime:** 10-15 minutes (depends on internet speed for download)

### Individual Steps (Optional)

You can run individual scripts if needed:

```bash
# Step 1: Data Retrieval (downloads from Kaggle)
python scripts/01_data_retrieval.py

# Step 2: Data Integration
python scripts/02_data_integration.py

# Step 3: Quality Assessment
python scripts/03_data_quality.py

# Step 4: Data Cleaning
python scripts/04_data_cleaning.py

# Step 5: Analysis
python scripts/05_data_analysis.py
```

### Analysis Only (Using Pre-processed Data from Box)

If you downloaded processed data from Box:

```bash
python scripts/05_data_analysis.py
```

**Expected Runtime:** 2-3 minutes

---

## Expected Outputs

### File Structure After Completion

```
IS_477_Project/
├── data/
│   ├── raw/
│   │   ├── billboard_hot_100.csv      (17.36 MB, 330,087 rows)
│   │   ├── spotify_songs.csv           (106.21 MB, 586,672 rows)
│   │   └── data_sources.txt
│   └── processed/
│       ├── integrated_data.csv         (~25 MB, 223,185 rows)
│       ├── cleaned_data.csv            (~24 MB)
│       ├── integration_summary.txt
│       ├── quality_report.txt
│       └── cleaning_log.txt
├── results/
│   ├── analysis_results.txt
│   └── figures/
│       ├── feature_distributions.png
│       ├── correlation_heatmap.png
│       ├── feature_importance_diff.png
│       ├── rf_feature_importance.png
│       └── confusion_matrices.png
└── scripts/
    ├── 01_data_retrieval.py
    ├── 02_data_integration.py
    ├── 03_data_quality.py
    ├── 04_data_cleaning.py
    └── 05_data_analysis.py
```

### Expected Model Performance

**With Feature Engineering and SMOTE (Current Version):**
- **Random Forest Accuracy:** ~78-82%
- **Random Forest ROC-AUC:** ~85-88%
- **Logistic Regression Accuracy:** ~68-72%
- **Logistic Regression ROC-AUC:** ~72-76%
- **Gradient Boosting Accuracy:** ~79-83%
- **Gradient Boosting ROC-AUC:** ~86-89%

*Note: Minor variations (±2-3%) are expected due to system differences and random states*

---

## Software Dependencies

### Core Requirements (requirements.txt)

```
pandas==2.1.3
numpy==1.24.3
matplotlib==3.8.0
seaborn==0.13.0
scikit-learn==1.3.2
imbalanced-learn==0.11.0
kagglehub==0.2.5
snakemake==7.32.4
```

### Complete Environment Snapshot

After installation, generate your exact environment:

```bash
pip freeze > environment.txt
```

This captures all dependencies including sub-dependencies for full reproducibility.

### Python Version

```bash
python --version
# Should output: Python 3.8+ (3.12 recommended)
```

---

## Verification Checklist

Use this to verify successful reproduction:

- [ ] Virtual environment activated
- [ ] All dependencies installed (`pip list` shows all packages)
- [ ] Kaggle API configured
- [ ] Raw data downloaded (check `data/raw/` for CSV files)
- [ ] Integration completed (`data/processed/integrated_data.csv` exists)
- [ ] Quality assessment completed (`data/processed/quality_report.txt` exists)
- [ ] Data cleaned (`data/processed/cleaned_data.csv` exists)
- [ ] Analysis completed (`results/analysis_results.txt` exists)
- [ ] All 5 visualizations generated (`results/figures/*.png`)
- [ ] Model performance within expected ranges
- [ ] No error messages in terminal output

---

## Troubleshooting

### Issue 1: Kaggle API Authentication Error

**Error:** `OSError: Could not find kaggle'

**Solution:**
1. Follow Guide on Kaggle API Github, here https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md

### Issue 2: Column Name Mismatch

**Error:** `KeyError: 'Song'`

**This has been fixed!** The updated `02_data_integration.py` automatically detects column names regardless of case. If you still see this error, make sure you're using the latest version from the repository.

### Issue 3: Kaggle Download Fails

**Error:** Dataset download times out or fails

**Solutions:**
- Check internet connection
- Verify Kaggle API credentials are correct
- The script will automatically find the correct CSV file even if the filename doesn't match exactly
- Try running `01_data_retrieval.py` separately first

### Issue 4: Memory Error

**Error:** `MemoryError` or system freeze

**Solutions:**
- Close other applications
- Increase available RAM
- Use smaller test dataset (contact instructors)

### Issue 5: Missing Dependencies

**Error:** `ModuleNotFoundError: No module named 'X'`

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

---
