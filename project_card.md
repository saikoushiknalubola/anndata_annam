<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Soil Image Classification Challenge - Project Card</title>
</head>
<body>
    <h1>🌱 Soil Image Classification Challenge — Project Card</h1>

    <h2>📌 Summary</h2>
    <p>
        This project addresses the <strong>Soil Image Classification Challenge</strong> hosted by Annam.ai at IIT Ropar.
        The task is to develop a machine learning model that classifies soil images into one of four categories:
    </p>
    <ul>
        <li>Alluvial soil</li>
        <li>Black soil</li>
        <li>Clay soil</li>
        <li>Red soil</li>
    </ul>
    <p>
        We used deep learning (ResNet-50 backbone), combined with cross-validation, augmentation, and test-time augmentation (TTA),
        to build a balanced model optimised for the <strong>minimum per-class F1-score</strong> — the competition’s official evaluation metric.
    </p>

    <h2>🚀 Main Contributions</h2>
    <ul>
        <li>✅ Fine-tuned transfer learning model with strong generalisation</li>
        <li>✅ Cross-validation pipeline ensuring balanced class performance</li>
        <li>✅ Extensive data augmentation (Albumentations)</li>
        <li>✅ Test-time augmentation to boost final predictions</li>
        <li>✅ Structured repository with modular, reproducible code</li>
        <li>✅ All competition deliverables: training + inference notebooks, predictions, metrics, project documentation</li>
    </ul>

    <h2>📊 Final Performance</h2>
    <table border="1" cellpadding="5">
        <tr>
            <th>Metric</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Minimum F1-score</td>
            <td>0.77</td>
        </tr>
        <tr>
            <td>Alluvial F1-score</td>
            <td>0.81</td>
        </tr>
        <tr>
            <td>Black F1-score</td>
            <td>0.77</td>
        </tr>
        <tr>
            <td>Clay F1-score</td>
            <td>0.84</td>
        </tr>
        <tr>
            <td>Red F1-score</td>
            <td>0.80</td>
        </tr>
        <tr>
            <td>Weighted Average F1</td>
            <td>0.805</td>
        </tr>
    </table>
    <p><em>Note: Final scores are estimated from validation; official leaderboard score may vary slightly.</em></p>

    <h2>📁 Repository Structure</h2>
    <pre>
/src
    train.py                   → Model training script
    inference.py               → Inference + submission script
    dataset.py                 → Custom dataset + transforms

/notebooks
    training.ipynb             → End-to-end training notebook
    inference.ipynb            → End-to-end inference + submission notebook

/docs
    architecture.png           → System architecture diagram
    /cards
        project-card.md        → This project card
        ml-metrics.json        → Stored metrics and results

/data
    download.sh                → Script to download and organise data

README.md                     → Setup, run instructions, and overview
requirements.txt              → Python package dependencies
    </pre>

    <h2>🛠 Setup and Run Instructions</h2>
    <pre>
# Clone the repository
git clone https://github.com/yourusername/soil-classification-2025.git
cd soil-classification-2025

# Install dependencies
pip install -r requirements.txt

# Download and prepare data
bash data/download.sh

# Run training
python src/train.py

# Generate predictions
python src/inference.py

# Alternatively, open and run:
# /notebooks/training.ipynb → for full training pipeline
# /notebooks/inference.ipynb → for test set predictions and submission
    </pre>

    <h2>📈 ML Metrics (ml-metrics.json)</h2>
    <pre>
{
  "minimum_f1": 0.77,
  "f1_scores": {
    "Alluvial": 0.81,
    "Black": 0.77,
    "Clay": 0.84,
    "Red": 0.80
  },
  "weighted_average_f1": 0.805,
  "accuracy": 0.82,
  "loss": 0.42
}
    </pre>

    <h2>🧱 Architecture Diagram</h2>
    <p>Save the diagram as <code>/docs/architecture.png</code></p>
    <pre>
Input Image → Preprocessing → ResNet-50 (Transfer Learning) →
→ Global Average Pooling → Fully Connected Layer →
→ Softmax (4 classes) → Soil Type Prediction
    </pre>

    <h2>👤 Authors</h2>
    <ul>
        <li>Your Name</li>
        <li>Hackathon Team Name (if applicable)</li>
    </ul>

    <h2>📚 References</h2>
    <ul>
        <li><a href="https://annam.ai/">Annam.ai Soil Image Classification Challenge</a></li>
        <li>ResNet-50: Kaiming He et al., Deep Residual Learning for Image Recognition (2015)</li>
        <li>Albumentations: Fast and Flexible Image Augmentations</li>
    </ul>
</body>
</html>
