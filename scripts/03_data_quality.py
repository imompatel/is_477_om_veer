import pandas as pd
import numpy as np
from pathlib import Path

"""
This script checks and assesses the quality of the integrated dataset we created in Data Integration
"""

def assess_quality():
    
    """Function Built to evaluate the quailty of the integrated dataset"""
    print("Integrated Data Quality Check Process")
    
    df = pd.read_csv("data/processed/integrated_data.csv")
    
    print(f"Dataset shape: {df.shape}")
    
    #Created to make a text file at the end with all information within the assess_quailty after function excutes for later refrenece
    quality_report = []
    
    #First, we are checking the dataset that was created to see how complete it is with values, checking for null or missing values
    print("\nFirst, Checking to see if Dataset is complete with no Null Values")
    
    missing_data = df.isnull().sum()
    missing_pct = (df.isnull().sum() / len(df) * 100).round(2)

    #Going to show the user what null or missing values are present in the new dataset
    print(f"\nMissing values per column:")
    quality_report.append("\nMissing values per column:")
    #loop that is using Fstring to print per each column with missing data/null data
    for col in df.columns:
        if missing_data[col] > 0:
            print(f"  {col}: {missing_data[col]} ({missing_pct[col]}%)")
            quality_report.append(f"  {col}: {missing_data[col]} ({missing_pct[col]}%)")
            
    if missing_data.sum() == 0:
        print("  No missing values found!")
        quality_report.append("  No missing values found!")

    #Second, Accuracy Testing to see how valid the data is compared to the varaible guidelines for the dataset
    print("Secondly, Accuracy Test to see if values are in valid ranges")

    quality_report.append("\n\n2. Accuracy Test")
    
    # Check for valid ranges
    issues = []

    # Spotify features should be in valid ranges
    if ((df['acousticness'] < 0) | (df['acousticness'] > 1)).any():
        issues.append("Acousticness values outside [0,1] range")

    if ((df['danceability'] < 0) | (df['danceability'] > 1)).any():
        issues.append("Danceability values outside [0,1] range")

    if ((df['energy'] < 0) | (df['energy'] > 1)).any():
        issues.append("Energy values outside [0,1] range")

    if ((df['valence'] < 0) | (df['valence'] > 1)).any():
        issues.append("Valence values outside [0,1] range")

    if ((df['Rank'] < 1) | (df['Rank'] > 100)).any():
        issues.append("Rank values outside [1,100] range")

    if ((df['Peak Position'] < 1) | (df['Peak Position'] > 100)).any():
        issues.append("Peak Position values outside [1,100] range")

    if len(issues) > 0:
        print("Issues found:")
        quality_report.append("\nIssues found:")
        for issue in issues:
            print(f"  : {issue}")
            quality_report.append(f"  : {issue}")
    else:
        print("All values within expected ranges!")
        quality_report.append("All values within expected ranges!")

    #Third, Consistency Test, searching for Duplicate Songs
    quality_report.append("\n\n3. Consistency Test")
    
    
    # Check duplicate songs
    duplicates = df.duplicated(subset=['Song', 'Artist', 'Date'])
    print(f"Duplicate records (Items with same song name, artist, date): {duplicates.sum()}")
    quality_report.append(f"Duplicate records (Items with same song name, artist, date): {duplicates.sum()}")
    
    #Fourth, Analyizing the Distribution of Data
    
    print("4. Distribution Analysis")
    quality_report.append("\n\n4. Distribution Analysis")
    
    # Numerical columns we will be using for our analysis
    numeric_cols = ['danceability', 'energy', 'loudness', 'speechiness',
                    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    
    print("\nBasic Statistics for Key Features:")
    quality_report.append("\nBasic Statistics for key features:")
    
    stats = df[numeric_cols].describe()
    print(stats)
    #now add to the report
    quality_report.append("\n" + stats.to_string())

    #We are going to look at outliers in the data using IQR
    print("\n\nOutlier detection using IQR method:")
    quality_report.append("\n\nOutlier detection using IQR method:")
    
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
        outlier_percent = (outliers / len(df) * 100).round(2)

        if outliers > 0:
            print(f"  {col}: {outliers} outliers ({outlier_percent}%)")
            quality_report.append(f"  {col}: {outliers} outliers ({outlier_percent}%)")
            
    #Fifth, we are going to create a list of data types for all the variables for reference
    print("5. Data Types")
    quality_report.append("\n\n5. Data Types")
    
    print("\nColumn data types:")
    quality_report.append("\nColumn data types:")
    
    for col in df.columns:
        print(f"  {col}: {df[col].dtype}")
        quality_report.append(f"  {col}: {df[col].dtype}")

    #Finally, Summarize the Information from the Integrated Data Set
    print("Integrated Data Quality Summary")
    
    total_cells = df.shape[0] * df.shape[1]
    
    missing_cells = df.isnull().sum().sum()
    
    completeness = ((total_cells - missing_cells) / total_cells * 100).round(2)

    print(f"\nCompleteness: {completeness}%")
    print(f"Total records: {len(df):,}")
    print(f"Total features: {len(df.columns)}")

    quality_report.append(f"\nCompleteness: {completeness}%")
    quality_report.append(f"Total records: {len(df):,}")
    quality_report.append(f"Total features: {len(df.columns)}")
    
    #Now save the report into Text File for later reference after running
    report_path = Path("data/processed/quality_report.txt")
    with open(report_path, 'w') as f:
        f.write('\n'.join(quality_report))

    print(f"\nQuality report saved to: {report_path}")

    return df

if __name__ == "__main__":
    assess_quality()
    

     
    
