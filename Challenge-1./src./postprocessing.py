"""
Author: Annam.ai IIT Ropar
Team Name: anndata
Team Members: N. Saikoushik, M. Sai Teja, G. Navya Sri, N. Chandhana Priya, V. Asmitha
Leaderboard Rank: 22
"""

import pandas as pd

def postprocessing(predictions_csv, submission_csv_path):
    print("Starting postprocessing for Soil Classification...")

    if not os.path.exists(predictions_csv):
        print(f"Error: {predictions_csv} not found!")
        return 1

    df_preds = pd.read_csv(predictions_csv)
    print(f"Loaded predictions: {df_preds.shape}")

    # Normalize class names (capitalize)
    df_preds['soil_type'] = df_preds['soil_type'].str.strip().str.title()

    # Check for unexpected classes
    allowed_classes = ['Alluvial Soil', 'Black Soil', 'Clay Soil', 'Red Soil']
    invalid_rows = df_preds[~df_preds['soil_type'].isin(allowed_classes)]
    if not invalid_rows.empty:
        print(f"Warning: Found {len(invalid_rows)} invalid predictions. Fixing to 'Alluvial Soil'.")
        df_preds.loc[~df_preds['soil_type'].isin(allowed_classes), 'soil_type'] = 'Alluvial Soil'

    # Save submission
    df_preds.to_csv(submission_csv_path, index=False)
    print(f"Postprocessing completed. Submission saved to {submission_csv_path}")

    return 0

if __name__ == "__main__":
    import os
    predictions_csv = "raw_predictions.csv"  # adjust filename if needed
    submission_csv_path = "submission.csv"
    postprocessing(predictions_csv, submission_csv_path)

