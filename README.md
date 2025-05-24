Soil Image Classification – IIT Ropar x Annam.ai Hackathon 2025

This project was developed as part of the Hackathon and Internship opportunity organized by IIT Ropar and Annam.ai. 
It focuses on classifying soil types (Alluvial, Black, Clay, Red) from images using deep learning techniques to support AI-driven sustainable agriculture.

Project Folder Structure:

/src
    Source code modules (model definitions, utility functions, custom dataloaders)

/notebooks
    training.ipynb        → Jupyter Notebook for model training
    inference.ipynb       → Jupyter Notebook for inference and generating submission CSV

/docs
    architecture.png      → Model architecture or system overview image
    cards/
        project-card.txt      → Project overview description
        ml-metrics.txt        → Text file with classification performance metrics

/models
    best_model.pth        → Saved trained model weights

/outputs
    predictions.csv       → Final predictions ready for submission

/data
    download.sh           → Script to download or prepare the dataset (if applicable)

README.txt               → This documentation file
requirements.txt         → List of Python package dependencies

Setup Instructions:

1. Clone the repository or unzip the package.

2. Navigate into the project directory.

3. (Optional) Create a Python virtual environment:
    python -m venv env
    source env/bin/activate       (on Windows, use env\Scripts\activate)

4. Install required dependencies:
    pip install -r requirements.txt

5. Ensure the dataset is prepared and placed in the /data folder (or use download.sh if provided).

Run Instructions:

- To train the model:
    Open and run notebooks/training.ipynb.

- To generate predictions:
    Open and run notebooks/inference.ipynb.

Model Highlights:

- Architecture: CNN-based transfer learning (ResNet-50, EfficientNet, or similar)
- Input: 224x224 RGB soil images
- Augmentation: Random flips, rotations, color jittering
- Training method: Stratified K-fold cross-validation
- Additional techniques: Ensemble models, test-time augmentation (TTA) for performance boost

Performance:

- Final Accuracy: Approximately 91%
- Final F1-score: Approximately 89.5%
- Refer to docs/cards/ml-metrics.txt for detailed precision, recall, confusion matrix, and per-class metrics.

Deliverables Included:

- Complete training and inference code (Jupyter notebooks)
- Trained model checkpoint (best_model.pth)
- Final submission CSV (predictions.csv)
- Project card (project-card.txt) summarizing the approach and methods
- ML metrics report (ml-metrics.txt) detailing model evaluation results
- Model architecture/system image (architecture.png)

Notes:

This repository is part of the IIT Ropar x Annam.ai Hackathon 2025. Please check licensing terms before reuse beyond competition purposes.
For any questions or collaboration, please contact the development team.

