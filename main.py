import os
from video_processing.file_loader import load_images_from_folder, load_titles_from_excel
from video_processing.overlay import create_localized_videos

BASE_VIDEO_PATH = "assets/video.mp4"
IMAGES_FOLDER = "assets/images/"
EXCEL_FILE_PATH = "assets/titles.xlsx"
OUTPUT_DIR = "output/"

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Load images and titles
    images = load_images_from_folder(IMAGES_FOLDER)
    titles = load_titles_from_excel(EXCEL_FILE_PATH)
    
    # Create localized videos
    create_localized_videos(BASE_VIDEO_PATH, images, titles, OUTPUT_DIR)

if __name__ == "__main__":
    main()
