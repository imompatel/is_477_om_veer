import pandas as pd
import numpy as np
from pathlib import Path

def clean_data():
    """Clean the integrated dataset"""

    print("Data Cleaning")
    
    df = pd.read_csv("data/processed/integrated_data.csv")
    
    print(f"Original dataset shape: {df.shape}")

    #Creating a Text file highlighting the process of this Script for future reference after excutation
    cleaning_log = []
    cleaning_log.append("Data Cleaning Log")
    cleaning_log.append(f"\nOriginal dataset shape: {df.shape}")
    
    #First, Missing Value handling
    
    print("1. Handling Missing Values")
    cleaning_log.append("\n1. Handling Missing Values")
    
    #Find total missing value before cleaning
    missing_before_cleaning = df.isnull().sum().sum()
    print(f"\nMissing values before cleaning: {missing_before_cleaning}")
    cleaning_log.append(f"\nMissing values before cleaning: {missing_before_cleaning}")

    # Drop rows with missing critical values, as these are needed for the analysis
    critical_cols = ['Song', 'Artist', 'Rank', 'danceability', 'energy', 'loudness']
    df_clean = df.dropna(subset=critical_cols)

    rows_dropped = len(df) - len(df_clean)
    print(f"Rows removed due to missing critical values: {rows_dropped}")
    cleaning_log.append(f"Rows removed due to missing critical values: {rows_dropped}")
    
    # Fill the remaining missing values with the median for numeric columns. We decided this was the best choice because other critical numeric columns could be distorted due to Spotify adding older songs into their system.
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        missing_count = df_clean[col].isnull().sum()
        if missing_count > 0:
            median_val = df_clean[col].median()
            df_clean[col].fillna(median_val, inplace=True)
            print(f"  {col}: Filled {missing_count} missing values with median ({median_val:.4f})")
            cleaning_log.append(f"  {col}: Filled {missing_count} missing values with median ({median_val:.4f})")

    missing_after = df_clean.isnull().sum().sum()
    print(f"\nMissing values after cleaning: {missing_after}")
    cleaning_log.append(f"\nMissing values after cleaning: {missing_after}")

    #Second, We will have the process of handling duplicate songs, Since Songs have many verison we have to keep this in mind not getting rid songs with many verisons.
    
    print("2. Handling Duplicates")
    cleaning_log.append("\n2. Handling Duplicates")
    
    #Print number and record number of the duplicate values
    duplicates_before = df_clean.duplicated().sum()
    print(f"\nDuplicate Song Rows before removal: {duplicates_before}")
    cleaning_log.append(f"\nDuplicate Song Rows before removal: {duplicates_before}")
    
    #drops the duplicate values
    df_clean = df_clean.drop_duplicates()

    #Print the new list after dropping
    duplicates_after = df_clean.duplicated().sum()
    print(f"Duplicate Song Rows after removal: {duplicates_after}")
    cleaning_log.append(f"Duplicate Song Rows after removal: {duplicates_after}")
    
    # Thrid, we will handle Outliers/extreme cases
    
    print("3. Outlier Handling")
    cleaning_log.append("\n3. Outlier Handling")
    
    # For features like tempo and loudness, cap at reasonable percentiles
    outlier_columns = ['tempo', 'loudness', 'duration_ms']

    for column in outlier_columns:
        if column in df_clean.columns:
            
            # Will use the 1st and 99th percentile for capping values, so we still get them at a high extreme value range of only 1% of varaible
            lower_bound = df_clean[column].quantile(0.01)
            upper_bound = df_clean[column].quantile(0.99)

            outliers_lower = (df_clean[column] < lower_bound).sum()
            outliers_upper = (df_clean[column] > upper_bound).sum()

            if outliers_lower > 0 or outliers_upper > 0:
                df_clean[column] = df_clean[column].clip(lower=lower_bound, upper=upper_bound)
                print(f"  {column}: Capped {outliers_lower} Lower and {outliers_upper} Upper outliers")
                cleaning_log.append(f"  {column}: Capped {outliers_lower} Lower and {outliers_upper} Upper outliers")
                
    #Fourth, we will now validate the data ranges making sure they are within variable bound if they are bounded values like percentages
    
    print("4. Validating Data Ranges")
    cleaning_log.append("\n4. Validating Data Ranges")
    
    """Ensuring the bounded values are between domain of [0,1] like mentioned before"""
    
    #Here is the list of bounded features
    
    bounded_features = ['acousticness', 'danceability', 'energy', 'instrumentalness',
                        'liveness', 'speechiness', 'valence']

    for column in bounded_features:
        if column in df_clean.columns:
            df_clean[column] = df_clean[column].clip(lower=0, upper=1)
            
    print("All Bounded Features Validated to be in [0, 1] range")
    cleaning_log.append("All Bounded Features Validated to be in [0, 1] range")
    
    # Fifth, We will Covert Data Types to make sure all the varaibles are the correct/desired Data type
    
    print("5. Converting Data Types")
    cleaning_log.append("\n5. Converting Data Types")
    
    """
    First in this Step 5, we will handle non-numrice values like '-' which is present in the Last Week and Weeks in Charts varaibles
    Then, we will do the same to ensure integer values are also correct using .astype(int)
    """
    
    for column in ['Last Week', 'Weeks in Charts']:
        if column in df_clean.columns:
            df_clean[column] = pd.to_numeric(df_clean[column], errors='coerce')
            df_clean[column] = df_clean[column].fillna(0).astype(int)


    int_cols = ['Rank', 'Peak Position', 'year', 'mode', 'key', 'explicit']
    for col in int_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(int)

    print("Data types converted successfully")
    cleaning_log.append("Data types converted successfully")
    
    # Finally we will Summarize the Information we excuted for the terminal to print and to record for the Cleaning Log
    
    print("Cleaning Summary")
    cleaning_log.append("Cleaning Summary")
    
    print(f"\Starting Integrate Dataset shape: {df.shape}")
    print(f"Cleaned shape: {df_clean.shape}")
    print(f"Rows removed: {len(df) - len(df_clean)} ({(len(df) - len(df_clean))/len(df)*100:.2f}%)")
    print(f"Data quality: {(1 - df_clean.isnull().sum().sum()/(df_clean.shape[0]*df_clean.shape[1]))*100:.2f}% complete")

    cleaning_log.append(f"\nStarting Integrate Dataset shape: {df.shape}")
    cleaning_log.append(f"Cleaned shape: {df_clean.shape}")
    cleaning_log.append(f"Rows removed: {len(df) - len(df_clean)} ({(len(df) - len(df_clean))/len(df)*100:.2f}%)")
    cleaning_log.append(f"Data quality: {(1 - df_clean.isnull().sum().sum()/(df_clean.shape[0]*df_clean.shape[1]))*100:.2f}% complete")

    #Now we will Save the Dataset, to be used in the next Process 5 the analysis and the Cleaning_Log txt file for a reference after excuting program
    output_path = Path("data/processed/cleaned_data.csv")
    df_clean.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")

    # Save cleaning log
    cleaning_log_path = Path("data/processed/cleaning_log.txt")
    with open(cleaning_log_path, 'w') as f:
        f.write('\n'.join(cleaning_log))

    print(f"Cleaning log saved to: {cleaning_log_path}")
    return df_clean

if __name__ == "__main__":
    clean_data()