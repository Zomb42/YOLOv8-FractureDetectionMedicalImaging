import os
import shutil

# Define the base path
base_path = "/Users/derickshi/Documents/Yolomedical"

# Directories to restructure
dirs_to_fix = ['train', 'test', 'val']

for dir_name in dirs_to_fix:
    path = os.path.join(base_path, 'data', dir_name, 'images')
    
    # Move fractured and non_fractured directories up one level
    for category in ['fractured', 'non_fractured']:
        src_path = os.path.join(path, category)
        dest_path = os.path.join(base_path, dir_name, category)
        
        # Create destination directory if it does not exist
        os.makedirs(dest_path, exist_ok=True)
        
        # Move files from src to dest
        if os.path.exists(src_path):
            files = os.listdir(src_path)
            for file in files:
                shutil.move(os.path.join(src_path, file), dest_path)
            
            # Remove the now-empty source directory
            os.rmdir(src_path)
    
    # Remove the now-empty 'images' directory
    if os.path.exists(path):
        os.rmdir(path)