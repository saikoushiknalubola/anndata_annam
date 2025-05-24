 Soil Image Classification Challenge — Project Card
📌 Summary
This project addresses the Soil Image Classification Challenge hosted by Annam.ai at IIT Ropar.
The task is to develop a machine learning model that classifies soil images into one of four categories:

Alluvial soil

Black soil

Clay soil

Red soil

We used deep learning (ResNet-50 backbone), combined with cross-validation, augmentation, and test-time augmentation (TTA), to build a balanced model optimised for the minimum per-class F1-score — the competition’s official evaluation metric.

🚀 Main Contributions
✅ Fine-tuned transfer learning model with strong generalisation
✅ Cross-validation pipeline ensuring balanced class performance
✅ Extensive data augmentation (Albumentations)
✅ Test-time augmentation to boost final predictions
✅ Structured repository with modular, reproducible code
✅ All competition deliverables: training + inference notebooks, predictions, metrics, project documentation

📊 Final Performance
Metric	Value
Minimum F1-score	0.77
Alluvial F1-score	0.81
Black F1-score	0.77
Clay F1-score	0.84
Red F1-score	0.80
Weighted Average F1	0.805

Note: Final scores are estimated from validation; official leaderboard score may vary slightly.
