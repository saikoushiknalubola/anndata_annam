"""
Author: Annam.ai IIT Ropar
Team Name: anndata
Team Members: N. Saikoushik, M. Sai Teja, G. Navya Sri, N. Chandhana Priya, V. Asmitha
Leaderboard Rank: 22
"""

import os
import pandas as pd
from PIL import Image
import torchvision.transforms as transforms

def preprocessing(data_dir):
    print("Starting preprocessing for Soil Classification...")

    train_csv = os.path.join(data_dir, 'train_labels.csv')
    train_dir = os.path.join(data_dir, 'train')

    if not os.path.exists(train_csv):
        print(f"Error: {train_csv} not found!")
        return 1

    df = pd.read_csv(train_csv)
    print(f"Loaded {len(df)} training labels.")

    # Define image transformations (resize + tensor)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    # Check sample images to verify transformations
    sample_imgs = df['image_id'].head(5)
    for img_name in sample_imgs:
        img_path = os.path.join(train_dir, img_name)
        if not os.path.exists(img_path):
            print(f"Warning: {img_path} missing!")
            continue
        img = Image.open(img_path).convert('RGB')
        img_tensor = transform(img)
        print(f"Processed image: {img_name}, shape: {img_tensor.shape}")

    print("Preprocessing completed successfully.")
    return 0

if __name__ == "__main__":
    data_dir = "/kaggle/input/soil-classification/soil_classification-2025"
    preprocessing(data_dir)

