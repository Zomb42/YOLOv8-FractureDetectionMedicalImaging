import os
import shutil
import random

# Set paths
base_dir = '/Users/derickshi/Documents/Yolomedical'
image_dir = os.path.join(base_dir, 'FracAtlas', 'images')
fractured_dir = os.path.join(image_dir, 'Fractured')
non_fractured_dir = os.path.join(image_dir, 'Non_fractured')

# Create directories for train and test sets
train_dir = os.path.join(base_dir, 'train', 'images')
test_dir = os.path.join(base_dir, 'test', 'images')
os.makedirs(os.path.join(train_dir, 'fractured'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'non_fractured'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'fractured'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'non_fractured'), exist_ok=True)

# Function to split data
def split_data(source_dir, train_dir, test_dir, split_ratio=0.8):
    files = os.listdir(source_dir)
    random.shuffle(files)
    split_index = int(len(files) * split_ratio)
    train_files = files[:split_index]
    test_files = files[split_index:]

    for file in train_files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(train_dir, os.path.basename(source_dir), file))
    for file in test_files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(test_dir, os.path.basename(source_dir), file))

# Split the data
split_data(fractured_dir, train_dir, test_dir)
split_data(non_fractured_dir, train_dir, test_dir)