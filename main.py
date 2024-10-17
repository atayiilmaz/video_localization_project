import os
import argparse
from video_processing.file_loader import load_images_from_folder, load_titles_from_excel, load_music_from_folder
from video_processing.overlay import create_localized_videos

BASE_VIDEO_PATH = "assets/video.mp4"
IMAGES_FOLDER = "assets/images/"
MUSICS_FOLDER = "assets/musics/"
EXCEL_FILE_PATH = "assets/titles.xlsx"
OUTPUT_DIR = "output/"

def main(args):
    # Load images and titles
    images = load_images_from_folder(IMAGES_FOLDER)
    titles = load_titles_from_excel(EXCEL_FILE_PATH)
    musics = load_music_from_folder(MUSICS_FOLDER)
    
    os.makedirs(args.output_dir, exist_ok=True)

    # Create localized videos
    create_localized_videos(BASE_VIDEO_PATH, images, titles, musics, args.font_size, args.output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create localized videos by overlaying images and titles on a base video.")
    parser.add_argument("--output_dir", type=str, default=OUTPUT_DIR, help="Output directory for localized videos.")
    parser.add_argument("--font_size", type=int, default=45, help="Font size for title text.")
    
    args = parser.parse_args()
    main(args)
