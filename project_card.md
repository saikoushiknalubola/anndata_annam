# 🌱 Soil Image Classification Challenge — Project Card

## 📘 Summary

This project addresses the **Soil Image Classification Challenge** hosted by Annam.ai at IIT Ropar.

The task is to classify soil images into one of the following four categories:

- **Alluvial soil**
- **Black soil**
- **Clay soil**
- **Red soil**

We built a deep learning pipeline using a **ResNet-50** backbone with cross-validation,  
Albumentations-based data augmentation, and test-time augmentation (TTA),  
targeting the **minimum per-class F1-score** — the official competition metric.

---

## 🚀 Main Contributions

✅ Fine-tuned transfer learning model (ResNet-50)  
✅ Cross-validation ensuring balanced class performance  
✅ Rich data augmentation pipeline (Albumentations)  
✅ Test-time augmentation (TTA) for stronger predictions  
✅ Modular, reproducible, and well-documented codebase  
✅ Complete deliverables including notebooks, scripts, metrics, and documentation

---

## 📊 Final Performance (Validation)

| **Metric**           | **Value** |
|----------------------|-----------|
| Minimum F1-score     | 0.77      |
| Alluvial F1          | 0.81      |
| Black F1             | 0.77      |
| Clay F1             | 0.84      |
| Red F1               | 0.80      |
| Weighted Avg F1      | 0.805     |
| Accuracy             | 0.82      |
| Loss                | 0.42      |

> *Note: These are validation results; leaderboard results may vary.*
