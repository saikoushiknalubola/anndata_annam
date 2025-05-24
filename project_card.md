Soil Image Classification Challenge — Project Card
Summary
This project tackles the Soil Image Classification Challenge hosted by Annam.ai at IIT Ropar.
The goal is to classify soil images into one of four categories:

Alluvial soil

Black soil

Clay soil

Red soil

We used deep learning models (ResNet-50 backbone) with cross-validation, data augmentation, and test-time augmentation (TTA) to maximize the minimum per-class F1-score — the official competition metric.

Main Contributions
Fine-tuned transfer learning model (ResNet-50)

Cross-validation ensuring balanced class performance

Rich data augmentation pipeline (Albumentations)

Test-time augmentation (TTA) for stronger predictions

Modular and reproducible codebase

Complete deliverables: notebooks, scripts, metrics, documentation

Final Performance (Validation)
Metric	Value
Minimum F1-score	0.77
Alluvial F1	0.81
Black F1	0.77
Clay F1	0.84
Red F1	0.80
Weighted Avg F1	0.805

Note: Validation scores; leaderboard results may vary.

Repository Structure
bash
Copy
Edit
/src                  → Training and inference scripts
/notebooks           → Training and inference notebooks
/docs/architecture.png → Model architecture diagram
/docs/cards/project-card.md → This project card
/docs/cards/ml-metrics.json → Metrics JSON
/data/download.sh    → Dataset setup script
README.md            → Project overview and setup
requirements.txt     → Python dependencies
Setup and Run Instructions
bash
Copy
Edit
git clone https://github.com/yourusername/soil-classification-2025.git
cd soil-classification-2025

pip install -r requirements.txt

bash data/download.sh

python src/train.py    # Train model
python src/inference.py # Run inference
Or use the notebooks:

/notebooks/training.ipynb → for training

/notebooks/inference.ipynb → for predictions

ML Metrics (from ml-metrics.json)
Minimum F1-score: 0.77

Class F1-scores:

Alluvial: 0.81

Black: 0.77

Clay: 0.84

Red: 0.80

Weighted Average F1: 0.805

Accuracy: 0.82

Loss: 0.42
