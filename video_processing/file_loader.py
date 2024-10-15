import os
import glob
import pandas as pd

def load_images_from_folder(folder_path):
    """Loads image file paths with various extensions from the specified folder."""
    # List of common image extensions to match
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.webp', '*.avif']
    
    # Collect all image files matching the extensions
    images = []
    for ext in image_extensions:
        images.extend(glob.glob(os.path.join(folder_path, ext)))
    
    # Return the sorted list of image file paths
    return sorted(images)

def load_titles_from_excel(excel_file, sheet_name=0, title_column=None):
    """Loads titles from an Excel file and returns them as a list."""
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # If no title column is specified, assume the first column contains titles
    if title_column is None:
        title_column = df.columns[0]  # Automatically take the first column
    
    if title_column not in df.columns:
        raise ValueError(f"Column '{title_column}' not found in Excel file.")

    return df[title_column].tolist()