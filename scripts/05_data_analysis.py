"""
Analysis and Visualization Script
This Script will analyze the Spotify features to identify what makes a song chart onto the Billboard Hot 100.
Focusing on what factors are the most important to get a song to chart, along with a smaller focus on Top 10 and Top 1 songs to see what truly makes a song Special.
"""

#Data Manipulation 
import pandas as pd
import numpy as np

#Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

#Data Modeling and Analysis
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score , roc_auc_score
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier

#Path
from pathlib import Path

"""
We will do several different models and graphs to visualize along with find these important features in songs.
"""

# Setting a Common Style for all Visualization
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)


def analyze_data():
    """Perform analysis to identify features that predict chart success"""
    
    print("Analysis: What Makes Songs Chart on Billboard Hot 100?")
    
    print("\nLoading cleaned data to analyze")
    
    #retrives clean_data after 04_data_cleaning runs by tracing the data directory file got saved under
    df = pd.read_csv("data/processed/cleaned_data.csv")

    #Print out the shape to show the Dataset has been loaded and give a base outlook of the Clean Dataset
    print(f"Dataset shape: {df.shape}")
    
    #Create a directory for all the results, which will have all things created or found in analysis
    Path("results/figures").mkdir(parents=True, exist_ok=True)
    
    # Feature Engineering
    df['energy_loudness'] = df['energy'] * df['loudness']
    df['energy_danceability'] = df['energy'] * df['danceability']
    df['positive_energy'] = df['valence'] * df['energy']
    df['vocal_prominence'] = df['speechiness'] * (1 - df['instrumentalness'])
    df['tempo_normalized'] = (df['tempo'] - 120) / 60

    # Update feature_cols to include new features
    feature_cols = ['danceability', 'energy', 'loudness', 'speechiness',
                'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
                'energy_loudness', 'energy_danceability', 'positive_energy',
                'vocal_prominence', 'tempo_normalized']

    # First, We will do a Descriptive Analysis of the songs that reached Top 10 and their mean values for each feature
    
    print("1. Descriptive Analysis Statistics")
    
    # Compare Top 10 vs. Others
    top_10_songs = df[df['reached_top_10'] == 1]
    other_songs = df[df['reached_top_10'] == 0]
    
    print(f"\nSongs that reached Top 10: {len(top_10_songs)}")
    print(f"Songs that didn't reach Top 10: {len(other_songs)}")

    # Calculate mean differences
    print("\n")
    print("Feature Comparison: Top 10 vs Others")
    print("\n")
    
    #Create a Dataframe that hold the comparison of all values
    comparison = pd.DataFrame({
        'Top_10_Mean': top_10_songs[feature_cols].mean(),
        'Others_Mean': other_songs[feature_cols].mean(),
        'Difference': top_10_songs[feature_cols].mean() - other_songs[feature_cols].mean()
    })
    comparison['Abs_Difference'] = comparison['Difference'].abs()
    comparison = comparison.sort_values('Abs_Difference', ascending=False)

    print(comparison)
    
    
    #Secondly, We will create a Visual for Feature Distributons
    
    print("2. Creating Visualizations")
    
    # Plot 1 will be a Feature Comparison Boxplot
    n_features = len(feature_cols)
    n_cols = 3
    n_rows = int(np.ceil(n_features / n_cols))

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))
    axes = axes.flatten()

    for id_x, col in enumerate(feature_cols):
        ax = axes[id_x]
        data_points_to_plot = [other_songs[col], top_10_songs[col]]
        bp = ax.boxplot(
            data_points_to_plot,
            labels=['Below Top 10', 'Top 10'],
            patch_artist=True
        )

        # Color boxes
        bp['boxes'][0].set_facecolor('lightblue')
        bp['boxes'][1].set_facecolor('lightcoral')

        ax.set_title(col.replace("_", " ").title(), fontsize=12, fontweight='bold')
        ax.set_ylabel('Value')
        ax.grid(True, alpha=0.3)

    # Hide any unused subplots (if grid has more cells than features)
    for j in range(n_features, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.savefig('results/figures/feature_distributions.png', dpi=300, bbox_inches='tight')
    print("Saved: feature_distributions.png")
    plt.close()
    
    #Plot 2 will be a Correlation Heatmap
    plt.figure(figsize=(10, 8))
    
    correlation = df[feature_cols + ['reached_top_10']].corr()
    
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    
    plt.title('Feature Correlation Matrix', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('results/figures/correlation_heatmap.png', dpi=300, bbox_inches='tight')
    print("Saved: correlation_heatmap.png")
    plt.close()
    
    # Plot 3 will be a Figure showing the Importance of all the Top Features showing their Differences
    
    plt.figure(figsize=(10, 6))
    
    top_features = comparison.head(9)
    
    colors = ['green' if x > 0 else 'red' for x in top_features['Difference']]
    
    plt.barh(range(len(top_features)), top_features['Difference'], color=colors, alpha=0.7)
    
    plt.yticks(range(len(top_features)), top_features.index)
    plt.xlabel('Mean Difference (Top 10 - Others)', fontsize=12)
    
    plt.title('Which Features Differ Most for Top 10 Songs?', fontsize=14, fontweight='bold')
    plt.axvline(x=0, color='black', linestyle='--', linewidth=1)
    plt.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('results/figures/feature_importance_diff.png', dpi=300, bbox_inches='tight')
    print("Saved: feature_importance_diff.png")
    plt.close()
    
    # Third, We will look into Machine Learning Analysis using Sklearn
    
    print("3. Machine Learning: Predicting Chart Success")
    
    # Prepare data
    X = df[feature_cols]
    y = df['reached_top_10']

    # Split data, This is needed to make sure the model can perform with unseen data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    print(f"\nTraining set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")
    print(f"Class distribution in training: {y_train.value_counts().to_dict()}")
    
    # Scale the features to help algorithms find the optimal solution more easily
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("\nApplying SMOTE to balance classes...")
    smote = SMOTE(random_state=42, k_neighbors=5)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train_scaled, y_train)
    print(f"Training set after SMOTE: {len(X_train_balanced)} samples")

    # The First Model we will use is Random Forest, which builds many decision trees and aggregates their results to predict chart success
    print("Random Forest Classifier")
    
    rf_model = RandomForestClassifier(
        n_estimators=400,      
        max_depth=12,          
        min_samples_leaf=2,    
        min_samples_split=5,   
        random_state=42
    )
    
    rf_model.fit(X_train_balanced, y_train_balanced)
    
    rf_pred = rf_model.predict(X_test_scaled)
    rf_accuracy = accuracy_score(y_test, rf_pred)
    
    rf_proba = rf_model.predict_proba(X_test_scaled)[:, 1]
    rf_auc = roc_auc_score(y_test, rf_proba)

    print(f"\nAccuracy: {rf_accuracy:.4f}")
    print(f"ROC-AUC:  {rf_auc:.4f}")
    print("\nClassification Report:")
    #To see how the model is predicting data overall 
    print(classification_report(y_test, rf_pred, target_names=['Below Top 10', 'Top 10']))
    #To see how the model is predicting data overall 
    
    
    # Now we will check the Feature importance from Random Forest
    feature_importance = pd.DataFrame({
        'feature': feature_cols,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)

    print("\nFeature Importance:")
    print(feature_importance)
    
    # Plot 4 will be a feature importance visual based on the Random Forest Algorithm
    plt.figure(figsize=(10, 6))
    
    plt.barh(range(len(feature_importance)), feature_importance['importance'], color='steelblue', alpha=0.7)
    
    plt.yticks(range(len(feature_importance)), feature_importance['feature'])
    plt.xlabel('Importance Score', fontsize=12)
    
    plt.title('Random Forest: Feature Importance for Chart Success', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('results/figures/rf_feature_importance.png', dpi=300, bbox_inches='tight')
    print("\nSaved: rf_feature_importance.png")
    plt.close()
    
    #The Second Model will be a Logistic Regression, to find what features are the most important using Logistic Regression
    
    print("Logistic Regression")
    
    log_model = LogisticRegression(
        random_state=42,
        max_iter=2000,
        C=0.1,      
        class_weight=None,
        solver='saga'
    )
    log_model.fit(X_train_balanced, y_train_balanced) 

    log_pred = log_model.predict(X_test_scaled)
    log_accuracy = accuracy_score(y_test, log_pred)

    log_proba = log_model.predict_proba(X_test_scaled)[:, 1]
    log_auc = roc_auc_score(y_test, log_proba)

    print(f"\nAccuracy: {log_accuracy:.4f}")
    print(f"ROC-AUC:  {log_auc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, log_pred, target_names=['Below Top 10', 'Top 10']))
    
    #This will show the Coefficients found from the Logistic Regression
    
    log_coefficients = pd.DataFrame({
        'feature': feature_cols,
        'coefficient': log_model.coef_[0]
    }).sort_values('coefficient', key=abs, ascending=False)

    print("\nLogistic Regression Model Coefficients:")
    print(log_coefficients)
    
    
    print("\nGradient Boosting Classifier")


    gb_model = GradientBoostingClassifier(
        n_estimators=200,
        learning_rate=0.1,
        max_depth=5,
        random_state=42
    )

    gb_model.fit(X_train_balanced, y_train_balanced)

    gb_pred = gb_model.predict(X_test_scaled)
    gb_accuracy = accuracy_score(y_test, gb_pred)

    gb_proba = gb_model.predict_proba(X_test_scaled)[:, 1]
    gb_auc = roc_auc_score(y_test, gb_proba)

    print(f"\nAccuracy: {gb_accuracy:.4f}")
    print(f"ROC-AUC:  {gb_auc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, gb_pred, target_names=['Below Top 10', 'Top 10']))

    # Plot 5 will be a Confusion Matrix that highlights, the Performance of Models against the actual Values
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Random Forest Model Confusion Matrix
    cm_rf = confusion_matrix(y_test, rf_pred)
    
    sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', ax=axes[0],
                xticklabels=['Below Top 10', 'Top 10'],
                yticklabels=['Below Top 10', 'Top 10'])
    
    axes[0].set_title(f'Random Forest\nAccuracy: {rf_accuracy:.4f}', fontweight='bold')
    axes[0].set_ylabel('Actual')
    axes[0].set_xlabel('Predicted')

    # Logistic Regression Model Confusion Matrix
    cm_log = confusion_matrix(y_test, log_pred)
    
    sns.heatmap(cm_log, annot=True, fmt='d', cmap='Greens', ax=axes[1],
                xticklabels=['Below Top 10', 'Top 10'],
                yticklabels=['Below Top 10', 'Top 10'])
    
    axes[1].set_title(f'Logistic Regression\nAccuracy: {log_accuracy:.4f}', fontweight='bold')
    axes[1].set_ylabel('Actual')
    axes[1].set_xlabel('Predicted')
    
    plt.tight_layout()
    plt.savefig('results/figures/confusion_matrices.png', dpi=300, bbox_inches='tight')
    print("\nSaved: confusion_matrices.png")
    plt.close()
    
    # Finally we will Save Results we had
    
    print("4. Saving Results")
  

    results = {
        'Feature Comparison': comparison,
        'Random Forest Accuracy': rf_accuracy,
        'Logistic Regression Accuracy': log_accuracy,
        'Gradient Boosting Classifier Accuracy' : gb_accuracy,
        'Gradient Boosting Classifier ROC_AUC' : gb_auc,
        'Random Forest ROC-AUC': rf_auc,
        'Logistic Regression ROC-AUC': log_auc,
        'Feature Importance (RF)': feature_importance,
        'LR Coefficients': log_coefficients,
    }
    
    # Now save to Text File to reference of results after running in Text File
    results_path = Path("results/analysis_results.txt")
    
    with open(results_path, 'w') as f:
        
        f.write("Analysis Results: What Makes Songs Chart on Billboard Hot 100?\n")
        f.write("\n\n")

        f.write("1. Feature Comparison (Top 10 vs Others)\n")
        f.write("\n")
        f.write(comparison.to_string())
        f.write("\n\n")

        f.write("2. Machine Learning Results\n")
        f.write("\n")
        f.write(f"Random Forest Accuracy: {rf_accuracy:.4f}\n")
        f.write(f"Random Forest ROC-AUC: {rf_auc:.4f}\n")
        f.write(f"Logistic Regression Accuracy: {log_accuracy:.4f}\n\n")
        f.write(f"Logistic Regression ROC-AUC: {log_auc:.4f}\n\n")
        f.write(f"Gradient Boosting Classifier Accuracy: {gb_accuracy:.4f}\n\n")
        f.write(f"Gradient Boosting Classifier ROC-AUC: {gb_auc:.4f}\n\n")

        f.write("3. Feature Importance (Random Forest)\n")
        f.write("\n")
        f.write(feature_importance.to_string())
        f.write("\n\n")

        f.write("4. Logistic Regression Coefficients\n")
        f.write( "\n")
        f.write(log_coefficients.to_string())
        f.write("\n\n")

        f.write("5. Key Findings\n")
        f.write("\n")
        f.write("Top 3 most important features:\n")
        for idx, row in feature_importance.head(3).iterrows():
            f.write(f"  {idx+1}. {row['feature']}: {row['importance']:.4f}\n")

    print(f"\nResults saved to: {results_path}")
    
    print("Analysis Complete")
    
    return results

if __name__ == "__main__":
    analyze_data()
